# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-20T22:18Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 45,021): 0-3 14.2%, 3-5 9.5%, 5-10 19.7%, 10-15 15.4%, 15-25 19.3%, 25-40 14.0%, 40+ 8.0%; median gap 12.04 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.8%, Challenger 12.6%, doubles 6.8%). Main tour: ATP 4.9% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 9,901): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.6%, BOOK_QUALITY 19.0%, STALE_QUOTE 17.6%, POOR_DATA 8.9%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.6%, execution 19.0%, market_freshness 17.6%, data 12.7%, market_freshness/coverage 8.8%, mapping 4.3%, model_calibration_or_unknown 2.2%, model_calibration 0.7%.
* **Stale / settled / in-play**: 51.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 9,901 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.6%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.0% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 507.0 points vs 1754.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.047, Gen-2 0.845, Gen-1 ledger 0.875 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 475 model 0.2251 vs Kalshi 0.2105; n 94 model 0.3003 vs Kalshi 0.1784.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 192,748 model-market comparisons (313,027 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 66,132 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-20T22:04:09.381127+00:00'], shadow board 50,728 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-20T22:04:14.863624+00:00'], Model 4 24,213 rows, 17,771 settled tickers, 6,023 tickers with an external scan.
* By model: {"gen1_ledger": 44687, "gen1_elo": 25507, "fair_v1": 25507, "gen2": 25507, "gen1_sr": 25507, "model4_fundamental": 23030, "model4_conditioned": 23003}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 45,021 | 14.2 | 9.5 | 19.7 | 15.4 | 19.3 | 14.0 | 8.0 | 12.04 | 41.3% | 22.0% |
| MW fair_v1 | 25,507 | 13.2 | 8.5 | 18.2 | 15.7 | 20.0 | 14.9 | 9.6 | 13.14 | 44.4% | 24.4% |
| MW gen1_elo | 25,507 | 12.9 | 8.8 | 19.2 | 15.2 | 19.8 | 14.9 | 9.2 | 12.85 | 44.0% | 24.1% |
| MW gen1_ledger | 19,514 | 15.4 | 10.7 | 21.7 | 14.9 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| MW gen1_sr | 25,507 | 9.9 | 7.2 | 16.6 | 14.1 | 21.4 | 18.7 | 12.1 | 15.87 | 52.2% | 30.8% |
| MW gen2 | 25,507 | 11.1 | 7.3 | 16.2 | 14.2 | 20.1 | 17.8 | 13.3 | 15.52 | 51.1% | 31.1% |
| all families model4_conditioned | 23,003 | 21.8 | 19.2 | 34.3 | 17.7 | 4.6 | 1.4 | 1.1 | 5.94 | 7.0% | 2.4% |
| all families model4_fundamental | 23,030 | 16.3 | 13.0 | 34.1 | 20.5 | 11.4 | 3.4 | 1.4 | 7.91 | 16.2% | 4.8% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.7%, >=15pp 41.3%, >=20pp 30.6%, >=25pp 22.0%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.41pp; >=10pp 45.1%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,244 | 28.4 | 13.8 | 24.5 | 15.2 | 12.3 | 5.2 | 0.6 | 6.31 | 18.1% | 5.8% |
| CHALLENGER | 4,264 | 15.5 | 10.1 | 20.2 | 15.8 | 15.0 | 12.6 | 10.9 | 11.32 | 38.5% | 23.4% |
| ITF_MEN | 6,753 | 10.9 | 7.7 | 17.0 | 14.4 | 20.9 | 17.1 | 12.0 | 14.99 | 50.0% | 29.1% |
| ITF_WOMEN | 10,032 | 9.7 | 6.7 | 15.5 | 15.6 | 23.1 | 18.3 | 11.2 | 15.92 | 52.6% | 29.5% |
| WTA | 1,554 | 17.3 | 12.3 | 24.5 | 20.3 | 20.5 | 4.4 | 0.7 | 8.85 | 25.6% | 5.1% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,244 | 23.3 | 14.9 | 24.5 | 17.2 | 14.0 | 5.2 | 0.8 | 6.85 | 20.1% | 6.1% |
| CHALLENGER | 4,264 | 14.5 | 8.5 | 18.7 | 14.5 | 17.8 | 14.0 | 11.9 | 12.7 | 43.8% | 26.0% |
| ITF_MEN | 6,753 | 8.9 | 6.4 | 15.0 | 13.3 | 19.7 | 20.3 | 16.4 | 17.82 | 56.4% | 36.7% |
| ITF_WOMEN | 10,032 | 8.2 | 5.6 | 13.4 | 13.5 | 21.6 | 21.0 | 16.8 | 18.97 | 59.4% | 37.8% |
| WTA | 1,554 | 14.6 | 9.5 | 20.0 | 16.6 | 24.4 | 14.2 | 0.8 | 11.67 | 39.3% | 14.9% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,244 | 23.8 | 13.1 | 24.3 | 16.0 | 15.2 | 6.5 | 1.1 | 7.26 | 22.8% | 7.6% |
| CHALLENGER | 4,264 | 14.1 | 9.6 | 20.9 | 15.2 | 16.2 | 12.9 | 11.1 | 11.41 | 40.2% | 24.0% |
| ITF_MEN | 6,753 | 10.2 | 7.8 | 17.2 | 13.8 | 21.5 | 17.4 | 12.1 | 15.44 | 51.0% | 29.5% |
| ITF_WOMEN | 10,032 | 9.3 | 6.7 | 16.2 | 15.7 | 23.2 | 18.5 | 10.3 | 15.83 | 52.1% | 28.8% |
| WTA | 1,554 | 24.3 | 16.6 | 30.2 | 16.0 | 10.2 | 2.2 | 0.5 | 6.01 | 12.9% | 2.6% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,279 | 26.6 | 19.9 | 29.5 | 12.0 | 8.6 | 3.1 | 0.4 | 5.38 | 12.1% | 3.5% |
| CHALLENGER | 2,963 | 21.2 | 14.7 | 26.8 | 14.1 | 14.8 | 6.4 | 1.9 | 7.29 | 23.2% | 8.3% |
| DOUBLES | 1,393 | 4.8 | 4.1 | 11.6 | 10.4 | 20.8 | 25.8 | 22.5 | 24.11 | 69.1% | 48.3% |
| ITF_MEN | 5,427 | 14.1 | 8.8 | 20.6 | 15.9 | 20.4 | 13.3 | 6.8 | 11.97 | 40.6% | 20.2% |
| ITF_WOMEN | 6,562 | 12.2 | 8.9 | 19.2 | 15.2 | 21.8 | 16.6 | 6.1 | 13.04 | 44.5% | 22.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,009 | 22.1 | 15.8 | 29.7 | 18.1 | 10.3 | 3.7 | 0.3 | 7.04 | 14.3% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,187 | 28.8 | 14.0 | 24.9 | 15.0 | 12.0 | 4.8 | 0.6 | 6.16 | 17.3% | 5.3% |
| CHALLENGER | 3,005 | 20.3 | 12.4 | 24.9 | 18.3 | 15.4 | 6.7 | 2.1 | 8.44 | 24.2% | 8.7% |
| ITF_MEN | 4,958 | 13.2 | 9.3 | 20.2 | 16.4 | 21.6 | 13.9 | 5.3 | 12.06 | 40.8% | 19.2% |
| ITF_WOMEN | 7,505 | 11.4 | 8.1 | 17.6 | 17.8 | 24.9 | 15.3 | 4.9 | 13.53 | 45.1% | 20.2% |
| WTA | 1,513 | 17.5 | 12.0 | 24.4 | 20.5 | 20.4 | 4.4 | 0.7 | 8.85 | 25.5% | 5.1% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,187 | 23.6 | 15.2 | 24.6 | 17.0 | 14.0 | 4.9 | 0.7 | 6.63 | 19.6% | 5.6% |
| CHALLENGER | 3,005 | 18.2 | 10.9 | 23.4 | 17.4 | 18.0 | 9.8 | 2.3 | 9.4 | 30.1% | 12.1% |
| ITF_MEN | 4,959 | 10.6 | 7.7 | 17.2 | 15.1 | 21.7 | 18.3 | 9.4 | 14.88 | 49.5% | 27.7% |
| ITF_WOMEN | 7,505 | 9.2 | 6.4 | 14.8 | 15.0 | 23.7 | 20.4 | 10.6 | 16.66 | 54.6% | 31.0% |
| WTA | 1,513 | 14.6 | 9.4 | 20.0 | 16.5 | 24.4 | 14.3 | 0.8 | 11.71 | 39.5% | 15.1% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,239 | 26.8 | 20.1 | 29.5 | 12.2 | 8.2 | 3.0 | 0.2 | 5.33 | 11.4% | 3.2% |
| CHALLENGER | 2,576 | 22.7 | 15.7 | 28.5 | 14.1 | 14.2 | 4.2 | 0.6 | 6.72 | 19.1% | 4.8% |
| DOUBLES | 1,295 | 4.9 | 4.2 | 11.7 | 10.6 | 20.8 | 25.9 | 21.9 | 23.94 | 68.6% | 47.8% |
| ITF_MEN | 4,516 | 15.5 | 9.5 | 22.4 | 16.6 | 20.1 | 11.7 | 4.1 | 10.77 | 35.9% | 15.8% |
| ITF_WOMEN | 5,458 | 13.1 | 9.4 | 20.6 | 16.0 | 22.1 | 15.3 | 3.5 | 11.84 | 40.8% | 18.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 962 | 22.6 | 16.2 | 29.8 | 18.2 | 10.3 | 2.9 | 0.0 | 6.85 | 13.2% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,393 | 4.8 | 4.1 | 11.6 | 10.4 | 20.8 | 25.8 | 22.5 | 24.11 | 69.1% | 48.3% |
| singles | 18,121 | 16.2 | 11.2 | 22.4 | 15.3 | 18.3 | 11.8 | 4.7 | 10.03 | 34.8% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,750 | 13.4 | 8.8 | 19.1 | 15.7 | 18.8 | 14.8 | 9.6 | 12.77 | 43.1% | 24.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 16,138 | 13.5 | 8.5 | 18.3 | 15.4 | 20.2 | 14.7 | 9.4 | 13.14 | 44.3% | 24.1% |
| UNKNOWN | 3,382 | 11.4 | 8.0 | 16.6 | 17.3 | 20.7 | 15.9 | 10.2 | 13.78 | 46.8% | 26.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,341 | 19.7 | 11.4 | 21.1 | 16.8 | 16.0 | 9.0 | 6.0 | 9.36 | 31.0% | 15.0% |
| B | 3,264 | 12.5 | 9.1 | 19.9 | 17.2 | 18.9 | 12.0 | 10.4 | 12.2 | 41.4% | 22.5% |
| C | 3,577 | 12.2 | 8.8 | 18.8 | 14.8 | 19.8 | 15.5 | 10.1 | 13.3 | 45.4% | 25.6% |
| D | 4,176 | 12.2 | 7.8 | 16.8 | 15.6 | 22.2 | 16.0 | 9.5 | 14.09 | 47.7% | 25.5% |
| F | 7,149 | 7.9 | 5.6 | 15.0 | 14.4 | 23.3 | 21.3 | 12.5 | 17.8 | 57.1% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,592 | 23.2 | 15.8 | 28.5 | 15.1 | 11.8 | 4.1 | 1.5 | 6.68 | 17.3% | 5.5% |
| B | 2,728 | 15.9 | 10.5 | 24.1 | 16.1 | 18.8 | 10.8 | 3.9 | 9.92 | 33.5% | 14.7% |
| C | 3,843 | 10.9 | 7.2 | 18.4 | 14.4 | 21.8 | 16.3 | 10.9 | 14.46 | 49.0% | 27.2% |
| D | 2,803 | 13.9 | 9.7 | 19.7 | 14.7 | 21.1 | 14.7 | 6.2 | 12.11 | 41.9% | 20.9% |
| F | 4,548 | 10.3 | 8.0 | 15.7 | 14.6 | 22.2 | 20.6 | 8.6 | 15.75 | 51.4% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,355 | 17.8 | 10.2 | 20.4 | 16.8 | 16.5 | 9.8 | 8.4 | 10.43 | 34.7% | 18.2% |
| LIMITED | 5,597 | 13.9 | 10.2 | 20.0 | 15.6 | 19.2 | 13.6 | 7.5 | 11.8 | 40.4% | 21.1% |
| POOR | 11,555 | 9.5 | 6.5 | 15.7 | 14.9 | 22.8 | 19.1 | 11.4 | 16.16 | 53.4% | 30.5% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,913 | 26.7 | 20.9 | 34.4 | 11.9 | 4.4 | 1.5 | 0.2 | 5.2 | 6.1% | 1.7% |
| GAME_SPREAD | 4,273 | 23.0 | 15.3 | 33.4 | 17.1 | 8.6 | 2.3 | 0.3 | 6.54 | 11.2% | 2.6% |
| MATCH_WINNER | 19,514 | 15.4 | 10.7 | 21.7 | 14.9 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,042 | 29.9 | 16.9 | 30.4 | 12.7 | 8.2 | 1.6 | 0.4 | 5.41 | 10.2% | 2.1% |
| TOTAL_GAMES | 6,921 | 8.0 | 9.2 | 36.5 | 29.2 | 10.9 | 3.4 | 2.8 | 9.59 | 17.1% | 6.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,043 | 25.4 | 34.6 | 32.1 | 4.0 | 3.2 | 0.6 | 0.1 | 4.45 | 3.9% | 0.7% |
| GAME_SPREAD | 5,504 | 45.9 | 17.0 | 26.9 | 7.6 | 1.8 | 0.6 | 0.2 | 3.41 | 2.6% | 0.8% |
| TOTAL_GAMES | 9,456 | 4.8 | 7.3 | 40.5 | 35.2 | 7.4 | 2.4 | 2.3 | 9.73 | 12.2% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,046 | 24.2 | 17.9 | 35.4 | 12.4 | 7.3 | 2.6 | 0.3 | 5.81 | 10.2% | 2.9% |
| GAME_SPREAD | 5,507 | 19.1 | 13.2 | 28.2 | 20.0 | 14.4 | 4.2 | 0.9 | 7.98 | 19.5% | 5.1% |
| TOTAL_GAMES | 9,477 | 7.9 | 8.8 | 36.4 | 27.7 | 13.1 | 3.7 | 2.5 | 9.67 | 19.3% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 25,507 | 44.4% | 24.4% | 13.14 | 36.0% | 15.2% | 10.94 |
| gen1_elo | 25,507 | 44.0% | 24.1% | 12.85 | 35.3% | 15.3% | 10.52 |
| gen1_sr | 25,507 | 52.2% | 30.8% | 15.87 | 44.5% | 21.6% | 13.13 |
| gen2 | 25,507 | 51.1% | 31.1% | 15.52 | 44.6% | 23.2% | 13.12 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 13,479 | 15.9 | 10.3 | 21.0 | 17.4 | 20.4 | 11.8 | 3.3 | 10.8 | 35.4% | 15.0% |
| STALE | 12,028 | 10.1 | 6.5 | 15.1 | 13.8 | 19.4 | 18.4 | 16.6 | 17.14 | 54.4% | 35.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 12,982 | 16.6 | 11.3 | 22.6 | 15.0 | 17.5 | 12.2 | 4.8 | 9.86 | 34.5% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 45,021 | 12982 | 16951 | 15088 | 23.9 | 133.0 | 1400.4 |
| ge_15pp | 18,602 | 4480 | 6066 | 8056 | 25.7 | 433.3 | 1380.4 |
| ge_25pp | 9,901 | 2207 | 2616 | 5078 | 31.4 | 574.8 | 1380.4 |
| lt_10pp | 19,506 | 6555 | 7996 | 4955 | 21.7 | 47.3 | 1341.5 |

