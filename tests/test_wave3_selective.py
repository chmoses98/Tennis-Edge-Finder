"""Wave 3: the selective mispricing detector.

These tests exist because every one of them corresponds to a way the system could quietly start lying:
an opportunity edited after the outcome, a market that had already started, a stale quote treated as
executable, an "edge" that is really the taker fee, a selector fitted on the block it is judged on, a
candidate confirmed by the data that suggested it, a name matched to the wrong player.
"""
from __future__ import annotations

import json
import os
import tempfile
from datetime import date, datetime, timedelta, timezone

import numpy as np
import pandas as pd
import pytest

from tennis_edge.models.fair import FairConfig, PERTURBATIONS
from tennis_edge.opportunity.qualify import QualificationInputs, QualificationPolicy, qualify
from tennis_edge.opportunity.schema import (Opportunity, OpportunityError, OpportunityStore,
                                            RESEARCH_AUTHORITY)
from tennis_edge.pricing.fees import FeeSchedule, breakeven_price, taker_fee
from tennis_edge.research.registry import EdgeCandidate, FirewallError
from tennis_edge.selector.decide import DecisionInputs, DecisionPolicy, decide
from tennis_edge.selector.features import FEATURES, FORBIDDEN, assert_no_leakage, build_features
from tennis_edge.selector.model import Selector, SelectorFirewallError

NOW = "2026-09-12T12:00:00+00:00"


def _opp(**kw):
    base = dict(opportunity_id="o1", generated_at=NOW, physical_match_id="ATP:1:2:2026-09-12",
                event="EV", ticker="EV-A", family="MATCH_WINNER", side="YES", strike=None,
                lane="MODEL_3", model_version="v1", fair_prob=0.58, uncertainty=0.02)
    base.update(kw)
    return Opportunity(**base)


# --------------------------------------------------------------------------- the object itself
def test_an_opportunity_cannot_be_edited_after_the_fact():
    o = _opp()
    with pytest.raises(Exception):
        o.fair_prob = 0.9                       # frozen dataclass
    changed = o.evolve(fair_prob=0.9)
    assert o.fair_prob == 0.58                  # the original is untouched
    assert changed.fingerprint != o.fingerprint  # and the copy is a different record


def test_the_fingerprint_covers_every_field():
    a, b = _opp(), _opp(reason_for="because")
    assert a.fingerprint != b.fingerprint
    assert _opp().fingerprint == a.fingerprint   # and is deterministic


def test_there_is_no_real_money_state():
    with pytest.raises(OpportunityError):
        _opp(authority="REAL_MONEY")
    assert _opp().authority == RESEARCH_AUTHORITY
    from tennis_edge.opportunity.schema import Decision
    assert set(Decision.ALL) == {"PASS", "WATCH", "SHADOW_BET"}


def test_a_post_start_market_cannot_be_a_shadow_bet():
    ok = {k: True for k in ("qualified",)}
    with pytest.raises(OpportunityError):
        _opp(decision="SHADOW_BET", first_ball_classification="POST_START",
             reason_against="x", qualification=ok)
    # and the same row pregame is allowed
    assert _opp(decision="SHADOW_BET", first_ball_classification="STRICT_PREGAME",
                reason_against="x", qualification=ok).decision == "SHADOW_BET"


def test_a_shadow_bet_must_carry_its_counter_argument_and_pass_every_filter():
    with pytest.raises(OpportunityError):
        _opp(decision="SHADOW_BET", qualification={"a": True}, reason_against="  ")
    with pytest.raises(OpportunityError):
        _opp(decision="SHADOW_BET", qualification={"a": True, "b": False}, reason_against="x")
    with pytest.raises(OpportunityError):
        _opp(decision="SHADOW_BET", qualification={}, reason_against="x")


