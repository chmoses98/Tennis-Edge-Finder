"""Live frozen producers, effective experiment starts, TENNIS-15 and the sibling physical-match CLV join."""
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

from tennis_edge.confirmation import candidates as C
from tennis_edge.confirmation import evidence as ev
from tennis_edge.confirmation import scorecards as SC
from tennis_edge.confirmation import sources as src
from tennis_edge.confirmation import started_candidates as L
from tennis_edge.confirmation.status import (INSUFFICIENT_N, UNSCORABLE_MISSING_HISTORICAL_FIELDS)
from tennis_edge.firstball.truth import FirstBallTruth, DERIVATION_EXPLICIT
from tennis_edge.health import gates as G
from tennis_edge.producers import records as R

FROZEN = os.path.join(REPO, "data", "research", "edge_candidates")
T0 = datetime(2026, 9, 29, 12, 0, tzinfo=timezone.utc)

# ---------------------------------------------------------------------------------------------- invariants
#: sha256 of every frozen model/rule source at the Wave 5 baseline 625bc55. A change to any of these files
#: is a change to a frozen model and must fail here, not be discovered later in the evidence.
FROZEN_SOURCES = {
    "tennis_edge/models/fair.py": "3a41f3f502759f676dc23caa1f5469d4135784e9d022cd8d40bf005463e4741f",
    "tennis_edge/models/gen2.py": "595c2e7ff30772fc5cefe890707c7d38f795ad1aeec6a63a71a026b70516ce29",
    "tennis_edge/models/elo.py": "993ce3aa5b38ed067f1fc11af827dde8ab57e09a7ad16cff18f3846dd60ea2f6",
    "tennis_edge/models/asof.py": "a3f8cc5d195c0fd1d6128240e44b1dc3ad77872821ff004ec8a8c36fc3b12984",
    "tennis_edge/models/market_conditioned.py": "640098ebab087c4337a66e4c87d689edc6cd77c7c17d9ac5d4bd163bf08649c8",
    "tennis_edge/selector/decide.py": "40b54d4a81e7a9dae28cc237570f146f294378c01505e926b9bdbd00a9c8d3bb",
    "tennis_edge/selector/model.py": "56c532f938777940ddbd396c5827b8a45a2d3bf279becf7e0f9f2dbc02900441",
    "tennis_edge/selector/features.py": "e4a3797d2502ed36fd7d6f855a380576b53196d3286990b0a7a232af264f6c5f",
    "tennis_edge/opportunity/qualify.py": "2cbc8ca49a9f9bdbdb03f395a4bebcaf166795d245192680f148254759c5caf2",
    "tennis_edge/external_market/dislocation.py": "a8044f08a48ff40d2d4a4b647ea16e7f17a1f14d665d6c5808cb92e4cc9f5901",
    "tennis_edge/external_market/consensus.py": "dc0f0d0aa1d3f0f21759be729b32b983c33c5202d32cc6dad6325f49e19dd58b",
    "tennis_edge/sim/analytic.py": "680b6b16dfc52a584a6e55e5997abd98a10c516c9acc53bdf8b976744498e38e",
    "tennis_edge/pricing/payoffs.py": "112e8c5384a93c6f0ddc851f95c960f204362659c8ad3bc48494f15ee3486ce4",
    "tennis_edge/pricing/fees.py": "606991eab443533aa84c3ee6aabacfa4aed49cbbedf57c04ec7994b6d576e1a9",
}
FROZEN_CANDIDATES = {
    "EC-2026-001-MKTCOND-EXACT-SCORE.json": "01f7d802a7f021670efb208c8b77f34d6330c3b7dbe874ba24bafc3015e850b6",
    "EC-2026-002-MKTCOND-GAME-SPREAD.json": "7646ddf2cdbe3e61eabf843352184e566f657b413d7ad17f88d0bbe466ae7e3a",
    "EC-2026-003-GEN2-MODERATE-EVIDENCE.json": "33b2ae68b31ff9d75e7b82d133f623e593e07b5902c9e41802a3f428dbb6c730",
    "EC-2026-004-COHERENCE-EXECUTABLE.json": "59829bf405f4ae99deb1827b63c0a74a87632b522eeb47d2ebd6832c5621a0a6",
    "W3-2026-001-ABSTAIN-ITF.json": "8286e635405f564d928e3f1d758dc2145c22a7b7915c42b541d88b1061cef90c",
    "W3-2026-002-NONITF-POSITIVE-EDGE.json": "586074ecb494ea5ca8d8691378da50171e391172d4cafaa84895234490b2fb0a",
    "W4-2026-001-KALSHI-LONE-OUTLIER.json": "8b4fdf6258466586fd0f776b28a640fedb5c7c701f1c91db0e9aa473edbc5ebe",
}


