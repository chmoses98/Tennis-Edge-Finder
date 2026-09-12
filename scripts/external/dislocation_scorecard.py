#!/usr/bin/env python3
"""What happened after we flagged a dislocation.

Two questions, in order of how quickly they can be answered:

1. **Did Kalshi move toward the external reference?** Answerable within hours, from the ledger itself,
   because the scan re-observes every ticker every pass. If an independent venue's disagreement carries
   information, the Kalshi price should drift toward it before the match starts. If it does not, the
   disagreement is noise or the two venues simply price differently.
2. **Who was right?** Answerable only at settlement, and reported separately when outcomes exist.

Both are MONITORING. This script does not tune anything, and the confirmation period is not a period
during which rules may be changed.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import statistics as st
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJ)


def _iso(x):
    try:
        return datetime.fromisoformat(str(x).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def boot_ci(x, n_boot=4000, seed=20260915):
    import numpy as np
    x = np.asarray([v for v in x if v is not None], float)
    if len(x) < 3:
        return [None, None]
    rng = np.random.default_rng(seed)
    m = x[rng.integers(0, len(x), size=(n_boot, len(x)))].mean(axis=1)
    return [round(float(np.percentile(m, 2.5)), 5), round(float(np.percentile(m, 97.5)), 5)]


def load(root):
    rows = []
    for f in sorted(glob.glob(os.path.join(root, "*.jsonl"))):
        for line in open(f):
            if line.strip():
                rows.append(json.loads(line))
    return rows


def follow_ups(rows, min_gap_min=20.0):
    """For each observation, the SAME ticker's Kalshi mid at least `min_gap_min` later."""
    by_ticker = defaultdict(list)
    for r in rows:
        t = _iso(r.get("generated_at"))
        if t and r.get("kalshi_mid") is not None:
            by_ticker[r["kalshi_ticker"]].append((t, r))
    for v in by_ticker.values():
        v.sort(key=lambda x: x[0])
    out = []
    for tk, seq in by_ticker.items():
        for i, (t, r) in enumerate(seq):
            if r.get("external_fair") is None:
                continue
            later = next(((t2, r2) for t2, r2 in seq[i + 1:]
                          if (t2 - t) >= timedelta(minutes=min_gap_min)), None)
            if not later:
                continue
            t2, r2 = later
            gap = (t2 - t).total_seconds() / 60.0
            move = r2["kalshi_mid"] - r["kalshi_mid"]
            gapsign = 1.0 if r["external_fair"] > r["kalshi_mid"] else -1.0
            out.append({**r, "follow_up_minutes": gap, "kalshi_move": move,
                        "move_toward_external": gapsign * move,
                        "kalshi_mid_later": r2["kalshi_mid"],
                        "closed_gap_fraction": (gapsign * move) / max(abs(r["external_fair"] - r["kalshi_mid"]), 1e-9)})
    return out


