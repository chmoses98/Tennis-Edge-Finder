"""Operational fixes from the prospective-evidence audit: Laver Cup taxonomy, trade-tape pagination,
TENNIS-6 semantics, the settlement layer the health gates read, and the pregame guard."""
import json
import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tennis_edge.health import gates as G
from tennis_edge.kalshi.families import FAMILIES, SERIES, unknown_series
from tennis_edge.kalshi.markets import parse_market
from tennis_edge.kalshi.trade_tape import TradeTape, scan


# ------------------------------------------------------------------------------------------ Laver Cup
def _laver(ticker, who, a, b, doubles=False):
    comp = "Laver Cup Doubles 2026 Laver Cup, Double Matches" if doubles else "Laver Cup Singles 2026 Laver Cup,Singles Matches"
    return {"ticker": ticker, "event_ticker": ticker.rsplit("-", 1)[0],
            "custom_strike": {"tennis_doubles_competitor" if doubles else "tennis_competitor": "u"},
            "rules_primary": f"If {who} wins the {a} vs {b} professional tennis match in the 2026 {comp} after a "
                             "ball has been played, then the market resolves to Yes."}


def test_laver_cup_series_are_known_and_explicit():
    assert unknown_series(["KXLAVERCUPMATCH", "KXLAVERCUPDOUBLESMATCH", "KXLAVERCUP"]) == []
    assert SERIES["KXLAVERCUPMATCH"] == ("TEAM_EVENT_MATCH_WINNER", "ATP", "TEAM", "singles")
    assert SERIES["KXLAVERCUPDOUBLESMATCH"] == ("TEAM_EVENT_MATCH_WINNER", "ATP", "TEAM", "doubles")
    assert FAMILIES["TEAM_EVENT_MATCH_WINNER"]["projectable"] is False     # format is not guessed


def test_laver_cup_markets_parse_semantics_but_are_never_priced():
    s = parse_market(_laver("KXLAVERCUPMATCH-26SEP27JODFRI-JOD", "Rafael Jodar", "Jodar", "Fritz"))
    assert s.status == "UNSUPPORTED_FAMILY" and s.family == "TEAM_EVENT_MATCH_WINNER"
    assert s.discipline == "singles" and s.subject == "Rafael Jodar" and s.subject_is_a is True
    assert s.player_a == "Jodar" and s.player_b == "Fritz" and "Laver Cup" in s.competition
    d = parse_market(_laver("KXLAVERCUPDOUBLESMATCH-26SEP27COBMENDEFRI-DEFRI", "Alex de Minaur / Taylor Fritz",
                            "Cobolli / Mensik", "de Minaur / Fritz", doubles=True))
    assert d.status == "UNSUPPORTED_FAMILY" and d.discipline == "doubles" and d.subject_is_a is False
    # unrecognisable rules text still fails loudly rather than being waved through
    bad = parse_market({"ticker": "KXLAVERCUPMATCH-X-Y", "rules_primary": "Something else entirely."})
    assert bad.status == "UNPARSED"


