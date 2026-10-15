# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-15T05:21Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 33,556): 0-3 14.5%, 3-5 9.5%, 5-10 20.1%, 10-15 15.3%, 15-25 18.9%, 25-40 13.6%, 40+ 8.2%; median gap 11.83 pp.
* **Where the extremes live**: 98.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.6%, Challenger 12.3%, doubles 7.0%). Main tour: ATP 1.4% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,291): MARKET_ALREADY_SETTLED_WHEN_PRICED 37.5%, BOOK_QUALITY 17.6%, STALE_QUOTE 17.1%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 4.0%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 37.5%, execution 17.6%, market_freshness 17.1%, data 12.3%, market_freshness/coverage 8.8%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.4%.
* **Stale / settled / in-play**: 53.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 46.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,291 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.6%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.3% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 553.5 points vs 1794.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.059, Gen-2 0.864, Gen-1 ledger 0.87 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 345 model 0.2264 vs Kalshi 0.2074; n 72 model 0.29 vs Kalshi 0.1741.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 132,975 model-market comparisons (221,037 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 47,214 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-15T05:11:32.938023+00:00'], shadow board 36,729 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-15T05:11:36.501314+00:00'], Model 4 14,232 rows, 14,477 settled tickers, 4,732 tickers with an external scan.
* By model: {"gen1_ledger": 31002, "gen1_elo": 18459, "fair_v1": 18459, "gen2": 18459, "gen1_sr": 18459, "model4_fundamental": 14073, "model4_conditioned": 14064}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 33,556 | 14.5 | 9.5 | 20.1 | 15.3 | 18.9 | 13.6 | 8.2 | 11.83 | 40.6% | 21.7% |
| MW fair_v1 | 18,459 | 13.6 | 8.5 | 18.6 | 15.9 | 19.2 | 14.5 | 9.7 | 12.9 | 43.4% | 24.1% |
| MW gen1_elo | 18,459 | 13.2 | 8.9 | 19.9 | 15.2 | 19.1 | 14.3 | 9.3 | 12.4 | 42.7% | 23.6% |
| MW gen1_ledger | 15,097 | 15.5 | 10.7 | 21.9 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.8% |
| MW gen1_sr | 18,459 | 9.8 | 7.6 | 16.3 | 14.2 | 21.8 | 18.4 | 11.8 | 15.74 | 52.1% | 30.2% |
| MW gen2 | 18,459 | 11.6 | 7.1 | 16.3 | 14.3 | 20.4 | 17.2 | 13.1 | 15.35 | 50.7% | 30.3% |
| all families model4_conditioned | 14,064 | 21.6 | 20.1 | 35.3 | 16.6 | 4.4 | 1.1 | 0.9 | 5.82 | 6.4% | 2.0% |
| all families model4_fundamental | 14,073 | 16.8 | 13.5 | 35.7 | 19.7 | 10.6 | 2.6 | 1.1 | 7.59 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 55.9%, >=15pp 40.6%, >=20pp 30.1%, >=25pp 21.7%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.45pp; >=10pp 45.2%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,332 | 30.6 | 14.6 | 25.1 | 17.5 | 10.3 | 1.1 | 0.8 | 5.69 | 12.2% | 1.9% |
| CHALLENGER | 3,140 | 15.7 | 9.9 | 20.1 | 15.9 | 14.7 | 12.1 | 11.6 | 11.53 | 38.4% | 23.7% |
| ITF_MEN | 5,249 | 11.1 | 8.2 | 18.0 | 14.9 | 19.6 | 16.1 | 12.1 | 14.1 | 47.7% | 28.2% |
| ITF_WOMEN | 7,204 | 10.4 | 6.6 | 16.2 | 16.0 | 22.3 | 18.1 | 10.4 | 15.33 | 50.8% | 28.5% |
| WTA | 939 | 21.5 | 10.7 | 24.6 | 15.8 | 20.8 | 5.5 | 1.2 | 8.18 | 27.5% | 6.7% |
| WTA125 | 595 | 13.3 | 7.4 | 22.2 | 21.2 | 20.3 | 13.8 | 1.9 | 11.33 | 36.0% | 15.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,332 | 24.8 | 14.5 | 24.6 | 18.8 | 14.4 | 1.9 | 1.0 | 6.55 | 17.3% | 2.9% |
| CHALLENGER | 3,140 | 14.9 | 7.6 | 19.5 | 13.5 | 18.2 | 14.0 | 12.2 | 12.72 | 44.5% | 26.3% |
| ITF_MEN | 5,249 | 9.6 | 6.9 | 16.0 | 14.0 | 20.0 | 18.6 | 14.9 | 16.38 | 53.4% | 33.5% |
| ITF_WOMEN | 7,204 | 8.7 | 5.8 | 13.3 | 13.5 | 21.9 | 20.5 | 16.2 | 18.58 | 58.7% | 36.7% |
| WTA | 939 | 17.6 | 8.1 | 18.6 | 16.3 | 23.2 | 15.0 | 1.2 | 12.12 | 39.4% | 16.2% |
| WTA125 | 595 | 6.2 | 4.7 | 17.0 | 17.5 | 25.7 | 19.7 | 9.2 | 17.24 | 54.6% | 28.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,332 | 27.9 | 14.4 | 28.6 | 15.3 | 10.4 | 2.5 | 0.9 | 6.03 | 13.8% | 3.4% |
| CHALLENGER | 3,140 | 15.0 | 10.2 | 20.5 | 15.2 | 15.5 | 11.7 | 11.9 | 11.03 | 39.1% | 23.6% |
| ITF_MEN | 5,249 | 10.2 | 8.1 | 18.6 | 14.2 | 20.2 | 16.4 | 12.2 | 14.51 | 48.9% | 28.6% |
| ITF_WOMEN | 7,204 | 10.0 | 6.8 | 16.6 | 15.9 | 23.0 | 18.3 | 9.4 | 15.24 | 50.7% | 27.7% |
| WTA | 939 | 22.7 | 15.6 | 32.6 | 15.8 | 10.5 | 2.1 | 0.8 | 6.12 | 13.4% | 2.9% |
| WTA125 | 595 | 22.4 | 12.9 | 29.2 | 15.0 | 13.9 | 6.2 | 0.3 | 7.5 | 20.5% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 728 | 31.0 | 22.8 | 35.3 | 9.2 | 1.2 | 0.4 | 0.0 | 4.69 | 1.7% | 0.4% |
| CHALLENGER | 2,155 | 22.1 | 15.6 | 27.6 | 14.8 | 13.0 | 5.0 | 2.0 | 6.98 | 20.0% | 7.0% |
| DOUBLES | 1,025 | 5.3 | 3.8 | 11.5 | 10.7 | 18.8 | 24.6 | 25.3 | 24.85 | 68.7% | 49.9% |
| ITF_MEN | 4,640 | 14.7 | 8.5 | 20.8 | 15.4 | 20.8 | 12.5 | 7.3 | 11.87 | 40.6% | 19.9% |
| ITF_WOMEN | 5,071 | 11.7 | 9.3 | 19.6 | 14.7 | 22.3 | 16.6 | 5.7 | 13.01 | 44.7% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 653 | 21.3 | 15.3 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.52 | 19.0% | 5.4% |
| WTA125 | 676 | 20.6 | 13.6 | 22.6 | 18.5 | 14.3 | 8.1 | 2.2 | 8.25 | 24.7% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,318 | 30.5 | 14.5 | 25.3 | 17.5 | 10.2 | 1.1 | 0.8 | 5.75 | 12.1% | 1.9% |
| CHALLENGER | 2,248 | 20.3 | 12.4 | 25.3 | 18.5 | 15.2 | 5.9 | 2.4 | 8.32 | 23.5% | 8.3% |
| ITF_MEN | 3,806 | 13.7 | 10.2 | 21.4 | 16.7 | 20.0 | 12.8 | 5.2 | 11.23 | 38.0% | 18.1% |
| ITF_WOMEN | 5,307 | 12.6 | 8.1 | 18.6 | 18.3 | 23.8 | 14.7 | 3.9 | 12.83 | 42.4% | 18.6% |
| WTA | 923 | 21.7 | 10.0 | 25.0 | 15.9 | 20.8 | 5.4 | 1.2 | 8.22 | 27.4% | 6.6% |
| WTA125 | 571 | 13.7 | 7.2 | 21.5 | 21.5 | 21.0 | 13.7 | 1.4 | 11.47 | 36.1% | 15.1% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,318 | 24.7 | 14.6 | 24.7 | 18.8 | 14.4 | 1.8 | 1.0 | 6.58 | 17.2% | 2.8% |
| CHALLENGER | 2,248 | 19.1 | 9.7 | 24.3 | 16.4 | 18.5 | 9.6 | 2.6 | 9.11 | 30.6% | 12.1% |
| ITF_MEN | 3,807 | 11.5 | 8.3 | 18.4 | 15.8 | 22.0 | 16.0 | 8.1 | 13.66 | 46.1% | 24.1% |
| ITF_WOMEN | 5,307 | 10.0 | 6.7 | 15.1 | 14.8 | 24.1 | 19.4 | 9.9 | 16.23 | 53.5% | 29.4% |
| WTA | 923 | 17.4 | 7.9 | 18.6 | 16.6 | 23.2 | 15.1 | 1.2 | 12.25 | 39.4% | 16.2% |
| WTA125 | 571 | 6.0 | 4.9 | 17.0 | 17.9 | 25.6 | 20.3 | 8.4 | 17.24 | 54.3% | 28.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 708 | 31.1 | 23.0 | 35.6 | 9.3 | 0.6 | 0.4 | 0.0 | 4.66 | 1.0% | 0.4% |
| CHALLENGER | 1,860 | 23.9 | 16.9 | 29.7 | 14.5 | 12.1 | 2.3 | 0.5 | 6.36 | 14.9% | 2.9% |
| DOUBLES | 946 | 5.4 | 3.9 | 11.8 | 10.8 | 18.9 | 24.5 | 24.6 | 24.2 | 68.1% | 49.1% |
| ITF_MEN | 3,816 | 16.2 | 9.3 | 22.8 | 16.2 | 20.6 | 10.5 | 4.4 | 10.54 | 35.5% | 14.9% |
| ITF_WOMEN | 4,141 | 12.9 | 10.1 | 21.4 | 15.5 | 22.6 | 15.0 | 2.6 | 11.56 | 40.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 619 | 21.8 | 16.0 | 27.5 | 17.1 | 13.9 | 3.7 | 0.0 | 7.21 | 17.6% | 3.7% |
| WTA125 | 572 | 22.6 | 15.0 | 24.1 | 20.1 | 12.8 | 5.1 | 0.3 | 7.33 | 18.2% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,025 | 5.3 | 3.8 | 11.5 | 10.7 | 18.8 | 24.6 | 25.3 | 24.85 | 68.7% | 49.9% |
| singles | 14,072 | 16.2 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.95 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,326 | 13.2 | 9.0 | 19.7 | 16.0 | 18.1 | 14.2 | 9.7 | 12.61 | 42.0% | 24.0% |
| Grass | 190 | 12.6 | 11.6 | 15.3 | 15.3 | 21.6 | 17.9 | 5.8 | 14.16 | 45.3% | 23.7% |
| Hard | 12,031 | 14.0 | 8.4 | 18.6 | 15.4 | 19.6 | 14.3 | 9.6 | 12.86 | 43.5% | 23.9% |
| UNKNOWN | 1,912 | 12.1 | 7.2 | 16.8 | 18.8 | 19.1 | 15.9 | 10.0 | 13.38 | 45.1% | 25.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,421 | 19.8 | 10.7 | 20.9 | 16.9 | 15.9 | 8.8 | 7.0 | 9.53 | 31.7% | 15.8% |
| B | 2,405 | 14.5 | 9.1 | 20.2 | 16.6 | 18.1 | 12.1 | 9.5 | 11.5 | 39.7% | 21.6% |
| C | 2,654 | 13.0 | 9.5 | 19.9 | 14.6 | 19.6 | 14.2 | 9.3 | 12.58 | 43.0% | 23.4% |
| D | 3,220 | 11.5 | 8.0 | 17.8 | 16.1 | 21.9 | 15.5 | 9.2 | 13.75 | 46.6% | 24.7% |
| F | 4,759 | 8.0 | 5.3 | 15.1 | 15.0 | 21.7 | 21.6 | 13.3 | 17.84 | 56.6% | 34.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,368 | 22.8 | 15.9 | 28.9 | 15.1 | 11.3 | 4.4 | 1.6 | 6.7 | 17.3% | 6.0% |
| B | 2,270 | 14.9 | 10.0 | 24.0 | 16.3 | 19.5 | 11.1 | 4.2 | 10.19 | 34.7% | 15.2% |
| C | 2,993 | 12.2 | 7.8 | 18.3 | 14.1 | 20.2 | 15.8 | 11.6 | 13.64 | 47.6% | 27.4% |
| D | 2,274 | 14.0 | 9.8 | 20.8 | 13.6 | 21.3 | 13.9 | 6.6 | 11.86 | 41.8% | 20.5% |
| F | 3,192 | 10.2 | 7.5 | 15.3 | 13.9 | 23.7 | 20.3 | 9.2 | 16.37 | 53.2% | 29.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,075 | 18.1 | 9.7 | 20.3 | 16.7 | 16.2 | 9.8 | 9.1 | 10.51 | 35.2% | 18.9% |
| LIMITED | 4,308 | 15.1 | 10.4 | 20.8 | 15.6 | 18.8 | 12.5 | 6.9 | 11.1 | 38.2% | 19.4% |
| POOR | 8,076 | 9.4 | 6.5 | 16.2 | 15.5 | 21.7 | 19.0 | 11.6 | 15.88 | 52.3% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,042 | 31.2 | 24.5 | 36.4 | 5.5 | 1.7 | 0.7 | 0.1 | 4.49 | 2.5% | 0.7% |
| GAME_SPREAD | 2,894 | 25.8 | 16.1 | 36.6 | 16.8 | 4.1 | 0.4 | 0.2 | 5.97 | 4.7% | 0.6% |
| MATCH_WINNER | 15,097 | 15.5 | 10.7 | 21.9 | 14.6 | 18.4 | 12.5 | 6.3 | 10.45 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,525 | 33.4 | 19.5 | 31.1 | 9.6 | 5.1 | 1.1 | 0.2 | 4.72 | 6.4% | 1.4% |
| TOTAL_GAMES | 4,420 | 6.7 | 9.2 | 39.2 | 29.5 | 10.4 | 2.7 | 2.3 | 9.44 | 15.4% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,921 | 25.6 | 38.3 | 31.4 | 0.3 | 3.9 | 0.4 | 0.1 | 4.3 | 4.4% | 0.5% |
| GAME_SPREAD | 3,507 | 45.3 | 16.4 | 28.8 | 7.3 | 1.1 | 0.7 | 0.4 | 3.56 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,636 | 3.5 | 6.5 | 42.7 | 36.7 | 6.8 | 1.9 | 1.9 | 9.78 | 10.7% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,921 | 26.4 | 18.8 | 37.1 | 9.1 | 6.2 | 2.1 | 0.3 | 5.47 | 8.6% | 2.4% |
| GAME_SPREAD | 3,507 | 19.5 | 13.5 | 30.2 | 20.9 | 12.8 | 2.3 | 0.7 | 7.7 | 15.8% | 3.0% |
| TOTAL_GAMES | 5,645 | 6.7 | 8.9 | 37.9 | 28.1 | 13.1 | 3.3 | 2.1 | 9.65 | 18.5% | 5.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 18,459 | 43.4% | 24.1% | 12.9 | 34.2% | 14.3% | 10.51 |
| gen1_elo | 18,459 | 42.7% | 23.6% | 12.4 | 33.1% | 14.1% | 10.0 |
| gen1_sr | 18,459 | 52.1% | 30.2% | 15.74 | 43.9% | 20.5% | 13.05 |
| gen2 | 18,459 | 50.7% | 30.3% | 15.35 | 43.6% | 21.9% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 9,789 | 16.4 | 10.4 | 21.6 | 17.4 | 19.6 | 11.2 | 3.3 | 10.42 | 34.2% | 14.5% |
| STALE | 8,670 | 10.4 | 6.2 | 15.3 | 14.3 | 18.8 | 18.2 | 16.8 | 17.01 | 53.7% | 35.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,565 | 17.3 | 11.6 | 23.6 | 14.5 | 16.9 | 11.2 | 4.9 | 9.38 | 32.9% | 16.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 33,556 | 8565 | 13261 | 11730 | 24.4 | 143.1 | 1400.4 |
| ge_15pp | 13,624 | 2819 | 4636 | 6169 | 26.8 | 444.3 | 1380.4 |
| ge_25pp | 7,291 | 1374 | 2014 | 3903 | 34.1 | 579.9 | 1380.4 |
| lt_10pp | 14,784 | 4501 | 6375 | 3908 | 22.6 | 48.7 | 1341.5 |

