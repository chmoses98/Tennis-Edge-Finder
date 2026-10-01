"""Discrepancy sanity layer (assisted track), TENNIS-17 and the historical discrepancy audit.

A production-shaped synthetic world per test (capture pass, frozen shadow-board and Gen-1 ledger rows, an
optional external scan row, track start, slate). The layer must classify every model-market gap, hold
extreme ones at DATA_WARNING unless all nine Part J conditions hold, and never change a model probability.
"""
import copy
import gzip
import hashlib
import json
import os
import sys
from datetime import datetime, timedelta, timezone

import pytest

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, REPO)

from tennis_edge.assisted import discrepancy as DS
from tennis_edge.assisted import record as R
from tennis_edge.assisted import schema as SC
from tennis_edge.assisted.health import gate_17
from tennis_edge.assisted.slate import build_slate, render_markdown, write_slate
from tennis_edge.assisted.store import RecordStore, ensure_track_start

UTC = timezone.utc
DAY = "2026-10-01"
T_START = datetime(2026, 10, 1, 8, 0, tzinfo=UTC)
T_CAP = datetime(2026, 10, 1, 8, 0, 30, tzinfo=UTC)
T_SLATE = datetime(2026, 10, 1, 8, 5, tzinfo=UTC)
T_DEC = datetime(2026, 10, 1, 8, 8, tzinfo=UTC)
EV = "KXATPMATCH-26OCT01AAABBB"
MW_A, MW_B = EV + "-AAA", EV + "-BBB"
PMID = "ATP:100:200:2026-10-01"


def _mw(ticker, name, bid, ask, at):
    return {"run_id": at.strftime("%Y%m%dT%H%M%SZ"), "captured_at": at.isoformat(), "snapshot_kind": "full",
            "ticker": ticker, "event_ticker": EV, "status": "active", "title": f"{name} wins", "yes_sub_title": name,
            "rules_primary": (f"If {name} wins the Alpha Aaa vs Beta Bbb professional tennis match in the 2026 ATP Tokyo "
                              "Round Of 32 after a ball has been played, then the market resolves to Yes."),
            "occurrence_datetime": "2026-10-01T10:00:00Z", "custom_strike": {"tennis_competitor": ticker[-3:]},
            "yes_bid_dollars": f"{bid:.4f}", "yes_ask_dollars": f"{ask:.4f}", "yes_bid_size_fp": "500.00",
            "yes_ask_size_fp": "500.00", "open_interest_fp": "1000.00", "volume_24h_fp": "500.00"}


def _jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")


