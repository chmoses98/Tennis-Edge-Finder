"""Two scoped corrections (2026-10-01):

1. Evidence accounting: a frozen producer observation timestamped at or after the exchange's recorded settlement
   of its contract cannot be prospective evidence (MARKET_SETTLED_BEFORE_OBSERVATION). The FIRST observation
   stays the unit; a contaminated one is excluded, never replaced; the correction is appended, never rewritten.
2. Assisted handicapping: the Gen-1 doubles model failed its no-skill test, so no doubles probability reaches
   the assisted slate or a recorded decision; doubles markets themselves stay on the slate.
"""
import gzip
import hashlib
import json
import os
import sys
from datetime import datetime, timedelta, timezone

import pytest

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "scripts", "ops"))

from tennis_edge.assisted import record as R
from tennis_edge.assisted import schema as SC
from tennis_edge.assisted.health import gate_17
from tennis_edge.assisted.slate import GEN1_DOUBLES_WARNING, build_slate, render_markdown, write_slate
from tennis_edge.confirmation import evidence as ev
from tennis_edge.confirmation import sources as src
from tennis_edge.confirmation import started_candidates as L
from tennis_edge.confirmation.corrections import post_settlement_correction
from tennis_edge.confirmation.evidence import EvidenceStore
from tests.test_frozen_producers import FROZEN, FROZEN_CANDIDATES, FROZEN_SOURCES, _ctx, _live_root, _shadow_row, _truth
from tests import test_discrepancy_sanity as DW

UTC = timezone.utc
T0 = "2026-09-29T00:00:00+00:00"            # effective start
OBS = "2026-09-29T01:00:00+00:00"           # first observation
TK = "KXATPMATCH-26SEP29AAABBB-AAA"
W3_002 = "W3-2026-002-NONITF-POSITIVE-EDGE"
EC3 = "EC-2026-003-GEN2-MODERATE-EVIDENCE"


def _sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def _settle(tk, ts, result="no"):
    d = {"ticker": tk, "result": result, "settlement_value_dollars": "1.0" if result == "yes" else "0.0"}
    if ts is not None:
        d["settlement_ts"] = ts
    return d


def _w3(tmp_path, settlements, rows=None, truths=None, cid=W3_002):
    rows = rows or [_shadow_row(OBS, TK)]
    root = _live_root(tmp_path, rows, T0, settlements=settlements)
    res = L.harvest_w3_live(_ctx(root, truths), src.load_candidates(FROZEN)[cid])
    return root, res


# ------------------------------------------------------------------------------------------ the helper
def test_settled_before_observation_helper():
    ctx = type("C", (), {"settlements": {"A": _settle("A", "2026-09-29T00:30:00Z"), "B": _settle("B", OBS),
                                         "C": _settle("C", None), "D": _settle("D", "garbage"),
                                         "E": _settle("E", "2026-09-29T02:00:00Z")}})()
    assert L._settled_before_observation(ctx, "A", OBS) == (True, "2026-09-29T00:30:00Z")
    assert L._settled_before_observation(ctx, "B", OBS)[0] is True          # same instant fails closed
    assert L._settled_before_observation(ctx, "C", OBS) == (False, None)    # no timestamp: never fabricated
    assert L._settled_before_observation(ctx, "D", OBS) == (False, None)    # malformed: never fabricated
    assert L._settled_before_observation(ctx, "E", OBS) == (False, "2026-09-29T02:00:00Z")
    assert L._settled_before_observation(ctx, "ZZZ", OBS) == (False, None)
    assert L._settled_before_observation(ctx, "A", "not a time") == (False, "2026-09-29T00:30:00Z")
    assert ev.R_SETTLED_BEFORE_OBSERVATION == "MARKET_SETTLED_BEFORE_OBSERVATION" != ev.R_TIMING_POST


