# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-10T13:07Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 27,489): 0-3 14.5%, 3-5 9.7%, 5-10 20.0%, 10-15 15.4%, 15-25 18.4%, 25-40 13.7%, 40+ 8.3%; median gap 11.83 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 11.9%, doubles 7.2%). Main tour: ATP 1.5% and WTA 7.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,064): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.7%, BOOK_QUALITY 16.6%, STALE_QUOTE 16.5%, POOR_DATA 8.0%, POSSIBLY_IN_PLAY_QUOTE 5.5%, LIMITED_DATA 4.3%, IDENTITY_AMBIGUOUS 3.7%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.3%. By class: coverage 39.7%, execution 16.6%, market_freshness 16.5%, data 12.3%, market_freshness/coverage 9.0%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.3%.
* **Stale / settled / in-play**: 55.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,064 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 18.6% of the time and with the model 0.2%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 647.0 points vs 1888.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.057, Gen-2 0.854, Gen-1 ledger 0.883 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 255 model 0.2211 vs Kalshi 0.2012; n 56 model 0.2885 vs Kalshi 0.1688.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 108,445 model-market comparisons (178,709 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 40,782 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-10T12:59:28.849945+00:00'], shadow board 28,827 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-10T12:59:32.739912+00:00'], Model 4 12,049 rows, 12,135 settled tickers, 3,275 tickers with an external scan.
* By model: {"gen1_ledger": 26708, "gen1_elo": 14484, "fair_v1": 14484, "gen2": 14484, "gen1_sr": 14484, "model4_fundamental": 11905, "model4_conditioned": 11896}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 27,489 | 14.5 | 9.7 | 20.0 | 15.4 | 18.4 | 13.7 | 8.3 | 11.83 | 40.5% | 22.1% |
| MW fair_v1 | 14,484 | 13.7 | 8.7 | 18.4 | 16.2 | 18.3 | 14.6 | 10.0 | 12.8 | 42.9% | 24.6% |
| MW gen1_elo | 14,484 | 13.2 | 9.1 | 20.1 | 15.0 | 18.8 | 14.4 | 9.4 | 12.29 | 42.6% | 23.8% |
| MW gen1_ledger | 13,005 | 15.3 | 10.8 | 21.7 | 14.5 | 18.6 | 12.8 | 6.5 | 10.61 | 37.8% | 19.2% |
| MW gen1_sr | 14,484 | 10.2 | 7.9 | 16.4 | 14.4 | 21.4 | 18.2 | 11.7 | 15.43 | 51.2% | 29.8% |
| MW gen2 | 14,484 | 12.2 | 7.2 | 16.2 | 14.3 | 19.9 | 17.1 | 13.1 | 15.02 | 50.1% | 30.2% |
| all families model4_conditioned | 11,896 | 22.2 | 20.2 | 36.0 | 15.8 | 4.1 | 0.8 | 0.9 | 5.71 | 5.8% | 1.7% |
| all families model4_fundamental | 11,905 | 16.8 | 13.4 | 35.9 | 19.7 | 10.6 | 2.4 | 1.2 | 7.54 | 14.2% | 3.6% |

