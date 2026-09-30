"""Validate and record assisted decisions, wagers, postmortems and post-decision evidence.

A submission is refused (AssistedValidationError with a stable code) rather than repaired. Nothing here
can overwrite an existing record: the store refuses an id that exists, and a content duplicate of a
recent decision is refused as DUPLICATE_SUBMISSION.

Refusal codes: INVALID_PAYLOAD, UNKNOWN_FIELD, TRACK_NOT_STARTED, INVALID_DECISION, INVALID_ID,
INVALID_TICKER, INVALID_TIMESTAMP, DECISION_IN_FUTURE, RECORDED_TOO_LATE, BEFORE_TRACK_START,
UNSUPPORTED_MARKET_FAMILY, MARKET_NOT_FOUND, MARKET_NOT_OPEN, IDENTIFIER_MISMATCH, POST_START_DECISION,
INVALID_FIELD, MISSING_FIELD, INVALID_FACTOR_TAG, EXPRESSION_MISMATCH, MARKET_PRICE_UNAVAILABLE,
DUPLICATE_ID, DUPLICATE_SUBMISSION, UNKNOWN_DECISION, WAGER_MARKET_MISMATCH, STAKE_MISMATCH.
"""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timedelta, timezone

from tennis_edge.kalshi.families import SERIES
from tennis_edge.pricing.fees import taker_fee

from . import ASSISTED_AUTHORITY, AUTONOMOUS_REAL_MONEY_AUTHORITY, TRACK_NAME
from .market import first_ball_bound, fnum, iso, load_truths, quote_record_at, truth_for
from .schema import (ASSISTED_SCHEMA_VERSION, CONFIDENCE, DECISION_FIELDS, DECISIONS, EVIDENCE_FIELDS,
                     FACTOR_TAGS, LOSS_ATTRIBUTION, MARKET_EXPRESSIONS, MATERIAL_DISAGREEMENT,
                     MAX_CLOCK_SKEW_S, MAX_RECORDING_LAG_S, POSTMORTEM_FIELDS, POSTMORTEM_USE_RESTRICTION, SIDES,
                     SUPPORTED_FAMILIES, WAGER_FIELDS, WAGER_SOURCES, WAGER_STATUS, AssistedValidationError,
                     classify_agreement, expression_of_family, level_bucket, match_code_of, preferred_side, series_of,
                     side_edges, side_prices, surface_bucket, valid_physical_match_id, valid_record_id, valid_ticker)
from .slate import FIRST_BALL_COVERED, load_slate, slate_market
from .store import RecordStore, canonical_hash, load_track_start

RECORDER_VERSION = "assisted_recorder_v1"
DUPLICATE_WINDOW_S = 6 * 3600
SLATE_MAX_AGE_H = 13.0
STALE_QUOTE_S = 30 * 60
MAX_STAKE_UNITS = 10.0
MAX_TEXT = 4000

#: what a handicapper may submit for a decision. Everything else is derived and stamped by the recorder.
DECISION_INPUT_KEYS = {
    "decision_id", "created_at", "ticker", "side", "decision", "event_id", "physical_match_id", "strike",
    # model context the handicapper saw (optional; otherwise filled from the repo slate)
    "gen1_probability", "gen2_probability", "model4_probability_if_applicable", "fair_v1_probability",
    "selector_state", "model_uncertainty", "serve_evidence_player_a", "serve_evidence_player_b", "rating_state",
    "surface_adjustment", "recent_form_inputs", "additional_model_inputs",
    # market context the handicapper saw on the live book (optional; otherwise the capture at created_at)
    "kalshi_bid", "kalshi_ask", "displayed_size",
    # external context (optional; otherwise filled from the slate)
    "bovada_probability_if_available", "smarkets_probability_if_available", "external_consensus",
    "triangulation_state", "external_freshness",
    # handicapping
    "chatgpt_fair_probability", "chatgpt_confidence", "chatgpt_thesis", "key_supporting_factors",
    "key_opposing_factors", "factor_tags", "market_disagreement_reason", "why_market_may_be_wrong",
    "why_model_may_be_wrong", "pass_reason_if_pass",
    # expression
    "primary_match_thesis", "available_expressions", "chosen_expression", "why_chosen_expression_best_matches_thesis",
    # decision
    "recommended_price", "bet_up_to_probability", "bet_up_to_price", "stake_units_if_bet", "actual_wagered",
}
MODEL_INPUT_KEYS = ("gen1_probability", "gen2_probability", "model4_probability_if_applicable", "fair_v1_probability",
                    "selector_state", "model_uncertainty", "serve_evidence_player_a", "serve_evidence_player_b",
                    "rating_state", "surface_adjustment", "recent_form_inputs", "additional_model_inputs")
EXTERNAL_INPUT_KEYS = ("bovada_probability_if_available", "smarkets_probability_if_available", "external_consensus",
                       "triangulation_state", "external_freshness")
WAGER_INPUT_KEYS = {"wager_id", "decision_id", "placed_at", "ticker", "side", "entry_price", "contracts",
                    "stake_dollars", "fees", "source", "status", "external_order_id"}
