# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-06T20:47Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 20,080): 0-3 13.3%, 3-5 9.4%, 5-10 19.6%, 10-15 15.3%, 15-25 18.8%, 25-40 14.8%, 40+ 8.8%; median gap 12.39 pp.
* **Where the extremes live**: 97.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.4%, Challenger 13.4%, doubles 4.4%). Main tour: ATP 2.1% and WTA 8.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 4,741): MARKET_ALREADY_SETTLED_WHEN_PRICED 41.2%, STALE_QUOTE 19.4%, BOOK_QUALITY 16.5%, POOR_DATA 7.8%, POSSIBLY_IN_PLAY_QUOTE 4.6%, LIMITED_DATA 3.2%, IN_PLAY_QUOTE 2.9%, IDENTITY_AMBIGUOUS 2.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 41.2%, market_freshness 19.4%, execution 16.5%, data 11.0%, market_freshness/coverage 7.4%, mapping 2.5%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 60.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 4,741 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 5.6% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 596.0 points vs 1798.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.142, Gen-2 0.932, Gen-1 ledger 0.928 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 171 model 0.2124 vs Kalshi 0.1967; n 39 model 0.3105 vs Kalshi 0.1436.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 73,885 model-market comparisons (124,611 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 29,010 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-06T20:40:24.402991+00:00'], shadow board 20,685 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-06T20:40:27.946786+00:00'], Model 4 7,103 rows, 9,485 settled tickers, 2,151 tickers with an external scan.
* By model: {"gen1_ledger": 18340, "gen1_elo": 10397, "fair_v1": 10397, "gen2": 10397, "gen1_sr": 10397, "model4_fundamental": 6983, "model4_conditioned": 6974}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 20,080 | 13.3 | 9.4 | 19.6 | 15.3 | 18.8 | 14.8 | 8.8 | 12.39 | 42.4% | 23.6% |
| MW fair_v1 | 10,397 | 12.7 | 8.9 | 18.2 | 15.7 | 18.3 | 15.7 | 10.6 | 13.18 | 44.5% | 26.3% |
| MW gen1_elo | 10,397 | 12.7 | 8.7 | 19.5 | 14.7 | 19.2 | 15.2 | 10.0 | 12.85 | 44.4% | 25.2% |
| MW gen1_ledger | 9,683 | 14.1 | 10.0 | 21.1 | 14.8 | 19.4 | 13.8 | 6.9 | 11.52 | 40.1% | 20.8% |
| MW gen1_sr | 10,397 | 9.6 | 7.6 | 15.9 | 14.1 | 21.8 | 18.6 | 12.4 | 16.01 | 52.8% | 30.9% |
| MW gen2 | 10,397 | 11.2 | 7.0 | 16.0 | 14.4 | 19.9 | 17.6 | 14.0 | 15.59 | 51.5% | 31.6% |
| all families model4_conditioned | 6,974 | 21.6 | 20.2 | 33.8 | 16.8 | 5.6 | 1.1 | 0.9 | 5.87 | 7.6% | 2.0% |
| all families model4_fundamental | 6,983 | 16.4 | 13.0 | 34.0 | 20.2 | 11.4 | 3.6 | 1.4 | 7.85 | 16.3% | 5.0% |

