"""Adversarial tests for first-ball truth, strict pregame labelling and the executable close.

Each test is a way the old scheduled-time logic was quietly wrong. The point is not coverage; it is that
a reader can find the failure mode they are worried about and see it pinned down.
"""
import json
import os
import sys
from datetime import datetime, timedelta, timezone

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tennis_edge.firstball.classify import (AMBIGUOUS, POST_START, START_UNKNOWN, STRICT_PREGAME,
                                            BASIS_NO_PLAY, classify)
from tennis_edge.firstball.horizons import horizon_quotes
from tennis_edge.firstball.mapping import OurMatch, map_all
from tennis_edge.firstball.reconcile import reconcile
from tennis_edge.firstball.sources import REGISTRY, SourceMatch
from tennis_edge.firstball.store import FirstBallStore
from tennis_edge.firstball.truth import (CONTRADICTION_MATERIAL, FirstBallObservation, FirstBallTruth,
                                         DERIVATION_EXPLICIT)
from tennis_edge.ledger.clv import clv_record
from tennis_edge.ledger.close import (BASIS_ACTUAL, BASIS_BRACKET, BASIS_NO_QUOTE, BASIS_NONE,
                                      BASIS_SCHEDULED, Quote, canonical_close)

UTC = timezone.utc
SCHED = datetime(2026, 9, 11, 14, 0, tzinfo=UTC)


def obs(match="m1", source="espn_atp", state="PRE", at=SCHED, **kw):
    kw.setdefault("authority", "secondary")
    kw.setdefault("independence_group", source.split("_")[0])
    return FirstBallObservation(match_id=match, source=source, observed_at_utc=at, state=state, **kw)


def bracketed(lo_min, hi_min, source="espn_atp"):
    """Truth from a PRE->IN transition observed at SCHED+lo_min and SCHED+hi_min."""
    return reconcile("m1", [obs(source=source, state="PRE", at=SCHED + timedelta(minutes=lo_min)),
                            obs(source=source, state="IN", at=SCHED + timedelta(minutes=hi_min))])


def q(minutes, bid=0.60, ask=0.63, source="market_record", **kw):
    return Quote(SCHED + timedelta(minutes=minutes), bid, ask, source=source, **kw)


# ---------------------------------------------------------------- 1-3: the start is not the schedule
def test_1_scheduled_1400_actual_1447():
    t = bracketed(46, 47)
    # 60 s of polling plus the 120 s feed-lag allowance: the uncertainty is carried, not rounded away
    assert t.confidence == "B" and t.bracket_seconds == 180
    # an observation at 14:30, half an hour AFTER the scheduled time, is still genuinely pregame
    assert classify(SCHED + timedelta(minutes=30), t).timing_class == STRICT_PREGAME
    assert classify(SCHED - timedelta(hours=2), t).timing_class == STRICT_PREGAME


def test_2_match_begins_early():
    t = bracketed(-12, -11)
    assert classify(SCHED - timedelta(minutes=20), t).timing_class == STRICT_PREGAME
    # the old rule (captured_at <= scheduled_start) would have called this pregame. It is not.
    assert classify(SCHED - timedelta(minutes=5), t).timing_class == POST_START
    assert classify(SCHED, t).timing_class == POST_START


def test_3_prior_match_delays_start_by_two_hours():
    t = bracketed(119, 120)
    late = SCHED + timedelta(minutes=110)
    assert classify(late, t).timing_class == STRICT_PREGAME
    assert classify(late, t).seconds_before_lower_bound == 7 * 60


def test_4_itf_nominal_falls_after_the_market_closed():
    """The ITF/Challenger pathology: the nominal timestamp is AFTER the close, so it cannot be a start."""
    close_time = SCHED - timedelta(hours=7)
    nominal = SCHED
    assert nominal > close_time
    t = bracketed(-8 * 60 + 5, -8 * 60 + 6)          # play actually began an hour before the close
    quotes = [q(-9 * 60), q(-8 * 60 + 4)]
    cc = canonical_close(quotes, t)
    assert cc.close_basis == BASIS_BRACKET
    # the close is the latest quote that provably precedes the EARLIEST possible first ball, and the
    # nominal time plays no part in choosing it
    assert cc.quote.ts < t.lower_bound_utc
    assert cc.quote.ts == max(x.ts for x in quotes if x.ts < t.lower_bound_utc)


