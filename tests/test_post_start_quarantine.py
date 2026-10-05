"""TENNIS-6 legacy quarantine: history stays auditable, active leaks can never be hidden."""
import json
import os
from datetime import datetime, timedelta, timezone

import pytest

from tennis_edge.health.gates import gate_6_no_post_start_leakage
from tennis_edge.ledger import quarantine as q

G = q.GUARD_DEPLOYED_AT


def _row(pid, gen):
    return {"prediction_id": pid, "match_id": f"M-{pid}", "generated_at_utc": gen.isoformat(), "ticker": "T", "series_ticker": "S"}


def _setup(tmp_path):
    first_ball = G - timedelta(days=2)
    rows = [_row("old_leak", first_ball + timedelta(minutes=30)),           # priced in play, before the guard
            _row("clean", first_ball - timedelta(hours=3))]
    starts = {"M-old_leak": (first_ball, first_ball, first_ball + timedelta(minutes=4)),
              "M-clean": (first_ball, first_ball)}
    return rows, starts


def test_legacy_rows_quarantined_gate_passes_and_ledger_untouched(tmp_path):
    rows, starts = _setup(tmp_path)
    before = json.dumps(rows, sort_keys=True)
    assert q.append(str(tmp_path), q.legacy_violations(rows, starts)) == 1
    assert q.append(str(tmp_path), q.legacy_violations(rows, starts)) == 0          # idempotent
    reg, problems = q.load(str(tmp_path))
    g = gate_6_no_post_start_leakage(rows, starts, [], reg, problems)
    assert g.status == "PASS" and g.detail["legacy_quarantined"] == 1 and g.detail["n_violations"] == 1
    assert json.dumps(rows, sort_keys=True) == before


def test_post_guard_leak_cannot_be_quarantined_and_fails_the_gate(tmp_path):
    rows, starts = _setup(tmp_path)
    fb = G + timedelta(days=1)
    rows.append(_row("new_leak", fb + timedelta(minutes=10)))
    starts["M-new_leak"] = (fb, fb)
    assert all(v["prediction_id"] != "new_leak" for v in q.legacy_violations(rows, starts))
    with pytest.raises(ValueError):
        q.append(str(tmp_path), [{"prediction_id": "new_leak", "match_id": "M-new_leak",
                                  "generated_at_utc": (fb + timedelta(minutes=10)).isoformat()}])
    q.append(str(tmp_path), q.legacy_violations(rows, starts))
    reg, problems = q.load(str(tmp_path))
    g = gate_6_no_post_start_leakage(rows, starts, [], reg, problems)
    assert g.status == "FAIL" and g.detail["active_violations"] == 1 and "new_leak" in g.detail["active_violation_ids"]


def test_unregistered_legacy_violation_still_fails(tmp_path):
    rows, starts = _setup(tmp_path)
    g = gate_6_no_post_start_leakage(rows, starts, [], {}, [])
    assert g.status == "FAIL" and g.detail["active_violations"] == 1


def test_strict_research_leak_fails_even_with_register(tmp_path):
    rows, starts = _setup(tmp_path)
    q.append(str(tmp_path), q.legacy_violations(rows, starts))
    reg, problems = q.load(str(tmp_path))
    g = gate_6_no_post_start_leakage(rows, starts, [{"strict": True, "timing_class": "POST_START"}], reg, problems)
    assert g.status == "FAIL"


def test_tampered_register_is_detected_and_fails(tmp_path):
    rows, starts = _setup(tmp_path)
    q.append(str(tmp_path), q.legacy_violations(rows, starts))
    p = os.path.join(str(tmp_path), q.REGISTER)
    rec = json.loads(open(p).read().splitlines()[0])
    rec["reason"] = "edited"
    open(p, "w").write(json.dumps(rec) + "\n")
    reg, problems = q.load(str(tmp_path))
    assert problems
    assert gate_6_no_post_start_leakage(rows, starts, [], reg, problems).status == "FAIL"


def test_post_settlement_rows_detected_without_first_ball_truth(tmp_path):
    """An ITF row (no first-ball source) priced after the exchange settled is a certain post-start violation."""
    settled = G + timedelta(days=3)
    old = {**_row("itf_old", settled + timedelta(minutes=8)), "git_sha": "oldsha"}
    new = {**_row("itf_new", settled + timedelta(minutes=8)), "git_sha": "newsha"}
    ok = {**_row("itf_ok", settled - timedelta(hours=5)), "git_sha": "newsha"}
    rows = [old, new, ok]
    settled_at = {"itf_old": settled, "itf_new": settled, "itf_ok": settled}
    # Kalshi's ITF nominal start is hours AFTER the real first ball: the schedule check alone passes these rows
    starts = {f"M-{p}": (None, settled + timedelta(days=1)) for p in ("itf_old", "itf_new", "itf_ok")}
    g0 = gate_6_no_post_start_leakage(rows, starts, [], {}, [], settled_at)
    assert g0.status == "FAIL" and g0.detail["violation_classes"]["post_settlement"] == 2
    entries = q.legacy_violations(rows, {}, settled_at, legacy_shas={"oldsha"})
    assert [e["prediction_id"] for e in entries] == ["itf_old"]          # new-code row is never eligible
    with pytest.raises(ValueError):
        q.append(str(tmp_path), [{**e, "prediction_id": "itf_new", "git_sha": "newsha"} for e in entries])
    import tennis_edge.ledger.quarantine as qq
    orig = qq.pre_lifecycle_guard_shas
    qq.pre_lifecycle_guard_shas = lambda: {"oldsha"}
    try:
        q.append(str(tmp_path / "r2"), entries)
        reg, problems = q.load(str(tmp_path / "r2"))
        g = gate_6_no_post_start_leakage(rows, starts, [], reg, problems, settled_at)
    finally:
        qq.pre_lifecycle_guard_shas = orig
    assert g.status == "FAIL" and g.detail["active_violations"] == 1 and g.detail["legacy_quarantined"] == 1
