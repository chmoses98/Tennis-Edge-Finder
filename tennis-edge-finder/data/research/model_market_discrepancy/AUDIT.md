# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-09T04:30Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 26,177): 0-3 14.3%, 3-5 9.6%, 5-10 19.8%, 10-15 15.5%, 15-25 18.6%, 25-40 13.9%, 40+ 8.4%; median gap 11.95 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.0%, Challenger 12.1%, doubles 6.8%). Main tour: ATP 1.5% and WTA 8.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,844): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.4%, STALE_QUOTE 17.1%, BOOK_QUALITY 16.8%, POOR_DATA 7.9%, POSSIBLY_IN_PLAY_QUOTE 5.5%, LIMITED_DATA 4.3%, IN_PLAY_QUOTE 3.5%, IDENTITY_AMBIGUOUS 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.2%. By class: coverage 39.4%, market_freshness 17.1%, execution 16.8%, data 12.3%, market_freshness/coverage 8.9%, mapping 3.4%, model_calibration_or_unknown 1.9%, model_calibration 0.2%.
* **Stale / settled / in-play**: 55.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,844 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 15.0% of the time and with the model 0.3%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 625.0 points vs 1791.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.098, Gen-2 0.879, Gen-1 ledger 0.921 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 243 model 0.2181 vs Kalshi 0.2011; n 53 model 0.2878 vs Kalshi 0.1771.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 100,215 model-market comparisons (166,966 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 37,929 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-09T04:25:24.244226+00:00'], shadow board 27,348 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-09T04:25:27.144367+00:00'], Model 4 10,554 rows, 11,186 settled tickers, 3,072 tickers with an external scan.
* By model: {"gen1_ledger": 24434, "gen1_elo": 13741, "fair_v1": 13741, "gen2": 13741, "gen1_sr": 13741, "model4_fundamental": 10413, "model4_conditioned": 10404}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 26,177 | 14.3 | 9.6 | 19.8 | 15.5 | 18.6 | 13.9 | 8.4 | 11.95 | 40.9% | 22.3% |
| MW fair_v1 | 13,741 | 13.5 | 8.7 | 18.3 | 16.3 | 18.4 | 14.7 | 10.1 | 12.9 | 43.3% | 24.9% |
| MW gen1_elo | 13,741 | 13.1 | 8.8 | 20.1 | 14.9 | 19.1 | 14.5 | 9.6 | 12.47 | 43.1% | 24.1% |
| MW gen1_ledger | 12,436 | 15.1 | 10.5 | 21.6 | 14.6 | 18.7 | 12.9 | 6.6 | 10.81 | 38.3% | 19.5% |
| MW gen1_sr | 13,741 | 10.3 | 7.8 | 16.2 | 14.1 | 21.4 | 18.4 | 11.8 | 15.53 | 51.7% | 30.2% |
| MW gen2 | 13,741 | 12.1 | 7.2 | 16.1 | 14.3 | 19.7 | 17.3 | 13.3 | 15.18 | 50.3% | 30.6% |
| all families model4_conditioned | 10,404 | 22.3 | 20.5 | 35.8 | 15.8 | 4.0 | 0.8 | 0.8 | 5.68 | 5.6% | 1.6% |
| all families model4_fundamental | 10,413 | 16.7 | 13.2 | 35.5 | 20.1 | 10.7 | 2.7 | 1.1 | 7.62 | 14.4% | 3.8% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.4%, >=15pp 40.9%, >=20pp 30.6%, >=25pp 22.3%, >=30pp 16.4%, >=40pp 8.5%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.7%, >=25pp 18.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,052 | 28.9 | 14.8 | 24.4 | 17.6 | 12.0 | 1.2 | 1.1 | 5.93 | 14.3% | 2.3% |
| CHALLENGER | 2,304 | 15.5 | 10.8 | 18.6 | 16.2 | 12.9 | 13.0 | 12.9 | 11.89 | 38.9% | 25.9% |
| ITF_MEN | 3,969 | 11.4 | 8.7 | 18.5 | 15.0 | 19.2 | 14.9 | 12.3 | 13.69 | 46.5% | 27.3% |
| ITF_WOMEN | 5,531 | 10.4 | 6.7 | 15.8 | 16.4 | 21.7 | 18.6 | 10.4 | 15.29 | 50.7% | 29.0% |
| WTA | 548 | 24.4 | 9.3 | 25.6 | 15.9 | 16.8 | 6.0 | 2.0 | 7.81 | 24.8% | 8.0% |
| WTA125 | 337 | 11.6 | 6.2 | 21.7 | 26.1 | 15.7 | 16.3 | 2.4 | 11.47 | 34.4% | 18.7% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,052 | 23.3 | 14.0 | 24.5 | 18.5 | 16.4 | 2.1 | 1.2 | 6.9 | 19.7% | 3.3% |
| CHALLENGER | 2,304 | 15.3 | 7.5 | 18.1 | 13.4 | 18.1 | 14.4 | 13.3 | 13.13 | 45.8% | 27.7% |
| ITF_MEN | 3,969 | 10.6 | 7.6 | 16.9 | 14.7 | 19.9 | 17.3 | 13.0 | 15.24 | 50.2% | 30.3% |
| ITF_WOMEN | 5,531 | 9.2 | 6.0 | 12.8 | 13.0 | 20.7 | 21.3 | 16.9 | 18.93 | 58.9% | 38.3% |
| WTA | 548 | 22.6 | 5.3 | 18.8 | 14.8 | 20.6 | 15.9 | 2.0 | 11.69 | 38.5% | 17.9% |
| WTA125 | 337 | 4.5 | 2.7 | 17.2 | 20.8 | 22.3 | 21.4 | 11.3 | 17.24 | 54.9% | 32.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,052 | 26.3 | 13.5 | 29.4 | 15.4 | 11.3 | 3.0 | 1.1 | 6.51 | 15.4% | 4.1% |
| CHALLENGER | 2,304 | 16.0 | 10.6 | 20.2 | 14.3 | 13.9 | 12.2 | 12.9 | 10.89 | 39.0% | 25.0% |
| ITF_MEN | 3,969 | 10.4 | 8.8 | 18.9 | 13.9 | 20.2 | 15.4 | 12.4 | 13.99 | 47.9% | 27.8% |
| ITF_WOMEN | 5,531 | 9.7 | 6.7 | 16.9 | 15.7 | 23.2 | 18.7 | 9.2 | 15.47 | 51.0% | 27.8% |
| WTA | 548 | 23.4 | 12.8 | 35.8 | 14.2 | 9.1 | 3.5 | 1.3 | 6.78 | 13.9% | 4.7% |
| WTA125 | 337 | 21.7 | 11.3 | 31.2 | 16.6 | 13.9 | 4.8 | 0.6 | 7.99 | 19.3% | 5.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 578 | 30.4 | 22.7 | 35.3 | 10.0 | 1.4 | 0.2 | 0.0 | 4.75 | 1.6% | 0.2% |
| CHALLENGER | 1,498 | 23.6 | 17.3 | 25.8 | 13.8 | 12.1 | 5.4 | 2.0 | 6.53 | 19.5% | 7.4% |
| DOUBLES | 787 | 3.9 | 3.4 | 10.8 | 11.4 | 19.7 | 24.4 | 26.3 | 25.56 | 70.4% | 50.7% |
| ITF_MEN | 3,886 | 14.8 | 8.5 | 21.0 | 15.2 | 20.3 | 12.5 | 7.8 | 11.78 | 40.6% | 20.2% |
| ITF_WOMEN | 4,586 | 11.5 | 9.3 | 19.9 | 14.5 | 22.4 | 16.7 | 5.7 | 13.04 | 44.8% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 445 | 21.4 | 11.5 | 25.4 | 18.6 | 15.3 | 7.2 | 0.7 | 8.4 | 23.2% | 7.9% |
| WTA125 | 507 | 16.6 | 12.8 | 22.5 | 20.3 | 16.4 | 8.7 | 2.8 | 9.33 | 27.8% | 11.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,047 | 28.9 | 14.7 | 24.4 | 17.7 | 11.9 | 1.2 | 1.1 | 5.93 | 14.2% | 2.3% |
| CHALLENGER | 1,623 | 20.5 | 13.9 | 23.9 | 19.2 | 13.2 | 6.5 | 2.8 | 7.99 | 22.6% | 9.3% |
| ITF_MEN | 2,833 | 14.1 | 10.9 | 22.0 | 16.7 | 19.2 | 12.0 | 5.2 | 10.88 | 36.3% | 17.2% |
| ITF_WOMEN | 3,946 | 12.9 | 8.4 | 18.6 | 18.8 | 23.2 | 14.9 | 3.2 | 12.62 | 41.3% | 18.1% |
| WTA | 545 | 24.4 | 9.4 | 25.7 | 15.8 | 16.9 | 5.9 | 2.0 | 7.78 | 24.8% | 7.9% |
| WTA125 | 324 | 12.0 | 6.5 | 21.0 | 26.5 | 16.1 | 16.4 | 1.5 | 11.47 | 34.0% | 17.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,047 | 23.2 | 13.9 | 24.6 | 18.5 | 16.3 | 2.1 | 1.2 | 6.9 | 19.7% | 3.3% |
| CHALLENGER | 1,623 | 20.1 | 9.9 | 22.8 | 16.4 | 18.6 | 9.6 | 2.6 | 9.08 | 30.8% | 12.2% |
| ITF_MEN | 2,834 | 12.6 | 9.2 | 19.5 | 16.6 | 21.2 | 14.9 | 6.0 | 12.46 | 42.1% | 20.9% |
| ITF_WOMEN | 3,946 | 10.8 | 7.2 | 14.5 | 14.2 | 23.1 | 20.3 | 10.1 | 16.26 | 53.4% | 30.4% |
| WTA | 545 | 22.6 | 5.3 | 18.9 | 14.9 | 20.6 | 15.8 | 2.0 | 11.64 | 38.4% | 17.8% |
| WTA125 | 324 | 4.6 | 2.8 | 17.3 | 21.6 | 21.6 | 21.9 | 10.2 | 16.84 | 53.7% | 32.1% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 563 | 30.7 | 22.9 | 35.4 | 10.1 | 0.7 | 0.2 | 0.0 | 4.69 | 0.9% | 0.2% |
| CHALLENGER | 1,268 | 25.8 | 19.6 | 27.9 | 13.5 | 11.1 | 2.0 | 0.1 | 5.78 | 13.2% | 2.1% |
| DOUBLES | 727 | 3.9 | 3.4 | 11.0 | 11.4 | 19.9 | 24.1 | 26.3 | 25.54 | 70.3% | 50.3% |
| ITF_MEN | 3,129 | 16.5 | 9.5 | 23.3 | 16.2 | 20.1 | 10.0 | 4.4 | 10.16 | 34.5% | 14.5% |
| ITF_WOMEN | 3,732 | 12.8 | 10.1 | 21.8 | 15.3 | 22.7 | 14.9 | 2.4 | 11.43 | 40.0% | 17.3% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 415 | 21.9 | 12.1 | 26.0 | 18.8 | 15.7 | 5.5 | 0.0 | 8.28 | 21.2% | 5.5% |
| WTA125 | 422 | 18.5 | 14.2 | 24.9 | 23.2 | 14.4 | 4.5 | 0.2 | 8.21 | 19.2% | 4.7% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 787 | 3.9 | 3.4 | 10.8 | 11.4 | 19.7 | 24.4 | 26.3 | 25.56 | 70.4% | 50.7% |
| singles | 11,649 | 15.8 | 11.0 | 22.3 | 14.8 | 18.7 | 12.2 | 5.3 | 10.22 | 36.1% | 17.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,175 | 13.5 | 9.5 | 20.2 | 15.9 | 16.1 | 14.4 | 10.4 | 12.21 | 40.9% | 24.8% |
| Hard | 9,206 | 13.8 | 8.4 | 18.1 | 16.1 | 19.0 | 14.5 | 10.0 | 12.95 | 43.5% | 24.6% |
| UNKNOWN | 1,360 | 11.7 | 8.1 | 15.0 | 18.1 | 20.1 | 16.8 | 10.2 | 14.1 | 47.1% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,003 | 19.8 | 10.6 | 20.3 | 17.3 | 14.6 | 9.4 | 8.0 | 9.8 | 32.1% | 17.4% |
| B | 1,830 | 15.3 | 9.5 | 19.4 | 17.4 | 16.6 | 11.8 | 9.9 | 11.19 | 38.3% | 21.7% |
| C | 2,128 | 12.4 | 9.9 | 19.6 | 15.4 | 18.5 | 14.8 | 9.4 | 12.69 | 42.7% | 24.2% |
| D | 2,606 | 10.9 | 8.4 | 17.3 | 16.4 | 22.2 | 14.9 | 9.9 | 13.98 | 47.0% | 24.8% |
| F | 3,174 | 7.6 | 5.1 | 14.9 | 14.9 | 21.1 | 22.9 | 13.6 | 18.4 | 57.6% | 36.4% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,456 | 22.4 | 15.6 | 27.6 | 15.5 | 12.0 | 5.0 | 1.9 | 6.92 | 18.9% | 6.9% |
| B | 1,956 | 14.6 | 9.7 | 24.5 | 16.2 | 18.7 | 11.7 | 4.7 | 10.34 | 35.0% | 16.3% |
| C | 2,554 | 11.9 | 8.0 | 18.1 | 14.2 | 20.8 | 15.7 | 11.3 | 13.81 | 47.8% | 27.1% |
| D | 2,065 | 13.9 | 9.2 | 21.4 | 13.0 | 22.0 | 14.1 | 6.3 | 12.05 | 42.4% | 20.4% |
| F | 2,405 | 9.2 | 7.8 | 14.2 | 13.6 | 23.5 | 21.5 | 10.2 | 16.91 | 55.1% | 31.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,518 | 18.3 | 9.8 | 19.5 | 17.3 | 15.0 | 9.9 | 10.1 | 10.65 | 35.0% | 20.0% |
| LIMITED | 3,402 | 14.8 | 10.5 | 20.6 | 16.1 | 17.5 | 13.4 | 7.2 | 11.31 | 38.1% | 20.6% |
| POOR | 5,821 | 9.1 | 6.7 | 15.9 | 15.6 | 21.6 | 19.2 | 11.8 | 16.04 | 52.7% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,404 | 29.9 | 25.0 | 37.2 | 5.4 | 1.8 | 0.5 | 0.1 | 4.56 | 2.5% | 0.6% |
| GAME_SPREAD | 2,250 | 25.0 | 15.7 | 36.8 | 17.6 | 4.5 | 0.2 | 0.1 | 6.13 | 4.9% | 0.4% |
| MATCH_WINNER | 12,436 | 15.1 | 10.5 | 21.6 | 14.6 | 18.7 | 12.9 | 6.6 | 10.81 | 38.3% | 19.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 4,094 | 31.7 | 19.9 | 30.4 | 10.1 | 6.4 | 1.3 | 0.3 | 4.82 | 8.0% | 1.6% |
| TOTAL_GAMES | 3,226 | 7.3 | 9.2 | 38.8 | 30.6 | 9.1 | 2.9 | 2.0 | 9.43 | 14.1% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,872 | 24.5 | 38.5 | 31.2 | 0.3 | 4.8 | 0.5 | 0.1 | 4.34 | 5.5% | 0.7% |
| GAME_SPREAD | 2,700 | 45.9 | 14.5 | 29.3 | 8.2 | 1.1 | 0.7 | 0.3 | 3.54 | 2.1% | 1.0% |
| TOTAL_GAMES | 3,832 | 3.3 | 6.5 | 45.1 | 37.0 | 5.1 | 1.2 | 1.7 | 9.55 | 8.1% | 2.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,872 | 25.6 | 18.3 | 36.3 | 9.8 | 7.0 | 2.6 | 0.4 | 5.61 | 10.0% | 3.0% |
| GAME_SPREAD | 2,700 | 18.9 | 13.1 | 28.1 | 22.1 | 14.5 | 2.7 | 0.7 | 8.12 | 17.8% | 3.3% |
| TOTAL_GAMES | 3,841 | 6.1 | 8.3 | 40.0 | 29.1 | 11.7 | 2.8 | 2.0 | 9.52 | 16.4% | 4.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 13,741 | 43.3% | 24.9% | 12.9 | 33.1% | 14.3% | 10.36 |
| gen1_elo | 13,741 | 43.1% | 24.1% | 12.47 | 32.7% | 13.9% | 9.8 |
| gen1_sr | 13,741 | 51.7% | 30.2% | 15.53 | 42.6% | 19.8% | 12.66 |
| gen2 | 13,741 | 50.3% | 30.6% | 15.18 | 42.5% | 21.6% | 12.59 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 6,917 | 16.5 | 11.0 | 21.3 | 17.6 | 18.6 | 11.6 | 3.5 | 10.35 | 33.6% | 15.0% |
| STALE | 6,824 | 10.6 | 6.3 | 15.2 | 14.9 | 18.3 | 17.9 | 16.9 | 16.67 | 53.0% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 5,904 | 17.2 | 11.6 | 23.6 | 14.4 | 16.8 | 11.6 | 4.8 | 9.35 | 33.2% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 26,177 | 5904 | 10389 | 9884 | 25.0 | 160.6 | 1400.4 |
| ge_15pp | 10,707 | 1962 | 3615 | 5130 | 28.8 | 455.3 | 1380.4 |
| ge_25pp | 5,844 | 968 | 1632 | 3244 | 37.0 | 574.1 | 1380.4 |
| lt_10pp | 11,421 | 3093 | 5002 | 3326 | 23.5 | 49.5 | 1230.8 |