def _sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def test_frozen_model_sources_are_byte_identical_to_the_baseline():
    for rel, h in FROZEN_SOURCES.items():
        assert _sha(os.path.join(REPO, rel)) == h, f"{rel} changed: frozen models may not be edited"


def test_frozen_model_version_strings():
    from tennis_edge.models.fair import FAIR_VERSION, PERTURBATIONS, FairConfig
    from tennis_edge.models.gen2 import Gen2Config
    from tennis_edge.models.market_conditioned import MODEL_VERSION
    from tennis_edge.selector.decide import SELECTOR_VERSION
    assert (FAIR_VERSION, SELECTOR_VERSION, MODEL_VERSION) == ("fair_v1", "selector_v1", "market_conditioned_v1")
    assert len(PERTURBATIONS) == 13 and PERTURBATIONS[0] == FairConfig()
    # fair_v1's base config IS the Gen-2 default, so the Model 4 fundamental lane and fair_v1 share Gen-2
    assert (FairConfig().gen2_prior_points, FairConfig().gen2_surface_prior_points) == \
           (Gen2Config().prior_points, Gen2Config().surface_prior_points)


def test_frozen_candidate_definitions_are_byte_identical():
    assert sorted(os.listdir(FROZEN)) == sorted(FROZEN_CANDIDATES)
    for fn, h in FROZEN_CANDIDATES.items():
        assert _sha(os.path.join(FROZEN, fn)) == h, f"{fn} changed"
    assert all(c["_fingerprint_ok"] for c in src.load_candidates(FROZEN).values())


def test_merge_state_audit_layer_is_present():
    """The audit branch (d0b28d9) is merged: its modules, gates and producers are importable."""
    from tennis_edge.confirmation import candidates, evidence, scorecards, status  # noqa: F401
    from tennis_edge.kalshi.trade_tape import TradeTape  # noqa: F401
    from tennis_edge.ledger.quotes import book_top  # noqa: F401
    assert hasattr(G, "settlement_stats") and hasattr(G, "gate_15_prospective_confirmation")
    assert os.path.exists(os.path.join(REPO, "scripts", "research", "harvest_candidate_evidence.py"))


def test_workflow_schedules_the_frozen_producers_before_the_harvest():
    y = open(os.path.join(REPO, ".github", "workflows", "tennis-run.yml")).read()
    i_run, i_sb, i_m4 = y.index("scripts/run_tennis.py"), y.index("scripts/ops/shadow_board.py"), y.index("scripts/ops/model4_board.py")
    i_settle, i_h, i_health = y.index("settle_ledger.py"), y.index("harvest_candidate_evidence.py --data-root"), y.index("run_all()")
    assert i_run < i_sb < i_m4 < i_settle < i_h < i_health
    assert "--record-failure" in y and "::error::candidate evidence harvest failed" in y
    assert "real" not in y.lower().split("authority")[0][-5:]   # no authority switch anywhere near


def test_shadow_board_persists_every_field_the_frozen_rules_need():
    s = open(os.path.join(REPO, "scripts", "ops", "shadow_board.py")).read()
    for k in ("gen1_elo_probability", "gen2_probability", "gen2_blend_probability", "fair_v1_probability",
              "thinner_serve_points", "model_uncertainty", "qualification", "qualification_ok", "selector_decision",
              "selector_version", "fee_adjusted_edge", "kalshi_bid", "kalshi_ask", "fee", "spread", "displayed_size",
              "identity_confidence", "model_versions", "physical_match_id", "level", "predicted_at",
              "first_ball_already_observed", "ensure_experiment_starts"):
        assert f'"{k}"' in s or k in s, k
    # the frozen call itself is unchanged: base config fair, envelope over PERTURBATIONS, selector decide()
    assert "compute_fair(st, ma[\"player_id\"], mb[\"player_id\"]" in s and "for cfg in PERTURBATIONS" in s


