#!/usr/bin/env python3
"""Does anchoring the winner probability to the market improve DERIVATIVE prediction?

The comparison, on matches where a real bookmaker price and a real final score both exist:

  FUNDAMENTAL        one distribution from the Gen-2 point probabilities
  MARKET-CONDITIONED one distribution that keeps the Gen-2 SERVICE LEVEL and reproduces the de-vigged
                     market winner probability exactly
  ELO-CONDITIONED    the same construction with Gen-1 Elo supplying the difference instead of the market,
                     as the control that separates "the market is informative" from "conditioning on
                     anything is informative"

Scored on things the winner probability alone cannot tell you: how long the match runs, whether it goes
the distance, and the exact set score. The winner probability itself is deliberately NOT scored for the
conditioned lane, because by construction it IS the market's and comparing it would be circular.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from datetime import datetime, timezone

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tennis_edge.models.market_conditioned import conditioned_distribution, remove_vig_two_sided  # noqa: E402
from tennis_edge.rules.formats import MatchFormat, TOUR_SINGLES_BO3                    # noqa: E402
from tennis_edge.sim.analytic import match_distribution                                # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_D: dict = {}


def dist(pa: float, pb: float, best_of: int):
    key = (round(pa, 3), round(pb, 3), best_of)
    d = _D.get(key)
    if d is None:
        fmt = TOUR_SINGLES_BO3 if best_of == 3 else MatchFormat(
            **{**TOUR_SINGLES_BO3.__dict__, "best_of": 5})
        d = match_distribution(key[0], key[1], fmt)
        _D[key] = d
    return d


def _logloss(p: float, hit: bool) -> float:
    p = min(max(p, 1e-6), 1 - 1e-6)
    return -math.log(p if hit else 1 - p)


def score_row(d, games_a, games_b, sets_a, sets_b):
    """Derivative scores for one distribution against one actual result, from A's point of view."""
    total = games_a + games_b
    out = {}
    over = d.total_games_over(21.5)
    out["brier_over_21_5"] = (over - (1.0 if total > 21.5 else 0.0)) ** 2
    out["logloss_over_21_5"] = _logloss(over, total > 21.5)
    e_total = sum(k * v for k, v in d.total_games.items())
    out["abs_err_total_games"] = abs(e_total - total)
    out["sq_err_total_games"] = (e_total - total) ** 2
    p3 = sum(v for k, v in d.sets_played.items() if k >= 3)
    went_long = (sets_a + sets_b) >= 3
    out["brier_sets_played"] = (p3 - (1.0 if went_long else 0.0)) ** 2
    out["logloss_sets_played"] = _logloss(p3, went_long)
    key = (int(sets_a), int(sets_b))
    out["logloss_exact_score"] = _logloss(d.set_score.get(key, 0.0), True)
    diff = games_a - games_b
    e_diff = sum(k * v for k, v in d.game_diff.items())
    out["abs_err_game_diff"] = abs(e_diff - diff)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tour", default="ATP")
    ap.add_argument("--benchmark", default=os.path.join(PROJ, "research", "market_benchmark", "linked_ATP.parquet"))
    ap.add_argument("--gen2", default=os.path.join(PROJ, "research", "gen2", "predictions_ATP.parquet"))
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "market_conditioned"))
    a = ap.parse_args()

    bm = pd.read_parquet(a.benchmark)[["match_key", "p_winner_PS", "p_loser_PS", "season", "level", "surface"]]
    g2 = pd.read_parquet(a.gen2)
    df = g2.merge(bm, on="match_key", how="inner", suffixes=("", "_bm"))
    df = df[df.p_winner_PS.notna() & df.games_w.notna() & df.sets_w.notna()].copy()
    print(f"{a.tour}: {len(df)} matches with a bookmaker price, a Gen-2 state and a final score", flush=True)

    rows, t0 = [], time.time()
    for r in df.itertuples(index=False):
        # orientation: the study frame's side A is the row winner when a_is_winner
        pw, pl = remove_vig_two_sided(float(r.p_winner_PS), float(r.p_loser_PS))
        p_mkt_a = pw if r.a_is_winner else pl
        ga, gb = (r.games_w, r.games_l) if r.a_is_winner else (r.games_l, r.games_w)
        sa, sb = (r.sets_w, r.sets_l) if r.a_is_winner else (r.sets_l, r.sets_w)
        bo = int(r.best_of or 3)
        try:
            d_fund = dist(r.gen2_pa, r.gen2_pb, bo)
            d_mkt, _ = conditioned_distribution(p_mkt_a, r.gen2_pa, r.gen2_pb,
                                                TOUR_SINGLES_BO3 if bo == 3 else
                                                MatchFormat(**{**TOUR_SINGLES_BO3.__dict__, "best_of": 5}))
            d_elo, _ = conditioned_distribution(float(r.p_elo), r.gen2_pa, r.gen2_pb,
                                                TOUR_SINGLES_BO3 if bo == 3 else
                                                MatchFormat(**{**TOUR_SINGLES_BO3.__dict__, "best_of": 5}))
        except Exception:
            continue
        base = {"match_key": r.match_key, "season": r.season, "level": r.level, "surface": r.surface,
                "y": r.y, "p_market": p_mkt_a, "p_elo": r.p_elo, "p_gen2": r.p_gen2,
                "total_games": ga + gb, "went_long": int((sa + sb) >= 3)}
        for lane, d in (("fundamental", d_fund), ("market_conditioned", d_mkt), ("elo_conditioned", d_elo)):
            s = score_row(d, ga, gb, sa, sb)
            rows.append({**base, "lane": lane, **s})
    out = pd.DataFrame(rows)
    os.makedirs(a.out, exist_ok=True)
    out.to_parquet(os.path.join(a.out, f"scored_{a.tour}.parquet"), index=False)

    metrics = ["brier_over_21_5", "logloss_over_21_5", "abs_err_total_games", "sq_err_total_games",
               "brier_sets_played", "logloss_sets_played", "logloss_exact_score", "abs_err_game_diff"]
    agg = out.groupby("lane")[metrics].mean().round(5)
    n = out.lane.value_counts().to_dict()
    print(f"scored in {time.time()-t0:.0f}s; rows per lane {n}")
    print(agg.to_string())

    # paired bootstrap of market-conditioned minus fundamental, per metric
    piv = out.pivot_table(index="match_key", columns="lane", values=metrics)
    rng = np.random.default_rng(20260912)
    boot = {}
    for m in metrics:
        try:
            d_ = (piv[(m, "market_conditioned")] - piv[(m, "fundamental")]).dropna().values
        except KeyError:
            continue
        if len(d_) < 100:
            continue
        idx = rng.integers(0, len(d_), size=(2000, len(d_)))
        means = d_[idx].mean(axis=1)
        boot[m] = {"diff": float(d_.mean()), "ci_lo": float(np.percentile(means, 2.5)),
                   "ci_hi": float(np.percentile(means, 97.5)),
                   "p_better": float((means < 0).mean()), "n": int(len(d_))}
    res = {"tour": a.tour, "generated_at": datetime.now(timezone.utc).isoformat(), "n_matches": int(len(df)),
           "rows_per_lane": n, "means": json.loads(agg.to_json()), "bootstrap_mc_minus_fundamental": boot}
    json.dump(res, open(os.path.join(a.out, f"results_{a.tour}.json"), "w"), indent=1, default=str)

    L = [f"# Market-conditioned derivative pricing ({a.tour})", "",
         f"{len(df)} matches with a de-vigged Pinnacle price, a Gen-2 structural state and a final score.",
         "", "Lower is better for every metric.", "",
         "| metric | fundamental | market-conditioned | elo-conditioned |", "|---|---|---|---|"]
    for m in metrics:
        L.append(f"| {m} | {agg.loc['fundamental', m]:.5f} | {agg.loc['market_conditioned', m]:.5f} | "
                 f"{agg.loc['elo_conditioned', m]:.5f} |")
    L += ["", "## Paired bootstrap, market-conditioned minus fundamental (negative favours conditioning)", "",
          "| metric | diff | 95% CI | P(better) | n |", "|---|---|---|---|---|"]
    for m, b in boot.items():
        L.append(f"| {m} | {b['diff']:+.5f} | [{b['ci_lo']:+.5f}, {b['ci_hi']:+.5f}] | {b['p_better']:.2f} | {b['n']} |")
    open(os.path.join(a.out, f"RESULTS_{a.tour}.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L[-14:]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
