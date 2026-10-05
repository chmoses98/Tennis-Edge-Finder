#!/usr/bin/env python3
"""Workstream G: does the match-winner improvement carry into the derivative distribution?

Every derivative market (sets, exact set score, total games, game spread) is priced from ONE exact match
distribution built from point probabilities. Those come from inverting the match probability with an assumed
service level (spw): the incumbent uses the tour/surface baseline. V2 changes the match probability; the
service level is a separate choice, scored here:

  INCUMBENT       incumbent match probability, baseline spw              (production today)
  V2_BASE_SPW     V2 match probability, baseline spw
  V2_G2_SPW       V2 match probability, Gen-2 implied service level 0.5 * (pa + 1 - pb)
  V2_BLEND_SPW    V2 match probability, spw shrunk from baseline toward Gen-2 by the thinner player's evidence

Scored on COMPLETED matches with parsed scores (retirements excluded: their score is truncated) with proper
scoring rules: ranked probability score (RPS) for total games and game differential, log score for the set
score, Brier for "goes the distance" and for a line near each match's median total. Selection of the spw
rule uses 2023-2024 only; 2025-2026 is reported as confirmation.
"""
from __future__ import annotations

import argparse, json, os, sys
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "research", "projection_v2")
VARIANTS = ("INCUMBENT", "V2_BASE_SPW", "V2_G2_SPW", "V2_BLEND_SPW")


def _dist_summ(args):
    from tennis_edge.rules.formats import TOUR_SINGLES_BO3
    from tennis_edge.sim.analytic import match_distribution
    from tennis_edge.sim.vectorized import point_probs_from_match_prob
    from tennis_edge.v2.replay import BO5
    p, spw2, bo = args
    fmt = BO5 if bo == 5 else TOUR_SINGLES_BO3
    out = []
    pa, pb = point_probs_from_match_prob(np.asarray(p), np.asarray(spw2), fmt)
    cache = {}
    for a, b in zip(pa, pb):
        key = (round(float(a), 3), round(float(b), 3))
        d = cache.get(key)
        if d is None:
            md = match_distribution(key[0], key[1], fmt)
            d = (dict(md.total_games), dict(md.game_diff), dict(md.set_score))
            cache[key] = d
        out.append(d)
    return out


def rps(dist: dict, obs: int, support) -> float:
    cdf = np.cumsum([dist.get(k, 0.0) for k in support])
    o = (np.asarray(support) >= obs).astype(float)
    return float(np.mean((cdf - o) ** 2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--replay", default="/home/user/work/v2/replay")
    ap.add_argument("--per-season", type=int, default=6000)
    a = ap.parse_args()
    preds = pd.concat([pd.read_parquet(os.path.join(OUT, f"predictions_{s}.parquet")) for s in ("validate", "holdout")])
    preds = preds[preds.season >= 2023]
    rows = []
    for t in ("ATP", "WTA"):
        r = pd.read_parquet(os.path.join(a.replay, f"replay_{t}.parquet"),
                            columns=["uid", "spw", "g2_pa", "g2_pb", "g2_ev_min", "games_a", "games_b", "sets_a", "sets_b",
                                     "outcome", "best_of"])
        rows.append(preds[preds.tour == t].merge(r, on="uid", suffixes=("", "_r")))
    df = pd.concat(rows, ignore_index=True)
    df = df[(df.outcome == "COMPLETED") & df.games_a.notna() & df.games_b.notna() & df.sets_a.notna()]
    df = df.sample(frac=1.0, random_state=1).groupby(["season", "tour"]).head(a.per_season // 2).reset_index(drop=True)
    g2_spw = 0.5 * (df.g2_pa + (1 - df.g2_pb))
    w = df.g2_ev_min / (df.g2_ev_min + 1500.0)
    spw = {"INCUMBENT": df.spw, "V2_BASE_SPW": df.spw, "V2_G2_SPW": g2_spw, "V2_BLEND_SPW": (1 - w) * df.spw + w * g2_spw}
    pm = {"INCUMBENT": df.INCUMBENT, "V2_BASE_SPW": df.CHALLENGER, "V2_G2_SPW": df.CHALLENGER, "V2_BLEND_SPW": df.CHALLENGER}
    dists = {}
    jobs = []
    for v in VARIANTS:
        for bo in (3, 5):
            m = (df.best_of == bo).to_numpy()
            idx = np.where(m)[0]
            for chunk in np.array_split(idx, 4):
                if len(chunk):
                    jobs.append((v, chunk, (pm[v].to_numpy()[chunk], 2 * spw[v].to_numpy()[chunk], bo)))
    with ProcessPoolExecutor(max_workers=4) as ex:
        for (v, chunk, _), res in zip(jobs, ex.map(_dist_summ, [j[2] for j in jobs])):
            for i, d in zip(chunk, res):
                dists[(v, int(i))] = d
    recs = []
    for i, row in df.iterrows():
        tg = int(row.games_a + row.games_b)
        gd = int(row.games_a - row.games_b)
        ss = (int(row.sets_a), int(row.sets_b))
        full = (row.sets_a + row.sets_b) == row.best_of
        for v in VARIANTS:
            tot, diff, sets = dists[(v, i)]
            tsup = range(min(tot) if tot else 0, (max(tot) if tot else 0) + 1)
            dsup = range(min(diff), max(diff) + 1)
            p_full = sum(p for (x, y), p in sets.items() if x + y == row.best_of)
            line = 22.5 if row.best_of == 3 else 38.5
            p_over = sum(p for k, p in tot.items() if k > line)
            recs.append({"season": row.season, "tour": row.tour, "variant": v,
                         "rps_total_games": rps(tot, tg, tsup), "rps_game_diff": rps(diff, gd, dsup),
                         "ll_set_score": -np.log(max(sets.get(ss, 0.0), 1e-9)),
                         "brier_distance": (p_full - float(full)) ** 2,
                         "brier_over_line": (p_over - float(tg > line)) ** 2})
    R = pd.DataFrame(recs)
    R["window"] = np.where(R.season <= 2024, "selection_2023_2024", "confirmation_2025_2026")
    summ = R.groupby(["window", "tour", "variant"]).mean(numeric_only=True).drop(columns="season").round(5)
    sel = R[R.window == "selection_2023_2024"].groupby("variant")[["rps_total_games", "ll_set_score"]].mean()
    chosen = sel.rank().sum(axis=1).idxmin()
    out = {"summary": {f"{w}|{t}|{v}": row.to_dict() for (w, t, v), row in summ.iterrows()},
           "n_matches": int(len(df)), "chosen_on_selection_window": chosen,
           "note": "V2 spw rule chosen on 2023-2024 by mean rank of total-games RPS and set-score log score; 2025-2026 confirms."}
    json.dump(out, open(os.path.join(OUT, "derivatives_eval.json"), "w"), indent=1)
    print(summ.to_string())
    print("chosen:", chosen)


if __name__ == "__main__":
    main()