# ---------------------------------------------------------------------------------------------- start records
def test_experiment_start_records_are_write_once(tmp_path):
    cdefs = src.load_candidates(FROZEN)
    w = R.ensure_experiment_starts(str(tmp_path), "shadow_board_v1", started_at="2026-09-28T03:25:00+00:00",
                                   main_sha="abc", candidate_defs=cdefs, producer_version="shadow_board_v1@abc")
    assert {r["candidate_id"] for r in w} == set(R.PRODUCERS["shadow_board_v1"]["candidates"])
    again = R.ensure_experiment_starts(str(tmp_path), "shadow_board_v1", started_at="2026-10-30T00:00:00+00:00",
                                       main_sha="zzz", candidate_defs=cdefs, producer_version="x")
    assert again == []
    recs = R.load_start_records(str(tmp_path))
    r = recs["W3-2026-001-ABSTAIN-ITF"]
    assert r["effective_scorable_start"] == "2026-09-28T03:25:00+00:00" and r["activating_main_sha"] == "abc"
    assert r["original_frozen_at"] == cdefs["W3-2026-001-ABSTAIN-ITF"]["frozen_at"]
    assert r["producer_missing_period_start"] == r["original_confirmation_start"]
    assert r["producer_missing_period_end"] == r["effective_scorable_start"] and r["_fingerprint_ok"]
    for k in ("candidate_id", "original_frozen_at", "original_confirmation_start", "producer_missing_period_start",
              "producer_missing_period_end", "effective_scorable_start", "model_version", "producer_version",
              "activating_main_sha", "reason_prior_period_unscorable"):
        assert r.get(k), k
    p = os.path.join(str(tmp_path), "W3-2026-001-ABSTAIN-ITF.json")
    d = json.load(open(p)); d["effective_scorable_start"] = "2026-09-01T00:00:00+00:00"; json.dump(d, open(p, "w"))
    assert not R.load_start_records(str(tmp_path))["W3-2026-001-ABSTAIN-ITF"]["_fingerprint_ok"]


def test_producer_store_is_append_only(tmp_path):
    st = R.ProducerStore(str(tmp_path))
    st.append({"predicted_at": "2026-09-28T03:00:00+00:00", "x": 1})
    st.append({"predicted_at": "2026-09-28T04:00:00+00:00", "x": 2})
    assert st.verify_chain() == []
    with pytest.raises(ValueError):
        st.append({"x": 3})                       # no prediction timestamp, no row
    p = os.path.join(str(tmp_path), "2026-09-28.jsonl")
    lines = open(p).read().splitlines(); d = json.loads(lines[0]); d["x"] = 9; lines[0] = json.dumps(d)
    open(p, "w").write("\n".join(lines) + "\n")
    assert st.verify_chain()


# ---------------------------------------------------------------------------------------------- live harvest
def _truth(mid, fb, conf="B"):
    return FirstBallTruth(mid, None, fb, fb + timedelta(minutes=3), conf, DERIVATION_EXPLICIT, created_at=fb)


def _shadow_row(at, tk, *, level="ATP_TOUR", edge=0.03, fair=0.55, ask=0.50, bid=0.49, thin=5000.0, a=True,
                qual=True, pm="ATP:1:2:2026-09-29"):
    return {"producer": "shadow_board_v1", "predicted_at": at, "physical_match_id": pm, "event": tk.rsplit("-", 1)[0],
            "ticker": tk, "market_family": "MATCH_WINNER", "side": "YES", "subject_is_a": a, "tour": "ATP",
            "level": level, "gen1_elo_probability": 0.60, "gen2_probability": 0.56, "gen2_blend_probability": fair,
            "fair_v1_probability": fair, "thinner_serve_points": thin, "qualification_ok": qual,
            "selector_decision": "PASS", "fee_adjusted_edge": edge, "kalshi_bid": bid, "kalshi_ask": ask,
            "kalshi_mid": 0.5 * (ask + bid), "spread": ask - bid, "fee": 0.02, "displayed_size": 10.0,
            "identity_confidence": 1.0, "authority": "RESEARCH_ONLY_NO_REAL_MONEY"}


def _live_root(tmp_path, rows, start_at, settlements=(), quotes=(), producer="shadow_board_v1"):
    root = tmp_path / "data"
    st = R.ProducerStore(str(root / "research" / "frozen_producers" / L.PRODUCER_DIRS[producer]))
    for r in rows:
        st.append(r)
    R.ensure_experiment_starts(str(root / "research" / "experiment_starts"), producer, started_at=start_at,
                               main_sha="sha", candidate_defs=src.load_candidates(FROZEN), producer_version="v")
    cap = root / "kalshi" / "capture" / "2026-09-29"; cap.mkdir(parents=True)
    with gzip.open(cap / "r.settlements.jsonl.gz", "wt") as f:
        for s in settlements:
            f.write(json.dumps(s) + "\n")
    with gzip.open(cap / "r.quotes.jsonl.gz", "wt") as f:
        for q in quotes:
            f.write(json.dumps(q) + "\n")
    return str(root)


def _ctx(root, truths=None):
    cap = os.path.join(root, "kalshi", "capture")
    return C.Context(data_root=root, candidates={}, truths=truths or {}, settlements=src.settlements(cap), capture_root=cap)


