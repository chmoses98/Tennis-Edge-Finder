"""The TENNIS routed-wager accounting ledger: thin stdlib wrappers over the vendored shared ledger.

ACCOUNTING ONLY. These tests prove the guarantees docs/ACCOUNTING.md states: deterministic identity minted from
``source_bet_key``; same row twice -> DUPLICATE_NOOP with zero bytes changed; different economics -> CONFLICT and
nothing rewritten; model/recommendation provenance refused; orphan settlements refused; a SCALAR tennis
settlement (result None, money established) accepted; the validator; and that the scripts' public stdout never
carries a ticker, price, stake or key.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "contract"))

from edge_finder_contract import routed_ledger as rl  # noqa: E402
from tennis_edge.accounting.spec import SPEC  # noqa: E402

KEY = "kalshi:order:tennis-test-0001"
TICKER = "KXATPMATCH-26OCT01SAWHAN-SAW"


def wager_row(**over) -> dict:
    row = {"source_bet_key": KEY, "import_batch_id": "batch-1", "entry_method": "IMPORTED_RECEIPT",
           "game_date": "2026-10-01", "market_ticker": TICKER, "side": "YES", "executed_at": "2026-10-01T10:00:00Z",
           "contracts": 10, "execution_price": 0.55, "stake": 5.57, "fees_paid": 0.07, "fees_are_estimated": False,
           "venue": "kalshi"}
    row.update(over)
    return row


def settlement_row(**over) -> dict:
    row = {"source_bet_key": KEY, "market_ticker": TICKER, "side": "YES", "settlement_status": "SETTLED",
           "settled_at": "2026-10-02T01:00:00Z", "result": "WON", "gross_return": 10.0, "net_profit_loss": 4.43,
           "refusals": [], "venue": "kalshi", "economics_version": rl.ECONOMICS_V2}
    row.update(over)
    return row


def test_spec_is_the_tennis_ledger_and_stdlib_only():
    assert SPEC.sport == "TENNIS" and SPEC.id_prefix == "ten"
    assert SPEC.wager_schema == "tennis_accounted_wager.v1"
    assert SPEC.settlement_schema == "tennis_wager_settlement.v1"
    assert SPEC.mint_wager_id(KEY).startswith("tenw-") and SPEC.mint_settlement_id(KEY).startswith("tens-")
    assert SPEC.mint_wager_id(KEY) == SPEC.mint_wager_id(KEY)
    # importing the spec must not pull numpy/pandas (the router's runner installs nothing from this repo)
    code = ("import sys; sys.modules['numpy'] = None; sys.modules['pandas'] = None; "
            "import tennis_edge.accounting.spec as s; print(s.SPEC.id_prefix)")
    out = subprocess.run([sys.executable, "-c", code], cwd=str(REPO), capture_output=True, text=True, check=True)
    assert out.stdout.strip() == "ten"


def test_new_then_duplicate_noop_is_byte_identical(tmp_path):
    r1 = rl.import_wagers(SPEC, tmp_path, [wager_row()], import_batch_id="batch-1")
    assert (r1.written, r1.duplicate, r1.refused) == (1, 0, 0)
    assert r1.rows[0]["status"] == rl.NEW and r1.rows[0]["wager_id"] == SPEC.mint_wager_id(KEY)
    before = SPEC.wagers_path(tmp_path).read_bytes()
    r2 = rl.import_wagers(SPEC, tmp_path, [wager_row()], import_batch_id="batch-1")
    assert (r2.written, r2.duplicate, r2.refused) == (0, 1, 0) and r2.rows[0]["status"] == rl.DUPLICATE_NOOP
    assert SPEC.wagers_path(tmp_path).read_bytes() == before
    rec = rl.read_jsonl(SPEC.wagers_path(tmp_path))[0]
    assert rec["schema_version"] == "tennis_accounted_wager.v1" and rec["wager_id"].startswith("tenw-")


def test_conflict_never_rewrites(tmp_path):
    rl.import_wagers(SPEC, tmp_path, [wager_row()], import_batch_id="batch-1")
    before = SPEC.wagers_path(tmp_path).read_bytes()
    r = rl.import_wagers(SPEC, tmp_path, [wager_row(contracts=20, stake=11.07)], import_batch_id="batch-1")
    assert r.refused == 1 and r.conflicted and r.rows[0]["status"] == rl.CONFLICT
    assert set(r.rows[0]["conflicting_fields"]) == {"contracts", "stake"}
    assert SPEC.wagers_path(tmp_path).read_bytes() == before


def test_provenance_refused(tmp_path):
    r = rl.import_wagers(SPEC, tmp_path, [wager_row(model_probability=0.6)], import_batch_id="batch-1")
    assert r.refused == 1 and "provenance" in r.rows[0]["reason"]
    assert not SPEC.wagers_path(tmp_path).exists()
    rl.import_wagers(SPEC, tmp_path, [wager_row()], import_batch_id="batch-1")
    s = rl.import_settlements(SPEC, tmp_path, [settlement_row(decision_id="AD-20261001-abc")])
    assert s.refused == 1 and "provenance" in s.rows[0]["reason"]
    assert not SPEC.settlements_path(tmp_path).exists()


def test_orphan_settlement_refused(tmp_path):
    r = rl.import_settlements(SPEC, tmp_path, [settlement_row()])
    assert r.refused == 1 and r.rows[0]["reason"].startswith("ORPHAN")
    assert not SPEC.settlements_path(tmp_path).exists()


def test_scalar_settlement_result_none_with_established_money_accepted(tmp_path):
    rl.import_wagers(SPEC, tmp_path, [wager_row()], import_batch_id="batch-1")
    # a walkover settles at a fair price strictly between 0 and 1: the exchange states the money, result is None
    row = settlement_row(result=None, gross_return=6.2, net_profit_loss=0.63)
    r = rl.import_settlements(SPEC, tmp_path, [row])
    assert (r.written, r.refused) == (1, 0) and r.rows[0]["settlement_id"] == SPEC.mint_settlement_id(KEY)
    rec = rl.read_jsonl(SPEC.settlements_path(tmp_path))[0]
    assert rec["result"] is None and rec["gross_return"] == 6.2 and rec["schema_version"] == "tennis_wager_settlement.v1"
    before = SPEC.settlements_path(tmp_path).read_bytes()
    again = rl.import_settlements(SPEC, tmp_path, [row])
    assert again.duplicate == 1 and SPEC.settlements_path(tmp_path).read_bytes() == before
    other = rl.import_settlements(SPEC, tmp_path, [settlement_row(result="LOST", gross_return=0.0, net_profit_loss=-5.57)])
    assert other.refused == 1 and other.rows[0]["status"] == rl.CONFLICT
    assert SPEC.settlements_path(tmp_path).read_bytes() == before


def test_validator(tmp_path):
    assert rl.validate_ledger(SPEC, tmp_path)["ok"]
    rl.import_wagers(SPEC, tmp_path, [wager_row()], import_batch_id="batch-1")
    rl.import_settlements(SPEC, tmp_path, [settlement_row()])
    res = rl.validate_ledger(SPEC, tmp_path)
    assert res["ok"] and res["counts"] == {"wagers": 1, "settlements": 1}
    with SPEC.settlements_path(tmp_path).open("a") as fh:
        fh.write(json.dumps({**settlement_row(source_bet_key="other"), "settlement_id": SPEC.mint_settlement_id("other"),
                             "schema_version": SPEC.settlement_schema}) + "\n")
    res = rl.validate_ledger(SPEC, tmp_path)
    assert not res["ok"] and any("ORPHAN" in f for f in res["failures"])
    for f in res["failures"]:
        assert TICKER not in f and KEY not in f


SECRET_SHAPED = (TICKER, KEY, "0.55", "5.57", "4.43")


def _run(script: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(REPO / "scripts" / "accounting" / script), *args],
                          cwd=str(REPO), capture_output=True, text=True, check=False)


def test_scripts_end_to_end_print_no_ticker_price_or_key(tmp_path):
    base = tmp_path / "accounting-data"
    base.mkdir()
    wp = tmp_path / "wagers.json"
    wp.write_text(json.dumps({"importBatchId": "batch-1", "rows": [wager_row()]}))
    r = _run("import_routed_wagers.py", "--payload", str(wp), "--base-dir", str(base), "--receipts-out", str(tmp_path / "wr.json"))
    assert r.returncode == 0, r.stdout + r.stderr
    assert "written:         1" in r.stdout
    receipts = json.loads((tmp_path / "wr.json").read_text())
    assert receipts["importBatchId"] == "batch-1" and receipts["rows"][0]["status"] == "NEW"
    # re-delivery: DUPLICATE_NOOP, exit 0, zero bytes changed
    before = SPEC.wagers_path(base).read_bytes()
    r = _run("import_routed_wagers.py", "--payload", str(wp), "--base-dir", str(base))
    assert r.returncode == 0 and "already present: 1" in r.stdout and SPEC.wagers_path(base).read_bytes() == before
    # conflicting economics: exit 1, nothing rewritten, stdout names fields not values
    cp = tmp_path / "conflict.json"
    cp.write_text(json.dumps({"importBatchId": "batch-1", "rows": [wager_row(contracts=20, stake=11.07)]}))
    r = _run("import_routed_wagers.py", "--payload", str(cp), "--base-dir", str(base))
    assert r.returncode == 1 and "CONFLICT" in r.stdout and SPEC.wagers_path(base).read_bytes() == before
    sp = tmp_path / "settlements.json"
    sp.write_text(json.dumps({"settlements": [settlement_row(result=None, gross_return=6.2, net_profit_loss=0.63)]}))
    r = _run("import_routed_settlements.py", "--payload", str(sp), "--base-dir", str(base), "--receipts-out", str(tmp_path / "sr.json"))
    assert r.returncode == 0 and "written:         1" in r.stdout, r.stdout + r.stderr
    r = _run("validate_routed_ledger.py", "--base-dir", str(base), "--result-out", str(tmp_path / "v.json"))
    assert r.returncode == 0 and "wagers=1 settlements=1 problems=0" in r.stdout
    assert json.loads((tmp_path / "v.json").read_text())["passed"] is True
    for proc_out in (r.stdout, r.stderr):
        for s in SECRET_SHAPED:
            assert s not in proc_out
    # unreadable payload: exit 2, reason is a type name only
    bad = tmp_path / "bad.json"
    bad.write_text("{not json")
    r = _run("import_routed_wagers.py", "--payload", str(bad), "--base-dir", str(base))
    assert r.returncode == 2 and "unreadable payload" in r.stderr


@pytest.mark.parametrize("script", ["import_routed_wagers.py", "import_routed_settlements.py", "validate_routed_ledger.py"])
def test_scripts_run_without_numpy_or_pandas(script, tmp_path):
    """The router's runner installs nothing from this repository: the scripts must be stdlib-only."""
    blockers = tmp_path / "blockers"
    blockers.mkdir()
    for m in ("numpy", "pandas", "scipy", "sklearn", "pyarrow"):
        (blockers / f"{m}.py").write_text("raise ImportError('blocked')\n")
    env = {**os.environ, "PYTHONPATH": str(blockers)}
    r = subprocess.run([sys.executable, str(REPO / "scripts" / "accounting" / script), "--help"], cwd=str(REPO),
                       capture_output=True, text=True, env=env)
    assert r.returncode == 0, r.stderr
