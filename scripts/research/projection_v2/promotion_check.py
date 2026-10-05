#!/usr/bin/env python3
"""Apply the preregistered promotion rules P1-P8 (research/projection_v2/PREREGISTRATION.md section 5)
mechanically to the validate (2021-2025) and holdout (2026) results. P9 (operational) is checked by the
test suite and the live verification and is recorded separately. Writes PROMOTION_DECISION.json."""
from __future__ import annotations

import argparse, json, os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from tennis_edge.v2.evaluate import cluster_bootstrap_diff  # noqa: E402
from tennis_edge.v2.stacker import level_group  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "research", "projection_v2")
TOURS = ("ATP", "WTA")
SEG_NAMES = {"GS": "Grand Slam", "M": "Masters 1000", "T": "Tour 250/500", "C": "Challenger / WTA 125", "I": "ITF"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=OUT)
    a = ap.parse_args()
    rv = json.load(open(os.path.join(a.dir, "results_validate.json")))
    pv = pd.read_parquet(os.path.join(a.dir, "predictions_validate.parquet"))
    rh_path = os.path.join(a.dir, "results_holdout.json")
    rh = json.load(open(rh_path)) if os.path.exists(rh_path) else None
    rules, detail = {}, {}

    # P1 / P2 / P3 per tour
    p1 = p2 = p3 = True
    for t in TOURS:
        d = rv[t]["vs_incumbent"]["CHALLENGER"]
        inc, ch = rv[t]["lanes"]["INCUMBENT"], rv[t]["lanes"]["CHALLENGER"]
        detail[f"{t}_aggregate"] = {"brier_diff": d["brier_diff"], "brier_ci": d["brier_ci"], "ll_diff": d["ll_diff"],
                                    "ll_ci": d["ll_ci"], "n": d["n"], "clusters": d["clusters"]}
        p1 &= d["brier_ci"][1] < 0 and d["ll_ci"][1] < 0
        p2 &= -d["brier_diff"] >= 0.0005
        slope_ok = (0.90 <= ch["cal_slope"] <= 1.10) or abs(ch["cal_slope"] - 1) < abs(inc["cal_slope"] - 1)
        ece_ok = ch["ece"] <= inc["ece"] + 0.002
        detail[f"{t}_calibration"] = {"challenger_slope": ch["cal_slope"], "incumbent_slope": inc["cal_slope"],
                                      "challenger_ece": ch["ece"], "incumbent_ece": inc["ece"], "slope_ok": slope_ok, "ece_ok": ece_ok}
        p3 &= slope_ok and ece_ok
    rules["P1_aggregate_significant_both_tours"] = p1
    rules["P2_min_improvement_0.0005_both_tours"] = p2
    rules["P3_no_calibration_regression"] = p3

    # P4 seasons
    p4 = True
    for t in TOURS:
        seasons = rv[t]["segments"]["season"]
        better = sum(1 for s in seasons.values() if s["diff"]["brier_diff"] < 0)
        sig_worse = [k for k, s in seasons.items() if s["diff"]["brier_ci"][0] > 0]
        detail[f"{t}_seasons"] = {k: {"n": s["n"], "brier_diff": s["diff"]["brier_diff"], "ci": s["diff"]["brier_ci"]}
                                  for k, s in seasons.items()}
        p4 &= better >= 4 and not sig_worse
    rules["P4_temporal_robustness"] = p4

    # P5 segments (tour x level group, n >= 2000)
    p5 = True
    seg_rows = []
    for t in TOURS:
        for g, s in rv[t]["segments"]["level"].items():
            if g not in SEG_NAMES or s["n"] < 2000:
                continue
            d = s["diff"]
            bad = d["brier_ci"][0] > 0 or d["brier_diff"] > 0.003
            seg_rows.append({"tour": t, "segment": SEG_NAMES[g], "n": s["n"], "brier_diff": d["brier_diff"],
                             "ci": d["brier_ci"], "fails": bad})
            p5 &= not bad
    detail["segments"] = seg_rows
    rules["P5_no_segment_degradation"] = p5

    # P6 remove the single largest-contributing segment and re-test (both tours pooled)
    pv["seg"] = pv["tour"] + ":" + level_group(pv["level"].to_numpy())
    db = (pv["CHALLENGER"] - pv["y"]) ** 2 - (pv["INCUMBENT"] - pv["y"]) ** 2
    contrib = db.groupby(pv["seg"]).sum().sort_values()
    top = contrib.index[0]
    rest = pv[pv["seg"] != top]
    cl = (rest["tour"] + "|" + rest["tourney_id"].astype(str) + "|" + rest["season"].astype(str)).to_numpy()
    d6 = cluster_bootstrap_diff(rest["y"].to_numpy(), rest["CHALLENGER"].to_numpy(), rest["INCUMBENT"].to_numpy(), cl)
    detail["P6"] = {"removed_segment": top, "removed_share_of_gain": float(contrib.iloc[0] / contrib.sum()),
                    "remaining": {k: d6[k] for k in ("n", "brier_diff", "brier_ci", "ll_diff", "ll_ci")}}
    rules["P6_not_driven_by_one_segment"] = d6["brier_ci"][1] < 0

    # P7 2025 alone
    p7 = True
    for t in TOURS:
        s = rv[t]["segments"]["season"].get("2025")
        p7 &= s is not None and s["diff"]["brier_diff"] < 0
    rules["P7_validation_2025_improves_both_tours"] = p7

    # P8 holdout
    if rh is None:
        rules["P8_holdout_2026_not_worse"] = None
    else:
        ok = True
        num = den = 0.0
        for t in TOURS:
            d = rh[t]["vs_incumbent"]["CHALLENGER"]
            detail[f"{t}_holdout"] = {k: d[k] for k in ("n", "brier_diff", "brier_ci", "ll_diff", "ll_ci")}
            ok &= d["brier_ci"][0] <= 0
            num += d["brier_diff"] * d["n"]
            den += d["n"]
        detail["holdout_pooled_brier_diff"] = num / den
        rules["P8_holdout_2026_not_worse"] = ok and num / den <= 0
    decided = [v for v in rules.values() if v is not None]
    verdict = ("PROMOTE_IF_P9_OPERATIONAL_CHECKS_PASS" if all(decided) and rules["P8_holdout_2026_not_worse"] is not None
               else "HOLD_PENDING_HOLDOUT" if all(decided) else "DO_NOT_PROMOTE")
    out = {"rules": rules, "verdict": verdict, "detail": detail, "spec_fingerprint": rv["_meta"]["spec_fingerprint"]}
    json.dump(out, open(os.path.join(a.dir, "PROMOTION_DECISION.json"), "w"), indent=1, default=float)
    print(json.dumps({"rules": rules, "verdict": verdict}, indent=1))


if __name__ == "__main__":
    main()
