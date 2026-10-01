# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-01T17:39Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 9,882): 0-3 13.4%, 3-5 9.2%, 5-10 19.5%, 10-15 14.7%, 15-25 19.7%, 25-40 14.3%, 40+ 9.2%; median gap 12.47 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.3%, Challenger 11.7%, doubles 7.7%). Main tour: ATP 3.6% and WTA 8.8% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,322): MARKET_ALREADY_SETTLED_WHEN_PRICED 45.0%, STALE_QUOTE 23.2%, POOR_DATA 6.9%, BOOK_QUALITY 6.2%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IN_PLAY_QUOTE 5.3%, LIMITED_DATA 3.3%, IDENTITY_AMBIGUOUS 2.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%. By class: coverage 45.0%, market_freshness 23.2%, market_freshness/coverage 11.0%, data 10.2%, execution 6.2%, mapping 2.5%, model_calibration_or_unknown 2.0%.
* **Stale / settled / in-play**: 68.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 55.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,322 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 15.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 9.5% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 750.0 points vs 1940.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.175, Gen-2 0.966, Gen-1 ledger 0.902 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 77 model 0.2348 vs Kalshi 0.1757; n 20 model 0.3007 vs Kalshi 0.1249.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 30,247 model-market comparisons (52,153 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 15,996 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-01T17:35:00.309201+00:00'], shadow board 8,143 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-01T17:35:04.340157+00:00'], Model 4 2,336 rows, 7,936 settled tickers, 1,701 tickers with an external scan.
* By model: {"gen1_ledger": 9335, "gen1_elo": 4096, "fair_v1": 4096, "gen2": 4096, "gen1_sr": 4096, "model4_fundamental": 2267, "model4_conditioned": 2261}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 9,882 | 13.4 | 9.2 | 19.5 | 14.7 | 19.7 | 14.3 | 9.2 | 12.47 | 43.2% | 23.5% |
| MW fair_v1 | 4,096 | 13.6 | 8.8 | 18.8 | 14.8 | 18.9 | 14.9 | 10.3 | 12.92 | 44.1% | 25.2% |
| MW gen1_elo | 4,096 | 13.4 | 8.6 | 20.0 | 14.9 | 18.6 | 14.9 | 9.6 | 12.45 | 43.0% | 24.5% |
| MW gen1_ledger | 5,786 | 13.3 | 9.4 | 20.0 | 14.7 | 20.4 | 13.8 | 8.4 | 12.23 | 42.6% | 22.3% |
| MW gen1_sr | 4,096 | 10.0 | 6.9 | 16.9 | 13.4 | 21.9 | 18.6 | 12.4 | 16.1 | 52.8% | 31.0% |
| MW gen2 | 4,096 | 11.2 | 6.4 | 16.5 | 15.4 | 19.8 | 17.0 | 13.7 | 15.29 | 50.5% | 30.7% |
| all families model4_conditioned | 2,261 | 19.0 | 14.9 | 29.6 | 23.3 | 9.3 | 2.0 | 1.9 | 7.34 | 13.2% | 3.9% |
| all families model4_fundamental | 2,267 | 13.9 | 10.6 | 30.9 | 22.3 | 14.2 | 5.3 | 2.8 | 9.03 | 22.3% | 8.1% |

