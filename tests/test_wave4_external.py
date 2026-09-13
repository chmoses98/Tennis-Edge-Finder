"""Wave 4: an independent market as the witness against Kalshi.

The failure modes these guard against are all quiet ones: a margin mistaken for an edge, an invented
opposite side, a stale line averaged into a live consensus, two names for one book counted as two
witnesses, a first-set price compared against a match contract, and our own model promoted from witness
to plaintiff after Wave 3 established it cannot carry that role.
"""
from __future__ import annotations

import json
import os
import tempfile
from datetime import datetime, timedelta, timezone

import pytest

from tennis_edge.external_market.bovada import FAMILY_MAP, MATCH_PERIODS, parse_coupon
from tennis_edge.external_market.consensus import Reference, build_reference, group_of
from tennis_edge.external_market.devig import (american_to_decimal, decimal_to_american, devig_all,
                                               devig_power, devig_proportional, devig_shin, implied,
                                               overround)
from tennis_edge.external_market.dislocation import (ALL_THREE_DISAGREE, Dislocation,
                                                     DislocationLedger, EXTERNAL_LONE_OUTLIER,
                                                     KALSHI_LONE_OUTLIER, MARKETS_AGREE,
                                                     MODEL_LONE_OUTLIER, triangulate)
from tennis_edge.external_market.mapping import (AMBIGUOUS_PLAYER, DOUBLES_UNSUPPORTED, MAPPED,
                                                 UNMAPPED_PLAYER, audit, join_to_kalshi, map_event)
from tennis_edge.external_market.schema import (EXCHANGE, ExternalMarketError,
                                                ExternalMarketObservation, ExternalStore, SPORTSBOOK)
from tennis_edge.pricing.fees import FeeSchedule, taker_fee

NOW = "2026-09-12T12:00:00+00:00"


def _obs(**kw):
    base = dict(source="bovada", source_kind=SPORTSBOOK, source_event_id="e1", observed_at=NOW,
                physical_match_id="ATP:1:2:2026-09-12", participant_a="A Player", participant_b="B Player",
                market_family="MATCH_WINNER", side="A Player", decimal_odds=1.90,
                implied_probability=1 / 1.90, devigged_probability=0.5, devig_method="proportional",
                n_sides_in_market=2, source_timestamp=NOW)
    base.update(kw)
    return ExternalMarketObservation(**base)


# --------------------------------------------------------------------------- odds and de-vigging
def test_the_margin_is_not_an_edge():
    """A book quoting 1.90/1.90 is not offering 52.6%; it is offering 50% and keeping 5.3%."""
    r = devig_all([1.90, 1.90])
    assert implied(1.90) == pytest.approx(0.5263, abs=1e-4)
    assert r.overround == pytest.approx(1.0526, abs=1e-4)
    assert r.margin == pytest.approx(0.0526, abs=1e-4)
    assert r.probabilities == pytest.approx((0.5, 0.5))


def test_devig_methods_agree_at_even_money_and_diverge_on_longshots():
    even = devig_all([1.90, 1.90])
    assert even.max_method_spread < 1e-6 and not even.method_choice_is_material
    longshot = devig_all([1.10, 7.50])
    assert longshot.method_choice_is_material
    # power takes proportionally more out of the longshot than proportional does
    assert devig_power([1.10, 7.50])[1] < devig_proportional([1.10, 7.50])[1]
    assert 0 < devig_shin([1.10, 7.50])[1] < 1
    for m in (devig_proportional, devig_power, devig_shin):
        assert sum(m([1.10, 7.50])) == pytest.approx(1.0)


def test_devigging_needs_the_whole_market():
    with pytest.raises(ValueError):
        devig_all([1.90])
    assert overround([1.90, 1.90]) > 1.0


def test_odds_conversions_round_trip():
    for d in (1.10, 1.50, 2.0, 3.75, 9.0):
        assert american_to_decimal(decimal_to_american(d)) == pytest.approx(d, abs=0.01)
    assert american_to_decimal(-150) == pytest.approx(1.6667, abs=1e-4)
    assert american_to_decimal(+150) == pytest.approx(2.5)


