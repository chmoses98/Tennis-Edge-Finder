"""Start-time reconciliation, window planning and fail-closed start status (2026-10-02).

Tonight's failure: Kalshi's nominal 06:00Z was a day placeholder for every WTA Beijing match, ESPN's order of
play had them at 03:05Z-05:50Z, and the first-ball watchlist (built from a stale daily discovery snapshot)
never watched them. These tests pin the fix: live evidence outranks the nominal, nothing is presented as
pregame without a live reading, and the refresh is planned off the EARLIEST credible first ball.
"""
import copy
import gzip
import json
import os
import sys
from datetime import datetime, timedelta, timezone

import pytest

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "scripts", "firstball"))

from tennis_edge.assisted import AUTONOMOUS_REAL_MONEY_AUTHORITY
from tennis_edge.assisted import record as R
from tennis_edge.assisted import schema as SC
from tennis_edge.assisted.health import gate_18, schema_problems
from tennis_edge.assisted.market import first_ball_bound, truth_for
from tennis_edge.assisted.slate import build_slate, render_markdown, write_slate
from tennis_edge.firstball import start_times as ST
from tennis_edge.firstball.sources import REGISTRY, SourceMatch
from tennis_edge.firstball.store import FirstBallStore
from tennis_edge.firstball.truth import DERIVATION_EXPLICIT, FirstBallObservation, FirstBallTruth
from tests import test_discrepancy_sanity as DW

UTC = timezone.utc


def T(h, m=0, d=2):
    return datetime(2026, 10, d, h, m, tzinfo=UTC)


def obs(t, state="PRE", *, sched=None, valid=True, source="espn_wta", group="espn", court="", ctx=None, mid="EV"):
    return FirstBallObservation(match_id=mid, source=source, authority="secondary", observed_at_utc=t, state=state,
                                source_match_id="1", source_status={"PRE": "Scheduled", "IN": "In Progress",
                                                                     "POST": "Final"}.get(state, state),
                                source_event_timestamp=sched, source_time_interpretation="iso8601_explicit_utc",
                                independence_group=group, source_time_valid=valid, court=court, court_context=ctx)


def truth(lo, hi, conf="B", **kw):
    return FirstBallTruth("EV", None, lo, hi, conf, DERIVATION_EXPLICIT, created_at=hi or lo, **kw)


def rs(observations=(), *, nominal=T(6), level="WTA", now=T(4), tr=None, placeholder=False):
    return ST.reconcile_start(match_id="EV", nominal=nominal, level_bucket=level, observations=list(observations),
                              truth=tr, now=now, nominal_is_placeholder=placeholder)


# ------------------------------------------------------------------------------------------ 1. live earlier than nominal
def test_live_source_earlier_than_nominal_moves_everything_earlier():
    r = rs([obs(T(3, 50), sched=T(5, 15))], nominal=T(6), now=T(4))
    assert r["current_expected_start"] == T(5, 15).isoformat() and r["start_time_source"] == "LIVE_SCHEDULE:espn_wta"
    assert r["start_time_confidence"] == "HIGH" and r["start_status"] == ST.VERIFIED_UPCOMING and r["bet_allowed"]
    assert r["recommended_handicap_by"] == T(4, 30).isoformat() and r["final_check_time"] == T(5, 5).isoformat()
    assert any(x.startswith("EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_-45_MIN") for x in r["status_reasons"])
    plan = ST.plan_windows([{"match_id": "EV", "label": "A vs B", "level_bucket": "WTA", "discipline": "singles", "start": r}], T(4))
    assert plan["next_window"]["recommended_run_tennis_time"] == T(4, 30).isoformat()       # not 05:15 (= 06:00 - 45)