Configurable thresholds (primary): >=5pp 77.5%, >=10pp 57.9%, >=15pp 43.2%, >=20pp 32.4%, >=25pp 23.5%, >=30pp 17.4%, >=40pp 9.2%, >=50pp 4.2%
Executable gap (model outside the book, before fees): median 10.0pp; >=10pp 50.0%, >=25pp 20.8%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 203 | 22.7 | 19.7 | 23.1 | 13.8 | 15.8 | 1.5 | 3.5 | 6.01 | 20.7% | 4.9% |
| CHALLENGER | 732 | 16.0 | 8.9 | 16.3 | 15.3 | 16.3 | 14.5 | 12.8 | 13.16 | 43.6% | 27.3% |
| ITF_MEN | 1,299 | 11.8 | 8.7 | 19.9 | 13.9 | 18.8 | 15.1 | 11.9 | 13.06 | 45.8% | 27.0% |
| ITF_WOMEN | 1,434 | 10.9 | 6.9 | 16.2 | 15.0 | 20.9 | 19.0 | 11.1 | 15.38 | 51.0% | 30.1% |
| WTA | 354 | 21.5 | 11.0 | 28.2 | 13.8 | 17.5 | 6.8 | 1.1 | 8.09 | 25.4% | 7.9% |
| WTA125 | 74 | 10.8 | 5.4 | 17.6 | 27.0 | 21.6 | 12.2 | 5.4 | 12.8 | 39.2% | 17.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 203 | 23.1 | 13.8 | 24.1 | 15.8 | 17.2 | 2.0 | 3.9 | 7.04 | 23.2% | 5.9% |
| CHALLENGER | 732 | 11.2 | 5.7 | 17.9 | 17.6 | 17.6 | 17.4 | 12.6 | 14.64 | 47.5% | 29.9% |
| ITF_MEN | 1,299 | 10.3 | 5.7 | 16.7 | 16.2 | 20.0 | 16.7 | 14.3 | 15.41 | 51.0% | 31.0% |
| ITF_WOMEN | 1,434 | 8.7 | 6.6 | 14.1 | 13.1 | 19.6 | 19.8 | 18.2 | 18.06 | 57.6% | 38.0% |
| WTA | 354 | 19.2 | 5.4 | 18.1 | 16.4 | 24.3 | 15.2 | 1.4 | 13.12 | 41.0% | 16.7% |
| WTA125 | 74 | 5.4 | 5.4 | 14.9 | 20.3 | 25.7 | 16.2 | 12.2 | 16.39 | 54.0% | 28.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 203 | 30.5 | 12.8 | 27.6 | 10.3 | 9.4 | 5.9 | 3.5 | 6.49 | 18.7% | 9.4% |
| CHALLENGER | 732 | 15.3 | 7.8 | 20.5 | 15.2 | 14.6 | 14.2 | 12.4 | 11.99 | 41.3% | 26.6% |
| ITF_MEN | 1,299 | 10.5 | 9.6 | 18.6 | 15.4 | 18.6 | 16.1 | 11.4 | 13.08 | 46.0% | 27.5% |
| ITF_WOMEN | 1,434 | 9.8 | 6.6 | 17.3 | 14.3 | 23.4 | 18.6 | 10.0 | 16.29 | 52.0% | 28.6% |
| WTA | 354 | 24.6 | 12.7 | 30.2 | 15.0 | 13.3 | 3.1 | 1.1 | 6.99 | 17.5% | 4.2% |
| WTA125 | 74 | 17.6 | 6.8 | 23.0 | 29.7 | 13.5 | 9.5 | 0.0 | 10.52 | 23.0% | 9.5% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 71 | 23.9 | 22.5 | 35.2 | 11.3 | 7.0 | 0.0 | 0.0 | 6.19 | 7.0% | 0.0% |
| CHALLENGER | 777 | 21.2 | 13.9 | 26.2 | 15.8 | 13.6 | 6.6 | 2.6 | 7.45 | 22.8% | 9.1% |
| DOUBLES | 363 | 5.5 | 3.9 | 9.6 | 10.5 | 21.5 | 20.7 | 28.4 | 24.32 | 70.5% | 49.0% |
| ITF_MEN | 1,942 | 14.2 | 9.0 | 18.8 | 13.5 | 21.3 | 13.7 | 9.5 | 12.59 | 44.5% | 23.2% |
| ITF_WOMEN | 1,790 | 9.1 | 8.3 | 17.5 | 14.5 | 23.2 | 18.6 | 8.9 | 15.23 | 50.7% | 27.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 331 | 13.6 | 9.7 | 21.1 | 17.2 | 23.3 | 11.2 | 3.9 | 11.35 | 38.4% | 15.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 202 | 22.3 | 19.8 | 23.3 | 13.9 | 15.8 | 1.5 | 3.5 | 6.01 | 20.8% | 5.0% |
| CHALLENGER | 538 | 20.1 | 11.2 | 19.7 | 18.2 | 17.3 | 8.7 | 4.8 | 9.8 | 30.9% | 13.6% |
| ITF_MEN | 869 | 15.7 | 11.6 | 24.4 | 14.8 | 18.5 | 10.6 | 4.4 | 9.65 | 33.5% | 15.0% |
| ITF_WOMEN | 988 | 14.7 | 8.8 | 19.5 | 17.8 | 22.3 | 12.8 | 4.0 | 12.36 | 39.2% | 16.9% |
| WTA | 353 | 21.5 | 11.1 | 28.3 | 13.9 | 17.6 | 6.5 | 1.1 | 8.09 | 25.2% | 7.6% |
| WTA125 | 73 | 11.0 | 5.5 | 17.8 | 27.4 | 21.9 | 11.0 | 5.5 | 12.79 | 38.4% | 16.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 202 | 23.3 | 13.4 | 24.3 | 15.8 | 17.3 | 2.0 | 4.0 | 7.04 | 23.3% | 5.9% |
| CHALLENGER | 538 | 13.8 | 7.2 | 22.5 | 21.4 | 19.0 | 12.3 | 3.9 | 11.48 | 35.1% | 16.2% |
| ITF_MEN | 869 | 13.2 | 7.0 | 19.9 | 18.5 | 21.2 | 13.8 | 6.3 | 12.49 | 41.3% | 20.1% |
| ITF_WOMEN | 988 | 10.2 | 8.4 | 16.1 | 13.5 | 22.8 | 17.5 | 11.5 | 15.57 | 51.8% | 29.0% |
| WTA | 353 | 19.3 | 5.4 | 18.1 | 16.4 | 24.4 | 15.0 | 1.4 | 13.07 | 40.8% | 16.4% |
| WTA125 | 73 | 5.5 | 5.5 | 15.1 | 20.6 | 26.0 | 16.4 | 11.0 | 16.14 | 53.4% | 27.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 59 | 25.4 | 25.4 | 35.6 | 11.9 | 1.7 | 0.0 | 0.0 | 4.87 | 1.7% | 0.0% |
| CHALLENGER | 637 | 23.7 | 16.2 | 29.2 | 15.4 | 12.9 | 2.5 | 0.2 | 6.68 | 15.5% | 2.7% |
| DOUBLES | 281 | 6.0 | 3.6 | 9.6 | 10.7 | 21.7 | 21.4 | 27.1 | 24.11 | 70.1% | 48.4% |
| ITF_MEN | 1,388 | 17.3 | 10.7 | 22.1 | 14.6 | 21.1 | 10.5 | 3.7 | 9.95 | 35.3% | 14.2% |
| ITF_WOMEN | 1,220 | 11.2 | 9.6 | 21.3 | 16.7 | 24.1 | 15.0 | 2.1 | 12.12 | 41.2% | 17.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 255 | 15.3 | 9.0 | 25.5 | 23.5 | 19.6 | 7.1 | 0.0 | 10.01 | 26.7% | 7.1% |
| WTA125 | 252 | 16.3 | 10.7 | 25.4 | 19.8 | 21.0 | 6.3 | 0.4 | 9.32 | 27.8% | 6.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 363 | 5.5 | 3.9 | 9.6 | 10.5 | 21.5 | 20.7 | 28.4 | 24.32 | 70.5% | 49.0% |
| singles | 5,423 | 13.8 | 9.8 | 20.7 | 14.9 | 20.3 | 13.4 | 7.1 | 11.8 | 40.8% | 20.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 895 | 16.1 | 8.0 | 18.6 | 13.7 | 17.3 | 14.0 | 12.3 | 12.24 | 43.6% | 26.3% |
| Hard | 2,931 | 12.8 | 9.3 | 19.2 | 14.6 | 19.3 | 15.0 | 9.8 | 12.94 | 44.1% | 24.8% |
| UNKNOWN | 270 | 14.1 | 5.9 | 15.2 | 19.6 | 19.3 | 16.7 | 9.3 | 13.58 | 45.2% | 25.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,213 | 18.1 | 10.9 | 21.2 | 15.2 | 17.1 | 10.6 | 7.0 | 9.98 | 34.6% | 17.6% |
| B | 548 | 15.5 | 11.1 | 17.1 | 18.2 | 15.5 | 10.8 | 11.7 | 11.95 | 38.0% | 22.4% |
| C | 699 | 12.6 | 8.6 | 23.6 | 13.2 | 16.2 | 14.9 | 11.0 | 12.36 | 42.1% | 25.9% |
| D | 765 | 12.4 | 8.5 | 17.5 | 13.7 | 21.2 | 14.8 | 11.9 | 14.14 | 47.8% | 26.7% |
| F | 871 | 7.9 | 4.8 | 13.8 | 14.0 | 23.6 | 23.6 | 12.2 | 18.92 | 59.5% | 35.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,762 | 18.8 | 12.0 | 26.3 | 16.9 | 16.6 | 6.8 | 2.7 | 8.57 | 26.1% | 9.5% |
| B | 957 | 14.1 | 9.1 | 21.5 | 16.5 | 18.9 | 12.3 | 7.5 | 11.55 | 38.8% | 19.9% |
| C | 1,188 | 11.2 | 8.4 | 15.6 | 14.1 | 21.8 | 15.4 | 13.6 | 15.33 | 50.8% | 29.0% |
| D | 897 | 11.4 | 8.2 | 20.3 | 11.9 | 24.0 | 15.6 | 8.6 | 14.24 | 48.2% | 24.2% |
| F | 982 | 6.8 | 7.2 | 12.4 | 12.2 | 23.5 | 24.4 | 13.3 | 19.52 | 61.3% | 37.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,487 | 16.5 | 10.1 | 20.2 | 16.5 | 16.8 | 10.8 | 9.0 | 10.7 | 36.6% | 19.8% |
| LIMITED | 956 | 15.0 | 10.8 | 22.4 | 13.5 | 15.4 | 13.4 | 9.6 | 10.86 | 38.4% | 23.0% |
| POOR | 1,653 | 10.2 | 6.5 | 15.4 | 13.8 | 22.8 | 19.4 | 11.9 | 16.92 | 54.1% | 31.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 325 | 34.8 | 23.1 | 32.9 | 5.8 | 2.5 | 0.9 | 0.0 | 4.14 | 3.4% | 0.9% |
| GAME_SPREAD | 394 | 20.3 | 16.5 | 36.3 | 16.0 | 9.1 | 1.3 | 0.5 | 6.5 | 10.9% | 1.8% |
| MATCH_WINNER | 5,786 | 13.3 | 9.4 | 20.0 | 14.7 | 20.4 | 13.8 | 8.4 | 12.23 | 42.6% | 22.3% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,686 | 21.9 | 13.5 | 29.9 | 17.4 | 13.8 | 2.8 | 0.7 | 7.06 | 17.2% | 3.4% |
| TOTAL_GAMES | 1,120 | 9.9 | 9.0 | 26.2 | 25.2 | 17.1 | 8.0 | 4.5 | 10.68 | 29.6% | 12.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 753 | 28.6 | 31.1 | 27.0 | 0.8 | 10.2 | 2.0 | 0.4 | 4.3 | 12.6% | 2.4% |
| GAME_SPREAD | 455 | 37.1 | 13.4 | 24.4 | 20.4 | 2.9 | 1.3 | 0.4 | 4.81 | 4.6% | 1.8% |
| TOTAL_GAMES | 1,053 | 4.4 | 4.1 | 33.7 | 40.5 | 11.4 | 2.3 | 3.6 | 10.71 | 17.3% | 5.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 753 | 23.9 | 17.4 | 33.3 | 8.9 | 10.4 | 5.0 | 1.1 | 5.94 | 16.5% | 6.1% |
| GAME_SPREAD | 455 | 17.1 | 10.3 | 25.1 | 24.2 | 16.3 | 5.0 | 2.0 | 9.62 | 23.3% | 7.0% |
| TOTAL_GAMES | 1,059 | 5.5 | 5.8 | 31.7 | 31.0 | 16.0 | 5.6 | 4.4 | 10.84 | 26.0% | 10.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4,096 | 44.1% | 25.2% | 12.92 | 33.2% | 13.9% | 9.98 |
| gen1_elo | 4,096 | 43.0% | 24.5% | 12.45 | 31.7% | 13.8% | 9.53 |
| gen1_sr | 4,096 | 52.8% | 31.0% | 16.1 | 43.8% | 20.1% | 13.03 |
| gen2 | 4,096 | 50.5% | 30.7% | 15.29 | 42.7% | 21.1% | 12.98 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,626 | 17.6 | 12.3 | 23.1 | 15.1 | 18.6 | 10.0 | 3.3 | 9.27 | 31.9% | 13.3% |
| STALE | 2,470 | 10.9 | 6.5 | 15.9 | 14.5 | 19.0 | 18.1 | 14.9 | 16.17 | 52.1% | 33.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,127 | 15.2 | 10.3 | 21.8 | 15.9 | 20.0 | 12.2 | 4.7 | 10.76 | 36.8% | 16.9% |
| STALE | 2,659 | 11.1 | 8.4 | 17.9 | 13.2 | 20.8 | 15.8 | 12.9 | 14.76 | 49.5% | 28.7% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 9,882 | 0 | 4753 | 5129 | 31.0 | 166.6 | 1400.4 |
| ge_15pp | 4,273 | 0 | 1671 | 2602 | 34.7 | 411.0 | 1380.4 |
| ge_25pp | 2,322 | 0 | 743 | 1579 | 49.5 | 562.2 | 1380.4 |
| lt_10pp | 4,156 | 0 | 2339 | 1817 | 28.3 | 54.8 | 1102.2 |

