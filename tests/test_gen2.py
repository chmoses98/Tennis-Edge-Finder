"""Model-lane discipline and Gen-2 behaviour.

The first test is the important one: Model 3 must not be able to see a price, and that is checked by
walking the import graph rather than by trusting a docstring.
"""
import ast
import os
import sys
from datetime import date, timedelta

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

from tennis_edge.models.gen2 import Gen2Config, Gen2State, logit, serve_points   # noqa: E402
from tennis_edge.models.market_conditioned import (condition, conditioned_distribution,   # noqa: E402
                                                   remove_vig_two_sided, service_level)
from tennis_edge.sim.analytic import match_distribution                          # noqa: E402

#: anything that reads, parses or carries an exchange price
PRICE_BEARING = ("tennis_edge.kalshi", "tennis_edge.pricing.coherence", "tennis_edge.ledger.close",
                 "tennis_edge.ledger.clv", "tennis_edge.ledger.quotes",
                 "tennis_edge.models.market_conditioned")


def _imports_of(module_path):
    tree = ast.parse(open(module_path).read())
    out = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            out.update(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            out.add(node.module)
    return out


def _transitive(module: str, seen=None):
    seen = seen if seen is not None else set()
    if module in seen or not module.startswith("tennis_edge"):
        return seen
    seen.add(module)
    path = os.path.join(ROOT, *module.split(".")) + ".py"
    if not os.path.exists(path):
        return seen
    for imp in _imports_of(path):
        _transitive(imp, seen)
    return seen


def test_model_3_cannot_see_a_price():
    """MODEL 3 is the fundamental lane. If it ever imports the price surface, the whole comparison
    against the market becomes circular and every result in the wave is worthless."""
    reached = _transitive("tennis_edge.models.gen2")
    leaks = sorted(m for m in reached if any(m.startswith(p) for p in PRICE_BEARING))
    assert leaks == [], f"Model 3 reaches price-bearing modules: {leaks}"


def test_model_4_does_see_the_market_and_says_so():
    reached = _transitive("tennis_edge.models.market_conditioned")
    assert "tennis_edge.sim.analytic" in reached
    src = open(os.path.join(ROOT, "tennis_edge", "models", "market_conditioned.py")).read()
    assert "MODEL 4" in src and "USES market prices" in src


def test_point_probability_convention_matches_the_scoring_engine():
    """pb is P(A wins a point on B's serve). Returning P(B holds) instead prices every match at ~0.99."""
    st = Gen2State(Gen2Config())
    d = date(2026, 1, 1)
    for i in range(40):                      # A serves a little better than B; a realistic gap
        st.observe(server="A", returner="B", points=80, won=53, tour="ATP", level="TOUR_500_250",
                   surface="Hard", date=d + timedelta(days=i))
        st.observe(server="B", returner="A", points=80, won=49, tour="ATP", level="TOUR_500_250",
                   surface="Hard", date=d + timedelta(days=i))
    pa, pb = st.predict_point_probs("A", "B", "ATP", "TOUR_500_250", "Hard")
    assert 0.5 < pa < 0.9, pa
    assert 0.2 < pb < 0.6, pb                 # A wins SOME points on B's serve, not almost all
    p = match_distribution(pa, pb).p_match
    assert 0.55 < p < 0.99, p                 # a favourite, not a certainty
    # the wrong convention (returning P(B holds) as pb) prices this same matchup at essentially 1.0
    wrong = match_distribution(pa, 1.0 - pb).p_match
    assert wrong > 0.99 and wrong > p


def test_abilities_do_not_decay_to_the_baseline_under_repeated_evidence():
    """The estimator is a precision-weighted MEAN of opponent-adjusted excess, not an innovation filter.

    Accumulating residuals instead makes the numerator stop growing while the denominator keeps growing,
    so every player drifts back to the baseline and the model predicts 0.50 for everything.
    """
    st = Gen2State(Gen2Config())
    d = date(2026, 1, 1)
    seen = []
    for i in range(120):
        st.observe(server="A", returner="B", points=80, won=64, tour="ATP", level="TOUR_500_250",
                   surface="Hard", date=d + timedelta(days=i))
        st.observe(server="B", returner="A", points=80, won=48, tour="ATP", level="TOUR_500_250",
                   surface="Hard", date=d + timedelta(days=i))
        if i % 30 == 29:
            seen.append(st.ability("A", "Hard")[0])
    assert seen[-1] > 0.02, seen
    assert seen[-1] >= seen[0] * 0.8, f"ability decayed toward the baseline: {seen}"


def test_thin_players_are_shrunk_and_evidence_is_reported():
    st = Gen2State(Gen2Config())
    st.observe(server="A", returner="B", points=40, won=32, tour="ATP", level="ITF", surface="Clay",
               date=date(2026, 1, 1))
    s, r, ev = st.ability("A", "Clay")
    raw_excess = logit(32 / 40) - st.baseline("ATP")
    assert ev == 40
    # 40 points against a 500-point prior must move the ability to a small fraction of the raw excess
    assert 0 < s < 0.25 * raw_excess, (s, raw_excess)


def test_market_conditioning_reproduces_the_market_and_keeps_the_service_level():
    pa_f, pb_f = 0.66, 0.38
    lvl = service_level(pa_f, pb_f)
    d, c = conditioned_distribution(0.64, pa_f, pb_f)
    assert abs(d.p_match - 0.64) < 5e-3
    assert abs(c.service_level - lvl) < 1e-9
    # and it must actually move the derivatives relative to the fundamental distribution
    d_f = match_distribution(pa_f, pb_f)
    assert abs(sum(k * v for k, v in d.total_games.items()) -
               sum(k * v for k, v in d_f.total_games.items())) > 1e-3


def test_vig_must_be_removed_before_conditioning():
    a, b = remove_vig_two_sided(0.66, 0.38)
    assert abs(a + b - 1.0) < 1e-12
    with pytest.raises(ValueError):
        remove_vig_two_sided(0.0, 0.0)


def test_serve_points_rejects_impossible_rows():
    assert serve_points({"w_svpt": 0, "w_1stWon": 0, "w_2ndWon": 0}, "w") == (None, None)
    assert serve_points({"w_svpt": 50, "w_1stWon": 40, "w_2ndWon": 30}, "w") == (None, None)   # won > played
    assert serve_points({"w_svpt": 50, "w_1stWon": 20, "w_2ndWon": 10}, "w") == (50.0, 30.0)
