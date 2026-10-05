"""Append-only quarantine register for ledger rows that were priced after the first ball.

Why
---
Between 2026-09-12 and 2026-09-27, 330 ledger rows (mostly WTA 125 / Challenger) were priced after the match
had started, because Kalshi's nominal start for those series is hours late. The guard that prevents it
(`run_tennis.py` refuses any match the first-ball store has seen start) was committed 2026-09-27T20:02Z; no
violation has been generated since. The rows themselves are evidence and are never edited or deleted.

What this does
--------------
It records each such row, by prediction_id, in `data/research/quarantine/post_start_ledger_rows.jsonl`
with the first-ball bounds that convict it. A row may be registered ONLY if it was generated before
`GUARD_DEPLOYED_AT`; anything generated later is an ACTIVE leak and cannot be quarantined by this module,
so TENNIS-6 keeps failing until the pipeline is fixed. Every record carries a sha256 of its own content and
of the previous record (a hash chain), so a silent edit or deletion is detectable.

Quarantined rows are ineligible for strict research: strict CLV already requires the STRICT_PREGAME timing
class, and TENNIS-6 independently checks that no post-start row is used as strict evidence.
"""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone

GUARD_DEPLOYED_AT = datetime(2026, 9, 27, 20, 2, 23, tzinfo=timezone.utc)
REGISTER = "post_start_ledger_rows.jsonl"

#: Second class (found 2026-10-05): priced AFTER THE EXCHANGE HAD SETTLED the market -- certain post-start, even
#: with no first-ball source (ITF). Legacy iff the row was produced by a code version that lacked the lifecycle
#: guard; the frozen list is config/pre_lifecycle_guard_shas.json. Code from any later commit cannot be quarantined.
_PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def pre_lifecycle_guard_shas() -> set:
    p = os.path.join(_PROJ, "config", "pre_lifecycle_guard_shas.json")
    return set(json.load(open(p))["shas"]) if os.path.exists(p) else set()


def is_legacy(entry: dict, legacy_shas: set | None = None) -> bool:
    if entry.get("class") == "post_settlement":
        shas = legacy_shas if legacy_shas is not None else pre_lifecycle_guard_shas()
        return entry.get("git_sha") in shas
    return datetime.fromisoformat(entry["generated_at_utc"]) < GUARD_DEPLOYED_AT


def _h(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()


def load(root: str) -> tuple[dict, list]:
    """(prediction_id -> record, chain problems)."""
    path = os.path.join(root, REGISTER)
    out, problems, prev = {}, [], None
    if not os.path.exists(path):
        return out, problems
    for i, line in enumerate(open(path)):
        rec = json.loads(line)
        body = {k: v for k, v in rec.items() if k not in ("record_sha256",)}
        if rec.get("prev_sha256") != prev:
            problems.append(f"line {i + 1}: broken chain")
        if _h(body) != rec.get("record_sha256"):
            problems.append(f"line {i + 1}: record hash mismatch")
        prev = rec.get("record_sha256")
        out[rec["prediction_id"]] = rec
    return out, problems


def legacy_violations(ledger_rows, starts: dict, settled_at: dict | None = None, legacy_shas: set | None = None) -> list[dict]:
    """Rows priced at/after the earliest possible first ball AND generated before the guard existed, plus rows
    priced after the exchange's own settlement time by a pre-lifecycle-guard code version."""
    out = []
    legacy_shas = legacy_shas if legacy_shas is not None else pre_lifecycle_guard_shas()
    fb_ids = set()
    for r in ledger_rows:
        st = starts.get(r["match_id"], (None, None))
        afb = st[0]
        if afb is None:
            continue
        gen = datetime.fromisoformat(r["generated_at_utc"])
        if gen >= afb and gen < GUARD_DEPLOYED_AT:
            upper = st[2] if len(st) > 2 else None
            out.append({"prediction_id": r["prediction_id"], "match_id": r["match_id"], "ticker": r.get("ticker"),
                        "series_ticker": r.get("series_ticker"), "generated_at_utc": r["generated_at_utc"],
                        "first_ball_lower_utc": str(afb), "first_ball_upper_utc": str(upper) if upper else None,
                        "class": "post_start_confirmed" if (upper is None or gen >= upper) else "inside_first_ball_bracket"})
            fb_ids.add(r["prediction_id"])
    for r in ledger_rows:
        ts = (settled_at or {}).get(r["prediction_id"])
        if not ts or r["prediction_id"] in fb_ids:
            continue
        gen = datetime.fromisoformat(r["generated_at_utc"])
        if gen > ts and r.get("git_sha") in legacy_shas:
            out.append({"prediction_id": r["prediction_id"], "match_id": r["match_id"], "ticker": r.get("ticker"),
                        "series_ticker": r.get("series_ticker"), "generated_at_utc": r["generated_at_utc"],
                        "exchange_settled_at_utc": ts.isoformat(), "git_sha": r.get("git_sha"), "class": "post_settlement"})
    return out


def append(root: str, entries: list[dict], now: datetime | None = None) -> int:
    """Append entries not already registered. Refuses any row generated at/after the guard."""
    os.makedirs(root, exist_ok=True)
    have, problems = load(root)
    if problems:
        raise RuntimeError(f"quarantine register integrity: {problems[:3]}")
    path = os.path.join(root, REGISTER)
    prev = None
    if os.path.exists(path):
        lines = open(path).read().splitlines()
        prev = json.loads(lines[-1])["record_sha256"] if lines else None
    n = 0
    now = (now or datetime.now(timezone.utc)).isoformat()
    with open(path, "a") as f:
        for e in sorted(entries, key=lambda x: (x["generated_at_utc"], x["prediction_id"])):
            if e["prediction_id"] in have:
                continue
            if not is_legacy(e):
                raise ValueError(f"{e['prediction_id']} was produced after its guard existed: an ACTIVE leak cannot be quarantined")
            reason = ("priced after the exchange had settled the market (legacy code without the lifecycle guard)"
                      if e.get("class") == "post_settlement" else "priced after the actual first ball (legacy; pre-guard)")
            body = {**e, "quarantined_at": now, "reason": reason,
                    "strict_research_eligible": False, "prev_sha256": prev}
            rec = {**body, "record_sha256": _h(body)}
            f.write(json.dumps(rec, sort_keys=True, default=str) + "\n")
            prev = rec["record_sha256"]
            have[e["prediction_id"]] = rec
            n += 1
    return n
