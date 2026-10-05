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


@pytest.mark.parametrize("fmt", FORMATS, ids=lambda f: f.name)
def test_match_win_prob_matches_scalar_engine(fmt):
    rng = np.random.default_rng(7)
    pa = rng.uniform(0.45, 0.80, 25)
    pb = rng.uniform(0.20, 0.55, 25)
    vec = vz.match_win_prob(pa, pb, fmt)
    ref = np.array([analytic.match_win_prob(a, b, fmt) for a, b in zip(pa, pb)])
    tol = 1e-6 if fmt.final_set == "ADVANTAGE" else 1e-9    # scalar engine truncates the advantage tail
    assert np.max(np.abs(vec - ref)) < tol


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