def test_rows_before_the_effective_start_are_never_scored(tmp_path):
    start = "2026-09-29T00:00:00+00:00"
    rows = [_shadow_row("2026-09-28T20:00:00+00:00", "KXATPMATCH-26SEP29AAABBB-AAA", level="ITF"),
            _shadow_row("2026-09-29T06:00:00+00:00", "KXATPMATCH-26SEP29CCCDDD-CCC", level="ITF", pm="ATP:3:4:2026-09-29")]
    root = _live_root(tmp_path, rows, start)
    cand = src.load_candidates(FROZEN)["W3-2026-001-ABSTAIN-ITF"]
    res = L.harvest_w3_live(_ctx(root), cand)
    assert res.universe["history"]["producer_rows_before_effective_start"] == 1
    assert res.universe["history"]["permanently_unscorable_period"] == [cand["confirmation_start"], start]
    assert [r.ticker for r in res.evidence_rows] == ["KXATPMATCH-26SEP29CCCDDD-CCC"]
    assert all(r.captured_at >= start for r in res.evidence_rows)
    assert res.status == INSUFFICIENT_N


def test_without_a_start_record_the_candidate_stays_unscorable(tmp_path):
    root = str(tmp_path / "d")
    for sub in ("research/ledger", "research/opportunities", "research/external/dislocations", "kalshi/capture"):
        os.makedirs(os.path.join(root, sub))
    for cid in R.CANDIDATE_PRODUCER:
        res = C.HARVESTERS[cid](_ctx(root), src.load_candidates(FROZEN)[cid])
        assert res.status == UNSCORABLE_MISSING_HISTORICAL_FIELDS, cid


def test_w3_first_observation_per_contract_and_frozen_fields(tmp_path):
    tk = "KXATPMATCH-26SEP29AAABBB-AAA"
    rows = [_shadow_row("2026-09-29T01:00:00+00:00", tk, edge=-0.01),        # first observation: no edge
            _shadow_row("2026-09-29T07:00:00+00:00", tk, edge=0.05)]         # later edge is NOT a new decision
    sets = [{"ticker": tk, "result": "yes", "settlement_value_dollars": "1.0", "settlement_ts": "2026-09-29T20:00:00Z"}]
    root = _live_root(tmp_path, rows, "2026-09-29T00:00:00+00:00", settlements=sets)
    res = L.harvest_w3_live(_ctx(root), src.load_candidates(FROZEN)["W3-2026-002-NONITF-POSITIVE-EDGE"])
    assert len(res.evidence_rows) == 1 and res.evidence_rows[0].inclusion_result == ev.EXCLUDED
    assert res.exclusion_counts[ev.R_REOBSERVATION] == 1


def test_w3_002_requires_qualification_and_non_itf_and_keeps_accuracy_binding(tmp_path):
    rows = [_shadow_row("2026-09-29T01:00:00+00:00", "KXATPMATCH-26SEP29AAABBB-AAA", qual=False),
            _shadow_row("2026-09-29T01:00:00+00:00", "KXITFMATCH-26SEP29CCCDDD-CCC", level="ITF", pm="ATP:3:4:2026-09-29"),
            _shadow_row("2026-09-29T01:00:00+00:00", "KXATPMATCH-26SEP29EEEFFF-EEE", pm="ATP:5:6:2026-09-29")]
    sets = [{"ticker": "KXATPMATCH-26SEP29EEEFFF-EEE", "result": "no", "settlement_value_dollars": "0.0",
             "settlement_ts": "2026-09-29T20:00:00Z"}]
    root = _live_root(tmp_path, rows, "2026-09-29T00:00:00+00:00", settlements=sets)
    res = L.harvest_w3_live(_ctx(root), src.load_candidates(FROZEN)["W3-2026-002-NONITF-POSITIVE-EDGE"])
    inc = [r for r in res.evidence_rows if r.inclusion_result == ev.INCLUDED]
    assert [r.ticker for r in inc] == ["KXATPMATCH-26SEP29EEEFFF-EEE"]
    assert res.metrics["accuracy_condition_binding"].startswith("selected-row Brier")
    assert res.metrics["brier_fair_v1"] > res.metrics["brier_kalshi_mid"]      # worse than the mid: recorded as such


def test_ec3_evidence_band_gen1_comparison_and_post_start_exclusion(tmp_path):
    mk = lambda pm, thin, ev_=None: [_shadow_row("2026-09-29T01:00:00+00:00", f"KXATPMATCH-26SEP29{pm}-A", thin=thin, pm=pm, a=True),
                                     _shadow_row("2026-09-29T01:00:00+00:00", f"KXATPMATCH-26SEP29{pm}-B", thin=thin, pm=pm, a=False)]
    rows = mk("AAABBB", 5000.0) + mk("CCCDDD", 999.0) + mk("EEEFFF", 25000.0) + mk("GGGHHH", 5000.0)
    truths = {"KXATPMATCH-26SEP29GGGHHH": _truth("KXATPMATCH-26SEP29GGGHHH", datetime(2026, 9, 29, 0, 30, tzinfo=timezone.utc))}
    root = _live_root(tmp_path, rows, "2026-09-29T00:00:00+00:00")
    res = L.harvest_ec3_live(_ctx(root, truths), src.load_candidates(FROZEN)["EC-2026-003-GEN2-MODERATE-EVIDENCE"])
    inc = [r.physical_match_id for r in res.evidence_rows if r.inclusion_result == ev.INCLUDED]
    assert inc == ["AAABBB"]                                     # band 1,000-20,000 and not post-start
    post = [r for r in res.evidence_rows if r.physical_match_id == "GGGHHH"][0]
    assert ev.R_TIMING_POST in post.exclusion_reasons
    a = [r for r in res.evidence_rows if r.physical_match_id == "AAABBB"][0]
    assert a.fair_probability == 0.55 and a.model_probability == 0.60   # Gen-2 blend vs Gen-1 Elo, as captured
    assert res.summary.minimum_n == 1000


