"""The candidate status engine: one deterministic mapping from scored evidence to a status.

The statuses are a closed set, fixed before any prospective outcome was read. There is no softer
category, and the order of the checks below is the order of precedence: a candidate that cannot be
scored is reported as unscorable before anything is said about its size, and a candidate that is too
small is reported as too small before anything is said about whether it passed.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict, field

INSUFFICIENT_N = "INSUFFICIENT_N"
PENDING_SETTLEMENT = "PENDING_SETTLEMENT"
PENDING_STRICT_CLV = "PENDING_STRICT_CLV"
FAIL_ACCURACY = "FAIL_ACCURACY"
FAIL_CLV = "FAIL_CLV"
FAIL_ECONOMICS = "FAIL_ECONOMICS"
REJECTED = "REJECTED"
SUPPORTED_FOR_MORE_RESEARCH = "SUPPORTED_FOR_MORE_RESEARCH"
ELIGIBLE_FOR_CEO_REVIEW = "ELIGIBLE_FOR_CEO_REVIEW"
ABSTENTION_SUPPORTED = "ABSTENTION_SUPPORTED"
UNSCORABLE_MISSING_HISTORICAL_FIELDS = "UNSCORABLE_MISSING_HISTORICAL_FIELDS"

STATUSES = (INSUFFICIENT_N, PENDING_SETTLEMENT, PENDING_STRICT_CLV, FAIL_ACCURACY, FAIL_CLV,
            FAIL_ECONOMICS, REJECTED, SUPPORTED_FOR_MORE_RESEARCH, ELIGIBLE_FOR_CEO_REVIEW,
            ABSTENTION_SUPPORTED, UNSCORABLE_MISSING_HISTORICAL_FIELDS)

# what kind of claim a candidate makes decides what "all conditions pass" can earn
KIND_TRADE = "TRADE"                  # accuracy + CLV + economics; the only kind that can reach CEO review
KIND_PRICING = "PRICING_ACCURACY"     # a forecasting claim that may not justify a trade on its own
KIND_ABSTENTION = "ABSTENTION"        # a rule for NOT acting; can never become a position
KIND_EXISTENCE = "EXISTENCE"          # "this structure occurs"; discovery only


@dataclass(frozen=True)
class ScoreSummary:
    kind: str
    minimum_n: int
    eligible_n: int                  # rows that satisfied the frozen rule AND are admissible evidence
    settled_n: int = 0
    strict_clv_n: int = 0
    unsettled_n: int = 0             # eligible rows still waiting for settlement
    clv_pending_n: int = 0           # eligible rows whose strict close could still arrive
    unscorable_n: int = 0            # universe rows the rule could not be evaluated on (missing fields)
    accuracy_pass: bool | None = None     # None = not applicable to this candidate
    clv_pass: bool | None = None
    economics_pass: bool | None = None
    clv_required: bool = False
    notes: tuple = field(default_factory=tuple)

    def to_dict(self):
        return asdict(self)


def assign_status(s: ScoreSummary) -> tuple[str, str]:
    """(status, one-line reason). Pure function of the summary; no thresholds live here."""
    if s.kind not in (KIND_TRADE, KIND_PRICING, KIND_ABSTENTION, KIND_EXISTENCE):
        raise ValueError(f"unknown candidate kind {s.kind!r}")
    if s.unscorable_n > 0 and s.eligible_n < s.minimum_n:
        return (UNSCORABLE_MISSING_HISTORICAL_FIELDS,
                f"{s.unscorable_n} post-freeze observations could not be evaluated because a field the "
                f"frozen rule needs was not preserved at capture; {s.eligible_n} scorable of {s.minimum_n} required")
    if s.eligible_n < s.minimum_n:
        return INSUFFICIENT_N, f"{s.eligible_n} eligible of {s.minimum_n} required"
    if s.kind != KIND_EXISTENCE and s.settled_n < s.minimum_n:
        return (PENDING_SETTLEMENT,
                f"{s.settled_n} settled of {s.minimum_n} required ({s.unsettled_n} awaiting settlement)")
    if s.clv_required and s.strict_clv_n < s.minimum_n:
        if s.clv_pending_n > 0:
            return (PENDING_STRICT_CLV,
                    f"{s.strict_clv_n} strict-CLV rows of {s.minimum_n} required ({s.clv_pending_n} could still gain a strict close)")
        return INSUFFICIENT_N, f"{s.strict_clv_n} strict-CLV rows of {s.minimum_n} required and none pending"
    if s.accuracy_pass is False:
        return FAIL_ACCURACY, "the frozen accuracy condition is not met"
    if s.clv_required and s.clv_pass is not True:
        return FAIL_CLV, "the frozen strict-CLV condition is not met"
    if s.economics_pass is False:
        return FAIL_ECONOMICS, "the frozen after-fee condition is not met"
    if s.kind == KIND_ABSTENTION:
        return ABSTENTION_SUPPORTED, "every frozen condition met; this supports NOT acting, never a position"
    if s.kind in (KIND_PRICING, KIND_EXISTENCE):
        return SUPPORTED_FOR_MORE_RESEARCH, "every frozen condition met; the claim cannot justify a trade on its own"
    if s.accuracy_pass is None or s.economics_pass is None:
        return SUPPORTED_FOR_MORE_RESEARCH, "met what was evaluable; a condition could not be evaluated"
    return ELIGIBLE_FOR_CEO_REVIEW, "every frozen condition met at the frozen minimum N"
