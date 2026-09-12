"""Exactly one state for every active Kalshi tennis contract. No silent omission.

The projection run already records WHY each market was not priced, but it records it in the vocabulary
of the pipeline stage that rejected it ("identity", "scope", "pregame"). That is the wrong vocabulary for
a coverage question, because two very different problems -- "we have no draw feed" and "we cannot tell
which player this is" -- both read as "excluded". This module maps those stages onto the states that
actually describe the board, and computes two different coverage numbers, because they answer two
different questions:

  COVERAGE A  priced / every active contract.
              Honest but pessimistic: it counts contracts nothing could price today, such as tournament
              winners with no draw feed and in-play game markets.

  COVERAGE B  priced / contracts that SHOULD be priceable with the inputs we actually have.
              The denominator excludes contracts blocked by a missing capability rather than a missing
              value: unknown contract semantics, unsupported families, tournament scope with no draw.
              This is the number that measures the pipeline rather than the roadmap.

Neither number is allowed to improve by dropping a contract from the accounting.
"""
from __future__ import annotations

PROJECTED = "PROJECTED"
UNSUPPORTED_FAMILY = "UNSUPPORTED_FAMILY"
UNMAPPED_IDENTITY = "UNMAPPED_IDENTITY"
NO_DRAW = "NO_DRAW"
NO_FIRST_BALL_SOURCE = "NO_FIRST_BALL_SOURCE"
INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
UNKNOWN_CONTRACT = "UNKNOWN_CONTRACT"
OTHER_EXPLICIT_FAIL_CLOSED = "OTHER_EXPLICIT_FAIL_CLOSED"
CLOSED_SINCE_DISCOVERY = "CLOSED_SINCE_DISCOVERY"      # not an active contract; kept out of both ratios

BOARD_STATES = (PROJECTED, UNSUPPORTED_FAMILY, UNMAPPED_IDENTITY, NO_DRAW, NO_FIRST_BALL_SOURCE,
                INSUFFICIENT_DATA, UNKNOWN_CONTRACT, OTHER_EXPLICIT_FAIL_CLOSED, CLOSED_SINCE_DISCOVERY)

#: states whose cause is a missing CAPABILITY (a feed or a model we have not built), not a missing value
#: for this particular contract. Excluded from coverage B's denominator, never from the accounting.
CAPABILITY_BLOCKED = (UNSUPPORTED_FAMILY, NO_DRAW, UNKNOWN_CONTRACT)

_STAGE_TO_STATE = {
    "lifecycle": CLOSED_SINCE_DISCOVERY,
    "parse": UNKNOWN_CONTRACT,
    "family": UNSUPPORTED_FAMILY,
    "scope": NO_DRAW,
    "identity": UNMAPPED_IDENTITY,
    "event": UNMAPPED_IDENTITY,
    "pregame": NO_FIRST_BALL_SOURCE,
    "doubles": INSUFFICIENT_DATA,
    "format": OTHER_EXPLICIT_FAIL_CLOSED,
    "pricing": OTHER_EXPLICIT_FAIL_CLOSED,
}


#: reason fragments that identify an identity failure whatever stage reported it. A doubles event
#: rejected because a partner's surname does not resolve is an IDENTITY problem, not a data-volume one,
#: and filing it under INSUFFICIENT_DATA would point future work at the wrong thing.
_IDENTITY_MARKERS = ("unmapped", "ambiguous", "no exact full-name match", "could not recover")


def classify_exclusion(stage: str | None, reason: str = "") -> str:
    """Map one projection-run exclusion onto a board state. Unknown stages fail closed, loudly."""
    low = (reason or "").lower()
    st = _STAGE_TO_STATE.get((stage or "").strip().lower())
    if st in (INSUFFICIENT_DATA, OTHER_EXPLICIT_FAIL_CLOSED) and any(k in low for k in _IDENTITY_MARKERS):
        return UNMAPPED_IDENTITY
    if st is not None:
        return st
    return OTHER_EXPLICIT_FAIL_CLOSED


def board_accounting(projection: dict) -> dict:
    """Full accounting from one projection artifact (data/research/projections/<run>.json)."""
    priced = list(projection.get("projected_tickers") or [])
    rows = {t: {"ticker": t, "state": PROJECTED, "reason": ""} for t in priced}
    for e in projection.get("excluded") or []:
        t = e.get("ticker")
        if not t or t in rows:
            continue
        rows[t] = {"ticker": t, "state": classify_exclusion(e.get("stage"), e.get("reason", "")),
                   "reason": (e.get("reason") or "")[:200], "stage": e.get("stage")}
    counts: dict[str, int] = {}
    for r in rows.values():
        counts[r["state"]] = counts.get(r["state"], 0) + 1

    active = [r for r in rows.values() if r["state"] != CLOSED_SINCE_DISCOVERY]
    n_active = len(active)
    n_priced = counts.get(PROJECTED, 0)
    should = [r for r in active if r["state"] not in CAPABILITY_BLOCKED]
    n_should = len(should)
    return {
        "contracts_seen": len(rows),
        "active": n_active,
        "closed_since_discovery": counts.get(CLOSED_SINCE_DISCOVERY, 0),
        "projected": n_priced,
        "coverage_a_all_active": round(n_priced / n_active, 4) if n_active else None,
        "coverage_b_should_be_priceable": round(n_priced / n_should, 4) if n_should else None,
        "coverage_b_denominator": n_should,
        "states": counts,
        "capability_blocked": {k: counts.get(k, 0) for k in CAPABILITY_BLOCKED},
        "unaccounted": 0,
        "rows": list(rows.values()),
    }


def check_total(accounting: dict) -> list[str]:
    """Every contract must carry exactly one state, and the states must sum to the total."""
    v = []
    total = sum(accounting["states"].values())
    if total != accounting["contracts_seen"]:
        v.append(f"state counts sum to {total} but {accounting['contracts_seen']} contracts were seen")
    unknown = [s for s in accounting["states"] if s not in BOARD_STATES]
    if unknown:
        v.append(f"unknown states: {unknown}")
    dupes = len(accounting["rows"]) - len({r["ticker"] for r in accounting["rows"]})
    if dupes:
        v.append(f"{dupes} contracts carry more than one state")
    return v
