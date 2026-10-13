# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-13T01:09Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 30,396): 0-3 14.6%, 3-5 9.7%, 5-10 20.2%, 10-15 15.4%, 15-25 18.6%, 25-40 13.4%, 40+ 8.1%; median gap 11.67 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.0%, Challenger 12.4%, doubles 7.1%). Main tour: ATP 1.5% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,543): MARKET_ALREADY_SETTLED_WHEN_PRICED 38.6%, BOOK_QUALITY 17.6%, STALE_QUOTE 16.3%, POOR_DATA 8.1%, POSSIBLY_IN_PLAY_QUOTE 5.6%, LIMITED_DATA 4.2%, IDENTITY_AMBIGUOUS 3.8%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 38.6%, execution 17.6%, market_freshness 16.3%, data 12.3%, market_freshness/coverage 9.1%, mapping 3.8%, model_calibration_or_unknown 2.0%, model_calibration 0.4%.
* **Stale / settled / in-play**: 53.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 47.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,543 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.5% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 608.0 points vs 1893.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.06, Gen-2 0.865, Gen-1 ledger 0.87 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 284 model 0.2207 vs Kalshi 0.2021; n 65 model 0.2875 vs Kalshi 0.1787.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 121,382 model-market comparisons (199,623 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 44,841 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-13T01:04:33.950267+00:00'], shadow board 32,237 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-13T01:04:36.669330+00:00'], Model 4 13,684 rows, 13,218 settled tickers, 3,831 tickers with an external scan.
* By model: {"gen1_ledger": 29533, "gen1_elo": 16198, "fair_v1": 16198, "gen2": 16198, "gen1_sr": 16198, "model4_fundamental": 13533, "model4_conditioned": 13524}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 30,396 | 14.6 | 9.7 | 20.2 | 15.4 | 18.6 | 13.4 | 8.1 | 11.67 | 40.1% | 21.5% |
| MW fair_v1 | 16,198 | 13.8 | 8.8 | 18.7 | 16.0 | 18.7 | 14.3 | 9.6 | 12.69 | 42.6% | 24.0% |
| MW gen1_elo | 16,198 | 13.4 | 9.1 | 20.3 | 15.1 | 18.7 | 14.2 | 9.2 | 12.06 | 42.0% | 23.4% |
| MW gen1_ledger | 14,198 | 15.4 | 10.8 | 21.9 | 14.7 | 18.5 | 12.4 | 6.3 | 10.46 | 37.2% | 18.7% |
| MW gen1_sr | 16,198 | 10.1 | 7.9 | 16.6 | 14.4 | 21.6 | 18.0 | 11.3 | 15.38 | 51.0% | 29.3% |
| MW gen2 | 16,198 | 12.0 | 7.4 | 16.4 | 14.3 | 20.1 | 17.0 | 12.8 | 14.97 | 49.9% | 29.8% |
| all families model4_conditioned | 13,524 | 21.8 | 20.1 | 35.7 | 16.2 | 4.2 | 1.1 | 0.9 | 5.79 | 6.2% | 2.0% |
| all families model4_fundamental | 13,533 | 16.6 | 13.3 | 35.9 | 19.9 | 10.6 | 2.6 | 1.1 | 7.63 | 14.3% | 3.8% |

