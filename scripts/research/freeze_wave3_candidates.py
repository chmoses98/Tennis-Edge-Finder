#!/usr/bin/env python3
"""Freeze the Wave 3 candidates. Two, both abstentions, neither an edge claim.

Wave 3 found no subset in which our probability was more accurate than the Kalshi price. What it did
find, replicated across two independent blocks with bootstrap intervals excluding zero, is a place where
acting on our disagreement is measurably WORSE than abstaining. That is worth tracking prospectively, so
it is frozen the same way a positive claim would be.

Nothing here alters the Wave 2 candidates. Nothing here can be confirmed on the eighteen days that
produced it: the registry refuses evidence dated before the freeze.
"""
from __future__ import annotations

import os
import sys
from datetime import datetime, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.research.registry import EdgeCandidate, PROSPECTIVE_PENDING, save, load_all  # noqa: E402

ROOT = os.path.join(PROJ, "data", "research", "edge_candidates")
NOW = datetime.now(timezone.utc).isoformat()
DISCOVERY = ("2026-08-25", "2026-09-11")

CANDIDATES = [
    EdgeCandidate(
        candidate_id="W3-2026-001-ABSTAIN-ITF",
        hypothesis="Acting on our disagreement with the Kalshi price is NEGATIVE-VALUE at ITF level; "
                   "excluding ITF raises the realised after-fee edge of the positive-edge set.",
        inclusion_rule="MATCH_WINNER contracts where fee-adjusted edge at the executable ask is > 0. "
                       "Compare the realised after-fee P&L per contract of rows with level == 'ITF' "
                       "against rows with level != 'ITF'. One contract at the displayed ask, taker fee.",
        market_family="MATCH_WINNER", model_version="gen2_dyn_hier_sr_v1+fair_v1+selector_v1",
        discovery_window_start=DISCOVERY[0], discovery_window_end=DISCOVERY[1],
        frozen_at=NOW, confirmation_start=NOW, minimum_n=400,
        required_accuracy_condition="ITF realised after-fee P&L per contract < 0 with a bootstrap 95% "
                                    "interval excluding zero, AND below the non-ITF subset's",
        required_clv_condition="not required: this is an abstention rule and generates no position",
        required_after_fee_condition="the non-ITF subset's realised after-fee P&L per contract exceeds "
                                     "the combined set's",
        status=PROSPECTIVE_PENDING,
        rationale="Discovery+validation: ITF realised -3.5c per contract, 95% CI [-6.5c, -0.4c], n=763. "
                  "Holdout: -4.8c, CI [-9.2c, -0.4c], n=369. Same sign, both intervals excluding zero, "
                  "on blocks separated in time. The mechanism is plausible and was predicted by Wave 2: "
                  "serve statistics cover about 4% of ITF matches, so the structural model is running on "
                  "rating-implied point probabilities and cross-level translation at exactly the level "
                  "where the rating substrate is thinnest.",
        strongest_opposing_reason="Eighteen days of one exchange, and the two blocks are adjacent rather "
                                  "than independent seasons: the same players, tournaments and surface "
                                  "conditions appear in both, so 'replicated' is weaker here than the two "
                                  "intervals make it look. ITF is also where our identity coverage is "
                                  "worst, so part of the effect may be mis-mapped players rather than a "
                                  "modelling failure -- and that has a different fix.",
        prereg_dimensions=("level",)),
    EdgeCandidate(
        candidate_id="W3-2026-002-NONITF-POSITIVE-EDGE",
        hypothesis="Outside ITF, opportunities with a positive fee-adjusted edge return more than they "
                   "cost after fees.",
        inclusion_rule="MATCH_WINNER contracts, level != 'ITF', fee-adjusted edge at the executable ask "
                       "> 0, qualification passes, one contract at the displayed ask, taker fee.",
        market_family="MATCH_WINNER", model_version="gen2_dyn_hier_sr_v1+fair_v1+selector_v1",
        discovery_window_start=DISCOVERY[0], discovery_window_end=DISCOVERY[1],
        frozen_at=NOW, confirmation_start=NOW, minimum_n=600,
        required_accuracy_condition="on the SELECTED rows our Brier must be no worse than the Kalshi "
                                    "mid's. This condition currently FAILS and is the reason the "
                                    "candidate is not a claim.",
        required_clv_condition="mean strict executable CLV > 0 with a 95% interval excluding zero, once "
                               "A/B first-ball truth exists to compute it; none exists today",
        required_after_fee_condition="realised after-fee P&L per contract > 0 with a 95% interval "
                                     "excluding zero",
        status=PROSPECTIVE_PENDING,
        rationale="Positive in all three blocks (+1.6c discovery, +6.1c validation, +4.2c holdout) and "
                  "never significant in any of them. Frozen because a consistent sign across a "
                  "chronological split is the weakest evidence worth keeping, and because writing the "
                  "pass conditions down now is the only way to stop a later wave from lowering them.",
        strongest_opposing_reason="On the very rows it selects, our probability is LESS accurate than the "
                                  "price (holdout Brier 0.2248 against the market's 0.2159). A positive "
                                  "return with worse accuracy on 220 mostly-underdog bets is what "
                                  "variance looks like, not what an edge looks like. Its sibling rule "
                                  "R1, which added two more filters and looked far better on discovery "
                                  "and validation, went NEGATIVE on the holdout -- from the same data.",
        prereg_dimensions=("level", "fee_adjusted_edge")),
]


def main():
    existing = {c.candidate_id for c in load_all(ROOT)} if os.path.isdir(ROOT) else set()
    for c in CANDIDATES:
        if c.candidate_id in existing:
            print(f"{c.candidate_id}: already frozen, left alone")
            continue
        print(f"frozen {c.candidate_id} -> {save(c, ROOT)}")
    print(f"\ntotal candidates on file: {len(load_all(ROOT))}")
    for c in load_all(ROOT):
        print(f"  {c.candidate_id:34s} {c.status:22s} min_n={c.minimum_n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