# --------------------------------------------------------------------------- the observation object
def test_the_opposite_side_is_never_fabricated():
    """A de-vigged probability may only exist when the whole market was observed."""
    with pytest.raises(ExternalMarketError):
        _obs(n_sides_in_market=1)
    with pytest.raises(ExternalMarketError):
        _obs(devig_method="")
    assert _obs(devigged_probability=None, devig_method="", n_sides_in_market=1).devigged_probability is None


def test_a_timestamp_is_never_invented():
    o = _obs(source_timestamp=None)
    assert o.staleness_seconds is None, "no venue timestamp must read as unknown, never as zero"
    older = _obs(source_timestamp="2026-09-12T11:45:00+00:00")
    assert older.staleness_seconds == pytest.approx(900.0)


def test_observations_are_immutable_and_fingerprinted():
    a = _obs()
    with pytest.raises(Exception):
        a.decimal_odds = 3.0
    b = a.evolve(decimal_odds=3.0)
    assert a.decimal_odds == 1.90 and b.fingerprint != a.fingerprint
    assert _obs().fingerprint == a.fingerprint


def test_the_external_store_is_append_only_and_notices_tampering():
    with tempfile.TemporaryDirectory() as td:
        s = ExternalStore(td)
        s.append_many([_obs(side=f"P{i}") for i in range(3)])
        assert s.verify_chain() == [] and len(list(s.rows())) == 3
        path = os.path.join(td, NOW[:10] + ".jsonl")
        lines = path and open(path).read().splitlines()
        rec = json.loads(lines[1]); rec["devigged_probability"] = 0.99
        lines[1] = json.dumps(rec, separators=(",", ":"))
        open(path, "w").write("\n".join(lines) + "\n")
        assert any("modified after the fact" in p for p in s.verify_chain())


# --------------------------------------------------------------------------- consensus
def test_a_stale_line_is_excluded_not_averaged():
    fresh = _obs(source="bovada", devigged_probability=0.60)
    stale = _obs(source="smarkets", source_kind=EXCHANGE, devigged_probability=0.40,
                 source_timestamp="2026-09-12T10:00:00+00:00")          # two hours old
    r = build_reference([fresh, stale], now=NOW, max_source_staleness_s=900)
    assert r.excluded_stale == 1 and r.value == pytest.approx(0.60)
    assert r.n_independent_groups == 1


def test_two_names_for_one_book_are_one_witness():
    a = _obs(source="espn_odds", devigged_probability=0.60)
    b = _obs(source="espn_bet", devigged_probability=0.70)
    assert group_of("espn_odds") == group_of("espn_bet") == "espn"
    r = build_reference([a, b], now=NOW)
    assert r.n_independent_groups == 1
    assert r.value == pytest.approx(0.65), "duplicates collapse to one group's median, not two votes"


def test_the_reference_is_a_median_across_groups_and_reports_its_dispersion():
    obs = [_obs(source=s, devigged_probability=p) for s, p in
           (("bovada", 0.50), ("smarkets", 0.60), ("polymarket", 0.80))]
    r = build_reference(obs, now=NOW)
    assert r.n_independent_groups == 3 and r.value == pytest.approx(0.60)
    assert r.dispersion == pytest.approx(0.30)
    assert r.aggregation == "median_across_independent_groups"


def test_a_kalshi_derived_source_is_not_admissible_as_a_witness_against_kalshi():
    r = build_reference([_obs(source="kalshi", devigged_probability=0.7)], now=NOW)
    assert r.value is None and r.excluded_inadmissible == 1


def test_an_exchange_makes_it_a_sharp_reference_a_book_alone_does_not():
    assert build_reference([_obs(source="bovada")], now=NOW).kind == "MULTI_BOOK_CONSENSUS"
    assert build_reference([_obs(source="smarkets", source_kind=EXCHANGE)], now=NOW).kind == "SHARP_REFERENCE"


def test_a_reference_needs_the_minimum_number_of_independent_groups():
    r = build_reference([_obs()], now=NOW, min_groups=2)
    assert r.value is None and "independent group" in r.reason


