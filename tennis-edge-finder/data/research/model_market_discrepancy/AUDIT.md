# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-05T18:57Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 14,961): 0-3 12.9%, 3-5 9.1%, 5-10 18.9%, 10-15 15.1%, 15-25 19.2%, 25-40 15.2%, 40+ 9.6%; median gap 12.82 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.9%, Challenger 14.8%, doubles 5.1%). Main tour: ATP 3.5% and WTA 9.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 3,716): MARKET_ALREADY_SETTLED_WHEN_PRICED 44.5%, STALE_QUOTE 23.1%, BOOK_QUALITY 11.2%, POOR_DATA 6.0%, POSSIBLY_IN_PLAY_QUOTE 4.8%, IN_PLAY_QUOTE 3.1%, LIMITED_DATA 2.6%, IDENTITY_AMBIGUOUS 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.1%. By class: coverage 44.5%, market_freshness 23.1%, execution 11.2%, data 8.6%, market_freshness/coverage 7.9%, mapping 2.6%, model_calibration_or_unknown 2.0%, model_calibration 0.1%.
* **Stale / settled / in-play**: 67.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 52.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 3,716 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 13.8% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 645.5 points vs 1873.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.127, Gen-2 0.921, Gen-1 ledger 0.908 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 129 model 0.2274 vs Kalshi 0.1824; n 30 model 0.3354 vs Kalshi 0.1357.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 52,108 model-market comparisons (89,321 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 21,328 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-05T18:50:35.000398+00:00'], shadow board 15,030 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-05T18:50:39.147785+00:00'], Model 4 4,595 rows, 8,700 settled tickers, 1,950 tickers with an external scan.
* By model: {"gen1_ledger": 12951, "gen1_elo": 7552, "fair_v1": 7552, "gen2": 7552, "gen1_sr": 7552, "model4_fundamental": 4479, "model4_conditioned": 4470}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 14,961 | 12.9 | 9.1 | 18.9 | 15.1 | 19.2 | 15.2 | 9.6 | 12.82 | 44.0% | 24.8% |
| MW fair_v1 | 7,552 | 12.7 | 8.7 | 17.6 | 15.3 | 18.3 | 16.0 | 11.4 | 13.38 | 45.7% | 27.4% |
| MW gen1_elo | 7,552 | 12.6 | 8.5 | 19.5 | 14.3 | 18.7 | 15.7 | 10.7 | 13.01 | 45.1% | 26.4% |
| MW gen1_ledger | 7,409 | 13.3 | 9.4 | 20.1 | 14.8 | 20.2 | 14.4 | 7.8 | 12.14 | 42.4% | 22.2% |
| MW gen1_sr | 7,552 | 9.5 | 7.4 | 15.8 | 13.7 | 21.5 | 19.1 | 13.0 | 16.51 | 53.6% | 32.1% |
| MW gen2 | 7,552 | 10.9 | 6.8 | 16.1 | 13.8 | 20.1 | 17.7 | 14.6 | 16.08 | 52.5% | 32.4% |
| all families model4_conditioned | 4,470 | 20.8 | 18.5 | 31.0 | 18.7 | 8.1 | 1.6 | 1.3 | 6.42 | 11.1% | 2.9% |
| all families model4_fundamental | 4,479 | 15.7 | 12.1 | 31.1 | 20.5 | 13.4 | 5.2 | 2.1 | 8.31 | 20.6% | 7.3% |

