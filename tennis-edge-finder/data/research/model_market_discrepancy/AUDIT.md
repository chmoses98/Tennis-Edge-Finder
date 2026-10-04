# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-04T11:15Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 11,915): 0-3 13.3%, 3-5 9.1%, 5-10 19.2%, 10-15 15.0%, 15-25 19.5%, 25-40 14.5%, 40+ 9.4%; median gap 12.57 pp.
* **Where the extremes live**: 96.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.6%, Challenger 12.7%, doubles 6.5%). Main tour: ATP 5.9% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,850): MARKET_ALREADY_SETTLED_WHEN_PRICED 46.0%, STALE_QUOTE 25.8%, POOR_DATA 5.9%, BOOK_QUALITY 5.8%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IN_PLAY_QUOTE 3.6%, LIMITED_DATA 3.0%, IDENTITY_AMBIGUOUS 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 46.0%, market_freshness 25.8%, data 8.9%, market_freshness/coverage 8.8%, execution 5.8%, mapping 2.6%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 71.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 54.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,850 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 14.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 6.7% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 824.0 points vs 1948.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.106, Gen-2 0.921, Gen-1 ledger 0.888 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 98 model 0.2321 vs Kalshi 0.1873; n 27 model 0.338 vs Kalshi 0.1489.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 38,134 model-market comparisons (66,510 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 17,176 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-04T11:10:53.534989+00:00'], shadow board 11,135 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-04T11:10:57.065218+00:00'], Model 4 3,018 rows, 8,354 settled tickers, 1,901 tickers with an external scan.
* By model: {"gen1_ledger": 9921, "gen1_elo": 5599, "fair_v1": 5599, "gen2": 5599, "gen1_sr": 5599, "model4_fundamental": 2913, "model4_conditioned": 2904}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 11,915 | 13.3 | 9.1 | 19.2 | 15.0 | 19.5 | 14.5 | 9.4 | 12.57 | 43.4% | 23.9% |
| MW fair_v1 | 5,599 | 13.4 | 8.5 | 18.5 | 15.3 | 18.4 | 15.2 | 10.7 | 12.95 | 44.3% | 25.9% |
| MW gen1_elo | 5,599 | 13.4 | 8.8 | 19.8 | 14.8 | 18.2 | 15.0 | 10.0 | 12.47 | 43.3% | 25.1% |
| MW gen1_ledger | 6,316 | 13.2 | 9.6 | 19.8 | 14.7 | 20.5 | 13.8 | 8.3 | 12.21 | 42.6% | 22.2% |
| MW gen1_sr | 5,599 | 9.6 | 7.4 | 16.5 | 13.6 | 22.1 | 18.2 | 12.6 | 16.15 | 52.9% | 30.8% |
| MW gen2 | 5,599 | 11.3 | 6.7 | 16.6 | 14.2 | 20.2 | 17.1 | 13.9 | 15.55 | 51.2% | 30.9% |
| all families model4_conditioned | 2,904 | 18.0 | 15.0 | 28.6 | 23.1 | 11.2 | 2.3 | 1.8 | 7.66 | 15.3% | 4.1% |
| all families model4_fundamental | 2,913 | 14.2 | 10.4 | 29.1 | 21.2 | 15.7 | 6.3 | 3.0 | 9.37 | 25.0% | 9.4% |

