"""Hard qualification: the deterministic gate that runs BEFORE anything is scored.

These are not preferences the selector can trade off against a big edge. They are the conditions under
which a number is allowed to mean anything at all: we know what the contract pays, we know who is
playing, we have a price we could actually hit, the price is recent, there is size behind it, we know the
fee, and the match has not already started.

The policy is a frozen, versioned object rather than scattered literals, so a threshold cannot drift
between the research that set it and the board that uses it.

One deliberate asymmetry. START_UNKNOWN does NOT block qualification, because at the levels Kalshi
actually lists (Challenger, ITF, qualifying) no A/B first-ball source exists and blocking would end the
research rather than protect it. POST_START does block. START_UNKNOWN is carried forward as itself and is
never relabelled STRICT_PREGAME, and every consumer must show it.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict

POLICY_VERSION = "qualify_v1"

#: families whose payoff we can price deterministically from a match distribution
KNOWN_FAMILIES = ("MATCH_WINNER", "SET_WINNER", "EXACT_SET_SCORE", "TOTAL_GAMES", "GAME_SPREAD",
                  "TOTAL_SETS", "SET_SPREAD", "TIEBREAK_OCCURS", "ANY_SET_WINNER")


@dataclass(frozen=True)
class QualificationPolicy:
    version: str = POLICY_VERSION
    max_spread: float = 0.06             # dollars, two-sided
    max_quote_age_s: float = 3600.0      # an hourly candle is the coarsest quote we accept
    min_size: float = 1.0                # contracts at the displayed ask
    min_identity_confidence: float = 0.95
    min_data_quality: float = 0.40       # grade C or better
    min_price: float = 0.02              # avoid the tails where one tick is the whole edge
    max_price: float = 0.98


@dataclass(frozen=True)
class QualificationInputs:
    family: str
    identity_confidence: float | None
    fair_prob: float | None
    executable_ask: float | None
    executable_bid: float | None
    quote_age_seconds: float | None
    available_size: float | None
    fee_per_contract: float | None
    first_ball_classification: str
    data_quality_score: float | None
    broken_health_gates: tuple = ()      # names of CRITICAL gates relevant to this market


@dataclass(frozen=True)
class Qualification:
    checks: dict
    policy_version: str

    @property
    def ok(self) -> bool:
        return bool(self.checks) and all(self.checks.values())

    @property
    def failed(self) -> tuple:
        return tuple(sorted(k for k, v in self.checks.items() if not v))

    def to_dict(self) -> dict:
        return {"checks": dict(self.checks), "policy_version": self.policy_version,
                "ok": self.ok, "failed": list(self.failed)}


def qualify(q: QualificationInputs, policy: QualificationPolicy = QualificationPolicy()) -> Qualification:
    ask, bid = q.executable_ask, q.executable_bid
    two_sided = ask is not None and bid is not None and 0 < bid <= ask < 1
    spread = (ask - bid) if two_sided else None
    checks = {
        "contract_semantics_known": q.family in KNOWN_FAMILIES,
        "identity_safe": q.identity_confidence is not None and q.identity_confidence >= policy.min_identity_confidence,
        "model_probability_exists": q.fair_prob is not None and 0.0 <= q.fair_prob <= 1.0,
        "executable_price_exists": two_sided,
        "price_not_stale": q.quote_age_seconds is not None and q.quote_age_seconds <= policy.max_quote_age_s,
        "size_available": q.available_size is not None and q.available_size >= policy.min_size,
        "spread_acceptable": spread is not None and spread <= policy.max_spread,
        "price_not_in_tail": two_sided and policy.min_price <= ask <= policy.max_price,
        "fees_known": q.fee_per_contract is not None,
        "not_post_start": q.first_ball_classification != "POST_START",
        "health_gates_ok": not q.broken_health_gates,
        "data_quality_sufficient": q.data_quality_score is not None and q.data_quality_score >= policy.min_data_quality,
    }
    return Qualification(checks=checks, policy_version=policy.version)


def policy_dict(policy: QualificationPolicy = QualificationPolicy()) -> dict:
    return asdict(policy)