def make_world(tmp_path, *, bid=0.47, ask=0.48, fair_a=0.56, ext=None, conf=1.0, shadow_is_a=(True, False),
               grade="A", serve=(5000.0, 3000.0), slate_now=T_SLATE):
    data = tmp_path / "data"
    cap = data / "kalshi" / "capture" / DAY
    os.makedirs(cap, exist_ok=True)
    with gzip.open(cap / "20261001T080030Z.quotes.jsonl.gz", "wt") as f:
        for r in (_mw(MW_A, "Alpha Aaa", bid, ask, T_CAP), _mw(MW_B, "Beta Bbb", round(1 - ask, 4), round(1 - bid, 4), T_CAP)):
            f.write(json.dumps(r) + "\n")
    res = data / "research"
    common = {"physical_match_id": PMID, "event": EV, "market_family": "MATCH_WINNER", "tour": "ATP", "level": "TOUR_500_250",
              "surface": "Hard", "predicted_at": "2026-10-01T08:02:00+00:00", "player_a_id": "100", "player_b_id": "200",
              "serve_evidence_a": serve[0], "serve_evidence_b": serve[1], "thinner_serve_points": min(serve),
              "model_uncertainty": 0.02, "qualification_ok": True, "blend_weight": 0.5, "data_quality_score": 0.8,
              "data_quality_grade": grade, "identity_confidence": conf, "identity_confidence_a": conf,
              "identity_confidence_b": conf, "quote_captured_at": T_CAP.isoformat(), "displayed_size": 500.0}
    qa = {"kalshi_bid": bid, "kalshi_ask": ask, "kalshi_mid": round((bid + ask) / 2, 4)}
    qb = {"kalshi_bid": round(1 - ask, 4), "kalshi_ask": round(1 - bid, 4), "kalshi_mid": round(1 - (bid + ask) / 2, 4)}
    env = {"base": fair_a, "surface_pool_low": fair_a - 0.01, "surface_pool_high": fair_a + 0.01}
    _jsonl(str(res / "frozen_producers" / "shadow_board" / f"{DAY}.jsonl"), [
        {**common, **qa, "ticker": MW_A, "subject": "Alpha Aaa", "subject_is_a": shadow_is_a[0], "gen1_elo_probability": fair_a,
         "gen2_probability": fair_a, "fair_v1_probability": fair_a, "fair_envelope": env, "selector_decision": "PASS"},
        {**common, **qb, "ticker": MW_B, "subject": "Beta Bbb", "subject_is_a": shadow_is_a[1], "gen1_elo_probability": 1 - fair_a,
         "gen2_probability": 1 - fair_a, "fair_v1_probability": 1 - fair_a,
         "fair_envelope": {k: 1 - v for k, v in env.items()}, "selector_decision": "PASS"}])
    _jsonl(str(res / "ledger" / f"{DAY}.jsonl"), [
        {"ticker": MW_A, "family": "MATCH_WINNER", "event_ticker": EV, "series_ticker": "KXATPMATCH", "subject": "Alpha Aaa",
         "tour": "ATP", "scheduled_start": "2026-10-01T10:00:00Z",
         "market_quote": {"yes_bid": bid, "yes_ask": ask, "quote_ts": T_CAP.isoformat()},
         "player_a": "Alpha Aaa", "player_b": "Beta Bbb", "player_a_id": "100", "player_b_id": "200",
         "generated_at_utc": "2026-10-01T08:02:00+00:00", "level": "TOUR_500_250", "surface": "Hard", "ratings_as_of": DAY,
         "models": {"ELO_DP_FAIR": fair_a, "ELO": fair_a, "STRUCTURAL": fair_a},
         "inputs": {"elo_a": 1900.0, "elo_b": 1850.0, "pa": 0.66, "pb": 0.63},
         "quality": {"grade": grade, "data_quality_score": 0.8, "pillars": {"recency": 0.9, "experience": 0.9, "identity_confidence": conf},
                     "inputs": {"n_matches_a": 300, "n_matches_b": 250, "days_since_last_a": 6, "days_since_last_b": 13}}}])
    if ext is not None:
        _jsonl(str(res / "external" / "dislocations" / f"{DAY}.jsonl"), [
            {"generated_at": "2026-10-01T08:01:00+00:00", "kalshi_ticker": MW_A, "external_prices": {"smarkets": ext},
             "external_fair": ext, "reference_kind": "SHARP_REFERENCE", "triangulation": "x", "external_quote_age_s": 30,
             "n_independent_groups": 1, "decision": "PASS"}])
    store = tmp_path / "research" / "assisted_decisions"
    ensure_track_start(str(store), started_at=T_START.isoformat(), main_sha="testsha")
    slate_dir = tmp_path / "research" / "assisted_slates"
    slate = build_slate(str(data), now=slate_now)
    write_slate(slate, str(slate_dir))
    return {"data": str(data), "store": str(store), "slate_dir": str(slate_dir), "research": str(tmp_path / "research"),
            "slate": slate, "shadow": str(res / "frozen_producers" / "shadow_board" / f"{DAY}.jsonl")}


def _row(w, ticker=MW_A):
    return next(r for x in w["slate"]["matches"] for r in x["markets"] if r["ticker"] == ticker)


def _kw(w, now=T_DEC):
    return {"store_root": w["store"], "data_root": w["data"], "slate_dir": w["slate_dir"], "now": now}


def _bet(**over):
    p = {"ticker": MW_A, "side": "YES", "decision": "BET", "chatgpt_fair_probability": 0.56, "chatgpt_confidence": "MEDIUM",
         "chatgpt_thesis": "A's serve is under-priced.", "bet_up_to_price": 0.52, "stake_units_if_bet": 1.0}
    p.update(over)
    return p


EXTREME_OK = dict(kalshi_bid=0.20, kalshi_ask=0.21, chatgpt_fair_probability=0.50, bet_up_to_price=0.30,
                  discrepancy_explanation="Kalshi has not repriced A's return to form; confirmed on the live book.",
                  why_market_may_be_wrong="thin ITF-style flow, price unchanged since the draw",
                  why_model_may_be_wrong="A's last two months are thinly sampled")


# ------------------------------------------------------------------------------------------ calculation & bands
def test_discrepancy_calculation():
    assert DS.gap_pp(0.80, 0.20) == 60.0 and DS.gap_pp(0.20, 0.80) == -60.0
    assert DS.gap_pp(None, 0.5) is None and DS.gap_pp(1.2, 0.5) is None and DS.gap_pp(True, 0.5) is None
    assert DS.executable_gap_pp(0.80, 0.19, 0.21) == 59.0                  # model above the ask
    assert DS.executable_gap_pp(0.10, 0.19, 0.21) == 9.0                   # model below the bid (NO side)
    assert DS.executable_gap_pp(0.20, 0.19, 0.21) == 0.0                   # inside the spread: nothing executable