Current slate `SL-20261009T043042Z-578ff3fa`: 700 priced rows, quote age at build {'median': 5.7, 'max': 5.7}, freshness {'FRESH': 700}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 4 | 0.0 | 0.0 | 25.0 | 0.0 | 75.0 | 0.0 | 0.0 | 20.45 | 75.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 3 | 33.3 | 66.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.05 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 757 | 24.8 | 11.2 | 20.7 | 20.7 | 14.8 | 7.3 | 0.4 | 8.01 | 22.5% | 7.7% |
| MARKETS_AGREE | 90 | 78.9 | 21.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.74 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 151 | 0.0 | 2.6 | 32.5 | 34.4 | 19.9 | 9.9 | 0.7 | 11.92 | 30.5% | 10.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 13,741 | 1005 (7.3%) | 15.0% | 0.3% | {"EXTERNAL_STALE": 757, "AGREES_WITH_KALSHI": 151, "ALL_AGREE": 90, "SUPPORTS_MODEL_DIRECTION": 3, "EXTERNAL_OUTLIER": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 5,946 | 219 (3.7%) | 21.0% | 1.4% | {"EXTERNAL_STALE": 170, "AGREES_WITH_KALSHI": 46, "SUPPORTS_MODEL_DIRECTION": 3} |
| fair_v1_ge_25pp | 3,414 | 74 (2.2%) | 21.6% | 0.0% | {"EXTERNAL_STALE": 58, "AGREES_WITH_KALSHI": 16} |
| fair_v1_ge_25pp_pregame_clean | 1,476 | 72 (4.9%) | 22.2% | 0.0% | {"EXTERNAL_STALE": 56, "AGREES_WITH_KALSHI": 16} |
| fair_v1_lt_10pp | 5,559 | 577 (10.4%) | 9.2% | 0.0% | {"EXTERNAL_STALE": 430, "ALL_AGREE": 90, "AGREES_WITH_KALSHI": 53, "EXTERNAL_OUTLIER": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,810 | 11.7 | 8.4 | 19.6 | 15.6 | 20.9 | 13.8 | 10.1 | 13.04 | 44.7% | 23.9% |
| 4-10x | 1,950 | 11.2 | 9.2 | 18.4 | 15.2 | 20.1 | 16.7 | 9.2 | 13.57 | 45.9% | 25.9% |
| <2x | 7,238 | 15.6 | 9.2 | 18.3 | 17.3 | 16.7 | 13.2 | 9.8 | 12.0 | 39.6% | 23.0% |
| >=10x | 1,743 | 10.6 | 6.4 | 15.6 | 14.4 | 20.0 | 20.5 | 12.6 | 16.49 | 53.1% | 33.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,578 | 14.3 | 8.6 | 19.3 | 16.0 | 18.0 | 12.9 | 11.0 | 12.22 | 41.8% | 23.8% |
| 300-1000 | 3,397 | 11.8 | 9.2 | 16.6 | 16.4 | 20.9 | 16.0 | 9.1 | 13.73 | 46.0% | 25.1% |
| <300 | 3,663 | 8.1 | 6.0 | 15.8 | 15.0 | 21.1 | 21.0 | 13.1 | 17.19 | 55.2% | 34.1% |
| >=3000 | 3,103 | 20.9 | 11.4 | 21.9 | 18.0 | 13.0 | 8.1 | 6.7 | 8.88 | 27.9% | 14.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 433 | 0.5422 | 0.4097 | 0.4873 | +0.055 | -0.078 | 0.0022 ± 0.0071 |
| ratio 4-10x | 304 | 0.5817 | 0.4399 | 0.523 | +0.059 | -0.083 | -0.0024 ± 0.009 |
| ratio <2x | 915 | 0.5436 | 0.4185 | 0.459 | +0.085 | -0.041 | 0.0112 ± 0.0048 |
| ratio >=10x | 292 | 0.5481 | 0.3781 | 0.4384 | +0.110 | -0.060 | 0.0135 ± 0.0103 |
| thinner_sample 1000-3000 | 525 | 0.5476 | 0.4228 | 0.4686 | +0.079 | -0.046 | 0.0058 ± 0.0063 |
| thinner_sample 300-1000 | 536 | 0.5699 | 0.4291 | 0.5 | +0.070 | -0.071 | 0.0011 ± 0.0068 |
| thinner_sample <300 | 594 | 0.5429 | 0.3821 | 0.463 | +0.080 | -0.081 | 0.0089 ± 0.0069 |
| thinner_sample >=3000 | 289 | 0.5316 | 0.4342 | 0.4464 | +0.085 | -0.012 | 0.0192 ± 0.0068 |
| data_status ADEQUATE | 505 | 0.5302 | 0.4254 | 0.4436 | +0.087 | -0.018 | 0.0128 ± 0.0055 |
| data_status LIMITED | 500 | 0.5648 | 0.432 | 0.498 | +0.067 | -0.066 | 0.0008 ± 0.0068 |
| data_status POOR | 939 | 0.5526 | 0.3979 | 0.4739 | +0.079 | -0.076 | 0.0081 ± 0.0054 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 292 | 0.1862 | 0.1875 | -0.0013 ± 0.0009 | 0.5482 | 0.5515 | 0.4917 | 0.4771 | 0.5171 | -0.069 ± 0.0266 | -0.01 (3) |
| 3-5 | 197 | 0.1865 | 0.1874 | -0.0009 ± 0.0025 | 0.5522 | 0.5522 | 0.5145 | 0.4745 | 0.5025 | -0.070 ± 0.0313 | 0.02 (1) |
| 5-10 | 398 | 0.2012 | 0.2034 | -0.0022 ± 0.0034 | 0.5891 | 0.5941 | 0.5217 | 0.4477 | 0.4899 | -0.087 ± 0.0236 | -0.0125 (4) |
| 10-15 | 345 | 0.2127 | 0.2076 | +0.0051 ± 0.0062 | 0.612 | 0.5963 | 0.5226 | 0.3984 | 0.4377 | -0.093 ± 0.0246 | -0.0633 (3) |
| 15-25 | 416 | 0.2227 | 0.2127 | +0.0100 ± 0.0088 | 0.637 | 0.6132 | 0.5736 | 0.378 | 0.4495 | -0.082 ± 0.0226 | -0.0133 (6) |
| 25-40 | 243 | 0.2181 | 0.2011 | +0.0170 ± 0.0171 | 0.6256 | 0.5776 | 0.6475 | 0.3385 | 0.465 | -0.072 ± 0.0255 | -0.01 (1) |
| 40+ | 53 | 0.2878 | 0.1771 | +0.1107 ± 0.0514 | 0.7805 | 0.5305 | 0.7594 | 0.311 | 0.4151 | -0.127 ± 0.0502 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1437 | 0.1673 | 0.1681 | -0.0008 ± 0.0004 | 0.5032 | 0.5039 | 0.4722 | 0.4574 | 0.4934 | -0.027 ± 0.011 | -0.0188 (8) |
| 3-5 | 956 | 0.191 | 0.1872 | +0.0039 ± 0.0011 | 0.563 | 0.548 | 0.479 | 0.4394 | 0.4069 | -0.093 ± 0.0142 | 0.02 (1) |
| 5-10 | 2037 | 0.1929 | 0.1908 | +0.0021 ± 0.0014 | 0.5686 | 0.5614 | 0.4918 | 0.418 | 0.4354 | -0.054 ± 0.0098 | -0.0082 (17) |
| 10-15 | 1854 | 0.1981 | 0.1816 | +0.0165 ± 0.0025 | 0.5802 | 0.5337 | 0.4718 | 0.3472 | 0.343 | -0.074 ± 0.0099 | -0.0475 (4) |
| 15-25 | 2173 | 0.2001 | 0.1639 | +0.0362 ± 0.0034 | 0.5894 | 0.4883 | 0.4893 | 0.2933 | 0.2996 | -0.070 ± 0.0087 | -0.0048 (29) |
| 25-40 | 1837 | 0.2166 | 0.1237 | +0.0929 ± 0.0051 | 0.6253 | 0.3828 | 0.5272 | 0.2137 | 0.2248 | -0.059 ± 0.0079 | -0.01 (1) |
| 40+ | 1272 | 0.371 | 0.0454 | +0.3256 ± 0.0066 | 0.9673 | 0.1782 | 0.6229 | 0.1067 | 0.0597 | -0.083 ± 0.0056 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 228 | 0.1954 | 0.1956 | -0.0003 ± 0.001 | 0.5743 | 0.5752 | 0.4903 | 0.4751 | 0.4781 | -0.103 ± 0.031 | -0.01 (1) |
| 3-5 | 149 | 0.2036 | 0.2049 | -0.0014 ± 0.003 | 0.586 | 0.5915 | 0.52 | 0.48 | 0.5101 | -0.060 ± 0.039 | 0.02 (1) |
| 5-10 | 334 | 0.1928 | 0.1898 | +0.0030 ± 0.0036 | 0.5674 | 0.5607 | 0.5674 | 0.4924 | 0.506 | -0.100 ± 0.0247 | -0.01 (4) |
| 10-15 | 332 | 0.217 | 0.2109 | +0.0060 ± 0.0063 | 0.6201 | 0.6089 | 0.5811 | 0.4564 | 0.5 | -0.095 ± 0.0262 | -0.05 (4) |
| 15-25 | 465 | 0.2245 | 0.207 | +0.0176 ± 0.0084 | 0.6378 | 0.5957 | 0.5997 | 0.4024 | 0.4624 | -0.097 ± 0.0217 | -0.01 (5) |
| 25-40 | 317 | 0.2712 | 0.2014 | +0.0698 ± 0.0159 | 0.7572 | 0.5832 | 0.6708 | 0.3571 | 0.4038 | -0.139 ± 0.0252 | -0.025 (2) |
| 40+ | 119 | 0.3395 | 0.1867 | +0.1527 ± 0.0384 | 0.9544 | 0.5477 | 0.7618 | 0.2833 | 0.3782 | -0.068 ± 0.0368 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1305 | 0.174 | 0.1747 | -0.0007 ± 0.0004 | 0.5205 | 0.5222 | 0.4921 | 0.4776 | 0.5027 | -0.034 ± 0.012 | -0.0217 (6) |
| 3-5 | 802 | 0.1887 | 0.1859 | +0.0028 ± 0.0012 | 0.5492 | 0.5429 | 0.5211 | 0.4813 | 0.4663 | -0.069 ± 0.0154 | 0.02 (1) |
| 5-10 | 1790 | 0.1842 | 0.1801 | +0.0041 ± 0.0015 | 0.5496 | 0.5354 | 0.5191 | 0.4456 | 0.4559 | -0.057 ± 0.0102 | -0.01 (5) |
| 10-15 | 1629 | 0.1949 | 0.1814 | +0.0134 ± 0.0026 | 0.5754 | 0.5311 | 0.5156 | 0.3913 | 0.4027 | -0.064 ± 0.0107 | -0.02 (14) |
| 15-25 | 2269 | 0.2141 | 0.1724 | +0.0417 ± 0.0034 | 0.6238 | 0.5105 | 0.5289 | 0.3332 | 0.3275 | -0.085 ± 0.0088 | -0.0026 (27) |
| 25-40 | 2098 | 0.2477 | 0.1371 | +0.1106 ± 0.0052 | 0.7017 | 0.4184 | 0.5614 | 0.2446 | 0.2297 | -0.088 ± 0.0081 | -0.015 (6) |
| 40+ | 1673 | 0.4026 | 0.0677 | +0.3349 ± 0.0073 | 1.0545 | 0.2377 | 0.6689 | 0.131 | 0.1022 | -0.071 ± 0.0062 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 297 | 0.1915 | 0.194 | -0.0026 ± 0.0009 | 0.5616 | 0.5687 | 0.4966 | 0.4813 | 0.5455 | -0.025 ± 0.0258 | -0.0133 (6) |
| 3-5 | 204 | 0.184 | 0.1826 | +0.0014 ± 0.0024 | 0.5429 | 0.5389 | 0.4991 | 0.4599 | 0.4657 | -0.119 ± 0.0317 | -0.01 (1) |
| 5-10 | 420 | 0.1977 | 0.1976 | +0.0000 ± 0.0033 | 0.5813 | 0.5795 | 0.5111 | 0.4373 | 0.469 | -0.089 ± 0.0227 | -0.01 (4) |
| 10-15 | 325 | 0.215 | 0.2138 | +0.0013 ± 0.0064 | 0.62 | 0.6115 | 0.5357 | 0.4126 | 0.4708 | -0.083 ± 0.0253 | -0.044 (5) |
| 15-25 | 407 | 0.2244 | 0.2081 | +0.0163 ± 0.0088 | 0.6452 | 0.601 | 0.5795 | 0.386 | 0.4398 | -0.100 ± 0.0224 | -0.03 (1) |
| 25-40 | 244 | 0.2013 | 0.207 | -0.0057 ± 0.0169 | 0.5857 | 0.5932 | 0.6552 | 0.3435 | 0.5041 | -0.047 ± 0.0248 | 0.0 (1) |
| 40+ | 47 | 0.3129 | 0.1765 | +0.1364 ± 0.0556 | 0.8395 | 0.5287 | 0.7528 | 0.2988 | 0.383 | -0.139 ± 0.0556 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1365 | 0.1793 | 0.1802 | -0.0009 ± 0.0004 | 0.5317 | 0.5337 | 0.4827 | 0.4675 | 0.496 | -0.032 ± 0.0115 | -0.0183 (23) |
| 3-5 | 955 | 0.183 | 0.1804 | +0.0026 ± 0.0011 | 0.5407 | 0.5341 | 0.4689 | 0.4297 | 0.4157 | -0.084 ± 0.0143 | -0.0243 (7) |
| 5-10 | 2184 | 0.1853 | 0.1805 | +0.0048 ± 0.0014 | 0.5519 | 0.5357 | 0.481 | 0.4067 | 0.4125 | -0.060 ± 0.0092 | -0.01 (18) |
| 10-15 | 1729 | 0.1957 | 0.1795 | +0.0161 ± 0.0025 | 0.5756 | 0.5268 | 0.4885 | 0.365 | 0.3597 | -0.078 ± 0.0101 | -0.03 (9) |
| 15-25 | 2338 | 0.2033 | 0.1678 | +0.0354 ± 0.0033 | 0.5985 | 0.4989 | 0.4929 | 0.2973 | 0.3058 | -0.065 ± 0.0085 | -0.03 (2) |
| 25-40 | 1787 | 0.212 | 0.1196 | +0.0924 ± 0.0052 | 0.6145 | 0.371 | 0.5231 | 0.2057 | 0.2222 | -0.057 ± 0.0077 | 0.0 (1) |
| 40+ | 1208 | 0.3856 | 0.0469 | +0.3387 ± 0.007 | 1.0072 | 0.1828 | 0.6309 | 0.1078 | 0.0571 | -0.086 ± 0.0059 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 582 | 0.2013 | 0.2014 | -0.0001 ± 0.0006 | 0.5853 | 0.5851 | 0.4997 | 0.4848 | 0.4863 | -0.048 ± 0.0185 | -0.0226 (46) |
| 3-5 | 435 | 0.195 | 0.1937 | +0.0013 ± 0.0017 | 0.5708 | 0.5661 | 0.4795 | 0.44 | 0.446 | -0.050 ± 0.0211 | -0.0058 (33) |
| 5-10 | 888 | 0.1919 | 0.1868 | +0.0052 ± 0.0022 | 0.5682 | 0.5547 | 0.4796 | 0.4062 | 0.4088 | -0.058 ± 0.0148 | -0.0049 (73) |
| 10-15 | 580 | 0.2041 | 0.1947 | +0.0095 ± 0.0046 | 0.5974 | 0.5709 | 0.4825 | 0.3596 | 0.381 | -0.043 ± 0.0182 | 0.0014 (64) |
| 15-25 | 782 | 0.2329 | 0.2077 | +0.0251 ± 0.0064 | 0.6598 | 0.6007 | 0.5481 | 0.3538 | 0.3875 | -0.056 ± 0.0164 | -0.0216 (58) |
| 25-40 | 444 | 0.2456 | 0.1854 | +0.0602 ± 0.0127 | 0.691 | 0.5443 | 0.6267 | 0.3135 | 0.3716 | -0.075 ± 0.0191 | -0.0216 (25) |
| 40+ | 149 | 0.3493 | 0.1859 | +0.1634 ± 0.0358 | 0.9929 | 0.5499 | 0.7782 | 0.2869 | 0.3893 | -0.060 ± 0.0322 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1721 | 0.1862 | 0.1862 | +0.0000 ± 0.0004 | 0.5474 | 0.5463 | 0.5006 | 0.4855 | 0.4863 | -0.043 ± 0.0103 | -0.0155 (82) |
| 3-5 | 1213 | 0.1861 | 0.1835 | +0.0026 ± 0.001 | 0.5461 | 0.5402 | 0.4908 | 0.4513 | 0.4419 | -0.057 ± 0.0123 | -0.0148 (63) |
| 5-10 | 2491 | 0.1911 | 0.1833 | +0.0078 ± 0.0013 | 0.5663 | 0.5445 | 0.4768 | 0.4031 | 0.3914 | -0.065 ± 0.0087 | -0.0087 (125) |
| 10-15 | 1702 | 0.2001 | 0.1861 | +0.0140 ± 0.0026 | 0.5877 | 0.5501 | 0.4966 | 0.3735 | 0.3772 | -0.056 ± 0.0103 | -0.0053 (105) |
| 15-25 | 2204 | 0.2257 | 0.1951 | +0.0307 ± 0.0037 | 0.6501 | 0.569 | 0.5422 | 0.3472 | 0.3666 | -0.057 ± 0.0095 | -0.0255 (106) |
| 25-40 | 1547 | 0.2398 | 0.1604 | +0.0794 ± 0.0064 | 0.6794 | 0.4783 | 0.5892 | 0.2747 | 0.3077 | -0.061 ± 0.0099 | -0.0206 (47) |
| 40+ | 736 | 0.3648 | 0.1095 | +0.2553 ± 0.013 | 1.0013 | 0.3447 | 0.6821 | 0.1773 | 0.1889 | -0.067 ± 0.0113 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1944 | 1.098 ± 0.065 | 1.196 | 0.1709 | 0.1696 | 0.2086 | 0.2011 |
| gen2 | 1944 | 0.879 ± 0.057 | 1.127 | 0.1871 | 0.169 | 0.2274 | 0.2011 |
| gen1_elo | 1944 | 1.088 ± 0.063 | 1.188 | 0.1748 | 0.1701 | 0.207 | 0.2011 |
| gen1_sr | 1944 | 1.088 ± 0.073 | 1.206 | 0.1446 | 0.1715 | 0.2223 | 0.2008 |
| gen1_ledger | 3860 | 0.921 ± 0.041 | 1.079 | 0.1729 | 0.1912 | 0.2161 | 0.195 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 10,707)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,930 | 27.4% |
| STALE_QUOTE | market_freshness | 2,233 | 20.9% |
| BOOK_QUALITY | execution | 1,857 | 17.3% |
| POOR_DATA | data | 1,140 | 10.7% |
| LIMITED_DATA | data | 804 | 7.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 581 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 471 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 322 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 321 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 47 | 0.4% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 27.4%, market_freshness 20.9%, data 18.2%, execution 17.3%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.4%, mapping 3.0%, model_calibration 0.4%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.2%, START_UNVERIFIABLE 96.3%, LOW_DATA_QUALITY 69.0%, STALE_PLAYER_DATA 57.6%, THIN_PLAYER_HISTORY 57.2%, STALE_KALSHI_QUOTE 47.9%, MODEL_INTERNAL_DISAGREEMENT 37.3%, ASYMMETRIC_SAMPLE_SIZE 30.6%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 16.2%, PLAYER_IDENTITY_RISK 11.3%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 7.9%, LOW_DISPLAYED_LIQUIDITY 7.3%, MODEL_CALIBRATION_OUTLIER 3.3%, EXTERNAL_MARKET_REJECTION 0.7%, UNKNOWN 0.5%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.9%, POST_SETTLEMENT_OBSERVATION 27.4%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,844)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,300 | 39.4% |
| STALE_QUOTE | market_freshness | 999 | 17.1% |
| BOOK_QUALITY | execution | 982 | 16.8% |
| POOR_DATA | data | 463 | 7.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 319 | 5.5% |
| LIMITED_DATA | data | 254 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 203 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 200 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 110 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 14 | 0.2% |

