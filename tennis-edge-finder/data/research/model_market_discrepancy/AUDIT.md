# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-19T14:59Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 41,066): 0-3 14.3%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 19.1%, 25-40 13.7%, 40+ 8.0%; median gap 11.89 pp.
* **Where the extremes live**: 97.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.2%, Challenger 12.7%, doubles 7.4%). Main tour: ATP 4.1% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,899): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.9%, BOOK_QUALITY 19.2%, STALE_QUOTE 17.8%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.7%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.6%. By class: coverage 34.9%, execution 19.2%, market_freshness 17.8%, data 12.5%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.6%.
* **Stale / settled / in-play**: 51.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,899 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 24.1% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 531.0 points vs 1808.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.054, Gen-2 0.839, Gen-1 ledger 0.88 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 425 model 0.2221 vs Kalshi 0.2099; n 85 model 0.3039 vs Kalshi 0.1748.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 174,604 model-market comparisons (283,471 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 61,568 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-19T14:52:26.976368+00:00'], shadow board 45,711 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-19T14:52:29.888558+00:00'], Model 4 21,453 rows, 16,675 settled tickers, 5,588 tickers with an external scan.
* By model: {"gen1_ledger": 41650, "gen1_elo": 22985, "fair_v1": 22985, "gen2": 22985, "gen1_sr": 22985, "model4_fundamental": 20516, "model4_conditioned": 20498}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 41,066 | 14.3 | 9.5 | 19.9 | 15.4 | 19.1 | 13.7 | 8.0 | 11.89 | 40.8% | 21.7% |
| MW fair_v1 | 22,985 | 13.4 | 8.6 | 18.4 | 16.0 | 19.5 | 14.5 | 9.6 | 12.95 | 43.5% | 24.0% |
| MW gen1_elo | 22,985 | 13.0 | 9.1 | 19.5 | 15.3 | 19.4 | 14.4 | 9.2 | 12.58 | 43.1% | 23.7% |
| MW gen1_ledger | 18,081 | 15.4 | 10.7 | 21.8 | 14.8 | 18.6 | 12.6 | 6.1 | 10.49 | 37.2% | 18.6% |
| MW gen1_sr | 22,985 | 9.9 | 7.4 | 16.8 | 14.2 | 21.4 | 18.4 | 11.8 | 15.56 | 51.6% | 30.2% |
| MW gen2 | 22,985 | 11.4 | 7.3 | 16.4 | 14.3 | 20.0 | 17.5 | 13.1 | 15.31 | 50.6% | 30.6% |
| all families model4_conditioned | 20,498 | 21.8 | 18.8 | 34.5 | 17.6 | 4.8 | 1.4 | 1.1 | 5.98 | 7.3% | 2.5% |
| all families model4_fundamental | 20,516 | 16.1 | 12.9 | 34.4 | 20.4 | 11.3 | 3.4 | 1.4 | 7.91 | 16.1% | 4.8% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.2%, >=15pp 40.8%, >=20pp 30.2%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.22pp; >=10pp 44.6%, >=25pp 16.8%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,013 | 29.2 | 13.1 | 24.8 | 16.4 | 11.7 | 4.2 | 0.6 | 6.37 | 16.5% | 4.8% |
| CHALLENGER | 3,893 | 15.2 | 10.3 | 20.1 | 16.2 | 14.8 | 12.3 | 11.0 | 11.39 | 38.1% | 23.3% |
| ITF_MEN | 6,049 | 10.9 | 7.8 | 17.2 | 14.9 | 20.2 | 16.5 | 12.5 | 14.69 | 49.2% | 29.0% |
| ITF_WOMEN | 8,959 | 10.1 | 6.9 | 15.8 | 15.6 | 22.7 | 18.1 | 10.9 | 15.56 | 51.7% | 29.0% |
| WTA | 1,411 | 18.2 | 12.3 | 24.7 | 19.5 | 20.3 | 4.2 | 0.8 | 8.45 | 25.3% | 5.0% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,013 | 23.6 | 15.3 | 23.9 | 17.5 | 14.1 | 4.7 | 0.9 | 6.85 | 19.7% | 5.6% |
| CHALLENGER | 3,893 | 14.7 | 8.1 | 18.8 | 14.2 | 18.0 | 14.2 | 12.1 | 12.84 | 44.2% | 26.2% |
| ITF_MEN | 6,049 | 9.4 | 6.6 | 15.6 | 13.4 | 19.7 | 19.5 | 15.8 | 17.19 | 55.1% | 35.4% |
| ITF_WOMEN | 8,959 | 8.3 | 5.5 | 13.7 | 13.6 | 21.3 | 20.8 | 16.7 | 18.87 | 58.8% | 37.5% |
| WTA | 1,411 | 15.4 | 9.1 | 20.2 | 16.4 | 23.5 | 14.6 | 0.8 | 11.5 | 38.9% | 15.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,013 | 23.9 | 13.8 | 25.5 | 16.5 | 14.4 | 5.2 | 0.8 | 7.02 | 20.4% | 6.0% |
| CHALLENGER | 3,893 | 14.4 | 9.9 | 21.1 | 15.2 | 15.9 | 12.3 | 11.3 | 11.3 | 39.5% | 23.6% |
| ITF_MEN | 6,049 | 9.9 | 8.0 | 17.7 | 14.2 | 20.9 | 16.9 | 12.5 | 15.06 | 50.3% | 29.4% |
| ITF_WOMEN | 8,959 | 9.6 | 6.9 | 16.3 | 15.8 | 22.9 | 18.4 | 10.1 | 15.52 | 51.4% | 28.5% |
| WTA | 1,411 | 24.4 | 17.1 | 30.1 | 15.2 | 10.3 | 2.3 | 0.5 | 6.0 | 13.1% | 2.8% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,176 | 27.2 | 20.3 | 30.7 | 11.3 | 7.6 | 2.6 | 0.3 | 5.26 | 10.5% | 2.9% |
| CHALLENGER | 2,712 | 21.7 | 14.7 | 27.2 | 13.8 | 14.5 | 6.2 | 1.8 | 7.13 | 22.6% | 8.1% |
| DOUBLES | 1,344 | 4.5 | 4.2 | 10.6 | 10.7 | 21.1 | 26.0 | 22.8 | 24.16 | 69.9% | 48.8% |
| ITF_MEN | 5,036 | 14.4 | 8.6 | 20.8 | 15.9 | 20.9 | 12.5 | 7.0 | 11.87 | 40.4% | 19.5% |
| ITF_WOMEN | 5,962 | 11.7 | 8.9 | 19.4 | 15.1 | 22.1 | 16.6 | 6.1 | 13.15 | 44.9% | 22.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 970 | 22.4 | 16.1 | 29.4 | 17.5 | 10.5 | 3.8 | 0.3 | 6.86 | 14.6% | 4.1% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,971 | 29.4 | 13.2 | 25.1 | 16.2 | 11.6 | 3.9 | 0.6 | 6.24 | 16.1% | 4.5% |
| CHALLENGER | 2,774 | 19.8 | 12.8 | 24.9 | 18.8 | 15.2 | 6.5 | 2.0 | 8.38 | 23.7% | 8.5% |
| ITF_MEN | 4,384 | 13.4 | 9.7 | 20.6 | 16.9 | 20.5 | 13.3 | 5.6 | 11.74 | 39.4% | 18.9% |
| ITF_WOMEN | 6,726 | 11.9 | 8.2 | 17.8 | 17.7 | 24.2 | 15.3 | 4.9 | 13.34 | 44.4% | 20.2% |
| WTA | 1,375 | 18.4 | 12.0 | 24.6 | 19.6 | 20.5 | 4.2 | 0.8 | 8.47 | 25.4% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,971 | 23.7 | 15.6 | 23.9 | 17.5 | 14.0 | 4.6 | 0.8 | 6.72 | 19.3% | 5.3% |
| CHALLENGER | 2,774 | 18.6 | 10.3 | 23.3 | 17.1 | 18.5 | 9.7 | 2.5 | 9.47 | 30.7% | 12.2% |
| ITF_MEN | 4,385 | 11.1 | 7.9 | 18.1 | 15.3 | 21.8 | 17.2 | 8.7 | 14.17 | 47.7% | 25.9% |
| ITF_WOMEN | 6,726 | 9.2 | 6.3 | 15.0 | 15.0 | 23.5 | 20.4 | 10.6 | 16.76 | 54.5% | 31.0% |
| WTA | 1,375 | 15.4 | 9.1 | 20.1 | 16.2 | 23.6 | 14.8 | 0.9 | 11.62 | 39.2% | 15.6% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,139 | 27.4 | 20.5 | 30.9 | 11.5 | 7.1 | 2.5 | 0.1 | 5.23 | 9.7% | 2.5% |
| CHALLENGER | 2,358 | 23.2 | 15.9 | 29.1 | 13.5 | 13.9 | 3.9 | 0.6 | 6.53 | 18.3% | 4.4% |
| DOUBLES | 1,248 | 4.6 | 4.3 | 10.7 | 10.9 | 21.1 | 26.2 | 22.2 | 24.07 | 69.5% | 48.4% |
| ITF_MEN | 4,167 | 15.7 | 9.4 | 22.7 | 16.8 | 20.7 | 10.6 | 4.2 | 10.62 | 35.4% | 14.8% |
| ITF_WOMEN | 4,951 | 12.4 | 9.5 | 21.0 | 15.9 | 22.3 | 15.3 | 3.5 | 11.9 | 41.2% | 18.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 924 | 22.8 | 16.6 | 29.4 | 17.5 | 10.6 | 3.0 | 0.0 | 6.79 | 13.6% | 3.0% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,344 | 4.5 | 4.2 | 10.6 | 10.7 | 21.1 | 26.0 | 22.8 | 24.16 | 69.9% | 48.8% |
| singles | 16,737 | 16.3 | 11.2 | 22.7 | 15.1 | 18.4 | 11.5 | 4.7 | 9.92 | 34.6% | 16.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,199 | 13.5 | 9.0 | 19.3 | 16.0 | 18.3 | 14.2 | 9.6 | 12.6 | 42.2% | 23.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 14,797 | 13.8 | 8.6 | 18.5 | 15.5 | 19.8 | 14.3 | 9.5 | 12.96 | 43.6% | 23.8% |
| UNKNOWN | 2,752 | 11.3 | 7.8 | 16.7 | 18.5 | 20.0 | 15.9 | 9.8 | 13.38 | 45.7% | 25.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,773 | 19.8 | 11.1 | 21.3 | 17.3 | 16.0 | 8.7 | 5.9 | 9.34 | 30.6% | 14.6% |
| B | 2,984 | 12.9 | 9.2 | 19.9 | 17.2 | 18.5 | 11.7 | 10.5 | 12.06 | 40.8% | 22.2% |
| C | 3,284 | 12.8 | 9.2 | 19.1 | 14.9 | 19.3 | 14.9 | 9.8 | 12.84 | 44.0% | 24.7% |
| D | 3,851 | 12.3 | 8.1 | 17.0 | 15.7 | 22.0 | 15.4 | 9.5 | 13.94 | 46.9% | 24.9% |
| F | 6,093 | 7.7 | 5.6 | 15.1 | 14.7 | 22.4 | 21.4 | 13.1 | 17.84 | 56.9% | 34.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,306 | 23.3 | 16.0 | 28.7 | 15.0 | 11.6 | 4.0 | 1.4 | 6.61 | 17.0% | 5.5% |
| B | 2,554 | 15.4 | 10.0 | 24.2 | 16.5 | 19.2 | 10.8 | 4.0 | 10.06 | 34.0% | 14.8% |
| C | 3,637 | 11.1 | 7.5 | 18.1 | 14.2 | 21.8 | 16.4 | 11.0 | 14.54 | 49.2% | 27.4% |
| D | 2,642 | 13.8 | 9.8 | 20.5 | 14.0 | 21.0 | 14.5 | 6.4 | 12.05 | 42.0% | 20.9% |
| F | 3,942 | 10.1 | 7.7 | 15.4 | 14.4 | 23.1 | 20.4 | 8.9 | 16.11 | 52.4% | 29.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,695 | 18.0 | 10.1 | 20.7 | 17.2 | 16.4 | 9.4 | 8.3 | 10.37 | 34.1% | 17.7% |
| LIMITED | 5,141 | 14.4 | 10.3 | 20.1 | 15.6 | 18.9 | 13.3 | 7.3 | 11.57 | 39.5% | 20.6% |
| POOR | 10,149 | 9.5 | 6.6 | 15.9 | 15.2 | 22.2 | 18.9 | 11.6 | 15.95 | 52.8% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,528 | 26.7 | 21.4 | 34.8 | 11.4 | 4.1 | 1.3 | 0.2 | 5.14 | 5.6% | 1.5% |
| GAME_SPREAD | 4,010 | 23.6 | 15.4 | 33.8 | 17.3 | 7.6 | 2.1 | 0.3 | 6.44 | 10.0% | 2.4% |
| MATCH_WINNER | 18,081 | 15.4 | 10.7 | 21.8 | 14.8 | 18.6 | 12.6 | 6.1 | 10.49 | 37.2% | 18.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,497 | 30.4 | 17.4 | 30.2 | 12.3 | 8.1 | 1.2 | 0.4 | 5.27 | 9.7% | 1.7% |
| TOTAL_GAMES | 6,510 | 7.3 | 8.8 | 37.1 | 29.2 | 11.1 | 3.5 | 3.0 | 9.65 | 17.6% | 6.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,179 | 25.2 | 34.3 | 32.5 | 3.9 | 3.4 | 0.6 | 0.2 | 4.48 | 4.2% | 0.8% |
| GAME_SPREAD | 4,901 | 46.1 | 16.8 | 27.2 | 7.2 | 1.8 | 0.6 | 0.3 | 3.4 | 2.6% | 0.9% |
| TOTAL_GAMES | 8,418 | 4.6 | 6.9 | 40.5 | 35.4 | 7.7 | 2.6 | 2.4 | 9.81 | 12.6% | 5.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,182 | 24.2 | 17.6 | 36.0 | 11.9 | 7.3 | 2.5 | 0.3 | 5.84 | 10.2% | 2.9% |
| GAME_SPREAD | 4,904 | 19.4 | 13.4 | 28.4 | 20.0 | 13.9 | 3.9 | 1.0 | 7.91 | 18.7% | 4.8% |
| TOTAL_GAMES | 8,430 | 7.4 | 8.5 | 36.6 | 27.9 | 13.2 | 3.9 | 2.5 | 9.71 | 19.6% | 6.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 22,985 | 43.5% | 24.0% | 12.95 | 35.1% | 15.0% | 10.77 |
| gen1_elo | 22,985 | 43.1% | 23.7% | 12.58 | 34.3% | 15.0% | 10.32 |
| gen1_sr | 22,985 | 51.6% | 30.2% | 15.56 | 44.0% | 21.1% | 13.02 |
| gen2 | 22,985 | 50.6% | 30.6% | 15.31 | 44.0% | 22.7% | 13.01 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 12,288 | 16.1 | 10.4 | 21.3 | 17.6 | 19.9 | 11.4 | 3.2 | 10.59 | 34.6% | 14.6% |
| STALE | 10,697 | 10.3 | 6.5 | 15.2 | 14.1 | 19.0 | 18.0 | 16.8 | 17.02 | 53.9% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 11,549 | 16.8 | 11.4 | 23.0 | 14.8 | 17.5 | 11.7 | 4.8 | 9.7 | 34.1% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 41,066 | 11549 | 15760 | 13757 | 23.7 | 136.3 | 1400.4 |
| ge_15pp | 16,745 | 3936 | 5537 | 7272 | 25.8 | 438.1 | 1380.4 |
| ge_25pp | 8,899 | 1911 | 2390 | 4598 | 32.3 | 575.6 | 1380.4 |
| lt_10pp | 17,980 | 5906 | 7515 | 4559 | 21.7 | 47.9 | 1341.5 |