def test_band_boundaries():
    cases = [(0, "NORMAL"), (9.99, "NORMAL"), (10, "REVIEW"), (14.99, "REVIEW"), (15, "HIGH_REVIEW"),
             (24.99, "HIGH_REVIEW"), (25, "EXTREME"), (60, "EXTREME"), (-25, "EXTREME"), (-10, "REVIEW"), (None, "UNPRICED")]
    for g, band in cases:
        assert DS.band_of(g) == band, (g, band)
    assert DS.band_of(DS.gap_pp(0.75, 0.50)) == "EXTREME" and DS.band_of(DS.gap_pp(0.65, 0.50)) == "HIGH_REVIEW"
    labels = [DS.audit_bucket(x) for x in (0, 2.99, 3, 4.99, 5, 10, 15, 25, 39.99, 40, 85)]
    assert labels == ["0-3", "0-3", "3-5", "3-5", "5-10", "10-15", "15-25", "25-40", "25-40", "40+", "40+"]
    assert DS.bucket_labels() == ["0-3", "3-5", "5-10", "10-15", "15-25", "25-40", "40+"]


def test_thresholds_are_configurable(tmp_path):
    cfg = copy.deepcopy(DS.load_config())
    cfg["bands_pp"] = {"REVIEW": 5, "HIGH_REVIEW": 8, "EXTREME": 12}
    cfg["freshness_minutes"] = {"FRESH": 1, "AGING": 2}
    assert DS.band_of(12.0, cfg) == "EXTREME" and DS.band_of(12.0) == "REVIEW"
    assert DS.freshness_of(150, cfg) == "STALE" and DS.freshness_of(150) == "FRESH"
    assert DS.audit_bucket(7, edges=[0, 5, 50]) == "5-50"


# ------------------------------------------------------------------------------------------ identity / orientation
def test_ticker_orientation():
    assert DS.ticker_orientation(MW_A, EV, True)[0] == "VERIFIED"
    assert DS.ticker_orientation(MW_B, EV, False)[0] == "VERIFIED"
    assert DS.ticker_orientation(MW_A, EV, False)[0] == "FAILED"                   # YES names A, we think B
    assert DS.ticker_orientation(MW_A, EV, None)[0] == "UNKNOWN"
    assert DS.ticker_orientation("KXATPMATCH-26OCT01AAAAAA-AAA", "KXATPMATCH-26OCT01AAAAAA", True)[0] == "UNKNOWN"
    assert DS.ticker_orientation("KXATPMATCH-26OCT01AAABBB-ZZZ", EV, True)[0] == "UNKNOWN"
    assert DS.derivative_orientation(False, None, None) == "NOT_APPLICABLE"
    assert DS.derivative_orientation(True, True, False) == "FAILED"


def test_identity_verification():
    ok = {"physical_match_id": "PASS", "player_ids": "PASS", "namesake": "NA", "ticker_orientation": "PASS"}
    assert DS.identity_status(ok) == DS.ID_VERIFIED
    assert DS.identity_status({**ok, "namesake": "AMBIGUOUS"}) == DS.ID_AMBIGUOUS        # ambiguity fails closed
    assert DS.identity_status({**ok, "ticker_orientation": "FAIL"}) == DS.ID_FAILED
    assert DS.identity_status({"a": "NA"}) == DS.ID_AMBIGUOUS                              # no evidence is not verified
    assert DS.check_player_ids("1", "1") == "FAIL" and DS.check_player_ids(None, "1") == "AMBIGUOUS"
    assert DS.check_complement(0.6, 0.4) == "PASS" and DS.check_complement(0.6, 0.6) == "FAIL"
    assert DS.check_market_pair(0.6, 0.38) == "PASS" and DS.check_market_pair(0.9, 0.9) == "AMBIGUOUS"
    assert DS.check_identity_confidence(1.0, 0.9) == "AMBIGUOUS"
    assert DS.check_physical_match_id("garbage") == "FAIL" and DS.check_physical_match_id(PMID) == "PASS"


def test_namesakes_fail_closed(tmp_path):
    p = tmp_path / "ratings_ATP.json"
    json.dump({"players": {"1": {"name": "Alpha Aaa", "last_date": "2026-09-01"}, "2": {"name": "Alpha Aaa", "last_date": "2026-08-01"},
                           "3": {"name": "Beta Bbb", "last_date": "2026-09-01"}, "4": {"name": "Beta Bbb", "last_date": "2019-01-01"}}}, open(p, "w"))
    idx = DS.namesake_index([str(p)], as_of=datetime(2026, 10, 1).date())
    assert DS.check_namesakes(["Alpha Aaa"], idx) == "AMBIGUOUS"
    assert DS.check_namesakes(["Beta Bbb"], idx) == "PASS"                  # the namesake retired long ago
    assert DS.check_namesakes(["Beta Bbb"], None) == "NA"


def test_slate_orientation_mismatch_is_a_data_warning_and_fails_tennis17(tmp_path):
    w = make_world(tmp_path, shadow_is_a=(False, True))                      # producer thinks YES on -AAA is player B
    r = _row(w)
    assert r["ticker_orientation_status"] == "FAILED" and r["identity_check_status"] == DS.ID_FAILED
    assert r["discrepancy_sanity_status"] == DS.DATA_WARNING and "TICKER_SIDE_RISK" in r["discrepancy_reason_tags"]
    status, d = gate_17(w["research"], now=T_SLATE)
    assert status == "FAIL" and "TICKER_ORIENTATION_MISMATCH" in d["failing"]


