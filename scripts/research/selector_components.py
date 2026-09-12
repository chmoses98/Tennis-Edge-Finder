#!/usr/bin/env python3
"""The component questions behind the selector, each answered on DISCOVERY+VALIDATION only.

Phase 4  robustness      does an edge that survives reparameterisation behave better than one that does not?
Phase 7  consensus       does agreement between independent lanes predict anything?
Phase 8  execution       what does the edge look like after the fee, and up to what price is it still there?
Phase 9  sensitivity     is it durable or one tick from nothing?
Phase 10 movement        does the market's recent behaviour separate good disagreements from bad?
Phase 14 failure modes   what characterises the confident misses?

Plus a second selector trained on the ECONOMICS rather than on proper-score superiority, because the
first one's target turned out to be dominated by how far the price sits from even money.

The holdout block is not read here.
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

from tennis_edge.pricing.fees import taker_fee, breakeven_price, FeeSchedule   # noqa: E402
from tennis_edge.selector.features import FEATURES, build_features             # noqa: E402
from tennis_edge.selector.model import Selector                                # noqa: E402


def boot_ci(x, n_boot=4000, seed=20260913):
    x = np.asarray(x, float)
    if len(x) < 3:
        return [None, None]
    rng = np.random.default_rng(seed)
    m = x[rng.integers(0, len(x), size=(n_boot, len(x)))].mean(axis=1)
    return [float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))]


def grp(d: pd.DataFrame, name: str) -> dict:
    if not len(d):
        return {"subset": name, "n": 0}
    cost = d.kalshi_ask + d.fee
    return {"subset": name, "n": int(len(d)), "hit_rate": float(d.y.mean()),
            "avg_ask": float(d.kalshi_ask.mean()), "claimed_edge": float(d.fee_adjusted_edge.mean()),
            "realised_edge": float(d.pnl.mean()), "roi": float(d.pnl.sum() / cost.sum()),
            "ci_realised": boot_ci(d.pnl.to_numpy(float)),
            "model_brier": float(np.mean((d.p_fair - d.y) ** 2)),
            "market_brier": float(np.mean((d.kalshi_mid - d.y) ** 2))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=os.path.join(PROJ, "research", "selector", "scored.parquet"))
    ap.add_argument("--discovery-end", default="2026-09-02")
    ap.add_argument("--validation-end", default="2026-09-06")
    a = ap.parse_args()
    d = pd.read_parquet(a.data)
    dv = d[d.sched_date <= a.validation_end].copy()
    disc = dv[dv.sched_date <= a.discovery_end]
    val = dv[dv.sched_date > a.discovery_end]
    pos = dv[dv.fee_adjusted_edge > 0]
    stamp = {"generated_at": datetime.now(timezone.utc).isoformat(),
             "window": [str(dv.sched_date.min()), str(dv.sched_date.max())],
             "n_rows": int(len(dv)), "note": "discovery+validation only; the holdout is not read here"}

    # ---------------------------------------------------------------- Phase 4: robustness
    rob = {**stamp, "subsets": [
        grp(pos, "positive fee-adjusted edge"),
        grp(pos[pos.robust_edge > 0], "edge survives EVERY perturbation"),
        grp(pos[pos.robust_edge <= 0], "edge dies under at least one perturbation"),
        grp(pos[(pos.p_env_max - pos.p_env_min) < 0.05], "narrow envelope (<5c)"),
        grp(pos[(pos.p_env_max - pos.p_env_min) >= 0.05], "wide envelope (>=5c)"),
    ]}
    for band in ((0.0, 0.03), (0.03, 0.07), (0.07, 0.15), (0.15, 1.01)):
        s = pos[(pos.fee_adjusted_edge >= band[0]) & (pos.fee_adjusted_edge < band[1])]
        rob["subsets"].append(grp(s, f"claimed edge {band[0]:.2f}-{band[1]:.2f}"))
        rob["subsets"].append(grp(s[s.robust_edge > 0], f"claimed edge {band[0]:.2f}-{band[1]:.2f} AND robust"))

    # ---------------------------------------------------------------- Phase 7: consensus
    dis_g2 = dv.p_fair - dv.kalshi_mid
    agree_elo = np.sign(dv.p_elo - dv.kalshi_mid) == np.sign(dis_g2)
    agree_sr = np.sign(dv.p_sr - dv.kalshi_mid) == np.sign(dis_g2)
    con = {**stamp,
           "dependence_note": "Elo, Gen-1 structural and Gen-2 are all fundamental and share the same "
                              "rating substrate, so they are NOT independent witnesses; a "
                              "market-conditioned lane would be dependent on the market itself and is "
                              "excluded from every consensus count below.",
           "subsets": [
               grp(pos, "positive edge, any consensus"),
               grp(pos[agree_elo.loc[pos.index] & agree_sr.loc[pos.index]], "Gen-2 + Elo + Gen-1 agree"),
               grp(pos[agree_elo.loc[pos.index] & ~agree_sr.loc[pos.index]], "Gen-2 + Elo agree, Gen-1 does not"),
               grp(pos[~agree_elo.loc[pos.index]], "Elo disagrees with Gen-2"),
               grp(pos[(pos.p_fair - pos.p_elo).abs() < 0.02], "Gen-2 and Elo within 2c of each other"),
               grp(pos[(pos.p_fair - pos.p_elo).abs() >= 0.08], "Gen-2 and Elo more than 8c apart"),
           ]}

    # ------------------------------------------------- Phase 8/9: execution and price sensitivity
    ex_rows = []
    for label, sub in (("positive edge", pos), ("positive robust edge", pos[pos.robust_edge > 0])):
        for bump in (0.0, 0.01, 0.02, 0.03, 0.05):
            price = np.minimum(sub.kalshi_ask + bump, 0.99)
            fee = np.array([taker_fee(p, 1.0, FeeSchedule()) for p in price])
            pnl = sub.y - price - fee
            ex_rows.append({"subset": label, "worse_execution_cents": int(bump * 100), "n": int(len(sub)),
                            "mean_pnl": float(pnl.mean()), "roi": float(pnl.sum() / (price + fee).sum()),
                            "ci": boot_ci(pnl)})
    bet_up = [breakeven_price(float(p), FeeSchedule()) for p in pos.p_fair]
    exe = {**stamp, "sensitivity": ex_rows,
           "bet_up_to": {"n": int(len(pos)), "median_bet_up_to": float(np.median(bet_up)) if len(bet_up) else None,
                         "median_ask": float(pos.kalshi_ask.median()) if len(pos) else None,
                         "median_headroom_cents": float(np.median(np.array(bet_up) - pos.kalshi_ask.to_numpy()) * 100)
                         if len(bet_up) else None},
           "one_tick_fragile_share": float((pos.fee_adjusted_edge < 0.01).mean()) if len(pos) else None}

    # ---------------------------------------------------------------- Phase 10: market movement
    mv = pos.assign(toward=np.sign(pos.p_fair - pos.kalshi_mid) * pos.mv_move_6h.fillna(0.0))
    mov = {**stamp, "subsets": [
        grp(mv[mv.toward > 0.005], "market moved TOWARD our side in the last 6h"),
        grp(mv[mv.toward < -0.005], "market moved AGAINST our side in the last 6h"),
        grp(mv[mv.toward.abs() <= 0.005], "market barely moved"),
        grp(pos[pos.mv_abs_move_6h.fillna(0) > 0.10], "a large 6h move in either direction"),
        grp(pos[pos.mv_volatility_24h.fillna(0) > 0.06], "high 24h volatility"),
        grp(pos[pos.mv_n_quotes_24h.fillna(0) >= 20], "quoted in at least 20 of the last 24 hours"),
        grp(pos[pos.mv_n_quotes_24h.fillna(0) < 8], "quoted in fewer than 8 of the last 24 hours"),
    ]}

    # ------------------------------------------- a second selector, trained on the ECONOMICS
    X = build_features(d)
    s2 = Selector(version="selector_v1_econ", feature_names=tuple(FEATURES),
                  target="after_fee_profitable", trained_from=str(disc.sched_date.min()),
                  trained_through=a.discovery_end, l2=100.0,
                  notes="P(buying this side at this ask returns more than it costs). Same features, "
                        "same discovery block, economics as the label.")
    s2.fit(X.loc[disc.index], (disc.pnl > 0).astype(float).to_numpy(), disc.sched_date).freeze()
    val_scores = s2.score(X.loc[val.index])
    econ_sel = {**stamp, "coefficients": dict(sorted(s2.coefficients().items(), key=lambda kv: -abs(kv[1]))[:12]),
                "validation": []}
    v = val.assign(s2=val_scores)
    for rate in (0.01, 0.02, 0.05, 0.10):
        k = max(1, int(round(rate * len(v))))
        econ_sel["validation"].append({"rate": rate, **grp(v.nlargest(k, "s2"), f"top {rate:.0%} by econ selector")})

    # ---------------------------------------------------------------- Phase 14: failure modes
    misses = pos[(pos.fee_adjusted_edge > 0.05) & (pos.y == 0)]
    hits = pos[(pos.fee_adjusted_edge > 0.05) & (pos.y == 1)]
    def profile(x):
        if not len(x):
            return {}
        return {"n": int(len(x)), "median_ask": float(x.kalshi_ask.median()),
                "median_ev_min": float(x.ev_min.median()), "median_days_stale": float(x.days_stale_max.median()),
                "median_data_quality": float(x.data_quality.median()),
                "share_itf": float((x.level == "ITF").mean()), "share_wta": float((x.tour == "WTA").mean()),
                "median_env_width": float((x.p_env_max - x.p_env_min).median()),
                "share_elo_disagrees": float((np.sign(x.p_elo - x.kalshi_mid) != np.sign(x.p_fair - x.kalshi_mid)).mean()),
                "median_n_matches_min": float(x.n_matches_min.median()),
                "median_move_6h_toward": float((np.sign(x.p_fair - x.kalshi_mid) * x.mv_move_6h.fillna(0)).median())}
    fail = {**stamp, "confident_misses": profile(misses), "confident_hits": profile(hits),
            "by_level": [grp(pos[pos.level == lv], f"level {lv}") for lv in sorted(pos.level.unique())],
            "by_price_band": [grp(pos[(pos.kalshi_ask >= lo) & (pos.kalshi_ask < hi)], f"ask {lo:.2f}-{hi:.2f}")
                              for lo, hi in ((0.0, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 1.0))]}

    # ------------------------------------------------------- market's own calibration (model-free)
    bins = [0, .05, .1, .2, .3, .4, .5, .6, .7, .8, .9, .95, 1.001]
    cal = []
    b = pd.cut(dv.kalshi_mid, bins)
    for name, g in dv.groupby(b, observed=True):
        cal.append({"bucket": str(name), "n": int(len(g)), "mean_mid": float(g.kalshi_mid.mean()),
                    "observed": float(g.y.mean()), "diff": float(g.y.mean() - g.kalshi_mid.mean()),
                    "ci": boot_ci((g.y - g.kalshi_mid).to_numpy(float))})
    market = {**stamp, "calibration": cal,
              "all_rows_ask_roi": float((dv.y - dv.kalshi_ask - dv.fee).sum() / (dv.kalshi_ask + dv.fee).sum()),
              "median_spread": float(dv.spread.median()), "median_fee": float(dv.fee.median())}

    for sub, obj, fn in (("robustness", rob, "results.json"), ("consensus", con, "results.json"),
                         ("execution", exe, "results.json"), ("execution", mov, "movement.json"),
                         ("failure_modes", fail, "results.json"), ("selector", econ_sel, "econ_selector.json"),
                         ("selector", market, "market_calibration.json")):
        os.makedirs(os.path.join(PROJ, "research", sub), exist_ok=True)
        json.dump(obj, open(os.path.join(PROJ, "research", sub, fn), "w"), indent=1, default=str)

    for title, obj in (("ROBUSTNESS", rob), ("CONSENSUS", con), ("MOVEMENT", mov)):
        print(f"\n== {title}")
        for s in obj["subsets"]:
            if s.get("n"):
                print(f"  {s['subset']:52s} n={s['n']:4d} claimed={s['claimed_edge']:+.4f} "
                      f"realised={s['realised_edge']:+.4f} ci=[{s['ci_realised'][0]:+.3f},{s['ci_realised'][1]:+.3f}] roi={s['roi']:+.3f}")
    print("\n== EXECUTION sensitivity")
    for r in exe["sensitivity"]:
        print(f"  {r['subset']:22s} +{r['worse_execution_cents']}c n={r['n']:4d} mean_pnl={r['mean_pnl']:+.4f} roi={r['roi']:+.3f}")
    print(f"\n  bet_up_to: {exe['bet_up_to']}")
    print(f"  one-tick-fragile share: {exe['one_tick_fragile_share']:.3f}")
    print("\n== ECON SELECTOR (validation)")
    for r in econ_sel["validation"]:
        print(f"  top {r['rate']:.0%} n={r['n']:3d} hit={r['hit_rate']:.3f} realised={r['realised_edge']:+.4f} roi={r['roi']:+.3f}")
    print("\n== FAILURE PROFILE (claimed edge > 5c)")
    print("  miss:", json.dumps(fail["confident_misses"], default=str))
    print("  hit :", json.dumps(fail["confident_hits"], default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