# --------------------------------------------------------------------------- triangulation
def test_triangulation_names_the_odd_one_out():
    assert triangulate(0.46, 0.52, 0.50)["class"] == KALSHI_LONE_OUTLIER
    assert triangulate(0.46, 0.46, 0.52)["class"] == MODEL_LONE_OUTLIER
    assert triangulate(0.46, 0.52, 0.46)["class"] == EXTERNAL_LONE_OUTLIER
    assert triangulate(0.46, 0.52, 0.30)["class"] == ALL_THREE_DISAGREE
    assert triangulate(0.46, 0.47, 0.47)["class"] == MARKETS_AGREE


def test_corroboration_is_directional_not_proximity():
    r = triangulate(0.46, 0.52, 0.62)
    assert r["class"] == KALSHI_LONE_OUTLIER and r["model_overshoots_external"] is True


def test_with_no_model_view_the_two_markets_decide():
    r = triangulate(0.46, 0.52, None)
    assert r["class"] == KALSHI_LONE_OUTLIER and "rests on the two markets only" in r["note"]


# --------------------------------------------------------------------------- the dislocation row
def _dis(**kw):
    base = dict(generated_at=NOW, physical_match_id="ATP:1:2:2026-09-12", kalshi_ticker="T-A",
                kalshi_event="T", side="A Player", market_family="MATCH_WINNER", kalshi_bid=0.45,
                kalshi_ask=0.46, kalshi_mid=0.455, kalshi_size=100.0, kalshi_spread=0.01,
                kalshi_fee=0.02, kalshi_quote_age_s=120.0, external_fair=0.52,
                triangulation=KALSHI_LONE_OUTLIER, external_edge=0.04, reason_against="thin evidence")
    base.update(kw)
    return Dislocation(**base)


def test_a_shadow_bet_cannot_rest_on_our_model_alone():
    # a PASS row with no external reference is legitimate: we record what we looked at and refused
    assert _dis(external_fair=None, external_edge=None).decision == "PASS"
    with pytest.raises(ValueError):
        _dis(decision="SHADOW_BET", external_fair=None)
    with pytest.raises(ValueError):
        _dis(decision="SHADOW_BET", triangulation=MODEL_LONE_OUTLIER)
    with pytest.raises(ValueError):
        _dis(decision="SHADOW_BET", reason_against="  ")
    assert _dis(decision="SHADOW_BET").decision == "SHADOW_BET"


def test_there_is_no_real_money_state_on_a_dislocation():
    with pytest.raises(ValueError):
        _dis(authority="REAL_MONEY")
    with pytest.raises(ValueError):
        _dis(decision="BUY")


def test_the_dislocation_ledger_is_append_only_and_hash_chained():
    with tempfile.TemporaryDirectory() as td:
        lg = DislocationLedger(td)
        for i in range(3):
            lg.append(_dis(kalshi_ticker=f"T-{i}"))
        assert lg.verify_chain() == [] and len(list(lg.rows())) == 3
        path = os.path.join(td, NOW[:10] + ".jsonl")
        lines = open(path).read().splitlines()
        rec = json.loads(lines[0]); rec["external_fair"] = 0.99
        lines[0] = json.dumps(rec, separators=(",", ":"))
        open(path, "w").write("\n".join(lines) + "\n")
        assert any("modified after the fact" in p for p in lg.verify_chain())


def test_the_fee_is_what_kills_a_one_cent_dislocation():
    ask, fair = 0.46, 0.47
    fee = taker_fee(ask, 1.0, FeeSchedule())
    assert fair - ask > 0 and fair - ask - fee < 0
    assert _dis(external_fair=fair, external_edge=fair - ask - fee).external_edge < 0


# --------------------------------------------------------------------------- mapping
class _FakeMapper:
    def __init__(self, table):
        self.table = table

    def resolve(self, tour, name, competitor_id=None, today=None):
        v = self.table.get((tour, name))
        if v is None:
            return {"status": "UNMAPPED", "reason": "no exact full-name match", "player_id": None,
                    "confidence": 0.0}
        if v == "AMBIGUOUS":
            return {"status": "AMBIGUOUS", "reason": "2 namesakes", "player_id": None, "confidence": 0.0}
        return {"status": "MAPPED", "player_id": v, "confidence": 1.0}