def describe(rows, label):
    if not rows:
        return {"subset": label, "n": 0}
    d = [r["external_vs_kalshi"] for r in rows if r.get("external_vs_kalshi") is not None]
    e = [r["external_edge"] for r in rows if r.get("external_edge") is not None]
    out = {"subset": label, "n": len(rows)}
    if d:
        out.update({"ext_vs_kalshi_median": round(st.median(d), 5),
                    "ext_vs_kalshi_mean": round(st.mean(d), 5),
                    "ext_vs_kalshi_p90_abs": round(sorted(abs(x) for x in d)[int(0.9 * (len(d) - 1))], 5),
                    "share_over_2c": round(sum(1 for x in d if abs(x) > 0.02) / len(d), 4),
                    "share_over_5c": round(sum(1 for x in d if abs(x) > 0.05) / len(d), 4)})
    if e:
        out.update({"external_edge_median": round(st.median(e), 5),
                    "external_edge_max": round(max(e), 5),
                    "share_edge_over_2c": round(sum(1 for x in e if x >= 0.02) / len(e), 4)})
    mv = [r["move_toward_external"] for r in rows if r.get("move_toward_external") is not None]
    if mv:
        out.update({"n_with_follow_up": len(mv), "move_toward_external_mean": round(st.mean(mv), 5),
                    "move_toward_external_ci": boot_ci(mv),
                    "share_moved_toward": round(sum(1 for x in mv if x > 0) / len(mv), 4),
                    "median_follow_up_minutes": round(st.median(
                        [r["follow_up_minutes"] for r in rows if r.get("follow_up_minutes")]), 1)})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default=os.path.join(PROJ, "data", "research", "external", "dislocations"))
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "external_market"))
    ap.add_argument("--min-gap-min", type=float, default=20.0)
    a = ap.parse_args()
    rows = load(a.ledger)
    if not rows:
        print("::warning::no dislocation rows on disk")
        return 0
    fu = follow_ups(rows, a.min_gap_min)
    fu_by_key = {(r["kalshi_ticker"], r["generated_at"]): r for r in fu}
    merged = [fu_by_key.get((r["kalshi_ticker"], r["generated_at"]), r) for r in rows]
    withref = [r for r in merged if r.get("external_fair") is not None]

    res = {"generated_at": datetime.now(timezone.utc).isoformat(),
           "rows": len(rows), "rows_with_reference": len(withref),
           "distinct_tickers": len({r["kalshi_ticker"] for r in rows}),
           "distinct_matches": len({r["physical_match_id"] for r in rows}),
           "window": [min(r["generated_at"] for r in rows), max(r["generated_at"] for r in rows)],
           "decisions": {k: sum(1 for r in rows if r["decision"] == k)
                         for k in ("PASS", "WATCH", "SHADOW_BET")},
           "triangulation": {}, "overall": describe(withref, "all rows with a reference"),
           "by_triangulation": [], "scorecards": {}}
    for cls in sorted({r["triangulation"] for r in merged}):
        sub = [r for r in merged if r["triangulation"] == cls]
        res["triangulation"][cls] = len(sub)
        res["by_triangulation"].append(describe([r for r in sub if r.get("external_fair") is not None], cls))

    # monitoring scorecards. Reported, never acted on during the confirmation period.
    for name, keyfn in (("by_day", lambda r: r["generated_at"][:10]),
                        ("by_week", lambda r: _iso(r["generated_at"]).strftime("%G-W%V")),
                        ("by_tour", lambda r: r["physical_match_id"].split(":")[0]),
                        ("by_family", lambda r: r["market_family"])):
        buckets = defaultdict(list)
        for r in withref:
            buckets[keyfn(r)].append(r)
        res["scorecards"][name] = [describe(v, k) for k, v in sorted(buckets.items())]

    os.makedirs(a.out, exist_ok=True)
    json.dump(res, open(os.path.join(a.out, "scorecard.json"), "w"), indent=1, default=str)

    L = ["# External dislocation scorecard", "",
         f"{res['rows']} observations over {res['distinct_matches']} matches "
         f"({res['distinct_tickers']} contracts), {res['window'][0][:16]}Z to {res['window'][1][:16]}Z. "
         f"**Monitoring only.** Nothing here authorises a rule change.", "",
         f"Decisions: " + ", ".join(f"{k} {v}" for k, v in res["decisions"].items()), "",
         "## How far apart are the two venues", "",
         "| subset | n | median ext-Kalshi | mean | share >2c | share >5c | median edge after fees | share edge >=2c |",
         "|---|---|---|---|---|---|---|---|"]
    for s in [res["overall"]] + res["by_triangulation"]:
        if not s.get("n"):
            continue
        L.append(f"| {s['subset']} | {s['n']} | {s.get('ext_vs_kalshi_median', float('nan')):+.4f} | "
                 f"{s.get('ext_vs_kalshi_mean', float('nan')):+.4f} | {s.get('share_over_2c', 0):.3f} | "
                 f"{s.get('share_over_5c', 0):.3f} | {s.get('external_edge_median', float('nan')):+.4f} | "
                 f"{s.get('share_edge_over_2c', 0):.3f} |")
    L += ["", "## Did Kalshi move toward the external reference", "",
          "| subset | n | mean move toward | 95% CI | share moved toward | median gap (min) |",
          "|---|---|---|---|---|---|"]
    for s in [res["overall"]] + res["by_triangulation"]:
        if not s.get("n_with_follow_up"):
            continue
        L.append(f"| {s['subset']} | {s['n_with_follow_up']} | {s['move_toward_external_mean']:+.5f} | "
                 f"[{s['move_toward_external_ci'][0]}, {s['move_toward_external_ci'][1]}] | "
                 f"{s['share_moved_toward']:.3f} | {s['median_follow_up_minutes']:.0f} |")
    open(os.path.join(a.out, "SCORECARD.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