Configurable thresholds (primary): >=5pp 78.0%, >=10pp 59.1%, >=15pp 44.0%, >=20pp 33.7%, >=25pp 24.8%, >=30pp 18.4%, >=40pp 9.6%, >=50pp 4.2%
Executable gap (model outside the book, before fees): median 9.53pp; >=10pp 48.6%, >=25pp 20.8%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 458 | 21.8 | 19.0 | 24.4 | 15.3 | 14.4 | 2.6 | 2.4 | 6.19 | 19.4% | 5.0% |
| CHALLENGER | 1,578 | 14.5 | 10.3 | 16.5 | 15.5 | 14.8 | 14.3 | 14.3 | 13.0 | 43.3% | 28.5% |
| ITF_MEN | 2,106 | 11.3 | 8.3 | 18.5 | 14.5 | 17.9 | 16.3 | 13.2 | 13.74 | 47.4% | 29.5% |
| ITF_WOMEN | 2,799 | 9.3 | 6.3 | 15.2 | 15.5 | 21.3 | 20.8 | 11.7 | 16.64 | 53.7% | 32.5% |
| WTA | 459 | 22.7 | 10.2 | 25.1 | 13.7 | 18.7 | 7.2 | 2.4 | 8.36 | 28.3% | 9.6% |
| WTA125 | 152 | 14.5 | 7.9 | 19.7 | 27.6 | 14.5 | 10.5 | 5.3 | 11.11 | 30.3% | 15.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 458 | 19.2 | 15.1 | 26.2 | 15.5 | 16.6 | 4.6 | 2.8 | 7.5 | 24.0% | 7.4% |
| CHALLENGER | 1,578 | 13.4 | 6.2 | 17.7 | 13.9 | 18.7 | 16.4 | 13.8 | 14.66 | 48.9% | 30.2% |
| ITF_MEN | 2,106 | 8.9 | 6.7 | 16.8 | 15.4 | 19.4 | 17.9 | 15.0 | 15.68 | 52.2% | 32.8% |
| ITF_WOMEN | 2,799 | 8.2 | 6.2 | 12.8 | 11.6 | 21.6 | 20.7 | 18.9 | 19.93 | 61.2% | 39.6% |
| WTA | 459 | 20.3 | 5.5 | 16.6 | 15.7 | 22.0 | 17.6 | 2.4 | 13.18 | 42.0% | 20.0% |
| WTA125 | 152 | 6.6 | 3.3 | 17.8 | 20.4 | 24.3 | 15.8 | 11.8 | 15.82 | 52.0% | 27.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 458 | 25.8 | 12.2 | 29.5 | 14.4 | 8.9 | 6.5 | 2.6 | 7.4 | 18.1% | 9.2% |
| CHALLENGER | 1,578 | 15.5 | 9.6 | 21.2 | 12.7 | 13.3 | 13.3 | 14.3 | 11.33 | 40.9% | 27.6% |
| ITF_MEN | 2,106 | 9.6 | 9.1 | 17.8 | 14.7 | 19.4 | 16.3 | 13.1 | 14.19 | 48.8% | 29.4% |
| ITF_WOMEN | 2,799 | 9.2 | 6.2 | 15.9 | 14.2 | 23.9 | 20.5 | 10.2 | 17.26 | 54.6% | 30.7% |
| WTA | 459 | 22.2 | 14.2 | 31.4 | 15.7 | 10.9 | 4.1 | 1.5 | 7.0 | 16.6% | 5.7% |
| WTA125 | 152 | 20.4 | 4.6 | 25.0 | 21.7 | 21.1 | 5.9 | 1.3 | 10.02 | 28.3% | 7.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 205 | 26.8 | 21.0 | 37.6 | 12.2 | 2.4 | 0.0 | 0.0 | 5.42 | 2.4% | 0.0% |
| CHALLENGER | 1,049 | 20.5 | 14.8 | 26.2 | 15.2 | 13.8 | 6.9 | 2.7 | 7.41 | 23.4% | 9.5% |
| DOUBLES | 414 | 5.3 | 3.6 | 11.3 | 11.1 | 22.7 | 20.5 | 25.4 | 23.58 | 68.6% | 45.9% |
| ITF_MEN | 2,359 | 13.7 | 8.7 | 18.7 | 14.5 | 20.8 | 14.3 | 9.4 | 12.72 | 44.5% | 23.7% |
| ITF_WOMEN | 2,484 | 8.9 | 7.9 | 16.9 | 14.3 | 23.9 | 20.0 | 8.0 | 15.82 | 51.9% | 28.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 387 | 17.6 | 8.8 | 26.1 | 20.9 | 17.6 | 8.3 | 0.8 | 9.5 | 26.6% | 9.0% |
| WTA125 | 362 | 14.1 | 9.4 | 21.6 | 18.5 | 21.6 | 11.3 | 3.6 | 10.91 | 36.5% | 14.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 457 | 21.7 | 19.0 | 24.5 | 15.3 | 14.4 | 2.6 | 2.4 | 6.21 | 19.5% | 5.0% |
| CHALLENGER | 1,097 | 19.1 | 12.9 | 21.0 | 18.4 | 16.4 | 8.2 | 4.0 | 9.19 | 28.6% | 12.2% |
| ITF_MEN | 1,417 | 14.4 | 11.2 | 22.5 | 16.0 | 18.3 | 12.1 | 5.6 | 10.41 | 35.9% | 17.6% |
| ITF_WOMEN | 1,946 | 12.0 | 8.1 | 18.1 | 17.7 | 22.9 | 16.8 | 4.5 | 13.37 | 44.1% | 21.3% |
| WTA | 458 | 22.7 | 10.3 | 25.1 | 13.8 | 18.8 | 7.0 | 2.4 | 8.32 | 28.2% | 9.4% |
| WTA125 | 146 | 15.1 | 8.2 | 20.6 | 28.8 | 14.4 | 9.6 | 3.4 | 10.84 | 27.4% | 13.0% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 457 | 19.3 | 14.9 | 26.3 | 15.5 | 16.6 | 4.6 | 2.8 | 7.5 | 24.1% | 7.4% |
| CHALLENGER | 1,097 | 17.3 | 7.9 | 22.4 | 17.5 | 19.8 | 11.6 | 3.5 | 10.51 | 34.8% | 15.0% |
| ITF_MEN | 1,417 | 11.5 | 8.3 | 20.2 | 17.9 | 20.5 | 14.2 | 7.5 | 12.54 | 42.2% | 21.7% |
| ITF_WOMEN | 1,946 | 10.1 | 7.6 | 14.4 | 11.7 | 24.5 | 19.1 | 12.6 | 17.16 | 56.2% | 31.8% |
| WTA | 458 | 20.3 | 5.5 | 16.6 | 15.7 | 22.1 | 17.5 | 2.4 | 13.18 | 41.9% | 19.9% |
| WTA125 | 146 | 6.8 | 3.4 | 17.8 | 21.2 | 25.3 | 16.4 | 8.9 | 15.34 | 50.7% | 25.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 195 | 27.2 | 22.1 | 38.0 | 12.3 | 0.5 | 0.0 | 0.0 | 5.34 | 0.5% | 0.0% |
| CHALLENGER | 857 | 22.5 | 17.4 | 29.2 | 14.8 | 13.3 | 2.7 | 0.1 | 6.68 | 16.1% | 2.8% |
| DOUBLES | 375 | 5.3 | 3.5 | 11.7 | 11.2 | 22.7 | 20.8 | 24.8 | 23.56 | 68.3% | 45.6% |
| ITF_MEN | 1,745 | 16.3 | 10.1 | 21.4 | 15.8 | 20.8 | 11.2 | 4.4 | 10.68 | 36.4% | 15.6% |
| ITF_WOMEN | 1,811 | 10.3 | 9.2 | 19.6 | 15.9 | 24.7 | 17.7 | 2.5 | 13.17 | 45.0% | 20.3% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 358 | 17.9 | 9.2 | 26.8 | 21.5 | 18.2 | 6.4 | 0.0 | 9.24 | 24.6% | 6.4% |
| WTA125 | 283 | 16.6 | 10.2 | 25.4 | 21.9 | 19.8 | 5.7 | 0.3 | 9.33 | 25.8% | 6.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 414 | 5.3 | 3.6 | 11.3 | 11.1 | 22.7 | 20.5 | 25.4 | 23.58 | 68.6% | 45.9% |
| singles | 6,995 | 13.7 | 9.8 | 20.7 | 15.0 | 20.0 | 14.1 | 6.7 | 11.76 | 40.8% | 20.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,707 | 13.8 | 9.0 | 17.1 | 15.5 | 16.7 | 14.7 | 13.3 | 13.06 | 44.7% | 28.0% |
| Hard | 5,216 | 12.4 | 8.9 | 18.2 | 15.1 | 18.9 | 15.9 | 10.5 | 13.32 | 45.3% | 26.4% |
| UNKNOWN | 629 | 11.4 | 6.0 | 14.3 | 17.0 | 17.0 | 20.8 | 13.3 | 15.41 | 51.2% | 34.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,256 | 16.7 | 10.9 | 19.3 | 15.7 | 16.1 | 11.3 | 10.0 | 10.83 | 37.4% | 21.2% |
| B | 1,045 | 15.6 | 10.6 | 18.4 | 17.7 | 16.4 | 10.3 | 11.0 | 11.12 | 37.7% | 21.3% |
| C | 1,121 | 12.8 | 9.8 | 20.4 | 13.8 | 16.4 | 16.0 | 10.8 | 12.69 | 43.2% | 26.8% |
| D | 1,347 | 10.8 | 7.9 | 16.5 | 15.0 | 22.2 | 16.0 | 11.7 | 14.97 | 49.9% | 27.7% |
| F | 1,783 | 7.1 | 4.8 | 14.1 | 14.7 | 20.2 | 25.4 | 13.6 | 19.48 | 59.3% | 39.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,213 | 19.4 | 12.7 | 26.5 | 16.6 | 15.3 | 6.7 | 2.9 | 8.08 | 24.8% | 9.5% |
| B | 1,135 | 13.5 | 9.2 | 21.9 | 15.9 | 20.1 | 12.2 | 7.2 | 11.64 | 39.5% | 19.4% |
| C | 1,441 | 11.2 | 8.3 | 16.0 | 14.3 | 23.0 | 15.5 | 11.8 | 15.16 | 50.2% | 27.3% |
| D | 1,151 | 10.9 | 8.0 | 21.0 | 12.4 | 23.6 | 16.4 | 7.6 | 14.02 | 47.6% | 24.0% |
| F | 1,469 | 7.7 | 6.9 | 12.7 | 13.5 | 22.1 | 25.3 | 11.8 | 18.82 | 59.2% | 37.1% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 2,743 | 16.2 | 10.1 | 18.6 | 16.3 | 16.3 | 11.4 | 11.1 | 11.32 | 38.8% | 22.5% |
| LIMITED | 1,657 | 14.1 | 11.5 | 20.8 | 14.8 | 15.8 | 13.6 | 9.3 | 11.27 | 38.8% | 23.0% |
| POOR | 3,152 | 8.8 | 6.1 | 15.1 | 14.8 | 21.3 | 21.3 | 12.8 | 17.45 | 55.3% | 34.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 861 | 31.6 | 26.1 | 35.5 | 4.8 | 1.6 | 0.3 | 0.0 | 4.35 | 2.0% | 0.4% |
| GAME_SPREAD | 774 | 22.4 | 16.0 | 36.3 | 17.8 | 6.5 | 0.7 | 0.4 | 6.14 | 7.5% | 1.0% |
| MATCH_WINNER | 7,409 | 13.3 | 9.4 | 20.1 | 14.8 | 20.2 | 14.4 | 7.8 | 12.14 | 42.4% | 22.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 2,318 | 26.5 | 15.8 | 31.0 | 14.2 | 10.0 | 2.0 | 0.5 | 5.97 | 12.5% | 2.5% |
| TOTAL_GAMES | 1,565 | 8.8 | 9.5 | 31.9 | 25.8 | 14.6 | 5.8 | 3.6 | 9.93 | 24.0% | 9.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,620 | 27.4 | 35.4 | 24.3 | 0.4 | 11.1 | 1.1 | 0.4 | 4.29 | 12.5% | 1.4% |
| GAME_SPREAD | 993 | 40.9 | 14.5 | 27.9 | 13.5 | 1.6 | 1.2 | 0.4 | 4.07 | 3.2% | 1.6% |
| TOTAL_GAMES | 1,857 | 4.3 | 5.8 | 38.4 | 37.5 | 9.0 | 2.3 | 2.7 | 10.2 | 14.0% | 5.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,620 | 25.4 | 16.7 | 32.4 | 9.4 | 9.9 | 5.3 | 0.9 | 5.87 | 16.2% | 6.2% |
| GAME_SPREAD | 993 | 18.0 | 11.4 | 27.1 | 23.1 | 14.1 | 4.8 | 1.5 | 9.07 | 20.4% | 6.3% |
| TOTAL_GAMES | 1,866 | 6.0 | 8.4 | 32.2 | 28.8 | 16.0 | 5.3 | 3.4 | 10.5 | 24.6% | 8.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7,552 | 45.7% | 27.4% | 13.38 | 35.1% | 16.0% | 10.58 |
| gen1_elo | 7,552 | 45.1% | 26.4% | 13.01 | 34.1% | 15.6% | 10.03 |
| gen1_sr | 7,552 | 53.6% | 32.1% | 16.51 | 44.0% | 20.6% | 13.22 |
| gen2 | 7,552 | 52.5% | 32.4% | 16.08 | 44.4% | 22.7% | 13.04 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 2,884 | 15.9 | 12.4 | 21.5 | 15.8 | 18.7 | 11.7 | 4.0 | 10.02 | 34.4% | 15.6% |
| STALE | 4,668 | 10.6 | 6.5 | 15.2 | 15.0 | 18.0 | 18.7 | 16.0 | 16.51 | 52.7% | 34.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 877 | 14.4 | 8.7 | 23.3 | 14.9 | 17.9 | 16.8 | 4.1 | 11.08 | 38.8% | 20.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 14,961 | 877 | 6356 | 7728 | 30.7 | 227.5 | 1400.4 |
| ge_15pp | 6,589 | 340 | 2280 | 3969 | 37.6 | 466.9 | 1380.4 |
| ge_25pp | 3,716 | 183 | 1042 | 2491 | 49.5 | 574.3 | 1380.4 |
| lt_10pp | 6,119 | 406 | 3068 | 2645 | 28.3 | 59.2 | 1201.9 |