# ------------------------------------------------------------------------------------------ freshness / external / data
def test_fresh_and_stale_quotes():
    assert [DS.freshness_of(s) for s in (0, 600, 601, 1800, 1801, None, -500)] == \
        ["FRESH", "FRESH", "AGING", "AGING", "STALE", "UNKNOWN", "UNKNOWN"]
    a = DS.assess(p_model=0.80, bid=0.19, ask=0.21, quote_age_s=3 * 3600, identity=DS.ID_VERIFIED, orientation="VERIFIED")
    assert a["market_freshness_status"] == "STALE" and "STALE_KALSHI_QUOTE" in a["discrepancy_reason_tags"]
    assert a["discrepancy_sanity_status"] == DS.DATA_WARNING and a["display_status"] == "DATA_WARNING / PASS UNTIL RECHECKED"


def test_stale_slate_quote_is_flagged(tmp_path):
    w = make_world(tmp_path, bid=0.20, ask=0.21, slate_now=T_CAP + timedelta(hours=2))
    r = _row(w)
    assert r["market_freshness_status"] == "STALE" and r["discrepancy_band"] == "EXTREME"
    assert r["discrepancy_sanity_status"] == DS.DATA_WARNING
    assert "fresh_executable_price" in r["discrepancy"]["extreme_preconditions"]["failed"]


def test_external_agreement_disagreement_and_absence():
    assert DS.external_confirmation(0.80, 0.20, 0.22) == ("AGREES_WITH_KALSHI", "MODEL_LONE_OUTLIER")
    assert DS.external_confirmation(0.80, 0.20, 0.78) == ("AGREES_WITH_MODEL", "KALSHI_LONE_OUTLIER")
    assert DS.external_confirmation(0.80, 0.20, 0.45) == ("SUPPORTS_MODEL_DIRECTION", "ALL_THREE_DISAGREE")
    assert DS.external_confirmation(0.80, 0.20, 0.05) == ("ALL_DISAGREE", "ALL_THREE_DISAGREE")
    assert DS.external_confirmation(0.50, 0.50, 0.51) == ("ALL_AGREE", "MARKETS_AGREE")
    assert DS.external_confirmation(0.50, 0.51, 0.80) == ("EXTERNAL_OUTLIER", "EXTERNAL_LONE_OUTLIER")
    assert DS.external_confirmation(0.80, 0.20, None) == ("NO_EXTERNAL_REFERENCE", "INSUFFICIENT_INPUTS")
    assert DS.external_confirmation(0.80, 0.20, 0.78, ext_age_s=7200)[0] == "EXTERNAL_STALE"
    tags = DS.assess(p_model=0.8, bid=0.19, ask=0.21, quote_age_s=60, p_ext=0.22)["discrepancy_reason_tags"]
    assert "EXTERNAL_MARKET_REJECTION" in tags
    assert "NO_EXTERNAL_REFERENCE" in DS.assess(p_model=0.8, bid=0.19, ask=0.21, quote_age_s=60)["discrepancy_reason_tags"]


def test_data_quality_and_sample_asymmetry():
    good = DS.data_quality(grade="A", serve_a=5000, serve_b=3000, n_a=300, n_b=250, days_a=5, days_b=9)
    assert good["data_quality_status"] == "ADEQUATE" and good["tags"] == [] and not good["severe_sample_asymmetry"]
    thin = DS.data_quality(grade="B", serve_a=5000, serve_b=800)
    assert thin["data_quality_status"] == "LIMITED" and {"THIN_PLAYER_HISTORY", "ASYMMETRIC_SAMPLE_SIZE"} <= set(thin["tags"])
    severe = DS.data_quality(grade="B", serve_a=8000, serve_b=500)
    assert severe["severe_sample_asymmetry"] and severe["data_quality_status"] == "POOR"
    assert DS.data_quality(grade="F", serve_a=5000, serve_b=5000)["data_quality_status"] == "POOR"
    assert "STALE_PLAYER_DATA" in DS.data_quality(grade="A", serve_a=5000, serve_b=5000, days_a=200)["tags"]
    assert DS.data_quality()["data_quality_status"] == "UNKNOWN"


# ------------------------------------------------------------------------------------------ bands on the slate & recorder
def test_normal_discrepancies_are_unaffected(tmp_path):
    w = make_world(tmp_path)                                                  # fair 0.56 vs mid 0.475: 8.5pp
    r = _row(w)
    assert (r["discrepancy_band"], r["discrepancy_sanity_status"]) == ("NORMAL", "OK")
    assert r["identity_check_status"] == DS.ID_VERIFIED and r["ticker_orientation_status"] == "VERIFIED"
    rec = R.record_decision(_bet(), **_kw(w))
    assert rec["schema_version"] == 2 and list(rec) == SC.DECISION_FIELDS
    assert (rec["discrepancy_band"], rec["discrepancy_sanity_status"]) == ("NORMAL", "OK")
    assert rec["model_market_gap_pp"] == pytest.approx(8.5) and rec["discrepancy_conditions"] is None
    assert not any(x.startswith("DISCREPANCY") for x in rec["warnings"])