Current slate `SL-20261001T173934Z-bbf2c1bc`: 397 priced rows, quote age at build {'median': 26.3, 'max': 45.9}, freshness {'AGING': 247, 'STALE': 150}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 159 | 23.9 | 11.9 | 22.6 | 19.5 | 15.7 | 6.3 | 0.0 | 7.14 | 22.0% | 6.3% |
| MARKETS_AGREE | 11 | 63.6 | 36.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.19 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 18 | 0.0 | 0.0 | 16.7 | 38.9 | 38.9 | 5.6 | 0.0 | 13.48 | 44.4% | 5.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 4,096 | 189 (4.6%) | 9.5% | 0.0% | {"EXTERNAL_STALE": 159, "AGREES_WITH_KALSHI": 18, "ALL_AGREE": 11, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 1,806 | 43 (2.4%) | 18.6% | 0.0% | {"EXTERNAL_STALE": 35, "AGREES_WITH_KALSHI": 8} |
| fair_v1_ge_25pp | 1,033 | 11 (1.1%) | 9.1% | 0.0% | {"EXTERNAL_STALE": 10, "AGREES_WITH_KALSHI": 1} |
| fair_v1_ge_25pp_pregame_clean | 419 | 11 (2.6%) | 9.1% | 0.0% | {"EXTERNAL_STALE": 10, "AGREES_WITH_KALSHI": 1} |
| fair_v1_lt_10pp | 1,686 | 108 (6.4%) | 2.8% | 0.0% | {"EXTERNAL_STALE": 93, "ALL_AGREE": 11, "AGREES_WITH_KALSHI": 3, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 813 | 12.3 | 7.6 | 18.7 | 15.2 | 20.8 | 15.1 | 10.2 | 13.55 | 46.1% | 25.3% |
| 4-10x | 571 | 12.3 | 9.8 | 18.7 | 14.2 | 18.2 | 15.8 | 11.0 | 13.25 | 45.0% | 26.8% |
| <2x | 2,208 | 14.9 | 9.7 | 19.6 | 15.2 | 17.8 | 12.9 | 9.8 | 11.87 | 40.6% | 22.7% |
| >=10x | 504 | 11.5 | 5.4 | 15.5 | 12.5 | 21.0 | 22.2 | 11.9 | 17.89 | 55.2% | 34.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,041 | 13.4 | 9.5 | 21.6 | 15.3 | 17.1 | 12.2 | 10.8 | 11.96 | 40.2% | 23.1% |
| 300-1000 | 1,019 | 13.8 | 8.2 | 17.7 | 15.7 | 20.0 | 14.9 | 9.7 | 13.48 | 44.6% | 24.6% |
| <300 | 1,049 | 8.9 | 5.8 | 14.8 | 12.2 | 22.5 | 22.3 | 13.5 | 18.88 | 58.3% | 35.8% |
| >=3000 | 987 | 18.4 | 11.8 | 21.3 | 15.9 | 15.7 | 9.8 | 7.0 | 9.78 | 32.5% | 16.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 170 | 0.5168 | 0.3867 | 0.4 | +0.117 | -0.013 | 0.0177 ± 0.011 |
| ratio 4-10x | 122 | 0.5761 | 0.4445 | 0.4754 | +0.101 | -0.031 | 0.0137 ± 0.0128 |
| ratio <2x | 330 | 0.5316 | 0.4118 | 0.4697 | +0.062 | -0.058 | 0.0061 ± 0.0073 |
| ratio >=10x | 120 | 0.5362 | 0.3774 | 0.4417 | +0.095 | -0.064 | 0.0198 ± 0.0161 |
| thinner_sample 1000-3000 | 189 | 0.5379 | 0.4175 | 0.4656 | +0.072 | -0.048 | 0.0006 ± 0.0097 |
| thinner_sample 300-1000 | 217 | 0.5533 | 0.4308 | 0.47 | +0.083 | -0.039 | 0.0054 ± 0.0092 |
| thinner_sample <300 | 249 | 0.5277 | 0.3695 | 0.4257 | +0.102 | -0.056 | 0.0252 ± 0.0107 |
| thinner_sample >=3000 | 87 | 0.5153 | 0.4225 | 0.4368 | +0.079 | -0.014 | 0.0171 ± 0.0117 |
| data_status ADEQUATE | 190 | 0.5222 | 0.4144 | 0.4579 | +0.064 | -0.043 | 0.0026 ± 0.0089 |
| data_status LIMITED | 170 | 0.5599 | 0.4436 | 0.4941 | +0.066 | -0.051 | 0.0008 ± 0.0102 |
| data_status POOR | 382 | 0.5329 | 0.3848 | 0.4267 | +0.106 | -0.042 | 0.0221 ± 0.0081 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 125 | 0.1805 | 0.1812 | -0.0007 ± 0.0013 | 0.5346 | 0.5367 | 0.4911 | 0.4764 | 0.496 | -0.093 ± 0.0414 | -0.01 (3) |
| 3-5 | 78 | 0.1675 | 0.1641 | +0.0034 ± 0.0038 | 0.5147 | 0.5017 | 0.5131 | 0.4721 | 0.4487 | -0.115 ± 0.0488 | 0.02 (1) |
| 5-10 | 160 | 0.1956 | 0.1966 | -0.0009 ± 0.0052 | 0.5758 | 0.577 | 0.5221 | 0.4476 | 0.4938 | -0.064 ± 0.0355 | -0.02 (2) |
| 10-15 | 123 | 0.2133 | 0.2071 | +0.0062 ± 0.0103 | 0.6092 | 0.5948 | 0.5266 | 0.4025 | 0.439 | -0.074 ± 0.0412 | -0.0633 (3) |
| 15-25 | 159 | 0.212 | 0.2107 | +0.0013 ± 0.0143 | 0.6117 | 0.6018 | 0.5583 | 0.3612 | 0.4591 | -0.015 ± 0.0351 | -0.02 (4) |
| 25-40 | 77 | 0.2348 | 0.1757 | +0.0591 ± 0.0299 | 0.6586 | 0.5212 | 0.5992 | 0.283 | 0.3377 | -0.080 ± 0.0456 | -0.01 (1) |
| 40+ | 20 | 0.3007 | 0.1249 | +0.1758 ± 0.072 | 0.781 | 0.4036 | 0.6658 | 0.2205 | 0.25 | -0.082 ± 0.0678 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 360 | 0.1654 | 0.1661 | -0.0007 ± 0.0007 | 0.4949 | 0.4966 | 0.5058 | 0.4908 | 0.525 | -0.032 ± 0.0226 | -0.0188 (8) |
| 3-5 | 234 | 0.167 | 0.166 | +0.0010 ± 0.0022 | 0.5106 | 0.5021 | 0.4896 | 0.4494 | 0.4573 | -0.050 ± 0.0275 | 0.02 (1) |
| 5-10 | 504 | 0.1827 | 0.1828 | -0.0001 ± 0.0028 | 0.5435 | 0.5405 | 0.4753 | 0.4023 | 0.4444 | -0.022 ± 0.0192 | -0.0133 (6) |
| 10-15 | 397 | 0.1921 | 0.176 | +0.0161 ± 0.0053 | 0.5646 | 0.516 | 0.476 | 0.3519 | 0.3476 | -0.071 ± 0.021 | -0.0633 (3) |
| 15-25 | 560 | 0.1892 | 0.1592 | +0.0300 ± 0.0067 | 0.5656 | 0.4716 | 0.4773 | 0.28 | 0.3018 | -0.038 ± 0.0165 | -0.017 (10) |
| 25-40 | 503 | 0.2117 | 0.0891 | +0.1226 ± 0.0085 | 0.6136 | 0.2978 | 0.4935 | 0.1758 | 0.1431 | -0.079 ± 0.0129 | -0.01 (1) |
| 40+ | 356 | 0.3623 | 0.0351 | +0.3272 ± 0.0106 | 0.9387 | 0.1498 | 0.611 | 0.0981 | 0.0449 | -0.080 ± 0.009 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 78 | 0.1735 | 0.176 | -0.0025 ± 0.0016 | 0.5197 | 0.5236 | 0.516 | 0.5015 | 0.5769 | -0.017 ± 0.0463 | -0.01 (1) |
| 3-5 | 59 | 0.2157 | 0.2148 | +0.0009 ± 0.0049 | 0.6124 | 0.6183 | 0.4929 | 0.4537 | 0.4576 | -0.074 ± 0.0641 | 0.02 (1) |
| 5-10 | 139 | 0.1815 | 0.1739 | +0.0076 ± 0.0054 | 0.5443 | 0.5244 | 0.5739 | 0.4982 | 0.4748 | -0.132 ± 0.0357 | -0.01 (3) |
| 10-15 | 133 | 0.2191 | 0.2063 | +0.0127 ± 0.01 | 0.6256 | 0.5975 | 0.5855 | 0.4607 | 0.4812 | -0.083 ± 0.0408 | -0.0667 (3) |
| 15-25 | 177 | 0.2149 | 0.1953 | +0.0196 ± 0.0131 | 0.6135 | 0.5642 | 0.5793 | 0.3825 | 0.435 | -0.070 ± 0.0341 | -0.0167 (3) |
| 25-40 | 109 | 0.263 | 0.1889 | +0.0742 ± 0.0258 | 0.7316 | 0.5509 | 0.6453 | 0.3365 | 0.367 | -0.120 ± 0.0428 | -0.025 (2) |
| 40+ | 47 | 0.3615 | 0.1989 | +0.1627 ± 0.0658 | 0.9851 | 0.5841 | 0.7367 | 0.2409 | 0.3404 | +0.001 ± 0.0602 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 293 | 0.1521 | 0.1536 | -0.0015 ± 0.0008 | 0.4583 | 0.4616 | 0.5525 | 0.5381 | 0.5802 | -0.010 ± 0.023 | -0.0217 (6) |
| 3-5 | 170 | 0.176 | 0.176 | +0.0001 ± 0.0025 | 0.5197 | 0.5268 | 0.5461 | 0.5067 | 0.5235 | -0.035 ± 0.0326 | 0.02 (1) |
| 5-10 | 445 | 0.1756 | 0.1733 | +0.0023 ± 0.003 | 0.528 | 0.5165 | 0.5288 | 0.4536 | 0.4742 | -0.040 ± 0.0198 | -0.01 (4) |
| 10-15 | 429 | 0.1898 | 0.1773 | +0.0124 ± 0.0051 | 0.5592 | 0.5226 | 0.5248 | 0.4002 | 0.4219 | -0.040 ± 0.0207 | -0.0575 (4) |
| 15-25 | 565 | 0.1981 | 0.158 | +0.0401 ± 0.0066 | 0.582 | 0.4726 | 0.5089 | 0.314 | 0.3133 | -0.071 ± 0.0168 | -0.0143 (7) |
| 25-40 | 534 | 0.225 | 0.1122 | +0.1128 ± 0.0092 | 0.6502 | 0.3523 | 0.5344 | 0.2197 | 0.2022 | -0.075 ± 0.0148 | -0.015 (6) |
| 40+ | 478 | 0.3985 | 0.0652 | +0.3333 ± 0.0135 | 1.0449 | 0.2311 | 0.6592 | 0.1218 | 0.0941 | -0.059 ± 0.0111 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 121 | 0.1741 | 0.1763 | -0.0022 ± 0.0013 | 0.5172 | 0.5229 | 0.5105 | 0.4964 | 0.5455 | -0.041 ± 0.0387 | -0.01 (5) |
| 3-5 | 81 | 0.1641 | 0.1615 | +0.0027 ± 0.0036 | 0.499 | 0.4919 | 0.5118 | 0.4723 | 0.4568 | -0.128 ± 0.0483 | -- (0) |
| 5-10 | 151 | 0.1989 | 0.1986 | +0.0003 ± 0.0054 | 0.5886 | 0.5806 | 0.508 | 0.4365 | 0.4702 | -0.063 ± 0.0364 | -0.01 (2) |
| 10-15 | 132 | 0.2124 | 0.2127 | -0.0004 ± 0.01 | 0.612 | 0.6082 | 0.5498 | 0.4259 | 0.5 | -0.051 ± 0.0404 | -0.044 (5) |
| 15-25 | 155 | 0.2142 | 0.2042 | +0.0100 ± 0.0141 | 0.6212 | 0.5881 | 0.5738 | 0.3799 | 0.4516 | -0.045 ± 0.0348 | -0.03 (1) |
| 25-40 | 87 | 0.2352 | 0.1816 | +0.0536 ± 0.0287 | 0.6623 | 0.5386 | 0.5931 | 0.2775 | 0.3448 | -0.068 ± 0.0435 | 0.0 (1) |
| 40+ | 15 | 0.3193 | 0.1394 | +0.1799 ± 0.0908 | 0.8257 | 0.4377 | 0.6747 | 0.2183 | 0.2667 | -0.071 ± 0.0858 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 348 | 0.1624 | 0.1627 | -0.0003 ± 0.0008 | 0.49 | 0.4907 | 0.5067 | 0.4921 | 0.5115 | -0.044 ± 0.0219 | -0.0162 (13) |
| 3-5 | 234 | 0.1744 | 0.1715 | +0.0029 ± 0.0022 | 0.5197 | 0.5112 | 0.4804 | 0.4412 | 0.4274 | -0.079 ± 0.0278 | -0.01 (2) |
| 5-10 | 501 | 0.1857 | 0.1825 | +0.0032 ± 0.0029 | 0.5535 | 0.5354 | 0.466 | 0.393 | 0.4112 | -0.038 ± 0.0192 | -0.01 (2) |
| 10-15 | 412 | 0.1943 | 0.1829 | +0.0113 ± 0.0053 | 0.5734 | 0.5348 | 0.4914 | 0.368 | 0.3859 | -0.051 ± 0.0211 | -0.03 (9) |
| 15-25 | 586 | 0.1808 | 0.1435 | +0.0374 ± 0.0062 | 0.5482 | 0.4355 | 0.4809 | 0.2821 | 0.2884 | -0.052 ± 0.0152 | -0.03 (2) |
| 25-40 | 502 | 0.2154 | 0.0964 | +0.1190 ± 0.0088 | 0.6234 | 0.3145 | 0.4942 | 0.1749 | 0.1494 | -0.075 ± 0.0134 | 0.0 (1) |
| 40+ | 331 | 0.3792 | 0.0343 | +0.3449 ± 0.0112 | 0.9879 | 0.1489 | 0.6143 | 0.0962 | 0.0332 | -0.089 ± 0.0092 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 402 | 0.2018 | 0.2019 | -0.0000 ± 0.0008 | 0.5839 | 0.584 | 0.5012 | 0.4867 | 0.4876 | -0.043 ± 0.0225 | -0.0226 (46) |
| 3-5 | 284 | 0.1922 | 0.1918 | +0.0005 ± 0.0021 | 0.5646 | 0.5601 | 0.4614 | 0.4215 | 0.4401 | -0.032 ± 0.0258 | -0.0059 (32) |
| 5-10 | 615 | 0.1868 | 0.1818 | +0.0050 ± 0.0026 | 0.5566 | 0.5428 | 0.4586 | 0.3853 | 0.3886 | -0.043 ± 0.0172 | -0.0049 (71) |
| 10-15 | 406 | 0.2024 | 0.1903 | +0.0122 ± 0.0054 | 0.5945 | 0.5585 | 0.4541 | 0.3307 | 0.3424 | -0.040 ± 0.0215 | 0.0016 (63) |
| 15-25 | 544 | 0.2352 | 0.2095 | +0.0256 ± 0.0077 | 0.664 | 0.6058 | 0.5285 | 0.3353 | 0.3658 | -0.034 ± 0.0196 | -0.0216 (58) |
| 25-40 | 261 | 0.2626 | 0.1653 | +0.0973 ± 0.0158 | 0.7258 | 0.4997 | 0.5697 | 0.2581 | 0.2567 | -0.066 ± 0.0248 | -0.0216 (25) |
| 40+ | 91 | 0.4328 | 0.1575 | +0.2753 ± 0.0447 | 1.217 | 0.4875 | 0.7317 | 0.2235 | 0.2308 | -0.065 ± 0.0435 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 744 | 0.193 | 0.1927 | +0.0004 ± 0.0005 | 0.5635 | 0.562 | 0.4953 | 0.4808 | 0.4704 | -0.052 ± 0.0161 | -0.0155 (82) |
| 3-5 | 522 | 0.1982 | 0.197 | +0.0012 ± 0.0016 | 0.576 | 0.5702 | 0.468 | 0.4281 | 0.4349 | -0.039 ± 0.0195 | -0.018 (54) |
| 5-10 | 1123 | 0.1853 | 0.1789 | +0.0064 ± 0.0019 | 0.5533 | 0.5337 | 0.4434 | 0.3696 | 0.3669 | -0.044 ± 0.0127 | -0.0089 (121) |
| 10-15 | 817 | 0.1978 | 0.184 | +0.0139 ± 0.0038 | 0.5824 | 0.5416 | 0.4475 | 0.3239 | 0.3293 | -0.041 ± 0.0149 | -0.0053 (99) |
| 15-25 | 1138 | 0.2219 | 0.1867 | +0.0352 ± 0.005 | 0.6397 | 0.5482 | 0.5009 | 0.3052 | 0.3128 | -0.045 ± 0.0128 | -0.0255 (106) |
| 25-40 | 784 | 0.2447 | 0.1285 | +0.1162 ± 0.0081 | 0.6905 | 0.4024 | 0.5278 | 0.2124 | 0.1875 | -0.070 ± 0.0127 | -0.0206 (47) |
| 40+ | 466 | 0.3925 | 0.0795 | +0.3130 ± 0.0142 | 1.0718 | 0.2676 | 0.653 | 0.1364 | 0.103 | -0.076 ± 0.0134 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 742 | 1.175 ± 0.107 | 1.224 | 0.1717 | 0.1897 | 0.2035 | 0.1913 |
| gen2 | 742 | 0.966 ± 0.093 | 1.153 | 0.1889 | 0.1888 | 0.2215 | 0.1921 |
| gen1_elo | 742 | 1.134 ± 0.104 | 1.215 | 0.1773 | 0.1902 | 0.2034 | 0.1914 |
| gen1_sr | 742 | 1.179 ± 0.122 | 1.205 | 0.1452 | 0.1913 | 0.2181 | 0.1912 |
| gen1_ledger | 2603 | 0.902 ± 0.053 | 1.073 | 0.1624 | 0.2014 | 0.2185 | 0.1906 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 4,273)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,344 | 31.4% |
| STALE_QUOTE | market_freshness | 1,225 | 28.7% |
| POOR_DATA | data | 366 | 8.6% |
| BOOK_QUALITY | execution | 297 | 7.0% |
| LIMITED_DATA | data | 274 | 6.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 260 | 6.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 211 | 4.9% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 210 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 83 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 31.4%, market_freshness 28.7%, data 15.0%, market_freshness/coverage 11.0%, execution 7.0%, model_calibration_or_unknown 4.9%, mapping 1.9%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.8%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 65.9%, STALE_KALSHI_QUOTE 60.9%, STALE_PLAYER_DATA 57.3%, THIN_PLAYER_HISTORY 53.4%, MODEL_INTERNAL_DISAGREEMENT 32.8%, ASYMMETRIC_SAMPLE_SIZE 29.3%, WIDE_SPREAD 15.7%, PLAYER_IDENTITY_RISK 11.6%, MODEL_HIGH_UNCERTAINTY 11.4%, LEVEL_TRANSFER_RISK 9.2%, EVENT_MAPPING_RISK 7.2%, LOW_DISPLAYED_LIQUIDITY 4.6%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.8%, EXTERNAL_MARKET_REJECTION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 34.3%, POST_SETTLEMENT_OBSERVATION 31.4%, POSSIBLE_IN_PLAY_QUOTE 6.9%, CONFIRMED_IN_PLAY_QUOTE 2.6%

### >= ge_25 pp (N = 2,322)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,044 | 45.0% |
| STALE_QUOTE | market_freshness | 539 | 23.2% |
| POOR_DATA | data | 160 | 6.9% |
| BOOK_QUALITY | execution | 143 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 131 | 5.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 124 | 5.3% |
| LIMITED_DATA | data | 76 | 3.3% |
| IDENTITY_AMBIGUOUS | mapping | 58 | 2.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 47 | 2.0% |

Cause class: coverage 45.0%, market_freshness 23.2%, market_freshness/coverage 11.0%, data 10.2%, execution 6.2%, mapping 2.5%, model_calibration_or_unknown 2.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 70.2%, STALE_KALSHI_QUOTE 68.0%, THIN_PLAYER_HISTORY 55.9%, STALE_PLAYER_DATA 55.5%, MODEL_INTERNAL_DISAGREEMENT 33.7%, ASYMMETRIC_SAMPLE_SIZE 31.8%, PLAYER_IDENTITY_RISK 14.6%, WIDE_SPREAD 14.3%, MODEL_HIGH_UNCERTAINTY 12.6%, EVENT_MAPPING_RISK 9.0%, LEVEL_TRANSFER_RISK 8.8%, LOW_DISPLAYED_LIQUIDITY 4.9%, MODEL_CALIBRATION_OUTLIER 3.1%, UNKNOWN 0.3%, EXTERNAL_MARKET_REJECTION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 48.0%, POST_SETTLEMENT_OBSERVATION 45.0%, POSSIBLE_IN_PLAY_QUOTE 6.6%, CONFIRMED_IN_PLAY_QUOTE 2.9%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 1952, "IDENTITY_AMBIGUOUS": 370}; ticker orientation: {"VERIFIED": 2322}.