# ---------------------------------------------------------------------------------------------- Model 4
class _FakeG2:
    def predict_point_probs(self, a, b, tour, level, surface):
        return 0.64, 0.36

    def evidence(self, pid):
        return 5000.0


class _FakeAsof:
    base_date = datetime(2026, 6, 1).date()

    def __init__(self):
        self.calls = []

    def state(self, pid, on):
        self.calls.append(on)
        return {"elo": 1500}

    def gen2_state(self, pids, on):
        self.calls.append(on)
        return _FakeG2()


class _Mapper:
    def resolve(self, tour, name, cid, on):
        return {"status": "MAPPED", "player_id": name.split()[-1], "confidence": 1.0}


def _q(tk, rules, bid, ask, occ="2026-09-30T12:00:00Z"):
    return {"ticker": tk, "event_ticker": tk.rsplit("-", 1)[0], "status": "active", "rules_primary": rules,
            "yes_bid_dollars": str(bid), "yes_ask_dollars": str(ask), "yes_ask_size_fp": "25",
            "occurrence_datetime": occ, "captured_at": "2026-09-30T08:00:00+00:00"}


MW = "If {w} wins the Walton vs Tien professional tennis match in the 2026 ATP Tokyo Round Of 16 after a ball has been played, then the market resolves to Yes."
EX = "If {w} wins the Adam Walton vs Learner Tien professional tennis match in the 2026 ATP Tokyo Round Of 16 by a set score of {s}, then the market resolves to Yes."


def _board(with_derivs=True, swap=False):
    q = {"KXATPMATCH-26SEP30WALTIE-WAL": _q("KXATPMATCH-26SEP30WALTIE-WAL", MW.format(w="Adam Walton"), 0.40, 0.42),
         "KXATPMATCH-26SEP30WALTIE-TIE": _q("KXATPMATCH-26SEP30WALTIE-TIE", MW.format(w="Learner Tien"), 0.58, 0.60)}
    if with_derivs:
        for code, who, sc in (("WAL20", "Adam Walton", "2-0"), ("TIE21", "Learner Tien", "2-1")):
            rules = EX.format(w=who, s=sc)
            if swap:
                rules = rules.replace("Adam Walton vs Learner Tien", "Learner Tien vs Adam Walton")
            q[f"KXATPEXACTMATCH-26SEP30WALTIE-{code}"] = _q(f"KXATPEXACTMATCH-26SEP30WALTIE-{code}", rules, 0.10, 0.14)
    return q


def _build(q, started=frozenset()):
    import model4_board as M
    asof = {"ATP": _FakeAsof(), "WTA": _FakeAsof()}
    rows, sk = M.build_rows(q, asof=asof, mapper=_Mapper(), surface_of=lambda c, h: "Hard", started=set(started),
                            now=datetime(2026, 9, 30, 8, 5, tzinfo=timezone.utc), sha="t")
    return rows, sk, asof


def test_model4_records_only_listed_contracts_with_both_lanes():
    rows, sk, asof = _build(_board())
    assert sorted(r["ticker"] for r in rows) == ["KXATPEXACTMATCH-26SEP30WALTIE-TIE21", "KXATPEXACTMATCH-26SEP30WALTIE-WAL20"]
    r = rows[0]
    for k in ("physical_match_id", "model_version", "fundamental_version", "fundamental_probability",
              "conditioned_probability", "kalshi_bid", "kalshi_ask", "spread", "fee", "displayed_ask_size",
              "predicted_at", "quote_captured_at", "first_ball_status_at_prediction", "fundamental_distribution",
              "conditioned_distribution"):
        assert k in r, k
    assert r["model_version"] == "market_conditioned_v1" and r["fundamental_version"] == "gen2_dyn_hier_sr_v1"
    c = r["conditioning"]
    assert abs(c["p_market_a"] - 0.42 / (0.42 + 0.60)) < 1e-12 and c["two_sided"]
    assert abs(r["conditioned_distribution"]["p_match_a"] - c["p_market_a"]) < 1e-6    # reproduces the market
    # nothing theoretical: a board with only match-winner markets yields no derivative rows at all
    assert _build(_board(with_derivs=False))[0] == []


