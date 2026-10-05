#!/usr/bin/env python3
"""Market benchmark AFTER the V2 freeze (PREREGISTRATION.md section 1: the market is an external yardstick
only; nothing computed here can change the challenger -- that would start a new research cycle).

Pinnacle (vig-free, tennis-data.co.uk, ATP main tour) on the matches the original benchmark already linked
(research/market_benchmark/linked_ATP.parquet, fail-closed identity), joined to the FROZEN V2 / incumbent
walk-forward predictions (predictions_validate.parquet 2021-2025, predictions_holdout.parquet 2026).

Reports: Brier / log loss / calibration of incumbent, V2 and Pinnacle on identical matches; paired V2 - Pinnacle
with the cluster bootstrap; disagreement buckets (how often the V2 side wins vs what the market implied); and
the information question -- does V2 carry information the market lacks? -- as a walk-forward logistic regression
y ~ a * logit(market) + b * logit(V2), fitted on earlier seasons and scored on the next (a diagnostic: b > 0
with a better out-of-sample score would mean V2 adds information; it is NOT a deployable blend).
"""
from __future__ import annotations

import json, os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from tennis_edge.v2.evaluate import cluster_bootstrap_diff, favourite_scores, scores  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "research", "projection_v2")
PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def logit(p):
    p = np.clip(np.asarray(p, float), 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


def main():
    link = pd.read_parquet(os.path.join(PROJ, "research", "market_benchmark", "linked_ATP.parquet"),
                           columns=["match_key", "season", "mkt_PS"]).dropna()
    link = link.drop_duplicates(["match_key", "season"], keep=False)          # fail closed on any key collision
    preds = pd.concat([pd.read_parquet(os.path.join(OUT, f"predictions_{s}.parquet")) for s in ("validate", "holdout")])
    preds = preds[(preds.tour == "ATP") & preds.uid.str.startswith("sackmann_ATP")]
    preds["match_key"] = preds.uid.str.split("|").str[1]
    df = preds.merge(link, on=["match_key", "season"])
    # mkt_PS is the WINNER's probability; orient it to player A (y = 1 means A won)
    df["MARKET_PINNACLE"] = np.where(df.y == 1, df.mkt_PS, 1 - df.mkt_PS)
    y = df.y.to_numpy()
    cl = (df.tourney_id.astype(str) + "|" + df.season.astype(str)).to_numpy()
    out = {"n_linked": int(len(df)), "seasons": sorted(int(s) for s in df.season.unique()), "scores": {}}
    for k in ("INCUMBENT", "CHALLENGER", "MARKET_PINNACLE"):
        out["scores"][k] = {**scores(y, df[k]), **favourite_scores(y, df[k])}
    out["v2_minus_pinnacle"] = cluster_bootstrap_diff(y, df.CHALLENGER.to_numpy(), df.MARKET_PINNACLE.to_numpy(), cl)
    out["incumbent_minus_pinnacle"] = cluster_bootstrap_diff(y, df.INCUMBENT.to_numpy(), df.MARKET_PINNACLE.to_numpy(), cl)
    out["v2_minus_incumbent_on_linked"] = cluster_bootstrap_diff(y, df.CHALLENGER.to_numpy(), df.INCUMBENT.to_numpy(), cl)
    out["by_season"] = {}
    for s, g in df.groupby("season"):
        out["by_season"][int(s)] = {k: scores(g.y, g[k])["brier"] for k in ("INCUMBENT", "CHALLENGER", "MARKET_PINNACLE")} | {"n": int(len(g))}
    # disagreement buckets: does the side V2 prefers over the market win as often as V2 says, or as the market says?
    gap = df.CHALLENGER - df.MARKET_PINNACLE
    side_a = gap > 0
    p_model_side = np.where(side_a, df.CHALLENGER, 1 - df.CHALLENGER)
    p_mkt_side = np.where(side_a, df.MARKET_PINNACLE, 1 - df.MARKET_PINNACLE)
    won = np.where(side_a, df.y, 1 - df.y)
    buckets = {}
    for lo, hi in ((0, .05), (.05, .10), (.10, .15), (.15, .20), (.20, 1.0)):
        m = (gap.abs() >= lo) & (gap.abs() < hi)
        if m.sum():
            buckets[f"{int(lo * 100)}-{int(hi * 100)}pp"] = {"n": int(m.sum()), "v2_side_implied_by_v2": float(p_model_side[m].mean()),
                                                           "v2_side_implied_by_market": float(p_mkt_side[m].mean()),
                                                           "v2_side_actual_win_rate": float(won[m].mean())}
    out["disagreement_buckets"] = buckets
    # information beyond the market: walk-forward logistic regression on the two logits
    from sklearn.linear_model import LogisticRegression
    info = {}
    for s in sorted(df.season.unique()):
        tr, te = df[df.season < s], df[df.season == s]
        if len(tr) < 1500 or not len(te):
            continue
        X = np.column_stack([logit(tr.MARKET_PINNACLE), logit(tr.CHALLENGER)])
        lr = LogisticRegression(C=1e6, fit_intercept=False).fit(X, tr.y)
        p = lr.predict_proba(np.column_stack([logit(te.MARKET_PINNACLE), logit(te.CHALLENGER)]))[:, 1]
        info[int(s)] = {"weight_market": float(lr.coef_[0][0]), "weight_v2": float(lr.coef_[0][1]),
                        "brier_combined": scores(te.y, p)["brier"], "brier_market": scores(te.y, te.MARKET_PINNACLE)["brier"], "n": int(len(te))}
    out["information_beyond_market"] = info
    out["note"] = ("Computed after the V2 freeze. A combined score better than the market's would only motivate a new, "
                   "separately preregistered research cycle; no market-informed blend is part of the independent model.")
    json.dump(out, open(os.path.join(OUT, "market_benchmark_v2.json"), "w"), indent=1, default=float)
    print(json.dumps({k: out[k] for k in ("n_linked", "v2_minus_pinnacle", "incumbent_minus_pinnacle", "v2_minus_incumbent_on_linked")}, indent=1, default=float))
    print(json.dumps(out["scores"], indent=1, default=float)[:1500])
    print(json.dumps(buckets, indent=1))
    print(json.dumps(info, indent=1))


if __name__ == "__main__":
    main()
