#!/usr/bin/env python3
"""Walk-forward comparison of the model lanes on canonical results. No prices anywhere in this file.

Lanes scored here:
  MODEL 1  Gen-1 Elo (production configuration)
  MODEL 2  Gen-1 structural serve/return
  MODEL 3  Gen-2 dynamic hierarchical serve/return
  rank     ATP/WTA ranking baseline, for scale

Every lane predicts a match BEFORE it is used to update that lane's state, in strict match order, so no
prediction can see its own outcome or anything after it. Orientation is randomised per match so a model
cannot score well by always favouring the row's winner column.

Derivative accuracy is measured too, on the subset with serve statistics: the same latent state has to
produce a total-games distribution and an exact-set-score distribution, not just a winner probability.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tennis_edge.eval.metrics import summary                                        # noqa: E402
from tennis_edge.models.elo import Elo, EloConfig, match_sort_key                    # noqa: E402
from tennis_edge.models.gen2 import Gen2Config, Gen2State, serve_points, logit, sigmoid  # noqa: E402
from tennis_edge.models.serve_return import SRConfig, ServeReturnModel               # noqa: E402
from tennis_edge.rules.formats import TOUR_SINGLES_BO3, MatchFormat                  # noqa: E402
from tennis_edge.sim.analytic import match_distribution, match_win_prob, point_probs_from_match_prob  # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PROD_ELO = EloConfig(k0=180, use_surface=True, use_level_k=True, use_level_prior=True)
_MWP: dict = {}
_INV: dict = {}


def inv_point_probs(p_match: float, spw_sum: float):
    """Cached inversion of a match probability to point probabilities.

    The bisection costs about a millisecond; at 350k matches per tour that is six minutes of pure search
    for answers that repeat constantly once rounded. The service level is rounded harder than the match
    probability: the level shifts the DERIVATIVES, while the match probability is the thing that must be
    reproduced, and a three-by-three-decimal key almost never hits twice.
    """
    key = (round(p_match, 3), round(spw_sum, 2))
    v = _INV.get(key)
    if v is None:
        v = point_probs_from_match_prob(key[0], key[1], TOUR_SINGLES_BO3)
        _INV[key] = v
    return v


def mwp(pa: float, pb: float, best_of: int) -> float:
    key = (round(pa, 3), round(pb, 3), best_of)
    v = _MWP.get(key)
    if v is None:
        fmt = TOUR_SINGLES_BO3 if best_of == 3 else MatchFormat(best_of=5, **{k: v2 for k, v2 in
                                                                              TOUR_SINGLES_BO3.__dict__.items()
                                                                              if k != "best_of"})
        v = match_win_prob(key[0], key[1], fmt)
        _MWP[key] = v
    return v


def orient(match_key: str) -> bool:
    """Deterministic coin flip per match: True means the row's WINNER is oriented as side A."""
    return hashlib.sha256(str(match_key).encode()).digest()[0] % 2 == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tour", default="ATP")
    ap.add_argument("--from-season", type=int, default=2015)
    ap.add_argument("--matches", default=os.path.join(PROJ, "data", "processed", "matches.parquet"))
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "gen2"))
    ap.add_argument("--half-life", type=float, default=300.0)
    ap.add_argument("--prior-points", type=float, default=500.0)
    ap.add_argument("--deriv-from-season", type=int, default=2023, help="derivative scoring is DP-heavy")
    ap.add_argument("--blend-points", type=float, default=1500.0,
                    help="serve points at which the structural model carries half the weight against the rating")
    a = ap.parse_args()

    t0 = time.time()
    df = pd.read_parquet(a.matches)
    m = df[(df.tour == a.tour) & (df.outcome_type == "COMPLETED") & df.tourney_date.notna()].copy()
    if "canonical_id_status" in m.columns:
        m = m[m.canonical_id_status == "MAPPED"].copy()
        m["winner_id"] = m["canonical_winner_id"].astype(str)
        m["loser_id"] = m["canonical_loser_id"].astype(str)
    m["tourney_date"] = pd.to_datetime(m["tourney_date"]).dt.date
    m = match_sort_key(m)
    print(f"{a.tour}: {len(m)} completed matches, {m.tourney_date.min()} .. {m.tourney_date.max()}", flush=True)

    elo = Elo(PROD_ELO)
    sr = ServeReturnModel(SRConfig())
    g2 = Gen2State(Gen2Config(half_life_days=a.half_life, prior_points=a.prior_points))

    rows = []
    # the Gen-1 serve/return updater takes an attribute-style record, so iterate namedtuples and expose a
    # dict view for everything else
    recs = list(m.itertuples(index=False))
    for i, rec in enumerate(recs):
        row = rec._asdict()
        season = row.get("season")
        tour, level = row.get("tour"), row.get("level_canonical") or "OTHER"
        surface, date = row.get("surface"), row.get("tourney_date")
        w, l = str(row.get("winner_id")), str(row.get("loser_id"))
        best_of = int(row.get("best_of") or 3)
        evaluate = season is not None and season >= a.from_season

        if evaluate:
            a_is_winner = orient(row.get("match_key") or f"{w}|{l}|{date}")
            pa_id, pb_id = (w, l) if a_is_winner else (l, w)
            y = 1.0 if a_is_winner else 0.0

            elo._init(pa_id, level)
            elo._init(pb_id, level)
            p_elo = elo.predict(pa_id, pb_id, surface, level)
            spa, spb = sr.predict(pa_id, pb_id, tour, surface)
            p_sr = mwp(spa, spb, best_of)
            gpa, gpb = g2.predict_point_probs(pa_id, pb_id, tour, level, surface)
            p_g2 = mwp(gpa, gpb, best_of)
            # UNCERTAINTY-WEIGHTED FALLBACK (still Model 3: ratings come from results, never prices).
            # Serve statistics exist for four percent of ITF matches, so a structural model has nothing
            # to say about most of the universe. Rather than pretend, the structural point probabilities
            # are shrunk toward the point probabilities IMPLIED by the rating, in proportion to how much
            # serve evidence the thinner of the two players actually has.
            ev_min = min(g2.evidence(pa_id), g2.evidence(pb_id))
            wgt = ev_min / (ev_min + a.blend_points)
            base_spw = 0.5 * (gpa + (1.0 - gpb))
            epa, epb = inv_point_probs(p_elo, 2 * base_spw)
            bpa, bpb = wgt * gpa + (1 - wgt) * epa, wgt * gpb + (1 - wgt) * epb
            p_g2b = mwp(bpa, bpb, best_of)
            wr, lr = row.get("winner_rank"), row.get("loser_rank")
            try:
                ra = float(wr if a_is_winner else lr); rb = float(lr if a_is_winner else wr)
                p_rank = 1.0 / (1.0 + (max(ra, 1) / max(rb, 1)) ** 0.5) if ra == ra and rb == rb else np.nan
            except (TypeError, ValueError):
                p_rank = np.nan
            rows.append({"match_key": row.get("match_key"), "season": season, "level": level,
                         "surface": surface, "best_of": best_of, "y": y, "p_elo": p_elo, "p_sr": p_sr,
                         "p_gen2": p_g2, "p_gen2_blend": p_g2b, "blend_weight": wgt, "p_rank": p_rank,
                         "gen2_pa": gpa, "gen2_pb": gpb, "sr_pa": spa, "sr_pb": spb,
                         "ev_a": g2.evidence(pa_id), "ev_b": g2.evidence(pb_id),
                         "games_w": row.get("games_w"), "games_l": row.get("games_l"),
                         "sets_w": row.get("sets_w"), "sets_l": row.get("sets_l"),
                         "a_is_winner": a_is_winner, "date": str(date)})

        weight = PROD_ELO.retirement_weight if row.get("outcome_type") in ("RETIRED", "DEFAULT") else 1.0
        elo.update(w, l, surface, level, weight, date)
        sr.update(rec)
        wp, ww = serve_points(row, "w")
        lp, lw = serve_points(row, "l")
        if wp and lp:
            g2.observe(server=w, returner=l, points=wp, won=ww, tour=tour, level=level, surface=surface, date=date)
            g2.observe(server=l, returner=w, points=lp, won=lw, tour=tour, level=level, surface=surface, date=date)
        if (i + 1) % 200000 == 0:
            print(f"  {i+1}/{len(recs)} ({time.time()-t0:.0f}s)", flush=True)

    out = pd.DataFrame(rows)
    os.makedirs(a.out, exist_ok=True)
    out.to_parquet(os.path.join(a.out, f"predictions_{a.tour}.parquet"), index=False)
    print(f"evaluated {len(out)} matches in {time.time()-t0:.0f}s", flush=True)
    return out


if __name__ == "__main__":
    main()