Current slate `SL-20261019T145939Z-7623eebe`: 450 priced rows, quote age at build {'median': 7.5, 'max': 7.5}, freshness {'FRESH': 450}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,128 | 20.8 | 10.9 | 23.6 | 19.0 | 18.7 | 6.6 | 0.5 | 8.77 | 25.8% | 7.1% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 375 | 68.8 | 31.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.1 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 804 | 0.0 | 2.7 | 35.1 | 28.6 | 23.5 | 9.4 | 0.6 | 12.01 | 33.6% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 22,985 | 3341 (14.5%) | 24.1% | 0.6% | {"EXTERNAL_STALE": 2128, "AGREES_WITH_KALSHI": 804, "ALL_AGREE": 375, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 10,010 | 827 (8.3%) | 32.6% | 1.1% | {"EXTERNAL_STALE": 548, "AGREES_WITH_KALSHI": 270, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,526 | 235 (4.2%) | 34.5% | 1.3% | {"EXTERNAL_STALE": 151, "AGREES_WITH_KALSHI": 81, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,673 | 223 (8.3%) | 35.4% | 1.4% | {"EXTERNAL_STALE": 141, "AGREES_WITH_KALSHI": 79, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 9,305 | 1880 (20.2%) | 16.2% | 0.6% | {"EXTERNAL_STALE": 1176, "ALL_AGREE": 375, "AGREES_WITH_KALSHI": 304, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,414 | 10.9 | 7.9 | 19.4 | 15.1 | 21.8 | 15.2 | 9.8 | 13.81 | 46.8% | 25.0% |
| 4-10x | 3,004 | 12.0 | 8.8 | 18.9 | 16.0 | 19.5 | 15.1 | 9.8 | 13.05 | 44.3% | 24.8% |
| <2x | 11,940 | 15.5 | 9.5 | 19.0 | 17.0 | 18.0 | 12.5 | 8.5 | 11.7 | 39.1% | 21.1% |
| >=10x | 3,627 | 10.8 | 6.4 | 15.2 | 13.7 | 21.8 | 19.7 | 12.4 | 16.44 | 53.8% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,895 | 12.8 | 8.6 | 19.4 | 16.3 | 19.8 | 13.1 | 10.0 | 12.8 | 43.0% | 23.1% |
| 300-1000 | 5,088 | 12.1 | 8.8 | 16.9 | 15.8 | 20.8 | 16.0 | 9.6 | 13.75 | 46.3% | 25.6% |
| <300 | 6,937 | 8.9 | 5.9 | 15.5 | 14.9 | 22.1 | 20.1 | 12.5 | 16.82 | 54.8% | 32.7% |
| >=3000 | 5,065 | 21.7 | 12.1 | 22.8 | 17.2 | 14.4 | 6.8 | 4.9 | 8.11 | 26.1% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 691 | 0.543 | 0.4082 | 0.4935 | +0.050 | -0.085 | -0.0009 ± 0.0057 |
| ratio 4-10x | 474 | 0.5921 | 0.4496 | 0.5127 | +0.080 | -0.063 | 0.0084 ± 0.0073 |
| ratio <2x | 1705 | 0.5382 | 0.4174 | 0.4499 | +0.088 | -0.033 | 0.0126 ± 0.0034 |
| ratio >=10x | 579 | 0.5616 | 0.3888 | 0.4473 | +0.114 | -0.059 | 0.0115 ± 0.0076 |
| thinner_sample 1000-3000 | 952 | 0.5432 | 0.4174 | 0.4611 | +0.082 | -0.044 | 0.0081 ± 0.0046 |
| thinner_sample 300-1000 | 822 | 0.5669 | 0.4258 | 0.4976 | +0.069 | -0.072 | 0.0004 ± 0.0055 |
| thinner_sample <300 | 1082 | 0.5546 | 0.392 | 0.4519 | +0.103 | -0.060 | 0.0137 ± 0.0053 |
| thinner_sample >=3000 | 593 | 0.5321 | 0.4392 | 0.4604 | +0.072 | -0.021 | 0.0146 ± 0.0047 |
| data_status ADEQUATE | 1006 | 0.534 | 0.4299 | 0.4543 | +0.080 | -0.024 | 0.0116 ± 0.0039 |
| data_status LIMITED | 849 | 0.5546 | 0.4239 | 0.49 | +0.065 | -0.066 | 0.0031 ± 0.005 |
| data_status POOR | 1594 | 0.5588 | 0.4012 | 0.4624 | +0.096 | -0.061 | 0.0108 ± 0.0043 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 524 | 0.1956 | 0.197 | -0.0013 ± 0.0007 | 0.5698 | 0.5726 | 0.4956 | 0.4808 | 0.5324 | -0.048 ± 0.0203 | -0.01 (5) |
| 3-5 | 330 | 0.1979 | 0.197 | +0.0010 ± 0.002 | 0.5779 | 0.5742 | 0.5057 | 0.4657 | 0.4727 | -0.091 ± 0.0251 | 0.02 (1) |
| 5-10 | 718 | 0.1995 | 0.1993 | +0.0002 ± 0.0025 | 0.5846 | 0.5822 | 0.5126 | 0.4382 | 0.4694 | -0.085 ± 0.0173 | -0.0167 (6) |
| 10-15 | 613 | 0.215 | 0.2058 | +0.0092 ± 0.0046 | 0.6198 | 0.5939 | 0.5259 | 0.4018 | 0.4258 | -0.096 ± 0.0183 | -0.048 (5) |
| 15-25 | 754 | 0.2268 | 0.2135 | +0.0133 ± 0.0066 | 0.6474 | 0.6121 | 0.5813 | 0.3863 | 0.4496 | -0.088 ± 0.0167 | -0.0033 (9) |
| 25-40 | 425 | 0.2221 | 0.2099 | +0.0122 ± 0.0132 | 0.6324 | 0.6028 | 0.657 | 0.3487 | 0.4824 | -0.071 ± 0.0201 | -0.01 (1) |
| 40+ | 85 | 0.3039 | 0.1748 | +0.1291 ± 0.0409 | 0.8278 | 0.523 | 0.7553 | 0.3058 | 0.3882 | -0.129 ± 0.0396 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2502 | 0.181 | 0.1823 | -0.0013 ± 0.0003 | 0.5371 | 0.5385 | 0.4797 | 0.4646 | 0.5048 | -0.017 ± 0.0086 | -0.0129 (17) |
| 3-5 | 1580 | 0.1946 | 0.1922 | +0.0023 ± 0.0009 | 0.5698 | 0.5604 | 0.4788 | 0.439 | 0.4278 | -0.069 ± 0.0112 | 0.0 (2) |
| 5-10 | 3420 | 0.1944 | 0.1912 | +0.0032 ± 0.0011 | 0.571 | 0.5609 | 0.4841 | 0.4104 | 0.4237 | -0.051 ± 0.0076 | -0.0119 (21) |
| 10-15 | 3013 | 0.2032 | 0.185 | +0.0182 ± 0.002 | 0.5939 | 0.543 | 0.487 | 0.3624 | 0.3521 | -0.075 ± 0.0078 | -0.0281 (16) |
| 15-25 | 3662 | 0.2092 | 0.1728 | +0.0364 ± 0.0027 | 0.6098 | 0.5099 | 0.5039 | 0.3078 | 0.3143 | -0.068 ± 0.0068 | -0.0025 (44) |
| 25-40 | 2823 | 0.222 | 0.1268 | +0.0952 ± 0.0042 | 0.6384 | 0.3903 | 0.533 | 0.22 | 0.2281 | -0.067 ± 0.0065 | -0.01 (1) |
| 40+ | 1888 | 0.3796 | 0.0431 | +0.3365 ± 0.0054 | 0.9883 | 0.1704 | 0.6297 | 0.1068 | 0.0572 | -0.087 ± 0.0045 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 392 | 0.1998 | 0.2004 | -0.0005 ± 0.0008 | 0.5815 | 0.5827 | 0.5026 | 0.4875 | 0.5102 | -0.084 ± 0.024 | -0.01 (3) |
| 3-5 | 285 | 0.2158 | 0.2153 | +0.0005 ± 0.0022 | 0.615 | 0.6147 | 0.516 | 0.4761 | 0.4842 | -0.090 ± 0.0293 | 0.02 (1) |
| 5-10 | 616 | 0.1987 | 0.199 | -0.0003 ± 0.0027 | 0.5807 | 0.5811 | 0.5451 | 0.4702 | 0.5097 | -0.071 ± 0.0185 | -0.01 (4) |
| 10-15 | 571 | 0.2174 | 0.2109 | +0.0065 ± 0.0048 | 0.625 | 0.6081 | 0.5681 | 0.4437 | 0.4834 | -0.094 ± 0.0199 | -0.04 (5) |
| 15-25 | 828 | 0.2307 | 0.2097 | +0.0210 ± 0.0063 | 0.6533 | 0.6021 | 0.5916 | 0.3954 | 0.4444 | -0.097 ± 0.0162 | -0.0133 (9) |
| 25-40 | 554 | 0.2664 | 0.1983 | +0.0681 ± 0.0119 | 0.7425 | 0.5776 | 0.6656 | 0.3503 | 0.4007 | -0.123 ± 0.0186 | -0.0075 (4) |
| 40+ | 203 | 0.3681 | 0.1765 | +0.1917 ± 0.0292 | 1.0238 | 0.5241 | 0.7455 | 0.2633 | 0.3202 | -0.084 ± 0.0285 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2120 | 0.1849 | 0.1854 | -0.0005 ± 0.0003 | 0.546 | 0.5469 | 0.5017 | 0.4869 | 0.5085 | -0.035 ± 0.0097 | -0.0133 (15) |
| 3-5 | 1351 | 0.196 | 0.1952 | +0.0008 ± 0.001 | 0.5682 | 0.5662 | 0.5157 | 0.4758 | 0.4848 | -0.045 ± 0.0123 | 0.02 (1) |
| 5-10 | 3036 | 0.1914 | 0.1894 | +0.0020 ± 0.0012 | 0.565 | 0.5569 | 0.5071 | 0.433 | 0.4582 | -0.037 ± 0.008 | -0.0117 (6) |
| 10-15 | 2657 | 0.1999 | 0.189 | +0.0109 ± 0.0021 | 0.5882 | 0.5505 | 0.5206 | 0.396 | 0.4166 | -0.051 ± 0.0086 | -0.0189 (18) |
| 15-25 | 3788 | 0.2181 | 0.1802 | +0.0379 ± 0.0027 | 0.6311 | 0.5292 | 0.5317 | 0.3355 | 0.3408 | -0.071 ± 0.007 | -0.0086 (42) |
| 25-40 | 3338 | 0.2512 | 0.137 | +0.1142 ± 0.0041 | 0.7088 | 0.4202 | 0.5637 | 0.2475 | 0.2265 | -0.092 ± 0.0064 | -0.0044 (18) |
| 40+ | 2598 | 0.4022 | 0.0655 | +0.3367 ± 0.0058 | 1.0614 | 0.2293 | 0.663 | 0.1259 | 0.0943 | -0.072 ± 0.0049 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 506 | 0.198 | 0.2006 | -0.0026 ± 0.0007 | 0.5768 | 0.5829 | 0.4976 | 0.4823 | 0.5573 | -0.011 ± 0.0202 | -0.0137 (8) |
| 3-5 | 370 | 0.1937 | 0.1913 | +0.0024 ± 0.0018 | 0.5649 | 0.5593 | 0.4996 | 0.46 | 0.4514 | -0.121 ± 0.0238 | 0.0067 (3) |
| 5-10 | 747 | 0.2014 | 0.1979 | +0.0035 ± 0.0025 | 0.5897 | 0.5781 | 0.5078 | 0.434 | 0.4444 | -0.098 ± 0.0168 | -0.0071 (7) |
| 10-15 | 598 | 0.2091 | 0.2062 | +0.0028 ± 0.0046 | 0.6059 | 0.5956 | 0.5416 | 0.4185 | 0.4716 | -0.076 ± 0.0183 | -0.0317 (6) |
| 15-25 | 706 | 0.2344 | 0.211 | +0.0234 ± 0.0067 | 0.6676 | 0.606 | 0.5898 | 0.3967 | 0.432 | -0.116 ± 0.0172 | -0.03 (1) |
| 25-40 | 436 | 0.2059 | 0.215 | -0.0091 ± 0.0128 | 0.5965 | 0.6143 | 0.6633 | 0.3536 | 0.5206 | -0.044 ± 0.0195 | 0.015 (2) |
| 40+ | 86 | 0.3215 | 0.1911 | +0.1304 ± 0.0424 | 0.8738 | 0.5597 | 0.7597 | 0.3072 | 0.3953 | -0.116 ± 0.0444 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2393 | 0.1878 | 0.1888 | -0.0010 ± 0.0003 | 0.5525 | 0.5544 | 0.4886 | 0.4733 | 0.501 | -0.027 ± 0.0089 | -0.0163 (35) |
| 3-5 | 1664 | 0.1897 | 0.1864 | +0.0033 ± 0.0009 | 0.5574 | 0.5495 | 0.4796 | 0.44 | 0.4195 | -0.083 ± 0.0109 | -0.0094 (18) |
| 5-10 | 3638 | 0.1955 | 0.1891 | +0.0065 ± 0.0011 | 0.5755 | 0.5546 | 0.4833 | 0.4095 | 0.4005 | -0.069 ± 0.0073 | -0.01 (31) |
| 10-15 | 2818 | 0.1975 | 0.1808 | +0.0167 ± 0.002 | 0.5801 | 0.5315 | 0.5009 | 0.3774 | 0.3722 | -0.073 ± 0.0079 | -0.015 (12) |
| 15-25 | 3771 | 0.2094 | 0.1717 | +0.0378 ± 0.0026 | 0.612 | 0.5077 | 0.5091 | 0.3145 | 0.3153 | -0.072 ± 0.0068 | -0.03 (2) |
| 25-40 | 2783 | 0.2163 | 0.1253 | +0.0909 ± 0.0042 | 0.6252 | 0.3854 | 0.5308 | 0.2152 | 0.2325 | -0.061 ± 0.0064 | 0.01 (3) |
| 40+ | 1821 | 0.3944 | 0.0479 | +0.3465 ± 0.0058 | 1.0298 | 0.1832 | 0.641 | 0.1121 | 0.061 | -0.089 ± 0.0049 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 849 | 0.1967 | 0.1968 | -0.0002 ± 0.0005 | 0.5738 | 0.574 | 0.5069 | 0.4919 | 0.4959 | -0.055 ± 0.0154 | -0.0224 (49) |
| 3-5 | 601 | 0.1941 | 0.1935 | +0.0006 ± 0.0015 | 0.5666 | 0.564 | 0.4831 | 0.4433 | 0.4526 | -0.053 ± 0.0181 | -0.0194 (34) |
| 5-10 | 1260 | 0.1989 | 0.1926 | +0.0063 ± 0.0019 | 0.5855 | 0.5671 | 0.4907 | 0.4173 | 0.4119 | -0.069 ± 0.0126 | -0.005 (78) |
| 10-15 | 809 | 0.2089 | 0.1971 | +0.0118 ± 0.0039 | 0.6059 | 0.576 | 0.5129 | 0.3898 | 0.4017 | -0.066 ± 0.0158 | 0.0014 (64) |
| 15-25 | 1078 | 0.2329 | 0.2123 | +0.0207 ± 0.0055 | 0.6636 | 0.6108 | 0.5713 | 0.3763 | 0.4221 | -0.063 ± 0.0141 | -0.0214 (59) |
| 25-40 | 644 | 0.2467 | 0.2006 | +0.0461 ± 0.0108 | 0.6992 | 0.5801 | 0.6588 | 0.3464 | 0.427 | -0.084 ± 0.0164 | -0.0219 (26) |
| 40+ | 223 | 0.3519 | 0.195 | +0.1569 ± 0.0296 | 1.0186 | 0.5712 | 0.8042 | 0.3172 | 0.4215 | -0.080 ± 0.0262 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2653 | 0.1875 | 0.1876 | -0.0001 ± 0.0003 | 0.55 | 0.5493 | 0.5051 | 0.4898 | 0.4979 | -0.038 ± 0.0084 | -0.0157 (88) |
| 3-5 | 1834 | 0.1912 | 0.1886 | +0.0026 ± 0.0008 | 0.559 | 0.5529 | 0.4889 | 0.4493 | 0.4368 | -0.061 ± 0.0102 | -0.0209 (69) |
| 5-10 | 3676 | 0.1957 | 0.1869 | +0.0088 ± 0.0011 | 0.5764 | 0.552 | 0.4887 | 0.4152 | 0.395 | -0.072 ± 0.0072 | -0.0082 (132) |
| 10-15 | 2514 | 0.2042 | 0.1893 | +0.0149 ± 0.0022 | 0.5954 | 0.5569 | 0.5185 | 0.3955 | 0.3954 | -0.061 ± 0.0087 | -0.0053 (105) |
| 15-25 | 3133 | 0.2288 | 0.1984 | +0.0304 ± 0.0031 | 0.6588 | 0.5768 | 0.5641 | 0.3687 | 0.39 | -0.063 ± 0.008 | -0.0253 (107) |
| 25-40 | 2146 | 0.2529 | 0.1745 | +0.0784 ± 0.0057 | 0.7173 | 0.5132 | 0.6189 | 0.3052 | 0.3406 | -0.076 ± 0.0087 | -0.0229 (51) |
| 40+ | 1012 | 0.3772 | 0.1363 | +0.2409 ± 0.0123 | 1.0716 | 0.4141 | 0.7212 | 0.2171 | 0.2441 | -0.073 ± 0.0108 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3449 | 1.054 ± 0.048 | 1.182 | 0.1679 | 0.1648 | 0.2129 | 0.2037 |
| gen2 | 3449 | 0.839 ± 0.044 | 1.142 | 0.1735 | 0.1651 | 0.2319 | 0.2036 |
| gen1_elo | 3449 | 1.036 ± 0.047 | 1.166 | 0.1737 | 0.1652 | 0.2117 | 0.2037 |
| gen1_sr | 3449 | 1.041 ± 0.057 | 1.214 | 0.1337 | 0.1668 | 0.2278 | 0.2033 |
| gen1_ledger | 5464 | 0.88 ± 0.033 | 1.085 | 0.1787 | 0.1806 | 0.2181 | 0.199 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 16,745)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,934 | 23.5% |
| STALE_QUOTE | market_freshness | 3,418 | 20.4% |
| BOOK_QUALITY | execution | 3,284 | 19.6% |
| POOR_DATA | data | 1,852 | 11.1% |
| LIMITED_DATA | data | 1,138 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 888 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 834 | 5.0% |
| IDENTITY_AMBIGUOUS | mapping | 676 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 475 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 246 | 1.5% |

Cause class: coverage 23.5%, market_freshness 20.4%, execution 19.6%, data 17.9%, market_freshness/coverage 8.1%, model_calibration_or_unknown 5.0%, mapping 4.0%, model_calibration 1.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.4%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 69.8%, THIN_PLAYER_HISTORY 58.1%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 43.4%, MODEL_INTERNAL_DISAGREEMENT 40.6%, ASYMMETRIC_SAMPLE_SIZE 32.4%, WIDE_SPREAD 25.6%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 15.1%, LEVEL_TRANSFER_RISK 9.4%, EVENT_MAPPING_RISK 8.5%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.5%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.9%, POST_SETTLEMENT_OBSERVATION 23.5%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,899)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,107 | 34.9% |
| BOOK_QUALITY | execution | 1,711 | 19.2% |
| STALE_QUOTE | market_freshness | 1,583 | 17.8% |
| POOR_DATA | data | 780 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 472 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 386 | 4.3% |
| LIMITED_DATA | data | 333 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 294 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 181 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 52 | 0.6% |

Cause class: coverage 34.9%, execution 19.2%, market_freshness 17.8%, data 12.5%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.6%, START_UNVERIFIABLE 97.3%, LOW_DATA_QUALITY 73.9%, THIN_PLAYER_HISTORY 60.9%, STALE_KALSHI_QUOTE 51.7%, STALE_PLAYER_DATA 47.2%, MODEL_INTERNAL_DISAGREEMENT 41.3%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 25.3%, PLAYER_IDENTITY_RISK 18.4%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 10.3%, LEVEL_TRANSFER_RISK 8.3%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.4%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.8%, POST_SETTLEMENT_OBSERVATION 34.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7029, "IDENTITY_AMBIGUOUS": 1870}; ticker orientation: {"VERIFIED": 8899}.

Checks: discipline:AMBIGUOUS 656, discipline:PASS 8243, identity_confidence:AMBIGUOUS 1639, identity_confidence:PASS 7260, level_mapping:NA 668, level_mapping:PASS 8231, market_pair:AMBIGUOUS 321, market_pair:NA 217, market_pair:PASS 8361, model_complement:NA 184, model_complement:PASS 8715, namesake:PASS 8899, physical_match_id:NA 3373, physical_match_id:PASS 5526, player_ids:PASS 8899, same_pair_other_event:PASS 8899, ticker_orientation:PASS 8899

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,189 | 4.1% | 3.8% | 1.5% | {"market_freshness": 43, "data": 29, "model_calibration_or_unknown": 19, "execution": 17, "market_freshness/coverage": 10, "model_calibration": 10, "coverage": 2} | 5.84 | 0.2185 / 0.2103 (347) | 18.2% | 3.5% | 3.9% | 2.5% |
| CHALLENGER | 6,605 | 17.1% | 6.6% | 12.7% | {"coverage": 646, "market_freshness/coverage": 140, "market_freshness": 134, "data": 101, "model_calibration_or_unknown": 53, "execution": 26, "mapping": 14, "model_calibration": 12} | 7.35 | 0.2167 / 0.206 (1622) | 35.4% | 15.9% | 3.6% | 22.3% |
| DOUBLES | 1,344 | 48.8% | 48.4% | 7.4% | {"execution": 325, "mapping": 173, "market_freshness": 106, "market_freshness/coverage": 45, "coverage": 7} | 24.07 | 0.322 / 0.2343 (346) | 17.4% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 11,085 | 24.7% | 16.9% | 30.8% | {"coverage": 1071, "execution": 558, "market_freshness": 422, "data": 362, "market_freshness/coverage": 222, "mapping": 99, "model_calibration_or_unknown": 2} | 11.23 | 0.2151 / 0.1953 (2682) | 36.3% | 62.5% | 14.0% | 22.9% |
| ITF_WOMEN | 14,921 | 26.5% | 19.6% | 44.4% | {"coverage": 1364, "market_freshness": 802, "execution": 755, "data": 587, "market_freshness/coverage": 300, "mapping": 94, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.83 | 0.2018 / 0.1937 (3001) | 38.0% | 58.0% | 10.3% | 21.7% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,381 | 4.6% | 4.2% | 1.2% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 16, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.78 | 0.2385 / 0.2317 (385) | 23.5% | 1.4% | 1.5% | 3.4% |
| WTA125 | 1,392 | 12.5% | 9.9% | 2.0% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 9 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 10 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 11 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 12 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 13 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 14 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 15 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 16 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 17 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 18 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 19 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 20 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 23 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 24 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 25 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 26 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 28 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 29 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 30 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 31 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 32 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 34 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 35 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 36 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 37 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 38 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 39 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 730 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 40 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 41 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 42 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 44 | `KXITFWMATCH-26OCT19VLABOU-VLA` | ITF_WOMEN | fair_v1 | 77% / 2% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 140 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 3.13); no external reference |
| 45 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 47 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 48 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 49 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 50 | `KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF` | DOUBLES | gen1_ledger | 90% / 15% | +75 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.973, "by_level_share_of_ge_25pp": {"ATP": 0.0146, "CHALLENGER": 0.1265, "DOUBLES": 0.0737, "ITF_MEN": 0.3075, "ITF_WOMEN": 0.4444, "OTHER": 0.0013, "WTA": 0.0124, "WTA125": 0.0196}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5167, "share_primary_cause_market_settled_or_in_play": 0.4351, "share_primary_cause_stale_quote_only": 0.1779}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8899, "identity_ambiguous_share": 0.2101, "ticker_orientation": {"VERIFIED": 8899}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5526, "with_external": 235, "coverage": 0.0425, "external_status": {"EXTERNAL_STALE": 151, "AGREES_WITH_KALSHI": 81, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 151, "MODEL_LONE_OUTLIER": 81, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3447, "share_external_supports_model": 0.0128}, "pregame_clean_ge_25pp": {"n": 2673, "with_external": 223, "coverage": 0.0834, "external_status": {"EXTERNAL_STALE": 141, "AGREES_WITH_KALSHI": 79, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 141, "MODEL_LONE_OUTLIER": 79, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3543, "share_external_supports_model": 0.0135}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 531.0, "median_sample_ratio": 2.46, "median_min_matches": 21.0, "median_max_days_since_last": 218.0, "share_severe_asymmetry": 0.2081, "data_status": {"POOR": 4830, "LIMITED": 2509, "ADEQUATE": 1560}, "comparison_lt_10pp": {"median_thinner_serve_points": 1808.0, "median_sample_ratio": 1.67, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 691, "model_minus_observed": 0.0495, "kalshi_minus_observed": -0.0853, "brier_diff_model_minus_kalshi": -0.0009}, "4-10x": {"n": 474, "model_minus_observed": 0.0795, "kalshi_minus_observed": -0.063, "brier_diff_model_minus_kalshi": 0.0084}, "<2x": {"n": 1705, "model_minus_observed": 0.0884, "kalshi_minus_observed": -0.0325, "brier_diff_model_minus_kalshi": 0.0126}, ">=10x": {"n": 579, "model_minus_observed": 0.1142, "kalshi_minus_observed": -0.0585, "brier_diff_model_minus_kalshi": 0.0115}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3449, "model": {"intercept": -0.528, "slope": 0.839, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.237, "slope": 1.142, "slope_se": 0.051}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.1651, "model_brier": 0.2319, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0282, "brier_diff_se": 0.0032, "model_logloss": 0.6605, "kalshi_logloss": 0.5897}, "fair_v1": {"n": 3449, "model": {"intercept": -0.404, "slope": 1.054, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.314, "slope": 1.182, "slope_se": 0.051}, "mean_extremity_model": 0.1679, "mean_extremity_kalshi": 0.1648, "model_brier": 0.2129, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0092, "brier_diff_se": 0.0026, "model_logloss": 0.6136, "kalshi_logloss": 0.5897}, "gen1_elo": {"n": 3449, "model": {"intercept": -0.393, "slope": 1.036, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.31, "slope": 1.166, "slope_se": 0.05}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1652, "model_brier": 0.2117, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0026, "model_logloss": 0.6118, "kalshi_logloss": 0.5896}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2404, "share_ge_15": 0.4355, "median_abs_gap": 12.95, "n": 22985}, "gen1_elo": {"share_ge_25": 0.237, "share_ge_15": 0.4312, "median_abs_gap": 12.58, "n": 22985}, "gen1_sr": {"share_ge_25": 0.3019, "share_ge_15": 0.5164, "median_abs_gap": 15.56, "n": 22985}, "gen2": {"share_ge_25": 0.306, "share_ge_15": 0.5057, "median_abs_gap": 15.31, "n": 22985}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1496, "share_ge_15": 0.3506, "median_abs_gap": 10.77, "n": 17864}, "gen1_elo": {"share_ge_25": 0.1497, "share_ge_15": 0.3427, "median_abs_gap": 10.32, "n": 17862}, "gen1_sr": {"share_ge_25": 0.2105, "share_ge_15": 0.4398, "median_abs_gap": 13.02, "n": 17864}, "gen2": {"share_ge_25": 0.2269, "share_ge_15": 0.4404, "median_abs_gap": 13.01, "n": 17865}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0408, "share_ge_25_pregame_clean": 0.0379}, "WTA": {"median_abs_gap_pregame_clean": 7.78, "share_ge_25_all": 0.0462, "share_ge_25_pregame_clean": 0.0418}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2385, "share_within_10pp_all": 0.4378, "share_within_10pp_pregame_clean": 0.4913, "corr_model_vs_mid_pregame_clean": 0.8423}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 524, "model_brier": 0.1956, "kalshi_brier": 0.197, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 613, "model_brier": 0.215, "kalshi_brier": 0.2058, "brier_diff_model_minus_kalshi": 0.0092}, "15-25": {"n_settled": 754, "model_brier": 0.2268, "kalshi_brier": 0.2135, "brier_diff_model_minus_kalshi": 0.0133}, "25-40": {"n_settled": 425, "model_brier": 0.2221, "kalshi_brier": 0.2099, "brier_diff_model_minus_kalshi": 0.0122}, "3-5": {"n_settled": 330, "model_brier": 0.1979, "kalshi_brier": 0.197, "brier_diff_model_minus_kalshi": 0.001}, "40+": {"n_settled": 85, "model_brier": 0.3039, "kalshi_brier": 0.1748, "brier_diff_model_minus_kalshi": 0.1291}, "5-10": {"n_settled": 718, "model_brier": 0.1995, "kalshi_brier": 0.1993, "brier_diff_model_minus_kalshi": 0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.528, "slope": 0.839, "slope_se": 0.044}, "kalshi_slope": {"intercept": 0.237, "slope": 1.142, "slope_se": 0.051}, "n": 3449}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.516, "slope": 0.88, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.151, "slope": 1.085, "slope_se": 0.038}, "n": 5464}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 346, "model_brier": 0.322, "kalshi_brier": 0.2343, "brier_diff_model_minus_kalshi": 0.0878, "brier_diff_se": 0.0169, "corr_model_outcome": 0.0119, "corr_kalshi_outcome": 0.2598}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
