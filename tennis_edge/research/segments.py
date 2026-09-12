"""Research segments, PRE-REGISTERED before any profitability was examined.

The rule this file exists to enforce: a bucket defined after looking at results is a DISCOVERY, not a
confirmation. Both are useful; conflating them is how a research programme convinces itself of an edge
that is really a lucky slice. So the buckets live here, in code, fixed before the numbers were read, and
anything added later is marked with the date it was added and can only ever produce a discovery-stage
hypothesis.
"""
from __future__ import annotations

PREREGISTERED_AT = "2026-09-12"

TOUR = ("ATP", "WTA", "CHALLENGER", "ITF_M", "ITF_W", "WTA_125")
SURFACE = ("Hard", "Clay", "Grass", "Carpet", "UNKNOWN")
MARKET_FAMILY = ("MATCH_WINNER", "SET_WINNER", "EXACT_SET_SCORE", "TOTAL_GAMES", "GAME_SPREAD",
                 "TOTAL_SETS", "SET_SPREAD", "TIEBREAK_OCCURS", "ANY_SET_WINNER")

FAVOURITE_PROB = ((0.0, 0.55, "toss-up"), (0.55, 0.65, "55-65"), (0.65, 0.75, "65-75"),
                  (0.75, 0.85, "75-85"), (0.85, 1.01, "85+"))
DISAGREEMENT_PP = ((0.0, 2.5, "0-2.5pp"), (2.5, 5.0, "2.5-5pp"), (5.0, 10.0, "5-10pp"),
                   (10.0, 15.0, "10-15pp"), (15.0, 20.0, "15-20pp"), (20.0, 1e9, "20pp+"))
LIQUIDITY = ((0, 10, "<=10"), (10, 100, "<=100"), (100, 1000, "<=1000"), (1000, 1e12, ">1000"))
SPREAD_WIDTH = ((0.0, 0.02, "<=2c"), (0.02, 0.05, "<=5c"), (0.05, 0.10, "<=10c"), (0.10, 1.0, ">10c"))
TIME_TO_FIRST_BALL = ((0, 900, "<=15m"), (900, 3600, "<=1h"), (3600, 10800, "<=3h"),
                      (10800, 21600, "<=6h"), (21600, 1e9, ">6h"))
DATA_QUALITY = ("A", "B", "C", "D")
MODEL_UNCERTAINTY = ((0, 1000, "thin"), (1000, 5000, "medium"), (5000, 1e12, "rich"))
SIDE = ("FAVOURITE", "UNDERDOG")
DERIVATIVE_POSITION = ("CENTRAL", "TAIL")

#: every pre-registered dimension, by name, so a scorecard cannot quietly gain one
DIMENSIONS = ("tour", "surface", "market_family", "favourite_prob", "disagreement_pp", "liquidity",
              "spread_width", "time_to_first_ball", "data_quality", "model_uncertainty", "side",
              "derivative_position")

#: dimensions added AFTER results were first examined. Empty at pre-registration. Anything listed here
#: may only support a DISCOVERY_ONLY hypothesis, never a confirmation.
POST_HOC_DIMENSIONS: dict[str, str] = {}


def bucket(value, table, none_label: str = "UNKNOWN") -> str:
    if value is None:
        return none_label
    try:
        v = float(value)
    except (TypeError, ValueError):
        return none_label
    for lo, hi, label in table:
        if lo <= v < hi:
            return label
    return none_label


def is_preregistered(dimension: str) -> bool:
    return dimension in DIMENSIONS and dimension not in POST_HOC_DIMENSIONS
