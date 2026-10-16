# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-16T12:06Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 34,774): 0-3 14.5%, 3-5 9.4%, 5-10 20.1%, 10-15 15.3%, 15-25 18.9%, 25-40 13.6%, 40+ 8.2%; median gap 11.88 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.9%, Challenger 12.2%, doubles 6.8%). Main tour: ATP 1.4% and WTA 6.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,608): MARKET_ALREADY_SETTLED_WHEN_PRICED 36.7%, STALE_QUOTE 18.1%, BOOK_QUALITY 17.4%, POOR_DATA 8.3%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 4.1%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 36.7%, market_freshness 18.1%, execution 17.4%, data 12.4%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 53.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 45.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,608 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.6% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 554.0 points vs 1769.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.056, Gen-2 0.866, Gen-1 ledger 0.868 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 354 model 0.2244 vs Kalshi 0.2093; n 72 model 0.29 vs Kalshi 0.1741.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 137,581 model-market comparisons (229,654 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 47,919 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-16T11:58:33.356711+00:00'], shadow board 38,631 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-16T11:58:36.079223+00:00'], Model 4 14,397 rows, 14,790 settled tickers, 4,996 tickers with an external scan.
* By model: {"gen1_ledger": 31428, "gen1_elo": 19422, "fair_v1": 19422, "gen2": 19422, "gen1_sr": 19422, "model4_fundamental": 14237, "model4_conditioned": 14228}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 34,774 | 14.5 | 9.4 | 20.1 | 15.3 | 18.9 | 13.6 | 8.2 | 11.88 | 40.8% | 21.9% |
| MW fair_v1 | 19,422 | 13.6 | 8.4 | 18.6 | 15.8 | 19.3 | 14.6 | 9.8 | 12.96 | 43.7% | 24.4% |
| MW gen1_elo | 19,422 | 13.1 | 9.0 | 19.7 | 15.1 | 19.2 | 14.3 | 9.5 | 12.47 | 43.0% | 23.8% |
| MW gen1_ledger | 15,352 | 15.6 | 10.7 | 21.9 | 14.7 | 18.4 | 12.4 | 6.2 | 10.45 | 37.2% | 18.7% |
| MW gen1_sr | 19,422 | 9.7 | 7.5 | 16.3 | 14.2 | 21.7 | 18.7 | 11.9 | 15.88 | 52.3% | 30.6% |
| MW gen2 | 19,422 | 11.4 | 7.1 | 16.5 | 14.2 | 20.1 | 17.6 | 13.1 | 15.41 | 50.8% | 30.7% |
| all families model4_conditioned | 14,228 | 21.7 | 20.1 | 35.2 | 16.7 | 4.3 | 1.1 | 0.9 | 5.81 | 6.3% | 2.0% |
| all families model4_fundamental | 14,237 | 16.8 | 13.6 | 35.8 | 19.6 | 10.5 | 2.6 | 1.1 | 7.56 | 14.2% | 3.7% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.49pp; >=10pp 45.4%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,344 | 30.6 | 14.6 | 25.3 | 17.3 | 10.2 | 1.1 | 0.8 | 5.67 | 12.1% | 1.9% |
| CHALLENGER | 3,245 | 16.1 | 9.8 | 20.1 | 15.8 | 14.5 | 12.2 | 11.5 | 11.46 | 38.1% | 23.6% |
| ITF_MEN | 5,568 | 11.0 | 8.2 | 17.6 | 14.8 | 19.9 | 16.2 | 12.2 | 14.32 | 48.3% | 28.4% |
| ITF_WOMEN | 7,656 | 10.5 | 6.6 | 16.3 | 15.8 | 22.2 | 17.9 | 10.8 | 15.37 | 50.9% | 28.7% |
| WTA | 982 | 21.0 | 10.9 | 24.9 | 15.6 | 20.8 | 5.7 | 1.1 | 8.16 | 27.6% | 6.8% |
| WTA125 | 627 | 13.1 | 7.7 | 22.8 | 20.6 | 20.1 | 13.7 | 2.1 | 11.31 | 35.9% | 15.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,344 | 24.9 | 14.4 | 24.9 | 18.7 | 14.3 | 1.9 | 1.0 | 6.54 | 17.1% | 2.8% |
| CHALLENGER | 3,245 | 14.8 | 7.9 | 19.6 | 13.4 | 18.1 | 14.2 | 12.1 | 12.67 | 44.3% | 26.2% |
| ITF_MEN | 5,568 | 9.6 | 6.8 | 15.9 | 13.7 | 19.9 | 19.2 | 14.8 | 16.63 | 54.0% | 34.1% |
| ITF_WOMEN | 7,656 | 8.6 | 5.7 | 13.8 | 13.5 | 21.5 | 20.7 | 16.2 | 18.55 | 58.4% | 36.9% |
| WTA | 982 | 17.1 | 8.2 | 19.4 | 16.2 | 22.5 | 15.5 | 1.2 | 11.9 | 39.2% | 16.7% |
| WTA125 | 627 | 6.4 | 4.6 | 17.2 | 18.0 | 24.9 | 19.6 | 9.2 | 17.0 | 53.8% | 28.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,344 | 28.1 | 14.3 | 28.7 | 15.2 | 10.3 | 2.5 | 0.9 | 6.03 | 13.7% | 3.4% |
| CHALLENGER | 3,245 | 14.9 | 10.3 | 20.8 | 15.0 | 15.4 | 11.8 | 11.8 | 10.98 | 39.0% | 23.5% |
| ITF_MEN | 5,568 | 10.1 | 8.2 | 18.2 | 14.1 | 20.5 | 16.5 | 12.4 | 14.79 | 49.4% | 28.9% |
| ITF_WOMEN | 7,656 | 10.0 | 7.0 | 16.5 | 15.8 | 22.9 | 18.0 | 9.9 | 15.33 | 50.8% | 27.9% |
| WTA | 982 | 22.6 | 15.4 | 32.2 | 16.2 | 10.5 | 2.4 | 0.7 | 6.17 | 13.7% | 3.2% |
| WTA125 | 627 | 22.5 | 12.4 | 29.0 | 15.2 | 14.5 | 6.1 | 0.3 | 7.71 | 20.9% | 6.4% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 731 | 31.1 | 22.9 | 35.3 | 9.2 | 1.2 | 0.4 | 0.0 | 4.69 | 1.6% | 0.4% |
| CHALLENGER | 2,226 | 22.4 | 15.3 | 27.7 | 14.7 | 12.8 | 5.2 | 2.0 | 6.94 | 20.0% | 7.2% |
| DOUBLES | 1,050 | 5.3 | 3.7 | 11.4 | 10.8 | 19.7 | 24.3 | 24.8 | 24.16 | 68.8% | 49.0% |
| ITF_MEN | 4,728 | 14.7 | 8.6 | 20.6 | 15.4 | 20.9 | 12.6 | 7.2 | 11.89 | 40.6% | 19.8% |
| ITF_WOMEN | 5,094 | 11.7 | 9.3 | 19.7 | 14.6 | 22.3 | 16.6 | 5.7 | 13.01 | 44.7% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 677 | 21.3 | 15.2 | 27.2 | 17.4 | 13.4 | 5.0 | 0.4 | 7.52 | 18.9% | 5.5% |
| WTA125 | 697 | 20.4 | 13.8 | 22.8 | 18.4 | 14.3 | 8.2 | 2.1 | 8.3 | 24.7% | 10.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,330 | 30.6 | 14.5 | 25.5 | 17.4 | 10.2 | 1.1 | 0.8 | 5.69 | 12.0% | 1.9% |
| CHALLENGER | 2,325 | 20.9 | 12.3 | 25.2 | 18.4 | 14.9 | 5.9 | 2.4 | 8.27 | 23.2% | 8.3% |
| ITF_MEN | 4,067 | 13.4 | 10.1 | 20.9 | 16.6 | 20.3 | 13.1 | 5.6 | 11.49 | 39.0% | 18.7% |
| ITF_WOMEN | 5,715 | 12.4 | 7.9 | 18.5 | 17.9 | 23.6 | 14.9 | 4.7 | 12.99 | 43.2% | 19.6% |
| WTA | 962 | 21.2 | 10.3 | 25.3 | 15.6 | 20.9 | 5.6 | 1.1 | 8.18 | 27.7% | 6.8% |
| WTA125 | 603 | 13.4 | 7.5 | 22.2 | 20.9 | 20.7 | 13.6 | 1.7 | 11.33 | 36.0% | 15.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,330 | 24.7 | 14.5 | 25.0 | 18.6 | 14.3 | 1.8 | 1.0 | 6.55 | 17.1% | 2.8% |
| CHALLENGER | 2,325 | 18.9 | 10.1 | 24.3 | 16.2 | 18.3 | 9.5 | 2.6 | 9.07 | 30.4% | 12.1% |
| ITF_MEN | 4,068 | 11.3 | 8.1 | 18.2 | 15.3 | 21.9 | 16.7 | 8.4 | 14.02 | 47.0% | 25.1% |
| ITF_WOMEN | 5,715 | 9.8 | 6.5 | 15.4 | 14.7 | 23.5 | 19.9 | 10.2 | 16.27 | 53.6% | 30.1% |
| WTA | 962 | 17.1 | 8.0 | 19.3 | 16.2 | 22.6 | 15.6 | 1.2 | 12.08 | 39.4% | 16.8% |
| WTA125 | 603 | 6.1 | 4.8 | 17.2 | 18.4 | 24.7 | 20.2 | 8.5 | 16.84 | 53.4% | 28.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 711 | 31.1 | 23.1 | 35.6 | 9.3 | 0.6 | 0.4 | 0.0 | 4.64 | 1.0% | 0.4% |
| CHALLENGER | 1,919 | 24.2 | 16.6 | 29.8 | 14.5 | 11.8 | 2.5 | 0.6 | 6.34 | 14.9% | 3.1% |
| DOUBLES | 967 | 5.5 | 3.8 | 11.8 | 10.9 | 19.6 | 24.3 | 24.1 | 24.07 | 68.0% | 48.4% |
| ITF_MEN | 3,898 | 16.2 | 9.4 | 22.5 | 16.3 | 20.8 | 10.6 | 4.3 | 10.59 | 35.6% | 14.9% |
| ITF_WOMEN | 4,162 | 12.9 | 10.0 | 21.5 | 15.5 | 22.6 | 15.0 | 2.6 | 11.56 | 40.2% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 643 | 21.8 | 15.9 | 27.4 | 17.4 | 13.7 | 3.9 | 0.0 | 7.21 | 17.6% | 3.9% |
| WTA125 | 592 | 22.3 | 15.2 | 24.3 | 19.9 | 12.8 | 5.1 | 0.3 | 7.38 | 18.2% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,050 | 5.3 | 3.7 | 11.4 | 10.8 | 19.7 | 24.3 | 24.8 | 24.16 | 68.8% | 49.0% |
| singles | 14,302 | 16.3 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 4.9 | 9.95 | 34.8% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,575 | 13.5 | 8.9 | 19.4 | 15.8 | 17.9 | 14.5 | 10.1 | 12.66 | 42.5% | 24.6% |
| Grass | 215 | 11.2 | 11.6 | 17.2 | 13.5 | 22.8 | 16.3 | 7.4 | 14.16 | 46.5% | 23.7% |
| Hard | 12,562 | 13.9 | 8.4 | 18.6 | 15.3 | 19.8 | 14.4 | 9.7 | 12.99 | 43.9% | 24.1% |
| UNKNOWN | 2,070 | 12.2 | 7.2 | 17.0 | 18.8 | 19.0 | 15.7 | 10.1 | 13.32 | 44.8% | 25.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,619 | 19.9 | 10.6 | 21.1 | 16.9 | 15.7 | 8.9 | 6.9 | 9.51 | 31.6% | 15.8% |
| B | 2,537 | 14.2 | 8.9 | 19.9 | 16.5 | 18.3 | 12.5 | 9.7 | 11.77 | 40.5% | 22.2% |
| C | 2,811 | 12.8 | 9.5 | 20.0 | 14.2 | 19.2 | 14.3 | 9.9 | 12.66 | 43.4% | 24.2% |
| D | 3,364 | 11.6 | 7.9 | 17.6 | 16.1 | 22.1 | 15.3 | 9.5 | 13.91 | 46.9% | 24.8% |
| F | 5,091 | 8.1 | 5.4 | 15.0 | 14.9 | 21.9 | 21.5 | 13.3 | 17.93 | 56.6% | 34.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,464 | 22.9 | 15.8 | 28.9 | 15.2 | 11.2 | 4.4 | 1.7 | 6.7 | 17.2% | 6.1% |
| B | 2,294 | 14.9 | 10.0 | 23.9 | 16.4 | 19.5 | 11.1 | 4.2 | 10.21 | 34.8% | 15.3% |
| C | 3,035 | 12.1 | 7.8 | 18.2 | 14.1 | 20.7 | 15.8 | 11.4 | 13.95 | 47.8% | 27.2% |
| D | 2,297 | 13.9 | 9.8 | 20.8 | 13.6 | 21.4 | 13.9 | 6.5 | 11.86 | 41.8% | 20.4% |
| F | 3,262 | 10.4 | 7.6 | 15.2 | 14.0 | 23.5 | 20.3 | 9.0 | 16.28 | 52.8% | 29.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 6,362 | 18.1 | 9.6 | 20.3 | 16.7 | 16.2 | 10.0 | 9.1 | 10.52 | 35.3% | 19.1% |
| LIMITED | 4,496 | 14.8 | 10.3 | 20.9 | 15.3 | 18.6 | 12.8 | 7.3 | 11.19 | 38.7% | 20.1% |
| POOR | 8,564 | 9.6 | 6.5 | 16.0 | 15.4 | 21.9 | 18.9 | 11.7 | 15.92 | 52.5% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,066 | 31.2 | 24.6 | 36.2 | 5.6 | 1.7 | 0.7 | 0.1 | 4.48 | 2.5% | 0.7% |
| GAME_SPREAD | 2,908 | 25.8 | 16.3 | 36.5 | 16.8 | 4.1 | 0.4 | 0.2 | 5.96 | 4.7% | 0.6% |
| MATCH_WINNER | 15,352 | 15.6 | 10.7 | 21.9 | 14.7 | 18.4 | 12.4 | 6.2 | 10.45 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,628 | 33.1 | 19.4 | 30.9 | 9.8 | 5.4 | 1.2 | 0.2 | 4.76 | 6.9% | 1.5% |
| TOTAL_GAMES | 4,450 | 6.7 | 9.2 | 39.4 | 29.4 | 10.3 | 2.6 | 2.3 | 9.44 | 15.3% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,969 | 25.7 | 38.3 | 31.3 | 0.3 | 3.8 | 0.4 | 0.1 | 4.29 | 4.4% | 0.5% |
| GAME_SPREAD | 3,539 | 45.5 | 16.6 | 28.5 | 7.2 | 1.1 | 0.7 | 0.4 | 3.53 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,720 | 3.5 | 6.6 | 42.7 | 36.8 | 6.8 | 1.9 | 1.9 | 9.77 | 10.5% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,969 | 26.5 | 18.9 | 37.0 | 9.1 | 6.2 | 2.0 | 0.3 | 5.47 | 8.5% | 2.4% |
| GAME_SPREAD | 3,539 | 19.6 | 13.6 | 30.4 | 20.8 | 12.7 | 2.3 | 0.7 | 7.64 | 15.7% | 3.0% |
| TOTAL_GAMES | 5,729 | 6.7 | 9.1 | 38.0 | 27.9 | 13.0 | 3.2 | 2.1 | 9.6 | 18.3% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 19,422 | 43.7% | 24.4% | 12.96 | 34.9% | 15.0% | 10.64 |
| gen1_elo | 19,422 | 43.0% | 23.8% | 12.47 | 33.9% | 14.8% | 10.11 |
| gen1_sr | 19,422 | 52.3% | 30.6% | 15.88 | 44.5% | 21.3% | 13.29 |
| gen2 | 19,422 | 50.8% | 30.7% | 15.41 | 44.1% | 22.6% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 10,350 | 16.4 | 10.3 | 21.6 | 17.2 | 19.7 | 11.3 | 3.3 | 10.43 | 34.3% | 14.6% |
| STALE | 9,072 | 10.3 | 6.2 | 15.1 | 14.1 | 18.8 | 18.3 | 17.2 | 17.19 | 54.3% | 35.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,820 | 17.4 | 11.6 | 23.6 | 14.6 | 17.0 | 11.2 | 4.8 | 9.4 | 33.0% | 16.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 34,774 | 8820 | 13822 | 12132 | 24.4 | 154.2 | 1400.4 |
| ge_15pp | 14,187 | 2906 | 4842 | 6439 | 26.9 | 455.5 | 1380.4 |
| ge_25pp | 7,608 | 1410 | 2102 | 4096 | 34.5 | 586.0 | 1380.4 |
| lt_10pp | 15,275 | 4629 | 6644 | 4002 | 22.4 | 48.7 | 1341.5 |