def test_mapping_refuses_half_an_identification():
    m = _FakeMapper({("ATP", "A Player"): "1"})
    r = map_event(m, source="bovada", source_event_id="e", tour="ATP", name_a="A Player",
                  name_b="Unknown Person", start_utc="2026-09-12T10:00:00Z")
    assert r.status == UNMAPPED_PLAYER and r.physical_match_id is None


def test_mapping_refuses_a_shared_name_and_refuses_doubles():
    m = _FakeMapper({("ATP", "A Player"): "1", ("ATP", "B Player"): "AMBIGUOUS"})
    assert map_event(m, source="b", source_event_id="e", tour="ATP", name_a="A Player",
                     name_b="B Player", start_utc="2026-09-12T10:00:00Z").status == AMBIGUOUS_PLAYER
    assert map_event(m, source="b", source_event_id="e", tour="ATP", name_a="X/Y", name_b="Z/W",
                     start_utc="2026-09-12T10:00:00Z").status == DOUBLES_UNSUPPORTED


def test_a_mapped_event_keys_on_canonical_ids_in_a_stable_order():
    m = _FakeMapper({("ATP", "A Player"): "9", ("ATP", "B Player"): "2"})
    r = map_event(m, source="b", source_event_id="e", tour="ATP", name_a="A Player", name_b="B Player",
                  start_utc="2026-09-12T10:00:00Z")
    assert r.status == MAPPED and r.physical_match_id == "ATP:2:9:2026-09-12"
    flipped = map_event(m, source="b", source_event_id="e", tour="ATP", name_a="B Player",
                        name_b="A Player", start_utc="2026-09-12T10:00:00Z")
    assert flipped.physical_match_id == r.physical_match_id
    assert audit([r, flipped])["by_status"][MAPPED] == 2


def test_a_one_day_slip_is_allowed_only_for_near_simultaneous_starts():
    ext = {"ATP:1:2:2026-09-12": {"start_utc": "2026-09-12T23:30:00+00:00"},
           "ATP:3:4:2026-09-10": {"start_utc": "2026-09-10T10:00:00+00:00"}}
    kal = {"ATP:1:2:2026-09-13": {"start_utc": "2026-09-13T00:30:00+00:00"},
           "ATP:3:4:2026-09-11": {"start_utc": "2026-09-11T18:00:00+00:00"}}
    j = join_to_kalshi(ext, kal)
    assert "ATP:1:2:2026-09-13" in j and "slip accepted" in j["ATP:1:2:2026-09-13"][2]
    assert "ATP:3:4:2026-09-11" not in j, "32 hours apart is a different match, not a clock difference"


# --------------------------------------------------------------------------- the source adapter
def _coupon(period="Match", live=False, status="O", key="Head To Head"):
    return [{"path": [{"description": "Guadalajara"}, {"description": "WTA"}],
             "events": [{"id": "1", "description": "A vs B", "startTime": 1789300000000,
                         "lastModified": 1789299000000, "live": live,
                         "competitors": [{"name": "A Player"}, {"name": "B Player"}],
                         "displayGroups": [{"markets": [{
                             "descriptionKey": key, "description": "Moneyline", "status": "O",
                             "period": {"description": period, "live": False},
                             "outcomes": [
                                 {"description": "A Player", "status": status,
                                  "price": {"decimal": "1.90", "american": "-111"}},
                                 {"description": "B Player", "status": "O",
                                  "price": {"decimal": "1.90", "american": "-111"}}]}]}]}]}]


def test_only_whole_match_markets_are_parsed():
    rows, stats = parse_coupon(_coupon(period="Match"), observed_at=NOW)
    assert len(rows) == 2 and stats["skipped_period"] == 0
    rows, stats = parse_coupon(_coupon(period="1st Set"), observed_at=NOW)
    assert rows == [] and stats["skipped_period"] == 1
    assert "Match" in MATCH_PERIODS and "1st Set" not in MATCH_PERIODS


def test_a_live_event_is_never_treated_as_a_pregame_reference():
    rows, stats = parse_coupon(_coupon(live=True), observed_at=NOW)
    assert rows == [] and stats["skipped_live"] == 1


def test_a_suspended_side_is_not_de_vigged_against_an_invented_opposite():
    rows, stats = parse_coupon(_coupon(status="SU"), observed_at=NOW)
    assert stats["devigged"] == 0
    assert all(r.devigged_probability is None for r in rows)


