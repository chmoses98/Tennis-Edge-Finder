"""Projection V2 invariants: incumbent reproduction, no lookahead, no market inputs, A/B symmetry, form signs."""
import glob
import os
import sys
from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from tennis_edge.models.elo import Elo                                     # noqa: E402
from tennis_edge.models.state import PROD_ELO                              # noqa: E402
from tennis_edge.v2.elo import EloV2, EloV2Config                          # noqa: E402
from tennis_edge.v2.form import ContextState, FormState                    # noqa: E402
from tennis_edge.v2.replay import INCUMBENT_ELO, finalise, replay          # noqa: E402
from tennis_edge.v2.stacker import StackerSpec, build_features, fit        # noqa: E402
from tests.test_gen2 import PRICE_BEARING, _transitive                     # noqa: E402

PLAYERS = [f"p{i}" for i in range(14)]


def synthetic(n=900, seed=3, tour="ATP"):
    """A small canonical-shaped table: latent strengths, serve stats, several levels and surfaces."""
    rng = np.random.default_rng(seed)
    skill = {p: rng.normal(0, 1) for p in PLAYERS}
    rows = []
    d0 = date(2015, 1, 5)
    for i in range(n):
        a, b = rng.choice(PLAYERS, 2, replace=False)
        pa = 1 / (1 + np.exp(-(skill[a] - skill[b])))
        w, l = (a, b) if rng.random() < pa else (b, a)
        svw, svl = int(rng.integers(50, 90)), int(rng.integers(50, 90))
        gw, gl = int(rng.integers(12, 19)), int(rng.integers(3, 12))
        rows.append({"tour": tour, "outcome_type": "RETIRED" if i % 37 == 0 else "COMPLETED",
                     "tourney_date": d0 + timedelta(days=7 * (i // 30)), "canonical_id_status": "MAPPED",
                     "canonical_winner_id": w, "canonical_loser_id": l, "id_system": "sackmann", "winner_id": w,
                     "loser_id": l, "match_key": f"{tour}:t{i // 30}:{i}", "source_label": "synthetic",
                     "tourney_id": f"t{i // 30}", "tourney_name": f"T{i // 30}",
                     "level_canonical": ["ITF", "CHALLENGER", "TOUR_500_250", "GRAND_SLAM"][(i // 30) % 4],
                     "surface": ["Hard", "Clay", "Grass"][(i // 30) % 3], "best_of": 5 if (i // 30) % 4 == 3 else 3,
                     "round": "R32", "match_num": i, "games_w": gw, "games_l": gl, "sets_w": 2, "sets_l": 0,
                     "score_raw": "6-3 6-4", "winner_age": 24.0, "loser_age": 27.0, "winner_rank": 10, "loser_rank": 20,
                     "minutes": 90.0, "w_svpt": svw, "w_1stWon": int(svw * .5), "w_2ndWon": int(svw * .2),
                     "l_svpt": svl, "l_1stWon": int(svl * .45), "l_2ndWon": int(svl * .15)})
    return pd.DataFrame(rows)


def test_incumbent_replica_reproduces_gen1_elo():
    m = synthetic()
    from tennis_edge.v2.replay import prepare
    sub = prepare(m, "ATP")
    ref = Elo(PROD_ELO).run(sub)["p_winner"].to_numpy()
    e = EloV2(INCUMBENT_ELO)
    got = []
    for r in sub.to_dict("records"):
        got.append(e.predict(r["winner_id"], r["loser_id"], r["surface"], r["level_canonical"]))
        e.update(r["winner_id"], r["loser_id"], r["surface"], r["level_canonical"], r["tourney_date"],
                 r["outcome_type"] in ("RETIRED", "DEFAULT"), None)
    assert np.max(np.abs(np.array(got) - ref)) == 0.0


def test_no_lookahead_future_rows_cannot_change_past_records():
    """Rewriting every result AFTER a cut-off must leave every record before the cut-off identical."""
    m = synthetic()
    cut = m["tourney_date"].iloc[600]
    m2 = m.copy()
    fut = m2["tourney_date"] > cut
    m2.loc[fut, ["canonical_winner_id", "canonical_loser_id"]] = m2.loc[fut, ["canonical_loser_id", "canonical_winner_id"]].to_numpy()
    m2.loc[fut, ["w_svpt", "l_svpt"]] = 40
    r1, _ = replay(m, "ATP", record_from=2015)
    r2, _ = replay(m2, "ATP", record_from=2015)
    early = r1["date"] <= cut
    num = [c for c in r1.columns if r1[c].dtype.kind == "f" and c != "y"]
    pd.testing.assert_frame_equal(r1.loc[early, num].reset_index(drop=True), r2.loc[early, num].reset_index(drop=True))


def test_same_match_result_not_visible_to_its_own_prediction():
    """Flipping one match's result must not change that match's own recorded probabilities."""
    m = synthetic()
    m2 = m.copy()
    i = 500
    m2.loc[i, ["canonical_winner_id", "canonical_loser_id"]] = m2.loc[i, ["canonical_loser_id", "canonical_winner_id"]].to_numpy()
    r1, _ = replay(m, "ATP", record_from=2015)
    r2, _ = replay(m2, "ATP", record_from=2015)
    key = m.loc[i, "match_key"]
    a = r1[r1.uid.str.contains(f"|{key}|", regex=False)]
    b = r2[r2.uid.str.contains(f"|{key}|", regex=False)]
    # orientation can differ (uid contains winner/loser); compare the probability that the SAME player wins
    pa = a["p_E_lp"].iloc[0] if a["a_id"].iloc[0] == b["a_id"].iloc[0] else 1 - a["p_E_lp"].iloc[0]
    assert abs(pa - b["p_E_lp"].iloc[0]) < 1e-12


def test_v2_package_cannot_reach_a_price():
    leaks = set()
    for path in glob.glob(os.path.join(ROOT, "tennis_edge", "v2", "*.py")):
        mod = "tennis_edge.v2." + os.path.basename(path)[:-3]
        reached = _transitive(mod)
        leaks |= {x for x in reached if any(x.startswith(p) for p in PRICE_BEARING)}
    assert leaks == set(), f"V2 reaches price-bearing modules: {sorted(leaks)}"


def test_stacker_is_exactly_symmetric_in_players():
    m = synthetic(n=1200)
    df, _ = replay(m, "ATP", record_from=2015)
    df = finalise(df)
    df["season"] = np.where(np.arange(len(df)) < 700, 2015, 2016)
    spec = StackerSpec(elo="E_lp", blocks=("level", "exp", "g2", "form", "context", "age"), form_horizon=60)
    f = fit(df[df.season == 2015], spec)
    test = df[df.season == 2016].reset_index(drop=True)
    swapped = test.copy()
    for c in list(test.columns):
        if c.endswith("_a"):
            o = c[:-2] + "_b"
            swapped[c], swapped[o] = test[o], test[c]
    for c in [c for c in test.columns if c.startswith("pf_")]:
        swapped[c] = 1 - test[c]
    for k in ("g2", "g2s"):
        pass
    # Gen-2 / Gen-1 evidence minima are symmetric already; the probabilities were flipped above
    p = f.predict(test)
    q = f.predict(swapped)
    assert np.max(np.abs(p + q - 1)) < 1e-12


def test_form_is_opponent_adjusted_and_signed():
    fs = FormState()
    d = date(2024, 1, 1)
    fs.update("x", d, residual=1 - 0.2)   # beat a much stronger opponent
    fs.update("y", d, residual=1 - 0.95)  # beat a much weaker opponent
    fs.update("z", d, residual=-(1 - 0.95))  # lost to a much weaker opponent... (residual of the loser)
    rx, ry = fs.read("x", d + timedelta(days=1))["form60"], fs.read("y", d + timedelta(days=1))["form60"]
    assert rx > ry > 0
    assert fs.read("z", d)["form60"] < 0
    # decays with the horizon's half-life
    assert abs(fs.read("x", d + timedelta(days=60))["form60"] - 0.8 * 0.5) < 1e-12


def test_context_counts_only_prior_matches():
    cs = ContextState()
    d = date(2024, 3, 1)
    cs.update("p", d, 120.0, "Clay", "t1|2024", retired_loser=True)
    r = cs.read("p", d + timedelta(days=3), "Hard", "t2|2024")
    assert r["days"] == 3 and r["n14"] == 1 and r["mins7"] == 120.0 and r["ret30"] == 1.0 and r["surf_switch"] == 1.0
    assert r["in_event"] == 0.0
    assert cs.read("p", d + timedelta(days=40), "Clay", "t3|2024")["ret30"] == 0.0


def test_margin_of_victory_moves_more_for_a_rout():
    c = EloV2Config(name="m", mov_a=0.6, mov_b=1.6)
    e1, e2 = EloV2(c), EloV2(c)
    e1.update("a", "b", None, "ITF", date(2024, 1, 1), False, dominance=0.9)
    e2.update("a", "b", None, "ITF", date(2024, 1, 1), False, dominance=0.05)
    assert e1.r["a"] - e2.r["a"] > 0
