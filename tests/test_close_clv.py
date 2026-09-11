import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from datetime import datetime, timedelta, timezone
from tennis_edge.ledger.close import Quote, canonical_close, BASIS_ACTUAL, BASIS_SCHEDULED, BASIS_NO_QUOTE
from tennis_edge.ledger.clv import clv_record
from tennis_edge.ledger.truth import SportsTruth, ExchangeTruth, reconcile
from tennis_edge.firstball.truth import FirstBallTruth, DERIVATION_EXPLICIT
from tennis_edge.firstball.classify import classify

T0 = datetime(2026, 9, 9, 18, 30, tzinfo=timezone.utc)
TRUTH = FirstBallTruth("m1", T0, T0, T0, "A", DERIVATION_EXPLICIT, created_at=T0)


def q(minutes, bid, ask, source="market_record"):
    return Quote(T0 + timedelta(minutes=minutes), bid, ask, source=source)


def test_close_is_last_executable_strictly_before_first_ball():
    quotes = [q(-60, 0.60, 0.63), q(-10, 0.61, 0.64), q(-1, 0.62, 0.65), q(0, 0.70, 0.72), q(5, 0.80, 0.82)]
    cc = canonical_close(quotes, TRUTH)
    assert cc.close_basis == BASIS_ACTUAL and cc.quote.ts == T0 - timedelta(minutes=1)
    # a quote exactly AT first ball is not strictly before
    assert cc.quote.yes_bid == 0.62 and cc.strict


def test_scheduled_fallback_must_be_asked_for_and_is_never_strict():
    quotes = [q(-60, 0.60, 0.63), q(-4, 0.61, 0.64)]
    # without an explicit opt-in there is simply no close: a scheduled time is not first-ball truth
    assert canonical_close(quotes, None).close_basis == "NO_FIRST_BALL_TRUTH"
    cc = canonical_close(quotes, None, scheduled_start=T0, allow_scheduled_fallback=True)
    assert cc.close_basis == BASIS_SCHEDULED and cc.quote.ts == T0 - timedelta(minutes=60) and not cc.strict


def test_no_synthetic_close():
    assert canonical_close([q(-1, None, 0.6), q(-2, 0.7, 0.6)], TRUTH).quote is None
    assert canonical_close([], TRUTH).quote is None
    assert canonical_close([q(-3, 0.5, 0.52, source="trade")], TRUTH).quote is None


def test_clv_signs_and_separation_of_measures():
    decision = q(-120, 0.55, 0.58)
    cc = canonical_close([q(-1, 0.62, 0.65)], TRUTH)
    r = clv_record(prediction_id="p", ticker="T", match_id="m1", family="MATCH_WINNER", entry=decision,
                   close=cc, truth=TRUTH, timing=classify(decision.ts, TRUTH), model_prob=0.61)
    assert abs(r.clv_executable - (0.62 - 0.58)) < 1e-12
    assert abs(r.clv_ask_to_ask - (0.65 - 0.58)) < 1e-12
    assert abs(r.clv_midpoint - (0.635 - 0.565)) < 1e-12
    assert r.prob_move == r.clv_midpoint and abs(r.price_move_cents - 100 * r.clv_midpoint) < 1e-9
    assert r.strict and r.seconds_entry_to_first_ball == 7200
    # fees are computed but never folded into a CLV number
    assert r.entry_taker_fee_per_contract > 0 and r.close_taker_fee_per_contract > 0


def test_truth_reconciliation():
    s = SportsTruth("m1", "A", "B", "RETIRED", "6-3 2-1 RET", confidence=0.95)
    e_yes = ExchangeTruth("t", "finalized", "yes", 1.0, None)
    e_scalar = ExchangeTruth("t", "finalized", "scalar", 0.55, None)
    assert reconcile(s, e_yes, True)["consistent"]
    assert not reconcile(s, e_yes, False)["consistent"]
    assert not reconcile(s, e_scalar, True)["consistent"]
    wo = SportsTruth("m1", "A", "B", "WALKOVER", "W/O", confidence=0.95)
    assert reconcile(wo, e_scalar, True)["consistent"]
    assert not wo.gradeable_binary and s.gradeable_binary
