# Prospective confirmation report (2026-09-27)

**Real-money authority: OFF.** No candidate is eligible for CEO review. No model, threshold, rule,
minimum N or pass condition was changed; no candidate was created; no candidate definition file was
written (all seven are byte-identical to their frozen copies and their fingerprints re-verify).

Evidence snapshot: `tennis-data` @ `6344965` (2026-09-27 18:54 UTC). Harvest run `20260927T195248Z`,
reproduced bit-for-bit by an earlier run on the same evidence. Details: `research/candidate_confirmation/`
(per-candidate JSON, `SUMMARY.md`, scorecards) and the derived evidence layer
`data/research/candidate_evidence/`. Field-by-field provenance: `research/PROSPECTIVE_EVIDENCE_AUDIT.md`.

## The headline

The bottleneck was not the empty `evidence` field. It was that **five of the seven frozen candidates
decide on a probability that no production job computed after they were frozen.** The prospective
pipeline kept capturing markets, first balls, external venues and settlements, but the only model it
kept writing down was Gen-1 (`elo_surface_k_lo+sr_v0.1`, the prediction ledger). The Gen-2 / fair_v1 /
selector_v1 lane (the shadow board) ran once, at 17:13 on 2026-09-12, eleven minutes before the Wave 3
freeze, and is scheduled by no workflow; the market-conditioned lane was never run prospectively at all.
Those five are UNSCORABLE for every post-freeze row. Reconstructing their probabilities now from today's
artifacts would be synthesising historical state, so it was not done.

The two candidates whose inputs were captured -- W4 and EC-004 -- are scored exactly. Both are
INSUFFICIENT_N.

## Candidate scoreboard

| candidate | status | eligible N / min | settled | strict CLV | why |
|---|---|---|---|---|---|
| EC-2026-001-MKTCOND-EXACT-SCORE | **UNSCORABLE_MISSING_HISTORICAL_FIELDS** | 0 / 400 | -- | -- | no prospective market-conditioned or fundamental exact-score distribution exists; Kalshi listed only 382 exact-score contracts on 95 matches after the freeze, so it could not have reached 400 matches anyway |
| EC-2026-002-MKTCOND-GAME-SPREAD | **UNSCORABLE_MISSING_HISTORICAL_FIELDS** | 0 / 400 | -- | -- | same missing lanes; no games-level sports truth to compute a game-differential MAE; 1,004 contracts on 254 matches listed |
| EC-2026-003-GEN2-MODERATE-EVIDENCE | **UNSCORABLE_MISSING_HISTORICAL_FIELDS** | 0 / 1,000 | -- | -- | no preserved row has Gen-2, Gen-1 and the thinner player's Gen-2 serve points for the same decision; the only Gen-2 serve-evidence rows are one shadow-board run (502 rows) |
| EC-2026-004-COHERENCE-EXECUTABLE | **INSUFFICIENT_N** (DISCOVERY_ONLY) | 3 / 10 | n/a | n/a | 3 size-verified, after-fee-positive structures in 1,585 capture passes |
| W3-2026-001-ABSTAIN-ITF | **UNSCORABLE_MISSING_HISTORICAL_FIELDS** | 0 / 400 | -- | -- | the frozen fair_v1 probability (with surface) was never computed after the freeze |
| W3-2026-002-NONITF-POSITIVE-EDGE | **UNSCORABLE_MISSING_HISTORICAL_FIELDS** | 0 / 600 | -- | -- | same, plus the selector_v1 qualification checklist and the selected-row Kalshi mid |
| W4-2026-001-KALSHI-LONE-OUTLIER | **INSUFFICIENT_N** | 1 / 200 | 1 | 1 | 14 first qualifying observations, 1 of them STRICT_PREGAME |

Nothing was substituted for a missing field. In particular the dislocation scan's `model_fair` was NOT
used as the W3 probability: it is fair_v1 computed with `surface=None` on only the matches an external
venue lists -- a different number on a different population, i.e. a different rule.

## W4-2026-001 in full

