# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-20T17:56Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 44,621): 0-3 14.2%, 3-5 9.5%, 5-10 19.7%, 10-15 15.4%, 15-25 19.3%, 25-40 13.9%, 40+ 8.0%; median gap 12.0 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.7%, Challenger 12.6%, doubles 6.9%). Main tour: ATP 4.9% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 9,775): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.2%, BOOK_QUALITY 19.1%, STALE_QUOTE 17.7%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.9%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%. By class: coverage 34.2%, execution 19.1%, market_freshness 17.7%, data 13.0%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.2%, model_calibration 0.8%.
* **Stale / settled / in-play**: 51.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 9,775 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 24.9% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 509.0 points vs 1754.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.049, Gen-2 0.847, Gen-1 ledger 0.877 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 467 model 0.2236 vs Kalshi 0.2105; n 92 model 0.3021 vs Kalshi 0.176.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 190,598 model-market comparisons (309,428 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 65,834 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-20T17:42:04.928724+00:00'], shadow board 50,017 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-20T17:42:10.174956+00:00'], Model 4 23,907 rows, 17,613 settled tickers, 5,959 tickers with an external scan.
* By model: {"gen1_ledger": 44442, "gen1_elo": 25148, "fair_v1": 25148, "gen2": 25148, "gen1_sr": 25148, "model4_fundamental": 22794, "model4_conditioned": 22770}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 44,621 | 14.2 | 9.5 | 19.7 | 15.4 | 19.3 | 13.9 | 8.0 | 12.0 | 41.2% | 21.9% |
| MW fair_v1 | 25,148 | 13.2 | 8.6 | 18.2 | 15.7 | 19.9 | 14.8 | 9.5 | 13.09 | 44.2% | 24.3% |
| MW gen1_elo | 25,148 | 12.9 | 8.8 | 19.2 | 15.2 | 19.8 | 14.8 | 9.2 | 12.79 | 43.8% | 24.0% |
| MW gen1_ledger | 19,473 | 15.4 | 10.7 | 21.7 | 14.9 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| MW gen1_sr | 25,148 | 10.0 | 7.2 | 16.7 | 14.1 | 21.4 | 18.6 | 12.0 | 15.77 | 52.0% | 30.6% |
| MW gen2 | 25,148 | 11.2 | 7.4 | 16.2 | 14.2 | 20.1 | 17.7 | 13.2 | 15.49 | 51.0% | 30.9% |
| all families model4_conditioned | 22,770 | 21.8 | 19.2 | 34.3 | 17.7 | 4.6 | 1.4 | 1.1 | 5.93 | 7.0% | 2.4% |
| all families model4_fundamental | 22,794 | 16.2 | 13.0 | 34.1 | 20.5 | 11.4 | 3.4 | 1.4 | 7.91 | 16.2% | 4.8% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.6%, >=15pp 41.2%, >=20pp 30.5%, >=25pp 21.9%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.39pp; >=10pp 45.0%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,222 | 28.4 | 13.8 | 24.6 | 15.3 | 12.2 | 5.1 | 0.6 | 6.33 | 17.9% | 5.7% |
| CHALLENGER | 4,224 | 15.6 | 10.1 | 20.2 | 15.8 | 15.0 | 12.5 | 10.8 | 11.23 | 38.2% | 23.2% |
| ITF_MEN | 6,637 | 10.9 | 7.8 | 17.0 | 14.5 | 20.8 | 16.9 | 12.1 | 14.96 | 49.9% | 29.1% |
| ITF_WOMEN | 9,867 | 9.8 | 6.8 | 15.5 | 15.6 | 23.1 | 18.2 | 11.1 | 15.79 | 52.4% | 29.3% |
| WTA | 1,538 | 17.4 | 12.4 | 24.2 | 20.3 | 20.6 | 4.4 | 0.7 | 8.85 | 25.7% | 5.1% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,222 | 23.2 | 15.0 | 24.5 | 17.2 | 14.0 | 5.2 | 0.9 | 6.83 | 20.1% | 6.1% |
| CHALLENGER | 4,224 | 14.5 | 8.5 | 18.9 | 14.5 | 17.9 | 14.0 | 11.8 | 12.67 | 43.7% | 25.8% |
| ITF_MEN | 6,637 | 9.0 | 6.5 | 15.1 | 13.3 | 19.7 | 20.2 | 16.2 | 17.66 | 56.1% | 36.4% |
| ITF_WOMEN | 9,867 | 8.2 | 5.6 | 13.4 | 13.5 | 21.6 | 20.9 | 16.7 | 18.93 | 59.3% | 37.6% |
| WTA | 1,538 | 14.6 | 9.5 | 19.9 | 16.5 | 24.4 | 14.2 | 0.8 | 11.71 | 39.5% | 15.0% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,222 | 23.7 | 13.1 | 24.5 | 16.0 | 15.2 | 6.4 | 1.0 | 7.26 | 22.7% | 7.5% |
| CHALLENGER | 4,224 | 14.2 | 9.6 | 21.1 | 15.2 | 16.1 | 12.7 | 11.1 | 11.34 | 39.9% | 23.8% |
| ITF_MEN | 6,637 | 10.1 | 7.8 | 17.3 | 13.9 | 21.4 | 17.3 | 12.2 | 15.39 | 50.9% | 29.5% |
| ITF_WOMEN | 9,867 | 9.4 | 6.8 | 16.2 | 15.7 | 23.3 | 18.5 | 10.2 | 15.74 | 51.9% | 28.6% |
| WTA | 1,538 | 24.3 | 16.6 | 30.2 | 15.9 | 10.2 | 2.2 | 0.5 | 6.01 | 12.9% | 2.7% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,265 | 26.6 | 19.8 | 29.6 | 11.9 | 8.5 | 3.1 | 0.4 | 5.38 | 12.0% | 3.5% |
| CHALLENGER | 2,955 | 21.2 | 14.6 | 26.9 | 14.1 | 14.8 | 6.4 | 1.9 | 7.29 | 23.2% | 8.4% |
| DOUBLES | 1,382 | 4.7 | 4.0 | 11.5 | 10.4 | 20.8 | 25.9 | 22.6 | 24.13 | 69.3% | 48.5% |
| ITF_MEN | 5,422 | 14.2 | 8.8 | 20.6 | 15.9 | 20.4 | 13.3 | 6.8 | 11.96 | 40.6% | 20.2% |
| ITF_WOMEN | 6,561 | 12.2 | 8.9 | 19.2 | 15.2 | 21.8 | 16.6 | 6.1 | 13.04 | 44.5% | 22.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,007 | 22.1 | 15.8 | 29.7 | 18.1 | 10.3 | 3.7 | 0.3 | 7.03 | 14.3% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,170 | 28.6 | 14.0 | 24.9 | 15.2 | 11.9 | 4.8 | 0.6 | 6.17 | 17.3% | 5.4% |
| CHALLENGER | 2,999 | 20.3 | 12.4 | 24.9 | 18.2 | 15.4 | 6.6 | 2.1 | 8.43 | 24.1% | 8.7% |
| ITF_MEN | 4,872 | 13.3 | 9.5 | 20.2 | 16.4 | 21.4 | 13.8 | 5.4 | 12.02 | 40.6% | 19.2% |
| ITF_WOMEN | 7,403 | 11.5 | 8.1 | 17.6 | 17.8 | 24.8 | 15.3 | 4.9 | 13.52 | 45.1% | 20.3% |
| WTA | 1,497 | 17.6 | 12.2 | 24.2 | 20.4 | 20.6 | 4.3 | 0.7 | 8.85 | 25.7% | 5.1% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,170 | 23.5 | 15.2 | 24.6 | 17.1 | 13.9 | 5.0 | 0.7 | 6.67 | 19.6% | 5.7% |
| CHALLENGER | 2,999 | 18.2 | 10.9 | 23.5 | 17.3 | 18.1 | 9.7 | 2.3 | 9.4 | 30.2% | 12.1% |
| ITF_MEN | 4,873 | 10.6 | 7.7 | 17.4 | 15.0 | 21.8 | 18.2 | 9.3 | 14.71 | 49.2% | 27.4% |
| ITF_WOMEN | 7,403 | 9.2 | 6.4 | 14.7 | 15.0 | 23.8 | 20.4 | 10.6 | 16.71 | 54.7% | 31.0% |
| WTA | 1,497 | 14.6 | 9.5 | 19.8 | 16.4 | 24.4 | 14.4 | 0.8 | 11.74 | 39.7% | 15.2% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,225 | 26.8 | 20.1 | 29.7 | 12.2 | 8.1 | 2.9 | 0.2 | 5.33 | 11.3% | 3.2% |
| CHALLENGER | 2,578 | 22.6 | 15.8 | 28.6 | 14.0 | 14.1 | 4.3 | 0.6 | 6.72 | 19.0% | 4.9% |
| DOUBLES | 1,285 | 4.8 | 4.2 | 11.7 | 10.6 | 20.8 | 26.1 | 21.9 | 24.07 | 68.8% | 48.0% |
| ITF_MEN | 4,518 | 15.5 | 9.5 | 22.4 | 16.6 | 20.1 | 11.7 | 4.1 | 10.77 | 35.9% | 15.8% |
| ITF_WOMEN | 5,470 | 13.0 | 9.4 | 20.7 | 16.0 | 22.0 | 15.4 | 3.5 | 11.85 | 40.9% | 18.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 960 | 22.6 | 16.2 | 29.8 | 18.1 | 10.3 | 2.9 | 0.0 | 6.83 | 13.2% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,382 | 4.7 | 4.0 | 11.5 | 10.4 | 20.8 | 25.9 | 22.6 | 24.13 | 69.3% | 48.5% |
| singles | 18,091 | 16.2 | 11.2 | 22.4 | 15.3 | 18.3 | 11.8 | 4.7 | 10.03 | 34.9% | 16.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,664 | 13.4 | 8.9 | 19.2 | 15.7 | 18.7 | 14.7 | 9.5 | 12.7 | 42.8% | 24.1% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 15,948 | 13.5 | 8.6 | 18.2 | 15.4 | 20.2 | 14.6 | 9.4 | 13.1 | 44.2% | 24.1% |
| UNKNOWN | 3,299 | 11.6 | 8.0 | 16.6 | 17.4 | 20.6 | 15.8 | 10.1 | 13.67 | 46.5% | 25.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,271 | 19.7 | 11.4 | 21.1 | 16.9 | 16.0 | 8.9 | 5.9 | 9.34 | 30.9% | 14.8% |
| B | 3,228 | 12.6 | 9.1 | 20.0 | 17.2 | 18.8 | 12.0 | 10.3 | 12.14 | 41.1% | 22.3% |
| C | 3,527 | 12.3 | 8.8 | 18.8 | 14.8 | 19.8 | 15.5 | 10.0 | 13.24 | 45.2% | 25.5% |
| D | 4,123 | 12.2 | 7.9 | 16.8 | 15.6 | 22.1 | 15.9 | 9.5 | 14.05 | 47.5% | 25.4% |
| F | 6,999 | 7.9 | 5.6 | 15.0 | 14.4 | 23.3 | 21.2 | 12.6 | 17.79 | 57.0% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,575 | 23.2 | 15.8 | 28.5 | 15.1 | 11.8 | 4.1 | 1.5 | 6.68 | 17.3% | 5.6% |
| B | 2,727 | 15.9 | 10.5 | 24.1 | 16.1 | 18.8 | 10.8 | 3.9 | 9.92 | 33.5% | 14.7% |
| C | 3,828 | 10.9 | 7.2 | 18.5 | 14.4 | 21.8 | 16.3 | 10.9 | 14.48 | 49.0% | 27.2% |
| D | 2,802 | 13.9 | 9.7 | 19.7 | 14.7 | 21.0 | 14.7 | 6.2 | 12.11 | 41.9% | 20.9% |
| F | 4,541 | 10.3 | 8.0 | 15.7 | 14.6 | 22.2 | 20.6 | 8.6 | 15.74 | 51.4% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,256 | 17.9 | 10.3 | 20.5 | 16.9 | 16.4 | 9.7 | 8.3 | 10.39 | 34.5% | 18.0% |
| LIMITED | 5,544 | 14.0 | 10.2 | 20.0 | 15.6 | 19.2 | 13.6 | 7.4 | 11.77 | 40.2% | 21.0% |
| POOR | 11,348 | 9.5 | 6.5 | 15.8 | 15.0 | 22.8 | 19.1 | 11.4 | 16.1 | 53.2% | 30.5% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,859 | 26.7 | 20.9 | 34.4 | 11.9 | 4.3 | 1.5 | 0.2 | 5.2 | 6.0% | 1.7% |
| GAME_SPREAD | 4,238 | 23.0 | 15.3 | 33.5 | 17.1 | 8.6 | 2.3 | 0.3 | 6.54 | 11.2% | 2.6% |
| MATCH_WINNER | 19,473 | 15.4 | 10.7 | 21.7 | 14.9 | 18.5 | 12.8 | 6.0 | 10.54 | 37.3% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,978 | 29.9 | 16.9 | 30.4 | 12.7 | 8.1 | 1.6 | 0.4 | 5.4 | 10.2% | 2.0% |
| TOTAL_GAMES | 6,870 | 7.9 | 9.2 | 36.5 | 29.2 | 10.9 | 3.4 | 2.8 | 9.6 | 17.2% | 6.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,966 | 25.3 | 34.6 | 32.1 | 4.0 | 3.2 | 0.6 | 0.1 | 4.45 | 3.9% | 0.7% |
| GAME_SPREAD | 5,454 | 46.0 | 17.0 | 26.8 | 7.6 | 1.8 | 0.6 | 0.2 | 3.39 | 2.6% | 0.8% |
| TOTAL_GAMES | 9,350 | 4.7 | 7.3 | 40.6 | 35.2 | 7.3 | 2.4 | 2.3 | 9.73 | 12.1% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,969 | 24.2 | 17.8 | 35.4 | 12.4 | 7.3 | 2.6 | 0.3 | 5.82 | 10.2% | 2.9% |
| GAME_SPREAD | 5,457 | 19.1 | 13.2 | 28.3 | 19.9 | 14.4 | 4.2 | 0.9 | 7.97 | 19.5% | 5.1% |
| TOTAL_GAMES | 9,368 | 7.8 | 8.8 | 36.4 | 27.7 | 13.1 | 3.7 | 2.5 | 9.67 | 19.3% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 25,148 | 44.2% | 24.3% | 13.09 | 35.9% | 15.2% | 10.91 |
| gen1_elo | 25,148 | 43.8% | 24.0% | 12.79 | 35.2% | 15.3% | 10.5 |
| gen1_sr | 25,148 | 52.0% | 30.6% | 15.77 | 44.4% | 21.5% | 13.11 |
| gen2 | 25,148 | 51.0% | 30.9% | 15.49 | 44.5% | 23.1% | 13.1 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 13,342 | 15.9 | 10.3 | 21.0 | 17.4 | 20.4 | 11.7 | 3.3 | 10.78 | 35.3% | 14.9% |
| STALE | 11,806 | 10.2 | 6.6 | 15.1 | 13.9 | 19.4 | 18.3 | 16.5 | 17.1 | 54.2% | 34.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 12,941 | 16.6 | 11.2 | 22.7 | 15.0 | 17.5 | 12.2 | 4.8 | 9.86 | 34.5% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 44,621 | 12941 | 16814 | 14866 | 23.7 | 129.1 | 1400.4 |
| ge_15pp | 18,383 | 4466 | 6004 | 7913 | 25.7 | 421.8 | 1380.4 |
| ge_25pp | 9,775 | 2202 | 2585 | 4988 | 31.3 | 562.2 | 1380.4 |
| lt_10pp | 19,378 | 6535 | 7940 | 4903 | 21.7 | 47.3 | 1341.5 |

