"""CLV engine v2: closing-line value measured against the ACTUAL first ball.

What CLV is here
----------------
CLV is an INFORMATION AND EXECUTION DIAGNOSTIC, not profit. It asks: given a hypothetical YES entry at
the contemporaneous executable ask, had the market moved toward that view by the last executable quote
before the first ball? It is never added to, netted against, or reported alongside realised P/L, and it
is never used as evidence that a strategy makes money.

Three movement measures, kept separate and never averaged together:

  clv_executable   close_yes_bid - entry_yes_ask   PRIMARY. What a taker who bought YES could have sold
                                                   back for at the close. Spread-inclusive and therefore
                                                   pessimistic, which is the point.
  clv_ask_to_ask   close_yes_ask - entry_yes_ask   same side of the book at both ends; isolates level
                                                   movement from spread movement.
  clv_midpoint     close_mid - entry_mid           SECONDARY, and only meaningful where both ends are
                                                   two-sided.

Units. A Kalshi YES contract pays $1, so its price in dollars IS the market-implied probability of the
event. Price-space and probability-space movement are therefore the SAME NUMBER for every family here,
including spreads and totals, whose contracts are binary on a threshold. Both are reported, with explicit
units, so that nobody later mistakes one for a separate piece of evidence.

Fees are computed but reported SEPARATELY and never folded into a CLV number.

Strictness. A CLV record is `strict` only when the close is anchored to A/B first-ball truth AND the
entry itself classifies as STRICT_PREGAME. Anything else is retained, labelled, and excluded from strict
research. Nothing is dropped.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict, field
from datetime import datetime

from tennis_edge.firstball.classify import TimingClassification, STRICT_PREGAME
from tennis_edge.firstball.truth import FirstBallTruth
from tennis_edge.ledger.close import CanonicalClose, Quote
from tennis_edge.pricing.fees import FeeSchedule, taker_fee

CLV_ENGINE_VERSION = 2


@dataclass(frozen=True)
class ClvRecord:
    # ---- identity
    prediction_id: str
    ticker: str
    match_id: str
    family: str
    tour: str = ""
    level: str = ""
    # ---- entry (the decision-time quote, straight off the immutable ledger row)
    entry_ts: datetime | None = None
    entry_yes_bid: float | None = None
    entry_yes_ask: float | None = None
    entry_mid: float | None = None
    entry_spread: float | None = None
    entry_depth: float | None = None
    # ---- close (last executable quote strictly before the earliest possible first ball)
    close_ts: datetime | None = None
    close_yes_bid: float | None = None
    close_yes_ask: float | None = None
    close_mid: float | None = None
    close_spread: float | None = None
    close_depth: float | None = None
    close_basis: str = "NONE"
    # ---- timing, all relative to ACTUAL first-ball truth
    first_ball_lower_utc: datetime | None = None
    first_ball_upper_utc: datetime | None = None
    truth_confidence: str = "UNKNOWN"
    derivation_version: int = 0
    timing_class: str = "START_UNKNOWN"
    seconds_entry_to_first_ball: float | None = None
    seconds_close_to_first_ball: float | None = None
    seconds_entry_to_close: float | None = None
    # ---- movement
    clv_executable: float | None = None
    clv_ask_to_ask: float | None = None
    clv_midpoint: float | None = None
    price_move_cents: float | None = None
    prob_move: float | None = None
    # ---- model context
    model_prob: float | None = None
    market_mid_at_entry: float | None = None
    model_market_disagreement: float | None = None
    data_quality_grade: str = ""
    # ---- fees, separate by construction
    entry_taker_fee_per_contract: float | None = None
    close_taker_fee_per_contract: float | None = None
    # ---- provenance
    strict: bool = False
    exclusion_reason: str = ""
    engine_version: int = CLV_ENGINE_VERSION

    def to_dict(self):
        d = asdict(self)
        for k, v in list(d.items()):
            if isinstance(v, datetime):
                d[k] = v.isoformat()
        return d


def clv_record(*, prediction_id: str, ticker: str, match_id: str, family: str, entry: Quote,
               close: CanonicalClose, truth: FirstBallTruth | None, timing: TimingClassification,
               tour: str = "", level: str = "", model_prob: float | None = None,
               data_quality_grade: str = "", fee_schedule: FeeSchedule | None = None) -> ClvRecord:
    fs = fee_schedule or FeeSchedule()
    cq = close.quote
    lo = truth.lower_bound_utc if truth else None
    hi = truth.upper_bound_utc if truth else None

    entry_ok = entry is not None and entry.executable
    close_ok = cq is not None and cq.executable
    strict = bool(close.strict and timing.timing_class == STRICT_PREGAME and entry_ok and close_ok)
    reasons = []
    if not entry_ok:
        reasons.append("entry quote not executable")
    if not close_ok:
        reasons.append(f"no executable close ({close.close_basis})")
    if timing.timing_class != STRICT_PREGAME:
        reasons.append(f"entry timing {timing.timing_class}")
    if not close.strict:
        reasons.append(f"close basis {close.close_basis} is not first-ball anchored")

    exe = (cq.yes_bid - entry.yes_ask) if (entry_ok and close_ok) else None
    a2a = (cq.yes_ask - entry.yes_ask) if (entry_ok and close_ok) else None
    midclv = (cq.mid - entry.mid) if (entry_ok and close_ok) else None
    return ClvRecord(
        prediction_id=prediction_id, ticker=ticker, match_id=match_id, family=family, tour=tour, level=level,
        entry_ts=entry.ts if entry else None,
        entry_yes_bid=entry.yes_bid if entry else None, entry_yes_ask=entry.yes_ask if entry else None,
        entry_mid=entry.mid if entry else None, entry_spread=entry.spread if entry else None,
        entry_depth=entry.depth if entry else None,
        close_ts=cq.ts if cq else None, close_yes_bid=cq.yes_bid if cq else None, close_yes_ask=cq.yes_ask if cq else None,
        close_mid=cq.mid if cq else None, close_spread=cq.spread if cq else None, close_depth=cq.depth if cq else None,
        close_basis=close.close_basis,
        first_ball_lower_utc=lo, first_ball_upper_utc=hi,
        truth_confidence=truth.confidence if truth else "UNKNOWN",
        derivation_version=truth.derivation_version if truth else 0,
        timing_class=timing.timing_class,
        seconds_entry_to_first_ball=(lo - entry.ts).total_seconds() if (lo and entry) else None,
        seconds_close_to_first_ball=(lo - cq.ts).total_seconds() if (lo and cq) else None,
        seconds_entry_to_close=(cq.ts - entry.ts).total_seconds() if (cq and entry) else None,
        clv_executable=exe, clv_ask_to_ask=a2a, clv_midpoint=midclv,
        price_move_cents=round(midclv * 100, 4) if midclv is not None else None,
        prob_move=midclv,
        model_prob=model_prob,
        market_mid_at_entry=entry.mid if entry else None,
        model_market_disagreement=(model_prob - entry.mid) if (model_prob is not None and entry_ok) else None,
        data_quality_grade=data_quality_grade,
        entry_taker_fee_per_contract=taker_fee(entry.yes_ask, 1, fs) if entry_ok else None,
        close_taker_fee_per_contract=taker_fee(cq.yes_bid, 1, fs) if close_ok else None,
        strict=strict, exclusion_reason="; ".join(reasons))