# ------------------------------------------------------------------------------------------ 2/3/10. started wins
def test_live_source_says_in_progress_while_schedule_is_future():
    r = rs([obs(T(3, 0), sched=T(5)), obs(T(3, 10), "IN", sched=T(3, 5))], nominal=T(6), now=T(3, 20))
    assert r["start_status"] == ST.STARTED and not r["bet_allowed"] and r["first_ball_status"] == "OBSERVED_STARTED"


def test_first_ball_truth_beats_open_market_and_every_schedule():
    # ESPN still shows PRE (feed lag) and a valid later time, Kalshi is open at 06:00 -- the truth says play began
    r = rs([obs(T(5, 20), sched=T(6))], nominal=T(6), now=T(5, 25), tr=truth(T(5, 8), T(5, 10)))
    assert r["start_status"] == ST.STARTED and not r["bet_allowed"]
    assert r["first_ball_status"] == "OBSERVED_STARTED" and "confidence B" in r["first_ball_source"]


# ------------------------------------------------------------------------------------------ 4. disagreement
def test_sources_disagree_fail_closed():
    r = rs([obs(T(5, 0), "IN", sched=T(5)), obs(T(5, 2), "PRE", source="sofascore_live", group="sofascore")],
           now=T(5, 5))
    assert r["start_status"] == ST.STATUS_AMBIGUOUS and not r["bet_allowed"] and r["first_ball_status"] == "SOURCES_DISAGREE"
    t = FirstBallTruth("EV", None, None, None, "UNKNOWN", "x", contradiction_status="MATERIAL", contradiction_detail="disjoint")
    assert rs(now=T(5), tr=t)["start_status"] == ST.STATUS_AMBIGUOUS


# ------------------------------------------------------------------------------------------ 5. no live source
def test_no_live_source_uses_nominal_at_low_confidence_and_blocks_main_tour_bets():
    r = rs([], nominal=T(9), now=T(4))
    assert r["start_status"] == ST.ESTIMATED_UPCOMING and r["start_time_confidence"] == "LOW"
    assert r["start_time_source"] == "KALSHI_NOMINAL" and not r["bet_allowed"]
    assert any(x.startswith("NO_RECENT_LIVE_STATUS") for x in r["status_reasons"])
    ph = rs([], nominal=T(6), now=T(4), placeholder=True)                      # tonight: a day placeholder
    assert ph["start_status"] == ST.START_UNKNOWN and ph["current_expected_start"] is None and not ph["bet_allowed"]
    ch = rs([], nominal=T(9), level="CHALLENGER", now=T(4))                   # no source exists: unchanged treatment
    assert ch["start_status"] == ST.START_UNKNOWN and ch["bet_allowed"] and ch["first_ball_status"] == "NO_FIRST_BALL_SOURCE"
    stale = rs([obs(T(2), sched=T(9))], nominal=T(9), now=T(4))              # a 2 h old reading is not current status
    assert stale["start_status"] == ST.ESTIMATED_UPCOMING and not stale["bet_allowed"]


def test_espn_placeholder_time_is_not_used():
    r = rs([obs(T(3, 50), sched=T(4), valid=False)], nominal=T(6), now=T(3, 55), placeholder=True)
    assert r["current_expected_start"] is None and r["start_status"] == ST.START_UNKNOWN
    assert any(x.startswith("LIVE_TIME_IS_PLACEHOLDER") for x in r["status_reasons"])


# ------------------------------------------------------------------------------------------ 6. court progression
def _sm(mid, state, sched, court="Court 3", period=None, valid=True):
    return SourceMatch(source="espn_wta", source_match_id=mid, player_a=f"P{mid}", player_b=f"Q{mid}", state=state,
                       scheduled_utc=sched, tournament="China Open", time_valid=valid, court=court, period=period, best_of=3)