def test_model4_chronology_reads_states_strictly_as_of_the_match_date():
    rows, sk, asof = _build(_board())
    assert rows and all(d == datetime(2026, 9, 30).date() for d in asof["ATP"].calls)
    assert rows[0]["predicted_at"] == "2026-09-30T08:05:00+00:00"


def test_model4_refuses_started_matches_and_swapped_semantics():
    rows, sk, _ = _build(_board(), started={"26SEP30WALTIE"})
    assert rows == [] and sk["first_ball_already_observed"] == 1
    # the same contracts with the competitors named in the opposite order are refused, never flipped
    # (the parser already refuses them when the ticker side and the name side disagree)
    rows, sk, _ = _build(_board(swap=True))
    assert rows == []


def test_derivative_semantic_identity():
    import model4_board as M
    assert M.same_player("Coleman Wong", "Wong") and M.same_player("Martin Damm Jr", "Damm Jr")
    assert not M.same_player("Coleman Wong", "Vallejo") and not M.same_player("Adam Walton", "")


# ---------------------------------------------------------------------------------------------- TENNIS-15
def _t15(tmp_path, *, heartbeat_age_h=1.0, starts=True, eligible=0, status="INSUFFICIENT_N", ok_age=1.0, bad_age=None):
    rr = tmp_path / "research"; rep = rr / "candidate_confirmation"; rep.mkdir(parents=True)
    now = T0
    (rr / "frozen_producers").mkdir()
    with open(rr / "frozen_producers" / "heartbeats.jsonl", "w") as f:
        for p in ("shadow_board_v1", "model4_board_v1"):
            f.write(json.dumps({"producer": p, "ran_at": (now - timedelta(hours=heartbeat_age_h)).isoformat()}) + "\n")
    (rr / "external" / "scans").mkdir(parents=True)
    open(rr / "external" / "scans" / f"scan_{(now - timedelta(minutes=10)).strftime('%Y%m%dT%H%M%SZ')}.json", "w").write("{}")
    cap = tmp_path / "capture" / "d"; cap.mkdir(parents=True)
    json.dump({"finished_at": (now - timedelta(minutes=10)).isoformat()}, open(cap / "r.manifest.json", "w"))
    if starts:
        R.ensure_experiment_starts(str(rr / "experiment_starts"), "shadow_board_v1", started_at="2026-09-28T03:00:00+00:00",
                                   main_sha="s", candidate_defs={}, producer_version="v")
        R.ensure_experiment_starts(str(rr / "experiment_starts"), "model4_board_v1", started_at="2026-09-28T03:00:00+00:00",
                                   main_sha="s", candidate_defs={}, producer_version="v")
    for cid in G.CANDIDATE_PRODUCERS:
        json.dump({"candidate_id": cid, "status": status, "summary": {"eligible_n": eligible, "settled_n": 0, "strict_clv_n": 0},
                   "harvest_run": "20260929T110000Z"}, open(rep / f"{cid}.json", "w"))
    hs = {"last_success": (now - timedelta(hours=ok_age)).isoformat()}
    if bad_age is not None:
        hs["last_failure"] = (now - timedelta(hours=bad_age)).isoformat()
    json.dump(hs, open(rep / "HARVEST_STATUS.json", "w"))
    return G.gate_15_prospective_confirmation(str(rr), str(tmp_path / "capture"), now=now)


def test_tennis15_no_qualifying_markets_is_healthy(tmp_path):
    g = _t15(tmp_path, eligible=0)
    assert g.status == "PASS"
    assert {c["health"] for c in g.detail["candidates"].values()} == {G.HEALTHY_NO_QUALIFYING_MARKETS}
    assert all(c["producer_active"] and c["producer_required"] for c in g.detail["candidates"].values())


def test_tennis15_dead_producer_fails(tmp_path):
    g = _t15(tmp_path, heartbeat_age_h=30.0)
    assert g.status == "FAIL"
    assert g.detail["candidates"]["W3-2026-001-ABSTAIN-ITF"]["health"] == G.PRODUCER_NOT_RUNNING
    assert g.detail["candidates"]["W4-2026-001-KALSHI-LONE-OUTLIER"]["health"] == G.HEALTHY_NO_QUALIFYING_MARKETS


def test_tennis15_missing_start_record_is_a_dead_producer(tmp_path):
    g = _t15(tmp_path, starts=False)
    assert g.detail["candidates"]["EC-2026-001-MKTCOND-EXACT-SCORE"]["health"] == G.PRODUCER_NOT_RUNNING


def test_tennis15_reports_scoring_states(tmp_path):
    g = _t15(tmp_path, eligible=5, status="INSUFFICIENT_N")
    assert g.status == "PASS" and g.detail["candidates"]["W4-2026-001-KALSHI-LONE-OUTLIER"]["health"] == "INSUFFICIENT_N"


