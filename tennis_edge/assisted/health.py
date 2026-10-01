"""TENNIS-16: assisted decision pipeline health. An OPERATIONS gate, never a profitability gate.

It answers "is the assisted lane recording, settling and scoring correctly?", not "is it making money?".
Zero decisions is healthy. What fails: no fresh slate, a stalled settle/score pipeline, a record whose
fingerprint broke, a malformed or duplicated decision, a decision the first-ball store shows was made after
the match started (recent ones; older ones stay listed), a decision left unsettled long after its market.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone

from . import AUTONOMOUS_REAL_MONEY_AUTHORITY, CHATGPT_ASSISTED_TRACK
from .market import first_ball_bound, iso, load_truths, truth_for
from .schema import (AGREEMENT_STATES, DECISION_FIELDS, DECISION_FIELDS_BY_VERSION, DECISIONS, FACTOR_TAGS, MARKET_EXPRESSIONS,
                     valid_record_id, valid_ticker)
from .settle import latest_settlements
from .store import CANONICAL, AppendOnlyJsonl, RecordStore, canonical_hash, load_track_start

PIPELINE_STATUS_FILE = "PIPELINE_STATUS.json"
MAX_SLATE_AGE_H = 13.0
MAX_PIPELINE_AGE_H = 13.0
UNSETTLED_STALL_DAYS = 7
RECENT_VIOLATION_DAYS = 7


def schema_problems(d: dict) -> list[str]:
    p = []
    missing = [k for k in DECISION_FIELDS_BY_VERSION.get(d.get("schema_version"), DECISION_FIELDS) if k not in d]
    if missing:
        p.append(f"missing fields {missing[:5]}")
    if not valid_record_id(d.get("decision_id") or "", "AD"):
        p.append("bad decision_id")
    if d.get("decision") not in DECISIONS:
        p.append("bad decision")
    if not valid_ticker(d.get("ticker")):
        p.append("bad ticker")
    if d.get("chosen_expression") not in MARKET_EXPRESSIONS:
        p.append("bad chosen_expression")
    if d.get("model_agreement_state") not in AGREEMENT_STATES:
        p.append("bad model_agreement_state")
    if any(t not in FACTOR_TAGS for t in d.get("factor_tags") or []):
        p.append("bad factor tag")
    if d.get("automated_execution") is not False or d.get("autonomous_real_money_authority") != "OFF":
        p.append("authority fields altered")
    return p


def gate_16(research_root: str, *, firstball_root: str | None = None, now: datetime | None = None) -> tuple[str, dict]:
    now = now or datetime.now(timezone.utc)
    root = os.path.join(research_root, "assisted_decisions")
    slate_runs = os.path.join(research_root, "assisted_slates", "slate_runs.jsonl")
    track = load_track_start(root)
    last_slate = None
    if os.path.exists(slate_runs):
        for line in open(slate_runs):
            try:
                last_slate = json.loads(line)
            except ValueError:
                continue
    try:
        status_doc = json.load(open(os.path.join(root, PIPELINE_STATUS_FILE)))
    except (OSError, ValueError):
        status_doc = {}
    detail = {"AUTONOMOUS_REAL_MONEY_AUTHORITY": AUTONOMOUS_REAL_MONEY_AUTHORITY,
              "CHATGPT_ASSISTED_TRACK": CHATGPT_ASSISTED_TRACK,
              "gate_kind": "OPERATIONS (not profitability)",
              "track_effective_start": (track or {}).get("effective_start"),
              "track_start_fingerprint_ok": (track or {}).get("_fingerprint_ok")}
    if track is None or last_slate is None:
        detail["reason"] = "the assisted pipeline has not run in production yet (no TRACK_START or no slate build)"
        return "UNKNOWN", detail

    store = RecordStore(root)
    decisions = store.records("decisions")
    wagers = store.records("wagers")
    sets = latest_settlements(root)
    truths = load_truths(firstball_root) if firstball_root else {}
    slate_age = (now - iso(last_slate["built_at"])).total_seconds() / 3600 if iso(last_slate.get("built_at")) else None
    pipe_at = iso(status_doc.get("last_run_at"))
    pipe_age = (now - pipe_at).total_seconds() / 3600 if pipe_at else None

    integrity = [d.get("_path") for d in decisions + wagers if not d.get("_fingerprint_ok")]
    integrity += list(status_doc.get("integrity_violations") or [])
    for kind, fn in CANONICAL.items():
        integrity += AppendOnlyJsonl(os.path.join(root, fn)).verify_chain()
    integrity += AppendOnlyJsonl(os.path.join(root, "assisted_settlements.jsonl")).verify_chain()
    schema_bad = {d.get("decision_id") or d.get("_path"): schema_problems(d) for d in decisions if schema_problems(d)}
    ids = [d.get("decision_id") for d in decisions]
    dup_ids = sorted({i for i in ids if ids.count(i) > 1})
    keys = {}
    dup_content = []
    for d in decisions:
        k = canonical_hash([d.get("ticker"), d.get("side"), d.get("decision"), d.get("chatgpt_fair_probability"),
                            d.get("chatgpt_thesis"), d.get("pass_reason_if_pass")])
        if k in keys:
            dup_content.append([keys[k], d.get("decision_id")])
        keys[k] = d.get("decision_id")
    violations = []
    for d in decisions:
        created = iso(d.get("created_at"))
        t = truth_for(truths, d.get("event_id") or d.get("ticker") or "")
        b = first_ball_bound(t)
        s = sets.get(("DECISION", d.get("decision_id"), None)) or {}
        if (b is not None and created is not None and b <= created) or s.get("post_start_violation"):
            violations.append({"decision_id": d.get("decision_id"), "created_at": d.get("created_at"),
                               "first_ball_bound": b.isoformat() if b else s.get("first_ball_lower_utc")})
    recent_viol = [v for v in violations if iso(v["created_at"]) and now - iso(v["created_at"]) <= timedelta(days=RECENT_VIOLATION_DAYS)]
    unsettled = [d for d in decisions if ("DECISION", d.get("decision_id"), None) not in sets]
    stalled = [d.get("decision_id") for d in unsettled
               if iso(d.get("created_at")) and now - iso(d["created_at"]) > timedelta(days=UNSETTLED_STALL_DAYS)]
    settled_sided = [s for (kind, _d, _w), s in sets.items() if kind == "DECISION" and s.get("side") in ("YES", "NO")]
    strict_n = sum(1 for s in settled_sided if s.get("strict_executable_clv") is not None)
    last_dec = max((d.get("recorded_at") or "" for d in decisions), default=None)
    last_settle = max((s.get("settled_at") or "" for s in sets.values()), default=None)
    detail.update({
        "latest_slate_build": last_slate.get("built_at"), "latest_slate_id": last_slate.get("slate_id"),
        "slate_age_h": round(slate_age, 2) if slate_age is not None else None,
        "latest_slate_matches": last_slate.get("matches"),
        "latest_assisted_decision": last_dec or None, "decisions": len(decisions), "wagers": len(wagers),
        "pipeline_last_run_at": status_doc.get("last_run_at"),
        "pipeline_age_h": round(pipe_age, 2) if pipe_age is not None else None,
        "settlement_freshness": {"last_settlement_row_at": last_settle or None, "pipeline_last_run_at": status_doc.get("last_run_at")},
        "unsettled_decisions": len(unsettled), "unsettled_stalled_over_7d": stalled,
        "strict_clv_coverage": {"settled_with_side": len(settled_sided), "with_strict_clv": strict_n,
                                "rate": round(strict_n / len(settled_sided), 3) if settled_sided else None,
                                "note": "Challenger/ITF have no first-ball source, so strict CLV there is structurally absent"},
        "schema_validity": {"invalid": schema_bad, "valid": len(decisions) - len(schema_bad)},
        "duplicate_decisions": {"ids": dup_ids, "content": dup_content},
        "post_start_decision_violations": {"total": len(violations), f"last_{RECENT_VIOLATION_DAYS}d": len(recent_viol),
                                           "rows": violations[:20]},
        "integrity_violations": integrity[:20],
    })
    fails = []
    if slate_age is None or slate_age > MAX_SLATE_AGE_H:
        fails.append("SLATE_STALE")
    if pipe_age is None or pipe_age > MAX_PIPELINE_AGE_H:
        fails.append("PIPELINE_STALE")
    err_at = iso(status_doc.get("last_error_at"))
    if err_at is not None and (pipe_at is None or err_at > pipe_at):
        fails.append("PIPELINE_ERROR")
        detail["pipeline_last_error"] = (status_doc.get("last_error") or "")[-400:]
    if integrity:
        fails.append("INTEGRITY_VIOLATION")
    if schema_bad:
        fails.append("SCHEMA_INVALID")
    if dup_ids or dup_content:
        fails.append("DUPLICATE_DECISIONS")
    if recent_viol:
        fails.append("POST_START_DECISIONS")
    if stalled:
        fails.append("SETTLEMENT_STALLED")
    if not (track or {}).get("_fingerprint_ok"):
        fails.append("TRACK_START_MODIFIED")
    detail["failing"] = fails
    detail["health"] = "HEALTHY_NO_DECISIONS_YET" if (not fails and not decisions) else ("HEALTHY" if not fails else "UNHEALTHY")
    return ("FAIL" if fails else "PASS"), detail


# ---------------------------------------------------------------------------------------------- TENNIS-17
_SANITY_FIELDS = ("model_market_gap_pp", "discrepancy_band", "discrepancy_sanity_status", "discrepancy_reason_tags",
                  "identity_check_status", "market_freshness_status", "external_confirmation_status",
                  "data_quality_status")


def _probs_of_row(r: dict) -> dict:
    mo = r.get("model") or {}
    out = {"model_probability_yes": r.get("model_probability_yes"), "kalshi_mid": (r.get("kalshi") or {}).get("mid")}
    for k in ("gen1", "gen2", "fair_v1", "model4_conditioned", "model4_fundamental", "gen1_elo_only", "gen1_structural"):
        out[k] = mo.get(k)
    return out


def gate_17(research_root: str, *, now: datetime | None = None) -> tuple[str, dict]:
    """TENNIS-17 model_market_discrepancy_integrity: is every model-market disagreement on the assisted slate
    (and on every recorded decision) classified, and does no extreme one escape the sanity layer?

    An INTEGRITY gate, not a profitability gate: a disagreement alone never fails it. It FAILS on
      SLATE_LACKS_DISCREPANCY_CLASSIFICATION  the slate predates the layer or a priced row has no classification
      BAND_MISMATCH                           a row's band is not the band of its own model-minus-mid gap (bypass)
      MALFORMED_PROBABILITY                   a model or market probability outside [0, 1] / not a number
      TICKER_ORIENTATION_MISMATCH             a contract whose YES side contradicts our player A/B orientation
      EXTREME_UNRESOLVED_IDENTITY             an EXTREME gap with ambiguous/failed identity not held at DATA_WARNING
      EXTREME_STALE_PRICE_ACTIONABLE          an EXTREME gap on a STALE quote not held at DATA_WARNING
      EXTREME_BYPASS                          an EXTREME gap surfaced as anything but DATA_WARNING on the slate, or a
                                              recorded BET on one that is not ELIGIBLE with all nine conditions met
      HIGH_REVIEW_BYPASS                      a HIGH_REVIEW gap surfaced without the explanation requirement, or a
                                              recorded BET on one with no discrepancy_explanation
    """
    from . import discrepancy as DS
    from .slate import load_slate
    now = now or datetime.now(timezone.utc)
    slate = load_slate(os.path.join(research_root, "assisted_slates"))
    detail = {"gate_kind": "INTEGRITY (not profitability; model-market disagreement alone never fails this gate)",
              "AUTONOMOUS_REAL_MONEY_AUTHORITY": AUTONOMOUS_REAL_MONEY_AUTHORITY,
              "CHATGPT_ASSISTED_TRACK": CHATGPT_ASSISTED_TRACK}
    if slate is None:
        detail["reason"] = "no assisted slate on disk yet"
        return "UNKNOWN", detail
    fails: dict[str, list] = {}

    def fail(code, item):
        fails.setdefault(code, []).append(item)

    ds = slate.get("discrepancy_sanity")
    detail.update({"slate_id": slate.get("slate_id"), "slate_built_at": slate.get("built_at"),
                   "discrepancy_version": (ds or {}).get("version")})
    if not ds:
        fail("SLATE_LACKS_DISCREPANCY_CLASSIFICATION", "slate has no discrepancy_sanity section (built before the layer)")
    rows = [(x, r) for x in slate.get("matches") or [] for r in x.get("markets") or []]
    bands, statuses, fresh, ident, orient = {}, {}, {}, {}, {}
    extreme = []
    for x, r in rows:
        t = r.get("ticker")
        probs = _probs_of_row(r)
        bad = [k for k, v in probs.items() if v is not None and not DS.valid_probability(v)]
        if bad:
            fail("MALFORMED_PROBABILITY", {"ticker": t, "fields": bad})
        p, mid = probs["model_probability_yes"], probs["kalshi_mid"]
        modeled = DS.valid_probability(p) and DS.valid_probability(mid)
        if not modeled:
            continue
        missing = [f for f in _SANITY_FIELDS if f not in r]
        if missing or r.get("discrepancy_sanity_status") not in DS.SANITY_STATUSES:
            fail("SLATE_LACKS_DISCREPANCY_CLASSIFICATION", {"ticker": t, "missing": missing})
            continue
        k = r.get("kalshi") or {}
        if DS.valid_probability(k.get("bid")) and DS.valid_probability(k.get("ask")) and k["bid"] <= k["ask"]:
            mid = 0.5 * (k["bid"] + k["ask"])                 # the layer's own arithmetic, not the rounded display mid
        expect = DS.band_of(DS.gap_pp(p, mid))
        band, status = r["discrepancy_band"], r["discrepancy_sanity_status"]
        if band != expect:
            fail("BAND_MISMATCH", {"ticker": t, "band": band, "expected": expect})
        o = r.get("ticker_orientation_status") or (r.get("discrepancy") or {}).get("ticker_orientation_status")
        if o == "FAILED":
            fail("TICKER_ORIENTATION_MISMATCH", {"ticker": t, "subject": r.get("subject")})
        for d, k in ((bands, expect), (statuses, status), (fresh, r["market_freshness_status"]),
                     (ident, r["identity_check_status"]), (orient, o)):
            d[k] = d.get(k, 0) + 1
        if expect == DS.EXTREME:
            extreme.append({"ticker": t, "level_bucket": x.get("level_bucket"), "gap_pp": r["model_market_gap_pp"],
                            "status": status, "identity": r["identity_check_status"],
                            "freshness": r["market_freshness_status"], "external": r["external_confirmation_status"],
                            "data_quality": r["data_quality_status"], "reasons": r["discrepancy_reason_tags"]})
            if status != DS.DATA_WARNING:
                fail("EXTREME_BYPASS", {"ticker": t, "status": status})
                if r["identity_check_status"] != DS.ID_VERIFIED:
                    fail("EXTREME_UNRESOLVED_IDENTITY", {"ticker": t, "identity": r["identity_check_status"]})
                if r["market_freshness_status"] == DS.STALE:
                    fail("EXTREME_STALE_PRICE_ACTIONABLE", {"ticker": t})
        elif expect == DS.HIGH_REVIEW and status not in (DS.EXPLANATION_REQUIRED, DS.DATA_WARNING):
            fail("HIGH_REVIEW_BYPASS", {"ticker": t, "status": status})

    # ---- recorded decisions (schema v2 carries the layer; v1 predates it and no v1 decision exists)
    decisions = RecordStore(os.path.join(research_root, "assisted_decisions")).records("decisions")
    n_v2 = 0
    for d in decisions:
        if d.get("schema_version", 1) < 2:
            continue
        n_v2 += 1
        did = d.get("decision_id")
        bad = [k for k in ("model_probability_yes", "gen1_probability", "gen2_probability", "fair_v1_probability",
                           "model4_probability_if_applicable", "chatgpt_fair_probability", "kalshi_mid")
               if d.get(k) is not None and not DS.valid_probability(d.get(k))]
        if bad:
            fail("MALFORMED_PROBABILITY", {"decision_id": did, "fields": bad})
        band = d.get("discrepancy_band")
        if band is None or d.get("discrepancy_sanity_status") not in DS.SANITY_STATUSES:
            fail("SLATE_LACKS_DISCREPANCY_CLASSIFICATION", {"decision_id": did})
            continue
        if d.get("ticker_orientation_status") == "FAILED" and d.get("decision") == "BET":
            fail("TICKER_ORIENTATION_MISMATCH", {"decision_id": did})
        if d.get("decision") != "BET":
            continue
        conds = d.get("discrepancy_conditions") or {}
        if band == DS.EXTREME and not (d.get("discrepancy_sanity_status") == DS.ELIGIBLE and conds.get("all_met")
                                       and d.get("discrepancy_explanation")):
            fail("EXTREME_BYPASS", {"decision_id": did, "status": d.get("discrepancy_sanity_status")})
        if band == DS.HIGH_REVIEW and not d.get("discrepancy_explanation"):
            fail("HIGH_REVIEW_BYPASS", {"decision_id": did})
    detail.update({
        "priced_rows": sum(bands.values()), "counts_by_band": bands, "counts_by_status": statuses,
        "counts_by_freshness": fresh, "counts_by_identity": ident, "counts_by_orientation": orient,
        "extreme_rows": len(extreme), "extreme_sample": extreme[:20], "decisions_checked_v2": n_v2,
        "failures": {k: v[:10] for k, v in fails.items()}, "failing": sorted(fails),
        "note": ("EXTREME rows held at DATA_WARNING with ambiguous identity or stale quotes are the layer WORKING; "
                 "the gate fails only when such a row escapes it"),
    })
    return ("FAIL" if fails else "PASS"), detail
