# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-01T13:55Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 9,610): 0-3 13.4%, 3-5 9.3%, 5-10 19.6%, 10-15 14.7%, 15-25 19.8%, 25-40 14.2%, 40+ 9.0%; median gap 12.37 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.1%, Challenger 11.6%, doubles 8.0%). Main tour: ATP 3.4% and WTA 8.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,226): MARKET_ALREADY_SETTLED_WHEN_PRICED 43.3%, STALE_QUOTE 24.8%, POOR_DATA 6.9%, BOOK_QUALITY 6.0%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IN_PLAY_QUOTE 5.6%, LIMITED_DATA 3.4%, IDENTITY_AMBIGUOUS 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%. By class: coverage 43.3%, market_freshness 24.8%, market_freshness/coverage 11.2%, data 10.2%, execution 6.0%, mapping 2.6%, model_calibration_or_unknown 1.8%.
* **Stale / settled / in-play**: 67.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 54.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,226 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.0% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 714.0 points vs 1938.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.237, Gen-2 1.008, Gen-1 ledger 0.917 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 71 model 0.2373 vs Kalshi 0.1789; n 18 model 0.2907 vs Kalshi 0.1346.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 28,899 model-market comparisons (49,821 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 15,926 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-01T13:51:40.442967+00:00'], shadow board 7,660 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-01T13:51:43.225758+00:00'], Model 4 2,152 rows, 7,794 settled tickers, 1,765 tickers with an external scan.
* By model: {"gen1_ledger": 9307, "gen1_elo": 3852, "fair_v1": 3852, "gen2": 3852, "gen1_sr": 3852, "model4_fundamental": 2094, "model4_conditioned": 2090}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 9,610 | 13.4 | 9.3 | 19.6 | 14.7 | 19.8 | 14.2 | 9.0 | 12.37 | 43.0% | 23.2% |
| MW fair_v1 | 3,852 | 13.6 | 9.1 | 19.0 | 14.8 | 19.0 | 14.7 | 9.9 | 12.73 | 43.6% | 24.6% |
| MW gen1_elo | 3,852 | 13.8 | 8.7 | 19.9 | 15.1 | 18.6 | 14.7 | 9.2 | 12.29 | 42.5% | 23.9% |
| MW gen1_ledger | 5,758 | 13.3 | 9.4 | 20.1 | 14.7 | 20.4 | 13.8 | 8.4 | 12.23 | 42.6% | 22.2% |
| MW gen1_sr | 3,852 | 10.1 | 6.9 | 17.1 | 13.7 | 21.5 | 18.4 | 12.4 | 15.93 | 52.3% | 30.8% |
| MW gen2 | 3,852 | 11.2 | 6.5 | 16.5 | 15.5 | 19.8 | 16.9 | 13.6 | 15.21 | 50.3% | 30.5% |
| all families model4_conditioned | 2,090 | 19.3 | 14.9 | 29.7 | 22.7 | 9.7 | 1.9 | 1.9 | 7.33 | 13.4% | 3.8% |
| all families model4_fundamental | 2,094 | 13.8 | 10.8 | 30.9 | 22.2 | 14.1 | 5.3 | 2.8 | 9.02 | 22.2% | 8.1% |

