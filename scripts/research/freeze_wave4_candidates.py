#!/usr/bin/env python3
"""Freeze ONE Wave 4 candidate, and be clear that discovery did not support it.

Wave 4's discovery found no actionable dislocation: across 260 observations an independent venue and
Kalshi differed by a median of 0.8c against a round-trip cost near 3c, and not one observation produced
an external edge of 2c after fees. On the mandate's own terms that is zero supported candidates.

This candidate is frozen anyway, and the distinction matters. It is a PRE-REGISTRATION, not a finding:
the infrastructure can now detect a Kalshi-lone-outlier, so the rule and its pass conditions are written
down BEFORE any instance accumulates. Without that, a future wave with a handful of instances would be
evaluating them post-hoc, choosing the threshold after seeing the outcomes -- exactly the failure Wave 3
demonstrated with R1.
"""
from __future__ import annotations

import os
import sys
from datetime import datetime, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.research.registry import EdgeCandidate, PROSPECTIVE_PENDING, load_all, save  # noqa: E402

ROOT = os.path.join(PROJ, "data", "research", "edge_candidates")
NOW = datetime.now(timezone.utc).isoformat()

CANDIDATE = EdgeCandidate(
    candidate_id="W4-2026-001-KALSHI-LONE-OUTLIER",
    hypothesis="When an independent venue and our frozen fundamental model sit on the SAME side of the "
               "Kalshi price, the Kalshi price is the one that is wrong, and it moves toward the "
               "external reference before the match starts.",
    inclusion_rule="MATCH_WINNER contracts where: a reference value exists from at least one admissible "
                   "external group whose venue timestamp is under 30 minutes old; triangulation is "
                   "KALSHI_LONE_OUTLIER; external fair minus the executable Kalshi ask minus the taker "
                   "fee is >= 0.02; the Kalshi quote is two-sided, under an hour old, inside a 6c spread "
                   "and backed by at least one contract of displayed size. Measured on the FIRST such "
                   "observation of each contract; later observations of the same contract are follow-up, "
                   "not new evidence.",
    market_family="MATCH_WINNER",
    model_version="external_v1 + fair_v1 (frozen) + gen2_dyn_hier_sr_v1 (frozen)",
    discovery_window_start="2026-09-12", discovery_window_end="2026-09-12",
    frozen_at=NOW, confirmation_start=NOW, minimum_n=200,
    required_accuracy_condition="on the flagged contracts, the external reference's Brier must beat the "
                                "Kalshi mid's with a 95% interval excluding zero. Our own model's "
                                "accuracy is NOT part of the test; Wave 3 settled what it is worth.",
    required_clv_condition="mean strict executable CLV > 0 with a 95% interval excluding zero, computed "
                           "only against A/B first-ball truth. Confidence C is excluded and this "
                           "condition may not be met with midpoint CLV.",
    required_after_fee_condition="realised after-fee P&L per contract > 0 at the executable ask with a "
                                 "95% interval excluding zero, one contract, no assumed depth",
    status=PROSPECTIVE_PENDING,
    rationale="PRE-REGISTRATION, NOT A FINDING. Discovery produced 5 KALSHI_LONE_OUTLIER observations out "
              "of 148 with a reference, none of which cleared 2c after fees, so there is nothing here to "
              "support. The rule is frozen now precisely because there is nothing to support: when "
              "instances do accumulate, the threshold and the pass conditions will already be fixed, and "
              "nobody will be able to choose them after seeing the outcomes.",
    strongest_opposing_reason="The premise looks weak before the test starts. The two venues agreed to "
                              "within a median of 0.8c across every observation, never differed by more "
                              "than 4.1c even including stale lines, and the round-trip cost is about 3c "
                              "-- so a dislocation large enough to pay may simply not occur. The single "
                              "external witness is also a recreational sportsbook, which is the venue "
                              "more likely to be wrong when the two disagree, and the only "
                              "KALSHI_LONE_OUTLIER with a follow-up observation saw Kalshi not move at "
                              "all.",
    prereg_dimensions=("triangulation", "external_edge"))


def main():
    existing = {c.candidate_id for c in load_all(ROOT)} if os.path.isdir(ROOT) else set()
    if CANDIDATE.candidate_id in existing:
        print(f"{CANDIDATE.candidate_id}: already frozen, left alone")
    else:
        print(f"frozen {CANDIDATE.candidate_id} -> {save(CANDIDATE, ROOT)}")
    for c in load_all(ROOT):
        print(f"  {c.candidate_id:34s} {c.status:20s} evidence={len(c.evidence)} min_n={c.minimum_n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