POSTMORTEM_INPUT_KEYS = {"postmortem_id", "decision_id", "result", "what_thesis_got_right", "what_thesis_got_wrong",
                         "whether_loss_was_process_or_variance", "data_that_would_have_helped",
                         "potential_research_question"}
POSTMORTEM_RESULTS = ("WIN", "LOSS", "VOID", "NOT_BET", "UNSETTLED")
EVIDENCE_INPUT_KEYS = {"evidence_id", "decision_id", "discovered_at", "evidence", "source", "bears_on"}


# ---------------------------------------------------------------------------------------------- helpers
def _now() -> datetime:
    return datetime.now(timezone.utc)


def payload_sha(payload: dict) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _check_keys(payload, allowed: set, what: str):
    if not isinstance(payload, dict):
        raise AssistedValidationError("INVALID_PAYLOAD", f"a {what} must be a JSON object")
    extra = sorted(set(payload) - allowed)
    if extra:
        raise AssistedValidationError("UNKNOWN_FIELD", f"{what} fields not in the schema: {extra}")


def _prob(payload, key, *, required=False, open_unit=True):
    v = payload.get(key)
    if v is None:
        if required:
            raise AssistedValidationError("MISSING_FIELD", f"{key} is required")
        return None
    if isinstance(v, bool):
        raise AssistedValidationError("INVALID_FIELD", f"{key} must be a number")
    try:
        f = float(v)
    except (TypeError, ValueError):
        raise AssistedValidationError("INVALID_FIELD", f"{key} must be a number") from None
    if open_unit and not (0.0 < f < 1.0):
        raise AssistedValidationError("INVALID_FIELD", f"{key} must be strictly between 0 and 1 (got {f})")
    return f


def _text(payload, key, *, required=False):
    v = payload.get(key)
    if v is None or (isinstance(v, str) and not v.strip()):
        if required:
            raise AssistedValidationError("MISSING_FIELD", f"{key} is required")
        return None
    if not isinstance(v, str):
        raise AssistedValidationError("INVALID_FIELD", f"{key} must be text")
    if len(v) > MAX_TEXT:
        raise AssistedValidationError("INVALID_FIELD", f"{key} longer than {MAX_TEXT} characters")
    return v.strip()


def _text_list(payload, key):
    v = payload.get(key)
    if v is None:
        return []
    if isinstance(v, str):
        v = [v]
    if not isinstance(v, list) or not all(isinstance(x, str) and x.strip() for x in v):
        raise AssistedValidationError("INVALID_FIELD", f"{key} must be a list of non-empty strings")
    return [x.strip() for x in v]


def _ts(payload, key, *, default: datetime | None = None) -> datetime:
    v = payload.get(key)
    if v is None:
        if default is None:
            raise AssistedValidationError("MISSING_FIELD", f"{key} is required")
        return default
    try:
        t = datetime.fromisoformat(v.replace("Z", "+00:00")) if isinstance(v, str) else None
    except ValueError:
        t = None
    if t is None or t.tzinfo is None:
        raise AssistedValidationError("INVALID_TIMESTAMP", f"{key} must be an ISO-8601 timestamp WITH a UTC offset (got {v!r})")
    return t.astimezone(timezone.utc)


def _new_id(prefix: str, at: datetime, *parts) -> str:
    h = hashlib.sha256(json.dumps(parts, sort_keys=True, default=str).encode()).hexdigest()[:12]
    return f"{prefix}-{at.strftime('%Y%m%d')}-{h}"


def _given_id(payload, key, prefix):
    v = payload.get(key)
    if v is None:
        return None
    if not valid_record_id(v, prefix):
        raise AssistedValidationError("INVALID_ID", f"{key} must look like {prefix}-YYYYMMDD-<12 hex> (got {v!r})")
    return v