Configurable thresholds (primary): >=5pp 77.3%, >=10pp 57.7%, >=15pp 43.0%, >=20pp 32.1%, >=25pp 23.2%, >=30pp 17.2%, >=40pp 9.0%, >=50pp 4.1%
Executable gap (model outside the book, before fees): median 9.98pp; >=10pp 50.0%, >=25pp 20.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 192 | 22.4 | 20.3 | 22.9 | 13.0 | 16.7 | 1.6 | 3.1 | 6.01 | 21.3% | 4.7% |
| CHALLENGER | 705 | 16.4 | 8.9 | 15.9 | 15.7 | 16.4 | 13.9 | 12.6 | 13.15 | 43.0% | 26.5% |
| ITF_MEN | 1,211 | 12.1 | 9.0 | 20.0 | 13.6 | 18.9 | 14.9 | 11.4 | 12.61 | 45.2% | 26.3% |
| ITF_WOMEN | 1,353 | 10.8 | 7.2 | 16.6 | 15.1 | 20.9 | 18.9 | 10.6 | 15.17 | 50.4% | 29.5% |
| WTA | 319 | 20.4 | 11.6 | 30.1 | 13.5 | 17.6 | 6.3 | 0.6 | 7.97 | 24.4% | 6.9% |
| WTA125 | 72 | 9.7 | 5.6 | 18.1 | 27.8 | 22.2 | 11.1 | 5.6 | 12.8 | 38.9% | 16.7% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 192 | 23.4 | 13.5 | 23.4 | 16.1 | 17.7 | 2.1 | 3.6 | 6.98 | 23.4% | 5.7% |
| CHALLENGER | 705 | 11.3 | 5.8 | 18.2 | 17.6 | 17.4 | 17.2 | 12.5 | 14.64 | 47.1% | 29.6% |
| ITF_MEN | 1,211 | 10.6 | 6.0 | 16.9 | 16.1 | 19.8 | 16.9 | 13.9 | 15.32 | 50.5% | 30.7% |
| ITF_WOMEN | 1,353 | 8.7 | 6.6 | 14.0 | 13.2 | 19.7 | 19.7 | 18.2 | 18.02 | 57.6% | 37.8% |
| WTA | 319 | 18.2 | 5.3 | 18.5 | 16.6 | 25.4 | 14.7 | 1.2 | 13.18 | 41.4% | 16.0% |
| WTA125 | 72 | 4.2 | 5.6 | 15.3 | 20.8 | 26.4 | 15.3 | 12.5 | 16.39 | 54.2% | 27.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 192 | 31.8 | 13.5 | 26.0 | 9.9 | 9.4 | 6.2 | 3.1 | 6.04 | 18.8% | 9.4% |
| CHALLENGER | 705 | 15.6 | 7.9 | 20.3 | 15.6 | 15.0 | 14.0 | 11.5 | 11.54 | 40.6% | 25.5% |
| ITF_MEN | 1,211 | 10.9 | 9.7 | 18.3 | 15.5 | 18.7 | 15.7 | 11.1 | 12.89 | 45.5% | 26.8% |
| ITF_WOMEN | 1,353 | 10.1 | 6.9 | 17.4 | 14.4 | 23.2 | 18.5 | 9.6 | 15.74 | 51.3% | 28.1% |
| WTA | 319 | 25.1 | 12.2 | 31.0 | 15.1 | 13.5 | 2.5 | 0.6 | 6.99 | 16.6% | 3.1% |
| WTA125 | 72 | 18.1 | 5.6 | 22.2 | 30.6 | 13.9 | 9.7 | 0.0 | 10.72 | 23.6% | 9.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 71 | 23.9 | 22.5 | 35.2 | 11.3 | 7.0 | 0.0 | 0.0 | 6.19 | 7.0% | 0.0% |
| CHALLENGER | 777 | 21.2 | 13.9 | 26.2 | 15.8 | 13.6 | 6.6 | 2.6 | 7.45 | 22.8% | 9.1% |
| DOUBLES | 363 | 5.5 | 3.9 | 9.6 | 10.5 | 21.5 | 20.7 | 28.4 | 24.32 | 70.5% | 49.0% |
| ITF_MEN | 1,929 | 14.2 | 9.0 | 18.8 | 13.6 | 21.4 | 13.6 | 9.4 | 12.58 | 44.5% | 23.1% |
| ITF_WOMEN | 1,775 | 9.0 | 8.3 | 17.6 | 14.4 | 23.2 | 18.6 | 8.8 | 15.23 | 50.6% | 27.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 331 | 13.6 | 9.7 | 21.1 | 17.2 | 23.3 | 11.2 | 3.9 | 11.35 | 38.4% | 15.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 191 | 22.0 | 20.4 | 23.0 | 13.1 | 16.8 | 1.6 | 3.1 | 6.01 | 21.5% | 4.7% |
| CHALLENGER | 526 | 20.5 | 11.2 | 18.8 | 18.6 | 17.3 | 8.8 | 4.8 | 9.94 | 30.8% | 13.5% |
| ITF_MEN | 841 | 16.2 | 11.7 | 24.4 | 14.5 | 18.8 | 10.2 | 4.3 | 9.34 | 33.3% | 14.5% |
| ITF_WOMEN | 964 | 14.4 | 8.9 | 19.3 | 17.9 | 22.0 | 13.3 | 4.2 | 12.36 | 39.4% | 17.4% |
| WTA | 318 | 20.4 | 11.6 | 30.2 | 13.5 | 17.6 | 6.0 | 0.6 | 7.96 | 24.2% | 6.6% |
| WTA125 | 71 | 9.9 | 5.6 | 18.3 | 28.2 | 22.5 | 9.9 | 5.6 | 12.79 | 38.0% | 15.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 191 | 23.6 | 13.1 | 23.6 | 16.2 | 17.8 | 2.1 | 3.7 | 7.04 | 23.6% | 5.8% |
| CHALLENGER | 526 | 13.9 | 7.2 | 22.4 | 20.9 | 19.0 | 12.7 | 3.8 | 11.57 | 35.5% | 16.5% |
| ITF_MEN | 841 | 13.4 | 7.2 | 20.2 | 18.2 | 21.1 | 13.6 | 6.3 | 12.44 | 40.9% | 19.9% |
| ITF_WOMEN | 964 | 10.1 | 8.5 | 16.0 | 13.6 | 22.5 | 17.5 | 11.8 | 15.57 | 51.9% | 29.4% |
| WTA | 318 | 18.2 | 5.3 | 18.6 | 16.7 | 25.5 | 14.5 | 1.3 | 13.18 | 41.2% | 15.7% |
| WTA125 | 71 | 4.2 | 5.6 | 15.5 | 21.1 | 26.8 | 15.5 | 11.3 | 16.14 | 53.5% | 26.8% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 59 | 25.4 | 25.4 | 35.6 | 11.9 | 1.7 | 0.0 | 0.0 | 4.87 | 1.7% | 0.0% |
| CHALLENGER | 639 | 23.6 | 16.3 | 29.1 | 15.3 | 12.8 | 2.7 | 0.2 | 6.68 | 15.7% | 2.8% |
| DOUBLES | 282 | 6.0 | 3.5 | 9.6 | 10.6 | 21.6 | 21.6 | 26.9 | 24.13 | 70.2% | 48.6% |
| ITF_MEN | 1,385 | 17.3 | 10.7 | 22.0 | 14.6 | 21.2 | 10.5 | 3.8 | 10.02 | 35.4% | 14.3% |
| ITF_WOMEN | 1,222 | 11.1 | 9.7 | 21.4 | 16.5 | 24.0 | 15.2 | 2.2 | 12.16 | 41.4% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 255 | 15.3 | 9.0 | 25.5 | 23.5 | 19.6 | 7.1 | 0.0 | 10.01 | 26.7% | 7.1% |
| WTA125 | 252 | 16.3 | 10.7 | 25.4 | 19.8 | 21.0 | 6.3 | 0.4 | 9.32 | 27.8% | 6.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 363 | 5.5 | 3.9 | 9.6 | 10.5 | 21.5 | 20.7 | 28.4 | 24.32 | 70.5% | 49.0% |
| singles | 5,395 | 13.8 | 9.8 | 20.8 | 14.9 | 20.3 | 13.4 | 7.0 | 11.75 | 40.7% | 20.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 849 | 16.2 | 8.2 | 19.0 | 14.0 | 17.4 | 13.4 | 11.7 | 11.93 | 42.5% | 25.1% |
| Hard | 2,751 | 12.8 | 9.6 | 19.3 | 14.6 | 19.4 | 14.8 | 9.5 | 12.78 | 43.7% | 24.3% |
| UNKNOWN | 252 | 13.9 | 6.3 | 15.1 | 18.6 | 19.8 | 17.5 | 8.7 | 13.77 | 46.0% | 26.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,123 | 18.2 | 11.3 | 21.3 | 15.4 | 17.0 | 10.2 | 6.6 | 9.96 | 33.8% | 16.8% |
| B | 504 | 15.3 | 11.3 | 16.9 | 18.4 | 16.1 | 10.3 | 11.7 | 12.01 | 38.1% | 22.0% |
| C | 655 | 13.3 | 8.8 | 24.4 | 13.0 | 15.9 | 14.2 | 10.4 | 11.76 | 40.5% | 24.6% |
| D | 728 | 12.2 | 8.9 | 17.6 | 13.7 | 21.3 | 14.7 | 11.5 | 14.1 | 47.5% | 26.2% |
| F | 842 | 8.0 | 5.0 | 14.1 | 13.9 | 23.9 | 23.5 | 11.6 | 18.83 | 59.0% | 35.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,759 | 18.8 | 12.1 | 26.3 | 16.8 | 16.6 | 6.8 | 2.7 | 8.55 | 26.0% | 9.4% |
| B | 955 | 14.1 | 9.0 | 21.6 | 16.5 | 18.9 | 12.4 | 7.4 | 11.55 | 38.7% | 19.8% |
| C | 1,185 | 11.1 | 8.4 | 15.6 | 14.1 | 21.7 | 15.4 | 13.6 | 15.33 | 50.7% | 29.0% |
| D | 887 | 11.4 | 8.3 | 20.4 | 11.7 | 24.1 | 15.4 | 8.6 | 14.21 | 48.1% | 24.0% |
| F | 972 | 6.7 | 7.3 | 12.4 | 12.2 | 23.7 | 24.6 | 13.1 | 19.52 | 61.3% | 37.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,356 | 16.4 | 10.5 | 20.3 | 16.7 | 17.0 | 10.4 | 8.7 | 10.64 | 36.1% | 19.1% |
| LIMITED | 910 | 15.5 | 11.0 | 22.9 | 13.5 | 15.2 | 12.9 | 9.1 | 10.27 | 37.1% | 22.0% |
| POOR | 1,586 | 10.1 | 6.8 | 15.6 | 13.8 | 22.9 | 19.4 | 11.5 | 16.69 | 53.8% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 325 | 34.8 | 23.1 | 32.9 | 5.8 | 2.5 | 0.9 | 0.0 | 4.14 | 3.4% | 0.9% |
| GAME_SPREAD | 394 | 20.3 | 16.5 | 36.3 | 16.0 | 9.1 | 1.3 | 0.5 | 6.5 | 10.9% | 1.8% |
| MATCH_WINNER | 5,758 | 13.3 | 9.4 | 20.1 | 14.7 | 20.4 | 13.8 | 8.4 | 12.23 | 42.6% | 22.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,686 | 21.9 | 13.5 | 29.9 | 17.4 | 13.8 | 2.8 | 0.7 | 7.06 | 17.2% | 3.4% |
| TOTAL_GAMES | 1,120 | 9.9 | 9.0 | 26.2 | 25.2 | 17.1 | 8.0 | 4.5 | 10.68 | 29.6% | 12.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 717 | 28.3 | 30.8 | 26.8 | 0.8 | 10.7 | 2.1 | 0.4 | 4.34 | 13.2% | 2.5% |
| GAME_SPREAD | 425 | 37.9 | 12.2 | 24.0 | 20.9 | 3.1 | 1.4 | 0.5 | 4.99 | 4.9% | 1.9% |
| TOTAL_GAMES | 948 | 4.1 | 4.1 | 34.4 | 40.0 | 11.8 | 1.9 | 3.7 | 10.66 | 17.4% | 5.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 717 | 23.4 | 17.4 | 33.0 | 8.9 | 10.7 | 5.3 | 1.1 | 5.97 | 17.2% | 6.4% |
| GAME_SPREAD | 425 | 17.4 | 10.8 | 24.0 | 23.3 | 16.9 | 5.4 | 2.1 | 9.68 | 24.5% | 7.5% |
| TOTAL_GAMES | 952 | 5.0 | 5.8 | 32.5 | 31.7 | 15.3 | 5.4 | 4.3 | 10.84 | 25.0% | 9.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3,852 | 43.6% | 24.6% | 12.73 | 33.2% | 13.8% | 9.98 |
| gen1_elo | 3,852 | 42.5% | 23.9% | 12.29 | 31.7% | 13.7% | 9.54 |
| gen1_sr | 3,852 | 52.3% | 30.8% | 15.93 | 43.7% | 20.3% | 13.03 |
| gen2 | 3,852 | 50.3% | 30.5% | 15.21 | 42.8% | 21.2% | 13.01 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,530 | 17.2 | 12.6 | 23.0 | 15.4 | 19.1 | 9.7 | 3.1 | 9.33 | 31.9% | 12.8% |
| STALE | 2,322 | 11.2 | 6.8 | 16.3 | 14.3 | 18.9 | 18.0 | 14.4 | 15.61 | 51.3% | 32.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,110 | 15.1 | 10.3 | 21.9 | 15.9 | 20.0 | 12.2 | 4.7 | 10.78 | 36.8% | 16.8% |
| STALE | 2,648 | 11.1 | 8.4 | 17.9 | 13.2 | 20.9 | 15.8 | 12.7 | 14.7 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 9,610 | 0 | 4640 | 4970 | 31.0 | 143.0 | 1400.4 |
| ge_15pp | 4,132 | 0 | 1633 | 2499 | 34.5 | 353.9 | 1380.4 |
| ge_25pp | 2,226 | 0 | 719 | 1507 | 48.5 | 562.2 | 1380.4 |
| lt_10pp | 4,066 | 0 | 2277 | 1789 | 28.4 | 54.8 | 1102.2 |