def test_an_unknown_market_family_is_skipped_rather_than_guessed():
    rows, stats = parse_coupon(_coupon(key="Some New Prop"), observed_at=NOW)
    assert rows == [] and stats["skipped_family"] == 1
    assert "Head To Head" in FAMILY_MAP and FAMILY_MAP["Head To Head"] == "MATCH_WINNER"


def test_the_parsed_rows_carry_the_venue_timestamp_and_a_margin():
    rows, _ = parse_coupon(_coupon(), observed_at=NOW)
    assert all(r.source_timestamp for r in rows)
    assert rows[0].source_margin == pytest.approx(0.0526, abs=1e-3)
    assert rows[0].devigged_probability == pytest.approx(0.5)


# --------------------------------------------------------------------------- the frozen models
def test_the_wave_three_models_are_frozen():
    """Wave 4 may not retune what Wave 3 measured. The version strings are the contract."""
    from tennis_edge.models.fair import FAIR_VERSION
    from tennis_edge.models.gen2 import MODEL_VERSION as GEN2
    from tennis_edge.selector.decide import SELECTOR_VERSION
    assert (FAIR_VERSION, GEN2, SELECTOR_VERSION) == ("fair_v1", "gen2_dyn_hier_sr_v1", "selector_v1")


def test_the_wave_two_and_three_candidates_are_untouched():
    from tennis_edge.research.registry import load_all
    root = os.path.join(os.path.dirname(__file__), "..", "data", "research", "edge_candidates")
    if not os.path.isdir(root):
        pytest.skip("no candidate registry on this checkout")
    ids = {c.candidate_id for c in load_all(root)}
    assert {"EC-2026-001-MKTCOND-EXACT-SCORE", "EC-2026-002-MKTCOND-GAME-SPREAD",
            "EC-2026-003-GEN2-MODERATE-EVIDENCE", "EC-2026-004-COHERENCE-EXECUTABLE",
            "W3-2026-001-ABSTAIN-ITF", "W3-2026-002-NONITF-POSITIVE-EDGE"} <= ids


# --------------------------------------------------------------------------- reviewed aliases
def test_a_pending_alias_is_inert_and_an_accepted_one_never_reaches_full_confidence():
    """The residue of unmapped names needs a person, not a looser matcher."""
    import tempfile as _tf
    from tennis_edge.identity.reviewed_aliases import ACCEPTED, ALIAS_CONFIDENCE, audit, load
    doc = {"schema_version": 1, "aliases": [
        {"tour": "WTA", "source_name": "Nick Name", "canonical_id": None,
         "review_status": "PENDING_REVIEW", "provenance": "unverified"},
        {"tour": "WTA", "source_name": "Real Alias", "canonical_id": "123",
         "review_status": ACCEPTED, "provenance": "checked against the governing-body record"},
        {"tour": "WTA", "source_name": "Bad Idea", "canonical_id": "999", "review_status": "REJECTED",
         "provenance": "two different players"}]}
    with _tf.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(doc, f); path = f.name
    live = load(path)
    assert list(live) == [("WTA", "real alias")], "only ACCEPTED entries with a canonical id are live"
    assert audit(path)["by_status"]["PENDING_REVIEW"] == 1
    # 0.95 is exactly the floor qualification requires: enough to price, never enough to be the reason
    from tennis_edge.opportunity.qualify import QualificationPolicy
    assert ALIAS_CONFIDENCE == QualificationPolicy().min_identity_confidence
    os.unlink(path)


# --------------------------------------------------------------------------- the live scan's gates
def _gate(**kw):
    from tennis_edge.external_market.dislocation import scan_gates
    base = dict(external_fair=0.52, kalshi_bid=0.45, kalshi_ask=0.46, size=200.0, quote_age_s=120.0,
                triangulation=KALSHI_LONE_OUTLIER, external_edge=0.04)
    base.update(kw)
    return scan_gates(**base)