Configurable thresholds (primary): >=5pp 77.6%, >=10pp 58.4%, >=15pp 43.4%, >=20pp 33.0%, >=25pp 23.9%, >=30pp 17.5%, >=40pp 9.4%, >=50pp 4.3%
Executable gap (model outside the book, before fees): median 10.16pp; >=10pp 50.4%, >=25pp 21.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 264 | 21.2 | 16.3 | 26.9 | 12.9 | 15.2 | 3.4 | 4.2 | 6.67 | 22.7% | 7.6% |
| CHALLENGER | 1,113 | 15.9 | 10.9 | 16.7 | 16.3 | 15.1 | 14.0 | 11.1 | 12.07 | 40.2% | 25.2% |
| ITF_MEN | 1,700 | 11.9 | 8.3 | 19.8 | 14.9 | 17.7 | 14.7 | 12.6 | 12.78 | 45.0% | 27.3% |
| ITF_WOMEN | 1,996 | 10.2 | 6.0 | 15.7 | 15.4 | 21.3 | 19.7 | 11.7 | 16.12 | 52.7% | 31.4% |
| WTA | 435 | 23.0 | 10.6 | 25.8 | 12.6 | 18.9 | 6.7 | 2.5 | 8.16 | 28.1% | 9.2% |
| WTA125 | 91 | 13.2 | 4.4 | 17.6 | 26.4 | 18.7 | 14.3 | 5.5 | 12.01 | 38.5% | 19.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 264 | 21.6 | 12.9 | 25.0 | 15.2 | 17.8 | 3.0 | 4.5 | 7.73 | 25.4% | 7.6% |
| CHALLENGER | 1,113 | 13.7 | 6.3 | 19.3 | 15.2 | 18.1 | 16.4 | 11.1 | 13.54 | 45.6% | 27.5% |
| ITF_MEN | 1,700 | 9.6 | 6.9 | 17.5 | 15.2 | 20.2 | 16.5 | 14.0 | 15.4 | 50.8% | 30.5% |
| ITF_WOMEN | 1,996 | 8.4 | 6.3 | 13.1 | 12.1 | 21.1 | 20.0 | 19.0 | 19.55 | 60.1% | 39.0% |
| WTA | 435 | 20.5 | 5.5 | 16.8 | 15.6 | 22.3 | 16.8 | 2.5 | 12.98 | 41.6% | 19.3% |
| WTA125 | 91 | 5.5 | 5.5 | 15.4 | 19.8 | 25.3 | 15.4 | 13.2 | 16.64 | 53.8% | 28.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 264 | 26.9 | 11.7 | 26.9 | 9.8 | 10.2 | 9.8 | 4.5 | 7.4 | 24.6% | 14.4% |
| CHALLENGER | 1,113 | 16.7 | 9.6 | 22.3 | 13.5 | 13.2 | 12.8 | 11.9 | 10.49 | 37.9% | 24.7% |
| ITF_MEN | 1,700 | 10.4 | 9.3 | 18.4 | 15.7 | 18.6 | 15.2 | 12.3 | 13.47 | 46.2% | 27.5% |
| ITF_WOMEN | 1,996 | 10.0 | 6.4 | 16.4 | 14.5 | 23.4 | 19.4 | 10.0 | 16.59 | 52.8% | 29.4% |
| WTA | 435 | 23.4 | 14.0 | 29.4 | 15.6 | 11.5 | 4.4 | 1.6 | 6.99 | 17.5% | 6.0% |
| WTA125 | 91 | 16.5 | 5.5 | 24.2 | 29.7 | 13.2 | 9.9 | 1.1 | 10.92 | 24.2% | 11.0% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 919 | 21.4 | 14.7 | 25.4 | 15.2 | 14.5 | 6.2 | 2.6 | 7.39 | 23.3% | 8.8% |
| DOUBLES | 384 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.8 | 27.3 | 24.07 | 70.0% | 48.2% |
| ITF_MEN | 2,081 | 14.0 | 9.2 | 18.9 | 14.1 | 20.8 | 13.5 | 9.5 | 12.43 | 43.8% | 23.0% |
| ITF_WOMEN | 2,008 | 8.8 | 8.2 | 17.2 | 14.3 | 23.8 | 18.8 | 8.9 | 15.6 | 51.4% | 27.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 340 | 13.2 | 10.0 | 21.5 | 16.8 | 22.6 | 12.1 | 3.8 | 11.33 | 38.5% | 15.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 263 | 20.9 | 16.4 | 27.0 | 12.9 | 15.2 | 3.4 | 4.2 | 6.77 | 22.8% | 7.6% |
| CHALLENGER | 857 | 19.5 | 13.3 | 19.6 | 18.7 | 16.1 | 8.6 | 4.2 | 9.32 | 28.9% | 12.8% |
| ITF_MEN | 1,072 | 15.8 | 11.8 | 24.9 | 16.6 | 17.5 | 9.3 | 4.0 | 9.45 | 30.9% | 13.3% |
| ITF_WOMEN | 1,370 | 13.5 | 7.7 | 18.6 | 17.7 | 22.4 | 15.3 | 4.7 | 12.91 | 42.4% | 20.0% |
| WTA | 434 | 23.0 | 10.6 | 25.8 | 12.7 | 18.9 | 6.5 | 2.5 | 8.16 | 27.9% | 9.0% |
| WTA125 | 88 | 13.6 | 4.5 | 18.2 | 27.3 | 18.2 | 12.5 | 5.7 | 11.65 | 36.4% | 18.2% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 263 | 21.7 | 12.6 | 25.1 | 15.2 | 17.9 | 3.0 | 4.6 | 7.75 | 25.5% | 7.6% |
| CHALLENGER | 857 | 16.7 | 7.8 | 23.2 | 17.7 | 18.8 | 12.4 | 3.4 | 10.68 | 34.5% | 15.8% |
| ITF_MEN | 1,072 | 13.0 | 8.7 | 21.8 | 17.6 | 21.3 | 12.2 | 5.4 | 11.65 | 38.9% | 17.6% |
| ITF_WOMEN | 1,370 | 9.8 | 8.2 | 14.7 | 11.7 | 24.1 | 18.3 | 13.1 | 17.11 | 55.5% | 31.5% |
| WTA | 434 | 20.5 | 5.5 | 16.8 | 15.7 | 22.4 | 16.6 | 2.5 | 12.96 | 41.5% | 19.1% |
| WTA125 | 88 | 5.7 | 5.7 | 14.8 | 20.4 | 26.1 | 15.9 | 11.4 | 16.39 | 53.4% | 27.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 763 | 23.6 | 17.0 | 27.8 | 14.8 | 13.9 | 2.6 | 0.3 | 6.68 | 16.8% | 2.9% |
| DOUBLES | 345 | 5.8 | 3.8 | 10.1 | 10.4 | 21.7 | 21.2 | 27.0 | 24.1 | 69.9% | 48.1% |
| ITF_MEN | 1,480 | 17.1 | 11.2 | 22.1 | 15.3 | 20.7 | 9.9 | 3.6 | 9.92 | 34.3% | 13.6% |
| ITF_WOMEN | 1,383 | 10.6 | 9.7 | 20.7 | 16.5 | 24.7 | 15.5 | 2.3 | 12.3 | 42.5% | 17.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 334 | 15.6 | 9.9 | 26.4 | 23.1 | 18.3 | 6.9 | 0.0 | 9.55 | 25.1% | 6.9% |
| WTA125 | 262 | 15.7 | 11.1 | 25.6 | 19.9 | 21.0 | 6.5 | 0.4 | 9.43 | 27.9% | 6.9% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 384 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.8 | 27.3 | 24.07 | 70.0% | 48.2% |
| singles | 5,932 | 13.7 | 10.0 | 20.5 | 15.0 | 20.4 | 13.4 | 7.1 | 11.75 | 40.9% | 20.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,253 | 15.4 | 9.1 | 19.7 | 14.8 | 15.7 | 12.9 | 12.3 | 11.7 | 40.9% | 25.2% |
| Hard | 3,938 | 12.7 | 8.6 | 18.4 | 15.0 | 19.4 | 15.7 | 10.2 | 13.32 | 45.3% | 25.9% |
| UNKNOWN | 408 | 13.7 | 5.9 | 15.4 | 19.6 | 17.9 | 17.2 | 10.3 | 13.46 | 45.3% | 27.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,700 | 17.2 | 10.2 | 20.9 | 15.0 | 16.7 | 11.7 | 8.4 | 10.43 | 36.8% | 20.1% |
| B | 862 | 16.2 | 10.6 | 17.2 | 18.0 | 16.4 | 10.4 | 11.2 | 11.47 | 38.0% | 21.7% |
| C | 904 | 12.9 | 8.8 | 22.2 | 13.1 | 16.3 | 15.5 | 11.2 | 12.55 | 42.9% | 26.7% |
| D | 1,001 | 11.5 | 8.3 | 17.0 | 14.4 | 20.7 | 15.7 | 12.5 | 14.44 | 48.9% | 28.2% |
| F | 1,132 | 7.6 | 4.3 | 14.2 | 16.2 | 22.4 | 23.5 | 11.7 | 18.33 | 57.6% | 35.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,928 | 18.8 | 12.3 | 25.6 | 16.7 | 16.6 | 6.9 | 3.1 | 8.66 | 26.6% | 10.0% |
| B | 1,050 | 13.5 | 9.8 | 21.4 | 15.5 | 19.9 | 12.4 | 7.4 | 11.66 | 39.7% | 19.8% |
| C | 1,274 | 11.2 | 8.7 | 15.5 | 14.1 | 22.1 | 15.3 | 13.1 | 15.18 | 50.5% | 28.4% |
| D | 964 | 11.7 | 8.3 | 20.5 | 11.8 | 24.0 | 15.2 | 8.5 | 13.91 | 47.6% | 23.6% |
| F | 1,100 | 6.7 | 7.0 | 12.6 | 13.6 | 22.8 | 24.6 | 12.6 | 18.91 | 60.1% | 37.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 2,133 | 16.6 | 9.6 | 19.6 | 16.0 | 16.6 | 11.7 | 9.7 | 10.98 | 38.1% | 21.4% |
| LIMITED | 1,315 | 14.4 | 10.6 | 21.6 | 13.9 | 15.9 | 13.4 | 10.2 | 11.21 | 39.5% | 23.6% |
| POOR | 2,151 | 9.5 | 6.1 | 15.4 | 15.4 | 21.8 | 19.8 | 11.9 | 16.55 | 53.5% | 31.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 341 | 34.3 | 22.9 | 33.1 | 6.5 | 2.4 | 0.9 | 0.0 | 4.16 | 3.2% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 6,316 | 13.2 | 9.6 | 19.8 | 14.7 | 20.5 | 13.8 | 8.3 | 12.21 | 42.6% | 22.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,702 | 21.7 | 13.4 | 30.6 | 17.2 | 13.6 | 2.8 | 0.7 | 7.04 | 17.0% | 3.4% |
| TOTAL_GAMES | 1,132 | 9.9 | 9.4 | 26.5 | 24.9 | 17.0 | 8.0 | 4.4 | 10.66 | 29.3% | 12.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 975 | 26.1 | 29.6 | 24.4 | 0.6 | 17.3 | 1.5 | 0.4 | 4.63 | 19.3% | 1.9% |
| GAME_SPREAD | 565 | 36.6 | 15.0 | 25.3 | 17.9 | 2.5 | 1.9 | 0.7 | 4.55 | 5.1% | 2.6% |
| TOTAL_GAMES | 1,364 | 4.5 | 4.5 | 33.1 | 41.3 | 10.3 | 3.1 | 3.2 | 10.72 | 16.6% | 6.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 975 | 24.2 | 15.3 | 30.9 | 7.7 | 13.5 | 7.1 | 1.3 | 6.11 | 21.9% | 8.4% |
| GAME_SPREAD | 565 | 17.5 | 10.3 | 25.5 | 23.2 | 15.9 | 5.1 | 2.5 | 9.56 | 23.5% | 7.6% |
| TOTAL_GAMES | 1,373 | 5.8 | 7.0 | 29.4 | 29.9 | 17.0 | 6.3 | 4.4 | 10.91 | 27.8% | 10.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5,599 | 44.3% | 25.9% | 12.95 | 33.6% | 14.7% | 10.11 |
| gen1_elo | 5,599 | 43.3% | 25.1% | 12.47 | 32.1% | 14.6% | 9.53 |
| gen1_sr | 5,599 | 52.9% | 30.8% | 16.15 | 43.5% | 20.0% | 12.95 |
| gen2 | 5,599 | 51.2% | 30.9% | 15.55 | 43.3% | 21.6% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 2,040 | 17.6 | 12.0 | 22.9 | 15.8 | 18.4 | 10.1 | 3.3 | 9.48 | 31.8% | 13.4% |
| STALE | 3,559 | 11.0 | 6.5 | 16.0 | 15.0 | 18.5 | 18.1 | 14.9 | 15.89 | 51.5% | 33.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,334 | 15.2 | 10.5 | 21.8 | 15.9 | 20.0 | 12.0 | 4.6 | 10.71 | 36.7% | 16.7% |
| STALE | 2,982 | 11.0 | 8.7 | 17.7 | 13.3 | 20.9 | 15.9 | 12.5 | 14.73 | 49.3% | 28.4% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 11,915 | 0 | 5374 | 6541 | 31.9 | 206.8 | 1400.4 |
| ge_15pp | 5,175 | 0 | 1871 | 3304 | 39.7 | 488.1 | 1380.4 |
| ge_25pp | 2,850 | 0 | 828 | 2022 | 53.6 | 619.8 | 1380.4 |
| lt_10pp | 4,956 | 0 | 2651 | 2305 | 29.1 | 55.8 | 1201.9 |