Current slate `SL-20261020T221846Z-57911799`: 754 priced rows, quote age at build {'median': 14.9, 'max': 15.0}, freshness {'AGING': 754}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 12 | 0.0 | 0.0 | 33.3 | 0.0 | 50.0 | 16.7 | 0.0 | 20.33 | 66.7% | 16.7% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,363 | 19.9 | 10.9 | 23.4 | 18.8 | 19.3 | 7.0 | 0.7 | 9.1 | 27.0% | 7.7% |
| KALSHI_LONE_OUTLIER | 14 | 7.1 | 7.1 | 71.4 | 0.0 | 7.1 | 7.1 | 0.0 | 5.35 | 14.3% | 7.1% |
| MARKETS_AGREE | 427 | 68.4 | 31.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.11 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 943 | 0.0 | 2.5 | 33.8 | 27.1 | 25.8 | 10.0 | 0.7 | 12.55 | 36.5% | 10.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 25,507 | 3771 (14.8%) | 25.0% | 0.7% | {"EXTERNAL_STALE": 2363, "AGREES_WITH_KALSHI": 943, "ALL_AGREE": 427, "AGREES_WITH_MODEL": 14, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 11, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 11,323 | 991 (8.8%) | 34.7% | 1.0% | {"EXTERNAL_STALE": 637, "AGREES_WITH_KALSHI": 344, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,232 | 286 (4.6%) | 35.3% | 1.1% | {"EXTERNAL_STALE": 182, "AGREES_WITH_KALSHI": 101, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,021 | 269 (8.9%) | 36.1% | 1.1% | {"EXTERNAL_STALE": 169, "AGREES_WITH_KALSHI": 97, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 10,182 | 2080 (20.4%) | 16.5% | 0.7% | {"EXTERNAL_STALE": 1282, "ALL_AGREE": 427, "AGREES_WITH_KALSHI": 343, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 12, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,928 | 10.7 | 7.7 | 19.2 | 14.6 | 22.2 | 15.7 | 9.9 | 14.01 | 47.8% | 25.7% |
| 4-10x | 3,321 | 11.6 | 8.4 | 18.6 | 15.5 | 21.1 | 14.9 | 10.0 | 13.67 | 46.0% | 24.9% |
| <2x | 13,108 | 15.2 | 9.5 | 18.7 | 16.7 | 18.2 | 13.1 | 8.5 | 11.92 | 39.9% | 21.6% |
| >=10x | 4,150 | 11.1 | 6.5 | 15.2 | 13.9 | 21.9 | 19.4 | 12.1 | 16.31 | 53.4% | 31.5% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,485 | 12.5 | 8.4 | 19.5 | 16.2 | 19.7 | 13.7 | 10.0 | 12.91 | 43.4% | 23.7% |
| 300-1000 | 5,559 | 11.8 | 8.6 | 16.7 | 15.5 | 21.1 | 16.4 | 9.9 | 14.09 | 47.3% | 26.3% |
| <300 | 8,042 | 9.0 | 5.8 | 15.3 | 14.6 | 23.0 | 20.2 | 12.1 | 16.92 | 55.3% | 32.3% |
| >=3000 | 5,421 | 21.5 | 12.6 | 22.6 | 16.9 | 14.7 | 6.9 | 4.8 | 8.11 | 26.4% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 759 | 0.5446 | 0.4091 | 0.4954 | +0.049 | -0.086 | -0.0014 ± 0.0055 |
| ratio 4-10x | 516 | 0.5905 | 0.4449 | 0.5039 | +0.087 | -0.059 | 0.0121 ± 0.0071 |
| ratio <2x | 1851 | 0.537 | 0.4147 | 0.4506 | +0.086 | -0.036 | 0.0123 ± 0.0033 |
| ratio >=10x | 643 | 0.5645 | 0.3904 | 0.4588 | +0.106 | -0.068 | 0.0075 ± 0.0072 |
| thinner_sample 1000-3000 | 1034 | 0.5422 | 0.4161 | 0.4536 | +0.089 | -0.037 | 0.0101 ± 0.0044 |
| thinner_sample 300-1000 | 881 | 0.5662 | 0.4245 | 0.5006 | +0.066 | -0.076 | -0.0008 ± 0.0054 |
| thinner_sample <300 | 1221 | 0.5548 | 0.39 | 0.4554 | +0.099 | -0.065 | 0.0123 ± 0.005 |
| thinner_sample >=3000 | 633 | 0.5342 | 0.4396 | 0.4724 | +0.062 | -0.033 | 0.0126 ± 0.0046 |
| data_status ADEQUATE | 1083 | 0.5371 | 0.4325 | 0.4608 | +0.076 | -0.028 | 0.0113 ± 0.0038 |
| data_status LIMITED | 914 | 0.5516 | 0.4194 | 0.4814 | +0.070 | -0.062 | 0.0046 ± 0.0049 |
| data_status POOR | 1772 | 0.5582 | 0.399 | 0.4661 | +0.092 | -0.067 | 0.0092 ± 0.0041 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 562 | 0.1969 | 0.1983 | -0.0014 ± 0.0007 | 0.5723 | 0.5754 | 0.4992 | 0.4843 | 0.5374 | -0.049 ± 0.0196 | -0.01 (5) |
| 3-5 | 356 | 0.2004 | 0.2 | +0.0004 ± 0.0019 | 0.5837 | 0.5814 | 0.5039 | 0.4637 | 0.4775 | -0.090 ± 0.0245 | 0.02 (1) |
| 5-10 | 782 | 0.2009 | 0.2013 | -0.0004 ± 0.0024 | 0.5877 | 0.5865 | 0.5134 | 0.4389 | 0.4744 | -0.083 ± 0.0167 | -0.0167 (6) |
| 10-15 | 655 | 0.2131 | 0.2034 | +0.0097 ± 0.0044 | 0.6157 | 0.5881 | 0.5241 | 0.3999 | 0.4229 | -0.100 ± 0.0176 | -0.048 (5) |
| 15-25 | 845 | 0.2255 | 0.2149 | +0.0106 ± 0.0062 | 0.6461 | 0.6143 | 0.5781 | 0.3823 | 0.4533 | -0.085 ± 0.0158 | -0.0033 (9) |
| 25-40 | 475 | 0.2251 | 0.2105 | +0.0146 ± 0.0125 | 0.6384 | 0.6048 | 0.6548 | 0.3466 | 0.4737 | -0.072 ± 0.0192 | -0.01 (1) |
| 40+ | 94 | 0.3003 | 0.1784 | +0.1219 ± 0.039 | 0.8189 | 0.5303 | 0.7523 | 0.3041 | 0.3936 | -0.119 ± 0.0377 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2774 | 0.1826 | 0.1837 | -0.0011 ± 0.0003 | 0.5401 | 0.5414 | 0.4799 | 0.4648 | 0.5032 | -0.018 ± 0.0082 | -0.0129 (17) |
| 3-5 | 1827 | 0.1954 | 0.1942 | +0.0012 ± 0.0008 | 0.5716 | 0.5653 | 0.4832 | 0.4432 | 0.4472 | -0.053 ± 0.0105 | 0.0 (2) |
| 5-10 | 3858 | 0.1961 | 0.1931 | +0.0030 ± 0.0011 | 0.5749 | 0.5652 | 0.486 | 0.4121 | 0.4274 | -0.048 ± 0.0072 | -0.0119 (21) |
| 10-15 | 3369 | 0.2028 | 0.1847 | +0.0182 ± 0.0019 | 0.5933 | 0.5426 | 0.4852 | 0.3607 | 0.35 | -0.074 ± 0.0074 | -0.0281 (16) |
| 15-25 | 4212 | 0.2089 | 0.1717 | +0.0371 ± 0.0025 | 0.6112 | 0.5073 | 0.5014 | 0.305 | 0.3091 | -0.069 ± 0.0063 | -0.0025 (44) |
| 25-40 | 3260 | 0.2236 | 0.1298 | +0.0938 ± 0.0039 | 0.6417 | 0.3971 | 0.5311 | 0.2185 | 0.2282 | -0.062 ± 0.0061 | -0.01 (1) |
| 40+ | 2106 | 0.3798 | 0.0446 | +0.3352 ± 0.0052 | 0.9892 | 0.1732 | 0.6319 | 0.1069 | 0.0622 | -0.081 ± 0.0043 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 418 | 0.2006 | 0.2011 | -0.0006 ± 0.0008 | 0.5828 | 0.584 | 0.5008 | 0.4859 | 0.5096 | -0.089 ± 0.0235 | -0.01 (3) |
| 3-5 | 313 | 0.2201 | 0.2187 | +0.0013 ± 0.0021 | 0.6257 | 0.6232 | 0.5129 | 0.4728 | 0.4696 | -0.109 ± 0.0286 | 0.02 (1) |
| 5-10 | 665 | 0.1991 | 0.2002 | -0.0011 ± 0.0026 | 0.5815 | 0.5837 | 0.5471 | 0.4722 | 0.5173 | -0.069 ± 0.0178 | -0.01 (4) |
| 10-15 | 624 | 0.2181 | 0.2121 | +0.0061 ± 0.0046 | 0.6265 | 0.6109 | 0.5646 | 0.4402 | 0.4808 | -0.096 ± 0.0191 | -0.04 (5) |
| 15-25 | 903 | 0.2311 | 0.2113 | +0.0198 ± 0.006 | 0.6557 | 0.6055 | 0.5919 | 0.3955 | 0.4474 | -0.097 ± 0.0155 | -0.0133 (9) |
| 25-40 | 623 | 0.2628 | 0.2 | +0.0628 ± 0.0113 | 0.7336 | 0.5811 | 0.6581 | 0.3424 | 0.4029 | -0.110 ± 0.0176 | -0.0075 (4) |
| 40+ | 223 | 0.3649 | 0.1671 | +0.1978 ± 0.0271 | 1.0086 | 0.5006 | 0.7374 | 0.2555 | 0.3049 | -0.088 ± 0.0262 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2307 | 0.1882 | 0.1886 | -0.0004 ± 0.0003 | 0.5537 | 0.5544 | 0.5013 | 0.4865 | 0.5076 | -0.036 ± 0.0094 | -0.0133 (15) |
| 3-5 | 1581 | 0.198 | 0.198 | -0.0001 ± 0.0009 | 0.5739 | 0.5739 | 0.511 | 0.471 | 0.4908 | -0.034 ± 0.0115 | 0.02 (1) |
| 5-10 | 3425 | 0.1923 | 0.1914 | +0.0009 ± 0.0011 | 0.5674 | 0.5614 | 0.5056 | 0.4316 | 0.4642 | -0.028 ± 0.0076 | -0.0117 (6) |
| 10-15 | 3024 | 0.2003 | 0.1899 | +0.0104 ± 0.002 | 0.5881 | 0.5526 | 0.5142 | 0.3901 | 0.412 | -0.048 ± 0.008 | -0.0189 (18) |
| 15-25 | 4326 | 0.2175 | 0.1803 | +0.0371 ± 0.0026 | 0.632 | 0.5287 | 0.5296 | 0.3333 | 0.34 | -0.067 ± 0.0065 | -0.0086 (42) |
| 25-40 | 3823 | 0.2507 | 0.1391 | +0.1116 ± 0.0038 | 0.7063 | 0.4256 | 0.5619 | 0.2454 | 0.2302 | -0.083 ± 0.006 | -0.0044 (18) |
| 40+ | 2920 | 0.3988 | 0.0623 | +0.3364 ± 0.0053 | 1.0506 | 0.221 | 0.6582 | 0.1223 | 0.089 | -0.072 ± 0.0045 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 537 | 0.1977 | 0.2001 | -0.0024 ± 0.0007 | 0.5755 | 0.5812 | 0.4952 | 0.4798 | 0.5531 | -0.013 ± 0.0197 | -0.0137 (8) |
| 3-5 | 390 | 0.1944 | 0.1923 | +0.0021 ± 0.0018 | 0.5666 | 0.5616 | 0.5032 | 0.4636 | 0.459 | -0.118 ± 0.0232 | 0.0067 (3) |
| 5-10 | 807 | 0.2015 | 0.1987 | +0.0028 ± 0.0024 | 0.5901 | 0.5799 | 0.5109 | 0.437 | 0.4523 | -0.095 ± 0.0161 | -0.0071 (7) |
| 10-15 | 655 | 0.2095 | 0.2055 | +0.0041 ± 0.0044 | 0.6069 | 0.5933 | 0.5395 | 0.4162 | 0.4641 | -0.085 ± 0.0176 | -0.0317 (6) |
| 15-25 | 793 | 0.2329 | 0.2122 | +0.0207 ± 0.0064 | 0.665 | 0.608 | 0.5853 | 0.3915 | 0.4351 | -0.112 ± 0.0163 | -0.03 (1) |
| 25-40 | 489 | 0.2138 | 0.2183 | -0.0044 ± 0.0124 | 0.6144 | 0.6232 | 0.6641 | 0.3533 | 0.5133 | -0.049 ± 0.0189 | 0.015 (2) |
| 40+ | 98 | 0.3093 | 0.1956 | +0.1137 ± 0.0399 | 0.8461 | 0.5688 | 0.7622 | 0.3107 | 0.4184 | -0.098 ± 0.0411 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2694 | 0.186 | 0.1867 | -0.0008 ± 0.0003 | 0.5477 | 0.549 | 0.487 | 0.4717 | 0.4892 | -0.035 ± 0.0084 | -0.0163 (35) |
| 3-5 | 1846 | 0.1864 | 0.1836 | +0.0028 ± 0.0008 | 0.5501 | 0.5433 | 0.4831 | 0.4436 | 0.4296 | -0.074 ± 0.0102 | -0.0094 (18) |
| 5-10 | 4047 | 0.1968 | 0.1912 | +0.0056 ± 0.001 | 0.578 | 0.5592 | 0.4872 | 0.4134 | 0.4109 | -0.062 ± 0.0069 | -0.01 (31) |
| 10-15 | 3217 | 0.1972 | 0.1803 | +0.0170 ± 0.0019 | 0.5793 | 0.5309 | 0.5017 | 0.3781 | 0.3715 | -0.073 ± 0.0075 | -0.015 (12) |
| 15-25 | 4340 | 0.2128 | 0.1733 | +0.0395 ± 0.0025 | 0.62 | 0.5113 | 0.5084 | 0.3138 | 0.3097 | -0.075 ± 0.0063 | -0.03 (2) |
| 25-40 | 3216 | 0.2193 | 0.1313 | +0.0881 ± 0.004 | 0.6325 | 0.3995 | 0.5331 | 0.2171 | 0.2379 | -0.054 ± 0.0061 | 0.01 (3) |
| 40+ | 2046 | 0.3946 | 0.0495 | +0.3452 ± 0.0056 | 1.0314 | 0.1859 | 0.6443 | 0.1138 | 0.067 | -0.084 ± 0.0047 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 899 | 0.1955 | 0.1957 | -0.0002 ± 0.0005 | 0.5708 | 0.5709 | 0.5061 | 0.491 | 0.4939 | -0.058 ± 0.0149 | -0.0224 (49) |
| 3-5 | 625 | 0.1925 | 0.1921 | +0.0005 ± 0.0014 | 0.5625 | 0.5604 | 0.4837 | 0.4438 | 0.456 | -0.051 ± 0.0177 | -0.0194 (34) |
| 5-10 | 1326 | 0.2001 | 0.1937 | +0.0064 ± 0.0018 | 0.588 | 0.569 | 0.491 | 0.4177 | 0.4125 | -0.071 ± 0.0123 | -0.005 (78) |
| 10-15 | 862 | 0.2087 | 0.1976 | +0.0111 ± 0.0038 | 0.6058 | 0.5769 | 0.5163 | 0.3932 | 0.4084 | -0.066 ± 0.0154 | 0.0014 (64) |
| 15-25 | 1149 | 0.2313 | 0.2114 | +0.0199 ± 0.0053 | 0.6603 | 0.609 | 0.5724 | 0.3776 | 0.4256 | -0.064 ± 0.0136 | -0.0214 (59) |
| 25-40 | 699 | 0.2499 | 0.2044 | +0.0455 ± 0.0105 | 0.7085 | 0.5888 | 0.6637 | 0.3509 | 0.4335 | -0.086 ± 0.0159 | -0.0219 (26) |
| 40+ | 239 | 0.3512 | 0.196 | +0.1552 ± 0.0285 | 1.014 | 0.5738 | 0.8045 | 0.3194 | 0.4226 | -0.082 ± 0.0255 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2946 | 0.1833 | 0.1834 | -0.0002 ± 0.0003 | 0.5396 | 0.5392 | 0.5065 | 0.4911 | 0.5 | -0.038 ± 0.0079 | -0.0157 (88) |
| 3-5 | 2012 | 0.1907 | 0.1888 | +0.0019 ± 0.0008 | 0.5579 | 0.554 | 0.4884 | 0.4487 | 0.4443 | -0.053 ± 0.0098 | -0.0209 (69) |
| 5-10 | 4062 | 0.1968 | 0.1878 | +0.0090 ± 0.001 | 0.5786 | 0.5531 | 0.4871 | 0.4136 | 0.3922 | -0.074 ± 0.0069 | -0.0082 (132) |
| 10-15 | 2816 | 0.2048 | 0.19 | +0.0148 ± 0.002 | 0.5979 | 0.5585 | 0.5227 | 0.3997 | 0.4006 | -0.060 ± 0.0082 | -0.0053 (105) |
| 15-25 | 3460 | 0.2288 | 0.1986 | +0.0302 ± 0.003 | 0.6597 | 0.5771 | 0.5648 | 0.3696 | 0.3916 | -0.063 ± 0.0076 | -0.0253 (107) |
| 25-40 | 2422 | 0.26 | 0.1823 | +0.0777 ± 0.0055 | 0.7364 | 0.5328 | 0.6244 | 0.3099 | 0.3464 | -0.075 ± 0.0085 | -0.0229 (51) |
| 40+ | 1096 | 0.3765 | 0.1396 | +0.2369 ± 0.0119 | 1.0663 | 0.4231 | 0.7247 | 0.2212 | 0.2509 | -0.072 ± 0.0105 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3769 | 1.047 ± 0.046 | 1.167 | 0.1669 | 0.1647 | 0.2134 | 0.2047 |
| gen2 | 3769 | 0.845 ± 0.042 | 1.128 | 0.1707 | 0.1652 | 0.2322 | 0.2045 |
| gen1_elo | 3769 | 1.025 ± 0.045 | 1.15 | 0.1735 | 0.165 | 0.2126 | 0.2047 |
| gen1_sr | 3769 | 1.045 ± 0.055 | 1.205 | 0.1313 | 0.1671 | 0.2285 | 0.2041 |
| gen1_ledger | 5799 | 0.875 ± 0.032 | 1.086 | 0.1801 | 0.1798 | 0.2183 | 0.1993 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 18,602)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,298 | 23.1% |
| STALE_QUOTE | market_freshness | 3,827 | 20.6% |
| BOOK_QUALITY | execution | 3,595 | 19.3% |
| POOR_DATA | data | 2,118 | 11.4% |
| LIMITED_DATA | data | 1,234 | 6.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,007 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 937 | 5.0% |
| IDENTITY_AMBIGUOUS | mapping | 743 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 539 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 304 | 1.6% |

Cause class: coverage 23.1%, market_freshness 20.6%, execution 19.3%, data 18.0%, market_freshness/coverage 8.3%, model_calibration_or_unknown 5.0%, mapping 4.0%, model_calibration 1.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.0%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 70.4%, THIN_PLAYER_HISTORY 59.2%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 43.3%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 32.6%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.3%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.9%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.6%, POST_SETTLEMENT_OBSERVATION 23.1%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 9,901)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,423 | 34.6% |
| BOOK_QUALITY | execution | 1,880 | 19.0% |
| STALE_QUOTE | market_freshness | 1,746 | 17.6% |
| POOR_DATA | data | 885 | 8.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 530 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 431 | 4.3% |
| LIMITED_DATA | data | 376 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 338 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 219 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 73 | 0.7% |

Cause class: coverage 34.6%, execution 19.0%, market_freshness 17.6%, data 12.7%, market_freshness/coverage 8.8%, mapping 4.3%, model_calibration_or_unknown 2.2%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.3%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.3%, THIN_PLAYER_HISTORY 61.8%, STALE_KALSHI_QUOTE 51.3%, STALE_PLAYER_DATA 47.1%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 24.9%, PLAYER_IDENTITY_RISK 18.6%, MODEL_HIGH_UNCERTAINTY 18.3%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.6%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.6%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7797, "IDENTITY_AMBIGUOUS": 2104}; ticker orientation: {"VERIFIED": 9901}.

Checks: discipline:AMBIGUOUS 673, discipline:PASS 9228, identity_confidence:AMBIGUOUS 1843, identity_confidence:PASS 8058, level_mapping:NA 685, level_mapping:PASS 9216, market_pair:AMBIGUOUS 363, market_pair:NA 240, market_pair:PASS 9298, model_complement:NA 207, model_complement:PASS 9694, namesake:PASS 9901, physical_match_id:NA 3669, physical_match_id:PASS 6232, player_ids:PASS 9901, same_pair_other_event:PASS 9901, ticker_orientation:PASS 9901

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,523 | 4.9% | 4.5% | 1.8% | {"market_freshness": 52, "model_calibration_or_unknown": 39, "data": 33, "execution": 19, "model_calibration": 13, "market_freshness/coverage": 11, "coverage": 7} | 5.88 | 0.2252 / 0.2152 (395) | 18.4% | 3.9% | 3.5% | 2.8% |
| CHALLENGER | 7,227 | 17.2% | 6.9% | 12.6% | {"coverage": 705, "market_freshness/coverage": 155, "market_freshness": 145, "data": 112, "model_calibration_or_unknown": 58, "execution": 30, "model_calibration": 27, "mapping": 14} | 7.49 | 0.2173 / 0.2074 (1756) | 35.1% | 17.1% | 3.9% | 22.8% |
| DOUBLES | 1,393 | 48.3% | 47.8% | 6.8% | {"execution": 336, "mapping": 177, "market_freshness": 106, "market_freshness/coverage": 47, "coverage": 7} | 23.94 | 0.3222 / 0.2343 (361) | 16.8% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 12,180 | 25.1% | 17.6% | 30.9% | {"coverage": 1144, "execution": 627, "market_freshness": 482, "data": 417, "market_freshness/coverage": 251, "mapping": 136, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.49 | 0.2143 / 0.1949 (2820) | 36.2% | 65.4% | 16.5% | 22.2% |
| ITF_WOMEN | 16,594 | 26.8% | 19.6% | 44.9% | {"coverage": 1543, "market_freshness": 884, "execution": 837, "data": 665, "market_freshness/coverage": 355, "mapping": 98, "model_calibration_or_unknown": 51, "model_calibration": 10} | 12.92 | 0.203 / 0.1948 (3287) | 37.9% | 57.9% | 10.2% | 21.9% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,563 | 4.6% | 4.2% | 1.2% | {"market_freshness": 37, "model_calibration_or_unknown": 28, "execution": 17, "model_calibration": 11, "data": 11, "market_freshness/coverage": 10, "coverage": 4, "mapping": 1} | 7.96 | 0.2365 / 0.2304 (419) | 23.6% | 1.3% | 1.4% | 3.4% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.8% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 15 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 16 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 17 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 18 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 19 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 20 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 21 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 22 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 23 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 24 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 25 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 26 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 27 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 30 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 31 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 32 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 36 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 37 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 38 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 39 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 41 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 42 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 43 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 44 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 45 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 46 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 770 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 47 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 48 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9704, "by_level_share_of_ge_25pp": {"ATP": 0.0176, "CHALLENGER": 0.1258, "DOUBLES": 0.068, "ITF_MEN": 0.3091, "ITF_WOMEN": 0.4487, "OTHER": 0.0012, "WTA": 0.012, "WTA125": 0.0176}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5129, "share_primary_cause_market_settled_or_in_play": 0.4333, "share_primary_cause_stale_quote_only": 0.1763}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 9901, "identity_ambiguous_share": 0.2125, "ticker_orientation": {"VERIFIED": 9901}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6232, "with_external": 286, "coverage": 0.0459, "external_status": {"EXTERNAL_STALE": 182, "AGREES_WITH_KALSHI": 101, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 182, "MODEL_LONE_OUTLIER": 101, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3531, "share_external_supports_model": 0.0105}, "pregame_clean_ge_25pp": {"n": 3021, "with_external": 269, "coverage": 0.089, "external_status": {"EXTERNAL_STALE": 169, "AGREES_WITH_KALSHI": 97, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 169, "MODEL_LONE_OUTLIER": 97, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3606, "share_external_supports_model": 0.0112}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 507.0, "median_sample_ratio": 2.43, "median_min_matches": 20.0, "median_max_days_since_last": 223.0, "share_severe_asymmetry": 0.2086, "data_status": {"POOR": 5457, "LIMITED": 2701, "ADEQUATE": 1743}, "comparison_lt_10pp": {"median_thinner_serve_points": 1754.0, "median_sample_ratio": 1.69, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 759, "model_minus_observed": 0.0492, "kalshi_minus_observed": -0.0863, "brier_diff_model_minus_kalshi": -0.0014}, "4-10x": {"n": 516, "model_minus_observed": 0.0866, "kalshi_minus_observed": -0.059, "brier_diff_model_minus_kalshi": 0.0121}, "<2x": {"n": 1851, "model_minus_observed": 0.0864, "kalshi_minus_observed": -0.0359, "brier_diff_model_minus_kalshi": 0.0123}, ">=10x": {"n": 643, "model_minus_observed": 0.1057, "kalshi_minus_observed": -0.0684, "brier_diff_model_minus_kalshi": 0.0075}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3769, "model": {"intercept": -0.529, "slope": 0.845, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.241, "slope": 1.128, "slope_se": 0.048}, "mean_extremity_model": 0.1707, "mean_extremity_kalshi": 0.1652, "model_brier": 0.2322, "kalshi_brier": 0.2045, "brier_diff_model_minus_kalshi": 0.0277, "brier_diff_se": 0.0031, "model_logloss": 0.661, "kalshi_logloss": 0.5914}, "fair_v1": {"n": 3769, "model": {"intercept": -0.397, "slope": 1.047, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.322, "slope": 1.167, "slope_se": 0.049}, "mean_extremity_model": 0.1669, "mean_extremity_kalshi": 0.1647, "model_brier": 0.2134, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0087, "brier_diff_se": 0.0025, "model_logloss": 0.6151, "kalshi_logloss": 0.5918}, "gen1_elo": {"n": 3769, "model": {"intercept": -0.393, "slope": 1.025, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.15, "slope_se": 0.048}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.165, "model_brier": 0.2126, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0079, "brier_diff_se": 0.0025, "model_logloss": 0.6141, "kalshi_logloss": 0.5917}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2443, "share_ge_15": 0.4439, "median_abs_gap": 13.14, "n": 25507}, "gen1_elo": {"share_ge_25": 0.2415, "share_ge_15": 0.44, "median_abs_gap": 12.85, "n": 25507}, "gen1_sr": {"share_ge_25": 0.3084, "share_ge_15": 0.522, "median_abs_gap": 15.87, "n": 25507}, "gen2": {"share_ge_25": 0.3107, "share_ge_15": 0.5115, "median_abs_gap": 15.52, "n": 25507}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1525, "share_ge_15": 0.3597, "median_abs_gap": 10.94, "n": 19802}, "gen1_elo": {"share_ge_25": 0.1535, "share_ge_15": 0.353, "median_abs_gap": 10.52, "n": 19800}, "gen1_sr": {"share_ge_25": 0.2161, "share_ge_15": 0.445, "median_abs_gap": 13.13, "n": 19803}, "gen2": {"share_ge_25": 0.2317, "share_ge_15": 0.4456, "median_abs_gap": 13.12, "n": 19803}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.88, "share_ge_25_all": 0.0494, "share_ge_25_pregame_clean": 0.0455}, "WTA": {"median_abs_gap_pregame_clean": 7.96, "share_ge_25_all": 0.0464, "share_ge_25_pregame_clean": 0.0424}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2362, "share_within_10pp_all": 0.4333, "share_within_10pp_pregame_clean": 0.486, "corr_model_vs_mid_pregame_clean": 0.844}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 562, "model_brier": 0.1969, "kalshi_brier": 0.1983, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 655, "model_brier": 0.2131, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 845, "model_brier": 0.2255, "kalshi_brier": 0.2149, "brier_diff_model_minus_kalshi": 0.0106}, "25-40": {"n_settled": 475, "model_brier": 0.2251, "kalshi_brier": 0.2105, "brier_diff_model_minus_kalshi": 0.0146}, "3-5": {"n_settled": 356, "model_brier": 0.2004, "kalshi_brier": 0.2, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 94, "model_brier": 0.3003, "kalshi_brier": 0.1784, "brier_diff_model_minus_kalshi": 0.1219}, "5-10": {"n_settled": 782, "model_brier": 0.2009, "kalshi_brier": 0.2013, "brier_diff_model_minus_kalshi": -0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.529, "slope": 0.845, "slope_se": 0.042}, "kalshi_slope": {"intercept": 0.241, "slope": 1.128, "slope_se": 0.048}, "n": 3769}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.511, "slope": 0.875, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.159, "slope": 1.086, "slope_se": 0.037}, "n": 5799}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 361, "model_brier": 0.3222, "kalshi_brier": 0.2343, "brier_diff_model_minus_kalshi": 0.0879, "brier_diff_se": 0.0165, "corr_model_outcome": 0.0079, "corr_kalshi_outcome": 0.2595}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