# ------------------------------------------------------------------------------------------ W3
def test_w3_first_observation_before_settlement_stays_eligible(tmp_path):
    _root, res = _w3(tmp_path, [_settle(TK, "2026-09-29T20:00:00Z", "yes")])
    r = res.evidence_rows[0]
    assert r.inclusion_result == ev.INCLUDED and r.settled_at is None and r.settlement_result == "yes"
    assert res.universe["post_settlement_first_observations_excluded"] == 0


def test_w3_first_observation_after_settlement_is_excluded(tmp_path):
    _root, res = _w3(tmp_path, [_settle(TK, "2026-09-29T00:30:00Z")])
    r = res.evidence_rows[0]
    assert r.inclusion_result == ev.EXCLUDED and ev.R_SETTLED_BEFORE_OBSERVATION in r.exclusion_reasons
    assert ev.R_TIMING_POST not in r.exclusion_reasons                 # a different fact, a different reason
    assert r.settled_at == "2026-09-29T00:30:00Z" and r.settlement_result == "no"   # outcome kept
    assert res.universe["post_settlement_first_observations_excluded"] == 1
    assert res.universe["post_settlement_first_observations_by_level"] == {"ATP": 1}
    assert res.summary.eligible_n == 0


def test_w3_settlement_at_the_same_instant_is_excluded(tmp_path):
    _root, res = _w3(tmp_path, [_settle(TK, "2026-09-29T01:00:00Z")])
    assert ev.R_SETTLED_BEFORE_OBSERVATION in res.evidence_rows[0].exclusion_reasons


@pytest.mark.parametrize("ts", [None, "garbage", ""])
def test_missing_or_malformed_settlement_ts_fabricates_nothing(tmp_path, ts):
    _root, res = _w3(tmp_path, [_settle(TK, ts)])
    r = res.evidence_rows[0]
    assert r.inclusion_result == ev.INCLUDED and ev.R_SETTLED_BEFORE_OBSERVATION not in r.exclusion_reasons
    assert r.settlement_result == "no"                                   # the result itself is still attached


def test_a_later_observation_never_replaces_a_contaminated_first(tmp_path):
    rows = [_shadow_row(OBS, TK), _shadow_row("2026-09-29T07:00:00+00:00", TK, edge=0.08)]
    _root, res = _w3(tmp_path, [_settle(TK, "2026-09-29T00:30:00Z")], rows=rows)
    assert len(res.evidence_rows) == 1
    r = res.evidence_rows[0]
    assert r.captured_at == OBS and r.inclusion_result == ev.EXCLUDED and r.decision_edge == 0.03
    assert res.exclusion_counts[ev.R_REOBSERVATION] == 1 and res.summary.eligible_n == 0


def test_first_ball_post_start_protection_still_works(tmp_path):
    truths = {"KXATPMATCH-26SEP29AAABBB": _truth("KXATPMATCH-26SEP29AAABBB", datetime(2026, 9, 29, 0, 30, tzinfo=UTC))}
    _root, res = _w3(tmp_path, [_settle(TK, "2026-09-29T20:00:00Z")], truths=truths)
    r = res.evidence_rows[0]
    assert r.exclusion_reasons == (ev.R_TIMING_POST,) and r.inclusion_result == ev.EXCLUDED


# ------------------------------------------------------------------------------------------ EC-003
def _ec3_rows(pm="AAABBB", at=OBS):
    return [_shadow_row(at, f"KXATPMATCH-26SEP29{pm}-A", pm=pm, a=True),
            _shadow_row(at, f"KXATPMATCH-26SEP29{pm}-B", pm=pm, a=False)]