def test_court_progression_pulls_the_refresh_earlier():
    feed = [_sm("1", "POST", T(3, 5)), _sm("2", "IN", T(4, 10), period=2), _sm("3", "PRE", T(6)),
            _sm("9", "IN", T(4, 10), court="Lotus", period=1)]
    ctx = ST.court_context(feed[2], feed)
    assert ctx["preceding"]["source_match_id"] == "2" and ctx["preceding"]["period"] == 2 and ctx["queue_ahead_pre"] == 0
    r = rs([obs(T(5), sched=T(6), court="Court 3", ctx=ctx)], nominal=T(6), now=T(5, 2))
    assert r["current_expected_start"] == T(5, 15).isoformat() and r["start_time_source"].startswith("COURT_PROGRESSION")
    assert r["start_time_confidence"] == "MEDIUM" and r["start_status"] == ST.START_IMMINENT
    set1 = ST.court_context(feed[2], [_sm("2", "IN", T(4, 10), period=1), feed[2]])      # 04:20 + 35 + 5 = 05:00
    plan = ST.plan_windows([{"match_id": "EV", "label": "x", "level_bucket": "WTA", "discipline": "singles",
                             "start": rs([obs(T(4, 20), sched=T(6), ctx=set1)], nominal=T(6), now=T(4, 25))}], T(4, 25))
    assert plan["next_window"]["earliest_credible_first_ball"] == T(5).isoformat()
    acts = ST.due_actions(plan, T(4, 25), last_slate_built_at=T(1).isoformat(), last_model_run_at=T(3).isoformat())
    assert [a["kind"] for a in acts] == ["slate_primary"]                    # with 06:00 alone nothing would be due
    assert ST.court_estimate(None, T(5)) == (None, "")
    done = ST.court_context(_sm("3", "PRE", T(6)), [_sm("2", "POST", T(4, 10)), _sm("3", "PRE", T(6))])
    assert ST.court_estimate(done, T(5))[0] == T(5, 5)                        # court free: imminent


# ------------------------------------------------------------------------------------------ 7. delay
def test_delayed_match_adapts_without_being_called_started():
    o = [obs(T(4, 30), sched=T(5)), obs(T(5, 25), sched=T(7))]               # ESPN moved it later
    r = rs(o, nominal=T(5), now=T(5, 30))
    assert r["start_status"] == ST.VERIFIED_UPCOMING and r["current_expected_start"] == T(7).isoformat() and r["bet_allowed"]
    plan = ST.plan_windows([{"match_id": "EV", "label": "x", "level_bucket": "WTA", "discipline": "singles", "start": r}], T(5, 30))
    assert plan["next_window"]["earliest_credible_first_ball"] == T(7).isoformat()
    assert ST.due_actions(plan, T(5, 30), last_slate_built_at=T(4).isoformat(), last_model_run_at=T(5).isoformat()) == []


def test_overdue_match_is_ambiguous_unless_seen_pending_just_now():
    assert rs([obs(T(5, 50), sched=T(6))], now=T(6, 5))["start_status"] == ST.STATUS_AMBIGUOUS
    r = rs([obs(T(6, 4), sched=T(6))], now=T(6, 5))
    assert r["start_status"] == ST.START_IMMINENT and r["bet_allowed"]


# ------------------------------------------------------------------------------------------ 8/9. windows
def _entry(mid, st, label=None, level="WTA", disc="singles"):
    return {"match_id": mid, "label": label or mid, "level_bucket": level, "discipline": disc, "start": st}


def test_earliest_credible_start_controls_the_window():
    now = T(3)
    es = [_entry("A", rs([obs(T(2, 55), sched=T(5, 15))], now=now)), _entry("B", rs([obs(T(2, 55), sched=T(5, 40))], now=now)),
          _entry("C", rs([obs(T(2, 55), sched=T(6, 30))], now=now)), _entry("D", rs([obs(T(2, 55), sched=T(9))], now=now)),
          _entry("ITF", rs([], nominal=T(4), level="ITF", now=now), level="ITF"),
          _entry("DBL", rs([obs(T(2, 55), sched=T(4))], now=now), disc="doubles")]
    plan = ST.plan_windows(es, now)
    w = plan["next_window"]
    assert w["earliest_credible_first_ball"] == T(5, 15).isoformat() and w["n_matches"] == 3
    assert w["recommended_run_tennis_time"] == T(4, 30).isoformat() and w["final_status_price_check_time"] == T(5, 5).isoformat()
    assert [m["match_id"] for m in w["matches"]] == ["A", "B", "C"] and plan["windows"][1]["matches"][0]["match_id"] == "D"