Current slate `SL-20261001T135518Z-35bae44f`: 399 priced rows, quote age at build {'median': 58.4, 'max': 85.6}, freshness {'STALE': 399}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 136 | 22.8 | 11.0 | 21.3 | 21.3 | 18.4 | 5.2 | 0.0 | 7.37 | 23.5% | 5.1% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 11 | 0.0 | 0.0 | 9.1 | 45.5 | 45.5 | 0.0 | 0.0 | 13.64 | 45.5% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 3,852 | 156 (4.0%) | 7.0% | 0.0% | {"EXTERNAL_STALE": 136, "AGREES_WITH_KALSHI": 11, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 1,680 | 37 (2.2%) | 13.5% | 0.0% | {"EXTERNAL_STALE": 32, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 948 | 7 (0.7%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 7} |
| fair_v1_ge_25pp_pregame_clean | 402 | 7 (1.7%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 7} |
| fair_v1_lt_10pp | 1,604 | 85 (5.3%) | 1.2% | 0.0% | {"EXTERNAL_STALE": 75, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 767 | 12.7 | 8.1 | 18.6 | 15.5 | 20.6 | 14.7 | 9.8 | 13.43 | 45.1% | 24.5% |
| 4-10x | 545 | 12.3 | 10.1 | 18.9 | 14.3 | 18.5 | 14.9 | 11.0 | 12.89 | 44.4% | 25.9% |
| <2x | 2,057 | 14.8 | 10.0 | 19.9 | 15.2 | 18.0 | 12.8 | 9.4 | 11.65 | 40.2% | 22.2% |
| >=10x | 483 | 11.6 | 5.6 | 15.7 | 12.0 | 21.3 | 22.4 | 11.4 | 17.89 | 55.1% | 33.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 963 | 13.4 | 9.8 | 22.0 | 15.3 | 17.4 | 11.8 | 10.3 | 11.95 | 39.6% | 22.1% |
| 300-1000 | 959 | 14.2 | 8.6 | 18.0 | 15.8 | 19.8 | 14.6 | 9.1 | 12.98 | 43.5% | 23.7% |
| <300 | 1,016 | 8.9 | 6.0 | 15.0 | 12.1 | 22.6 | 22.1 | 13.3 | 18.82 | 58.1% | 35.4% |
| >=3000 | 914 | 18.5 | 12.2 | 21.2 | 16.1 | 15.8 | 9.4 | 6.8 | 9.67 | 31.9% | 16.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 159 | 0.5211 | 0.3906 | 0.4214 | +0.100 | -0.031 | 0.0122 ± 0.0114 |
| ratio 4-10x | 118 | 0.5739 | 0.4463 | 0.4746 | +0.099 | -0.028 | 0.0111 ± 0.0127 |
| ratio <2x | 308 | 0.5329 | 0.4136 | 0.4643 | +0.069 | -0.051 | 0.009 ± 0.0075 |
| ratio >=10x | 109 | 0.5395 | 0.3764 | 0.4495 | +0.090 | -0.073 | 0.0192 ± 0.0176 |
| thinner_sample 1000-3000 | 173 | 0.5412 | 0.4223 | 0.4624 | +0.079 | -0.040 | -0.0006 ± 0.01 |
| thinner_sample 300-1000 | 207 | 0.5539 | 0.432 | 0.4831 | +0.071 | -0.051 | 0.0017 ± 0.0095 |
| thinner_sample <300 | 235 | 0.5291 | 0.3706 | 0.4255 | +0.104 | -0.055 | 0.0263 ± 0.011 |
| thinner_sample >=3000 | 79 | 0.5177 | 0.4256 | 0.443 | +0.075 | -0.017 | 0.0213 ± 0.0117 |
| data_status ADEQUATE | 172 | 0.5234 | 0.4183 | 0.4651 | +0.058 | -0.047 | 0.0025 ± 0.009 |
| data_status LIMITED | 162 | 0.5637 | 0.4464 | 0.4938 | +0.070 | -0.047 | 0.0001 ± 0.0106 |
| data_status POOR | 360 | 0.5338 | 0.3859 | 0.4306 | +0.103 | -0.045 | 0.0213 ± 0.0084 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 117 | 0.175 | 0.176 | -0.0010 ± 0.0014 | 0.5228 | 0.5255 | 0.4947 | 0.4799 | 0.4957 | -0.098 ± 0.0419 | -0.01 (3) |
| 3-5 | 73 | 0.1626 | 0.1606 | +0.0019 ± 0.0039 | 0.5011 | 0.4929 | 0.5138 | 0.4729 | 0.4658 | -0.098 ± 0.05 | 0.02 (1) |
| 5-10 | 147 | 0.1898 | 0.1917 | -0.0019 ± 0.0054 | 0.5623 | 0.5619 | 0.5272 | 0.4528 | 0.5034 | -0.065 ± 0.0366 | -0.02 (2) |
| 10-15 | 118 | 0.2132 | 0.206 | +0.0072 ± 0.0105 | 0.6091 | 0.5927 | 0.5222 | 0.398 | 0.4322 | -0.079 ± 0.042 | -0.0633 (3) |
| 15-25 | 150 | 0.2122 | 0.2084 | +0.0038 ± 0.0145 | 0.6121 | 0.5954 | 0.5629 | 0.3664 | 0.46 | -0.025 ± 0.0358 | -0.02 (4) |
| 25-40 | 71 | 0.2373 | 0.1789 | +0.0584 ± 0.0316 | 0.6651 | 0.5282 | 0.5987 | 0.2817 | 0.338 | -0.081 ± 0.0482 | -0.01 (1) |
| 40+ | 18 | 0.2907 | 0.1346 | +0.1561 ± 0.0788 | 0.7586 | 0.4251 | 0.6703 | 0.2242 | 0.2778 | -0.066 ± 0.0745 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 319 | 0.1583 | 0.159 | -0.0007 ± 0.0008 | 0.4795 | 0.4807 | 0.511 | 0.4962 | 0.5235 | -0.041 ± 0.0234 | -0.0188 (8) |
| 3-5 | 215 | 0.1663 | 0.1661 | +0.0002 ± 0.0023 | 0.5079 | 0.5025 | 0.4939 | 0.4537 | 0.4698 | -0.042 ± 0.0287 | 0.02 (1) |
| 5-10 | 443 | 0.1737 | 0.1734 | +0.0003 ± 0.0029 | 0.523 | 0.5156 | 0.4787 | 0.4053 | 0.4424 | -0.029 ± 0.0199 | -0.0133 (6) |
| 10-15 | 362 | 0.1905 | 0.1741 | +0.0163 ± 0.0055 | 0.5614 | 0.5118 | 0.4732 | 0.3489 | 0.3453 | -0.071 ± 0.0219 | -0.0633 (3) |
| 15-25 | 508 | 0.1916 | 0.1597 | +0.0319 ± 0.007 | 0.5708 | 0.4728 | 0.4796 | 0.2825 | 0.3012 | -0.043 ± 0.0174 | -0.017 (10) |
| 25-40 | 448 | 0.2111 | 0.0874 | +0.1237 ± 0.0089 | 0.6134 | 0.2914 | 0.4905 | 0.172 | 0.1384 | -0.079 ± 0.0136 | -0.01 (1) |
| 40+ | 318 | 0.3584 | 0.0356 | +0.3227 ± 0.0112 | 0.9275 | 0.1506 | 0.6094 | 0.0972 | 0.0472 | -0.077 ± 0.0096 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 71 | 0.1566 | 0.1594 | -0.0028 ± 0.0016 | 0.4768 | 0.4832 | 0.518 | 0.5032 | 0.6056 | +0.003 ± 0.0459 | -0.01 (1) |
| 3-5 | 53 | 0.2151 | 0.213 | +0.0021 ± 0.0052 | 0.6076 | 0.6081 | 0.4861 | 0.4468 | 0.434 | -0.096 ± 0.0675 | 0.02 (1) |
| 5-10 | 133 | 0.1798 | 0.1733 | +0.0065 ± 0.0054 | 0.5403 | 0.5231 | 0.5673 | 0.4915 | 0.4737 | -0.128 ± 0.0365 | -0.01 (3) |
| 10-15 | 125 | 0.2134 | 0.2025 | +0.0108 ± 0.0102 | 0.6127 | 0.5871 | 0.5862 | 0.4616 | 0.488 | -0.076 ± 0.0415 | -0.0667 (3) |
| 15-25 | 169 | 0.2182 | 0.1983 | +0.0199 ± 0.0136 | 0.6217 | 0.5708 | 0.5775 | 0.3794 | 0.432 | -0.073 ± 0.0352 | -0.0167 (3) |
| 25-40 | 100 | 0.2658 | 0.1792 | +0.0866 ± 0.0261 | 0.7392 | 0.5265 | 0.6465 | 0.3382 | 0.35 | -0.145 ± 0.0434 | -0.025 (2) |
| 40+ | 43 | 0.3483 | 0.2154 | +0.1329 ± 0.07 | 0.9592 | 0.6253 | 0.7398 | 0.2513 | 0.3721 | +0.016 ± 0.0652 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 258 | 0.1342 | 0.1361 | -0.0019 ± 0.0008 | 0.4154 | 0.4207 | 0.5515 | 0.5368 | 0.5969 | +0.007 ± 0.0226 | -0.0217 (6) |
| 3-5 | 136 | 0.1707 | 0.1699 | +0.0008 ± 0.0029 | 0.5036 | 0.5058 | 0.5371 | 0.4973 | 0.5 | -0.054 ± 0.0359 | 0.02 (1) |
| 5-10 | 401 | 0.1789 | 0.1776 | +0.0013 ± 0.0032 | 0.5367 | 0.5276 | 0.5265 | 0.4515 | 0.4788 | -0.035 ± 0.0212 | -0.01 (4) |
| 10-15 | 390 | 0.1857 | 0.1738 | +0.0119 ± 0.0053 | 0.5501 | 0.5126 | 0.527 | 0.4027 | 0.4256 | -0.038 ± 0.0215 | -0.0575 (4) |
| 15-25 | 517 | 0.1984 | 0.1587 | +0.0397 ± 0.007 | 0.5828 | 0.4743 | 0.5078 | 0.3116 | 0.3133 | -0.069 ± 0.0176 | -0.0143 (7) |
| 25-40 | 482 | 0.2261 | 0.1066 | +0.1195 ± 0.0094 | 0.6538 | 0.3375 | 0.5338 | 0.2188 | 0.1929 | -0.085 ± 0.0152 | -0.015 (6) |
| 40+ | 429 | 0.3924 | 0.0664 | +0.3260 ± 0.0143 | 1.0309 | 0.2329 | 0.6554 | 0.1205 | 0.0956 | -0.056 ± 0.0119 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 113 | 0.1654 | 0.1681 | -0.0026 ± 0.0014 | 0.4981 | 0.5047 | 0.5072 | 0.4929 | 0.5398 | -0.042 ± 0.0385 | -0.01 (5) |
| 3-5 | 74 | 0.1617 | 0.1579 | +0.0038 ± 0.0038 | 0.4935 | 0.4834 | 0.5138 | 0.4743 | 0.4459 | -0.147 ± 0.05 | -- (0) |
| 5-10 | 140 | 0.1972 | 0.1961 | +0.0010 ± 0.0055 | 0.5836 | 0.5727 | 0.5161 | 0.445 | 0.4786 | -0.066 ± 0.0373 | -0.01 (2) |
| 10-15 | 128 | 0.2126 | 0.2118 | +0.0008 ± 0.0102 | 0.6133 | 0.6063 | 0.5459 | 0.422 | 0.4922 | -0.057 ± 0.041 | -0.044 (5) |
| 15-25 | 145 | 0.2119 | 0.2038 | +0.0081 ± 0.0144 | 0.6165 | 0.5859 | 0.5781 | 0.3848 | 0.4621 | -0.045 ± 0.0358 | -0.03 (1) |
| 25-40 | 80 | 0.2334 | 0.1816 | +0.0518 ± 0.0302 | 0.66 | 0.5346 | 0.596 | 0.2796 | 0.35 | -0.070 ± 0.0455 | 0.0 (1) |
| 40+ | 14 | 0.3177 | 0.1479 | +0.1698 ± 0.0969 | 0.8219 | 0.4582 | 0.6811 | 0.2239 | 0.2857 | -0.064 ± 0.0919 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 315 | 0.1532 | 0.1539 | -0.0007 ± 0.0008 | 0.469 | 0.4702 | 0.5052 | 0.4903 | 0.5048 | -0.048 ± 0.0223 | -0.0162 (13) |
| 3-5 | 208 | 0.1729 | 0.169 | +0.0039 ± 0.0023 | 0.5163 | 0.5057 | 0.4839 | 0.4447 | 0.4183 | -0.096 ± 0.0292 | -0.01 (2) |
| 5-10 | 435 | 0.1801 | 0.1751 | +0.0051 ± 0.003 | 0.5415 | 0.5158 | 0.4755 | 0.4029 | 0.4092 | -0.051 ± 0.0201 | -0.01 (2) |
| 10-15 | 381 | 0.1914 | 0.178 | +0.0134 ± 0.0054 | 0.5679 | 0.5232 | 0.4867 | 0.3633 | 0.3753 | -0.057 ± 0.0216 | -0.03 (9) |
| 15-25 | 534 | 0.1818 | 0.1456 | +0.0362 ± 0.0066 | 0.5508 | 0.4401 | 0.4828 | 0.2844 | 0.294 | -0.051 ± 0.0161 | -0.03 (2) |
| 25-40 | 445 | 0.214 | 0.0962 | +0.1178 ± 0.0094 | 0.6213 | 0.3114 | 0.4938 | 0.1735 | 0.1506 | -0.072 ± 0.0143 | 0.0 (1) |
| 40+ | 295 | 0.3777 | 0.0346 | +0.3431 ± 0.012 | 0.9844 | 0.1488 | 0.6131 | 0.0945 | 0.0339 | -0.086 ± 0.0098 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 391 | 0.2019 | 0.2019 | +0.0001 ± 0.0008 | 0.5837 | 0.5836 | 0.5048 | 0.4901 | 0.4859 | -0.048 ± 0.0228 | -0.0226 (46) |
| 3-5 | 282 | 0.1915 | 0.1914 | +0.0002 ± 0.0021 | 0.5631 | 0.5592 | 0.461 | 0.4212 | 0.4433 | -0.029 ± 0.0259 | -0.0059 (32) |
| 5-10 | 602 | 0.1857 | 0.1798 | +0.0058 ± 0.0026 | 0.5542 | 0.5381 | 0.461 | 0.3878 | 0.3854 | -0.048 ± 0.0173 | -0.0049 (71) |
| 10-15 | 399 | 0.2019 | 0.1884 | +0.0135 ± 0.0055 | 0.5934 | 0.5545 | 0.4528 | 0.3294 | 0.3358 | -0.046 ± 0.0216 | 0.0016 (63) |
| 15-25 | 532 | 0.2344 | 0.2088 | +0.0255 ± 0.0077 | 0.6624 | 0.6034 | 0.5307 | 0.3374 | 0.3684 | -0.034 ± 0.0197 | -0.0216 (58) |
| 25-40 | 253 | 0.262 | 0.1663 | +0.0957 ± 0.0161 | 0.7238 | 0.5017 | 0.5667 | 0.2553 | 0.2569 | -0.062 ± 0.0254 | -0.0216 (25) |
| 40+ | 91 | 0.4328 | 0.1575 | +0.2753 ± 0.0447 | 1.217 | 0.4875 | 0.7317 | 0.2235 | 0.2308 | -0.065 ± 0.0435 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 715 | 0.1932 | 0.1927 | +0.0005 ± 0.0006 | 0.5637 | 0.5619 | 0.4977 | 0.4831 | 0.4671 | -0.058 ± 0.0164 | -0.0155 (82) |
| 3-5 | 514 | 0.1969 | 0.1958 | +0.0012 ± 0.0016 | 0.5732 | 0.5674 | 0.4675 | 0.4276 | 0.4339 | -0.039 ± 0.0195 | -0.018 (54) |
| 5-10 | 1091 | 0.1837 | 0.1762 | +0.0076 ± 0.0019 | 0.5499 | 0.5273 | 0.4463 | 0.3725 | 0.3621 | -0.052 ± 0.0128 | -0.0089 (121) |
| 10-15 | 797 | 0.1963 | 0.1813 | +0.0151 ± 0.0038 | 0.5791 | 0.536 | 0.4453 | 0.3218 | 0.3225 | -0.045 ± 0.015 | -0.0053 (99) |
| 15-25 | 1105 | 0.2215 | 0.1864 | +0.0351 ± 0.0051 | 0.639 | 0.5467 | 0.5034 | 0.3076 | 0.3158 | -0.044 ± 0.013 | -0.0255 (106) |
| 25-40 | 755 | 0.2438 | 0.1285 | +0.1153 ± 0.0082 | 0.688 | 0.4018 | 0.5254 | 0.21 | 0.1868 | -0.068 ± 0.0129 | -0.0206 (47) |
| 40+ | 457 | 0.394 | 0.081 | +0.3129 ± 0.0145 | 1.0764 | 0.2719 | 0.6549 | 0.1381 | 0.105 | -0.077 ± 0.0137 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 694 | 1.237 ± 0.114 | 1.289 | 0.1717 | 0.1879 | 0.2007 | 0.189 |
| gen2 | 694 | 1.008 ± 0.098 | 1.224 | 0.1883 | 0.1869 | 0.2183 | 0.1897 |
| gen1_elo | 694 | 1.184 ± 0.11 | 1.27 | 0.1778 | 0.1884 | 0.2007 | 0.1893 |
| gen1_sr | 694 | 1.224 ± 0.128 | 1.274 | 0.1454 | 0.1895 | 0.2166 | 0.1889 |
| gen1_ledger | 2550 | 0.917 ± 0.054 | 1.086 | 0.1625 | 0.2012 | 0.2179 | 0.1897 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 4,132)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,238 | 30.0% |
| STALE_QUOTE | market_freshness | 1,233 | 29.8% |
| POOR_DATA | data | 356 | 8.6% |
| BOOK_QUALITY | execution | 284 | 6.9% |
| LIMITED_DATA | data | 269 | 6.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 255 | 6.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 211 | 5.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 200 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 83 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 30.0%, market_freshness 29.8%, data 15.1%, market_freshness/coverage 11.3%, execution 6.9%, model_calibration_or_unknown 4.8%, mapping 2.0%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 66.1%, STALE_KALSHI_QUOTE 60.5%, STALE_PLAYER_DATA 58.6%, THIN_PLAYER_HISTORY 53.4%, MODEL_INTERNAL_DISAGREEMENT 32.7%, ASYMMETRIC_SAMPLE_SIZE 29.5%, WIDE_SPREAD 15.6%, PLAYER_IDENTITY_RISK 11.9%, MODEL_HIGH_UNCERTAINTY 10.8%, LEVEL_TRANSFER_RISK 9.4%, EVENT_MAPPING_RISK 7.4%, LOW_DISPLAYED_LIQUIDITY 4.3%, MODEL_CALIBRATION_OUTLIER 2.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 32.9%, POST_SETTLEMENT_OBSERVATION 30.0%, POSSIBLE_IN_PLAY_QUOTE 7.0%, CONFIRMED_IN_PLAY_QUOTE 2.7%

### >= ge_25 pp (N = 2,226)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 963 | 43.3% |
| STALE_QUOTE | market_freshness | 553 | 24.8% |
| POOR_DATA | data | 153 | 6.9% |
| BOOK_QUALITY | execution | 134 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 126 | 5.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 124 | 5.6% |
| LIMITED_DATA | data | 75 | 3.4% |
| IDENTITY_AMBIGUOUS | mapping | 58 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 40 | 1.8% |

Cause class: coverage 43.3%, market_freshness 24.8%, market_freshness/coverage 11.2%, data 10.2%, execution 6.0%, mapping 2.6%, model_calibration_or_unknown 1.8%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 70.6%, STALE_KALSHI_QUOTE 67.7%, STALE_PLAYER_DATA 57.0%, THIN_PLAYER_HISTORY 56.2%, MODEL_INTERNAL_DISAGREEMENT 33.5%, ASYMMETRIC_SAMPLE_SIZE 32.0%, PLAYER_IDENTITY_RISK 15.0%, WIDE_SPREAD 14.3%, MODEL_HIGH_UNCERTAINTY 11.7%, EVENT_MAPPING_RISK 9.2%, LEVEL_TRANSFER_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 4.4%, MODEL_CALIBRATION_OUTLIER 3.0%, UNKNOWN 0.3%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 46.5%, POST_SETTLEMENT_OBSERVATION 43.3%, POSSIBLE_IN_PLAY_QUOTE 6.6%, CONFIRMED_IN_PLAY_QUOTE 3.0%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 1865, "IDENTITY_AMBIGUOUS": 361}; ticker orientation: {"VERIFIED": 2226}.

Checks: discipline:AMBIGUOUS 178, discipline:PASS 2048, identity_confidence:AMBIGUOUS 334, identity_confidence:PASS 1892, level_mapping:NA 190, level_mapping:PASS 2036, market_pair:AMBIGUOUS 57, market_pair:NA 60, market_pair:PASS 2109, model_complement:NA 33, model_complement:PASS 2193, namesake:PASS 2226, physical_match_id:NA 1278, physical_match_id:PASS 948, player_ids:PASS 2226, same_pair_other_event:PASS 2226, ticker_orientation:PASS 2226

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 263 | 3.4% | 3.6% | 0.4% | {"market_freshness": 9} | 5.96 | 0.1838 / 0.1834 (45) | 37.6% | 0.0% | 0.8% | 4.9% |
| CHALLENGER | 1,482 | 17.4% | 7.6% | 11.6% | {"coverage": 135, "market_freshness": 60, "market_freshness/coverage": 34, "data": 15, "model_calibration_or_unknown": 11, "execution": 3} | 7.51 | 0.2229 / 0.2035 (497) | 51.5% | 4.3% | 0.7% | 21.4% |
| DOUBLES | 363 | 49.0% | 48.6% | 8.0% | {"market_freshness": 89, "market_freshness/coverage": 36, "execution": 28, "mapping": 20, "coverage": 5} | 24.13 | 0.3226 / 0.2212 (144) | 60.6% | 0.0% | 100.0% | 22.3% |
| ITF_MEN | 3,140 | 24.3% | 14.4% | 34.3% | {"coverage": 378, "market_freshness": 164, "data": 83, "market_freshness/coverage": 66, "execution": 62, "mapping": 10, "model_calibration_or_unknown": 1} | 9.84 | 0.2069 / 0.1802 (1175) | 53.7% | 51.8% | 5.6% | 29.1% |
| ITF_WOMEN | 3,128 | 28.3% | 17.4% | 39.8% | {"coverage": 433, "market_freshness": 199, "data": 113, "market_freshness/coverage": 72, "execution": 32, "mapping": 26, "model_calibration_or_unknown": 11} | 12.22 | 0.2063 / 0.1871 (1019) | 56.5% | 55.3% | 6.9% | 30.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.5% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 682 | 8.4% | 6.8% | 2.6% | {"market_freshness": 19, "market_freshness/coverage": 14, "data": 9, "model_calibration_or_unknown": 6, "execution": 4, "coverage": 4, "mapping": 1} | 8.47 | 0.1995 / 0.1973 (113) | 37.4% | 3.1% | 1.8% | 16.0% |
| WTA125 | 403 | 15.4% | 8.7% | 2.8% | {"market_freshness/coverage": 27, "market_freshness": 11, "model_calibration_or_unknown": 9, "data": 8, "coverage": 7} | 10.53 | 0.2278 / 0.204 (209) | 34.5% | 9.4% | 0.5% | 19.9% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 5 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 6 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 7 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 8 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 9 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 10 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 11 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 13 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 14 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 15 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 16 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 17 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 19 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 20 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 21 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 22 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 23 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 24 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 25 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 27 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 28 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 29 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 30 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 31 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 183 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 32 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 34 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 36 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 86 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 37 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 38 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 39 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 40 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 41 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 819 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 42 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 43 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXITFWMATCH-26SEP24BOUKUR-BOU` | ITF_WOMEN | gen1_ledger | 76% / 8% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 1497.0, ratio 2.48); no external reference |
| 45 | `KXATPCHALLENGERMATCH-26SEP28TABSAN-SAN` | CHALLENGER | gen1_ledger | 70% / 4% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 48 min (STALE); no external reference |
| 46 | `KXITFWMATCH-26SEP22SHCPAS-PAS` | ITF_WOMEN | gen1_ledger | 69% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 199 min (STALE); data POOR (grade F, thinner serve sample 239.0, ratio 5.93); no external reference |
| 47 | `KXITFWMATCH-26SEP29KRURAY-KRU` | ITF_WOMEN | fair_v1 | 78% / 12% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 126 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 223.0); no external reference |
| 48 | `KXWTADOUBLES-26SEP20DETKHRPRETAR-PRETAR` | DOUBLES | gen1_ledger | 84% / 18% | +66 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26SEP30BIOKRO-KRO` | ITF_WOMEN | fair_v1 | 68% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 3.24); no external reference |
| 50 | `KXITFMATCH-26SEP12EFSMOR-MOR` | ITF_MEN | gen1_ledger | 67% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 36 min (STALE); data LIMITED (grade B, thinner serve sample 3783.0, ratio 1.33); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9704, "by_level_share_of_ge_25pp": {"ATP": 0.004, "CHALLENGER": 0.1159, "DOUBLES": 0.08, "ITF_MEN": 0.3432, "ITF_WOMEN": 0.398, "OTHER": 0.0054, "WTA": 0.0256, "WTA125": 0.0279}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.677, "share_primary_cause_market_settled_or_in_play": 0.5449, "share_primary_cause_stale_quote_only": 0.2484}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2226, "identity_ambiguous_share": 0.1622, "ticker_orientation": {"VERIFIED": 2226}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 948, "with_external": 7, "coverage": 0.0074, "external_status": {"EXTERNAL_STALE": 7}, "triangulation": {"INSUFFICIENT_INPUTS": 7}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 402, "with_external": 7, "coverage": 0.0174, "external_status": {"EXTERNAL_STALE": 7}, "triangulation": {"INSUFFICIENT_INPUTS": 7}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 714.0, "median_sample_ratio": 2.46, "median_min_matches": 24.0, "median_max_days_since_last": 173.5, "share_severe_asymmetry": 0.1765, "data_status": {"POOR": 1079, "LIMITED": 789, "ADEQUATE": 358}, "comparison_lt_10pp": {"median_thinner_serve_points": 1938.0, "median_sample_ratio": 1.71, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 159, "model_minus_observed": 0.0997, "kalshi_minus_observed": -0.0308, "brier_diff_model_minus_kalshi": 0.0122}, "4-10x": {"n": 118, "model_minus_observed": 0.0993, "kalshi_minus_observed": -0.0283, "brier_diff_model_minus_kalshi": 0.0111}, "<2x": {"n": 308, "model_minus_observed": 0.0686, "kalshi_minus_observed": -0.0507, "brier_diff_model_minus_kalshi": 0.009}, ">=10x": {"n": 109, "model_minus_observed": 0.09, "kalshi_minus_observed": -0.0731, "brier_diff_model_minus_kalshi": 0.0192}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 694, "model": {"intercept": -0.659, "slope": 1.008, "slope_se": 0.098}, "kalshi_mid_same_rows": {"intercept": 0.231, "slope": 1.224, "slope_se": 0.108}, "mean_extremity_model": 0.1883, "mean_extremity_kalshi": 0.1869, "model_brier": 0.2183, "kalshi_brier": 0.1897, "brier_diff_model_minus_kalshi": 0.0286, "brier_diff_se": 0.0071, "model_logloss": 0.6264, "kalshi_logloss": 0.5555}, "fair_v1": {"n": 694, "model": {"intercept": -0.453, "slope": 1.237, "slope_se": 0.114}, "kalshi_mid_same_rows": {"intercept": 0.343, "slope": 1.289, "slope_se": 0.112}, "mean_extremity_model": 0.1717, "mean_extremity_kalshi": 0.1879, "model_brier": 0.2007, "kalshi_brier": 0.189, "brier_diff_model_minus_kalshi": 0.0117, "brier_diff_se": 0.0055, "model_logloss": 0.5835, "kalshi_logloss": 0.554}, "gen1_elo": {"n": 694, "model": {"intercept": -0.429, "slope": 1.184, "slope_se": 0.11}, "kalshi_mid_same_rows": {"intercept": 0.351, "slope": 1.27, "slope_se": 0.109}, "mean_extremity_model": 0.1778, "mean_extremity_kalshi": 0.1884, "model_brier": 0.2007, "kalshi_brier": 0.1893, "brier_diff_model_minus_kalshi": 0.0114, "brier_diff_se": 0.0055, "model_logloss": 0.586, "kalshi_logloss": 0.5544}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2461, "share_ge_15": 0.4361, "median_abs_gap": 12.73, "n": 3852}, "gen1_elo": {"share_ge_25": 0.2386, "share_ge_15": 0.425, "median_abs_gap": 12.29, "n": 3852}, "gen1_sr": {"share_ge_25": 0.3079, "share_ge_15": 0.5231, "median_abs_gap": 15.93, "n": 3852}, "gen2": {"share_ge_25": 0.305, "share_ge_15": 0.5034, "median_abs_gap": 15.21, "n": 3852}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1381, "share_ge_15": 0.3322, "median_abs_gap": 9.98, "n": 2911}, "gen1_elo": {"share_ge_25": 0.1374, "share_ge_15": 0.3167, "median_abs_gap": 9.54, "n": 2911}, "gen1_sr": {"share_ge_25": 0.2027, "share_ge_15": 0.4366, "median_abs_gap": 13.03, "n": 2911}, "gen2": {"share_ge_25": 0.212, "share_ge_15": 0.4277, "median_abs_gap": 13.01, "n": 2911}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.96, "share_ge_25_all": 0.0342, "share_ge_25_pregame_clean": 0.036}, "WTA": {"median_abs_gap_pregame_clean": 8.47, "share_ge_25_all": 0.0836, "share_ge_25_pregame_clean": 0.0681}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2268, "share_within_10pp_all": 0.4231, "share_within_10pp_pregame_clean": 0.499, "corr_model_vs_mid_pregame_clean": 0.834}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 117, "model_brier": 0.175, "kalshi_brier": 0.176, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 118, "model_brier": 0.2132, "kalshi_brier": 0.206, "brier_diff_model_minus_kalshi": 0.0072}, "15-25": {"n_settled": 150, "model_brier": 0.2122, "kalshi_brier": 0.2084, "brier_diff_model_minus_kalshi": 0.0038}, "25-40": {"n_settled": 71, "model_brier": 0.2373, "kalshi_brier": 0.1789, "brier_diff_model_minus_kalshi": 0.0584}, "3-5": {"n_settled": 73, "model_brier": 0.1626, "kalshi_brier": 0.1606, "brier_diff_model_minus_kalshi": 0.0019}, "40+": {"n_settled": 18, "model_brier": 0.2907, "kalshi_brier": 0.1346, "brier_diff_model_minus_kalshi": 0.1561}, "5-10": {"n_settled": 147, "model_brier": 0.1898, "kalshi_brier": 0.1917, "brier_diff_model_minus_kalshi": -0.0019}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 144, "model_brier": 0.3226, "kalshi_brier": 0.2212, "brier_diff_model_minus_kalshi": 0.1014, "brier_diff_se": 0.0276, "corr_model_outcome": -0.0648, "corr_kalshi_outcome": 0.3753}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