def test_ec3_first_run_after_settlement_is_excluded_and_not_replaced(tmp_path):
    rows = _ec3_rows("AAABBB") + _ec3_rows("AAABBB", at="2026-09-29T07:00:00+00:00") + _ec3_rows("CCCDDD")
    sets = [_settle("KXATPMATCH-26SEP29AAABBB-B", "2026-09-29T00:45:00Z", "yes"),     # either contract is enough
            _settle("KXATPMATCH-26SEP29CCCDDD-A", "2026-09-29T21:00:00Z", "yes")]
    root = _live_root(tmp_path, rows, T0, settlements=sets)
    res = L.harvest_ec3_live(_ctx(root), src.load_candidates(FROZEN)[EC3])
    by = {r.physical_match_id: r for r in res.evidence_rows}
    a = by["AAABBB"]
    assert a.inclusion_result == ev.EXCLUDED and a.exclusion_reasons == (ev.R_SETTLED_BEFORE_OBSERVATION,)
    assert a.captured_at == OBS and a.settled_at == "2026-09-29T00:45:00Z"        # first run, never the 07:00 run
    assert by["CCCDDD"].inclusion_result == ev.INCLUDED and by["CCCDDD"].settled_at is None
    assert res.universe["post_settlement_first_runs_excluded"] == 1 and res.summary.eligible_n == 1


def test_model4_first_run_uses_the_same_generic_invariant(tmp_path):
    from tests.test_frozen_producers import _board, _build
    rows, _sk, _ = _build(_board())
    sets = [_settle("KXATPMATCH-26SEP30WALTIE-TIE", "2026-09-30T08:00:00Z", "yes")]      # before 08:05 prediction
    root = _live_root(tmp_path, rows, "2026-09-30T00:00:00+00:00", settlements=sets, producer="model4_board_v1")
    res = L.harvest_ec1_live(_ctx(root), src.load_candidates(FROZEN)["EC-2026-001-MKTCOND-EXACT-SCORE"])
    assert [r.exclusion_reasons for r in res.evidence_rows] == [(ev.R_SETTLED_BEFORE_OBSERVATION,)]
    assert res.universe["post_settlement_first_runs_excluded"] == 1
    root2 = _live_root(tmp_path / "late", rows, "2026-09-30T00:00:00+00:00",
                       settlements=[_settle("KXATPMATCH-26SEP30WALTIE-TIE", "2026-09-30T20:00:00Z", "yes")],
                       producer="model4_board_v1")
    res2 = L.harvest_ec1_live(_ctx(root2), src.load_candidates(FROZEN)["EC-2026-001-MKTCOND-EXACT-SCORE"])
    assert all(ev.R_SETTLED_BEFORE_OBSERVATION not in r.exclusion_reasons for r in res2.evidence_rows)


# ------------------------------------------------------------------------------------------ append-only repair
def test_correction_is_a_newer_version_never_a_rewrite(tmp_path):
    cand = src.load_candidates(FROZEN)[W3_002]
    store = EvidenceStore(str(tmp_path / "evidence"))
    # 1) the settlement record has not been swept yet: the observation is INCLUDED
    root = _live_root(tmp_path / "a", [_shadow_row(OBS, TK)], T0)
    before = L.harvest_w3_live(_ctx(root), cand)
    assert store.append_new(W3_002, before.evidence_rows, "run1") == 1
    path = store.path(W3_002)
    original = open(path, "rb").read()
    assert store.latest(W3_002)[before.evidence_rows[0].observation_id]["inclusion_result"] == ev.INCLUDED
    # 2) the corrected harvest sees Kalshi's settlement BEFORE the observation
    root2 = _live_root(tmp_path / "b", [_shadow_row(OBS, TK)], T0, settlements=[_settle(TK, "2026-09-29T00:30:00Z")])
    after = L.harvest_w3_live(_ctx(root2), cand)
    prior = store.latest(W3_002)
    assert store.append_new(W3_002, after.evidence_rows, "run2") == 1
    raw = open(path, "rb").read()
    assert raw.startswith(original) and raw.count(b"\n") == 2                 # old line byte-identical, kept
    lines = store.rows(W3_002)
    assert lines[0]["inclusion_result"] == ev.INCLUDED                        # history is not rewritten
    assert lines[0]["observation_id"] == lines[1]["observation_id"]
    for k in ("captured_at", "kalshi_bid", "kalshi_ask", "fair_probability", "decision_edge", "ticker"):
        assert lines[0][k] == lines[1][k], k                                  # same decision-time fields
    latest = store.latest(W3_002)[lines[0]["observation_id"]]
    assert latest["inclusion_result"] == ev.EXCLUDED and latest["settled_at"] == "2026-09-29T00:30:00Z"
    assert ev.R_SETTLED_BEFORE_OBSERVATION in latest["exclusion_reasons"]
    assert store.verify_chain(W3_002) == []                                   # the chain stays intact
    c = post_settlement_correction(prior, after.evidence_rows)
    assert (c["corrected_included_to_excluded"], c["corrected_by_level"]) == (1, {"ATP": 1})
    assert c["corrected_observations"][0]["settled_at"] == "2026-09-29T00:30:00Z"
    assert after.summary.eligible_n == 0 and before.summary.eligible_n == 1  # scoring uses the corrected unit
    assert store.append_new(W3_002, after.evidence_rows, "run3") == 0         # idempotent


