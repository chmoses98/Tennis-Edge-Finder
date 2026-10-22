# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-22T13:05Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 49,043): 0-3 14.0%, 3-5 9.4%, 5-10 19.7%, 10-15 15.3%, 15-25 19.4%, 25-40 14.1%, 40+ 8.1%; median gap 12.14 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.7%, Challenger 11.9%, doubles 6.8%). Main tour: ATP 4.9% and WTA 4.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 10,877): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.5%, STALE_QUOTE 18.4%, BOOK_QUALITY 18.4%, POOR_DATA 8.9%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.6%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.5%, market_freshness 18.4%, execution 18.4%, data 12.6%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%.
* **Stale / settled / in-play**: 52.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 10,877 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.6% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.0 points vs 1667.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.039, Gen-2 0.844, Gen-1 ledger 0.868 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 533 model 0.2249 vs Kalshi 0.2111; n 105 model 0.2842 vs Kalshi 0.1913.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 210,428 model-market comparisons (342,757 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 70,495 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-22T12:52:17.993587+00:00'], shadow board 56,140 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-22T12:52:22.322143+00:00'], Model 4 26,381 rows, 18,864 settled tickers, 6,656 tickers with an external scan.
* By model: {"gen1_ledger": 47665, "gen1_elo": 28231, "fair_v1": 28231, "gen2": 28231, "gen1_sr": 28231, "model4_fundamental": 24933, "model4_conditioned": 24906}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 49,043 | 14.0 | 9.4 | 19.7 | 15.3 | 19.4 | 14.1 | 8.1 | 12.14 | 41.6% | 22.2% |
| MW fair_v1 | 28,231 | 12.9 | 8.5 | 18.4 | 15.6 | 20.0 | 14.9 | 9.7 | 13.21 | 44.6% | 24.7% |
| MW gen1_elo | 28,231 | 12.9 | 8.5 | 18.9 | 15.2 | 20.0 | 15.0 | 9.5 | 13.01 | 44.5% | 24.4% |
| MW gen1_ledger | 20,812 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.8 | 5.9 | 10.59 | 37.5% | 18.8% |
| MW gen1_sr | 28,231 | 9.9 | 7.0 | 16.5 | 13.8 | 21.2 | 18.8 | 12.7 | 16.09 | 52.8% | 31.6% |
| MW gen2 | 28,231 | 10.9 | 7.2 | 16.2 | 14.2 | 19.7 | 17.9 | 13.9 | 15.65 | 51.5% | 31.8% |
| all families model4_conditioned | 24,906 | 21.7 | 19.1 | 34.6 | 17.7 | 4.4 | 1.4 | 1.0 | 5.97 | 6.9% | 2.5% |
| all families model4_fundamental | 24,933 | 16.6 | 13.2 | 34.0 | 20.5 | 10.9 | 3.5 | 1.3 | 7.83 | 15.7% | 4.8% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.9%, >=15pp 41.6%, >=20pp 30.9%, >=25pp 22.2%, >=30pp 16.0%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.51pp; >=10pp 45.5%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,420 | 28.9 | 14.0 | 24.5 | 14.7 | 12.2 | 5.0 | 0.7 | 6.17 | 17.9% | 5.8% |
| CHALLENGER | 4,463 | 15.9 | 9.9 | 20.5 | 15.7 | 14.8 | 12.4 | 10.9 | 11.06 | 38.0% | 23.3% |
| ITF_MEN | 7,747 | 10.4 | 7.5 | 16.9 | 14.7 | 21.6 | 17.1 | 11.8 | 15.18 | 50.5% | 28.9% |
| ITF_WOMEN | 11,277 | 9.4 | 6.9 | 15.8 | 15.4 | 22.7 | 18.2 | 11.6 | 15.8 | 52.5% | 29.8% |
| WTA | 1,664 | 17.1 | 13.0 | 25.5 | 19.9 | 19.3 | 4.6 | 0.7 | 8.43 | 24.5% | 5.2% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,420 | 23.6 | 14.9 | 25.1 | 16.9 | 13.5 | 5.0 | 1.0 | 6.58 | 19.4% | 5.9% |
| CHALLENGER | 4,463 | 14.9 | 8.6 | 18.6 | 14.8 | 17.4 | 13.9 | 11.8 | 12.5 | 43.1% | 25.7% |
| ITF_MEN | 7,747 | 8.5 | 6.0 | 14.4 | 13.1 | 19.8 | 20.6 | 17.5 | 18.45 | 57.9% | 38.1% |
| ITF_WOMEN | 11,277 | 8.0 | 5.6 | 13.7 | 13.5 | 20.9 | 21.1 | 17.2 | 18.94 | 59.2% | 38.2% |
| WTA | 1,664 | 14.4 | 9.9 | 21.2 | 16.4 | 23.6 | 13.7 | 0.7 | 11.18 | 38.0% | 14.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,420 | 24.5 | 12.7 | 24.0 | 15.9 | 14.8 | 6.9 | 1.2 | 7.3 | 22.9% | 8.1% |
| CHALLENGER | 4,463 | 14.4 | 9.3 | 20.8 | 15.3 | 16.3 | 12.8 | 11.2 | 11.42 | 40.2% | 23.9% |
| ITF_MEN | 7,747 | 9.9 | 7.5 | 17.0 | 14.1 | 22.1 | 17.4 | 12.0 | 15.51 | 51.5% | 29.4% |
| ITF_WOMEN | 11,277 | 9.6 | 6.6 | 16.2 | 15.6 | 23.0 | 18.3 | 10.7 | 15.67 | 52.0% | 29.0% |
| WTA | 1,664 | 24.3 | 16.8 | 29.8 | 16.2 | 10.2 | 2.3 | 0.4 | 6.02 | 12.9% | 2.8% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,387 | 25.5 | 19.5 | 30.8 | 11.8 | 8.9 | 3.0 | 0.4 | 5.53 | 12.3% | 3.4% |
| CHALLENGER | 3,080 | 21.5 | 14.8 | 26.6 | 14.0 | 14.7 | 6.6 | 1.9 | 7.27 | 23.2% | 8.4% |
| DOUBLES | 1,542 | 5.4 | 4.2 | 11.5 | 10.2 | 21.0 | 26.4 | 21.4 | 24.04 | 68.8% | 47.8% |
| ITF_MEN | 5,917 | 13.8 | 8.9 | 20.1 | 16.0 | 21.3 | 13.3 | 6.6 | 12.16 | 41.2% | 19.9% |
| ITF_WOMEN | 6,977 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.86 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,028 | 22.3 | 15.9 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,355 | 29.3 | 14.2 | 24.9 | 14.6 | 11.9 | 4.6 | 0.5 | 5.98 | 17.0% | 5.1% |
| CHALLENGER | 3,162 | 20.7 | 12.3 | 25.2 | 18.1 | 15.2 | 6.6 | 2.0 | 8.34 | 23.8% | 8.6% |
| ITF_MEN | 5,718 | 12.6 | 8.9 | 20.2 | 16.6 | 22.6 | 14.0 | 5.1 | 12.45 | 41.7% | 19.1% |
| ITF_WOMEN | 8,437 | 11.2 | 8.2 | 18.0 | 17.5 | 24.6 | 15.4 | 5.1 | 13.54 | 45.1% | 20.5% |
| WTA | 1,615 | 17.3 | 12.8 | 25.5 | 20.2 | 19.3 | 4.3 | 0.7 | 8.39 | 24.2% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,355 | 24.0 | 15.2 | 25.3 | 16.8 | 13.5 | 4.6 | 0.6 | 6.48 | 18.7% | 5.3% |
| CHALLENGER | 3,162 | 18.8 | 11.0 | 23.1 | 17.7 | 17.6 | 9.6 | 2.3 | 9.2 | 29.4% | 11.9% |
| ITF_MEN | 5,719 | 10.1 | 7.2 | 16.7 | 14.9 | 21.5 | 19.1 | 10.5 | 15.46 | 51.1% | 29.6% |
| ITF_WOMEN | 8,438 | 9.0 | 6.4 | 15.2 | 15.0 | 23.0 | 20.6 | 10.8 | 16.62 | 54.4% | 31.4% |
| WTA | 1,615 | 14.5 | 9.9 | 21.2 | 16.4 | 23.6 | 13.6 | 0.7 | 11.18 | 38.0% | 14.4% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,345 | 25.7 | 19.8 | 30.9 | 12.0 | 8.5 | 2.9 | 0.2 | 5.42 | 11.6% | 3.1% |
| CHALLENGER | 2,684 | 22.9 | 15.9 | 28.1 | 13.9 | 14.1 | 4.4 | 0.6 | 6.68 | 19.1% | 5.0% |
| DOUBLES | 1,434 | 5.4 | 4.3 | 11.7 | 10.4 | 20.9 | 26.4 | 20.9 | 23.86 | 68.2% | 47.3% |
| ITF_MEN | 4,953 | 15.0 | 9.5 | 21.8 | 16.8 | 21.2 | 11.7 | 4.1 | 11.16 | 36.9% | 15.8% |
| ITF_WOMEN | 5,793 | 13.6 | 9.6 | 20.7 | 15.9 | 21.8 | 15.1 | 3.4 | 11.69 | 40.2% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 978 | 22.8 | 16.5 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,542 | 5.4 | 4.2 | 11.5 | 10.2 | 21.0 | 26.4 | 21.4 | 24.04 | 68.8% | 47.8% |
| singles | 19,270 | 16.2 | 11.2 | 22.3 | 15.2 | 18.5 | 11.8 | 4.7 | 10.04 | 35.0% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,308 | 13.2 | 8.8 | 19.0 | 15.6 | 18.9 | 14.9 | 9.6 | 12.89 | 43.3% | 24.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 17,561 | 13.3 | 8.5 | 18.4 | 15.3 | 20.1 | 14.7 | 9.7 | 13.17 | 44.5% | 24.4% |
| UNKNOWN | 4,125 | 10.9 | 7.8 | 17.2 | 17.0 | 20.9 | 15.9 | 10.4 | 13.94 | 47.1% | 26.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,848 | 19.7 | 11.7 | 21.3 | 16.5 | 15.7 | 8.9 | 6.2 | 9.21 | 30.9% | 15.2% |
| B | 3,526 | 12.6 | 9.0 | 19.8 | 16.6 | 19.5 | 12.2 | 10.4 | 12.39 | 42.1% | 22.6% |
| C | 3,983 | 11.6 | 8.9 | 19.6 | 15.0 | 19.5 | 15.1 | 10.4 | 13.18 | 44.9% | 25.5% |
| D | 4,549 | 12.1 | 7.8 | 17.2 | 15.5 | 21.6 | 15.7 | 10.0 | 13.98 | 47.3% | 25.7% |
| F | 8,325 | 7.7 | 5.6 | 15.0 | 14.6 | 23.5 | 21.3 | 12.3 | 17.78 | 57.1% | 33.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,823 | 23.0 | 15.9 | 28.8 | 15.0 | 11.8 | 4.0 | 1.5 | 6.65 | 17.3% | 5.5% |
| B | 2,854 | 16.3 | 10.4 | 23.4 | 16.0 | 19.3 | 10.7 | 3.9 | 9.99 | 33.9% | 14.6% |
| C | 4,108 | 11.3 | 7.4 | 18.4 | 14.2 | 21.5 | 16.6 | 10.6 | 14.33 | 48.8% | 27.3% |
| D | 2,957 | 14.5 | 9.8 | 19.9 | 14.4 | 21.0 | 14.3 | 6.1 | 11.95 | 41.4% | 20.4% |
| F | 5,070 | 10.2 | 8.2 | 15.5 | 14.8 | 22.8 | 20.3 | 8.2 | 15.68 | 51.3% | 28.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,992 | 17.9 | 10.4 | 20.6 | 16.4 | 16.3 | 9.8 | 8.6 | 10.34 | 34.7% | 18.4% |
| LIMITED | 6,083 | 13.4 | 10.1 | 20.4 | 15.6 | 19.3 | 13.5 | 7.6 | 11.91 | 40.4% | 21.2% |
| POOR | 13,156 | 9.3 | 6.4 | 15.9 | 15.0 | 22.8 | 19.1 | 11.5 | 16.15 | 53.4% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,359 | 26.4 | 20.4 | 34.2 | 12.6 | 4.8 | 1.4 | 0.2 | 5.33 | 6.4% | 1.6% |
| GAME_SPREAD | 4,574 | 22.3 | 15.2 | 33.6 | 17.2 | 9.0 | 2.3 | 0.3 | 6.7 | 11.7% | 2.6% |
| MATCH_WINNER | 20,812 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.8 | 5.9 | 10.59 | 37.5% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,583 | 29.3 | 16.9 | 31.1 | 12.5 | 8.1 | 1.7 | 0.4 | 5.47 | 10.2% | 2.1% |
| TOTAL_GAMES | 7,313 | 8.4 | 9.6 | 36.5 | 29.0 | 10.6 | 3.2 | 2.7 | 9.51 | 16.5% | 5.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,701 | 25.3 | 33.9 | 32.6 | 4.4 | 3.0 | 0.5 | 0.2 | 4.48 | 3.7% | 0.7% |
| GAME_SPREAD | 5,973 | 45.4 | 16.9 | 27.1 | 7.7 | 1.8 | 0.8 | 0.3 | 3.5 | 2.9% | 1.1% |
| TOTAL_GAMES | 10,232 | 4.8 | 7.7 | 40.7 | 35.0 | 7.1 | 2.5 | 2.2 | 9.66 | 11.8% | 4.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,704 | 24.2 | 17.8 | 35.4 | 12.7 | 7.1 | 2.5 | 0.3 | 5.82 | 9.9% | 2.8% |
| GAME_SPREAD | 5,976 | 19.3 | 13.3 | 28.1 | 20.2 | 13.8 | 4.5 | 0.9 | 7.96 | 19.1% | 5.4% |
| TOTAL_GAMES | 10,253 | 8.5 | 9.2 | 36.3 | 27.3 | 12.5 | 3.8 | 2.4 | 9.52 | 18.7% | 6.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 28,231 | 44.6% | 24.7% | 13.21 | 36.3% | 15.5% | 11.0 |
| gen1_elo | 28,231 | 44.5% | 24.4% | 13.01 | 35.9% | 15.6% | 10.71 |
| gen1_sr | 28,231 | 52.8% | 31.6% | 16.09 | 45.1% | 22.4% | 13.32 |
| gen2 | 28,231 | 51.5% | 31.8% | 15.65 | 44.9% | 23.9% | 13.2 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 14,377 | 15.8 | 10.3 | 21.1 | 17.2 | 20.4 | 11.9 | 3.3 | 10.81 | 35.6% | 15.2% |
| STALE | 13,854 | 9.9 | 6.7 | 15.5 | 13.9 | 19.5 | 18.1 | 16.4 | 16.91 | 54.0% | 34.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,280 | 16.5 | 11.2 | 22.3 | 14.9 | 17.9 | 12.3 | 4.9 | 9.99 | 35.0% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 49,043 | 14280 | 17849 | 16914 | 24.0 | 135.7 | 1400.4 |
| ge_15pp | 20,406 | 5004 | 6413 | 8989 | 25.9 | 431.1 | 1380.4 |
| ge_25pp | 10,877 | 2446 | 2779 | 5652 | 31.5 | 574.2 | 1380.4 |
| lt_10pp | 21,146 | 7149 | 8414 | 5583 | 21.9 | 47.4 | 1341.5 |