def test_review_band_surfaces_context(tmp_path):
    w = make_world(tmp_path, bid=0.43, ask=0.44)                              # 12.5pp
    r = _row(w)
    assert (r["discrepancy_band"], r["discrepancy_sanity_status"]) == ("REVIEW", "REVIEW_CONTEXT")
    rec = R.record_decision(_bet(bet_up_to_price=0.50), **_kw(w))
    assert rec["discrepancy_sanity_status"] == "REVIEW_CONTEXT" and any(x.startswith("DISCREPANCY_REVIEW") for x in rec["warnings"])


def test_high_review_requires_explanation_before_bet(tmp_path):
    w = make_world(tmp_path, bid=0.38, ask=0.39)                              # 17.5pp
    assert _row(w)["discrepancy_sanity_status"] == DS.EXPLANATION_REQUIRED
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(_bet(bet_up_to_price=0.45), **_kw(w))
    assert e.value.code == "DISCREPANCY_EXPLANATION_REQUIRED"
    rec = R.record_decision(_bet(bet_up_to_price=0.45, discrepancy_explanation="B's ranking jump is not in the model yet"), **_kw(w))
    assert rec["discrepancy_band"] == "HIGH_REVIEW" and rec["discrepancy_explanation"].startswith("B's ranking")
    assert rec["discrepancy_conditions"] == {"explanation_required": True, "explanation_provided": True}
    p = R.record_decision({"ticker": MW_A, "decision": "PASS", "pass_reason_if_pass": "too far from the market"}, **_kw(w))
    assert p["discrepancy_band"] == "HIGH_REVIEW"                            # PASS needs no explanation


def test_extreme_defaults_to_data_warning(tmp_path):
    w = make_world(tmp_path, bid=0.20, ask=0.21, ext=0.55)                    # fair 0.56 vs mid 0.205: +35.5pp
    r = _row(w)
    assert r["discrepancy_band"] == "EXTREME" and r["discrepancy_sanity_status"] == DS.DATA_WARNING
    pre = r["discrepancy"]["extreme_preconditions"]
    assert not pre["all_met"] and {"explains_why_market_may_be_wrong", "explains_why_model_may_be_wrong",
                                   "price_clears_fees_and_execution"} <= set(pre["failed"])
    with pytest.raises(SC.AssistedValidationError) as e:                    # explanation missing
        R.build_decision(_bet(bet_up_to_price=0.30), **_kw(w))
    assert e.value.code == "DISCREPANCY_EXPLANATION_REQUIRED"
    no_live = {k: v for k, v in EXTREME_OK.items() if k not in ("kalshi_bid", "kalshi_ask")}
    with pytest.raises(SC.AssistedValidationError) as e:                    # capture quote 7.5 min old is fresh, but ...
        R.build_decision(_bet(**{**no_live, "why_model_may_be_wrong": None}), **_kw(w))
    assert e.value.code == "DISCREPANCY_DATA_WARNING" and "explains_why_model_may_be_wrong" in str(e.value)
    p = R.record_decision({"ticker": MW_A, "decision": "PASS", "pass_reason_if_pass": "data warning"}, **_kw(w))
    assert (p["discrepancy_band"], p["discrepancy_sanity_status"]) == ("EXTREME", DS.DATA_WARNING)


def test_extreme_needs_a_fresh_price(tmp_path):
    w = make_world(tmp_path, bid=0.20, ask=0.21, ext=0.55)
    no_live = {k: v for k, v in EXTREME_OK.items() if k not in ("kalshi_bid", "kalshi_ask")}
    with pytest.raises(SC.AssistedValidationError) as e:                    # capture quote 39.5 min old: STALE
        R.build_decision(_bet(**no_live), **_kw(w, T_CAP + timedelta(minutes=39, seconds=30)))
    assert e.value.code == "DISCREPANCY_DATA_WARNING" and "fresh_executable_price" in str(e.value)


def test_extreme_with_every_condition_is_only_eligible_for_human_review(tmp_path):
    w = make_world(tmp_path, bid=0.20, ask=0.21, ext=0.55)
    rec = R.record_decision(_bet(**EXTREME_OK), **_kw(w))
    assert rec["discrepancy_sanity_status"] == DS.ELIGIBLE and rec["discrepancy_conditions"]["all_met"]
    assert rec["market_freshness_status"] == "FRESH" and rec["external_confirmation_status"] == "AGREES_WITH_MODEL"
    assert any(x.startswith("EXTREME_DISCREPANCY_ELIGIBLE_FOR_HUMAN_REVIEW_ONLY") for x in rec["warnings"])
    assert rec["actual_wagered"] is False and rec["automated_execution"] is False   # never an automatic bet
    assert RecordStore(w["store"]).records("wagers") == []
    status, d = gate_17(w["research"], now=T_DEC)
    assert status == "PASS" and d["decisions_checked_v2"] == 1


