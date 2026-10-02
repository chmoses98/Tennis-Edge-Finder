"""The Edge Finder app export (tennis_edge.app_export) against the vendored contract.

Fixtures under tests/fixtures/app_export are carved from REAL tennis-data records (six slate packets with their
markets, the production health gates, producer heartbeats and the assisted pipeline status), so every shape the
adapter maps is a shape production actually writes.
"""
from __future__ import annotations

import glob
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "contract"))

from edge_finder_contract import publish, sync, timeutil  # noqa: E402
from edge_finder_contract import routed_ledger as rl  # noqa: E402
from tennis_edge import app_export as ax  # noqa: E402
from tennis_edge.accounting.spec import SPEC  # noqa: E402

FIXTURE_ROOT = REPO / "tests" / "fixtures" / "app_export"
NOW = "2026-10-02T13:45:00Z"
SECRET_SHAPED = ("PRIVATE KEY", "ghp_", "github_pat_", "Bearer ", "AIRTABLE")


def _slate(root: Path) -> dict:
    return json.loads((root / "research" / "assisted_slates" / "latest.json").read_text())


def _write_slate(root: Path, slate: dict) -> None:
    (root / "research" / "assisted_slates" / "latest.json").write_text(json.dumps(slate))


def _tree_digests(root: Path) -> dict[str, str]:
    return {os.path.relpath(p, root): hashlib.sha256(Path(p).read_bytes()).hexdigest()
            for p in glob.glob(str(root / "**" / "*.json"), recursive=True)}


def _export(root: Path, out: Path, now: str = NOW, **kw) -> dict:
    return ax.export(str(root), str(out), now=timeutil.parse_ts(now), **kw)


def _load(out: Path, name: str) -> dict:
    return json.loads((out / f"{name}.json").read_text())


@pytest.fixture
def data_root(tmp_path: Path) -> Path:
    root = tmp_path / "data"
    shutil.copytree(FIXTURE_ROOT, root)
    return root


def test_vendored_contract_intact():
    assert sync.check() == []