Configurable thresholds (primary): >=5pp 75.8%, >=10pp 55.5%, >=15pp 40.1%, >=20pp 29.7%, >=25pp 21.5%, >=30pp 15.8%, >=40pp 8.1%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.23pp; >=10pp 44.7%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,299 | 30.2 | 14.6 | 24.8 | 17.9 | 10.6 | 1.1 | 0.8 | 5.84 | 12.6% | 2.0% |
| CHALLENGER | 2,873 | 15.7 | 10.1 | 20.1 | 15.9 | 14.6 | 12.0 | 11.4 | 11.5 | 38.0% | 23.4% |
| ITF_MEN | 4,465 | 11.5 | 8.7 | 18.2 | 14.9 | 19.2 | 15.4 | 12.1 | 13.82 | 46.7% | 27.5% |
| ITF_WOMEN | 6,189 | 10.2 | 6.6 | 15.9 | 16.2 | 21.8 | 18.6 | 10.7 | 15.46 | 51.1% | 29.3% |
| WTA | 849 | 21.3 | 11.1 | 25.3 | 16.2 | 19.3 | 5.4 | 1.3 | 8.09 | 26.0% | 6.7% |
| WTA125 | 523 | 13.2 | 8.2 | 23.5 | 19.5 | 18.9 | 14.5 | 2.1 | 11.08 | 35.6% | 16.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,299 | 23.9 | 14.7 | 24.3 | 19.3 | 14.8 | 1.9 | 1.0 | 6.9 | 17.7% | 2.9% |
| CHALLENGER | 2,873 | 15.3 | 7.5 | 19.5 | 13.4 | 18.2 | 14.2 | 11.9 | 12.68 | 44.3% | 26.1% |
| ITF_MEN | 4,465 | 10.3 | 7.4 | 16.6 | 14.5 | 19.9 | 18.0 | 13.3 | 15.48 | 51.2% | 31.3% |
| ITF_WOMEN | 6,189 | 8.9 | 5.8 | 12.8 | 12.8 | 21.6 | 21.1 | 17.0 | 19.11 | 59.7% | 38.0% |
| WTA | 849 | 18.5 | 8.4 | 18.5 | 16.0 | 23.0 | 14.4 | 1.3 | 11.64 | 38.6% | 15.7% |
| WTA125 | 523 | 5.5 | 4.2 | 19.3 | 18.4 | 23.7 | 18.7 | 10.1 | 16.74 | 52.6% | 28.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,299 | 27.3 | 14.3 | 29.2 | 15.2 | 10.5 | 2.5 | 0.9 | 6.1 | 13.9% | 3.5% |
| CHALLENGER | 2,873 | 15.3 | 10.2 | 21.2 | 15.3 | 14.9 | 11.7 | 11.4 | 10.7 | 38.0% | 23.1% |
| ITF_MEN | 4,465 | 10.5 | 8.7 | 18.9 | 13.8 | 20.0 | 15.8 | 12.2 | 14.06 | 48.0% | 28.0% |
| ITF_WOMEN | 6,189 | 9.8 | 6.8 | 16.5 | 15.7 | 22.6 | 19.0 | 9.5 | 15.49 | 51.1% | 28.5% |
| WTA | 849 | 22.6 | 15.4 | 33.5 | 15.3 | 10.0 | 2.4 | 0.8 | 6.12 | 13.2% | 3.2% |
| WTA125 | 523 | 21.8 | 11.7 | 29.2 | 15.3 | 14.7 | 6.9 | 0.4 | 7.73 | 22.0% | 7.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 707 | 30.6 | 22.9 | 35.8 | 9.1 | 1.3 | 0.4 | 0.0 | 4.73 | 1.7% | 0.4% |
| CHALLENGER | 1,989 | 22.1 | 15.8 | 27.3 | 14.8 | 13.0 | 5.0 | 2.1 | 6.94 | 20.1% | 7.1% |
| DOUBLES | 922 | 4.5 | 3.1 | 11.4 | 11.4 | 19.4 | 24.7 | 25.5 | 25.33 | 69.6% | 50.2% |
| ITF_MEN | 4,243 | 14.8 | 8.5 | 21.0 | 15.5 | 20.5 | 12.3 | 7.3 | 11.76 | 40.1% | 19.6% |
| ITF_WOMEN | 4,915 | 11.6 | 9.3 | 19.5 | 14.6 | 22.5 | 16.7 | 5.8 | 13.12 | 45.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 632 | 21.7 | 14.9 | 26.7 | 17.2 | 13.9 | 5.1 | 0.5 | 7.61 | 19.5% | 5.5% |
| WTA125 | 641 | 19.5 | 14.2 | 22.0 | 18.6 | 14.8 | 8.6 | 2.3 | 8.37 | 25.7% | 10.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,285 | 30.1 | 14.5 | 25.0 | 18.0 | 10.5 | 1.1 | 0.9 | 5.84 | 12.4% | 1.9% |
| CHALLENGER | 2,101 | 19.9 | 12.5 | 25.1 | 18.5 | 15.2 | 6.1 | 2.6 | 8.36 | 23.9% | 8.7% |
| ITF_MEN | 3,172 | 14.4 | 10.9 | 21.8 | 16.7 | 19.2 | 12.1 | 4.9 | 10.79 | 36.2% | 17.0% |
| ITF_WOMEN | 4,429 | 12.6 | 8.3 | 18.5 | 18.8 | 23.4 | 14.9 | 3.4 | 12.71 | 41.8% | 18.3% |
| WTA | 836 | 21.4 | 10.5 | 25.7 | 16.4 | 19.4 | 5.3 | 1.3 | 8.14 | 26.0% | 6.6% |
| WTA125 | 501 | 13.8 | 8.0 | 22.9 | 19.8 | 19.6 | 14.4 | 1.6 | 11.08 | 35.5% | 16.0% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,285 | 23.8 | 14.8 | 24.4 | 19.3 | 14.8 | 1.9 | 1.0 | 6.9 | 17.7% | 2.9% |
| CHALLENGER | 2,101 | 19.4 | 9.5 | 24.0 | 16.0 | 18.6 | 9.8 | 2.7 | 9.19 | 31.0% | 12.4% |
| ITF_MEN | 3,173 | 12.4 | 9.0 | 19.2 | 16.4 | 21.6 | 15.3 | 6.2 | 12.7 | 43.1% | 21.5% |
| ITF_WOMEN | 4,429 | 10.4 | 6.9 | 14.5 | 14.0 | 24.3 | 19.8 | 10.1 | 16.51 | 54.2% | 29.9% |
| WTA | 836 | 18.3 | 8.1 | 18.7 | 16.3 | 23.0 | 14.3 | 1.3 | 11.74 | 38.6% | 15.7% |
| WTA125 | 501 | 5.6 | 4.4 | 19.4 | 18.8 | 23.4 | 19.4 | 9.2 | 16.14 | 51.9% | 28.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 687 | 30.6 | 23.1 | 36.1 | 9.2 | 0.6 | 0.4 | 0.0 | 4.7 | 1.0% | 0.4% |
| CHALLENGER | 1,716 | 23.9 | 17.3 | 29.4 | 14.6 | 12.0 | 2.2 | 0.6 | 6.31 | 14.7% | 2.7% |
| DOUBLES | 854 | 4.5 | 3.2 | 11.7 | 11.4 | 19.6 | 24.6 | 25.2 | 24.68 | 69.3% | 49.8% |
| ITF_MEN | 3,442 | 16.5 | 9.4 | 23.2 | 16.4 | 20.3 | 10.1 | 4.2 | 10.21 | 34.5% | 14.2% |
| ITF_WOMEN | 4,018 | 12.8 | 10.0 | 21.4 | 15.4 | 22.8 | 15.0 | 2.6 | 11.64 | 40.4% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 598 | 22.2 | 15.6 | 26.9 | 17.2 | 14.2 | 3.9 | 0.0 | 7.21 | 18.1% | 3.9% |
| WTA125 | 541 | 21.4 | 15.7 | 23.5 | 20.5 | 13.1 | 5.4 | 0.4 | 7.5 | 18.9% | 5.7% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 922 | 4.5 | 3.1 | 11.4 | 11.4 | 19.4 | 24.7 | 25.5 | 25.33 | 69.6% | 50.2% |
| singles | 13,276 | 16.1 | 11.3 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.96 | 35.0% | 16.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,731 | 13.5 | 9.3 | 20.5 | 15.9 | 17.1 | 13.9 | 9.8 | 12.15 | 40.8% | 23.7% |
| Grass | 105 | 12.4 | 19.1 | 15.2 | 9.5 | 25.7 | 16.2 | 1.9 | 12.57 | 43.8% | 18.1% |
| Hard | 10,747 | 14.3 | 8.6 | 18.6 | 15.9 | 19.0 | 14.1 | 9.5 | 12.64 | 42.6% | 23.6% |
| UNKNOWN | 1,615 | 11.6 | 8.1 | 15.6 | 17.8 | 19.7 | 16.7 | 10.6 | 14.04 | 46.9% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,021 | 20.0 | 10.8 | 21.1 | 17.0 | 15.3 | 8.7 | 7.0 | 9.42 | 31.0% | 15.7% |
| B | 2,187 | 14.3 | 9.3 | 19.9 | 17.1 | 17.6 | 11.9 | 9.7 | 11.5 | 39.3% | 21.7% |
| C | 2,366 | 13.3 | 9.7 | 19.5 | 14.7 | 19.0 | 14.6 | 9.1 | 12.6 | 42.8% | 23.8% |
| D | 2,867 | 10.8 | 8.4 | 17.9 | 16.0 | 22.2 | 14.7 | 9.9 | 13.92 | 46.8% | 24.6% |
| F | 3,757 | 7.9 | 5.3 | 15.0 | 14.9 | 20.9 | 22.8 | 13.2 | 18.21 | 56.9% | 36.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,188 | 22.4 | 16.0 | 28.6 | 15.2 | 11.6 | 4.5 | 1.7 | 6.78 | 17.8% | 6.2% |
| B | 2,196 | 15.2 | 9.8 | 24.1 | 16.2 | 19.1 | 11.2 | 4.3 | 10.17 | 34.6% | 15.5% |
| C | 2,812 | 12.2 | 7.6 | 18.1 | 14.4 | 20.4 | 15.8 | 11.4 | 13.7 | 47.6% | 27.2% |
| D | 2,201 | 14.0 | 9.9 | 20.9 | 13.3 | 21.7 | 13.9 | 6.3 | 11.85 | 41.8% | 20.2% |
| F | 2,801 | 9.3 | 7.5 | 14.8 | 14.0 | 23.8 | 20.8 | 9.6 | 16.71 | 54.2% | 30.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,543 | 18.4 | 9.8 | 20.3 | 17.0 | 15.5 | 9.6 | 9.3 | 10.42 | 34.4% | 18.9% |
| LIMITED | 3,975 | 15.3 | 10.5 | 20.7 | 15.7 | 18.4 | 12.8 | 6.7 | 11.02 | 37.8% | 19.4% |
| POOR | 6,680 | 9.2 | 6.8 | 16.3 | 15.4 | 21.5 | 19.2 | 11.7 | 15.93 | 52.3% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,922 | 31.3 | 24.1 | 36.5 | 5.5 | 1.8 | 0.7 | 0.1 | 4.51 | 2.6% | 0.8% |
| GAME_SPREAD | 2,826 | 25.6 | 15.9 | 36.9 | 16.9 | 4.2 | 0.4 | 0.2 | 6.03 | 4.8% | 0.6% |
| MATCH_WINNER | 14,198 | 15.4 | 10.8 | 21.9 | 14.7 | 18.5 | 12.4 | 6.3 | 10.46 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,321 | 33.2 | 19.5 | 30.8 | 9.8 | 5.3 | 1.2 | 0.2 | 4.76 | 6.7% | 1.4% |
| TOTAL_GAMES | 4,242 | 6.7 | 9.1 | 39.2 | 29.7 | 10.3 | 2.7 | 2.4 | 9.46 | 15.4% | 5.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,805 | 25.6 | 38.0 | 31.6 | 0.3 | 4.0 | 0.4 | 0.1 | 4.32 | 4.5% | 0.6% |
| GAME_SPREAD | 3,419 | 45.0 | 16.2 | 29.1 | 7.4 | 1.1 | 0.7 | 0.4 | 3.59 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,300 | 3.3 | 6.5 | 43.6 | 36.2 | 6.5 | 1.9 | 1.9 | 9.7 | 10.4% | 3.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,805 | 26.2 | 18.5 | 37.3 | 9.3 | 6.4 | 2.1 | 0.3 | 5.53 | 8.8% | 2.4% |
| GAME_SPREAD | 3,419 | 18.9 | 13.1 | 30.3 | 21.4 | 13.2 | 2.4 | 0.7 | 7.88 | 16.2% | 3.1% |
| TOTAL_GAMES | 5,309 | 6.5 | 8.7 | 38.2 | 28.4 | 12.8 | 3.3 | 2.1 | 9.67 | 18.2% | 5.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 16,198 | 42.6% | 24.0% | 12.69 | 32.9% | 13.7% | 10.22 |
| gen1_elo | 16,198 | 42.0% | 23.4% | 12.06 | 31.9% | 13.5% | 9.59 |
| gen1_sr | 16,198 | 51.0% | 29.3% | 15.38 | 42.2% | 19.1% | 12.55 |
| gen2 | 16,198 | 49.9% | 29.8% | 14.97 | 42.4% | 20.9% | 12.5 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 8,628 | 16.7 | 10.9 | 21.7 | 17.5 | 18.9 | 11.0 | 3.3 | 10.18 | 33.2% | 14.3% |
| STALE | 7,570 | 10.6 | 6.3 | 15.3 | 14.4 | 18.5 | 18.1 | 16.9 | 16.86 | 53.4% | 35.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 7,666 | 17.3 | 11.8 | 23.8 | 14.6 | 16.8 | 11.0 | 4.6 | 9.27 | 32.4% | 15.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 30,396 | 7666 | 12100 | 10630 | 24.1 | 140.6 | 1400.4 |
| ge_15pp | 12,194 | 2487 | 4152 | 5555 | 27.1 | 440.2 | 1380.4 |
| ge_25pp | 6,543 | 1198 | 1827 | 3518 | 34.5 | 574.7 | 1380.4 |
| lt_10pp | 13,520 | 4058 | 5889 | 3573 | 22.4 | 48.8 | 1341.5 |