Current slate `SL-20261005T185713Z-784f2692`: 962 priced rows, quote age at build {'median': 7.3, 'max': 7.3}, freshness {'FRESH': 962}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 197 | 20.8 | 13.2 | 21.8 | 20.8 | 17.3 | 5.6 | 0.5 | 7.39 | 23.4% | 6.1% |
| MARKETS_AGREE | 15 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.09 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 34 | 0.0 | 14.7 | 38.2 | 23.5 | 17.6 | 5.9 | 0.0 | 9.16 | 23.5% | 5.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 7,552 | 247 (3.3%) | 13.8% | 0.0% | {"EXTERNAL_STALE": 197, "AGREES_WITH_KALSHI": 34, "ALL_AGREE": 15, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 3,450 | 54 (1.6%) | 14.8% | 0.0% | {"EXTERNAL_STALE": 46, "AGREES_WITH_KALSHI": 8} |
| fair_v1_ge_25pp | 2,071 | 14 (0.7%) | 14.3% | 0.0% | {"EXTERNAL_STALE": 12, "AGREES_WITH_KALSHI": 2} |
| fair_v1_ge_25pp_pregame_clean | 883 | 13 (1.5%) | 15.4% | 0.0% | {"EXTERNAL_STALE": 11, "AGREES_WITH_KALSHI": 2} |
| fair_v1_lt_10pp | 2,944 | 144 (4.9%) | 12.5% | 0.0% | {"EXTERNAL_STALE": 110, "AGREES_WITH_KALSHI": 18, "ALL_AGREE": 15, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,514 | 11.6 | 8.0 | 19.8 | 15.7 | 20.1 | 15.0 | 9.9 | 13.14 | 45.0% | 24.9% |
| 4-10x | 1,051 | 12.0 | 10.7 | 17.1 | 14.5 | 17.4 | 18.3 | 10.1 | 13.57 | 45.8% | 28.3% |
| <2x | 4,048 | 13.9 | 9.4 | 17.8 | 15.5 | 17.6 | 14.1 | 11.6 | 12.8 | 43.3% | 25.7% |
| >=10x | 939 | 9.6 | 4.8 | 13.9 | 14.8 | 19.2 | 23.4 | 14.3 | 18.31 | 56.9% | 37.7% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,979 | 13.4 | 8.8 | 19.6 | 16.0 | 16.6 | 12.7 | 12.8 | 12.38 | 42.1% | 25.5% |
| 300-1000 | 1,755 | 12.5 | 8.8 | 16.6 | 15.3 | 20.6 | 16.1 | 10.1 | 13.94 | 46.8% | 26.2% |
| <300 | 2,064 | 8.0 | 5.6 | 14.2 | 14.3 | 20.4 | 23.7 | 13.8 | 18.87 | 58.0% | 37.5% |
| >=3000 | 1,754 | 17.5 | 12.1 | 20.4 | 15.8 | 15.2 | 10.6 | 8.3 | 9.99 | 34.2% | 18.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 248 | 0.519 | 0.3885 | 0.4274 | +0.092 | -0.039 | 0.0087 ± 0.0089 |
| ratio 4-10x | 170 | 0.578 | 0.4401 | 0.4882 | +0.090 | -0.048 | 0.0132 ± 0.0114 |
| ratio <2x | 501 | 0.5358 | 0.4113 | 0.4671 | +0.069 | -0.056 | 0.0119 ± 0.0063 |
| ratio >=10x | 173 | 0.5523 | 0.3799 | 0.4624 | +0.090 | -0.083 | 0.0126 ± 0.0143 |
| thinner_sample 1000-3000 | 292 | 0.541 | 0.421 | 0.4521 | +0.089 | -0.031 | 0.0096 ± 0.0081 |
| thinner_sample 300-1000 | 296 | 0.5565 | 0.4253 | 0.4764 | +0.080 | -0.051 | 0.0059 ± 0.0084 |
| thinner_sample <300 | 359 | 0.5379 | 0.3716 | 0.4568 | +0.081 | -0.085 | 0.0162 ± 0.0093 |
| thinner_sample >=3000 | 145 | 0.5182 | 0.4189 | 0.4552 | +0.063 | -0.036 | 0.0151 ± 0.0094 |
| data_status ADEQUATE | 319 | 0.5292 | 0.4201 | 0.4514 | +0.078 | -0.031 | 0.0086 ± 0.007 |
| data_status LIMITED | 224 | 0.5551 | 0.4287 | 0.4911 | +0.064 | -0.062 | 0.0041 ± 0.0098 |
| data_status POOR | 549 | 0.5425 | 0.3878 | 0.4536 | +0.089 | -0.066 | 0.0162 ± 0.007 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 171 | 0.1812 | 0.1823 | -0.0011 ± 0.0011 | 0.5371 | 0.5401 | 0.4967 | 0.4824 | 0.5029 | -0.081 ± 0.0348 | -0.01 (3) |
| 3-5 | 109 | 0.1749 | 0.1756 | -0.0007 ± 0.0033 | 0.5287 | 0.5267 | 0.5175 | 0.4768 | 0.5046 | -0.068 ± 0.0418 | 0.02 (1) |
| 5-10 | 220 | 0.1957 | 0.2003 | -0.0046 ± 0.0045 | 0.5764 | 0.5859 | 0.514 | 0.4399 | 0.5 | -0.049 ± 0.0304 | -0.0167 (3) |
| 10-15 | 189 | 0.2141 | 0.2106 | +0.0035 ± 0.0083 | 0.6135 | 0.6029 | 0.5167 | 0.3931 | 0.4392 | -0.066 ± 0.0333 | -0.0633 (3) |
| 15-25 | 244 | 0.2159 | 0.2102 | +0.0057 ± 0.0115 | 0.6196 | 0.6052 | 0.5604 | 0.3641 | 0.4508 | -0.033 ± 0.0288 | -0.02 (4) |
| 25-40 | 129 | 0.2274 | 0.1824 | +0.0450 ± 0.023 | 0.6436 | 0.5355 | 0.6266 | 0.3143 | 0.3953 | -0.074 ± 0.0347 | -0.01 (1) |
| 40+ | 30 | 0.3354 | 0.1357 | +0.1998 ± 0.0606 | 0.9067 | 0.4279 | 0.7106 | 0.2678 | 0.2667 | -0.167 ± 0.0655 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 564 | 0.165 | 0.1661 | -0.0011 ± 0.0006 | 0.4975 | 0.4999 | 0.5015 | 0.4867 | 0.5319 | -0.016 ± 0.0177 | -0.0188 (8) |
| 3-5 | 363 | 0.1682 | 0.1676 | +0.0007 ± 0.0018 | 0.5108 | 0.504 | 0.4742 | 0.4342 | 0.449 | -0.043 ± 0.0218 | 0.02 (1) |
| 5-10 | 816 | 0.1785 | 0.1783 | +0.0002 ± 0.0022 | 0.5366 | 0.5331 | 0.4768 | 0.403 | 0.4363 | -0.027 ± 0.0149 | -0.0129 (7) |
| 10-15 | 719 | 0.1815 | 0.1683 | +0.0131 ± 0.0038 | 0.5424 | 0.4987 | 0.4678 | 0.3441 | 0.3519 | -0.053 ± 0.0153 | -0.0633 (3) |
| 15-25 | 936 | 0.1956 | 0.1591 | +0.0366 ± 0.0052 | 0.5797 | 0.4739 | 0.4776 | 0.2792 | 0.2863 | -0.052 ± 0.0129 | -0.017 (10) |
| 25-40 | 918 | 0.211 | 0.0949 | +0.1161 ± 0.0064 | 0.614 | 0.3107 | 0.5052 | 0.1887 | 0.1656 | -0.074 ± 0.0098 | -0.01 (1) |
| 40+ | 705 | 0.3744 | 0.0306 | +0.3438 ± 0.0071 | 0.9731 | 0.1423 | 0.6157 | 0.1024 | 0.0326 | -0.098 ± 0.0059 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 112 | 0.1769 | 0.1784 | -0.0014 ± 0.0014 | 0.5269 | 0.5282 | 0.5066 | 0.4917 | 0.5268 | -0.053 ± 0.0398 | -0.01 (1) |
| 3-5 | 85 | 0.1986 | 0.1965 | +0.0020 ± 0.0039 | 0.5738 | 0.5746 | 0.4953 | 0.456 | 0.4471 | -0.092 ± 0.0515 | 0.02 (1) |
| 5-10 | 203 | 0.1854 | 0.1857 | -0.0003 ± 0.0046 | 0.5526 | 0.5519 | 0.5691 | 0.4938 | 0.5271 | -0.071 ± 0.0312 | -0.01 (4) |
| 10-15 | 179 | 0.2239 | 0.2127 | +0.0112 ± 0.0087 | 0.6369 | 0.6122 | 0.5801 | 0.4556 | 0.4804 | -0.084 ± 0.0353 | -0.0667 (3) |
| 15-25 | 277 | 0.2245 | 0.1997 | +0.0248 ± 0.0107 | 0.6359 | 0.5776 | 0.5841 | 0.3866 | 0.4296 | -0.088 ± 0.0279 | -0.0167 (3) |
| 25-40 | 163 | 0.2614 | 0.1989 | +0.0624 ± 0.0216 | 0.7262 | 0.5782 | 0.6505 | 0.3399 | 0.3926 | -0.096 ± 0.0364 | -0.025 (2) |
| 40+ | 73 | 0.381 | 0.1718 | +0.2092 ± 0.0492 | 1.0454 | 0.5148 | 0.7445 | 0.2517 | 0.3014 | -0.073 ± 0.0465 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 451 | 0.1527 | 0.1542 | -0.0015 ± 0.0006 | 0.4658 | 0.4689 | 0.5256 | 0.5109 | 0.5499 | -0.010 ± 0.0187 | -0.0217 (6) |
| 3-5 | 306 | 0.1695 | 0.1662 | +0.0033 ± 0.0019 | 0.5047 | 0.5001 | 0.524 | 0.4843 | 0.4641 | -0.073 ± 0.0239 | 0.02 (1) |
| 5-10 | 743 | 0.1691 | 0.1704 | -0.0013 ± 0.0023 | 0.5122 | 0.5115 | 0.5165 | 0.4415 | 0.4818 | -0.016 ± 0.0153 | -0.01 (5) |
| 10-15 | 645 | 0.187 | 0.1741 | +0.0128 ± 0.0041 | 0.5564 | 0.5139 | 0.5069 | 0.3831 | 0.4 | -0.046 ± 0.0166 | -0.0575 (4) |
| 15-25 | 1024 | 0.2027 | 0.1578 | +0.0449 ± 0.005 | 0.594 | 0.4726 | 0.5114 | 0.3139 | 0.3037 | -0.077 ± 0.0125 | -0.0143 (7) |
| 25-40 | 961 | 0.2286 | 0.1163 | +0.1123 ± 0.007 | 0.6594 | 0.3646 | 0.537 | 0.2203 | 0.2029 | -0.071 ± 0.0112 | -0.015 (6) |
| 40+ | 891 | 0.4123 | 0.0518 | +0.3605 ± 0.0088 | 1.076 | 0.1997 | 0.6595 | 0.1211 | 0.0673 | -0.086 ± 0.0072 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 175 | 0.1902 | 0.1921 | -0.0019 ± 0.0012 | 0.5568 | 0.5622 | 0.5212 | 0.5066 | 0.5371 | -0.055 ± 0.0328 | -0.01 (5) |
| 3-5 | 116 | 0.1681 | 0.1653 | +0.0028 ± 0.003 | 0.5078 | 0.5012 | 0.5028 | 0.4633 | 0.4483 | -0.122 ± 0.0401 | -- (0) |
| 5-10 | 220 | 0.1979 | 0.1963 | +0.0016 ± 0.0045 | 0.5847 | 0.5752 | 0.4992 | 0.4261 | 0.4455 | -0.079 ± 0.0299 | -0.01 (3) |
| 10-15 | 183 | 0.2164 | 0.2137 | +0.0027 ± 0.0086 | 0.6217 | 0.6133 | 0.5423 | 0.4188 | 0.4754 | -0.067 ± 0.0343 | -0.044 (5) |
| 15-25 | 238 | 0.2082 | 0.2019 | +0.0063 ± 0.0113 | 0.6061 | 0.5841 | 0.5712 | 0.3765 | 0.458 | -0.042 ± 0.028 | -0.03 (1) |
| 25-40 | 135 | 0.2235 | 0.1964 | +0.0272 ± 0.0231 | 0.6388 | 0.5697 | 0.6261 | 0.3145 | 0.4222 | -0.053 ± 0.0348 | 0.0 (1) |
| 40+ | 25 | 0.3648 | 0.1373 | +0.2275 ± 0.0667 | 0.9712 | 0.4311 | 0.711 | 0.2606 | 0.24 | -0.185 ± 0.0761 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 576 | 0.1714 | 0.1717 | -0.0002 ± 0.0006 | 0.5138 | 0.5144 | 0.5028 | 0.4882 | 0.4983 | -0.049 ± 0.0172 | -0.0162 (13) |
| 3-5 | 389 | 0.1665 | 0.1626 | +0.0039 ± 0.0016 | 0.5041 | 0.4939 | 0.4904 | 0.451 | 0.4267 | -0.085 ± 0.0208 | -0.01 (2) |
| 5-10 | 833 | 0.1835 | 0.1759 | +0.0076 ± 0.0022 | 0.549 | 0.5224 | 0.4631 | 0.3895 | 0.3745 | -0.071 ± 0.0146 | -0.01 (3) |
| 10-15 | 672 | 0.1872 | 0.1763 | +0.0109 ± 0.004 | 0.556 | 0.5227 | 0.4799 | 0.3563 | 0.375 | -0.044 ± 0.0162 | -0.03 (9) |
| 15-25 | 999 | 0.1835 | 0.1462 | +0.0373 ± 0.0049 | 0.5547 | 0.4426 | 0.4829 | 0.283 | 0.2903 | -0.051 ± 0.0118 | -0.03 (2) |
| 25-40 | 892 | 0.2104 | 0.0946 | +0.1158 ± 0.0066 | 0.6136 | 0.3073 | 0.5006 | 0.1805 | 0.1614 | -0.072 ± 0.0098 | 0.0 (1) |
| 40+ | 660 | 0.3924 | 0.032 | +0.3603 ± 0.0079 | 1.0222 | 0.1464 | 0.6254 | 0.1027 | 0.0303 | -0.100 ± 0.0064 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 449 | 0.2027 | 0.2026 | +0.0000 ± 0.0007 | 0.587 | 0.5874 | 0.4976 | 0.483 | 0.4855 | -0.041 ± 0.0213 | -0.0226 (46) |
| 3-5 | 333 | 0.1948 | 0.1936 | +0.0012 ± 0.0019 | 0.5711 | 0.5653 | 0.4689 | 0.4292 | 0.4384 | -0.040 ± 0.0239 | -0.0059 (32) |
| 5-10 | 684 | 0.1874 | 0.1827 | +0.0046 ± 0.0025 | 0.5581 | 0.5454 | 0.4595 | 0.3862 | 0.3918 | -0.040 ± 0.0164 | -0.005 (72) |
| 10-15 | 462 | 0.2029 | 0.191 | +0.0119 ± 0.0051 | 0.5951 | 0.5621 | 0.4584 | 0.3351 | 0.3485 | -0.036 ± 0.0202 | 0.0016 (63) |
| 15-25 | 621 | 0.2318 | 0.2089 | +0.0229 ± 0.0071 | 0.6569 | 0.6033 | 0.527 | 0.3339 | 0.372 | -0.024 ± 0.0183 | -0.0216 (58) |
| 25-40 | 310 | 0.2629 | 0.1652 | +0.0977 ± 0.0144 | 0.7287 | 0.4984 | 0.5719 | 0.2606 | 0.2581 | -0.068 ± 0.0227 | -0.0216 (25) |
| 40+ | 98 | 0.424 | 0.155 | +0.2689 ± 0.0426 | 1.187 | 0.48 | 0.7319 | 0.2239 | 0.2347 | -0.063 ± 0.0412 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 844 | 0.192 | 0.1914 | +0.0005 ± 0.0005 | 0.5618 | 0.5603 | 0.4909 | 0.4764 | 0.4668 | -0.050 ± 0.0151 | -0.0155 (82) |
| 3-5 | 610 | 0.1946 | 0.1928 | +0.0018 ± 0.0014 | 0.569 | 0.5621 | 0.4718 | 0.4319 | 0.4311 | -0.045 ± 0.0178 | -0.018 (54) |
| 5-10 | 1259 | 0.1849 | 0.1785 | +0.0064 ± 0.0018 | 0.552 | 0.5325 | 0.4433 | 0.3693 | 0.3662 | -0.044 ± 0.012 | -0.0089 (122) |
| 10-15 | 946 | 0.196 | 0.182 | +0.0140 ± 0.0035 | 0.578 | 0.5387 | 0.448 | 0.3247 | 0.3298 | -0.039 ± 0.0138 | -0.0053 (99) |
| 15-25 | 1311 | 0.2184 | 0.1847 | +0.0337 ± 0.0047 | 0.6318 | 0.5426 | 0.5016 | 0.3062 | 0.3173 | -0.039 ± 0.0119 | -0.0255 (106) |
| 25-40 | 922 | 0.2411 | 0.1242 | +0.1169 ± 0.0073 | 0.6822 | 0.3906 | 0.5265 | 0.2115 | 0.1844 | -0.074 ± 0.0114 | -0.0206 (47) |
| 40+ | 520 | 0.3873 | 0.0779 | +0.3094 ± 0.0134 | 1.056 | 0.2643 | 0.6504 | 0.1345 | 0.1038 | -0.073 ± 0.0125 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1092 | 1.127 ± 0.087 | 1.245 | 0.1699 | 0.1812 | 0.2066 | 0.1951 |
| gen2 | 1092 | 0.921 ± 0.077 | 1.164 | 0.1856 | 0.1809 | 0.2262 | 0.1948 |
| gen1_elo | 1092 | 1.119 ± 0.086 | 1.198 | 0.1749 | 0.1815 | 0.2058 | 0.1951 |
| gen1_sr | 1092 | 1.14 ± 0.1 | 1.222 | 0.1424 | 0.1828 | 0.2216 | 0.1947 |
| gen1_ledger | 2957 | 0.908 ± 0.05 | 1.073 | 0.1622 | 0.2011 | 0.2181 | 0.191 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 6,589)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,087 | 31.7% |
| STALE_QUOTE | market_freshness | 1,875 | 28.5% |
| BOOK_QUALITY | execution | 807 | 12.2% |
| POOR_DATA | data | 504 | 7.6% |
| LIMITED_DATA | data | 341 | 5.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 333 | 5.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 296 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 196 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 142 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 8 | 0.1% |

Cause class: coverage 31.7%, market_freshness 28.5%, data 12.8%, execution 12.2%, market_freshness/coverage 8.0%, model_calibration_or_unknown 4.5%, mapping 2.2%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.8%, START_UNVERIFIABLE 95.0%, LOW_DATA_QUALITY 66.1%, STALE_KALSHI_QUOTE 60.2%, THIN_PLAYER_HISTORY 55.5%, STALE_PLAYER_DATA 53.9%, MODEL_INTERNAL_DISAGREEMENT 35.9%, ASYMMETRIC_SAMPLE_SIZE 30.1%, WIDE_SPREAD 21.0%, MODEL_HIGH_UNCERTAINTY 14.4%, PLAYER_IDENTITY_RISK 11.1%, LEVEL_TRANSFER_RISK 8.2%, EVENT_MAPPING_RISK 6.8%, LOW_DISPLAYED_LIQUIDITY 6.2%, MODEL_CALIBRATION_OUTLIER 2.1%, UNKNOWN 0.7%, EXTERNAL_MARKET_REJECTION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 34.0%, POST_SETTLEMENT_OBSERVATION 31.7%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.9%

### >= ge_25 pp (N = 3,716)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,655 | 44.5% |
| STALE_QUOTE | market_freshness | 859 | 23.1% |
| BOOK_QUALITY | execution | 418 | 11.2% |
| POOR_DATA | data | 223 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 178 | 4.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 116 | 3.1% |
| LIMITED_DATA | data | 96 | 2.6% |
| IDENTITY_AMBIGUOUS | mapping | 96 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 73 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 2 | 0.1% |

Cause class: coverage 44.5%, market_freshness 23.1%, execution 11.2%, data 8.6%, market_freshness/coverage 7.9%, mapping 2.6%, model_calibration_or_unknown 2.0%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.3%, LOW_DATA_QUALITY 69.5%, STALE_KALSHI_QUOTE 67.0%, THIN_PLAYER_HISTORY 58.0%, STALE_PLAYER_DATA 51.2%, MODEL_INTERNAL_DISAGREEMENT 37.8%, ASYMMETRIC_SAMPLE_SIZE 32.9%, WIDE_SPREAD 19.6%, MODEL_HIGH_UNCERTAINTY 15.4%, PLAYER_IDENTITY_RISK 13.9%, LEVEL_TRANSFER_RISK 8.0%, EVENT_MAPPING_RISK 7.7%, LOW_DISPLAYED_LIQUIDITY 6.6%, MODEL_CALIBRATION_OUTLIER 3.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 46.9%, POST_SETTLEMENT_OBSERVATION 44.5%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 1.0%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 3103, "IDENTITY_AMBIGUOUS": 613}; ticker orientation: {"VERIFIED": 3716}.