Cause class: coverage 39.4%, market_freshness 17.1%, execution 16.8%, data 12.3%, market_freshness/coverage 8.9%, mapping 3.4%, model_calibration_or_unknown 1.9%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.6%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 71.7%, THIN_PLAYER_HISTORY 58.7%, STALE_KALSHI_QUOTE 55.5%, STALE_PLAYER_DATA 52.4%, MODEL_INTERNAL_DISAGREEMENT 38.6%, ASYMMETRIC_SAMPLE_SIZE 32.3%, WIDE_SPREAD 22.9%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 14.3%, EVENT_MAPPING_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.6%, LEVEL_TRANSFER_RISK 7.6%, MODEL_CALIBRATION_OUTLIER 4.2%, EXTERNAL_MARKET_REJECTION 0.4%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.3%, POST_SETTLEMENT_OBSERVATION 39.4%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4846, "IDENTITY_AMBIGUOUS": 998}; ticker orientation: {"VERIFIED": 5844}.

Checks: discipline:AMBIGUOUS 399, discipline:PASS 5445, identity_confidence:AMBIGUOUS 835, identity_confidence:PASS 5009, level_mapping:NA 411, level_mapping:PASS 5433, market_pair:AMBIGUOUS 220, market_pair:NA 130, market_pair:PASS 5494, model_complement:NA 97, model_complement:PASS 5747, namesake:PASS 5844, physical_match_id:NA 2430, physical_match_id:PASS 3414, player_ids:PASS 5844, same_pair_other_event:PASS 5844, ticker_orientation:PASS 5844

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,630 | 1.5% | 1.6% | 0.4% | {"market_freshness": 20, "execution": 5} | 5.4 | 0.2183 / 0.2094 (141) | 18.9% | 0.1% | 5.7% | 1.2% |
| CHALLENGER | 3,802 | 18.6% | 6.2% | 12.1% | {"coverage": 445, "market_freshness": 107, "market_freshness/coverage": 85, "model_calibration_or_unknown": 39, "data": 25, "execution": 4, "model_calibration": 3} | 6.72 | 0.2239 / 0.206 (894) | 45.6% | 4.7% | 1.7% | 24.0% |
| DOUBLES | 787 | 50.7% | 50.3% | 6.8% | {"execution": 147, "mapping": 113, "market_freshness": 106, "market_freshness/coverage": 26, "coverage": 7} | 25.54 | 0.3188 / 0.2271 (213) | 29.7% | 0.0% | 100.0% | 7.6% |
| ITF_MEN | 7,855 | 23.8% | 15.8% | 32.0% | {"coverage": 767, "execution": 383, "data": 268, "market_freshness": 268, "market_freshness/coverage": 162, "mapping": 19, "model_calibration_or_unknown": 1} | 10.54 | 0.2109 / 0.193 (1929) | 38.5% | 54.2% | 6.2% | 24.1% |
| ITF_WOMEN | 10,117 | 26.0% | 17.7% | 45.0% | {"coverage": 1064, "market_freshness": 440, "execution": 426, "data": 400, "market_freshness/coverage": 208, "mapping": 62, "model_calibration_or_unknown": 23, "model_calibration": 9} | 12.15 | 0.2014 / 0.192 (2151) | 39.5% | 57.6% | 9.7% | 24.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 993 | 8.0% | 6.9% | 1.4% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.0 | 0.2039 / 0.1997 (149) | 33.6% | 2.1% | 1.2% | 3.3% |
| WTA125 | 844 | 14.3% | 10.5% | 2.1% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 29, "market_freshness": 22, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 2} | 10.01 | 0.2257 / 0.2107 (285) | 25.8% | 6.3% | 4.0% | 11.6% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 9 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 10 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 11 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 14 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 17 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 18 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 20 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 21 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 22 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 23 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 24 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 26 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 27 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 28 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 29 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 30 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 31 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 32 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 33 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 34 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 37 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 38 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 39 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 40 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 41 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 26 min (AGING); no external reference |
| 42 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 43 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 44 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 45 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 46 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 123 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 49 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 50 | `KXITFWMATCH-26OCT08YANZHE-YAN` | ITF_WOMEN | fair_v1 | 90% / 18% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 61 min before settlement (in-play print); quote age at model time 166 min (STALE); data LIMITED (grade C, thinner serve sample 1212.0, ratio 2.36); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9822, "by_level_share_of_ge_25pp": {"ATP": 0.0043, "CHALLENGER": 0.1211, "DOUBLES": 0.0683, "ITF_MEN": 0.3196, "ITF_WOMEN": 0.4504, "OTHER": 0.0021, "WTA": 0.0135, "WTA125": 0.0207}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5551, "share_primary_cause_market_settled_or_in_play": 0.4829, "share_primary_cause_stale_quote_only": 0.1709}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5844, "identity_ambiguous_share": 0.1708, "ticker_orientation": {"VERIFIED": 5844}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3414, "with_external": 74, "coverage": 0.0217, "external_status": {"EXTERNAL_STALE": 58, "AGREES_WITH_KALSHI": 16}, "triangulation": {"INSUFFICIENT_INPUTS": 58, "MODEL_LONE_OUTLIER": 16}, "share_external_agrees_with_kalshi": 0.2162, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1476, "with_external": 72, "coverage": 0.0488, "external_status": {"EXTERNAL_STALE": 56, "AGREES_WITH_KALSHI": 16}, "triangulation": {"INSUFFICIENT_INPUTS": 56, "MODEL_LONE_OUTLIER": 16}, "share_external_agrees_with_kalshi": 0.2222, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 625.0, "median_sample_ratio": 2.32, "median_min_matches": 21.0, "median_max_days_since_last": 196.0, "share_severe_asymmetry": 0.1739, "data_status": {"POOR": 3001, "LIMITED": 1791, "ADEQUATE": 1052}, "comparison_lt_10pp": {"median_thinner_serve_points": 1791.0, "median_sample_ratio": 1.73, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 433, "model_minus_observed": 0.0549, "kalshi_minus_observed": -0.0776, "brier_diff_model_minus_kalshi": 0.0022}, "4-10x": {"n": 304, "model_minus_observed": 0.0587, "kalshi_minus_observed": -0.0831, "brier_diff_model_minus_kalshi": -0.0024}, "<2x": {"n": 915, "model_minus_observed": 0.0846, "kalshi_minus_observed": -0.0405, "brier_diff_model_minus_kalshi": 0.0112}, ">=10x": {"n": 292, "model_minus_observed": 0.1097, "kalshi_minus_observed": -0.0603, "brier_diff_model_minus_kalshi": 0.0135}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1944, "model": {"intercept": -0.566, "slope": 0.879, "slope_se": 0.057}, "kalshi_mid_same_rows": {"intercept": 0.226, "slope": 1.127, "slope_se": 0.065}, "mean_extremity_model": 0.1871, "mean_extremity_kalshi": 0.169, "model_brier": 0.2274, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.0263, "brier_diff_se": 0.0043, "model_logloss": 0.6501, "kalshi_logloss": 0.5842}, "fair_v1": {"n": 1944, "model": {"intercept": -0.399, "slope": 1.098, "slope_se": 0.065}, "kalshi_mid_same_rows": {"intercept": 0.35, "slope": 1.196, "slope_se": 0.067}, "mean_extremity_model": 0.1709, "mean_extremity_kalshi": 0.1696, "model_brier": 0.2086, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.0035, "model_logloss": 0.6033, "kalshi_logloss": 0.5842}, "gen1_elo": {"n": 1944, "model": {"intercept": -0.373, "slope": 1.088, "slope_se": 0.063}, "kalshi_mid_same_rows": {"intercept": 0.358, "slope": 1.188, "slope_se": 0.066}, "mean_extremity_model": 0.1748, "mean_extremity_kalshi": 0.1701, "model_brier": 0.207, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.006, "brier_diff_se": 0.0034, "model_logloss": 0.6009, "kalshi_logloss": 0.5839}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2485, "share_ge_15": 0.4327, "median_abs_gap": 12.9, "n": 13741}, "gen1_elo": {"share_ge_25": 0.2407, "share_ge_15": 0.4313, "median_abs_gap": 12.47, "n": 13741}, "gen1_sr": {"share_ge_25": 0.302, "share_ge_15": 0.5166, "median_abs_gap": 15.53, "n": 13741}, "gen2": {"share_ge_25": 0.3055, "share_ge_15": 0.5029, "median_abs_gap": 15.18, "n": 13741}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.143, "share_ge_15": 0.3314, "median_abs_gap": 10.36, "n": 10318}, "gen1_elo": {"share_ge_25": 0.139, "share_ge_15": 0.327, "median_abs_gap": 9.8, "n": 10317}, "gen1_sr": {"share_ge_25": 0.1981, "share_ge_15": 0.4259, "median_abs_gap": 12.66, "n": 10318}, "gen2": {"share_ge_25": 0.2155, "share_ge_15": 0.4255, "median_abs_gap": 12.59, "n": 10319}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.4, "share_ge_25_all": 0.0153, "share_ge_25_pregame_clean": 0.0155}, "WTA": {"median_abs_gap_pregame_clean": 8.0, "share_ge_25_all": 0.0796, "share_ge_25_pregame_clean": 0.0688}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.238, "share_within_10pp_all": 0.4363, "share_within_10pp_pregame_clean": 0.5006, "corr_model_vs_mid_pregame_clean": 0.8505}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 292, "model_brier": 0.1862, "kalshi_brier": 0.1875, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 345, "model_brier": 0.2127, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": 0.0051}, "15-25": {"n_settled": 416, "model_brier": 0.2227, "kalshi_brier": 0.2127, "brier_diff_model_minus_kalshi": 0.01}, "25-40": {"n_settled": 243, "model_brier": 0.2181, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.017}, "3-5": {"n_settled": 197, "model_brier": 0.1865, "kalshi_brier": 0.1874, "brier_diff_model_minus_kalshi": -0.0009}, "40+": {"n_settled": 53, "model_brier": 0.2878, "kalshi_brier": 0.1771, "brier_diff_model_minus_kalshi": 0.1107}, "5-10": {"n_settled": 398, "model_brier": 0.2012, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": -0.0022}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.566, "slope": 0.879, "slope_se": 0.057}, "kalshi_slope": {"intercept": 0.226, "slope": 1.127, "slope_se": 0.065}, "n": 1944}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 213, "model_brier": 0.3188, "kalshi_brier": 0.2271, "brier_diff_model_minus_kalshi": 0.0917, "brier_diff_se": 0.0216, "corr_model_outcome": -0.0023, "corr_kalshi_outcome": 0.3188}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
