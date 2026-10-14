# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-14T17:49Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 32,755): 0-3 14.5%, 3-5 9.5%, 5-10 20.1%, 10-15 15.3%, 15-25 18.8%, 25-40 13.6%, 40+ 8.2%; median gap 11.81 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.4%, Challenger 12.4%, doubles 7.0%). Main tour: ATP 1.4% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 7,126): MARKET_ALREADY_SETTLED_WHEN_PRICED 37.6%, BOOK_QUALITY 17.8%, STALE_QUOTE 16.4%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 4.1%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 37.6%, execution 17.8%, market_freshness 16.4%, data 12.5%, market_freshness/coverage 8.8%, mapping 4.4%, model_calibration_or_unknown 2.0%, model_calibration 0.4%.
* **Stale / settled / in-play**: 53.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 46.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 7,126 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.4% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 572.0 points vs 1835.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.061, Gen-2 0.864, Gen-1 ledger 0.87 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 334 model 0.2264 vs Kalshi 0.2078; n 72 model 0.29 vs Kalshi 0.1741.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 129,744 model-market comparisons (215,045 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 46,814 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-14T17:39:30.238442+00:00'], shadow board 35,409 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-14T17:39:34.890004+00:00'], Model 4 14,072 rows, 14,333 settled tickers, 4,512 tickers with an external scan.
* By model: {"gen1_ledger": 30739, "gen1_elo": 17795, "fair_v1": 17795, "gen2": 17795, "gen1_sr": 17795, "model4_fundamental": 13917, "model4_conditioned": 13908}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 32,755 | 14.5 | 9.5 | 20.1 | 15.3 | 18.8 | 13.6 | 8.2 | 11.81 | 40.6% | 21.8% |
| MW fair_v1 | 17,795 | 13.6 | 8.5 | 18.6 | 15.9 | 19.1 | 14.5 | 9.8 | 12.88 | 43.3% | 24.2% |
| MW gen1_elo | 17,795 | 13.2 | 9.0 | 19.9 | 15.2 | 19.0 | 14.3 | 9.3 | 12.39 | 42.7% | 23.7% |
| MW gen1_ledger | 14,960 | 15.4 | 10.7 | 21.9 | 14.7 | 18.4 | 12.4 | 6.4 | 10.48 | 37.3% | 18.8% |
| MW gen1_sr | 17,795 | 9.9 | 7.7 | 16.4 | 14.2 | 21.8 | 18.2 | 11.7 | 15.62 | 51.8% | 30.0% |
| MW gen2 | 17,795 | 11.7 | 7.2 | 16.3 | 14.3 | 20.4 | 17.1 | 13.1 | 15.29 | 50.5% | 30.2% |
| all families model4_conditioned | 13,908 | 21.6 | 20.1 | 35.4 | 16.5 | 4.3 | 1.1 | 0.9 | 5.81 | 6.3% | 2.0% |
| all families model4_fundamental | 13,917 | 16.7 | 13.5 | 35.7 | 19.7 | 10.6 | 2.6 | 1.1 | 7.59 | 14.4% | 3.7% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 55.9%, >=15pp 40.6%, >=20pp 30.0%, >=25pp 21.8%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.44pp; >=10pp 45.2%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,322 | 30.3 | 14.7 | 25.0 | 17.6 | 10.4 | 1.1 | 0.8 | 5.75 | 12.3% | 2.0% |
| CHALLENGER | 3,086 | 15.5 | 9.9 | 20.1 | 15.8 | 14.9 | 12.1 | 11.7 | 11.62 | 38.7% | 23.8% |
| ITF_MEN | 5,006 | 11.2 | 8.3 | 17.9 | 14.9 | 19.5 | 15.8 | 12.3 | 14.04 | 47.6% | 28.1% |
| ITF_WOMEN | 6,891 | 10.4 | 6.5 | 16.1 | 16.0 | 22.1 | 18.3 | 10.5 | 15.41 | 51.0% | 28.8% |
| WTA | 916 | 21.7 | 10.8 | 24.8 | 15.7 | 20.1 | 5.7 | 1.2 | 8.11 | 27.0% | 6.9% |
| WTA125 | 574 | 12.7 | 7.7 | 22.6 | 21.2 | 19.9 | 13.9 | 1.9 | 11.31 | 35.7% | 15.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,322 | 24.4 | 14.4 | 24.7 | 19.0 | 14.5 | 1.9 | 1.0 | 6.73 | 17.4% | 2.9% |
| CHALLENGER | 3,086 | 15.0 | 7.6 | 19.4 | 13.5 | 18.2 | 14.1 | 12.3 | 12.75 | 44.6% | 26.4% |
| ITF_MEN | 5,006 | 9.8 | 7.0 | 16.0 | 14.2 | 20.0 | 18.3 | 14.6 | 16.13 | 53.0% | 33.0% |
| ITF_WOMEN | 6,891 | 8.8 | 5.8 | 13.1 | 13.2 | 22.0 | 20.6 | 16.4 | 18.71 | 59.0% | 37.1% |
| WTA | 916 | 18.0 | 8.0 | 18.9 | 16.3 | 22.8 | 14.8 | 1.2 | 12.08 | 38.9% | 16.1% |
| WTA125 | 574 | 6.1 | 4.2 | 17.6 | 17.6 | 25.8 | 19.2 | 9.6 | 17.24 | 54.5% | 28.7% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,322 | 27.6 | 14.5 | 28.7 | 15.4 | 10.3 | 2.5 | 0.9 | 6.03 | 13.7% | 3.4% |
| CHALLENGER | 3,086 | 14.8 | 10.2 | 20.4 | 15.2 | 15.7 | 11.8 | 11.9 | 11.19 | 39.4% | 23.7% |
| ITF_MEN | 5,006 | 10.2 | 8.3 | 18.7 | 14.0 | 20.1 | 16.2 | 12.5 | 14.47 | 48.8% | 28.7% |
| ITF_WOMEN | 6,891 | 10.0 | 6.9 | 16.4 | 15.8 | 22.8 | 18.7 | 9.4 | 15.43 | 50.9% | 28.1% |
| WTA | 916 | 22.3 | 15.6 | 32.8 | 15.9 | 10.5 | 2.2 | 0.8 | 6.15 | 13.4% | 2.9% |
| WTA125 | 574 | 22.5 | 12.2 | 29.3 | 15.2 | 14.3 | 6.3 | 0.3 | 7.54 | 20.9% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 719 | 30.9 | 22.8 | 35.7 | 8.9 | 1.2 | 0.4 | 0.0 | 4.7 | 1.7% | 0.4% |
| CHALLENGER | 2,108 | 22.0 | 15.3 | 27.6 | 15.0 | 13.1 | 5.0 | 2.0 | 7.01 | 20.1% | 7.0% |
| DOUBLES | 991 | 5.2 | 3.6 | 11.5 | 10.7 | 18.5 | 24.3 | 26.1 | 25.37 | 68.9% | 50.4% |
| ITF_MEN | 4,598 | 14.7 | 8.5 | 20.8 | 15.4 | 20.8 | 12.5 | 7.4 | 11.87 | 40.6% | 19.9% |
| ITF_WOMEN | 5,066 | 11.7 | 9.3 | 19.6 | 14.7 | 22.4 | 16.7 | 5.7 | 13.04 | 44.7% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 653 | 21.3 | 15.3 | 27.3 | 17.1 | 13.6 | 4.9 | 0.5 | 7.52 | 19.0% | 5.4% |
| WTA125 | 676 | 20.6 | 13.6 | 22.6 | 18.5 | 14.3 | 8.1 | 2.2 | 8.25 | 24.7% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,308 | 30.3 | 14.6 | 25.2 | 17.7 | 10.3 | 1.1 | 0.8 | 5.82 | 12.2% | 1.9% |
| CHALLENGER | 2,206 | 20.0 | 12.4 | 25.3 | 18.4 | 15.4 | 5.9 | 2.5 | 8.36 | 23.8% | 8.4% |
| ITF_MEN | 3,602 | 13.9 | 10.3 | 21.4 | 16.7 | 19.8 | 12.5 | 5.5 | 11.18 | 37.7% | 18.0% |
| ITF_WOMEN | 5,039 | 12.6 | 8.1 | 18.5 | 18.4 | 23.6 | 14.9 | 3.9 | 12.8 | 42.4% | 18.8% |
| WTA | 900 | 21.9 | 10.1 | 25.2 | 15.9 | 20.1 | 5.6 | 1.2 | 8.16 | 26.9% | 6.8% |
| WTA125 | 551 | 13.1 | 7.4 | 22.1 | 21.6 | 20.5 | 13.8 | 1.4 | 11.33 | 35.8% | 15.2% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,308 | 24.3 | 14.5 | 24.9 | 19.0 | 14.5 | 1.8 | 1.0 | 6.76 | 17.3% | 2.8% |
| CHALLENGER | 2,206 | 19.2 | 9.7 | 24.1 | 16.3 | 18.5 | 9.7 | 2.5 | 9.16 | 30.8% | 12.2% |
| ITF_MEN | 3,603 | 11.7 | 8.4 | 18.4 | 16.1 | 22.1 | 15.6 | 7.7 | 13.5 | 45.4% | 23.3% |
| ITF_WOMEN | 5,039 | 10.2 | 6.8 | 14.8 | 14.4 | 24.3 | 19.4 | 10.0 | 16.3 | 53.8% | 29.4% |
| WTA | 900 | 17.9 | 7.8 | 18.9 | 16.6 | 22.8 | 14.9 | 1.2 | 12.08 | 38.9% | 16.1% |
| WTA125 | 551 | 6.0 | 4.4 | 17.6 | 18.0 | 25.6 | 19.8 | 8.7 | 17.19 | 54.1% | 28.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 699 | 30.9 | 23.0 | 36.0 | 9.0 | 0.6 | 0.4 | 0.0 | 4.69 | 1.0% | 0.4% |
| CHALLENGER | 1,816 | 23.8 | 16.7 | 29.7 | 14.8 | 12.2 | 2.3 | 0.6 | 6.37 | 15.0% | 2.8% |
| DOUBLES | 916 | 5.3 | 3.7 | 11.8 | 10.7 | 18.7 | 24.1 | 25.7 | 24.68 | 68.5% | 49.8% |
| ITF_MEN | 3,779 | 16.2 | 9.3 | 22.7 | 16.3 | 20.6 | 10.4 | 4.4 | 10.54 | 35.5% | 14.8% |
| ITF_WOMEN | 4,146 | 12.8 | 10.0 | 21.4 | 15.5 | 22.6 | 15.0 | 2.6 | 11.59 | 40.2% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 619 | 21.8 | 16.0 | 27.5 | 17.1 | 13.9 | 3.7 | 0.0 | 7.21 | 17.6% | 3.7% |
| WTA125 | 572 | 22.6 | 15.0 | 24.1 | 20.1 | 12.8 | 5.1 | 0.3 | 7.33 | 18.2% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 991 | 5.2 | 3.6 | 11.5 | 10.7 | 18.5 | 24.3 | 26.1 | 25.37 | 68.9% | 50.4% |
| singles | 13,969 | 16.2 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.99 | 35.0% | 16.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,155 | 13.4 | 8.9 | 19.7 | 16.0 | 17.9 | 14.3 | 9.9 | 12.61 | 42.1% | 24.2% |
| Grass | 168 | 10.7 | 13.1 | 15.5 | 15.5 | 21.4 | 17.9 | 6.0 | 13.9 | 45.2% | 23.8% |
| Hard | 11,660 | 14.0 | 8.5 | 18.6 | 15.5 | 19.4 | 14.2 | 9.7 | 12.81 | 43.4% | 23.9% |
| UNKNOWN | 1,812 | 12.0 | 7.5 | 16.7 | 18.3 | 19.3 | 15.9 | 10.3 | 13.5 | 45.6% | 26.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,314 | 19.8 | 10.7 | 21.0 | 16.9 | 15.8 | 8.8 | 7.1 | 9.52 | 31.6% | 15.9% |
| B | 2,334 | 14.5 | 9.0 | 20.0 | 16.7 | 18.1 | 12.1 | 9.6 | 11.54 | 39.9% | 21.7% |
| C | 2,560 | 13.1 | 9.4 | 19.8 | 14.8 | 19.1 | 14.4 | 9.3 | 12.58 | 42.8% | 23.7% |
| D | 3,119 | 11.2 | 8.1 | 17.9 | 16.0 | 22.1 | 15.2 | 9.5 | 13.8 | 46.8% | 24.7% |
| F | 4,468 | 8.0 | 5.3 | 14.9 | 15.0 | 21.3 | 22.0 | 13.5 | 18.01 | 56.8% | 35.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,332 | 22.7 | 15.8 | 28.9 | 15.2 | 11.4 | 4.4 | 1.7 | 6.71 | 17.4% | 6.1% |
| B | 2,260 | 14.9 | 10.0 | 24.1 | 16.4 | 19.5 | 11.0 | 4.2 | 10.2 | 34.7% | 15.2% |
| C | 2,949 | 12.2 | 7.7 | 18.4 | 14.2 | 20.2 | 15.7 | 11.7 | 13.68 | 47.6% | 27.4% |
| D | 2,264 | 14.0 | 9.8 | 20.7 | 13.7 | 21.3 | 13.9 | 6.5 | 11.86 | 41.7% | 20.4% |
| F | 3,155 | 10.1 | 7.5 | 15.1 | 13.9 | 23.8 | 20.4 | 9.3 | 16.45 | 53.4% | 29.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,916 | 18.2 | 9.7 | 20.2 | 16.6 | 16.1 | 9.8 | 9.2 | 10.5 | 35.2% | 19.1% |
| LIMITED | 4,212 | 15.2 | 10.3 | 20.9 | 15.8 | 18.5 | 12.5 | 6.8 | 11.07 | 37.9% | 19.4% |
| POOR | 7,667 | 9.3 | 6.6 | 16.1 | 15.4 | 21.7 | 19.1 | 11.8 | 15.97 | 52.5% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,006 | 31.3 | 24.4 | 36.4 | 5.4 | 1.8 | 0.7 | 0.1 | 4.49 | 2.5% | 0.7% |
| GAME_SPREAD | 2,867 | 25.8 | 15.9 | 36.8 | 16.8 | 4.2 | 0.4 | 0.2 | 5.99 | 4.7% | 0.6% |
| MATCH_WINNER | 14,960 | 15.4 | 10.7 | 21.9 | 14.7 | 18.4 | 12.4 | 6.4 | 10.48 | 37.3% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,489 | 33.3 | 19.6 | 31.0 | 9.6 | 5.1 | 1.1 | 0.2 | 4.73 | 6.5% | 1.4% |
| TOTAL_GAMES | 4,393 | 6.7 | 9.1 | 39.1 | 29.6 | 10.4 | 2.7 | 2.3 | 9.46 | 15.5% | 5.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,881 | 25.6 | 38.1 | 31.6 | 0.3 | 3.9 | 0.4 | 0.1 | 4.3 | 4.5% | 0.5% |
| GAME_SPREAD | 3,481 | 45.2 | 16.4 | 28.9 | 7.3 | 1.1 | 0.7 | 0.4 | 3.57 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,546 | 3.4 | 6.5 | 42.9 | 36.7 | 6.7 | 1.9 | 1.9 | 9.77 | 10.6% | 3.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,881 | 26.3 | 18.8 | 37.1 | 9.2 | 6.3 | 2.1 | 0.3 | 5.48 | 8.7% | 2.4% |
| GAME_SPREAD | 3,481 | 19.3 | 13.4 | 30.3 | 21.0 | 12.9 | 2.3 | 0.7 | 7.77 | 15.9% | 3.0% |
| TOTAL_GAMES | 5,555 | 6.6 | 8.9 | 37.9 | 28.2 | 13.0 | 3.2 | 2.1 | 9.66 | 18.4% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 17,795 | 43.3% | 24.2% | 12.88 | 34.0% | 14.3% | 10.46 |
| gen1_elo | 17,795 | 42.7% | 23.7% | 12.39 | 32.9% | 14.1% | 9.97 |
| gen1_sr | 17,795 | 51.8% | 30.0% | 15.62 | 43.4% | 20.1% | 12.93 |
| gen2 | 17,795 | 50.5% | 30.2% | 15.29 | 43.4% | 21.6% | 12.82 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 9,679 | 16.5 | 10.5 | 21.6 | 17.4 | 19.6 | 11.2 | 3.3 | 10.42 | 34.2% | 14.5% |
| STALE | 8,116 | 10.3 | 6.2 | 15.1 | 14.2 | 18.4 | 18.4 | 17.4 | 17.19 | 54.2% | 35.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 8,428 | 17.3 | 11.5 | 23.7 | 14.6 | 16.9 | 11.1 | 4.9 | 9.4 | 32.9% | 16.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 32,755 | 8428 | 13151 | 11176 | 24.1 | 143.3 | 1400.4 |
| ge_15pp | 13,281 | 2775 | 4594 | 5912 | 26.2 | 440.2 | 1380.4 |
| ge_25pp | 7,126 | 1353 | 1997 | 3776 | 33.5 | 574.5 | 1380.4 |
| lt_10pp | 14,446 | 4422 | 6324 | 3700 | 22.4 | 47.8 | 1341.5 |