def test_live_match_excluded_later_matches_remain():
    now = T(5, 30)
    started = rs([obs(T(5, 0), sched=T(5)), obs(T(5, 20), "IN", sched=T(5))], now=now)
    later = rs([obs(T(5, 28), sched=T(7))], now=now)
    plan = ST.plan_windows([_entry("LIVE", started), _entry("LATER", later)], now)
    assert started["start_status"] == ST.STARTED and later["bet_allowed"]
    assert [m["match_id"] for m in plan["next_window"]["matches"]] == ["LATER"]


# ------------------------------------------------------------------------------------------ dispatch / staleness
def test_due_actions_primary_final_full_run_dedupe_and_cap():
    plan = ST.plan_windows([_entry("A", rs([obs(T(3, 50), sched=T(6))], now=T(4)))], T(4))
    full = ST.due_actions(plan, T(4, 40), last_slate_built_at=T(1).isoformat(), last_model_run_at=T(0, 30).isoformat())
    assert [a["kind"] for a in full] == ["run_tennis"]                        # producer rows 4 h old: full run first
    log = full
    assert ST.due_actions(plan, T(5, 10), last_slate_built_at=T(1).isoformat(), last_model_run_at=T(0, 30).isoformat(),
                          dispatch_log=log) == []                             # the full run will publish the slate
    prim = ST.due_actions(plan, T(5, 10), last_slate_built_at=T(1).isoformat(), last_model_run_at=T(4).isoformat())
    assert [a["kind"] for a in prim] == ["slate_primary"]
    assert ST.due_actions(plan, T(5, 20), last_slate_built_at=T(1).isoformat(), last_model_run_at=T(4).isoformat(),
                          dispatch_log=prim) == []                            # once per window
    fin = ST.due_actions(plan, T(5, 50), last_slate_built_at=T(5, 15).isoformat(), last_model_run_at=T(4).isoformat(), dispatch_log=prim)
    assert [a["kind"] for a in fin] == ["slate_final"]
    assert ST.due_actions(plan, T(6, 1), last_slate_built_at=T(1).isoformat()) == []           # never after first ball
    cap = [{"kind": "run_tennis", "window": f"x{i}", "at": T(0, i).isoformat()} for i in range(ST.DAILY_FULL_RUN_CAP)]
    assert "run_tennis" not in [a["kind"] for a in ST.due_actions(plan, T(4, 40), last_model_run_at=T(0).isoformat(), dispatch_log=cap)]


def test_slate_freshness_flags_a_stale_or_overtaken_slate():
    plan = ST.plan_windows([_entry("EV", rs([obs(T(4, 50), sched=T(5, 15))], now=T(4, 55)))], T(4, 55))
    slate = {"slate_id": "S", "built_at": T(1).isoformat(),
             "matches": [{"event_id": "EV", "start": rs([obs(T(0, 50), sched=T(6))], now=T(1))}]}
    f = ST.slate_freshness(slate, plan, T(4, 55))
    assert f["stale"] and any(r.startswith("PRIMARY_REFRESH_DUE") for r in f["reasons"])
    assert any(c["change"].startswith("EXPECTED_START_MOVED_EARLIER_45") for c in f["changed_matches"])
    assert ST.slate_freshness(None, plan, T(4))["stale"]