def test_failed_harvest_is_visible(tmp_path):
    g = _t15(tmp_path, ok_age=7.0, bad_age=1.0)
    assert g.status == "FAIL" and g.detail["harvest_failed"]
    assert {c["health"] for c in g.detail["candidates"].values()} == {G.HARVEST_FAILED}
    g2 = _t15(tmp_path / "later", ok_age=1.0, bad_age=7.0)     # a later success clears it
    assert g2.status == "PASS"


def test_record_failure_cli_never_erases_last_success(tmp_path):
    sys.path.insert(0, os.path.join(REPO, "scripts", "research"))
    import harvest_candidate_evidence as H
    H.record_status(str(tmp_path), success=True, run="r1", statuses={"x": "INSUFFICIENT_N"})
    H.record_status(str(tmp_path), success=False, run="", detail="boom")
    st = json.load(open(tmp_path / "HARVEST_STATUS.json"))
    assert st["last_success_run"] == "r1" and st["last_failure_detail"] == "boom" and st["last_failure"] >= st["last_success"]


# ---------------------------------------------------------------------------------------------- sibling join
def _led(pid, mid, tk, fam, a="100", b="200", tour="ATP", gen="2026-09-20T08:00:00+00:00"):
    return {"prediction_id": pid, "match_id": mid, "ticker": tk, "family": fam, "tour": tour, "player_a_id": a,
            "player_b_id": b, "generated_at_utc": gen, "market_quote": {"yes_bid": 0.40, "yes_ask": 0.42},
            "models": {}, "subject": "x", "player_a": "x"}


def _sib_ctx(tmp_path, truths):
    cap = tmp_path / "cap" / "2026-09-20"; cap.mkdir(parents=True)
    with gzip.open(cap / "r.quotes.jsonl.gz", "wt") as f:
        for tk in ("KXATPGTOTAL-26SEP20AAABBB-22", "KXATPDOUBLES-26SEP20AAABBBCCCDDD-AAABBB", "KXATPGTOTAL-26SEP20EEEFFF-22"):
            f.write(json.dumps({"ticker": tk, "captured_at": "2026-09-20T11:50:00+00:00",
                                "yes_bid_dollars": "0.45", "yes_ask_dollars": "0.47"}) + "\n")
    return C.Context(data_root=str(tmp_path), candidates={}, truths=truths, settlements={}, capture_root=str(tmp_path / "cap"))


def test_sibling_join_recovers_only_same_physical_match(tmp_path):
    fb = datetime(2026, 9, 20, 12, 0, tzinfo=timezone.utc)
    truths = {"KXATPMATCH-26SEP20AAABBB": _truth("KXATPMATCH-26SEP20AAABBB", fb),
              "KXATPSETWINNER-26SEP20EEEFFF-2": _truth("KXATPSETWINNER-26SEP20EEEFFF-2", fb)}
    rows = [_led("mw", "KXATPMATCH-26SEP20AAABBB", "KXATPMATCH-26SEP20AAABBB-AAA", "MATCH_WINNER"),
            _led("tot", "KXATPGTOTAL-26SEP20AAABBB", "KXATPGTOTAL-26SEP20AAABBB-22", "TOTAL_GAMES"),
            # doubles with the same code prefix and player ids that are pairs: a different physical match
            _led("dbl", "KXATPDOUBLES-26SEP20AAABBBCCCDDD", "KXATPDOUBLES-26SEP20AAABBBCCCDDD-AAABBB", "MATCH_WINNER",
                 a="100|300", b="200|400"),
            # truth only on a set LEG of this other match: refused as a source
            _led("leg", "KXATPSETWINNER-26SEP20EEEFFF-2", "KXATPSETWINNER-26SEP20EEEFFF-2-EEE", "SET_WINNER", a="500", b="600"),
            _led("tot2", "KXATPGTOTAL-26SEP20EEEFFF", "KXATPGTOTAL-26SEP20EEEFFF-22", "TOTAL_GAMES", a="500", b="600")]
    ctx = _sib_ctx(tmp_path, truths)
    out = SC.sibling_join_clv(ctx, rows, [])
    got = {d["prediction_id"]: d for d in out["rows"]}
    assert set(got) == {"tot"}
    d = got["tot"]
    assert d["strict"] and d["truth_source_event_id"] == "KXATPMATCH-26SEP20AAABBB"
    assert d["join_method"] == "CANONICAL_PHYSICAL_MATCH" and d["clv_join_version"] == 1
    assert d["physical_match_id"] == "ATP:singles:100:200:2026-09-20" and d["target_event_id"] == "KXATPGTOTAL-26SEP20AAABBB"
    assert out["rows_recovered_strict"] == 1 and out["families_recovered"] == {"TOTAL_GAMES": 1}
    assert out["rejected"]["source_is_a_match_leg"] == 1