Current slate `SL-20261014T174931Z-6869c50a`: 389 priced rows, quote age at build {'median': 10.3, 'max': 10.4}, freshness {'AGING': 389}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 9 | 0.0 | 0.0 | 33.3 | 0.0 | 44.4 | 22.2 | 0.0 | 20.47 | 66.7% | 22.2% |
| EXTERNAL_LONE_OUTLIER | 11 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,422 | 21.0 | 10.7 | 22.7 | 18.6 | 19.5 | 6.8 | 0.6 | 8.95 | 26.9% | 7.4% |
| KALSHI_LONE_OUTLIER | 7 | 14.3 | 0.0 | 57.1 | 0.0 | 14.3 | 14.3 | 0.0 | 5.14 | 28.6% | 14.3% |
| MARKETS_AGREE | 249 | 71.9 | 28.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.04 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 463 | 0.0 | 3.7 | 34.6 | 30.2 | 22.9 | 8.0 | 0.7 | 11.65 | 31.5% | 8.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 17,795 | 2161 (12.1%) | 21.4% | 0.7% | {"EXTERNAL_STALE": 1422, "AGREES_WITH_KALSHI": 463, "ALL_AGREE": 249, "EXTERNAL_OUTLIER": 11, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 7, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 7,707 | 537 (7.0%) | 27.2% | 1.5% | {"EXTERNAL_STALE": 383, "AGREES_WITH_KALSHI": 146, "SUPPORTS_MODEL_DIRECTION": 6, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 4,311 | 149 (3.5%) | 26.9% | 2.0% | {"EXTERNAL_STALE": 106, "AGREES_WITH_KALSHI": 40, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 1,948 | 141 (7.2%) | 27.0% | 2.1% | {"EXTERNAL_STALE": 100, "AGREES_WITH_KALSHI": 38, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 7,255 | 1219 (16.8%) | 14.5% | 0.6% | {"EXTERNAL_STALE": 774, "ALL_AGREE": 249, "AGREES_WITH_KALSHI": 177, "EXTERNAL_OUTLIER": 11, "AGREES_WITH_MODEL": 5, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,500 | 11.6 | 8.0 | 20.0 | 14.8 | 21.5 | 14.3 | 9.8 | 13.34 | 45.6% | 24.1% |
| 4-10x | 2,349 | 12.0 | 8.8 | 19.3 | 15.6 | 19.9 | 15.4 | 9.0 | 13.02 | 44.3% | 24.4% |
| <2x | 9,356 | 15.6 | 9.2 | 18.8 | 16.9 | 17.6 | 12.8 | 9.1 | 11.86 | 39.5% | 21.9% |
| >=10x | 2,590 | 10.8 | 6.5 | 15.4 | 14.2 | 20.5 | 19.8 | 12.7 | 16.29 | 53.0% | 32.5% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,645 | 13.9 | 8.2 | 19.4 | 16.0 | 19.4 | 12.7 | 10.3 | 12.58 | 42.4% | 23.0% |
| 300-1000 | 4,082 | 12.0 | 8.6 | 17.6 | 16.1 | 21.1 | 15.6 | 8.9 | 13.52 | 45.7% | 24.5% |
| <300 | 5,075 | 8.8 | 6.1 | 15.6 | 14.8 | 21.2 | 20.6 | 12.9 | 16.98 | 54.7% | 33.6% |
| >=3000 | 3,993 | 21.2 | 11.8 | 22.6 | 17.1 | 13.9 | 7.5 | 5.9 | 8.49 | 27.4% | 13.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 581 | 0.5368 | 0.4044 | 0.4854 | +0.051 | -0.081 | 0.0001 ± 0.0061 |
| ratio 4-10x | 390 | 0.5877 | 0.448 | 0.5179 | +0.070 | -0.070 | 0.0054 ± 0.008 |
| ratio <2x | 1407 | 0.5378 | 0.4159 | 0.4591 | +0.079 | -0.043 | 0.0106 ± 0.0038 |
| ratio >=10x | 459 | 0.5469 | 0.3786 | 0.4292 | +0.118 | -0.051 | 0.0147 ± 0.0083 |
| thinner_sample 1000-3000 | 788 | 0.5438 | 0.4194 | 0.4772 | +0.067 | -0.058 | 0.004 ± 0.0051 |
| thinner_sample 300-1000 | 697 | 0.5607 | 0.4226 | 0.4849 | +0.076 | -0.062 | 0.0031 ± 0.0058 |
| thinner_sample <300 | 863 | 0.5446 | 0.383 | 0.4484 | +0.096 | -0.065 | 0.0134 ± 0.0059 |
| thinner_sample >=3000 | 489 | 0.5306 | 0.4357 | 0.4622 | +0.068 | -0.026 | 0.0141 ± 0.0053 |
| data_status ADEQUATE | 810 | 0.5338 | 0.4299 | 0.463 | +0.071 | -0.033 | 0.008 ± 0.0044 |
| data_status LIMITED | 730 | 0.5526 | 0.4239 | 0.489 | +0.064 | -0.065 | 0.0032 ± 0.0054 |
| data_status POOR | 1297 | 0.5497 | 0.394 | 0.4588 | +0.091 | -0.065 | 0.0115 ± 0.0047 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 433 | 0.1935 | 0.1948 | -0.0013 ± 0.0007 | 0.5654 | 0.5682 | 0.4919 | 0.4769 | 0.5242 | -0.047 ± 0.0222 | -0.01 (3) |
| 3-5 | 281 | 0.1911 | 0.1919 | -0.0008 ± 0.0021 | 0.5623 | 0.5628 | 0.5114 | 0.4716 | 0.4982 | -0.065 ± 0.0266 | 0.02 (1) |
| 5-10 | 597 | 0.1956 | 0.197 | -0.0014 ± 0.0027 | 0.5763 | 0.5776 | 0.5118 | 0.4373 | 0.4757 | -0.077 ± 0.0189 | -0.0125 (4) |
| 10-15 | 501 | 0.2097 | 0.2029 | +0.0068 ± 0.005 | 0.6064 | 0.5865 | 0.5217 | 0.3981 | 0.4311 | -0.081 ± 0.02 | -0.0633 (3) |
| 15-25 | 619 | 0.229 | 0.2169 | +0.0121 ± 0.0073 | 0.653 | 0.6203 | 0.5756 | 0.3806 | 0.4491 | -0.072 ± 0.0186 | -0.0133 (6) |
| 25-40 | 334 | 0.2264 | 0.2078 | +0.0185 ± 0.0149 | 0.6442 | 0.597 | 0.6444 | 0.3357 | 0.4611 | -0.066 ± 0.0228 | -0.01 (1) |
| 40+ | 72 | 0.29 | 0.1741 | +0.1160 ± 0.0438 | 0.7878 | 0.5206 | 0.7443 | 0.2967 | 0.3889 | -0.113 ± 0.0433 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2024 | 0.1777 | 0.1788 | -0.0011 ± 0.0003 | 0.5298 | 0.5311 | 0.4809 | 0.4659 | 0.5025 | -0.020 ± 0.0095 | -0.0188 (8) |
| 3-5 | 1267 | 0.1949 | 0.1933 | +0.0016 ± 0.001 | 0.5709 | 0.563 | 0.4825 | 0.4429 | 0.4396 | -0.062 ± 0.0126 | 0.02 (1) |
| 5-10 | 2790 | 0.1926 | 0.1914 | +0.0013 ± 0.0012 | 0.5677 | 0.5618 | 0.487 | 0.413 | 0.438 | -0.041 ± 0.0084 | -0.0082 (17) |
| 10-15 | 2412 | 0.2001 | 0.1821 | +0.0180 ± 0.0022 | 0.5858 | 0.5355 | 0.4797 | 0.3554 | 0.3454 | -0.074 ± 0.0087 | -0.0475 (4) |
| 15-25 | 2892 | 0.2068 | 0.1718 | +0.0350 ± 0.003 | 0.6058 | 0.507 | 0.5002 | 0.3042 | 0.315 | -0.062 ± 0.0077 | -0.0048 (29) |
| 25-40 | 2294 | 0.2198 | 0.1258 | +0.0940 ± 0.0046 | 0.633 | 0.3875 | 0.5274 | 0.2141 | 0.2249 | -0.060 ± 0.0072 | -0.01 (1) |
| 40+ | 1558 | 0.3727 | 0.0439 | +0.3288 ± 0.0059 | 0.9711 | 0.173 | 0.6249 | 0.1061 | 0.0591 | -0.084 ± 0.005 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 329 | 0.1953 | 0.1957 | -0.0003 ± 0.0009 | 0.5716 | 0.5725 | 0.5014 | 0.4863 | 0.5015 | -0.086 ± 0.0257 | -0.01 (1) |
| 3-5 | 225 | 0.2106 | 0.2104 | +0.0002 ± 0.0025 | 0.6034 | 0.6043 | 0.5199 | 0.4798 | 0.4933 | -0.071 ± 0.0322 | 0.02 (1) |
| 5-10 | 516 | 0.1987 | 0.1988 | -0.0001 ± 0.003 | 0.5806 | 0.5811 | 0.5549 | 0.4799 | 0.5194 | -0.065 ± 0.0204 | -0.01 (4) |
| 10-15 | 465 | 0.2148 | 0.2066 | +0.0082 ± 0.0053 | 0.6163 | 0.5986 | 0.573 | 0.4486 | 0.4817 | -0.091 ± 0.0219 | -0.05 (4) |
| 15-25 | 685 | 0.2263 | 0.2087 | +0.0176 ± 0.0069 | 0.6438 | 0.6001 | 0.5886 | 0.3914 | 0.4496 | -0.082 ± 0.0177 | -0.01 (5) |
| 25-40 | 444 | 0.2676 | 0.1981 | +0.0695 ± 0.0133 | 0.7489 | 0.5757 | 0.6642 | 0.3501 | 0.3986 | -0.119 ± 0.021 | -0.025 (2) |
| 40+ | 173 | 0.3522 | 0.1852 | +0.1670 ± 0.0318 | 0.9781 | 0.5437 | 0.7415 | 0.2609 | 0.341 | -0.057 ± 0.0316 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1727 | 0.1814 | 0.1819 | -0.0004 ± 0.0003 | 0.5378 | 0.5387 | 0.4972 | 0.4825 | 0.5072 | -0.031 ± 0.0106 | -0.0217 (6) |
| 3-5 | 1114 | 0.1938 | 0.1934 | +0.0004 ± 0.0011 | 0.5629 | 0.562 | 0.5175 | 0.4775 | 0.4919 | -0.036 ± 0.0134 | 0.02 (1) |
| 5-10 | 2441 | 0.1912 | 0.1896 | +0.0016 ± 0.0013 | 0.5652 | 0.558 | 0.5164 | 0.4427 | 0.4707 | -0.035 ± 0.009 | -0.01 (5) |
| 10-15 | 2123 | 0.1964 | 0.1826 | +0.0138 ± 0.0023 | 0.5783 | 0.5353 | 0.5223 | 0.3979 | 0.4074 | -0.060 ± 0.0094 | -0.02 (14) |
| 15-25 | 3072 | 0.2152 | 0.1763 | +0.0389 ± 0.003 | 0.6262 | 0.5203 | 0.5334 | 0.3371 | 0.3395 | -0.073 ± 0.0077 | -0.0026 (27) |
| 25-40 | 2665 | 0.2483 | 0.1379 | +0.1104 ± 0.0046 | 0.7047 | 0.4199 | 0.5617 | 0.2456 | 0.2311 | -0.084 ± 0.0072 | -0.015 (6) |
| 40+ | 2095 | 0.3996 | 0.0688 | +0.3308 ± 0.0066 | 1.0487 | 0.2386 | 0.6649 | 0.1278 | 0.1021 | -0.066 ± 0.0056 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 425 | 0.195 | 0.1978 | -0.0028 ± 0.0008 | 0.5703 | 0.5773 | 0.4939 | 0.4787 | 0.5576 | +0.001 ± 0.0218 | -0.0133 (6) |
| 3-5 | 303 | 0.1838 | 0.1821 | +0.0017 ± 0.002 | 0.5426 | 0.5384 | 0.4916 | 0.4522 | 0.4521 | -0.112 ± 0.0258 | -0.01 (1) |
| 5-10 | 632 | 0.2 | 0.1976 | +0.0024 ± 0.0027 | 0.5872 | 0.5779 | 0.5044 | 0.4307 | 0.4478 | -0.088 ± 0.0182 | -0.01 (4) |
| 10-15 | 487 | 0.207 | 0.2091 | -0.0021 ± 0.0051 | 0.601 | 0.6011 | 0.539 | 0.4162 | 0.4887 | -0.053 ± 0.0205 | -0.044 (5) |
| 15-25 | 576 | 0.2339 | 0.2118 | +0.0222 ± 0.0075 | 0.6674 | 0.6082 | 0.5825 | 0.3892 | 0.4288 | -0.101 ± 0.019 | -0.03 (1) |
| 25-40 | 349 | 0.2126 | 0.213 | -0.0004 ± 0.0145 | 0.6137 | 0.6092 | 0.6499 | 0.3392 | 0.4928 | -0.042 ± 0.022 | 0.0 (1) |
| 40+ | 65 | 0.3165 | 0.1747 | +0.1418 ± 0.0472 | 0.8502 | 0.5223 | 0.7504 | 0.2955 | 0.3692 | -0.124 ± 0.0479 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1920 | 0.1865 | 0.1879 | -0.0013 ± 0.0003 | 0.5498 | 0.5525 | 0.4867 | 0.4714 | 0.5099 | -0.015 ± 0.0099 | -0.0183 (23) |
| 3-5 | 1337 | 0.1847 | 0.1825 | +0.0022 ± 0.0009 | 0.5458 | 0.5405 | 0.4764 | 0.437 | 0.4293 | -0.071 ± 0.0121 | -0.0243 (7) |
| 5-10 | 2976 | 0.1934 | 0.188 | +0.0054 ± 0.0012 | 0.571 | 0.5526 | 0.4811 | 0.4073 | 0.4056 | -0.063 ± 0.008 | -0.01 (18) |
| 10-15 | 2279 | 0.1949 | 0.1811 | +0.0138 ± 0.0022 | 0.5741 | 0.5315 | 0.4966 | 0.3735 | 0.3791 | -0.062 ± 0.0089 | -0.03 (9) |
| 15-25 | 2973 | 0.2088 | 0.171 | +0.0378 ± 0.003 | 0.6122 | 0.5061 | 0.5039 | 0.3085 | 0.3115 | -0.068 ± 0.0076 | -0.03 (2) |
| 25-40 | 2259 | 0.2139 | 0.1237 | +0.0902 ± 0.0047 | 0.6197 | 0.3809 | 0.5234 | 0.2074 | 0.2266 | -0.055 ± 0.007 | 0.0 (1) |
| 40+ | 1493 | 0.3864 | 0.0456 | +0.3408 ± 0.0062 | 1.0094 | 0.1777 | 0.6328 | 0.108 | 0.0569 | -0.087 ± 0.0052 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 744 | 0.1982 | 0.1988 | -0.0006 ± 0.0006 | 0.5776 | 0.5788 | 0.5058 | 0.4907 | 0.5081 | -0.037 ± 0.0163 | -0.0226 (46) |
| 3-5 | 535 | 0.1935 | 0.193 | +0.0005 ± 0.0015 | 0.5655 | 0.5624 | 0.4798 | 0.44 | 0.4505 | -0.046 ± 0.0191 | -0.0058 (33) |
| 5-10 | 1126 | 0.1943 | 0.189 | +0.0052 ± 0.002 | 0.574 | 0.5594 | 0.4848 | 0.4113 | 0.413 | -0.061 ± 0.0132 | -0.0049 (73) |
| 10-15 | 713 | 0.2065 | 0.1966 | +0.0100 ± 0.0041 | 0.6014 | 0.5749 | 0.5012 | 0.3783 | 0.3983 | -0.048 ± 0.0166 | 0.0014 (64) |
| 15-25 | 951 | 0.2313 | 0.2117 | +0.0196 ± 0.0058 | 0.6609 | 0.6094 | 0.5604 | 0.366 | 0.4132 | -0.048 ± 0.0149 | -0.0216 (58) |
| 25-40 | 545 | 0.2548 | 0.1948 | +0.0600 ± 0.0117 | 0.7171 | 0.5667 | 0.6428 | 0.3299 | 0.389 | -0.085 ± 0.0176 | -0.0216 (25) |
| 40+ | 191 | 0.3694 | 0.1915 | +0.1779 ± 0.0322 | 1.0695 | 0.5637 | 0.7934 | 0.3027 | 0.3874 | -0.077 ± 0.029 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2246 | 0.1892 | 0.1895 | -0.0003 ± 0.0003 | 0.554 | 0.5536 | 0.5036 | 0.4882 | 0.5031 | -0.030 ± 0.0091 | -0.0155 (82) |
| 3-5 | 1533 | 0.1878 | 0.1854 | +0.0024 ± 0.0009 | 0.5501 | 0.5441 | 0.4867 | 0.4471 | 0.4371 | -0.056 ± 0.0111 | -0.0148 (63) |
| 5-10 | 3169 | 0.1916 | 0.1843 | +0.0073 ± 0.0011 | 0.5672 | 0.5463 | 0.4788 | 0.4051 | 0.3957 | -0.062 ± 0.0077 | -0.0087 (125) |
| 10-15 | 2128 | 0.2025 | 0.1889 | +0.0136 ± 0.0023 | 0.5923 | 0.556 | 0.5082 | 0.3852 | 0.3914 | -0.052 ± 0.0094 | -0.0053 (105) |
| 15-25 | 2671 | 0.229 | 0.1982 | +0.0307 ± 0.0034 | 0.6612 | 0.5759 | 0.5535 | 0.3586 | 0.3785 | -0.058 ± 0.0087 | -0.0255 (106) |
| 25-40 | 1808 | 0.255 | 0.1684 | +0.0867 ± 0.0061 | 0.723 | 0.498 | 0.6056 | 0.2909 | 0.3131 | -0.077 ± 0.0094 | -0.0206 (47) |
| 40+ | 894 | 0.3859 | 0.1284 | +0.2574 ± 0.0128 | 1.095 | 0.3939 | 0.7096 | 0.2021 | 0.2148 | -0.073 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2837 | 1.061 ± 0.053 | 1.18 | 0.1688 | 0.1711 | 0.2106 | 0.2022 |
| gen2 | 2837 | 0.864 ± 0.048 | 1.126 | 0.1786 | 0.1711 | 0.2287 | 0.2021 |
| gen1_elo | 2837 | 1.038 ± 0.051 | 1.168 | 0.1733 | 0.1715 | 0.2098 | 0.2022 |
| gen1_sr | 2837 | 1.068 ± 0.062 | 1.2 | 0.1377 | 0.173 | 0.2248 | 0.2019 |
| gen1_ledger | 4805 | 0.87 ± 0.036 | 1.084 | 0.1765 | 0.1868 | 0.2178 | 0.1974 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 13,281)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,393 | 25.6% |
| STALE_QUOTE | market_freshness | 2,576 | 19.4% |
| BOOK_QUALITY | execution | 2,435 | 18.3% |
| POOR_DATA | data | 1,488 | 11.2% |
| LIMITED_DATA | data | 986 | 7.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 731 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 645 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 513 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 381 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 133 | 1.0% |

Cause class: coverage 25.6%, market_freshness 19.4%, data 18.6%, execution 18.3%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.9%, mapping 3.9%, model_calibration 1.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.3%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 68.7%, THIN_PLAYER_HISTORY 57.6%, STALE_PLAYER_DATA 54.9%, STALE_KALSHI_QUOTE 44.5%, MODEL_INTERNAL_DISAGREEMENT 38.8%, ASYMMETRIC_SAMPLE_SIZE 31.5%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 16.7%, PLAYER_IDENTITY_RISK 13.3%, LEVEL_TRANSFER_RISK 8.6%, EVENT_MAPPING_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.5%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 28.0%, POST_SETTLEMENT_OBSERVATION 25.6%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 7,126)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,680 | 37.6% |
| BOOK_QUALITY | execution | 1,265 | 17.8% |
| STALE_QUOTE | market_freshness | 1,171 | 16.4% |
| POOR_DATA | data | 602 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 395 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 316 | 4.4% |
| LIMITED_DATA | data | 291 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 236 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 141 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 29 | 0.4% |

Cause class: coverage 37.6%, execution 17.8%, market_freshness 16.4%, data 12.5%, market_freshness/coverage 8.8%, mapping 4.4%, model_calibration_or_unknown 2.0%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.1%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 72.5%, THIN_PLAYER_HISTORY 59.8%, STALE_KALSHI_QUOTE 53.0%, STALE_PLAYER_DATA 49.9%, MODEL_INTERNAL_DISAGREEMENT 39.8%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 17.4%, PLAYER_IDENTITY_RISK 17.1%, EVENT_MAPPING_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 7.6%, LEVEL_TRANSFER_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 4.5%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 40.4%, POST_SETTLEMENT_OBSERVATION 37.6%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5726, "IDENTITY_AMBIGUOUS": 1400}; ticker orientation: {"VERIFIED": 7126}.

Checks: discipline:AMBIGUOUS 500, discipline:PASS 6626, identity_confidence:AMBIGUOUS 1221, identity_confidence:PASS 5905, level_mapping:NA 512, level_mapping:PASS 6614, market_pair:AMBIGUOUS 251, market_pair:NA 172, market_pair:PASS 6703, model_complement:NA 139, model_complement:PASS 6987, namesake:PASS 7126, physical_match_id:NA 2815, physical_match_id:PASS 4311, player_ids:PASS 7126, same_pair_other_event:PASS 7126, ticker_orientation:PASS 7126

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,041 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.24 | 0.2103 / 0.2125 (251) | 16.3% | 0.5% | 5.4% | 1.7% |
| CHALLENGER | 5,194 | 17.0% | 5.9% | 12.4% | {"coverage": 539, "market_freshness": 109, "market_freshness/coverage": 107, "data": 58, "model_calibration_or_unknown": 45, "execution": 13, "mapping": 6, "model_calibration": 5} | 7.25 | 0.2176 / 0.2034 (1356) | 37.7% | 8.9% | 2.4% | 22.6% |
| DOUBLES | 991 | 50.4% | 49.8% | 7.0% | {"execution": 198, "mapping": 152, "market_freshness": 106, "market_freshness/coverage": 37, "coverage": 7} | 24.68 | 0.3362 / 0.2329 (288) | 23.6% | 0.0% | 100.0% | 7.6% |
| ITF_MEN | 9,604 | 24.2% | 16.4% | 32.6% | {"coverage": 917, "execution": 494, "market_freshness": 320, "data": 313, "market_freshness/coverage": 198, "mapping": 79, "model_calibration_or_unknown": 2} | 10.89 | 0.2118 / 0.1938 (2418) | 35.5% | 58.6% | 10.4% | 23.2% |
| ITF_WOMEN | 11,957 | 26.1% | 18.3% | 43.8% | {"coverage": 1200, "market_freshness": 543, "execution": 531, "data": 488, "market_freshness/coverage": 243, "mapping": 73, "model_calibration_or_unknown": 33, "model_calibration": 10} | 12.35 | 0.2024 / 0.1928 (2578) | 37.7% | 58.1% | 9.8% | 23.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,569 | 6.2% | 5.5% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 22, "data": 11, "market_freshness/coverage": 10, "model_calibration": 7, "execution": 7, "coverage": 4, "mapping": 1} | 7.81 | 0.2387 / 0.2306 (279) | 25.9% | 1.3% | 1.7% | 3.2% |
| WTA125 | 1,250 | 12.9% | 10.2% | 2.3% | {"model_calibration_or_unknown": 37, "market_freshness": 35, "market_freshness/coverage": 34, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 7, "mapping": 4} | 9.4 | 0.2156 / 0.2078 (430) | 22.8% | 8.2% | 4.2% | 10.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 5 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 6 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 8 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 9 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 10 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 11 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 12 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 13 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 14 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 15 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 16 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 17 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 18 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 20 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 21 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 23 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 24 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 25 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 26 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 28 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 29 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 30 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
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
| 44 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 760 min (STALE); no external reference |
| 45 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 46 | `KXITFWMATCH-26OCT13MAMSTR-MAM` | ITF_WOMEN | fair_v1 | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 406 min (STALE); data LIMITED (grade C, thinner serve sample 879.0, ratio 2.64); no external reference |
| 47 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 48 | `KXITFMATCH-26OCT13VISMUE-MUE` | ITF_MEN | fair_v1 | 25% / 98% | -74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 103 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 0.0); no external reference |
| 49 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 50 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9823, "by_level_share_of_ge_25pp": {"ATP": 0.0041, "CHALLENGER": 0.1238, "DOUBLES": 0.0702, "ITF_MEN": 0.326, "ITF_WOMEN": 0.438, "OTHER": 0.0017, "WTA": 0.0138, "WTA125": 0.0226}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5299, "share_primary_cause_market_settled_or_in_play": 0.4646, "share_primary_cause_stale_quote_only": 0.1643}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 7126, "identity_ambiguous_share": 0.1965, "ticker_orientation": {"VERIFIED": 7126}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 4311, "with_external": 149, "coverage": 0.0346, "external_status": {"EXTERNAL_STALE": 106, "AGREES_WITH_KALSHI": 40, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 106, "MODEL_LONE_OUTLIER": 40, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2685, "share_external_supports_model": 0.0201}, "pregame_clean_ge_25pp": {"n": 1948, "with_external": 141, "coverage": 0.0724, "external_status": {"EXTERNAL_STALE": 100, "AGREES_WITH_KALSHI": 38, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 100, "MODEL_LONE_OUTLIER": 38, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.2695, "share_external_supports_model": 0.0213}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 572.0, "median_sample_ratio": 2.37, "median_min_matches": 20.0, "median_max_days_since_last": 204.0, "share_severe_asymmetry": 0.197, "data_status": {"POOR": 3781, "LIMITED": 2050, "ADEQUATE": 1295}, "comparison_lt_10pp": {"median_thinner_serve_points": 1835.0, "median_sample_ratio": 1.68, "median_min_matches": 85.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 581, "model_minus_observed": 0.0514, "kalshi_minus_observed": -0.081, "brier_diff_model_minus_kalshi": 0.0001}, "4-10x": {"n": 390, "model_minus_observed": 0.0697, "kalshi_minus_observed": -0.07, "brier_diff_model_minus_kalshi": 0.0054}, "<2x": {"n": 1407, "model_minus_observed": 0.0786, "kalshi_minus_observed": -0.0432, "brier_diff_model_minus_kalshi": 0.0106}, ">=10x": {"n": 459, "model_minus_observed": 0.1177, "kalshi_minus_observed": -0.0506, "brier_diff_model_minus_kalshi": 0.0147}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2837, "model": {"intercept": -0.534, "slope": 0.864, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.244, "slope": 1.126, "slope_se": 0.054}, "mean_extremity_model": 0.1786, "mean_extremity_kalshi": 0.1711, "model_brier": 0.2287, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0266, "brier_diff_se": 0.0036, "model_logloss": 0.6531, "kalshi_logloss": 0.5863}, "fair_v1": {"n": 2837, "model": {"intercept": -0.38, "slope": 1.061, "slope_se": 0.053}, "kalshi_mid_same_rows": {"intercept": 0.341, "slope": 1.18, "slope_se": 0.055}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1711, "model_brier": 0.2106, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0084, "brier_diff_se": 0.0028, "model_logloss": 0.6087, "kalshi_logloss": 0.5864}, "gen1_elo": {"n": 2837, "model": {"intercept": -0.36, "slope": 1.038, "slope_se": 0.051}, "kalshi_mid_same_rows": {"intercept": 0.342, "slope": 1.168, "slope_se": 0.055}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1715, "model_brier": 0.2098, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0076, "brier_diff_se": 0.0028, "model_logloss": 0.6078, "kalshi_logloss": 0.5863}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2423, "share_ge_15": 0.4331, "median_abs_gap": 12.88, "n": 17795}, "gen1_elo": {"share_ge_25": 0.237, "share_ge_15": 0.4267, "median_abs_gap": 12.39, "n": 17795}, "gen1_sr": {"share_ge_25": 0.2997, "share_ge_15": 0.518, "median_abs_gap": 15.62, "n": 17795}, "gen2": {"share_ge_25": 0.3017, "share_ge_15": 0.5055, "median_abs_gap": 15.29, "n": 17795}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1432, "share_ge_15": 0.3395, "median_abs_gap": 10.46, "n": 13606}, "gen1_elo": {"share_ge_25": 0.1413, "share_ge_15": 0.3292, "median_abs_gap": 9.97, "n": 13605}, "gen1_sr": {"share_ge_25": 0.2005, "share_ge_15": 0.434, "median_abs_gap": 12.93, "n": 13606}, "gen2": {"share_ge_25": 0.2156, "share_ge_15": 0.4336, "median_abs_gap": 12.82, "n": 13607}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.24, "share_ge_25_all": 0.0142, "share_ge_25_pregame_clean": 0.014}, "WTA": {"median_abs_gap_pregame_clean": 7.81, "share_ge_25_all": 0.0625, "share_ge_25_pregame_clean": 0.0553}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2396, "share_within_10pp_all": 0.441, "share_within_10pp_pregame_clean": 0.5005, "corr_model_vs_mid_pregame_clean": 0.8482}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 433, "model_brier": 0.1935, "kalshi_brier": 0.1948, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 501, "model_brier": 0.2097, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": 0.0068}, "15-25": {"n_settled": 619, "model_brier": 0.229, "kalshi_brier": 0.2169, "brier_diff_model_minus_kalshi": 0.0121}, "25-40": {"n_settled": 334, "model_brier": 0.2264, "kalshi_brier": 0.2078, "brier_diff_model_minus_kalshi": 0.0185}, "3-5": {"n_settled": 281, "model_brier": 0.1911, "kalshi_brier": 0.1919, "brier_diff_model_minus_kalshi": -0.0008}, "40+": {"n_settled": 72, "model_brier": 0.29, "kalshi_brier": 0.1741, "brier_diff_model_minus_kalshi": 0.116}, "5-10": {"n_settled": 597, "model_brier": 0.1956, "kalshi_brier": 0.197, "brier_diff_model_minus_kalshi": -0.0014}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.534, "slope": 0.864, "slope_se": 0.048}, "kalshi_slope": {"intercept": 0.244, "slope": 1.126, "slope_se": 0.054}, "n": 2837}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.499, "slope": 0.87, "slope_se": 0.036}, "kalshi_slope": {"intercept": 0.166, "slope": 1.084, "slope_se": 0.04}, "n": 4805}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 288, "model_brier": 0.3362, "kalshi_brier": 0.2329, "brier_diff_model_minus_kalshi": 0.1033, "brier_diff_se": 0.0192, "corr_model_outcome": -0.0382, "corr_kalshi_outcome": 0.2642}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