# ------------------------------------------------------------------------------------------ 11. determinism
def test_replay_is_deterministic_and_ignores_future_evidence():
    base = [obs(T(3, 50), sched=T(5, 15))]
    a = rs(base, now=T(4))
    assert a == rs(copy.deepcopy(base), now=T(4))
    later = rs(base + [obs(T(4, 30), "IN")], now=T(4))                       # a reading from after `now`
    assert later == a
    plan1 = ST.plan_windows([_entry("EV", a)], T(4))
    assert plan1 == ST.plan_windows([_entry("EV", copy.deepcopy(a))], T(4))


# ------------------------------------------------------------------------------------------ root cause regressions
def test_pregame_only_truth_does_not_mean_started():
    pre_only = FirstBallTruth("KXWTAMATCH-26OCT01AAABBB", None, T(1), None, "C", "STATE_TRANSITION_BRACKET", created_at=T(1))
    assert first_ball_bound(pre_only) is None                                # it said NOT started by 01:00
    played = FirstBallTruth("KXWTASETWINNER-26OCT01AAABBB-1", None, T(3), T(3, 4), "B", "STATE_TRANSITION_BRACKET", created_at=T(3, 5))
    assert first_ball_bound(played) == T(3)
    t = truth_for({pre_only.match_id: pre_only, played.match_id: played}, "KXWTAMATCH-26OCT01AAABBB-AAA")
    assert t is played                                                       # a sibling event that saw play wins


def test_watchlist_includes_markets_listed_after_the_discovery_snapshot(tmp_path):
    from tennis_edge.firstball.watchlist import build_watchlist
    disc = tmp_path / "disc" / "markets"
    disc.mkdir(parents=True)
    json.dump({"open": {"markets": []}}, open(disc / "KXWTAMATCH.json", "w"))           # stale: lists nothing
    cap = tmp_path / "capture" / "2026-10-02"
    cap.mkdir(parents=True)
    rows = [DW._mw("KXWTAMATCH-26OCT02AAABBB-AAA", "Alpha Aaa", 0.4, 0.42, T(1)),
            DW._mw("KXWTAMATCH-26OCT02AAABBB-BBB", "Beta Bbb", 0.58, 0.6, T(1))]
    for r in rows:
        r.update(event_ticker="KXWTAMATCH-26OCT02AAABBB", occurrence_datetime="2026-10-02T06:00:00Z",
                 rules_primary=r["rules_primary"].replace("ATP Tokyo", "WTA Beijing"))
    with gzip.open(cap / "20261002T010000Z.quotes.jsonl.gz", "wt") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    items, diag = build_watchlist(str(tmp_path / "disc"), now=T(1, 30), capture_root=str(tmp_path / "capture"))
    assert [i.match_id for i in items] == ["KXWTAMATCH-26OCT02AAABBB"] and diag["events_only_on_capture_board"] == 1
    assert (items[0].player_a, items[0].player_b) == ("Alpha Aaa", "Beta Bbb")
    assert build_watchlist(str(tmp_path / "disc"), now=T(0, 30), capture_root=str(tmp_path / "capture"))[0] == []  # replay-safe


def test_espn_adapter_reads_time_valid_court_and_set():
    comp = {"id": "184", "date": "2026-10-02T03:05Z", "timeValid": True, "venue": {"court": "Court 3"},
            "status": {"period": 2, "type": {"state": "in", "description": "In Progress"}},
            "format": {"regulation": {"periods": 3}},
            "competitors": [{"athlete": {"displayName": "Peyton Stearns"}, "linescores": [{"value": 4}, {"value": 2}]},
                            {"athlete": {"displayName": "Viktorija Golubic"}, "linescores": [{"value": 6}, {"value": 1}]}]}
    placeholder = {**comp, "id": "185", "date": "2026-10-04T04:00Z", "timeValid": False, "venue": {"court": ""},
                   "status": {"period": 1, "type": {"state": "pre", "description": "Scheduled"}}}
    got = REGISTRY["espn_wta"].parse({"events": [{"name": "China Open", "groupings": [{"competitions": [comp, placeholder]}]}]})
    a, b = got
    assert (a.state, a.time_valid, a.court, a.period, a.best_of, a.scheduled_utc) == ("IN", True, "Court 3", 2, 3, T(3, 5))
    assert (b.state, b.time_valid, b.court) == ("PRE", False, "")


