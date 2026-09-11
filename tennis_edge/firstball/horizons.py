"""Canonical decision horizons, measured from the ACTUAL first ball.

The research question this exists for is WHEN, not WHETHER: if an edge exists at all, does it live six
hours out, or only in the last ten minutes when the book is thin? That question is meaningless against a
scheduled time, because a two-hour court delay moves every horizon.

Rules:
  * a horizon is populated from the last EXECUTABLE quote at or before its target instant;
  * a horizon is NEVER fabricated. If the newest qualifying quote is staler than `max_staleness_s`,
    the horizon is reported as missing, with the staleness recorded so the gap is visible;
  * every populated horizon records the target instant, the actual quote timestamp, the distance from
    the target, and the distance from the first ball. Nothing is rounded into place;
  * LAST_VALID_PREMATCH is the canonical close itself: the last executable quote strictly before the
    earliest possible first ball.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timedelta

from tennis_edge.ledger.close import Quote
from .truth import FirstBallTruth

HORIZONS: tuple[tuple[str, int], ...] = (
    ("T-6h", 21600), ("T-3h", 10800), ("T-1h", 3600), ("T-30m", 1800),
    ("T-15m", 900), ("T-10m", 600), ("T-5m", 300), ("LAST_VALID_PREMATCH", 0),
)

#: how stale the newest qualifying quote may be before a horizon is reported missing instead of filled
DEFAULT_MAX_STALENESS_S = {"T-6h": 3600, "T-3h": 3600, "T-1h": 1800, "T-30m": 900,
                           "T-15m": 600, "T-10m": 420, "T-5m": 300, "LAST_VALID_PREMATCH": 86400}


@dataclass(frozen=True)
class HorizonQuote:
    horizon: str
    target_offset_s: int
    target_utc: datetime | None
    quote_ts: datetime | None
    seconds_from_target: float | None
    seconds_to_first_ball: float | None
    yes_bid: float | None = None
    yes_ask: float | None = None
    mid: float | None = None
    spread: float | None = None
    depth: float | None = None
    populated: bool = False
    missing_reason: str = ""

    def to_dict(self):
        d = asdict(self)
        for k in ("target_utc", "quote_ts"):
            d[k] = d[k].isoformat() if d[k] else None
        return d


def horizon_quotes(quotes: list[Quote], truth: FirstBallTruth | None, *,
                   max_staleness_s: dict | None = None) -> list[HorizonQuote]:
    """One record per canonical horizon. Requires strict-eligible first-ball truth; otherwise every
    horizon is reported missing (a horizon relative to an unknown start is not a horizon)."""
    stale = {**DEFAULT_MAX_STALENESS_S, **(max_staleness_s or {})}
    if truth is None or not truth.strict_eligible or truth.no_play or truth.lower_bound_utc is None:
        return [HorizonQuote(name, off, None, None, None, None, populated=False,
                             missing_reason="no strict-eligible first-ball truth") for name, off in HORIZONS]
    fb = truth.lower_bound_utc
    execs = sorted([q for q in quotes if q.executable], key=lambda q: q.ts)
    out = []
    for name, off in HORIZONS:
        target = fb - timedelta(seconds=off)
        cands = [q for q in execs if q.ts < target] if off == 0 else [q for q in execs if q.ts <= target]
        if not cands:
            out.append(HorizonQuote(name, off, target, None, None, None, populated=False,
                                    missing_reason="no executable quote at or before the target"))
            continue
        q = cands[-1]
        age = (target - q.ts).total_seconds()
        if age > stale[name]:
            out.append(HorizonQuote(name, off, target, q.ts, age, (fb - q.ts).total_seconds(), populated=False,
                                    missing_reason=f"newest qualifying quote is {age:.0f}s stale (limit {stale[name]}s)"))
            continue
        out.append(HorizonQuote(name, off, target, q.ts, age, (fb - q.ts).total_seconds(),
                                yes_bid=q.yes_bid, yes_ask=q.yes_ask, mid=q.mid, spread=q.spread, depth=q.depth,
                                populated=True))
    return out