# --------------------------------------------------------------------------- qualification
def _qi(**kw):
    base = dict(family="MATCH_WINNER", identity_confidence=1.0, fair_prob=0.58, executable_ask=0.54,
                executable_bid=0.52, quote_age_seconds=600.0, available_size=180.0,
                fee_per_contract=0.01, first_ball_classification="START_UNKNOWN",
                data_quality_score=0.8)
    base.update(kw)
    return QualificationInputs(**base)


def test_a_stale_quote_does_not_qualify():
    assert qualify(_qi()).ok
    q = qualify(_qi(quote_age_seconds=7200.0))
    assert not q.ok and "price_not_stale" in q.failed


def test_a_quote_with_no_size_behind_it_does_not_qualify():
    for size in (0.0, None):
        q = qualify(_qi(available_size=size))
        assert not q.ok and "size_available" in q.failed


def test_a_one_sided_or_crossed_quote_does_not_qualify():
    assert "executable_price_exists" in qualify(_qi(executable_bid=None)).failed
    assert "executable_price_exists" in qualify(_qi(executable_ask=0.40, executable_bid=0.50)).failed


def test_a_wide_spread_and_an_unknown_family_do_not_qualify():
    assert "spread_acceptable" in qualify(_qi(executable_bid=0.30)).failed
    assert "contract_semantics_known" in qualify(_qi(family="MYSTERY_PROP")).failed


def test_post_start_fails_qualification_but_start_unknown_does_not():
    assert "not_post_start" in qualify(_qi(first_ball_classification="POST_START")).failed
    assert qualify(_qi(first_ball_classification="START_UNKNOWN")).ok


def test_a_broken_health_gate_blocks_the_market():
    assert "health_gates_ok" in qualify(_qi(broken_health_gates=("TENNIS-4",))).failed


# --------------------------------------------------------------------------- the money
def test_the_fee_is_not_an_edge():
    fair, ask = 0.52, 0.51
    fee = taker_fee(ask, 1.0, FeeSchedule())
    assert fair - ask > 0                       # raw edge says yes
    assert fair - ask - fee < 0                 # after the fee it is a losing trade
    assert fee == pytest.approx(0.07 * 0.51 * 0.49, abs=0.01)


def test_bet_up_to_is_the_last_price_that_still_pays():
    for fair in (0.30, 0.55, 0.80):
        p = breakeven_price(fair, FeeSchedule())
        assert fair - p - taker_fee(p, 1.0) >= 0
        assert fair - (p + 0.01) - taker_fee(p + 0.01, 1.0) < 0
        assert p < fair                          # the fee always costs something


def test_the_price_sensitivity_curve_falls_monotonically():
    fair, ask = 0.58, 0.50
    evs = [fair - (ask + c / 100) - taker_fee(ask + c / 100, 1.0) for c in (0, 1, 2, 3, 5)]
    assert all(b < a for a, b in zip(evs, evs[1:]))


# --------------------------------------------------------------------------- robustness
def test_the_robust_edge_is_the_worst_case_over_the_perturbation_set():
    env = [0.61, 0.58, 0.55, 0.52]
    ask, fee = 0.54, 0.017
    assert min(env) - ask - fee < 0 < max(env) - ask - fee     # sign flips inside the set
    assert min(env) - ask - fee == pytest.approx(0.52 - 0.54 - 0.017)


def test_the_perturbation_set_is_a_real_set_and_contains_the_centre():
    names = [c.name for c in PERTURBATIONS]
    assert names[0] == "base" and len(set(names)) == len(names) >= 8
    assert FairConfig() == PERTURBATIONS[0]
    axes = {(c.surface_w_max, c.gen2_prior_points, c.blend_points, c.extra_half_life_days)
            for c in PERTURBATIONS}
    assert len(axes) >= 8, "the set must actually move the parameters, not just rename them"