def test_export_end_to_end_on_real_record_shapes(data_root, tmp_path):
    out = tmp_path / "app"
    manifest = _export(data_root, out)
    assert publish.verify_published(out) == []
    slate = _slate(data_root)
    events, markets = _load(out, "events")["items"], _load(out, "markets")["items"]
    assert len(events) == slate["counts"]["matches"] == 6 and len(markets) == slate["counts"]["markets"] == 18
    assert manifest["source_branch"] == "tennis-data" and manifest["model_version"] == "assisted_slate_v2"
    # identity: kalshi event ticker, players under the name namespace, match_key / physical_match_id beside
    by_kalshi = {e["source_ids"]["kalshi_event_ticker"]: e for e in events}
    for m in slate["matches"]:
        ev = by_kalshi[m["event_id"]]
        assert ev["source_ids"]["match_key"] == m["match_key"] and "physical_match_id" in ev["source_ids"]
        assert [p["display_name"] for p in ev["participants"]] == [m["players"]["a"], m["players"]["b"]]
        assert ev["home_participant"] is None and ev["away_participant"] is None and ev["status"] == "SCHEDULED"
        assert timeutil.is_canonical(ev["start_time_utc"])
    confidences = {e["source_ids"]["kalshi_event_ticker"]: e["start_time_confidence"] for e in events}
    placeholder = [m for m in slate["matches"] if m["start"]["nominal_is_placeholder"] and not m["start"]["current_expected_start"]]
    live = [m for m in slate["matches"] if (m["start"].get("start_time_source") or "").startswith("LIVE")]
    assert placeholder and all(confidences[m["event_id"]] == "PLACEHOLDER" for m in placeholder)
    assert live and all(confidences[m["event_id"]] == "ESTIMATED" for m in live)
    # markets: one per slate row, PARTICIPANT side only when the contract names a player, prices in dollars
    rows = {r["ticker"]: r for m in slate["matches"] for r in m["markets"]}
    for mk in markets:
        r = rows[mk["kalshi_ticker"]]
        assert mk["yes_bid"] == r["kalshi"]["bid"] and mk["yes_ask"] == r["kalshi"]["ask"] and mk["no_ask"] == r["kalshi"]["no_ask"]
        assert (mk["side"] == "PARTICIPANT") == isinstance(r["subject_is_a"], bool)
        assert mk["extensions"]["discrepancy_band"] == r["discrepancy_band"] and mk["market_status"] == "OPEN"
    # model prices: PRIMARY only, none for a doubles / unpriced row, envelope only from fair_v1
    prices = _load(out, "model_prices")["items"]
    priced = {p["market_id"] for p in prices}
    assert len(prices) == sum(1 for r in rows.values() if r["model_probability_yes"] is not None) > 0
    for mk in markets:
        r = rows[mk["kalshi_ticker"]]
        assert (mk["market_id"] in priced) == (r["model_probability_yes"] is not None)
    for p in prices:
        r = rows[p["market_id"][len("mkt_kalshi_"):]]
        assert p["fair_probability"] == r["model_probability_yes"] and p["model_version"] == r["model_probability_source"]
        assert p["uncertainty"] is None and p["generated_at"] == timeutil.to_iso(slate["built_at"])
        assert (p["lower_bound"] is not None) == (r["model_probability_source"].startswith("fair_v1") and bool(r["model"]["fair_v1_envelope"]))
    # recommendations: no automated pick exists; only research-only candidates the slate itself flagged
    recs = _load(out, "recommendations")["items"]
    expected = [r for m in slate["matches"] for r in m["markets"] if r["discrepancy_band"] in ax.DISAGREEMENT_BANDS
                and r["model_preferred_side"] in ("YES", "NO") and m["start"]["bet_allowed"]]
    assert len(recs) == len(expected) > 0
    assert {r["status"] for r in recs} == {"RESEARCH_CANDIDATE", "NOT_PLAYABLE"}
    for rec in recs:
        r = rows[rec["source_ids"]["kalshi_ticker"]]
        assert rec["authority"] == "RESEARCH_ONLY" and rec["research_only"] is True
        assert rec["selection"] == r["model_preferred_side"] and rec["edge"] == r["model_side_edges"][rec["selection"]]
        assert (rec["status"] == "NOT_PLAYABLE") == (r["discrepancy_sanity_status"] == "DATA_WARNING")
        assert rec["source_ids"]["slate_id"] == slate["slate_id"]
    assert _load(out, "theses")["count"] == 0 and _load(out, "wagers")["count"] == 0
    run = _load(out, "runs")["items"][0]
    assert run["source_ids"]["native_run_id"] == slate["slate_id"] and run["commit_sha"] == "74696c3bfdd083737c4ebdc50b313109e93be10a"
    health = _load(out, "health")
    assert health["bet_authority"] == "ASSISTED" and health["overall_status"] == "HEALTHY"
    assert health["components"]["export"]["status"] == "OK" and health["payload_run_id"] == manifest["run_id"]
    assert health["thresholds"]["market_data"] == {"fresh_after_seconds": 600, "stale_after_seconds": 1800}
    assert health["thresholds"]["model"] == {"fresh_after_seconds": 6 * 3600, "stale_after_seconds": 13 * 3600}
    assert health["next_scheduled_run"] == timeutil.to_iso(slate["refresh_due_by"])
    assert "TENNIS-2 taxonomy_normalization FAIL" in health["warnings"] and health["errors"] == []
    board = _load(out, "board")
    assert board["count"] == len(events) and all((out / row["detail_path"]).exists() for row in board["items"])


def test_cli_script_runs(data_root, tmp_path):
    out = tmp_path / "app"
    r = subprocess.run([sys.executable, str(REPO / "scripts" / "app_export.py"), "--data-root", str(data_root), "--out", str(out),
                        "--now", NOW], capture_output=True, text=True, cwd=str(REPO))
    assert r.returncode == 0, r.stderr
    assert "app export OK" in r.stdout and publish.verify_published(out) == []


def test_determinism(data_root, tmp_path):
    a = _export(data_root, tmp_path / "a")
    b = _export(data_root, tmp_path / "b")
    assert a["run_id"] == b["run_id"]
    assert {k: v["sha256"] for k, v in a["files"].items()} == {k: v["sha256"] for k, v in b["files"].items()}
    assert _tree_digests(tmp_path / "a") == _tree_digests(tmp_path / "b")


