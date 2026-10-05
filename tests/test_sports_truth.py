"""Independent sports truth: resolved from non-Kalshi results, fail closed, never fooled by an adjacent meeting."""
from datetime import date

import pandas as pd

from tennis_edge.ledger.sports_truth import (AMBIGUOUS, NOT_COVERED, NOT_FOUND, RESOLVED, ResultsIndex,
                                              reconcile_match_winner, ticker_date)


def _m(rows):
    base = {"canonical_id_status": "MAPPED", "outcome_type": "COMPLETED", "score_raw": "6-4 6-4", "games_w": 12,
            "games_l": 8, "sets_w": 2, "sets_l": 0, "match_key": "k", "tourney_name": "T", "level_canonical": "CHALLENGER"}
    return pd.DataFrame([{**base, **r} for r in rows])


def test_ticker_date():
    assert ticker_date("KXWTACHALLENGERMATCH-26SEP29KOSCEN") == date(2026, 9, 29)
    assert ticker_date("garbage") is None


def test_adjacent_week_meeting_is_not_mistaken_for_this_match():
    """Production case: the pair met in the previous week's event (TML, dated 09-07); the Kalshi match on 09-15
    was a different meeting. The first, wide-window version reported a false 'conflict' here."""
    m = _m([{"tour": "ATP", "tourney_date": "2026-09-07", "canonical_winner_id": "b", "canonical_loser_id": "a",
             "source_label": "tml_ATP_challenger"},
            {"tour": "ATP", "tourney_date": "2026-09-30", "canonical_winner_id": "x", "canonical_loser_id": "y",
             "source_label": "tml_ATP_challenger"}])
    idx = ResultsIndex(m, since=date(2026, 8, 1))
    assert idx.resolve("ATP", "a", "b", "CHALLENGER", date(2026, 9, 15)).status == NOT_FOUND


def test_resolves_within_source_window_and_orientation():
    m = _m([{"tour": "WTA", "tourney_date": "2026-10-01", "canonical_winner_id": "a", "canonical_loser_id": "b",
             "source_label": "espn_WTA", "level_canonical": "TOUR_500_250"}])
    idx = ResultsIndex(m, since=date(2026, 8, 1))
    t = idx.resolve("WTA", "b", "a", "TOUR_500_250", date(2026, 9, 29))     # ESPN +2 (rain delay) is inside
    assert t.status == RESOLVED and t.winner_id == "a"
    assert reconcile_match_winner(t, {"result": "yes"}, "a")["status"] == "AGREE"
    assert reconcile_match_winner(t, {"result": "yes"}, "b")["status"] == "CONFLICT"


def test_two_meetings_in_window_is_ambiguous_and_uncovered_level_is_reported():
    # two events starting a day apart (a Monday and a Tuesday Challenger in the same week) both fit the window
    m = _m([{"tour": "ATP", "tourney_date": d, "canonical_winner_id": "a", "canonical_loser_id": "b",
             "source_label": "tml_ATP_challenger"} for d in ("2026-09-14", "2026-09-15")])
    idx = ResultsIndex(m, since=date(2026, 8, 1))
    assert idx.resolve("ATP", "a", "b", "CHALLENGER", date(2026, 9, 16)).status == AMBIGUOUS
    assert idx.resolve("ATP", "a", "c", "CHALLENGER", date(2026, 10, 3)).status == NOT_COVERED


def test_walkover_is_explained_not_a_conflict():
    m = _m([{"tour": "ATP", "tourney_date": "2026-09-28", "canonical_winner_id": "a", "canonical_loser_id": "b",
             "source_label": "espn_ATP", "outcome_type": "WALKOVER", "level_canonical": "TOUR_500_250"}])
    t = ResultsIndex(m, since=date(2026, 8, 1)).resolve("ATP", "a", "b", "TOUR_500_250", date(2026, 9, 28))
    assert reconcile_match_winner(t, {"result": "scalar"}, "a")["status"] == "AGREE"


def test_tour_market_is_not_settled_by_a_challenger_meeting_days_later():
    """Production case: KXATPMATCH-26SEP23 Tomic-Sun (tour qualifying, Sun won); TML has Tomic beating Sun at the
    Jingshan Challenger dated 2026-09-29. Same pair, inside the TML window, different match."""
    m = _m([{"tour": "ATP", "tourney_date": "2026-09-29", "canonical_winner_id": "tomic", "canonical_loser_id": "sun",
             "source_label": "tml_ATP_challenger", "level_canonical": "CHALLENGER"}])
    idx = ResultsIndex(m, since=date(2026, 8, 1))
    assert idx.resolve("ATP", "tomic", "sun", "TOUR_500_250", date(2026, 9, 23)).status != RESOLVED
    assert idx.resolve("ATP", "tomic", "sun", "CHALLENGER", date(2026, 9, 30)).status == RESOLVED


def test_previous_weeks_challenger_meeting_is_not_this_weeks_result():
    """Production case 2026-10-05: Alves beat Pereira at the Copa Internacional (TML, dated Monday 09-28); they met
    again in Antofagasta qualifying on 10-05 and Pereira won. The old (7, 8) window took the 09-28 result as truth
    for the 10-05 match: 6 false TENNIS-9 conflicts. Agreeing TML Challenger rows lie at -6..0 days."""
    m = _m([{"tour": "ATP", "tourney_date": "2026-09-28", "canonical_winner_id": "alves", "canonical_loser_id": "pereira",
             "source_label": "tml_ATP_challenger"}])
    idx = ResultsIndex(m, since=date(2026, 8, 1))
    assert idx.resolve("ATP", "alves", "pereira", "CHALLENGER", date(2026, 10, 5)).status != RESOLVED
    assert idx.resolve("ATP", "alves", "pereira", "CHALLENGER", date(2026, 10, 4)).status == RESOLVED     # Sunday final