Current slate `SL-20261004T111532Z-04ee27c2`: 296 priced rows, quote age at build {'median': 64.3, 'max': 64.4}, freshness {'STALE': 296}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 158 | 21.5 | 12.0 | 20.2 | 20.9 | 19.0 | 5.1 | 1.3 | 7.76 | 25.3% | 6.3% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 8.3 | 50.0 | 41.7 | 0.0 | 0.0 | 14.32 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 5,599 | 179 (3.2%) | 6.7% | 0.0% | {"EXTERNAL_STALE": 158, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,482 | 45 (1.8%) | 11.1% | 0.0% | {"EXTERNAL_STALE": 40, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,449 | 10 (0.7%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 10} |
| fair_v1_ge_25pp_pregame_clean | 602 | 10 (1.7%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 10} |
| fair_v1_lt_10pp | 2,261 | 95 (4.2%) | 1.1% | 0.0% | {"EXTERNAL_STALE": 85, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,127 | 12.9 | 7.2 | 19.2 | 16.1 | 19.9 | 15.3 | 9.5 | 12.94 | 44.6% | 24.8% |
| 4-10x | 734 | 12.3 | 10.2 | 17.4 | 14.8 | 17.7 | 16.1 | 11.4 | 13.62 | 45.2% | 27.5% |
| <2x | 3,030 | 14.5 | 9.3 | 19.3 | 15.1 | 17.8 | 13.2 | 10.8 | 12.09 | 41.8% | 24.0% |
| >=10x | 708 | 10.7 | 5.4 | 14.8 | 15.2 | 19.9 | 22.7 | 11.2 | 16.77 | 53.8% | 33.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,588 | 14.4 | 8.9 | 20.6 | 15.9 | 16.8 | 12.0 | 11.4 | 11.64 | 40.2% | 23.4% |
| 300-1000 | 1,315 | 13.4 | 8.3 | 16.4 | 15.6 | 19.9 | 15.8 | 10.7 | 13.97 | 46.3% | 26.5% |
| <300 | 1,350 | 8.5 | 5.6 | 15.0 | 14.6 | 21.5 | 22.4 | 12.4 | 18.17 | 56.3% | 34.8% |
| >=3000 | 1,346 | 17.2 | 11.2 | 21.5 | 14.9 | 16.0 | 11.1 | 8.2 | 10.02 | 35.2% | 19.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 204 | 0.5154 | 0.3834 | 0.4216 | +0.094 | -0.038 | 0.0109 ± 0.0101 |
| ratio 4-10x | 146 | 0.5827 | 0.4436 | 0.4863 | +0.096 | -0.043 | 0.0114 ± 0.0124 |
| ratio <2x | 423 | 0.5357 | 0.4165 | 0.4681 | +0.068 | -0.052 | 0.0104 ± 0.0067 |
| ratio >=10x | 146 | 0.5586 | 0.394 | 0.4726 | +0.086 | -0.079 | 0.0142 ± 0.0154 |
| thinner_sample 1000-3000 | 248 | 0.5394 | 0.4198 | 0.4637 | +0.076 | -0.044 | 0.0072 ± 0.0089 |
| thinner_sample 300-1000 | 261 | 0.555 | 0.425 | 0.4713 | +0.084 | -0.046 | 0.0044 ± 0.009 |
| thinner_sample <300 | 287 | 0.5432 | 0.3817 | 0.453 | +0.090 | -0.071 | 0.0197 ± 0.0103 |
| thinner_sample >=3000 | 123 | 0.5193 | 0.4236 | 0.4553 | +0.064 | -0.032 | 0.0145 ± 0.01 |
| data_status ADEQUATE | 268 | 0.527 | 0.4185 | 0.459 | +0.068 | -0.040 | 0.0062 ± 0.0077 |
| data_status LIMITED | 200 | 0.559 | 0.4356 | 0.5 | +0.059 | -0.064 | 0.0016 ± 0.0104 |
| data_status POOR | 451 | 0.544 | 0.3933 | 0.4457 | +0.098 | -0.052 | 0.0185 ± 0.0077 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 152 | 0.1781 | 0.1791 | -0.0011 ± 0.0012 | 0.5302 | 0.5333 | 0.4936 | 0.4791 | 0.5 | -0.082 ± 0.0373 | -0.01 (3) |
| 3-5 | 94 | 0.1737 | 0.1733 | +0.0004 ± 0.0036 | 0.5274 | 0.5222 | 0.5264 | 0.4853 | 0.5 | -0.077 ± 0.0459 | 0.02 (1) |
| 5-10 | 193 | 0.1991 | 0.2029 | -0.0038 ± 0.0049 | 0.5835 | 0.5917 | 0.5107 | 0.4359 | 0.4922 | -0.047 ± 0.0326 | -0.0167 (3) |
| 10-15 | 156 | 0.217 | 0.2096 | +0.0074 ± 0.0091 | 0.6176 | 0.6014 | 0.5209 | 0.397 | 0.4295 | -0.074 ± 0.0365 | -0.0633 (3) |
| 15-25 | 199 | 0.2129 | 0.21 | +0.0028 ± 0.0127 | 0.6127 | 0.6011 | 0.5657 | 0.3691 | 0.4623 | -0.024 ± 0.0319 | -0.02 (4) |
| 25-40 | 98 | 0.2321 | 0.1873 | +0.0448 ± 0.027 | 0.654 | 0.5484 | 0.6307 | 0.3167 | 0.398 | -0.071 ± 0.0411 | -0.01 (1) |
| 40+ | 27 | 0.338 | 0.1489 | +0.1891 ± 0.067 | 0.9165 | 0.4615 | 0.7278 | 0.2846 | 0.2963 | -0.169 ± 0.0729 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 485 | 0.1609 | 0.1622 | -0.0013 ± 0.0006 | 0.488 | 0.4911 | 0.5045 | 0.4898 | 0.534 | -0.015 ± 0.0191 | -0.0188 (8) |
| 3-5 | 293 | 0.1767 | 0.1775 | -0.0008 ± 0.002 | 0.5335 | 0.5303 | 0.4938 | 0.4537 | 0.4846 | -0.026 ± 0.0253 | 0.02 (1) |
| 5-10 | 678 | 0.1826 | 0.1817 | +0.0009 ± 0.0024 | 0.5448 | 0.5402 | 0.4729 | 0.399 | 0.4307 | -0.026 ± 0.0165 | -0.0129 (7) |
| 10-15 | 574 | 0.1918 | 0.175 | +0.0167 ± 0.0043 | 0.5644 | 0.5145 | 0.4731 | 0.3496 | 0.3432 | -0.067 ± 0.0174 | -0.0633 (3) |
| 15-25 | 743 | 0.1964 | 0.1611 | +0.0352 ± 0.0059 | 0.5818 | 0.477 | 0.4862 | 0.2882 | 0.2961 | -0.051 ± 0.0146 | -0.017 (10) |
| 25-40 | 671 | 0.2107 | 0.096 | +0.1147 ± 0.0075 | 0.6135 | 0.3126 | 0.505 | 0.1901 | 0.1684 | -0.071 ± 0.0117 | -0.01 (1) |
| 40+ | 494 | 0.3752 | 0.0344 | +0.3408 ± 0.0091 | 0.9761 | 0.149 | 0.6206 | 0.1043 | 0.0425 | -0.093 ± 0.0077 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 92 | 0.1787 | 0.1804 | -0.0017 ± 0.0015 | 0.5312 | 0.5339 | 0.5283 | 0.5135 | 0.5652 | -0.040 ± 0.0436 | -0.01 (1) |
| 3-5 | 72 | 0.2036 | 0.2011 | +0.0025 ± 0.0043 | 0.5867 | 0.5869 | 0.4884 | 0.4493 | 0.4306 | -0.090 ± 0.0554 | 0.02 (1) |
| 5-10 | 182 | 0.1866 | 0.1851 | +0.0015 ± 0.0049 | 0.555 | 0.5504 | 0.5712 | 0.4957 | 0.5165 | -0.080 ± 0.0325 | -0.01 (4) |
| 10-15 | 159 | 0.2236 | 0.2094 | +0.0142 ± 0.0093 | 0.6354 | 0.6046 | 0.5766 | 0.4517 | 0.4654 | -0.090 ± 0.0378 | -0.0667 (3) |
| 15-25 | 226 | 0.2231 | 0.1978 | +0.0253 ± 0.0117 | 0.6321 | 0.5718 | 0.5867 | 0.3895 | 0.4292 | -0.085 ± 0.0303 | -0.0167 (3) |
| 25-40 | 132 | 0.2565 | 0.1986 | +0.0579 ± 0.0241 | 0.7171 | 0.5736 | 0.6604 | 0.3492 | 0.4091 | -0.095 ± 0.0401 | -0.025 (2) |
| 40+ | 56 | 0.3813 | 0.1952 | +0.1861 ± 0.0597 | 1.0592 | 0.5753 | 0.7595 | 0.2663 | 0.3393 | -0.059 ± 0.0579 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 381 | 0.1556 | 0.1576 | -0.0021 ± 0.0007 | 0.4722 | 0.4773 | 0.5412 | 0.5265 | 0.5827 | +0.006 ± 0.0205 | -0.0217 (6) |
| 3-5 | 247 | 0.1685 | 0.1661 | +0.0024 ± 0.0021 | 0.5055 | 0.5042 | 0.5348 | 0.4953 | 0.4818 | -0.062 ± 0.0261 | 0.02 (1) |
| 5-10 | 623 | 0.1765 | 0.1779 | -0.0014 ± 0.0026 | 0.5285 | 0.5286 | 0.5241 | 0.4486 | 0.4912 | -0.013 ± 0.017 | -0.01 (5) |
| 10-15 | 547 | 0.1895 | 0.1755 | +0.0140 ± 0.0045 | 0.562 | 0.5182 | 0.5122 | 0.3879 | 0.4022 | -0.045 ± 0.0182 | -0.0575 (4) |
| 15-25 | 801 | 0.2068 | 0.1593 | +0.0475 ± 0.0056 | 0.6031 | 0.4756 | 0.5156 | 0.3193 | 0.3009 | -0.084 ± 0.0141 | -0.0143 (7) |
| 25-40 | 709 | 0.2274 | 0.1196 | +0.1078 ± 0.0083 | 0.6585 | 0.3696 | 0.5466 | 0.231 | 0.22 | -0.068 ± 0.0132 | -0.015 (6) |
| 40+ | 630 | 0.4097 | 0.0576 | +0.3521 ± 0.0112 | 1.0758 | 0.2124 | 0.6645 | 0.123 | 0.0825 | -0.074 ± 0.0091 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 148 | 0.1849 | 0.1865 | -0.0016 ± 0.0013 | 0.5427 | 0.5475 | 0.5149 | 0.5005 | 0.527 | -0.054 ± 0.0357 | -0.01 (5) |
| 3-5 | 102 | 0.1717 | 0.1691 | +0.0025 ± 0.0033 | 0.5172 | 0.5112 | 0.5011 | 0.4618 | 0.451 | -0.116 ± 0.0436 | -- (0) |
| 5-10 | 188 | 0.2044 | 0.2045 | -0.0002 ± 0.0049 | 0.5998 | 0.5941 | 0.5022 | 0.4295 | 0.4628 | -0.065 ± 0.0333 | -0.01 (3) |
| 10-15 | 157 | 0.2075 | 0.2037 | +0.0038 ± 0.009 | 0.6006 | 0.5881 | 0.5466 | 0.4231 | 0.4777 | -0.065 ± 0.0363 | -0.044 (5) |
| 15-25 | 194 | 0.2094 | 0.2013 | +0.0082 ± 0.0125 | 0.6088 | 0.5829 | 0.5781 | 0.385 | 0.4588 | -0.043 ± 0.031 | -0.03 (1) |
| 25-40 | 109 | 0.2265 | 0.2003 | +0.0262 ± 0.0262 | 0.6443 | 0.5806 | 0.6235 | 0.3099 | 0.422 | -0.047 ± 0.0396 | 0.0 (1) |
| 40+ | 21 | 0.3707 | 0.1604 | +0.2102 ± 0.0791 | 0.9917 | 0.4892 | 0.7365 | 0.2879 | 0.2857 | -0.191 ± 0.0908 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 472 | 0.1685 | 0.1685 | -0.0000 ± 0.0006 | 0.5063 | 0.5071 | 0.5095 | 0.495 | 0.4979 | -0.053 ± 0.019 | -0.0162 (13) |
| 3-5 | 320 | 0.1793 | 0.1753 | +0.0040 ± 0.0019 | 0.5343 | 0.5242 | 0.488 | 0.4489 | 0.425 | -0.084 ± 0.024 | -0.01 (2) |
| 5-10 | 675 | 0.1873 | 0.1814 | +0.0059 ± 0.0025 | 0.5577 | 0.5331 | 0.4612 | 0.3876 | 0.3867 | -0.056 ± 0.0165 | -0.01 (3) |
| 10-15 | 568 | 0.1878 | 0.1729 | +0.0149 ± 0.0043 | 0.5567 | 0.5138 | 0.4847 | 0.3612 | 0.3644 | -0.059 ± 0.0175 | -0.03 (9) |
| 15-25 | 783 | 0.1864 | 0.1516 | +0.0349 ± 0.0056 | 0.5618 | 0.4555 | 0.4936 | 0.2947 | 0.3052 | -0.046 ± 0.0136 | -0.03 (2) |
| 25-40 | 659 | 0.2117 | 0.0993 | +0.1124 ± 0.0077 | 0.6153 | 0.3189 | 0.5017 | 0.1839 | 0.1684 | -0.069 ± 0.0118 | 0.0 (1) |
| 40+ | 461 | 0.3907 | 0.0335 | +0.3572 ± 0.0095 | 1.0195 | 0.1476 | 0.6247 | 0.1025 | 0.0325 | -0.100 ± 0.0079 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 430 | 0.2026 | 0.2025 | +0.0001 ± 0.0007 | 0.587 | 0.5871 | 0.4959 | 0.4812 | 0.4814 | -0.042 ± 0.0218 | -0.0226 (46) |
| 3-5 | 315 | 0.1943 | 0.1933 | +0.0010 ± 0.002 | 0.5702 | 0.5649 | 0.4656 | 0.4259 | 0.4381 | -0.036 ± 0.0246 | -0.0059 (32) |
| 5-10 | 651 | 0.1883 | 0.1836 | +0.0047 ± 0.0025 | 0.56 | 0.547 | 0.4603 | 0.3869 | 0.3932 | -0.039 ± 0.0168 | -0.005 (72) |
| 10-15 | 436 | 0.2039 | 0.1917 | +0.0122 ± 0.0053 | 0.5972 | 0.5626 | 0.4577 | 0.3342 | 0.3463 | -0.038 ± 0.0209 | 0.0016 (63) |
| 15-25 | 583 | 0.2336 | 0.2096 | +0.0240 ± 0.0074 | 0.6608 | 0.6056 | 0.5306 | 0.3376 | 0.3722 | -0.028 ± 0.0189 | -0.0216 (58) |
| 25-40 | 280 | 0.2676 | 0.1703 | +0.0974 ± 0.0154 | 0.7399 | 0.5106 | 0.577 | 0.2657 | 0.2643 | -0.066 ± 0.0243 | -0.0216 (25) |
| 40+ | 94 | 0.4254 | 0.1611 | +0.2643 ± 0.0443 | 1.1952 | 0.4956 | 0.7368 | 0.2289 | 0.2447 | -0.060 ± 0.0429 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 799 | 0.1912 | 0.1906 | +0.0006 ± 0.0005 | 0.56 | 0.5582 | 0.4894 | 0.4748 | 0.4606 | -0.055 ± 0.0154 | -0.0155 (82) |
| 3-5 | 570 | 0.1975 | 0.1958 | +0.0016 ± 0.0015 | 0.5753 | 0.5689 | 0.4701 | 0.4304 | 0.4316 | -0.043 ± 0.0186 | -0.018 (54) |
| 5-10 | 1192 | 0.1871 | 0.1806 | +0.0064 ± 0.0018 | 0.557 | 0.5376 | 0.4454 | 0.3714 | 0.3691 | -0.043 ± 0.0124 | -0.0089 (122) |
| 10-15 | 881 | 0.1982 | 0.1841 | +0.0141 ± 0.0036 | 0.5829 | 0.543 | 0.4491 | 0.3256 | 0.3303 | -0.040 ± 0.0143 | -0.0053 (99) |
| 15-25 | 1230 | 0.2211 | 0.1869 | +0.0342 ± 0.0048 | 0.6378 | 0.5484 | 0.5042 | 0.3086 | 0.3187 | -0.041 ± 0.0124 | -0.0255 (106) |
| 25-40 | 845 | 0.244 | 0.1272 | +0.1168 ± 0.0077 | 0.689 | 0.398 | 0.5283 | 0.2128 | 0.187 | -0.071 ± 0.0121 | -0.0206 (47) |
| 40+ | 499 | 0.3888 | 0.0779 | +0.3109 ± 0.0137 | 1.0618 | 0.2629 | 0.6519 | 0.1363 | 0.1042 | -0.075 ± 0.0127 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 919 | 1.106 ± 0.093 | 1.228 | 0.173 | 0.1823 | 0.2066 | 0.1954 |
| gen2 | 919 | 0.921 ± 0.082 | 1.148 | 0.1896 | 0.1814 | 0.2244 | 0.1958 |
| gen1_elo | 919 | 1.096 ± 0.091 | 1.2 | 0.1777 | 0.1826 | 0.2056 | 0.1954 |
| gen1_sr | 919 | 1.139 ± 0.107 | 1.214 | 0.1449 | 0.1837 | 0.2198 | 0.1953 |
| gen1_ledger | 2789 | 0.888 ± 0.051 | 1.06 | 0.163 | 0.1999 | 0.219 | 0.1922 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 5,175)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,686 | 32.6% |
| STALE_QUOTE | market_freshness | 1,616 | 31.2% |
| POOR_DATA | data | 397 | 7.7% |
| BOOK_QUALITY | execution | 337 | 6.5% |
| LIMITED_DATA | data | 315 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 291 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 252 | 4.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 175 | 3.4% |
| IDENTITY_AMBIGUOUS | mapping | 103 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 32.6%, market_freshness 31.2%, data 13.8%, market_freshness/coverage 9.0%, execution 6.5%, model_calibration_or_unknown 4.9%, mapping 2.0%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.5%, STALE_KALSHI_QUOTE 63.8%, LOW_DATA_QUALITY 63.6%, STALE_PLAYER_DATA 54.1%, THIN_PLAYER_HISTORY 51.8%, MODEL_INTERNAL_DISAGREEMENT 33.7%, ASYMMETRIC_SAMPLE_SIZE 28.9%, WIDE_SPREAD 14.7%, MODEL_HIGH_UNCERTAINTY 14.3%, PLAYER_IDENTITY_RISK 10.9%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 6.3%, LOW_DISPLAYED_LIQUIDITY 5.1%, MODEL_CALIBRATION_OUTLIER 2.1%, UNKNOWN 0.7%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 35.1%, POST_SETTLEMENT_OBSERVATION 32.6%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 1.1%

### >= ge_25 pp (N = 2,850)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,312 | 46.0% |
| STALE_QUOTE | market_freshness | 735 | 25.8% |
| POOR_DATA | data | 168 | 5.9% |
| BOOK_QUALITY | execution | 165 | 5.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 148 | 5.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 102 | 3.6% |
| LIMITED_DATA | data | 85 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 75 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 60 | 2.1% |

Cause class: coverage 46.0%, market_freshness 25.8%, data 8.9%, market_freshness/coverage 8.8%, execution 5.8%, mapping 2.6%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.7%, STALE_KALSHI_QUOTE 71.0%, LOW_DATA_QUALITY 67.4%, THIN_PLAYER_HISTORY 54.2%, STALE_PLAYER_DATA 51.9%, MODEL_INTERNAL_DISAGREEMENT 34.9%, ASYMMETRIC_SAMPLE_SIZE 31.4%, MODEL_HIGH_UNCERTAINTY 15.7%, PLAYER_IDENTITY_RISK 13.8%, WIDE_SPREAD 13.7%, LEVEL_TRANSFER_RISK 8.1%, EVENT_MAPPING_RISK 7.6%, LOW_DISPLAYED_LIQUIDITY 5.7%, MODEL_CALIBRATION_OUTLIER 3.0%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 48.7%, POST_SETTLEMENT_OBSERVATION 46.0%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 1.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2425, "IDENTITY_AMBIGUOUS": 425}; ticker orientation: {"VERIFIED": 2850}.

Checks: discipline:AMBIGUOUS 185, discipline:PASS 2665, identity_confidence:AMBIGUOUS 393, identity_confidence:PASS 2457, level_mapping:NA 197, level_mapping:PASS 2653, market_pair:AMBIGUOUS 62, market_pair:NA 77, market_pair:PASS 2711, model_complement:NA 48, model_complement:PASS 2802, namesake:PASS 2850, physical_match_id:NA 1401, physical_match_id:PASS 1449, player_ids:PASS 2850, same_pair_other_event:PASS 2850, ticker_orientation:PASS 2850

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 336 | 5.9% | 6.2% | 0.7% | {"market_freshness": 19, "execution": 1} | 6.47 | 0.1791 / 0.1823 (49) | 43.1% | 0.0% | 0.6% | 3.3% |
| CHALLENGER | 2,032 | 17.8% | 8.2% | 12.7% | {"coverage": 188, "market_freshness": 94, "market_freshness/coverage": 41, "data": 20, "model_calibration_or_unknown": 14, "execution": 4} | 7.54 | 0.2226 / 0.2072 (567) | 56.0% | 4.9% | 1.1% | 20.3% |
| DOUBLES | 384 | 48.2% | 48.1% | 6.5% | {"market_freshness": 106, "execution": 32, "mapping": 28, "market_freshness/coverage": 12, "coverage": 7} | 24.1 | 0.3208 / 0.2301 (163) | 60.9% | 0.0% | 100.0% | 10.2% |
| ITF_MEN | 3,781 | 24.9% | 13.5% | 33.1% | {"coverage": 527, "market_freshness": 171, "data": 88, "execution": 74, "market_freshness/coverage": 72, "mapping": 10, "model_calibration_or_unknown": 1} | 9.74 | 0.2132 / 0.1882 (1338) | 55.7% | 49.0% | 5.1% | 32.5% |
| ITF_WOMEN | 4,004 | 29.5% | 18.9% | 41.5% | {"coverage": 577, "market_freshness": 295, "data": 126, "market_freshness/coverage": 85, "execution": 45, "mapping": 35, "model_calibration_or_unknown": 19} | 12.62 | 0.2056 / 0.1862 (1201) | 59.9% | 55.9% | 7.7% | 31.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.4% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 798 | 9.4% | 8.1% | 2.6% | {"market_freshness": 34, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.66 | 0.2006 / 0.1964 (129) | 40.5% | 2.6% | 1.5% | 3.8% |
| WTA125 | 431 | 16.7% | 9.7% | 2.5% | {"market_freshness/coverage": 30, "market_freshness": 14, "model_calibration_or_unknown": 12, "data": 8, "coverage": 8} | 10.27 | 0.2261 / 0.2035 (219) | 35.3% | 8.8% | 0.5% | 18.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 5 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 6 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 9 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 11 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 12 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 14 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 15 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 16 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 17 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 18 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 19 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 20 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 22 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 23 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 24 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 25 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 26 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 27 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 256 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 28 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 29 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 30 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 31 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 32 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 4% | +71 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 38 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 33 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 36 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 37 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 39 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 183 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 40 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 41 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 43 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 45 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 776 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 46 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 47 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 48 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 49 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 50 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 220 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9667, "by_level_share_of_ge_25pp": {"ATP": 0.007, "CHALLENGER": 0.1267, "DOUBLES": 0.0649, "ITF_MEN": 0.3309, "ITF_WOMEN": 0.4147, "OTHER": 0.0042, "WTA": 0.0263, "WTA125": 0.0253}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.7095, "share_primary_cause_market_settled_or_in_play": 0.5481, "share_primary_cause_stale_quote_only": 0.2579}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2850, "identity_ambiguous_share": 0.1491, "ticker_orientation": {"VERIFIED": 2850}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1449, "with_external": 10, "coverage": 0.0069, "external_status": {"EXTERNAL_STALE": 10}, "triangulation": {"INSUFFICIENT_INPUTS": 10}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 602, "with_external": 10, "coverage": 0.0166, "external_status": {"EXTERNAL_STALE": 10}, "triangulation": {"INSUFFICIENT_INPUTS": 10}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 824.0, "median_sample_ratio": 2.31, "median_min_matches": 28.0, "median_max_days_since_last": 173.0, "share_severe_asymmetry": 0.1789, "data_status": {"POOR": 1331, "LIMITED": 951, "ADEQUATE": 568}, "comparison_lt_10pp": {"median_thinner_serve_points": 1948.0, "median_sample_ratio": 1.74, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 204, "model_minus_observed": 0.0939, "kalshi_minus_observed": -0.0382, "brier_diff_model_minus_kalshi": 0.0109}, "4-10x": {"n": 146, "model_minus_observed": 0.0964, "kalshi_minus_observed": -0.0427, "brier_diff_model_minus_kalshi": 0.0114}, "<2x": {"n": 423, "model_minus_observed": 0.0676, "kalshi_minus_observed": -0.0516, "brier_diff_model_minus_kalshi": 0.0104}, ">=10x": {"n": 146, "model_minus_observed": 0.086, "kalshi_minus_observed": -0.0786, "brier_diff_model_minus_kalshi": 0.0142}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 919, "model": {"intercept": -0.614, "slope": 0.921, "slope_se": 0.082}, "kalshi_mid_same_rows": {"intercept": 0.205, "slope": 1.148, "slope_se": 0.092}, "mean_extremity_model": 0.1896, "mean_extremity_kalshi": 0.1814, "model_brier": 0.2244, "kalshi_brier": 0.1958, "brier_diff_model_minus_kalshi": 0.0287, "brier_diff_se": 0.0062, "model_logloss": 0.642, "kalshi_logloss": 0.5711}, "fair_v1": {"n": 919, "model": {"intercept": -0.407, "slope": 1.106, "slope_se": 0.093}, "kalshi_mid_same_rows": {"intercept": 0.347, "slope": 1.228, "slope_se": 0.096}, "mean_extremity_model": 0.173, "mean_extremity_kalshi": 0.1823, "model_brier": 0.2066, "kalshi_brier": 0.1954, "brier_diff_model_minus_kalshi": 0.0113, "brier_diff_se": 0.0049, "model_logloss": 0.5984, "kalshi_logloss": 0.5702}, "gen1_elo": {"n": 919, "model": {"intercept": -0.419, "slope": 1.096, "slope_se": 0.091}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.2, "slope_se": 0.094}, "mean_extremity_model": 0.1777, "mean_extremity_kalshi": 0.1826, "model_brier": 0.2056, "kalshi_brier": 0.1954, "brier_diff_model_minus_kalshi": 0.0103, "brier_diff_se": 0.0049, "model_logloss": 0.5977, "kalshi_logloss": 0.57}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2588, "share_ge_15": 0.4433, "median_abs_gap": 12.95, "n": 5599}, "gen1_elo": {"share_ge_25": 0.2508, "share_ge_15": 0.4329, "median_abs_gap": 12.47, "n": 5599}, "gen1_sr": {"share_ge_25": 0.3077, "share_ge_15": 0.5292, "median_abs_gap": 16.15, "n": 5599}, "gen2": {"share_ge_25": 0.3095, "share_ge_15": 0.5121, "median_abs_gap": 15.55, "n": 5599}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1474, "share_ge_15": 0.3362, "median_abs_gap": 10.11, "n": 4084}, "gen1_elo": {"share_ge_25": 0.1462, "share_ge_15": 0.321, "median_abs_gap": 9.53, "n": 4084}, "gen1_sr": {"share_ge_25": 0.1996, "share_ge_15": 0.4346, "median_abs_gap": 12.95, "n": 4084}, "gen2": {"share_ge_25": 0.216, "share_ge_15": 0.4329, "median_abs_gap": 12.83, "n": 4084}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.47, "share_ge_25_all": 0.0595, "share_ge_25_pregame_clean": 0.0615}, "WTA": {"median_abs_gap_pregame_clean": 8.66, "share_ge_25_all": 0.094, "share_ge_25_pregame_clean": 0.0807}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2239, "share_within_10pp_all": 0.4159, "share_within_10pp_pregame_clean": 0.494, "corr_model_vs_mid_pregame_clean": 0.8299}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 152, "model_brier": 0.1781, "kalshi_brier": 0.1791, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 156, "model_brier": 0.217, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.0074}, "15-25": {"n_settled": 199, "model_brier": 0.2129, "kalshi_brier": 0.21, "brier_diff_model_minus_kalshi": 0.0028}, "25-40": {"n_settled": 98, "model_brier": 0.2321, "kalshi_brier": 0.1873, "brier_diff_model_minus_kalshi": 0.0448}, "3-5": {"n_settled": 94, "model_brier": 0.1737, "kalshi_brier": 0.1733, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 27, "model_brier": 0.338, "kalshi_brier": 0.1489, "brier_diff_model_minus_kalshi": 0.1891}, "5-10": {"n_settled": 193, "model_brier": 0.1991, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": -0.0038}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.557, "slope": 0.888, "slope_se": 0.051}, "kalshi_slope": {"intercept": 0.093, "slope": 1.06, "slope_se": 0.052}, "n": 2789}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 163, "model_brier": 0.3208, "kalshi_brier": 0.2301, "brier_diff_model_minus_kalshi": 0.0907, "brier_diff_se": 0.0257, "corr_model_outcome": -0.1018, "corr_kalshi_outcome": 0.3278}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