Current slate `SL-20261020T175601Z-c1d387d7`: 649 priced rows, quote age at build {'median': 14.3, 'max': 14.3}, freshness {'AGING': 649}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 12 | 0.0 | 0.0 | 33.3 | 0.0 | 50.0 | 16.7 | 0.0 | 20.33 | 66.7% | 16.7% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,352 | 20.0 | 10.9 | 23.3 | 18.8 | 19.2 | 7.1 | 0.7 | 9.1 | 27.0% | 7.7% |
| KALSHI_LONE_OUTLIER | 14 | 7.1 | 7.1 | 71.4 | 0.0 | 7.1 | 7.1 | 0.0 | 5.35 | 14.3% | 7.1% |
| MARKETS_AGREE | 422 | 68.2 | 31.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.12 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 935 | 0.0 | 2.6 | 34.1 | 27.2 | 25.4 | 9.9 | 0.8 | 12.5 | 36.1% | 10.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 25,148 | 3747 (14.9%) | 24.9% | 0.7% | {"EXTERNAL_STALE": 2352, "AGREES_WITH_KALSHI": 935, "ALL_AGREE": 422, "AGREES_WITH_MODEL": 14, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 11, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 11,118 | 982 (8.8%) | 34.4% | 1.0% | {"EXTERNAL_STALE": 634, "AGREES_WITH_KALSHI": 338, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,111 | 285 (4.7%) | 35.1% | 1.1% | {"EXTERNAL_STALE": 182, "AGREES_WITH_KALSHI": 100, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,983 | 270 (9.0%) | 36.3% | 1.1% | {"EXTERNAL_STALE": 169, "AGREES_WITH_KALSHI": 98, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 10,074 | 2068 (20.5%) | 16.6% | 0.7% | {"EXTERNAL_STALE": 1275, "ALL_AGREE": 422, "AGREES_WITH_KALSHI": 343, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 12, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,861 | 10.7 | 7.7 | 19.4 | 14.7 | 22.1 | 15.6 | 9.8 | 13.93 | 47.5% | 25.5% |
| 4-10x | 3,274 | 11.6 | 8.4 | 18.5 | 15.6 | 20.9 | 14.9 | 10.0 | 13.62 | 45.9% | 24.9% |
| <2x | 12,947 | 15.3 | 9.6 | 18.7 | 16.8 | 18.2 | 13.0 | 8.4 | 11.87 | 39.7% | 21.4% |
| >=10x | 4,066 | 11.1 | 6.5 | 15.3 | 13.8 | 21.8 | 19.4 | 12.2 | 16.35 | 53.4% | 31.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,401 | 12.6 | 8.4 | 19.6 | 16.2 | 19.7 | 13.5 | 9.9 | 12.84 | 43.2% | 23.5% |
| 300-1000 | 5,487 | 11.9 | 8.7 | 16.7 | 15.6 | 21.0 | 16.4 | 9.8 | 14.0 | 47.1% | 26.2% |
| <300 | 7,879 | 9.0 | 5.9 | 15.3 | 14.6 | 22.9 | 20.1 | 12.1 | 16.92 | 55.2% | 32.3% |
| >=3000 | 5,381 | 21.5 | 12.6 | 22.6 | 16.9 | 14.6 | 6.9 | 4.8 | 8.09 | 26.4% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 748 | 0.544 | 0.4091 | 0.4987 | +0.045 | -0.090 | -0.0021 ± 0.0055 |
| ratio 4-10x | 513 | 0.5908 | 0.4454 | 0.5029 | +0.088 | -0.058 | 0.0127 ± 0.0071 |
| ratio <2x | 1834 | 0.5368 | 0.415 | 0.4509 | +0.086 | -0.036 | 0.012 ± 0.0033 |
| ratio >=10x | 634 | 0.5641 | 0.3903 | 0.4574 | +0.107 | -0.067 | 0.0086 ± 0.0073 |
| thinner_sample 1000-3000 | 1021 | 0.5431 | 0.4178 | 0.4554 | +0.088 | -0.038 | 0.0094 ± 0.0044 |
| thinner_sample 300-1000 | 873 | 0.5655 | 0.4244 | 0.5006 | +0.065 | -0.076 | -0.0003 ± 0.0054 |
| thinner_sample <300 | 1206 | 0.5543 | 0.3895 | 0.4552 | +0.099 | -0.066 | 0.0126 ± 0.0051 |
| thinner_sample >=3000 | 629 | 0.5332 | 0.4392 | 0.4722 | +0.061 | -0.033 | 0.0126 ± 0.0046 |
| data_status ADEQUATE | 1074 | 0.5369 | 0.4327 | 0.4609 | +0.076 | -0.028 | 0.0111 ± 0.0038 |
| data_status LIMITED | 902 | 0.552 | 0.4209 | 0.4823 | +0.070 | -0.061 | 0.0046 ± 0.0049 |
| data_status POOR | 1753 | 0.5577 | 0.3986 | 0.4666 | +0.091 | -0.068 | 0.0093 ± 0.0041 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 560 | 0.1962 | 0.1976 | -0.0014 ± 0.0007 | 0.5708 | 0.5739 | 0.4995 | 0.4846 | 0.5375 | -0.049 ± 0.0196 | -0.01 (5) |
| 3-5 | 353 | 0.201 | 0.2008 | +0.0002 ± 0.0019 | 0.5851 | 0.5833 | 0.5054 | 0.4653 | 0.4816 | -0.086 ± 0.0246 | 0.02 (1) |
| 5-10 | 773 | 0.2003 | 0.2008 | -0.0006 ± 0.0024 | 0.5863 | 0.5857 | 0.5136 | 0.4391 | 0.4761 | -0.081 ± 0.0167 | -0.0167 (6) |
| 10-15 | 653 | 0.2125 | 0.2033 | +0.0092 ± 0.0044 | 0.6145 | 0.5878 | 0.5238 | 0.3996 | 0.4242 | -0.097 ± 0.0175 | -0.048 (5) |
| 15-25 | 831 | 0.2265 | 0.2147 | +0.0119 ± 0.0063 | 0.6481 | 0.6141 | 0.5779 | 0.3823 | 0.4501 | -0.087 ± 0.0159 | -0.0033 (9) |
| 25-40 | 467 | 0.2236 | 0.2105 | +0.0132 ± 0.0126 | 0.6351 | 0.6047 | 0.6537 | 0.3452 | 0.4754 | -0.069 ± 0.0193 | -0.01 (1) |
| 40+ | 92 | 0.3021 | 0.176 | +0.1261 ± 0.0392 | 0.8232 | 0.5249 | 0.7541 | 0.3058 | 0.3913 | -0.125 ± 0.0376 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2734 | 0.1817 | 0.1829 | -0.0012 ± 0.0003 | 0.5382 | 0.5397 | 0.4801 | 0.4649 | 0.5062 | -0.015 ± 0.0083 | -0.0129 (17) |
| 3-5 | 1794 | 0.1949 | 0.1939 | +0.0010 ± 0.0008 | 0.5708 | 0.5651 | 0.4837 | 0.4437 | 0.4504 | -0.051 ± 0.0106 | 0.0 (2) |
| 5-10 | 3814 | 0.1957 | 0.1924 | +0.0032 ± 0.0011 | 0.5738 | 0.5635 | 0.4859 | 0.412 | 0.4263 | -0.048 ± 0.0072 | -0.0119 (21) |
| 10-15 | 3319 | 0.2025 | 0.1837 | +0.0189 ± 0.0019 | 0.5926 | 0.5403 | 0.4854 | 0.361 | 0.3474 | -0.077 ± 0.0074 | -0.0281 (16) |
| 15-25 | 4132 | 0.2089 | 0.1717 | +0.0372 ± 0.0025 | 0.6111 | 0.5074 | 0.5019 | 0.3055 | 0.3095 | -0.069 ± 0.0064 | -0.0025 (44) |
| 25-40 | 3162 | 0.222 | 0.13 | +0.0920 ± 0.004 | 0.6384 | 0.3973 | 0.5302 | 0.2174 | 0.2302 | -0.059 ± 0.0062 | -0.01 (1) |
| 40+ | 2050 | 0.3813 | 0.0423 | +0.3389 ± 0.0051 | 0.9924 | 0.1679 | 0.6312 | 0.1064 | 0.0571 | -0.086 ± 0.0042 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 414 | 0.2007 | 0.2013 | -0.0006 ± 0.0008 | 0.5832 | 0.5845 | 0.5015 | 0.4866 | 0.5121 | -0.086 ± 0.0235 | -0.01 (3) |
| 3-5 | 309 | 0.2197 | 0.2185 | +0.0012 ± 0.0022 | 0.6249 | 0.6226 | 0.5139 | 0.4739 | 0.4725 | -0.105 ± 0.0285 | 0.02 (1) |
| 5-10 | 658 | 0.1977 | 0.1988 | -0.0010 ± 0.0026 | 0.5786 | 0.5805 | 0.5476 | 0.4725 | 0.5167 | -0.069 ± 0.0178 | -0.01 (4) |
| 10-15 | 621 | 0.2179 | 0.2121 | +0.0058 ± 0.0046 | 0.626 | 0.611 | 0.5644 | 0.4401 | 0.4815 | -0.094 ± 0.0191 | -0.04 (5) |
| 15-25 | 890 | 0.2318 | 0.2104 | +0.0214 ± 0.0061 | 0.6573 | 0.6037 | 0.5921 | 0.3959 | 0.4438 | -0.100 ± 0.0156 | -0.0133 (9) |
| 25-40 | 617 | 0.2618 | 0.2006 | +0.0612 ± 0.0113 | 0.7312 | 0.5826 | 0.6583 | 0.3428 | 0.4052 | -0.109 ± 0.0176 | -0.0075 (4) |
| 40+ | 220 | 0.3667 | 0.1681 | +0.1986 ± 0.0274 | 1.014 | 0.5032 | 0.7379 | 0.2557 | 0.3045 | -0.088 ± 0.0266 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2281 | 0.1873 | 0.1878 | -0.0005 ± 0.0003 | 0.5515 | 0.5523 | 0.5018 | 0.487 | 0.5068 | -0.037 ± 0.0094 | -0.0133 (15) |
| 3-5 | 1554 | 0.1974 | 0.1972 | +0.0002 ± 0.0009 | 0.5725 | 0.5717 | 0.513 | 0.473 | 0.4891 | -0.037 ± 0.0115 | 0.02 (1) |
| 5-10 | 3369 | 0.1912 | 0.19 | +0.0012 ± 0.0011 | 0.5649 | 0.5583 | 0.5058 | 0.4317 | 0.4622 | -0.031 ± 0.0076 | -0.0117 (6) |
| 10-15 | 2975 | 0.2001 | 0.1885 | +0.0116 ± 0.002 | 0.5879 | 0.5497 | 0.5145 | 0.3904 | 0.4077 | -0.053 ± 0.0081 | -0.0189 (18) |
| 15-25 | 4241 | 0.2179 | 0.1799 | +0.0381 ± 0.0026 | 0.6333 | 0.5279 | 0.5299 | 0.3335 | 0.3379 | -0.070 ± 0.0066 | -0.0086 (42) |
| 25-40 | 3735 | 0.2494 | 0.1394 | +0.1100 ± 0.0039 | 0.7038 | 0.4262 | 0.5618 | 0.2457 | 0.2321 | -0.082 ± 0.0061 | -0.0044 (18) |
| 40+ | 2850 | 0.3999 | 0.0629 | +0.3370 ± 0.0054 | 1.0538 | 0.2223 | 0.6594 | 0.1231 | 0.0898 | -0.072 ± 0.0046 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 532 | 0.1985 | 0.2009 | -0.0025 ± 0.0007 | 0.5776 | 0.5835 | 0.4973 | 0.482 | 0.5564 | -0.012 ± 0.0198 | -0.0137 (8) |
| 3-5 | 388 | 0.1942 | 0.1923 | +0.0020 ± 0.0018 | 0.5662 | 0.5616 | 0.5035 | 0.464 | 0.4613 | -0.116 ± 0.0233 | 0.0067 (3) |
| 5-10 | 802 | 0.201 | 0.1984 | +0.0027 ± 0.0024 | 0.589 | 0.5791 | 0.5106 | 0.4367 | 0.4526 | -0.094 ± 0.0162 | -0.0071 (7) |
| 10-15 | 648 | 0.2086 | 0.2051 | +0.0035 ± 0.0044 | 0.6047 | 0.5926 | 0.539 | 0.4158 | 0.466 | -0.082 ± 0.0176 | -0.0317 (6) |
| 15-25 | 781 | 0.2323 | 0.2114 | +0.0209 ± 0.0064 | 0.6637 | 0.6063 | 0.5846 | 0.3909 | 0.4341 | -0.111 ± 0.0163 | -0.03 (1) |
| 25-40 | 483 | 0.2133 | 0.2185 | -0.0052 ± 0.0124 | 0.6131 | 0.6236 | 0.6631 | 0.3524 | 0.5135 | -0.047 ± 0.019 | 0.015 (2) |
| 40+ | 95 | 0.3141 | 0.1923 | +0.1219 ± 0.0404 | 0.8578 | 0.5616 | 0.7631 | 0.3111 | 0.4105 | -0.110 ± 0.0411 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2657 | 0.187 | 0.1878 | -0.0008 ± 0.0003 | 0.5503 | 0.5518 | 0.4885 | 0.4731 | 0.4919 | -0.034 ± 0.0085 | -0.0163 (35) |
| 3-5 | 1831 | 0.1863 | 0.1835 | +0.0029 ± 0.0008 | 0.55 | 0.543 | 0.4834 | 0.4439 | 0.4287 | -0.076 ± 0.0103 | -0.0094 (18) |
| 5-10 | 3998 | 0.1961 | 0.1907 | +0.0054 ± 0.001 | 0.5766 | 0.5582 | 0.4859 | 0.4119 | 0.4107 | -0.061 ± 0.007 | -0.01 (31) |
| 10-15 | 3163 | 0.1964 | 0.1797 | +0.0167 ± 0.0019 | 0.5773 | 0.5297 | 0.5026 | 0.3791 | 0.3737 | -0.071 ± 0.0075 | -0.015 (12) |
| 15-25 | 4227 | 0.2117 | 0.1721 | +0.0395 ± 0.0025 | 0.6178 | 0.5085 | 0.5076 | 0.3127 | 0.309 | -0.075 ± 0.0064 | -0.03 (2) |
| 25-40 | 3136 | 0.218 | 0.1306 | +0.0873 ± 0.0041 | 0.6292 | 0.3978 | 0.532 | 0.2159 | 0.2382 | -0.053 ± 0.0062 | 0.01 (3) |
| 40+ | 1993 | 0.3962 | 0.0478 | +0.3484 ± 0.0055 | 1.035 | 0.1823 | 0.6434 | 0.1132 | 0.0622 | -0.088 ± 0.0046 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 895 | 0.1957 | 0.1959 | -0.0001 ± 0.0005 | 0.5715 | 0.5716 | 0.5076 | 0.4925 | 0.495 | -0.059 ± 0.015 | -0.0224 (49) |
| 3-5 | 621 | 0.1925 | 0.192 | +0.0005 ± 0.0014 | 0.5625 | 0.5604 | 0.4837 | 0.4439 | 0.4557 | -0.051 ± 0.0178 | -0.0194 (34) |
| 5-10 | 1322 | 0.1997 | 0.1934 | +0.0063 ± 0.0018 | 0.5873 | 0.5685 | 0.4909 | 0.4175 | 0.413 | -0.070 ± 0.0123 | -0.005 (78) |
| 10-15 | 853 | 0.2082 | 0.1975 | +0.0107 ± 0.0038 | 0.6045 | 0.5766 | 0.5152 | 0.3921 | 0.4091 | -0.063 ± 0.0154 | 0.0014 (64) |
| 15-25 | 1141 | 0.231 | 0.211 | +0.0200 ± 0.0053 | 0.6597 | 0.6081 | 0.5718 | 0.3769 | 0.4251 | -0.063 ± 0.0136 | -0.0214 (59) |
| 25-40 | 688 | 0.2499 | 0.2035 | +0.0464 ± 0.0106 | 0.7074 | 0.5868 | 0.6619 | 0.3493 | 0.4302 | -0.086 ± 0.016 | -0.0219 (26) |
| 40+ | 238 | 0.351 | 0.1966 | +0.1544 ± 0.0286 | 1.014 | 0.5751 | 0.8052 | 0.3198 | 0.4244 | -0.082 ± 0.0255 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2914 | 0.1834 | 0.1835 | -0.0001 ± 0.0003 | 0.5401 | 0.5397 | 0.5076 | 0.4923 | 0.5007 | -0.038 ± 0.008 | -0.0157 (88) |
| 3-5 | 1978 | 0.1893 | 0.1874 | +0.0020 ± 0.0008 | 0.5547 | 0.5503 | 0.4882 | 0.4484 | 0.4439 | -0.053 ± 0.0098 | -0.0209 (69) |
| 5-10 | 3998 | 0.1962 | 0.1874 | +0.0088 ± 0.001 | 0.5776 | 0.5526 | 0.4872 | 0.4138 | 0.3937 | -0.072 ± 0.0069 | -0.0082 (132) |
| 10-15 | 2776 | 0.2048 | 0.1895 | +0.0153 ± 0.0021 | 0.5977 | 0.5569 | 0.521 | 0.398 | 0.397 | -0.062 ± 0.0083 | -0.0053 (105) |
| 15-25 | 3428 | 0.2276 | 0.1982 | +0.0294 ± 0.003 | 0.6566 | 0.5761 | 0.5639 | 0.3686 | 0.3929 | -0.060 ± 0.0076 | -0.0253 (107) |
| 25-40 | 2364 | 0.2595 | 0.1802 | +0.0793 ± 0.0055 | 0.7339 | 0.5278 | 0.6225 | 0.3083 | 0.3426 | -0.077 ± 0.0085 | -0.0229 (51) |
| 40+ | 1087 | 0.3768 | 0.1389 | +0.2379 ± 0.0119 | 1.0678 | 0.4214 | 0.725 | 0.2213 | 0.2502 | -0.073 ± 0.0105 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3729 | 1.049 ± 0.046 | 1.171 | 0.1668 | 0.165 | 0.2131 | 0.2044 |
| gen2 | 3729 | 0.847 ± 0.042 | 1.13 | 0.1711 | 0.1655 | 0.2319 | 0.2042 |
| gen1_elo | 3729 | 1.028 ± 0.045 | 1.155 | 0.1732 | 0.1654 | 0.2123 | 0.2045 |
| gen1_sr | 3729 | 1.05 ± 0.055 | 1.206 | 0.1315 | 0.1674 | 0.2281 | 0.2038 |
| gen1_ledger | 5758 | 0.877 ± 0.032 | 1.089 | 0.1798 | 0.1801 | 0.218 | 0.1991 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 18,383)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,208 | 22.9% |
| STALE_QUOTE | market_freshness | 3,771 | 20.5% |
| BOOK_QUALITY | execution | 3,565 | 19.4% |
| POOR_DATA | data | 2,110 | 11.5% |
| LIMITED_DATA | data | 1,240 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 985 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 932 | 5.1% |
| IDENTITY_AMBIGUOUS | mapping | 738 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 534 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 300 | 1.6% |

Cause class: coverage 22.9%, market_freshness 20.5%, execution 19.4%, data 18.2%, market_freshness/coverage 8.3%, model_calibration_or_unknown 5.1%, mapping 4.0%, model_calibration 1.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.0%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 70.3%, THIN_PLAYER_HISTORY 59.1%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 43.0%, MODEL_INTERNAL_DISAGREEMENT 41.7%, ASYMMETRIC_SAMPLE_SIZE 32.6%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 15.2%, LEVEL_TRANSFER_RISK 10.4%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.9%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.4%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 9,775)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,348 | 34.2% |
| BOOK_QUALITY | execution | 1,866 | 19.1% |
| STALE_QUOTE | market_freshness | 1,729 | 17.7% |
| POOR_DATA | data | 888 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 513 | 5.2% |
| IDENTITY_AMBIGUOUS | mapping | 425 | 4.3% |
| LIMITED_DATA | data | 381 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 334 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 218 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 73 | 0.8% |

Cause class: coverage 34.2%, execution 19.1%, market_freshness 17.7%, data 13.0%, market_freshness/coverage 8.7%, mapping 4.3%, model_calibration_or_unknown 2.2%, model_calibration 0.8%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.3%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.3%, THIN_PLAYER_HISTORY 61.8%, STALE_KALSHI_QUOTE 51.0%, STALE_PLAYER_DATA 47.6%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 25.0%, PLAYER_IDENTITY_RISK 18.6%, MODEL_HIGH_UNCERTAINTY 18.3%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.6%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.2%, POST_SETTLEMENT_OBSERVATION 34.2%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7699, "IDENTITY_AMBIGUOUS": 2076}; ticker orientation: {"VERIFIED": 9775}.

Checks: discipline:AMBIGUOUS 670, discipline:PASS 9105, identity_confidence:AMBIGUOUS 1818, identity_confidence:PASS 7957, level_mapping:NA 682, level_mapping:PASS 9093, market_pair:AMBIGUOUS 359, market_pair:NA 234, market_pair:PASS 9182, model_complement:NA 201, model_complement:PASS 9574, namesake:PASS 9775, physical_match_id:NA 3664, physical_match_id:PASS 6111, player_ids:PASS 9775, same_pair_other_event:PASS 9775, ticker_orientation:PASS 9775

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,487 | 4.9% | 4.6% | 1.8% | {"market_freshness": 52, "model_calibration_or_unknown": 40, "data": 32, "execution": 19, "model_calibration": 13, "market_freshness/coverage": 10, "coverage": 5} | 5.9 | 0.2234 / 0.2145 (385) | 18.5% | 3.8% | 3.6% | 2.6% |
| CHALLENGER | 7,179 | 17.1% | 6.9% | 12.6% | {"coverage": 692, "market_freshness/coverage": 150, "market_freshness": 144, "data": 115, "model_calibration_or_unknown": 57, "execution": 30, "model_calibration": 27, "mapping": 14} | 7.48 | 0.217 / 0.207 (1736) | 35.0% | 17.1% | 3.9% | 22.3% |
| DOUBLES | 1,382 | 48.5% | 48.0% | 6.9% | {"execution": 334, "mapping": 177, "market_freshness": 106, "market_freshness/coverage": 46, "coverage": 7} | 24.07 | 0.3226 / 0.2343 (360) | 16.9% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 12,059 | 25.1% | 17.6% | 30.9% | {"coverage": 1128, "execution": 620, "market_freshness": 476, "data": 419, "market_freshness/coverage": 247, "mapping": 131, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.46 | 0.2144 / 0.1946 (2804) | 35.9% | 65.1% | 16.3% | 22.1% |
| ITF_WOMEN | 16,428 | 26.6% | 19.7% | 44.8% | {"coverage": 1499, "market_freshness": 874, "execution": 832, "data": 669, "market_freshness/coverage": 345, "mapping": 97, "model_calibration_or_unknown": 51, "model_calibration": 10} | 12.92 | 0.2024 / 0.1946 (3253) | 37.7% | 57.9% | 10.2% | 21.6% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,545 | 4.6% | 4.2% | 1.2% | {"market_freshness": 37, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 11, "data": 11, "market_freshness/coverage": 10, "coverage": 4, "mapping": 1} | 7.94 | 0.2365 / 0.2304 (419) | 23.6% | 1.3% | 1.5% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.8% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 15 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 16 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 17 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 18 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 19 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 20 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 21 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 22 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 23 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 24 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 25 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 26 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 27 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 30 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 31 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 32 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 36 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 37 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 38 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 39 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 41 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 42 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 43 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 44 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 45 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 46 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 20.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 1255 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 47 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 48 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9704, "by_level_share_of_ge_25pp": {"ATP": 0.0175, "CHALLENGER": 0.1257, "DOUBLES": 0.0685, "ITF_MEN": 0.3094, "ITF_WOMEN": 0.4478, "OTHER": 0.0012, "WTA": 0.0121, "WTA125": 0.0178}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5103, "share_primary_cause_market_settled_or_in_play": 0.4292, "share_primary_cause_stale_quote_only": 0.1769}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 9775, "identity_ambiguous_share": 0.2124, "ticker_orientation": {"VERIFIED": 9775}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6111, "with_external": 285, "coverage": 0.0466, "external_status": {"EXTERNAL_STALE": 182, "AGREES_WITH_KALSHI": 100, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 182, "MODEL_LONE_OUTLIER": 100, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3509, "share_external_supports_model": 0.0105}, "pregame_clean_ge_25pp": {"n": 2983, "with_external": 270, "coverage": 0.0905, "external_status": {"EXTERNAL_STALE": 169, "AGREES_WITH_KALSHI": 98, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 169, "MODEL_LONE_OUTLIER": 98, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.363, "share_external_supports_model": 0.0111}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 509.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 221.5, "share_severe_asymmetry": 0.2088, "data_status": {"POOR": 5385, "LIMITED": 2680, "ADEQUATE": 1710}, "comparison_lt_10pp": {"median_thinner_serve_points": 1754.0, "median_sample_ratio": 1.69, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 748, "model_minus_observed": 0.0453, "kalshi_minus_observed": -0.0896, "brier_diff_model_minus_kalshi": -0.0021}, "4-10x": {"n": 513, "model_minus_observed": 0.0879, "kalshi_minus_observed": -0.0576, "brier_diff_model_minus_kalshi": 0.0127}, "<2x": {"n": 1834, "model_minus_observed": 0.0859, "kalshi_minus_observed": -0.0359, "brier_diff_model_minus_kalshi": 0.012}, ">=10x": {"n": 634, "model_minus_observed": 0.1066, "kalshi_minus_observed": -0.0671, "brier_diff_model_minus_kalshi": 0.0086}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3729, "model": {"intercept": -0.531, "slope": 0.847, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.239, "slope": 1.13, "slope_se": 0.048}, "mean_extremity_model": 0.1711, "mean_extremity_kalshi": 0.1655, "model_brier": 0.2319, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0278, "brier_diff_se": 0.0031, "model_logloss": 0.6606, "kalshi_logloss": 0.5909}, "fair_v1": {"n": 3729, "model": {"intercept": -0.394, "slope": 1.049, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.325, "slope": 1.171, "slope_se": 0.049}, "mean_extremity_model": 0.1668, "mean_extremity_kalshi": 0.165, "model_brier": 0.2131, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0087, "brier_diff_se": 0.0025, "model_logloss": 0.6145, "kalshi_logloss": 0.5913}, "gen1_elo": {"n": 3729, "model": {"intercept": -0.389, "slope": 1.028, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.32, "slope": 1.155, "slope_se": 0.048}, "mean_extremity_model": 0.1732, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2123, "kalshi_brier": 0.2045, "brier_diff_model_minus_kalshi": 0.0079, "brier_diff_se": 0.0025, "model_logloss": 0.6133, "kalshi_logloss": 0.5913}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.243, "share_ge_15": 0.4421, "median_abs_gap": 13.09, "n": 25148}, "gen1_elo": {"share_ge_25": 0.24, "share_ge_15": 0.4382, "median_abs_gap": 12.79, "n": 25148}, "gen1_sr": {"share_ge_25": 0.3062, "share_ge_15": 0.5199, "median_abs_gap": 15.77, "n": 25148}, "gen2": {"share_ge_25": 0.309, "share_ge_15": 0.5101, "median_abs_gap": 15.49, "n": 25148}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1524, "share_ge_15": 0.3587, "median_abs_gap": 10.91, "n": 19575}, "gen1_elo": {"share_ge_25": 0.1529, "share_ge_15": 0.3519, "median_abs_gap": 10.5, "n": 19573}, "gen1_sr": {"share_ge_25": 0.2148, "share_ge_15": 0.4437, "median_abs_gap": 13.11, "n": 19576}, "gen2": {"share_ge_25": 0.2308, "share_ge_15": 0.4452, "median_abs_gap": 13.1, "n": 19576}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.9, "share_ge_25_all": 0.049, "share_ge_25_pregame_clean": 0.0459}, "WTA": {"median_abs_gap_pregame_clean": 7.94, "share_ge_25_all": 0.0464, "share_ge_25_pregame_clean": 0.0423}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2368, "share_within_10pp_all": 0.4343, "share_within_10pp_pregame_clean": 0.4866, "corr_model_vs_mid_pregame_clean": 0.8436}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 560, "model_brier": 0.1962, "kalshi_brier": 0.1976, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 653, "model_brier": 0.2125, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0092}, "15-25": {"n_settled": 831, "model_brier": 0.2265, "kalshi_brier": 0.2147, "brier_diff_model_minus_kalshi": 0.0119}, "25-40": {"n_settled": 467, "model_brier": 0.2236, "kalshi_brier": 0.2105, "brier_diff_model_minus_kalshi": 0.0132}, "3-5": {"n_settled": 353, "model_brier": 0.201, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": 0.0002}, "40+": {"n_settled": 92, "model_brier": 0.3021, "kalshi_brier": 0.176, "brier_diff_model_minus_kalshi": 0.1261}, "5-10": {"n_settled": 773, "model_brier": 0.2003, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": -0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.531, "slope": 0.847, "slope_se": 0.042}, "kalshi_slope": {"intercept": 0.239, "slope": 1.13, "slope_se": 0.048}, "n": 3729}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.51, "slope": 0.877, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.161, "slope": 1.089, "slope_se": 0.037}, "n": 5758}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 360, "model_brier": 0.3226, "kalshi_brier": 0.2343, "brier_diff_model_minus_kalshi": 0.0883, "brier_diff_se": 0.0165, "corr_model_outcome": 0.0102, "corr_kalshi_outcome": 0.2589}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