def test_5_observation_between_nominal_and_actual_start_is_strict_pregame():
    t = bracketed(46, 47)
    c = classify(SCHED + timedelta(minutes=20), t)
    assert c.timing_class == STRICT_PREGAME and c.basis == "FIRST_BALL_BRACKET"


def test_6_one_second_after_first_ball_is_post_start():
    t = FirstBallTruth("m1", SCHED, SCHED, SCHED, "A", DERIVATION_EXPLICIT, created_at=SCHED)
    assert classify(SCHED + timedelta(seconds=1), t).timing_class == POST_START


def test_7_no_source_is_start_unknown_not_a_guess():
    assert classify(SCHED, None).timing_class == START_UNKNOWN
    t = reconcile("m1", [])
    assert t.confidence == "UNKNOWN"
    assert classify(SCHED - timedelta(hours=5), t).timing_class == START_UNKNOWN


def test_8_conflicting_sources_fail_closed_as_ambiguous():
    t = reconcile("m1", [obs(source="espn_atp", state="PRE", at=SCHED + timedelta(minutes=10)),
                         obs(source="espn_atp", state="IN", at=SCHED + timedelta(minutes=11)),
                         obs(source="sofascore_live", state="PRE", at=SCHED + timedelta(minutes=50)),
                         obs(source="sofascore_live", state="IN", at=SCHED + timedelta(minutes=51))])
    assert t.contradiction_status == CONTRADICTION_MATERIAL and t.confidence == "UNKNOWN"
    assert t.actual_first_ball_at_utc is None
    assert classify(SCHED, t).timing_class == AMBIGUOUS
    assert not t.strict_eligible
    cc = canonical_close([q(-30)], t)
    assert cc.quote is None and cc.close_basis == BASIS_NONE


def test_9_no_executable_quote_before_the_start_means_no_close():
    t = bracketed(46, 47)
    assert canonical_close([], t).close_basis == BASIS_NO_QUOTE
    # one-sided, crossed and trade-derived prices are not quotes
    assert canonical_close([Quote(SCHED, 0.5, None)], t).close_basis == BASIS_NO_QUOTE
    assert canonical_close([Quote(SCHED, 0.7, 0.6)], t).close_basis == BASIS_NO_QUOTE
    assert canonical_close([Quote(SCHED, 0.5, 0.52, source="trade")], t).close_basis == BASIS_NO_QUOTE


def test_10_quote_exactly_at_the_first_ball_is_not_a_pregame_close():
    t = FirstBallTruth("m1", SCHED, SCHED, SCHED, "A", DERIVATION_EXPLICIT, created_at=SCHED)
    assert canonical_close([q(0)], t).quote is None
    cc = canonical_close([q(-1), q(0)], t)
    assert cc.quote.ts == SCHED - timedelta(minutes=1)


def test_11_delayed_source_updates_widen_the_bracket_they_do_not_sharpen_it():
    """A feed that only refreshes every ten minutes yields a ten-minute bracket, and says so."""
    wide = bracketed(40, 50)
    assert wide.confidence == "C" and wide.bracket_seconds == 720
    assert classify(SCHED + timedelta(minutes=45), wide).timing_class == START_UNKNOWN
    # ... and an observation before the earliest possible start is still not promoted on C evidence
    assert classify(SCHED, wide).timing_class == START_UNKNOWN
    assert classify(SCHED, wide, allow_indirect=True).timing_class == STRICT_PREGAME


def test_12_naive_timestamps_are_never_silently_read_as_local_time():
    from tennis_edge.firstball.sources import _iso_utc, _epoch
    assert _iso_utc("2026-09-11T14:00Z") == SCHED
    assert _iso_utc("2026-09-11T10:00-04:00") == SCHED                  # DST offset respected
    assert _iso_utc("2026-09-11T14:00") == SCHED                        # documented UTC default
    assert _epoch(1789156800) == datetime.fromtimestamp(1789156800, tz=UTC)
    assert _epoch(1789156800000) == datetime.fromtimestamp(1789156800, tz=UTC)
    assert _epoch("not a time") is None and _epoch(12) is None
    for t in (_iso_utc("2026-09-11T14:00"), _epoch(1789156800)):
        assert t.tzinfo is not None


def test_13_doubles_never_maps_onto_a_singles_feed_row():
    feed = [SourceMatch("espn_atp", "1", "Alexander Zverev", "Karen Khachanov", "IN", scheduled_utc=SCHED)]
    ours = [OurMatch("d1", "Zverev / Khachanov", "Sinner / Berrettini", SCHED, doubles=True)]
    mp, _ = map_all(ours, feed)
    assert mp["d1"].status == "UNMATCHED"