Current slate `SL-20261022T130544Z-58f30d3b`: 376 priced rows, quote age at build {'median': 13.8, 'max': 13.8}, freshness {'AGING': 376}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 22 | 0.0 | 0.0 | 22.7 | 4.5 | 40.9 | 31.8 | 0.0 | 20.48 | 72.7% | 31.8% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,623 | 19.4 | 10.8 | 24.0 | 18.7 | 18.9 | 7.4 | 0.7 | 9.1 | 27.0% | 8.1% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 504 | 66.3 | 33.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.22 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,096 | 0.0 | 2.2 | 34.9 | 25.7 | 25.6 | 10.9 | 0.8 | 12.59 | 37.2% | 11.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 28,231 | 4274 (15.1%) | 25.6% | 0.9% | {"EXTERNAL_STALE": 2623, "AGREES_WITH_KALSHI": 1096, "ALL_AGREE": 504, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 12,603 | 1135 (9.0%) | 35.9% | 1.6% | {"EXTERNAL_STALE": 709, "AGREES_WITH_KALSHI": 408, "SUPPORTS_MODEL_DIRECTION": 16, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,969 | 348 (5.0%) | 36.8% | 2.3% | {"EXTERNAL_STALE": 212, "AGREES_WITH_KALSHI": 128, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,389 | 325 (9.6%) | 37.2% | 2.5% | {"EXTERNAL_STALE": 196, "AGREES_WITH_KALSHI": 121, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,228 | 2365 (21.1%) | 17.2% | 0.8% | {"EXTERNAL_STALE": 1423, "ALL_AGREE": 504, "AGREES_WITH_KALSHI": 406, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,381 | 10.5 | 7.6 | 19.3 | 14.4 | 22.4 | 15.8 | 10.0 | 14.16 | 48.3% | 25.8% |
| 4-10x | 3,695 | 10.9 | 8.4 | 19.1 | 15.3 | 21.3 | 14.8 | 10.2 | 13.75 | 46.3% | 25.0% |
| <2x | 14,315 | 14.9 | 9.6 | 18.9 | 16.6 | 18.0 | 13.2 | 8.9 | 11.97 | 40.1% | 22.0% |
| >=10x | 4,840 | 11.2 | 6.4 | 15.3 | 14.2 | 21.9 | 19.4 | 11.7 | 16.12 | 52.9% | 31.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,106 | 12.3 | 8.4 | 19.4 | 16.2 | 19.7 | 13.5 | 10.4 | 12.98 | 43.5% | 23.9% |
| 300-1000 | 6,120 | 11.6 | 8.7 | 17.2 | 15.2 | 20.8 | 16.4 | 10.2 | 14.0 | 47.3% | 26.5% |
| <300 | 9,273 | 8.8 | 5.7 | 15.5 | 14.8 | 23.0 | 20.0 | 12.1 | 16.85 | 55.2% | 32.1% |
| >=3000 | 5,732 | 21.6 | 12.9 | 22.9 | 16.4 | 14.4 | 7.0 | 4.8 | 8.01 | 26.2% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 806 | 0.5473 | 0.4098 | 0.5012 | +0.046 | -0.091 | -0.0042 ± 0.0054 |
| ratio 4-10x | 560 | 0.5849 | 0.4386 | 0.4911 | +0.094 | -0.052 | 0.0133 ± 0.0068 |
| ratio <2x | 2008 | 0.5374 | 0.4132 | 0.4467 | +0.091 | -0.034 | 0.0122 ± 0.0032 |
| ratio >=10x | 734 | 0.5688 | 0.3941 | 0.4619 | +0.107 | -0.068 | 0.0074 ± 0.0067 |
| thinner_sample 1000-3000 | 1107 | 0.5425 | 0.4145 | 0.4499 | +0.093 | -0.035 | 0.0105 ± 0.0043 |
| thinner_sample 300-1000 | 945 | 0.564 | 0.4211 | 0.4942 | +0.070 | -0.073 | 0.0001 ± 0.0052 |
| thinner_sample <300 | 1386 | 0.5576 | 0.3919 | 0.4618 | +0.096 | -0.070 | 0.0095 ± 0.0047 |
| thinner_sample >=3000 | 670 | 0.5356 | 0.4404 | 0.4627 | +0.073 | -0.022 | 0.0134 ± 0.0045 |
| data_status ADEQUATE | 1159 | 0.5381 | 0.4318 | 0.4504 | +0.088 | -0.019 | 0.013 ± 0.0037 |
| data_status LIMITED | 965 | 0.5498 | 0.4168 | 0.4819 | +0.068 | -0.065 | 0.0035 ± 0.0048 |
| data_status POOR | 1984 | 0.56 | 0.3993 | 0.4677 | +0.092 | -0.068 | 0.0078 ± 0.0039 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 603 | 0.1989 | 0.2 | -0.0011 ± 0.0006 | 0.5779 | 0.5803 | 0.5012 | 0.4863 | 0.5323 | -0.059 ± 0.0191 | -0.01 (5) |
| 3-5 | 384 | 0.2026 | 0.2017 | +0.0009 ± 0.0018 | 0.5885 | 0.5848 | 0.5 | 0.4599 | 0.4688 | -0.100 ± 0.0236 | 0.02 (1) |
| 5-10 | 835 | 0.2029 | 0.2026 | +0.0004 ± 0.0024 | 0.5928 | 0.5889 | 0.5126 | 0.4382 | 0.4683 | -0.089 ± 0.0162 | -0.0167 (6) |
| 10-15 | 712 | 0.2124 | 0.203 | +0.0094 ± 0.0042 | 0.6142 | 0.5871 | 0.5256 | 0.4014 | 0.4242 | -0.104 ± 0.0168 | -0.048 (5) |
| 15-25 | 936 | 0.224 | 0.2131 | +0.0109 ± 0.0059 | 0.643 | 0.6101 | 0.5766 | 0.3807 | 0.4509 | -0.089 ± 0.0149 | -0.0033 (9) |
| 25-40 | 533 | 0.2249 | 0.2111 | +0.0138 ± 0.0119 | 0.6381 | 0.6064 | 0.6567 | 0.3471 | 0.4765 | -0.074 ± 0.0183 | -0.01 (1) |
| 40+ | 105 | 0.2842 | 0.1913 | +0.0928 ± 0.0374 | 0.7775 | 0.5665 | 0.7532 | 0.306 | 0.4286 | -0.091 ± 0.0364 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3059 | 0.1841 | 0.1851 | -0.0010 ± 0.0003 | 0.5438 | 0.5448 | 0.4872 | 0.4722 | 0.5087 | -0.020 ± 0.0079 | -0.0129 (17) |
| 3-5 | 2036 | 0.197 | 0.1956 | +0.0014 ± 0.0008 | 0.5742 | 0.5679 | 0.4841 | 0.4442 | 0.4465 | -0.054 ± 0.01 | 0.0 (2) |
| 5-10 | 4359 | 0.199 | 0.1959 | +0.0032 ± 0.001 | 0.5824 | 0.5719 | 0.4827 | 0.4088 | 0.4235 | -0.047 ± 0.0068 | -0.0119 (21) |
| 10-15 | 3739 | 0.1991 | 0.1809 | +0.0181 ± 0.0017 | 0.5843 | 0.5334 | 0.485 | 0.3604 | 0.3496 | -0.075 ± 0.0069 | -0.0281 (16) |
| 15-25 | 4713 | 0.2084 | 0.17 | +0.0384 ± 0.0024 | 0.6104 | 0.5029 | 0.5035 | 0.3071 | 0.3081 | -0.072 ± 0.0059 | -0.0025 (44) |
| 25-40 | 3669 | 0.2241 | 0.1332 | +0.0909 ± 0.0038 | 0.6426 | 0.4051 | 0.5324 | 0.2199 | 0.2341 | -0.057 ± 0.0058 | -0.01 (1) |
| 40+ | 2369 | 0.3806 | 0.0441 | +0.3366 ± 0.0049 | 0.991 | 0.1723 | 0.6319 | 0.1064 | 0.0612 | -0.081 ± 0.004 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 459 | 0.2032 | 0.2038 | -0.0005 ± 0.0007 | 0.5884 | 0.5895 | 0.5045 | 0.4895 | 0.5054 | -0.111 ± 0.0227 | -0.01 (3) |
| 3-5 | 335 | 0.2207 | 0.2193 | +0.0014 ± 0.0021 | 0.6267 | 0.6239 | 0.5121 | 0.4721 | 0.4687 | -0.111 ± 0.0274 | 0.02 (1) |
| 5-10 | 721 | 0.2054 | 0.2051 | +0.0003 ± 0.0025 | 0.597 | 0.5952 | 0.5457 | 0.4708 | 0.5076 | -0.080 ± 0.0174 | -0.01 (4) |
| 10-15 | 685 | 0.2175 | 0.2096 | +0.0079 ± 0.0044 | 0.625 | 0.6051 | 0.5647 | 0.4402 | 0.473 | -0.110 ± 0.0182 | -0.04 (5) |
| 15-25 | 970 | 0.2303 | 0.2103 | +0.0200 ± 0.0058 | 0.6538 | 0.6034 | 0.5882 | 0.3922 | 0.4433 | -0.101 ± 0.015 | -0.0133 (9) |
| 25-40 | 684 | 0.2616 | 0.1988 | +0.0628 ± 0.0107 | 0.7303 | 0.5784 | 0.6542 | 0.3385 | 0.3991 | -0.110 ± 0.0167 | -0.0075 (4) |
| 40+ | 254 | 0.3589 | 0.1746 | +0.1843 ± 0.0259 | 0.9904 | 0.5214 | 0.733 | 0.2494 | 0.315 | -0.070 ± 0.0251 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2565 | 0.1942 | 0.1943 | -0.0001 ± 0.0003 | 0.566 | 0.5661 | 0.5077 | 0.4929 | 0.5037 | -0.049 ± 0.009 | -0.0133 (15) |
| 3-5 | 1736 | 0.1991 | 0.1989 | +0.0003 ± 0.0009 | 0.5761 | 0.5749 | 0.5131 | 0.4731 | 0.4885 | -0.038 ± 0.0109 | 0.02 (1) |
| 5-10 | 3834 | 0.1949 | 0.1937 | +0.0013 ± 0.0011 | 0.5743 | 0.5664 | 0.5052 | 0.4313 | 0.4617 | -0.030 ± 0.0072 | -0.0117 (6) |
| 10-15 | 3399 | 0.2002 | 0.1875 | +0.0127 ± 0.0019 | 0.5875 | 0.5478 | 0.5136 | 0.3895 | 0.4016 | -0.058 ± 0.0075 | -0.0189 (18) |
| 15-25 | 4758 | 0.2162 | 0.1782 | +0.0380 ± 0.0024 | 0.6284 | 0.5241 | 0.5255 | 0.3295 | 0.3344 | -0.069 ± 0.0062 | -0.0086 (42) |
| 25-40 | 4291 | 0.2515 | 0.141 | +0.1105 ± 0.0036 | 0.7082 | 0.4305 | 0.56 | 0.2433 | 0.2298 | -0.080 ± 0.0057 | -0.0044 (18) |
| 40+ | 3361 | 0.3959 | 0.0627 | +0.3332 ± 0.0049 | 1.0428 | 0.2224 | 0.6537 | 0.1206 | 0.0878 | -0.071 ± 0.0042 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 578 | 0.1998 | 0.2022 | -0.0024 ± 0.0007 | 0.5806 | 0.5864 | 0.4965 | 0.4812 | 0.5519 | -0.021 ± 0.0192 | -0.0137 (8) |
| 3-5 | 414 | 0.2 | 0.1978 | +0.0023 ± 0.0018 | 0.582 | 0.5754 | 0.5077 | 0.4681 | 0.4614 | -0.122 ± 0.0227 | 0.0067 (3) |
| 5-10 | 862 | 0.2007 | 0.1973 | +0.0035 ± 0.0023 | 0.5881 | 0.576 | 0.5092 | 0.4351 | 0.4466 | -0.101 ± 0.0155 | -0.0071 (7) |
| 10-15 | 713 | 0.2082 | 0.2054 | +0.0028 ± 0.0042 | 0.6038 | 0.5931 | 0.5386 | 0.415 | 0.467 | -0.084 ± 0.0168 | -0.0317 (6) |
| 15-25 | 879 | 0.2314 | 0.212 | +0.0194 ± 0.006 | 0.6611 | 0.607 | 0.5858 | 0.3915 | 0.438 | -0.113 ± 0.0155 | -0.03 (1) |
| 25-40 | 551 | 0.213 | 0.2183 | -0.0053 ± 0.0117 | 0.6136 | 0.6229 | 0.6669 | 0.3553 | 0.5172 | -0.050 ± 0.0179 | 0.015 (2) |
| 40+ | 111 | 0.298 | 0.205 | +0.0929 ± 0.0377 | 0.8197 | 0.5966 | 0.7613 | 0.3119 | 0.4414 | -0.082 ± 0.0394 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3008 | 0.1885 | 0.1891 | -0.0006 ± 0.0003 | 0.5528 | 0.5538 | 0.4895 | 0.4742 | 0.4897 | -0.037 ± 0.008 | -0.0163 (35) |
| 3-5 | 2047 | 0.1937 | 0.1908 | +0.0028 ± 0.0008 | 0.5693 | 0.5607 | 0.4895 | 0.4499 | 0.4353 | -0.074 ± 0.0099 | -0.0094 (18) |
| 5-10 | 4455 | 0.1953 | 0.1893 | +0.0060 ± 0.001 | 0.5749 | 0.5552 | 0.4858 | 0.4118 | 0.4076 | -0.063 ± 0.0066 | -0.01 (31) |
| 10-15 | 3596 | 0.193 | 0.1769 | +0.0161 ± 0.0017 | 0.5696 | 0.5226 | 0.4978 | 0.3742 | 0.3704 | -0.070 ± 0.007 | -0.015 (12) |
| 15-25 | 4876 | 0.2114 | 0.1725 | +0.0389 ± 0.0023 | 0.6171 | 0.5089 | 0.5121 | 0.3171 | 0.3148 | -0.074 ± 0.0059 | -0.03 (2) |
| 25-40 | 3654 | 0.219 | 0.1356 | +0.0834 ± 0.0038 | 0.6319 | 0.4102 | 0.5367 | 0.2209 | 0.2485 | -0.047 ± 0.0058 | 0.01 (3) |
| 40+ | 2308 | 0.3947 | 0.0494 | +0.3453 ± 0.0052 | 1.0313 | 0.1859 | 0.6442 | 0.113 | 0.0672 | -0.083 ± 0.0044 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 954 | 0.1947 | 0.1948 | -0.0002 ± 0.0005 | 0.5686 | 0.5686 | 0.5078 | 0.4927 | 0.4969 | -0.058 ± 0.0145 | -0.0224 (49) |
| 3-5 | 662 | 0.1924 | 0.1917 | +0.0007 ± 0.0014 | 0.5626 | 0.5595 | 0.4863 | 0.4465 | 0.4547 | -0.057 ± 0.0173 | -0.0194 (34) |
| 5-10 | 1394 | 0.2002 | 0.1939 | +0.0063 ± 0.0018 | 0.5895 | 0.5698 | 0.4957 | 0.4224 | 0.4182 | -0.073 ± 0.012 | -0.005 (78) |
| 10-15 | 912 | 0.2092 | 0.198 | +0.0112 ± 0.0037 | 0.6064 | 0.5778 | 0.5167 | 0.3935 | 0.4079 | -0.066 ± 0.015 | 0.0014 (64) |
| 15-25 | 1237 | 0.2302 | 0.21 | +0.0202 ± 0.0051 | 0.6578 | 0.6049 | 0.574 | 0.3792 | 0.426 | -0.069 ± 0.0131 | -0.0214 (59) |
| 25-40 | 752 | 0.249 | 0.2069 | +0.0422 ± 0.0102 | 0.7069 | 0.5949 | 0.6685 | 0.3563 | 0.4441 | -0.085 ± 0.0156 | -0.0219 (26) |
| 40+ | 254 | 0.3539 | 0.1963 | +0.1576 ± 0.0275 | 1.0222 | 0.5742 | 0.8074 | 0.3248 | 0.4213 | -0.097 ± 0.0251 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3119 | 0.1833 | 0.1834 | -0.0001 ± 0.0003 | 0.5398 | 0.5392 | 0.5079 | 0.4926 | 0.5021 | -0.039 ± 0.0077 | -0.0157 (88) |
| 3-5 | 2150 | 0.1927 | 0.1909 | +0.0019 ± 0.0008 | 0.5635 | 0.559 | 0.4938 | 0.4541 | 0.4502 | -0.053 ± 0.0095 | -0.0209 (69) |
| 5-10 | 4317 | 0.1979 | 0.1893 | +0.0086 ± 0.001 | 0.5817 | 0.5565 | 0.4916 | 0.418 | 0.3998 | -0.072 ± 0.0067 | -0.0082 (132) |
| 10-15 | 2986 | 0.2055 | 0.1898 | +0.0158 ± 0.002 | 0.5993 | 0.5578 | 0.5242 | 0.401 | 0.3979 | -0.065 ± 0.008 | -0.0053 (105) |
| 15-25 | 3766 | 0.2284 | 0.1994 | +0.0290 ± 0.0029 | 0.6594 | 0.5782 | 0.5669 | 0.3713 | 0.3956 | -0.062 ± 0.0073 | -0.0253 (107) |
| 25-40 | 2597 | 0.26 | 0.1846 | +0.0754 ± 0.0053 | 0.7369 | 0.5383 | 0.63 | 0.3158 | 0.3554 | -0.076 ± 0.0082 | -0.0229 (51) |
| 40+ | 1168 | 0.3779 | 0.1429 | +0.2350 ± 0.0116 | 1.0723 | 0.4314 | 0.7288 | 0.2254 | 0.256 | -0.074 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4108 | 1.039 ± 0.044 | 1.136 | 0.1683 | 0.165 | 0.2137 | 0.2054 |
| gen2 | 4108 | 0.844 ± 0.041 | 1.094 | 0.1694 | 0.1655 | 0.2332 | 0.2052 |
| gen1_elo | 4108 | 1.016 ± 0.042 | 1.125 | 0.1751 | 0.1651 | 0.2127 | 0.2056 |
| gen1_sr | 4108 | 1.038 ± 0.053 | 1.165 | 0.13 | 0.1675 | 0.2293 | 0.2047 |
| gen1_ledger | 6165 | 0.868 ± 0.031 | 1.078 | 0.1826 | 0.1797 | 0.2181 | 0.1993 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 20,406)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,671 | 22.9% |
| STALE_QUOTE | market_freshness | 4,396 | 21.5% |
| BOOK_QUALITY | execution | 3,840 | 18.8% |
| POOR_DATA | data | 2,336 | 11.5% |
| LIMITED_DATA | data | 1,295 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,103 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 970 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 862 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 601 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 332 | 1.6% |

Cause class: coverage 22.9%, market_freshness 21.5%, execution 18.8%, data 17.8%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.2%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 50.6%, STALE_KALSHI_QUOTE 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 16.1%, LEVEL_TRANSFER_RISK 11.0%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.4%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 10,877)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,748 | 34.5% |
| STALE_QUOTE | market_freshness | 2,002 | 18.4% |
| BOOK_QUALITY | execution | 1,999 | 18.4% |
| POOR_DATA | data | 971 | 8.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 589 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 491 | 4.5% |
| LIMITED_DATA | data | 395 | 3.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 377 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 230 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 34.5%, market_freshness 18.4%, execution 18.4%, data 12.6%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.9%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 52.0%, STALE_PLAYER_DATA 45.6%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 24.3%, PLAYER_IDENTITY_RISK 19.4%, MODEL_HIGH_UNCERTAINTY 17.9%, LEVEL_TRANSFER_RISK 9.8%, EVENT_MAPPING_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.5%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8487, "IDENTITY_AMBIGUOUS": 2390}; ticker orientation: {"VERIFIED": 10877}.

Checks: discipline:AMBIGUOUS 737, discipline:PASS 10140, identity_confidence:AMBIGUOUS 2116, identity_confidence:PASS 8761, level_mapping:NA 749, level_mapping:PASS 10128, market_pair:AMBIGUOUS 384, market_pair:NA 271, market_pair:PASS 10222, model_complement:NA 238, model_complement:PASS 10639, namesake:PASS 10877, physical_match_id:NA 3908, physical_match_id:PASS 6969, player_ids:PASS 10877, same_pair_other_event:PASS 10877, ticker_orientation:PASS 10877

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,807 | 4.9% | 4.4% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 19, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.84 | 0.2247 / 0.217 (431) | 19.0% | 3.9% | 3.3% | 2.8% |
| CHALLENGER | 7,543 | 17.2% | 7.0% | 11.9% | {"coverage": 730, "market_freshness/coverage": 161, "market_freshness": 148, "data": 128, "model_calibration_or_unknown": 59, "execution": 30, "model_calibration": 27, "mapping": 15} | 7.43 | 0.2176 / 0.2067 (1814) | 35.1% | 17.4% | 3.9% | 22.5% |
| DOUBLES | 1,542 | 47.8% | 47.3% | 6.8% | {"execution": 378, "mapping": 194, "market_freshness": 106, "market_freshness/coverage": 52, "coverage": 7} | 23.86 | 0.3137 / 0.2365 (399) | 15.2% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 13,664 | 25.0% | 17.5% | 31.4% | {"coverage": 1262, "execution": 671, "market_freshness": 570, "data": 463, "market_freshness/coverage": 287, "mapping": 165, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.82 | 0.2141 / 0.1962 (3085) | 37.3% | 68.8% | 19.1% | 21.9% |
| ITF_WOMEN | 18,254 | 27.0% | 19.7% | 45.2% | {"coverage": 1716, "market_freshness": 1045, "execution": 870, "data": 706, "market_freshness/coverage": 404, "mapping": 111, "model_calibration_or_unknown": 58, "model_calibration": 11} | 12.86 | 0.2035 / 0.1946 (3563) | 39.4% | 56.8% | 9.9% | 22.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,692 | 4.7% | 4.2% | 1.2% | {"market_freshness": 40, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.82 | 0.2385 / 0.2306 (451) | 24.5% | 1.3% | 1.4% | 3.7% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 15 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 16 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 17 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 18 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 19 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | POOR_DATA | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 20 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 21 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 22 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 23 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 26 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 27 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 28 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 29 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 32 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 33 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 34 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 36 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 38 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 39 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 40 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 41 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 43 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 44 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 45 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 46 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 47 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 48 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 49 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 1143 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 50 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 730 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9711, "by_level_share_of_ge_25pp": {"ATP": 0.0172, "CHALLENGER": 0.1193, "DOUBLES": 0.0678, "ITF_MEN": 0.3145, "ITF_WOMEN": 0.4524, "OTHER": 0.0011, "WTA": 0.0117, "WTA125": 0.016}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5196, "share_primary_cause_market_settled_or_in_play": 0.4335, "share_primary_cause_stale_quote_only": 0.1841}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 10877, "identity_ambiguous_share": 0.2197, "ticker_orientation": {"VERIFIED": 10877}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6969, "with_external": 348, "coverage": 0.0499, "external_status": {"EXTERNAL_STALE": 212, "AGREES_WITH_KALSHI": 128, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 212, "MODEL_LONE_OUTLIER": 128, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3678, "share_external_supports_model": 0.023}, "pregame_clean_ge_25pp": {"n": 3389, "with_external": 325, "coverage": 0.0959, "external_status": {"EXTERNAL_STALE": 196, "AGREES_WITH_KALSHI": 121, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 196, "MODEL_LONE_OUTLIER": 121, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3723, "share_external_supports_model": 0.0246}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.0, "median_sample_ratio": 2.45, "median_min_matches": 20.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2135, "data_status": {"POOR": 6091, "LIMITED": 2896, "ADEQUATE": 1890}, "comparison_lt_10pp": {"median_thinner_serve_points": 1667.0, "median_sample_ratio": 1.71, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 806, "model_minus_observed": 0.0461, "kalshi_minus_observed": -0.0914, "brier_diff_model_minus_kalshi": -0.0042}, "4-10x": {"n": 560, "model_minus_observed": 0.0938, "kalshi_minus_observed": -0.0525, "brier_diff_model_minus_kalshi": 0.0133}, "<2x": {"n": 2008, "model_minus_observed": 0.0907, "kalshi_minus_observed": -0.0335, "brier_diff_model_minus_kalshi": 0.0122}, ">=10x": {"n": 734, "model_minus_observed": 0.1069, "kalshi_minus_observed": -0.0677, "brier_diff_model_minus_kalshi": 0.0074}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4108, "model": {"intercept": -0.545, "slope": 0.844, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.218, "slope": 1.094, "slope_se": 0.045}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1655, "model_brier": 0.2332, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.028, "brier_diff_se": 0.003, "model_logloss": 0.663, "kalshi_logloss": 0.5931}, "fair_v1": {"n": 4108, "model": {"intercept": -0.41, "slope": 1.039, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.308, "slope": 1.136, "slope_se": 0.046}, "mean_extremity_model": 0.1683, "mean_extremity_kalshi": 0.165, "model_brier": 0.2137, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.0024, "model_logloss": 0.6159, "kalshi_logloss": 0.5935}, "gen1_elo": {"n": 4108, "model": {"intercept": -0.394, "slope": 1.016, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.316, "slope": 1.125, "slope_se": 0.045}, "mean_extremity_model": 0.1751, "mean_extremity_kalshi": 0.1651, "model_brier": 0.2127, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0071, "brier_diff_se": 0.0025, "model_logloss": 0.6145, "kalshi_logloss": 0.5939}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2469, "share_ge_15": 0.4464, "median_abs_gap": 13.21, "n": 28231}, "gen1_elo": {"share_ge_25": 0.2443, "share_ge_15": 0.4447, "median_abs_gap": 13.01, "n": 28231}, "gen1_sr": {"share_ge_25": 0.3155, "share_ge_15": 0.5275, "median_abs_gap": 16.09, "n": 28231}, "gen2": {"share_ge_25": 0.3182, "share_ge_15": 0.515, "median_abs_gap": 15.65, "n": 28231}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1546, "share_ge_15": 0.3632, "median_abs_gap": 11.0, "n": 21921}, "gen1_elo": {"share_ge_25": 0.156, "share_ge_15": 0.3591, "median_abs_gap": 10.71, "n": 21918}, "gen1_sr": {"share_ge_25": 0.2235, "share_ge_15": 0.451, "median_abs_gap": 13.32, "n": 21922}, "gen2": {"share_ge_25": 0.2392, "share_ge_15": 0.4485, "median_abs_gap": 13.2, "n": 21923}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0491, "share_ge_25_pregame_clean": 0.0441}, "WTA": {"median_abs_gap_pregame_clean": 7.82, "share_ge_25_all": 0.0472, "share_ge_25_pregame_clean": 0.0417}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2343, "share_within_10pp_all": 0.4312, "share_within_10pp_pregame_clean": 0.4837, "corr_model_vs_mid_pregame_clean": 0.8451}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 603, "model_brier": 0.1989, "kalshi_brier": 0.2, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 712, "model_brier": 0.2124, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": 0.0094}, "15-25": {"n_settled": 936, "model_brier": 0.224, "kalshi_brier": 0.2131, "brier_diff_model_minus_kalshi": 0.0109}, "25-40": {"n_settled": 533, "model_brier": 0.2249, "kalshi_brier": 0.2111, "brier_diff_model_minus_kalshi": 0.0138}, "3-5": {"n_settled": 384, "model_brier": 0.2026, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0009}, "40+": {"n_settled": 105, "model_brier": 0.2842, "kalshi_brier": 0.1913, "brier_diff_model_minus_kalshi": 0.0928}, "5-10": {"n_settled": 835, "model_brier": 0.2029, "kalshi_brier": 0.2026, "brier_diff_model_minus_kalshi": 0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.545, "slope": 0.844, "slope_se": 0.041}, "kalshi_slope": {"intercept": 0.218, "slope": 1.094, "slope_se": 0.045}, "n": 4108}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.511, "slope": 0.868, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.157, "slope": 1.078, "slope_se": 0.035}, "n": 6165}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 399, "model_brier": 0.3137, "kalshi_brier": 0.2365, "brier_diff_model_minus_kalshi": 0.0772, "brier_diff_se": 0.0154, "corr_model_outcome": 0.0233, "corr_kalshi_outcome": 0.251}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
