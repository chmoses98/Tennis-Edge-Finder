"""MODEL 4 -- market-conditioned match distribution. This lane USES market prices, by design and by name.

The hypothesis
--------------
The market may know who wins better than we do, while our structural model may describe HOW the match
unfolds better than the market does. Fighting the market's 64% is then a bad trade; accepting it and
re-deriving everything else from it may be a good one.

The decomposition
-----------------
A match distribution built from point probabilities has two independent degrees of freedom:

    DIFFERENCE   who is better, which fixes the match-winner probability
    LEVEL        how server-dominated the match is (both hold rates high, or both low), which fixes how
                 long it runs, how often it reaches a tiebreak and how the games spread

The market prices the winner, so it speaks to the DIFFERENCE. It says almost nothing about the LEVEL
unless a total-games market exists, and on Kalshi tennis those are nearly absent. The structural model
knows the level from serve and return statistics and has no special claim on the difference.

So this lane takes the LEVEL from the fundamental model and the DIFFERENCE from the market: hold the
total service level fixed and solve for the point probabilities that reproduce the market's winner
probability exactly. Every derivative is then read off ONE coherent distribution, exactly as in the pure
fundamental lane, so the internal consistency invariants still hold.

Boundaries this lane must respect
---------------------------------
* It is never called Model 3 and never feeds Model 3. `tests/test_gen2.py` asserts the fundamental model
  imports nothing that touches prices.
* It cannot beat the market at picking winners: by construction its winner probability IS the market's.
  Any value it has lives entirely in the derivatives.
* A market probability must be de-vigged before it arrives here; a raw two-sided quote sums above one and
  would silently import the spread into the distribution.
"""
from __future__ import annotations

from dataclasses import dataclass

from tennis_edge.rules.formats import MatchFormat, TOUR_SINGLES_BO3
from tennis_edge.sim.analytic import MatchDistribution, match_distribution, point_probs_from_match_prob

MODEL_VERSION = "market_conditioned_v1"


@dataclass(frozen=True)
class Conditioned:
    pa: float                 # P(A wins a point on A's serve)
    pb: float                 # P(A wins a point on B's serve)
    service_level: float      # pa + (1 - pb): the level taken from the fundamental model
    p_market: float           # the winner probability the distribution reproduces
    source: str = MODEL_VERSION


def service_level(pa_fund: float, pb_fund: float) -> float:
    """Total service dominance implied by the fundamental point probabilities.

    pa is A's hold-point rate; (1 - pb) is B's. Their sum is the quantity the market cannot see and the
    structural model can.
    """
    return pa_fund + (1.0 - pb_fund)


def condition(p_market: float, pa_fund: float, pb_fund: float,
              fmt: MatchFormat = TOUR_SINGLES_BO3) -> Conditioned:
    """Point probabilities that keep the fundamental service level and hit the market's winner price."""
    lvl = service_level(pa_fund, pb_fund)
    lvl = min(max(lvl, 0.6), 1.9)                 # keep the inversion inside a sane, solvable band
    pa, pb = point_probs_from_match_prob(min(max(p_market, 1e-4), 1 - 1e-4), lvl, fmt)
    return Conditioned(pa=pa, pb=pb, service_level=lvl, p_market=p_market)


def conditioned_distribution(p_market: float, pa_fund: float, pb_fund: float,
                             fmt: MatchFormat = TOUR_SINGLES_BO3) -> tuple[MatchDistribution, Conditioned]:
    c = condition(p_market, pa_fund, pb_fund, fmt)
    return match_distribution(c.pa, c.pb, fmt), c


def remove_vig_two_sided(yes_a: float, yes_b: float, method: str = "proportional") -> tuple[float, float]:
    """Turn a two-sided quote into probabilities that sum to one.

    Passing a raw quote into `condition` would import the spread into the distribution, which is how a
    two-cent market edge becomes a fake half-game shift in the total.
    """
    s = yes_a + yes_b
    if s <= 0:
        raise ValueError("two-sided quote must be positive")
    if method != "proportional":
        raise ValueError(f"unsupported vig method {method!r}")
    return yes_a / s, yes_b / s
