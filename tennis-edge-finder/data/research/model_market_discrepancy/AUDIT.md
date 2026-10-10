# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-10T10:23Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 27,388): 0-3 14.4%, 3-5 9.7%, 5-10 20.0%, 10-15 15.4%, 15-25 18.4%, 25-40 13.7%, 40+ 8.3%; median gap 11.83 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 11.9%, doubles 7.2%). Main tour: ATP 1.6% and WTA 7.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,039): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.6%, BOOK_QUALITY 16.7%, STALE_QUOTE 16.6%, POOR_DATA 8.0%, POSSIBLY_IN_PLAY_QUOTE 5.5%, LIMITED_DATA 4.3%, IDENTITY_AMBIGUOUS 3.7%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.3%. By class: coverage 39.6%, execution 16.7%, market_freshness 16.6%, data 12.3%, market_freshness/coverage 8.9%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.3%.
* **Stale / settled / in-play**: 55.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,039 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 18.7% of the time and with the model 0.2%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 644.5 points vs 1884.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.053, Gen-2 0.854, Gen-1 ledger 0.901 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 254 model 0.2218 vs Kalshi 0.2009; n 55 model 0.2888 vs Kalshi 0.1716.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 107,704 model-market comparisons (177,689 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 40,524 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-10T10:19:28.380497+00:00'], shadow board 28,705 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-10T10:19:30.859188+00:00'], Model 4 11,912 rows, 11,922 settled tickers, 3,264 tickers with an external scan.
* By model: {"gen1_ledger": 26489, "gen1_elo": 14422, "fair_v1": 14422, "gen2": 14422, "gen1_sr": 14422, "model4_fundamental": 11768, "model4_conditioned": 11759}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 27,388 | 14.4 | 9.7 | 20.0 | 15.4 | 18.4 | 13.7 | 8.3 | 11.83 | 40.5% | 22.1% |
| MW fair_v1 | 14,422 | 13.7 | 8.7 | 18.4 | 16.3 | 18.3 | 14.6 | 10.0 | 12.79 | 42.9% | 24.6% |
| MW gen1_elo | 14,422 | 13.2 | 9.0 | 20.2 | 15.0 | 18.8 | 14.4 | 9.4 | 12.29 | 42.6% | 23.8% |
| MW gen1_ledger | 12,966 | 15.2 | 10.8 | 21.7 | 14.5 | 18.6 | 12.8 | 6.5 | 10.63 | 37.8% | 19.2% |
| MW gen1_sr | 14,422 | 10.2 | 7.9 | 16.4 | 14.3 | 21.4 | 18.1 | 11.7 | 15.43 | 51.2% | 29.8% |
| MW gen2 | 14,422 | 12.2 | 7.2 | 16.2 | 14.3 | 19.9 | 17.1 | 13.1 | 15.02 | 50.1% | 30.2% |
| all families model4_conditioned | 11,759 | 22.2 | 20.2 | 36.1 | 15.8 | 4.1 | 0.8 | 0.8 | 5.71 | 5.7% | 1.6% |
| all families model4_fundamental | 11,768 | 16.8 | 13.4 | 35.8 | 19.7 | 10.6 | 2.4 | 1.1 | 7.53 | 14.2% | 3.5% |

