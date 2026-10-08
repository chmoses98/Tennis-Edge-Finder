# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-08T14:09Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 25,159): 0-3 14.0%, 3-5 9.6%, 5-10 19.8%, 10-15 15.4%, 15-25 18.6%, 25-40 14.1%, 40+ 8.4%; median gap 12.03 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.3%, Challenger 12.3%, doubles 6.3%). Main tour: ATP 1.7% and WTA 8.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,677): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.2%, STALE_QUOTE 17.3%, BOOK_QUALITY 17.2%, POOR_DATA 8.1%, POSSIBLY_IN_PLAY_QUOTE 5.4%, LIMITED_DATA 4.3%, IN_PLAY_QUOTE 3.5%, IDENTITY_AMBIGUOUS 2.9%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.2%. By class: coverage 39.2%, market_freshness 17.3%, execution 17.2%, data 12.3%, market_freshness/coverage 8.9%, mapping 2.9%, model_calibration_or_unknown 2.0%, model_calibration 0.2%.
* **Stale / settled / in-play**: 55.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,677 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 13.0% of the time and with the model 0.2%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 617.0 points vs 1738.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.132, Gen-2 0.909, Gen-1 ledger 0.95 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 236 model 0.2185 vs Kalshi 0.199; n 52 model 0.282 vs Kalshi 0.1791.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 94,838 model-market comparisons (158,947 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 35,842 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-08T14:02:24.146654+00:00'], shadow board 26,257 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-08T14:02:28.290574+00:00'], Model 4 9,768 rows, 10,969 settled tickers, 2,881 tickers with an external scan.
* By model: {"gen1_ledger": 22821, "gen1_elo": 13193, "fair_v1": 13193, "gen2": 13193, "gen1_sr": 13193, "model4_fundamental": 9627, "model4_conditioned": 9618}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 25,159 | 14.0 | 9.6 | 19.8 | 15.4 | 18.6 | 14.1 | 8.4 | 12.03 | 41.2% | 22.6% |
| MW fair_v1 | 13,193 | 13.3 | 8.7 | 18.3 | 16.2 | 18.4 | 15.0 | 10.1 | 12.96 | 43.5% | 25.0% |
| MW gen1_elo | 13,193 | 12.8 | 8.8 | 19.9 | 15.0 | 19.2 | 14.7 | 9.5 | 12.54 | 43.4% | 24.2% |
| MW gen1_ledger | 11,966 | 14.8 | 10.6 | 21.5 | 14.5 | 18.8 | 13.2 | 6.6 | 10.93 | 38.7% | 19.8% |
| MW gen1_sr | 13,193 | 10.2 | 7.8 | 16.1 | 14.1 | 21.4 | 18.5 | 11.8 | 15.59 | 51.8% | 30.3% |
| MW gen2 | 13,193 | 12.0 | 7.1 | 16.2 | 14.3 | 19.7 | 17.4 | 13.3 | 15.23 | 50.4% | 30.7% |
| all families model4_conditioned | 9,618 | 22.1 | 20.4 | 35.5 | 16.0 | 4.3 | 0.9 | 0.8 | 5.71 | 6.0% | 1.7% |
| all families model4_fundamental | 9,627 | 16.4 | 13.2 | 34.9 | 20.4 | 10.9 | 2.9 | 1.1 | 7.75 | 15.0% | 4.0% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.6%, >=15pp 41.2%, >=20pp 30.8%, >=25pp 22.6%, >=30pp 16.5%, >=40pp 8.4%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.51pp; >=10pp 45.6%, >=25pp 18.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 968 | 27.3 | 15.4 | 24.2 | 18.0 | 12.7 | 1.3 | 1.1 | 6.01 | 15.2% | 2.5% |
| CHALLENGER | 2,252 | 15.5 | 10.8 | 18.4 | 16.2 | 13.0 | 13.1 | 12.9 | 11.9 | 39.0% | 26.1% |
| ITF_MEN | 3,814 | 10.9 | 8.7 | 18.6 | 14.9 | 19.4 | 15.2 | 12.4 | 13.84 | 47.0% | 27.6% |
| ITF_WOMEN | 5,298 | 10.4 | 6.7 | 16.1 | 16.3 | 21.6 | 18.9 | 10.1 | 15.2 | 50.5% | 29.0% |
| WTA | 542 | 24.2 | 9.4 | 25.3 | 16.1 | 17.0 | 6.1 | 2.0 | 7.96 | 25.1% | 8.1% |
| WTA125 | 319 | 11.9 | 6.6 | 22.3 | 26.0 | 14.4 | 16.3 | 2.5 | 11.31 | 33.2% | 18.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 968 | 22.4 | 13.9 | 24.4 | 18.5 | 17.1 | 2.3 | 1.3 | 6.9 | 20.8% | 3.6% |
| CHALLENGER | 2,252 | 15.3 | 7.5 | 18.0 | 13.4 | 18.1 | 14.4 | 13.3 | 13.11 | 45.7% | 27.7% |
| ITF_MEN | 3,814 | 10.7 | 7.3 | 16.8 | 14.7 | 19.8 | 17.6 | 13.1 | 15.3 | 50.5% | 30.7% |
| ITF_WOMEN | 5,298 | 9.1 | 5.9 | 13.1 | 13.2 | 20.5 | 21.3 | 16.8 | 18.87 | 58.7% | 38.2% |
| WTA | 542 | 22.3 | 5.3 | 18.4 | 14.9 | 20.9 | 16.1 | 2.0 | 12.12 | 38.9% | 18.1% |
| WTA125 | 319 | 4.7 | 2.8 | 17.2 | 21.9 | 20.7 | 20.7 | 11.9 | 16.84 | 53.3% | 32.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 968 | 25.6 | 13.0 | 29.6 | 16.1 | 11.2 | 3.2 | 1.2 | 6.61 | 15.6% | 4.4% |
| CHALLENGER | 2,252 | 16.0 | 10.8 | 19.9 | 14.1 | 14.1 | 12.3 | 12.9 | 10.93 | 39.3% | 25.2% |
| ITF_MEN | 3,814 | 10.0 | 8.8 | 18.4 | 14.2 | 20.4 | 15.7 | 12.5 | 14.24 | 48.5% | 28.2% |
| ITF_WOMEN | 5,298 | 9.6 | 6.7 | 17.1 | 15.7 | 23.4 | 18.8 | 8.9 | 15.46 | 51.0% | 27.6% |
| WTA | 542 | 23.1 | 12.9 | 35.6 | 14.4 | 9.2 | 3.5 | 1.3 | 6.92 | 14.0% | 4.8% |
| WTA125 | 319 | 20.7 | 11.6 | 30.4 | 16.9 | 14.7 | 5.0 | 0.6 | 7.99 | 20.4% | 5.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 497 | 28.2 | 22.3 | 37.4 | 10.5 | 1.4 | 0.2 | 0.0 | 4.96 | 1.6% | 0.2% |
| CHALLENGER | 1,462 | 23.0 | 17.2 | 25.7 | 14.1 | 12.4 | 5.5 | 2.0 | 6.67 | 20.0% | 7.6% |
| DOUBLES | 722 | 4.0 | 3.5 | 11.1 | 11.1 | 20.6 | 25.1 | 24.6 | 24.46 | 70.4% | 49.7% |
| ITF_MEN | 3,774 | 14.5 | 8.7 | 20.7 | 15.0 | 20.4 | 12.8 | 8.0 | 11.89 | 41.1% | 20.8% |
| ITF_WOMEN | 4,431 | 11.7 | 9.4 | 19.7 | 14.3 | 22.1 | 17.0 | 5.9 | 13.11 | 44.9% | 22.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 442 | 20.8 | 11.5 | 25.6 | 18.8 | 15.4 | 7.2 | 0.7 | 8.44 | 23.3% | 7.9% |
| WTA125 | 489 | 16.6 | 12.5 | 22.3 | 19.8 | 17.0 | 9.0 | 2.9 | 9.56 | 28.8% | 11.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 963 | 27.3 | 15.3 | 24.2 | 18.1 | 12.7 | 1.4 | 1.1 | 6.01 | 15.2% | 2.5% |
| CHALLENGER | 1,593 | 20.4 | 13.8 | 23.7 | 19.0 | 13.5 | 6.7 | 3.0 | 8.04 | 23.1% | 9.6% |
| ITF_MEN | 2,727 | 13.4 | 10.9 | 22.0 | 16.6 | 19.4 | 12.3 | 5.4 | 11.01 | 37.1% | 17.7% |
| ITF_WOMEN | 3,794 | 12.9 | 8.4 | 18.9 | 18.7 | 23.0 | 15.1 | 3.1 | 12.62 | 41.2% | 18.1% |
| WTA | 539 | 24.1 | 9.5 | 25.4 | 16.0 | 17.1 | 5.9 | 2.0 | 7.94 | 25.1% | 8.0% |
| WTA125 | 307 | 12.4 | 6.8 | 21.8 | 26.4 | 14.7 | 16.3 | 1.6 | 11.31 | 32.6% | 17.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 963 | 22.3 | 13.9 | 24.5 | 18.5 | 17.1 | 2.3 | 1.4 | 6.9 | 20.8% | 3.6% |
| CHALLENGER | 1,593 | 20.1 | 9.9 | 22.7 | 16.4 | 18.5 | 9.7 | 2.8 | 9.08 | 30.9% | 12.5% |
| ITF_MEN | 2,728 | 12.7 | 8.9 | 19.5 | 16.6 | 21.0 | 15.2 | 6.2 | 12.55 | 42.4% | 21.4% |
| ITF_WOMEN | 3,794 | 10.6 | 7.0 | 14.9 | 14.3 | 22.7 | 20.1 | 10.3 | 16.2 | 53.2% | 30.4% |
| WTA | 539 | 22.3 | 5.4 | 18.6 | 15.0 | 20.8 | 16.0 | 2.0 | 12.12 | 38.8% | 18.0% |
| WTA125 | 307 | 4.9 | 2.9 | 17.3 | 22.8 | 19.9 | 21.5 | 10.8 | 16.74 | 52.1% | 32.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 482 | 28.4 | 22.6 | 37.5 | 10.6 | 0.6 | 0.2 | 0.0 | 4.89 | 0.8% | 0.2% |
| CHALLENGER | 1,235 | 25.0 | 19.5 | 27.9 | 13.8 | 11.5 | 2.2 | 0.1 | 5.87 | 13.8% | 2.3% |
| DOUBLES | 665 | 4.1 | 3.5 | 11.3 | 11.0 | 20.9 | 24.8 | 24.5 | 24.32 | 70.2% | 49.3% |
| ITF_MEN | 3,023 | 16.1 | 9.7 | 23.1 | 16.0 | 20.1 | 10.4 | 4.6 | 10.24 | 35.1% | 15.0% |
| ITF_WOMEN | 3,588 | 13.0 | 10.2 | 21.6 | 15.2 | 22.3 | 15.2 | 2.5 | 11.44 | 40.1% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 412 | 21.4 | 12.1 | 26.2 | 18.9 | 15.8 | 5.6 | 0.0 | 8.34 | 21.4% | 5.6% |
| WTA125 | 405 | 18.8 | 13.8 | 24.7 | 22.7 | 15.1 | 4.7 | 0.2 | 8.27 | 20.0% | 4.9% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 722 | 4.0 | 3.5 | 11.1 | 11.1 | 20.6 | 25.1 | 24.6 | 24.46 | 70.4% | 49.7% |
| singles | 11,244 | 15.5 | 11.0 | 22.1 | 14.8 | 18.7 | 12.5 | 5.5 | 10.35 | 36.6% | 17.9% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,070 | 13.4 | 9.6 | 20.5 | 15.5 | 15.9 | 14.7 | 10.5 | 12.18 | 41.1% | 25.1% |
| Hard | 8,832 | 13.4 | 8.5 | 18.1 | 16.2 | 19.0 | 14.7 | 10.0 | 13.02 | 43.8% | 24.7% |
| UNKNOWN | 1,291 | 12.0 | 8.1 | 14.5 | 18.0 | 20.4 | 17.4 | 9.7 | 14.11 | 47.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,791 | 19.2 | 10.9 | 20.3 | 17.1 | 14.8 | 9.7 | 8.1 | 9.95 | 32.6% | 17.9% |
| B | 1,721 | 14.9 | 9.5 | 19.8 | 17.7 | 16.4 | 12.1 | 9.7 | 11.2 | 38.2% | 21.8% |
| C | 2,048 | 12.4 | 10.1 | 19.8 | 15.3 | 18.5 | 14.4 | 9.4 | 12.66 | 42.3% | 23.8% |
| D | 2,522 | 11.1 | 8.3 | 17.2 | 16.3 | 22.1 | 15.2 | 9.7 | 13.98 | 46.9% | 24.8% |
| F | 3,111 | 7.4 | 5.0 | 15.1 | 14.8 | 21.1 | 23.1 | 13.4 | 18.39 | 57.7% | 36.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,264 | 21.4 | 15.6 | 27.4 | 15.8 | 12.5 | 5.3 | 2.0 | 7.1 | 19.8% | 7.3% |
| B | 1,880 | 14.4 | 9.8 | 24.7 | 16.3 | 18.2 | 11.7 | 4.8 | 10.34 | 34.8% | 16.5% |
| C | 2,437 | 12.0 | 8.1 | 18.5 | 13.8 | 20.9 | 16.0 | 10.7 | 13.63 | 47.5% | 26.7% |
| D | 2,010 | 14.1 | 9.2 | 21.0 | 12.8 | 22.0 | 14.4 | 6.4 | 12.11 | 42.9% | 20.8% |
| F | 2,375 | 9.3 | 7.9 | 14.2 | 13.5 | 23.3 | 21.5 | 10.3 | 16.88 | 55.0% | 31.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,297 | 17.9 | 10.1 | 19.5 | 17.3 | 15.1 | 10.2 | 10.0 | 10.69 | 35.3% | 20.2% |
| LIMITED | 3,222 | 14.4 | 10.6 | 20.9 | 15.9 | 17.4 | 13.4 | 7.3 | 11.23 | 38.1% | 20.7% |
| POOR | 5,674 | 9.1 | 6.6 | 16.0 | 15.5 | 21.6 | 19.5 | 11.7 | 16.06 | 52.8% | 31.2% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,068 | 29.8 | 25.4 | 37.1 | 5.7 | 1.6 | 0.3 | 0.0 | 4.54 | 2.0% | 0.3% |
| GAME_SPREAD | 2,025 | 24.7 | 15.5 | 36.7 | 18.2 | 4.5 | 0.2 | 0.1 | 6.18 | 4.9% | 0.4% |
| MATCH_WINNER | 11,966 | 14.8 | 10.6 | 21.5 | 14.5 | 18.8 | 13.2 | 6.6 | 10.93 | 38.7% | 19.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,746 | 30.3 | 19.8 | 30.8 | 10.7 | 6.8 | 1.3 | 0.3 | 4.97 | 8.4% | 1.6% |
| TOTAL_GAMES | 2,992 | 7.3 | 9.0 | 38.3 | 30.6 | 9.6 | 3.1 | 2.2 | 9.52 | 14.9% | 5.3% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,572 | 24.3 | 38.9 | 30.6 | 0.3 | 5.2 | 0.6 | 0.2 | 4.34 | 6.0% | 0.8% |
| GAME_SPREAD | 2,466 | 46.1 | 14.2 | 29.2 | 8.2 | 1.2 | 0.8 | 0.3 | 3.54 | 2.3% | 1.1% |
| TOTAL_GAMES | 3,580 | 3.4 | 6.3 | 44.6 | 37.1 | 5.5 | 1.3 | 1.8 | 9.62 | 8.6% | 3.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,572 | 25.4 | 18.2 | 36.0 | 9.8 | 7.3 | 2.8 | 0.4 | 5.63 | 10.5% | 3.2% |
| GAME_SPREAD | 2,466 | 18.8 | 13.0 | 26.9 | 23.0 | 14.7 | 2.9 | 0.7 | 8.39 | 18.4% | 3.6% |
| TOTAL_GAMES | 3,589 | 6.0 | 8.4 | 39.4 | 29.2 | 11.9 | 3.0 | 2.2 | 9.6 | 17.1% | 5.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 13,193 | 43.5% | 25.0% | 12.96 | 33.5% | 14.6% | 10.42 |
| gen1_elo | 13,193 | 43.4% | 24.2% | 12.54 | 33.1% | 14.1% | 9.99 |
| gen1_sr | 13,193 | 51.8% | 30.3% | 15.59 | 42.8% | 20.0% | 12.72 |
| gen2 | 13,193 | 50.4% | 30.7% | 15.23 | 42.7% | 21.9% | 12.64 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 6,630 | 16.1 | 11.1 | 21.3 | 17.6 | 18.6 | 11.9 | 3.5 | 10.39 | 34.0% | 15.4% |
| STALE | 6,563 | 10.4 | 6.3 | 15.3 | 14.8 | 18.3 | 18.1 | 16.7 | 16.7 | 53.1% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 5,434 | 16.8 | 11.7 | 23.6 | 14.2 | 16.9 | 12.1 | 4.6 | 9.4 | 33.6% | 16.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 25,159 | 5434 | 10102 | 9623 | 25.2 | 159.1 | 1400.4 |
| ge_15pp | 10,365 | 1828 | 3542 | 4995 | 28.8 | 440.2 | 1380.4 |
| ge_25pp | 5,677 | 911 | 1611 | 3155 | 37.4 | 559.8 | 1380.4 |
| lt_10pp | 10,918 | 2832 | 4844 | 3242 | 23.9 | 50.6 | 1230.8 |