# --------------------------------------------------------------------------- the selector
def _frame(n=200, start=date(2026, 8, 25), days=8, seed=0):
    rng = np.random.default_rng(seed)
    dts = [str(start + timedelta(days=int(i))) for i in rng.integers(0, days, n)]
    mid = rng.uniform(0.15, 0.85, n)
    return pd.DataFrame({
        "sched_date": dts, "y": rng.integers(0, 2, n).astype(float), "kalshi_mid": mid,
        "kalshi_ask": np.clip(mid + 0.01, 0.02, 0.98), "kalshi_bid": np.clip(mid - 0.01, 0.01, 0.97),
        "fee": 0.07 * mid * (1 - mid), "p_fair": np.clip(mid + rng.normal(0, 0.08, n), 0.02, 0.98),
        "p_elo": np.clip(mid + rng.normal(0, 0.08, n), 0.02, 0.98),
        "p_sr": np.clip(mid + rng.normal(0, 0.1, n), 0.02, 0.98),
        "p_env_min": np.clip(mid - 0.05, 0.01, 0.98), "p_env_max": np.clip(mid + 0.05, 0.02, 0.99),
        "blend_weight": rng.uniform(0, 1, n), "serve_level": rng.uniform(0.5, 0.7, n),
        "ev_min": rng.uniform(0, 5000, n), "ev_side": rng.uniform(0, 5000, n),
        "n_matches_min": rng.integers(1, 300, n), "days_stale_max": rng.integers(1, 200, n),
        "identity_confidence": 1.0, "data_quality": rng.uniform(0.2, 1, n),
        "spread": 0.02, "kalshi_oi": rng.uniform(10, 5000, n), "two_sided_gap": 0.005,
        "mv_move_6h": rng.normal(0, 0.03, n), "mv_abs_move_6h": rng.uniform(0, 0.1, n),
        "mv_volatility_24h": rng.uniform(0, 0.08, n), "mv_volume_24h": rng.uniform(0, 500, n),
        "mv_n_quotes_24h": rng.integers(1, 24, n),
        "mv_hours_since_last_change": rng.uniform(0, 40, n),
        "hours_to_sched": rng.uniform(1, 40, n), "quote_age_s": rng.uniform(60, 3000, n),
        "level": rng.choice(["ITF", "CHALLENGER", "TOUR_500_250"], n),
        "tour": rng.choice(["ATP", "WTA"], n)})


def test_no_feature_is_derived_from_the_outcome():
    assert_no_leakage(_frame())
    assert "y" in FORBIDDEN
    with pytest.raises(ValueError):
        assert_no_leakage(_frame(), features=("won_rate",))
    # and the real feature list survives the same check
    X = build_features(_frame())
    assert list(X.columns) == list(FEATURES) and X.notna().all().all()


def test_a_selector_refuses_to_be_fitted_outside_its_declared_window():
    d = _frame()
    X = build_features(d)
    s = Selector(version="t", feature_names=tuple(FEATURES), target="t",
                 trained_from="2026-08-25", trained_through="2026-08-28")
    with pytest.raises(SelectorFirewallError):
        s.fit(X, d.y.to_numpy(float), d.sched_date)          # the frame runs past 08-28
    keep = d.sched_date <= "2026-08-28"
    s.fit(X[keep.values], d.y[keep].to_numpy(float), d.sched_date[keep])
    assert s.n_train == int(keep.sum())


def test_the_holdout_cannot_be_used_to_refit_a_frozen_selector():
    d = _frame()
    X = build_features(d)
    keep = d.sched_date <= "2026-08-28"
    s = Selector(version="t", feature_names=tuple(FEATURES), target="t",
                 trained_from="2026-08-25", trained_through="2026-08-28")
    s.fit(X[keep.values], d.y[keep].to_numpy(float), d.sched_date[keep]).freeze()
    assert s.frozen_at
    with pytest.raises(SelectorFirewallError):
        s.fit(X[keep.values], d.y[keep].to_numpy(float), d.sched_date[keep])
    # scoring the later block is fine; that is what a holdout is for
    assert len(s.score(X[(~keep).values])) == int((~keep).sum())