# ---------------------------------------------------------------------------------------------- decisions
def build_decision(payload: dict, *, store_root: str, data_root: str, slate_dir: str | None = None,
                   now: datetime | None = None, code_sha: str = "unknown") -> dict:
    """Validate one decision submission and return the full, immutable decision record."""
    now = now or _now()
    _check_keys(payload, DECISION_INPUT_KEYS, "decision")
    track = load_track_start(store_root)
    if not track or not track.get("_fingerprint_ok"):
        raise AssistedValidationError("TRACK_NOT_STARTED", "the assisted track has no valid TRACK_START record yet; "
                                      "the scheduled pipeline writes it on its first production run")
    decision = str(payload.get("decision") or "").upper()
    if decision not in DECISIONS:
        raise AssistedValidationError("INVALID_DECISION", f"decision must be one of {DECISIONS}")
    ticker = payload.get("ticker")
    if not valid_ticker(ticker):
        raise AssistedValidationError("INVALID_TICKER", f"not a Kalshi ticker: {ticker!r}")
    series = series_of(ticker)
    fam = SERIES.get(series, (None,))[0]
    if fam not in SUPPORTED_FAMILIES:
        raise AssistedValidationError("UNSUPPORTED_MARKET_FAMILY",
                                      f"{series} ({fam}) is not a supported match-scope Kalshi family")

    # ---- timing: prospective only
    created = _ts(payload, "created_at", default=now)
    if (created - now).total_seconds() > MAX_CLOCK_SKEW_S:
        raise AssistedValidationError("DECISION_IN_FUTURE", f"created_at {created.isoformat()} is after the recording time")
    if (now - created).total_seconds() > MAX_RECORDING_LAG_S:
        raise AssistedValidationError("RECORDED_TOO_LATE", f"decisions must be recorded within {MAX_RECORDING_LAG_S // 3600}h "
                                      "of being made; older decisions are reconstructions and are not admitted")
    start = iso(track.get("effective_start"))
    if start is None or created < start:
        raise AssistedValidationError("BEFORE_TRACK_START", f"created_at precedes the track's effective start {track.get('effective_start')}")

    side = payload.get("side")
    side = str(side).upper() if side is not None else None
    if decision in ("BET", "WATCH") and side not in SIDES:
        raise AssistedValidationError("MISSING_FIELD", f"side must be YES or NO for a {decision}")
    if side is not None and side not in SIDES:
        raise AssistedValidationError("INVALID_FIELD", "side must be YES or NO")

    # ---- market identity: it must exist on the capture or the slate, and still be open
    rec = quote_record_at(os.path.join(data_root, "kalshi", "capture"), ticker, created)
    slate = load_slate(slate_dir) if slate_dir else None
    smatch, srow = slate_market(slate, ticker)
    slate_age_h = None
    if slate and srow:
        slate_age_h = (created - iso(slate["built_at"])).total_seconds() / 3600
        if slate_age_h > SLATE_MAX_AGE_H or slate_age_h < -MAX_CLOCK_SKEW_S / 3600:
            smatch, srow = None, None                   # a slate from another day is not this decision's context
    if rec is None and srow is None:
        raise AssistedValidationError("MARKET_NOT_FOUND", f"{ticker} is not on the captured Kalshi board or the current slate")
    if rec is not None and rec.get("status") not in (None, "active"):
        raise AssistedValidationError("MARKET_NOT_OPEN", f"{ticker} status {rec.get('status')!r} at decision time")
    event = (rec or {}).get("event_ticker") or (srow or {}).get("event")
    if payload.get("event_id") and payload["event_id"] != event:
        raise AssistedValidationError("IDENTIFIER_MISMATCH", f"event_id {payload['event_id']!r} is not {ticker}'s event {event!r}")
    if match_code_of(event) != match_code_of(ticker):
        raise AssistedValidationError("IDENTIFIER_MISMATCH", f"{ticker} and its event {event} name different matches")
    pmid = payload.get("physical_match_id") or (smatch or {}).get("physical_match_id")
    if payload.get("physical_match_id"):
        if not valid_physical_match_id(payload["physical_match_id"]):
            raise AssistedValidationError("IDENTIFIER_MISMATCH", "physical_match_id must look like TOUR:pid:pid:YYYY-MM-DD")
        if smatch and smatch.get("physical_match_id") and smatch["physical_match_id"] != payload["physical_match_id"]:
            raise AssistedValidationError("IDENTIFIER_MISMATCH", f"physical_match_id {payload['physical_match_id']} "
                                          f"is not the slate's {smatch['physical_match_id']} for {ticker}")

    # ---- first ball: a decision after an observed first ball is in-play and refused
    truths = load_truths(os.path.join(data_root, "firstball", "store"))
    truth = truth_for(truths, event or ticker)
    bound = first_ball_bound(truth)
    warnings = []
    if bound is not None and bound <= created:
        raise AssistedValidationError("POST_START_DECISION", f"the first-ball store has {event or ticker} under way from "
                                      f"{bound.isoformat()} (confidence {truth.confidence}); created_at {created.isoformat()} "
                                      "is not a pregame decision")
    if bound is not None and bound <= now:
        warnings.append("RECORDED_AFTER_FIRST_BALL: made before the first ball but written after it; excluded from headline scoring")
    lb = (smatch or {}).get("level_bucket") or level_bucket(series)
    sched = (rec or {}).get("occurrence_datetime") or (smatch or {}).get("scheduled_start")
    sched_passed = bool(iso(sched) and iso(sched) <= created)
    if sched_passed:
        warnings.append("SCHEDULED_START_PASSED_AT_DECISION: no first ball observed, but the nominal start had passed")

    # ---- market price at decision time
    ib, ia = _prob(payload, "kalshi_bid"), _prob(payload, "kalshi_ask")
    cb, ca = (fnum((rec or {}).get("yes_bid_dollars"), open_unit=True), fnum((rec or {}).get("yes_ask_dollars"), open_unit=True))
    repo_q = None
    if rec is not None:
        repo_q = {"yes_bid": cb, "yes_ask": ca, "yes_bid_size": fnum(rec.get("yes_bid_size_fp")),
                  "yes_ask_size": fnum(rec.get("yes_ask_size_fp")), "captured_at": rec.get("captured_at"),
                  "age_seconds": round((created - iso(rec["captured_at"])).total_seconds(), 1) if iso(rec.get("captured_at")) else None,
                  "run_id": rec.get("run_id")}
    if (ib is None) != (ia is None):
        raise AssistedValidationError("INVALID_FIELD", "kalshi_bid and kalshi_ask must be given together")
    if ib is not None:
        if ib > ia:
            raise AssistedValidationError("INVALID_FIELD", "kalshi_bid above kalshi_ask")
        bid, ask, qsrc, qat, qage = ib, ia, "INPUT_OBSERVED_LIVE", created.isoformat(), 0.0
    elif cb is not None and ca is not None and cb <= ca:
        bid, ask, qsrc, qat, qage = cb, ca, "CAPTURE", rec.get("captured_at"), (repo_q or {}).get("age_seconds")
    else:
        bid = ask = qat = qage = None
        qsrc = "UNAVAILABLE"
    if decision == "BET" and ask is None:
        raise AssistedValidationError("MARKET_PRICE_UNAVAILABLE", "a BET needs a two-sided quote at decision time "
                                      "(pass kalshi_bid/kalshi_ask from the live book, or wait for the next capture)")
    if qage is not None and qage > STALE_QUOTE_S:
        warnings.append("MARKET_QUOTE_STALE: the capture quote used is over 30 minutes older than the decision")
    mid = 0.5 * (bid + ask) if bid is not None else None
    s_bid, s_ask = side_prices(side or "YES", bid, ask) if bid is not None else (None, None)
    size = _prob(payload, "displayed_size", open_unit=False)
    if size is None and repo_q:
        size = repo_q["yes_ask_size"] if (side or "YES") == "YES" else repo_q["yes_bid_size"]

    # ---- model and external context: what the handicapper was shown, else the repo slate
    sm = (srow or {}).get("model") or {}
    mc = (smatch or {}).get("model_context") or {}
    repo_model = {
        "gen1_probability": sm.get("gen1"), "gen2_probability": sm.get("gen2"),
        "model4_probability_if_applicable": sm.get("model4_conditioned"), "fair_v1_probability": sm.get("fair_v1"),
        "selector_state": sm.get("selector_v1"), "model_uncertainty": sm.get("model_uncertainty", mc.get("model_uncertainty")),
        "serve_evidence_player_a": (mc.get("serve_evidence") or {}).get("player_a_points"),
        "serve_evidence_player_b": (mc.get("serve_evidence") or {}).get("player_b_points"),
        "rating_state": mc.get("rating_state"), "surface_adjustment": mc.get("surface_adjustment"),
        "recent_form_inputs": mc.get("recent_form_inputs"),
        "additional_model_inputs": {k: v for k, v in {
            "player_a_win": mc.get("player_a_win"), "fair_v1_envelope": sm.get("fair_v1_envelope"),
            "model4_fundamental": sm.get("model4_fundamental"), "gen1_elo_only": sm.get("gen1_elo_only"),
            "gen1_structural": sm.get("gen1_structural"), "qualification_ok": sm.get("qualification_ok"),
            "data_quality": mc.get("data_quality"), "model_rows_predicted_at": mc.get("model_rows_predicted_at"),
            "observed_by": (srow or {}).get("observed_by"), "slate_market_warnings": (srow or {}).get("warnings"),
            "slate_match_warnings": (smatch or {}).get("warnings"),
            "frozen_rule_context": (smatch or {}).get("frozen_rule_context")}.items() if v is not None} or None,
    }
    model = {}
    from_input = []
    for k in MODEL_INPUT_KEYS:
        if k in payload:
            model[k] = payload[k]
            from_input.append(k)
        else:
            model[k] = repo_model.get(k)
    for k in ("gen1_probability", "gen2_probability", "model4_probability_if_applicable", "fair_v1_probability"):
        if k in from_input and model[k] is not None:
            model[k] = _prob(payload, k)
    if model["fair_v1_probability"] is not None:
        mp, msrc = model["fair_v1_probability"], "fair_v1"
    elif model["model4_probability_if_applicable"] is not None:
        mp, msrc = model["model4_probability_if_applicable"], "market_conditioned_v1"
    elif model["gen1_probability"] is not None:
        mp, msrc = model["gen1_probability"], "gen1_elo_dp_fair"
    elif model["gen2_probability"] is not None:
        mp, msrc = model["gen2_probability"], "gen2"
    else:
        mp, msrc = None, None
        warnings.append("NO_MODEL_PROBABILITY: the repository had no model number for this contract")
    se = (srow or {}).get("external") or {}
    repo_ext = {"bovada_probability_if_available": se.get("bovada"), "smarkets_probability_if_available": se.get("smarkets"),
                "external_consensus": se.get("consensus"), "triangulation_state": se.get("triangulation"),
                "external_freshness": {"external_quote_age_s": se.get("external_quote_age_s"), "scanned_at": se.get("scanned_at"),
                                       "reference_kind": se.get("reference_kind"),
                                       "n_independent_groups": se.get("n_independent_groups")} if se else None}
    ext, ext_in = {}, []
    for k in EXTERNAL_INPUT_KEYS:
        if k in payload:
            ext[k] = payload[k]
            ext_in.append(k)
        else:
            ext[k] = repo_ext.get(k)
    for k in ("bovada_probability_if_available", "smarkets_probability_if_available", "external_consensus"):
        if k in ext_in and ext[k] is not None:
            ext[k] = _prob(payload, k)

    # ---- handicapping
    p_gpt = _prob(payload, "chatgpt_fair_probability", required=decision in ("BET", "WATCH"))
    conf = payload.get("chatgpt_confidence")
    conf = str(conf).upper() if conf is not None else None
    if conf is None and decision == "BET":
        raise AssistedValidationError("MISSING_FIELD", "chatgpt_confidence is required for a BET")
    if conf is not None and conf not in CONFIDENCE:
        raise AssistedValidationError("INVALID_FIELD", f"chatgpt_confidence must be one of {CONFIDENCE}")
    thesis = _text(payload, "chatgpt_thesis", required=decision in ("BET", "WATCH"))
    pass_reason = _text(payload, "pass_reason_if_pass", required=decision == "PASS")
    tags = payload.get("factor_tags") or []
    if not isinstance(tags, list) or not all(isinstance(t, str) for t in tags):
        raise AssistedValidationError("INVALID_FACTOR_TAG", "factor_tags must be a list of tag strings")
    tags = [t.strip().upper() for t in tags]
    bad = [t for t in tags if t not in FACTOR_TAGS]
    if bad:
        raise AssistedValidationError("INVALID_FACTOR_TAG", f"unknown factor tags {bad}; allowed: {list(FACTOR_TAGS)}")
    if len(set(tags)) != len(tags):
        raise AssistedValidationError("INVALID_FACTOR_TAG", "factor tags repeat")

    # ---- expression
    fam_expr = expression_of_family(fam)
    chosen = payload.get("chosen_expression")
    chosen = str(chosen).upper() if chosen is not None else fam_expr
    if chosen not in MARKET_EXPRESSIONS:
        raise AssistedValidationError("EXPRESSION_MISMATCH", f"chosen_expression must be one of {MARKET_EXPRESSIONS}")
    if chosen != fam_expr:
        raise AssistedValidationError("EXPRESSION_MISMATCH", f"{ticker} is a {fam} contract ({fam_expr}), not {chosen}")
    avail = payload.get("available_expressions")
    if avail is None:
        avail = (smatch or {}).get("available_expressions") or [fam_expr]
    if not isinstance(avail, list) or any(str(a).upper() not in MARKET_EXPRESSIONS for a in avail):
        raise AssistedValidationError("EXPRESSION_MISMATCH", f"available_expressions must be drawn from {MARKET_EXPRESSIONS}")
    avail = sorted({str(a).upper() for a in avail} | {chosen})

    # ---- decision block
    rec_price = _prob(payload, "recommended_price")
    bu_p, bu_x = _prob(payload, "bet_up_to_probability"), _prob(payload, "bet_up_to_price")
    stake = _prob(payload, "stake_units_if_bet", open_unit=False)
    if decision == "BET":
        if bu_p is None and bu_x is None:
            raise AssistedValidationError("MISSING_FIELD", "a BET needs bet_up_to_price or bet_up_to_probability")
        if stake is None or not (0 < stake <= MAX_STAKE_UNITS):
            raise AssistedValidationError("INVALID_FIELD", f"a BET needs stake_units_if_bet in (0, {MAX_STAKE_UNITS}]")
        bu_x = bu_x if bu_x is not None else bu_p
        bu_p = bu_p if bu_p is not None else bu_x
        if rec_price is None:
            rec_price = s_ask
        if s_ask is not None and bu_x is not None and s_ask > bu_x + 1e-9:
            warnings.append("ENTRY_ABOVE_BET_UP_TO: the side's ask at decision exceeds its own bet-up-to price")
    elif stake not in (None, 0.0):
        raise AssistedValidationError("INVALID_FIELD", f"stake_units_if_bet applies to BET only (decision {decision})")
    actual = payload.get("actual_wagered", False)
    if not isinstance(actual, bool):
        raise AssistedValidationError("INVALID_FIELD", "actual_wagered must be true or false")

    # ---- model vs ChatGPT (Part 4), computed on the decision's own quote
    model_side = preferred_side(mp, bid, ask)
    if decision == "BET":
        gpt_side = side
    else:
        gpt_side = preferred_side(p_gpt, bid, ask) if p_gpt is not None else "NONE"
    agreement = classify_agreement(decision, model_side, gpt_side)
    material = abs(p_gpt - mid) >= MATERIAL_DISAGREEMENT if (p_gpt is not None and mid is not None) else None
    if slate is None or srow is None:
        warnings.append("NO_CURRENT_SLATE_ROW: model/external context not filled from a slate built within 13h")

    # ---- identity of the record
    pay_hash = payload_sha(payload)
    did = _given_id(payload, "decision_id", "AD") or _new_id("AD", created, pay_hash, created.isoformat())
    store = RecordStore(store_root)
    if store.exists("decisions", did):
        raise AssistedValidationError("DUPLICATE_ID", f"decision_id {did} already exists; decisions are never overwritten")
    thesis_key = canonical_hash([ticker, side, decision, p_gpt, thesis, pass_reason])
    for old in store.records("decisions"):
        o_created = iso(old.get("created_at"))
        if not o_created or abs((o_created - created).total_seconds()) > DUPLICATE_WINDOW_S:
            continue
        if canonical_hash([old.get("ticker"), old.get("side"), old.get("decision"), old.get("chatgpt_fair_probability"),
                           old.get("chatgpt_thesis"), old.get("pass_reason_if_pass")]) == thesis_key:
            raise AssistedValidationError("DUPLICATE_SUBMISSION", f"same decision already recorded as {old.get('decision_id')}")

    players = (smatch or {}).get("players")
    if not players:
        from tennis_edge.kalshi.markets import parse_market
        pm = parse_market(rec) if rec else None
        players = {"a": getattr(pm, "player_a", None), "b": getattr(pm, "player_b", None)}
    fee_side = taker_fee(s_ask, 1.0) if s_ask is not None else None
    out = {
        "decision_id": did, "schema_version": ASSISTED_SCHEMA_VERSION, "track": TRACK_NAME,
        "created_at": created.isoformat(), "recorded_at": now.isoformat(), "recorder_version": RECORDER_VERSION,
        "code_sha": code_sha, "slate_id": (slate or {}).get("slate_id") if srow else None,
        "slate_built_at": (slate or {}).get("built_at") if srow else None, "input_payload_sha256": pay_hash,
        "physical_match_id": pmid, "event_id": event, "match_code": match_code_of(ticker), "ticker": ticker,
        "series": series, "tour": (smatch or {}).get("tour") or SERIES[series][1],
        "level": (smatch or {}).get("level") or SERIES[series][2], "level_bucket": lb,
        "competition": (smatch or {}).get("competition"), "surface": (smatch or {}).get("surface"),
        "surface_bucket": (smatch or {}).get("surface_bucket") or surface_bucket(None, None),
        "players": players, "market_family": fam,
        "market_description": (srow or {}).get("description") or (rec or {}).get("title"),
        "side": side, "strike": payload.get("strike", (srow or {}).get("line")),
        "scheduled_start": sched,
        "first_ball_status_at_decision": "NOT_OBSERVED_STARTED" if lb in FIRST_BALL_COVERED else "NOT_OBSERVED_STARTED_NO_SOURCE",
        "first_ball_source_coverage": "COVERED" if lb in FIRST_BALL_COVERED else "NO_SOURCE",
        "scheduled_start_passed_at_decision": sched_passed,
        **model,
        "model_probability_yes": mp, "model_probability_source": msrc,
        "model_context_source": {"slate_id": (slate or {}).get("slate_id") if srow else None,
                                 "slate_age_hours": round(slate_age_h, 2) if (srow and slate_age_h is not None) else None,
                                 "fields_from_input": from_input},
        "kalshi_bid": bid, "kalshi_ask": ask, "kalshi_mid": mid,
        "kalshi_spread": round(ask - bid, 6) if bid is not None else None, "displayed_size": size,
        "fee": fee_side, "market_implied_probability": mid, "side_entry_price": s_ask, "side_fee": fee_side,
        "market_quote_source": qsrc, "market_quote_observed_at": qat, "market_quote_age_seconds": qage,
        "repo_market_at_decision": repo_q,
        **ext, "external_context_source": {"fields_from_input": ext_in, "from_slate": bool(se)},
        "chatgpt_fair_probability": p_gpt, "chatgpt_confidence": conf, "chatgpt_thesis": thesis,
        "key_supporting_factors": _text_list(payload, "key_supporting_factors"),
        "key_opposing_factors": _text_list(payload, "key_opposing_factors"), "factor_tags": tags,
        "model_agreement_state": agreement, "model_preferred_side": model_side, "chatgpt_preferred_side": gpt_side,
        "model_side_edges": side_edges(mp, bid, ask), "material_disagreement_with_kalshi": material,
        "market_disagreement_reason": _text(payload, "market_disagreement_reason"),
        "why_market_may_be_wrong": _text(payload, "why_market_may_be_wrong"),
        "why_model_may_be_wrong": _text(payload, "why_model_may_be_wrong"),
        "pass_reason_if_pass": pass_reason,
        "primary_match_thesis": _text(payload, "primary_match_thesis"), "available_expressions": avail,
        "chosen_expression": chosen,
        "why_chosen_expression_best_matches_thesis": _text(payload, "why_chosen_expression_best_matches_thesis"),
        "decision": decision, "recommended_price": rec_price, "bet_up_to_probability": bu_p,
        "bet_up_to_price": bu_x, "stake_units_if_bet": stake if decision == "BET" else None, "actual_wagered": actual,
        "authority": ASSISTED_AUTHORITY, "autonomous_real_money_authority": AUTONOMOUS_REAL_MONEY_AUTHORITY,
        "automated_execution": False, "warnings": warnings,
    }
    missing = [k for k in DECISION_FIELDS if k not in out]
    assert not missing, missing                       # the record always carries the whole schema
    return {k: out[k] for k in DECISION_FIELDS}


