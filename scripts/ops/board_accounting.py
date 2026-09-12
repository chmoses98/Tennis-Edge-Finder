#!/usr/bin/env python3
"""Full accounting of the active Kalshi tennis board: exactly one state per contract, no omission.

Reads the latest projection artifact and writes data/research/board_accounting/<run>.json plus a
human-readable REPORT. Two coverage numbers, because they answer different questions: coverage A over
every active contract (honest but includes contracts nothing could price today), and coverage B over the
contracts that SHOULD be priceable with the inputs we actually have.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tennis_edge.kalshi.accounting import BOARD_STATES, board_accounting, check_total   # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--projection", default="")
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "research", "board_accounting"))
    a = ap.parse_args()
    path = a.projection or (sorted(glob.glob(os.path.join(PROJ, "data", "research", "projections", "2*.json")))
                            or [None])[-1]
    if not path:
        print("::warning::no projection artifact to account for")
        return 0
    pj = json.load(open(path))
    acc = board_accounting(pj)
    viol = check_total(acc)
    acc["invariant_violations"] = viol
    acc["projection_run"] = pj.get("run_id")
    acc["generated_at"] = datetime.now(timezone.utc).isoformat()
    os.makedirs(a.out, exist_ok=True)
    run = pj.get("run_id") or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    json.dump(acc, open(os.path.join(a.out, f"{run}.json"), "w"), indent=1, default=str)

    L = [f"# Active-board accounting ({run})", "",
         f"Every one of the {acc['contracts_seen']} contracts on the board carries exactly one state.",
         f"Invariant violations: {viol or 'none'}", "",
         "| coverage | value | denominator | what it measures |", "|---|---|---|---|",
         f"| A, all active | {acc['coverage_a_all_active']} | {acc['active']} | includes contracts nothing could price today |",
         f"| B, should be priceable | {acc['coverage_b_should_be_priceable']} | {acc['coverage_b_denominator']} | excludes contracts blocked by a missing capability, not a missing value |",
         "", "| state | contracts |", "|---|---|"]
    for s in BOARD_STATES:
        if acc["states"].get(s):
            L.append(f"| {s} | {acc['states'][s]} |")
    L += ["", "## Largest blockers, with the reason as recorded", ""]
    for s, n in sorted(acc["states"].items(), key=lambda kv: -kv[1]):
        if s in ("PROJECTED", "CLOSED_SINCE_DISCOVERY") or not n:
            continue
        rs = [r for r in acc["rows"] if r["state"] == s]
        L.append(f"**{s}** ({n})")
        for reason, c in Counter(r["reason"][:110] for r in rs).most_common(3):
            L.append(f"  * {c} x {reason or '(no reason recorded)'}")
        L.append("")
    open(os.path.join(a.out, f"REPORT_{run}.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))
    return 1 if viol else 0


if __name__ == "__main__":
    raise SystemExit(main())