def test_sibling_join_refuses_disagreeing_siblings(tmp_path):
    fb = datetime(2026, 9, 20, 12, 0, tzinfo=timezone.utc)
    truths = {"KXATPMATCH-26SEP20AAABBB": _truth("KXATPMATCH-26SEP20AAABBB", fb),
              "KXATPEXACTMATCH-26SEP20AAABBB": _truth("KXATPEXACTMATCH-26SEP20AAABBB", fb + timedelta(hours=2))}
    rows = [_led("mw", "KXATPMATCH-26SEP20AAABBB", "KXATPMATCH-26SEP20AAABBB-AAA", "MATCH_WINNER"),
            _led("ex", "KXATPEXACTMATCH-26SEP20AAABBB", "KXATPEXACTMATCH-26SEP20AAABBB-AAA20", "EXACT_SET_SCORE"),
            _led("tot", "KXATPGTOTAL-26SEP20AAABBB", "KXATPGTOTAL-26SEP20AAABBB-22", "TOTAL_GAMES")]
    out = SC.sibling_join_clv(_sib_ctx(tmp_path, truths), rows, [])
    assert out["rows"] == [] and out["rejected"]["sibling_truths_disagree"] == 1


# ---------------------------------------------------------------------------------------------- EC-004 depth
def _book(ticker, run, yes, no):
    return {"ticker": ticker, "run_id": run, "captured_at": f"2026-09-20T{run[-7:-5]}:00:00+00:00",
            "orderbook": {"orderbook_fp": {"yes_dollars": yes, "no_dollars": no}}}


def test_ec4_size_integrity_and_economics(tmp_path):
    cap = tmp_path / "cap" / "2026-09-20"; cap.mkdir(parents=True)
    rules = "If {w} wins the Walton vs Tien professional tennis match in the 2026 ATP Tokyo Round Of 16 after a ball has been played, then the market resolves to Yes."
    with gzip.open(cap / "r.quotes.jsonl.gz", "wt") as f:
        for tk, w in (("KXATPMATCH-26SEP20WALTIE-WAL", "Adam Walton"), ("KXATPMATCH-26SEP20WALTIE-TIE", "Learner Tien")):
            f.write(json.dumps({"ticker": tk, "event_ticker": tk.rsplit("-", 1)[0], "rules_primary": rules.format(w=w),
                                "captured_at": "2026-09-20T09:00:00+00:00", "run_id": "20260920T090000Z"}) + "\n")
    with gzip.open(cap / "r.books.jsonl.gz", "wt") as f:
        # pass 10:00 -- asks 0.45 + 0.50 = 0.95 on 12 contracts each: qualifies (margin after 0.04 fees = +1c)
        f.write(json.dumps(_book("KXATPMATCH-26SEP20WALTIE-WAL", "20260920T100000Z", [["0.40", "5"]], [["0.55", "12"]])) + "\n")
        f.write(json.dumps(_book("KXATPMATCH-26SEP20WALTIE-TIE", "20260920T100000Z", [["0.45", "5"]], [["0.50", "30"]])) + "\n")
        # pass 11:00 -- same prices, but only 4 contracts on one leg: must NOT count as a size-verified instance
        f.write(json.dumps(_book("KXATPMATCH-26SEP20WALTIE-WAL", "20260920T110000Z", [["0.40", "5"]], [["0.55", "4"]])) + "\n")
        f.write(json.dumps(_book("KXATPMATCH-26SEP20WALTIE-TIE", "20260920T110000Z", [["0.45", "5"]], [["0.50", "30"]])) + "\n")
    ctx = C.Context(data_root=str(tmp_path), candidates={}, truths={}, settlements={}, capture_root=str(tmp_path / "cap"))
    res = C.harvest_ec4(ctx, src.load_candidates(FROZEN)["EC-2026-004-COHERENCE-EXECUTABLE"])
    inc = [r for r in res.evidence_rows if r.inclusion_result == ev.INCLUDED]
    assert len(inc) == 1
    x = inc[0].extra
    assert x["max_size"] == 12.0 and x["qualifying_passes"] == 1 and x["passes_seen"] == 2
    assert abs(x["capital_required_per_set"] - (0.95 + 0.04)) < 1e-9 and x["guaranteed_payoff_per_set"] == 1.0
    assert abs(x["guaranteed_profit_per_set"] - 0.01) < 1e-9 and abs(x["guaranteed_profit_total"] - 0.12) < 1e-9
    assert abs(x["locked_capital_roi"] - 0.01 / 0.99) < 1e-9 and x["persisted_into_next_capture"] is True
    assert {l["size"] for l in x["leg_prices_sizes_fees"]} == {12.0, 30.0}