Configurable thresholds (primary): >=5pp 75.9%, >=10pp 55.9%, >=15pp 40.5%, >=20pp 30.3%, >=25pp 22.1%, >=30pp 16.2%, >=40pp 8.3%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.45pp; >=10pp 45.4%, >=25pp 17.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,183 | 30.1 | 14.3 | 25.3 | 16.9 | 11.3 | 1.2 | 0.9 | 5.88 | 13.4% | 2.1% |
| CHALLENGER | 2,371 | 15.9 | 10.8 | 18.6 | 16.2 | 12.8 | 12.9 | 12.7 | 11.75 | 38.4% | 25.6% |
| ITF_MEN | 4,150 | 11.6 | 8.8 | 18.4 | 14.9 | 19.1 | 15.1 | 12.1 | 13.59 | 46.3% | 27.1% |
| ITF_WOMEN | 5,790 | 10.2 | 6.6 | 15.9 | 16.5 | 21.7 | 18.6 | 10.6 | 15.37 | 50.8% | 29.1% |
| WTA | 635 | 22.4 | 10.6 | 25.7 | 16.2 | 16.9 | 6.6 | 1.7 | 7.89 | 25.2% | 8.3% |
| WTA125 | 355 | 11.6 | 5.9 | 23.1 | 25.1 | 16.6 | 15.5 | 2.2 | 11.33 | 34.4% | 17.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,183 | 24.3 | 13.8 | 24.9 | 18.7 | 15.3 | 1.9 | 1.1 | 6.9 | 18.3% | 3.0% |
| CHALLENGER | 2,371 | 15.4 | 7.6 | 18.2 | 13.3 | 18.1 | 14.1 | 13.2 | 13.06 | 45.4% | 27.3% |
| ITF_MEN | 4,150 | 10.4 | 7.5 | 16.9 | 15.0 | 19.8 | 17.5 | 12.8 | 15.19 | 50.1% | 30.3% |
| ITF_WOMEN | 5,790 | 9.1 | 5.9 | 12.8 | 12.8 | 21.2 | 21.0 | 17.2 | 19.08 | 59.4% | 38.1% |
| WTA | 635 | 20.9 | 6.6 | 18.3 | 15.1 | 21.1 | 16.2 | 1.7 | 12.12 | 39.1% | 17.9% |
| WTA125 | 355 | 4.2 | 2.8 | 18.3 | 20.6 | 22.8 | 20.6 | 10.7 | 17.24 | 54.1% | 31.3% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,183 | 26.5 | 14.5 | 29.0 | 15.2 | 11.0 | 2.7 | 1.0 | 6.29 | 14.7% | 3.7% |
| CHALLENGER | 2,371 | 15.9 | 10.7 | 20.4 | 14.7 | 13.8 | 12.1 | 12.6 | 10.67 | 38.4% | 24.7% |
| ITF_MEN | 4,150 | 10.4 | 8.9 | 19.2 | 13.8 | 20.1 | 15.4 | 12.2 | 13.94 | 47.7% | 27.6% |
| ITF_WOMEN | 5,790 | 9.9 | 6.7 | 16.7 | 15.7 | 22.9 | 18.8 | 9.4 | 15.5 | 51.1% | 28.2% |
| WTA | 635 | 22.4 | 13.9 | 34.8 | 15.9 | 9.0 | 3.0 | 1.1 | 6.68 | 13.1% | 4.1% |
| WTA125 | 355 | 22.8 | 11.8 | 30.7 | 16.3 | 13.2 | 4.5 | 0.6 | 7.73 | 18.3% | 5.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 647 | 30.3 | 23.8 | 35.1 | 9.0 | 1.4 | 0.5 | 0.0 | 4.69 | 1.8% | 0.5% |
| CHALLENGER | 1,553 | 23.7 | 17.4 | 26.4 | 13.5 | 11.7 | 5.3 | 1.9 | 6.43 | 18.9% | 7.2% |
| DOUBLES | 854 | 4.0 | 3.2 | 10.3 | 11.4 | 19.8 | 25.2 | 26.2 | 25.8 | 71.2% | 51.4% |
| ITF_MEN | 4,010 | 15.1 | 8.6 | 21.1 | 15.3 | 20.2 | 12.2 | 7.6 | 11.68 | 39.9% | 19.8% |
| ITF_WOMEN | 4,746 | 11.7 | 9.3 | 19.8 | 14.6 | 22.5 | 16.6 | 5.5 | 12.98 | 44.6% | 22.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 521 | 21.7 | 13.6 | 25.9 | 17.7 | 14.4 | 6.1 | 0.6 | 7.96 | 21.1% | 6.7% |
| WTA125 | 525 | 16.9 | 13.9 | 22.5 | 19.8 | 15.8 | 8.4 | 2.7 | 9.01 | 26.9% | 11.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,173 | 30.0 | 14.2 | 25.4 | 17.0 | 11.3 | 1.2 | 0.9 | 5.93 | 13.5% | 2.1% |
| CHALLENGER | 1,673 | 21.0 | 13.9 | 23.7 | 19.1 | 13.1 | 6.4 | 2.7 | 7.94 | 22.2% | 9.1% |
| ITF_MEN | 2,933 | 14.4 | 11.2 | 22.1 | 16.6 | 19.0 | 11.8 | 5.0 | 10.62 | 35.7% | 16.8% |
| ITF_WOMEN | 4,103 | 12.7 | 8.4 | 18.7 | 19.2 | 23.2 | 14.6 | 3.2 | 12.62 | 41.1% | 17.9% |
| WTA | 630 | 22.2 | 10.6 | 25.9 | 16.2 | 16.8 | 6.5 | 1.8 | 7.87 | 25.1% | 8.2% |
| WTA125 | 340 | 12.1 | 6.2 | 22.1 | 25.6 | 17.1 | 15.6 | 1.5 | 11.4 | 34.1% | 17.1% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,173 | 24.1 | 13.8 | 25.0 | 18.7 | 15.3 | 2.0 | 1.1 | 6.9 | 18.4% | 3.1% |
| CHALLENGER | 1,673 | 20.3 | 10.0 | 23.0 | 16.2 | 18.6 | 9.3 | 2.6 | 9.0 | 30.5% | 11.9% |
| ITF_MEN | 2,934 | 12.5 | 9.2 | 19.7 | 16.8 | 21.4 | 14.6 | 5.8 | 12.43 | 41.8% | 20.4% |
| ITF_WOMEN | 4,103 | 10.7 | 7.1 | 14.6 | 14.0 | 23.8 | 19.7 | 10.1 | 16.26 | 53.6% | 29.8% |
| WTA | 630 | 20.9 | 6.7 | 18.2 | 15.2 | 20.9 | 16.2 | 1.8 | 12.12 | 38.9% | 17.9% |
| WTA125 | 340 | 4.4 | 2.9 | 18.2 | 21.2 | 22.4 | 21.2 | 9.7 | 16.84 | 53.2% | 30.9% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 627 | 30.3 | 24.1 | 35.4 | 9.1 | 0.6 | 0.5 | 0.0 | 4.64 | 1.1% | 0.5% |
| CHALLENGER | 1,318 | 25.8 | 19.6 | 28.7 | 13.1 | 10.8 | 2.0 | 0.1 | 5.69 | 12.8% | 2.1% |
| DOUBLES | 787 | 3.9 | 3.2 | 10.6 | 11.4 | 19.9 | 25.0 | 25.9 | 25.63 | 70.9% | 50.9% |
| ITF_MEN | 3,228 | 16.8 | 9.5 | 23.4 | 16.3 | 19.9 | 9.7 | 4.3 | 10.04 | 33.9% | 14.1% |
| ITF_WOMEN | 3,870 | 12.9 | 10.1 | 21.7 | 15.4 | 22.7 | 14.9 | 2.3 | 11.5 | 39.9% | 17.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 491 | 22.2 | 14.3 | 26.5 | 17.7 | 14.7 | 4.7 | 0.0 | 7.91 | 19.4% | 4.7% |
| WTA125 | 438 | 18.9 | 15.5 | 24.4 | 22.6 | 13.9 | 4.3 | 0.2 | 7.89 | 18.5% | 4.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 854 | 4.0 | 3.2 | 10.3 | 11.4 | 19.8 | 25.2 | 26.2 | 25.8 | 71.2% | 51.4% |
| singles | 12,151 | 16.1 | 11.3 | 22.5 | 14.7 | 18.5 | 11.9 | 5.1 | 10.03 | 35.4% | 17.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,303 | 13.7 | 9.7 | 20.1 | 16.1 | 16.1 | 14.1 | 10.3 | 12.04 | 40.5% | 24.4% |
| Hard | 9,737 | 14.1 | 8.4 | 18.3 | 16.0 | 18.8 | 14.5 | 9.8 | 12.83 | 43.2% | 24.4% |
| UNKNOWN | 1,444 | 11.4 | 8.4 | 15.6 | 17.9 | 20.1 | 16.6 | 10.0 | 14.01 | 46.8% | 26.6% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,402 | 20.1 | 10.6 | 20.9 | 17.2 | 14.6 | 9.2 | 7.5 | 9.52 | 31.2% | 16.7% |
| B | 1,939 | 15.0 | 9.5 | 19.1 | 17.2 | 16.8 | 12.2 | 10.3 | 11.5 | 39.2% | 22.5% |
| C | 2,216 | 12.4 | 9.8 | 19.4 | 15.2 | 18.8 | 14.9 | 9.4 | 12.71 | 43.1% | 24.3% |
| D | 2,692 | 10.8 | 8.5 | 17.5 | 16.3 | 22.1 | 15.0 | 9.9 | 13.98 | 47.0% | 24.9% |
| F | 3,235 | 7.7 | 5.1 | 14.8 | 15.0 | 20.8 | 22.9 | 13.6 | 18.39 | 57.4% | 36.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,755 | 22.6 | 16.3 | 28.0 | 15.0 | 11.5 | 4.8 | 1.8 | 6.73 | 18.2% | 6.6% |
| B | 2,033 | 14.9 | 9.8 | 24.1 | 16.2 | 19.0 | 11.5 | 4.5 | 10.34 | 34.9% | 15.9% |
| C | 2,662 | 11.8 | 7.7 | 17.8 | 14.3 | 20.9 | 15.9 | 11.6 | 14.17 | 48.4% | 27.5% |
| D | 2,116 | 14.1 | 9.3 | 21.4 | 13.1 | 21.9 | 14.0 | 6.1 | 12.04 | 42.1% | 20.2% |
| F | 2,439 | 9.1 | 7.7 | 14.4 | 13.7 | 23.5 | 21.6 | 10.0 | 16.91 | 55.1% | 31.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,915 | 18.6 | 9.8 | 19.9 | 17.0 | 14.9 | 10.0 | 9.8 | 10.48 | 34.7% | 19.8% |
| LIMITED | 3,601 | 14.8 | 10.6 | 20.5 | 16.2 | 17.8 | 13.2 | 7.1 | 11.28 | 38.0% | 20.3% |
| POOR | 5,968 | 9.2 | 6.7 | 15.9 | 15.6 | 21.4 | 19.2 | 11.9 | 16.04 | 52.6% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,672 | 30.7 | 24.7 | 36.6 | 5.6 | 1.8 | 0.6 | 0.1 | 4.56 | 2.5% | 0.6% |
| GAME_SPREAD | 2,588 | 25.0 | 15.7 | 36.9 | 17.2 | 4.6 | 0.4 | 0.2 | 6.12 | 5.2% | 0.6% |
| MATCH_WINNER | 13,005 | 15.3 | 10.8 | 21.7 | 14.5 | 18.6 | 12.8 | 6.5 | 10.61 | 37.8% | 19.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 4,658 | 33.0 | 19.7 | 30.4 | 9.7 | 5.7 | 1.2 | 0.3 | 4.76 | 7.2% | 1.5% |
| TOTAL_GAMES | 3,761 | 7.1 | 9.2 | 38.7 | 30.3 | 9.7 | 2.6 | 2.5 | 9.45 | 14.7% | 5.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,367 | 25.3 | 37.8 | 31.7 | 0.3 | 4.3 | 0.5 | 0.1 | 4.33 | 4.9% | 0.6% |
| GAME_SPREAD | 3,085 | 44.7 | 15.0 | 30.1 | 7.9 | 1.2 | 0.8 | 0.4 | 3.65 | 2.3% | 1.1% |
| TOTAL_GAMES | 4,444 | 3.4 | 6.6 | 44.4 | 36.6 | 5.8 | 1.1 | 2.0 | 9.57 | 9.0% | 3.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,367 | 25.6 | 18.7 | 36.8 | 9.5 | 6.7 | 2.3 | 0.3 | 5.55 | 9.4% | 2.7% |
| GAME_SPREAD | 3,085 | 19.0 | 13.0 | 29.9 | 20.9 | 14.1 | 2.5 | 0.8 | 7.94 | 17.3% | 3.2% |
| TOTAL_GAMES | 4,453 | 6.7 | 8.6 | 39.1 | 28.8 | 12.0 | 2.5 | 2.2 | 9.51 | 16.8% | 4.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 14,484 | 42.9% | 24.6% | 12.8 | 32.6% | 13.9% | 10.21 |
| gen1_elo | 14,484 | 42.6% | 23.8% | 12.29 | 31.9% | 13.5% | 9.6 |
| gen1_sr | 14,484 | 51.2% | 29.8% | 15.43 | 41.9% | 19.1% | 12.55 |
| gen2 | 14,484 | 50.1% | 30.2% | 15.02 | 42.2% | 20.9% | 12.44 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 7,449 | 16.8 | 11.0 | 21.5 | 17.7 | 18.4 | 11.2 | 3.3 | 10.16 | 32.9% | 14.5% |
| STALE | 7,035 | 10.5 | 6.2 | 15.1 | 14.7 | 18.2 | 18.2 | 17.0 | 16.97 | 53.5% | 35.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 6,473 | 17.4 | 12.0 | 23.6 | 14.3 | 16.6 | 11.4 | 4.7 | 9.21 | 32.7% | 16.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 27,489 | 6473 | 10921 | 10095 | 24.8 | 159.1 | 1400.4 |
| ge_15pp | 11,128 | 2115 | 3742 | 5271 | 28.4 | 457.3 | 1380.4 |
| ge_25pp | 6,064 | 1040 | 1675 | 3349 | 36.4 | 577.3 | 1380.4 |
| lt_10pp | 12,123 | 3435 | 5309 | 3379 | 23.1 | 49.5 | 1341.5 |

