"""TENNIS-5 (2026-10-06): pricing-quote freshness and background-capture health are separate checks.

Before the split the gate failed on the age, at health-evaluation time, of the newest capture in RUN TENNIS's pulled
copy (20-34 min) although the quote each row was priced on was seconds old. These tests pin the new semantics:
neither threshold was loosened, a stale pricing quote still fails, an unhealthy conductor still fails, and the
pulled-artifact age is reported under its own name and never decides the status."""
import json
from datetime import datetime, timedelta, timezone

import pytest

from tennis_edge.health import gates as G

NOW = datetime(2026, 10, 6, 12, 0, tzinfo=timezone.utc)


def _capture(tmp_path, finishes, incomplete_last=False, backlog_age_s=None):
    for i, fin in enumerate(finishes):
        day = tmp_path / "data" / "kalshi" / "capture" / fin.strftime("%Y-%m-%d")
        day.mkdir(parents=True, exist_ok=True)
        rid = fin.strftime("%Y%m%dT%H%M%SZ")
        m = {"run_id": rid, "started_at": (fin - timedelta(minutes=4)).isoformat(), "finished_at": fin.isoformat(),
             "incomplete": [{"stage": "x"}] if (incomplete_last and i == len(finishes) - 1) else [],
             "trades": {"backlog": {"oldest_gap_age_s": backlog_age_s}} if backlog_age_s is not None else {}}
        json.dump(m, open(day / f"{rid}.manifest.json", "w"))


def _projection_run(tmp_path, quote_ages_s, priced_at, snapshot_age_s=4.0, drop_age_for=()):
    pj = tmp_path / "data" / "research" / "projections"
    pj.mkdir(parents=True, exist_ok=True)
    rows = []
    for i, a in enumerate(quote_ages_s):
        mq = {"source": "open_snapshot", "quote_ts": (priced_at - timedelta(seconds=a)).isoformat(),
              "priced_at": priced_at.isoformat(), "quote_age_s": a}
        if i in drop_age_for:
            mq = {"source": "discovery_record"}
        rows.append({"ticker": f"T{i}", "market_quote": mq})
    json.dump({"run_id": "P1"}, open(pj / "latest.json", "w"))
    json.dump({"run_id": "P1", "generated_at": priced_at.isoformat(),
               "lifecycle": {"open_snapshot_run": "S1", "open_snapshot_age_s": snapshot_age_s, "snapshot_authoritative": True},
               "projections": rows}, open(pj / "P1.json", "w"))


def _healthy_conductor(tmp_path, pulled_at):
    # a pass every ~10 min for the last 7 h before the pull, newest 4 min before the pull
    fins = [pulled_at - timedelta(minutes=4 + 10 * k) for k in range(42)][::-1]
    _capture(tmp_path, fins)


@pytest.fixture
def proj(tmp_path, monkeypatch):
    monkeypatch.setattr(G, "PROJ", str(tmp_path))
    return tmp_path


def test_production_shape_passes_and_pulled_age_is_reported_not_judged(proj):
    """The 2026-10-05 production situation: conductor every ~10 min, quotes seconds old at pricing, health evaluated
    ~24 min after the pull. PASS -- and the 24-min figure is visible under its own unambiguous name."""
    pulled = NOW - timedelta(minutes=20)
    _healthy_conductor(proj, pulled)
    _projection_run(proj, [4.0, 30.0, 95.0], priced_at=pulled + timedelta(minutes=8))
    g = G.gate_5_capture_freshness(now=NOW, pull_record={"pulled_at": pulled.isoformat()})
    assert g.status == "PASS"
    d = g.detail
    assert d["pricing_quote_freshness"] == "PASS" and d["background_capture_health"] == "PASS"
    assert d["pulled_capture_artifact_age_min"] == pytest.approx(24.0, abs=0.1)
    assert "NOT the age of any quote" in d["pulled_capture_artifact_age_note"]
    assert "age_min" not in d                      # the ambiguous old key is gone
    pq = d["pricing_quote"]
    assert pq["max_age_s"] == 95.0 and pq["n_over_threshold"] == 0 and pq["open_snapshot_age_at_pricing_s"] == 4.0
    assert pq["priced_at_last"] and pq["quote_ts_oldest"]
    cap = d["capture"]
    assert cap["capture_age_at_measurement_min"] == pytest.approx(4.0, abs=0.1) and cap["measured_at_kind"] == "pull"
    assert cap["cadence_median_min"] == pytest.approx(10.0, abs=0.1) and cap["gaps_over_threshold_min"] == []


def test_stale_pricing_quote_fails_even_with_a_healthy_conductor(proj):
    pulled = NOW - timedelta(minutes=20)
    _healthy_conductor(proj, pulled)
    _projection_run(proj, [5.0, 31 * 60.0], priced_at=pulled + timedelta(minutes=8))
    g = G.gate_5_capture_freshness(now=NOW, pull_record={"pulled_at": pulled.isoformat()})
    assert g.status == "FAIL"
    assert g.detail["pricing_quote_freshness"] == "FAIL" and g.detail["background_capture_health"] == "PASS"
    assert g.detail["pricing_quote"]["n_over_threshold"] == 1