def test_extreme_refused_when_external_sides_with_kalshi_or_price_does_not_clear(tmp_path):
    w = make_world(tmp_path, bid=0.20, ask=0.21, ext=0.22)
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(_bet(**EXTREME_OK), **_kw(w))
    assert e.value.code == "DISCREPANCY_DATA_WARNING" and "external_supports_or_documented_unavailable" in str(e.value)
    w2 = make_world(tmp_path / "w2", bid=0.20, ask=0.21, ext=0.55)
    with pytest.raises(SC.AssistedValidationError) as e:                    # ChatGPT's own price does not clear the fee
        R.build_decision(_bet(**{**EXTREME_OK, "chatgpt_fair_probability": 0.215}), **_kw(w2))
    assert "price_clears_fees_and_execution" in str(e.value)


def test_extreme_without_external_needs_a_documented_reason(tmp_path):
    w = make_world(tmp_path, bid=0.20, ask=0.21)
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(_bet(**EXTREME_OK), **_kw(w))
    assert "external_supports_or_documented_unavailable" in str(e.value)
    rec = R.build_decision(_bet(**EXTREME_OK, external_unavailable_reason="no Bovada/Smarkets market lists this match"), **_kw(w))
    assert rec["discrepancy_sanity_status"] == DS.ELIGIBLE and rec["external_confirmation_status"] == "NO_EXTERNAL_REFERENCE"


def test_extreme_with_severe_asymmetry_needs_justification_and_poor_data_cannot_pass(tmp_path):
    w = make_world(tmp_path, bid=0.20, ask=0.21, ext=0.55, serve=(9000.0, 1500.0))       # ratio 6: LIMITED, not severe
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(_bet(**EXTREME_OK), **_kw(w))
    assert "adequate_data_quality" in str(e.value)
    w2 = make_world(tmp_path / "w2", bid=0.20, ask=0.21, ext=0.55, serve=(30000.0, 2500.0))  # ratio 12: severe
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(_bet(**EXTREME_OK, sample_asymmetry_justification="B's challenger record is long"), **_kw(w2))
    assert "no_severe_asymmetry_or_justified" not in str(e.value) and "adequate_data_quality" in str(e.value)


def test_typed_model_probability_cannot_shrink_an_extreme_gap(tmp_path):
    w = make_world(tmp_path, bid=0.20, ask=0.21, ext=0.55)
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(_bet(fair_v1_probability=0.22, bet_up_to_price=0.30), **_kw(w))
    assert e.value.code == "DISCREPANCY_EXPLANATION_REQUIRED"


def test_ambiguous_identity_holds_high_review_at_data_warning(tmp_path):
    w = make_world(tmp_path, bid=0.38, ask=0.39, conf=0.9)
    r = _row(w)
    assert r["identity_check_status"] == DS.ID_AMBIGUOUS and r["discrepancy_sanity_status"] == DS.DATA_WARNING
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(_bet(bet_up_to_price=0.45, discrepancy_explanation="x"), **_kw(w))
    assert e.value.code == "DISCREPANCY_DATA_WARNING"


# ------------------------------------------------------------------------------------------ models / frozen state
def test_model_probabilities_unchanged(tmp_path):
    w = make_world(tmp_path, bid=0.20, ask=0.21, ext=0.55)
    sh = [json.loads(x) for x in open(w["shadow"])]
    r = _row(w)
    assert r["model"]["fair_v1"] == round(sh[0]["fair_v1_probability"], 4) and r["model_probability_yes"] == 0.56
    assert r["discrepancy"]["model_probability_yes"] == r["model_probability_yes"]
    before = copy.deepcopy(r)
    DS.assess(p_model=r["model_probability_yes"], bid=0.2, ask=0.21)
    assert r == before
    src = open(os.path.join(REPO, "tennis_edge", "assisted", "discrepancy.py")).read()
    for forbidden in ("tennis_edge.models", ".fit(", "edge_candidates", "experiment_starts", "place_order"):
        assert forbidden not in src