Checks: discipline:AMBIGUOUS 190, discipline:PASS 3526, identity_confidence:AMBIGUOUS 516, identity_confidence:PASS 3200, level_mapping:NA 202, level_mapping:PASS 3514, market_pair:AMBIGUOUS 127, market_pair:NA 93, market_pair:PASS 3496, model_complement:NA 62, model_complement:PASS 3654, namesake:PASS 3716, physical_match_id:NA 1645, physical_match_id:PASS 2071, player_ids:PASS 3716, same_pair_other_event:PASS 3716, ticker_orientation:PASS 3716

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 663 | 3.5% | 3.5% | 0.6% | {"market_freshness": 20, "execution": 3} | 6.01 | 0.1791 / 0.1823 (49) | 32.6% | 0.3% | 4.2% | 1.7% |
| CHALLENGER | 2,627 | 20.9% | 8.1% | 14.8% | {"coverage": 327, "market_freshness": 106, "market_freshness/coverage": 65, "data": 24, "model_calibration_or_unknown": 22, "execution": 5, "model_calibration": 1} | 7.61 | 0.2204 / 0.2044 (692) | 56.4% | 5.9% | 1.3% | 25.6% |
| DOUBLES | 414 | 45.9% | 45.6% | 5.1% | {"market_freshness": 106, "execution": 33, "mapping": 32, "market_freshness/coverage": 12, "coverage": 7} | 23.56 | 0.3208 / 0.2301 (163) | 56.5% | 0.0% | 100.0% | 9.4% |
| ITF_MEN | 4,465 | 26.4% | 16.5% | 31.8% | {"coverage": 578, "market_freshness": 220, "execution": 189, "data": 100, "market_freshness/coverage": 80, "mapping": 12, "model_calibration_or_unknown": 1} | 10.54 | 0.2148 / 0.1879 (1386) | 52.4% | 53.2% | 7.2% | 29.2% |
| ITF_WOMEN | 5,283 | 30.4% | 20.8% | 43.2% | {"coverage": 726, "market_freshness": 358, "execution": 178, "data": 175, "market_freshness/coverage": 97, "mapping": 49, "model_calibration_or_unknown": 21} | 13.3 | 0.2027 / 0.185 (1367) | 55.2% | 60.9% | 10.5% | 28.9% |
| OTHER | 149 | 8.1% | 7.3% | 0.3% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 846 | 9.3% | 8.1% | 2.1% | {"market_freshness": 34, "model_calibration_or_unknown": 15, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "model_calibration": 1, "mapping": 1} | 8.47 | 0.2006 / 0.1964 (129) | 38.3% | 2.5% | 1.4% | 3.5% |
| WTA125 | 514 | 15.2% | 8.4% | 2.1% | {"market_freshness/coverage": 30, "market_freshness": 13, "model_calibration_or_unknown": 12, "coverage": 12, "data": 9, "mapping": 1, "execution": 1} | 10.01 | 0.2273 / 0.204 (221) | 34.4% | 7.4% | 3.3% | 16.5% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 5 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 6 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 9 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 11 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 12 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 14 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 15 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 16 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 17 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 18 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 19 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 20 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 21 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 23 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 24 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 25 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 26 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 27 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 28 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 256 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 29 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 30 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 31 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 32 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 33 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 36 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 37 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 39 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 40 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 41 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 192 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.76); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 44 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 46 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 86 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 47 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 48 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 49 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 50 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9724, "by_level_share_of_ge_25pp": {"ATP": 0.0062, "CHALLENGER": 0.148, "DOUBLES": 0.0511, "ITF_MEN": 0.3175, "ITF_WOMEN": 0.4316, "OTHER": 0.0032, "WTA": 0.0213, "WTA125": 0.021}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6703, "share_primary_cause_market_settled_or_in_play": 0.5245, "share_primary_cause_stale_quote_only": 0.2312}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 3716, "identity_ambiguous_share": 0.165, "ticker_orientation": {"VERIFIED": 3716}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 2071, "with_external": 14, "coverage": 0.0068, "external_status": {"EXTERNAL_STALE": 12, "AGREES_WITH_KALSHI": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 12, "MODEL_LONE_OUTLIER": 2}, "share_external_agrees_with_kalshi": 0.1429, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 883, "with_external": 13, "coverage": 0.0147, "external_status": {"EXTERNAL_STALE": 11, "AGREES_WITH_KALSHI": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 11, "MODEL_LONE_OUTLIER": 2}, "share_external_agrees_with_kalshi": 0.1538, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 645.5, "median_sample_ratio": 2.31, "median_min_matches": 22.0, "median_max_days_since_last": 190.0, "share_severe_asymmetry": 0.1825, "data_status": {"POOR": 1905, "LIMITED": 1069, "ADEQUATE": 742}, "comparison_lt_10pp": {"median_thinner_serve_points": 1873.0, "median_sample_ratio": 1.74, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 248, "model_minus_observed": 0.0916, "kalshi_minus_observed": -0.0389, "brier_diff_model_minus_kalshi": 0.0087}, "4-10x": {"n": 170, "model_minus_observed": 0.0898, "kalshi_minus_observed": -0.0482, "brier_diff_model_minus_kalshi": 0.0132}, "<2x": {"n": 501, "model_minus_observed": 0.0688, "kalshi_minus_observed": -0.0557, "brier_diff_model_minus_kalshi": 0.0119}, ">=10x": {"n": 173, "model_minus_observed": 0.0899, "kalshi_minus_observed": -0.0826, "brier_diff_model_minus_kalshi": 0.0126}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1092, "model": {"intercept": -0.618, "slope": 0.921, "slope_se": 0.077}, "kalshi_mid_same_rows": {"intercept": 0.225, "slope": 1.164, "slope_se": 0.085}, "mean_extremity_model": 0.1856, "mean_extremity_kalshi": 0.1809, "model_brier": 0.2262, "kalshi_brier": 0.1948, "brier_diff_model_minus_kalshi": 0.0314, "brier_diff_se": 0.0058, "model_logloss": 0.6454, "kalshi_logloss": 0.5691}, "fair_v1": {"n": 1092, "model": {"intercept": -0.404, "slope": 1.127, "slope_se": 0.087}, "kalshi_mid_same_rows": {"intercept": 0.379, "slope": 1.245, "slope_se": 0.089}, "mean_extremity_model": 0.1699, "mean_extremity_kalshi": 0.1812, "model_brier": 0.2066, "kalshi_brier": 0.1951, "brier_diff_model_minus_kalshi": 0.0115, "brier_diff_se": 0.0046, "model_logloss": 0.5986, "kalshi_logloss": 0.5698}, "gen1_elo": {"n": 1092, "model": {"intercept": -0.44, "slope": 1.119, "slope_se": 0.086}, "kalshi_mid_same_rows": {"intercept": 0.311, "slope": 1.198, "slope_se": 0.086}, "mean_extremity_model": 0.1749, "mean_extremity_kalshi": 0.1815, "model_brier": 0.2058, "kalshi_brier": 0.1951, "brier_diff_model_minus_kalshi": 0.0107, "brier_diff_se": 0.0045, "model_logloss": 0.5985, "kalshi_logloss": 0.5696}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2742, "share_ge_15": 0.4568, "median_abs_gap": 13.38, "n": 7552}, "gen1_elo": {"share_ge_25": 0.2639, "share_ge_15": 0.4507, "median_abs_gap": 13.01, "n": 7552}, "gen1_sr": {"share_ge_25": 0.3208, "share_ge_15": 0.5363, "median_abs_gap": 16.51, "n": 7552}, "gen2": {"share_ge_25": 0.3235, "share_ge_15": 0.525, "median_abs_gap": 16.08, "n": 7552}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1599, "share_ge_15": 0.3514, "median_abs_gap": 10.58, "n": 5521}, "gen1_elo": {"share_ge_25": 0.156, "share_ge_15": 0.3405, "median_abs_gap": 10.03, "n": 5521}, "gen1_sr": {"share_ge_25": 0.2061, "share_ge_15": 0.4403, "median_abs_gap": 13.22, "n": 5521}, "gen2": {"share_ge_25": 0.227, "share_ge_15": 0.4438, "median_abs_gap": 13.04, "n": 5521}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.01, "share_ge_25_all": 0.0347, "share_ge_25_pregame_clean": 0.0353}, "WTA": {"median_abs_gap_pregame_clean": 8.47, "share_ge_25_all": 0.0934, "share_ge_25_pregame_clean": 0.0809}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2203, "share_within_10pp_all": 0.409, "share_within_10pp_pregame_clean": 0.4827, "corr_model_vs_mid_pregame_clean": 0.827}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 171, "model_brier": 0.1812, "kalshi_brier": 0.1823, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 189, "model_brier": 0.2141, "kalshi_brier": 0.2106, "brier_diff_model_minus_kalshi": 0.0035}, "15-25": {"n_settled": 244, "model_brier": 0.2159, "kalshi_brier": 0.2102, "brier_diff_model_minus_kalshi": 0.0057}, "25-40": {"n_settled": 129, "model_brier": 0.2274, "kalshi_brier": 0.1824, "brier_diff_model_minus_kalshi": 0.045}, "3-5": {"n_settled": 109, "model_brier": 0.1749, "kalshi_brier": 0.1756, "brier_diff_model_minus_kalshi": -0.0007}, "40+": {"n_settled": 30, "model_brier": 0.3354, "kalshi_brier": 0.1357, "brier_diff_model_minus_kalshi": 0.1998}, "5-10": {"n_settled": 220, "model_brier": 0.1957, "kalshi_brier": 0.2003, "brier_diff_model_minus_kalshi": -0.0046}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 163, "model_brier": 0.3208, "kalshi_brier": 0.2301, "brier_diff_model_minus_kalshi": 0.0907, "brier_diff_se": 0.0257, "corr_model_outcome": -0.1018, "corr_kalshi_outcome": 0.3278}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