# ------------------------------------------------------------------------------------------ slate + recorder (worlds)
def _add(w, *o):
    fb = FirstBallStore(os.path.join(w["data"], "firstball", "store"))
    for x in o:
        fb.add_observation(x)
    return fb


def _rebuild(w, now=DW.T_SLATE):
    s = build_slate(w["data"], now=now)
    write_slate(s, w["slate_dir"])
    w["slate"] = s
    return s


def test_slate_shows_start_status_and_next_window(tmp_path):
    w = DW.make_world(tmp_path)
    x = w["slate"]["matches"][0]
    st = x["start"]
    assert st["start_status"] == ST.VERIFIED_UPCOMING and st["current_expected_start"] == "2026-10-01T10:00:00+00:00"
    assert st["start_time_source"] == "LIVE_SCHEDULE:espn_atp" and st["bet_allowed"]
    nw = w["slate"]["next_actionable_window"]
    assert nw["earliest_credible_first_ball"] == "2026-10-01T10:00:00+00:00" and nw["recommended_run_tennis_time"] == "2026-10-01T09:15:00+00:00"
    md = render_markdown(w["slate"])
    for s in ("NEXT ACTIONABLE MAIN-TOUR WINDOW", "Earliest credible first ball: **2026-10-01 10:00Z**",
              "Recommended RUN TENNIS time: **2026-10-01 09:15Z**", "Final price/status check time: **2026-10-01 09:50Z**",
              "**START STATUS: VERIFIED_UPCOMING**", "* Nominal schedule: 2026-10-01 10:00Z",
              "* Current expected start: 2026-10-01 10:00Z", "* Recommended handicap-by time: 2026-10-01 09:15Z"):
        assert s in md, s


def test_slate_drops_started_and_flags_ambiguous(tmp_path):
    w = DW.make_world(tmp_path)
    _add(w, obs(datetime(2026, 10, 1, 8, 3, tzinfo=UTC), "IN", source="espn_atp", mid=DW.EV))
    s = _rebuild(w)
    assert s["matches"] == [] and s["counts"]["skipped_matches"]["first_ball_already_observed"] == 1
    w2 = DW.make_world(tmp_path / "b")
    _add(w2, obs(datetime(2026, 10, 1, 8, 1, tzinfo=UTC), "IN", source="espn_atp", mid=DW.EV),
         obs(datetime(2026, 10, 1, 8, 2, tzinfo=UTC), "PRE", source="sofascore_live", group="sofascore", mid=DW.EV))
    s2 = _rebuild(w2)
    x = s2["matches"][0]
    assert x["start_status"] == ST.STATUS_AMBIGUOUS and not x["start"]["bet_allowed"]
    assert x["warnings"][0].startswith("BET_BLOCKED_START_STATUS: STATUS_AMBIGUOUS")
    assert "BET BLOCKED" in render_markdown(s2)


