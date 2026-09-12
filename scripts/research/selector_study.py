#!/usr/bin/env python3
"""Wave 3 core study: can we tell a trustworthy disagreement from a worthless one?

Chronology is the spine of this script. The eighteen days of settled Kalshi markets are cut into three
consecutive blocks and they are used for exactly one thing each:

    DISCOVERY    fit the selector. Nothing else.
    VALIDATION   choose the regularisation and the decision thresholds. Never re-fit.
    HOLDOUT      read ONCE, at the end, and report whatever it says.

The target is proper-score superiority -- "was our number closer to the truth than the price was" --
not "who won". We are globally worse than the market at picking winners and re-learning that is not the
job. The economics (after-fee return at the executable ask) are the JUDGE, never the trainer: a selector
fitted on realised profit at n = 2,000 would be fitting noise with a dollar sign on it.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.eval.metrics import summary                          # noqa: E402
from tennis_edge.selector.features import FEATURES, build_features, edges, FEATURE_VERSION  # noqa: E402
from tennis_edge.selector.model import Selector                        # noqa: E402

SELECTOR_VERSION = "selector_v1"


def econ(d: pd.DataFrame) -> dict:
    """Hypothetical economics of buying every row at its ask, ONE contract, taker fee, no slippage."""
    if not len(d):
        return {"n": 0}
    cost = d.kalshi_ask + d.fee
    pnl = d.y - cost
    return {"n": int(len(d)), "hit_rate": float(d.y.mean()), "avg_ask": float(d.kalshi_ask.mean()),
            "avg_fee": float(d.fee.mean()), "total_pnl": float(pnl.sum()), "capital": float(cost.sum()),
            "roi": float(pnl.sum() / cost.sum()) if cost.sum() else None,
            "mean_pnl_per_contract": float(pnl.mean()),
            "worst_drawdown": float((pnl.cumsum() - pnl.cumsum().cummax()).min())}


def scored(d: pd.DataFrame, col: str) -> dict:
    y = d.y.to_numpy(float)
    s = summary(y, d[col].to_numpy(float))
    return {k: float(v) for k, v in s.items()}


def block_report(d: pd.DataFrame, label: str) -> dict:
    out = {"label": label, "n_rows": int(len(d)), "n_matches": int(d.event.nunique())}
    if len(d):
        out["model"] = scored(d, "p_fair")
        out["market"] = scored(d, "kalshi_mid")
        out["econ_all"] = econ(d)
    return out


def bootstrap_mean(x, n_boot=4000, seed=20260913):
    x = np.asarray(x, float)
    if len(x) < 2:
        return (None, None)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(x), size=(n_boot, len(x)))
    m = x[idx].mean(axis=1)
    return float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=os.path.join(PROJ, "research", "selector", "opportunities.parquet"))
    ap.add_argument("--discovery-end", default="2026-09-02")
    ap.add_argument("--validation-end", default="2026-09-06")
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "selector"))
    a = ap.parse_args()

    d = pd.read_parquet(a.data)
    e = edges(d)
    for c in e.columns:
        d[c] = e[c]
    # TARGET: was our probability closer to the truth than the price? Identical for both sides of a
    # match by construction, which is correct -- it is a property of the disagreement, not of the side.
    d["informative"] = ((d.p_fair - d.y) ** 2 < (d.kalshi_mid - d.y) ** 2).astype(float)
    d["pnl"] = d.y - d.kalshi_ask - d.fee

    disc = d[d.sched_date <= a.discovery_end]
    val = d[(d.sched_date > a.discovery_end) & (d.sched_date <= a.validation_end)]
    hold = d[d.sched_date > a.validation_end]
    X = build_features(d)
    Xd, Xv, Xh = X.loc[disc.index], X.loc[val.index], X.loc[hold.index]

    res = {"generated_at": datetime.now(timezone.utc).isoformat(), "feature_version": FEATURE_VERSION,
           "selector_version": SELECTOR_VERSION, "n_features": len(FEATURES),
           "splits": {"discovery": block_report(disc, "discovery"),
                      "validation": block_report(val, "validation"),
                      "holdout": block_report(hold, "holdout")}}

    # ---------------------------------------------------------------- fit + choose l2 on VALIDATION
    grid = []
    for l2 in (3.0, 10.0, 30.0, 100.0, 300.0):
        s = Selector(version=f"{SELECTOR_VERSION}_l2{l2:g}", feature_names=tuple(FEATURES),
                     target="proper_score_superiority", trained_from=str(disc.sched_date.min()),
                     trained_through=a.discovery_end, l2=l2)
        s.fit(Xd, disc.informative.to_numpy(float), disc.sched_date)
        pv = s.score(Xv)
        ll = float(-np.mean(val.informative * np.log(np.clip(pv, 1e-9, 1)) +
                            (1 - val.informative) * np.log(np.clip(1 - pv, 1e-9, 1))))
        grid.append({"l2": l2, "validation_log_loss": ll,
                     "validation_brier": float(np.mean((pv - val.informative) ** 2))})
    best = min(grid, key=lambda g: g["validation_log_loss"])
    res["l2_grid"] = grid
    res["l2_chosen"] = best["l2"]

    sel = Selector(version=SELECTOR_VERSION, feature_names=tuple(FEATURES),
                   target="proper_score_superiority", trained_from=str(disc.sched_date.min()),
                   trained_through=a.discovery_end, l2=best["l2"],
                   notes="P(our probability beats the price on this match). Fitted on discovery only; "
                         "L2 chosen on validation; holdout read once.")
    sel.fit(Xd, disc.informative.to_numpy(float), disc.sched_date).freeze()
    res["selector"] = sel.to_dict()
    res["coefficients"] = dict(sorted(sel.coefficients().items(), key=lambda kv: -abs(kv[1])))

    for name, blk, Xb in (("discovery", disc, Xd), ("validation", val, Xv), ("holdout", hold, Xh)):
        d.loc[blk.index, "selector_score"] = sel.score(Xb)
    res["base_rate_informative"] = {k: float(v.informative.mean()) for k, v in
                                    (("discovery", disc), ("validation", val), ("holdout", hold))}

    # -------------------------------------------------- Phase 3: which EDGE definition ranks best?
    # judged on VALIDATION only, and on the economics, because that is what an edge claims to predict
    rank_cmp = []
    for col in ("raw_edge", "fee_adjusted_edge", "uncertainty_adjusted_edge", "robust_edge",
                "selector_score"):
        for rate in (0.01, 0.02, 0.05, 0.10):
            v = val.assign(selector_score=d.loc[val.index, "selector_score"])
            k = max(1, int(round(rate * len(v))))
            top = v.nlargest(k, col)
            rank_cmp.append({"ranker": col, "rate": rate, **econ(top)})
    res["edge_definition_comparison_validation"] = rank_cmp

    # ------------------------------------------------------ Phase 6: thresholds, discovery+validation
    dv = pd.concat([disc, val])
    dv = dv.assign(selector_score=d.loc[dv.index, "selector_score"])
    cand = dv[(dv.fee_adjusted_edge > 0) & (dv.robust_edge > 0)]
    thresholds = {}
    for q in (0.99, 0.98, 0.95, 0.90):
        thresholds[f"top_{int((1-q)*100)}pct"] = float(np.quantile(dv.selector_score, q))
    res["threshold_candidates"] = thresholds
    res["positive_robust_edge_rate_dv"] = float(len(cand) / len(dv))

    # ------------------------------------------------------------------ Phase 13: HOLDOUT, read once
    h = hold.assign(selector_score=d.loc[hold.index, "selector_score"])
    holdout = {}
    for rate in (0.01, 0.02, 0.05, 0.10):
        k = max(1, int(round(rate * len(h))))
        for ranker in ("selector_score", "fee_adjusted_edge", "robust_edge"):
            top = h.nlargest(k, ranker)
            key = f"{ranker}@top{int(rate*100)}pct"
            lo, hi = bootstrap_mean(top.pnl.to_numpy(float))
            holdout[key] = {**econ(top), "selection_rate": float(k / len(h)),
                            "model_brier": float(np.mean((top.p_fair - top.y) ** 2)),
                            "market_brier": float(np.mean((top.kalshi_mid - top.y) ** 2)),
                            "model_log_loss": scored(top, "p_fair")["log_loss"],
                            "market_log_loss": scored(top, "kalshi_mid")["log_loss"],
                            "informative_rate": float(top.informative.mean()),
                            "mean_pnl_ci": [lo, hi]}
    # and the gated rule: qualification-style filters AND a selector threshold
    for tname, thr in thresholds.items():
        g = h[(h.fee_adjusted_edge > 0) & (h.robust_edge > 0) & (h.selector_score >= thr)]
        lo, hi = bootstrap_mean(g.pnl.to_numpy(float)) if len(g) else (None, None)
        holdout[f"gated_{tname}"] = {**econ(g), "selection_rate": float(len(g) / len(h)),
                                     "threshold": thr,
                                     "model_brier": float(np.mean((g.p_fair - g.y) ** 2)) if len(g) else None,
                                     "market_brier": float(np.mean((g.kalshi_mid - g.y) ** 2)) if len(g) else None,
                                     "mean_pnl_ci": [lo, hi]}
    res["holdout"] = holdout

    # ------------------------------------------------- Phase 5: calibration among SELECTED rows
    def reliability(x, bins=(0, 0.02, 0.05, 0.10, 1.01), col="fee_adjusted_edge"):
        rows = []
        for lo, hi in zip(bins, bins[1:]):
            g = x[(x[col] >= lo) & (x[col] < hi)]
            if not len(g):
                continue
            rows.append({"bucket": f"{lo:.2f}-{min(hi,1):.2f}", "n": int(len(g)),
                         "claimed_edge": float(g[col].mean()), "realised_edge": float(g.pnl.mean()),
                         "hit_rate": float(g.y.mean()), "implied_by_price": float(g.kalshi_ask.mean()),
                         "ci": list(bootstrap_mean(g.pnl.to_numpy(float)))})
        return rows
    res["selective_calibration"] = {
        "all_holdout": reliability(h),
        "positive_edge_holdout": reliability(h[h.fee_adjusted_edge > 0]),
        "gated_top5_holdout": reliability(h[(h.fee_adjusted_edge > 0) & (h.robust_edge > 0) &
                                            (h.selector_score >= thresholds["top_5pct"])]),
    }

    os.makedirs(a.out, exist_ok=True)
    json.dump(res, open(os.path.join(a.out, "selector_study.json"), "w"), indent=1, default=str)
    d.to_parquet(os.path.join(a.out, "scored.parquet"), index=False)
    json.dump(sel.to_dict(), open(os.path.join(a.out, f"{SELECTOR_VERSION}.json"), "w"), indent=1, default=str)
    print(json.dumps({k: res[k] for k in ("splits", "l2_chosen", "base_rate_informative")}, indent=1, default=str))
    print("\ntop coefficients:")
    for k, v in list(res["coefficients"].items())[:12]:
        print(f"  {k:28s} {v:+.4f}")
    print("\nholdout:")
    for k, v in res["holdout"].items():
        if v.get("n"):
            print(f"  {k:34s} n={v['n']:4d} rate={v.get('selection_rate',0):.3f} hit={v['hit_rate']:.3f} "
                  f"roi={v['roi']:+.4f} pnl={v['total_pnl']:+.2f} ci={v.get('mean_pnl_ci')}")
        else:
            print(f"  {k:34s} n=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
