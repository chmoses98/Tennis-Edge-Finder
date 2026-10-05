"""One chronological pass over the canonical table that records every model's PRE-match view of every match.

For each match, in match order (`models.elo.match_sort_key`), the replay

  1. reads every state -- each Elo variant, Gen-1 serve/return, Gen-2 (two half-lives), form, context --
     for the two players as they stand BEFORE the match, and stores predictions and features oriented to a
     deterministic coin-flip "player A";
  2. only then applies the match to every state.

So a stored row can only contain information from matches that precede it in match order. Nothing here
reads a price; `tests/test_v2_engine.py` walks the import graph of this package and fails if it can reach
a market module.

The output is a DataFrame with, per match: outcome y (1 if A won), identifiers and segments, each Elo
variant's best-of-3-basis probability, Gen-1 and Gen-2 point probabilities and evidence, form and context
features for both sides. Match-format conversion (best-of-5) and the incumbent's ensemble rule are applied
afterwards, vectorised (`finalise`).
"""
from __future__ import annotations

import hashlib
import math

import numpy as np
import pandas as pd

from tennis_edge.models.elo import match_sort_key
from tennis_edge.models.gen2 import Gen2Config, Gen2State, serve_points
from tennis_edge.models.serve_return import ServeReturnModel, SRConfig
from tennis_edge.rules.formats import MatchFormat, TOUR_SINGLES_BO3
from tennis_edge.sim import vectorized as vz
from tennis_edge.v2.elo import EloV2, EloV2Config
from tennis_edge.v2.form import HORIZONS, ContextState, FormState, rest_feature

BO5 = MatchFormat(best_of=5, final_set="TB10_AT_6", name="slam_bo5")

#: the incumbent production Elo (state.PROD_ELO), reproduced exactly including Gen-1's surface seeding
INCUMBENT_ELO = EloV2Config(name="E_prod", k0=180, use_level_prior=True, use_level_k=True, surface_w_max=0.5,
                            gen1_surface_seed=True)

#: the rating tournament (C1). Hyper-parameters are fixed here BEFORE any evaluation and selected on the
#: development window only (see research/projection_v2/PREREGISTRATION.md).
ELO_VARIANTS = (
    INCUMBENT_ELO,
    EloV2Config(name="E_plain", use_level_prior=False),
    EloV2Config(name="E_lp"),
    EloV2Config(name="E_lp_k200", k0=200),
    EloV2Config(name="E_lp_k320", k0=320),
    EloV2Config(name="E_lp_sh3", shape=0.3, k0=180),
    EloV2Config(name="E_surf50", surface_w_max=0.5),
    EloV2Config(name="E_surf25", surface_w_max=0.25),
    EloV2Config(name="E_surf_levelk", surface_w_max=0.5, use_level_k=True),
    EloV2Config(name="E_mov", mov_a=0.6, mov_b=1.6),
    EloV2Config(name="E_mov_strong", mov_a=0.35, mov_b=2.6),
    EloV2Config(name="E_mov_k200", k0=200, mov_a=0.6, mov_b=1.6),
    EloV2Config(name="E_mov_surf25", mov_a=0.6, mov_b=1.6, surface_w_max=0.25),
    EloV2Config(name="E_mov_lay", mov_a=0.6, mov_b=1.6, layoff_boost=1.0),
    EloV2Config(name="E_lay", layoff_boost=1.0),
)
REFERENCE_ELO = "E_lp"   # residual reference for the form state

GEN2_VARIANTS = {"g2": Gen2Config(), "g2s": Gen2Config(half_life_days=60.0)}


def orient(uid: str) -> bool:
    """Deterministic coin flip: True means the row's WINNER is player A."""
    return hashlib.sha256(uid.encode()).digest()[0] % 2 == 0


