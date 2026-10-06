# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-06T19:00Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 19,363): 0-3 13.4%, 3-5 9.5%, 5-10 19.5%, 10-15 15.2%, 15-25 18.7%, 25-40 14.8%, 40+ 8.8%; median gap 12.31 pp.
* **Where the extremes live**: 97.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.1%, Challenger 13.5%, doubles 4.5%). Main tour: ATP 2.2% and WTA 8.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 4,566): MARKET_ALREADY_SETTLED_WHEN_PRICED 40.6%, STALE_QUOTE 20.2%, BOOK_QUALITY 15.9%, POOR_DATA 8.1%, POSSIBLY_IN_PLAY_QUOTE 4.7%, LIMITED_DATA 3.1%, IN_PLAY_QUOTE 2.8%, IDENTITY_AMBIGUOUS 2.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 40.6%, market_freshness 20.2%, execution 15.9%, data 11.2%, market_freshness/coverage 7.5%, mapping 2.5%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 60.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 4,566 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 5.0% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 585.0 points vs 1833.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.133, Gen-2 0.921, Gen-1 ledger 0.924 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 171 model 0.2124 vs Kalshi 0.1967; n 39 model 0.3105 vs Kalshi 0.1436.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 70,837 model-market comparisons (119,525 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 28,180 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-06T18:51:24.571273+00:00'], shadow board 19,786 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-06T18:51:28.735514+00:00'], Model 4 6,771 rows, 9,455 settled tickers, 2,147 tickers with an external scan.
* By model: {"gen1_ledger": 17776, "gen1_elo": 9942, "fair_v1": 9942, "gen2": 9942, "gen1_sr": 9942, "model4_fundamental": 6651, "model4_conditioned": 6642}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 19,363 | 13.4 | 9.5 | 19.5 | 15.2 | 18.7 | 14.8 | 8.8 | 12.31 | 42.3% | 23.6% |
| MW fair_v1 | 9,942 | 12.8 | 9.0 | 18.2 | 15.6 | 18.2 | 15.6 | 10.5 | 13.09 | 44.3% | 26.1% |
| MW gen1_elo | 9,942 | 12.7 | 8.7 | 19.7 | 14.7 | 19.1 | 15.2 | 9.9 | 12.74 | 44.2% | 25.1% |
| MW gen1_ledger | 9,421 | 14.2 | 10.0 | 20.9 | 14.8 | 19.3 | 13.8 | 7.0 | 11.53 | 40.2% | 20.9% |
| MW gen1_sr | 9,942 | 9.7 | 7.6 | 16.0 | 14.1 | 21.8 | 18.6 | 12.2 | 15.96 | 52.6% | 30.9% |
| MW gen2 | 9,942 | 11.2 | 7.0 | 16.1 | 14.4 | 19.9 | 17.5 | 13.9 | 15.53 | 51.3% | 31.4% |
| all families model4_conditioned | 6,642 | 21.6 | 20.1 | 33.4 | 17.0 | 5.9 | 1.1 | 1.0 | 5.91 | 8.0% | 2.1% |
| all families model4_fundamental | 6,651 | 16.4 | 12.9 | 33.8 | 20.2 | 11.5 | 3.7 | 1.5 | 7.88 | 16.7% | 5.2% |

