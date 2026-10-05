"""The vectorised engine must reproduce the scalar exact engine; it is a speed-up, never a second model."""
import numpy as np
import pytest

from tennis_edge.rules.formats import MatchFormat, TOUR_SINGLES_BO3
from tennis_edge.sim import analytic, vectorized as vz

FORMATS = [
    TOUR_SINGLES_BO3,
    MatchFormat(best_of=5, final_set="TB10_AT_6", name="slam_bo5_tb10"),
    MatchFormat(best_of=5, final_set="ADVANTAGE", name="bo5_adv"),
    MatchFormat(best_of=3, final_set="MATCH_TB10", no_ad=True, name="doubles"),
    MatchFormat(best_of=3, final_set="TB10_AT_6", name="bo3_tb10"),
    MatchFormat(best_of=5, final_set="TB7_AT_12", name="wimbledon_2019"),
]


@pytest.mark.parametrize("fmt", [f for f in FORMATS if f.final_set != "ADVANTAGE"], ids=lambda f: f.name)
def test_match_win_prob_matches_scalar_engine(fmt):
    rng = np.random.default_rng(7)
    pa = rng.uniform(0.45, 0.80, 25)
    pb = rng.uniform(0.20, 0.55, 25)
    vec = vz.match_win_prob(pa, pb, fmt)
    ref = np.array([analytic.match_win_prob(a, b, fmt) for a, b in zip(pa, pb)])
    assert np.max(np.abs(vec - ref)) < 1e-9


def test_advantage_set_is_exact_against_a_long_tail_reference():
    """Advantage final sets: the FROZEN scalar engine truncates the tail at 40-40 and splits the residual with
    1 - P(break) where P(break) belongs. With two big servers ~6% of the mass reaches 40-40, so its
    match_win_prob is off by up to ~0.014 for ADVANTAGE formats (all of which ended in 2021 -- no live format
    is affected). analytic.py is a frozen source of the prospective experiments and is NOT edited; the
    reference here is the same scalar set DP run with a 400-game tail, where the residual is negligible."""
    rng = np.random.default_rng(7)
    for a, b in zip(rng.uniform(0.55, 0.80, 15), rng.uniform(0.20, 0.45, 15)):
        for first in (True, False):
            d = analytic.set_distribution(a, b, None, 0, False, first, max_adv_games=400)
            ref = sum(v for (x, y), v in d.items() if x > y)
            o = vz._set_outcomes(np.array([a]), np.array([b]), None, 0, False, first)
            got = float(np.asarray(o[(True, True)] + o[(True, False)]).ravel()[0])
            assert abs(got - ref) < 1e-9


def test_tiebreak_and_game_match_scalar():
    for pa, pb in ((0.62, 0.35), (0.7, 0.28), (0.55, 0.45)):
        for to in (7, 10):
            for first in (True, False):
                assert abs(float(vz.tiebreak_win_prob(np.array([pa]), np.array([pb]), to, first)[0])
                           - analytic.tiebreak_win_prob(pa, pb, to, first)) < 1e-12
        assert abs(float(vz.game_win_prob(np.array([pa]))[0]) - analytic.game_win_prob(pa)) < 1e-12


def test_inversion_round_trip_and_matches_scalar():
    target = np.array([0.2, 0.5, 0.73, 0.91])
    pa, pb = vz.point_probs_from_match_prob(target, 1.28)
    back = vz.match_win_prob(pa, pb)
    assert np.max(np.abs(back - target)) < 1e-9
    spa, spb = analytic.point_probs_from_match_prob(0.73, 1.28)
    assert abs(pa[2] - spa) < 1e-6 and abs(pb[2] - spb) < 1e-6


def test_symmetry_swapping_players():
    """P(A beats B) + P(B beats A) = 1 with B's pair written from B's perspective."""
    pa, pb = np.array([0.66, 0.6]), np.array([0.31, 0.42])
    for fmt in FORMATS[:3]:
        p_ab = vz.match_win_prob(pa, pb, fmt)
        p_ba = vz.match_win_prob(1 - pb, 1 - pa, fmt)
        assert np.max(np.abs(p_ab + p_ba - 1)) < 1e-9