def test_14_qualifying_rows_are_kept_and_labelled_not_dropped():
    """A qualifier with no live-score coverage must still get a row, labelled START_UNKNOWN."""
    t = reconcile("q1", [])
    c = classify(SCHED - timedelta(hours=1), t)
    assert c.timing_class == START_UNKNOWN and c.truth_confidence == "UNKNOWN"
    assert c.to_dict()["classifier_version"] >= 1


def test_15_retirement_after_the_first_ball_still_has_a_first_ball():
    t = bracketed(1, 2)
    assert t.strict_eligible and not t.no_play
    assert classify(SCHED - timedelta(minutes=5), t).timing_class == STRICT_PREGAME


def test_16_walkover_means_there_was_never_a_first_ball():
    t = reconcile("m1", [obs(state="PRE", at=SCHED - timedelta(hours=1)),
                         obs(state="NO_PLAY", at=SCHED + timedelta(minutes=5), source_status="Walkover")])
    assert t.no_play and t.confidence == "A" and t.actual_first_ball_at_utc is None
    c = classify(SCHED, t)
    assert c.timing_class == STRICT_PREGAME and c.basis == BASIS_NO_PLAY
    # no ball was struck, so there is no executable pre-first-ball close to compute
    assert canonical_close([q(-30)], t).close_basis == BASIS_NONE


def test_17_market_closing_before_the_first_ball_is_fine_the_close_is_still_valid():
    t = bracketed(46, 47)
    quotes = [q(-120), q(-60)]                       # market went quiet an hour before the scheduled time
    cc = canonical_close(quotes, t)
    assert cc.strict and cc.quote.ts == quotes[-1].ts
    assert cc.seconds_to_first_ball == (t.lower_bound_utc - quotes[-1].ts).total_seconds()


def test_18_post_start_quotes_never_become_the_canonical_close():
    t = bracketed(46, 47)
    quotes = [q(-10, 0.60, 0.63), q(50, 0.90, 0.92), q(70, 0.95, 0.97)]
    cc = canonical_close(quotes, t)
    assert cc.quote.ts == quotes[0].ts and cc.quote.yes_bid == 0.60
    hz = {h.horizon: h for h in horizon_quotes(quotes, t)}
    assert hz["LAST_VALID_PREMATCH"].quote_ts == quotes[0].ts
    for h in hz.values():
        assert h.quote_ts is None or h.quote_ts < t.lower_bound_utc


def test_19_truth_recovered_later_reclassifies_without_touching_history(tmp_path):
    store = FirstBallStore(str(tmp_path))
    o1 = obs(state="IN", at=SCHED + timedelta(minutes=47))
    row = store.add_observation(o1)
    t1 = reconcile("m1", store.observations("m1"), derivation_version=1)
    store.add_truth(t1)
    assert t1.confidence == "C" and classify(SCHED, t1).timing_class == START_UNKNOWN

    # days later a second source supplies the PRE side and the bracket closes
    o2 = obs(source="sofascore_live", state="PRE", at=SCHED + timedelta(minutes=46))
    store.add_observation(o2)
    t2 = reconcile("m1", store.observations("m1"),
                   derivation_version=store.next_derivation_version("m1"))
    store.add_truth(t2)

    assert t2.derivation_version == 2 and t2.confidence == "B"
    assert classify(SCHED, t2).timing_class == STRICT_PREGAME
    assert store.latest_truths()["m1"].derivation_version == 2
    # the ORIGINAL observation row is byte-identical and the chain is intact
    first_line = json.loads(open(os.path.join(str(tmp_path), "observations",
                                              f"{SCHED:%Y-%m-%d}.jsonl")).readline())
    assert first_line == row and first_line["observed_at_utc"] == o1.observed_at_utc.isoformat()
    assert store.verify_chain() == []


def test_20_malformed_and_duplicate_feed_events_do_not_poison_anything():
    ad = REGISTRY["espn_atp"]
    assert ad.parse(None) == [] and ad.parse({}) == [] and ad.parse({"events": None}) == []
    junk = {"events": [{"competitions": [{"competitors": [{"athlete": {}}]}]},
                       {"competitions": [{"status": {}, "competitors": [{"athlete": {"displayName": "A B"}},
                                                                        {"athlete": {"displayName": "C D"}}]}]}]}
    got = ad.parse(junk)
    assert len(got) == 1 and got[0].state == "UNKNOWN"       # unknown status is never optimistically PRE
    # duplicate identical observations must not fabricate a transition
    dup = [obs(state="IN", at=SCHED + timedelta(minutes=47)) for _ in range(5)]
    t = reconcile("m1", dup)
    assert t.lower_bound_utc is None and t.confidence == "C"