def record_decision(payload: dict, **kw) -> dict:
    rec = build_decision(payload, **kw)
    RecordStore(kw["store_root"]).write("decisions", rec)
    return rec


# ---------------------------------------------------------------------------------------------- wagers
def build_wager(payload: dict, *, store_root: str, data_root: str, now: datetime | None = None) -> dict:
    """Link a wager the person SAYS they placed to its decision. Never inferred from a recommendation."""
    now = now or _now()
    _check_keys(payload, WAGER_INPUT_KEYS, "wager")
    store = RecordStore(store_root)
    did = payload.get("decision_id")
    dec = store.get("decisions", did) if valid_record_id(did or "", "AD") else None
    if dec is None:
        raise AssistedValidationError("UNKNOWN_DECISION", f"no recorded decision {did!r}; record the decision first")
    ticker = payload.get("ticker", dec["ticker"])
    side = str(payload.get("side", dec.get("side") or "")).upper()
    if ticker != dec["ticker"] or side != dec.get("side"):
        raise AssistedValidationError("WAGER_MARKET_MISMATCH", f"wager on {ticker} {side} does not match decision "
                                      f"{did} ({dec['ticker']} {dec.get('side')}); record a decision for that market first")
    placed = _ts(payload, "placed_at")
    if (placed - now).total_seconds() > MAX_CLOCK_SKEW_S:
        raise AssistedValidationError("INVALID_TIMESTAMP", "placed_at is in the future")
    if placed < iso(dec["created_at"]) - timedelta(seconds=MAX_CLOCK_SKEW_S):
        raise AssistedValidationError("INVALID_TIMESTAMP", "a wager cannot be placed before the decision it implements")
    price = _prob(payload, "entry_price", required=True)
    contracts = _prob(payload, "contracts", required=True, open_unit=False)
    if contracts <= 0:
        raise AssistedValidationError("INVALID_FIELD", "contracts must be positive")
    stake = _prob(payload, "stake_dollars", open_unit=False)
    exp = price * contracts
    if stake is None:
        stake = round(exp, 2)
    elif abs(stake - exp) > max(0.02, 0.01 * exp):
        raise AssistedValidationError("STAKE_MISMATCH", f"stake_dollars {stake} != entry_price x contracts ({exp:.2f})")
    fees = _prob(payload, "fees", open_unit=False)
    if fees is None:
        fees = taker_fee(price, contracts)
    if fees < 0:
        raise AssistedValidationError("INVALID_FIELD", "fees cannot be negative")
    source = str(payload.get("source", "MANUAL_KALSHI_UI")).upper()
    status = str(payload.get("status", "FILLED")).upper()
    if source not in WAGER_SOURCES:
        raise AssistedValidationError("INVALID_FIELD", f"source must be one of {WAGER_SOURCES}")
    if status not in WAGER_STATUS:
        raise AssistedValidationError("INVALID_FIELD", f"status must be one of {WAGER_STATUS}")
    ext_id = payload.get("external_order_id")
    if ext_id is not None and (not isinstance(ext_id, str) or not ext_id.strip()):
        raise AssistedValidationError("INVALID_FIELD", "external_order_id must be text")
    truth = truth_for(load_truths(os.path.join(data_root, "firstball", "store")), dec.get("event_id") or ticker)
    bound = first_ball_bound(truth)
    after = bool(bound is not None and bound <= placed)
    pay_hash = payload_sha(payload)
    wid = _given_id(payload, "wager_id", "AW") or _new_id("AW", placed, pay_hash, did)
    if store.exists("wagers", wid):
        raise AssistedValidationError("DUPLICATE_ID", f"wager_id {wid} already exists")
    for old in store.records("wagers"):
        if ext_id and old.get("external_order_id") == ext_id:
            raise AssistedValidationError("DUPLICATE_SUBMISSION", f"external_order_id {ext_id} already linked as {old.get('wager_id')}")
        if (old.get("decision_id"), old.get("placed_at"), old.get("entry_price"), old.get("contracts")) == \
                (did, placed.isoformat(), price, contracts):
            raise AssistedValidationError("DUPLICATE_SUBMISSION", f"same wager already recorded as {old.get('wager_id')}")
    warnings = []
    if dec["decision"] != "BET":
        warnings.append(f"DECISION_WAS_{dec['decision']}: the person wagered on a decision recorded as {dec['decision']}")
    if after:
        warnings.append("PLACED_AFTER_FIRST_BALL: an in-play wager; counted in actual P&L, excluded from pregame CLV")
    out = {"wager_id": wid, "decision_id": did, "schema_version": ASSISTED_SCHEMA_VERSION, "recorded_at": now.isoformat(),
           "placed_at": placed.isoformat(), "ticker": ticker, "side": side, "entry_price": price, "contracts": contracts,
           "stake_dollars": stake, "fees": fees, "source": source, "status": status,
           "external_order_id": ext_id, "decision_was_bet": dec["decision"] == "BET", "placed_after_first_ball": after,
           "first_ball_status_at_placement": ("OBSERVED_STARTED" if after else "NOT_OBSERVED_STARTED"),
           "input_payload_sha256": pay_hash, "authority": ASSISTED_AUTHORITY, "warnings": warnings}
    return {k: out[k] for k in WAGER_FIELDS}


