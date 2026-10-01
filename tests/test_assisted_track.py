"""The ChatGPT-assisted handicapping lane: ledger, recorder, settlement, slate, scorecard, TENNIS-16.

Everything runs on a synthetic but production-shaped world (capture passes, frozen producer rows, the
Gen-1 ledger, an external scan row, first-ball truth), built fresh in a tmp dir per test.
"""
import gzip
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone

import pytest

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, REPO)

from tennis_edge.assisted import AUTONOMOUS_REAL_MONEY_AUTHORITY, CHATGPT_ASSISTED_TRACK
from tennis_edge.assisted import record as R
from tennis_edge.assisted import schema as SC
from tennis_edge.assisted.health import gate_16
from tennis_edge.assisted.scorecard import build_scorecard, write_scorecard
from tennis_edge.assisted.settle import latest_settlements, settle
from tennis_edge.assisted.slate import build_slate, render_markdown, write_slate
from tennis_edge.assisted.store import (AppendOnlyJsonl, RecordStore, changed_immutable_fields, compile_canonical,
                                        ensure_track_start, load_track_start)
from tennis_edge.firstball.store import FirstBallStore
from tennis_edge.firstball.truth import DERIVATION_EXPLICIT, FirstBallTruth

UTC = timezone.utc
DAY = "2026-10-01"
T_START = datetime(2026, 10, 1, 8, 0, tzinfo=UTC)          # track start
T_FULL = datetime(2026, 10, 1, 8, 0, 30, tzinfo=UTC)       # first capture pass (full snapshot)
T_SLATE = datetime(2026, 10, 1, 8, 20, tzinfo=UTC)
T_DEC = datetime(2026, 10, 1, 8, 30, tzinfo=UTC)
T_LATE = datetime(2026, 10, 1, 9, 0, tzinfo=UTC)           # second pass (the strict close)
FIRST_BALL = datetime(2026, 10, 1, 10, 0, tzinfo=UTC)
EV = "KXATPMATCH-26OCT01AAABBB"
MW_A, MW_B = EV + "-AAA", EV + "-BBB"
TOT = "KXATPGTOTAL-26OCT01AAABBB-22"
PMID = "ATP:100:200:2026-10-01"
OTHER_EV = "KXATPMATCH-26OCT01CCCDDD"                        # a match already under way


def _quote(ticker, event, bid, ask, at, *, kind="full", title=None, rules=None, sub=None, size=500.0):
    return {"run_id": at.strftime("%Y%m%dT%H%M%SZ"), "captured_at": at.isoformat(), "snapshot_kind": kind,
            "ticker": ticker, "event_ticker": event, "status": "active", "title": title, "yes_sub_title": sub,
            "rules_primary": rules, "occurrence_datetime": "2026-10-01T10:00:00Z",
            "custom_strike": {"tennis_competitor": ticker[-3:]} if "MATCH-" in ticker else None,
            "yes_bid_dollars": f"{bid:.4f}", "yes_ask_dollars": f"{ask:.4f}",
            "yes_bid_size_fp": f"{size:.2f}", "yes_ask_size_fp": f"{size:.2f}",
            "open_interest_fp": "1000.00", "volume_24h_fp": "500.00"}


def _mw(ticker, event, name, bid, ask, at, kind="full", players=("Aaa", "Bbb"), comp="ATP Tokyo"):
    return _quote(ticker, event, bid, ask, at, kind=kind, title=f"{name} wins", sub=name,
                  rules=f"If {name} wins the {players[0]} vs {players[1]} professional tennis match in the 2026 {comp} "
                        "Round Of 32 after a ball has been played, then the market resolves to Yes.")