def test_a_selector_will_not_score_a_different_feature_set():
    d = _frame()
    X = build_features(d)
    keep = d.sched_date <= "2026-08-28"
    s = Selector(version="t", feature_names=tuple(FEATURES), target="t",
                 trained_from="2026-08-25", trained_through="2026-08-28")
    s.fit(X[keep.values], d.y[keep].to_numpy(float), d.sched_date[keep])
    with pytest.raises(SelectorFirewallError):
        s.score(X.drop(columns=[FEATURES[0]]))


def test_a_selector_round_trips_through_json_with_its_fingerprint():
    d = _frame()
    X = build_features(d)
    keep = d.sched_date <= "2026-08-28"
    s = Selector(version="t", feature_names=tuple(FEATURES), target="t",
                 trained_from="2026-08-25", trained_through="2026-08-28")
    s.fit(X[keep.values], d.y[keep].to_numpy(float), d.sched_date[keep]).freeze()
    back = Selector.from_dict(json.loads(json.dumps(s.to_dict())))
    assert np.allclose(back.score(X), s.score(X))
    with pytest.raises(SelectorFirewallError):
        back.fit(X[keep.values], d.y[keep].to_numpy(float), d.sched_date[keep])


# --------------------------------------------------------------------------- the decision
def _di(**kw):
    base = dict(qualification_ok=True, fee_adjusted_edge=0.04, robust_edge=0.01, env_width=0.03,
                data_quality=0.8, level="CHALLENGER")
    base.update(kw)
    return DecisionInputs(**base)


def test_the_decision_gates_do_what_they_say():
    assert decide(_di())["decision"] == "SHADOW_BET"
    assert decide(_di(level="ITF"))["decision"] == "WATCH"          # the replicated abstention
    assert decide(_di(robust_edge=-0.01))["decision"] == "WATCH"
    assert decide(_di(qualification_ok=False))["decision"] == "PASS"
    assert decide(_di(fee_adjusted_edge=-0.01))["decision"] == "PASS"


def test_an_implausibly_large_edge_is_not_a_shadow_bet():
    r = decide(_di(fee_adjusted_edge=0.30, robust_edge=0.20))
    assert r["decision"] == "WATCH" and "edge_is_plausible" in r["failed_gates"]
    assert "more likely to be our error" in r["reason_against"]


def test_every_decision_states_the_case_against_itself():
    for kw in ({}, {"level": "ITF"}, {"qualification_ok": False}, {"fee_adjusted_edge": 0.4}):
        assert decide(_di(**kw))["reason_against"].strip()


def test_a_market_conditioned_lane_is_never_counted_as_an_independent_witness():
    import tennis_edge.selector.features as feat
    src = open(feat.__file__).read()
    assert "market_conditioned" not in src, "a market-anchored lane cannot be a witness against the market"
    con = json.load(open(os.path.join(os.path.dirname(__file__), "..", "research", "consensus",
                                      "results.json"))) if os.path.exists(
        os.path.join(os.path.dirname(__file__), "..", "research", "consensus", "results.json")) else None
    if con:
        assert "NOT independent" in con["dependence_note"]


# --------------------------------------------------------------------------- the store
def test_the_opportunity_store_is_append_only_and_notices_tampering():
    with tempfile.TemporaryDirectory() as td:
        s = OpportunityStore(td)
        for i in range(3):
            s.append(_opp(opportunity_id=f"o{i}"))
        assert s.verify_chain() == []
        assert len(list(s.rows())) == 3
        path = os.path.join(td, NOW[:10] + ".jsonl")
        lines = open(path).read().splitlines()
        rec = json.loads(lines[1]); rec["fair_prob"] = 0.99
        lines[1] = json.dumps(rec, separators=(",", ":"))
        open(path, "w").write("\n".join(lines) + "\n")
        problems = s.verify_chain()
        assert problems and any("modified after the fact" in p for p in problems)