def test_recorder_blocks_bets_when_start_is_not_verified(tmp_path):
    w = DW.make_world(tmp_path)
    kw = {"store_root": w["store"], "data_root": w["data"], "slate_dir": w["slate_dir"], "now": DW.T_DEC}
    ok = R.record_decision(DW._bet(), **kw)
    assert ok["schema_version"] == 3 and ok["start_status_at_decision"] == ST.VERIFIED_UPCOMING
    assert ok["current_expected_start_at_decision"] == "2026-10-01T10:00:00+00:00"
    # ESPN says in progress, Kalshi still open with a 10:00 nominal: refused outright
    w2 = DW.make_world(tmp_path / "in")
    _add(w2, obs(datetime(2026, 10, 1, 8, 5, tzinfo=UTC), "IN", source="espn_atp", mid=DW.EV))
    kw2 = {**kw, "store_root": w2["store"], "data_root": w2["data"], "slate_dir": w2["slate_dir"]}
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(DW._bet(), **kw2)
    assert e.value.code == "POST_START_DECISION"
    # first-ball truth recorded later says play began 08:00-08:03: still refused at 08:08
    w3 = DW.make_world(tmp_path / "truth")
    _add(w3).add_truth(FirstBallTruth(DW.EV, None, datetime(2026, 10, 1, 8, 0, tzinfo=UTC), datetime(2026, 10, 1, 8, 3, tzinfo=UTC),
                                      "B", DERIVATION_EXPLICIT, created_at=datetime(2026, 10, 1, 8, 4, tzinfo=UTC)))
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(DW._bet(), **{**kw, "store_root": w3["store"], "data_root": w3["data"], "slate_dir": w3["slate_dir"]})
    assert e.value.code == "POST_START_DECISION"
    # sources disagree: BET refused, PASS recorded with the status
    w4 = DW.make_world(tmp_path / "amb")
    _add(w4, obs(datetime(2026, 10, 1, 8, 1, tzinfo=UTC), "IN", source="espn_atp", mid=DW.EV),
         obs(datetime(2026, 10, 1, 8, 2, tzinfo=UTC), "PRE", source="sofascore_live", group="sofascore", mid=DW.EV))
    kw4 = {**kw, "store_root": w4["store"], "data_root": w4["data"], "slate_dir": w4["slate_dir"]}
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(DW._bet(), **kw4)
    assert e.value.code == "START_STATUS_NOT_VERIFIED"
    p = R.build_decision({"ticker": DW.MW_A, "decision": "PASS", "pass_reason_if_pass": "status unclear"}, **kw4)
    assert p["start_status_at_decision"] == ST.STATUS_AMBIGUOUS


def test_recorder_needs_a_recent_live_reading_for_main_tour(tmp_path):
    w = DW.make_world(tmp_path)
    obs_dir = os.path.join(w["data"], "firstball", "store", "observations")
    for fn in os.listdir(obs_dir):
        os.remove(os.path.join(obs_dir, fn))                                  # nobody watched this match
    kw = {"store_root": w["store"], "data_root": w["data"], "slate_dir": w["slate_dir"], "now": DW.T_DEC}
    with pytest.raises(SC.AssistedValidationError) as e:
        R.build_decision(DW._bet(), **kw)
    assert e.value.code == "START_STATUS_NOT_VERIFIED" and "NO_RECENT_LIVE_STATUS" in str(e.value)
    w_ok = R.build_decision({"ticker": DW.MW_A, "decision": "WATCH", "side": "YES", "chatgpt_fair_probability": 0.55,
                             "chatgpt_thesis": "watch until live status"}, **kw)
    assert w_ok["decision"] == "WATCH"


# ------------------------------------------------------------------------------------------ 12-15. compatibility, safety
def test_old_records_and_old_observations_stay_readable(tmp_path):
    full = {k: None for k in SC.DECISION_FIELDS}
    base = {**full, "decision_id": "AD-20261001-0123456789ab", "decision": "PASS", "ticker": DW.MW_A,
            "chosen_expression": "MATCH_WINNER", "model_agreement_state": "MODEL_AND_CHATGPT_BOTH_PASS",
            "factor_tags": [], "automated_execution": False, "autonomous_real_money_authority": "OFF"}
    for v in (1, 2, 3):
        rec = {k: base[k] for k in SC.DECISION_FIELDS_BY_VERSION[v]}
        rec["schema_version"] = v
        assert schema_problems(rec) == [], v
    fb = FirstBallStore(str(tmp_path))
    old = obs(T(1)).to_dict()
    for k in ("source_time_valid", "court", "court_context"):
        old.pop(k)
    os.makedirs(fb.obs_dir, exist_ok=True)
    with open(os.path.join(fb.obs_dir, "2026-10-02.jsonl"), "w") as f:
        f.write(json.dumps({**old, "prev_hash": "GENESIS", "row_hash": "x"}) + "\n")
    o = fb.observations()[0]
    assert o.source_time_valid is None and o.court == "" and o.court_context is None