def test_harvest_script_reports_the_correction_and_leaves_frozen_files_alone(tmp_path):
    import subprocess
    root = _live_root(tmp_path, [_shadow_row(OBS, TK)], T0, settlements=[_settle(TK, "2026-09-29T00:30:00Z")])
    cand_dir = os.path.join(root, "research", "edge_candidates")
    os.makedirs(cand_dir)
    for fn in FROZEN_CANDIDATES:
        open(os.path.join(cand_dir, fn), "wb").write(open(os.path.join(FROZEN, fn), "rb").read())
    starts = os.path.join(root, "research", "experiment_starts")
    before = {fn: _sha(os.path.join(starts, fn)) for fn in os.listdir(starts)}
    out = subprocess.run([sys.executable, os.path.join(REPO, "scripts", "research", "harvest_candidate_evidence.py"),
                          "--data-root", root, "--evidence-out", str(tmp_path / "ev"), "--report-out", str(tmp_path / "rep")],
                         capture_output=True, text=True)
    assert out.returncode == 0, out.stdout + out.stderr
    rep = json.load(open(tmp_path / "rep" / f"{W3_002}.json"))
    c = rep["evidence_accounting_correction"]
    assert c["observations_settled_before_observation"] == 1 and c["first_harvested_this_run"] == 1
    assert rep["evidence_chain_violations"] == [] and rep["universe"]["post_settlement_first_observations_excluded"] == 1
    assert "Evidence-accounting correction" in open(tmp_path / "rep" / "SUMMARY.md").read()
    log = [json.loads(x) for x in open(tmp_path / "ev" / "harvest_runs.jsonl")][-1]
    assert log["post_settlement_correction"][W3_002]["observations_settled_before_observation"] == 1
    assert {fn: _sha(os.path.join(starts, fn)) for fn in os.listdir(starts)} == before
    for fn, h in FROZEN_CANDIDATES.items():
        assert _sha(os.path.join(cand_dir, fn)) == h and _sha(os.path.join(FROZEN, fn)) == h


def test_no_frozen_source_or_candidate_changed():
    for rel, h in FROZEN_SOURCES.items():
        assert _sha(os.path.join(REPO, rel)) == h, rel
    for fn, h in FROZEN_CANDIDATES.items():
        assert _sha(os.path.join(FROZEN, fn)) == h, fn


# ------------------------------------------------------------------------------------------ doubles
DEV = "KXATPDOUBLES-26OCT01AAAGGGBBBHHH"
D_A, D_B = DEV + "-AAAGGG", DEV + "-BBBHHH"
RULES = ("If {w} wins the Aaa / Ggg vs Bbb / Hhh professional tennis match in the 2026 ATP Tokyo Quarterfinal after a "
         "ball has been played, then the market resolves to Yes.")