def test_frozen_candidates_and_experiment_starts_unchanged(tmp_path):
    from tests.test_frozen_producers import FROZEN_CANDIDATES, FROZEN_SOURCES
    for rel, h in FROZEN_SOURCES.items():
        assert hashlib.sha256(open(os.path.join(REPO, rel), "rb").read()).hexdigest() == h, rel
    cdir = os.path.join(REPO, "data", "research", "edge_candidates")
    for fn, h in FROZEN_CANDIDATES.items():
        assert hashlib.sha256(open(os.path.join(cdir, fn), "rb").read()).hexdigest() == h, fn
    # the slate, the recorder and the audit run beside a write-once experiment start without touching it
    w = make_world(tmp_path, bid=0.20, ask=0.21, ext=0.55)
    starts = os.path.join(w["data"], "research", "experiment_starts")
    os.makedirs(starts)
    sp = os.path.join(starts, "W3-2026-001-ABSTAIN-ITF.json")
    open(sp, "w").write('{"effective_scorable_start": "2026-09-28T03:33:22Z"}')
    before = (hashlib.sha256(open(sp, "rb").read()).hexdigest(), hashlib.sha256(open(w["shadow"], "rb").read()).hexdigest())
    R.record_decision(_bet(**EXTREME_OK), **_kw(w))
    from tennis_edge.research.discrepancy_audit import run_audit
    run_audit(w["data"], now=T_DEC)
    write_slate(build_slate(w["data"], now=T_DEC), w["slate_dir"])
    assert before == (hashlib.sha256(open(sp, "rb").read()).hexdigest(), hashlib.sha256(open(w["shadow"], "rb").read()).hexdigest())


# ------------------------------------------------------------------------------------------ rendering
def test_assisted_slate_rendering(tmp_path):
    w = make_world(tmp_path, bid=0.20, ask=0.21, ext=0.55)
    md = render_markdown(w["slate"])
    assert "MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY" in md
    block = md[md.index("DISCREPANCY SANITY CHECK"):]
    for s in ("Model: 56%", "Kalshi: 20%", "Gap: +36 pp", "Band: EXTREME", "Identity: VERIFIED", "Quote freshness: FRESH",
              "External: AGREES_WITH_MODEL", "Data quality: A (ADEQUATE)", "Status: DATA_WARNING / PASS UNTIL RECHECKED"):
        assert s in block, s
    assert "Discrepancy sanity layer" in md and w["slate"]["discrepancy_sanity"]["model_probabilities_changed"] is False
    assert w["slate"]["discrepancy_sanity"]["extreme"] == [MW_A, MW_B]
    on_disk = json.load(open(os.path.join(w["slate_dir"], "latest.json")))
    assert all(f in _row({"slate": on_disk}) for f in ("model_market_gap_pp", "discrepancy_band", "discrepancy_sanity_status",
                                                        "discrepancy_reason_tags", "identity_check_status",
                                                        "market_freshness_status", "external_confirmation_status",
                                                        "data_quality_status"))
    normal = render_markdown(make_world(tmp_path / "n")["slate"])
    assert "DISCREPANCY SANITY CHECK" not in normal                          # a normal gap carries no alarm block


# ------------------------------------------------------------------------------------------ TENNIS-17
def _tamper(w, fn):
    p = os.path.join(w["slate_dir"], "latest.json")
    s = json.load(open(p))
    fn(next(r for x in s["matches"] for r in x["markets"] if r["ticker"] == MW_A), s)
    json.dump(s, open(p, "w"))


def test_tennis17_passes_when_extremes_are_contained(tmp_path):
    w = make_world(tmp_path, bid=0.20, ask=0.21, slate_now=T_CAP + timedelta(hours=2))  # extreme, stale, no external
    status, d = gate_17(w["research"], now=T_SLATE)
    assert status == "PASS" and d["extreme_rows"] == 2 and d["gate_kind"].startswith("INTEGRITY")
    assert d["counts_by_band"] == {"EXTREME": 2}                            # a disagreement alone never fails


def test_tennis17_failures(tmp_path):
    assert gate_17(str(tmp_path / "none"))[0] == "UNKNOWN"
    cases = [
        (lambda r, s: s.pop("discrepancy_sanity"), "SLATE_LACKS_DISCREPANCY_CLASSIFICATION"),
        (lambda r, s: r.pop("discrepancy_band"), "SLATE_LACKS_DISCREPANCY_CLASSIFICATION"),
        (lambda r, s: r.update(discrepancy_band="NORMAL"), "BAND_MISMATCH"),
        (lambda r, s: r.update(discrepancy_sanity_status="OK"), "EXTREME_BYPASS"),
        (lambda r, s: r.update(discrepancy_sanity_status="OK", identity_check_status=DS.ID_AMBIGUOUS), "EXTREME_UNRESOLVED_IDENTITY"),
        (lambda r, s: r.update(discrepancy_sanity_status="OK", market_freshness_status="STALE"), "EXTREME_STALE_PRICE_ACTIONABLE"),
        (lambda r, s: r["model"].update(gen2=1.7), "MALFORMED_PROBABILITY"),
        (lambda r, s: r.update(ticker_orientation_status="FAILED"), "TICKER_ORIENTATION_MISMATCH"),
    ]
    for i, (fn, code) in enumerate(cases):
        w = make_world(tmp_path / f"c{i}", bid=0.20, ask=0.21, ext=0.55)
        assert gate_17(w["research"])[0] == "PASS"
        _tamper(w, fn)
        status, d = gate_17(w["research"])
        assert status == "FAIL" and code in d["failing"], (code, d["failing"])
    w = make_world(tmp_path / "hr", bid=0.38, ask=0.39)
    _tamper(w, lambda r, s: r.update(discrepancy_sanity_status="REVIEW_CONTEXT"))
    assert "HIGH_REVIEW_BYPASS" in gate_17(w["research"])[1]["failing"]