def record_wager(payload: dict, **kw) -> dict:
    rec = build_wager(payload, **kw)
    RecordStore(kw["store_root"]).write("wagers", rec)
    return rec


# ---------------------------------------------------------------------------------------------- postmortems
def build_postmortem(payload: dict, *, store_root: str, now: datetime | None = None) -> dict:
    """Part 12: hypothesis generation only. A postmortem changes no weight, threshold or rule."""
    now = now or _now()
    _check_keys(payload, POSTMORTEM_INPUT_KEYS, "postmortem")
    store = RecordStore(store_root)
    did = payload.get("decision_id")
    dec = store.get("decisions", did) if valid_record_id(did or "", "AD") else None
    if dec is None:
        raise AssistedValidationError("UNKNOWN_DECISION", f"no recorded decision {did!r}")
    result = str(payload.get("result") or "").upper()
    if result not in POSTMORTEM_RESULTS:
        raise AssistedValidationError("INVALID_FIELD", f"result must be one of {POSTMORTEM_RESULTS}")
    attr = payload.get("whether_loss_was_process_or_variance")
    attr = str(attr).upper() if attr is not None else None
    if attr is not None and attr not in LOSS_ATTRIBUTION:
        raise AssistedValidationError("INVALID_FIELD", f"whether_loss_was_process_or_variance must be one of {LOSS_ATTRIBUTION}")
    pay_hash = payload_sha(payload)
    pid = _given_id(payload, "postmortem_id", "AP") or _new_id("AP", now, pay_hash, did)
    if store.exists("postmortems", pid):
        raise AssistedValidationError("DUPLICATE_ID", f"postmortem_id {pid} already exists")
    out = {"postmortem_id": pid, "decision_id": did, "schema_version": ASSISTED_SCHEMA_VERSION,
           "recorded_at": now.isoformat(), "result": result,
           "what_thesis_got_right": _text(payload, "what_thesis_got_right"),
           "what_thesis_got_wrong": _text(payload, "what_thesis_got_wrong"),
           "whether_loss_was_process_or_variance": attr,
           "data_that_would_have_helped": _text(payload, "data_that_would_have_helped"),
           "potential_research_question": _text(payload, "potential_research_question"),
           "use_restriction": POSTMORTEM_USE_RESTRICTION, "input_payload_sha256": pay_hash}
    return {k: out[k] for k in POSTMORTEM_FIELDS}


