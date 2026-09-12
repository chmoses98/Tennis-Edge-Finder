#!/usr/bin/env python3
"""Do related Kalshi tennis markets lead one another?

Before estimating a lag, this measures whether the data can support the estimate at all: how many
physical matches have TWO OR MORE families quoted at the same time, across enough passes for a lag to be
visible. Reporting a lag from a handful of series would be worse than reporting nothing.

Where the data does support it, the estimator is deliberately plain: for each pair of families on one
match, the cross-correlation of first differences in the executable midpoint at lags of one, two and
three capture passes. A lead shows up as the peak correlation sitting at a non-zero lag.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from scripts.research.coherence_scan import _f, latest_discovery, parsed_universe, passes  # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture", default=os.path.join(PROJ, "data", "kalshi", "capture"))
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "lead_lag"))
    ap.add_argument("--min-passes", type=int, default=6, help="series shorter than this cannot show a lag")
    a = ap.parse_args()

    disc = latest_discovery()
    universe = parsed_universe(disc) if disc else {}
    P = passes(a.capture)
    order = list(P)
    series: dict = defaultdict(dict)          # (match, family, ticker) -> {pass_index: mid}
    for i, run in enumerate(order):
        for tk, q in P[run].items():
            pm = universe.get(tk)
            if pm is None:
                continue
            yb, ya = _f(q.get("yes_bid_dollars")), _f(q.get("yes_ask_dollars"))
            if yb is None or ya is None:
                continue
            sfx = pm.event_ticker.split("-", 1)[1] if "-" in pm.event_ticker else pm.event_ticker
            series[(sfx, pm.family, tk)][i] = 0.5 * (yb + ya)

    by_match = defaultdict(set)
    for (sfx, fam, tk) in series:
        by_match[sfx].add(fam)
    long_enough = {k: v for k, v in series.items() if len(v) >= a.min_passes}
    matches_multi = {m for m, fams in by_match.items() if len(fams) >= 2}
    usable_pairs = []
    for m in matches_multi:
        fams = defaultdict(list)
        for (sfx, fam, tk), pts in long_enough.items():
            if sfx == m:
                fams[fam].append((tk, pts))
        keys = sorted(fams)
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                usable_pairs.append((m, keys[i], keys[j]))

    results = []
    for m, f1, f2 in usable_pairs:
        s1 = [pts for (sfx, fam, tk), pts in long_enough.items() if sfx == m and fam == f1][0]
        s2 = [pts for (sfx, fam, tk), pts in long_enough.items() if sfx == m and fam == f2][0]
        common = sorted(set(s1) & set(s2))
        if len(common) < a.min_passes:
            continue
        x = np.diff([s1[i] for i in common])
        z = np.diff([s2[i] for i in common])
        if x.std() == 0 or z.std() == 0:
            continue
        row = {"match": m, "family_a": f1, "family_b": f2, "n_points": len(common)}
        for lag in (0, 1, 2, 3):
            if lag >= len(x):
                continue
            xa, zb = (x[:-lag], z[lag:]) if lag else (x, z)
            if len(xa) < 3 or xa.std() == 0 or zb.std() == 0:
                continue
            row[f"corr_lag_{lag}"] = float(np.corrcoef(xa, zb)[0, 1])
        results.append(row)

    out = {"generated_at": datetime.now(timezone.utc).isoformat(),
           "capture_passes": len(order),
           "quoted_series": len(series),
           "series_with_at_least_%d_passes" % a.min_passes: len(long_enough),
           "matches_quoted": len(by_match),
           "matches_with_two_or_more_families": len(matches_multi),
           "family_pairs_examined": len(usable_pairs),
           "pairs_with_enough_overlap": len(results),
           "pairs": results[:100]}
    os.makedirs(a.out, exist_ok=True)
    json.dump(out, open(os.path.join(a.out, "results.json"), "w"), indent=1)

    L = ["# Lead-lag between related Kalshi tennis markets", "",
         "**Can this even be measured on the data we have?** That question comes first.", "",
         "| measure | value |", "|---|---|",
         f"| capture passes available | {out['capture_passes']} |",
         f"| distinct quoted contract series | {out['quoted_series']} |",
         f"| series quoted in at least {a.min_passes} passes | {out['series_with_at_least_%d_passes' % a.min_passes]} |",
         f"| physical matches quoted | {out['matches_quoted']} |",
         f"| matches with two or more FAMILIES quoted | {out['matches_with_two_or_more_families']} |",
         f"| family pairs examined | {out['family_pairs_examined']} |",
         f"| pairs with enough overlapping observations | {out['pairs_with_enough_overlap']} |", ""]
    if len(results) < 20:
        L += ["## Verdict: not measurable yet", "",
              "A lead-lag estimate needs many matches carrying at least two related families quoted "
              "simultaneously over a long enough window. On this archive that population is "
              f"{out['pairs_with_enough_overlap']} pairs, which is far too few to distinguish a lead from "
              "noise. This is a POWER problem, not a null result: the honest statement is that the "
              "question remains open, and it will stay open until Kalshi lists more derivative contracts "
              "or the capture archive covers many more days.", "",
              "The cause is the same structural fact the coherence scan found: almost every tennis match "
              "on this exchange has exactly two open contracts, the two sides of the match winner. There "
              "is no derivative to lag behind anything."]
    else:
        L += ["## Cross-correlation of first differences", "",
              "| match | family A | family B | n | lag 0 | lag 1 | lag 2 | lag 3 |", "|---|---|---|---|---|---|---|---|"]
        for r in results[:40]:
            L.append(f"| {r['match']} | {r['family_a']} | {r['family_b']} | {r['n_points']} | " +
                     " | ".join(f"{r.get(f'corr_lag_{k}', float('nan')):+.3f}" for k in (0, 1, 2, 3)) + " |")
    open(os.path.join(a.out, "RESULTS.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
