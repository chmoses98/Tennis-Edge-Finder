#!/usr/bin/env python3
"""Freeze the wave-2 edge candidates. Run once; the registry refuses to confirm any of them on the data
that produced them."""
from __future__ import annotations

import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tennis_edge.research.registry import DISCOVERY_ONLY, PROSPECTIVE_PENDING, EdgeCandidate, save  # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ROOT = os.path.join(PROJ, "data", "research", "edge_candidates")
FROZEN = "2026-09-12T06:30:00+00:00"

CANDIDATES = [
    EdgeCandidate(
        candidate_id="EC-2026-001-MKTCOND-EXACT-SCORE",
        hypothesis="Anchoring the winner probability to the de-vigged market while keeping the Gen-2 "
                   "service level improves EXACT SET SCORE prediction relative to the pure fundamental "
                   "distribution.",
        inclusion_rule="Singles match, ATP or WTA, with (a) a two-sided executable market quote on the "
                       "match winner that de-vigs to a probability in [0.05, 0.95], (b) a Gen-2 state for "
                       "both players, and (c) family EXACT_SET_SCORE. Best-of-3 and best-of-5 both admitted.",
        market_family="EXACT_SET_SCORE", model_version="market_conditioned_v1 + gen2_dyn_hier_sr_v1",
        discovery_window_start="2020-01-01", discovery_window_end="2026-09-01",
        frozen_at=FROZEN, confirmation_start=FROZEN, minimum_n=400,
        required_accuracy_condition="mean exact-score log loss below the pure fundamental lane by >= 0.010 "
                                    "with a paired bootstrap 95% CI excluding zero",
        required_clv_condition="not applicable to a pricing-accuracy claim; no CLV condition is asserted, "
                               "and no trade may be justified by this candidate alone",
        required_after_fee_condition="any trade derived from it must clear the Kalshi taker fee on every "
                                     "leg at the executable ask",
        status=PROSPECTIVE_PENDING,
        rationale="On 12,946 ATP matches with a de-vigged Pinnacle price and a final score, exact-score "
                  "log loss fell from 1.35038 (fundamental) to 1.32710 (market-conditioned), paired diff "
                  "-0.02329, 95% CI [-0.02776, -0.01867]. The Elo-conditioned control was WORSE than the "
                  "fundamental lane (1.37007), so the gain comes from the market's information rather "
                  "than from conditioning on anything.",
        strongest_opposing_reason="Kalshi lists almost no exact-score contracts: four were open across the "
                                  "entire captured board. A pricing improvement with nothing to trade "
                                  "against is a scientific result, not an edge.",
        prereg_dimensions=("market_family", "tour", "surface")),
    EdgeCandidate(
        candidate_id="EC-2026-002-MKTCOND-GAME-SPREAD",
        hypothesis="The same conditioning improves expected game differential and total-games prediction.",
        inclusion_rule="As EC-2026-001 but for families GAME_SPREAD and TOTAL_GAMES, requiring a "
                       "quoted line and a completed match (no retirement).",
        market_family="GAME_SPREAD,TOTAL_GAMES", model_version="market_conditioned_v1 + gen2_dyn_hier_sr_v1",
        discovery_window_start="2020-01-01", discovery_window_end="2026-09-01",
        frozen_at=FROZEN, confirmation_start=FROZEN, minimum_n=400,
        required_accuracy_condition="mean absolute error on game differential below the fundamental lane "
                                    "by >= 0.05 games with a paired bootstrap 95% CI excluding zero",
        required_clv_condition="no CLV condition asserted",
        required_after_fee_condition="as EC-2026-001",
        status=PROSPECTIVE_PENDING,
        rationale="Game-differential absolute error 4.10248 -> 4.00667, paired diff -0.09581, 95% CI "
                  "[-0.11491, -0.07675]; squared error on total games -0.38276 with a CI excluding zero.",
        strongest_opposing_reason="Three TOTAL_GAMES contracts were open across the whole captured board. "
                                  "The same liquidity objection as EC-2026-001, only sharper.",
        prereg_dimensions=("market_family", "tour", "surface")),
    EdgeCandidate(
        candidate_id="EC-2026-003-GEN2-MODERATE-EVIDENCE",
        hypothesis="Where both players have moderate serve evidence, the Gen-2 blended lane carries "
                   "information the Gen-1 rating does not.",
        inclusion_rule="Singles match where the THINNER of the two players has between 1,000 and 20,000 "
                       "observed serve points in the Gen-2 state at prediction time, tour ATP or WTA.",
        market_family="MATCH_WINNER", model_version="gen2_dyn_hier_sr_v1",
        discovery_window_start="2015-01-01", discovery_window_end="2026-09-01",
        frozen_at=FROZEN, confirmation_start=FROZEN, minimum_n=1000,
        required_accuracy_condition="Brier below Gen-1 Elo by >= 0.0015 with a paired bootstrap 95% CI "
                                    "excluding zero, AND not worse than the market by more than 0.005",
        required_clv_condition="mean strict executable CLV > 0 with a 95% CI excluding zero, on rows "
                               "classified STRICT_PREGAME",
        required_after_fee_condition="after-fee expected value per contract > 0 at the executable ask",
        status=PROSPECTIVE_PENDING,
        rationale="ATP Brier in the 1k-5k serve-point bucket: Elo 0.2175, Gen-2 blended 0.2149 (-0.0026); "
                  "5k-20k: 0.2204 -> 0.2185. Overall paired diff -0.00106, 95% CI [-0.00124, -0.00087].",
        strongest_opposing_reason="Beating Gen-1 Elo is not beating the market. On the previous wave's "
                                  "evidence the market beats the ensemble everywhere tested, so this "
                                  "candidate may be an improvement that is still on the wrong side of the "
                                  "price.",
        prereg_dimensions=("model_uncertainty", "tour", "surface")),
    EdgeCandidate(
        candidate_id="EC-2026-004-COHERENCE-EXECUTABLE",
        hypothesis="A size-verified, after-fee-positive cross-market coherence violation occurs on the "
                   "Kalshi tennis board at a non-zero rate.",
        inclusion_rule="Any structure detected by tennis_edge.pricing.coherence on executable bid/ask with "
                       "order-book depth on every leg and an executable margin > 0 after Kalshi taker fees.",
        market_family="ANY", model_version="coherence_v1",
        discovery_window_start="2026-09-11", discovery_window_end="2026-09-12",
        frozen_at=FROZEN, confirmation_start=FROZEN, minimum_n=10,
        required_accuracy_condition="not applicable; the claim is existence, not accuracy",
        required_clv_condition="not applicable",
        required_after_fee_condition="executable margin > 0 after taker fees on every leg, with the "
                                     "minimum leg size >= 10 contracts",
        status=DISCOVERY_ONLY,
        rationale="Zero violations were found over ten capture passes, price-only or size-verified. The "
                  "candidate is frozen so that continued monitoring accumulates evidence against a "
                  "pre-committed rule rather than being re-specified after the fact.",
        strongest_opposing_reason="The observed fee wall (roughly four cents on a two-leg structure) is "
                                  "wider than the widest inconsistency seen (one cent), so the prior "
                                  "should be that this rate is zero.",
        prereg_dimensions=("market_family", "liquidity", "spread_width")),
]


def main():
    for c in CANDIDATES:
        print("frozen", c.candidate_id, c.status, c.fingerprint, "->", save(c, ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
