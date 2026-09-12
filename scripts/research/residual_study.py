#!/usr/bin/env python3
"""MODEL 5 -- is the MARKET'S RESIDUAL predictable? Not "who wins".

Formulation, chosen so the null hypothesis is the honest one:

    logit p = logit(p_market) + X . beta

The market's own price is an OFFSET, not a feature. beta = 0 reproduces the market exactly, so the only
question the fit can answer is whether any feature adds information the price did not already contain.
Strong L2 regularisation, a strictly chronological split, and the test set is never touched during
fitting or feature selection.

Reported honestly: the number of features tried, the out-of-sample log-loss against the market itself,
and per-feature coefficients so a reader can see whether a "signal" is one variable or a diffuse smear.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tennis_edge.eval.metrics import summary                      # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def logit(p):
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p))


def fit_offset_logistic(X, y, offset, l2=10.0, iters=200):
    """Newton steps on logit p = offset + X.beta with an L2 penalty. Small, transparent, no black box."""
    beta = np.zeros(X.shape[1])
    for _ in range(iters):
        z = offset + X @ beta
        p = 1.0 / (1.0 + np.exp(-z))
        g = X.T @ (y - p) - l2 * beta
        W = p * (1 - p)
        H = -(X.T * W) @ X - l2 * np.eye(X.shape[1])
        try:
            step = np.linalg.solve(H, g)
        except np.linalg.LinAlgError:
            break
        beta -= step
        if np.max(np.abs(step)) < 1e-8:
            break
    return beta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gen2", default=os.path.join(PROJ, "research", "gen2", "predictions_ATP.parquet"))
    ap.add_argument("--benchmark", default=os.path.join(PROJ, "research", "market_benchmark", "linked_ATP.parquet"))
    ap.add_argument("--split-season", type=int, default=2024, help="test set is this season onward, untouched")
    ap.add_argument("--l2", type=float, default=25.0)
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "residual"))
    a = ap.parse_args()

    g2 = pd.read_parquet(a.gen2)
    bm = pd.read_parquet(a.benchmark)[["match_key", "p_winner_PS", "p_loser_PS"]]
    d = g2.merge(bm, on="match_key", how="inner")
    d = d[d.p_winner_PS.notna()].copy()
    s = d.p_winner_PS + d.p_loser_PS
    d["p_market"] = np.where(d.a_is_winner, d.p_winner_PS / s, d.p_loser_PS / s)
    d["ev_min"] = np.minimum(d.ev_a, d.ev_b)

    feats = {
        "disagree_gen2": d.p_gen2_blend - d.p_market,
        "disagree_elo": d.p_elo - d.p_market,
        "abs_disagree_gen2": (d.p_gen2_blend - d.p_market).abs(),
        "fav_centered": (d.p_market - 0.5).abs(),
        "log_evidence": np.log1p(d.ev_min) / 10.0,
        "is_clay": (d.surface == "Clay").astype(float),
        "is_grass": (d.surface == "Grass").astype(float),
        "is_slam": (d.level == "GRAND_SLAM").astype(float),
        "is_masters": (d.level == "MASTERS_1000").astype(float),
        "bo5": (d.best_of == 5).astype(float),
        "model_spread": (d.p_gen2_blend - d.p_elo).abs(),
    }
    X = pd.DataFrame(feats).fillna(0.0)
    y = d.y.values.astype(float)
    off = logit(d.p_market.values)

    tr = (d.season < a.split_season).values
    te = ~tr
    if tr.sum() < 500 or te.sum() < 200:
        print("::warning::not enough data either side of the split"); return 0
    mu, sd = X[tr].mean(), X[tr].std().replace(0, 1)
    Xs = ((X - mu) / sd).values

    beta = fit_offset_logistic(Xs[tr], y[tr], off[tr], l2=a.l2)
    p_market_te = 1 / (1 + np.exp(-off[te]))
    p_model_te = 1 / (1 + np.exp(-(off[te] + Xs[te] @ beta)))

    s_mkt = summary(y[te], p_market_te)
    s_res = summary(y[te], p_model_te)
    rng = np.random.default_rng(20260912)
    dd = ((p_model_te - y[te]) ** 2) - ((p_market_te - y[te]) ** 2)
    idx = rng.integers(0, len(dd), size=(4000, len(dd)))
    means = dd[idx].mean(axis=1)

    res = {"generated_at": datetime.now(timezone.utc).isoformat(), "n_train": int(tr.sum()),
           "n_test": int(te.sum()), "split_season": a.split_season, "l2": a.l2,
           "features_tried": list(X.columns), "n_features": int(X.shape[1]),
           "coefficients": {c: round(float(b), 5) for c, b in zip(X.columns, beta)},
           "market_test": {k: round(float(v), 5) for k, v in s_mkt.items()},
           "residual_model_test": {k: round(float(v), 5) for k, v in s_res.items()},
           "paired_brier_diff": float(dd.mean()),
           "ci": [float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))],
           "p_better_than_market": float((means < 0).mean())}
    os.makedirs(a.out, exist_ok=True)
    json.dump(res, open(os.path.join(a.out, "results_ATP.json"), "w"), indent=1)

    L = ["# Market-residual model (ATP)", "",
         f"Trained on seasons before {a.split_season} ({res['n_train']} matches), tested on "
         f"{a.split_season} onward ({res['n_test']} matches). The market price is an OFFSET, so a "
         f"coefficient vector of zero reproduces the market exactly and the only thing the fit can find "
         f"is information the price did not already contain. {res['n_features']} features were tried; "
         f"that count matters when reading any single coefficient.", "",
         "| forecaster | brier | log loss | ECE | cal slope |", "|---|---|---|---|---|",
         f"| market (de-vigged Pinnacle) | {s_mkt['brier']:.5f} | {s_mkt['log_loss']:.5f} | {s_mkt['ece']:.4f} | {s_mkt['cal_slope']:.3f} |",
         f"| market + residual model | {s_res['brier']:.5f} | {s_res['log_loss']:.5f} | {s_res['ece']:.4f} | {s_res['cal_slope']:.3f} |",
         "", f"Paired Brier difference (model minus market): **{res['paired_brier_diff']:+.5f}**, "
         f"95% CI [{res['ci'][0]:+.5f}, {res['ci'][1]:+.5f}], P(better) {res['p_better_than_market']:.2f}.", "",
         "| feature | coefficient (standardised) |", "|---|---|"]
    for c, b in sorted(res["coefficients"].items(), key=lambda kv: -abs(kv[1])):
        L.append(f"| {c} | {b:+.5f} |")
    open(os.path.join(a.out, "RESULTS_ATP.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