def _write_gz(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")


def _jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")


@pytest.fixture
def world(tmp_path):
    data = tmp_path / "data"
    cap = data / "kalshi" / "capture" / DAY
    rules_tot = ("If the number of completed games in the full match is above 21.5 in the Alpha Aaa vs Beta Bbb "
                 "professional tennis match in the 2026 ATP Tokyo Round Of 32, then the market resolves to Yes.")
    _write_gz(str(cap / "20261001T080030Z.quotes.jsonl.gz"), [
        _mw(MW_A, EV, "Alpha Aaa", 0.47, 0.48, T_FULL), _mw(MW_B, EV, "Beta Bbb", 0.52, 0.53, T_FULL),
        _quote(TOT, "KXATPGTOTAL-26OCT01AAABBB", 0.45, 0.46, T_FULL, title="Over 21.5 games", sub="Over 21.5 games", rules=rules_tot),
        _mw(OTHER_EV + "-CCC", OTHER_EV, "Gamma Ccc", 0.30, 0.31, T_FULL, players=("Ccc", "Ddd")),
        _mw(OTHER_EV + "-DDD", OTHER_EV, "Delta Ddd", 0.69, 0.70, T_FULL, players=("Ccc", "Ddd")),
        _quote("KXATP-26BEIJIN-ZVE", "KXATP-26BEIJIN", 0.2, 0.21, T_FULL, title="futures"),
    ])
    _write_gz(str(cap / "20261001T090000Z.quotes.jsonl.gz"), [
        _mw(MW_A, EV, "Alpha Aaa", 0.50, 0.51, T_LATE, kind="changed"),
        _mw(MW_B, EV, "Beta Bbb", 0.49, 0.50, T_LATE, kind="changed"),
        _quote(TOT, "KXATPGTOTAL-26OCT01AAABBB", 0.44, 0.45, T_LATE, kind="changed", title="Over 21.5 games", rules=rules_tot)])
    res = data / "research"
    common = {"physical_match_id": PMID, "event": EV, "market_family": "MATCH_WINNER", "tour": "ATP",
              "level": "TOUR_500_250", "surface": "Hard", "predicted_at": "2026-10-01T06:00:00+00:00",
              "serve_evidence_a": 5000.0, "serve_evidence_b": 3000.0, "thinner_serve_points": 3000.0,
              "model_uncertainty": 0.03, "qualification_ok": True, "blend_weight": 0.4,
              "data_quality_score": 0.8, "data_quality_grade": "A", "asof_base_date": {"ATP": "2026-06-01"}}
    env_a = {"base": 0.56, "surface_pool_low": 0.55, "surface_pool_high": 0.57, "shrink_low": 0.54}
    _jsonl(str(res / "frozen_producers" / "shadow_board" / f"{DAY}.jsonl"), [
        {**common, "ticker": MW_A, "subject": "Alpha Aaa", "subject_is_a": True, "gen1_elo_probability": 0.58,
         "gen2_probability": 0.57, "fair_v1_probability": 0.56, "fair_envelope": env_a, "selector_decision": "WATCH"},
        {**common, "ticker": MW_B, "subject": "Beta Bbb", "subject_is_a": False, "gen1_elo_probability": 0.42,
         "gen2_probability": 0.43, "fair_v1_probability": 0.44,
         "fair_envelope": {k: 1 - v for k, v in env_a.items()}, "selector_decision": "PASS"}])
    _jsonl(str(res / "frozen_producers" / "model4" / f"{DAY}.jsonl"), [
        {"physical_match_id": PMID, "ticker": TOT, "market_family": "TOTAL_GAMES", "predicted_at": "2026-10-01T06:00:01+00:00",
         "conditioned_probability": 0.55, "fundamental_probability": 0.53}])
    _jsonl(str(res / "ledger" / f"{DAY}.jsonl"), [
        {"ticker": MW_A, "player_a": "Alpha Aaa", "player_b": "Beta Bbb", "generated_at_utc": "2026-10-01T06:00:00+00:00",
         "level": "TOUR_500_250", "surface": "Hard", "ratings_as_of": DAY,
         "models": {"ELO_DP_FAIR": 0.58, "ELO": 0.6, "STRUCTURAL": 0.55},
         "inputs": {"elo_a": 1900.0, "elo_b": 1850.0, "pa": 0.66, "pb": 0.63, "sr_pa": 0.65, "sr_pb": 0.62, "spw_baseline": 0.63},
         "quality": {"grade": "A", "data_quality_score": 0.8, "pillars": {"recency": 0.9, "experience": 0.9},
                     "inputs": {"n_matches_a": 300, "n_matches_b": 250, "days_since_last_a": 6, "days_since_last_b": 13}}}])
    _jsonl(str(res / "external" / "dislocations" / f"{DAY}.jsonl"), [
        {"generated_at": "2026-10-01T08:10:00+00:00", "kalshi_ticker": MW_A, "external_prices": {"bovada": 0.49, "smarkets": 0.5},
         "external_fair": 0.495, "reference_kind": "CONSENSUS", "triangulation": "AGREE", "external_quote_age_s": 60,
         "n_independent_groups": 2, "decision": "PASS"}])
    fb = FirstBallStore(str(data / "firstball" / "store"))
    fb.add_truth(FirstBallTruth(OTHER_EV, None, datetime(2026, 10, 1, 7, 0, tzinfo=UTC), datetime(2026, 10, 1, 7, 3, tzinfo=UTC),
                                "B", DERIVATION_EXPLICIT, created_at=datetime(2026, 10, 1, 7, 5, tzinfo=UTC)))
    store = tmp_path / "research" / "assisted_decisions"
    ensure_track_start(str(store), started_at=T_START.isoformat(), main_sha="testsha")
    slate_dir = tmp_path / "research" / "assisted_slates"
    write_slate(build_slate(str(data), now=T_SLATE), str(slate_dir))
    return {"data": str(data), "store": str(store), "slate": str(slate_dir), "research": str(tmp_path / "research"),
            "cap": str(cap), "fb": fb}


def _kw(w, now=T_DEC):
    return {"store_root": w["store"], "data_root": w["data"], "slate_dir": w["slate"], "now": now}


def _bet(**over):
    p = {"ticker": MW_A, "side": "YES", "decision": "BET", "chatgpt_fair_probability": 0.56, "chatgpt_confidence": "MEDIUM",
         "chatgpt_thesis": "A serves better on this surface than the price implies.", "factor_tags": ["SERVE_EDGE", "PRICE_VALUE"],
         "bet_up_to_price": 0.52, "stake_units_if_bet": 1.0}
    p.update(over)
    return p


def _truth(w, lower=FIRST_BALL, conf="B"):
    w["fb"].add_truth(FirstBallTruth(EV, None, lower, lower + timedelta(minutes=3), conf, DERIVATION_EXPLICIT,
                                     created_at=lower + timedelta(minutes=5)))


def _settle_world(w, result_a="yes"):
    _write_gz(os.path.join(w["cap"], "20261001T130000Z.settlements.jsonl.gz"), [
        {"ticker": MW_A, "status": "finalized", "result": result_a, "settlement_value_dollars": "1.0000" if result_a == "yes" else "0.0000",
         "settlement_ts": "2026-10-01T12:30:00Z"},
        {"ticker": MW_B, "status": "finalized", "result": "no" if result_a == "yes" else "yes",
         "settlement_value_dollars": "0.0000" if result_a == "yes" else "1.0000", "settlement_ts": "2026-10-01T12:30:00Z"},
        {"ticker": TOT, "status": "finalized", "result": "no", "settlement_value_dollars": "0.0000", "settlement_ts": "2026-10-01T12:30:00Z"}])


def _sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


# ------------------------------------------------------------------------------------------ authority, start
def test_initial_authority_state_and_write_once_track_start(tmp_path):
    assert (AUTONOMOUS_REAL_MONEY_AUTHORITY, CHATGPT_ASSISTED_TRACK) == ("OFF", "ACTIVE")
    rec = ensure_track_start(str(tmp_path), started_at="2026-10-01T00:00:00+00:00", main_sha="abc")
    assert rec["AUTONOMOUS_REAL_MONEY_AUTHORITY"] == "OFF" and rec["CHATGPT_ASSISTED_TRACK"] == "ACTIVE"
    assert "NONE" in rec["profitability_claim"]
    assert ensure_track_start(str(tmp_path), started_at="2027-01-01T00:00:00+00:00", main_sha="zzz") is None
    t = load_track_start(str(tmp_path))
    assert t["effective_start"] == "2026-10-01T00:00:00+00:00" and t["_fingerprint_ok"]
    p = tmp_path / "TRACK_START.json"
    d = json.load(open(p)); d["effective_start"] = "2020-01-01T00:00:00+00:00"; json.dump(d, open(p, "w"))
    assert not load_track_start(str(tmp_path))["_fingerprint_ok"]


def test_recording_refused_before_the_track_has_started(world, tmp_path):
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(_bet(), store_root=str(tmp_path / "empty"), data_root=world["data"], slate_dir=world["slate"], now=T_DEC)
    assert e.value.code == "TRACK_NOT_STARTED"


def test_local_pipeline_runs_never_start_the_production_track(tmp_path):
    out = subprocess.run([sys.executable, os.path.join(REPO, "scripts", "research", "run_assisted_pipeline.py"),
                          "--data-root", str(tmp_path / "data"), "--store", str(tmp_path / "store"),
                          "--scorecard-out", str(tmp_path / "sc")], capture_output=True, text=True)
    assert out.returncode == 0, out.stdout + out.stderr
    assert not (tmp_path / "store" / "TRACK_START.json").exists()
    assert json.load(open(tmp_path / "sc" / "SCORECARD.json"))["evidence_state"] == "NO_DECISIONS_YET"


# ------------------------------------------------------------------------------------------ ledger
def test_decision_ledger_is_append_only_and_write_once(world):
    rec = R.record_decision(_bet(), **_kw(world))
    store = RecordStore(world["store"])
    p = store.find("decisions", rec["decision_id"])
    before = _sha(p)
    with pytest.raises(SC.AssistedValidationError) as e:
        store.write("decisions", {**rec, "chatgpt_fair_probability": 0.9})
    assert e.value.code == "DUPLICATE_ID" and _sha(p) == before
    assert not any(hasattr(store, m) for m in ("update", "delete", "overwrite", "edit"))
    c = compile_canonical(world["store"], "decisions")
    assert c["appended"] == 1 and c["violations"] == []
    c2 = compile_canonical(world["store"], "decisions")
    assert c2["appended"] == 0 and c2["total"] == 1                     # compiling again appends nothing
    rows = AppendOnlyJsonl(os.path.join(world["store"], "assisted_decisions.jsonl")).rows()
    assert rows[0]["decision_id"] == rec["decision_id"] and rows[0]["fingerprint"] == json.load(open(p))["fingerprint"]


def test_duplicate_decisions_are_refused_never_overwritten(world):
    rec = R.record_decision(_bet(), **_kw(world))
    with pytest.raises(SC.AssistedValidationError) as e:
        R.record_decision(_bet(decision_id=rec["decision_id"], chatgpt_thesis="different"), **_kw(world))
    assert e.value.code == "DUPLICATE_ID"
    with pytest.raises(SC.AssistedValidationError) as e:                  # same content resubmitted a minute later
        R.record_decision(_bet(), **_kw(world, T_DEC + timedelta(minutes=1)))
    assert e.value.code == "DUPLICATE_SUBMISSION"
    assert len(RecordStore(world["store"]).records("decisions")) == 1


def test_decision_timestamps_are_prospective(world):
    rec = R.record_decision(_bet(created_at="2026-10-01T08:25:00+00:00"), **_kw(world))
    assert rec["created_at"] == "2026-10-01T08:25:00+00:00" and rec["recorded_at"] == T_DEC.isoformat()
    for bad, code in (({"recorded_at": "2026-10-01T08:00:00+00:00"}, "UNKNOWN_FIELD"),
                      ({"created_at": "2026-10-01T08:45:00+00:00"}, "DECISION_IN_FUTURE"),
                      ({"created_at": "2026-10-01T08:25:00"}, "INVALID_TIMESTAMP"),
                      ({"created_at": "2026-10-01T07:59:00+00:00"}, "BEFORE_TRACK_START")):
        with pytest.raises(SC.AssistedValidationError) as e:
            R.build_decision(_bet(chatgpt_thesis=str(bad), **bad), **_kw(world))
        assert e.value.code == code, (bad, e.value.code)
    with pytest.raises(SC.AssistedValidationError) as e:                  # no retroactive decisions
        R.build_decision(_bet(created_at="2026-10-01T08:10:00+00:00"), **_kw(world, T_DEC + timedelta(hours=3)))
    assert e.value.code == "RECORDED_TOO_LATE"


# ------------------------------------------------------------------------------------------ first ball
def test_pre_first_ball_admission(world):
    _truth(world)
    rec = R.record_decision(_bet(), **_kw(world))
    assert rec["first_ball_status_at_decision"] == "NOT_OBSERVED_STARTED" and rec["first_ball_source_coverage"] == "COVERED"
    assert not any(w.startswith("RECORDED_AFTER_FIRST_BALL") for w in rec["warnings"])


def test_post_start_decision_is_refused(world):
    _truth(world)
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(_bet(created_at="2026-10-01T10:01:00+00:00"), **_kw(world, datetime(2026, 10, 1, 10, 10, tzinfo=UTC)))
    assert e.value.code == "POST_START_DECISION"
    with pytest.raises(SC.AssistedValidationError) as e:                  # a match the store saw start before the slate
        R.build_decision(_bet(ticker=OTHER_EV + "-CCC"), **_kw(world))
    assert e.value.code == "POST_START_DECISION"
    # made before the first ball but written after it: admitted, flagged, excluded from the headline scorecard
    late = R.record_decision(_bet(created_at="2026-10-01T09:58:00+00:00"), **_kw(world, datetime(2026, 10, 1, 10, 10, tzinfo=UTC)))
    assert any(w.startswith("RECORDED_AFTER_FIRST_BALL") for w in late["warnings"])
    s = build_scorecard(world["store"], now=datetime(2026, 10, 1, 11, 0, tzinfo=UTC))
    assert s["total_decisions"]["excluded"] == {"recorded_after_first_ball": 1} and s["total_decisions"]["headline"] == 0


# ------------------------------------------------------------------------------------------ market identity
def test_market_identity_is_validated(world):
    cases = [(_bet(ticker="KXATPMATCH-26OCT01ZZZYYY-ZZZ"), "MARKET_NOT_FOUND"),
             (_bet(ticker="not a ticker"), "INVALID_TICKER"),
             (_bet(ticker="KXATP-26BEIJIN-ZVE"), "UNSUPPORTED_MARKET_FAMILY"),
             (_bet(event_id="KXATPMATCH-26OCT01CCCDDD"), "IDENTIFIER_MISMATCH"),
             (_bet(physical_match_id="ATP:1:2:2026-10-01"), "IDENTIFIER_MISMATCH"),
             (_bet(physical_match_id="garbage"), "IDENTIFIER_MISMATCH")]
    for p, code in cases:
        with pytest.raises(SC.AssistedValidationError) as e:
            R.build_decision(p, **_kw(world))
        assert e.value.code == code, (p, e.value.code)
    rec = R.build_decision(_bet(event_id=EV, physical_match_id=PMID), **_kw(world))
    assert (rec["event_id"], rec["physical_match_id"], rec["match_code"]) == (EV, PMID, "26OCT01AAABBB")
    assert rec["players"] == {"a": "Alpha Aaa", "b": "Beta Bbb"} and rec["level_bucket"] == "ATP"


def test_market_price_at_decision_time_is_preserved(world):
    rec = R.build_decision(_bet(), **_kw(world))                            # capture quote at 08:30 = the 08:00 pass
    assert (rec["kalshi_bid"], rec["kalshi_ask"], rec["side_entry_price"]) == (0.47, 0.48, 0.48)
    assert rec["market_quote_source"] == "CAPTURE" and rec["market_quote_observed_at"] == T_FULL.isoformat()
    assert rec["market_implied_probability"] == pytest.approx(0.475) and rec["fee"] == 0.02
    live = R.build_decision(_bet(kalshi_bid=0.46, kalshi_ask=0.47, chatgpt_thesis="live"), **_kw(world))
    assert live["market_quote_source"] == "INPUT_OBSERVED_LIVE" and live["side_entry_price"] == 0.47
    assert live["repo_market_at_decision"]["yes_ask"] == 0.48              # the repo's own view is kept beside it
    no = R.build_decision(_bet(side="NO", chatgpt_fair_probability=0.4, chatgpt_thesis="no side"), **_kw(world))
    assert no["side_entry_price"] == pytest.approx(0.53)                   # NO ask = 1 - YES bid


# ------------------------------------------------------------------------------------------ immutability
def test_thesis_is_immutable(world):
    rec = R.record_decision(_bet(), **_kw(world))
    compile_canonical(world["store"], "decisions")
    p = RecordStore(world["store"]).find("decisions", rec["decision_id"])
    d = json.load(open(p)); orig = dict(d)
    d["chatgpt_thesis"] = "rewritten with hindsight"
    json.dump(d, open(p, "w"))
    assert changed_immutable_fields(orig, d, SC.IMMUTABLE_DECISION_FIELDS) == ["chatgpt_thesis"]
    assert not RecordStore(world["store"]).records("decisions")[0]["_fingerprint_ok"]
    c = compile_canonical(world["store"], "decisions")
    assert any("modified after it was written" in v for v in c["violations"])
    assert any("immutable fields changed" in v for v in c["violations"])


def test_probability_is_immutable_and_canonical_rows_cannot_be_rewritten(world):
    rec = R.record_decision(_bet(), **_kw(world))
    compile_canonical(world["store"], "decisions")
    path = os.path.join(world["store"], "assisted_decisions.jsonl")
    row = json.loads(open(path).read())
    row["chatgpt_fair_probability"] = 0.99
    open(path, "w").write(json.dumps(row) + "\n")
    assert AppendOnlyJsonl(path).verify_chain()
    p = RecordStore(world["store"]).find("decisions", rec["decision_id"])
    d = json.load(open(p)); d["chatgpt_fair_probability"] = 0.99; json.dump(d, open(p, "w"))
    assert changed_immutable_fields(rec, d, SC.IMMUTABLE_DECISION_FIELDS) == ["chatgpt_fair_probability"]
    status, detail = gate_16(world["research"], now=T_DEC)
    assert status == "FAIL" and "INTEGRITY_VIOLATION" in detail["failing"]
    assert set(SC.IMMUTABLE_DECISION_FIELDS) >= {"chatgpt_fair_probability", "chatgpt_thesis", "factor_tags", "chosen_expression",
                                                  "bet_up_to_price", "chatgpt_confidence", "decision", "kalshi_ask"}


# ------------------------------------------------------------------------------------------ wagers
def test_wager_linkage_is_explicit(world):
    rec = R.record_decision(_bet(), **_kw(world))
    assert rec["actual_wagered"] is False and RecordStore(world["store"]).records("wagers") == []
    wk = {"store_root": world["store"], "data_root": world["data"], "now": T_DEC + timedelta(minutes=5)}
    for p, code in (({"decision_id": "AD-20261001-000000000000", "placed_at": "2026-10-01T08:31:00+00:00", "entry_price": 0.48, "contracts": 10}, "UNKNOWN_DECISION"),
                    ({"decision_id": rec["decision_id"], "ticker": MW_B, "placed_at": "2026-10-01T08:31:00+00:00", "entry_price": 0.48, "contracts": 10}, "WAGER_MARKET_MISMATCH"),
                    ({"decision_id": rec["decision_id"], "placed_at": "2026-10-01T08:31:00+00:00", "entry_price": 0.48, "contracts": 10, "stake_dollars": 9.0}, "STAKE_MISMATCH"),
                    ({"decision_id": rec["decision_id"], "placed_at": "2026-10-01T08:00:00+00:00", "entry_price": 0.48, "contracts": 10}, "INVALID_TIMESTAMP")):
        with pytest.raises(SC.AssistedValidationError) as e:
            R.build_wager(p, **wk)
        assert e.value.code == code, (p, e.value.code)
    w = R.record_wager({"decision_id": rec["decision_id"], "placed_at": "2026-10-01T08:31:00+00:00", "entry_price": 0.48,
                        "contracts": 10, "external_order_id": "kalshi-123"}, **wk)
    assert set(w) == set(SC.WAGER_FIELDS)
    assert (w["stake_dollars"], w["fees"], w["status"], w["source"], w["decision_was_bet"]) == (4.8, 0.18, "FILLED", "MANUAL_KALSHI_UI", True)
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_wager({"decision_id": rec["decision_id"], "placed_at": "2026-10-01T08:32:00+00:00", "entry_price": 0.48,
                       "contracts": 5, "external_order_id": "kalshi-123"}, **wk)
    assert e.value.code == "DUPLICATE_SUBMISSION"
    watch = R.record_decision({"ticker": TOT, "decision": "WATCH", "side": "YES", "chatgpt_fair_probability": 0.5,
                               "chatgpt_thesis": "wait for a better number"}, **_kw(world))
    w2 = R.record_wager({"decision_id": watch["decision_id"], "placed_at": "2026-10-01T08:33:00+00:00",
                         "entry_price": 0.46, "contracts": 1}, **wk)
    assert w2["decision_was_bet"] is False and w2["warnings"][0].startswith("DECISION_WAS_WATCH")
    assert json.load(open(RecordStore(world["store"]).find("decisions", rec["decision_id"])))["actual_wagered"] is False


# ------------------------------------------------------------------------------------------ settlement
def test_settlement_attaches_without_touching_the_decision(world):
    _truth(world)
    rec = R.record_decision(_bet(), **_kw(world))
    R.record_wager({"decision_id": rec["decision_id"], "placed_at": "2026-10-01T08:31:00+00:00", "entry_price": 0.48,
                    "contracts": 10}, store_root=world["store"], data_root=world["data"], now=T_DEC + timedelta(minutes=2))
    p = RecordStore(world["store"]).find("decisions", rec["decision_id"])
    before = _sha(p)
    assert settle(world["store"], world["data"], now=datetime(2026, 10, 1, 11, tzinfo=UTC))["appended"] == 0   # not settled yet
    _settle_world(world, "yes")
    out = settle(world["store"], world["data"], now=datetime(2026, 10, 1, 14, tzinfo=UTC))
    assert out["appended"] == 2 and _sha(p) == before
    s = latest_settlements(world["store"])
    d = s[("DECISION", rec["decision_id"], None)]
    assert set(SC.SETTLEMENT_FIELDS) <= set(d)
    assert (d["settlement_result"], d["side_won"], d["gross_pnl"], d["fees"]) == ("YES", True, 0.52, 0.02)
    assert d["net_pnl"] == pytest.approx(0.50) and d["roi"] == pytest.approx(0.5 / 0.5)
    wr = [v for k, v in s.items() if k[0] == "WAGER"][0]
    assert wr["net_pnl"] == pytest.approx(10 * 0.52 - 0.18) and wr["pnl_unit"] == "ACTUAL_WAGER_DOLLARS"
    assert settle(world["store"], world["data"], now=datetime(2026, 10, 1, 15, tzinfo=UTC))["appended"] == 0   # idempotent
    assert AppendOnlyJsonl(os.path.join(world["store"], "assisted_settlements.jsonl")).verify_chain() == []


def test_strict_clv_linkage(world):
    _truth(world)
    yes = R.record_decision(_bet(), **_kw(world))
    no = R.record_decision(_bet(ticker=MW_B, side="NO", chatgpt_fair_probability=0.44, chatgpt_thesis="B overpriced"), **_kw(world))
    _settle_world(world, "yes")
    settle(world["store"], world["data"], now=datetime(2026, 10, 1, 14, tzinfo=UTC))
    s = latest_settlements(world["store"])
    d = s[("DECISION", yes["decision_id"], None)]
    # close = last executable quote before the A/B first-ball lower bound (the 09:00 pass: 0.50/0.51)
    assert d["strict_close"]["ts"] == T_LATE.isoformat() and d["strict_close"]["basis"] == "FIRST_BALL_BRACKET_LOWER"
    assert d["strict_executable_clv"] == pytest.approx(0.50 - 0.48) and d["midpoint_clv"] == pytest.approx(0.505 - 0.475)
    assert d["clv_timing_class"] == "STRICT_PREGAME" and d["first_ball_confidence"] == "B"
    n = s[("DECISION", no["decision_id"], None)]
    # NO on B: entry NO ask = 1 - 0.52; close NO bid = 1 - 0.50
    assert n["strict_executable_clv"] == pytest.approx((1 - 0.50) - (1 - 0.52))
    assert n["side_won"] is True                                           # B lost, so NO on B won


def test_no_first_ball_truth_means_no_strict_clv(world):
    rec = R.record_decision(_bet(), **_kw(world))
    _settle_world(world, "no")
    settle(world["store"], world["data"], now=datetime(2026, 10, 1, 14, tzinfo=UTC))
    d = latest_settlements(world["store"])[("DECISION", rec["decision_id"], None)]
    assert d["strict_executable_clv"] is None and d["strict_close"] is None and "not A/B" in d["clv_exclusion_reason"]
    assert d["side_won"] is False and d["net_pnl"] == pytest.approx(-0.50)
    _truth(world)                                                          # truth recovered later: ONE revision row
    settle(world["store"], world["data"], now=datetime(2026, 10, 2, 14, tzinfo=UTC))
    rows = [r for r in AppendOnlyJsonl(os.path.join(world["store"], "assisted_settlements.jsonl")).rows()
            if r["decision_id"] == rec["decision_id"]]
    assert [r["revision"] for r in rows] == [1, 2] and rows[1]["supersedes"] == rows[0]["settlement_id"]
    assert rows[0]["strict_executable_clv"] is None and rows[1]["strict_executable_clv"] == pytest.approx(0.02)


# ------------------------------------------------------------------------------------------ passes, agreement
def test_pass_decisions_are_preserved_and_scored(world):
    _truth(world)
    ps = R.record_decision({"ticker": MW_A, "decision": "PASS", "chatgpt_fair_probability": 0.49,
                            "pass_reason_if_pass": "external consensus sides with Kalshi"}, **_kw(world))
    assert ps["decision"] == "PASS" and ps["side"] is None and ps["stake_units_if_bet"] is None
    assert ps["model_preferred_side"] == "YES" and ps["model_agreement_state"] == SC.OVERRULED_MODEL
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision({"ticker": MW_B, "decision": "PASS"}, **_kw(world))
    assert e.value.code == "MISSING_FIELD"                                 # a PASS must say why
    _settle_world(world, "no")
    settle(world["store"], world["data"], now=datetime(2026, 10, 1, 14, tzinfo=UTC))
    compile_canonical(world["store"], "decisions")
    assert [r["decision"] for r in AppendOnlyJsonl(os.path.join(world["store"], "assisted_decisions.jsonl")).rows()] == ["PASS"]
    s = build_scorecard(world["store"], now=datetime(2026, 10, 1, 15, tzinfo=UTC))
    assert s["passes"]["passes"] == 1 and s["passes"]["passed_positive_model_edge"] == 1 and s["passes"]["settled"] == 1
    assert s["passes"]["hypothetical_model_side_net_per_contract"]["mean"] == pytest.approx(-0.50)   # the declined edge lost


def test_override_and_agreement_classification(world):
    assert SC.preferred_side(0.56, 0.47, 0.48) == "YES"
    assert SC.preferred_side(0.40, 0.47, 0.48) == "NO"
    assert SC.preferred_side(0.475, 0.47, 0.48) == "NEUTRAL" and SC.preferred_side(None, 0.47, 0.48) == "NONE"
    assert SC.classify_agreement("BET", "YES", "YES") == SC.AGREED_WITH_MODEL
    assert SC.classify_agreement("BET", "YES", "NO") == SC.OVERRULED_MODEL
    assert SC.classify_agreement("BET", "NEUTRAL", "YES") == SC.MODEL_NEUTRAL
    assert SC.classify_agreement("BET", "NONE", "NO") == SC.MODEL_NEUTRAL
    assert SC.classify_agreement("PASS", "NEUTRAL", "NONE") == SC.MODEL_AND_CHATGPT_BOTH_PASS
    assert SC.classify_agreement("PASS", "NO", "NONE") == SC.OVERRULED_MODEL
    agree = R.build_decision(_bet(), **_kw(world))
    assert (agree["model_preferred_side"], agree["chatgpt_preferred_side"], agree["model_agreement_state"]) == ("YES", "YES", SC.AGREED_WITH_MODEL)
    assert agree["model_probability_yes"] == 0.56 and agree["model_probability_source"] == "fair_v1"
    over = R.build_decision(_bet(side="NO", chatgpt_fair_probability=0.40, chatgpt_thesis="fade"), **_kw(world))
    assert over["model_agreement_state"] == SC.OVERRULED_MODEL and over["chatgpt_preferred_side"] == "NO"
    neutral = R.build_decision(_bet(fair_v1_probability=0.475, chatgpt_thesis="neutral"), **_kw(world))
    assert neutral["model_agreement_state"] == SC.MODEL_NEUTRAL and neutral["model_context_source"]["fields_from_input"] == ["fair_v1_probability"]


def test_factor_tag_validation(world):
    for tags in (["VIBES"], ["SERVE_EDGE", "SERVE_EDGE"], "SERVE_EDGE"):
        with pytest.raises(SC.AssistedValidationError) as e:
            R.build_decision(_bet(factor_tags=tags, chatgpt_thesis=str(tags)), **_kw(world))
        assert e.value.code == "INVALID_FACTOR_TAG"
    assert R.build_decision(_bet(factor_tags=[], chatgpt_thesis="no tag forced"), **_kw(world))["factor_tags"] == []
    assert R.build_decision(_bet(factor_tags=["lefty_righty", "OTHER"], chatgpt_thesis="lc"), **_kw(world))["factor_tags"] == ["LEFTY_RIGHTY", "OTHER"]
    assert len(SC.FACTOR_TAGS) == 23 and "DERIVATIVE_VALUE" in SC.FACTOR_TAGS


def test_market_expression(world):
    rec = R.build_decision(_bet(ticker=TOT, chatgpt_fair_probability=0.55, primary_match_thesis="long, even match",
                                why_chosen_expression_best_matches_thesis="the total captures closeness without picking a side",
                                chatgpt_thesis="totals"), **_kw(world))
    assert rec["chosen_expression"] == "TOTAL_GAMES" and rec["market_family"] == "TOTAL_GAMES"
    assert rec["available_expressions"] == ["MATCH_WINNER", "TOTAL_GAMES"]
    assert rec["model4_probability_if_applicable"] == 0.55 and rec["model_probability_source"] == "market_conditioned_v1"
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(_bet(ticker=TOT, chosen_expression="MATCH_WINNER", chatgpt_thesis="x"), **_kw(world))
    assert e.value.code == "EXPRESSION_MISMATCH"
    assert SC.expression_of_family("SET_SPREAD") == "PLAYER_SET_HANDICAP"
    assert SC.expression_of_family("TIEBREAK_OCCURS") == "OTHER_SUPPORTED_KALSHI_MARKET"
    assert SC.expression_of_family("TOURNAMENT_WINNER") is None


def test_decision_record_carries_the_exact_schema(world):
    rec = R.build_decision(_bet(), **_kw(world))
    assert list(rec) == SC.DECISION_FIELDS
    assert rec["automated_execution"] is False and rec["autonomous_real_money_authority"] == "OFF"
    assert (rec["gen1_probability"], rec["gen2_probability"], rec["fair_v1_probability"]) == (0.58, 0.57, 0.56)
    assert (rec["serve_evidence_player_a"], rec["serve_evidence_player_b"]) == (5000.0, 3000.0)
    assert rec["rating_state"]["elo_a"] == 1900.0 and rec["recent_form_inputs"]["days_since_last_match_b"] == 13
    assert rec["bovada_probability_if_available"] == 0.49 and rec["triangulation_state"] == "AGREE"
    assert rec["selector_state"] == "WATCH" and rec["slate_id"].startswith("SL-")


# ------------------------------------------------------------------------------------------ slate
def test_slate_export(world):
    s = json.load(open(os.path.join(world["slate"], "latest.json")))
    assert s["AUTONOMOUS_REAL_MONEY_AUTHORITY"] == "OFF" and s["CHATGPT_ASSISTED_TRACK"] == "ACTIVE"
    assert [m["event_id"] for m in s["matches"]] == [EV]                  # started match and futures left off
    assert s["counts"]["skipped_matches"] == {"first_ball_already_observed": 1}
    m = s["matches"][0]
    assert m["players"] == {"a": "Alpha Aaa", "b": "Beta Bbb"} and m["level_bucket"] == "ATP" and m["surface"] == "Hard"
    assert m["first_ball"]["status"] == "NOT_OBSERVED_STARTED"
    mc = m["model_context"]
    assert mc["player_a_win"] == {"gen1": 0.58, "gen2": 0.57, "fair_v1": 0.56, "fair_v1_envelope": [0.54, 0.57]}
    assert mc["serve_evidence"]["player_a_points"] == 5000.0 and mc["rating_state"]["serve_point_win_a"] == 0.66
    assert mc["surface_adjustment"]["surface_pool_low"] == pytest.approx(-0.01)
    assert mc["recent_form_inputs"]["days_since_last_match_a"] == 6
    rows = {r["ticker"]: r for r in m["markets"]}
    assert set(rows) == {MW_A, MW_B, TOT}
    a = rows[MW_A]
    assert a["kalshi"]["bid"] == 0.50 and a["kalshi"]["ask"] == 0.51            # carry-forward board at the latest pass
    assert a["external"]["bovada"] == 0.49 and a["external"]["triangulation"] == "AGREE"
    assert a["model"]["selector_v1"] == "WATCH" and a["observed_by"] == ["gen1_ledger", "shadow_board_v1", "external_scan"]
    assert rows[TOT]["model"]["model4_conditioned"] == 0.55 and rows[TOT]["expression"] == "TOTAL_GAMES"
    for r in m["markets"]:                                                 # a packet, not a selector
        assert not {"decision", "recommendation", "stake", "bet"} & set(r)
    md = open(os.path.join(world["slate"], "latest.md")).read()
    assert "AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF" in md and MW_A in md and "selects nothing" in md
    assert render_markdown(s) == md
    assert json.loads(open(os.path.join(world["slate"], "slate_runs.jsonl")).readline())["slate_id"] == s["slate_id"]


# ------------------------------------------------------------------------------------------ scorecard
def test_scorecard_is_reproducible(world, tmp_path):
    _truth(world)
    rec = R.record_decision(_bet(), **_kw(world))
    R.record_decision({"ticker": TOT, "decision": "WATCH", "side": "YES", "chatgpt_fair_probability": 0.5,
                       "chatgpt_thesis": "watch the total"}, **_kw(world))
    R.record_wager({"decision_id": rec["decision_id"], "placed_at": "2026-10-01T08:31:00+00:00", "entry_price": 0.48,
                    "contracts": 10}, store_root=world["store"], data_root=world["data"], now=T_DEC + timedelta(minutes=2))
    _settle_world(world, "yes")
    settle(world["store"], world["data"], now=datetime(2026, 10, 1, 14, tzinfo=UTC))
    a = build_scorecard(world["store"], now=datetime(2026, 10, 1, 15, tzinfo=UTC))
    b = build_scorecard(world["store"], now=datetime(2026, 10, 2, 9, tzinfo=UTC))
    assert a["content_sha256"] == b["content_sha256"] and a["inputs_sha256"] == b["inputs_sha256"]
    assert a["total_decisions"]["bets"] == 1 and a["total_decisions"]["watches"] == 1
    assert a["actual_wagers"]["number"] == 1 and a["actual_wagers"]["wins"] == 1
    assert a["actual_wagers"]["net_pnl_dollars"] == pytest.approx(5.02)
    assert a["pricing"]["strict_executable_clv"]["mean"] == pytest.approx(0.02)
    assert a["probability_quality"]["chatgpt"]["n"] == 2 and a["agreement"]["n"] == 1
    assert a["expression"]["MATCH_WINNER"]["settled"] == 1 and a["factors"]["SERVE_EDGE"]["n"] == 1
    assert a["level"]["ATP"]["n"] == 1 and a["surface"]["HARD"]["n"] == 1
    assert len(a["ceo"]) == 10 and all("INSUFFICIENT_EVIDENCE" in x["a"] or "NONE_IDENTIFIED" in x["a"] for x in a["ceo"])
    for key in ("total_decisions", "actual_wagers", "pricing", "probability_quality", "selective_disagreement", "agreement",
                "overrides", "model_follow", "passes", "expression", "factors", "level", "surface"):
        assert key in a
    write_scorecard(a, str(tmp_path / "sc"))
    assert "CEO scoreboard" in open(tmp_path / "sc" / "SCORECARD.md").read()


def test_scorecard_unit_is_the_decision_not_raw_model_rows(world):
    # thousands of frozen-producer rows exist on the same board; none of them enters the assisted scorecard
    _jsonl(os.path.join(world["data"], "research", "frozen_producers", "shadow_board", f"{DAY}.jsonl"),
           [{"ticker": f"{EV}-X{i}", "predicted_at": "2026-10-01T06:00:00+00:00"} for i in range(2000)])
    R.record_decision(_bet(), **_kw(world))
    s = build_scorecard(world["store"], now=T_DEC)
    assert s["total_decisions"]["recorded"] == 1 and s["probability_quality"]["model"]["n"] == 0


# ------------------------------------------------------------------------------------------ postmortems, evidence
def test_postmortem_and_later_evidence_never_touch_the_decision(world):
    rec = R.record_decision(_bet(), **_kw(world))
    p = RecordStore(world["store"]).find("decisions", rec["decision_id"])
    before = _sha(p)
    pm = R.record_postmortem({"decision_id": rec["decision_id"], "result": "LOSS", "what_thesis_got_wrong": "return games",
                              "whether_loss_was_process_or_variance": "VARIANCE",
                              "potential_research_question": "does serve evidence decay faster indoors?"},
                             store_root=world["store"], now=T_DEC + timedelta(hours=6))
    assert pm["use_restriction"].startswith("HYPOTHESIS_GENERATION_ONLY") and set(pm) == set(SC.POSTMORTEM_FIELDS)
    ev = R.record_evidence({"decision_id": rec["decision_id"], "evidence": "withdrew from doubles the night before",
                            "discovered_at": "2026-10-01T09:00:00+00:00", "bears_on": ["FATIGUE"]},
                           store_root=world["store"], now=T_DEC + timedelta(hours=1))
    assert ev["decision_id"] == rec["decision_id"]
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_evidence({"decision_id": rec["decision_id"], "evidence": "x", "discovered_at": "2026-10-01T08:00:00+00:00"},
                         store_root=world["store"], now=T_DEC + timedelta(hours=1))
    assert e.value.code == "INVALID_TIMESTAMP"
    with pytest.raises(SC.AssistedValidationError):
        R.build_postmortem({"decision_id": rec["decision_id"], "result": "LOSS", "whether_loss_was_process_or_variance": "BAD_LUCK"},
                           store_root=world["store"])
    assert _sha(p) == before
    for k in ("postmortems", "evidence"):
        assert compile_canonical(world["store"], k)["appended"] == 1


# ------------------------------------------------------------------------------------------ TENNIS-16
def test_tennis_16_operations_gate(world):
    status, d = gate_16(world["research"], now=T_DEC)
    assert status == "FAIL" and "PIPELINE_STALE" in d["failing"]           # the scored half has not run yet
    subprocess.run([sys.executable, os.path.join(REPO, "scripts", "research", "run_assisted_pipeline.py"), "--data-root",
                    world["data"], "--store", world["store"], "--scorecard-out", os.path.join(world["research"], "sc")],
                   check=True, capture_output=True)
    now = datetime.now(timezone.utc)
    with open(os.path.join(world["slate"], "slate_runs.jsonl"), "a") as f:
        f.write(json.dumps({"slate_id": "SL-x", "built_at": now.isoformat(), "matches": 1}) + "\n")
    status, d = gate_16(world["research"], now=now)
    assert status == "PASS" and d["health"] == "HEALTHY_NO_DECISIONS_YET" and d["gate_kind"].startswith("OPERATIONS")
    assert d["AUTONOMOUS_REAL_MONEY_AUTHORITY"] == "OFF" and d["CHATGPT_ASSISTED_TRACK"] == "ACTIVE"
    for k in ("latest_slate_build", "latest_assisted_decision", "settlement_freshness", "unsettled_decisions",
              "strict_clv_coverage", "schema_validity", "duplicate_decisions", "post_start_decision_violations"):
        assert k in d
    status, d = gate_16(world["research"], now=now + timedelta(hours=14))
    assert status == "FAIL" and {"SLATE_STALE", "PIPELINE_STALE"} <= set(d["failing"])
    status, d = gate_16(os.path.join(world["research"], "nowhere"), now=now)
    assert status == "UNKNOWN"


def test_tennis_16_is_in_the_health_run_and_separate_from_tennis_15():
    from tennis_edge.health import gates as G
    names = [g.gate for g in G.run_all()]
    assert names[-3:] == ["TENNIS-15", "TENNIS-16", "TENNIS-17"]          # TENNIS-17: discrepancy integrity
    assert "TENNIS-16" not in G.CANDIDATE_PRODUCERS.values()


# ------------------------------------------------------------------------------------------ no frozen change
def test_no_autonomous_model_or_frozen_candidate_changes():
    from tests.test_frozen_producers import FROZEN_CANDIDATES, FROZEN_SOURCES
    for rel, h in FROZEN_SOURCES.items():
        assert _sha(os.path.join(REPO, rel)) == h, rel
    cdir = os.path.join(REPO, "data", "research", "edge_candidates")
    assert sorted(os.listdir(cdir)) == sorted(FROZEN_CANDIDATES)
    for fn, h in FROZEN_CANDIDATES.items():
        assert _sha(os.path.join(cdir, fn)) == h, fn


def test_assisted_lane_cannot_write_models_candidates_or_starts():
    pkg = os.path.join(REPO, "tennis_edge", "assisted")
    srcs = {fn: open(os.path.join(pkg, fn)).read() for fn in os.listdir(pkg) if fn.endswith(".py")}
    for s in ("run_assisted_pipeline.py", "record_assisted_decision.py", "build_assisted_slate.py"):
        srcs[s] = open(os.path.join(REPO, "scripts", "research", s)).read()
    for fn, src in srcs.items():
        for forbidden in ("edge_candidates", "experiment_starts", "ensure_experiment_starts",
                          "tennis_edge.models", "tennis_edge.selector", ".fit(", "PERTURBATIONS", "place_order",
                          "create_order", "auth_adapter"):
            assert forbidden not in src, (fn, forbidden)
    # the slate READS producer stores; nothing in the lane opens one for writing
    assert "ProducerStore" not in "".join(srcs.values())


def test_pipeline_leaves_frozen_evidence_untouched(world):
    starts = os.path.join(world["research"], "experiment_starts")
    os.makedirs(starts)
    open(os.path.join(starts, "W3-2026-001-ABSTAIN-ITF.json"), "w").write('{"x": 1}')
    sb = os.path.join(world["data"], "research", "frozen_producers", "shadow_board", f"{DAY}.jsonl")
    before = (_sha(os.path.join(starts, "W3-2026-001-ABSTAIN-ITF.json")), _sha(sb))
    R.record_decision(_bet(), **_kw(world))
    subprocess.run([sys.executable, os.path.join(REPO, "scripts", "research", "run_assisted_pipeline.py"), "--data-root",
                    world["data"], "--store", world["store"], "--scorecard-out", os.path.join(world["research"], "sc")],
                   check=True, capture_output=True)
    write_slate(build_slate(world["data"], now=T_DEC), world["slate"])
    assert (_sha(os.path.join(starts, "W3-2026-001-ABSTAIN-ITF.json")), _sha(sb)) == before


def test_no_historical_assisted_decisions_are_reconstructed():
    # nothing ships in the code repository: every assisted record is written prospectively on tennis-data
    tracked = subprocess.run(["git", "ls-files", "data/research/assisted_decisions", "data/research/assisted_slates"],
                             cwd=REPO, capture_output=True, text=True).stdout.strip()
    assert tracked == ""
    gi = open(os.path.join(REPO, ".gitignore")).read()
    assert "data/research/assisted_decisions/" in gi and "data/research/assisted_slates/" in gi


# ------------------------------------------------------------------------------------------ workflows, CLI
def test_workflows_wire_the_lane_beside_the_frozen_producers():
    y = open(os.path.join(REPO, ".github", "workflows", "tennis-run.yml")).read()
    i_h, i_sl, i_pipe, i_health = (y.index("harvest_candidate_evidence.py --data-root"), y.index("build_assisted_slate.py"),
                                   y.index("run_assisted_pipeline.py --write-track-start"), y.index("run_all()"))
    assert i_h < i_sl < i_pipe < i_health
    r = open(os.path.join(REPO, ".github", "workflows", "tennis-assisted-record.yml")).read()
    assert "PAYLOAD: ${{ inputs.payload }}" in r and "--no-overwrite" in r and "assisted_decisions/records" in r
    assert "${{ inputs.payload }}\"" not in r.split("env:")[0]            # never interpolated into the shell
    assert "--no-overwrite" in open(os.path.join(REPO, "scripts", "ci", "publish_branch.py")).read()


def test_cli_records_and_refuses(world):
    cli = os.path.join(REPO, "scripts", "research", "record_assisted_decision.py")
    t = subprocess.run([sys.executable, cli, "--template", "decision"], capture_output=True, text=True)
    assert json.loads(t.stdout)["decision"] == "BET"
    bad = subprocess.run([sys.executable, cli, "--store", world["store"], "--data-root", world["data"], "--slate-dir",
                          world["slate"], "--json", json.dumps(_bet(ticker="KXATP-26BEIJIN-ZVE"))], capture_output=True, text=True)
    assert bad.returncode == 2 and json.loads(bad.stdout)["code"] == "UNSUPPORTED_MARKET_FAMILY"


def test_publish_no_overwrite_refuses_to_replace_a_record_on_the_branch(tmp_path):
    def git(*a, cwd):
        subprocess.run(["git", *a], cwd=cwd, check=True, capture_output=True)
    origin, seed, repo = tmp_path / "origin.git", tmp_path / "seed", tmp_path / "repo"
    git("init", "-q", "--bare", str(origin), cwd=tmp_path)
    for d in (seed, repo):
        git("init", "-q", "-b", "main", str(d), cwd=tmp_path)
        git("config", "user.email", "t@example.com", cwd=d); git("config", "user.name", "t", cwd=d)
        git("remote", "add", "origin", str(origin), cwd=d)
    rel = "tennis-edge-finder/data/research/assisted_decisions/records/decisions/2026-10-01"
    (seed / rel).mkdir(parents=True)
    (seed / rel / "AD-20261001-aaaaaaaaaaaa.json").write_text('{"original": true}\n')
    git("checkout", "-q", "--orphan", "tennis-data", cwd=seed); git("add", "-A", cwd=seed)
    git("commit", "-q", "-m", "seed", cwd=seed); git("push", "-q", "origin", "tennis-data", cwd=seed)
    (repo / "seed.txt").write_text("x\n"); git("add", "-A", cwd=repo); git("commit", "-q", "-m", "m", cwd=repo)
    local = repo / "data" / "research" / "assisted_decisions" / "records" / "decisions" / "2026-10-01"
    local.mkdir(parents=True)
    (local / "AD-20261001-aaaaaaaaaaaa.json").write_text('{"tampered": true}\n')
    pub = [sys.executable, os.path.join(REPO, "scripts", "ci", "publish_branch.py"), "--repo", str(repo), "--no-overwrite",
           "--src", "data/research/assisted_decisions/records", "--message", "m", "--attempts", "1"]
    r = subprocess.run(pub, capture_output=True, text=True)
    assert r.returncode == 4 and "write-once file already on tennis-data" in r.stdout
    (local / "AD-20261001-aaaaaaaaaaaa.json").write_text('{"original": true}\n')          # identical copy: fine
    (local / "AD-20261001-bbbbbbbbbbbb.json").write_text('{"new": true}\n')
    r = subprocess.run(pub, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    shown = subprocess.run(["git", "--git-dir", str(origin), "show", f"tennis-data:{rel}/AD-20261001-aaaaaaaaaaaa.json"],
                           capture_output=True, text=True).stdout
    assert json.loads(shown) == {"original": True}
    assert subprocess.run(["git", "--git-dir", str(origin), "show", f"tennis-data:{rel}/AD-20261001-bbbbbbbbbbbb.json"],
                          capture_output=True, text=True).returncode == 0