def _doubles_world(tmp_path):
    w = DW.make_world(tmp_path)
    at = DW.T_CAP + timedelta(minutes=1)

    def q(tk, name, bid, ask):
        return {"run_id": "x", "captured_at": at.isoformat(), "snapshot_kind": "changed", "ticker": tk, "event_ticker": DEV,
                "status": "active", "title": f"{name} wins", "yes_sub_title": name, "rules_primary": RULES.format(w=name),
                "occurrence_datetime": "2026-10-01T11:00:00Z", "custom_strike": {"tennis_doubles_competitor": tk[-6:]},
                "yes_bid_dollars": f"{bid:.4f}", "yes_ask_dollars": f"{ask:.4f}", "yes_bid_size_fp": "120.00",
                "yes_ask_size_fp": "80.00", "open_interest_fp": "50.00", "volume_24h_fp": "40.00"}
    cap = os.path.join(w["data"], "kalshi", "capture", DW.DAY)
    with gzip.open(os.path.join(cap, "20261001T080130Z.quotes.jsonl.gz"), "wt") as f:
        for r in (q(D_A, "Alpha Aaa / Gamma Ggg", 0.19, 0.29), q(D_B, "Beta Bbb / Eta Hhh", 0.71, 0.81)):
            f.write(json.dumps(r) + "\n")
    DW._jsonl(os.path.join(w["data"], "research", "ledger", f"{DW.DAY}.jsonl"), [
        {"ticker": D_A, "family": "MATCH_WINNER", "event_ticker": DEV, "series_ticker": "KXATPDOUBLES",
         "subject": "Alpha Aaa / Gamma Ggg", "player_a": "Alpha Aaa / Gamma Ggg", "player_b": "Beta Bbb / Eta Hhh",
         "player_a_id": "1|7", "player_b_id": "2|8", "generated_at_utc": "2026-10-01T08:02:00+00:00", "level": "TOUR_500_250",
         "models": {"ELO_DP_FAIR": 0.9186, "ELO": 0.93, "STRUCTURAL": 0.90},
         "market_quote": {"yes_bid": 0.19, "yes_ask": 0.29, "quote_ts": at.isoformat()},
         "quality": {"grade": "C", "pillars": {"identity_confidence": 1.0}, "inputs": {}}}])
    slate = build_slate(w["data"], now=DW.T_SLATE)
    write_slate(slate, w["slate_dir"])
    w["slate"] = slate
    return w


def _drow(w, tk=D_A):
    return next((x, r) for x in w["slate"]["matches"] for r in x["markets"] if r["ticker"] == tk)


def test_singles_gen1_unchanged(tmp_path):
    w = _doubles_world(tmp_path)
    x, r = _drow(w, DW.MW_A)
    assert (r["model"]["gen1"], r["model"]["fair_v1"], r["model_probability_yes"]) == (0.56, 0.56, 0.56)
    assert r["model_probability_source"].startswith("fair_v1") and r["model_validity"] is None and x["model_validity"] is None
    assert GEN1_DOUBLES_WARNING not in " ".join(x["warnings"] + r["warnings"])
    assert x["model_context"]["player_a_win"]["gen1"] == 0.56 and r["discrepancy_band"] == "NORMAL"


def test_doubles_gen1_suppressed_from_the_slate(tmp_path):
    w = _doubles_world(tmp_path)
    x, r = _drow(w)
    assert x["discipline"] == "doubles"
    for k in ("gen1", "gen1_elo_only", "gen1_structural", "gen2", "fair_v1", "model4_conditioned", "model4_fundamental"):
        assert r["model"][k] is None, k
    assert r["model_probability_yes"] is None and r["model_probability_source"] is None
    assert r["model_preferred_side"] == "NONE" and r["model_side_edges"] == {"YES": None, "NO": None}
    assert r["model_minus_mid"] is None and r["model_market_gap_pp"] is None
    assert (r["discrepancy_band"], r["discrepancy_sanity_status"]) == ("UNPRICED", "NOT_APPLICABLE")
    assert x["model_context"]["player_a_win"]["gen1"] is None and x["model_context"]["rating_state"]["elo_a"] is None
    assert r["model_validity"]["gen1"] == "UNVALIDATED_DO_NOT_USE" and "no-skill" in r["model_validity"]["reason"]
    assert GEN1_DOUBLES_WARNING in r["warnings"] and any(s.startswith(GEN1_DOUBLES_WARNING) for s in x["warnings"])
    assert "DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS" in x["warnings"]
    # the market itself stays: prices, size, spread, schedule, inventory
    k = r["kalshi"]
    assert (k["bid"], k["ask"], k["mid"], k["spread"], k["bid_size"], k["ask_size"]) == (0.19, 0.29, 0.24, 0.1, 120.0, 80.0)
    assert x["scheduled_start"] == "2026-10-01T11:00:00Z" and x["available_expressions"] == ["MATCH_WINNER"]
    assert {D_A, D_B} <= {m["ticker"] for m in x["markets"]}