Configurable thresholds (primary): >=5pp 77.1%, >=10pp 57.6%, >=15pp 42.3%, >=20pp 32.1%, >=25pp 23.6%, >=30pp 17.3%, >=40pp 8.8%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.77pp; >=10pp 46.5%, >=25pp 19.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 670 | 24.5 | 18.4 | 25.2 | 16.7 | 11.8 | 1.8 | 1.6 | 5.92 | 15.2% | 3.4% |
| CHALLENGER | 1,934 | 14.4 | 11.1 | 18.1 | 16.3 | 13.6 | 13.3 | 13.1 | 12.06 | 40.1% | 26.5% |
| ITF_MEN | 2,760 | 10.4 | 8.4 | 18.4 | 14.5 | 18.8 | 16.1 | 13.6 | 14.23 | 48.4% | 29.6% |
| ITF_WOMEN | 3,817 | 10.2 | 6.9 | 16.0 | 15.2 | 21.5 | 20.0 | 10.1 | 15.68 | 51.6% | 30.1% |
| WTA | 498 | 22.5 | 10.0 | 24.5 | 15.7 | 18.5 | 6.6 | 2.2 | 8.38 | 27.3% | 8.8% |
| WTA125 | 263 | 13.7 | 6.8 | 19.8 | 25.9 | 14.1 | 16.7 | 3.0 | 11.47 | 33.8% | 19.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 670 | 19.2 | 16.1 | 26.4 | 17.6 | 15.5 | 3.1 | 1.9 | 6.9 | 20.6% | 5.1% |
| CHALLENGER | 1,934 | 14.5 | 6.9 | 17.7 | 13.8 | 19.0 | 14.8 | 13.3 | 13.76 | 47.1% | 28.1% |
| ITF_MEN | 2,760 | 9.8 | 6.8 | 16.3 | 14.8 | 19.7 | 18.0 | 14.6 | 15.73 | 52.4% | 32.6% |
| ITF_WOMEN | 3,817 | 8.2 | 6.2 | 13.3 | 13.1 | 21.0 | 20.9 | 17.3 | 18.91 | 59.2% | 38.2% |
| WTA | 498 | 20.9 | 5.0 | 16.7 | 15.9 | 21.9 | 17.5 | 2.2 | 13.18 | 41.6% | 19.7% |
| WTA125 | 263 | 5.3 | 1.9 | 16.7 | 23.6 | 20.5 | 19.0 | 12.9 | 16.74 | 52.5% | 31.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 670 | 24.5 | 12.4 | 30.4 | 16.4 | 10.0 | 4.5 | 1.8 | 7.04 | 16.3% | 6.3% |
| CHALLENGER | 1,934 | 15.9 | 10.8 | 20.7 | 13.7 | 13.5 | 12.2 | 13.2 | 10.53 | 38.8% | 25.3% |
| ITF_MEN | 2,760 | 9.2 | 8.4 | 17.9 | 14.2 | 20.3 | 16.3 | 13.6 | 15.04 | 50.2% | 29.9% |
| ITF_WOMEN | 3,817 | 9.6 | 6.5 | 16.2 | 15.0 | 23.9 | 19.9 | 8.9 | 16.35 | 52.6% | 28.7% |
| WTA | 498 | 22.9 | 13.1 | 34.3 | 14.5 | 10.0 | 3.8 | 1.4 | 7.0 | 15.3% | 5.2% |
| WTA125 | 263 | 21.3 | 11.0 | 26.2 | 17.9 | 17.1 | 5.7 | 0.8 | 7.99 | 23.6% | 6.5% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 362 | 29.3 | 19.6 | 38.1 | 11.6 | 1.4 | 0.0 | 0.0 | 5.22 | 1.4% | 0.0% |
| CHALLENGER | 1,312 | 22.4 | 15.6 | 27.0 | 14.6 | 12.5 | 5.8 | 2.2 | 6.83 | 20.5% | 8.0% |
| DOUBLES | 468 | 4.7 | 3.2 | 13.5 | 10.9 | 24.1 | 20.1 | 23.5 | 22.7 | 67.7% | 43.6% |
| ITF_MEN | 2,932 | 13.5 | 8.4 | 18.5 | 15.3 | 20.6 | 14.4 | 9.4 | 12.84 | 44.3% | 23.7% |
| ITF_WOMEN | 3,335 | 10.2 | 8.7 | 18.3 | 14.2 | 22.9 | 18.9 | 6.8 | 14.28 | 48.6% | 25.7% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 418 | 18.9 | 10.5 | 26.1 | 19.9 | 16.3 | 7.7 | 0.7 | 8.86 | 24.6% | 8.4% |
| WTA125 | 445 | 14.8 | 11.7 | 22.0 | 19.8 | 18.6 | 9.9 | 3.1 | 10.26 | 31.7% | 13.0% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 666 | 24.5 | 18.2 | 25.2 | 16.8 | 11.9 | 1.8 | 1.6 | 5.93 | 15.3% | 3.5% |
| CHALLENGER | 1,381 | 18.6 | 14.0 | 23.2 | 18.9 | 14.8 | 7.2 | 3.3 | 8.6 | 25.3% | 10.5% |
| ITF_MEN | 1,960 | 12.7 | 10.8 | 22.1 | 16.0 | 18.6 | 13.3 | 6.5 | 11.11 | 38.4% | 19.8% |
| ITF_WOMEN | 2,756 | 12.8 | 8.7 | 18.7 | 17.2 | 22.9 | 16.3 | 3.5 | 12.92 | 42.6% | 19.8% |
| WTA | 496 | 22.6 | 10.1 | 24.6 | 15.5 | 18.6 | 6.5 | 2.2 | 8.36 | 27.2% | 8.7% |
| WTA125 | 254 | 14.2 | 7.1 | 19.7 | 26.4 | 14.2 | 16.5 | 2.0 | 11.31 | 32.7% | 18.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 666 | 19.1 | 16.1 | 26.6 | 17.6 | 15.6 | 3.1 | 1.9 | 6.9 | 20.7% | 5.1% |
| CHALLENGER | 1,381 | 18.8 | 8.9 | 22.1 | 16.6 | 20.2 | 10.3 | 3.0 | 10.05 | 33.5% | 13.3% |
| ITF_MEN | 1,960 | 12.1 | 8.2 | 19.0 | 16.7 | 20.6 | 15.5 | 7.9 | 13.0 | 43.9% | 23.3% |
| ITF_WOMEN | 2,756 | 9.6 | 7.4 | 15.1 | 13.9 | 23.3 | 19.4 | 11.3 | 16.63 | 54.0% | 30.8% |
| WTA | 496 | 21.0 | 5.0 | 16.7 | 15.9 | 21.8 | 17.3 | 2.2 | 13.18 | 41.3% | 19.6% |
| WTA125 | 254 | 5.5 | 2.0 | 16.9 | 24.4 | 20.1 | 19.7 | 11.4 | 15.82 | 51.2% | 31.1% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 349 | 29.5 | 19.8 | 38.7 | 11.8 | 0.3 | 0.0 | 0.0 | 5.11 | 0.3% | 0.0% |
| CHALLENGER | 1,103 | 24.6 | 17.6 | 29.6 | 14.2 | 11.8 | 2.2 | 0.1 | 6.18 | 14.1% | 2.3% |
| DOUBLES | 425 | 4.7 | 3.1 | 13.9 | 10.8 | 24.5 | 20.2 | 22.8 | 22.7 | 67.5% | 43.1% |
| ITF_MEN | 2,288 | 15.7 | 9.4 | 20.8 | 16.5 | 20.4 | 12.0 | 5.3 | 11.38 | 37.7% | 17.3% |
| ITF_WOMEN | 2,636 | 11.6 | 9.7 | 20.5 | 15.2 | 23.2 | 17.1 | 2.7 | 12.33 | 43.0% | 19.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 388 | 19.3 | 11.1 | 26.8 | 20.1 | 16.8 | 5.9 | 0.0 | 8.66 | 22.7% | 5.9% |
| WTA125 | 363 | 17.1 | 12.9 | 24.8 | 22.9 | 16.8 | 5.2 | 0.3 | 9.01 | 22.3% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 468 | 4.7 | 3.2 | 13.5 | 10.9 | 24.1 | 20.1 | 23.5 | 22.7 | 67.7% | 43.6% |
| singles | 8,953 | 14.7 | 10.3 | 21.3 | 15.0 | 19.1 | 13.5 | 6.2 | 11.12 | 38.8% | 19.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,351 | 13.4 | 9.7 | 19.3 | 15.6 | 15.8 | 14.9 | 11.4 | 12.44 | 42.1% | 26.3% |
| Hard | 6,737 | 12.6 | 8.9 | 18.3 | 15.4 | 19.1 | 15.5 | 10.1 | 13.24 | 44.7% | 25.6% |
| UNKNOWN | 854 | 12.2 | 8.0 | 15.0 | 17.2 | 17.6 | 18.7 | 11.4 | 14.13 | 47.7% | 30.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,919 | 17.5 | 11.6 | 20.3 | 16.8 | 14.7 | 10.5 | 8.7 | 10.22 | 33.9% | 19.2% |
| B | 1,278 | 15.7 | 9.7 | 19.7 | 17.4 | 16.2 | 11.1 | 10.1 | 11.04 | 37.4% | 21.2% |
| C | 1,498 | 12.2 | 10.3 | 21.0 | 14.5 | 17.6 | 14.9 | 9.5 | 12.4 | 42.0% | 24.4% |
| D | 1,823 | 11.2 | 8.8 | 16.4 | 15.1 | 22.6 | 16.3 | 9.7 | 14.17 | 48.5% | 25.9% |
| F | 2,424 | 7.0 | 5.0 | 14.7 | 14.4 | 20.5 | 24.2 | 14.2 | 18.97 | 58.9% | 38.4% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,748 | 21.0 | 13.9 | 27.3 | 16.3 | 13.5 | 5.7 | 2.3 | 7.46 | 21.5% | 8.0% |
| B | 1,404 | 14.1 | 9.8 | 22.6 | 16.0 | 19.1 | 12.2 | 6.1 | 11.16 | 37.5% | 18.4% |
| C | 1,767 | 11.4 | 8.0 | 18.7 | 14.7 | 22.0 | 14.9 | 10.3 | 13.8 | 47.3% | 25.2% |
| D | 1,548 | 12.4 | 8.5 | 20.7 | 12.8 | 22.0 | 16.5 | 7.0 | 13.09 | 45.5% | 23.6% |
| F | 1,954 | 8.4 | 7.4 | 12.7 | 13.6 | 23.1 | 23.4 | 11.3 | 17.84 | 57.8% | 34.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 3,401 | 16.6 | 10.6 | 19.5 | 17.3 | 15.1 | 10.6 | 10.2 | 10.92 | 36.0% | 20.8% |
| LIMITED | 2,263 | 14.3 | 11.1 | 21.8 | 14.9 | 16.6 | 13.5 | 7.8 | 10.93 | 37.9% | 21.3% |
| POOR | 4,278 | 8.9 | 6.7 | 15.4 | 14.7 | 21.5 | 20.7 | 12.2 | 17.0 | 54.4% | 32.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,525 | 30.0 | 26.6 | 36.5 | 5.1 | 1.6 | 0.2 | 0.0 | 4.43 | 1.8% | 0.2% |
| GAME_SPREAD | 1,407 | 23.3 | 15.5 | 37.1 | 18.4 | 5.1 | 0.4 | 0.2 | 6.2 | 5.7% | 0.6% |
| MATCH_WINNER | 9,421 | 14.2 | 10.0 | 20.9 | 14.8 | 19.3 | 13.8 | 7.0 | 11.53 | 40.2% | 20.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,106 | 28.5 | 18.6 | 31.6 | 11.5 | 8.0 | 1.5 | 0.3 | 5.37 | 9.8% | 1.9% |
| TOTAL_GAMES | 2,293 | 8.1 | 9.6 | 35.9 | 28.4 | 11.3 | 3.9 | 2.7 | 9.57 | 17.9% | 6.6% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,408 | 25.5 | 38.9 | 26.9 | 0.3 | 7.4 | 0.7 | 0.2 | 4.3 | 8.4% | 1.0% |
| GAME_SPREAD | 1,625 | 44.2 | 14.5 | 28.8 | 10.1 | 1.4 | 0.7 | 0.2 | 3.74 | 2.3% | 1.0% |
| TOTAL_GAMES | 2,609 | 3.9 | 6.1 | 42.3 | 36.6 | 7.2 | 1.7 | 2.1 | 9.82 | 11.0% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,408 | 26.0 | 17.7 | 34.9 | 9.1 | 8.1 | 3.6 | 0.6 | 5.62 | 12.3% | 4.3% |
| GAME_SPREAD | 1,625 | 18.6 | 13.5 | 27.3 | 23.1 | 12.9 | 3.6 | 0.9 | 8.34 | 17.4% | 4.5% |
| TOTAL_GAMES | 2,618 | 6.2 | 8.2 | 36.8 | 28.6 | 13.8 | 3.9 | 2.6 | 9.83 | 20.2% | 6.5% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 9,942 | 44.3% | 26.1% | 13.09 | 34.6% | 15.8% | 10.51 |
| gen1_elo | 9,942 | 44.2% | 25.1% | 12.74 | 34.1% | 15.3% | 10.13 |
| gen1_sr | 9,942 | 52.6% | 30.9% | 15.96 | 43.9% | 20.6% | 13.07 |
| gen2 | 9,942 | 51.3% | 31.4% | 15.53 | 43.7% | 22.6% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 4,503 | 15.4 | 12.1 | 21.8 | 16.6 | 18.1 | 12.2 | 3.8 | 10.18 | 34.1% | 15.9% |
| STALE | 5,439 | 10.6 | 6.5 | 15.3 | 14.8 | 18.2 | 18.5 | 16.1 | 16.55 | 52.8% | 34.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 2,889 | 16.5 | 10.9 | 23.5 | 14.9 | 16.7 | 13.2 | 4.3 | 9.83 | 34.2% | 17.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 19,363 | 2889 | 7975 | 8499 | 27.5 | 185.8 | 1400.4 |
| ge_15pp | 8,194 | 987 | 2824 | 4383 | 32.7 | 452.3 | 1380.4 |
| ge_25pp | 4,566 | 505 | 1309 | 2752 | 43.4 | 554.2 | 1380.4 |
| lt_10pp | 8,219 | 1470 | 3851 | 2898 | 25.3 | 54.1 | 1201.9 |