def test_the_shadow_bet_path_is_reachable_and_every_gate_can_close_it():
    """A decision path that nothing can ever satisfy is not a filter, it is dead code."""
    assert _gate()["decision"] == "SHADOW_BET"
    for kw, gate in (({"external_fair": None, "external_edge": None}, "reference_exists"),
                     ({"kalshi_bid": 0.30}, "spread_ok"),
                     ({"size": 0.0}, "size_ok"),
                     ({"quote_age_s": 7200.0}, "kalshi_quote_fresh"),
                     ({"external_edge": 0.01}, "external_edge_material"),
                     ({"triangulation": MODEL_LONE_OUTLIER}, "kalshi_is_the_outlier")):
        r = _gate(**kw)
        assert r["decision"] != "SHADOW_BET" and gate in r["failed"]


def test_a_real_dislocation_with_a_bad_quote_is_a_watch_not_a_pass():
    assert _gate(quote_age_s=7200.0)["decision"] == "WATCH"
    assert _gate(triangulation=MODEL_LONE_OUTLIER)["decision"] == "WATCH"
    assert _gate(external_edge=-0.01)["decision"] == "PASS"
    assert _gate(external_fair=None, external_edge=None)["decision"] == "PASS"


def test_a_crossed_or_one_sided_kalshi_quote_never_reaches_shadow_bet():
    assert _gate(kalshi_bid=0.50, kalshi_ask=0.46)["decision"] != "SHADOW_BET"
    assert _gate(kalshi_ask=None)["decision"] != "SHADOW_BET"


# --------------------------------------------------------------------------- Smarkets (Wave 5)
def _sm_market(name="Match winner", mid="1", ev="9"):
    return {"id": mid, "event_id": ev, "name": name, "state": "open"}


def _sm_fixture(bid=3472, ask=4348, other_bid=5495, other_ask=6536):
    from tennis_edge.external_market import smarkets as sm
    events = [{"id": "9", "name": "Alpha Player vs Beta Player",
               "start_datetime": "2026-09-13T18:05:00Z", "state": "upcoming", "bettable": True}]
    markets = [_sm_market(), _sm_market(name="Set 1 winner", mid="2")]
    contracts = [{"id": "c1", "market_id": "1", "name": "Alpha Player"},
                 {"id": "c2", "market_id": "1", "name": "Beta Player"},
                 {"id": "c3", "market_id": "2", "name": "Alpha Player"}]
    quotes = {"c1": {"bids": [{"price": bid, "quantity": 2916191}],
                     "offers": [{"price": ask, "quantity": 12637800}]},
              "c2": {"bids": [{"price": other_bid, "quantity": 1842586}],
                     "offers": [{"price": other_ask, "quantity": 2922927}]},
              "c3": {"bids": [], "offers": []}}
    lastex = {"last_executed_prices": {"1": [{"contract_id": "c1", "last_executed_price": "45.45",
                                              "timestamp": "2026-09-13T02:34:39Z"}]}}
    return sm, events, markets, contracts, quotes, lastex


def test_smarkets_prices_are_hundredths_of_a_percent():
    from tennis_edge.external_market.smarkets import price_to_prob
    assert price_to_prob(3472) == pytest.approx(0.3472)      # order book integer
    assert price_to_prob("45.45") == pytest.approx(0.4545)   # last-traded decimal percent
    assert price_to_prob(0) is None and price_to_prob(None) is None


def test_only_match_scope_smarkets_markets_are_mapped():
    from tennis_edge.external_market.smarkets import family_of
    assert family_of("Match winner") == ("MATCH_WINNER", None)
    assert family_of("Over/under 21.5") == ("TOTAL_GAMES", 21.5)
    assert family_of("A B +2.5 / C D -2.5 games")[0] == "GAME_SPREAD"
    # a set-scoped market prices a different question than a match-scope Kalshi contract
    assert family_of("Set 1 winner") == (None, None)
    assert family_of("Correct score Set 1") == (None, None)