Current slate `SL-20261015T052101Z-ac2e8057`: 501 priced rows, quote age at build {'median': 9.7, 'max': 9.8}, freshness {'FRESH': 501}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 10 | 0.0 | 0.0 | 40.0 | 0.0 | 40.0 | 20.0 | 0.0 | 20.33 | 60.0% | 20.0% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,513 | 21.3 | 10.6 | 22.9 | 18.6 | 19.0 | 6.9 | 0.6 | 8.83 | 26.5% | 7.5% |
| KALSHI_LONE_OUTLIER | 7 | 14.3 | 0.0 | 57.1 | 0.0 | 14.3 | 14.3 | 0.0 | 5.14 | 28.6% | 14.3% |
| MARKETS_AGREE | 253 | 71.9 | 28.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.04 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 486 | 0.0 | 3.9 | 34.0 | 29.4 | 24.1 | 8.0 | 0.6 | 11.66 | 32.7% | 8.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 18,459 | 2280 (12.3%) | 21.3% | 0.7% | {"EXTERNAL_STALE": 1513, "AGREES_WITH_KALSHI": 486, "ALL_AGREE": 253, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 9, "AGREES_WITH_MODEL": 7, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,006 | 568 (7.1%) | 28.0% | 1.4% | {"EXTERNAL_STALE": 401, "AGREES_WITH_KALSHI": 159, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,455 | 159 (3.6%) | 26.4% | 1.9% | {"EXTERNAL_STALE": 114, "AGREES_WITH_KALSHI": 42, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,034 | 150 (7.4%) | 26.7% | 2.0% | {"EXTERNAL_STALE": 107, "AGREES_WITH_KALSHI": 40, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,514 | 1287 (17.1%) | 14.3% | 0.6% | {"EXTERNAL_STALE": 830, "ALL_AGREE": 253, "AGREES_WITH_KALSHI": 184, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 5, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,609 | 11.5 | 8.0 | 20.0 | 14.9 | 21.6 | 14.2 | 9.8 | 13.38 | 45.6% | 23.9% |
| 4-10x | 2,422 | 12.3 | 8.8 | 19.5 | 15.6 | 19.5 | 15.4 | 8.9 | 12.91 | 43.8% | 24.3% |
| <2x | 9,643 | 15.5 | 9.1 | 18.8 | 16.9 | 17.8 | 12.9 | 9.0 | 11.88 | 39.6% | 21.9% |
| >=10x | 2,785 | 10.9 | 6.4 | 15.4 | 14.0 | 21.0 | 19.6 | 12.6 | 16.35 | 53.2% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,809 | 13.8 | 8.3 | 19.4 | 16.1 | 19.7 | 12.7 | 10.2 | 12.64 | 42.5% | 22.8% |
| 300-1000 | 4,205 | 12.1 | 8.8 | 17.5 | 16.2 | 21.0 | 15.6 | 8.9 | 13.52 | 45.5% | 24.5% |
| <300 | 5,400 | 8.9 | 6.0 | 15.9 | 14.8 | 21.4 | 20.5 | 12.7 | 16.81 | 54.5% | 33.1% |
| >=3000 | 4,045 | 21.3 | 11.7 | 22.7 | 17.1 | 14.0 | 7.5 | 5.9 | 8.43 | 27.3% | 13.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 597 | 0.5376 | 0.406 | 0.4874 | +0.050 | -0.081 | 0.0001 ± 0.006 |
| ratio 4-10x | 399 | 0.5869 | 0.4477 | 0.5138 | +0.073 | -0.066 | 0.0065 ± 0.0078 |
| ratio <2x | 1428 | 0.5375 | 0.4151 | 0.4566 | +0.081 | -0.042 | 0.0111 ± 0.0038 |
| ratio >=10x | 476 | 0.548 | 0.3797 | 0.4286 | +0.119 | -0.049 | 0.0148 ± 0.0081 |
| thinner_sample 1000-3000 | 806 | 0.5426 | 0.4177 | 0.4752 | +0.067 | -0.058 | 0.004 ± 0.005 |
| thinner_sample 300-1000 | 708 | 0.5613 | 0.4237 | 0.4873 | +0.074 | -0.064 | 0.0023 ± 0.0058 |
| thinner_sample <300 | 895 | 0.5452 | 0.3841 | 0.4436 | +0.102 | -0.059 | 0.0149 ± 0.0058 |
| thinner_sample >=3000 | 491 | 0.5312 | 0.4359 | 0.4623 | +0.069 | -0.026 | 0.0148 ± 0.0053 |
| data_status ADEQUATE | 821 | 0.5338 | 0.4295 | 0.4629 | +0.071 | -0.033 | 0.0084 ± 0.0044 |
| data_status LIMITED | 741 | 0.5516 | 0.4228 | 0.4899 | +0.062 | -0.067 | 0.0031 ± 0.0054 |
| data_status POOR | 1338 | 0.5505 | 0.3951 | 0.4552 | +0.095 | -0.060 | 0.0122 ± 0.0046 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 441 | 0.1948 | 0.1963 | -0.0014 ± 0.0007 | 0.5682 | 0.5713 | 0.4921 | 0.4772 | 0.5283 | -0.042 ± 0.022 | -0.01 (3) |
| 3-5 | 287 | 0.1911 | 0.1914 | -0.0003 ± 0.0021 | 0.5624 | 0.5618 | 0.5101 | 0.4703 | 0.4913 | -0.071 ± 0.0263 | 0.02 (1) |
| 5-10 | 610 | 0.1959 | 0.1969 | -0.0010 ± 0.0027 | 0.5768 | 0.5772 | 0.5119 | 0.4373 | 0.4738 | -0.078 ± 0.0187 | -0.0125 (4) |
| 10-15 | 510 | 0.2105 | 0.2024 | +0.0081 ± 0.005 | 0.6083 | 0.5853 | 0.5215 | 0.3978 | 0.4255 | -0.087 ± 0.0198 | -0.0633 (3) |
| 15-25 | 635 | 0.2296 | 0.2174 | +0.0122 ± 0.0072 | 0.6542 | 0.6211 | 0.5761 | 0.3812 | 0.4488 | -0.073 ± 0.0184 | -0.0133 (6) |
| 25-40 | 345 | 0.2264 | 0.2074 | +0.0190 ± 0.0146 | 0.6438 | 0.5961 | 0.6446 | 0.3363 | 0.4609 | -0.065 ± 0.0224 | -0.01 (1) |
| 40+ | 72 | 0.29 | 0.1741 | +0.1160 ± 0.0438 | 0.7878 | 0.5206 | 0.7443 | 0.2967 | 0.3889 | -0.113 ± 0.0433 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2063 | 0.1785 | 0.1797 | -0.0012 ± 0.0003 | 0.5313 | 0.5328 | 0.4811 | 0.466 | 0.5051 | -0.017 ± 0.0094 | -0.0188 (8) |
| 3-5 | 1290 | 0.1949 | 0.1933 | +0.0017 ± 0.001 | 0.5711 | 0.563 | 0.4825 | 0.4429 | 0.4388 | -0.063 ± 0.0125 | 0.02 (1) |
| 5-10 | 2847 | 0.1926 | 0.191 | +0.0016 ± 0.0012 | 0.5676 | 0.5608 | 0.4865 | 0.4125 | 0.4352 | -0.042 ± 0.0083 | -0.0082 (17) |
| 10-15 | 2443 | 0.2006 | 0.1821 | +0.0185 ± 0.0022 | 0.587 | 0.5358 | 0.4797 | 0.3554 | 0.3434 | -0.076 ± 0.0086 | -0.0475 (4) |
| 15-25 | 2969 | 0.2071 | 0.1717 | +0.0354 ± 0.003 | 0.6064 | 0.5065 | 0.5006 | 0.3045 | 0.3139 | -0.063 ± 0.0076 | -0.0048 (29) |
| 25-40 | 2356 | 0.2197 | 0.126 | +0.0937 ± 0.0046 | 0.6328 | 0.3879 | 0.5279 | 0.2148 | 0.2262 | -0.059 ± 0.0071 | -0.01 (1) |
| 40+ | 1591 | 0.3737 | 0.0436 | +0.3302 ± 0.0059 | 0.9731 | 0.1718 | 0.6256 | 0.1055 | 0.0585 | -0.084 ± 0.0049 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 337 | 0.198 | 0.1982 | -0.0002 ± 0.0009 | 0.5771 | 0.5776 | 0.5018 | 0.4867 | 0.5015 | -0.086 ± 0.0255 | -0.01 (1) |
| 3-5 | 231 | 0.2113 | 0.2104 | +0.0008 ± 0.0025 | 0.605 | 0.6046 | 0.5192 | 0.4792 | 0.4848 | -0.081 ± 0.0317 | 0.02 (1) |
| 5-10 | 523 | 0.1985 | 0.1986 | -0.0002 ± 0.0029 | 0.5802 | 0.5808 | 0.5555 | 0.4807 | 0.5201 | -0.066 ± 0.0203 | -0.01 (4) |
| 10-15 | 472 | 0.2143 | 0.2069 | +0.0074 ± 0.0052 | 0.6152 | 0.5991 | 0.5713 | 0.4469 | 0.4831 | -0.087 ± 0.0217 | -0.05 (4) |
| 15-25 | 708 | 0.2279 | 0.2086 | +0.0193 ± 0.0068 | 0.6474 | 0.5996 | 0.588 | 0.3912 | 0.4435 | -0.086 ± 0.0174 | -0.01 (5) |
| 25-40 | 453 | 0.2656 | 0.1979 | +0.0678 ± 0.0132 | 0.744 | 0.5749 | 0.6643 | 0.3497 | 0.4018 | -0.115 ± 0.0207 | -0.025 (2) |
| 40+ | 176 | 0.3557 | 0.1833 | +0.1724 ± 0.0315 | 0.9849 | 0.5396 | 0.7415 | 0.2609 | 0.3352 | -0.061 ± 0.0311 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1765 | 0.1828 | 0.1831 | -0.0003 ± 0.0003 | 0.5405 | 0.5412 | 0.4975 | 0.4828 | 0.5059 | -0.033 ± 0.0105 | -0.0217 (6) |
| 3-5 | 1132 | 0.194 | 0.1933 | +0.0007 ± 0.0011 | 0.5633 | 0.5618 | 0.5179 | 0.478 | 0.4885 | -0.040 ± 0.0133 | 0.02 (1) |
| 5-10 | 2471 | 0.1917 | 0.1898 | +0.0019 ± 0.0013 | 0.5663 | 0.5584 | 0.517 | 0.4434 | 0.4686 | -0.037 ± 0.0089 | -0.01 (5) |
| 10-15 | 2170 | 0.1961 | 0.1829 | +0.0133 ± 0.0023 | 0.5777 | 0.5361 | 0.5212 | 0.3968 | 0.4088 | -0.057 ± 0.0093 | -0.02 (14) |
| 15-25 | 3163 | 0.2157 | 0.1763 | +0.0395 ± 0.003 | 0.6272 | 0.52 | 0.5327 | 0.3364 | 0.337 | -0.074 ± 0.0075 | -0.0026 (27) |
| 25-40 | 2718 | 0.2479 | 0.137 | +0.1109 ± 0.0045 | 0.7034 | 0.4177 | 0.5614 | 0.2449 | 0.2303 | -0.084 ± 0.0071 | -0.015 (6) |
| 40+ | 2140 | 0.3996 | 0.0683 | +0.3313 ± 0.0065 | 1.048 | 0.2372 | 0.6644 | 0.1274 | 0.1009 | -0.066 ± 0.0055 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 432 | 0.1945 | 0.1972 | -0.0027 ± 0.0008 | 0.569 | 0.5759 | 0.4928 | 0.4776 | 0.5556 | +0.000 ± 0.0216 | -0.0133 (6) |
| 3-5 | 311 | 0.1859 | 0.1841 | +0.0019 ± 0.0019 | 0.5474 | 0.5428 | 0.4917 | 0.4523 | 0.4502 | -0.113 ± 0.0255 | -0.01 (1) |
| 5-10 | 639 | 0.2002 | 0.1976 | +0.0026 ± 0.0026 | 0.5875 | 0.5778 | 0.5049 | 0.4311 | 0.4476 | -0.088 ± 0.0181 | -0.01 (4) |
| 10-15 | 502 | 0.2083 | 0.2088 | -0.0005 ± 0.005 | 0.6039 | 0.6002 | 0.5392 | 0.4164 | 0.4821 | -0.060 ± 0.0202 | -0.044 (5) |
| 15-25 | 587 | 0.235 | 0.2118 | +0.0233 ± 0.0074 | 0.6697 | 0.6081 | 0.5829 | 0.3896 | 0.4259 | -0.103 ± 0.0188 | -0.03 (1) |
| 25-40 | 364 | 0.2109 | 0.2133 | -0.0024 ± 0.0142 | 0.6095 | 0.6097 | 0.6505 | 0.3405 | 0.4973 | -0.039 ± 0.0215 | 0.0 (1) |
| 40+ | 65 | 0.3165 | 0.1747 | +0.1418 ± 0.0472 | 0.8502 | 0.5223 | 0.7504 | 0.2955 | 0.3692 | -0.124 ± 0.0479 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1954 | 0.186 | 0.1873 | -0.0013 ± 0.0003 | 0.5485 | 0.5511 | 0.4861 | 0.4708 | 0.5082 | -0.016 ± 0.0098 | -0.0183 (23) |
| 3-5 | 1365 | 0.1849 | 0.1825 | +0.0024 ± 0.0009 | 0.5462 | 0.5403 | 0.4758 | 0.4365 | 0.4264 | -0.073 ± 0.0119 | -0.0243 (7) |
| 5-10 | 3024 | 0.1938 | 0.1882 | +0.0055 ± 0.0012 | 0.5717 | 0.553 | 0.4808 | 0.407 | 0.4044 | -0.064 ± 0.0079 | -0.01 (18) |
| 10-15 | 2326 | 0.1956 | 0.1814 | +0.0142 ± 0.0022 | 0.5756 | 0.5324 | 0.4973 | 0.3741 | 0.3783 | -0.063 ± 0.0088 | -0.03 (9) |
| 15-25 | 3038 | 0.2092 | 0.1707 | +0.0385 ± 0.0029 | 0.6127 | 0.5052 | 0.5041 | 0.3087 | 0.3097 | -0.069 ± 0.0075 | -0.03 (2) |
| 25-40 | 2320 | 0.2135 | 0.1247 | +0.0887 ± 0.0046 | 0.6187 | 0.3834 | 0.5248 | 0.2091 | 0.2306 | -0.053 ± 0.007 | 0.0 (1) |
| 40+ | 1532 | 0.3874 | 0.0451 | +0.3423 ± 0.0061 | 1.0114 | 0.1763 | 0.6333 | 0.1074 | 0.0561 | -0.087 ± 0.0051 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 755 | 0.1973 | 0.1978 | -0.0005 ± 0.0006 | 0.5755 | 0.5765 | 0.5042 | 0.4891 | 0.5033 | -0.040 ± 0.0162 | -0.0226 (46) |
| 3-5 | 541 | 0.1941 | 0.1936 | +0.0005 ± 0.0015 | 0.5667 | 0.5639 | 0.4799 | 0.4401 | 0.451 | -0.045 ± 0.019 | -0.0058 (33) |
| 5-10 | 1142 | 0.1953 | 0.1899 | +0.0055 ± 0.0019 | 0.5763 | 0.5611 | 0.4866 | 0.4132 | 0.4133 | -0.062 ± 0.0131 | -0.0049 (73) |
| 10-15 | 721 | 0.2067 | 0.1965 | +0.0102 ± 0.0041 | 0.6017 | 0.5748 | 0.5022 | 0.3793 | 0.3981 | -0.049 ± 0.0165 | 0.0014 (64) |
| 15-25 | 968 | 0.2316 | 0.2124 | +0.0192 ± 0.0058 | 0.6613 | 0.6108 | 0.5623 | 0.3678 | 0.4163 | -0.048 ± 0.0148 | -0.0216 (58) |
| 25-40 | 558 | 0.2536 | 0.1952 | +0.0584 ± 0.0116 | 0.7138 | 0.5676 | 0.6443 | 0.3315 | 0.3925 | -0.083 ± 0.0175 | -0.0216 (25) |
| 40+ | 192 | 0.3714 | 0.1911 | +0.1803 ± 0.0321 | 1.0746 | 0.5631 | 0.7938 | 0.303 | 0.3854 | -0.079 ± 0.0289 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2274 | 0.1883 | 0.1886 | -0.0002 ± 0.0003 | 0.5521 | 0.5515 | 0.5024 | 0.487 | 0.5 | -0.032 ± 0.0091 | -0.0155 (82) |
| 3-5 | 1551 | 0.1882 | 0.1857 | +0.0025 ± 0.0009 | 0.551 | 0.5451 | 0.4872 | 0.4476 | 0.4371 | -0.057 ± 0.011 | -0.0148 (63) |
| 5-10 | 3200 | 0.1924 | 0.185 | +0.0074 ± 0.0011 | 0.569 | 0.5479 | 0.4802 | 0.4066 | 0.3962 | -0.062 ± 0.0077 | -0.0087 (125) |
| 10-15 | 2155 | 0.2035 | 0.1892 | +0.0144 ± 0.0023 | 0.5946 | 0.5565 | 0.5088 | 0.3858 | 0.3889 | -0.055 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2707 | 0.2293 | 0.1989 | +0.0303 ± 0.0034 | 0.6617 | 0.5775 | 0.5548 | 0.3598 | 0.3809 | -0.057 ± 0.0086 | -0.0255 (106) |
| 25-40 | 1840 | 0.2548 | 0.1688 | +0.0860 ± 0.0061 | 0.7219 | 0.4992 | 0.6066 | 0.292 | 0.3147 | -0.076 ± 0.0093 | -0.0206 (47) |
| 40+ | 903 | 0.3857 | 0.1288 | +0.2569 ± 0.0128 | 1.0942 | 0.3947 | 0.7091 | 0.2019 | 0.2148 | -0.072 ± 0.0113 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2900 | 1.059 ± 0.052 | 1.175 | 0.1687 | 0.171 | 0.2112 | 0.2024 |
| gen2 | 2900 | 0.864 ± 0.047 | 1.124 | 0.1779 | 0.171 | 0.2292 | 0.2022 |
| gen1_elo | 2900 | 1.04 ± 0.051 | 1.164 | 0.1733 | 0.1714 | 0.2102 | 0.2024 |
| gen1_sr | 2900 | 1.069 ± 0.061 | 1.194 | 0.137 | 0.1729 | 0.2252 | 0.202 |
| gen1_ledger | 4877 | 0.87 ± 0.035 | 1.081 | 0.1769 | 0.1864 | 0.218 | 0.1976 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 13,624)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,457 | 25.4% |
| STALE_QUOTE | market_freshness | 2,769 | 20.3% |
| BOOK_QUALITY | execution | 2,464 | 18.1% |
| POOR_DATA | data | 1,498 | 11.0% |
| LIMITED_DATA | data | 987 | 7.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 747 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 646 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 522 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 389 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 145 | 1.1% |

Cause class: coverage 25.4%, market_freshness 20.3%, data 18.2%, execution 18.1%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 3.8%, model_calibration 1.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 69.0%, THIN_PLAYER_HISTORY 57.8%, STALE_PLAYER_DATA 53.7%, STALE_KALSHI_QUOTE 45.3%, MODEL_INTERNAL_DISAGREEMENT 39.0%, ASYMMETRIC_SAMPLE_SIZE 31.8%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 16.8%, PLAYER_IDENTITY_RISK 13.8%, LEVEL_TRANSFER_RISK 8.5%, EVENT_MAPPING_RISK 7.9%, LOW_DISPLAYED_LIQUIDITY 7.5%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.8%, POST_SETTLEMENT_OBSERVATION 25.4%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,291)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,733 | 37.5% |
| BOOK_QUALITY | execution | 1,283 | 17.6% |
| STALE_QUOTE | market_freshness | 1,245 | 17.1% |
| POOR_DATA | data | 604 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 403 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 319 | 4.4% |
| LIMITED_DATA | data | 292 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 240 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 141 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 31 | 0.4% |

Cause class: coverage 37.5%, execution 17.6%, market_freshness 17.1%, data 12.3%, market_freshness/coverage 8.8%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.1%, START_UNVERIFIABLE 98.3%, LOW_DATA_QUALITY 72.8%, THIN_PLAYER_HISTORY 60.1%, STALE_KALSHI_QUOTE 53.5%, STALE_PLAYER_DATA 48.9%, MODEL_INTERNAL_DISAGREEMENT 40.1%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.5%, PLAYER_IDENTITY_RISK 17.4%, EVENT_MAPPING_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 7.7%, LEVEL_TRANSFER_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 40.3%, POST_SETTLEMENT_OBSERVATION 37.5%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5842, "IDENTITY_AMBIGUOUS": 1449}; ticker orientation: {"VERIFIED": 7291}.

Checks: discipline:AMBIGUOUS 511, discipline:PASS 6780, identity_confidence:AMBIGUOUS 1268, identity_confidence:PASS 6023, level_mapping:NA 523, level_mapping:PASS 6768, market_pair:AMBIGUOUS 257, market_pair:NA 174, market_pair:PASS 6860, model_complement:NA 141, model_complement:PASS 7150, namesake:PASS 7291, physical_match_id:NA 2836, physical_match_id:PASS 4455, player_ids:PASS 7291, same_pair_other_event:PASS 7291, ticker_orientation:PASS 7291

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,060 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.24 | 0.2103 / 0.2125 (251) | 16.5% | 0.5% | 5.4% | 1.7% |
| CHALLENGER | 5,295 | 16.9% | 5.8% | 12.3% | {"coverage": 547, "market_freshness": 110, "market_freshness/coverage": 108, "data": 58, "model_calibration_or_unknown": 45, "execution": 13, "model_calibration": 7, "mapping": 6} | 7.24 | 0.2176 / 0.2038 (1368) | 37.7% | 9.1% | 2.4% | 22.4% |
| DOUBLES | 1,025 | 49.9% | 49.1% | 7.0% | {"execution": 208, "mapping": 151, "market_freshness": 106, "market_freshness/coverage": 39, "coverage": 7} | 24.2 | 0.3338 / 0.2309 (297) | 22.8% | 0.0% | 100.0% | 7.7% |
| ITF_MEN | 9,889 | 24.3% | 16.5% | 32.9% | {"coverage": 944, "execution": 497, "market_freshness": 354, "data": 319, "market_freshness/coverage": 201, "mapping": 83, "model_calibration_or_unknown": 2} | 10.95 | 0.213 / 0.1948 (2464) | 36.5% | 59.7% | 11.2% | 22.9% |
| ITF_WOMEN | 12,275 | 25.9% | 18.2% | 43.7% | {"coverage": 1218, "market_freshness": 580, "execution": 536, "data": 485, "market_freshness/coverage": 249, "mapping": 73, "model_calibration_or_unknown": 33, "model_calibration": 10} | 12.36 | 0.2025 / 0.1928 (2640) | 38.9% | 57.9% | 9.8% | 23.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,592 | 6.2% | 5.5% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "model_calibration": 7, "execution": 7, "coverage": 4, "mapping": 1} | 7.85 | 0.2387 / 0.2306 (279) | 26.5% | 1.3% | 1.7% | 3.1% |
| WTA125 | 1,271 | 12.8% | 10.2% | 2.2% | {"model_calibration_or_unknown": 37, "market_freshness": 37, "market_freshness/coverage": 34, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 7, "mapping": 4} | 9.51 | 0.2156 / 0.207 (436) | 23.8% | 8.0% | 4.2% | 10.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 5 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 6 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 8 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 9 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 10 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 11 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 12 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 13 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 14 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 15 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 16 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 17 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 18 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 20 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 21 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 23 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 24 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 25 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 26 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 28 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 29 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 30 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 31 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 32 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 33 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 37 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 38 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 39 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 40 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 41 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 42 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 757 min (STALE); no external reference |
| 44 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 45 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 46 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 47 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 48 | `KXITFMATCH-26OCT13VISMUE-MUE` | ITF_MEN | fair_v1 | 25% / 98% | -74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 617 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 0.0); no external reference |
| 49 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 50 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9826, "by_level_share_of_ge_25pp": {"ATP": 0.004, "CHALLENGER": 0.1226, "DOUBLES": 0.0701, "ITF_MEN": 0.3292, "ITF_WOMEN": 0.4367, "OTHER": 0.0016, "WTA": 0.0134, "WTA125": 0.0224}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5353, "share_primary_cause_market_settled_or_in_play": 0.463, "share_primary_cause_stale_quote_only": 0.1708}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7291, "identity_ambiguous_share": 0.1987, "ticker_orientation": {"VERIFIED": 7291}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4455, "with_external": 159, "coverage": 0.0357, "external_status": {"EXTERNAL_STALE": 114, "AGREES_WITH_KALSHI": 42, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 114, "MODEL_LONE_OUTLIER": 42, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2642, "share_external_supports_model": 0.0189}, "pregame_clean_ge_25pp": {"n": 2034, "with_external": 150, "coverage": 0.0737, "external_status": {"EXTERNAL_STALE": 107, "AGREES_WITH_KALSHI": 40, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 107, "MODEL_LONE_OUTLIER": 40, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2667, "share_external_supports_model": 0.02}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 553.5, "median_sample_ratio": 2.38, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2001, "data_status": {"POOR": 3893, "LIMITED": 2083, "ADEQUATE": 1315}, "comparison_lt_10pp": {"median_thinner_serve_points": 1794.0, "median_sample_ratio": 1.69, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 597, "model_minus_observed": 0.0502, "kalshi_minus_observed": -0.0814, "brier_diff_model_minus_kalshi": 0.0001}, "4-10x": {"n": 399, "model_minus_observed": 0.0731, "kalshi_minus_observed": -0.0661, "brier_diff_model_minus_kalshi": 0.0065}, "<2x": {"n": 1428, "model_minus_observed": 0.0809, "kalshi_minus_observed": -0.0415, "brier_diff_model_minus_kalshi": 0.0111}, ">=10x": {"n": 476, "model_minus_observed": 0.1194, "kalshi_minus_observed": -0.0489, "brier_diff_model_minus_kalshi": 0.0148}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2900, "model": {"intercept": -0.54, "slope": 0.864, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.236, "slope": 1.124, "slope_se": 0.053}, "mean_extremity_model": 0.1779, "mean_extremity_kalshi": 0.171, "model_brier": 0.2292, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.027, "brier_diff_se": 0.0035, "model_logloss": 0.6541, "kalshi_logloss": 0.5865}, "fair_v1": {"n": 2900, "model": {"intercept": -0.39, "slope": 1.059, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.329, "slope": 1.175, "slope_se": 0.055}, "mean_extremity_model": 0.1687, "mean_extremity_kalshi": 0.171, "model_brier": 0.2112, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.0088, "brier_diff_se": 0.0028, "model_logloss": 0.6098, "kalshi_logloss": 0.5867}, "gen1_elo": {"n": 2900, "model": {"intercept": -0.373, "slope": 1.04, "slope_se": 0.051}, "kalshi_mid_same_rows": {"intercept": 0.329, "slope": 1.164, "slope_se": 0.054}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2102, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.0079, "brier_diff_se": 0.0028, "model_logloss": 0.6086, "kalshi_logloss": 0.5865}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2413, "share_ge_15": 0.4337, "median_abs_gap": 12.9, "n": 18459}, "gen1_elo": {"share_ge_25": 0.2358, "share_ge_15": 0.4267, "median_abs_gap": 12.4, "n": 18459}, "gen1_sr": {"share_ge_25": 0.3025, "share_ge_15": 0.5208, "median_abs_gap": 15.74, "n": 18459}, "gen2": {"share_ge_25": 0.3029, "share_ge_15": 0.5067, "median_abs_gap": 15.35, "n": 18459}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1435, "share_ge_15": 0.3418, "median_abs_gap": 10.51, "n": 14173}, "gen1_elo": {"share_ge_25": 0.1412, "share_ge_15": 0.3307, "median_abs_gap": 10.0, "n": 14172}, "gen1_sr": {"share_ge_25": 0.2054, "share_ge_15": 0.4389, "median_abs_gap": 13.05, "n": 14173}, "gen2": {"share_ge_25": 0.2186, "share_ge_15": 0.436, "median_abs_gap": 12.86, "n": 14174}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0141, "share_ge_25_pregame_clean": 0.0138}, "WTA": {"median_abs_gap_pregame_clean": 7.85, "share_ge_25_all": 0.0616, "share_ge_25_pregame_clean": 0.0545}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2393, "share_within_10pp_all": 0.4406, "share_within_10pp_pregame_clean": 0.4997, "corr_model_vs_mid_pregame_clean": 0.8488}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 441, "model_brier": 0.1948, "kalshi_brier": 0.1963, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 510, "model_brier": 0.2105, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.0081}, "15-25": {"n_settled": 635, "model_brier": 0.2296, "kalshi_brier": 0.2174, "brier_diff_model_minus_kalshi": 0.0122}, "25-40": {"n_settled": 345, "model_brier": 0.2264, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.019}, "3-5": {"n_settled": 287, "model_brier": 0.1911, "kalshi_brier": 0.1914, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 72, "model_brier": 0.29, "kalshi_brier": 0.1741, "brier_diff_model_minus_kalshi": 0.116}, "5-10": {"n_settled": 610, "model_brier": 0.1959, "kalshi_brier": 0.1969, "brier_diff_model_minus_kalshi": -0.001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.54, "slope": 0.864, "slope_se": 0.047}, "kalshi_slope": {"intercept": 0.236, "slope": 1.124, "slope_se": 0.053}, "n": 2900}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.503, "slope": 0.87, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.16, "slope": 1.081, "slope_se": 0.04}, "n": 4877}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 297, "model_brier": 0.3338, "kalshi_brier": 0.2309, "brier_diff_model_minus_kalshi": 0.1029, "brier_diff_se": 0.0187, "corr_model_outcome": -0.0178, "corr_kalshi_outcome": 0.2748}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
