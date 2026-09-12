"""selector_v1: the rule that turns a priced opportunity into PASS, WATCH or SHADOW_BET.

It is a small ordered set of gates, not a score with tuned weights, and that is a finding rather than a
stylistic choice. Wave 3 fitted a logistic selector on proper-score superiority and another on realised
economics; neither survived its holdout. What DID replicate across two independent blocks was a single
abstention: our disagreement with the price is worth less than nothing at ITF level. So the gates carry
the decision and the fitted score is carried alongside as information, explicitly not as authority.

Every gate is a reason to abstain. None of them is a reason to bet: SHADOW_BET means "this survived
everything we know how to check", which is a statement about our checks, not about the market.

Thresholds were fixed on the discovery and validation blocks (2026-08-25..2026-09-06) and frozen before
the holdout was read. Changing one is a new selector version, not an edit to this one.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict

SELECTOR_VERSION = "selector_v1"

#: levels where Wave 3 measured our disagreement to be actively negative, in both evaluation blocks,
#: with bootstrap intervals excluding zero. Abstention here is the wave's one replicated result.
ABSTAIN_LEVELS = ("ITF",)


@dataclass(frozen=True)
class DecisionPolicy:
    version: str = SELECTOR_VERSION
    min_fee_adjusted_edge: float = 0.0     # after the taker fee, at the executable ask
    #: AN UPPER BOUND, which looks backwards and is the most important number here. Against a
    #: two-sided market whose mid beats ours globally, a claimed 25c edge is overwhelmingly more likely
    #: to be our error than theirs. Honest about the evidence: this band realised -3.7c on the discovery
    #: and validation blocks (the worst on the board) and +0.6c on the holdout, so the cap rests on the
    #: prior, not on a replicated measurement. It is a refusal to act on numbers we do not believe,
    #: which is the cheapest kind of protection and the easiest to justify being wrong about.
    max_fee_adjusted_edge: float = 0.15
    require_robust_edge: bool = True       # positive under EVERY configuration in the defensible set
    min_data_quality: float = 0.60
    abstain_levels: tuple = ABSTAIN_LEVELS
    max_env_width: float = 0.15            # a fair price we cannot pin to 15c is not a fair price
    frozen_on: str = "discovery+validation 2026-08-25..2026-09-06"


@dataclass(frozen=True)
class DecisionInputs:
    qualification_ok: bool
    fee_adjusted_edge: float | None
    robust_edge: float | None
    env_width: float | None
    data_quality: float | None
    level: str
    selector_score: float | None = None
    lanes_agree: bool | None = None
    market_moved_toward_us: float | None = None


def decide(x: DecisionInputs, policy: DecisionPolicy = DecisionPolicy()) -> dict:
    """Return the decision plus the reasons on both sides. The against-reason is never empty."""
    gates = {
        "qualified": bool(x.qualification_ok),
        "positive_after_fees": x.fee_adjusted_edge is not None and x.fee_adjusted_edge > policy.min_fee_adjusted_edge,
        "edge_is_plausible": x.fee_adjusted_edge is not None and x.fee_adjusted_edge <= policy.max_fee_adjusted_edge,
        "robust_to_reparameterisation": (not policy.require_robust_edge) or (x.robust_edge is not None and x.robust_edge > 0),
        "fair_price_is_pinned": x.env_width is not None and x.env_width <= policy.max_env_width,
        "data_quality_ok": x.data_quality is not None and x.data_quality >= policy.min_data_quality,
        "level_not_abstained": x.level not in policy.abstain_levels,
    }
    failed = [k for k, v in gates.items() if not v]
    if not failed:
        decision = "SHADOW_BET"
    elif gates["qualified"] and gates["positive_after_fees"]:
        decision = "WATCH"
    else:
        decision = "PASS"

    fors, againsts = [], []
    if x.fee_adjusted_edge is not None:
        fors.append(f"fee-adjusted edge {x.fee_adjusted_edge*100:+.1f}c at the executable ask")
    if gates["robust_to_reparameterisation"]:
        fors.append("the edge survives every configuration in the defensible parameter set")
    if x.lanes_agree:
        fors.append("Elo and Gen-2 disagree with the price in the same direction")
    if x.selector_score is not None:
        fors.append(f"selector score {x.selector_score:.2f}")

    if failed:
        againsts.append("fails: " + ", ".join(failed))
    if x.fee_adjusted_edge is not None and x.fee_adjusted_edge > policy.max_fee_adjusted_edge:
        againsts.append(f"a claimed {x.fee_adjusted_edge*100:.0f}c edge against a two-sided market is "
                        "far more likely to be our error than a mispricing; this band realised NEGATIVE")
    if x.level in policy.abstain_levels:
        againsts.append(f"{x.level} is a level where our disagreement measured NEGATIVE in both Wave 3 blocks")
    if x.market_moved_toward_us is not None and x.market_moved_toward_us > 0.005:
        againsts.append(f"the market has already drifted {x.market_moved_toward_us*100:.1f}c toward our side, "
                        "so part of what we think we know is already in the price")
    if x.env_width is not None and x.env_width > 0.05:
        againsts.append(f"reasonable reparameterisations move our fair price by {x.env_width*100:.1f}c")
    againsts.append("Wave 3 found no subset where our probability was MORE accurate than the price; "
                    "a positive realised return on a small sample is not evidence that it is")
    return {"decision": decision, "gates": gates, "failed_gates": failed,
            "reason_for": "; ".join(fors) if fors else "nothing",
            "reason_against": "; ".join(againsts), "policy": asdict(policy)}