Current slate `SL-20261006T185959Z-66ac9116`: 1059 priced rows, quote age at build {'median': 9.2, 'max': 9.2}, freshness {'FRESH': 1059}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 221 | 19.5 | 11.3 | 24.0 | 19.5 | 17.6 | 7.7 | 0.5 | 8.4 | 25.8% | 8.1% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 8.3 | 50.0 | 41.7 | 0.0 | 0.0 | 14.32 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 9,942 | 242 (2.4%) | 5.0% | 0.0% | {"EXTERNAL_STALE": 221, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 4,408 | 62 (1.4%) | 8.1% | 0.0% | {"EXTERNAL_STALE": 57, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 2,599 | 18 (0.7%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 18} |
| fair_v1_ge_25pp_pregame_clean | 1,191 | 18 (1.5%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 18} |
| fair_v1_lt_10pp | 3,980 | 131 (3.3%) | 0.8% | 0.0% | {"EXTERNAL_STALE": 121, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,982 | 10.6 | 8.6 | 20.5 | 15.0 | 21.1 | 14.4 | 9.7 | 13.12 | 45.3% | 24.1% |
| 4-10x | 1,457 | 11.4 | 10.5 | 17.4 | 14.1 | 19.4 | 18.0 | 9.2 | 13.67 | 46.6% | 27.2% |
| <2x | 5,250 | 14.6 | 9.6 | 18.4 | 16.6 | 16.7 | 13.9 | 10.3 | 12.29 | 40.9% | 24.2% |
| >=10x | 1,253 | 10.2 | 5.5 | 14.9 | 14.5 | 18.4 | 22.1 | 14.3 | 17.2 | 54.8% | 36.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 2,501 | 14.0 | 8.5 | 20.8 | 15.8 | 16.6 | 12.8 | 11.5 | 12.0 | 40.9% | 24.3% |
| 300-1000 | 2,332 | 11.9 | 9.9 | 16.5 | 15.2 | 21.4 | 16.6 | 8.7 | 13.81 | 46.6% | 25.3% |
| <300 | 2,826 | 8.1 | 6.2 | 15.0 | 14.3 | 20.4 | 22.4 | 13.7 | 18.15 | 56.5% | 36.1% |
| >=3000 | 2,283 | 18.1 | 12.3 | 21.2 | 17.6 | 14.0 | 9.4 | 7.3 | 9.65 | 30.8% | 16.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 303 | 0.5342 | 0.4005 | 0.4521 | +0.082 | -0.052 | 0.0042 ± 0.0082 |
| ratio 4-10x | 222 | 0.59 | 0.4507 | 0.5315 | +0.059 | -0.081 | 0.0015 ± 0.0101 |
| ratio <2x | 629 | 0.539 | 0.4136 | 0.4595 | +0.080 | -0.046 | 0.0124 ± 0.0058 |
| ratio >=10x | 206 | 0.5669 | 0.3905 | 0.4709 | +0.096 | -0.080 | 0.0103 ± 0.0131 |
| thinner_sample 1000-3000 | 352 | 0.5433 | 0.4213 | 0.4602 | +0.083 | -0.039 | 0.0062 ± 0.0075 |
| thinner_sample 300-1000 | 364 | 0.5699 | 0.4326 | 0.4945 | +0.075 | -0.062 | 0.0013 ± 0.0079 |
| thinner_sample <300 | 457 | 0.5543 | 0.3906 | 0.4792 | +0.075 | -0.089 | 0.0111 ± 0.0081 |
| thinner_sample >=3000 | 187 | 0.5168 | 0.4157 | 0.4278 | +0.089 | -0.012 | 0.0202 ± 0.0085 |
| data_status ADEQUATE | 375 | 0.525 | 0.4178 | 0.4427 | +0.082 | -0.025 | 0.0109 ± 0.0064 |
| data_status LIMITED | 299 | 0.5665 | 0.4342 | 0.4983 | +0.068 | -0.064 | -0.002 ± 0.0087 |
| data_status POOR | 686 | 0.5574 | 0.4016 | 0.4752 | +0.082 | -0.074 | 0.0117 ± 0.0064 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 205 | 0.1827 | 0.1832 | -0.0005 ± 0.001 | 0.5408 | 0.5423 | 0.4926 | 0.4782 | 0.4878 | -0.105 ± 0.0322 | -0.01 (3) |
| 3-5 | 136 | 0.1817 | 0.1843 | -0.0026 ± 0.003 | 0.5428 | 0.546 | 0.5169 | 0.476 | 0.5221 | -0.065 ± 0.0381 | 0.02 (1) |
| 5-10 | 282 | 0.2004 | 0.2043 | -0.0039 ± 0.004 | 0.587 | 0.5966 | 0.5241 | 0.45 | 0.5071 | -0.077 ± 0.0279 | -0.0167 (3) |
| 10-15 | 232 | 0.2222 | 0.2174 | +0.0048 ± 0.0077 | 0.6329 | 0.6184 | 0.5256 | 0.4017 | 0.444 | -0.098 ± 0.0306 | -0.0633 (3) |
| 15-25 | 295 | 0.2197 | 0.2103 | +0.0094 ± 0.0105 | 0.6287 | 0.6053 | 0.5713 | 0.3752 | 0.4475 | -0.078 ± 0.0267 | -0.02 (4) |
| 25-40 | 171 | 0.2124 | 0.1967 | +0.0156 ± 0.0203 | 0.6114 | 0.5672 | 0.6451 | 0.3326 | 0.462 | -0.060 ± 0.0298 | -0.01 (1) |
| 40+ | 39 | 0.3105 | 0.1436 | +0.1669 ± 0.0543 | 0.8355 | 0.4493 | 0.7382 | 0.2969 | 0.3333 | -0.170 ± 0.0539 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 817 | 0.1678 | 0.1683 | -0.0005 ± 0.0005 | 0.503 | 0.5036 | 0.4904 | 0.4756 | 0.5104 | -0.037 ± 0.0148 | -0.0188 (8) |
| 3-5 | 597 | 0.188 | 0.1871 | +0.0008 ± 0.0014 | 0.5554 | 0.5489 | 0.4798 | 0.4399 | 0.4439 | -0.068 ± 0.0183 | 0.02 (1) |
| 5-10 | 1252 | 0.1863 | 0.1874 | -0.0010 ± 0.0018 | 0.5536 | 0.5551 | 0.4846 | 0.411 | 0.4545 | -0.032 ± 0.0124 | -0.0129 (7) |
| 10-15 | 1069 | 0.196 | 0.1801 | +0.0159 ± 0.0032 | 0.576 | 0.5297 | 0.4718 | 0.3476 | 0.348 | -0.078 ± 0.0129 | -0.0633 (3) |
| 15-25 | 1375 | 0.2002 | 0.1603 | +0.0399 ± 0.0043 | 0.5899 | 0.4785 | 0.4893 | 0.2915 | 0.2887 | -0.083 ± 0.0108 | -0.017 (10) |
| 25-40 | 1307 | 0.2145 | 0.1194 | +0.0950 ± 0.006 | 0.6209 | 0.3716 | 0.523 | 0.2086 | 0.2165 | -0.060 ± 0.0092 | -0.01 (1) |
| 40+ | 921 | 0.3684 | 0.0411 | +0.3273 ± 0.0073 | 0.9589 | 0.1687 | 0.6194 | 0.106 | 0.0532 | -0.087 ± 0.0062 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 150 | 0.1884 | 0.1879 | +0.0004 ± 0.0012 | 0.5545 | 0.5518 | 0.4947 | 0.48 | 0.46 | -0.141 ± 0.0382 | -0.01 (1) |
| 3-5 | 97 | 0.2015 | 0.2011 | +0.0004 ± 0.0037 | 0.58 | 0.584 | 0.493 | 0.4534 | 0.4639 | -0.085 ± 0.0491 | 0.02 (1) |
| 5-10 | 243 | 0.1895 | 0.1914 | -0.0019 ± 0.0042 | 0.5601 | 0.5641 | 0.5681 | 0.4929 | 0.535 | -0.075 ± 0.0287 | -0.01 (4) |
| 10-15 | 232 | 0.2314 | 0.2187 | +0.0127 ± 0.0078 | 0.6531 | 0.6279 | 0.5836 | 0.4593 | 0.4741 | -0.123 ± 0.0323 | -0.0667 (3) |
| 15-25 | 331 | 0.2247 | 0.2036 | +0.0211 ± 0.0099 | 0.6368 | 0.587 | 0.5927 | 0.3953 | 0.4471 | -0.104 ± 0.0256 | -0.0167 (3) |
| 25-40 | 218 | 0.2566 | 0.1984 | +0.0582 ± 0.0187 | 0.7144 | 0.5769 | 0.665 | 0.3532 | 0.4128 | -0.126 ± 0.0304 | -0.025 (2) |
| 40+ | 89 | 0.3599 | 0.1822 | +0.1776 ± 0.0451 | 0.9987 | 0.5364 | 0.7556 | 0.2667 | 0.3483 | -0.063 ± 0.0428 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 707 | 0.1702 | 0.1705 | -0.0003 ± 0.0005 | 0.5084 | 0.5089 | 0.5095 | 0.4954 | 0.505 | -0.063 ± 0.0167 | -0.0217 (6) |
| 3-5 | 475 | 0.1821 | 0.1793 | +0.0028 ± 0.0016 | 0.534 | 0.53 | 0.5149 | 0.4753 | 0.4589 | -0.072 ± 0.0199 | 0.02 (1) |
| 5-10 | 1102 | 0.1776 | 0.1804 | -0.0027 ± 0.0019 | 0.5303 | 0.534 | 0.5129 | 0.4384 | 0.4909 | -0.019 ± 0.0129 | -0.01 (5) |
| 10-15 | 988 | 0.1964 | 0.178 | +0.0184 ± 0.0033 | 0.5811 | 0.5253 | 0.5136 | 0.39 | 0.3816 | -0.086 ± 0.0137 | -0.0575 (4) |
| 15-25 | 1461 | 0.2113 | 0.169 | +0.0423 ± 0.0043 | 0.6144 | 0.502 | 0.5263 | 0.331 | 0.3244 | -0.094 ± 0.0109 | -0.0143 (7) |
| 25-40 | 1401 | 0.24 | 0.1295 | +0.1104 ± 0.0061 | 0.682 | 0.3999 | 0.5547 | 0.2374 | 0.2206 | -0.088 ± 0.0097 | -0.015 (6) |
| 40+ | 1204 | 0.3997 | 0.0686 | +0.3311 ± 0.0086 | 1.0438 | 0.2403 | 0.6651 | 0.1271 | 0.1005 | -0.066 ± 0.0073 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 207 | 0.1907 | 0.1928 | -0.0021 ± 0.0011 | 0.5604 | 0.5666 | 0.5109 | 0.496 | 0.5362 | -0.055 ± 0.0307 | -0.01 (5) |
| 3-5 | 147 | 0.1779 | 0.1756 | +0.0023 ± 0.0028 | 0.5297 | 0.5246 | 0.5076 | 0.4683 | 0.4558 | -0.144 ± 0.0371 | -- (0) |
| 5-10 | 286 | 0.1999 | 0.2003 | -0.0005 ± 0.004 | 0.5873 | 0.5845 | 0.5142 | 0.4406 | 0.4755 | -0.091 ± 0.0269 | -0.01 (3) |
| 10-15 | 226 | 0.2158 | 0.2168 | -0.0011 ± 0.0077 | 0.6213 | 0.6199 | 0.5426 | 0.4191 | 0.4867 | -0.076 ± 0.031 | -0.044 (5) |
| 15-25 | 287 | 0.2219 | 0.2065 | +0.0155 ± 0.0105 | 0.6404 | 0.5947 | 0.583 | 0.3885 | 0.446 | -0.097 ± 0.0266 | -0.03 (1) |
| 25-40 | 174 | 0.2044 | 0.2063 | -0.0019 ± 0.0202 | 0.5935 | 0.5915 | 0.6522 | 0.3388 | 0.4943 | -0.044 ± 0.0293 | 0.0 (1) |
| 40+ | 33 | 0.3471 | 0.1356 | +0.2115 ± 0.058 | 0.918 | 0.43 | 0.7266 | 0.2779 | 0.2727 | -0.196 ± 0.0611 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 809 | 0.1683 | 0.1691 | -0.0008 ± 0.0005 | 0.5058 | 0.5076 | 0.4911 | 0.4764 | 0.5019 | -0.042 ± 0.0145 | -0.0162 (13) |
| 3-5 | 586 | 0.1881 | 0.183 | +0.0051 ± 0.0014 | 0.5533 | 0.5436 | 0.4792 | 0.4399 | 0.3925 | -0.130 ± 0.0184 | -0.01 (2) |
| 5-10 | 1302 | 0.1872 | 0.1825 | +0.0047 ± 0.0018 | 0.5574 | 0.5396 | 0.48 | 0.4063 | 0.4101 | -0.068 ± 0.0118 | -0.01 (3) |
| 10-15 | 1016 | 0.1893 | 0.1789 | +0.0103 ± 0.0033 | 0.5605 | 0.5262 | 0.4834 | 0.3601 | 0.3799 | -0.060 ± 0.0131 | -0.03 (9) |
| 15-25 | 1505 | 0.2014 | 0.1606 | +0.0407 ± 0.0041 | 0.5966 | 0.4808 | 0.4931 | 0.2945 | 0.2937 | -0.076 ± 0.0104 | -0.03 (2) |
| 25-40 | 1251 | 0.2153 | 0.1178 | +0.0975 ± 0.0062 | 0.6224 | 0.3654 | 0.5225 | 0.2038 | 0.2134 | -0.064 ± 0.0092 | 0.0 (1) |
| 40+ | 869 | 0.384 | 0.0422 | +0.3418 ± 0.0079 | 1.0042 | 0.1719 | 0.6265 | 0.1053 | 0.0495 | -0.088 ± 0.0066 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 481 | 0.2034 | 0.2036 | -0.0002 ± 0.0007 | 0.5882 | 0.5892 | 0.4978 | 0.4831 | 0.4906 | -0.041 ± 0.0206 | -0.0226 (46) |
| 3-5 | 361 | 0.1955 | 0.1956 | -0.0001 ± 0.0019 | 0.5732 | 0.572 | 0.4787 | 0.4389 | 0.4626 | -0.032 ± 0.0231 | -0.0059 (32) |
| 5-10 | 744 | 0.1889 | 0.184 | +0.0049 ± 0.0024 | 0.5617 | 0.5483 | 0.4661 | 0.3924 | 0.3965 | -0.051 ± 0.016 | -0.005 (72) |
| 10-15 | 500 | 0.2022 | 0.1918 | +0.0104 ± 0.0049 | 0.5931 | 0.564 | 0.4662 | 0.3432 | 0.362 | -0.043 ± 0.0195 | 0.0016 (63) |
| 15-25 | 671 | 0.2365 | 0.2112 | +0.0253 ± 0.0069 | 0.6692 | 0.6081 | 0.5345 | 0.3411 | 0.3741 | -0.045 ± 0.0178 | -0.0216 (58) |
| 25-40 | 363 | 0.2494 | 0.1748 | +0.0747 ± 0.0137 | 0.6993 | 0.5198 | 0.5976 | 0.2851 | 0.3196 | -0.067 ± 0.0207 | -0.0216 (25) |
| 40+ | 114 | 0.3798 | 0.1628 | +0.2170 ± 0.0399 | 1.0645 | 0.4966 | 0.7504 | 0.2496 | 0.307 | -0.053 ± 0.036 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1113 | 0.1937 | 0.194 | -0.0003 ± 0.0005 | 0.5634 | 0.5642 | 0.4964 | 0.4815 | 0.4951 | -0.034 ± 0.0131 | -0.0155 (82) |
| 3-5 | 800 | 0.188 | 0.1872 | +0.0009 ± 0.0012 | 0.5538 | 0.5516 | 0.489 | 0.4493 | 0.4587 | -0.039 ± 0.0154 | -0.018 (54) |
| 5-10 | 1677 | 0.1847 | 0.1786 | +0.0062 ± 0.0016 | 0.5507 | 0.5328 | 0.464 | 0.3896 | 0.3888 | -0.052 ± 0.0105 | -0.0089 (122) |
| 10-15 | 1278 | 0.1976 | 0.1851 | +0.0126 ± 0.003 | 0.583 | 0.547 | 0.4748 | 0.3518 | 0.3615 | -0.051 ± 0.0119 | -0.0053 (99) |
| 15-25 | 1665 | 0.2275 | 0.1929 | +0.0346 ± 0.0042 | 0.6547 | 0.5632 | 0.5241 | 0.3286 | 0.3381 | -0.060 ± 0.0109 | -0.0255 (106) |
| 25-40 | 1203 | 0.2389 | 0.1461 | +0.0928 ± 0.007 | 0.6762 | 0.4438 | 0.5608 | 0.2452 | 0.2569 | -0.067 ± 0.0107 | -0.0206 (47) |
| 40+ | 601 | 0.369 | 0.0873 | +0.2817 ± 0.0131 | 1.0034 | 0.2887 | 0.66 | 0.1505 | 0.1398 | -0.068 ± 0.0116 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1360 | 1.133 ± 0.08 | 1.251 | 0.1674 | 0.167 | 0.2084 | 0.1999 |
| gen2 | 1360 | 0.921 ± 0.07 | 1.168 | 0.1827 | 0.167 | 0.2278 | 0.1998 |
| gen1_elo | 1360 | 1.111 ± 0.078 | 1.22 | 0.1722 | 0.1673 | 0.2075 | 0.1997 |
| gen1_sr | 1360 | 1.165 ± 0.092 | 1.233 | 0.1402 | 0.169 | 0.2227 | 0.2 |
| gen1_ledger | 3234 | 0.924 ± 0.047 | 1.09 | 0.1647 | 0.1948 | 0.2172 | 0.1933 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 8,194)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,361 | 28.8% |
| STALE_QUOTE | market_freshness | 2,016 | 24.6% |
| BOOK_QUALITY | execution | 1,360 | 16.6% |
| POOR_DATA | data | 805 | 9.8% |
| LIMITED_DATA | data | 480 | 5.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 387 | 4.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 380 | 4.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 213 | 2.6% |
| IDENTITY_AMBIGUOUS | mapping | 189 | 2.3% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.0% |

Cause class: coverage 28.8%, market_freshness 24.6%, execution 16.6%, data 15.7%, market_freshness/coverage 7.3%, model_calibration_or_unknown 4.6%, mapping 2.3%, model_calibration 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 95.8%, LOW_DATA_QUALITY 68.5%, THIN_PLAYER_HISTORY 58.4%, STALE_PLAYER_DATA 57.4%, STALE_KALSHI_QUOTE 53.5%, MODEL_INTERNAL_DISAGREEMENT 37.1%, ASYMMETRIC_SAMPLE_SIZE 31.5%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 15.0%, PLAYER_IDENTITY_RISK 10.7%, LEVEL_TRANSFER_RISK 8.2%, EVENT_MAPPING_RISK 6.8%, LOW_DISPLAYED_LIQUIDITY 6.7%, MODEL_CALIBRATION_OUTLIER 2.5%, UNKNOWN 0.5%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 30.9%, POST_SETTLEMENT_OBSERVATION 28.8%, POSSIBLE_IN_PLAY_QUOTE 5.2%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### >= ge_25 pp (N = 4,566)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,856 | 40.6% |
| STALE_QUOTE | market_freshness | 920 | 20.2% |
| BOOK_QUALITY | execution | 726 | 15.9% |
| POOR_DATA | data | 370 | 8.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 213 | 4.7% |
| LIMITED_DATA | data | 142 | 3.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 128 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 113 | 2.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 98 | 2.1% |

Cause class: coverage 40.6%, market_freshness 20.2%, execution 15.9%, data 11.2%, market_freshness/coverage 7.5%, mapping 2.5%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.8%, LOW_DATA_QUALITY 71.3%, THIN_PLAYER_HISTORY 60.9%, STALE_KALSHI_QUOTE 60.3%, STALE_PLAYER_DATA 54.3%, MODEL_INTERNAL_DISAGREEMENT 39.4%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 22.9%, MODEL_HIGH_UNCERTAINTY 16.2%, PLAYER_IDENTITY_RISK 13.2%, LEVEL_TRANSFER_RISK 7.6%, EVENT_MAPPING_RISK 7.5%, LOW_DISPLAYED_LIQUIDITY 7.3%, MODEL_CALIBRATION_OUTLIER 3.4%, UNKNOWN 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.8%, POST_SETTLEMENT_OBSERVATION 40.6%, POSSIBLE_IN_PLAY_QUOTE 5.2%, CONFIRMED_IN_PLAY_QUOTE 0.8%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 3828, "IDENTITY_AMBIGUOUS": 738}; ticker orientation: {"VERIFIED": 4566}.

Checks: discipline:AMBIGUOUS 204, discipline:PASS 4362, identity_confidence:AMBIGUOUS 602, identity_confidence:PASS 3964, level_mapping:NA 216, level_mapping:PASS 4350, market_pair:AMBIGUOUS 168, market_pair:NA 111, market_pair:PASS 4287, model_complement:NA 80, model_complement:PASS 4486, namesake:PASS 4566, physical_match_id:NA 1967, physical_match_id:PASS 2599, player_ids:PASS 4566, same_pair_other_event:PASS 4566, ticker_orientation:PASS 4566

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,032 | 2.2% | 2.3% | 0.5% | {"market_freshness": 20, "execution": 3} | 5.58 | 0.1949 / 0.1839 (77) | 23.9% | 0.2% | 6.3% | 1.7% |
| CHALLENGER | 3,246 | 19.0% | 6.8% | 13.5% | {"coverage": 375, "market_freshness": 107, "market_freshness/coverage": 72, "model_calibration_or_unknown": 34, "data": 25, "execution": 4} | 7.17 | 0.2207 / 0.2033 (764) | 49.2% | 5.5% | 1.4% | 23.5% |
| DOUBLES | 468 | 43.6% | 43.1% | 4.5% | {"market_freshness": 106, "execution": 40, "mapping": 37, "market_freshness/coverage": 14, "coverage": 7} | 22.7 | 0.3142 / 0.227 (171) | 50.0% | 0.0% | 100.0% | 9.2% |
| ITF_MEN | 5,692 | 26.6% | 18.4% | 33.1% | {"coverage": 628, "execution": 324, "market_freshness": 247, "data": 192, "market_freshness/coverage": 102, "mapping": 19, "model_calibration_or_unknown": 1} | 11.21 | 0.2165 / 0.193 (1549) | 44.9% | 56.4% | 6.8% | 25.4% |
| ITF_WOMEN | 7,152 | 28.1% | 19.8% | 44.0% | {"coverage": 829, "market_freshness": 385, "execution": 338, "data": 271, "market_freshness/coverage": 112, "mapping": 51, "model_calibration_or_unknown": 22} | 12.69 | 0.2022 / 0.1901 (1607) | 46.0% | 61.1% | 11.2% | 24.6% |
| OTHER | 149 | 8.1% | 7.3% | 0.3% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 916 | 8.6% | 7.5% | 1.7% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.4 | 0.2026 / 0.197 (137) | 36.0% | 2.3% | 1.3% | 3.5% |
| WTA125 | 708 | 15.5% | 10.9% | 2.4% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 23, "market_freshness": 19, "data": 13, "coverage": 12, "execution": 8, "mapping": 4} | 10.09 | 0.2211 / 0.2059 (247) | 28.8% | 6.1% | 4.1% | 12.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 5 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 6 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 7 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 8 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 9 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 10 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 11 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 13 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 14 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 15 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 16 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 18 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 19 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 20 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 21 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 22 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 23 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 24 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 25 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 27 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 28 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 29 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 30 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 31 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 32 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 826 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 33 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 34 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 35 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 37 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 40 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 41 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 43 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 183 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 44 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 45 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 192 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.76); no external reference |
| 47 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 48 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 50 | `KXITFMATCH-26OCT06TANEIC-TAN` | ITF_MEN | fair_v1 | 75% / 6% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 78 min (STALE); data LIMITED (grade C, thinner serve sample 1550.0, ratio 1.07); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9777, "by_level_share_of_ge_25pp": {"ATP": 0.005, "CHALLENGER": 0.1351, "DOUBLES": 0.0447, "ITF_MEN": 0.3314, "ITF_WOMEN": 0.4398, "OTHER": 0.0026, "WTA": 0.0173, "WTA125": 0.0241}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6027, "share_primary_cause_market_settled_or_in_play": 0.4811, "share_primary_cause_stale_quote_only": 0.2015}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 4566, "identity_ambiguous_share": 0.1616, "ticker_orientation": {"VERIFIED": 4566}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 2599, "with_external": 18, "coverage": 0.0069, "external_status": {"EXTERNAL_STALE": 18}, "triangulation": {"INSUFFICIENT_INPUTS": 18}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1191, "with_external": 18, "coverage": 0.0151, "external_status": {"EXTERNAL_STALE": 18}, "triangulation": {"INSUFFICIENT_INPUTS": 18}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 585.0, "median_sample_ratio": 2.38, "median_min_matches": 19.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1844, "data_status": {"POOR": 2462, "LIMITED": 1262, "ADEQUATE": 842}, "comparison_lt_10pp": {"median_thinner_serve_points": 1833.0, "median_sample_ratio": 1.74, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 303, "model_minus_observed": 0.082, "kalshi_minus_observed": -0.0516, "brier_diff_model_minus_kalshi": 0.0042}, "4-10x": {"n": 222, "model_minus_observed": 0.0585, "kalshi_minus_observed": -0.0808, "brier_diff_model_minus_kalshi": 0.0015}, "<2x": {"n": 629, "model_minus_observed": 0.0796, "kalshi_minus_observed": -0.0459, "brier_diff_model_minus_kalshi": 0.0124}, ">=10x": {"n": 206, "model_minus_observed": 0.096, "kalshi_minus_observed": -0.0803, "brier_diff_model_minus_kalshi": 0.0103}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1360, "model": {"intercept": -0.602, "slope": 0.921, "slope_se": 0.07}, "kalshi_mid_same_rows": {"intercept": 0.231, "slope": 1.168, "slope_se": 0.08}, "mean_extremity_model": 0.1827, "mean_extremity_kalshi": 0.167, "model_brier": 0.2278, "kalshi_brier": 0.1998, "brier_diff_model_minus_kalshi": 0.028, "brier_diff_se": 0.0052, "model_logloss": 0.6489, "kalshi_logloss": 0.5809}, "fair_v1": {"n": 1360, "model": {"intercept": -0.405, "slope": 1.133, "slope_se": 0.08}, "kalshi_mid_same_rows": {"intercept": 0.374, "slope": 1.251, "slope_se": 0.083}, "mean_extremity_model": 0.1674, "mean_extremity_kalshi": 0.167, "model_brier": 0.2084, "kalshi_brier": 0.1999, "brier_diff_model_minus_kalshi": 0.0085, "brier_diff_se": 0.0041, "model_logloss": 0.6027, "kalshi_logloss": 0.581}, "gen1_elo": {"n": 1360, "model": {"intercept": -0.405, "slope": 1.111, "slope_se": 0.078}, "kalshi_mid_same_rows": {"intercept": 0.343, "slope": 1.22, "slope_se": 0.081}, "mean_extremity_model": 0.1722, "mean_extremity_kalshi": 0.1673, "model_brier": 0.2075, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": 0.0078, "brier_diff_se": 0.0041, "model_logloss": 0.6027, "kalshi_logloss": 0.5805}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2614, "share_ge_15": 0.4434, "median_abs_gap": 13.09, "n": 9942}, "gen1_elo": {"share_ge_25": 0.2512, "share_ge_15": 0.4418, "median_abs_gap": 12.74, "n": 9942}, "gen1_sr": {"share_ge_25": 0.3087, "share_ge_15": 0.5264, "median_abs_gap": 15.96, "n": 9942}, "gen2": {"share_ge_25": 0.3137, "share_ge_15": 0.5129, "median_abs_gap": 15.53, "n": 9942}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1585, "share_ge_15": 0.3457, "median_abs_gap": 10.51, "n": 7513}, "gen1_elo": {"share_ge_25": 0.1527, "share_ge_15": 0.341, "median_abs_gap": 10.13, "n": 7513}, "gen1_sr": {"share_ge_25": 0.2056, "share_ge_15": 0.4394, "median_abs_gap": 13.07, "n": 7513}, "gen2": {"share_ge_25": 0.2261, "share_ge_15": 0.4374, "median_abs_gap": 12.86, "n": 7513}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.58, "share_ge_25_all": 0.0223, "share_ge_25_pregame_clean": 0.0227}, "WTA": {"median_abs_gap_pregame_clean": 8.4, "share_ge_25_all": 0.0862, "share_ge_25_pregame_clean": 0.0747}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2292, "share_within_10pp_all": 0.4245, "share_within_10pp_pregame_clean": 0.4909, "corr_model_vs_mid_pregame_clean": 0.8373}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 205, "model_brier": 0.1827, "kalshi_brier": 0.1832, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 232, "model_brier": 0.2222, "kalshi_brier": 0.2174, "brier_diff_model_minus_kalshi": 0.0048}, "15-25": {"n_settled": 295, "model_brier": 0.2197, "kalshi_brier": 0.2103, "brier_diff_model_minus_kalshi": 0.0094}, "25-40": {"n_settled": 171, "model_brier": 0.2124, "kalshi_brier": 0.1967, "brier_diff_model_minus_kalshi": 0.0156}, "3-5": {"n_settled": 136, "model_brier": 0.1817, "kalshi_brier": 0.1843, "brier_diff_model_minus_kalshi": -0.0026}, "40+": {"n_settled": 39, "model_brier": 0.3105, "kalshi_brier": 0.1436, "brier_diff_model_minus_kalshi": 0.1669}, "5-10": {"n_settled": 282, "model_brier": 0.2004, "kalshi_brier": 0.2043, "brier_diff_model_minus_kalshi": -0.0039}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 171, "model_brier": 0.3142, "kalshi_brier": 0.227, "brier_diff_model_minus_kalshi": 0.0872, "brier_diff_se": 0.0247, "corr_model_outcome": -0.069, "corr_kalshi_outcome": 0.3465}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