def test_itf_and_doubles_safety_unchanged(tmp_path):
    r = rs([], nominal=T(9), level="ITF", now=T(4))
    assert r["start_status"] == ST.START_UNKNOWN and r["bet_allowed"]            # no source exists: as before
    from tests import test_post_settlement_and_doubles as PD
    w = PD._doubles_world(tmp_path)
    x, row = PD._drow(w)
    assert row["model_probability_yes"] is None and row["model_validity"]["gen1"] == "UNVALIDATED_DO_NOT_USE"
    assert x["start"]["start_status"] in ST.START_STATUSES


def test_no_model_probability_changes_with_start_evidence(tmp_path):
    w = DW.make_world(tmp_path)
    before = [(r["ticker"], r["model"], r["model_probability_yes"]) for x in w["slate"]["matches"] for r in x["markets"]]
    obs_dir = os.path.join(w["data"], "firstball", "store", "observations")
    for fn in os.listdir(obs_dir):
        os.remove(os.path.join(obs_dir, fn))
    s = _rebuild(w)
    after = [(r["ticker"], r["model"], r["model_probability_yes"]) for x in s["matches"] for r in x["markets"]]
    assert before == after


def test_no_staking_or_authority_change():
    assert AUTONOMOUS_REAL_MONEY_AUTHORITY == "OFF" and R.MAX_STAKE_UNITS == 10.0
    import plan_windows as PW
    assert set(PW.WORKFLOWS.values()) == {"tennis-run.yml", "tennis-assisted-slate.yml"}
    for rel in ("tennis_edge/firstball/start_times.py", "tennis_edge/firstball/start_evidence.py", "scripts/firstball/plan_windows.py"):
        src = open(os.path.join(REPO, rel)).read()
        for forbidden in ("place_order", "create_order", "auth_adapter", "tennis_edge.models", "edge_candidates"):
            assert forbidden not in src, (rel, forbidden)


# ------------------------------------------------------------------------------------------ planner script + TENNIS-18
def test_planner_script_and_tennis_18(tmp_path):
    import plan_windows as PW
    w = DW.make_world(tmp_path)
    store = os.path.join(w["data"], "firstball", "store")
    cap = os.path.join(w["data"], "kalshi", "capture")
    assert PW.main(["--store", store, "--capture", cap, "--slates", w["slate_dir"], "--now", "2026-10-01T09:10:00+00:00"]) == 0
    plan = json.load(open(os.path.join(store, "schedule", "plan_latest.json")))
    assert plan["next_window"]["earliest_credible_first_ball"] == "2026-10-01T10:00:00+00:00"
    assert [a["kind"] for a in plan["actions_this_pass"]] == ["slate_primary"] and plan["actions_this_pass"][0]["dispatched"] is False
    assert "NEXT ACTIONABLE MAIN-TOUR WINDOW" in open(os.path.join(store, "schedule", "NEXT_WINDOW.md")).read()
    status, d = gate_18(w["research"], firstball_root=store, now=datetime(2026, 10, 1, 9, 15, tzinfo=UTC))
    assert status == "PASS" and d["next_window_first_ball"] == "2026-10-01T10:00:00+00:00"
    status, d = gate_18(w["research"], firstball_root=store, now=datetime(2026, 10, 1, 10, 30, tzinfo=UTC))
    assert status == "FAIL" and {"PLAN_STALE", "WINDOW_MISSED"} <= set(d["failing"])    # slate built 08:05 only
    assert gate_18(w["research"], firstball_root=str(tmp_path / "none"))[0] == "UNKNOWN"
