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
from .schema import (AGREEMENT_STATES, DECISION_FIELDS, DECISIONS, FACTOR_TAGS, MARKET_EXPRESSIONS,
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
    missing = [k for k in DECISION_FIELDS if k not in d]
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