# ---------------------------------------------------------------- structural invariants
def test_invariant_close_cannot_be_anchored_to_a_scheduled_time_by_accident():
    """canonical_close takes a truth OBJECT; a datetime cannot be passed in its place."""
    with pytest.raises(AttributeError):
        canonical_close([q(-10)], SCHED)                      # type: ignore[arg-type]
    cc = canonical_close([q(-10)], None, scheduled_start=SCHED, allow_scheduled_fallback=True)
    assert cc.close_basis == BASIS_SCHEDULED and cc.strict is False


def test_invariant_kalshi_close_time_is_not_first_ball():
    """A market close time is exchange truth. It never produces a strict close on its own."""
    kalshi_close = SCHED - timedelta(hours=7)
    cc = canonical_close([q(-8 * 60)], None, scheduled_start=kalshi_close, allow_scheduled_fallback=True)
    assert not cc.strict
    rec = clv_record(prediction_id="p", ticker="T", match_id="m1", family="MATCH_WINNER",
                     entry=q(-9 * 60, 0.5, 0.52), close=cc, truth=None,
                     timing=classify(SCHED - timedelta(hours=9), None))
    assert rec.strict is False and "not first-ball anchored" in rec.exclusion_reason


def test_invariant_post_start_entry_can_never_produce_a_strict_clv_row():
    t = bracketed(46, 47)
    entry = q(48, 0.80, 0.82)                                  # decided AFTER play began
    cc = canonical_close([q(-10)], t)
    rec = clv_record(prediction_id="p", ticker="T", match_id="m1", family="MATCH_WINNER",
                     entry=entry, close=cc, truth=t, timing=classify(entry.ts, t))
    assert rec.timing_class == POST_START and rec.strict is False
    assert rec.clv_executable is not None                      # retained for diagnosis, not discarded


def test_invariant_exchange_evidence_alone_never_reaches_strict_confidence():
    t = reconcile("m1", [obs(source="kalshi", authority="exchange", state="PRE",
                             at=SCHED + timedelta(minutes=46), independence_group="kalshi"),
                         obs(source="kalshi", authority="exchange", state="IN",
                             at=SCHED + timedelta(minutes=47), independence_group="kalshi")])
    assert t.confidence == "C" and not t.strict_eligible


def test_invariant_same_provider_twice_is_one_witness():
    both = reconcile("m1", [obs(source="espn_atp", state="PRE", at=SCHED + timedelta(minutes=40)),
                            obs(source="espn_atp", state="IN", at=SCHED + timedelta(minutes=50)),
                            obs(source="espn_wta", state="PRE", at=SCHED + timedelta(minutes=40)),
                            obs(source="espn_wta", state="IN", at=SCHED + timedelta(minutes=50))])
    assert both.confidence == "C" and both.bracket_seconds == 720


def test_21_same_pair_in_several_rounds_is_broken_by_time_not_refused():
    """A tournament board lists the same pair across a fortnight; a name-only contest ties on all of them."""
    feed = [SourceMatch("espn_atp", "r1", "Alexander Zverev", "Karen Khachanov", "POST",
                        scheduled_utc=SCHED - timedelta(days=5)),
            SourceMatch("espn_atp", "r2", "Alexander Zverev", "Karen Khachanov", "PRE", scheduled_utc=SCHED),
            SourceMatch("espn_atp", "r3", "Alexander Zverev", "Karen Khachanov", "POST",
                        scheduled_utc=SCHED - timedelta(days=12))]
    mp, _ = map_all([OurMatch("m1", "Alexander Zverev", "Karen Khachanov", SCHED)], feed)
    assert mp["m1"].status == "MATCHED" and mp["m1"].source_match_id == "r2"


def test_22_a_genuine_collision_still_fails_closed():
    """Equal names AND equal times is a real collision: nothing is chosen."""
    feed = [SourceMatch("espn_atp", "a", "A B", "C D", "PRE", scheduled_utc=SCHED),
            SourceMatch("espn_atp", "b", "A B", "C D", "PRE", scheduled_utc=SCHED)]
    mp, _ = map_all([OurMatch("m2", "A B", "C D", SCHED)], feed)
    assert mp["m2"].status == "AMBIGUOUS" and "equidistant" in mp["m2"].reason


