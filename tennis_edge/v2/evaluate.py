"""Proper scores with paired, cluster-aware uncertainty.

Matches inside one tournament share players, conditions and draw structure, so treating 30,000 matches as
30,000 independent observations overstates certainty. Every interval here resamples TOURNAMENT INSTANCES
(the cluster key), with Poisson(1) weights -- the standard large-sample bootstrap that needs no
multinomial draw over clusters and is exact in expectation.
"""
from __future__ import annotations

import numpy as np

from tennis_edge.eval.metrics import calibration_slope_intercept, ece

EPS = 1e-6


def brier_vec(y, p):
    return (np.asarray(p, float) - np.asarray(y, float)) ** 2


def ll_vec(y, p):
    p = np.clip(np.asarray(p, float), EPS, 1 - EPS)
    y = np.asarray(y, float)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def scores(y, p) -> dict:
    y = np.asarray(y, float)
    p = np.asarray(p, float)
    if len(y) == 0:
        return {"n": 0}
    slope, icpt = calibration_slope_intercept(y, p)
    return {"n": int(len(y)), "brier": float(brier_vec(y, p).mean()), "log_loss": float(ll_vec(y, p).mean()),
            "accuracy": float(np.mean((p > 0.5) == (y == 1))), "ece": ece(y, p), "cal_slope": slope,
            "cal_intercept": icpt}


def favourite_scores(y, p) -> dict:
    """Calibration from the favourite's side: intercept != 0 here is a favourite-longshot bias, which the
    symmetric orientation hides by construction."""
    y = np.asarray(y, float)
    p = np.asarray(p, float)
    fav = p >= 0.5
    pf = np.where(fav, p, 1 - p)
    yf = np.where(fav, y, 1 - y)
    s = scores(yf, pf)
    return {"fav_" + k: v for k, v in s.items() if k in ("ece", "cal_slope", "cal_intercept")}


def cluster_bootstrap_diff(y, p_cand, p_base, clusters, n_boot: int = 2000, seed: int = 0) -> dict:
    """Paired candidate - baseline differences in Brier and log loss with a cluster bootstrap CI.
    Negative = candidate better."""
    y = np.asarray(y, float)
    db = brier_vec(y, p_cand) - brier_vec(y, p_base)
    dl = ll_vec(y, p_cand) - ll_vec(y, p_base)
    _, inv = np.unique(np.asarray(clusters).astype(str), return_inverse=True)
    k = inv.max() + 1
    nb = np.bincount(inv, minlength=k).astype(float)
    sb = np.bincount(inv, weights=db, minlength=k)
    sl = np.bincount(inv, weights=dl, minlength=k)
    rng = np.random.default_rng(seed)
    out_b = np.empty(n_boot)
    out_l = np.empty(n_boot)
    chunk = 200
    for s in range(0, n_boot, chunk):
        e = min(n_boot, s + chunk)
        w = rng.poisson(1.0, size=(e - s, k)).astype(float)
        den = w @ nb
        out_b[s:e] = (w @ sb) / den
        out_l[s:e] = (w @ sl) / den
    return {"n": int(len(y)), "clusters": int(k),
            "brier_diff": float(db.mean()), "brier_ci": [float(np.percentile(out_b, 2.5)), float(np.percentile(out_b, 97.5))],
            "ll_diff": float(dl.mean()), "ll_ci": [float(np.percentile(out_l, 2.5)), float(np.percentile(out_l, 97.5))],
            "p_better_brier": float(np.mean(out_b < 0))}


def reliability(y, p, edges=(0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0)) -> list:
    y = np.asarray(y, float)
    p = np.asarray(p, float)
    fav = p >= 0.5
    pf = np.where(fav, p, 1 - p)
    yf = np.where(fav, y, 1 - y)
    rows = []
    for lo, hi in zip((0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95), (0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0001)):
        m = (pf >= lo) & (pf < hi)
        if m.sum():
            rows.append({"bucket": f"{lo:.2f}-{min(hi, 1):.2f}", "n": int(m.sum()), "mean_p": float(pf[m].mean()),
                         "win_rate": float(yf[m].mean()), "gap": float(yf[m].mean() - pf[m].mean())})
    return rows