Current slate `SL-20261008T140923Z-f1a2e964`: 519 priced rows, quote age at build {'median': 7.4, 'max': 7.4}, freshness {'FRESH': 519}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 2 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.87 | 100.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 3 | 33.3 | 66.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.05 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 680 | 23.8 | 11.6 | 21.2 | 20.6 | 15.2 | 7.2 | 0.4 | 8.03 | 22.8% | 7.6% |
| MARKETS_AGREE | 67 | 79.1 | 20.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.99 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 112 | 0.0 | 1.8 | 31.2 | 33.9 | 22.3 | 10.7 | 0.0 | 12.36 | 33.0% | 10.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 13,193 | 864 (6.6%) | 13.0% | 0.2% | {"EXTERNAL_STALE": 680, "AGREES_WITH_KALSHI": 112, "ALL_AGREE": 67, "EXTERNAL_OUTLIER": 3, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_15pp | 5,738 | 194 (3.4%) | 19.1% | 1.0% | {"EXTERNAL_STALE": 155, "AGREES_WITH_KALSHI": 37, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp | 3,304 | 64 (1.9%) | 18.8% | 0.0% | {"EXTERNAL_STALE": 52, "AGREES_WITH_KALSHI": 12} |
| fair_v1_ge_25pp_pregame_clean | 1,446 | 62 (4.3%) | 19.4% | 0.0% | {"EXTERNAL_STALE": 50, "AGREES_WITH_KALSHI": 12} |
| fair_v1_lt_10pp | 5,317 | 492 (9.2%) | 7.5% | 0.0% | {"EXTERNAL_STALE": 385, "ALL_AGREE": 67, "AGREES_WITH_KALSHI": 37, "EXTERNAL_OUTLIER": 3} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,698 | 11.5 | 8.4 | 19.8 | 15.6 | 21.1 | 14.1 | 9.5 | 13.02 | 44.7% | 23.6% |
| 4-10x | 1,894 | 11.3 | 9.2 | 18.4 | 14.8 | 20.1 | 17.0 | 9.2 | 13.76 | 46.3% | 26.2% |
| <2x | 6,894 | 15.2 | 9.2 | 18.3 | 17.2 | 16.7 | 13.3 | 9.9 | 12.1 | 40.0% | 23.3% |
| >=10x | 1,707 | 10.2 | 6.5 | 15.9 | 14.5 | 19.6 | 20.7 | 12.5 | 16.24 | 52.8% | 33.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,397 | 14.0 | 8.7 | 19.8 | 16.0 | 17.6 | 13.0 | 10.8 | 12.14 | 41.4% | 23.8% |
| 300-1000 | 3,262 | 12.0 | 9.1 | 16.6 | 16.3 | 21.0 | 16.1 | 8.9 | 13.75 | 46.0% | 25.1% |
| <300 | 3,598 | 8.0 | 6.0 | 15.9 | 14.9 | 21.0 | 21.2 | 13.0 | 17.2 | 55.2% | 34.2% |
| >=3000 | 2,936 | 20.3 | 11.6 | 21.6 | 17.9 | 13.4 | 8.4 | 6.8 | 9.04 | 28.7% | 15.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 417 | 0.541 | 0.4102 | 0.4868 | +0.054 | -0.077 | 0.0017 ± 0.0071 |
| ratio 4-10x | 294 | 0.5866 | 0.4441 | 0.5272 | +0.059 | -0.083 | -0.0024 ± 0.0092 |
| ratio <2x | 880 | 0.544 | 0.4178 | 0.4602 | +0.084 | -0.042 | 0.0108 ± 0.0049 |
| ratio >=10x | 283 | 0.5499 | 0.3775 | 0.4417 | +0.108 | -0.064 | 0.014 ± 0.0106 |
| thinner_sample 1000-3000 | 502 | 0.5477 | 0.4239 | 0.4681 | +0.080 | -0.044 | 0.0062 ± 0.0063 |
| thinner_sample 300-1000 | 520 | 0.5712 | 0.4312 | 0.5038 | +0.067 | -0.073 | -0.0002 ± 0.0069 |
| thinner_sample <300 | 579 | 0.5451 | 0.3827 | 0.4663 | +0.079 | -0.084 | 0.0091 ± 0.0071 |
| thinner_sample >=3000 | 273 | 0.5306 | 0.4303 | 0.4432 | +0.087 | -0.013 | 0.0191 ± 0.0072 |
| data_status ADEQUATE | 484 | 0.5303 | 0.424 | 0.438 | +0.092 | -0.014 | 0.0132 ± 0.0056 |
| data_status LIMITED | 478 | 0.5652 | 0.4333 | 0.5042 | +0.061 | -0.071 | -0.0001 ± 0.0069 |
| data_status POOR | 912 | 0.5544 | 0.3989 | 0.477 | +0.077 | -0.078 | 0.0079 ± 0.0055 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 277 | 0.1823 | 0.1836 | -0.0013 ± 0.0009 | 0.5396 | 0.5429 | 0.4931 | 0.4787 | 0.5162 | -0.075 ± 0.0271 | -0.01 (3) |
| 3-5 | 189 | 0.1821 | 0.183 | -0.0009 ± 0.0025 | 0.5421 | 0.5422 | 0.5116 | 0.4716 | 0.4974 | -0.072 ± 0.0317 | 0.02 (1) |
| 5-10 | 389 | 0.1982 | 0.2013 | -0.0030 ± 0.0034 | 0.582 | 0.5896 | 0.5192 | 0.4451 | 0.4936 | -0.083 ± 0.0238 | -0.0125 (4) |
| 10-15 | 327 | 0.2147 | 0.2107 | +0.0040 ± 0.0064 | 0.6165 | 0.6033 | 0.5295 | 0.4054 | 0.4495 | -0.094 ± 0.0254 | -0.0633 (3) |
| 15-25 | 404 | 0.2217 | 0.2118 | +0.0099 ± 0.009 | 0.6349 | 0.6111 | 0.575 | 0.3793 | 0.4505 | -0.084 ± 0.0228 | -0.0133 (6) |
| 25-40 | 236 | 0.2185 | 0.199 | +0.0194 ± 0.0173 | 0.6269 | 0.5726 | 0.6451 | 0.336 | 0.4576 | -0.078 ± 0.0257 | -0.01 (1) |
| 40+ | 52 | 0.282 | 0.1791 | +0.1028 ± 0.0518 | 0.7673 | 0.5347 | 0.7592 | 0.3118 | 0.4231 | -0.120 ± 0.0507 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1346 | 0.1644 | 0.1652 | -0.0007 ± 0.0004 | 0.497 | 0.4977 | 0.4773 | 0.4626 | 0.4941 | -0.033 ± 0.0113 | -0.0188 (8) |
| 3-5 | 914 | 0.1903 | 0.1869 | +0.0033 ± 0.0012 | 0.5623 | 0.5488 | 0.4807 | 0.4411 | 0.4147 | -0.088 ± 0.0146 | 0.02 (1) |
| 5-10 | 1954 | 0.1913 | 0.1901 | +0.0011 ± 0.0015 | 0.5648 | 0.5609 | 0.4925 | 0.4187 | 0.4437 | -0.048 ± 0.01 | -0.0082 (17) |
| 10-15 | 1716 | 0.2024 | 0.1863 | +0.0161 ± 0.0026 | 0.5903 | 0.5458 | 0.4803 | 0.3557 | 0.3537 | -0.075 ± 0.0104 | -0.0475 (4) |
| 15-25 | 2075 | 0.2 | 0.1642 | +0.0358 ± 0.0035 | 0.5894 | 0.4892 | 0.4897 | 0.2937 | 0.3002 | -0.071 ± 0.0089 | -0.0048 (29) |
| 25-40 | 1776 | 0.2161 | 0.1232 | +0.0929 ± 0.0052 | 0.6243 | 0.3818 | 0.5266 | 0.2133 | 0.2241 | -0.060 ± 0.008 | -0.01 (1) |
| 40+ | 1214 | 0.3673 | 0.0466 | +0.3207 ± 0.0068 | 0.9586 | 0.1808 | 0.6211 | 0.1065 | 0.0626 | -0.080 ± 0.0058 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 220 | 0.1926 | 0.1927 | -0.0002 ± 0.001 | 0.5681 | 0.5685 | 0.4944 | 0.4791 | 0.4818 | -0.106 ± 0.0314 | -0.01 (1) |
| 3-5 | 143 | 0.2013 | 0.2022 | -0.0009 ± 0.003 | 0.5804 | 0.5852 | 0.5187 | 0.4788 | 0.5035 | -0.068 ± 0.0396 | 0.02 (1) |
| 5-10 | 323 | 0.1907 | 0.1887 | +0.0020 ± 0.0036 | 0.563 | 0.5587 | 0.5654 | 0.4902 | 0.5108 | -0.094 ± 0.0252 | -0.01 (4) |
| 10-15 | 319 | 0.2151 | 0.2086 | +0.0064 ± 0.0064 | 0.6159 | 0.6038 | 0.5871 | 0.4626 | 0.5047 | -0.100 ± 0.0267 | -0.05 (4) |
| 15-25 | 449 | 0.2224 | 0.2049 | +0.0175 ± 0.0085 | 0.6318 | 0.5907 | 0.5999 | 0.4023 | 0.4633 | -0.099 ± 0.0219 | -0.01 (5) |
| 25-40 | 306 | 0.2693 | 0.2026 | +0.0667 ± 0.0162 | 0.7517 | 0.586 | 0.6716 | 0.3579 | 0.4085 | -0.138 ± 0.0258 | -0.025 (2) |
| 40+ | 114 | 0.3379 | 0.1898 | +0.1482 ± 0.0396 | 0.9543 | 0.5545 | 0.7646 | 0.2842 | 0.386 | -0.061 ± 0.0377 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1249 | 0.1718 | 0.1725 | -0.0006 ± 0.0004 | 0.5159 | 0.5172 | 0.4939 | 0.4795 | 0.5044 | -0.035 ± 0.0123 | -0.0217 (6) |
| 3-5 | 773 | 0.1883 | 0.1853 | +0.0030 ± 0.0012 | 0.5481 | 0.5415 | 0.5197 | 0.4799 | 0.4631 | -0.071 ± 0.0157 | 0.02 (1) |
| 5-10 | 1717 | 0.1825 | 0.1793 | +0.0032 ± 0.0015 | 0.5462 | 0.5345 | 0.5193 | 0.4457 | 0.4613 | -0.052 ± 0.0104 | -0.01 (5) |
| 10-15 | 1519 | 0.1955 | 0.1824 | +0.0132 ± 0.0027 | 0.5779 | 0.5348 | 0.5258 | 0.4015 | 0.4134 | -0.066 ± 0.0112 | -0.02 (14) |
| 15-25 | 2168 | 0.2129 | 0.171 | +0.0419 ± 0.0035 | 0.6203 | 0.5075 | 0.5294 | 0.3341 | 0.328 | -0.087 ± 0.009 | -0.0026 (27) |
| 25-40 | 1989 | 0.2469 | 0.1388 | +0.1080 ± 0.0053 | 0.6988 | 0.4225 | 0.5625 | 0.2455 | 0.2348 | -0.086 ± 0.0084 | -0.015 (6) |
| 40+ | 1580 | 0.3992 | 0.0699 | +0.3293 ± 0.0076 | 1.0462 | 0.2429 | 0.6684 | 0.1317 | 0.107 | -0.067 ± 0.0064 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 285 | 0.1899 | 0.1925 | -0.0026 ± 0.0009 | 0.5581 | 0.5652 | 0.5007 | 0.4855 | 0.5509 | -0.026 ± 0.0262 | -0.0133 (6) |
| 3-5 | 200 | 0.1802 | 0.1794 | +0.0009 ± 0.0024 | 0.5337 | 0.5314 | 0.4939 | 0.4547 | 0.465 | -0.115 ± 0.0319 | -0.01 (1) |
| 5-10 | 396 | 0.1946 | 0.1958 | -0.0011 ± 0.0034 | 0.5742 | 0.5758 | 0.5108 | 0.4369 | 0.4773 | -0.083 ± 0.0232 | -0.01 (4) |
| 10-15 | 313 | 0.2154 | 0.214 | +0.0014 ± 0.0065 | 0.6212 | 0.6127 | 0.5412 | 0.418 | 0.476 | -0.086 ± 0.0258 | -0.044 (5) |
| 15-25 | 396 | 0.2236 | 0.2065 | +0.0170 ± 0.0089 | 0.6434 | 0.597 | 0.5811 | 0.3875 | 0.4394 | -0.104 ± 0.0226 | -0.03 (1) |
| 25-40 | 238 | 0.202 | 0.2065 | -0.0045 ± 0.0171 | 0.588 | 0.5919 | 0.6518 | 0.3407 | 0.5 | -0.050 ± 0.0251 | 0.0 (1) |
| 40+ | 46 | 0.3062 | 0.1787 | +0.1275 ± 0.0561 | 0.8241 | 0.5334 | 0.752 | 0.2995 | 0.3913 | -0.131 ± 0.0563 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1299 | 0.179 | 0.1799 | -0.0009 ± 0.0004 | 0.5315 | 0.5333 | 0.487 | 0.4719 | 0.4981 | -0.035 ± 0.0118 | -0.0183 (23) |
| 3-5 | 917 | 0.183 | 0.1806 | +0.0024 ± 0.0011 | 0.541 | 0.5358 | 0.4712 | 0.432 | 0.4209 | -0.082 ± 0.0146 | -0.0243 (7) |
| 5-10 | 2028 | 0.1832 | 0.1799 | +0.0033 ± 0.0014 | 0.5471 | 0.5354 | 0.4833 | 0.409 | 0.425 | -0.052 ± 0.0095 | -0.01 (18) |
| 10-15 | 1627 | 0.1979 | 0.1827 | +0.0152 ± 0.0026 | 0.5807 | 0.5355 | 0.4959 | 0.3725 | 0.3712 | -0.076 ± 0.0105 | -0.03 (9) |
| 15-25 | 2251 | 0.2034 | 0.1669 | +0.0365 ± 0.0034 | 0.5991 | 0.4966 | 0.4939 | 0.2982 | 0.3043 | -0.068 ± 0.0087 | -0.03 (2) |
| 25-40 | 1723 | 0.2121 | 0.1205 | +0.0916 ± 0.0053 | 0.6148 | 0.3731 | 0.5227 | 0.2053 | 0.2234 | -0.057 ± 0.0079 | 0.0 (1) |
| 40+ | 1150 | 0.3816 | 0.0477 | +0.3339 ± 0.0072 | 0.9981 | 0.1846 | 0.6285 | 0.1071 | 0.0591 | -0.084 ± 0.0061 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 568 | 0.2009 | 0.2009 | +0.0000 ± 0.0006 | 0.5847 | 0.584 | 0.4994 | 0.4845 | 0.4842 | -0.050 ± 0.0188 | -0.0226 (46) |
| 3-5 | 424 | 0.1954 | 0.194 | +0.0013 ± 0.0017 | 0.5721 | 0.5672 | 0.4796 | 0.44 | 0.4458 | -0.050 ± 0.0213 | -0.0058 (33) |
| 5-10 | 874 | 0.189 | 0.1837 | +0.0053 ± 0.0022 | 0.5614 | 0.5475 | 0.4779 | 0.4044 | 0.4062 | -0.059 ± 0.0148 | -0.0049 (73) |
| 10-15 | 568 | 0.2031 | 0.1931 | +0.0100 ± 0.0046 | 0.5953 | 0.5676 | 0.4799 | 0.3571 | 0.3768 | -0.045 ± 0.0184 | 0.0014 (64) |
| 15-25 | 769 | 0.2333 | 0.209 | +0.0243 ± 0.0065 | 0.6609 | 0.6034 | 0.5459 | 0.3516 | 0.3875 | -0.054 ± 0.0166 | -0.0216 (58) |
| 25-40 | 430 | 0.244 | 0.183 | +0.0610 ± 0.0128 | 0.6855 | 0.539 | 0.6219 | 0.3084 | 0.3651 | -0.073 ± 0.0193 | -0.0216 (25) |
| 40+ | 144 | 0.3394 | 0.185 | +0.1544 ± 0.0364 | 0.9642 | 0.5477 | 0.7737 | 0.2811 | 0.3958 | -0.043 ± 0.032 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1629 | 0.1881 | 0.1879 | +0.0002 ± 0.0004 | 0.5529 | 0.5513 | 0.4975 | 0.4822 | 0.48 | -0.047 ± 0.0107 | -0.0155 (82) |
| 3-5 | 1161 | 0.1856 | 0.1828 | +0.0028 ± 0.001 | 0.5456 | 0.5391 | 0.4921 | 0.4525 | 0.4401 | -0.061 ± 0.0126 | -0.0148 (63) |
| 5-10 | 2409 | 0.1864 | 0.1782 | +0.0082 ± 0.0013 | 0.5555 | 0.5327 | 0.4735 | 0.3998 | 0.3848 | -0.069 ± 0.0087 | -0.0087 (125) |
| 10-15 | 1646 | 0.1978 | 0.1847 | +0.0131 ± 0.0026 | 0.5826 | 0.5471 | 0.4928 | 0.3699 | 0.3773 | -0.053 ± 0.0105 | -0.0053 (105) |
| 15-25 | 2128 | 0.2256 | 0.1959 | +0.0296 ± 0.0038 | 0.6495 | 0.5711 | 0.5384 | 0.3431 | 0.3656 | -0.054 ± 0.0097 | -0.0255 (106) |
| 25-40 | 1490 | 0.2366 | 0.1583 | +0.0783 ± 0.0065 | 0.6704 | 0.4732 | 0.5841 | 0.2692 | 0.304 | -0.057 ± 0.01 | -0.0206 (47) |
| 40+ | 712 | 0.3552 | 0.1068 | +0.2484 ± 0.0131 | 0.9709 | 0.3373 | 0.6754 | 0.1698 | 0.1896 | -0.056 ± 0.0113 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1874 | 1.132 ± 0.067 | 1.237 | 0.17 | 0.1682 | 0.2071 | 0.1998 |
| gen2 | 1874 | 0.909 ± 0.058 | 1.163 | 0.1869 | 0.1675 | 0.2253 | 0.1998 |
| gen1_elo | 1874 | 1.118 ± 0.066 | 1.228 | 0.1737 | 0.1687 | 0.2056 | 0.1998 |
| gen1_sr | 1874 | 1.126 ± 0.075 | 1.244 | 0.1443 | 0.1701 | 0.221 | 0.1996 |
| gen1_ledger | 3777 | 0.95 ± 0.043 | 1.095 | 0.1714 | 0.1915 | 0.2146 | 0.194 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 10,365)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,832 | 27.3% |
| STALE_QUOTE | market_freshness | 2,193 | 21.2% |
| BOOK_QUALITY | execution | 1,844 | 17.8% |
| POOR_DATA | data | 1,099 | 10.6% |
| LIMITED_DATA | data | 738 | 7.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 564 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 463 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 310 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 284 | 2.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 38 | 0.4% |

Cause class: coverage 27.3%, market_freshness 21.2%, execution 17.8%, data 17.7%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.5%, mapping 2.7%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.4%, START_UNVERIFIABLE 96.2%, LOW_DATA_QUALITY 69.2%, STALE_PLAYER_DATA 58.0%, THIN_PLAYER_HISTORY 57.8%, STALE_KALSHI_QUOTE 48.2%, MODEL_INTERNAL_DISAGREEMENT 37.3%, ASYMMETRIC_SAMPLE_SIZE 31.0%, WIDE_SPREAD 23.9%, MODEL_HIGH_UNCERTAINTY 16.1%, PLAYER_IDENTITY_RISK 11.1%, LEVEL_TRANSFER_RISK 9.0%, EVENT_MAPPING_RISK 7.7%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.2%, EXTERNAL_MARKET_REJECTION 0.6%, UNKNOWN 0.5%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.9%, POST_SETTLEMENT_OBSERVATION 27.3%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,677)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,227 | 39.2% |
| STALE_QUOTE | market_freshness | 980 | 17.3% |
| BOOK_QUALITY | execution | 976 | 17.2% |
| POOR_DATA | data | 458 | 8.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 308 | 5.4% |
| LIMITED_DATA | data | 243 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 196 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 167 | 2.9% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 111 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 11 | 0.2% |