Configurable thresholds (primary): >=5pp 77.3%, >=10pp 57.7%, >=15pp 42.4%, >=20pp 32.1%, >=25pp 23.6%, >=30pp 17.3%, >=40pp 8.8%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.69pp; >=10pp 46.3%, >=25pp 19.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 702 | 24.8 | 17.8 | 25.4 | 16.9 | 11.8 | 1.7 | 1.6 | 5.93 | 15.1% | 3.3% |
| CHALLENGER | 1,981 | 14.4 | 11.1 | 18.1 | 16.1 | 13.5 | 13.5 | 13.3 | 12.18 | 40.3% | 26.9% |
| ITF_MEN | 2,905 | 10.2 | 8.2 | 18.3 | 14.6 | 19.3 | 15.7 | 13.8 | 14.44 | 48.8% | 29.5% |
| ITF_WOMEN | 4,035 | 10.3 | 6.7 | 16.0 | 15.5 | 21.3 | 20.1 | 10.2 | 15.64 | 51.5% | 30.3% |
| WTA | 502 | 22.5 | 10.0 | 24.5 | 15.9 | 18.3 | 6.6 | 2.2 | 8.38 | 27.1% | 8.8% |
| WTA125 | 272 | 13.2 | 6.6 | 20.6 | 25.4 | 14.3 | 16.9 | 2.9 | 11.47 | 34.2% | 19.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 702 | 19.8 | 15.7 | 26.2 | 17.7 | 15.8 | 3.0 | 1.9 | 6.9 | 20.7% | 4.8% |
| CHALLENGER | 1,981 | 14.6 | 6.9 | 17.5 | 13.7 | 18.9 | 14.7 | 13.8 | 13.87 | 47.3% | 28.5% |
| ITF_MEN | 2,905 | 9.8 | 6.8 | 16.1 | 14.6 | 20.0 | 18.1 | 14.6 | 15.87 | 52.7% | 32.7% |
| ITF_WOMEN | 4,035 | 8.2 | 6.2 | 13.2 | 13.2 | 20.8 | 21.1 | 17.3 | 18.93 | 59.2% | 38.4% |
| WTA | 502 | 20.9 | 5.0 | 16.7 | 15.9 | 21.9 | 17.3 | 2.2 | 13.18 | 41.4% | 19.5% |
| WTA125 | 272 | 5.2 | 1.8 | 16.5 | 23.5 | 20.6 | 19.5 | 12.9 | 16.74 | 52.9% | 32.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 702 | 24.5 | 12.2 | 30.5 | 16.7 | 10.1 | 4.3 | 1.7 | 7.04 | 16.1% | 6.0% |
| CHALLENGER | 1,981 | 15.8 | 10.8 | 20.3 | 13.9 | 13.6 | 12.4 | 13.3 | 10.71 | 39.3% | 25.7% |
| ITF_MEN | 2,905 | 9.3 | 8.3 | 17.7 | 14.1 | 20.7 | 16.1 | 13.8 | 15.35 | 50.6% | 29.9% |
| ITF_WOMEN | 4,035 | 9.7 | 6.6 | 16.2 | 15.1 | 23.7 | 19.9 | 8.9 | 16.25 | 52.4% | 28.7% |
| WTA | 502 | 23.1 | 12.9 | 34.5 | 14.3 | 10.0 | 3.8 | 1.4 | 7.0 | 15.1% | 5.2% |
| WTA125 | 272 | 21.3 | 11.0 | 26.5 | 18.0 | 16.5 | 5.9 | 0.7 | 7.99 | 23.2% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 374 | 28.9 | 19.8 | 38.2 | 11.8 | 1.3 | 0.0 | 0.0 | 5.24 | 1.3% | 0.0% |
| CHALLENGER | 1,318 | 22.5 | 15.6 | 26.9 | 14.5 | 12.4 | 5.8 | 2.2 | 6.81 | 20.4% | 8.0% |
| DOUBLES | 476 | 4.6 | 3.1 | 13.7 | 10.9 | 24.2 | 20.2 | 23.3 | 22.7 | 67.7% | 43.5% |
| ITF_MEN | 3,031 | 13.3 | 8.3 | 18.8 | 15.4 | 20.7 | 14.2 | 9.2 | 12.77 | 44.2% | 23.5% |
| ITF_WOMEN | 3,467 | 10.3 | 8.6 | 18.7 | 14.1 | 22.9 | 18.8 | 6.6 | 14.24 | 48.3% | 25.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 420 | 18.8 | 10.9 | 25.9 | 19.8 | 16.2 | 7.6 | 0.7 | 8.77 | 24.5% | 8.3% |
| WTA125 | 448 | 14.7 | 12.3 | 21.9 | 19.6 | 18.5 | 9.8 | 3.1 | 10.16 | 31.5% | 13.0% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 698 | 24.8 | 17.6 | 25.4 | 17.1 | 11.9 | 1.7 | 1.6 | 5.93 | 15.2% | 3.3% |
| CHALLENGER | 1,399 | 18.8 | 14.2 | 23.3 | 18.7 | 14.6 | 7.3 | 3.1 | 8.52 | 25.0% | 10.4% |
| ITF_MEN | 2,063 | 12.5 | 10.6 | 22.0 | 16.3 | 19.1 | 13.1 | 6.5 | 11.23 | 38.6% | 19.6% |
| ITF_WOMEN | 2,879 | 12.9 | 8.6 | 18.8 | 17.7 | 22.6 | 16.0 | 3.4 | 12.78 | 42.0% | 19.4% |
| WTA | 500 | 22.6 | 10.0 | 24.6 | 15.8 | 18.4 | 6.4 | 2.2 | 8.36 | 27.0% | 8.6% |
| WTA125 | 262 | 13.7 | 6.9 | 20.2 | 25.9 | 14.5 | 16.8 | 1.9 | 11.39 | 33.2% | 18.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 698 | 19.6 | 15.6 | 26.4 | 17.6 | 15.9 | 3.0 | 1.9 | 6.9 | 20.8% | 4.9% |
| CHALLENGER | 1,399 | 19.2 | 9.0 | 22.2 | 16.6 | 19.8 | 10.3 | 3.0 | 9.94 | 33.1% | 13.3% |
| ITF_MEN | 2,063 | 11.9 | 8.3 | 18.9 | 16.6 | 21.0 | 15.7 | 7.7 | 13.04 | 44.4% | 23.3% |
| ITF_WOMEN | 2,879 | 9.8 | 7.4 | 15.1 | 14.3 | 22.9 | 19.6 | 11.1 | 16.47 | 53.5% | 30.7% |
| WTA | 500 | 21.0 | 5.0 | 16.8 | 16.0 | 21.8 | 17.2 | 2.2 | 13.18 | 41.2% | 19.4% |
| WTA125 | 262 | 5.3 | 1.9 | 16.8 | 24.4 | 19.9 | 20.2 | 11.4 | 16.0 | 51.5% | 31.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 361 | 29.1 | 19.9 | 38.8 | 11.9 | 0.3 | 0.0 | 0.0 | 5.22 | 0.3% | 0.0% |
| CHALLENGER | 1,106 | 24.7 | 17.7 | 29.4 | 14.2 | 11.8 | 2.2 | 0.1 | 6.17 | 14.0% | 2.3% |
| DOUBLES | 433 | 4.6 | 3.0 | 14.1 | 10.8 | 24.5 | 20.3 | 22.6 | 22.7 | 67.4% | 43.0% |
| ITF_MEN | 2,387 | 15.2 | 9.3 | 21.0 | 16.6 | 20.6 | 11.9 | 5.2 | 11.4 | 37.8% | 17.2% |
| ITF_WOMEN | 2,759 | 11.6 | 9.6 | 20.8 | 15.1 | 23.2 | 16.9 | 2.6 | 12.3 | 42.8% | 19.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 390 | 19.2 | 11.5 | 26.7 | 20.0 | 16.7 | 5.9 | 0.0 | 8.66 | 22.6% | 5.9% |
| WTA125 | 366 | 16.9 | 13.7 | 24.6 | 22.7 | 16.7 | 5.2 | 0.3 | 9.01 | 22.1% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 476 | 4.6 | 3.1 | 13.7 | 10.9 | 24.2 | 20.2 | 23.3 | 22.7 | 67.7% | 43.5% |
| singles | 9,207 | 14.5 | 10.3 | 21.4 | 15.0 | 19.1 | 13.5 | 6.1 | 11.11 | 38.7% | 19.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,458 | 13.1 | 9.6 | 19.4 | 15.5 | 15.9 | 14.9 | 11.6 | 12.54 | 42.4% | 26.5% |
| Hard | 7,033 | 12.6 | 8.8 | 18.2 | 15.6 | 19.2 | 15.5 | 10.2 | 13.36 | 44.9% | 25.7% |
| UNKNOWN | 906 | 12.1 | 7.7 | 14.7 | 17.7 | 17.6 | 18.9 | 11.4 | 14.16 | 47.8% | 30.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,019 | 17.5 | 11.4 | 20.3 | 16.8 | 14.7 | 10.5 | 8.7 | 10.23 | 34.0% | 19.2% |
| B | 1,330 | 15.6 | 9.6 | 19.2 | 17.5 | 16.3 | 11.4 | 10.3 | 11.17 | 38.0% | 21.7% |
| C | 1,583 | 12.2 | 9.9 | 20.9 | 14.9 | 17.8 | 14.8 | 9.5 | 12.56 | 42.1% | 24.4% |
| D | 1,919 | 11.1 | 8.8 | 16.5 | 15.3 | 22.6 | 16.4 | 9.5 | 14.17 | 48.4% | 25.9% |
| F | 2,546 | 6.9 | 4.9 | 14.7 | 14.4 | 20.5 | 24.0 | 14.5 | 19.02 | 59.0% | 38.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,787 | 20.9 | 14.2 | 27.2 | 16.3 | 13.4 | 5.6 | 2.3 | 7.42 | 21.3% | 7.9% |
| B | 1,455 | 13.9 | 9.6 | 23.0 | 16.1 | 19.2 | 12.3 | 5.9 | 11.17 | 37.4% | 18.2% |
| C | 1,823 | 11.3 | 8.0 | 19.0 | 14.9 | 21.9 | 14.9 | 10.1 | 13.6 | 46.9% | 25.0% |
| D | 1,608 | 12.2 | 8.6 | 20.9 | 12.8 | 22.3 | 16.3 | 7.0 | 13.11 | 45.5% | 23.3% |
| F | 2,010 | 8.5 | 7.3 | 13.0 | 13.5 | 23.2 | 23.3 | 11.1 | 17.77 | 57.7% | 34.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 3,508 | 16.6 | 10.5 | 19.5 | 17.2 | 15.1 | 10.8 | 10.4 | 10.98 | 36.3% | 21.1% |
| LIMITED | 2,391 | 14.3 | 10.7 | 21.5 | 15.3 | 16.8 | 13.6 | 7.8 | 11.04 | 38.1% | 21.3% |
| POOR | 4,498 | 8.8 | 6.6 | 15.4 | 14.8 | 21.5 | 20.6 | 12.3 | 16.98 | 54.4% | 32.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,573 | 29.9 | 26.3 | 36.8 | 5.2 | 1.6 | 0.2 | 0.0 | 4.45 | 1.8% | 0.2% |
| GAME_SPREAD | 1,503 | 23.2 | 15.6 | 37.1 | 18.6 | 5.0 | 0.3 | 0.2 | 6.2 | 5.5% | 0.5% |
| MATCH_WINNER | 9,683 | 14.1 | 10.0 | 21.1 | 14.8 | 19.4 | 13.8 | 6.9 | 11.52 | 40.1% | 20.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,162 | 28.6 | 18.5 | 31.8 | 11.5 | 7.8 | 1.5 | 0.3 | 5.34 | 9.7% | 1.8% |
| TOTAL_GAMES | 2,395 | 8.0 | 9.7 | 36.3 | 28.8 | 10.9 | 3.8 | 2.6 | 9.54 | 17.3% | 6.3% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,536 | 25.1 | 39.2 | 27.4 | 0.3 | 7.1 | 0.7 | 0.2 | 4.31 | 8.0% | 0.9% |
| GAME_SPREAD | 1,721 | 44.6 | 14.4 | 29.1 | 9.7 | 1.3 | 0.7 | 0.2 | 3.73 | 2.2% | 0.9% |
| TOTAL_GAMES | 2,717 | 3.8 | 6.1 | 42.7 | 36.7 | 7.0 | 1.6 | 2.1 | 9.79 | 10.7% | 3.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,536 | 25.8 | 17.7 | 35.4 | 9.2 | 7.8 | 3.5 | 0.6 | 5.62 | 11.9% | 4.1% |
| GAME_SPREAD | 1,721 | 18.8 | 13.5 | 27.1 | 23.1 | 13.1 | 3.4 | 0.9 | 8.34 | 17.4% | 4.3% |
| TOTAL_GAMES | 2,726 | 6.1 | 8.3 | 37.2 | 28.7 | 13.5 | 3.7 | 2.5 | 9.8 | 19.7% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 10,397 | 44.5% | 26.3% | 13.18 | 34.4% | 15.7% | 10.53 |
| gen1_elo | 10,397 | 44.4% | 25.2% | 12.85 | 34.0% | 15.0% | 10.13 |
| gen1_sr | 10,397 | 52.8% | 30.9% | 16.01 | 43.7% | 20.3% | 13.02 |
| gen2 | 10,397 | 51.5% | 31.6% | 15.59 | 43.6% | 22.6% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 4,811 | 15.4 | 11.7 | 21.7 | 17.1 | 18.3 | 12.1 | 3.7 | 10.31 | 34.1% | 15.8% |
| STALE | 5,586 | 10.3 | 6.4 | 15.1 | 14.6 | 18.3 | 18.7 | 16.6 | 17.02 | 53.5% | 35.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 3,151 | 16.0 | 10.8 | 23.8 | 15.0 | 17.1 | 13.2 | 4.2 | 9.92 | 34.4% | 17.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 20,080 | 3151 | 8283 | 8646 | 26.9 | 198.5 | 1400.4 |
| ge_15pp | 8,515 | 1085 | 2929 | 4501 | 32.2 | 466.7 | 1380.4 |
| ge_25pp | 4,741 | 547 | 1352 | 2842 | 43.4 | 574.8 | 1380.4 |
| lt_10pp | 8,493 | 1594 | 3982 | 2917 | 24.9 | 54.0 | 1201.9 |