#: the only canonical columns the replay reads (keeps a 1.5M-row replay inside a few GB)
COLUMNS = ["tour", "outcome_type", "tourney_date", "canonical_id_status", "canonical_winner_id", "canonical_loser_id",
           "id_system", "winner_id", "loser_id", "match_key", "source_label", "tourney_id", "tourney_name",
           "level_canonical", "surface", "best_of", "round", "match_num", "games_w", "games_l", "sets_w", "sets_l",
           "score_raw", "winner_age", "loser_age", "winner_rank", "loser_rank", "minutes",
           "w_svpt", "w_1stWon", "w_2ndWon", "l_svpt", "l_1stWon", "l_2ndWon"]


def prepare(matches: pd.DataFrame, tour: str) -> pd.DataFrame:
    matches = matches[[c for c in COLUMNS if c in matches.columns]]
    m = matches[(matches.tour == tour) & (matches.outcome_type != "WALKOVER") & matches.tourney_date.notna()].copy()
    if "canonical_id_status" in m.columns:
        m = m[m.canonical_id_status == "MAPPED"].copy()
        m["winner_id"] = m["canonical_winner_id"].astype(str)
        m["loser_id"] = m["canonical_loser_id"].astype(str)
    else:
        m = m[m.id_system == "sackmann"].copy()
    m["tourney_date"] = pd.to_datetime(m["tourney_date"]).dt.date
    m = match_sort_key(m)
    return m


def _f(x):
    try:
        v = float(x)
        return None if v != v else v
    except (TypeError, ValueError):
        return None


