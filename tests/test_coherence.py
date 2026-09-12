"""Cross-market coherence: what counts as an opportunity, and what must never count as one."""
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tennis_edge.pricing.coherence import (COMPOSITE_OVERPRICED, COMPOSITE_UNDERPRICED, LADDER_INVERSION,
                                           PARTITION_OVERPRICED, PARTITION_UNDERPRICED, Contract,
                                           check_composite, check_ladder, check_partition, scan_match)

TS = datetime(2026, 9, 12, tzinfo=timezone.utc)


def c(tk, fam, bid, ask, size=100, **kw):
    return Contract(tk, fam, bid, ask, yes_bid_size=size, yes_ask_size=size, ts=TS, **kw)


def test_partition_underpriced_is_found_only_when_it_clears_fees():
    wide = [c("A", "MATCH_WINNER", 0.48, 0.50, subject_is_a=True), c("B", "MATCH_WINNER", 0.33, 0.35, subject_is_a=False)]
    got = scan_match(wide, "m")
    assert [o.kind for o in got] == [PARTITION_UNDERPRICED]
    assert got[0].worst_case_payoff == 1.0 and got[0].executable_margin > 0
    # the same shape with a three-cent gap does NOT clear Kalshi's taker fee on two legs
    tight = [c("A", "MATCH_WINNER", 0.55, 0.57, subject_is_a=True), c("B", "MATCH_WINNER", 0.38, 0.40, subject_is_a=False)]
    assert scan_match(tight, "m") == []


def test_partition_overpriced_sells_both_sides():
    over = [c("A", "MATCH_WINNER", 0.70, 0.72, subject_is_a=True), c("B", "MATCH_WINNER", 0.60, 0.62, subject_is_a=False)]
    got = [o for o in scan_match(over, "m") if o.kind == PARTITION_OVERPRICED]
    assert got and all(l["side"] == "BUY_NO" for l in got[0].legs)
    assert got[0].worst_case_payoff == 1.0            # n - 1 with n = 2


def test_ladder_direction_lower_strike_is_the_wider_event():
    """Every Kalshi tennis ladder is 'above <line>', so probability falls as the strike rises."""
    inverted = [c("T215", "TOTAL_GAMES", 0.60, 0.62, line=21.5, subject_is_a=True),
                c("T225", "TOTAL_GAMES", 0.70, 0.72, line=22.5, subject_is_a=True)]
    got = scan_match(inverted, "m")
    assert [o.kind for o in got] == [LADDER_INVERSION]
    assert got[0].legs[0]["ticker"] == "T215" and got[0].legs[0]["side"] == "BUY_YES"
    assert got[0].legs[1]["ticker"] == "T225" and got[0].legs[1]["side"] == "BUY_NO"
    # the coherent ladder must be silent; getting the direction backwards would flag every one of them
    coherent = [c("T215", "TOTAL_GAMES", 0.70, 0.72, line=21.5, subject_is_a=True),
                c("T225", "TOTAL_GAMES", 0.58, 0.60, line=22.5, subject_is_a=True)]
    assert scan_match(coherent, "m") == []


def test_composite_exact_scores_add_up_to_the_match_winner():
    whole = c("MW_A", "MATCH_WINNER", 0.70, 0.72, subject_is_a=True)
    parts = [c("S20", "EXACT_SET_SCORE", 0.20, 0.21, subject_is_a=True, exact_score="2-0"),
             c("S21", "EXACT_SET_SCORE", 0.20, 0.21, subject_is_a=True, exact_score="2-1")]
    got = check_composite(parts, whole, "m", "EXACT/MW")
    assert [o.kind for o in got] == [COMPOSITE_UNDERPRICED]
    assert got[0].worst_case_payoff == 1.0
    rich = [c("S20", "EXACT_SET_SCORE", 0.45, 0.46, subject_is_a=True, exact_score="2-0"),
            c("S21", "EXACT_SET_SCORE", 0.45, 0.46, subject_is_a=True, exact_score="2-1")]
    got = check_composite(rich, c("MW_A", "MATCH_WINNER", 0.70, 0.72, subject_is_a=True), "m", "EXACT/MW")
    assert [o.kind for o in got] == [COMPOSITE_OVERPRICED]


def test_size_is_the_minimum_across_legs_and_zero_size_is_no_opportunity():
    legs = [c("A", "MATCH_WINNER", 0.48, 0.50, size=7, subject_is_a=True),
            c("B", "MATCH_WINNER", 0.33, 0.35, size=200, subject_is_a=False)]
    got = scan_match(legs, "m")
    assert got[0].size == 7
    assert abs(got[0].total_executable_profit - got[0].executable_margin * 7) < 1e-9
    nosize = [c("A", "MATCH_WINNER", 0.48, 0.50, size=0, subject_is_a=True),
              c("B", "MATCH_WINNER", 0.33, 0.35, size=0, subject_is_a=False)]
    assert scan_match(nosize, "m") == []


def test_one_sided_or_crossed_quotes_are_never_executable():
    assert scan_match([Contract("A", "MATCH_WINNER", None, 0.50, 10, 10, subject_is_a=True, ts=TS),
                       c("B", "MATCH_WINNER", 0.33, 0.35, subject_is_a=False)], "m") == []
    assert scan_match([Contract("A", "MATCH_WINNER", 0.60, 0.50, 10, 10, subject_is_a=True, ts=TS),
                       c("B", "MATCH_WINNER", 0.33, 0.35, subject_is_a=False)], "m") == []


def test_margin_never_uses_the_midpoint():
    """A board that looks free at midpoints but is not tradeable at bid/ask must produce nothing."""
    mids_look_free = [c("A", "MATCH_WINNER", 0.40, 0.56, subject_is_a=True),
                      c("B", "MATCH_WINNER", 0.36, 0.52, subject_is_a=False)]
    assert (0.48 + 0.44) < 1.0                                   # midpoints sum to 0.92
    assert scan_match(mids_look_free, "m") == []                 # asks sum to 1.08


def test_match_winner_implies_winning_a_set():
    mw = c("MW_A", "MATCH_WINNER", 0.70, 0.72, subject_is_a=True)
    anyset = c("ANY_A", "ANY_SET_WINNER", 0.50, 0.52, subject_is_a=True)   # cannot be below the match price
    got = [o for o in scan_match([mw, anyset], "m") if o.family == "ANY_SET_WINNER/MATCH_WINNER"]
    assert got and got[0].legs[0]["ticker"] == "ANY_A"