def test_doubles_markdown_shows_no_model_number(tmp_path):
    w = _doubles_world(tmp_path)
    md = render_markdown(w["slate"])
    sec = md[md.index("Alpha Aaa / Gamma Ggg vs"):]
    sec = sec[:sec.index("\n## ")] if "\n## " in sec else sec
    row = next(line for line in sec.splitlines() if D_A in line)
    assert "91.9%" not in md and "| -- | -- | -- [-----] |" in row and "0.19 / 0.29" in row
    assert "Model validity: GEN1 DOUBLES = UNVALIDATED_DO_NOT_USE" in sec
    assert "DISCREPANCY SANITY CHECK" not in sec


def test_tennis17_passes_with_unmodelled_doubles_and_still_catches_a_bypass(tmp_path):
    w = _doubles_world(tmp_path)
    status, d = gate_17(w["research"], now=DW.T_SLATE)
    assert status == "PASS" and d["failing"] == []
    p = os.path.join(w["slate_dir"], "latest.json")
    s = json.load(open(p))
    r = next(r for x in s["matches"] for r in x["markets"] if r["ticker"] == D_A)
    r["model_probability_yes"] = 0.9186                                       # a probability sneaks back in
    json.dump(s, open(p, "w"))
    status, d = gate_17(w["research"], now=DW.T_SLATE)
    assert status == "FAIL" and "BAND_MISMATCH" in d["failing"]


def test_assisted_doubles_decision_records_no_model(tmp_path):
    w = _doubles_world(tmp_path)
    kw = {"store_root": w["store"], "data_root": w["data"], "slate_dir": w["slate_dir"], "now": DW.T_DEC}
    bet = {"ticker": D_A, "side": "YES", "decision": "BET", "chatgpt_fair_probability": 0.35, "chatgpt_confidence": "LOW",
           "chatgpt_thesis": "manual doubles read", "bet_up_to_price": 0.30, "stake_units_if_bet": 1.0}
    rec = R.record_decision(bet, **kw)                                         # manual doubles bets are still allowed
    for k in ("gen1_probability", "gen2_probability", "fair_v1_probability", "model4_probability_if_applicable",
              "model_probability_yes", "model_probability_source"):
        assert rec[k] is None, k
    assert rec["model_agreement_state"] == SC.MODEL_NEUTRAL and rec["model_preferred_side"] == "NONE"
    assert rec["model_side_edges"] == {"YES": None, "NO": None} and rec["discrepancy_band"] == "UNPRICED"
    assert any(x.startswith(GEN1_DOUBLES_WARNING) for x in rec["warnings"])
    p = R.build_decision({"ticker": D_A, "decision": "PASS", "pass_reason_if_pass": "no model", "side": "NO",
                          "chatgpt_fair_probability": 0.2}, **kw)
    assert p["model_agreement_state"] == SC.MODEL_AND_CHATGPT_BOTH_PASS and p["gen1_probability"] is None
    with pytest.raises(SC.AssistedValidationError) as e:                       # the old number cannot be typed back in
        R.build_decision({**bet, "gen1_probability": 0.9186, "chatgpt_thesis": "other"}, **kw)
    assert e.value.code == "UNVALIDATED_MODEL_PROBABILITY"
    single = R.build_decision({**bet, "ticker": DW.MW_A, "bet_up_to_price": 0.52, "chatgpt_fair_probability": 0.56,
                               "chatgpt_confidence": "MEDIUM", "chatgpt_thesis": "singles"}, **kw)
    assert single["gen1_probability"] == 0.56 and single["model_probability_yes"] == 0.56   # singles unaffected