| step | rows |
|---|---|
| dislocation rows before the freeze (excluded) | 260 |
| after the freeze | 15,678 |
| pass every preserved-field gate (family, reference, KALSHI_LONE_OUTLIER, edge >= 2c after fee, two-sided, < 1 h, <= 6c, size >= 1) | 86 (identical to the scanner's own SHADOW_BET rows) |
| ... and every contributing venue timestamp < 30 min (VERIFIED_FRESH) | 18 (58 Smarkets-only = unverifiable, 6 mixed, 4 unresolved: excluded) |
| first qualifying observation per contract | 14 (4 re-observations removed) |
| of which STRICT_PREGAME against A/B first-ball truth | **1** (13 START_UNKNOWN: Challenger / ITF / Davis Cup, no first-ball source) |

On the one eligible row (`KXWTAMATCH-26SEP19QUEBLI-QUE`, WTA tour, 2026-09-18 23:26Z; ask 40c, external 44.4c):
external-reference Brier 0.310 vs Kalshi mid 0.366 (paired diff -0.056, no interval at n=1); strict
executable CLV 0.0c (midpoint +1.0c); after-fee P&L +58c. None of the three frozen conditions can be
evaluated at n=1 and the frozen minimum is 200. Under the most permissive alternative reading (the
scanner's own SHADOW_BET flag, freshness not re-checked) there are 28 first observations and 3 strict
pregame ones; the status does not depend on the reading. At the observed rate (~1 per two weeks strict,
~14 per two weeks at all) W4 cannot reach 200 in any horizon that matters while ATP Challenger and ITF
have no first-ball source.

## EC-2026-004 in full (DISCOVERY_ONLY, never a betting candidate)

271,633 post-freeze order books scanned (1,585 passes, 104,512 match-passes), prices and depth taken
from the same book. 20 price-only violation instances (size ignored); 9 distinct structures with positive
after-fee margin on real depth; 3 with every leg >= 10 contracts:

| match | family | capital / set | worst-case payoff | after-fee margin | size | seen for |
|---|---|---|---|---|---|---|
| ITF W 26SEP19SIDWEI | MATCH_WINNER partition | $0.95 + $0.04 fees | $1.00 | +1c | 15 | one pass |
| Davis Cup 26SEP20MILVAI | MATCH_WINNER partition | $0.97 + $0.02 | $1.00 | +1c | 10 | one pass |
| ATP Ch. 26SEP22ZHUSEA | MATCH_WINNER partition | $0.96 + $0.02 | $1.00 | +2c | 20 | one pass |

Total worst-case profit across all three: about $0.66 on about $45 of capital, each alive for no more
than one ten-minute capture interval, legs read ~0.2 s apart, first-ball timing unknown (possibly in
play), and the worst case assumes the match is played (a walkover settles both legs at a "fair price").
3 of the 10 required: INSUFFICIENT_N. The discovery-era "size-verified: 0" had never seen a size (see
defects below), so this is the first size-verified reading of the rule.

## Settlement audit

**Settlement ingestion was healthy.** 12,330 settled rows (yes 5,939 / no 6,127 / scalar 264) cover
12,328 of 12,372 ledger rows; 0 duplicate prediction ids; 0 conflicts between the settle table and the
exchange's own settlement records. The 44 unsettled ledger rows are 18 settled by Kalshi after the last
settle run (swept 18:14Z) and 26 still open. Two settlement rows from a pre-migration 2026-09-11 run are
not in the ledger (reported, not deleted).

**Root cause of "no settled predictions yet": F -- the health layer was not reading the settlement
layer at all.** The workflow calls `run_all()` with no inputs and nothing computed `sports_total` /
`n_settled`, so TENNIS-8/9/10 reported UNKNOWN with that sentence for sixteen days. Fixed in
`tennis_edge/health/gates.py::settlement_stats`; no settlement row was rewritten and no backfill was
needed. Recomputed on the snapshot: TENNIS-8 **FAIL** (0 of 12,066 binary settlements have sports truth
independent of Kalshi -- every "sports truth" is Kalshi's own result copied), TENNIS-9 UNKNOWN (nothing
independent to reconcile against), TENNIS-10 **FAIL** (2,312 strict of 2,688 settled rows with A/B truth,
86% < 95%).

## Strict CLV scorecard (Gen-1 ledger, descriptive, not a candidate)

2,312 strict rows (unchanged by this work). Executable CLV = close YES bid - entry YES ask, so it is
spread-inclusive and pessimistic by construction; fees are separate.

**View B -- one row per physical decision** (earliest strict observation of each question; for match/set
winner only the side-A contract, so each question counts once):

| family | n | mean exec CLV | median | 95% CI | mean mid CLV | mean entry spread | mean fee | median h to first ball |
|---|---|---|---|---|---|---|---|---|
| MATCH_WINNER (singles) | 270 | -1.62c | -1.00c | [-2.78c, -0.52c] | +0.26c | 2.41c | 1.84c | 6.1 |
| MATCH_WINNER (doubles) | 19 | -10.79c | -5.00c | [-16.42c, -6.21c] | +4.00c | 18.11c | 1.84c | 14.4 |
| SET_WINNER | 209 | -10.00c | -5.00c | [-12.28c, -7.83c] | +0.14c | 14.67c | 1.83c | 8.8 |
| EXACT_SET_SCORE | 136 | -0.42c | -3.00c | [-3.24c, +2.56c] | +3.20c | 2.21c | 1.75c | 3.6 |
| GAME_SPREAD | 95 | -9.26c | -6.00c | [-13.46c, -5.06c] | +1.47c | 8.45c | 1.97c | 3.4 |
| SET_SPREAD | 2 | -1.00c | -- | -- | 0.00c | 1.00c | 2.00c | 6.0 |
| TOTAL_GAMES | 0 | -- | | | | | | |

View A (every strict row: both sides of each binary and every re-pricing -- the average cost of crossing
the spread in both directions, NOT a strategy): MATCH_WINNER 920 rows -1.53c [-1.98c, -1.09c], SET_WINNER
944 -8.10c, GAME_SPREAD 142 -8.13c, EXACT_SET_SCORE 210 -1.03c, doubles 92 -11.37c.

View C (descriptive only: the side the Gen-1 ledger row itself named at capture, same one-per-question
rows): MATCH_WINNER -0.74c [-1.54c, +0.16c]; SET_WINNER -8.77c; GAME_SPREAD -9.34c; EXACT_SET_SCORE -0.18c.
The market does not move toward the Gen-1 lane's side by enough to pay the spread.

**No TOTAL_GAMES row is strict, and that is a join gap, not missing truth.** The strict engine joins
first-ball truth on the exact Kalshi event ticker, and the first-ball watchlist keys truth under the
match-winner / set-winner / exact-score events it watches, never under a totals event. 671 ledger rows
(588 TOTAL_GAMES, 52 SET_WINNER, 21 GAME_SPREAD, 10 other) belong to a physical match that HAS A/B truth
under a sibling series. Joining on the shared match code would be a legitimate identity fix, but it
changes the production strict-CLV population, so it is reported here for a deliberate decision rather
than switched on inside an evidence harvest.

## External-market scorecard (since the W4 freeze, 1,471 scan passes)

| measure | value |
|---|---|
| dislocation rows (Kalshi MATCH_WINNER sides with an external match) | 15,678 |
| matched physical matches / Kalshi contracts | 1,084 / 2,168 |
| rows with a reference value | 7,494 |
| three-venue observations (Kalshi + Bovada + Smarkets) | 6,171 rows, 942 contracts |
| KALSHI_LONE_OUTLIER | 852 rows / 375 contracts |
| MODEL_LONE_OUTLIER | 5,444 / 1,179 |
| MARKETS_AGREE | 875 / 204 |
| ALL_THREE_DISAGREE | 249 / 132 |
| EXTERNAL_LONE_OUTLIER | 74 / 39 |
| INSUFFICIENT_INPUTS | 8,184 / 1,632 |
| W4 first qualifying observations | 14 (1 strict pregame) |
| strict CLV attached / settled attached (eligible) | 1 / 1 |
| after-fee P&L (eligible) | +58c on n=1 |

## Operational fixes

* **Order books were invisible.** Every captured book is `orderbook_fp` (dollars); both the CLV quote
  builder and the coherence scan read only the legacy cent keys. Fixed (`ledger/quotes.py::book_top`).
  Strict CLV count unchanged (2,312); 361 values moved, mean absolute 0.9c, mean signed 0.00c.
* **Laver Cup taxonomy -- fixed.** `KXLAVERCUPMATCH` (singles) and `KXLAVERCUPDOUBLESMATCH` (doubles)
  map to an explicit `TEAM_EVENT_MATCH_WINNER` family: parsed (competitors, side, competition), never
  priced, because neither the contract nor the format config states the scoring format. TENNIS-2 and
  TENNIS-3 now PASS on the snapshot (0 unknown series; 1 unparsed legacy ITF market of 61,084).
* **Trade capture truncation -- fixed in code, effective from the next capture pass.** All 1,689 passes
  truncated. The old cursor re-read ~12 minutes of tape per pass and skipped the unread older end for
  good: 54 windows, ~2.75 hours of tape, never read. The new scan reads the new window since the last
  one, queues any unread remainder as a backlog gap and drains it with leftover budget, inside the same
  250-page per-pass bound; gaps older than 24 h are abandoned explicitly (TENNIS-5 fails), and TENNIS-5
  also fails if the oldest queued gap exceeds 2 h. No candidate or strict CLV uses trades.
* **TENNIS-6 -- the violations are true post-start rows, and none leaked.** 330 ledger rows were
  generated after the actual first ball (297 POST_START, 33 inside the bracket) -- Challenger/WTA-125
  matches whose nominal start was hours late. 0 START_UNKNOWN rows violated the schedule fallback (9,718
  passed it; they were never violations). 0 of 2,312 strict rows is post-start: nothing leaked into
  strict research. The gate still FAILS on the 330; its detail now separates the classes, and
  `run_tennis.py` now refuses any match the first-ball store has already seen start.

## Answers

1. **final main SHA:** see the end of this session's hand-off (this file is part of that commit).
2. **tests:** 433 passed (389 pre-existing, 44 new), 0 failed.
3. **settlement ingestion:** healthy.
4. **root cause:** not a settlement break -- the health layer never read the settlement layer (F).
5. **prospective observations harvested:** 287,311 rule evaluations (15,678 dislocation rows for W4,
   271,633 order books for EC-004); unscorable universes counted per candidate (e.g. 24,414 post-freeze
   observations for EC-003, 23,768 for W3); 27 evidence rows written (18 W4 rule-qualifying, 9 EC-004 structures).
6. **settled observations:** 12,328 ledger rows; W4 rule-qualifying 14 of 18; W4 eligible 1.
7. **strict-CLV observations:** 2,312 (ledger); W4 eligible 1.
8. **eligible N:** EC-001 0, EC-002 0, EC-003 0, EC-004 3, W3-001 0, W3-002 0, W4 1.
9. **settled N:** W4 1; the others 0 (EC-004 has no settlement concept).
10. **strict-CLV N:** W4 1; the others 0.
11. **Brier / log-loss / MAE:** W4 external 0.310 vs Kalshi mid 0.366 (n=1). EC-001 log loss, EC-002 MAE,
    EC-003 Brier, W3-002 Brier: not computable (unscorable).
12. **strict executable CLV:** W4 0.0c (n=1). Others: none.
13. **after-fee P&L:** W4 +58c (n=1). EC-004 worst-case +$0.66 total across 3 structures. Others: none.
14. **confidence intervals:** none exist at these N (n < 3); none were produced for unscorable candidates.
15. **status:** see the scoreboard.
16. **W3-2026-001 abstention prospectively supported?** Cannot be determined: UNSCORABLE. Not supported,
    not refuted.
17. **W3-2026-002 survives its accuracy condition?** Cannot be evaluated: UNSCORABLE. The condition stays
    binding and stays unmet; the candidate remains not a claim.
18. **EC-2026-003 against Kalshi (not merely Gen-1)?** Cannot be evaluated: UNSCORABLE.
19. **W4 true qualifying first observations:** 14; 1 strict pregame.
20. **W4 strict CLV:** 0.0c executable, +1.0c midpoint (n=1).
21. **W4 settlement economics:** +58c after fees on the one eligible contract; no inference possible.
22. **Laver Cup taxonomy:** fixed, explicit, unpriced.
23. **trade capture truncation:** root-caused and fixed in code; effective on the next conductor run.
24. **TENNIS-6 true leakage:** 330 real post-start ledger rows (a pregame-policy defect, now guarded);
    0 used as strict evidence; 0 START_UNKNOWN conflation.
25. **first-ball A/B:** 706 matches (698 B + 8 A; 325 C, 1,031 total).
26. **strict CLV rows:** 2,312.
27. **any candidate ELIGIBLE_FOR_CEO_REVIEW:** no.
28. **real-money authority:** OFF.

## What would make the five unscorable candidates scorable

Not a model change and not a new candidate: run the frozen lanes prospectively and write their output
to an append-only record. Concretely, scheduling `scripts/ops/shadow_board.py` (fair_v1 + selector_v1,
unchanged) on the capture cadence would start W3-001, W3-002 and EC-003's Gen-2 half accumulating from
the day it is switched on; EC-003 additionally needs the Gen-1 probability on the same row, and
EC-001/002 need the market-conditioned lane run live. Evidence would count only from that day forward.
That is a decision for the owner, and it was not taken here.