def replay(matches: pd.DataFrame, tour: str, record_from: int = 2005, elo_variants=ELO_VARIANTS,
           gen2_variants=None, progress: bool = False) -> tuple[pd.DataFrame, dict]:
    """Returns (records, end_states). `matches` is the canonical table (all tours)."""
    gen2_variants = gen2_variants or GEN2_VARIANTS
    m = prepare(matches, tour)
    elos = {c.name: EloV2(c) for c in elo_variants}
    ref = elos[REFERENCE_ELO]
    g2s = {k: Gen2State(cfg=c) for k, c in gen2_variants.items()}
    sr = ServeReturnModel(SRConfig())
    form = FormState()
    ctx = ContextState()

    cols: dict = {k: [] for k in ("uid", "date", "season", "tourney_id", "tourney_name", "level", "surface",
                                  "best_of", "round", "outcome", "source", "y", "a_id", "b_id", "games_a",
                                  "games_b", "sets_a", "sets_b", "score", "age_a", "age_b", "rank_a", "rank_b")}
    for v in elos:
        cols[f"p_{v}"] = []
    for k in g2s:
        for c in ("pa", "pb", "ev_a", "ev_b"):
            cols[f"{k}_{c}"] = []
    for c in ("sr_pa", "sr_pb", "sr_pts_a", "sr_pts_b", "spw", "n_a", "n_b"):
        cols[c] = []
    for side in ("a", "b"):
        for h in HORIZONS:
            cols[f"form{h}_{side}"] = []
            cols[f"cnt{h}_{side}"] = []
        for c in ("rest", "days", "n14", "mins7", "surf_switch", "ret30", "in_event"):
            cols[f"{c}_{side}"] = []

    recs = m.to_dict("records")
    n = len(recs)
    last_date = str(m.tourney_date.max()) if n else None
    del m
    for i, row in enumerate(recs):
        w, l = row["winner_id"], row["loser_id"]
        date = row["tourney_date"]
        level = row.get("level_canonical") or "OTHER"
        surface = row.get("surface") if isinstance(row.get("surface"), str) else None
        season = date.year
        tkey = f"{row.get('tourney_id')}|{date.isocalendar()[0]}"
        outcome = row.get("outcome_type")
        retired = outcome in ("RETIRED", "DEFAULT")
        # Gen-1 decays a player's evidence before every prediction (as in ServeReturnModel.run)
        sr._decay(w, date)
        sr._decay(l, date)
        if season >= record_from:
            uid = f"{row.get('source_label')}|{row.get('match_key')}|{date}|{w}|{l}"
            a_win = orient(uid)
            a, b = (w, l) if a_win else (l, w)
            ga, gb = (row.get("games_w"), row.get("games_l")) if a_win else (row.get("games_l"), row.get("games_w"))
            sa, sb = (row.get("sets_w"), row.get("sets_l")) if a_win else (row.get("sets_l"), row.get("sets_w"))
            age_a, age_b = (row.get("winner_age"), row.get("loser_age")) if a_win else (row.get("loser_age"), row.get("winner_age"))
            rk_a, rk_b = (row.get("winner_rank"), row.get("loser_rank")) if a_win else (row.get("loser_rank"), row.get("winner_rank"))
            for k, v in (("uid", uid), ("date", date), ("season", season), ("tourney_id", row.get("tourney_id")),
                         ("tourney_name", row.get("tourney_name")), ("level", level), ("surface", surface),
                         ("best_of", int(_f(row.get("best_of")) or 3)), ("round", row.get("round")),
                         ("outcome", outcome), ("source", row.get("source_label")), ("y", 1.0 if a_win else 0.0),
                         ("a_id", a), ("b_id", b), ("games_a", _f(ga)), ("games_b", _f(gb)), ("sets_a", _f(sa)),
                         ("sets_b", _f(sb)), ("score", row.get("score_raw")), ("age_a", _f(age_a)), ("age_b", _f(age_b)),
                         ("rank_a", _f(rk_a)), ("rank_b", _f(rk_b))):
                cols[k].append(v)
            for name, e in elos.items():
                cols[f"p_{name}"].append(e.predict(a, b, surface, level))
            for k, g in g2s.items():
                gpa, gpb = g.predict_point_probs(a, b, tour, level, surface)
                cols[f"{k}_pa"].append(gpa)
                cols[f"{k}_pb"].append(gpb)
                cols[f"{k}_ev_a"].append(g.evidence(a))
                cols[f"{k}_ev_b"].append(g.evidence(b))
            spa, spb = sr.predict(a, b, tour, surface)
            cols["sr_pa"].append(spa)
            cols["sr_pb"].append(spb)
            cols["sr_pts_a"].append(sr.points_seen(a))
            cols["sr_pts_b"].append(sr.points_seen(b))
            cols["spw"].append(sr.baseline(tour, surface))
            cols["n_a"].append(ref.n.get(a, 0))
            cols["n_b"].append(ref.n.get(b, 0))
            for side, p in (("a", a), ("b", b)):
                fr = form.read(p, date)
                for h in HORIZONS:
                    cols[f"form{h}_{side}"].append(fr[f"form{h}"])
                    cols[f"cnt{h}_{side}"].append(fr[f"cnt{h}"])
                cx = ctx.read(p, date, surface, tkey)
                cols[f"rest_{side}"].append(rest_feature(cx["days"]))
                cols[f"days_{side}"].append(cx["days"] if cx["days"] is not None else np.nan)
                for c in ("n14", "mins7", "surf_switch", "ret30", "in_event"):
                    cols[f"{c}_{side}"].append(cx[c])

        # ------------------------------------------------------------------ updates (after recording)
        gw, gl = _f(row.get("games_w")), _f(row.get("games_l"))
        dom = (gw - gl) / (gw + gl) if (gw is not None and gl is not None and gw + gl > 0) else None
        p_ref_w = ref.predict(w, l, surface, level)
        for e in elos.values():
            e.update(w, l, surface, level, date, retired, dom)
        wt = 0.5 if retired else 1.0
        form.update(w, date, 1.0 - p_ref_w, wt)
        form.update(l, date, -(1.0 - p_ref_w), wt)
        mins = _f(row.get("minutes"))
        ctx.update(w, date, mins, surface, tkey, False)
        ctx.update(l, date, mins, surface, tkey, outcome == "RETIRED")
        sr.update(_Rec(row, w, l))
        wp, ww = serve_points(row, "w")
        lp, lw = serve_points(row, "l")
        if wp and lp:
            for g in g2s.values():
                g.observe(server=w, returner=l, points=wp, won=ww, tour=tour, level=level, surface=surface, date=date)
                g.observe(server=l, returner=w, points=lp, won=lw, tour=tour, level=level, surface=surface, date=date)
        if progress and (i + 1) % 200000 == 0:
            print(f"  {tour} {i + 1}/{n}", flush=True)

    df = pd.DataFrame(cols)
    states = {"elos": elos, "gen2": g2s, "sr": sr, "form": form, "ctx": ctx, "n_matches": n,
              "last_date": last_date}
    return df, states


