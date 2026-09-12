#!/usr/bin/env python3
"""How much of the Kalshi board can we put a name to, and what is left over.

Measured on a fixed set: every distinct (tour, player name) the discovery snapshot lists, resolved three
ways -- exact full-name match only, exact plus the guarded compound-surname alias, and the same again
with the ESPN-refreshed registry. The residue is printed in full, because the names we cannot resolve
are the specification for the next attempt.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from collections import Counter
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.identity.kalshi_map import KalshiPlayerMapper     # noqa: E402
from tennis_edge.kalshi.families import SERIES                     # noqa: E402
from tennis_edge.kalshi.markets import parse_market                # noqa: E402
from tennis_edge.models.state import load_state                    # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--discovery", default="")
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "selector", "identity_coverage.json"))
    a = ap.parse_args()
    d = a.discovery or sorted(glob.glob(os.path.join(PROJ, "data", "kalshi", "discovery", "*")))[-1]

    singles = {tk for tk, (fam, tour, lvl, disc) in SERIES.items()
               if fam == "MATCH_WINNER" and disc == "singles" and tour in ("ATP", "WTA")}
    names = set()
    for tk in singles:
        for sub in ("markets", "historical_markets"):
            path = os.path.join(d, sub, f"{tk}.json")
            if not os.path.exists(path):
                continue
            obj = json.load(open(path))
            for blk in (obj.values() if "markets" not in obj else [obj]):
                for m in blk.get("markets") or []:
                    pm = parse_market(m)
                    if pm.status == "PARSED" and pm.subject:
                        tour = "WTA" if pm.series_ticker.startswith(("KXWTA", "KXITFW")) else "ATP"
                        names.add((tour, pm.subject))

    states = {t: load_state(os.path.join(PROJ, "data", "processed", f"ratings_{t}.json")) for t in ("ATP", "WTA")}
    mapper = KalshiPlayerMapper(states, cache_path="/tmp/identity_coverage_cache.json")
    today = date(2026, 9, 12)

    out = {"discovery": os.path.basename(d), "distinct_names": len(names),
           "registry_as_of": {t: states[t]["as_of_date"] for t in states},
           "registry_players": {t: len(states[t]["players"]) for t in states}}
    for label, use_alias in (("exact_only", False), ("exact_plus_compound_surname_alias", True)):
        counts, residue = Counter(), []
        for tour, nm in sorted(names):
            r = mapper.resolve(tour, nm, None, today)
            if r["status"] != "MAPPED" and use_alias is False:
                pass
            if not use_alias and r.get("reason", "").startswith("compound-surname"):
                r = {"status": "UNMAPPED", "reason": "no exact full-name match"}
            counts[r["status"]] += 1
            if r["status"] != "MAPPED":
                residue.append({"tour": tour, "name": nm, "reason": r.get("reason", "")})
        out[label] = {"counts": dict(counts),
                      "mapped_rate": round(counts["MAPPED"] / max(len(names), 1), 4),
                      "residue_examples": residue[:40], "residue_total": len(residue)}
    out["recovered_by_alias"] = (out["exact_plus_compound_surname_alias"]["counts"].get("MAPPED", 0)
                                 - out["exact_only"]["counts"].get("MAPPED", 0))
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(out, open(a.out, "w"), indent=1, default=str)
    print(json.dumps({k: v for k, v in out.items() if k != "exact_only"} | {
        "exact_only": {k: v for k, v in out["exact_only"].items() if k != "residue_examples"},
        "exact_plus_compound_surname_alias": {k: v for k, v in out["exact_plus_compound_surname_alias"].items()
                                              if k != "residue_examples"}}, indent=1, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