Current slate `SL-20261010T130658Z-e834a542`: 288 priced rows, quote age at build {'median': 7.8, 'max': 7.8}, freshness {'FRESH': 288}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 4 | 0.0 | 0.0 | 25.0 | 0.0 | 75.0 | 0.0 | 0.0 | 20.45 | 75.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 4 | 25.0 | 75.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.22 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 872 | 23.7 | 11.6 | 21.9 | 19.6 | 16.3 | 6.5 | 0.3 | 7.99 | 23.2% | 6.9% |
| MARKETS_AGREE | 156 | 75.6 | 24.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.94 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 237 | 0.0 | 3.8 | 35.9 | 33.8 | 17.3 | 8.9 | 0.4 | 11.28 | 26.6% | 9.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 14,484 | 1273 (8.8%) | 18.6% | 0.2% | {"EXTERNAL_STALE": 872, "AGREES_WITH_KALSHI": 237, "ALL_AGREE": 156, "EXTERNAL_OUTLIER": 4, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 6,214 | 268 (4.3%) | 23.5% | 1.1% | {"EXTERNAL_STALE": 202, "AGREES_WITH_KALSHI": 63, "SUPPORTS_MODEL_DIRECTION": 3} |
| fair_v1_ge_25pp | 3,562 | 82 (2.3%) | 26.8% | 0.0% | {"EXTERNAL_STALE": 60, "AGREES_WITH_KALSHI": 22} |
| fair_v1_ge_25pp_pregame_clean | 1,512 | 80 (5.3%) | 27.5% | 0.0% | {"EXTERNAL_STALE": 58, "AGREES_WITH_KALSHI": 22} |
| fair_v1_lt_10pp | 5,919 | 754 (12.7%) | 12.5% | 0.0% | {"EXTERNAL_STALE": 499, "ALL_AGREE": 156, "AGREES_WITH_KALSHI": 94, "EXTERNAL_OUTLIER": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,928 | 11.7 | 8.4 | 19.6 | 15.4 | 20.7 | 14.0 | 10.2 | 13.14 | 44.9% | 24.2% |
| 4-10x | 2,004 | 11.2 | 9.2 | 18.5 | 15.3 | 20.0 | 16.5 | 9.4 | 13.56 | 45.8% | 25.9% |
| <2x | 7,774 | 15.8 | 9.2 | 18.6 | 17.2 | 16.6 | 13.0 | 9.5 | 11.84 | 39.2% | 22.5% |
| >=10x | 1,778 | 11.0 | 6.4 | 15.6 | 14.3 | 19.9 | 20.4 | 12.4 | 16.3 | 52.8% | 32.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,794 | 14.0 | 8.5 | 19.2 | 15.9 | 18.1 | 13.1 | 11.1 | 12.44 | 42.3% | 24.1% |
| 300-1000 | 3,535 | 11.7 | 9.1 | 16.7 | 16.2 | 20.9 | 16.1 | 9.2 | 13.75 | 46.2% | 25.3% |
| <300 | 3,733 | 8.3 | 6.0 | 15.6 | 15.1 | 20.9 | 21.0 | 13.1 | 17.15 | 55.0% | 34.1% |
| >=3000 | 3,422 | 21.4 | 11.5 | 22.3 | 17.8 | 12.9 | 7.9 | 6.2 | 8.5 | 27.0% | 14.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 464 | 0.5363 | 0.4044 | 0.4763 | +0.060 | -0.072 | 0.0035 ± 0.0068 |
| ratio 4-10x | 321 | 0.5808 | 0.4395 | 0.5234 | +0.058 | -0.084 | -0.0006 ± 0.0087 |
| ratio <2x | 1061 | 0.5406 | 0.4185 | 0.4533 | +0.087 | -0.035 | 0.0129 ± 0.0044 |
| ratio >=10x | 304 | 0.5489 | 0.3812 | 0.4375 | +0.111 | -0.056 | 0.0162 ± 0.01 |
| thinner_sample 1000-3000 | 594 | 0.5427 | 0.4189 | 0.463 | +0.080 | -0.044 | 0.0079 ± 0.0059 |
| thinner_sample 300-1000 | 576 | 0.5651 | 0.4245 | 0.4913 | +0.074 | -0.067 | 0.0021 ± 0.0065 |
| thinner_sample <300 | 615 | 0.5429 | 0.3834 | 0.4585 | +0.084 | -0.075 | 0.0114 ± 0.0068 |
| thinner_sample >=3000 | 365 | 0.5312 | 0.437 | 0.4466 | +0.085 | -0.009 | 0.0196 ± 0.0059 |
| data_status ADEQUATE | 592 | 0.5308 | 0.4288 | 0.4426 | +0.088 | -0.014 | 0.0147 ± 0.005 |
| data_status LIMITED | 578 | 0.5562 | 0.4244 | 0.4844 | +0.072 | -0.060 | 0.0035 ± 0.0063 |
| data_status POOR | 980 | 0.551 | 0.3974 | 0.4704 | +0.081 | -0.073 | 0.0096 ± 0.0053 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 331 | 0.1934 | 0.1949 | -0.0014 ± 0.0008 | 0.5648 | 0.5684 | 0.4905 | 0.4758 | 0.5227 | -0.053 ± 0.0254 | -0.01 (3) |
| 3-5 | 221 | 0.1891 | 0.1909 | -0.0018 ± 0.0023 | 0.5584 | 0.5606 | 0.5111 | 0.4713 | 0.5113 | -0.052 ± 0.0298 | 0.02 (1) |
| 5-10 | 443 | 0.201 | 0.2024 | -0.0014 ± 0.0032 | 0.5878 | 0.5909 | 0.5226 | 0.4485 | 0.4876 | -0.081 ± 0.0222 | -0.0125 (4) |
| 10-15 | 392 | 0.2129 | 0.2047 | +0.0082 ± 0.0057 | 0.6131 | 0.5903 | 0.5167 | 0.393 | 0.4184 | -0.096 ± 0.0228 | -0.0633 (3) |
| 15-25 | 452 | 0.2286 | 0.214 | +0.0145 ± 0.0085 | 0.6527 | 0.6159 | 0.5743 | 0.3786 | 0.4381 | -0.087 ± 0.0217 | -0.0133 (6) |
| 25-40 | 255 | 0.2211 | 0.2012 | +0.0199 ± 0.0167 | 0.6322 | 0.5778 | 0.6463 | 0.3382 | 0.4588 | -0.072 ± 0.025 | -0.01 (1) |
| 40+ | 56 | 0.2885 | 0.1688 | +0.1197 ± 0.0489 | 0.7814 | 0.5101 | 0.7479 | 0.3017 | 0.3929 | -0.129 ± 0.0475 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1655 | 0.1728 | 0.1738 | -0.0010 ± 0.0004 | 0.5166 | 0.5178 | 0.4737 | 0.459 | 0.4967 | -0.020 ± 0.0104 | -0.0188 (8) |
| 3-5 | 1051 | 0.1925 | 0.1897 | +0.0028 ± 0.0011 | 0.5666 | 0.5548 | 0.4795 | 0.4399 | 0.4206 | -0.077 ± 0.0137 | 0.02 (1) |
| 5-10 | 2253 | 0.1954 | 0.1929 | +0.0025 ± 0.0014 | 0.5737 | 0.5657 | 0.4892 | 0.4154 | 0.4328 | -0.050 ± 0.0094 | -0.0082 (17) |
| 10-15 | 2040 | 0.2007 | 0.1823 | +0.0184 ± 0.0024 | 0.5867 | 0.5357 | 0.4732 | 0.3488 | 0.3373 | -0.078 ± 0.0094 | -0.0475 (4) |
| 15-25 | 2328 | 0.204 | 0.1655 | +0.0386 ± 0.0033 | 0.6002 | 0.4921 | 0.4921 | 0.2957 | 0.2964 | -0.073 ± 0.0084 | -0.0048 (29) |
| 25-40 | 1943 | 0.2181 | 0.123 | +0.0952 ± 0.005 | 0.629 | 0.3804 | 0.5263 | 0.2128 | 0.2208 | -0.060 ± 0.0077 | -0.01 (1) |
| 40+ | 1331 | 0.3719 | 0.0439 | +0.3280 ± 0.0064 | 0.969 | 0.1742 | 0.6224 | 0.1055 | 0.0571 | -0.084 ± 0.0054 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 255 | 0.1954 | 0.1959 | -0.0004 ± 0.001 | 0.5733 | 0.5747 | 0.493 | 0.4781 | 0.4902 | -0.086 ± 0.0292 | -0.01 (1) |
| 3-5 | 170 | 0.2098 | 0.2104 | -0.0006 ± 0.0029 | 0.6008 | 0.6041 | 0.5226 | 0.4825 | 0.5059 | -0.061 ± 0.0368 | 0.02 (1) |
| 5-10 | 380 | 0.1957 | 0.193 | +0.0028 ± 0.0034 | 0.5738 | 0.5674 | 0.562 | 0.4871 | 0.5053 | -0.087 ± 0.0233 | -0.01 (4) |
| 10-15 | 365 | 0.2154 | 0.2067 | +0.0086 ± 0.006 | 0.6173 | 0.5996 | 0.5775 | 0.4527 | 0.4849 | -0.098 ± 0.0246 | -0.05 (4) |
| 15-25 | 518 | 0.2272 | 0.2082 | +0.0190 ± 0.0079 | 0.644 | 0.5989 | 0.5983 | 0.401 | 0.4575 | -0.090 ± 0.0205 | -0.01 (5) |
| 25-40 | 337 | 0.2761 | 0.2024 | +0.0736 ± 0.0155 | 0.7741 | 0.5851 | 0.6728 | 0.3586 | 0.4006 | -0.136 ± 0.0245 | -0.025 (2) |
| 40+ | 125 | 0.3433 | 0.189 | +0.1542 ± 0.0376 | 0.9623 | 0.5532 | 0.7606 | 0.2826 | 0.376 | -0.063 ± 0.0363 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1468 | 0.1767 | 0.1771 | -0.0004 ± 0.0004 | 0.5261 | 0.5273 | 0.4907 | 0.4762 | 0.502 | -0.029 ± 0.0114 | -0.0217 (6) |
| 3-5 | 895 | 0.1937 | 0.1925 | +0.0012 ± 0.0012 | 0.5618 | 0.5593 | 0.5236 | 0.4837 | 0.4883 | -0.047 ± 0.0149 | 0.02 (1) |
| 5-10 | 1998 | 0.1863 | 0.1829 | +0.0035 ± 0.0014 | 0.554 | 0.5416 | 0.5146 | 0.4411 | 0.458 | -0.046 ± 0.0097 | -0.01 (5) |
| 10-15 | 1762 | 0.196 | 0.1807 | +0.0153 ± 0.0025 | 0.5783 | 0.5301 | 0.518 | 0.3935 | 0.3973 | -0.068 ± 0.0103 | -0.02 (14) |
| 15-25 | 2483 | 0.2162 | 0.1746 | +0.0416 ± 0.0033 | 0.6283 | 0.516 | 0.5309 | 0.3355 | 0.3302 | -0.080 ± 0.0085 | -0.0026 (27) |
| 25-40 | 2241 | 0.2504 | 0.1377 | +0.1127 ± 0.005 | 0.7119 | 0.419 | 0.5623 | 0.246 | 0.2276 | -0.089 ± 0.0079 | -0.015 (6) |
| 40+ | 1754 | 0.4038 | 0.0676 | +0.3361 ± 0.0071 | 1.0577 | 0.2372 | 0.6688 | 0.1308 | 0.1015 | -0.070 ± 0.006 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 335 | 0.1949 | 0.1977 | -0.0028 ± 0.0009 | 0.5691 | 0.5764 | 0.5002 | 0.4849 | 0.5582 | -0.009 ± 0.0245 | -0.0133 (6) |
| 3-5 | 232 | 0.1867 | 0.185 | +0.0017 ± 0.0022 | 0.549 | 0.545 | 0.4991 | 0.4598 | 0.4612 | -0.113 ± 0.0297 | -0.01 (1) |
| 5-10 | 479 | 0.2006 | 0.1985 | +0.0021 ± 0.0031 | 0.5892 | 0.582 | 0.5091 | 0.4353 | 0.453 | -0.093 ± 0.0211 | -0.01 (4) |
| 10-15 | 366 | 0.2162 | 0.2144 | +0.0018 ± 0.006 | 0.6225 | 0.6125 | 0.5374 | 0.415 | 0.4699 | -0.075 ± 0.024 | -0.044 (5) |
| 15-25 | 431 | 0.229 | 0.2086 | +0.0204 ± 0.0086 | 0.6577 | 0.6019 | 0.5786 | 0.3851 | 0.4292 | -0.104 ± 0.0217 | -0.03 (1) |
| 25-40 | 258 | 0.2028 | 0.2058 | -0.0030 ± 0.0164 | 0.5888 | 0.5901 | 0.6513 | 0.3402 | 0.4961 | -0.045 ± 0.0243 | 0.0 (1) |
| 40+ | 49 | 0.3106 | 0.1697 | +0.1409 ± 0.0534 | 0.834 | 0.5113 | 0.7427 | 0.2906 | 0.3673 | -0.138 ± 0.0533 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1565 | 0.1821 | 0.1829 | -0.0009 ± 0.0004 | 0.5373 | 0.539 | 0.4804 | 0.4652 | 0.4965 | -0.025 ± 0.0109 | -0.0183 (23) |
| 3-5 | 1090 | 0.1835 | 0.1811 | +0.0024 ± 0.001 | 0.542 | 0.5363 | 0.4754 | 0.4362 | 0.4248 | -0.076 ± 0.0134 | -0.0243 (7) |
| 5-10 | 2437 | 0.1902 | 0.1853 | +0.0050 ± 0.0013 | 0.5639 | 0.5475 | 0.4803 | 0.4064 | 0.4099 | -0.059 ± 0.0088 | -0.01 (18) |
| 10-15 | 1876 | 0.1978 | 0.182 | +0.0158 ± 0.0024 | 0.5808 | 0.5329 | 0.4929 | 0.3698 | 0.3657 | -0.074 ± 0.0098 | -0.03 (9) |
| 15-25 | 2473 | 0.208 | 0.169 | +0.0390 ± 0.0032 | 0.6107 | 0.5013 | 0.4947 | 0.2992 | 0.2988 | -0.071 ± 0.0083 | -0.03 (2) |
| 25-40 | 1895 | 0.2114 | 0.1177 | +0.0937 ± 0.005 | 0.6133 | 0.366 | 0.5205 | 0.2033 | 0.2174 | -0.057 ± 0.0074 | 0.0 (1) |
| 40+ | 1265 | 0.3856 | 0.0455 | +0.3400 ± 0.0067 | 1.0071 | 0.1792 | 0.6299 | 0.1071 | 0.0545 | -0.087 ± 0.0057 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 622 | 0.2032 | 0.2034 | -0.0002 ± 0.0006 | 0.5897 | 0.5897 | 0.5004 | 0.4855 | 0.492 | -0.043 ± 0.018 | -0.0226 (46) |
| 3-5 | 467 | 0.1997 | 0.1982 | +0.0015 ± 0.0017 | 0.5808 | 0.5754 | 0.4808 | 0.4412 | 0.4411 | -0.055 ± 0.0206 | -0.0058 (33) |
| 5-10 | 947 | 0.193 | 0.1872 | +0.0057 ± 0.0021 | 0.5704 | 0.5554 | 0.479 | 0.4054 | 0.4055 | -0.060 ± 0.0143 | -0.0049 (73) |
| 10-15 | 619 | 0.2047 | 0.1944 | +0.0102 ± 0.0044 | 0.5979 | 0.5706 | 0.4898 | 0.367 | 0.3861 | -0.046 ± 0.0177 | 0.0014 (64) |
| 15-25 | 819 | 0.235 | 0.2092 | +0.0257 ± 0.0063 | 0.6687 | 0.6039 | 0.5513 | 0.357 | 0.3895 | -0.057 ± 0.016 | -0.0216 (58) |
| 25-40 | 463 | 0.2484 | 0.1869 | +0.0615 ± 0.0125 | 0.6998 | 0.5476 | 0.6328 | 0.3194 | 0.3758 | -0.081 ± 0.0188 | -0.0216 (25) |
| 40+ | 155 | 0.3593 | 0.1885 | +0.1708 ± 0.0358 | 1.0396 | 0.5559 | 0.7836 | 0.289 | 0.3871 | -0.062 ± 0.0321 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1916 | 0.1929 | 0.1928 | +0.0001 ± 0.0004 | 0.5631 | 0.5618 | 0.502 | 0.4868 | 0.489 | -0.041 ± 0.01 | -0.0155 (82) |
| 3-5 | 1350 | 0.1891 | 0.1862 | +0.0029 ± 0.0009 | 0.5528 | 0.5462 | 0.4899 | 0.4504 | 0.4356 | -0.061 ± 0.0118 | -0.0148 (63) |
| 5-10 | 2716 | 0.1913 | 0.183 | +0.0082 ± 0.0012 | 0.5664 | 0.5436 | 0.4753 | 0.4016 | 0.387 | -0.067 ± 0.0083 | -0.0087 (125) |
| 10-15 | 1848 | 0.2012 | 0.1864 | +0.0148 ± 0.0025 | 0.5895 | 0.5512 | 0.503 | 0.3798 | 0.381 | -0.058 ± 0.01 | -0.0053 (105) |
| 15-25 | 2356 | 0.2305 | 0.1974 | +0.0331 ± 0.0036 | 0.6653 | 0.5741 | 0.5453 | 0.3504 | 0.3642 | -0.060 ± 0.0092 | -0.0255 (106) |
| 25-40 | 1618 | 0.247 | 0.1626 | +0.0844 ± 0.0063 | 0.7029 | 0.4833 | 0.5959 | 0.2812 | 0.3066 | -0.070 ± 0.0097 | -0.0206 (47) |
| 40+ | 785 | 0.3777 | 0.119 | +0.2587 ± 0.0132 | 1.0621 | 0.369 | 0.6944 | 0.1865 | 0.1975 | -0.067 ± 0.0116 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2150 | 1.057 ± 0.06 | 1.172 | 0.1695 | 0.1706 | 0.2112 | 0.2019 |
| gen2 | 2150 | 0.854 ± 0.053 | 1.11 | 0.1861 | 0.17 | 0.2289 | 0.202 |
| gen1_elo | 2150 | 1.058 ± 0.06 | 1.158 | 0.1733 | 0.1711 | 0.2093 | 0.2019 |
| gen1_sr | 2150 | 1.044 ± 0.068 | 1.184 | 0.1441 | 0.1724 | 0.224 | 0.2018 |
| gen1_ledger | 4092 | 0.883 ± 0.039 | 1.064 | 0.1736 | 0.1895 | 0.218 | 0.1964 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 11,128)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,062 | 27.5% |
| STALE_QUOTE | market_freshness | 2,246 | 20.2% |
| BOOK_QUALITY | execution | 1,905 | 17.1% |
| POOR_DATA | data | 1,184 | 10.6% |
| LIMITED_DATA | data | 860 | 7.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 619 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 503 | 4.5% |
| IDENTITY_AMBIGUOUS | mapping | 352 | 3.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 335 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 62 | 0.6% |

Cause class: coverage 27.5%, market_freshness 20.2%, data 18.4%, execution 17.1%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.5%, mapping 3.2%, model_calibration 0.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.1%, START_UNVERIFIABLE 96.0%, LOW_DATA_QUALITY 68.3%, STALE_PLAYER_DATA 56.8%, THIN_PLAYER_HISTORY 56.3%, STALE_KALSHI_QUOTE 47.4%, MODEL_INTERNAL_DISAGREEMENT 37.0%, ASYMMETRIC_SAMPLE_SIZE 30.0%, WIDE_SPREAD 23.0%, MODEL_HIGH_UNCERTAINTY 16.4%, PLAYER_IDENTITY_RISK 11.5%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.3%, MODEL_CALIBRATION_OUTLIER 3.4%, EXTERNAL_MARKET_REJECTION 0.9%, UNKNOWN 0.6%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 30.1%, POST_SETTLEMENT_OBSERVATION 27.5%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,064)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,406 | 39.7% |
| BOOK_QUALITY | execution | 1,008 | 16.6% |
| STALE_QUOTE | market_freshness | 1,001 | 16.5% |
| POOR_DATA | data | 484 | 8.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 336 | 5.5% |
| LIMITED_DATA | data | 262 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 225 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 208 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 115 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 19 | 0.3% |

