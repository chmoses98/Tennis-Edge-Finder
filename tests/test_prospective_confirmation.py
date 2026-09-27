"""Prospective confirmation layer: the frozen rules, applied exactly, to what was captured after the freeze."""
import gzip
import inspect
import json
import os
import shutil
import sys
from datetime import datetime, timedelta, timezone

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tennis_edge.confirmation import candidates as C
from tennis_edge.confirmation import evidence as ev
from tennis_edge.confirmation import sources as src
from tennis_edge.confirmation import stats
from tennis_edge.confirmation import status as S
from tennis_edge.firstball.truth import FirstBallTruth, DERIVATION_EXPLICIT, DERIVATION_SCORE_BACKCAST
from tennis_edge.ledger.quotes import book_top
from tennis_edge.pricing.fees import taker_fee

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FROZEN = os.path.join(REPO, "data", "research", "edge_candidates")
W4_ID = "W4-2026-001-KALSHI-LONE-OUTLIER"
T_FREEZE = "2026-09-12T21:09:38.644348+00:00"


# ------------------------------------------------------------------------------------------ fixtures
def _iso(dt):
    return dt.isoformat()


def w4_row(at, ticker="KXWTAMATCH-26SEP19AAABBB-AAA", ask=0.40, bid=0.39, ext=0.45, tri="KALSHI_LONE_OUTLIER",
           size=50.0, qage=100.0, sources=("bovada",)):
    fee = taker_fee(ask, 1.0)
    return {"generated_at": at, "physical_match_id": "WTA:1:2:2026-09-19", "kalshi_ticker": ticker,
            "kalshi_event": ticker.rsplit("-", 1)[0], "side": "Player A", "market_family": "MATCH_WINNER",
            "kalshi_bid": bid, "kalshi_ask": ask, "kalshi_mid": 0.5 * (ask + bid), "kalshi_size": size,
            "kalshi_spread": ask - bid, "kalshi_fee": fee, "kalshi_quote_age_s": qage,
            "external_sources": list(sources), "external_prices": {s: ext for s in sources},
            "external_fair": ext, "triangulation": tri, "external_edge": ext - ask - fee,
            "model_fair": 0.44, "decision": "SHADOW_BET", "selector_version": "external_v1",
            "row_hash": f"h-{ticker}-{at}"}


def ext_obs(at, source, p, venue_ts):
    return {"source": source, "source_kind": "EXCHANGE" if source == "smarkets" else "SPORTSBOOK",
            "observed_at": at, "market_family": "MATCH_WINNER", "devigged_probability": p,
            "source_timestamp": venue_ts, "source_margin": 0.03}