def test_an_exchange_midpoint_is_the_reference_and_the_spread_is_the_margin():
    sm, events, markets, contracts, quotes, lastex = _sm_fixture()
    rows, stats = sm.observations(events=events, markets=markets, contracts=contracts, quotes=quotes,
                                  last_executed=lastex, observed_at=NOW)
    # the set-scoped market is skipped by family, so its contract is never priced at all
    assert stats["skipped_family"] == 1 and stats["rows"] == 2
    by_side = {r.side: r for r in rows}
    a = by_side["Alpha Player"]
    assert a.source_kind == EXCHANGE and a.devig_method == "exchange_midpoint"
    assert a.devigged_probability == pytest.approx(0.5 * (0.3472 + 0.4348))
    assert a.source_margin == pytest.approx(0.0876)      # for an exchange the margin IS the spread
    assert a.lay_price == pytest.approx(0.3472) and a.back_price == pytest.approx(0.4348)


def test_smarkets_publishes_no_quote_timestamp_and_we_do_not_invent_one():
    sm, events, markets, contracts, quotes, lastex = _sm_fixture()
    rows, _ = sm.observations(events=events, markets=markets, contracts=contracts, quotes=quotes,
                              last_executed=lastex, observed_at=NOW)
    a = next(r for r in rows if r.side == "Alpha Player")
    assert a.source_timestamp is None and a.staleness_seconds is None
    # the last TRADED price does carry a time, and it is a different fact, kept as such
    assert "last traded 0.4545 at 2026-09-13T02:34:39Z" in a.line


def test_a_one_sided_smarkets_book_yields_no_reference_and_an_empty_one_yields_no_row():
    sm, events, markets, contracts, quotes, lastex = _sm_fixture()
    quotes["c2"] = {"bids": [], "offers": []}
    rows, stats = sm.observations(events=events, markets=markets, contracts=contracts, quotes=quotes,
                                  last_executed=lastex, observed_at=NOW)
    assert stats["no_book"] == 1 and not any(r.side == "Beta Player" for r in rows)

    sm, events, markets, contracts, quotes, lastex = _sm_fixture()
    quotes["c1"] = {"bids": [{"price": 3472, "quantity": 100}], "offers": []}
    rows, _ = sm.observations(events=events, markets=markets, contracts=contracts, quotes=quotes,
                              last_executed=lastex, observed_at=NOW)
    a = next(r for r in rows if r.side == "Alpha Player")
    assert a.devigged_probability is None and a.n_sides_in_market == 1


def test_a_wide_exchange_book_is_stored_but_cannot_drive_a_decision():
    """Smarkets quotes tennis at a median 10c spread. That midpoint is an opinion, not a price."""
    from tennis_edge.external_market.consensus import DEFAULT_MAX_EXCHANGE_SPREAD
    wide = _obs(source="smarkets", source_kind=EXCHANGE, devigged_probability=0.55, source_margin=0.10,
                devig_method="exchange_midpoint")
    tight = _obs(source="smarkets", source_kind=EXCHANGE, devigged_probability=0.55, source_margin=0.02,
                 devig_method="exchange_midpoint")
    book = _obs(source="bovada", devigged_probability=0.52, source_margin=0.045)
    r = build_reference([wide, book], now=NOW)
    assert r.excluded_wide_book == 1 and r.groups == ("bovada",) and r.value == pytest.approx(0.52)
    r2 = build_reference([tight, book], now=NOW)
    assert r2.n_independent_groups == 2 and r2.kind == "SHARP_REFERENCE"
    # a sportsbook's overround is a different quantity and is never judged by this bound
    assert build_reference([_obs(source="bovada", source_margin=0.12)], now=NOW).excluded_wide_book == 0
    assert DEFAULT_MAX_EXCHANGE_SPREAD < 0.10


def test_the_two_venues_are_separate_witness_groups():
    from tennis_edge.external_market.consensus import group_of
    assert group_of("bovada") != group_of("smarkets")
    r = build_reference([_obs(source="bovada", devigged_probability=0.50),
                         _obs(source="smarkets", source_kind=EXCHANGE, devigged_probability=0.60,
                              source_margin=0.02, devig_method="exchange_midpoint")], now=NOW)
    assert r.n_independent_groups == 2 and r.value == pytest.approx(0.55)


def test_the_smarkets_traversal_is_recorded_in_code():
    """The path is not discoverable from the docs; losing it would cost another wave to rediscover."""
    from tennis_edge.external_market.smarkets import TRAVERSAL
    joined = " ".join(TRAVERSAL)
    assert "type=tennis_match" in joined and "/quotes/" in joined and "/contracts/" in joined