def test_failure_leaves_last_known_good_and_writes_health_only(data_root, tmp_path):
    out = tmp_path / "app"
    _export(data_root, out)
    before = _tree_digests(out)
    (data_root / "research" / "assisted_slates" / "latest.json").write_text("{corrupt")
    rc = ax.run_cli(["--data-root", str(data_root), "--out", str(out), "--now", "2026-10-02T13:50:00Z"])
    assert rc == 1
    after = _tree_digests(out)
    assert {k: v for k, v in after.items() if k != "health.json"} == {k: v for k, v in before.items() if k != "health.json"}
    health = _load(out, "health")
    assert health["components"]["export"]["status"] == "DEGRADED" and "failed" in health["components"]["export"]["detail"]
    assert health["overall_status"] == "DEGRADED"
    assert health["payload_run_id"] == _load(out, "manifest")["run_id"] and health["errors"]
    assert publish.verify_published(out) == []
    # nothing good yet: UNAVAILABLE, and still only a health file
    empty = tmp_path / "empty"
    assert ax.run_cli(["--data-root", str(data_root), "--out", str(empty), "--now", NOW]) == 1
    assert sorted(p.name for p in empty.iterdir()) == ["health.json"]
    assert _load(empty, "health")["overall_status"] == "UNAVAILABLE"


def test_stale_data_health(data_root, tmp_path):
    out = tmp_path / "app"
    _export(data_root, out, now="2026-10-05T00:00:00Z")
    health = _load(out, "health")
    assert health["overall_status"] == "STALE" and health["freshness_status"] == "STALE"


def test_naive_timestamp_refused(data_root, tmp_path):
    slate = _slate(data_root)
    slate["built_at"] = "2026-10-02T13:37:19"                      # no zone
    _write_slate(data_root, slate)
    with pytest.raises(timeutil.NaiveTimestampError):
        _export(data_root, tmp_path / "app")
    assert not (tmp_path / "app" / "manifest.json").exists()
    slate = _slate(data_root)
    slate["matches"][0]["start"]["nominal_scheduled_start"] = "2026-10-02T06:00:00"
    slate["matches"][0]["start"]["current_expected_start"] = None
    _write_slate(data_root, slate)
    with pytest.raises(timeutil.NaiveTimestampError):
        _export(data_root, tmp_path / "app2")


def test_no_secret_shaped_strings(data_root, tmp_path):
    out = tmp_path / "app"
    _export(data_root, out)
    for p in glob.glob(str(out / "**" / "*.json"), recursive=True):
        text = Path(p).read_text()
        for s in SECRET_SHAPED:
            assert s not in text, (p, s)


def _decision_record(slate: dict, store: Path, created_at: str) -> dict:
    """A BET decision in the shape ``tennis_edge.assisted.record.build_decision`` writes (fields the export reads)."""
    m = slate["matches"][0]
    r = m["markets"][0]
    rec = {"decision_id": "AD-20261002-0123456789ab", "schema_version": 3, "track": "CHATGPT_ASSISTED_HANDICAPPING",
           "created_at": created_at, "recorded_at": created_at, "slate_id": slate["slate_id"], "slate_built_at": slate["built_at"],
           "physical_match_id": m["physical_match_id"], "event_id": m["event_id"], "match_code": m["match_code"], "ticker": r["ticker"],
           "tour": m["tour"], "level": m["level"], "level_bucket": m["level_bucket"], "competition": m["competition"],
           "surface": m["surface"], "players": m["players"], "market_family": r["market_family"],
           "market_description": r["description"], "side": "YES", "scheduled_start": m["scheduled_start"],
           "model_probability_yes": r["model_probability_yes"], "model_probability_source": r["model_probability_source"],
           "kalshi_bid": r["kalshi"]["bid"], "kalshi_ask": r["kalshi"]["ask"], "kalshi_mid": r["kalshi"]["mid"],
           "market_implied_probability": r["kalshi"]["mid"], "side_entry_price": r["kalshi"]["ask"], "side_fee": 0.02,
           "market_quote_age_seconds": 120.0, "chatgpt_fair_probability": 0.61, "chatgpt_confidence": "MEDIUM",
           "chatgpt_thesis": "test thesis", "factor_tags": [], "model_agreement_state": "AGREED_WITH_MODEL",
           "model_preferred_side": r["model_preferred_side"], "chatgpt_preferred_side": "YES",
           "discrepancy_band": r["discrepancy_band"], "discrepancy_sanity_status": r["discrepancy_sanity_status"],
           "start_status_at_decision": m["start"]["start_status"], "chosen_expression": r["expression"],
           "decision": "BET", "recommended_price": r["kalshi"]["ask"], "bet_up_to_probability": None, "bet_up_to_price": 0.6,
           "stake_units_if_bet": 1.0, "actual_wagered": None, "authority": "ASSISTED_HUMAN_DECISION_NO_AUTOMATED_EXECUTION",
           "automated_execution": False, "warnings": []}
    p = store / "records" / "decisions" / created_at[:10] / f"{rec['decision_id']}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(rec))
    return rec