def record_postmortem(payload: dict, **kw) -> dict:
    rec = build_postmortem(payload, **kw)
    RecordStore(kw["store_root"]).write("postmortems", rec)
    return rec


def build_evidence(payload: dict, *, store_root: str, now: datetime | None = None) -> dict:
    """New evidence discovered AFTER a decision. Appended beside it; the decision itself never changes."""
    now = now or _now()
    _check_keys(payload, EVIDENCE_INPUT_KEYS, "evidence")
    store = RecordStore(store_root)
    did = payload.get("decision_id")
    dec = store.get("decisions", did) if valid_record_id(did or "", "AD") else None
    if dec is None:
        raise AssistedValidationError("UNKNOWN_DECISION", f"no recorded decision {did!r}")
    disc = _ts(payload, "discovered_at", default=now)
    if disc < iso(dec["created_at"]):
        raise AssistedValidationError("INVALID_TIMESTAMP", "evidence discovered before the decision belongs in the decision, "
                                      "and a recorded decision is never edited")
    pay_hash = payload_sha(payload)
    eid = _given_id(payload, "evidence_id", "AE") or _new_id("AE", now, pay_hash, did)
    if store.exists("evidence", eid):
        raise AssistedValidationError("DUPLICATE_ID", f"evidence_id {eid} already exists")
    out = {"evidence_id": eid, "decision_id": did, "schema_version": ASSISTED_SCHEMA_VERSION,
           "recorded_at": now.isoformat(), "discovered_at": disc.isoformat(),
           "evidence": _text(payload, "evidence", required=True), "source": _text(payload, "source"),
           "bears_on": _text_list(payload, "bears_on"), "input_payload_sha256": pay_hash}
    return {k: out[k] for k in EVIDENCE_FIELDS}


def record_evidence(payload: dict, **kw) -> dict:
    rec = build_evidence(payload, **kw)
    RecordStore(kw["store_root"]).write("evidence", rec)
    return rec