Cause class: coverage 39.2%, market_freshness 17.3%, execution 17.2%, data 12.3%, market_freshness/coverage 8.9%, mapping 2.9%, model_calibration_or_unknown 2.0%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.7%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 71.8%, THIN_PLAYER_HISTORY 59.4%, STALE_KALSHI_QUOTE 55.6%, STALE_PLAYER_DATA 53.1%, MODEL_INTERNAL_DISAGREEMENT 38.9%, ASYMMETRIC_SAMPLE_SIZE 32.8%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 17.3%, PLAYER_IDENTITY_RISK 13.9%, EVENT_MAPPING_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 7.7%, LEVEL_TRANSFER_RISK 7.7%, MODEL_CALIBRATION_OUTLIER 4.0%, EXTERNAL_MARKET_REJECTION 0.3%, UNKNOWN 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.1%, POST_SETTLEMENT_OBSERVATION 39.2%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4724, "IDENTITY_AMBIGUOUS": 953}; ticker orientation: {"VERIFIED": 5677}.

Checks: discipline:AMBIGUOUS 359, discipline:PASS 5318, identity_confidence:AMBIGUOUS 790, identity_confidence:PASS 4887, level_mapping:NA 371, level_mapping:PASS 5306, market_pair:AMBIGUOUS 220, market_pair:NA 129, market_pair:PASS 5328, model_complement:NA 96, model_complement:PASS 5581, namesake:PASS 5677, physical_match_id:NA 2373, physical_match_id:PASS 3304, player_ids:PASS 5677, same_pair_other_event:PASS 5677, ticker_orientation:PASS 5677

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,465 | 1.7% | 1.7% | 0.4% | {"market_freshness": 20, "execution": 5} | 5.52 | 0.2167 / 0.2062 (139) | 20.3% | 0.1% | 5.9% | 1.4% |
| CHALLENGER | 3,714 | 18.8% | 6.4% | 12.3% | {"coverage": 433, "market_freshness": 108, "market_freshness/coverage": 84, "model_calibration_or_unknown": 41, "data": 25, "execution": 4, "model_calibration": 3} | 6.8 | 0.2214 / 0.2029 (862) | 46.1% | 4.8% | 1.7% | 23.9% |
| DOUBLES | 722 | 49.7% | 49.3% | 6.3% | {"execution": 140, "market_freshness": 106, "mapping": 82, "market_freshness/coverage": 24, "coverage": 7} | 24.32 | 0.31 / 0.2242 (200) | 32.4% | 0.0% | 100.0% | 7.9% |
| ITF_MEN | 7,588 | 24.2% | 16.3% | 32.4% | {"coverage": 744, "execution": 384, "data": 269, "market_freshness": 264, "market_freshness/coverage": 158, "mapping": 19, "model_calibration_or_unknown": 1} | 10.64 | 0.2098 / 0.1916 (1897) | 38.5% | 55.0% | 6.2% | 24.2% |
| ITF_WOMEN | 9,729 | 26.2% | 17.9% | 44.9% | {"coverage": 1026, "execution": 426, "market_freshness": 425, "data": 383, "market_freshness/coverage": 197, "mapping": 60, "model_calibration_or_unknown": 23, "model_calibration": 7} | 12.12 | 0.2005 / 0.1916 (2083) | 39.7% | 58.5% | 9.9% | 24.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 984 | 8.0% | 6.9% | 1.4% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.16 | 0.2058 / 0.2016 (147) | 33.9% | 2.1% | 1.2% | 3.4% |
| WTA125 | 808 | 14.6% | 10.5% | 2.1% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 21, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 1} | 9.91 | 0.2277 / 0.2132 (281) | 26.6% | 6.6% | 4.2% | 11.9% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 9 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 10 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 11 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 16 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 17 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 19 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 20 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 21 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 22 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 23 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 24 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 20% | +75 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 26 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 27 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 28 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 29 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 30 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 31 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 32 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 33 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 34 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 799 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 37 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 38 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 39 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 40 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 41 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 26 min (AGING); no external reference |
| 42 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 43 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 44 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 45 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 49 | `KXITFWMATCH-26OCT08YANZHE-YAN` | ITF_WOMEN | fair_v1 | 90% / 18% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 61 min before settlement (in-play print); quote age at model time 166 min (STALE); data LIMITED (grade C, thinner serve sample 1212.0, ratio 2.36); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9817, "by_level_share_of_ge_25pp": {"ATP": 0.0044, "CHALLENGER": 0.123, "DOUBLES": 0.0632, "ITF_MEN": 0.3239, "ITF_WOMEN": 0.4487, "OTHER": 0.0021, "WTA": 0.0139, "WTA125": 0.0208}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5558, "share_primary_cause_market_settled_or_in_play": 0.4811, "share_primary_cause_stale_quote_only": 0.1726}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5677, "identity_ambiguous_share": 0.1679, "ticker_orientation": {"VERIFIED": 5677}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3304, "with_external": 64, "coverage": 0.0194, "external_status": {"EXTERNAL_STALE": 52, "AGREES_WITH_KALSHI": 12}, "triangulation": {"INSUFFICIENT_INPUTS": 52, "MODEL_LONE_OUTLIER": 12}, "share_external_agrees_with_kalshi": 0.1875, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1446, "with_external": 62, "coverage": 0.0429, "external_status": {"EXTERNAL_STALE": 50, "AGREES_WITH_KALSHI": 12}, "triangulation": {"INSUFFICIENT_INPUTS": 50, "MODEL_LONE_OUTLIER": 12}, "share_external_agrees_with_kalshi": 0.1935, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 617.0, "median_sample_ratio": 2.33, "median_min_matches": 20.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1763, "data_status": {"POOR": 2954, "LIMITED": 1708, "ADEQUATE": 1015}, "comparison_lt_10pp": {"median_thinner_serve_points": 1738.0, "median_sample_ratio": 1.76, "median_min_matches": 72.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 417, "model_minus_observed": 0.0542, "kalshi_minus_observed": -0.0766, "brier_diff_model_minus_kalshi": 0.0017}, "4-10x": {"n": 294, "model_minus_observed": 0.0593, "kalshi_minus_observed": -0.0831, "brier_diff_model_minus_kalshi": -0.0024}, "<2x": {"n": 880, "model_minus_observed": 0.0838, "kalshi_minus_observed": -0.0424, "brier_diff_model_minus_kalshi": 0.0108}, ">=10x": {"n": 283, "model_minus_observed": 0.1082, "kalshi_minus_observed": -0.0642, "brier_diff_model_minus_kalshi": 0.014}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1874, "model": {"intercept": -0.572, "slope": 0.909, "slope_se": 0.058}, "kalshi_mid_same_rows": {"intercept": 0.244, "slope": 1.163, "slope_se": 0.068}, "mean_extremity_model": 0.1869, "mean_extremity_kalshi": 0.1675, "model_brier": 0.2253, "kalshi_brier": 0.1998, "brier_diff_model_minus_kalshi": 0.0255, "brier_diff_se": 0.0044, "model_logloss": 0.645, "kalshi_logloss": 0.5814}, "fair_v1": {"n": 1874, "model": {"intercept": -0.404, "slope": 1.132, "slope_se": 0.067}, "kalshi_mid_same_rows": {"intercept": 0.37, "slope": 1.237, "slope_se": 0.07}, "mean_extremity_model": 0.17, "mean_extremity_kalshi": 0.1682, "model_brier": 0.2071, "kalshi_brier": 0.1998, "brier_diff_model_minus_kalshi": 0.0072, "brier_diff_se": 0.0035, "model_logloss": 0.5999, "kalshi_logloss": 0.5813}, "gen1_elo": {"n": 1874, "model": {"intercept": -0.373, "slope": 1.118, "slope_se": 0.066}, "kalshi_mid_same_rows": {"intercept": 0.382, "slope": 1.228, "slope_se": 0.069}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1687, "model_brier": 0.2056, "kalshi_brier": 0.1998, "brier_diff_model_minus_kalshi": 0.0058, "brier_diff_se": 0.0035, "model_logloss": 0.5978, "kalshi_logloss": 0.5811}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2504, "share_ge_15": 0.4349, "median_abs_gap": 12.96, "n": 13193}, "gen1_elo": {"share_ge_25": 0.242, "share_ge_15": 0.4342, "median_abs_gap": 12.54, "n": 13193}, "gen1_sr": {"share_ge_25": 0.3033, "share_ge_15": 0.5177, "median_abs_gap": 15.59, "n": 13193}, "gen2": {"share_ge_25": 0.3071, "share_ge_15": 0.5038, "median_abs_gap": 15.23, "n": 13193}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1457, "share_ge_15": 0.3349, "median_abs_gap": 10.42, "n": 9923}, "gen1_elo": {"share_ge_25": 0.1414, "share_ge_15": 0.3311, "median_abs_gap": 9.99, "n": 9922}, "gen1_sr": {"share_ge_25": 0.2002, "share_ge_15": 0.4281, "median_abs_gap": 12.72, "n": 9923}, "gen2": {"share_ge_25": 0.2185, "share_ge_15": 0.4268, "median_abs_gap": 12.64, "n": 9924}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0171, "share_ge_25_pregame_clean": 0.0173}, "WTA": {"median_abs_gap_pregame_clean": 8.16, "share_ge_25_all": 0.0803, "share_ge_25_pregame_clean": 0.0694}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2357, "share_within_10pp_all": 0.434, "share_within_10pp_pregame_clean": 0.4979, "corr_model_vs_mid_pregame_clean": 0.8509}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 277, "model_brier": 0.1823, "kalshi_brier": 0.1836, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 327, "model_brier": 0.2147, "kalshi_brier": 0.2107, "brier_diff_model_minus_kalshi": 0.004}, "15-25": {"n_settled": 404, "model_brier": 0.2217, "kalshi_brier": 0.2118, "brier_diff_model_minus_kalshi": 0.0099}, "25-40": {"n_settled": 236, "model_brier": 0.2185, "kalshi_brier": 0.199, "brier_diff_model_minus_kalshi": 0.0194}, "3-5": {"n_settled": 189, "model_brier": 0.1821, "kalshi_brier": 0.183, "brier_diff_model_minus_kalshi": -0.0009}, "40+": {"n_settled": 52, "model_brier": 0.282, "kalshi_brier": 0.1791, "brier_diff_model_minus_kalshi": 0.1028}, "5-10": {"n_settled": 389, "model_brier": 0.1982, "kalshi_brier": 0.2013, "brier_diff_model_minus_kalshi": -0.003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 200, "model_brier": 0.31, "kalshi_brier": 0.2242, "brier_diff_model_minus_kalshi": 0.0858, "brier_diff_se": 0.0222, "corr_model_outcome": 0.0228, "corr_kalshi_outcome": 0.3477}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