def test_threshold_is_thirty_minutes_not_looser():
    assert G.GATE5_MAX_AGE_MIN == 30
    import inspect
    assert inspect.signature(G.gate_5_capture_freshness).parameters["max_age_min"].default == 30


def test_quote_of_unknown_age_fails_closed(proj):
    pulled = NOW - timedelta(minutes=20)
    _healthy_conductor(proj, pulled)
    _projection_run(proj, [5.0, 6.0], priced_at=pulled + timedelta(minutes=8), drop_age_for=(1,))
    g = G.gate_5_capture_freshness(now=NOW, pull_record={"pulled_at": pulled.isoformat()})
    assert g.status == "FAIL" and g.detail["pricing_quote"]["n_age_unknown"] == 1


def test_no_projection_run_is_not_a_pass(proj):
    pulled = NOW - timedelta(minutes=20)
    _healthy_conductor(proj, pulled)
    g = G.gate_5_capture_freshness(now=NOW, pull_record={"pulled_at": pulled.isoformat()})
    assert g.status == "UNKNOWN"


def test_stale_conductor_at_pull_fails_even_with_fresh_pricing_quotes(proj):
    pulled = NOW - timedelta(minutes=20)
    _capture(proj, [pulled - timedelta(minutes=45 + 10 * k) for k in range(40)][::-1])   # newest pass 45 min before pull
    _projection_run(proj, [4.0], priced_at=pulled + timedelta(minutes=8))
    g = G.gate_5_capture_freshness(now=NOW, pull_record={"pulled_at": pulled.isoformat()})
    assert g.status == "FAIL"
    assert g.detail["background_capture_health"] == "FAIL" and g.detail["pricing_quote_freshness"] == "PASS"


def test_a_gap_inside_the_cadence_window_fails(proj):
    pulled = NOW - timedelta(minutes=20)
    fins = [pulled - timedelta(minutes=4 + 10 * k) for k in range(10)]                    # last 1.5 h healthy
    fins += [pulled - timedelta(minutes=4 + 90 + 40 + 10 * k) for k in range(30)]         # a 40-min hole before it
    _capture(proj, sorted(fins))
    _projection_run(proj, [4.0], priced_at=pulled + timedelta(minutes=8))
    g = G.gate_5_capture_freshness(now=NOW, pull_record={"pulled_at": pulled.isoformat()})
    assert g.status == "FAIL" and g.detail["capture"]["gaps_over_threshold_min"]


def test_incomplete_latest_pass_and_old_backlog_still_fail(proj):
    pulled = NOW - timedelta(minutes=20)
    _capture(proj, [pulled - timedelta(minutes=4 + 10 * k) for k in range(40)][::-1], incomplete_last=True)
    _projection_run(proj, [4.0], priced_at=pulled + timedelta(minutes=8))
    assert G.gate_5_capture_freshness(now=NOW, pull_record={"pulled_at": pulled.isoformat()}).status == "FAIL"


def test_old_trade_backlog_fails(proj):
    pulled = NOW - timedelta(minutes=20)
    _capture(proj, [pulled - timedelta(minutes=4 + 10 * k) for k in range(40)][::-1], backlog_age_s=3 * 3600)
    _projection_run(proj, [4.0], priced_at=pulled + timedelta(minutes=8))
    g = G.gate_5_capture_freshness(now=NOW, pull_record={"pulled_at": pulled.isoformat()})
    assert g.status == "FAIL" and g.detail["trade_backlog_ok"] is False


def test_without_a_pull_record_conductor_age_is_measured_now_strictly(proj):
    """No pull record -> the conductor is judged at evaluation time (stricter), and the detail says so."""
    pulled = NOW - timedelta(minutes=40)
    _healthy_conductor(proj, pulled)                 # newest pass 44 min before NOW
    _projection_run(proj, [4.0], priced_at=pulled + timedelta(minutes=8))
    g = G.gate_5_capture_freshness(now=NOW)
    assert g.status == "FAIL" and g.detail["capture"]["measured_at_kind"].startswith("evaluation")


def test_pull_record_is_read_from_data_dir(proj):
    pulled = NOW - timedelta(minutes=20)
    _healthy_conductor(proj, pulled)
    _projection_run(proj, [4.0], priced_at=pulled + timedelta(minutes=8))
    json.dump({"pulled_at": pulled.isoformat()}, open(proj / "data" / ".pull_record.json", "w"))
    g = G.gate_5_capture_freshness(now=NOW)
    assert g.status == "PASS" and g.detail["capture"]["measured_at_kind"] == "pull"


def test_run_tennis_records_quote_age_at_pricing_time():
    from scripts.run_tennis import quote_provenance
    priced = datetime(2026, 10, 6, 12, 0, 4, tzinfo=timezone.utc)
    rec = {"captured_at": "2026-10-06T12:00:00+00:00"}
    src, q_ts, age, priced_at = quote_provenance("T", rec, {"T": rec}, {"T": rec}, True, {"started_at": "x"}, now=priced)
    assert src == "open_snapshot" and q_ts == rec["captured_at"] and age == 4.0 and priced_at == priced.isoformat()
    src, *_ = quote_provenance("T", rec, {"T": rec}, None, False, {"started_at": "x"}, now=priced)
    assert src == "capture"