def test_wagers_settlements_and_ledger_totals(data_root, tmp_path):
    slate = _slate(data_root)
    r0 = slate["matches"][0]["markets"][0]
    ticker = r0["ticker"]
    # ---- routed ledger (accounting-data): one settled wager, one SCALAR settlement on a market no longer listed
    acc = tmp_path / "accounting-data"
    rows = [{"source_bet_key": "k:1", "import_batch_id": "b1", "entry_method": "IMPORTED_RECEIPT", "game_date": "2026-10-02",
             "market_ticker": ticker, "side": "YES", "executed_at": "2026-10-02T13:40:00Z", "contracts": 10,
             "execution_price": 0.55, "stake": 5.57, "fees_paid": 0.07, "fees_are_estimated": False, "venue": "kalshi"},
            {"source_bet_key": "k:2", "import_batch_id": "b1", "entry_method": "IMPORTED_RECEIPT", "game_date": "2026-09-30",
             "market_ticker": "KXATPMATCH-26SEP30ABCDEF-ABC", "side": "NO", "executed_at": "2026-09-30T10:00:00Z", "contracts": 4,
             "execution_price": 0.5, "stake": 2.04, "fees_paid": 0.04, "fees_are_estimated": False, "venue": "kalshi"}]
    res = rl.import_wagers(SPEC, acc, rows, import_batch_id="b1")
    assert res.written == 2
    sres = rl.import_settlements(SPEC, acc, [
        {"source_bet_key": "k:1", "market_ticker": ticker, "side": "YES", "settlement_status": "SETTLED",
         "settled_at": "2026-10-02T20:00:00Z", "result": "WON", "gross_return": 10.0, "net_profit_loss": 4.43, "refusals": [],
         "venue": "kalshi", "economics_version": rl.ECONOMICS_V2},
        {"source_bet_key": "k:2", "market_ticker": "KXATPMATCH-26SEP30ABCDEF-ABC", "side": "NO", "settlement_status": "SETTLED",
         "settled_at": "2026-09-30T20:00:00Z", "result": None, "gross_return": 2.2, "net_profit_loss": 0.16, "refusals": [],
         "venue": "kalshi", "economics_version": rl.ECONOMICS_V2}])
    assert sres.written == 2
    # ---- assisted track: a BET decision recorded BEFORE a human-recorded wager on the same contract
    store = data_root / "research" / "assisted_decisions"
    dec = _decision_record(slate, store, "2026-10-02T13:38:00+00:00")
    aw = {"wager_id": "AW-20261002-0123456789ab", "decision_id": dec["decision_id"], "schema_version": 3,
          "recorded_at": "2026-10-02T13:42:00+00:00", "placed_at": "2026-10-02T13:41:00+00:00", "ticker": ticker, "side": "YES",
          "entry_price": r0["kalshi"]["ask"], "contracts": 5, "stake_dollars": round(5 * r0["kalshi"]["ask"], 2), "fees": 0.05,
          "source": "MANUAL_KALSHI_UI", "status": "FILLED", "external_order_id": "ord-123", "decision_was_bet": True,
          "placed_after_first_ball": False, "first_ball_status_at_placement": "NOT_OBSERVED_STARTED",
          "input_payload_sha256": "0" * 64, "authority": "ASSISTED_HUMAN_DECISION_NO_AUTOMATED_EXECUTION", "warnings": []}
    p = store / "records" / "wagers" / "2026-10-02" / f"{aw['wager_id']}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(aw))

    out = tmp_path / "app"
    _export(data_root, out, now="2026-10-03T00:00:00Z", accounting_dir=str(acc))
    assert publish.verify_published(out) == []
    wagers = {w["source_bet_key"] or w["source_ids"]["assisted_wager_id"]: w for w in _load(out, "wagers")["items"]}
    settlements = {s["wager_id"]: s for s in _load(out, "settlements")["items"]}
    markets = {m["market_id"]: m for m in _load(out, "markets")["items"]}
    assert set(wagers) == {"k:1", "k:2", "AW-20261002-0123456789ab"}
    w1, w2, wa = wagers["k:1"], wagers["k:2"], wagers["AW-20261002-0123456789ab"]
    assert w1["source"] == "KALSHI_ROUTER" and w1["settlement_status"] == "SETTLED" and w1["profit_loss"] == 4.43 and w1["fees"] == 0.07
    assert settlements[w1["wager_id"]]["result"] == "WON" and settlements[w1["wager_id"]]["verification_status"] == "EXCHANGE_CONFIRMED"
    assert settlements[w2["wager_id"]]["result"] == "SCALAR" and w2["payout"] == 2.2
    assert markets[w2["market_id"]]["market_status"] == "SETTLED" and markets[w2["market_id"]]["yes_bid"] is None   # stub
    assert w1["event_id"] == markets[w1["market_id"]]["event_id"] is not None
    assert wa["source"] == "MANUAL" and wa["source_ids"]["external_order_id"] == "ord-123" and wa["settlement_status"] == "PENDING"
    # temporal linkage: the decision (13:38) and the slate's model price (13:37) predate the assisted wager (13:41)
    recs = {r["source_ids"].get("decision_id"): r for r in _load(out, "recommendations")["items"]}
    rec = recs[dec["decision_id"]]
    assert rec["status"] == "RECOMMENDED" and rec["authority"] == "ASSISTED" and rec["research_only"] is False
    assert rec["fair_probability"] == 0.61 and rec["selection"] == "YES"
    assert wa["recommendation_id"] == rec["recommendation_id"] and wa["model_price_id"] is not None
    assert w1["recommendation_id"] == rec["recommendation_id"]     # same contract, decision predates the fill: temporal link
    assert w2["recommendation_id"] is None and w2["model_price_id"] is None   # nothing predates it: null, never the nearest
    # ledger P&L totals equal the ledger's own sums
    perf = _load(out, "performance")
    ledger_pnl = sum(s["net_profit_loss"] for s in rl.read_jsonl(SPEC.settlements_path(acc)))
    assert perf["by_source"]["KALSHI_ROUTER"]["net_pnl"] == round(ledger_pnl, 4)
    assert perf["totals"]["wagers"] == 3 and perf["totals"]["settled"] == 2 and perf["totals"]["pending"] == 1
    assert perf["totals"]["scalar"] == 1 and perf["totals"]["won"] == 1
    assert perf["data_completeness"]["settlements_with_economics"] == 2


def _real_data_root() -> Path | None:
    env = os.environ.get("TENNIS_DATA_ROOT")
    for cand in ([Path(env)] if env else []) + [REPO / "data"]:
        if (cand / "research" / "assisted_slates" / "latest.json").exists():
            return cand
    return None


def test_real_data_smoke(tmp_path):
    root = _real_data_root()
    if root is None:
        pytest.skip("production assisted slate lives on the tennis-data branch (tennis-edge-finder/data), not checked out; "
                    "set TENNIS_DATA_ROOT to run")
    out = tmp_path / "app"
    manifest = _export(root, out)
    assert publish.verify_published(out) == []
    assert manifest["counts"]["events"] > 0 and manifest["counts"]["markets"] > 0