# ------------------------------------------------------------------------------------------ trade tape
class FakeTape:
    """A global tape of one trade per second, served newest-first in pages of `per_page`."""

    def __init__(self, per_page=10, fail=False):
        self.per_page, self.fail, self.calls = per_page, fail, []

    def trades(self, min_ts, max_ts, limit, max_pages):
        self.calls.append((min_ts, max_ts, max_pages))
        if self.fail:
            return [], False, {"pages": 0, "error": "HTTP 500"}
        ts = list(range(max_ts, min_ts - 1, -1))
        cap = self.per_page * max_pages
        got = ts[:cap]
        pages = min(max_pages, -(-len(got) // self.per_page) if got else 1)
        complete = len(ts) <= cap
        return ([{"created_time": t, "trade_id": str(t)} for t in got], complete,
                {"pages": pages, "error": None, "truncated_by_max_pages": not complete})


def _p(x):
    return int(x) if x is not None else None


def test_truncated_window_queues_the_older_remainder_and_never_rescans():
    tape, api = TradeTape(cursor_ts=1000), FakeTape(per_page=10)
    trades, rep = scan(api, tape, 1300, page_budget=10, new_window_pages=10, parse=_p)
    assert rep["new_window"]["complete"] is False and rep["pages"] <= 10
    assert tape.cursor_ts == 1300                         # the next NEW window starts where this one ended
    assert tape.backlog == [[1000, 1201]]                 # the unread older end is queued, boundary included
    trades2, rep2 = scan(api, tape, 1310, page_budget=40, new_window_pages=10, parse=_p)
    assert api.calls[-2][:2] == (1300, 1310)              # no re-scan of 1201..1300
    assert rep2["pages"] <= 40
    got = {t["created_time"] for t in trades + trades2}
    assert set(range(1201, 1301)) <= got


def test_backlog_drains_and_budget_bounds_runtime():
    tape, api = TradeTape(cursor_ts=0), FakeTape(per_page=10)
    scan(api, tape, 500, page_budget=5, new_window_pages=5, parse=_p)
    assert tape.backlog
    for k in range(20):
        _t, rep = scan(api, tape, 500 + k, page_budget=12, new_window_pages=2, parse=_p)
        assert rep["pages"] <= 12
    assert tape.backlog == [] and tape.pending_seconds() == 0


def test_old_gaps_are_abandoned_explicitly_not_silently():
    tape = TradeTape(cursor_ts=100_000, backlog=[[10, 20], [99_000, 99_100]])
    api = FakeTape(per_page=1000)
    _t, rep = scan(api, tape, 100_010, page_budget=5, new_window_pages=1, max_gap_age_s=5000, parse=_p)
    assert rep["abandoned"] == [[10, 20]]


def test_fetch_error_is_incomplete_and_queues_the_window():
    tape = TradeTape(cursor_ts=100)
    _t, rep = scan(FakeTape(fail=True), tape, 200, parse=_p)
    assert rep["errors"] and tape.backlog == [[100, 200]]


def test_legacy_state_is_read_and_written_back():
    tape = TradeTape.from_state({"trades_cursor_ts": 1234})
    assert tape.cursor_ts == 1234 and tape.backlog == []
    tape.backlog = [[1, 2]]
    st = tape.to_state({})
    assert st["trades_backlog"] == [[1, 2]] and st["trades_cursor_ts"] == st["trades_tape_cursor_ts"] == 1234


# ------------------------------------------------------------------------------------------ TENNIS-6
def test_tennis6_separates_true_post_start_from_start_unknown():
    t0 = datetime(2026, 9, 12, 10, 0, tzinfo=timezone.utc)
    rows = [{"prediction_id": "post", "match_id": "m1", "generated_at_utc": (t0 + timedelta(hours=1)).isoformat()},
            {"prediction_id": "brk", "match_id": "m2", "generated_at_utc": (t0 + timedelta(minutes=1)).isoformat()},
            {"prediction_id": "unk", "match_id": "m3", "generated_at_utc": (t0 - timedelta(hours=3)).isoformat()},
            {"prediction_id": "late", "match_id": "m4", "generated_at_utc": (t0 - timedelta(minutes=2)).isoformat()}]
    starts = {"m1": (t0, t0 + timedelta(hours=2), t0 + timedelta(minutes=3)),
              "m2": (t0, t0 + timedelta(hours=2), t0 + timedelta(minutes=3)),
              "m3": (None, t0), "m4": (None, t0)}
    r = G.gate_6_no_post_start_leakage(rows, starts, strict_research_rows=[
        {"strict": True, "timing_class": "STRICT_PREGAME"}, {"strict": False, "timing_class": "POST_START"}])
    assert r.status == "FAIL"                              # the fail-closed rule is unchanged
    assert r.detail["violation_classes"] == {"post_start_confirmed": 1, "inside_first_ball_bracket": 1,
                                             "schedule_fallback": 1, "no_start_information": 0}
    assert r.detail["n_violations"] == 3 and r.detail["start_unknown_passed_schedule_check"] == 1
    assert r.detail["post_start_rows_in_strict_research"] == 0
    # a post-start row USED as strict evidence is a leak on its own, even with a clean ledger
    leak = G.gate_6_no_post_start_leakage(rows[2:3], {"m3": (None, t0)},
                                          strict_research_rows=[{"strict": True, "timing_class": "POST_START"}])
    assert leak.status == "FAIL" and leak.detail["post_start_rows_in_strict_research"] == 1


# ------------------------------------------------------------------------------------------ settlement layer
def test_settlement_stats_read_the_settle_tables(tmp_path):
    (tmp_path / "settlements").mkdir(); (tmp_path / "clv").mkdir()
    rows = [{"prediction_id": "a", "gradeable": True, "sports": {"source": "kalshi_result", "confidence": 0.9}},
            {"prediction_id": "b", "gradeable": True, "sports": {"source": "espn", "confidence": 0.95}},
            {"prediction_id": "c", "gradeable": False, "sports": None},
            {"prediction_id": "a", "gradeable": True, "sports": None}]
    open(tmp_path / "settlements" / "1.jsonl", "w").write("\n".join(json.dumps(r) for r in rows) + "\n")
    clv = [{"prediction_id": "a", "truth_confidence": "B", "close_ts": "x", "strict": True, "timing_class": "STRICT_PREGAME"},
           {"prediction_id": "b", "truth_confidence": "C", "close_ts": None, "strict": False, "timing_class": "START_UNKNOWN"}]
    open(tmp_path / "clv" / "2.jsonl", "w").write("\n".join(json.dumps(r) for r in clv) + "\n")
    st = G.settlement_stats(str(tmp_path))
    assert st["settled"] == 3 and st["settled_binary"] == 2 and st["settled_scalar"] == 1
    assert st["sports_truth_kalshi_derived"] == 1 and st["sports_truth_independent"] == 1
    assert st["settled_with_ab_truth"] == 1 and st["settled_strict_clv"] == 1
    g8, g9 = G.gate_8_9_truth(st["sports_truth_independent"], st["settled_binary"], None, [],
                              first_ball={"strict_truths": 1}, settlement=st)
    assert g8.status == "FAIL" and g8.detail["total"] == 2        # Kalshi-derived sports truth is not counted
    assert g9.status == "UNKNOWN" and "independent" in g9.detail["reason"]
    g10 = G.gate_10_clv_coverage(3, 1, 1, first_ball={"strict_truths": 1, "strict_clv_rows": 99}, n_strict_settled=1)
    assert g10.status == "PASS" and g10.detail["strict_rate"] == 1.0
    assert G.settlement_stats(str(tmp_path / "nothing")) is None


def test_gate5_backlog_semantics(tmp_path, monkeypatch):
    now = datetime(2026, 9, 27, 12, 0, tzinfo=timezone.utc)
    cap = tmp_path / "data" / "kalshi" / "capture" / "2026-09-27"; cap.mkdir(parents=True)
    monkeypatch.setattr(G, "PROJ", str(tmp_path))
    man = {"run_id": "r", "finished_at": (now - timedelta(minutes=5)).isoformat(), "incomplete": [],
           "trades": {"backlog": {"gaps": 1, "pending_seconds": 60, "oldest_gap_age_s": 600}}}
    json.dump(man, open(cap / "r.manifest.json", "w"))
    assert G.gate_5_capture_freshness(now=now).status == "PASS"
    man["trades"]["backlog"]["oldest_gap_age_s"] = 3 * 3600
    json.dump(man, open(cap / "r.manifest.json", "w"))
    assert G.gate_5_capture_freshness(now=now).status == "FAIL"
    man["trades"]["backlog"]["oldest_gap_age_s"] = 60
    man["incomplete"] = [{"stage": "trades_gap_abandoned"}]
    json.dump(man, open(cap / "r.manifest.json", "w"))
    assert G.gate_5_capture_freshness(now=now).status == "FAIL"


# ------------------------------------------------------------------------------------------ pregame guard
def test_run_tennis_refuses_matches_the_first_ball_store_has_seen_start(tmp_path):
    from scripts.run_tennis import matches_already_started, _match_code
    from tennis_edge.firstball.store import FirstBallStore
    from tennis_edge.firstball.truth import FirstBallTruth, DERIVATION_SCORE_BACKCAST, DERIVATION_NO_PLAY
    now = datetime(2026, 9, 12, 12, 0, tzinfo=timezone.utc)
    st = FirstBallStore(str(tmp_path))
    st.add_truth(FirstBallTruth("KXWTACHALLENGERMATCH-26SEP12DENBUR", None, None, now - timedelta(hours=1), "C",
                                DERIVATION_SCORE_BACKCAST, created_at=now))
    st.add_truth(FirstBallTruth("KXATPMATCH-26SEP12NOPLAY", None, None, None, "A", DERIVATION_NO_PLAY,
                                no_play=True, created_at=now))
    # seen "Scheduled" (lower bound only: NOT started when last polled) -- the 2026-10-05 false refusals
    st.add_truth(FirstBallTruth("KXATPMATCH-26SEP13SCHEDL", None, now - timedelta(hours=3), None, "C",
                                DERIVATION_SCORE_BACKCAST, created_at=now))
    # bracketed: last seen not started, then seen under way
    st.add_truth(FirstBallTruth("KXATPMATCH-26SEP12BRACKT", None, now - timedelta(hours=2), now - timedelta(minutes=90), "B",
                                DERIVATION_SCORE_BACKCAST, created_at=now))
    started = matches_already_started(str(tmp_path), now)
    assert _match_code("KXWTASETWINNER-26SEP12DENBUR-2") in started       # every series of the same match
    assert "26SEP12NOPLAY" not in started
    assert "26SEP13SCHEDL" not in started and "26SEP12BRACKT" in started
    assert matches_already_started(str(tmp_path / "missing"), now) == set()