Current slate `SL-20261013T010927Z-2a934939`: 625 priced rows, quote age at build {'median': 5.1, 'max': 5.2}, freshness {'FRESH': 625}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 8 | 0.0 | 0.0 | 37.5 | 0.0 | 37.5 | 25.0 | 0.0 | 20.45 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 8 | 62.5 | 37.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,192 | 22.0 | 11.0 | 23.1 | 18.6 | 18.5 | 6.4 | 0.5 | 8.59 | 25.3% | 6.9% |
| KALSHI_LONE_OUTLIER | 5 | 20.0 | 0.0 | 60.0 | 0.0 | 20.0 | 0.0 | 0.0 | 5.14 | 20.0% | 0.0% |
| MARKETS_AGREE | 214 | 72.0 | 28.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.01 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 390 | 0.0 | 4.4 | 35.9 | 30.3 | 21.0 | 7.7 | 0.8 | 11.26 | 29.5% | 8.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 16,198 | 1817 (11.2%) | 21.5% | 0.7% | {"EXTERNAL_STALE": 1192, "AGREES_WITH_KALSHI": 390, "ALL_AGREE": 214, "EXTERNAL_OUTLIER": 8, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 5, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 6,908 | 423 (6.1%) | 27.2% | 1.4% | {"EXTERNAL_STALE": 302, "AGREES_WITH_KALSHI": 115, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp | 3,883 | 117 (3.0%) | 28.2% | 1.7% | {"EXTERNAL_STALE": 82, "AGREES_WITH_KALSHI": 33, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp_pregame_clean | 1,691 | 111 (6.6%) | 27.9% | 1.8% | {"EXTERNAL_STALE": 78, "AGREES_WITH_KALSHI": 31, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_lt_10pp | 6,693 | 1054 (15.8%) | 14.9% | 0.6% | {"EXTERNAL_STALE": 668, "ALL_AGREE": 214, "AGREES_WITH_KALSHI": 157, "EXTERNAL_OUTLIER": 8, "AGREES_WITH_MODEL": 4, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,209 | 11.7 | 8.3 | 19.7 | 15.1 | 21.4 | 13.8 | 10.0 | 13.25 | 45.2% | 23.8% |
| 4-10x | 2,160 | 12.0 | 9.0 | 19.2 | 15.3 | 19.5 | 15.8 | 9.2 | 13.04 | 44.5% | 25.0% |
| <2x | 8,695 | 15.9 | 9.3 | 18.9 | 17.2 | 17.1 | 12.6 | 9.0 | 11.67 | 38.7% | 21.6% |
| >=10x | 2,134 | 10.6 | 6.7 | 16.1 | 13.5 | 20.0 | 20.7 | 12.3 | 16.38 | 53.0% | 33.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,283 | 14.1 | 8.3 | 19.4 | 16.0 | 18.9 | 12.7 | 10.6 | 12.51 | 42.2% | 23.2% |
| 300-1000 | 3,772 | 12.1 | 8.9 | 17.3 | 16.0 | 21.1 | 15.6 | 9.0 | 13.56 | 45.7% | 24.7% |
| <300 | 4,302 | 8.6 | 6.2 | 15.9 | 14.7 | 20.8 | 21.1 | 12.7 | 17.02 | 54.6% | 33.8% |
| >=3000 | 3,841 | 21.1 | 11.8 | 22.6 | 17.6 | 13.7 | 7.4 | 5.7 | 8.49 | 26.8% | 13.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 520 | 0.5349 | 0.4036 | 0.4788 | +0.056 | -0.075 | 0.0028 ± 0.0063 |
| ratio 4-10x | 348 | 0.5835 | 0.4432 | 0.5201 | +0.063 | -0.077 | 0.0027 ± 0.0084 |
| ratio <2x | 1240 | 0.5387 | 0.4174 | 0.4589 | +0.080 | -0.042 | 0.0108 ± 0.004 |
| ratio >=10x | 357 | 0.5509 | 0.3827 | 0.4398 | +0.111 | -0.057 | 0.0134 ± 0.0095 |
| thinner_sample 1000-3000 | 698 | 0.5438 | 0.4191 | 0.4756 | +0.068 | -0.057 | 0.0043 ± 0.0054 |
| thinner_sample 300-1000 | 632 | 0.5621 | 0.4234 | 0.4858 | +0.076 | -0.062 | 0.0038 ± 0.0062 |
| thinner_sample <300 | 703 | 0.5458 | 0.3858 | 0.4566 | +0.089 | -0.071 | 0.0121 ± 0.0065 |
| thinner_sample >=3000 | 432 | 0.5266 | 0.4327 | 0.4537 | +0.073 | -0.021 | 0.0155 ± 0.0055 |
| data_status ADEQUATE | 698 | 0.5298 | 0.4264 | 0.4527 | +0.077 | -0.026 | 0.0094 ± 0.0047 |
| data_status LIMITED | 672 | 0.5536 | 0.4245 | 0.4926 | +0.061 | -0.068 | 0.0022 ± 0.0057 |
| data_status POOR | 1095 | 0.5517 | 0.3976 | 0.4648 | +0.087 | -0.067 | 0.0114 ± 0.0051 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 380 | 0.1937 | 0.1951 | -0.0014 ± 0.0008 | 0.5659 | 0.569 | 0.4909 | 0.4761 | 0.5211 | -0.052 ± 0.0237 | -0.01 (3) |
| 3-5 | 254 | 0.1893 | 0.1909 | -0.0016 ± 0.0022 | 0.5584 | 0.5606 | 0.5071 | 0.4674 | 0.5039 | -0.056 ± 0.0278 | 0.02 (1) |
| 5-10 | 516 | 0.1981 | 0.2008 | -0.0027 ± 0.003 | 0.5804 | 0.5861 | 0.5167 | 0.4427 | 0.4884 | -0.075 ± 0.0206 | -0.0125 (4) |
| 10-15 | 439 | 0.211 | 0.2037 | +0.0073 ± 0.0054 | 0.6095 | 0.5883 | 0.5183 | 0.3946 | 0.4237 | -0.091 ± 0.0215 | -0.0633 (3) |
| 15-25 | 527 | 0.2303 | 0.2163 | +0.0140 ± 0.0079 | 0.6556 | 0.6201 | 0.5753 | 0.3806 | 0.444 | -0.083 ± 0.0203 | -0.0133 (6) |
| 25-40 | 284 | 0.2207 | 0.2021 | +0.0186 ± 0.0159 | 0.6323 | 0.5802 | 0.65 | 0.3408 | 0.4648 | -0.074 ± 0.0239 | -0.01 (1) |
| 40+ | 65 | 0.2875 | 0.1787 | +0.1088 ± 0.0465 | 0.785 | 0.5325 | 0.7482 | 0.3016 | 0.4 | -0.118 ± 0.0466 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1889 | 0.1764 | 0.1775 | -0.0011 ± 0.0003 | 0.5269 | 0.528 | 0.4778 | 0.4628 | 0.4981 | -0.021 ± 0.0098 | -0.0188 (8) |
| 3-5 | 1188 | 0.1955 | 0.1941 | +0.0014 ± 0.001 | 0.5726 | 0.5648 | 0.4783 | 0.4388 | 0.4377 | -0.060 ± 0.013 | 0.02 (1) |
| 5-10 | 2546 | 0.1931 | 0.1912 | +0.0019 ± 0.0013 | 0.5679 | 0.5611 | 0.4864 | 0.4126 | 0.4321 | -0.048 ± 0.0088 | -0.0082 (17) |
| 10-15 | 2217 | 0.2007 | 0.183 | +0.0176 ± 0.0023 | 0.5871 | 0.5377 | 0.4783 | 0.3539 | 0.3451 | -0.075 ± 0.0091 | -0.0475 (4) |
| 15-25 | 2601 | 0.2059 | 0.1706 | +0.0353 ± 0.0032 | 0.6039 | 0.5043 | 0.4983 | 0.3025 | 0.313 | -0.064 ± 0.0081 | -0.0048 (29) |
| 25-40 | 2110 | 0.2197 | 0.1237 | +0.0960 ± 0.0048 | 0.6327 | 0.3826 | 0.5292 | 0.2152 | 0.2227 | -0.064 ± 0.0074 | -0.01 (1) |
| 40+ | 1439 | 0.3705 | 0.045 | +0.3254 ± 0.0062 | 0.9666 | 0.1767 | 0.6234 | 0.1075 | 0.0605 | -0.085 ± 0.0052 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 289 | 0.197 | 0.1973 | -0.0003 ± 0.0009 | 0.5769 | 0.5777 | 0.497 | 0.482 | 0.4913 | -0.090 ± 0.0279 | -0.01 (1) |
| 3-5 | 193 | 0.2125 | 0.2128 | -0.0003 ± 0.0027 | 0.6071 | 0.6092 | 0.5226 | 0.4825 | 0.5026 | -0.064 ± 0.0348 | 0.02 (1) |
| 5-10 | 456 | 0.195 | 0.1943 | +0.0007 ± 0.0031 | 0.5714 | 0.57 | 0.5553 | 0.4802 | 0.511 | -0.076 ± 0.0214 | -0.01 (4) |
| 10-15 | 415 | 0.2167 | 0.2071 | +0.0095 ± 0.0056 | 0.6204 | 0.6001 | 0.5753 | 0.4507 | 0.4795 | -0.099 ± 0.0231 | -0.05 (4) |
| 15-25 | 594 | 0.2234 | 0.2084 | +0.0150 ± 0.0074 | 0.6354 | 0.5991 | 0.5951 | 0.398 | 0.463 | -0.083 ± 0.0191 | -0.01 (5) |
| 25-40 | 378 | 0.273 | 0.1976 | +0.0754 ± 0.0145 | 0.7647 | 0.5744 | 0.6719 | 0.3576 | 0.3968 | -0.139 ± 0.0227 | -0.025 (2) |
| 40+ | 140 | 0.3461 | 0.1924 | +0.1537 ± 0.0358 | 0.9729 | 0.5596 | 0.7547 | 0.277 | 0.3714 | -0.058 ± 0.0354 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1631 | 0.1821 | 0.1826 | -0.0005 ± 0.0004 | 0.5401 | 0.5409 | 0.494 | 0.4794 | 0.5046 | -0.030 ± 0.011 | -0.0217 (6) |
| 3-5 | 1034 | 0.1953 | 0.1948 | +0.0006 ± 0.0011 | 0.5658 | 0.5645 | 0.5161 | 0.4762 | 0.4884 | -0.038 ± 0.0139 | 0.02 (1) |
| 5-10 | 2242 | 0.188 | 0.1851 | +0.0029 ± 0.0014 | 0.5575 | 0.5465 | 0.5137 | 0.4399 | 0.459 | -0.045 ± 0.0092 | -0.01 (5) |
| 10-15 | 1960 | 0.1974 | 0.1825 | +0.0149 ± 0.0024 | 0.5809 | 0.5348 | 0.5228 | 0.3985 | 0.4036 | -0.066 ± 0.0098 | -0.02 (14) |
| 15-25 | 2794 | 0.2138 | 0.1759 | +0.0380 ± 0.0031 | 0.6231 | 0.5192 | 0.5345 | 0.3387 | 0.3432 | -0.073 ± 0.008 | -0.0026 (27) |
| 25-40 | 2440 | 0.2496 | 0.1371 | +0.1124 ± 0.0048 | 0.7087 | 0.4182 | 0.5627 | 0.2468 | 0.2287 | -0.089 ± 0.0075 | -0.015 (6) |
| 40+ | 1889 | 0.4025 | 0.0684 | +0.3341 ± 0.0069 | 1.0548 | 0.2385 | 0.6675 | 0.1304 | 0.1022 | -0.069 ± 0.0059 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 377 | 0.1949 | 0.1975 | -0.0026 ± 0.0008 | 0.5694 | 0.5762 | 0.4999 | 0.4849 | 0.5623 | -0.004 ± 0.0231 | -0.0133 (6) |
| 3-5 | 268 | 0.1872 | 0.1868 | +0.0004 ± 0.0021 | 0.5504 | 0.5494 | 0.5026 | 0.4632 | 0.4776 | -0.102 ± 0.0279 | -0.01 (1) |
| 5-10 | 552 | 0.1994 | 0.1986 | +0.0008 ± 0.0029 | 0.5853 | 0.5805 | 0.5089 | 0.4352 | 0.462 | -0.085 ± 0.0196 | -0.01 (4) |
| 10-15 | 422 | 0.2102 | 0.2119 | -0.0017 ± 0.0055 | 0.6087 | 0.6064 | 0.536 | 0.4135 | 0.4834 | -0.061 ± 0.0223 | -0.044 (5) |
| 15-25 | 497 | 0.2328 | 0.2083 | +0.0244 ± 0.008 | 0.6652 | 0.6012 | 0.5804 | 0.3873 | 0.4225 | -0.109 ± 0.0203 | -0.03 (1) |
| 25-40 | 292 | 0.2054 | 0.2107 | -0.0053 ± 0.0157 | 0.5966 | 0.6015 | 0.6544 | 0.3423 | 0.5034 | -0.044 ± 0.0234 | 0.0 (1) |
| 40+ | 57 | 0.3206 | 0.1777 | +0.1429 ± 0.0507 | 0.8629 | 0.5311 | 0.7518 | 0.2983 | 0.3684 | -0.143 ± 0.0517 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1773 | 0.1841 | 0.1851 | -0.0010 ± 0.0004 | 0.5439 | 0.5457 | 0.4879 | 0.4728 | 0.5048 | -0.023 ± 0.0103 | -0.0183 (23) |
| 3-5 | 1232 | 0.1855 | 0.1836 | +0.0019 ± 0.001 | 0.547 | 0.5421 | 0.4804 | 0.441 | 0.4359 | -0.070 ± 0.0126 | -0.0243 (7) |
| 5-10 | 2736 | 0.1921 | 0.1876 | +0.0046 ± 0.0012 | 0.5679 | 0.5521 | 0.4824 | 0.4086 | 0.4137 | -0.058 ± 0.0084 | -0.01 (18) |
| 10-15 | 2088 | 0.1954 | 0.1816 | +0.0138 ± 0.0023 | 0.5753 | 0.5321 | 0.4928 | 0.3697 | 0.375 | -0.064 ± 0.0093 | -0.03 (9) |
| 15-25 | 2713 | 0.2094 | 0.171 | +0.0384 ± 0.0031 | 0.6137 | 0.5066 | 0.5026 | 0.3073 | 0.3093 | -0.070 ± 0.008 | -0.03 (2) |
| 25-40 | 2078 | 0.2138 | 0.1215 | +0.0923 ± 0.0048 | 0.619 | 0.3754 | 0.5238 | 0.207 | 0.2233 | -0.058 ± 0.0072 | 0.0 (1) |
| 40+ | 1370 | 0.3852 | 0.0467 | +0.3385 ± 0.0065 | 1.0072 | 0.1818 | 0.6318 | 0.1095 | 0.0577 | -0.088 ± 0.0055 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 681 | 0.2028 | 0.2036 | -0.0008 ± 0.0006 | 0.5881 | 0.5897 | 0.4999 | 0.4849 | 0.5051 | -0.032 ± 0.0173 | -0.0226 (46) |
| 3-5 | 501 | 0.1978 | 0.1972 | +0.0007 ± 0.0016 | 0.5755 | 0.5721 | 0.4814 | 0.4417 | 0.4511 | -0.046 ± 0.0199 | -0.0058 (33) |
| 5-10 | 1027 | 0.1911 | 0.1855 | +0.0056 ± 0.002 | 0.566 | 0.5513 | 0.4798 | 0.4064 | 0.406 | -0.062 ± 0.0137 | -0.0049 (73) |
| 10-15 | 658 | 0.2035 | 0.1942 | +0.0093 ± 0.0043 | 0.5946 | 0.5699 | 0.4971 | 0.3741 | 0.3967 | -0.044 ± 0.0172 | 0.0014 (64) |
| 15-25 | 880 | 0.2357 | 0.2118 | +0.0239 ± 0.0061 | 0.6708 | 0.6094 | 0.5547 | 0.3606 | 0.3977 | -0.057 ± 0.0156 | -0.0216 (58) |
| 25-40 | 501 | 0.2543 | 0.1904 | +0.0638 ± 0.0122 | 0.716 | 0.5558 | 0.6413 | 0.3277 | 0.3812 | -0.090 ± 0.0183 | -0.0216 (25) |
| 40+ | 169 | 0.3622 | 0.1919 | +0.1704 ± 0.0345 | 1.0563 | 0.5644 | 0.7927 | 0.2986 | 0.3964 | -0.070 ± 0.0308 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2128 | 0.1917 | 0.192 | -0.0003 ± 0.0003 | 0.5594 | 0.559 | 0.5019 | 0.4865 | 0.5005 | -0.030 ± 0.0095 | -0.0155 (82) |
| 3-5 | 1470 | 0.1895 | 0.187 | +0.0025 ± 0.0009 | 0.5537 | 0.5476 | 0.487 | 0.4475 | 0.4367 | -0.057 ± 0.0113 | -0.0148 (63) |
| 5-10 | 2983 | 0.1898 | 0.1819 | +0.0079 ± 0.0012 | 0.5632 | 0.5409 | 0.4758 | 0.4022 | 0.3889 | -0.065 ± 0.0079 | -0.0087 (125) |
| 10-15 | 2018 | 0.1992 | 0.1859 | +0.0133 ± 0.0024 | 0.5847 | 0.5496 | 0.506 | 0.3829 | 0.3905 | -0.051 ± 0.0096 | -0.0053 (105) |
| 15-25 | 2552 | 0.231 | 0.1988 | +0.0322 ± 0.0035 | 0.6663 | 0.5772 | 0.5518 | 0.3569 | 0.3734 | -0.061 ± 0.0089 | -0.0255 (106) |
| 25-40 | 1726 | 0.254 | 0.1652 | +0.0888 ± 0.0062 | 0.721 | 0.4898 | 0.6036 | 0.2886 | 0.3076 | -0.080 ± 0.0095 | -0.0206 (47) |
| 40+ | 847 | 0.3864 | 0.1246 | +0.2618 ± 0.0131 | 1.0992 | 0.3843 | 0.7069 | 0.1979 | 0.209 | -0.074 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2465 | 1.06 ± 0.057 | 1.189 | 0.1687 | 0.1693 | 0.2106 | 0.2023 |
| gen2 | 2465 | 0.865 ± 0.05 | 1.129 | 0.1833 | 0.1689 | 0.2277 | 0.2021 |
| gen1_elo | 2465 | 1.046 ± 0.056 | 1.177 | 0.1728 | 0.1697 | 0.2095 | 0.2023 |
| gen1_sr | 2465 | 1.068 ± 0.065 | 1.213 | 0.1419 | 0.1709 | 0.2234 | 0.2018 |
| gen1_ledger | 4417 | 0.87 ± 0.037 | 1.081 | 0.1749 | 0.1873 | 0.2181 | 0.1969 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 12,194)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,196 | 26.2% |
| STALE_QUOTE | market_freshness | 2,410 | 19.8% |
| BOOK_QUALITY | execution | 2,216 | 18.2% |
| POOR_DATA | data | 1,285 | 10.5% |
| LIMITED_DATA | data | 940 | 7.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 682 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 598 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 401 | 3.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 361 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 105 | 0.9% |

Cause class: coverage 26.2%, market_freshness 19.8%, data 18.2%, execution 18.2%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.9%, mapping 3.3%, model_calibration 0.9%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.5%, START_UNVERIFIABLE 95.7%, LOW_DATA_QUALITY 67.8%, STALE_PLAYER_DATA 56.3%, THIN_PLAYER_HISTORY 56.3%, STALE_KALSHI_QUOTE 45.6%, MODEL_INTERNAL_DISAGREEMENT 38.1%, ASYMMETRIC_SAMPLE_SIZE 30.5%, WIDE_SPREAD 24.1%, MODEL_HIGH_UNCERTAINTY 16.5%, PLAYER_IDENTITY_RISK 12.0%, LEVEL_TRANSFER_RISK 9.0%, EVENT_MAPPING_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 1.5%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 28.7%, POST_SETTLEMENT_OBSERVATION 26.2%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,543)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,524 | 38.6% |
| BOOK_QUALITY | execution | 1,155 | 17.6% |
| STALE_QUOTE | market_freshness | 1,064 | 16.3% |
| POOR_DATA | data | 529 | 8.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 369 | 5.6% |
| LIMITED_DATA | data | 275 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 249 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 224 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 131 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 23 | 0.4% |

Cause class: coverage 38.6%, execution 17.6%, market_freshness 16.3%, data 12.3%, market_freshness/coverage 9.1%, mapping 3.8%, model_calibration_or_unknown 2.0%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.2%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 58.6%, STALE_KALSHI_QUOTE 53.8%, STALE_PLAYER_DATA 51.1%, MODEL_INTERNAL_DISAGREEMENT 39.3%, ASYMMETRIC_SAMPLE_SIZE 32.6%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 17.4%, PLAYER_IDENTITY_RISK 15.3%, EVENT_MAPPING_RISK 9.7%, LEVEL_TRANSFER_RISK 7.9%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.7%, EXTERNAL_MARKET_REJECTION 0.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 41.5%, POST_SETTLEMENT_OBSERVATION 38.6%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5376, "IDENTITY_AMBIGUOUS": 1167}; ticker orientation: {"VERIFIED": 6543}.

Checks: discipline:AMBIGUOUS 463, discipline:PASS 6080, identity_confidence:AMBIGUOUS 1001, identity_confidence:PASS 5542, level_mapping:NA 475, level_mapping:PASS 6068, market_pair:AMBIGUOUS 226, market_pair:NA 155, market_pair:PASS 6162, model_complement:NA 122, model_complement:PASS 6421, namesake:PASS 6543, physical_match_id:NA 2660, physical_match_id:PASS 3883, player_ids:PASS 6543, same_pair_other_event:PASS 6543, ticker_orientation:PASS 6543

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,006 | 1.5% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.28 | 0.2127 / 0.2136 (235) | 16.5% | 0.5% | 5.5% | 1.7% |
| CHALLENGER | 4,862 | 16.7% | 6.0% | 12.4% | {"coverage": 483, "market_freshness": 109, "market_freshness/coverage": 102, "data": 53, "model_calibration_or_unknown": 45, "execution": 12, "mapping": 6, "model_calibration": 4} | 7.23 | 0.2158 / 0.2026 (1166) | 38.2% | 8.4% | 2.3% | 21.5% |
| DOUBLES | 922 | 50.2% | 49.8% | 7.1% | {"execution": 178, "mapping": 141, "market_freshness": 106, "market_freshness/coverage": 31, "coverage": 7} | 24.68 | 0.3377 / 0.23 (256) | 25.4% | 0.0% | 100.0% | 7.4% |
| ITF_MEN | 8,708 | 23.6% | 15.5% | 31.5% | {"coverage": 850, "execution": 438, "market_freshness": 285, "data": 276, "market_freshness/coverage": 182, "mapping": 26, "model_calibration_or_unknown": 2} | 10.53 | 0.2119 / 0.1936 (2151) | 37.0% | 54.9% | 7.6% | 24.1% |
| ITF_WOMEN | 11,104 | 26.3% | 18.0% | 44.6% | {"coverage": 1167, "execution": 499, "market_freshness": 473, "data": 441, "market_freshness/coverage": 232, "mapping": 70, "model_calibration_or_unknown": 26, "model_calibration": 9} | 12.3 | 0.2049 / 0.1933 (2406) | 38.4% | 57.9% | 9.7% | 23.9% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,481 | 6.2% | 5.4% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 20, "data": 11, "market_freshness/coverage": 10, "execution": 6, "model_calibration": 4, "coverage": 4, "mapping": 1} | 7.78 | 0.2246 / 0.2196 (223) | 27.1% | 1.4% | 1.8% | 3.2% |
| WTA125 | 1,164 | 13.5% | 10.7% | 2.4% | {"model_calibration_or_unknown": 36, "market_freshness/coverage": 34, "market_freshness": 33, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 6, "mapping": 4} | 9.26 | 0.223 / 0.2145 (403) | 23.5% | 8.2% | 4.1% | 10.5% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 8 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 9 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 10 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 11 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 12 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 13 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 14 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 15 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 16 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 19 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 20 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 22 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 23 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 24 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 25 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 26 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 27 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 29 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 30 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 31 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 32 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 33 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 34 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 35 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 36 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 37 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 38 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 40 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 41 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 43 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 44 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 45 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 26 min (AGING); no external reference |
| 46 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 826 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 47 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 48 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 49 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 50 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.9h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 780 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9815, "by_level_share_of_ge_25pp": {"ATP": 0.0044, "CHALLENGER": 0.1244, "DOUBLES": 0.0708, "ITF_MEN": 0.3147, "ITF_WOMEN": 0.4458, "OTHER": 0.0018, "WTA": 0.0141, "WTA125": 0.024}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5377, "share_primary_cause_market_settled_or_in_play": 0.4764, "share_primary_cause_stale_quote_only": 0.1626}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6543, "identity_ambiguous_share": 0.1784, "ticker_orientation": {"VERIFIED": 6543}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3883, "with_external": 117, "coverage": 0.0301, "external_status": {"EXTERNAL_STALE": 82, "AGREES_WITH_KALSHI": 33, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 82, "MODEL_LONE_OUTLIER": 33, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2821, "share_external_supports_model": 0.0171}, "pregame_clean_ge_25pp": {"n": 1691, "with_external": 111, "coverage": 0.0656, "external_status": {"EXTERNAL_STALE": 78, "AGREES_WITH_KALSHI": 31, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 78, "MODEL_LONE_OUTLIER": 31, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2793, "share_external_supports_model": 0.018}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 608.0, "median_sample_ratio": 2.32, "median_min_matches": 21.0, "median_max_days_since_last": 198.0, "share_severe_asymmetry": 0.186, "data_status": {"POOR": 3374, "LIMITED": 1959, "ADEQUATE": 1210}, "comparison_lt_10pp": {"median_thinner_serve_points": 1893.0, "median_sample_ratio": 1.66, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 520, "model_minus_observed": 0.0561, "kalshi_minus_observed": -0.0752, "brier_diff_model_minus_kalshi": 0.0028}, "4-10x": {"n": 348, "model_minus_observed": 0.0634, "kalshi_minus_observed": -0.0769, "brier_diff_model_minus_kalshi": 0.0027}, "<2x": {"n": 1240, "model_minus_observed": 0.0799, "kalshi_minus_observed": -0.0415, "brier_diff_model_minus_kalshi": 0.0108}, ">=10x": {"n": 357, "model_minus_observed": 0.1111, "kalshi_minus_observed": -0.0571, "brier_diff_model_minus_kalshi": 0.0134}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2465, "model": {"intercept": -0.536, "slope": 0.865, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.23, "slope": 1.129, "slope_se": 0.058}, "mean_extremity_model": 0.1833, "mean_extremity_kalshi": 0.1689, "model_brier": 0.2277, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0256, "brier_diff_se": 0.0038, "model_logloss": 0.651, "kalshi_logloss": 0.5861}, "fair_v1": {"n": 2465, "model": {"intercept": -0.379, "slope": 1.06, "slope_se": 0.057}, "kalshi_mid_same_rows": {"intercept": 0.338, "slope": 1.189, "slope_se": 0.06}, "mean_extremity_model": 0.1687, "mean_extremity_kalshi": 0.1693, "model_brier": 0.2106, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.003, "model_logloss": 0.6085, "kalshi_logloss": 0.5864}, "gen1_elo": {"n": 2465, "model": {"intercept": -0.349, "slope": 1.046, "slope_se": 0.056}, "kalshi_mid_same_rows": {"intercept": 0.349, "slope": 1.177, "slope_se": 0.059}, "mean_extremity_model": 0.1728, "mean_extremity_kalshi": 0.1697, "model_brier": 0.2095, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.0072, "brier_diff_se": 0.003, "model_logloss": 0.607, "kalshi_logloss": 0.5864}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2397, "share_ge_15": 0.4265, "median_abs_gap": 12.69, "n": 16198}, "gen1_elo": {"share_ge_25": 0.2338, "share_ge_15": 0.4204, "median_abs_gap": 12.06, "n": 16198}, "gen1_sr": {"share_ge_25": 0.2933, "share_ge_15": 0.5098, "median_abs_gap": 15.38, "n": 16198}, "gen2": {"share_ge_25": 0.2978, "share_ge_15": 0.499, "median_abs_gap": 14.97, "n": 16198}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1372, "share_ge_15": 0.3289, "median_abs_gap": 10.22, "n": 12324}, "gen1_elo": {"share_ge_25": 0.1352, "share_ge_15": 0.3194, "median_abs_gap": 9.59, "n": 12323}, "gen1_sr": {"share_ge_25": 0.1908, "share_ge_15": 0.4218, "median_abs_gap": 12.55, "n": 12324}, "gen2": {"share_ge_25": 0.2092, "share_ge_15": 0.4243, "median_abs_gap": 12.5, "n": 12325}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.28, "share_ge_25_all": 0.0145, "share_ge_25_pregame_clean": 0.0142}, "WTA": {"median_abs_gap_pregame_clean": 7.78, "share_ge_25_all": 0.0621, "share_ge_25_pregame_clean": 0.0544}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2425, "share_within_10pp_all": 0.4448, "share_within_10pp_pregame_clean": 0.5064, "corr_model_vs_mid_pregame_clean": 0.8521}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 380, "model_brier": 0.1937, "kalshi_brier": 0.1951, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 439, "model_brier": 0.211, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0073}, "15-25": {"n_settled": 527, "model_brier": 0.2303, "kalshi_brier": 0.2163, "brier_diff_model_minus_kalshi": 0.014}, "25-40": {"n_settled": 284, "model_brier": 0.2207, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0186}, "3-5": {"n_settled": 254, "model_brier": 0.1893, "kalshi_brier": 0.1909, "brier_diff_model_minus_kalshi": -0.0016}, "40+": {"n_settled": 65, "model_brier": 0.2875, "kalshi_brier": 0.1787, "brier_diff_model_minus_kalshi": 0.1088}, "5-10": {"n_settled": 516, "model_brier": 0.1981, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": -0.0027}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.536, "slope": 0.865, "slope_se": 0.05}, "kalshi_slope": {"intercept": 0.23, "slope": 1.129, "slope_se": 0.058}, "n": 2465}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.511, "slope": 0.87, "slope_se": 0.037}, "kalshi_slope": {"intercept": 0.152, "slope": 1.081, "slope_se": 0.042}, "n": 4417}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 256, "model_brier": 0.3377, "kalshi_brier": 0.23, "brier_diff_model_minus_kalshi": 0.1077, "brier_diff_se": 0.0203, "corr_model_outcome": -0.035, "corr_kalshi_outcome": 0.2806}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