Configurable thresholds (primary): >=5pp 75.9%, >=10pp 55.9%, >=15pp 40.5%, >=20pp 30.3%, >=25pp 22.1%, >=30pp 16.2%, >=40pp 8.3%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.46pp; >=10pp 45.4%, >=25pp 17.8%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,171 | 29.9 | 14.4 | 25.1 | 17.0 | 11.4 | 1.2 | 0.9 | 5.93 | 13.6% | 2.1% |
| CHALLENGER | 2,364 | 15.9 | 10.8 | 18.6 | 16.2 | 12.8 | 12.9 | 12.7 | 11.76 | 38.5% | 25.6% |
| ITF_MEN | 4,136 | 11.6 | 8.8 | 18.4 | 15.0 | 19.2 | 15.0 | 12.0 | 13.54 | 46.2% | 27.0% |
| ITF_WOMEN | 5,770 | 10.2 | 6.6 | 15.9 | 16.5 | 21.7 | 18.6 | 10.5 | 15.36 | 50.8% | 29.1% |
| WTA | 626 | 22.7 | 10.4 | 25.7 | 16.4 | 16.3 | 6.7 | 1.8 | 7.81 | 24.8% | 8.5% |
| WTA125 | 355 | 11.6 | 5.9 | 23.1 | 25.1 | 16.6 | 15.5 | 2.2 | 11.33 | 34.4% | 17.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,171 | 24.2 | 13.8 | 24.9 | 18.5 | 15.5 | 2.0 | 1.1 | 6.9 | 18.5% | 3.1% |
| CHALLENGER | 2,364 | 15.4 | 7.5 | 18.3 | 13.3 | 18.1 | 14.1 | 13.2 | 13.07 | 45.5% | 27.4% |
| ITF_MEN | 4,136 | 10.5 | 7.5 | 16.9 | 15.0 | 19.9 | 17.5 | 12.7 | 15.05 | 50.0% | 30.2% |
| ITF_WOMEN | 5,770 | 9.1 | 5.9 | 12.8 | 12.8 | 21.2 | 21.0 | 17.1 | 19.07 | 59.3% | 38.1% |
| WTA | 626 | 21.2 | 6.4 | 18.4 | 15.2 | 21.1 | 16.0 | 1.8 | 12.12 | 38.8% | 17.7% |
| WTA125 | 355 | 4.2 | 2.8 | 18.3 | 20.6 | 22.8 | 20.6 | 10.7 | 17.24 | 54.1% | 31.3% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,171 | 26.6 | 14.3 | 28.9 | 15.3 | 11.1 | 2.7 | 1.0 | 6.34 | 14.9% | 3.8% |
| CHALLENGER | 2,364 | 15.9 | 10.7 | 20.4 | 14.7 | 13.8 | 12.1 | 12.6 | 10.68 | 38.5% | 24.7% |
| ITF_MEN | 4,136 | 10.4 | 8.9 | 19.3 | 13.9 | 20.1 | 15.3 | 12.1 | 13.89 | 47.5% | 27.4% |
| ITF_WOMEN | 5,770 | 9.8 | 6.7 | 16.7 | 15.7 | 22.9 | 18.8 | 9.4 | 15.48 | 51.0% | 28.2% |
| WTA | 626 | 22.4 | 13.9 | 35.0 | 15.5 | 9.1 | 3.0 | 1.1 | 6.68 | 13.3% | 4.2% |
| WTA125 | 355 | 22.8 | 11.8 | 30.7 | 16.3 | 13.2 | 4.5 | 0.6 | 7.73 | 18.3% | 5.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 639 | 30.2 | 23.8 | 35.0 | 9.1 | 1.4 | 0.5 | 0.0 | 4.69 | 1.9% | 0.5% |
| CHALLENGER | 1,547 | 23.7 | 17.4 | 26.4 | 13.6 | 11.7 | 5.3 | 1.9 | 6.43 | 18.9% | 7.2% |
| DOUBLES | 848 | 3.9 | 3.2 | 10.4 | 11.4 | 19.8 | 24.9 | 26.4 | 25.71 | 71.1% | 51.3% |
| ITF_MEN | 4,007 | 15.1 | 8.6 | 21.1 | 15.3 | 20.2 | 12.2 | 7.6 | 11.69 | 40.0% | 19.8% |
| ITF_WOMEN | 4,739 | 11.6 | 9.3 | 19.8 | 14.6 | 22.4 | 16.6 | 5.5 | 12.98 | 44.6% | 22.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 512 | 21.7 | 13.3 | 26.0 | 17.8 | 14.4 | 6.2 | 0.6 | 7.98 | 21.3% | 6.8% |
| WTA125 | 525 | 16.9 | 13.9 | 22.5 | 19.8 | 15.8 | 8.4 | 2.7 | 9.01 | 26.9% | 11.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,162 | 29.9 | 14.3 | 25.2 | 17.0 | 11.4 | 1.2 | 0.9 | 5.93 | 13.6% | 2.1% |
| CHALLENGER | 1,667 | 20.9 | 13.9 | 23.9 | 19.1 | 13.1 | 6.4 | 2.7 | 7.94 | 22.1% | 9.1% |
| ITF_MEN | 2,938 | 14.4 | 11.1 | 21.9 | 16.6 | 19.1 | 11.8 | 5.0 | 10.64 | 35.9% | 16.8% |
| ITF_WOMEN | 4,099 | 12.7 | 8.3 | 18.6 | 19.1 | 23.3 | 14.6 | 3.2 | 12.62 | 41.2% | 17.8% |
| WTA | 622 | 22.5 | 10.4 | 25.9 | 16.4 | 16.4 | 6.6 | 1.8 | 7.81 | 24.8% | 8.4% |
| WTA125 | 341 | 12.0 | 6.2 | 22.3 | 25.5 | 17.0 | 15.5 | 1.5 | 11.33 | 34.0% | 17.0% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,162 | 24.2 | 13.9 | 24.9 | 18.5 | 15.5 | 2.0 | 1.1 | 6.9 | 18.6% | 3.1% |
| CHALLENGER | 1,667 | 20.3 | 9.9 | 23.2 | 16.2 | 18.6 | 9.3 | 2.6 | 9.0 | 30.5% | 11.9% |
| ITF_MEN | 2,939 | 12.5 | 9.2 | 19.6 | 16.8 | 21.3 | 14.8 | 5.8 | 12.44 | 41.9% | 20.5% |
| ITF_WOMEN | 4,099 | 10.7 | 7.1 | 14.5 | 14.0 | 23.8 | 19.8 | 10.1 | 16.27 | 53.7% | 29.9% |
| WTA | 622 | 21.2 | 6.4 | 18.3 | 15.3 | 21.1 | 15.9 | 1.8 | 12.12 | 38.8% | 17.7% |
| WTA125 | 341 | 4.4 | 2.9 | 18.5 | 21.1 | 22.3 | 21.1 | 9.7 | 16.84 | 53.1% | 30.8% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 619 | 30.2 | 24.1 | 35.4 | 9.2 | 0.7 | 0.5 | 0.0 | 4.68 | 1.1% | 0.5% |
| CHALLENGER | 1,313 | 25.7 | 19.6 | 28.6 | 13.2 | 10.7 | 2.0 | 0.1 | 5.68 | 12.8% | 2.1% |
| DOUBLES | 783 | 3.8 | 3.2 | 10.6 | 11.5 | 19.9 | 24.6 | 26.3 | 25.63 | 70.9% | 51.0% |
| ITF_MEN | 3,231 | 16.8 | 9.6 | 23.4 | 16.2 | 19.9 | 9.8 | 4.4 | 10.04 | 34.0% | 14.1% |
| ITF_WOMEN | 3,869 | 12.9 | 10.1 | 21.7 | 15.5 | 22.7 | 14.9 | 2.3 | 11.5 | 39.9% | 17.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 482 | 22.2 | 13.9 | 26.6 | 17.8 | 14.7 | 4.8 | 0.0 | 7.91 | 19.5% | 4.8% |
| WTA125 | 439 | 18.9 | 15.5 | 24.6 | 22.6 | 13.9 | 4.3 | 0.2 | 7.88 | 18.4% | 4.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 848 | 3.9 | 3.2 | 10.4 | 11.4 | 19.8 | 24.9 | 26.4 | 25.71 | 71.1% | 51.3% |
| singles | 12,118 | 16.0 | 11.3 | 22.5 | 14.8 | 18.5 | 11.9 | 5.1 | 10.05 | 35.5% | 17.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,293 | 13.6 | 9.6 | 20.2 | 16.1 | 16.1 | 14.0 | 10.3 | 12.03 | 40.4% | 24.3% |
| Hard | 9,693 | 14.1 | 8.4 | 18.2 | 16.1 | 18.8 | 14.5 | 9.8 | 12.83 | 43.2% | 24.3% |
| UNKNOWN | 1,436 | 11.4 | 8.4 | 15.5 | 18.0 | 20.2 | 16.6 | 9.9 | 13.98 | 46.7% | 26.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,366 | 20.0 | 10.6 | 20.9 | 17.3 | 14.5 | 9.1 | 7.6 | 9.52 | 31.2% | 16.7% |
| B | 1,931 | 15.0 | 9.5 | 19.2 | 17.2 | 16.7 | 12.2 | 10.2 | 11.42 | 39.1% | 22.3% |
| C | 2,209 | 12.4 | 9.8 | 19.4 | 15.3 | 18.9 | 14.8 | 9.4 | 12.71 | 43.1% | 24.2% |
| D | 2,686 | 10.8 | 8.5 | 17.4 | 16.3 | 22.1 | 15.0 | 9.9 | 13.98 | 47.0% | 24.9% |
| F | 3,230 | 7.7 | 5.1 | 14.8 | 15.0 | 20.9 | 22.9 | 13.6 | 18.39 | 57.4% | 36.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,730 | 22.5 | 16.2 | 28.0 | 15.0 | 11.6 | 4.8 | 1.8 | 6.78 | 18.2% | 6.7% |
| B | 2,029 | 15.0 | 9.8 | 24.1 | 16.3 | 19.0 | 11.4 | 4.5 | 10.34 | 34.9% | 15.9% |
| C | 2,655 | 11.8 | 7.7 | 17.9 | 14.4 | 20.9 | 15.8 | 11.6 | 14.13 | 48.3% | 27.4% |
| D | 2,114 | 14.1 | 9.3 | 21.3 | 13.2 | 21.9 | 14.0 | 6.2 | 12.04 | 42.1% | 20.2% |
| F | 2,438 | 9.1 | 7.7 | 14.4 | 13.7 | 23.5 | 21.6 | 10.0 | 16.91 | 55.1% | 31.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,875 | 18.5 | 9.8 | 19.9 | 17.1 | 14.9 | 10.0 | 9.8 | 10.5 | 34.7% | 19.8% |
| LIMITED | 3,590 | 14.7 | 10.6 | 20.5 | 16.2 | 17.8 | 13.2 | 7.1 | 11.26 | 38.0% | 20.2% |
| POOR | 5,957 | 9.2 | 6.7 | 15.9 | 15.6 | 21.4 | 19.2 | 11.8 | 16.04 | 52.6% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,640 | 30.6 | 24.7 | 36.6 | 5.6 | 1.9 | 0.6 | 0.1 | 4.56 | 2.5% | 0.6% |
| GAME_SPREAD | 2,555 | 25.1 | 15.7 | 36.9 | 17.3 | 4.6 | 0.3 | 0.2 | 6.12 | 5.1% | 0.5% |
| MATCH_WINNER | 12,966 | 15.2 | 10.8 | 21.7 | 14.5 | 18.6 | 12.8 | 6.5 | 10.63 | 37.8% | 19.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 4,594 | 32.8 | 19.7 | 30.4 | 9.8 | 5.8 | 1.2 | 0.3 | 4.78 | 7.3% | 1.5% |
| TOTAL_GAMES | 3,710 | 7.1 | 9.2 | 38.6 | 30.4 | 9.8 | 2.6 | 2.3 | 9.46 | 14.7% | 4.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,323 | 25.3 | 37.7 | 31.7 | 0.3 | 4.3 | 0.5 | 0.1 | 4.33 | 5.0% | 0.6% |
| GAME_SPREAD | 3,049 | 44.8 | 15.0 | 30.2 | 7.9 | 1.2 | 0.7 | 0.3 | 3.65 | 2.2% | 1.0% |
| TOTAL_GAMES | 4,387 | 3.4 | 6.6 | 44.5 | 36.6 | 5.9 | 1.1 | 1.9 | 9.56 | 8.9% | 3.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,323 | 25.6 | 18.7 | 36.7 | 9.5 | 6.8 | 2.3 | 0.3 | 5.55 | 9.4% | 2.7% |
| GAME_SPREAD | 3,049 | 19.1 | 13.0 | 29.7 | 21.0 | 14.2 | 2.4 | 0.7 | 7.95 | 17.3% | 3.1% |
| TOTAL_GAMES | 4,396 | 6.7 | 8.5 | 39.2 | 28.8 | 12.0 | 2.5 | 2.2 | 9.5 | 16.7% | 4.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 14,422 | 42.9% | 24.6% | 12.79 | 32.7% | 14.0% | 10.25 |
| gen1_elo | 14,422 | 42.6% | 23.8% | 12.29 | 32.0% | 13.5% | 9.62 |
| gen1_sr | 14,422 | 51.2% | 29.8% | 15.43 | 42.0% | 19.2% | 12.56 |
| gen2 | 14,422 | 50.1% | 30.2% | 15.02 | 42.3% | 21.0% | 12.48 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 7,415 | 16.8 | 11.0 | 21.5 | 17.7 | 18.4 | 11.2 | 3.3 | 10.18 | 33.0% | 14.5% |
| STALE | 7,007 | 10.5 | 6.3 | 15.1 | 14.7 | 18.2 | 18.2 | 17.0 | 16.93 | 53.4% | 35.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 6,434 | 17.4 | 12.0 | 23.7 | 14.3 | 16.6 | 11.4 | 4.7 | 9.23 | 32.7% | 16.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 27,388 | 6434 | 10887 | 10067 | 24.8 | 159.1 | 1400.4 |
| ge_15pp | 11,089 | 2104 | 3732 | 5253 | 28.5 | 457.2 | 1380.4 |
| ge_25pp | 6,039 | 1034 | 1669 | 3336 | 36.4 | 579.5 | 1380.4 |
| lt_10pp | 12,069 | 3409 | 5290 | 3370 | 23.1 | 49.5 | 1341.5 |