def test_tennis17_checks_recorded_decisions(tmp_path):
    w = make_world(tmp_path, bid=0.38, ask=0.39)
    rec = R.record_decision(_bet(bet_up_to_price=0.45, discrepancy_explanation="why"), **_kw(w))
    assert gate_17(w["research"])[0] == "PASS"
    p = RecordStore(w["store"]).find("decisions", rec["decision_id"])
    d = json.load(open(p)); d["discrepancy_explanation"] = None; json.dump(d, open(p, "w"))
    status, det = gate_17(w["research"])
    assert status == "FAIL" and "HIGH_REVIEW_BYPASS" in det["failing"]


def test_tennis17_is_in_the_health_run():
    from tennis_edge.health import gates as G
    g = G.gate_17_discrepancy_integrity(research_root="/nonexistent")
    assert (g.gate, g.name, g.status) == ("TENNIS-17", "model_market_discrepancy_integrity", "UNKNOWN")


# ------------------------------------------------------------------------------------------ audit: no leakage, no reconstruction
def _audit_world(tmp_path, settle=True):
    w = make_world(tmp_path, bid=0.20, ask=0.21, ext=0.55)
    sp = os.path.join(w["data"], "research", "settlements", "20261001T120000Z.jsonl")
    if settle:
        _jsonl(sp, [{"ticker": MW_A, "exchange": {"result": "no", "settlement_ts": "2026-10-01T08:01:00+00:00"},
                     "close": {"strict": False}},
                    {"ticker": MW_B, "exchange": {"result": "yes", "settlement_ts": "2026-10-01T08:01:00+00:00"},
                     "close": {"strict": False}}])
    return w


def test_audit_has_no_hindsight_leakage(tmp_path):
    from tennis_edge.research.discrepancy_audit import build_observations
    a, _ = build_observations(_audit_world(tmp_path / "a", settle=True)["data"])
    b, _ = build_observations(_audit_world(tmp_path / "b", settle=False)["data"])
    ex_ante = ["model", "ticker", "p", "mid", "gap_pp", "band", "status", "tags", "identity", "freshness", "external_status",
               "data_status"]
    key = ["model", "ticker"]
    ka, kb = a.sort_values(key)[ex_ante].reset_index(drop=True), b.sort_values(key)[ex_ante].reset_index(drop=True)
    assert ka.to_dict("records") == kb.to_dict("records")                  # outcomes change no ex-ante classification
    assert set(a.hindsight.map(tuple)) == {("POST_SETTLEMENT_OBSERVATION", "LIKELY_IN_PLAY_QUOTE")}
    assert set(b.hindsight.map(tuple)) == {()}
    assert a.y.notna().all() and b.y.isna().all()


def test_audit_never_reconstructs_probabilities(tmp_path):
    from tennis_edge.research.discrepancy_audit import build_observations, run_audit, write_audit
    w = _audit_world(tmp_path)
    obs, meta = build_observations(w["data"])
    sh = {json.loads(x)["ticker"]: json.loads(x) for x in open(w["shadow"])}
    for r in obs.itertuples():
        if r.source == "shadow_board_v1":
            key = {"fair_v1": "fair_v1_probability", "gen2": "gen2_probability", "gen1_elo": "gen1_elo_probability"}.get(r.model)
            if key:
                assert r.p == sh[r.ticker][key]                              # the producer's own number, untouched
    src = open(os.path.join(REPO, "tennis_edge", "research", "discrepancy_audit.py")).read()
    for forbidden in ("tennis_edge.models", ".fit(", "ELO_DP_FAIR\"] =", "predict("):
        assert forbidden not in src
    a = run_audit(w["data"], now=T_DEC)
    assert a["model_probabilities_changed"] is False and a["total_observations"]["comparisons"] > 0
    write_audit(a, str(tmp_path / "out"))
    md = open(tmp_path / "out" / "AUDIT.md").read()
    assert "Executive summary" in md and "MODEL_CHANGE_RECOMMENDED" in md
    assert json.load(open(tmp_path / "out" / "AUDIT.json"))["audit_version"] == a["audit_version"]


def test_committed_audit_snapshot_exists():
    d = os.path.join(REPO, "research", "model_market_discrepancy")
    a = json.load(open(os.path.join(d, "AUDIT.json")))
    assert a["model_probabilities_changed"] is False and a["AUTONOMOUS_REAL_MONEY_AUTHORITY"] == "OFF"
    for k in ("total_observations", "histogram", "by_level", "by_data_quality_grade", "by_quote_freshness_at_model_time",
              "external_triangulation", "sample_asymmetry", "performance_by_bucket", "top_50", "answers",
              "model_change_recommendation", "unresolved_questions"):
        assert k in a, k
    assert a["model_change_recommendation"]["implemented_in_this_change"] is False
    assert len(a["answers"]) == 11