Current slate `SL-20261006T204737Z-c5da8c5c`: 1086 priced rows, quote age at build {'median': 7.7, 'max': 7.7}, freshness {'FRESH': 1086}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 260 | 22.7 | 11.9 | 22.7 | 18.9 | 16.9 | 6.5 | 0.4 | 7.79 | 23.8% | 6.9% |
| MARKETS_AGREE | 11 | 45.5 | 54.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.05 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 16 | 0.0 | 0.0 | 25.0 | 43.8 | 31.2 | 0.0 | 0.0 | 12.49 | 31.2% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 10,397 | 288 (2.8%) | 5.6% | 0.0% | {"EXTERNAL_STALE": 260, "AGREES_WITH_KALSHI": 16, "ALL_AGREE": 11, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 4,631 | 67 (1.5%) | 7.5% | 0.0% | {"EXTERNAL_STALE": 62, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 2,732 | 18 (0.7%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 18} |
| fair_v1_ge_25pp_pregame_clean | 1,223 | 18 (1.5%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 18} |
| fair_v1_lt_10pp | 4,130 | 165 (4.0%) | 2.4% | 0.0% | {"EXTERNAL_STALE": 149, "ALL_AGREE": 11, "AGREES_WITH_KALSHI": 4, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,074 | 10.8 | 8.3 | 20.4 | 14.9 | 21.2 | 14.5 | 9.8 | 13.24 | 45.5% | 24.3% |
| 4-10x | 1,536 | 11.1 | 10.2 | 17.4 | 14.4 | 19.7 | 18.0 | 9.2 | 13.84 | 46.9% | 27.2% |
| <2x | 5,466 | 14.4 | 9.5 | 18.3 | 16.7 | 16.7 | 14.0 | 10.4 | 12.5 | 41.1% | 24.4% |
| >=10x | 1,321 | 10.1 | 5.7 | 15.1 | 14.6 | 18.4 | 21.8 | 14.3 | 17.1 | 54.5% | 36.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 2,616 | 13.9 | 8.3 | 20.6 | 15.9 | 16.7 | 13.0 | 11.6 | 12.14 | 41.4% | 24.7% |
| 300-1000 | 2,455 | 11.8 | 9.6 | 16.2 | 15.4 | 21.8 | 16.6 | 8.6 | 14.1 | 47.0% | 25.2% |
| <300 | 2,968 | 7.9 | 6.1 | 15.2 | 14.4 | 20.2 | 22.2 | 13.9 | 18.04 | 56.3% | 36.1% |
| >=3000 | 2,358 | 18.1 | 12.3 | 21.2 | 17.7 | 13.9 | 9.3 | 7.4 | 9.64 | 30.7% | 16.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 309 | 0.5328 | 0.4 | 0.4498 | +0.083 | -0.050 | 0.0044 ± 0.0081 |
| ratio 4-10x | 224 | 0.5912 | 0.4526 | 0.5357 | +0.055 | -0.083 | 0.0011 ± 0.01 |
| ratio <2x | 635 | 0.5381 | 0.4132 | 0.4567 | +0.081 | -0.043 | 0.0127 ± 0.0057 |
| ratio >=10x | 207 | 0.5671 | 0.391 | 0.4686 | +0.099 | -0.078 | 0.011 ± 0.013 |
| thinner_sample 1000-3000 | 356 | 0.5416 | 0.4201 | 0.4579 | +0.084 | -0.038 | 0.0065 ± 0.0074 |
| thinner_sample 300-1000 | 369 | 0.5695 | 0.4328 | 0.4932 | +0.076 | -0.060 | 0.0018 ± 0.0078 |
| thinner_sample <300 | 460 | 0.5547 | 0.3914 | 0.4804 | +0.074 | -0.089 | 0.011 ± 0.0081 |
| thinner_sample >=3000 | 190 | 0.516 | 0.4158 | 0.4211 | +0.095 | -0.005 | 0.0206 ± 0.0083 |
| data_status ADEQUATE | 381 | 0.5235 | 0.417 | 0.4383 | +0.085 | -0.021 | 0.0112 ± 0.0063 |
| data_status LIMITED | 301 | 0.5652 | 0.4329 | 0.495 | +0.070 | -0.062 | -0.0015 ± 0.0087 |
| data_status POOR | 693 | 0.5578 | 0.4028 | 0.4762 | +0.082 | -0.073 | 0.0117 ± 0.0063 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 206 | 0.183 | 0.1836 | -0.0006 ± 0.001 | 0.5415 | 0.5431 | 0.4927 | 0.4783 | 0.4903 | -0.104 ± 0.032 | -0.01 (3) |
| 3-5 | 139 | 0.1809 | 0.1832 | -0.0022 ± 0.003 | 0.5408 | 0.5433 | 0.5178 | 0.4771 | 0.518 | -0.068 ± 0.0375 | 0.02 (1) |
| 5-10 | 288 | 0.2006 | 0.204 | -0.0034 ± 0.004 | 0.5876 | 0.5959 | 0.5239 | 0.4499 | 0.5035 | -0.082 ± 0.0277 | -0.0167 (3) |
| 10-15 | 236 | 0.2216 | 0.2162 | +0.0054 ± 0.0076 | 0.6317 | 0.6158 | 0.5248 | 0.4009 | 0.4407 | -0.103 ± 0.0304 | -0.0633 (3) |
| 15-25 | 296 | 0.2193 | 0.2096 | +0.0097 ± 0.0104 | 0.628 | 0.6038 | 0.5705 | 0.3744 | 0.4459 | -0.079 ± 0.0267 | -0.02 (4) |
| 25-40 | 171 | 0.2124 | 0.1967 | +0.0156 ± 0.0203 | 0.6114 | 0.5672 | 0.6451 | 0.3326 | 0.462 | -0.060 ± 0.0298 | -0.01 (1) |
| 40+ | 39 | 0.3105 | 0.1436 | +0.1669 ± 0.0543 | 0.8355 | 0.4493 | 0.7382 | 0.2969 | 0.3333 | -0.170 ± 0.0539 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 829 | 0.1676 | 0.1681 | -0.0006 ± 0.0005 | 0.5025 | 0.5031 | 0.4888 | 0.474 | 0.509 | -0.038 ± 0.0147 | -0.0188 (8) |
| 3-5 | 614 | 0.1869 | 0.1858 | +0.0011 ± 0.0014 | 0.5527 | 0.5456 | 0.4799 | 0.4401 | 0.4397 | -0.071 ± 0.0179 | 0.02 (1) |
| 5-10 | 1282 | 0.1862 | 0.1868 | -0.0005 ± 0.0018 | 0.5533 | 0.5535 | 0.484 | 0.4104 | 0.4501 | -0.037 ± 0.0122 | -0.0129 (7) |
| 10-15 | 1099 | 0.1963 | 0.1791 | +0.0172 ± 0.0032 | 0.5768 | 0.5274 | 0.4701 | 0.3459 | 0.3412 | -0.085 ± 0.0127 | -0.0633 (3) |
| 15-25 | 1415 | 0.1992 | 0.1584 | +0.0408 ± 0.0042 | 0.5879 | 0.4737 | 0.4862 | 0.2885 | 0.2834 | -0.084 ± 0.0105 | -0.017 (10) |
| 25-40 | 1357 | 0.2132 | 0.1159 | +0.0973 ± 0.0058 | 0.6182 | 0.3624 | 0.5195 | 0.2049 | 0.2093 | -0.062 ± 0.0089 | -0.01 (1) |
| 40+ | 973 | 0.368 | 0.04 | +0.3280 ± 0.0071 | 0.9582 | 0.165 | 0.6181 | 0.103 | 0.0514 | -0.085 ± 0.006 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 151 | 0.1874 | 0.1869 | +0.0005 ± 0.0012 | 0.5524 | 0.5495 | 0.4927 | 0.478 | 0.457 | -0.142 ± 0.0379 | -0.01 (1) |
| 3-5 | 98 | 0.2001 | 0.1995 | +0.0007 ± 0.0036 | 0.577 | 0.5804 | 0.4905 | 0.4509 | 0.4592 | -0.086 ± 0.0486 | 0.02 (1) |
| 5-10 | 248 | 0.1922 | 0.1924 | -0.0002 ± 0.0042 | 0.566 | 0.5664 | 0.5681 | 0.4929 | 0.5242 | -0.088 ± 0.0288 | -0.01 (4) |
| 10-15 | 235 | 0.2309 | 0.2185 | +0.0124 ± 0.0077 | 0.652 | 0.6275 | 0.5846 | 0.4605 | 0.4766 | -0.125 ± 0.0321 | -0.0667 (3) |
| 15-25 | 335 | 0.2241 | 0.2018 | +0.0222 ± 0.0098 | 0.6356 | 0.5831 | 0.5904 | 0.3932 | 0.4418 | -0.107 ± 0.0253 | -0.0167 (3) |
| 25-40 | 219 | 0.2557 | 0.1986 | +0.0571 ± 0.0187 | 0.7125 | 0.5774 | 0.6654 | 0.3538 | 0.4155 | -0.125 ± 0.0303 | -0.025 (2) |
| 40+ | 89 | 0.3599 | 0.1822 | +0.1776 ± 0.0451 | 0.9987 | 0.5364 | 0.7556 | 0.2667 | 0.3483 | -0.063 ± 0.0428 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 719 | 0.1695 | 0.1697 | -0.0002 ± 0.0005 | 0.5066 | 0.5071 | 0.5089 | 0.4947 | 0.5049 | -0.062 ± 0.0165 | -0.0217 (6) |
| 3-5 | 483 | 0.1804 | 0.1773 | +0.0031 ± 0.0015 | 0.5308 | 0.5259 | 0.5111 | 0.4714 | 0.4513 | -0.075 ± 0.0196 | 0.02 (1) |
| 5-10 | 1134 | 0.1801 | 0.1811 | -0.0009 ± 0.0019 | 0.5357 | 0.5356 | 0.5136 | 0.4389 | 0.4806 | -0.032 ± 0.0129 | -0.01 (5) |
| 10-15 | 1016 | 0.1951 | 0.177 | +0.0181 ± 0.0033 | 0.578 | 0.5228 | 0.5127 | 0.3892 | 0.3819 | -0.089 ± 0.0135 | -0.0575 (4) |
| 15-25 | 1507 | 0.209 | 0.1658 | +0.0432 ± 0.0042 | 0.6101 | 0.4937 | 0.5211 | 0.3261 | 0.3165 | -0.095 ± 0.0106 | -0.0143 (7) |
| 25-40 | 1444 | 0.2394 | 0.1276 | +0.1118 ± 0.006 | 0.6807 | 0.3948 | 0.5529 | 0.2355 | 0.2168 | -0.089 ± 0.0094 | -0.015 (6) |
| 40+ | 1266 | 0.3988 | 0.0662 | +0.3326 ± 0.0083 | 1.0406 | 0.2333 | 0.6625 | 0.1235 | 0.0964 | -0.065 ± 0.007 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 210 | 0.1898 | 0.1917 | -0.0019 ± 0.0011 | 0.5584 | 0.5644 | 0.5133 | 0.4985 | 0.5381 | -0.057 ± 0.0306 | -0.01 (5) |
| 3-5 | 150 | 0.178 | 0.1761 | +0.0019 ± 0.0027 | 0.5297 | 0.5253 | 0.5052 | 0.4659 | 0.46 | -0.135 ± 0.0369 | -- (0) |
| 5-10 | 288 | 0.1996 | 0.1999 | -0.0003 ± 0.004 | 0.5866 | 0.5835 | 0.5156 | 0.442 | 0.4757 | -0.093 ± 0.0269 | -0.01 (3) |
| 10-15 | 230 | 0.2154 | 0.217 | -0.0016 ± 0.0076 | 0.6205 | 0.6203 | 0.5443 | 0.4209 | 0.4913 | -0.077 ± 0.0307 | -0.044 (5) |
| 15-25 | 290 | 0.2213 | 0.2055 | +0.0158 ± 0.0104 | 0.639 | 0.5924 | 0.5823 | 0.3879 | 0.4448 | -0.098 ± 0.0264 | -0.03 (1) |
| 25-40 | 174 | 0.2044 | 0.2063 | -0.0019 ± 0.0202 | 0.5935 | 0.5915 | 0.6522 | 0.3388 | 0.4943 | -0.044 ± 0.0293 | 0.0 (1) |
| 40+ | 33 | 0.3471 | 0.1356 | +0.2115 ± 0.058 | 0.918 | 0.43 | 0.7266 | 0.2779 | 0.2727 | -0.196 ± 0.0611 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 834 | 0.1671 | 0.1679 | -0.0007 ± 0.0005 | 0.5032 | 0.5048 | 0.4917 | 0.4769 | 0.5024 | -0.043 ± 0.0143 | -0.0162 (13) |
| 3-5 | 598 | 0.1877 | 0.1829 | +0.0048 ± 0.0014 | 0.5522 | 0.5429 | 0.4768 | 0.4375 | 0.3946 | -0.124 ± 0.0183 | -0.01 (2) |
| 5-10 | 1325 | 0.1865 | 0.1818 | +0.0047 ± 0.0017 | 0.5557 | 0.5377 | 0.4811 | 0.4075 | 0.4106 | -0.069 ± 0.0117 | -0.01 (3) |
| 10-15 | 1041 | 0.1888 | 0.1784 | +0.0104 ± 0.0032 | 0.5592 | 0.5245 | 0.4827 | 0.3595 | 0.3794 | -0.062 ± 0.013 | -0.03 (9) |
| 15-25 | 1548 | 0.201 | 0.1585 | +0.0425 ± 0.004 | 0.5957 | 0.4759 | 0.4907 | 0.2922 | 0.2868 | -0.080 ± 0.0102 | -0.03 (2) |
| 25-40 | 1302 | 0.214 | 0.1149 | +0.0991 ± 0.006 | 0.6197 | 0.3577 | 0.5187 | 0.2 | 0.2074 | -0.064 ± 0.0089 | 0.0 (1) |
| 40+ | 921 | 0.3828 | 0.041 | +0.3418 ± 0.0077 | 1.0021 | 0.1679 | 0.6246 | 0.1022 | 0.0478 | -0.086 ± 0.0064 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 486 | 0.2027 | 0.2029 | -0.0002 ± 0.0007 | 0.5867 | 0.5877 | 0.4963 | 0.4816 | 0.4877 | -0.043 ± 0.0204 | -0.0226 (46) |
| 3-5 | 363 | 0.1952 | 0.1954 | -0.0002 ± 0.0019 | 0.5727 | 0.5716 | 0.4783 | 0.4386 | 0.4628 | -0.033 ± 0.023 | -0.0059 (32) |
| 5-10 | 750 | 0.1886 | 0.1836 | +0.0050 ± 0.0024 | 0.561 | 0.5474 | 0.4666 | 0.3928 | 0.396 | -0.052 ± 0.0159 | -0.005 (72) |
| 10-15 | 500 | 0.2022 | 0.1918 | +0.0104 ± 0.0049 | 0.5931 | 0.564 | 0.4662 | 0.3432 | 0.362 | -0.043 ± 0.0195 | 0.0016 (63) |
| 15-25 | 673 | 0.2366 | 0.2113 | +0.0252 ± 0.0069 | 0.6693 | 0.6084 | 0.535 | 0.3415 | 0.3744 | -0.046 ± 0.0178 | -0.0216 (58) |
| 25-40 | 363 | 0.2494 | 0.1748 | +0.0747 ± 0.0137 | 0.6993 | 0.5198 | 0.5976 | 0.2851 | 0.3196 | -0.067 ± 0.0207 | -0.0216 (25) |
| 40+ | 114 | 0.3798 | 0.1628 | +0.2170 ± 0.0399 | 1.0645 | 0.4966 | 0.7504 | 0.2496 | 0.307 | -0.053 ± 0.036 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1136 | 0.1924 | 0.1927 | -0.0003 ± 0.0005 | 0.5607 | 0.5614 | 0.4931 | 0.478 | 0.4903 | -0.036 ± 0.0129 | -0.0155 (82) |
| 3-5 | 807 | 0.1878 | 0.1871 | +0.0007 ± 0.0012 | 0.5533 | 0.5516 | 0.4896 | 0.4499 | 0.4622 | -0.039 ± 0.0152 | -0.018 (54) |
| 5-10 | 1705 | 0.184 | 0.1775 | +0.0065 ± 0.0015 | 0.5489 | 0.5304 | 0.4641 | 0.3897 | 0.3865 | -0.055 ± 0.0104 | -0.0089 (122) |
| 10-15 | 1280 | 0.1976 | 0.1852 | +0.0124 ± 0.003 | 0.5829 | 0.5473 | 0.475 | 0.352 | 0.3625 | -0.050 ± 0.0119 | -0.0053 (99) |
| 15-25 | 1672 | 0.2277 | 0.1928 | +0.0349 ± 0.0042 | 0.6551 | 0.563 | 0.5243 | 0.3288 | 0.3373 | -0.062 ± 0.0109 | -0.0255 (106) |
| 25-40 | 1208 | 0.2388 | 0.1457 | +0.0931 ± 0.007 | 0.676 | 0.4426 | 0.5604 | 0.2448 | 0.2558 | -0.067 ± 0.0106 | -0.0206 (47) |
| 40+ | 602 | 0.3691 | 0.0872 | +0.2819 ± 0.013 | 1.0035 | 0.2888 | 0.66 | 0.1507 | 0.1395 | -0.068 ± 0.0116 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1375 | 1.142 ± 0.08 | 1.257 | 0.167 | 0.1667 | 0.2082 | 0.1995 |
| gen2 | 1375 | 0.932 ± 0.07 | 1.173 | 0.1823 | 0.1667 | 0.2276 | 0.1994 |
| gen1_elo | 1375 | 1.12 ± 0.078 | 1.229 | 0.1721 | 0.1669 | 0.2071 | 0.1994 |
| gen1_sr | 1375 | 1.173 ± 0.092 | 1.236 | 0.14 | 0.1686 | 0.2227 | 0.1995 |
| gen1_ledger | 3249 | 0.928 ± 0.047 | 1.094 | 0.1647 | 0.1946 | 0.217 | 0.1931 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 8,515)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,486 | 29.2% |
| STALE_QUOTE | market_freshness | 2,014 | 23.6% |
| BOOK_QUALITY | execution | 1,489 | 17.5% |
| POOR_DATA | data | 821 | 9.6% |
| LIMITED_DATA | data | 502 | 5.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 395 | 4.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 388 | 4.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 222 | 2.6% |
| IDENTITY_AMBIGUOUS | mapping | 195 | 2.3% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.0% |

Cause class: coverage 29.2%, market_freshness 23.6%, execution 17.5%, data 15.5%, market_freshness/coverage 7.2%, model_calibration_or_unknown 4.6%, mapping 2.3%, model_calibration 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 68.6%, THIN_PLAYER_HISTORY 58.6%, STALE_PLAYER_DATA 57.4%, STALE_KALSHI_QUOTE 52.9%, MODEL_INTERNAL_DISAGREEMENT 37.3%, ASYMMETRIC_SAMPLE_SIZE 31.6%, WIDE_SPREAD 24.5%, MODEL_HIGH_UNCERTAINTY 15.2%, PLAYER_IDENTITY_RISK 10.5%, LEVEL_TRANSFER_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 6.9%, EVENT_MAPPING_RISK 6.8%, MODEL_CALIBRATION_OUTLIER 2.6%, UNKNOWN 0.5%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 31.3%, POST_SETTLEMENT_OBSERVATION 29.2%, POSSIBLE_IN_PLAY_QUOTE 5.1%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### >= ge_25 pp (N = 4,741)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,952 | 41.2% |
| STALE_QUOTE | market_freshness | 918 | 19.4% |
| BOOK_QUALITY | execution | 781 | 16.5% |
| POOR_DATA | data | 372 | 7.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 216 | 4.6% |
| LIMITED_DATA | data | 150 | 3.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 136 | 2.9% |
| IDENTITY_AMBIGUOUS | mapping | 116 | 2.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 100 | 2.1% |

Cause class: coverage 41.2%, market_freshness 19.4%, execution 16.5%, data 11.0%, market_freshness/coverage 7.4%, mapping 2.5%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.9%, LOW_DATA_QUALITY 71.4%, THIN_PLAYER_HISTORY 60.9%, STALE_KALSHI_QUOTE 60.0%, STALE_PLAYER_DATA 53.9%, MODEL_INTERNAL_DISAGREEMENT 39.7%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 16.6%, PLAYER_IDENTITY_RISK 13.0%, LEVEL_TRANSFER_RISK 7.5%, EVENT_MAPPING_RISK 7.5%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.4%, UNKNOWN 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 43.5%, POST_SETTLEMENT_OBSERVATION 41.2%, POSSIBLE_IN_PLAY_QUOTE 5.1%, CONFIRMED_IN_PLAY_QUOTE 0.8%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 3979, "IDENTITY_AMBIGUOUS": 762}; ticker orientation: {"VERIFIED": 4741}.

Checks: discipline:AMBIGUOUS 207, discipline:PASS 4534, identity_confidence:AMBIGUOUS 616, identity_confidence:PASS 4125, level_mapping:NA 219, level_mapping:PASS 4522, market_pair:AMBIGUOUS 178, market_pair:NA 119, market_pair:PASS 4444, model_complement:NA 88, model_complement:PASS 4653, namesake:PASS 4741, physical_match_id:NA 2009, physical_match_id:PASS 2732, player_ids:PASS 4741, same_pair_other_event:PASS 4741, ticker_orientation:PASS 4741

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,076 | 2.1% | 2.2% | 0.5% | {"market_freshness": 20, "execution": 3} | 5.62 | 0.1949 / 0.1839 (77) | 23.0% | 0.2% | 6.2% | 1.6% |
| CHALLENGER | 3,299 | 19.3% | 6.8% | 13.4% | {"coverage": 394, "market_freshness": 106, "market_freshness/coverage": 72, "model_calibration_or_unknown": 36, "data": 25, "execution": 4} | 7.09 | 0.2196 / 0.202 (776) | 49.0% | 5.4% | 1.4% | 24.1% |
| DOUBLES | 476 | 43.5% | 43.0% | 4.4% | {"market_freshness": 106, "execution": 42, "mapping": 38, "market_freshness/coverage": 14, "coverage": 7} | 22.7 | 0.3142 / 0.227 (171) | 49.2% | 0.0% | 100.0% | 9.0% |
| ITF_MEN | 5,936 | 26.4% | 18.3% | 33.1% | {"coverage": 652, "execution": 351, "market_freshness": 247, "data": 195, "market_freshness/coverage": 102, "mapping": 20, "model_calibration_or_unknown": 1} | 11.27 | 0.2165 / 0.193 (1549) | 43.8% | 56.4% | 6.8% | 25.0% |
| ITF_WOMEN | 7,502 | 28.0% | 19.5% | 44.4% | {"coverage": 882, "market_freshness": 383, "execution": 364, "data": 278, "market_freshness/coverage": 123, "mapping": 52, "model_calibration_or_unknown": 21} | 12.61 | 0.2021 / 0.19 (1625) | 44.9% | 60.8% | 11.2% | 24.9% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 922 | 8.6% | 7.4% | 1.7% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.39 | 0.2026 / 0.197 (137) | 35.8% | 2.3% | 1.3% | 3.5% |
| WTA125 | 720 | 15.6% | 11.0% | 2.4% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 24, "market_freshness": 20, "data": 13, "coverage": 12, "execution": 8, "mapping": 4} | 10.09 | 0.2211 / 0.2059 (247) | 28.7% | 6.0% | 4.2% | 12.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 5 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 6 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 7 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 8 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 10 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 11 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 13 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
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
| 24 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 25 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 27 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 28 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 29 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 30 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 31 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 32 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 256 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 33 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 34 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 35 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 37 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 40 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 41 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 44 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 45 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 227 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.76); no external reference |
| 47 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 48 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 50 | `KXITFMATCH-26OCT06TANEIC-TAN` | ITF_MEN | fair_v1 | 75% / 6% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 213 min (STALE); data LIMITED (grade C, thinner serve sample 1550.0, ratio 1.07); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9785, "by_level_share_of_ge_25pp": {"ATP": 0.0049, "CHALLENGER": 0.1344, "DOUBLES": 0.0437, "ITF_MEN": 0.3307, "ITF_WOMEN": 0.4436, "OTHER": 0.0025, "WTA": 0.0167, "WTA125": 0.0236}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5995, "share_primary_cause_market_settled_or_in_play": 0.486, "share_primary_cause_stale_quote_only": 0.1936}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 4741, "identity_ambiguous_share": 0.1607, "ticker_orientation": {"VERIFIED": 4741}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 2732, "with_external": 18, "coverage": 0.0066, "external_status": {"EXTERNAL_STALE": 18}, "triangulation": {"INSUFFICIENT_INPUTS": 18}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1223, "with_external": 18, "coverage": 0.0147, "external_status": {"EXTERNAL_STALE": 18}, "triangulation": {"INSUFFICIENT_INPUTS": 18}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 596.0, "median_sample_ratio": 2.38, "median_min_matches": 19.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1837, "data_status": {"POOR": 2559, "LIMITED": 1307, "ADEQUATE": 875}, "comparison_lt_10pp": {"median_thinner_serve_points": 1798.0, "median_sample_ratio": 1.75, "median_min_matches": 77.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 309, "model_minus_observed": 0.083, "kalshi_minus_observed": -0.0499, "brier_diff_model_minus_kalshi": 0.0044}, "4-10x": {"n": 224, "model_minus_observed": 0.0554, "kalshi_minus_observed": -0.0831, "brier_diff_model_minus_kalshi": 0.0011}, "<2x": {"n": 635, "model_minus_observed": 0.0814, "kalshi_minus_observed": -0.0435, "brier_diff_model_minus_kalshi": 0.0127}, ">=10x": {"n": 207, "model_minus_observed": 0.0985, "kalshi_minus_observed": -0.0776, "brier_diff_model_minus_kalshi": 0.011}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1375, "model": {"intercept": -0.616, "slope": 0.932, "slope_se": 0.07}, "kalshi_mid_same_rows": {"intercept": 0.22, "slope": 1.173, "slope_se": 0.08}, "mean_extremity_model": 0.1823, "mean_extremity_kalshi": 0.1667, "model_brier": 0.2276, "kalshi_brier": 0.1994, "brier_diff_model_minus_kalshi": 0.0282, "brier_diff_se": 0.0052, "model_logloss": 0.6483, "kalshi_logloss": 0.5799}, "fair_v1": {"n": 1375, "model": {"intercept": -0.411, "slope": 1.142, "slope_se": 0.08}, "kalshi_mid_same_rows": {"intercept": 0.367, "slope": 1.257, "slope_se": 0.083}, "mean_extremity_model": 0.167, "mean_extremity_kalshi": 0.1667, "model_brier": 0.2082, "kalshi_brier": 0.1995, "brier_diff_model_minus_kalshi": 0.0087, "brier_diff_se": 0.0041, "model_logloss": 0.6022, "kalshi_logloss": 0.5801}, "gen1_elo": {"n": 1375, "model": {"intercept": -0.402, "slope": 1.12, "slope_se": 0.078}, "kalshi_mid_same_rows": {"intercept": 0.348, "slope": 1.229, "slope_se": 0.081}, "mean_extremity_model": 0.1721, "mean_extremity_kalshi": 0.1669, "model_brier": 0.2071, "kalshi_brier": 0.1994, "brier_diff_model_minus_kalshi": 0.0077, "brier_diff_se": 0.0041, "model_logloss": 0.6016, "kalshi_logloss": 0.5796}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2628, "share_ge_15": 0.4454, "median_abs_gap": 13.18, "n": 10397}, "gen1_elo": {"share_ge_25": 0.2523, "share_ge_15": 0.444, "median_abs_gap": 12.85, "n": 10397}, "gen1_sr": {"share_ge_25": 0.3094, "share_ge_15": 0.5277, "median_abs_gap": 16.01, "n": 10397}, "gen2": {"share_ge_25": 0.316, "share_ge_15": 0.5151, "median_abs_gap": 15.59, "n": 10397}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1568, "share_ge_15": 0.3442, "median_abs_gap": 10.53, "n": 7801}, "gen1_elo": {"share_ge_25": 0.1502, "share_ge_15": 0.34, "median_abs_gap": 10.13, "n": 7801}, "gen1_sr": {"share_ge_25": 0.2031, "share_ge_15": 0.4371, "median_abs_gap": 13.02, "n": 7801}, "gen2": {"share_ge_25": 0.2261, "share_ge_15": 0.4365, "median_abs_gap": 12.86, "n": 7801}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.62, "share_ge_25_all": 0.0214, "share_ge_25_pregame_clean": 0.0217}, "WTA": {"median_abs_gap_pregame_clean": 8.39, "share_ge_25_all": 0.0857, "share_ge_25_pregame_clean": 0.0742}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2273, "share_within_10pp_all": 0.423, "share_within_10pp_pregame_clean": 0.49, "corr_model_vs_mid_pregame_clean": 0.8395}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 206, "model_brier": 0.183, "kalshi_brier": 0.1836, "brier_diff_model_minus_kalshi": -0.0006}, "10-15": {"n_settled": 236, "model_brier": 0.2216, "kalshi_brier": 0.2162, "brier_diff_model_minus_kalshi": 0.0054}, "15-25": {"n_settled": 296, "model_brier": 0.2193, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.0097}, "25-40": {"n_settled": 171, "model_brier": 0.2124, "kalshi_brier": 0.1967, "brier_diff_model_minus_kalshi": 0.0156}, "3-5": {"n_settled": 139, "model_brier": 0.1809, "kalshi_brier": 0.1832, "brier_diff_model_minus_kalshi": -0.0022}, "40+": {"n_settled": 39, "model_brier": 0.3105, "kalshi_brier": 0.1436, "brier_diff_model_minus_kalshi": 0.1669}, "5-10": {"n_settled": 288, "model_brier": 0.2006, "kalshi_brier": 0.204, "brier_diff_model_minus_kalshi": -0.0034}}}`

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