Current slate `SL-20261010T102349Z-e08064eb`: 308 priced rows, quote age at build {'median': 4.6, 'max': 4.6}, freshness {'FRESH': 308}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 4 | 0.0 | 0.0 | 25.0 | 0.0 | 75.0 | 0.0 | 0.0 | 20.45 | 75.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 4 | 25.0 | 75.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.22 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 871 | 23.8 | 11.7 | 21.8 | 19.6 | 16.2 | 6.5 | 0.3 | 7.98 | 23.1% | 6.9% |
| MARKETS_AGREE | 143 | 76.2 | 23.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.87 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 235 | 0.0 | 3.4 | 35.7 | 34.0 | 17.4 | 8.9 | 0.4 | 11.41 | 26.8% | 9.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 14,422 | 1257 (8.7%) | 18.7% | 0.2% | {"EXTERNAL_STALE": 871, "AGREES_WITH_KALSHI": 235, "ALL_AGREE": 143, "EXTERNAL_OUTLIER": 4, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 6,186 | 267 (4.3%) | 23.6% | 1.1% | {"EXTERNAL_STALE": 201, "AGREES_WITH_KALSHI": 63, "SUPPORTS_MODEL_DIRECTION": 3} |
| fair_v1_ge_25pp | 3,543 | 82 (2.3%) | 26.8% | 0.0% | {"EXTERNAL_STALE": 60, "AGREES_WITH_KALSHI": 22} |
| fair_v1_ge_25pp_pregame_clean | 1,511 | 80 (5.3%) | 27.5% | 0.0% | {"EXTERNAL_STALE": 58, "AGREES_WITH_KALSHI": 22} |
| fair_v1_lt_10pp | 5,891 | 739 (12.5%) | 12.4% | 0.0% | {"EXTERNAL_STALE": 499, "ALL_AGREE": 143, "AGREES_WITH_KALSHI": 92, "EXTERNAL_OUTLIER": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,916 | 11.7 | 8.4 | 19.6 | 15.4 | 20.8 | 13.8 | 10.2 | 13.08 | 44.8% | 24.0% |
| 4-10x | 2,001 | 11.2 | 9.2 | 18.4 | 15.3 | 20.0 | 16.5 | 9.3 | 13.57 | 45.8% | 25.8% |
| <2x | 7,730 | 15.8 | 9.2 | 18.6 | 17.3 | 16.6 | 13.1 | 9.5 | 11.86 | 39.1% | 22.5% |
| >=10x | 1,775 | 11.0 | 6.4 | 15.6 | 14.3 | 19.9 | 20.4 | 12.4 | 16.24 | 52.7% | 32.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,779 | 14.1 | 8.5 | 19.3 | 16.0 | 18.1 | 13.1 | 11.0 | 12.4 | 42.2% | 24.0% |
| 300-1000 | 3,525 | 11.7 | 9.1 | 16.7 | 16.3 | 21.0 | 16.0 | 9.2 | 13.75 | 46.2% | 25.2% |
| <300 | 3,727 | 8.3 | 6.0 | 15.7 | 15.0 | 20.9 | 21.0 | 13.0 | 17.15 | 54.9% | 34.0% |
| >=3000 | 3,391 | 21.3 | 11.5 | 22.3 | 17.9 | 12.9 | 7.8 | 6.2 | 8.5 | 27.0% | 14.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 460 | 0.5369 | 0.4046 | 0.4761 | +0.061 | -0.071 | 0.0042 ± 0.0069 |
| ratio 4-10x | 319 | 0.5813 | 0.4404 | 0.5235 | +0.058 | -0.083 | -0.0013 ± 0.0087 |
| ratio <2x | 1032 | 0.5411 | 0.4186 | 0.4525 | +0.088 | -0.034 | 0.0137 ± 0.0044 |
| ratio >=10x | 299 | 0.55 | 0.3805 | 0.4381 | +0.112 | -0.058 | 0.0163 ± 0.0102 |
| thinner_sample 1000-3000 | 579 | 0.5427 | 0.4183 | 0.4629 | +0.080 | -0.045 | 0.0081 ± 0.006 |
| thinner_sample 300-1000 | 571 | 0.5662 | 0.4256 | 0.4921 | +0.074 | -0.067 | 0.0027 ± 0.0066 |
| thinner_sample <300 | 607 | 0.5439 | 0.3836 | 0.4596 | +0.084 | -0.076 | 0.0111 ± 0.0069 |
| thinner_sample >=3000 | 353 | 0.5313 | 0.4372 | 0.4419 | +0.089 | -0.005 | 0.0214 ± 0.006 |
| data_status ADEQUATE | 574 | 0.5309 | 0.4288 | 0.439 | +0.092 | -0.010 | 0.0158 ± 0.0051 |
| data_status LIMITED | 566 | 0.5564 | 0.4242 | 0.4859 | +0.071 | -0.062 | 0.0038 ± 0.0063 |
| data_status POOR | 970 | 0.5521 | 0.3981 | 0.4711 | +0.081 | -0.073 | 0.0096 ± 0.0053 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 325 | 0.1936 | 0.195 | -0.0014 ± 0.0008 | 0.565 | 0.5685 | 0.4918 | 0.4772 | 0.5231 | -0.055 ± 0.0256 | -0.01 (3) |
| 3-5 | 218 | 0.1884 | 0.1903 | -0.0019 ± 0.0024 | 0.5569 | 0.5593 | 0.5117 | 0.4718 | 0.5138 | -0.051 ± 0.03 | 0.02 (1) |
| 5-10 | 428 | 0.2011 | 0.2026 | -0.0015 ± 0.0033 | 0.5883 | 0.5917 | 0.5232 | 0.449 | 0.4883 | -0.084 ± 0.0227 | -0.0125 (4) |
| 10-15 | 384 | 0.2128 | 0.2056 | +0.0072 ± 0.0058 | 0.6131 | 0.5924 | 0.5159 | 0.3921 | 0.4219 | -0.093 ± 0.0231 | -0.0633 (3) |
| 15-25 | 446 | 0.2287 | 0.2119 | +0.0168 ± 0.0086 | 0.6531 | 0.6111 | 0.5748 | 0.3791 | 0.4327 | -0.093 ± 0.0217 | -0.0133 (6) |
| 25-40 | 254 | 0.2218 | 0.2009 | +0.0208 ± 0.0167 | 0.6336 | 0.5772 | 0.6459 | 0.3376 | 0.4567 | -0.074 ± 0.0251 | -0.01 (1) |
| 40+ | 55 | 0.2888 | 0.1716 | +0.1171 ± 0.0497 | 0.7822 | 0.5171 | 0.752 | 0.305 | 0.4 | -0.128 ± 0.0484 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1620 | 0.173 | 0.174 | -0.0010 ± 0.0004 | 0.5168 | 0.518 | 0.4746 | 0.4599 | 0.4994 | -0.019 ± 0.0105 | -0.0188 (8) |
| 3-5 | 1035 | 0.1929 | 0.1901 | +0.0028 ± 0.0011 | 0.5674 | 0.5556 | 0.4805 | 0.4409 | 0.4222 | -0.077 ± 0.0138 | 0.02 (1) |
| 5-10 | 2190 | 0.1956 | 0.1931 | +0.0025 ± 0.0014 | 0.5743 | 0.5664 | 0.4907 | 0.4169 | 0.4338 | -0.052 ± 0.0095 | -0.0082 (17) |
| 10-15 | 2011 | 0.2008 | 0.1827 | +0.0181 ± 0.0024 | 0.5871 | 0.5366 | 0.472 | 0.3476 | 0.3371 | -0.078 ± 0.0095 | -0.0475 (4) |
| 15-25 | 2298 | 0.2043 | 0.1641 | +0.0402 ± 0.0033 | 0.6007 | 0.489 | 0.4921 | 0.2957 | 0.2924 | -0.077 ± 0.0084 | -0.0048 (29) |
| 25-40 | 1928 | 0.2186 | 0.1228 | +0.0958 ± 0.005 | 0.6298 | 0.3801 | 0.5262 | 0.2126 | 0.2194 | -0.062 ± 0.0077 | -0.01 (1) |
| 40+ | 1319 | 0.3717 | 0.0441 | +0.3276 ± 0.0064 | 0.9689 | 0.1748 | 0.6225 | 0.1056 | 0.0576 | -0.084 ± 0.0054 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 252 | 0.1961 | 0.1965 | -0.0004 ± 0.001 | 0.5746 | 0.576 | 0.4931 | 0.4781 | 0.4881 | -0.089 ± 0.0295 | -0.01 (1) |
| 3-5 | 166 | 0.2118 | 0.2126 | -0.0008 ± 0.0029 | 0.6053 | 0.6092 | 0.5278 | 0.4877 | 0.512 | -0.060 ± 0.0374 | 0.02 (1) |
| 5-10 | 366 | 0.1945 | 0.1912 | +0.0033 ± 0.0034 | 0.5711 | 0.5638 | 0.5653 | 0.4905 | 0.5055 | -0.093 ± 0.0236 | -0.01 (4) |
| 10-15 | 361 | 0.2158 | 0.2078 | +0.0080 ± 0.006 | 0.6186 | 0.602 | 0.5773 | 0.4525 | 0.4875 | -0.096 ± 0.0249 | -0.05 (4) |
| 15-25 | 507 | 0.2275 | 0.2068 | +0.0207 ± 0.008 | 0.6445 | 0.5958 | 0.5967 | 0.3993 | 0.4517 | -0.096 ± 0.0207 | -0.01 (5) |
| 25-40 | 335 | 0.2771 | 0.2013 | +0.0757 ± 0.0155 | 0.7765 | 0.5827 | 0.6727 | 0.3585 | 0.397 | -0.140 ± 0.0245 | -0.025 (2) |
| 40+ | 123 | 0.341 | 0.1909 | +0.1501 ± 0.0381 | 0.9583 | 0.5575 | 0.7617 | 0.2833 | 0.3821 | -0.059 ± 0.0368 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1444 | 0.1775 | 0.1781 | -0.0006 ± 0.0004 | 0.5276 | 0.5292 | 0.4929 | 0.4785 | 0.5069 | -0.027 ± 0.0115 | -0.0217 (6) |
| 3-5 | 879 | 0.1943 | 0.193 | +0.0013 ± 0.0012 | 0.5632 | 0.5605 | 0.5252 | 0.4853 | 0.4881 | -0.049 ± 0.0151 | 0.02 (1) |
| 5-10 | 1935 | 0.1858 | 0.1822 | +0.0037 ± 0.0014 | 0.553 | 0.5403 | 0.5177 | 0.4444 | 0.4599 | -0.049 ± 0.0098 | -0.01 (5) |
| 10-15 | 1743 | 0.1968 | 0.1814 | +0.0154 ± 0.0026 | 0.5802 | 0.5316 | 0.5174 | 0.3929 | 0.3964 | -0.069 ± 0.0104 | -0.02 (14) |
| 15-25 | 2446 | 0.2161 | 0.1735 | +0.0425 ± 0.0033 | 0.6282 | 0.5136 | 0.5295 | 0.3341 | 0.3267 | -0.083 ± 0.0085 | -0.0026 (27) |
| 25-40 | 2216 | 0.2517 | 0.137 | +0.1147 ± 0.005 | 0.7148 | 0.4176 | 0.5623 | 0.2458 | 0.2243 | -0.093 ± 0.0079 | -0.015 (6) |
| 40+ | 1738 | 0.4031 | 0.0679 | +0.3352 ± 0.0072 | 1.0564 | 0.2377 | 0.6686 | 0.1306 | 0.1024 | -0.069 ± 0.0061 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 330 | 0.1936 | 0.1962 | -0.0026 ± 0.0009 | 0.5661 | 0.5733 | 0.5017 | 0.4864 | 0.5545 | -0.015 ± 0.0246 | -0.0133 (6) |
| 3-5 | 227 | 0.188 | 0.1866 | +0.0014 ± 0.0023 | 0.5518 | 0.5485 | 0.5009 | 0.4616 | 0.467 | -0.110 ± 0.0303 | -0.01 (1) |
| 5-10 | 466 | 0.2011 | 0.2001 | +0.0011 ± 0.0031 | 0.5903 | 0.5853 | 0.5103 | 0.4365 | 0.4614 | -0.088 ± 0.0215 | -0.01 (4) |
| 10-15 | 354 | 0.2147 | 0.2126 | +0.0021 ± 0.0061 | 0.6193 | 0.6089 | 0.5371 | 0.4147 | 0.4689 | -0.079 ± 0.0243 | -0.044 (5) |
| 15-25 | 428 | 0.2291 | 0.208 | +0.0211 ± 0.0086 | 0.6581 | 0.6007 | 0.5787 | 0.3853 | 0.4276 | -0.106 ± 0.0218 | -0.03 (1) |
| 25-40 | 257 | 0.2028 | 0.2044 | -0.0016 ± 0.0164 | 0.5887 | 0.5869 | 0.6517 | 0.3406 | 0.4942 | -0.048 ± 0.0242 | 0.0 (1) |
| 40+ | 48 | 0.3114 | 0.1729 | +0.1385 ± 0.0545 | 0.836 | 0.5193 | 0.7473 | 0.2942 | 0.375 | -0.138 ± 0.0544 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1529 | 0.1817 | 0.1826 | -0.0009 ± 0.0004 | 0.5366 | 0.5384 | 0.4825 | 0.4672 | 0.4964 | -0.028 ± 0.011 | -0.0183 (23) |
| 3-5 | 1056 | 0.1864 | 0.1838 | +0.0026 ± 0.0011 | 0.5483 | 0.5423 | 0.4757 | 0.4364 | 0.4233 | -0.079 ± 0.0137 | -0.0243 (7) |
| 5-10 | 2401 | 0.1901 | 0.1855 | +0.0046 ± 0.0013 | 0.5637 | 0.548 | 0.4799 | 0.406 | 0.4123 | -0.057 ± 0.0089 | -0.01 (18) |
| 10-15 | 1828 | 0.1966 | 0.18 | +0.0166 ± 0.0025 | 0.5781 | 0.5284 | 0.4917 | 0.3686 | 0.3616 | -0.078 ± 0.0098 | -0.03 (9) |
| 15-25 | 2453 | 0.2082 | 0.1687 | +0.0395 ± 0.0032 | 0.6112 | 0.5007 | 0.4951 | 0.2996 | 0.2976 | -0.073 ± 0.0083 | -0.03 (2) |
| 25-40 | 1883 | 0.2118 | 0.1175 | +0.0943 ± 0.005 | 0.6142 | 0.3657 | 0.5213 | 0.2038 | 0.2172 | -0.058 ± 0.0075 | 0.0 (1) |
| 40+ | 1251 | 0.3854 | 0.0457 | +0.3397 ± 0.0068 | 1.0067 | 0.1797 | 0.63 | 0.107 | 0.0552 | -0.087 ± 0.0058 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 617 | 0.2034 | 0.2036 | -0.0002 ± 0.0006 | 0.5903 | 0.5903 | 0.5017 | 0.4868 | 0.4911 | -0.045 ± 0.0181 | -0.0226 (46) |
| 3-5 | 460 | 0.1983 | 0.1967 | +0.0017 ± 0.0017 | 0.5779 | 0.5721 | 0.4804 | 0.4408 | 0.4391 | -0.057 ± 0.0207 | -0.0058 (33) |
| 5-10 | 936 | 0.1932 | 0.1877 | +0.0055 ± 0.0021 | 0.5708 | 0.5562 | 0.4785 | 0.4049 | 0.406 | -0.060 ± 0.0144 | -0.0049 (73) |
| 10-15 | 609 | 0.2031 | 0.1935 | +0.0097 ± 0.0045 | 0.5946 | 0.5685 | 0.489 | 0.3662 | 0.3875 | -0.044 ± 0.0178 | 0.0014 (64) |
| 15-25 | 814 | 0.2351 | 0.2086 | +0.0265 ± 0.0063 | 0.6692 | 0.6026 | 0.5506 | 0.3563 | 0.387 | -0.058 ± 0.0161 | -0.0216 (58) |
| 25-40 | 457 | 0.2445 | 0.1865 | +0.0580 ± 0.0125 | 0.6889 | 0.5467 | 0.6306 | 0.3176 | 0.3786 | -0.077 ± 0.0188 | -0.0216 (25) |
| 40+ | 152 | 0.3536 | 0.1875 | +0.1661 ± 0.0358 | 1.0093 | 0.5536 | 0.781 | 0.2877 | 0.3882 | -0.061 ± 0.0323 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1888 | 0.1932 | 0.193 | +0.0002 ± 0.0004 | 0.5638 | 0.5623 | 0.5035 | 0.4882 | 0.4883 | -0.043 ± 0.0101 | -0.0155 (82) |
| 3-5 | 1318 | 0.1893 | 0.1862 | +0.0031 ± 0.0009 | 0.5535 | 0.5465 | 0.492 | 0.4525 | 0.4355 | -0.063 ± 0.0119 | -0.0148 (63) |
| 5-10 | 2683 | 0.1911 | 0.1829 | +0.0082 ± 0.0012 | 0.5661 | 0.5433 | 0.475 | 0.4012 | 0.3869 | -0.067 ± 0.0084 | -0.0087 (125) |
| 10-15 | 1820 | 0.1995 | 0.1856 | +0.0139 ± 0.0025 | 0.5858 | 0.5494 | 0.5017 | 0.3785 | 0.3835 | -0.054 ± 0.01 | -0.0053 (105) |
| 15-25 | 2330 | 0.23 | 0.1965 | +0.0335 ± 0.0036 | 0.6643 | 0.5721 | 0.5449 | 0.3498 | 0.3631 | -0.061 ± 0.0093 | -0.0255 (106) |
| 25-40 | 1593 | 0.2416 | 0.1614 | +0.0802 ± 0.0063 | 0.6877 | 0.4806 | 0.5927 | 0.2785 | 0.3095 | -0.064 ± 0.0097 | -0.0206 (47) |
| 40+ | 760 | 0.367 | 0.1165 | +0.2505 ± 0.0131 | 1.0088 | 0.3622 | 0.687 | 0.1811 | 0.1961 | -0.062 ± 0.0116 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2110 | 1.053 ± 0.061 | 1.17 | 0.1701 | 0.1709 | 0.2114 | 0.2016 |
| gen2 | 2110 | 0.854 ± 0.054 | 1.106 | 0.1867 | 0.1702 | 0.2293 | 0.2017 |
| gen1_elo | 2110 | 1.055 ± 0.06 | 1.158 | 0.1742 | 0.1714 | 0.2092 | 0.2016 |
| gen1_sr | 2110 | 1.044 ± 0.069 | 1.178 | 0.1445 | 0.1727 | 0.2242 | 0.2015 |
| gen1_ledger | 4045 | 0.901 ± 0.04 | 1.066 | 0.1735 | 0.1901 | 0.2171 | 0.1961 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 11,089)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,042 | 27.4% |
| STALE_QUOTE | market_freshness | 2,248 | 20.3% |
| BOOK_QUALITY | execution | 1,904 | 17.2% |
| POOR_DATA | data | 1,183 | 10.7% |
| LIMITED_DATA | data | 862 | 7.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 602 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 500 | 4.5% |
| IDENTITY_AMBIGUOUS | mapping | 352 | 3.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 333 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 63 | 0.6% |

Cause class: coverage 27.4%, market_freshness 20.3%, data 18.4%, execution 17.2%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.5%, mapping 3.2%, model_calibration 0.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.1%, START_UNVERIFIABLE 96.1%, LOW_DATA_QUALITY 68.4%, STALE_PLAYER_DATA 57.0%, THIN_PLAYER_HISTORY 56.4%, STALE_KALSHI_QUOTE 47.4%, MODEL_INTERNAL_DISAGREEMENT 37.1%, ASYMMETRIC_SAMPLE_SIZE 30.0%, WIDE_SPREAD 23.0%, MODEL_HIGH_UNCERTAINTY 16.4%, PLAYER_IDENTITY_RISK 11.5%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.3%, MODEL_CALIBRATION_OUTLIER 3.4%, EXTERNAL_MARKET_REJECTION 0.9%, UNKNOWN 0.6%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 30.0%, POST_SETTLEMENT_OBSERVATION 27.4%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,039)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,390 | 39.6% |
| BOOK_QUALITY | execution | 1,008 | 16.7% |
| STALE_QUOTE | market_freshness | 1,004 | 16.6% |
| POOR_DATA | data | 482 | 8.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 329 | 5.5% |
| LIMITED_DATA | data | 262 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 223 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 208 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 114 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 19 | 0.3% |