Cause class: coverage 39.7%, execution 16.6%, market_freshness 16.5%, data 12.3%, market_freshness/coverage 9.0%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.5%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.3%, THIN_PLAYER_HISTORY 57.9%, STALE_KALSHI_QUOTE 55.2%, STALE_PLAYER_DATA 51.3%, MODEL_INTERNAL_DISAGREEMENT 38.3%, ASYMMETRIC_SAMPLE_SIZE 31.6%, WIDE_SPREAD 22.6%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 14.6%, EVENT_MAPPING_RISK 10.0%, LOW_DISPLAYED_LIQUIDITY 7.5%, LEVEL_TRANSFER_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 4.3%, EXTERNAL_MARKET_REJECTION 0.5%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.6%, POST_SETTLEMENT_OBSERVATION 39.7%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5013, "IDENTITY_AMBIGUOUS": 1051}; ticker orientation: {"VERIFIED": 6064}.

Checks: discipline:AMBIGUOUS 439, discipline:PASS 5625, identity_confidence:AMBIGUOUS 888, identity_confidence:PASS 5176, level_mapping:NA 451, level_mapping:PASS 5613, market_pair:AMBIGUOUS 221, market_pair:NA 137, market_pair:PASS 5706, model_complement:NA 104, model_complement:PASS 5960, namesake:PASS 6064, physical_match_id:NA 2502, physical_match_id:PASS 3562, player_ids:PASS 6064, same_pair_other_event:PASS 6064, ticker_orientation:PASS 6064

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,830 | 1.5% | 1.6% | 0.5% | {"market_freshness": 20, "execution": 8} | 5.32 | 0.2106 / 0.2074 (193) | 17.5% | 0.1% | 6.0% | 1.6% |
| CHALLENGER | 3,924 | 18.3% | 6.0% | 11.9% | {"coverage": 453, "market_freshness": 107, "market_freshness/coverage": 87, "model_calibration_or_unknown": 40, "data": 25, "execution": 4, "model_calibration": 3} | 6.61 | 0.2248 / 0.206 (934) | 44.5% | 4.6% | 1.6% | 23.8% |
| DOUBLES | 854 | 51.4% | 50.9% | 7.2% | {"execution": 163, "mapping": 132, "market_freshness": 106, "market_freshness/coverage": 31, "coverage": 7} | 25.63 | 0.3254 / 0.2297 (239) | 27.4% | 0.0% | 100.0% | 7.8% |
| ITF_MEN | 8,160 | 23.5% | 15.3% | 31.6% | {"coverage": 803, "execution": 386, "data": 271, "market_freshness": 268, "market_freshness/coverage": 169, "mapping": 19, "model_calibration_or_unknown": 2} | 10.29 | 0.2102 / 0.1937 (2041) | 37.9% | 53.1% | 6.3% | 24.5% |
| ITF_WOMEN | 10,536 | 26.0% | 17.5% | 45.2% | {"coverage": 1126, "market_freshness": 441, "execution": 430, "data": 426, "market_freshness/coverage": 216, "mapping": 68, "model_calibration_or_unknown": 23, "model_calibration": 9} | 12.15 | 0.2046 / 0.1922 (2299) | 38.9% | 56.9% | 9.5% | 24.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,156 | 7.6% | 6.7% | 1.5% | {"market_freshness": 35, "model_calibration_or_unknown": 20, "data": 11, "market_freshness/coverage": 9, "model_calibration": 4, "execution": 4, "coverage": 4, "mapping": 1} | 7.91 | 0.2165 / 0.2142 (187) | 30.0% | 1.8% | 1.1% | 3.0% |
| WTA125 | 880 | 13.8% | 10.0% | 2.0% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 22, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 3} | 9.83 | 0.2348 / 0.2183 (307) | 25.0% | 6.0% | 3.9% | 11.6% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 9 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 10 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 11 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 14 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 15 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 18 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 19 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 21 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 22 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 23 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 24 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 25 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 27 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 28 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 29 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 30 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 31 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 32 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 33 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 34 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 35 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 799 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 38 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 40 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 41 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 42 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 26 min (AGING); no external reference |
| 43 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 44 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 45 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 46 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 47 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 229 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |
| 48 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 123 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.981, "by_level_share_of_ge_25pp": {"ATP": 0.0046, "CHALLENGER": 0.1186, "DOUBLES": 0.0724, "ITF_MEN": 0.3163, "ITF_WOMEN": 0.4517, "OTHER": 0.002, "WTA": 0.0145, "WTA125": 0.02}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5523, "share_primary_cause_market_settled_or_in_play": 0.4865, "share_primary_cause_stale_quote_only": 0.1651}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6064, "identity_ambiguous_share": 0.1733, "ticker_orientation": {"VERIFIED": 6064}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3562, "with_external": 82, "coverage": 0.023, "external_status": {"EXTERNAL_STALE": 60, "AGREES_WITH_KALSHI": 22}, "triangulation": {"INSUFFICIENT_INPUTS": 60, "MODEL_LONE_OUTLIER": 22}, "share_external_agrees_with_kalshi": 0.2683, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1512, "with_external": 80, "coverage": 0.0529, "external_status": {"EXTERNAL_STALE": 58, "AGREES_WITH_KALSHI": 22}, "triangulation": {"INSUFFICIENT_INPUTS": 58, "MODEL_LONE_OUTLIER": 22}, "share_external_agrees_with_kalshi": 0.275, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 647.0, "median_sample_ratio": 2.28, "median_min_matches": 21.0, "median_max_days_since_last": 196.0, "share_severe_asymmetry": 0.1699, "data_status": {"POOR": 3067, "LIMITED": 1870, "ADEQUATE": 1127}, "comparison_lt_10pp": {"median_thinner_serve_points": 1888.0, "median_sample_ratio": 1.67, "median_min_matches": 85.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 464, "model_minus_observed": 0.06, "kalshi_minus_observed": -0.0719, "brier_diff_model_minus_kalshi": 0.0035}, "4-10x": {"n": 321, "model_minus_observed": 0.0575, "kalshi_minus_observed": -0.0839, "brier_diff_model_minus_kalshi": -0.0006}, "<2x": {"n": 1061, "model_minus_observed": 0.0872, "kalshi_minus_observed": -0.0348, "brier_diff_model_minus_kalshi": 0.0129}, ">=10x": {"n": 304, "model_minus_observed": 0.1114, "kalshi_minus_observed": -0.0563, "brier_diff_model_minus_kalshi": 0.0162}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2150, "model": {"intercept": -0.553, "slope": 0.854, "slope_se": 0.053}, "kalshi_mid_same_rows": {"intercept": 0.209, "slope": 1.11, "slope_se": 0.061}, "mean_extremity_model": 0.1861, "mean_extremity_kalshi": 0.17, "model_brier": 0.2289, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0269, "brier_diff_se": 0.0041, "model_logloss": 0.6541, "kalshi_logloss": 0.5862}, "fair_v1": {"n": 2150, "model": {"intercept": -0.399, "slope": 1.057, "slope_se": 0.06}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.172, "slope_se": 0.063}, "mean_extremity_model": 0.1695, "mean_extremity_kalshi": 0.1706, "model_brier": 0.2112, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0093, "brier_diff_se": 0.0032, "model_logloss": 0.6098, "kalshi_logloss": 0.5858}, "gen1_elo": {"n": 2150, "model": {"intercept": -0.381, "slope": 1.058, "slope_se": 0.06}, "kalshi_mid_same_rows": {"intercept": 0.314, "slope": 1.158, "slope_se": 0.062}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1711, "model_brier": 0.2093, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0075, "brier_diff_se": 0.0032, "model_logloss": 0.6067, "kalshi_logloss": 0.5857}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2459, "share_ge_15": 0.429, "median_abs_gap": 12.8, "n": 14484}, "gen1_elo": {"share_ge_25": 0.2383, "share_ge_15": 0.4259, "median_abs_gap": 12.29, "n": 14484}, "gen1_sr": {"share_ge_25": 0.2982, "share_ge_15": 0.5122, "median_abs_gap": 15.43, "n": 14484}, "gen2": {"share_ge_25": 0.302, "share_ge_15": 0.5006, "median_abs_gap": 15.02, "n": 14484}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1393, "share_ge_15": 0.3258, "median_abs_gap": 10.21, "n": 10852}, "gen1_elo": {"share_ge_25": 0.1352, "share_ge_15": 0.3195, "median_abs_gap": 9.6, "n": 10851}, "gen1_sr": {"share_ge_25": 0.1915, "share_ge_15": 0.4191, "median_abs_gap": 12.55, "n": 10852}, "gen2": {"share_ge_25": 0.2095, "share_ge_15": 0.4218, "median_abs_gap": 12.44, "n": 10853}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.32, "share_ge_25_all": 0.0153, "share_ge_25_pregame_clean": 0.0156}, "WTA": {"median_abs_gap_pregame_clean": 7.91, "share_ge_25_all": 0.0761, "share_ge_25_pregame_clean": 0.0669}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2414, "share_within_10pp_all": 0.441, "share_within_10pp_pregame_clean": 0.5059, "corr_model_vs_mid_pregame_clean": 0.8507}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 331, "model_brier": 0.1934, "kalshi_brier": 0.1949, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 392, "model_brier": 0.2129, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0082}, "15-25": {"n_settled": 452, "model_brier": 0.2286, "kalshi_brier": 0.214, "brier_diff_model_minus_kalshi": 0.0145}, "25-40": {"n_settled": 255, "model_brier": 0.2211, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0199}, "3-5": {"n_settled": 221, "model_brier": 0.1891, "kalshi_brier": 0.1909, "brier_diff_model_minus_kalshi": -0.0018}, "40+": {"n_settled": 56, "model_brier": 0.2885, "kalshi_brier": 0.1688, "brier_diff_model_minus_kalshi": 0.1197}, "5-10": {"n_settled": 443, "model_brier": 0.201, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": -0.0014}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.553, "slope": 0.854, "slope_se": 0.053}, "kalshi_slope": {"intercept": 0.209, "slope": 1.11, "slope_se": 0.061}, "n": 2150}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.534, "slope": 0.883, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.125, "slope": 1.064, "slope_se": 0.043}, "n": 4092}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 239, "model_brier": 0.3254, "kalshi_brier": 0.2297, "brier_diff_model_minus_kalshi": 0.0957, "brier_diff_se": 0.0209, "corr_model_outcome": -0.0137, "corr_kalshi_outcome": 0.2978}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