Checks: discipline:AMBIGUOUS 178, discipline:PASS 2144, identity_confidence:AMBIGUOUS 338, identity_confidence:PASS 1984, level_mapping:NA 190, level_mapping:PASS 2132, market_pair:AMBIGUOUS 62, market_pair:NA 63, market_pair:PASS 2197, model_complement:NA 36, model_complement:PASS 2286, namesake:PASS 2322, physical_match_id:NA 1289, physical_match_id:PASS 1033, player_ids:PASS 2322, same_pair_other_event:PASS 2322, ticker_orientation:PASS 2322

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 274 | 3.6% | 3.8% | 0.4% | {"market_freshness": 10} | 6.01 | 0.1838 / 0.1834 (45) | 36.5% | 0.0% | 0.7% | 4.7% |
| CHALLENGER | 1,509 | 18.0% | 7.7% | 11.7% | {"coverage": 144, "market_freshness": 58, "market_freshness/coverage": 37, "data": 17, "model_calibration_or_unknown": 12, "execution": 3} | 7.51 | 0.2245 / 0.2067 (513) | 51.6% | 4.3% | 0.7% | 22.1% |
| DOUBLES | 363 | 49.0% | 48.4% | 7.7% | {"market_freshness": 88, "market_freshness/coverage": 36, "execution": 28, "mapping": 20, "coverage": 6} | 24.11 | 0.324 / 0.2247 (149) | 60.6% | 0.0% | 100.0% | 22.6% |
| ITF_MEN | 3,241 | 24.8% | 14.5% | 34.5% | {"coverage": 409, "market_freshness": 157, "data": 88, "execution": 71, "market_freshness/coverage": 66, "mapping": 10, "model_calibration_or_unknown": 1} | 9.85 | 0.2089 / 0.1822 (1205) | 54.1% | 51.4% | 5.8% | 30.4% |
| ITF_WOMEN | 3,224 | 28.6% | 17.0% | 39.8% | {"coverage": 473, "market_freshness": 191, "data": 114, "market_freshness/coverage": 74, "execution": 32, "mapping": 26, "model_calibration_or_unknown": 13} | 12.21 | 0.2059 / 0.1865 (1069) | 56.7% | 55.1% | 6.8% | 31.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.5% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 717 | 8.8% | 7.4% | 2.7% | {"market_freshness": 22, "market_freshness/coverage": 14, "model_calibration_or_unknown": 9, "data": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.48 | 0.1995 / 0.1973 (113) | 37.5% | 2.9% | 1.7% | 15.2% |
| WTA125 | 405 | 15.6% | 8.9% | 2.7% | {"market_freshness/coverage": 27, "market_freshness": 11, "model_calibration_or_unknown": 10, "data": 8, "coverage": 7} | 10.53 | 0.2278 / 0.204 (209) | 34.3% | 9.4% | 0.5% | 19.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 5 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 6 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 7 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 8 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 9 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 10 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 11 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 13 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 14 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 15 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 16 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 17 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 19 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 20 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 21 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 22 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 23 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 24 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 25 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 26 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 28 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 29 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 30 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 32 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 183 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 33 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 34 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 35 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 37 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 86 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 38 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 39 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 40 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 41 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 42 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.1h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 793 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 43 | `KXITFWMATCH-26OCT01TANVED-TAN` | ITF_WOMEN | fair_v1 | 76% / 8% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 167 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 45 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFWMATCH-26SEP24BOUKUR-BOU` | ITF_WOMEN | gen1_ledger | 76% / 8% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 1497.0, ratio 2.48); no external reference |
| 47 | `KXATPCHALLENGERMATCH-26SEP28TABSAN-SAN` | CHALLENGER | gen1_ledger | 70% / 4% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 48 min (STALE); no external reference |
| 48 | `KXITFWMATCH-26SEP22SHCPAS-PAS` | ITF_WOMEN | gen1_ledger | 69% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 199 min (STALE); data POOR (grade F, thinner serve sample 239.0, ratio 5.93); no external reference |
| 49 | `KXWTADOUBLES-26SEP20DETKHRPRETAR-PRETAR` | DOUBLES | gen1_ledger | 84% / 18% | +66 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26SEP29KRURAY-KRU` | ITF_WOMEN | fair_v1 | 78% / 12% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 126 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 223.0); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9686, "by_level_share_of_ge_25pp": {"ATP": 0.0043, "CHALLENGER": 0.1167, "DOUBLES": 0.0767, "ITF_MEN": 0.3454, "ITF_WOMEN": 0.3975, "OTHER": 0.0052, "WTA": 0.0271, "WTA125": 0.0271}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.68, "share_primary_cause_market_settled_or_in_play": 0.5594, "share_primary_cause_stale_quote_only": 0.2321}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2322, "identity_ambiguous_share": 0.1593, "ticker_orientation": {"VERIFIED": 2322}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1033, "with_external": 11, "coverage": 0.0106, "external_status": {"EXTERNAL_STALE": 10, "AGREES_WITH_KALSHI": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 10, "MODEL_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.0909, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 419, "with_external": 11, "coverage": 0.0263, "external_status": {"EXTERNAL_STALE": 10, "AGREES_WITH_KALSHI": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 10, "MODEL_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.0909, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 750.0, "median_sample_ratio": 2.43, "median_min_matches": 23.0, "median_max_days_since_last": 177.0, "share_severe_asymmetry": 0.1744, "data_status": {"POOR": 1117, "LIMITED": 810, "ADEQUATE": 395}, "comparison_lt_10pp": {"median_thinner_serve_points": 1940.0, "median_sample_ratio": 1.71, "median_min_matches": 77.5}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 170, "model_minus_observed": 0.1168, "kalshi_minus_observed": -0.0133, "brier_diff_model_minus_kalshi": 0.0177}, "4-10x": {"n": 122, "model_minus_observed": 0.1007, "kalshi_minus_observed": -0.0309, "brier_diff_model_minus_kalshi": 0.0137}, "<2x": {"n": 330, "model_minus_observed": 0.0619, "kalshi_minus_observed": -0.0579, "brier_diff_model_minus_kalshi": 0.0061}, ">=10x": {"n": 120, "model_minus_observed": 0.0946, "kalshi_minus_observed": -0.0643, "brier_diff_model_minus_kalshi": 0.0198}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 742, "model": {"intercept": -0.652, "slope": 0.966, "slope_se": 0.093}, "kalshi_mid_same_rows": {"intercept": 0.2, "slope": 1.153, "slope_se": 0.1}, "mean_extremity_model": 0.1889, "mean_extremity_kalshi": 0.1888, "model_brier": 0.2215, "kalshi_brier": 0.1921, "brier_diff_model_minus_kalshi": 0.0294, "brier_diff_se": 0.0069, "model_logloss": 0.6336, "kalshi_logloss": 0.5621}, "fair_v1": {"n": 742, "model": {"intercept": -0.445, "slope": 1.175, "slope_se": 0.107}, "kalshi_mid_same_rows": {"intercept": 0.317, "slope": 1.224, "slope_se": 0.104}, "mean_extremity_model": 0.1717, "mean_extremity_kalshi": 0.1897, "model_brier": 0.2035, "kalshi_brier": 0.1913, "brier_diff_model_minus_kalshi": 0.0122, "brier_diff_se": 0.0053, "model_logloss": 0.5898, "kalshi_logloss": 0.5601}, "gen1_elo": {"n": 742, "model": {"intercept": -0.409, "slope": 1.134, "slope_se": 0.104}, "kalshi_mid_same_rows": {"intercept": 0.34, "slope": 1.215, "slope_se": 0.102}, "mean_extremity_model": 0.1773, "mean_extremity_kalshi": 0.1902, "model_brier": 0.2034, "kalshi_brier": 0.1914, "brier_diff_model_minus_kalshi": 0.012, "brier_diff_se": 0.0054, "model_logloss": 0.5916, "kalshi_logloss": 0.5602}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2522, "share_ge_15": 0.4409, "median_abs_gap": 12.92, "n": 4096}, "gen1_elo": {"share_ge_25": 0.2449, "share_ge_15": 0.4304, "median_abs_gap": 12.45, "n": 4096}, "gen1_sr": {"share_ge_25": 0.3098, "share_ge_15": 0.5283, "median_abs_gap": 16.1, "n": 4096}, "gen2": {"share_ge_25": 0.3074, "share_ge_15": 0.5051, "median_abs_gap": 15.29, "n": 4096}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1386, "share_ge_15": 0.3318, "median_abs_gap": 9.98, "n": 3023}, "gen1_elo": {"share_ge_25": 0.1376, "share_ge_15": 0.3169, "median_abs_gap": 9.53, "n": 3023}, "gen1_sr": {"share_ge_25": 0.2005, "share_ge_15": 0.4376, "median_abs_gap": 13.03, "n": 3023}, "gen2": {"share_ge_25": 0.2114, "share_ge_15": 0.4267, "median_abs_gap": 12.98, "n": 3023}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.01, "share_ge_25_all": 0.0365, "share_ge_25_pregame_clean": 0.0383}, "WTA": {"median_abs_gap_pregame_clean": 8.48, "share_ge_25_all": 0.0879, "share_ge_25_pregame_clean": 0.074}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2255, "share_within_10pp_all": 0.4206, "share_within_10pp_pregame_clean": 0.4996, "corr_model_vs_mid_pregame_clean": 0.8343}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 125, "model_brier": 0.1805, "kalshi_brier": 0.1812, "brier_diff_model_minus_kalshi": -0.0007}, "10-15": {"n_settled": 123, "model_brier": 0.2133, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0062}, "15-25": {"n_settled": 159, "model_brier": 0.212, "kalshi_brier": 0.2107, "brier_diff_model_minus_kalshi": 0.0013}, "25-40": {"n_settled": 77, "model_brier": 0.2348, "kalshi_brier": 0.1757, "brier_diff_model_minus_kalshi": 0.0591}, "3-5": {"n_settled": 78, "model_brier": 0.1675, "kalshi_brier": 0.1641, "brier_diff_model_minus_kalshi": 0.0034}, "40+": {"n_settled": 20, "model_brier": 0.3007, "kalshi_brier": 0.1249, "brier_diff_model_minus_kalshi": 0.1758}, "5-10": {"n_settled": 160, "model_brier": 0.1956, "kalshi_brier": 0.1966, "brier_diff_model_minus_kalshi": -0.0009}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 149, "model_brier": 0.324, "kalshi_brier": 0.2247, "brier_diff_model_minus_kalshi": 0.0993, "brier_diff_se": 0.0269, "corr_model_outcome": -0.0842, "corr_kalshi_outcome": 0.353}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
