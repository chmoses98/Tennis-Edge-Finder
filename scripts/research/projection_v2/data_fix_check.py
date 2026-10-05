#!/usr/bin/env python3
"""Judge the canonical_v2 data fix on its own (PREREGISTRATION.md section 5, last paragraph): the INCUMBENT
model replayed on canonical_v1 vs on canonical_v2, scored on the matches common to both tables (a match the
v1 table carried twice is scored once, on the copy v2 kept)."""
from __future__ import annotations

import argparse, json, os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
import pandas as pd  # noqa: E402

from tennis_edge.v2.evaluate import cluster_bootstrap_diff, scores  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "research", "projection_v2")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--v1", default="/home/user/work/v1/replay")
    ap.add_argument("--v2", default="/home/user/work/v2/replay")
    ap.add_argument("--from-season", type=int, default=2021)
    ap.add_argument("--to-season", type=int, default=2025)
    a = ap.parse_args()
    res = {}
    cols = ["uid", "season", "tourney_id", "y", "pf_incumbent", "pf_E_prod"]
    for t in ("ATP", "WTA"):
        r1 = pd.read_parquet(os.path.join(a.v1, f"replay_{t}.parquet"), columns=cols)
        r2 = pd.read_parquet(os.path.join(a.v2, f"replay_{t}.parquet"), columns=cols)
        r1 = r1[(r1.season >= a.from_season) & (r1.season <= a.to_season)].drop_duplicates("uid")
        r2 = r2[(r2.season >= a.from_season) & (r2.season <= a.to_season)].drop_duplicates("uid")
        j = r2.merge(r1[["uid", "pf_incumbent", "pf_E_prod"]], on="uid", suffixes=("_v2", "_v1"))
        cl = (j.tourney_id.astype(str) + "|" + j.season.astype(str)).to_numpy()
        res[t] = {"v1_rows": int(len(r1)), "v2_rows": int(len(r2)), "common_rows": int(len(j)),
                  "v1_rows_not_in_v2_(removed_duplicates)": int(len(r1) - r1.uid.isin(r2.uid).sum()),
                  "incumbent_v1data": scores(j.y, j.pf_incumbent_v1), "incumbent_v2data": scores(j.y, j.pf_incumbent_v2),
                  "v2_minus_v1": cluster_bootstrap_diff(j.y.to_numpy(), j.pf_incumbent_v2.to_numpy(), j.pf_incumbent_v1.to_numpy(), cl)}
        d = res[t]["v2_minus_v1"]
        print(t, "common", len(j), f"dBrier {d['brier_diff']:+.5f} {d['brier_ci']}  dLL {d['ll_diff']:+.5f}")
    ok = all(res[t]["v2_minus_v1"]["brier_ci"][0] <= 0 for t in res)
    res["decision"] = "DEPLOY_DATA_FIX" if ok else "DO_NOT_DEPLOY_DATA_FIX"
    res["seasons"] = [a.from_season, a.to_season]
    json.dump(res, open(os.path.join(OUT, "DATA_FIX_DECISION.json"), "w"), indent=1, default=float)
    print(res["decision"])


if __name__ == "__main__":
    main()
