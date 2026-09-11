"""Canonical executable close, anchored to ACTUAL first-ball truth.

CANONICAL_CLOSE = the last valid EXECUTABLE quote strictly before the EARLIEST possible first ball.

Three things this module refuses to do, each of which was possible in v1:

1. It will not accept a bare datetime as "the start". `canonical_close()` takes a FirstBallTruth object.
   A scheduled time, a Kalshi `occurrence_datetime` and a market `close_time` are not truth objects, so
   they cannot be substituted by accident. A scheduled-time close is still computable for diagnostics,
   but only through `allow_scheduled_fallback=True`, and the result is stamped `strict=False`.
2. It will not use the point estimate of a bracketed first ball. The cutoff is the LOWER bound, so a
   close is only ever selected from quotes that provably precede any possible first ball.
3. It will not synthesise. No executable quote before the cutoff means NO EXECUTABLE CLOSE.

Executable means a real two-sided quote: both yes_bid and yes_ask present, 0 < bid <= ask < 1, from a
market record, an orderbook top or a bid/ask candle. Trade prints and settlement values are never quotes.
The midpoint is retained as a SECONDARY measure only; the primary close is the executable side.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timedelta

from tennis_edge.firstball.truth import FirstBallTruth

SAFETY_MARGIN = timedelta(minutes=5)

BASIS_ACTUAL = "ACTUAL_FIRST_BALL"
BASIS_BRACKET = "FIRST_BALL_BRACKET_LOWER"
BASIS_SCHEDULED = "SCHEDULED_MINUS_MARGIN"
BASIS_NONE = "NO_FIRST_BALL_TRUTH"
BASIS_NO_QUOTE = "NO_EXECUTABLE_QUOTE"


@dataclass(frozen=True)
class Quote:
    ts: datetime
    yes_bid: float | None
    yes_ask: float | None
    yes_bid_size: float | None = None
    yes_ask_size: float | None = None
    no_bid: float | None = None
    no_ask: float | None = None
    no_bid_size: float | None = None
    no_ask_size: float | None = None
    source: str = "market_record"    # market_record | orderbook | candle_bidask

    @property
    def executable(self) -> bool:
        return (self.yes_bid is not None and self.yes_ask is not None and 0.0 < self.yes_bid <= self.yes_ask < 1.0
                and self.source in ("market_record", "orderbook", "candle_bidask"))

    @property
    def mid(self) -> float | None:
        return 0.5 * (self.yes_bid + self.yes_ask) if self.executable else None

    @property
    def spread(self) -> float | None:
        return self.yes_ask - self.yes_bid if self.executable else None

    @property
    def depth(self) -> float | None:
        sizes = [s for s in (self.yes_bid_size, self.yes_ask_size) if s is not None]
        return min(sizes) if len(sizes) == 2 else (sizes[0] if sizes else None)

    def implied_no(self) -> tuple[float | None, float | None]:
        """NO side quoted directly when available, else derived from the YES book (no_bid = 1 - yes_ask)."""
        if self.no_bid is not None and self.no_ask is not None:
            return self.no_bid, self.no_ask
        if not self.executable:
            return None, None
        return 1.0 - self.yes_ask, 1.0 - self.yes_bid

    def to_dict(self):
        d = asdict(self)
        d["ts"] = self.ts.isoformat() if self.ts else None
        d.update(mid=self.mid, spread=self.spread, depth=self.depth)
        return d


@dataclass(frozen=True)
class CanonicalClose:
    quote: Quote | None
    cutoff: datetime | None
    close_basis: str
    strict: bool
    seconds_to_cutoff: float | None
    seconds_to_first_ball: float | None
    n_quotes_considered: int
    n_executable_considered: int
    truth_confidence: str = "UNKNOWN"
    derivation_version: int = 0

    def to_dict(self):
        return {"basis": self.close_basis, "strict": self.strict,
                "cutoff": self.cutoff.isoformat() if self.cutoff else None,
                "seconds_to_cutoff": self.seconds_to_cutoff, "seconds_to_first_ball": self.seconds_to_first_ball,
                "n_quotes": self.n_quotes_considered, "n_executable": self.n_executable_considered,
                "truth_confidence": self.truth_confidence, "derivation_version": self.derivation_version,
                "quote": self.quote.to_dict() if self.quote else None}


def _pick(quotes, cutoff):
    best, n_exec = None, 0
    for q in quotes:
        if not q.executable:
            continue
        n_exec += 1
        if q.ts < cutoff and (best is None or q.ts > best.ts):
            best = q
    return best, n_exec


def canonical_close(quotes: list[Quote], truth: FirstBallTruth | None, *, scheduled_start: datetime | None = None,
                    allow_scheduled_fallback: bool = False, margin: timedelta = SAFETY_MARGIN) -> CanonicalClose:
    conf = truth.confidence if truth else "UNKNOWN"
    ver = truth.derivation_version if truth else 0
    if truth is not None and truth.strict_eligible and not truth.no_play and truth.lower_bound_utc is not None:
        cutoff = truth.lower_bound_utc
        basis = BASIS_ACTUAL if truth.bracket_seconds == 0 else BASIS_BRACKET
        strict = True
        fb = truth.lower_bound_utc
    elif allow_scheduled_fallback and scheduled_start is not None:
        cutoff, basis, strict, fb = scheduled_start - margin, BASIS_SCHEDULED, False, None
    else:
        return CanonicalClose(None, None, BASIS_NONE, False, None, None, len(quotes),
                              sum(1 for q in quotes if q.executable), conf, ver)
    best, n_exec = _pick(quotes, cutoff)
    if best is None:
        return CanonicalClose(None, cutoff, BASIS_NO_QUOTE, False, None, None, len(quotes), n_exec, conf, ver)
    return CanonicalClose(best, cutoff, basis, strict, (cutoff - best.ts).total_seconds(),
                          (fb - best.ts).total_seconds() if fb else None, len(quotes), n_exec, conf, ver)