def build_root(tmp, rows, obs, quotes=(), settlements=()):
    d = tmp / "data"
    (d / "research" / "external" / "dislocations").mkdir(parents=True)
    (d / "research" / "external" / "market").mkdir(parents=True)
    (d / "kalshi" / "capture" / "2026-09-19").mkdir(parents=True)
    with open(d / "research" / "external" / "dislocations" / "2026-09-19.jsonl", "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    with open(d / "research" / "external" / "market" / "2026-09-19.jsonl", "w") as f:
        for o in obs:
            f.write(json.dumps(o) + "\n")
    with gzip.open(d / "kalshi" / "capture" / "2026-09-19" / "20260919T000000Z.quotes.jsonl.gz", "wt") as f:
        for q in quotes:
            f.write(json.dumps(q) + "\n")
    with gzip.open(d / "kalshi" / "capture" / "2026-09-19" / "20260919T000000Z.settlements.jsonl.gz", "wt") as f:
        for s in settlements:
            f.write(json.dumps(s) + "\n")
    return str(d)


def truth_ab(match_id, first_ball, conf="B"):
    return FirstBallTruth(match_id, None, first_ball, first_ball + timedelta(minutes=3), conf, DERIVATION_EXPLICIT,
                          created_at=first_ball, evidence_payload_hash="fbhash")


def ctx_for(root, truths=None):
    capture = os.path.join(root, "kalshi", "capture")
    return C.Context(data_root=root, candidates={}, truths=truths or {},
                     settlements=src.settlements(capture), capture_root=capture)


def w4_cand():
    return src.load_candidates(FROZEN)[W4_ID]


START = datetime(2026, 9, 19, 12, 0, tzinfo=timezone.utc)


def _standard_case(tmp_path, truth_conf="B", first_ball=START, settle="yes"):
    at1 = _iso(START - timedelta(hours=3))
    at2 = _iso(START - timedelta(hours=2))
    rows = [w4_row(_iso(datetime(2026, 9, 12, 20, tzinfo=timezone.utc))),      # before the W4 freeze
            w4_row(at1), w4_row(at2, ask=0.41, bid=0.40)]
    obs = [ext_obs(r["generated_at"], "bovada", 0.45, _iso(src.iso(r["generated_at"]) - timedelta(minutes=5)))
           for r in rows]
    tk = rows[1]["kalshi_ticker"]
    quotes = [{"ticker": tk, "run_id": "r", "captured_at": _iso(START - timedelta(minutes=20)),
               "yes_bid_dollars": "0.44", "yes_ask_dollars": "0.45"}]
    sets = [{"ticker": tk, "result": settle, "settlement_value_dollars": "1.0000" if settle == "yes" else "0.0000",
             "settlement_ts": _iso(START + timedelta(hours=2))}]
    root = build_root(tmp_path, rows, obs, quotes, sets)
    truths = {}
    if truth_conf in ("A", "B"):
        truths[rows[1]["kalshi_event"]] = truth_ab(rows[1]["kalshi_event"], first_ball, truth_conf)
    elif truth_conf == "C":
        truths[rows[1]["kalshi_event"]] = FirstBallTruth(rows[1]["kalshi_event"], None, None, first_ball, "C",
                                                         DERIVATION_SCORE_BACKCAST, created_at=first_ball)
    return root, truths, rows


# ------------------------------------------------------------------------------------------ firewall
def test_confirmation_start_excludes_pre_freeze_rows(tmp_path):
    root, truths, rows = _standard_case(tmp_path)
    res = C.harvest_w4(ctx_for(root, truths), w4_cand())
    assert res.universe["rows_before_confirmation_start"] == 1
    assert res.exclusion_counts[ev.R_PRE_FREEZE] == 1
    assert all(r.captured_at >= w4_cand()["confirmation_start"] for r in res.evidence_rows)


def test_pre_freeze_row_can_never_be_included():
    with pytest.raises(ValueError):
        ev.EvidenceRow(candidate_id="X", observation_id="o", physical_match_id=None, ticker="T", market_family="MW",
                       side=None, captured_at="2026-09-01T00:00:00+00:00", candidate_freeze_at=T_FREEZE,
                       confirmation_start=T_FREEZE, candidate_fingerprint="f", inclusion_result=ev.INCLUDED)
    with pytest.raises(ValueError):          # an excluded row must say why
        ev.EvidenceRow(candidate_id="X", observation_id="o", physical_match_id=None, ticker="T", market_family="MW",
                       side=None, captured_at=T_FREEZE, candidate_freeze_at=T_FREEZE,
                       confirmation_start=T_FREEZE, candidate_fingerprint="f", inclusion_result=ev.EXCLUDED)


# ------------------------------------------------------------------------------------------ exactness
def test_w4_rule_gates_are_the_frozen_text():
    base = w4_row(T_FREEZE)
    assert all(C.w4_rule_gates(base).values())
    # "inside a 6c spread": 6c passes, 7c fails -- compared in cents, so float noise cannot flip it
    assert C.w4_rule_gates(w4_row(T_FREEZE, ask=0.63, bid=0.57, ext=0.70))["spread_within_6c"]
    assert not C.w4_rule_gates(w4_row(T_FREEZE, ask=0.64, bid=0.57, ext=0.70))["spread_within_6c"]
    # "under an hour old"
    assert not C.w4_rule_gates(w4_row(T_FREEZE, qage=3600.0))["kalshi_quote_under_1h"]
    assert C.w4_rule_gates(w4_row(T_FREEZE, qage=3599.0))["kalshi_quote_under_1h"]
    # "at least one contract of displayed size"
    assert not C.w4_rule_gates(w4_row(T_FREEZE, size=0.99))["displayed_size_ge_1"]
    # two-sided
    one_sided = {**w4_row(T_FREEZE), "kalshi_bid": None}
    assert not C.w4_rule_gates(one_sided)["kalshi_two_sided"]
    # triangulation must be KALSHI_LONE_OUTLIER, nothing else
    assert not C.w4_rule_gates(w4_row(T_FREEZE, tri="MODEL_LONE_OUTLIER"))["kalshi_lone_outlier"]


def test_w4_two_cent_after_fee_threshold():
    fee = taker_fee(0.40, 1.0)
    assert fee == 0.02
    just = w4_row(T_FREEZE, ask=0.40, ext=0.40 + fee + 0.02)
    short = w4_row(T_FREEZE, ask=0.40, ext=0.40 + fee + 0.0199)
    assert C.w4_rule_gates(just)["external_edge_ge_2c"]
    assert not C.w4_rule_gates(short)["external_edge_ge_2c"]
    assert C.W4_MIN_EXTERNAL_EDGE == 0.02


def test_first_observation_per_contract_only(tmp_path):
    root, truths, rows = _standard_case(tmp_path)
    res = C.harvest_w4(ctx_for(root, truths), w4_cand())
    firsts = [r for r in res.evidence_rows if r.extra["first_qualifying"]]
    reobs = [r for r in res.evidence_rows if not r.extra["first_qualifying"]]
    assert len(firsts) == 1 and firsts[0].captured_at == rows[1]["generated_at"]
    assert len(reobs) == 1 and reobs[0].inclusion_result == ev.EXCLUDED
    assert ev.R_REOBSERVATION in reobs[0].exclusion_reasons
    assert res.summary.eligible_n == 1


def test_external_freshness_verified_unverifiable_mixed():
    at = "2026-09-19T09:00:00+00:00"
    r = w4_row(at, sources=("bovada",))
    fresh = {(at, "bovada"): [ext_obs(at, "bovada", 0.45, "2026-09-19T08:50:00+00:00")]}
    assert C.w4_freshness(r, fresh)[0] == "VERIFIED_FRESH"
    # a venue that publishes no timestamp can never be VERIFIED fresh
    r2 = w4_row(at, sources=("smarkets",))
    none = {(at, "smarkets"): [ext_obs(at, "smarkets", 0.45, None)]}
    assert C.w4_freshness(r2, none)[0] == "UNVERIFIABLE"
    r3 = w4_row(at, sources=("bovada", "smarkets"))
    both = {**fresh, **none}
    assert C.w4_freshness(r3, both)[0] == "MIXED"
    # the observation behind the stored reference cannot be found: unresolved, never assumed fresh
    assert C.w4_freshness(r, {})[0] == "UNRESOLVED"


# ------------------------------------------------------------------------------------------ truth joins
def test_settlement_join_and_after_fee_pnl(tmp_path):
    root, truths, rows = _standard_case(tmp_path, settle="yes")
    res = C.harvest_w4(ctx_for(root, truths), w4_cand())
    first = [r for r in res.evidence_rows if r.inclusion_result == ev.INCLUDED][0]
    assert first.settlement_result == "yes" and first.settlement_value == 1.0
    assert abs(first.after_fee_pnl - (1.0 - 0.40 - taker_fee(0.40, 1.0))) < 1e-12
    root2, truths2, _ = _standard_case(tmp_path / "b", settle="no")
    first2 = [r for r in C.harvest_w4(ctx_for(root2, truths2), w4_cand()).evidence_rows
              if r.inclusion_result == ev.INCLUDED][0]
    assert abs(first2.after_fee_pnl - (0.0 - 0.40 - 0.02)) < 1e-12


def test_strict_clv_join(tmp_path):
    root, truths, rows = _standard_case(tmp_path)
    first = [r for r in C.harvest_w4(ctx_for(root, truths), w4_cand()).evidence_rows
             if r.inclusion_result == ev.INCLUDED][0]
    assert first.timing_class == "STRICT_PREGAME"
    # close = last executable quote strictly before the first-ball lower bound: bid 0.44; entry ask 0.40
    assert abs(first.strict_clv_executable - (0.44 - 0.40)) < 1e-12
    assert first.close_basis == "FIRST_BALL_BRACKET_LOWER"


def test_confidence_c_is_excluded(tmp_path):
    root, truths, rows = _standard_case(tmp_path, truth_conf="C")
    res = C.harvest_w4(ctx_for(root, truths), w4_cand())
    first = [r for r in res.evidence_rows if r.extra["first_qualifying"]][0]
    assert first.inclusion_result == ev.EXCLUDED and ev.R_TRUTH_C in first.exclusion_reasons
    assert first.strict_clv_executable is None and res.summary.eligible_n == 0


def test_post_start_observation_is_excluded(tmp_path):
    # the first ball was struck BEFORE the observation: a post-start row is never pregame evidence
    root, truths, rows = _standard_case(tmp_path, first_ball=START - timedelta(hours=5))
    first = [r for r in C.harvest_w4(ctx_for(root, truths), w4_cand()).evidence_rows
             if r.extra["first_qualifying"]][0]
    assert first.timing_class == "POST_START"
    assert first.inclusion_result == ev.EXCLUDED and ev.R_TIMING_POST in first.exclusion_reasons


def test_start_unknown_is_excluded(tmp_path):
    root, _truths, rows = _standard_case(tmp_path, truth_conf=None)
    res = C.harvest_w4(ctx_for(root, {}), w4_cand())
    first = [r for r in res.evidence_rows if r.extra["first_qualifying"]][0]
    assert first.timing_class == "START_UNKNOWN" and ev.R_TIMING_UNKNOWN in first.exclusion_reasons


def test_fee_calculation():
    assert taker_fee(0.40, 1.0) == 0.02          # ceil(0.07 * 0.24 * 100) / 100
    assert taker_fee(0.05, 1.0) == 0.01
    assert taker_fee(0.50, 10.0) == 0.18         # ceil(0.07 * 10 * 0.25 * 100) / 100


# ------------------------------------------------------------------------------------------ immutability
def _erow(i, pnl=None):
    return ev.EvidenceRow(candidate_id="X", observation_id=f"o{i}", physical_match_id=None, ticker="T",
                          market_family="MATCH_WINNER", side=None, captured_at=T_FREEZE,
                          candidate_freeze_at=T_FREEZE, confirmation_start=T_FREEZE, candidate_fingerprint="f",
                          after_fee_pnl=pnl, inclusion_result=ev.INCLUDED)


def test_evidence_store_is_append_only_and_idempotent(tmp_path):
    st = ev.EvidenceStore(str(tmp_path))
    assert st.append_new("X", [_erow(1), _erow(2)], "run1") == 2
    assert st.append_new("X", [_erow(1), _erow(2)], "run2") == 0          # nothing new, nothing written
    assert st.append_new("X", [_erow(1, pnl=0.58)], "run3") == 1          # settlement arrived: a NEW version
    assert len(st.rows("X")) == 3 and st.latest("X")["o1"]["after_fee_pnl"] == 0.58
    assert st.verify_chain("X") == []
    lines = open(st.path("X")).read().splitlines()
    d = json.loads(lines[0]); d["after_fee_pnl"] = 9.99
    lines[0] = json.dumps(d, separators=(",", ":"))
    open(st.path("X"), "w").write("\n".join(lines) + "\n")
    assert any("modified" in p for p in st.verify_chain("X"))
    with pytest.raises(ValueError):
        st.append_new("X", [ev.EvidenceRow(**{**_erow(3).__dict__, "candidate_id": "Y"})], "run4")


def test_candidate_definitions_verify_and_detect_edits(tmp_path):
    cands = src.load_candidates(FROZEN)
    assert len(cands) == 7 and all(c["_fingerprint_ok"] for c in cands.values())
    d = tmp_path / "cands"
    shutil.copytree(FROZEN, d)
    p = d / f"{W4_ID}.json"
    raw = json.load(open(p)); raw["minimum_n"] = 20                      # a hindsight edit
    json.dump(raw, open(p, "w"))
    assert not src.load_candidates(str(d))[W4_ID]["_fingerprint_ok"]


def test_harvest_never_writes_frozen_definitions(tmp_path):
    before = {f: open(os.path.join(FROZEN, f), "rb").read() for f in os.listdir(FROZEN)}
    root, truths, _ = _standard_case(tmp_path)
    C.harvest_w4(ctx_for(root, truths), w4_cand())
    assert before == {f: open(os.path.join(FROZEN, f), "rb").read() for f in os.listdir(FROZEN)}
    for c in src.load_candidates(FROZEN).values():
        assert c["evidence"] == []                                      # evidence lives in its own layer


# ------------------------------------------------------------------------------------------ statistics
def test_bootstrap_is_reproducible():
    x = [0.1, -0.3, 0.25, 0.05, -0.02, 0.4, -0.1, 0.0, 0.2]
    a, b = stats.mean_ci(x), stats.mean_ci(x)
    assert a == b and a["seed"] == stats.SEED and a["n_boot"] == stats.N_BOOT
    assert stats.mean_ci([1.0, 2.0])["ci_low"] is None                  # too few for an interval
    p = stats.paired_ci([0.2, 0.3, 0.1, 0.25], [0.3, 0.35, 0.2, 0.3])
    assert p["mean"] < 0 and p == stats.paired_ci([0.2, 0.3, 0.1, 0.25], [0.3, 0.35, 0.2, 0.3])


# ------------------------------------------------------------------------------------------ status engine
@pytest.mark.parametrize("kw,expected", [
    (dict(kind=S.KIND_TRADE, minimum_n=200, eligible_n=0, unscorable_n=500), S.UNSCORABLE_MISSING_HISTORICAL_FIELDS),
    (dict(kind=S.KIND_TRADE, minimum_n=200, eligible_n=1), S.INSUFFICIENT_N),
    (dict(kind=S.KIND_TRADE, minimum_n=10, eligible_n=12, settled_n=5, unsettled_n=7), S.PENDING_SETTLEMENT),
    (dict(kind=S.KIND_TRADE, minimum_n=10, eligible_n=12, settled_n=12, strict_clv_n=3, clv_pending_n=4,
          clv_required=True), S.PENDING_STRICT_CLV),
    (dict(kind=S.KIND_TRADE, minimum_n=10, eligible_n=12, settled_n=12, strict_clv_n=12, clv_required=True,
          accuracy_pass=False, clv_pass=True, economics_pass=True), S.FAIL_ACCURACY),
    (dict(kind=S.KIND_TRADE, minimum_n=10, eligible_n=12, settled_n=12, strict_clv_n=12, clv_required=True,
          accuracy_pass=True, clv_pass=False, economics_pass=True), S.FAIL_CLV),
    (dict(kind=S.KIND_TRADE, minimum_n=10, eligible_n=12, settled_n=12, strict_clv_n=12, clv_required=True,
          accuracy_pass=True, clv_pass=True, economics_pass=False), S.FAIL_ECONOMICS),
    (dict(kind=S.KIND_TRADE, minimum_n=10, eligible_n=12, settled_n=12, strict_clv_n=12, clv_required=True,
          accuracy_pass=True, clv_pass=True, economics_pass=True), S.ELIGIBLE_FOR_CEO_REVIEW),
    (dict(kind=S.KIND_ABSTENTION, minimum_n=10, eligible_n=12, settled_n=12, accuracy_pass=True,
          economics_pass=True), S.ABSTENTION_SUPPORTED),
    (dict(kind=S.KIND_EXISTENCE, minimum_n=10, eligible_n=3), S.INSUFFICIENT_N),
    (dict(kind=S.KIND_EXISTENCE, minimum_n=10, eligible_n=11), S.SUPPORTED_FOR_MORE_RESEARCH),
    (dict(kind=S.KIND_PRICING, minimum_n=10, eligible_n=12, settled_n=12, accuracy_pass=True),
     S.SUPPORTED_FOR_MORE_RESEARCH),
])
def test_status_assignment(kw, expected):
    assert S.assign_status(S.ScoreSummary(**kw))[0] == expected
    assert expected in S.STATUSES


def test_an_abstention_can_never_reach_ceo_review():
    s = S.ScoreSummary(kind=S.KIND_ABSTENTION, minimum_n=1, eligible_n=5, settled_n=5, strict_clv_n=5,
                       accuracy_pass=True, clv_pass=True, economics_pass=True, clv_required=True)
    assert S.assign_status(s)[0] == S.ABSTENTION_SUPPORTED


def test_missing_historical_field_is_unscorable(tmp_path):
    root = str(tmp_path / "empty")
    for sub in ("research/ledger", "research/opportunities", "research/external/dislocations", "kalshi/capture"):
        os.makedirs(os.path.join(root, sub))
    with open(os.path.join(root, "research", "ledger", "2026-09-20.jsonl"), "w") as f:
        f.write(json.dumps({"generated_at_utc": "2026-09-20T00:00:00+00:00", "family": "MATCH_WINNER",
                            "tour": "ATP", "model_version": "elo_surface_k_lo+sr_v0.1",
                            "ticker": "KXATPMATCH-26SEP20AAABBB-AAA", "match_id": "KXATPMATCH-26SEP20AAABBB"}) + "\n")
    cands = src.load_candidates(FROZEN)
    ctx = ctx_for(root)
    for cid in ("W3-2026-001-ABSTAIN-ITF", "W3-2026-002-NONITF-POSITIVE-EDGE", "EC-2026-003-GEN2-MODERATE-EVIDENCE"):
        res = C.HARVESTERS[cid](ctx, cands[cid])
        assert res.status == S.UNSCORABLE_MISSING_HISTORICAL_FIELDS
        assert res.metrics["eligible_n"] == 0 and res.summary.unscorable_n >= 1
    # a Gen-1 ledger row is never passed off as the frozen model's probability
    assert all(f[2] in C.FIELD_CLASSES for rows in C.FIELD_AUDIT.values() for f in rows)


def test_no_hindsight_threshold_surface():
    """Thresholds live next to the frozen text as constants; no harvester accepts one as an argument."""
    for cid, h in C.HARVESTERS.items():
        assert list(inspect.signature(h).parameters) == ["ctx", "cand"], cid
    assert (C.W4_MIN_EXTERNAL_EDGE, C.W4_MAX_VENUE_AGE_S, C.W4_MAX_KALSHI_AGE_S, C.W4_MAX_SPREAD_CENTS,
            C.W4_MIN_SIZE, C.EC4_MIN_LEG_SIZE) == (0.02, 1800, 3600, 6, 1.0, 10.0)
    frozen = src.load_candidates(FROZEN)
    assert set(C.HARVESTERS) == set(frozen) == set(C.FIELD_AUDIT)
    w4 = frozen[W4_ID]["inclusion_rule"]
    for phrase in (">= 0.02", "under 30 minutes", "under an hour", "6c spread", "at least one contract",
                   "FIRST such observation"):
        assert phrase in w4
    assert "minimum leg size >= 10" in frozen["EC-2026-004-COHERENCE-EXECUTABLE"]["required_after_fee_condition"]


# ------------------------------------------------------------------------------------------ order books
def test_book_top_reads_both_captured_shapes():
    cur = {"orderbook": {"orderbook_fp": {"yes_dollars": [["0.2000", "2"], ["0.2200", "9474.65"]],
                                          "no_dollars": [["0.6800", "10.00"], ["0.1100", "1.00"]]}}}
    assert book_top(cur) == (0.22, 9474.65, 0.68, 10.0)
    legacy = {"orderbook": {"orderbook": {"yes": [[40, 5], [42, 3]], "no": [[55, 7]]}}}
    assert book_top(legacy) == (0.42, 3.0, 0.55, 7.0)
    assert book_top({"orderbook": {"orderbook_fp": {"yes_dollars": [["0.3", "1"]], "no_dollars": []}}}) is None


def test_quote_timeline_includes_captured_books(tmp_path):
    from tennis_edge.ledger.quotes import quotes_from_capture
    day = tmp_path / "2026-09-20"; day.mkdir()
    with gzip.open(day / "r.books.jsonl.gz", "wt") as f:
        f.write(json.dumps({"ticker": "T", "captured_at": "2026-09-20T00:00:00+00:00",
                            "orderbook": {"orderbook_fp": {"yes_dollars": [["0.40", "5"]],
                                                           "no_dollars": [["0.58", "7"]]}}}) + "\n")
    q = quotes_from_capture(str(tmp_path))["T"][0]
    assert q.source == "orderbook" and q.yes_bid == 0.40 and abs(q.yes_ask - 0.42) < 1e-12 and q.yes_ask_size == 7.0