# --------------------------------------------------------------------------- candidates
def test_a_candidate_cannot_be_confirmed_on_the_data_that_produced_it():
    from tennis_edge.research.registry import add_evidence
    c = EdgeCandidate(candidate_id="W3-TEST", hypothesis="h", inclusion_rule="r",
                      market_family="MATCH_WINNER", model_version="v",
                      discovery_window_start="2026-08-25", discovery_window_end="2026-09-06",
                      frozen_at="2026-09-12T00:00:00+00:00",
                      confirmation_start="2026-09-12T00:00:00+00:00", minimum_n=100,
                      required_accuracy_condition="a", required_clv_condition="b",
                      required_after_fee_condition="c", strongest_opposing_reason="d")
    with pytest.raises(FirewallError):
        add_evidence(c, observed_from="2026-09-01T00:00:00+00:00",
                     observed_to="2026-09-05T00:00:00+00:00", n=500, metrics={"roi": 0.4})
    add_evidence(c, observed_from="2026-09-13T00:00:00+00:00",
                 observed_to="2026-09-20T00:00:00+00:00", n=500, metrics={"roi": 0.4})
    assert len(c.evidence) == 1


# --------------------------------------------------------------------------- identity
def test_identity_refuses_a_shared_name_rather_than_guessing():
    from tennis_edge.identity.crosswalk import build_crosswalk
    m = pd.DataFrame({
        "id_system": ["sackmann", "sackmann", "espn", "espn"],
        "winner_id": ["1", "2", "e1", "e2"], "winner_name": ["Alex Smith", "Alex Smith", "Alex Smith", "Bo Jones"],
        "loser_id": ["9", "9", "e9", "e9"], "loser_name": ["Zed Other", "Zed Other", "Zed Other", "Zed Other"]})
    cw = build_crosswalk(m, foreign="espn")
    by_id = {r.foreign_id: r.status for r in cw.itertuples(index=False)}
    assert by_id["e1"] == "AMBIGUOUS_NAME"          # two canonical players share the name
    assert by_id["e2"] == "NO_CANONICAL_MATCH"      # nobody canonical uses it


# --------------------------------------------------------------------------- timing
def test_market_movement_cannot_see_past_the_cutoff():
    from scripts.research.build_opportunity_dataset import movement, prestart_quote
    cutoff = 1_000_000
    hour = 3600
    hist = [{"end_ts": cutoff - k * hour, "bid": 0.49, "ask": 0.51, "mid": 0.50, "volume": 10.0, "oi": 100.0}
            for k in range(24, 0, -1)]
    future = [{"end_ts": cutoff + k * hour, "bid": 0.09, "ask": 0.11, "mid": 0.10, "volume": 9999.0,
               "oi": 9999.0} for k in range(1, 6)]
    q = prestart_quote(hist + future, cutoff)
    assert q["end_ts"] <= cutoff
    a = movement(hist, cutoff, q)
    b = movement(hist + future, cutoff, q)
    assert a == b, "a candle that closed after the cutoff changed a feature"
    assert b["volume_24h"] < 9999.0


def test_strict_clv_requires_ab_first_ball_truth():
    """Confidence C is the only first-ball truth this system has ever produced. It must not be enough."""
    import inspect
    from tennis_edge.firstball.truth import FirstBallTruth
    from tennis_edge.ledger.close import canonical_close
    from tennis_edge.ledger.quotes import Quote
    t0 = datetime(2026, 9, 12, 10, 0, tzinfo=timezone.utc)
    fields = set(inspect.signature(Quote).parameters)
    tkey = "observed_at" if "observed_at" in fields else "ts"
    q = Quote(**{tkey: t0 - timedelta(minutes=30), "yes_bid": 0.50, "yes_ask": 0.52})
    for conf, strict_expected in (("C", False), ("UNKNOWN", False)):
        truth = FirstBallTruth(match_id="m", actual_first_ball_at_utc=t0, lower_bound_utc=t0, upper_bound_utc=t0,
                               confidence=conf, derivation_method="STATE_TRANSITION_BRACKET")
        assert canonical_close([q], truth).strict is strict_expected