def test_23_full_name_bindings_are_strong_bare_surnames_are_weak():
    from tennis_edge.firstball.mapping import affinity
    assert affinity("Alexander Zverev", "Alexander Zverev") == 1.0
    assert affinity("Zverev A.", "Alexander Zverev") == 1.0
    assert affinity("Juan Pablo Varillas", "Juan P. Varillas") == 1.0
    assert affinity("Zverev", "Alexander Zverev") == 0.7          # bare surname stays WEAK
    assert affinity("Alexander Zverev", "Mischa Zverev") == 0.0   # wrong person, never a partial match


def test_24_many_kalshi_events_for_one_physical_match_all_bind():
    """Kalshi lists one meeting under several event tickers; they are one match on one court."""
    feed = [SourceMatch("espn_atp", "182768", "Alexander Zverev", "Karen Khachanov", "PRE", scheduled_utc=SCHED)]
    ours = [OurMatch(f"KXATP{fam}-26SEP11ZVEKHA", "Alexander Zverev", "Karen Khachanov", SCHED)
            for fam in ("MATCH", "EXACTMATCH", "SSPREAD", "SETWINNER-2", "SETWINNER-3")]
    mp, _ = map_all(ours, feed)
    assert {m.status for m in mp.values()} == {"MATCHED"}
    assert {m.source_match_id for m in mp.values()} == {"182768"}


def test_25_two_different_physical_matches_claiming_one_row_still_collide():
    feed = [SourceMatch("espn_atp", "1", "A B", "C D", "PRE", scheduled_utc=SCHED)]
    ours = [OurMatch("m1", "A B", "C D", SCHED), OurMatch("m2", "A B", "C D", SCHED + timedelta(days=3))]
    mp, _ = map_all(ours, feed, window_hours=200)
    assert mp["m1"].status == "AMBIGUOUS" and mp["m2"].status == "AMBIGUOUS"
    assert "different physical matches" in mp["m1"].reason


def test_26_espn_doubles_are_parsed_from_the_roster_shape():
    """ESPN shapes a pair as `roster`: a DICT with a combined displayName and an athletes array."""
    ad = REGISTRY["espn_atp"]
    payload = {"events": [{"id": 1, "name": "US Open", "competitions": [{
        "id": "9", "date": "2026-09-11T15:00Z",
        "status": {"type": {"state": "in", "description": "In Progress"}},
        "competitors": [
            {"roster": {"displayName": "Luisa Stefani / Neal Skupski",
                        "athletes": [{"displayName": "Luisa Stefani"}, {"displayName": "Neal Skupski"}]}},
            {"roster": {"athletes": [{"displayName": "Erin Routliffe"}, {"displayName": "Lloyd Glasspool"}]}},
        ]}]}]}
    got = ad.parse(payload)
    assert len(got) == 1
    m = got[0]
    assert m.doubles and m.state == "IN"
    assert m.player_a == "Luisa Stefani / Neal Skupski"
    assert m.player_b == "Erin Routliffe / Lloyd Glasspool"


def test_27_a_doubles_team_binds_to_a_kalshi_style_team_name():
    from tennis_edge.firstball.mapping import affinity
    assert affinity("Luisa Stefani / Neal Skupski", "Stefani/Skupski") >= 0.9
    assert affinity("Luisa Stefani / Neal Skupski", "Erin Routliffe / Lloyd Glasspool") == 0.0


def test_28_a_match_seen_unstarted_past_its_nominal_time_goes_hot():
    """The delayed-match case, which is the whole reason this subsystem exists."""
    from tennis_edge.firstball.watchlist import TIER_COLD, TIER_HOT, TIER_WARM, WatchItem, poll_interval
    overdue = WatchItem("m", "A", "B", False, SCHED - timedelta(hours=2), True, "ATP", "GRAND_SLAM", "US Open", ())
    assert overdue.tier(SCHED) == TIER_WARM                       # schedule alone: five-minute cadence
    assert overdue.tier(SCHED, "PRE") == TIER_HOT                 # seen not started: one-minute cadence
    assert overdue.tier(SCHED, "IN") == TIER_COLD                 # already bracketed, stop hammering
    assert poll_interval([overdue], SCHED, {"m": "PRE"})[0] == 60
    assert poll_interval([overdue], SCHED)[0] == 300
    no_nominal = WatchItem("n", "A", "B", False, None, True, "ATP", "GRAND_SLAM", "US Open", ())
    assert no_nominal.tier(SCHED, "PRE") == TIER_HOT
