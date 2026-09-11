"""Quote timelines out of captured evidence, and what settlement is allowed to do with them.

The old version of this test pinned the behaviour this wave exists to remove: a close cut off at
`scheduled_start - margin`. It now pins the replacement: candles become quotes, malformed records are
skipped rather than poisoning the timeline, and no close is produced at all without first-ball truth.
"""
import gzip
import json
import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tennis_edge.firstball.truth import FirstBallTruth, DERIVATION_EXPLICIT
from tennis_edge.ledger.close import BASIS_ACTUAL, BASIS_NONE, canonical_close
from tennis_edge.ledger.quotes import quotes_from_capture

T0 = datetime(2026, 9, 10, 12, 0, tzinfo=timezone.utc)


def _write_capture(root, ticker="KXATPMATCH-26SEP10AB-A"):
    day = os.path.join(root, "2026-09-10")
    os.makedirs(day, exist_ok=True)
    ts = int(T0.timestamp())
    rec = {"ticker": ticker, "candles_60": [
        {"end_period_ts": ts - 10 * 3600, "yes_bid": {"close_dollars": "0.40"}, "yes_ask": {"close_dollars": "0.44"}},
        {"end_period_ts": ts - 8 * 3600, "yes_bid": {"close_dollars": "0.45"}, "yes_ask": {"close_dollars": "0.47"}},
        {"end_period_ts": ts - 2 * 3600, "yes_bid": {"close_dollars": "0.90"}, "yes_ask": {"close_dollars": "0.92"}},
        {"bad": True}, "not-a-dict"]}
    with gzip.open(os.path.join(day, "20260910T120000Z.candles.jsonl.gz"), "wt") as f:
        f.write(json.dumps(rec) + "\n")
        f.write("{ this line is truncated garbage\n")
    with gzip.open(os.path.join(day, "20260910T120000Z.quotes.jsonl.gz"), "wt") as f:
        f.write(json.dumps({"ticker": ticker, "captured_at": (T0 - timedelta(hours=9)).isoformat(),
                            "yes_bid_dollars": "0.42", "yes_ask_dollars": "0.45",
                            "no_bid_dollars": "0.55", "no_ask_dollars": "0.58"}) + "\n")
    return ticker


def test_candles_and_market_records_become_one_executable_timeline(tmp_path):
    root = str(tmp_path / "capture")
    ticker = _write_capture(root)
    qs = quotes_from_capture(root, {ticker})[ticker]
    assert [q.source for q in qs].count("candle_bidask") == 3
    assert [q.source for q in qs].count("market_record") == 1
    assert all(q.executable for q in qs)
    assert qs == sorted(qs, key=lambda q: q.ts)              # chronological
    assert qs[0].spread is not None and qs[-1].mid is not None


def test_in_play_candle_is_excluded_by_first_ball_truth(tmp_path):
    root = str(tmp_path / "capture")
    ticker = _write_capture(root)
    qs = quotes_from_capture(root, {ticker})[ticker]
    first_ball = T0 - timedelta(hours=3)
    truth = FirstBallTruth("m", first_ball, first_ball, first_ball, "A", DERIVATION_EXPLICIT, created_at=T0)
    cc = canonical_close(qs, truth)
    assert cc.close_basis == BASIS_ACTUAL and cc.strict
    assert cc.quote.yes_bid == 0.45                          # the in-play 0.90 quote is never the close
    assert cc.quote.ts < first_ball


def test_without_first_ball_truth_there_is_no_close_at_all(tmp_path):
    root = str(tmp_path / "capture")
    ticker = _write_capture(root)
    qs = quotes_from_capture(root, {ticker})[ticker]
    cc = canonical_close(qs, None)
    assert cc.quote is None and cc.close_basis == BASIS_NONE and not cc.strict
