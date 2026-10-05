"""Lifecycle + freshness guards added 2026-10-05: never price a settled market, never call an old quote fresh."""
import gzip
import json
import os
import sys
from datetime import datetime, timedelta, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import run_tennis as RT                                                    # noqa: E402
from tennis_edge.assisted.slate import overlay_run_snapshot               # noqa: E402
from tennis_edge.health.gates import gate_10_clv_coverage                 # noqa: E402


def _snapshot(root, now, tickers, complete=True, age_min=2):
    day = os.path.join(root, now.strftime("%Y-%m-%d"))
    os.makedirs(day, exist_ok=True)
    rid = (now - timedelta(minutes=age_min)).strftime("%Y%m%dT%H%M%SZ")
    with gzip.open(os.path.join(day, f"{rid}.open_snapshot.jsonl.gz"), "wt") as f:
        for t in tickers:
            f.write(json.dumps({"ticker": t, "status": "active", "captured_at": (now - timedelta(minutes=age_min)).isoformat(),
                                "yes_bid_dollars": "0.40", "yes_ask_dollars": "0.42"}) + "\n")
    json.dump({"run_id": rid, "finished_at": (now - timedelta(minutes=age_min)).isoformat(), "complete": complete},
              open(os.path.join(day, f"{rid}.open_snapshot.manifest.json"), "w"))


def test_settled_tickers_come_from_captured_settlement_sweeps(tmp_path):
    d = tmp_path / "2026-10-05"
    d.mkdir()
    with gzip.open(d / "x.settlements.jsonl.gz", "wt") as f:
        f.write(json.dumps({"ticker": "KXITFMATCH-26OCT05AB-A", "settlement_ts": "2026-10-05T12:42:07Z"}) + "\n")
    assert RT.captured_settled_tickers(str(tmp_path)) == {"KXITFMATCH-26OCT05AB-A": "2026-10-05T12:42:07Z"}


def test_only_a_fresh_complete_snapshot_is_the_lifecycle_authority(tmp_path):
    now = datetime(2026, 10, 5, 14, 0, tzinfo=timezone.utc)
    _snapshot(str(tmp_path), now, ["A", "B"])
    recs, run, age = RT.latest_open_snapshot(str(tmp_path), now)
    assert set(recs) == {"A", "B"} and age <= RT.SNAPSHOT_MAX_AGE_S
    later = now + timedelta(minutes=40)
    recs, run, age = RT.latest_open_snapshot(str(tmp_path), later)
    assert age > RT.SNAPSHOT_MAX_AGE_S                         # present, but too old to be authoritative


def test_quote_freshness_bands():
    assert RT.quote_freshness(5 * 60) == "FRESH"
    assert RT.quote_freshness(20 * 60) == "AGING"
    assert RT.quote_freshness(31 * 60) == "STALE"
    assert RT.quote_freshness(None) == "UNKNOWN"


def test_slate_overlay_drops_markets_absent_from_a_fresh_snapshot(tmp_path):
    now = datetime(2026, 10, 5, 14, 0, tzinfo=timezone.utc)
    _snapshot(str(tmp_path), now, ["KXATPMATCH-26OCT05AB-A"])
    board = {"KXATPMATCH-26OCT05AB-A": {"ticker": "KXATPMATCH-26OCT05AB-A", "yes_bid_dollars": "0.10"},
             "KXATPMATCH-26OCT05CD-C": {"ticker": "KXATPMATCH-26OCT05CD-C"},           # settled since: absent
             "KXATPFINALS-26-X": {"ticker": "KXATPFINALS-26-X"}}                        # not match scope: kept
    out, meta = overlay_run_snapshot(board, {}, str(tmp_path), now)
    assert set(out) == {"KXATPMATCH-26OCT05AB-A", "KXATPFINALS-26-X"}
    assert out["KXATPMATCH-26OCT05AB-A"]["yes_bid_dollars"] == "0.40" and meta["dropped_not_open_in_run_snapshot"] == 1
    stale_out, meta2 = overlay_run_snapshot(board, {}, str(tmp_path), now + timedelta(hours=1))
    assert stale_out == board and meta2["run_snapshot"] is None


def test_tennis10_separates_quarantined_post_start_rows_from_missing_closes():
    fb = {"strict_truths": 10, "strict_clv_rows": 90}
    g = gate_10_clv_coverage(200, 100, 100, first_ball=fb, n_strict_settled=90, n_quarantined_ab=8)
    assert g.detail["strict_rate"] == 0.9 and g.detail["pregame_eligible"] == 92
    assert g.status == "PASS" and g.detail["strict_rate_pregame_eligible"] == round(90 / 92, 4)
    g2 = gate_10_clv_coverage(200, 100, 100, first_ball=fb, n_strict_settled=80, n_quarantined_ab=8)
    assert g2.status == "FAIL"                                     # threshold unchanged
    assert gate_10_clv_coverage(200, 100, 100, first_ball=fb, n_strict_settled=90).status == "FAIL"


def test_latest_run_files_orders_plain_and_gzip_runs_by_run_id(tmp_path):
    from tennis_edge.health.gates import latest_run_files, settlement_stats
    clv = tmp_path / "clv"
    clv.mkdir()
    (clv / "20261005T061450Z.jsonl").write_text(json.dumps({"prediction_id": "p1", "strict": False}) + "\n")
    with gzip.open(clv / "20261005T200000Z.jsonl.gz", "wt") as f:
        f.write(json.dumps({"prediction_id": "p1", "strict": True, "truth_confidence": "A", "close_ts": "x"}) + "\n")
    assert [os.path.basename(p) for p in latest_run_files(str(clv))][-1] == "20261005T200000Z.jsonl.gz"
    st = tmp_path / "settlements"
    st.mkdir()
    (st / "r.jsonl").write_text(json.dumps({"prediction_id": "p1", "gradeable": True}) + "\n")
    s = settlement_stats(str(tmp_path))
    assert s["settled_strict_clv"] == 1 and s["clv_run"] == "20261005T200000Z.jsonl.gz"