Cause class: coverage 39.6%, execution 16.7%, market_freshness 16.6%, data 12.3%, market_freshness/coverage 8.9%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.5%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.3%, THIN_PLAYER_HISTORY 58.0%, STALE_KALSHI_QUOTE 55.2%, STALE_PLAYER_DATA 51.5%, MODEL_INTERNAL_DISAGREEMENT 38.4%, ASYMMETRIC_SAMPLE_SIZE 31.7%, WIDE_SPREAD 22.7%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 14.6%, EVENT_MAPPING_RISK 9.9%, LOW_DISPLAYED_LIQUIDITY 7.5%, LEVEL_TRANSFER_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 4.3%, EXTERNAL_MARKET_REJECTION 0.5%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.5%, POST_SETTLEMENT_OBSERVATION 39.6%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4994, "IDENTITY_AMBIGUOUS": 1045}; ticker orientation: {"VERIFIED": 6039}.

Checks: discipline:AMBIGUOUS 435, discipline:PASS 5604, identity_confidence:AMBIGUOUS 882, identity_confidence:PASS 5157, level_mapping:NA 447, level_mapping:PASS 5592, market_pair:AMBIGUOUS 221, market_pair:NA 135, market_pair:PASS 5683, model_complement:NA 102, model_complement:PASS 5937, namesake:PASS 6039, physical_match_id:NA 2496, physical_match_id:PASS 3543, player_ids:PASS 6039, same_pair_other_event:PASS 6039, ticker_orientation:PASS 6039

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,810 | 1.6% | 1.6% | 0.5% | {"market_freshness": 20, "execution": 8} | 5.34 | 0.214 / 0.2056 (181) | 17.5% | 0.1% | 6.0% | 1.6% |
| CHALLENGER | 3,911 | 18.4% | 6.0% | 11.9% | {"coverage": 453, "market_freshness": 107, "market_freshness/coverage": 87, "model_calibration_or_unknown": 39, "data": 25, "execution": 4, "model_calibration": 3} | 6.62 | 0.2248 / 0.206 (932) | 44.6% | 4.6% | 1.6% | 23.8% |
| DOUBLES | 848 | 51.3% | 51.0% | 7.2% | {"execution": 163, "mapping": 130, "market_freshness": 106, "market_freshness/coverage": 29, "coverage": 7} | 25.63 | 0.3145 / 0.2288 (232) | 27.6% | 0.0% | 100.0% | 7.7% |
| ITF_MEN | 8,143 | 23.4% | 15.4% | 31.6% | {"coverage": 793, "execution": 387, "data": 272, "market_freshness": 270, "market_freshness/coverage": 166, "mapping": 19, "model_calibration_or_unknown": 2} | 10.34 | 0.2102 / 0.1937 (2017) | 37.9% | 53.2% | 6.3% | 24.2% |
| ITF_WOMEN | 10,509 | 26.0% | 17.5% | 45.2% | {"coverage": 1120, "market_freshness": 442, "execution": 429, "data": 423, "market_freshness/coverage": 214, "mapping": 68, "model_calibration_or_unknown": 23, "model_calibration": 9} | 12.15 | 0.204 / 0.1917 (2271) | 38.9% | 56.9% | 9.5% | 24.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,138 | 7.7% | 6.8% | 1.5% | {"market_freshness": 35, "model_calibration_or_unknown": 20, "data": 11, "market_freshness/coverage": 9, "model_calibration": 4, "execution": 4, "coverage": 4, "mapping": 1} | 7.91 | 0.2207 / 0.2154 (175) | 30.0% | 1.8% | 1.1% | 3.0% |
| WTA125 | 880 | 13.8% | 10.0% | 2.0% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 22, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 3} | 9.81 | 0.2338 / 0.2168 (305) | 25.0% | 6.0% | 3.9% | 11.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 9 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 10 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 11 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 13 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 14 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 15 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 18 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 19 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 21 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 22 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 23 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 24 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 25 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 27 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 28 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 29 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 30 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 31 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 32 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 33 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 34 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 35 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 38 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 40 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 41 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 42 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 26 min (AGING); no external reference |
| 43 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 44 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 45 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 46 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 47 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.9h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 780 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |
| 48 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 770 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9807, "by_level_share_of_ge_25pp": {"ATP": 0.0046, "CHALLENGER": 0.1189, "DOUBLES": 0.072, "ITF_MEN": 0.3161, "ITF_WOMEN": 0.4517, "OTHER": 0.002, "WTA": 0.0146, "WTA125": 0.02}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5524, "share_primary_cause_market_settled_or_in_play": 0.4847, "share_primary_cause_stale_quote_only": 0.1663}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6039, "identity_ambiguous_share": 0.173, "ticker_orientation": {"VERIFIED": 6039}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3543, "with_external": 82, "coverage": 0.0231, "external_status": {"EXTERNAL_STALE": 60, "AGREES_WITH_KALSHI": 22}, "triangulation": {"INSUFFICIENT_INPUTS": 60, "MODEL_LONE_OUTLIER": 22}, "share_external_agrees_with_kalshi": 0.2683, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1511, "with_external": 80, "coverage": 0.0529, "external_status": {"EXTERNAL_STALE": 58, "AGREES_WITH_KALSHI": 22}, "triangulation": {"INSUFFICIENT_INPUTS": 58, "MODEL_LONE_OUTLIER": 22}, "share_external_agrees_with_kalshi": 0.275, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 644.5, "median_sample_ratio": 2.28, "median_min_matches": 21.0, "median_max_days_since_last": 196.0, "share_severe_asymmetry": 0.1704, "data_status": {"POOR": 3061, "LIMITED": 1861, "ADEQUATE": 1117}, "comparison_lt_10pp": {"median_thinner_serve_points": 1884.0, "median_sample_ratio": 1.68, "median_min_matches": 85.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 460, "model_minus_observed": 0.0608, "kalshi_minus_observed": -0.0715, "brier_diff_model_minus_kalshi": 0.0042}, "4-10x": {"n": 319, "model_minus_observed": 0.0578, "kalshi_minus_observed": -0.0831, "brier_diff_model_minus_kalshi": -0.0013}, "<2x": {"n": 1032, "model_minus_observed": 0.0885, "kalshi_minus_observed": -0.034, "brier_diff_model_minus_kalshi": 0.0137}, ">=10x": {"n": 299, "model_minus_observed": 0.1119, "kalshi_minus_observed": -0.0577, "brier_diff_model_minus_kalshi": 0.0163}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2110, "model": {"intercept": -0.564, "slope": 0.854, "slope_se": 0.054}, "kalshi_mid_same_rows": {"intercept": 0.199, "slope": 1.106, "slope_se": 0.062}, "mean_extremity_model": 0.1867, "mean_extremity_kalshi": 0.1702, "model_brier": 0.2293, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0276, "brier_diff_se": 0.0041, "model_logloss": 0.6552, "kalshi_logloss": 0.5857}, "fair_v1": {"n": 2110, "model": {"intercept": -0.405, "slope": 1.053, "slope_se": 0.061}, "kalshi_mid_same_rows": {"intercept": 0.312, "slope": 1.17, "slope_se": 0.064}, "mean_extremity_model": 0.1701, "mean_extremity_kalshi": 0.1709, "model_brier": 0.2114, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0097, "brier_diff_se": 0.0033, "model_logloss": 0.6102, "kalshi_logloss": 0.5853}, "gen1_elo": {"n": 2110, "model": {"intercept": -0.38, "slope": 1.055, "slope_se": 0.06}, "kalshi_mid_same_rows": {"intercept": 0.318, "slope": 1.158, "slope_se": 0.063}, "mean_extremity_model": 0.1742, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2092, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0076, "brier_diff_se": 0.0032, "model_logloss": 0.6064, "kalshi_logloss": 0.5852}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2457, "share_ge_15": 0.4289, "median_abs_gap": 12.79, "n": 14422}, "gen1_elo": {"share_ge_25": 0.2379, "share_ge_15": 0.4259, "median_abs_gap": 12.29, "n": 14422}, "gen1_sr": {"share_ge_25": 0.298, "share_ge_15": 0.5123, "median_abs_gap": 15.43, "n": 14422}, "gen2": {"share_ge_25": 0.3018, "share_ge_15": 0.5006, "median_abs_gap": 15.02, "n": 14422}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1395, "share_ge_15": 0.3267, "median_abs_gap": 10.25, "n": 10829}, "gen1_elo": {"share_ge_25": 0.1354, "share_ge_15": 0.3202, "median_abs_gap": 9.62, "n": 10828}, "gen1_sr": {"share_ge_25": 0.1922, "share_ge_15": 0.4204, "median_abs_gap": 12.56, "n": 10829}, "gen2": {"share_ge_25": 0.2102, "share_ge_15": 0.4226, "median_abs_gap": 12.48, "n": 10830}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.34, "share_ge_25_all": 0.0155, "share_ge_25_pregame_clean": 0.0157}, "WTA": {"median_abs_gap_pregame_clean": 7.91, "share_ge_25_all": 0.0773, "share_ge_25_pregame_clean": 0.0679}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2411, "share_within_10pp_all": 0.4407, "share_within_10pp_pregame_clean": 0.5051, "corr_model_vs_mid_pregame_clean": 0.8504}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 325, "model_brier": 0.1936, "kalshi_brier": 0.195, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 384, "model_brier": 0.2128, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0072}, "15-25": {"n_settled": 446, "model_brier": 0.2287, "kalshi_brier": 0.2119, "brier_diff_model_minus_kalshi": 0.0168}, "25-40": {"n_settled": 254, "model_brier": 0.2218, "kalshi_brier": 0.2009, "brier_diff_model_minus_kalshi": 0.0208}, "3-5": {"n_settled": 218, "model_brier": 0.1884, "kalshi_brier": 0.1903, "brier_diff_model_minus_kalshi": -0.0019}, "40+": {"n_settled": 55, "model_brier": 0.2888, "kalshi_brier": 0.1716, "brier_diff_model_minus_kalshi": 0.1171}, "5-10": {"n_settled": 428, "model_brier": 0.2011, "kalshi_brier": 0.2026, "brier_diff_model_minus_kalshi": -0.0015}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.564, "slope": 0.854, "slope_se": 0.054}, "kalshi_slope": {"intercept": 0.199, "slope": 1.106, "slope_se": 0.062}, "n": 2110}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.536, "slope": 0.901, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.128, "slope": 1.066, "slope_se": 0.043}, "n": 4045}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 232, "model_brier": 0.3145, "kalshi_brier": 0.2288, "brier_diff_model_minus_kalshi": 0.0857, "brier_diff_se": 0.0207, "corr_model_outcome": 0.0124, "corr_kalshi_outcome": 0.3121}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