Current slate `SL-20261016T120605Z-f17e2290`: 275 priced rows, quote age at build {'median': 7.8, 'max': 7.9}, freshness {'FRESH': 275}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 10 | 0.0 | 0.0 | 40.0 | 0.0 | 40.0 | 20.0 | 0.0 | 20.33 | 60.0% | 20.0% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,671 | 21.4 | 10.7 | 22.9 | 18.2 | 19.1 | 7.1 | 0.6 | 8.75 | 26.8% | 7.7% |
| KALSHI_LONE_OUTLIER | 8 | 12.5 | 0.0 | 62.5 | 0.0 | 12.5 | 12.5 | 0.0 | 5.11 | 25.0% | 12.5% |
| MARKETS_AGREE | 268 | 70.9 | 29.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.09 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 541 | 0.0 | 3.7 | 35.1 | 27.7 | 23.8 | 8.7 | 0.9 | 11.66 | 33.5% | 9.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 19,422 | 2509 (12.9%) | 21.6% | 0.7% | {"EXTERNAL_STALE": 1671, "AGREES_WITH_KALSHI": 541, "ALL_AGREE": 268, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 9, "AGREES_WITH_MODEL": 8, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 8,482 | 637 (7.5%) | 28.4% | 1.3% | {"EXTERNAL_STALE": 448, "AGREES_WITH_KALSHI": 181, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,736 | 184 (3.9%) | 28.3% | 1.6% | {"EXTERNAL_STALE": 129, "AGREES_WITH_KALSHI": 52, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,254 | 174 (7.7%) | 28.7% | 1.7% | {"EXTERNAL_STALE": 121, "AGREES_WITH_KALSHI": 50, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,877 | 1418 (18.0%) | 14.8% | 0.6% | {"EXTERNAL_STALE": 919, "ALL_AGREE": 268, "AGREES_WITH_KALSHI": 210, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 6, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,764 | 11.2 | 7.7 | 19.7 | 15.0 | 21.9 | 14.3 | 10.1 | 13.66 | 46.3% | 24.4% |
| 4-10x | 2,519 | 12.7 | 8.9 | 19.6 | 15.5 | 19.0 | 15.3 | 9.0 | 12.72 | 43.3% | 24.3% |
| <2x | 10,127 | 15.5 | 9.1 | 18.9 | 16.7 | 17.8 | 13.0 | 9.1 | 11.91 | 39.9% | 22.1% |
| >=10x | 3,012 | 10.9 | 6.5 | 15.2 | 13.8 | 21.4 | 19.4 | 12.7 | 16.44 | 53.5% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,117 | 13.7 | 8.2 | 19.4 | 15.9 | 19.6 | 12.9 | 10.3 | 12.71 | 42.8% | 23.2% |
| 300-1000 | 4,390 | 12.0 | 8.7 | 17.4 | 16.0 | 21.0 | 15.8 | 9.2 | 13.67 | 46.0% | 25.0% |
| <300 | 5,772 | 9.1 | 6.1 | 15.7 | 14.7 | 21.6 | 20.2 | 12.7 | 16.81 | 54.5% | 32.9% |
| >=3000 | 4,143 | 21.5 | 11.6 | 22.9 | 16.9 | 13.9 | 7.5 | 5.8 | 8.38 | 27.2% | 13.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 608 | 0.5372 | 0.4059 | 0.4885 | +0.049 | -0.083 | -0.0003 ± 0.0059 |
| ratio 4-10x | 407 | 0.5855 | 0.4466 | 0.5111 | +0.074 | -0.065 | 0.0071 ± 0.0078 |
| ratio <2x | 1488 | 0.5363 | 0.4142 | 0.455 | +0.081 | -0.041 | 0.0109 ± 0.0037 |
| ratio >=10x | 495 | 0.5461 | 0.3792 | 0.4202 | +0.126 | -0.041 | 0.0161 ± 0.0079 |
| thinner_sample 1000-3000 | 835 | 0.5419 | 0.4172 | 0.4719 | +0.070 | -0.055 | 0.0048 ± 0.0049 |
| thinner_sample 300-1000 | 722 | 0.5598 | 0.4225 | 0.4875 | +0.072 | -0.065 | 0.0014 ± 0.0057 |
| thinner_sample <300 | 931 | 0.544 | 0.3835 | 0.4372 | +0.107 | -0.054 | 0.0159 ± 0.0056 |
| thinner_sample >=3000 | 510 | 0.5295 | 0.4354 | 0.4647 | +0.065 | -0.029 | 0.0138 ± 0.0052 |
| data_status ADEQUATE | 863 | 0.5326 | 0.4285 | 0.4612 | +0.071 | -0.033 | 0.0088 ± 0.0042 |
| data_status LIMITED | 750 | 0.5511 | 0.4223 | 0.4907 | +0.060 | -0.068 | 0.0024 ± 0.0053 |
| data_status POOR | 1385 | 0.5489 | 0.3942 | 0.4505 | +0.098 | -0.056 | 0.0126 ± 0.0045 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 462 | 0.194 | 0.1955 | -0.0014 ± 0.0007 | 0.5664 | 0.5694 | 0.4933 | 0.4784 | 0.5303 | -0.040 ± 0.0215 | -0.01 (5) |
| 3-5 | 293 | 0.1903 | 0.1907 | -0.0004 ± 0.002 | 0.5605 | 0.56 | 0.5091 | 0.4692 | 0.4915 | -0.070 ± 0.0262 | 0.02 (1) |
| 5-10 | 631 | 0.1954 | 0.1955 | -0.0001 ± 0.0027 | 0.5756 | 0.5734 | 0.509 | 0.4345 | 0.4643 | -0.083 ± 0.0183 | -0.0167 (6) |
| 10-15 | 531 | 0.2128 | 0.2046 | +0.0083 ± 0.0049 | 0.6134 | 0.5911 | 0.5194 | 0.3955 | 0.4237 | -0.085 ± 0.0196 | -0.048 (5) |
| 15-25 | 655 | 0.2315 | 0.2168 | +0.0147 ± 0.0071 | 0.6583 | 0.6196 | 0.5761 | 0.3809 | 0.4427 | -0.078 ± 0.018 | -0.0075 (8) |
| 25-40 | 354 | 0.2244 | 0.2093 | +0.0151 ± 0.0145 | 0.6392 | 0.6006 | 0.6448 | 0.3361 | 0.4661 | -0.060 ± 0.0222 | -0.01 (1) |
| 40+ | 72 | 0.29 | 0.1741 | +0.1160 ± 0.0438 | 0.7878 | 0.5206 | 0.7443 | 0.2967 | 0.3889 | -0.113 ± 0.0433 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2171 | 0.1772 | 0.1783 | -0.0011 ± 0.0003 | 0.5278 | 0.5289 | 0.4779 | 0.4629 | 0.4979 | -0.020 ± 0.0092 | -0.0129 (17) |
| 3-5 | 1329 | 0.193 | 0.1914 | +0.0016 ± 0.001 | 0.5664 | 0.5584 | 0.4807 | 0.441 | 0.4372 | -0.062 ± 0.0122 | 0.0 (2) |
| 5-10 | 2940 | 0.1917 | 0.1897 | +0.0020 ± 0.0012 | 0.5655 | 0.5572 | 0.4832 | 0.4093 | 0.4293 | -0.044 ± 0.0082 | -0.0119 (21) |
| 10-15 | 2541 | 0.2021 | 0.1832 | +0.0189 ± 0.0021 | 0.5903 | 0.5385 | 0.4794 | 0.3549 | 0.342 | -0.076 ± 0.0085 | -0.0281 (16) |
| 15-25 | 3104 | 0.2097 | 0.1725 | +0.0373 ± 0.0029 | 0.612 | 0.5086 | 0.5019 | 0.3059 | 0.3102 | -0.068 ± 0.0074 | -0.0033 (42) |
| 25-40 | 2428 | 0.22 | 0.1272 | +0.0928 ± 0.0045 | 0.6331 | 0.3911 | 0.5278 | 0.2149 | 0.2269 | -0.059 ± 0.007 | -0.01 (1) |
| 40+ | 1632 | 0.3753 | 0.0433 | +0.3320 ± 0.0058 | 0.9768 | 0.1712 | 0.6262 | 0.1051 | 0.0576 | -0.084 ± 0.0048 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 350 | 0.198 | 0.1985 | -0.0005 ± 0.0008 | 0.5774 | 0.5785 | 0.5007 | 0.4855 | 0.5086 | -0.077 ± 0.025 | -0.01 (3) |
| 3-5 | 239 | 0.2098 | 0.2088 | +0.0010 ± 0.0024 | 0.6016 | 0.6007 | 0.5177 | 0.4777 | 0.4812 | -0.083 ± 0.0312 | 0.02 (1) |
| 5-10 | 540 | 0.1981 | 0.1971 | +0.0010 ± 0.0029 | 0.5792 | 0.5769 | 0.5509 | 0.4761 | 0.5074 | -0.073 ± 0.0198 | -0.01 (4) |
| 10-15 | 490 | 0.2131 | 0.2052 | +0.0079 ± 0.0051 | 0.6124 | 0.5948 | 0.5677 | 0.4433 | 0.4776 | -0.088 ± 0.0214 | -0.04 (5) |
| 15-25 | 726 | 0.2288 | 0.21 | +0.0188 ± 0.0067 | 0.6494 | 0.6026 | 0.5874 | 0.3906 | 0.4449 | -0.083 ± 0.0172 | -0.0188 (8) |
| 25-40 | 473 | 0.2657 | 0.202 | +0.0636 ± 0.013 | 0.7432 | 0.586 | 0.6603 | 0.3458 | 0.4038 | -0.106 ± 0.0205 | -0.0075 (4) |
| 40+ | 180 | 0.3557 | 0.1799 | +0.1758 ± 0.0308 | 0.9838 | 0.5308 | 0.738 | 0.2579 | 0.3278 | -0.063 ± 0.0305 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1832 | 0.1829 | 0.1833 | -0.0004 ± 0.0003 | 0.5411 | 0.5419 | 0.4969 | 0.4822 | 0.5066 | -0.032 ± 0.0103 | -0.0133 (15) |
| 3-5 | 1164 | 0.1924 | 0.1917 | +0.0007 ± 0.001 | 0.5595 | 0.5578 | 0.5161 | 0.4761 | 0.4863 | -0.041 ± 0.0131 | 0.02 (1) |
| 5-10 | 2580 | 0.1906 | 0.1877 | +0.0029 ± 0.0013 | 0.5634 | 0.5526 | 0.5121 | 0.4382 | 0.4574 | -0.043 ± 0.0087 | -0.0117 (6) |
| 10-15 | 2248 | 0.1949 | 0.1823 | +0.0127 ± 0.0023 | 0.5747 | 0.534 | 0.5178 | 0.3935 | 0.4079 | -0.054 ± 0.0092 | -0.02 (17) |
| 15-25 | 3266 | 0.2163 | 0.1774 | +0.0390 ± 0.0029 | 0.6284 | 0.5225 | 0.5318 | 0.3353 | 0.3377 | -0.071 ± 0.0074 | -0.0095 (41) |
| 25-40 | 2862 | 0.2488 | 0.139 | +0.1098 ± 0.0044 | 0.7047 | 0.4237 | 0.5596 | 0.2435 | 0.2299 | -0.082 ± 0.007 | -0.0044 (18) |
| 40+ | 2193 | 0.3981 | 0.0682 | +0.3298 ± 0.0064 | 1.044 | 0.237 | 0.6625 | 0.1266 | 0.1003 | -0.066 ± 0.0055 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 453 | 0.1927 | 0.1954 | -0.0026 ± 0.0007 | 0.5644 | 0.571 | 0.4943 | 0.4791 | 0.5541 | -0.002 ± 0.0211 | -0.0137 (8) |
| 3-5 | 323 | 0.1872 | 0.1851 | +0.0021 ± 0.0019 | 0.5501 | 0.5452 | 0.4961 | 0.4567 | 0.452 | -0.115 ± 0.0252 | 0.0067 (3) |
| 5-10 | 663 | 0.2016 | 0.198 | +0.0036 ± 0.0026 | 0.5905 | 0.5783 | 0.5044 | 0.4306 | 0.4404 | -0.093 ± 0.0177 | -0.0071 (7) |
| 10-15 | 517 | 0.2082 | 0.2083 | -0.0000 ± 0.0049 | 0.6041 | 0.6002 | 0.5361 | 0.4131 | 0.4778 | -0.060 ± 0.0199 | -0.0317 (6) |
| 15-25 | 604 | 0.2367 | 0.2114 | +0.0253 ± 0.0073 | 0.6733 | 0.6072 | 0.5842 | 0.3907 | 0.4222 | -0.108 ± 0.0185 | -0.03 (1) |
| 25-40 | 371 | 0.2106 | 0.213 | -0.0024 ± 0.014 | 0.6085 | 0.6093 | 0.6499 | 0.3398 | 0.496 | -0.040 ± 0.0213 | 0.0 (1) |
| 40+ | 67 | 0.3098 | 0.1842 | +0.1256 ± 0.0472 | 0.8354 | 0.5436 | 0.749 | 0.2957 | 0.3881 | -0.101 ± 0.0493 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2075 | 0.1836 | 0.1846 | -0.0010 ± 0.0003 | 0.5417 | 0.5435 | 0.482 | 0.4667 | 0.4964 | -0.023 ± 0.0095 | -0.0163 (35) |
| 3-5 | 1412 | 0.1853 | 0.1825 | +0.0028 ± 0.0009 | 0.5471 | 0.5403 | 0.4767 | 0.4373 | 0.4221 | -0.078 ± 0.0117 | -0.0094 (18) |
| 5-10 | 3131 | 0.194 | 0.1877 | +0.0063 ± 0.0012 | 0.572 | 0.5514 | 0.4795 | 0.4056 | 0.3983 | -0.068 ± 0.0078 | -0.01 (31) |
| 10-15 | 2400 | 0.1955 | 0.1813 | +0.0142 ± 0.0022 | 0.5755 | 0.5326 | 0.4963 | 0.373 | 0.3775 | -0.062 ± 0.0086 | -0.015 (12) |
| 15-25 | 3169 | 0.2111 | 0.1711 | +0.0400 ± 0.0029 | 0.617 | 0.5062 | 0.5058 | 0.3107 | 0.3074 | -0.073 ± 0.0074 | -0.03 (2) |
| 25-40 | 2380 | 0.2148 | 0.126 | +0.0888 ± 0.0046 | 0.6213 | 0.3872 | 0.5251 | 0.2097 | 0.2303 | -0.054 ± 0.0069 | 0.0 (1) |
| 40+ | 1578 | 0.3887 | 0.0458 | +0.3429 ± 0.0061 | 1.0143 | 0.1777 | 0.6348 | 0.1077 | 0.0577 | -0.085 ± 0.0051 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 781 | 0.1964 | 0.1967 | -0.0003 ± 0.0006 | 0.5738 | 0.5742 | 0.5057 | 0.4907 | 0.4981 | -0.047 ± 0.0159 | -0.0224 (49) |
| 3-5 | 559 | 0.1943 | 0.194 | +0.0003 ± 0.0015 | 0.5666 | 0.5644 | 0.4807 | 0.441 | 0.4544 | -0.044 ± 0.0187 | -0.0194 (34) |
| 5-10 | 1169 | 0.196 | 0.1905 | +0.0055 ± 0.0019 | 0.578 | 0.5622 | 0.4877 | 0.4141 | 0.414 | -0.062 ± 0.013 | -0.005 (78) |
| 10-15 | 734 | 0.2074 | 0.1967 | +0.0107 ± 0.0041 | 0.6036 | 0.5753 | 0.504 | 0.381 | 0.3978 | -0.052 ± 0.0165 | 0.0014 (64) |
| 15-25 | 985 | 0.2337 | 0.2121 | +0.0216 ± 0.0058 | 0.6661 | 0.6102 | 0.563 | 0.3683 | 0.4112 | -0.054 ± 0.0147 | -0.0216 (58) |
| 25-40 | 570 | 0.2523 | 0.1961 | +0.0562 ± 0.0115 | 0.7109 | 0.5697 | 0.6447 | 0.3321 | 0.3965 | -0.081 ± 0.0173 | -0.0219 (26) |
| 40+ | 193 | 0.3701 | 0.1933 | +0.1769 ± 0.0321 | 1.0713 | 0.5679 | 0.793 | 0.3026 | 0.3886 | -0.075 ± 0.029 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2334 | 0.188 | 0.1882 | -0.0002 ± 0.0003 | 0.5519 | 0.5512 | 0.5027 | 0.4873 | 0.4991 | -0.033 ± 0.0089 | -0.0157 (88) |
| 3-5 | 1596 | 0.1881 | 0.1857 | +0.0024 ± 0.0009 | 0.5507 | 0.5451 | 0.4886 | 0.449 | 0.4392 | -0.056 ± 0.0108 | -0.0209 (69) |
| 5-10 | 3258 | 0.1928 | 0.1854 | +0.0074 ± 0.0011 | 0.5701 | 0.5487 | 0.4814 | 0.4077 | 0.3972 | -0.062 ± 0.0076 | -0.0082 (132) |
| 10-15 | 2186 | 0.2041 | 0.1897 | +0.0144 ± 0.0023 | 0.5962 | 0.5578 | 0.5098 | 0.3868 | 0.3898 | -0.056 ± 0.0093 | -0.0053 (105) |
| 15-25 | 2756 | 0.2301 | 0.1986 | +0.0315 ± 0.0033 | 0.6636 | 0.5768 | 0.5548 | 0.3597 | 0.3781 | -0.060 ± 0.0085 | -0.0255 (106) |
| 25-40 | 1877 | 0.2544 | 0.1701 | +0.0843 ± 0.006 | 0.721 | 0.5022 | 0.6067 | 0.2924 | 0.3175 | -0.075 ± 0.0092 | -0.0229 (51) |
| 40+ | 910 | 0.3847 | 0.1312 | +0.2535 ± 0.0128 | 1.0915 | 0.4003 | 0.709 | 0.2021 | 0.2187 | -0.068 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2998 | 1.056 ± 0.051 | 1.165 | 0.1686 | 0.1714 | 0.2114 | 0.2024 |
| gen2 | 2998 | 0.866 ± 0.047 | 1.119 | 0.1761 | 0.1715 | 0.229 | 0.2024 |
| gen1_elo | 2998 | 1.038 ± 0.05 | 1.151 | 0.1737 | 0.1718 | 0.2105 | 0.2022 |
| gen1_sr | 2998 | 1.078 ± 0.061 | 1.185 | 0.1356 | 0.1733 | 0.2251 | 0.2022 |
| gen1_ledger | 4991 | 0.868 ± 0.035 | 1.073 | 0.1771 | 0.1862 | 0.2182 | 0.1978 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 14,187)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,534 | 24.9% |
| STALE_QUOTE | market_freshness | 2,961 | 20.9% |
| BOOK_QUALITY | execution | 2,545 | 17.9% |
| POOR_DATA | data | 1,572 | 11.1% |
| LIMITED_DATA | data | 1,023 | 7.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 760 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 680 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 556 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 397 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 159 | 1.1% |

Cause class: coverage 24.9%, market_freshness 20.9%, data 18.3%, execution 17.9%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.8%, mapping 3.9%, model_calibration 1.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 69.2%, THIN_PLAYER_HISTORY 58.0%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 45.4%, MODEL_INTERNAL_DISAGREEMENT 39.3%, ASYMMETRIC_SAMPLE_SIZE 31.8%, WIDE_SPREAD 23.7%, MODEL_HIGH_UNCERTAINTY 17.4%, PLAYER_IDENTITY_RISK 13.9%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 27.3%, POST_SETTLEMENT_OBSERVATION 24.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,608)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,790 | 36.7% |
| STALE_QUOTE | market_freshness | 1,381 | 18.1% |
| BOOK_QUALITY | execution | 1,321 | 17.4% |
| POOR_DATA | data | 635 | 8.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 410 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 325 | 4.3% |
| LIMITED_DATA | data | 309 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 244 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 155 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 38 | 0.5% |

Cause class: coverage 36.7%, market_freshness 18.1%, execution 17.4%, data 12.4%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.0%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 72.7%, THIN_PLAYER_HISTORY 60.2%, STALE_KALSHI_QUOTE 53.8%, STALE_PLAYER_DATA 47.4%, MODEL_INTERNAL_DISAGREEMENT 40.2%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 17.3%, EVENT_MAPPING_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 8.1%, LEVEL_TRANSFER_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 1.0%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 39.4%, POST_SETTLEMENT_OBSERVATION 36.7%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6096, "IDENTITY_AMBIGUOUS": 1512}; ticker orientation: {"VERIFIED": 7608}.

Checks: discipline:AMBIGUOUS 515, discipline:PASS 7093, identity_confidence:AMBIGUOUS 1316, identity_confidence:PASS 6292, level_mapping:NA 527, level_mapping:PASS 7081, market_pair:AMBIGUOUS 279, market_pair:NA 183, market_pair:PASS 7146, model_complement:NA 150, model_complement:PASS 7458, namesake:PASS 7608, physical_match_id:NA 2872, physical_match_id:PASS 4736, player_ids:PASS 7608, same_pair_other_event:PASS 7608, ticker_orientation:PASS 7608

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,075 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.24 | 0.2092 / 0.2117 (257) | 16.3% | 0.5% | 5.3% | 1.6% |
| CHALLENGER | 5,471 | 16.9% | 6.0% | 12.2% | {"coverage": 560, "market_freshness": 113, "market_freshness/coverage": 113, "data": 65, "model_calibration_or_unknown": 48, "execution": 13, "model_calibration": 9, "mapping": 6} | 7.17 | 0.2169 / 0.2044 (1425) | 37.2% | 9.3% | 2.4% | 22.4% |
| DOUBLES | 1,050 | 49.0% | 48.4% | 6.8% | {"execution": 210, "mapping": 152, "market_freshness": 106, "market_freshness/coverage": 40, "coverage": 7} | 24.07 | 0.3313 / 0.2336 (317) | 22.3% | 0.0% | 100.0% | 7.9% |
| ITF_MEN | 10,296 | 24.4% | 16.8% | 33.0% | {"coverage": 972, "execution": 512, "market_freshness": 394, "data": 346, "market_freshness/coverage": 202, "mapping": 86, "model_calibration_or_unknown": 2} | 11.12 | 0.2138 / 0.1953 (2538) | 36.4% | 60.7% | 12.0% | 22.6% |
| ITF_WOMEN | 12,750 | 26.2% | 18.7% | 43.9% | {"coverage": 1234, "market_freshness": 673, "execution": 552, "data": 499, "market_freshness/coverage": 252, "mapping": 75, "model_calibration_or_unknown": 41, "model_calibration": 10} | 12.49 | 0.2021 / 0.192 (2672) | 39.2% | 57.4% | 10.0% | 22.5% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,659 | 6.3% | 5.6% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "execution": 12, "data": 11, "market_freshness/coverage": 10, "model_calibration": 8, "coverage": 4, "mapping": 1} | 7.82 | 0.2398 / 0.2312 (289) | 25.9% | 1.5% | 1.8% | 3.2% |
| WTA125 | 1,324 | 12.9% | 10.4% | 2.2% | {"model_calibration_or_unknown": 40, "market_freshness": 37, "market_freshness/coverage": 35, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.38 | 0.2155 / 0.2055 (449) | 23.0% | 7.7% | 4.4% | 9.7% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 22 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 23 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 24 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 25 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 26 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 28 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 29 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 30 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 32 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 33 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 34 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 35 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 36 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 37 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 38 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 42 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 43 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 44 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 45 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 46 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 47 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |
| 49 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 50 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9825, "by_level_share_of_ge_25pp": {"ATP": 0.0038, "CHALLENGER": 0.1218, "DOUBLES": 0.0677, "ITF_MEN": 0.3304, "ITF_WOMEN": 0.4385, "OTHER": 0.0016, "WTA": 0.0137, "WTA125": 0.0225}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5384, "share_primary_cause_market_settled_or_in_play": 0.4527, "share_primary_cause_stale_quote_only": 0.1815}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7608, "identity_ambiguous_share": 0.1987, "ticker_orientation": {"VERIFIED": 7608}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4736, "with_external": 184, "coverage": 0.0389, "external_status": {"EXTERNAL_STALE": 129, "AGREES_WITH_KALSHI": 52, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 129, "MODEL_LONE_OUTLIER": 52, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2826, "share_external_supports_model": 0.0163}, "pregame_clean_ge_25pp": {"n": 2254, "with_external": 174, "coverage": 0.0772, "external_status": {"EXTERNAL_STALE": 121, "AGREES_WITH_KALSHI": 50, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 121, "MODEL_LONE_OUTLIER": 50, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2874, "share_external_supports_model": 0.0172}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 554.0, "median_sample_ratio": 2.38, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.2025, "data_status": {"POOR": 4058, "LIMITED": 2166, "ADEQUATE": 1384}, "comparison_lt_10pp": {"median_thinner_serve_points": 1769.0, "median_sample_ratio": 1.69, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 608, "model_minus_observed": 0.0487, "kalshi_minus_observed": -0.0826, "brier_diff_model_minus_kalshi": -0.0003}, "4-10x": {"n": 407, "model_minus_observed": 0.0744, "kalshi_minus_observed": -0.0645, "brier_diff_model_minus_kalshi": 0.0071}, "<2x": {"n": 1488, "model_minus_observed": 0.0813, "kalshi_minus_observed": -0.0408, "brier_diff_model_minus_kalshi": 0.0109}, ">=10x": {"n": 495, "model_minus_observed": 0.1259, "kalshi_minus_observed": -0.041, "brier_diff_model_minus_kalshi": 0.0161}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2998, "model": {"intercept": -0.539, "slope": 0.866, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.236, "slope": 1.119, "slope_se": 0.053}, "mean_extremity_model": 0.1761, "mean_extremity_kalshi": 0.1715, "model_brier": 0.229, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.0266, "brier_diff_se": 0.0035, "model_logloss": 0.6534, "kalshi_logloss": 0.5868}, "fair_v1": {"n": 2998, "model": {"intercept": -0.394, "slope": 1.056, "slope_se": 0.051}, "kalshi_mid_same_rows": {"intercept": 0.317, "slope": 1.165, "slope_se": 0.054}, "mean_extremity_model": 0.1686, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2114, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.009, "brier_diff_se": 0.0028, "model_logloss": 0.6101, "kalshi_logloss": 0.5867}, "gen1_elo": {"n": 2998, "model": {"intercept": -0.383, "slope": 1.038, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.31, "slope": 1.151, "slope_se": 0.053}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1718, "model_brier": 0.2105, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.0027, "model_logloss": 0.6089, "kalshi_logloss": 0.5863}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2438, "share_ge_15": 0.4367, "median_abs_gap": 12.96, "n": 19422}, "gen1_elo": {"share_ge_25": 0.238, "share_ge_15": 0.4301, "median_abs_gap": 12.47, "n": 19422}, "gen1_sr": {"share_ge_25": 0.3059, "share_ge_15": 0.5231, "median_abs_gap": 15.88, "n": 19422}, "gen2": {"share_ge_25": 0.3069, "share_ge_15": 0.5082, "median_abs_gap": 15.41, "n": 19422}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1502, "share_ge_15": 0.3491, "median_abs_gap": 10.64, "n": 15002}, "gen1_elo": {"share_ge_25": 0.1478, "share_ge_15": 0.3385, "median_abs_gap": 10.11, "n": 15001}, "gen1_sr": {"share_ge_25": 0.2128, "share_ge_15": 0.4452, "median_abs_gap": 13.29, "n": 15002}, "gen2": {"share_ge_25": 0.2262, "share_ge_15": 0.4406, "median_abs_gap": 13.0, "n": 15003}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.014, "share_ge_25_pregame_clean": 0.0137}, "WTA": {"median_abs_gap_pregame_clean": 7.82, "share_ge_25_all": 0.0627, "share_ge_25_pregame_clean": 0.0561}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2388, "share_within_10pp_all": 0.4393, "share_within_10pp_pregame_clean": 0.4968, "corr_model_vs_mid_pregame_clean": 0.8442}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 462, "model_brier": 0.194, "kalshi_brier": 0.1955, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 531, "model_brier": 0.2128, "kalshi_brier": 0.2046, "brier_diff_model_minus_kalshi": 0.0083}, "15-25": {"n_settled": 655, "model_brier": 0.2315, "kalshi_brier": 0.2168, "brier_diff_model_minus_kalshi": 0.0147}, "25-40": {"n_settled": 354, "model_brier": 0.2244, "kalshi_brier": 0.2093, "brier_diff_model_minus_kalshi": 0.0151}, "3-5": {"n_settled": 293, "model_brier": 0.1903, "kalshi_brier": 0.1907, "brier_diff_model_minus_kalshi": -0.0004}, "40+": {"n_settled": 72, "model_brier": 0.29, "kalshi_brier": 0.1741, "brier_diff_model_minus_kalshi": 0.116}, "5-10": {"n_settled": 631, "model_brier": 0.1954, "kalshi_brier": 0.1955, "brier_diff_model_minus_kalshi": -0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.539, "slope": 0.866, "slope_se": 0.047}, "kalshi_slope": {"intercept": 0.236, "slope": 1.119, "slope_se": 0.053}, "n": 2998}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.509, "slope": 0.868, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.147, "slope": 1.073, "slope_se": 0.039}, "n": 4991}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 317, "model_brier": 0.3313, "kalshi_brier": 0.2336, "brier_diff_model_minus_kalshi": 0.0977, "brier_diff_se": 0.0178, "corr_model_outcome": -0.0032, "corr_kalshi_outcome": 0.2527}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