class _Rec:
    """Attribute view the Gen-1 serve/return updater expects, with canonical ids substituted."""
    __slots__ = ("_row", "winner_id", "loser_id", "tour", "surface")

    def __init__(self, row, w, l):
        self._row = row
        self.winner_id, self.loser_id = w, l
        self.tour = row.get("tour")
        self.surface = row.get("surface")

    def __getattr__(self, k):
        return self._row.get(k)


# ---------------------------------------------------------------------------------------------- finalise
def _logit(p):
    p = np.clip(np.asarray(p, float), 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p))


def _sig(z):
    return 1.0 / (1.0 + np.exp(-z))


def finalise(df: pd.DataFrame, elo_names=None) -> pd.DataFrame:
    """Vectorised post-processing: format-adjust every lane, the incumbent ensemble, the fair_v1 blend."""
    out = df.copy()
    bo5 = (out["best_of"] == 5).to_numpy()
    spw = out["spw"].to_numpy()
    elo_names = elo_names or [c[2:] for c in out.columns if c.startswith("p_E")]
    for name in elo_names:
        p = out[f"p_{name}"].to_numpy().copy()
        if bo5.any():
            p[bo5] = vz.reformat_match_prob(p[bo5], 2 * spw[bo5], BO5)
        out[f"pf_{name}"] = p

    def mwp(pa, pb):
        r = vz.match_win_prob(pa, pb, TOUR_SINGLES_BO3)
        if bo5.any():
            r[bo5] = vz.match_win_prob(pa[bo5], pb[bo5], BO5)
        return r

    # Gen-1 structural and Gen-2 lanes
    out["pf_sr"] = mwp(out["sr_pa"].to_numpy(), out["sr_pb"].to_numpy())
    p_sr_bo3 = vz.match_win_prob(out["sr_pa"].to_numpy(), out["sr_pb"].to_numpy(), TOUR_SINGLES_BO3)
    out["p_sr_bo3"] = p_sr_bo3
    for k in ("g2", "g2s"):
        if f"{k}_pa" in out:
            out[f"pf_{k}"] = mwp(out[f"{k}_pa"].to_numpy(), out[f"{k}_pb"].to_numpy())

    # INCUMBENT: run_tennis.py's production rule, reproduced exactly (Elo E_prod + Gen-1 logit average when
    # both players have >= 1000 serve+return points, else Elo; best-of-3 basis, then the match format)
    pe = out["p_E_prod"].to_numpy()
    sr_ok = np.minimum(out["sr_pts_a"].to_numpy(), out["sr_pts_b"].to_numpy()) >= 1000
    ens = np.where(sr_ok, _sig(0.5 * _logit(pe) + 0.5 * _logit(p_sr_bo3)), pe)
    pin = ens.copy()
    if bo5.any():
        pin[bo5] = vz.reformat_match_prob(ens[bo5], 2 * spw[bo5], BO5)
    out["pf_incumbent"] = pin
    out["incumbent_sr_used"] = sr_ok

    # fair_v1 / Model 3 base configuration: Gen-2 point probabilities shrunk toward the incumbent Elo's
    # implied point probabilities by the THINNER player's serve evidence (w = ev_min / (ev_min + 1500))
    gpa, gpb = out["g2_pa"].to_numpy(), out["g2_pb"].to_numpy()
    ev_min = np.minimum(out["g2_ev_a"].to_numpy(), out["g2_ev_b"].to_numpy())
    wgt = ev_min / (ev_min + 1500.0)
    base_spw = 0.5 * (gpa + (1 - gpb))
    epa, epb = vz.point_probs_from_match_prob(pe, 2 * base_spw, TOUR_SINGLES_BO3)
    out["pf_fair_v1"] = mwp(wgt * gpa + (1 - wgt) * epa, wgt * gpb + (1 - wgt) * epb)
    out["g2_ev_min"] = ev_min
    return out
