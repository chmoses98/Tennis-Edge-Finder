# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-26T06:10Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 55,138): 0-3 13.9%, 3-5 9.5%, 5-10 19.8%, 10-15 15.4%, 15-25 19.2%, 25-40 13.9%, 40+ 8.1%; median gap 12.02 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.0%, Challenger 11.9%, doubles 7.1%). Main tour: ATP 4.4% and WTA 5.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 12,157): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.1%, BOOK_QUALITY 18.9%, STALE_QUOTE 18.6%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.1%, execution 18.9%, market_freshness 18.6%, data 12.0%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 12,157 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.5% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 480.0 points vs 1765.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.037, Gen-2 0.828, Gen-1 ledger 0.863 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 590 model 0.2216 vs Kalshi 0.2104; n 116 model 0.2743 vs Kalshi 0.202.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 242,022 model-market comparisons (391,382 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 81,649 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-26T05:55:32.461608+00:00'], shadow board 63,500 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-26T05:55:35.855185+00:00'], Model 4 31,056 rows, 20,680 settled tickers, 7,356 tickers with an external scan.
* By model: {"gen1_ledger": 55944, "gen1_elo": 31931, "fair_v1": 31931, "gen2": 31931, "gen1_sr": 31931, "model4_fundamental": 29199, "model4_conditioned": 29155}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 55,138 | 13.9 | 9.5 | 19.8 | 15.4 | 19.2 | 13.9 | 8.1 | 12.02 | 41.3% | 22.1% |
| MW fair_v1 | 31,931 | 12.9 | 8.6 | 18.5 | 15.6 | 19.8 | 14.9 | 9.8 | 13.1 | 44.4% | 24.7% |
| MW gen1_elo | 31,931 | 12.7 | 8.6 | 19.1 | 15.3 | 19.9 | 14.9 | 9.6 | 12.99 | 44.4% | 24.5% |
| MW gen1_ledger | 23,207 | 15.4 | 10.7 | 21.7 | 15.2 | 18.6 | 12.6 | 5.8 | 10.53 | 37.0% | 18.4% |
| MW gen1_sr | 31,931 | 10.2 | 7.1 | 16.9 | 13.6 | 20.8 | 18.6 | 12.8 | 15.95 | 52.2% | 31.4% |
| MW gen2 | 31,931 | 11.1 | 7.4 | 16.3 | 14.0 | 19.4 | 17.9 | 13.9 | 15.54 | 51.3% | 31.8% |
| all families model4_conditioned | 29,155 | 21.8 | 18.4 | 34.5 | 17.7 | 4.7 | 1.7 | 1.1 | 6.06 | 7.6% | 2.8% |
| all families model4_fundamental | 29,199 | 16.7 | 13.2 | 34.0 | 20.7 | 10.5 | 3.6 | 1.4 | 7.83 | 15.5% | 5.0% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.7%, >=15pp 41.3%, >=20pp 30.7%, >=25pp 22.1%, >=30pp 15.9%, >=40pp 8.1%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.37pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,942 | 27.4 | 14.5 | 26.2 | 15.0 | 11.8 | 4.3 | 0.7 | 6.12 | 16.8% | 5.0% |
| CHALLENGER | 5,067 | 15.7 | 10.1 | 20.1 | 15.7 | 15.6 | 12.3 | 10.6 | 11.15 | 38.5% | 22.9% |
| ITF_MEN | 8,600 | 10.1 | 7.2 | 16.7 | 14.6 | 21.6 | 17.6 | 12.2 | 15.5 | 51.4% | 29.8% |
| ITF_WOMEN | 12,470 | 9.5 | 6.9 | 15.9 | 15.3 | 22.4 | 18.2 | 11.8 | 15.8 | 52.5% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,096 | 17.1 | 13.4 | 25.8 | 19.9 | 17.2 | 6.0 | 0.6 | 8.25 | 23.8% | 6.6% |
| WTA125 | 750 | 14.0 | 7.3 | 21.6 | 21.9 | 20.5 | 12.8 | 1.9 | 11.38 | 35.2% | 14.7% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,942 | 24.0 | 15.2 | 25.6 | 17.5 | 12.4 | 4.4 | 0.9 | 6.58 | 17.7% | 5.3% |
| CHALLENGER | 5,067 | 14.9 | 8.8 | 18.1 | 14.6 | 18.1 | 14.1 | 11.4 | 12.71 | 43.6% | 25.5% |
| ITF_MEN | 8,600 | 8.1 | 5.8 | 14.4 | 13.0 | 19.6 | 21.2 | 17.8 | 18.81 | 58.7% | 39.1% |
| ITF_WOMEN | 12,470 | 8.2 | 5.6 | 13.7 | 13.0 | 20.7 | 21.1 | 17.7 | 19.2 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,096 | 14.4 | 10.4 | 22.4 | 15.9 | 22.5 | 13.3 | 1.2 | 10.87 | 37.0% | 14.5% |
| WTA125 | 750 | 6.9 | 5.9 | 16.5 | 18.1 | 24.8 | 19.2 | 8.5 | 16.36 | 52.5% | 27.7% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,942 | 23.2 | 12.4 | 24.4 | 16.4 | 15.8 | 6.7 | 1.3 | 7.54 | 23.7% | 7.9% |
| CHALLENGER | 5,067 | 14.3 | 9.3 | 20.9 | 15.6 | 16.2 | 12.9 | 10.8 | 11.47 | 39.9% | 23.7% |
| ITF_MEN | 8,600 | 9.6 | 7.3 | 16.8 | 13.8 | 22.2 | 17.9 | 12.4 | 15.99 | 52.5% | 30.4% |
| ITF_WOMEN | 12,470 | 9.3 | 6.6 | 16.3 | 15.8 | 22.7 | 18.2 | 11.0 | 15.6 | 51.9% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,096 | 23.8 | 17.1 | 30.7 | 15.3 | 9.6 | 2.7 | 0.8 | 6.04 | 13.1% | 3.5% |
| WTA125 | 750 | 22.4 | 11.6 | 27.1 | 16.4 | 16.0 | 6.1 | 0.4 | 7.99 | 22.5% | 6.5% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,788 | 24.8 | 19.4 | 29.9 | 13.1 | 9.5 | 3.0 | 0.3 | 5.67 | 12.8% | 3.3% |
| CHALLENGER | 3,504 | 21.0 | 14.2 | 26.7 | 14.9 | 14.8 | 6.6 | 1.7 | 7.44 | 23.1% | 8.3% |
| DOUBLES | 1,809 | 5.1 | 4.5 | 12.3 | 10.2 | 20.2 | 25.8 | 21.9 | 24.05 | 67.9% | 47.7% |
| ITF_MEN | 6,362 | 13.6 | 9.2 | 19.9 | 16.1 | 21.5 | 13.3 | 6.4 | 12.2 | 41.2% | 19.7% |
| ITF_WOMEN | 7,526 | 12.6 | 8.8 | 19.4 | 15.3 | 21.6 | 16.2 | 6.1 | 12.84 | 43.9% | 22.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,261 | 22.8 | 15.5 | 30.6 | 17.9 | 9.8 | 3.1 | 0.3 | 6.85 | 13.2% | 3.4% |
| WTA125 | 808 | 21.0 | 13.5 | 21.9 | 18.4 | 14.5 | 8.5 | 2.1 | 8.32 | 25.1% | 10.6% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,862 | 27.7 | 14.7 | 26.6 | 14.9 | 11.6 | 4.0 | 0.4 | 5.97 | 16.0% | 4.4% |
| CHALLENGER | 3,585 | 20.5 | 12.6 | 24.7 | 18.1 | 15.6 | 6.8 | 1.8 | 8.41 | 24.2% | 8.6% |
| ITF_MEN | 6,283 | 12.2 | 8.7 | 20.2 | 16.6 | 22.8 | 14.4 | 5.1 | 12.6 | 42.3% | 19.5% |
| ITF_WOMEN | 9,344 | 11.2 | 8.2 | 18.1 | 17.3 | 24.4 | 15.4 | 5.4 | 13.57 | 45.2% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,037 | 17.3 | 13.3 | 25.8 | 20.1 | 17.2 | 5.7 | 0.6 | 8.25 | 23.5% | 6.3% |
| WTA125 | 724 | 14.4 | 7.2 | 21.1 | 22.2 | 21.1 | 12.4 | 1.5 | 11.38 | 35.1% | 14.0% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,862 | 24.2 | 15.5 | 25.9 | 17.4 | 12.4 | 4.0 | 0.5 | 6.48 | 17.0% | 4.6% |
| CHALLENGER | 3,585 | 19.0 | 11.3 | 22.3 | 17.3 | 18.4 | 9.8 | 1.9 | 9.37 | 30.1% | 11.7% |
| ITF_MEN | 6,284 | 9.6 | 7.0 | 16.9 | 15.1 | 21.5 | 19.4 | 10.5 | 15.49 | 51.4% | 29.9% |
| ITF_WOMEN | 9,345 | 9.2 | 6.4 | 15.2 | 14.4 | 22.7 | 20.6 | 11.4 | 16.83 | 54.7% | 31.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,037 | 14.5 | 10.4 | 22.4 | 15.9 | 22.5 | 13.1 | 1.2 | 10.87 | 36.8% | 14.3% |
| WTA125 | 724 | 6.8 | 6.1 | 16.6 | 18.5 | 24.7 | 19.6 | 7.7 | 15.89 | 52.1% | 27.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,737 | 24.9 | 19.7 | 29.9 | 13.3 | 9.2 | 2.9 | 0.2 | 5.63 | 12.2% | 3.0% |
| CHALLENGER | 3,074 | 22.4 | 15.2 | 28.1 | 15.0 | 14.2 | 4.6 | 0.5 | 6.94 | 19.3% | 5.1% |
| DOUBLES | 1,689 | 5.1 | 4.6 | 12.6 | 10.4 | 20.0 | 25.8 | 21.7 | 23.92 | 67.4% | 47.4% |
| ITF_MEN | 5,340 | 14.7 | 9.8 | 21.6 | 16.9 | 21.5 | 11.6 | 3.9 | 11.25 | 37.0% | 15.5% |
| ITF_WOMEN | 6,273 | 13.4 | 9.3 | 20.7 | 16.1 | 21.8 | 14.9 | 3.6 | 11.83 | 40.4% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,209 | 23.2 | 15.9 | 30.6 | 17.9 | 9.8 | 2.5 | 0.1 | 6.8 | 12.3% | 2.6% |
| WTA125 | 697 | 22.8 | 14.8 | 23.2 | 19.8 | 12.9 | 5.9 | 0.6 | 7.6 | 19.4% | 6.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,809 | 5.1 | 4.5 | 12.3 | 10.2 | 20.2 | 25.8 | 21.9 | 24.05 | 67.9% | 47.7% |
| singles | 21,398 | 16.2 | 11.3 | 22.5 | 15.6 | 18.4 | 11.5 | 4.5 | 9.99 | 34.4% | 16.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 6,975 | 12.9 | 9.1 | 19.4 | 15.9 | 19.0 | 14.2 | 9.6 | 12.69 | 42.8% | 23.8% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 20,041 | 13.3 | 8.7 | 18.6 | 15.2 | 19.8 | 14.8 | 9.5 | 13.02 | 44.1% | 24.3% |
| UNKNOWN | 4,666 | 10.8 | 7.5 | 17.0 | 16.8 | 20.6 | 16.3 | 11.1 | 14.12 | 48.0% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,221 | 19.6 | 12.1 | 21.8 | 16.4 | 14.9 | 9.2 | 6.1 | 8.96 | 30.2% | 15.3% |
| B | 3,953 | 12.2 | 8.7 | 19.4 | 16.5 | 19.6 | 12.8 | 10.8 | 12.7 | 43.2% | 23.6% |
| C | 4,442 | 11.8 | 9.0 | 19.4 | 15.5 | 19.2 | 14.6 | 10.4 | 13.04 | 44.3% | 25.0% |
| D | 4,869 | 12.1 | 7.8 | 17.3 | 15.5 | 21.8 | 15.6 | 9.9 | 13.98 | 47.3% | 25.5% |
| F | 9,446 | 7.5 | 5.5 | 15.1 | 14.6 | 23.8 | 21.2 | 12.5 | 17.79 | 57.4% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,662 | 23.2 | 16.0 | 28.9 | 15.2 | 11.4 | 4.0 | 1.3 | 6.61 | 16.7% | 5.3% |
| B | 3,133 | 16.1 | 10.4 | 23.1 | 16.3 | 19.9 | 10.5 | 3.7 | 10.06 | 34.1% | 14.2% |
| C | 4,569 | 10.9 | 7.2 | 18.6 | 14.4 | 21.1 | 16.7 | 11.1 | 14.44 | 49.0% | 27.8% |
| D | 3,166 | 14.2 | 9.6 | 20.1 | 15.0 | 21.0 | 14.1 | 5.9 | 12.02 | 41.1% | 20.0% |
| F | 5,677 | 10.2 | 8.3 | 15.8 | 15.2 | 22.8 | 19.8 | 8.0 | 15.27 | 50.6% | 27.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,513 | 17.8 | 10.8 | 21.1 | 16.1 | 15.5 | 10.1 | 8.6 | 10.04 | 34.2% | 18.7% |
| LIMITED | 6,759 | 13.5 | 10.2 | 20.0 | 16.2 | 19.3 | 13.3 | 7.5 | 11.89 | 40.1% | 20.8% |
| POOR | 14,659 | 9.1 | 6.3 | 15.9 | 14.9 | 23.0 | 19.1 | 11.6 | 16.26 | 53.7% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,764 | 24.8 | 18.7 | 33.5 | 14.4 | 6.1 | 2.3 | 0.2 | 5.68 | 8.6% | 2.5% |
| GAME_SPREAD | 5,265 | 22.4 | 15.3 | 33.3 | 17.0 | 9.1 | 2.5 | 0.3 | 6.71 | 12.0% | 2.9% |
| MATCH_WINNER | 23,207 | 15.4 | 10.7 | 21.7 | 15.2 | 18.6 | 12.6 | 5.8 | 10.53 | 37.0% | 18.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,119 | 27.9 | 16.3 | 31.2 | 12.7 | 9.3 | 2.2 | 0.3 | 5.7 | 11.9% | 2.6% |
| TOTAL_GAMES | 8,565 | 9.0 | 10.0 | 36.2 | 27.6 | 10.5 | 3.8 | 2.8 | 9.39 | 17.2% | 6.6% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,452 | 24.5 | 31.4 | 32.8 | 6.6 | 3.7 | 0.8 | 0.2 | 4.65 | 4.7% | 1.0% |
| GAME_SPREAD | 6,829 | 46.0 | 16.6 | 26.3 | 7.8 | 1.8 | 1.1 | 0.4 | 3.41 | 3.2% | 1.5% |
| TOTAL_GAMES | 11,874 | 5.4 | 8.1 | 40.8 | 33.3 | 7.3 | 2.9 | 2.3 | 9.54 | 12.5% | 5.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,463 | 23.6 | 16.9 | 35.3 | 14.0 | 7.2 | 2.6 | 0.4 | 6.04 | 10.2% | 2.9% |
| GAME_SPREAD | 6,832 | 19.7 | 13.2 | 28.1 | 21.0 | 12.8 | 4.3 | 1.0 | 7.96 | 18.1% | 5.2% |
| TOTAL_GAMES | 11,904 | 8.9 | 9.8 | 36.2 | 26.4 | 12.0 | 4.2 | 2.5 | 9.42 | 18.6% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 31,931 | 44.4% | 24.7% | 13.1 | 36.0% | 15.5% | 10.91 |
| gen1_elo | 31,931 | 44.4% | 24.5% | 12.99 | 35.8% | 15.6% | 10.71 |
| gen1_sr | 31,931 | 52.2% | 31.4% | 15.95 | 44.4% | 22.1% | 13.02 |
| gen2 | 31,931 | 51.3% | 31.8% | 15.54 | 44.4% | 23.8% | 13.03 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 16,154 | 15.6 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.3 | 10.71 | 35.3% | 15.1% |
| STALE | 15,777 | 10.1 | 6.8 | 15.6 | 13.8 | 19.3 | 18.0 | 16.4 | 16.76 | 53.8% | 34.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 16,675 | 16.3 | 11.2 | 22.5 | 15.3 | 17.8 | 12.0 | 4.9 | 10.01 | 34.7% | 16.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 55,138 | 16675 | 19626 | 18837 | 24.1 | 136.3 | 1400.4 |
| ge_15pp | 22,770 | 5790 | 6987 | 9993 | 26.3 | 439.3 | 1380.4 |
| ge_25pp | 12,157 | 2820 | 3034 | 6303 | 31.7 | 581.6 | 1380.4 |
| lt_10pp | 23,871 | 8329 | 9289 | 6253 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261026T061008Z-bfce70b5`: 889 priced rows, quote age at build {'median': 15.1, 'max': 15.1}, freshness {'AGING': 889}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 28 | 0.0 | 0.0 | 21.4 | 10.7 | 39.3 | 28.6 | 0.0 | 20.48 | 67.9% | 28.6% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,089 | 19.4 | 11.3 | 24.8 | 18.8 | 18.1 | 7.0 | 0.6 | 8.81 | 25.7% | 7.6% |
| KALSHI_LONE_OUTLIER | 21 | 4.8 | 4.8 | 76.2 | 4.8 | 4.8 | 4.8 | 0.0 | 6.11 | 9.5% | 4.8% |
| MARKETS_AGREE | 631 | 65.3 | 34.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.23 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,362 | 0.0 | 2.6 | 35.0 | 26.6 | 24.9 | 10.3 | 0.7 | 12.14 | 35.8% | 10.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 31,931 | 5149 (16.1%) | 26.5% | 0.9% | {"EXTERNAL_STALE": 3089, "AGREES_WITH_KALSHI": 1362, "ALL_AGREE": 631, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 21, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 14,181 | 1303 (9.2%) | 37.5% | 1.6% | {"EXTERNAL_STALE": 794, "AGREES_WITH_KALSHI": 488, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,875 | 393 (5.0%) | 37.9% | 2.3% | {"EXTERNAL_STALE": 235, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,841 | 370 (9.6%) | 38.4% | 2.4% | {"EXTERNAL_STALE": 219, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,773 | 2898 (22.7%) | 17.6% | 0.8% | {"EXTERNAL_STALE": 1714, "ALL_AGREE": 631, "AGREES_WITH_KALSHI": 511, "EXTERNAL_OUTLIER": 18, "AGREES_WITH_MODEL": 18, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,088 | 10.1 | 7.6 | 19.4 | 14.7 | 22.5 | 15.9 | 9.9 | 14.13 | 48.3% | 25.7% |
| 4-10x | 4,119 | 11.1 | 8.4 | 18.7 | 15.4 | 21.7 | 14.7 | 9.8 | 13.75 | 46.2% | 24.5% |
| <2x | 16,322 | 15.0 | 9.9 | 19.2 | 16.4 | 17.5 | 13.0 | 8.9 | 11.7 | 39.4% | 21.9% |
| >=10x | 5,402 | 10.7 | 6.1 | 15.2 | 14.2 | 21.9 | 19.7 | 12.1 | 16.48 | 53.7% | 31.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,170 | 12.6 | 8.6 | 19.2 | 16.2 | 19.1 | 13.8 | 10.6 | 12.93 | 43.5% | 24.4% |
| 300-1000 | 6,692 | 11.7 | 8.7 | 17.3 | 15.4 | 20.7 | 16.1 | 10.0 | 13.83 | 46.9% | 26.2% |
| <300 | 10,380 | 8.5 | 5.7 | 15.4 | 14.7 | 23.3 | 20.1 | 12.3 | 17.02 | 55.7% | 32.4% |
| >=3000 | 6,689 | 21.2 | 13.2 | 23.6 | 16.4 | 14.0 | 6.9 | 4.6 | 7.8 | 25.5% | 11.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 901 | 0.5513 | 0.4135 | 0.5039 | +0.047 | -0.090 | -0.0042 ± 0.0051 |
| ratio 4-10x | 610 | 0.5891 | 0.4431 | 0.5 | +0.089 | -0.057 | 0.0092 ± 0.0065 |
| ratio <2x | 2235 | 0.539 | 0.4158 | 0.4483 | +0.091 | -0.033 | 0.0116 ± 0.003 |
| ratio >=10x | 823 | 0.5707 | 0.3952 | 0.4605 | +0.110 | -0.065 | 0.008 ± 0.0064 |
| thinner_sample 1000-3000 | 1244 | 0.5427 | 0.4158 | 0.4502 | +0.093 | -0.034 | 0.0094 ± 0.004 |
| thinner_sample 300-1000 | 1024 | 0.5665 | 0.4229 | 0.4922 | +0.074 | -0.069 | 0.0004 ± 0.0051 |
| thinner_sample <300 | 1538 | 0.5627 | 0.396 | 0.4655 | +0.097 | -0.070 | 0.0087 ± 0.0045 |
| thinner_sample >=3000 | 763 | 0.5369 | 0.443 | 0.4718 | +0.065 | -0.029 | 0.0116 ± 0.0042 |
| data_status ADEQUATE | 1321 | 0.5386 | 0.4346 | 0.4542 | +0.084 | -0.020 | 0.0115 ± 0.0034 |
| data_status LIMITED | 1053 | 0.5509 | 0.4172 | 0.4853 | +0.066 | -0.068 | 0.0028 ± 0.0046 |
| data_status POOR | 2195 | 0.5644 | 0.4028 | 0.4688 | +0.096 | -0.066 | 0.0074 ± 0.0037 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 668 | 0.2018 | 0.2026 | -0.0008 ± 0.0006 | 0.5846 | 0.5864 | 0.5021 | 0.4873 | 0.5195 | -0.075 ± 0.0183 | -0.01 (5) |
| 3-5 | 421 | 0.2055 | 0.2047 | +0.0008 ± 0.0018 | 0.5941 | 0.5909 | 0.5035 | 0.4635 | 0.4727 | -0.107 ± 0.0228 | 0.02 (1) |
| 5-10 | 942 | 0.2024 | 0.2024 | +0.0000 ± 0.0022 | 0.5914 | 0.5885 | 0.5136 | 0.4395 | 0.4713 | -0.090 ± 0.0152 | -0.0167 (6) |
| 10-15 | 795 | 0.215 | 0.2066 | +0.0083 ± 0.004 | 0.6205 | 0.5956 | 0.5313 | 0.4072 | 0.4352 | -0.101 ± 0.0161 | -0.048 (5) |
| 15-25 | 1037 | 0.2257 | 0.2133 | +0.0124 ± 0.0056 | 0.647 | 0.6102 | 0.5779 | 0.3821 | 0.4484 | -0.097 ± 0.0143 | -0.0033 (9) |
| 25-40 | 590 | 0.2216 | 0.2104 | +0.0111 ± 0.0112 | 0.6324 | 0.6043 | 0.6604 | 0.3505 | 0.4847 | -0.072 ± 0.0172 | -0.01 (1) |
| 40+ | 116 | 0.2743 | 0.202 | +0.0723 ± 0.036 | 0.7526 | 0.5904 | 0.7587 | 0.3114 | 0.4569 | -0.070 ± 0.0354 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3440 | 0.1856 | 0.1864 | -0.0009 ± 0.0003 | 0.5469 | 0.5478 | 0.4914 | 0.4764 | 0.5078 | -0.024 ± 0.0075 | -0.0129 (17) |
| 3-5 | 2267 | 0.199 | 0.1978 | +0.0012 ± 0.0008 | 0.5785 | 0.573 | 0.4843 | 0.4444 | 0.4486 | -0.053 ± 0.0095 | 0.0 (2) |
| 5-10 | 4914 | 0.1984 | 0.1952 | +0.0033 ± 0.0009 | 0.5815 | 0.5699 | 0.4836 | 0.4097 | 0.4235 | -0.048 ± 0.0064 | -0.0119 (21) |
| 10-15 | 4192 | 0.1977 | 0.1804 | +0.0173 ± 0.0016 | 0.5807 | 0.5319 | 0.488 | 0.3635 | 0.3562 | -0.071 ± 0.0066 | -0.0281 (16) |
| 15-25 | 5291 | 0.209 | 0.1694 | +0.0396 ± 0.0022 | 0.6116 | 0.5007 | 0.5039 | 0.3074 | 0.3062 | -0.075 ± 0.0056 | -0.0025 (44) |
| 25-40 | 4127 | 0.2231 | 0.1285 | +0.0946 ± 0.0035 | 0.6405 | 0.3937 | 0.5325 | 0.2192 | 0.2285 | -0.061 ± 0.0054 | -0.01 (1) |
| 40+ | 2664 | 0.3794 | 0.0451 | +0.3343 ± 0.0046 | 0.9881 | 0.1738 | 0.6322 | 0.1065 | 0.0638 | -0.078 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 529 | 0.2079 | 0.2086 | -0.0007 ± 0.0007 | 0.5978 | 0.5995 | 0.5065 | 0.4914 | 0.518 | -0.103 ± 0.0214 | -0.01 (3) |
| 3-5 | 373 | 0.2262 | 0.2232 | +0.0029 ± 0.002 | 0.639 | 0.6329 | 0.5149 | 0.4751 | 0.4531 | -0.134 ± 0.0261 | 0.02 (1) |
| 5-10 | 822 | 0.2072 | 0.2069 | +0.0003 ± 0.0024 | 0.6008 | 0.5995 | 0.5468 | 0.4719 | 0.5109 | -0.082 ± 0.0164 | -0.01 (4) |
| 10-15 | 758 | 0.2162 | 0.2098 | +0.0064 ± 0.0042 | 0.6214 | 0.6051 | 0.5647 | 0.4404 | 0.4789 | -0.107 ± 0.0174 | -0.04 (5) |
| 15-25 | 1058 | 0.229 | 0.2109 | +0.0181 ± 0.0055 | 0.6507 | 0.6044 | 0.5877 | 0.3921 | 0.448 | -0.098 ± 0.0144 | -0.0133 (9) |
| 25-40 | 748 | 0.2674 | 0.1993 | +0.0680 ± 0.0103 | 0.747 | 0.5801 | 0.6559 | 0.3409 | 0.393 | -0.122 ± 0.0161 | -0.0075 (4) |
| 40+ | 281 | 0.3519 | 0.1748 | +0.1771 ± 0.0246 | 0.968 | 0.5207 | 0.7338 | 0.25 | 0.3238 | -0.064 ± 0.0238 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2943 | 0.1944 | 0.1946 | -0.0002 ± 0.0003 | 0.5652 | 0.5656 | 0.5131 | 0.4981 | 0.5127 | -0.044 ± 0.0084 | -0.0133 (15) |
| 3-5 | 1948 | 0.1998 | 0.1987 | +0.0011 ± 0.0008 | 0.5777 | 0.5746 | 0.5141 | 0.4742 | 0.4795 | -0.049 ± 0.0103 | 0.02 (1) |
| 5-10 | 4343 | 0.1972 | 0.195 | +0.0022 ± 0.001 | 0.5804 | 0.5697 | 0.511 | 0.437 | 0.4624 | -0.035 ± 0.0068 | -0.0117 (6) |
| 10-15 | 3793 | 0.2012 | 0.1893 | +0.0119 ± 0.0018 | 0.5906 | 0.552 | 0.5142 | 0.3903 | 0.405 | -0.055 ± 0.0072 | -0.0189 (18) |
| 15-25 | 5227 | 0.2155 | 0.1785 | +0.0370 ± 0.0023 | 0.626 | 0.5246 | 0.5248 | 0.3288 | 0.3365 | -0.066 ± 0.0059 | -0.0086 (42) |
| 25-40 | 4820 | 0.2537 | 0.1367 | +0.1170 ± 0.0034 | 0.713 | 0.4198 | 0.5585 | 0.2415 | 0.218 | -0.090 ± 0.0053 | -0.0044 (18) |
| 40+ | 3821 | 0.3924 | 0.0606 | +0.3318 ± 0.0045 | 1.0326 | 0.2166 | 0.6503 | 0.119 | 0.0856 | -0.071 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 639 | 0.1992 | 0.2013 | -0.0021 ± 0.0006 | 0.579 | 0.5841 | 0.5005 | 0.4853 | 0.5462 | -0.034 ± 0.0184 | -0.0137 (8) |
| 3-5 | 455 | 0.2032 | 0.2017 | +0.0015 ± 0.0017 | 0.5896 | 0.5846 | 0.5068 | 0.4671 | 0.4703 | -0.118 ± 0.022 | 0.0067 (3) |
| 5-10 | 971 | 0.2031 | 0.1997 | +0.0034 ± 0.0022 | 0.5926 | 0.5814 | 0.5091 | 0.4351 | 0.448 | -0.104 ± 0.0147 | -0.0071 (7) |
| 10-15 | 788 | 0.209 | 0.2056 | +0.0034 ± 0.004 | 0.607 | 0.5936 | 0.5409 | 0.4173 | 0.467 | -0.087 ± 0.0161 | -0.0317 (6) |
| 15-25 | 976 | 0.2314 | 0.2142 | +0.0172 ± 0.0058 | 0.6608 | 0.6121 | 0.5897 | 0.3951 | 0.4477 | -0.108 ± 0.0148 | -0.03 (1) |
| 25-40 | 617 | 0.2136 | 0.2175 | -0.0039 ± 0.011 | 0.6164 | 0.6205 | 0.6693 | 0.3586 | 0.517 | -0.056 ± 0.0168 | 0.015 (2) |
| 40+ | 123 | 0.2879 | 0.2151 | +0.0728 ± 0.0362 | 0.7962 | 0.6188 | 0.7691 | 0.3198 | 0.4715 | -0.063 ± 0.0383 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3363 | 0.1863 | 0.187 | -0.0007 ± 0.0003 | 0.5478 | 0.5489 | 0.4888 | 0.4736 | 0.4927 | -0.034 ± 0.0075 | -0.0163 (35) |
| 3-5 | 2283 | 0.1959 | 0.1941 | +0.0019 ± 0.0007 | 0.5746 | 0.5685 | 0.4876 | 0.4479 | 0.4455 | -0.062 ± 0.0094 | -0.0094 (18) |
| 5-10 | 5009 | 0.1959 | 0.1903 | +0.0057 ± 0.0009 | 0.5756 | 0.5569 | 0.484 | 0.41 | 0.4093 | -0.060 ± 0.0062 | -0.01 (31) |
| 10-15 | 4055 | 0.1916 | 0.1764 | +0.0153 ± 0.0016 | 0.5668 | 0.5214 | 0.4996 | 0.3762 | 0.3756 | -0.066 ± 0.0066 | -0.015 (12) |
| 15-25 | 5430 | 0.2112 | 0.1719 | +0.0393 ± 0.0022 | 0.6168 | 0.5068 | 0.5143 | 0.319 | 0.3166 | -0.074 ± 0.0056 | -0.03 (2) |
| 25-40 | 4153 | 0.2195 | 0.1318 | +0.0877 ± 0.0035 | 0.6333 | 0.4005 | 0.5367 | 0.2209 | 0.2415 | -0.052 ± 0.0054 | 0.01 (3) |
| 40+ | 2602 | 0.3936 | 0.0506 | +0.3430 ± 0.005 | 1.0284 | 0.188 | 0.6448 | 0.1137 | 0.0703 | -0.080 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1026 | 0.196 | 0.1962 | -0.0001 ± 0.0005 | 0.5715 | 0.5714 | 0.5018 | 0.4867 | 0.4912 | -0.062 ± 0.014 | -0.0224 (49) |
| 3-5 | 707 | 0.1924 | 0.1916 | +0.0008 ± 0.0013 | 0.5623 | 0.5591 | 0.4909 | 0.4511 | 0.4583 | -0.062 ± 0.0168 | -0.0194 (34) |
| 5-10 | 1499 | 0.2021 | 0.1963 | +0.0058 ± 0.0017 | 0.5932 | 0.5751 | 0.4966 | 0.4233 | 0.4216 | -0.074 ± 0.0117 | -0.005 (78) |
| 10-15 | 999 | 0.2104 | 0.1983 | +0.0122 ± 0.0035 | 0.6102 | 0.5784 | 0.5246 | 0.4015 | 0.4114 | -0.073 ± 0.0144 | 0.0014 (64) |
| 15-25 | 1335 | 0.2321 | 0.2117 | +0.0204 ± 0.0049 | 0.6622 | 0.6085 | 0.5796 | 0.3848 | 0.4315 | -0.074 ± 0.0126 | -0.0214 (59) |
| 25-40 | 813 | 0.2458 | 0.2085 | +0.0373 ± 0.0098 | 0.7004 | 0.5988 | 0.6776 | 0.3652 | 0.4613 | -0.087 ± 0.0149 | -0.0219 (26) |
| 40+ | 269 | 0.3454 | 0.2025 | +0.1429 ± 0.0269 | 0.9985 | 0.5922 | 0.8091 | 0.3283 | 0.4387 | -0.090 ± 0.0247 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3395 | 0.1824 | 0.1826 | -0.0002 ± 0.0003 | 0.5376 | 0.5371 | 0.5024 | 0.487 | 0.4957 | -0.041 ± 0.0074 | -0.0157 (88) |
| 3-5 | 2347 | 0.1955 | 0.1936 | +0.0019 ± 0.0007 | 0.5699 | 0.5656 | 0.4978 | 0.4581 | 0.4542 | -0.055 ± 0.0092 | -0.0209 (69) |
| 5-10 | 4735 | 0.1962 | 0.1881 | +0.0081 ± 0.0009 | 0.5783 | 0.5537 | 0.492 | 0.4186 | 0.4027 | -0.071 ± 0.0064 | -0.0082 (132) |
| 10-15 | 3316 | 0.2073 | 0.1912 | +0.0161 ± 0.0019 | 0.6035 | 0.5607 | 0.5291 | 0.4061 | 0.4011 | -0.067 ± 0.0076 | -0.0053 (105) |
| 15-25 | 4116 | 0.231 | 0.2008 | +0.0302 ± 0.0028 | 0.6655 | 0.5812 | 0.5703 | 0.3747 | 0.3967 | -0.067 ± 0.007 | -0.0253 (107) |
| 25-40 | 2799 | 0.2591 | 0.1858 | +0.0733 ± 0.0051 | 0.7347 | 0.5415 | 0.6343 | 0.3209 | 0.363 | -0.078 ± 0.0079 | -0.0229 (51) |
| 40+ | 1229 | 0.3755 | 0.1458 | +0.2297 ± 0.0114 | 1.0633 | 0.4394 | 0.7316 | 0.2283 | 0.2653 | -0.071 ± 0.0102 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4569 | 1.037 ± 0.042 | 1.111 | 0.1685 | 0.163 | 0.2144 | 0.2069 |
| gen2 | 4569 | 0.828 ± 0.039 | 1.078 | 0.1683 | 0.1638 | 0.2341 | 0.2066 |
| gen1_elo | 4569 | 1.009 ± 0.04 | 1.108 | 0.1751 | 0.1632 | 0.2133 | 0.2071 |
| gen1_sr | 4569 | 1.013 ± 0.05 | 1.143 | 0.1293 | 0.1657 | 0.2304 | 0.2062 |
| gen1_ledger | 6648 | 0.863 ± 0.029 | 1.066 | 0.1839 | 0.1771 | 0.2185 | 0.2009 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 22,770)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,167 | 22.7% |
| STALE_QUOTE | market_freshness | 4,922 | 21.6% |
| BOOK_QUALITY | execution | 4,387 | 19.3% |
| POOR_DATA | data | 2,541 | 11.2% |
| LIMITED_DATA | data | 1,406 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,226 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,083 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 962 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 666 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 409 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.7%, market_freshness 21.6%, execution 19.3%, data 17.3%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 93.9%, LOW_DATA_QUALITY 70.7%, THIN_PLAYER_HISTORY 59.5%, STALE_PLAYER_DATA 49.7%, STALE_KALSHI_QUOTE 43.9%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.7%, EVENT_MAPPING_RISK 8.3%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.9%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.2%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 12,157)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,150 | 34.1% |
| BOOK_QUALITY | execution | 2,300 | 18.9% |
| STALE_QUOTE | market_freshness | 2,266 | 18.6% |
| POOR_DATA | data | 1,039 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 654 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 537 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 423 | 3.5% |
| LIMITED_DATA | data | 421 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 269 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 97 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.1%, execution 18.9%, market_freshness 18.6%, data 12.0%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.2%, THIN_PLAYER_HISTORY 61.5%, STALE_KALSHI_QUOTE 51.8%, STALE_PLAYER_DATA 44.2%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 24.8%, PLAYER_IDENTITY_RISK 20.1%, MODEL_HIGH_UNCERTAINTY 18.3%, EVENT_MAPPING_RISK 10.0%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.2%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.2%, POST_SETTLEMENT_OBSERVATION 34.1%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9410, "IDENTITY_AMBIGUOUS": 2747}; ticker orientation: {"VERIFIED": 12157}.

Checks: discipline:AMBIGUOUS 863, discipline:PASS 11294, identity_confidence:AMBIGUOUS 2440, identity_confidence:PASS 9717, level_mapping:NA 875, level_mapping:PASS 11282, market_pair:AMBIGUOUS 465, market_pair:NA 300, market_pair:PASS 11392, model_complement:NA 267, model_complement:PASS 11890, namesake:AMBIGUOUS 6, namesake:PASS 12151, physical_match_id:NA 4282, physical_match_id:PASS 7875, player_ids:PASS 12157, same_pair_other_event:PASS 12157, ticker_orientation:PASS 12157

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,730 | 4.4% | 3.9% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 47, "data": 35, "execution": 24, "model_calibration": 20, "market_freshness/coverage": 15, "coverage": 13} | 5.91 | 0.2239 / 0.2208 (539) | 19.5% | 3.3% | 3.3% | 2.8% |
| CHALLENGER | 8,571 | 16.9% | 7.0% | 11.9% | {"coverage": 813, "market_freshness/coverage": 175, "market_freshness": 164, "data": 144, "model_calibration_or_unknown": 70, "model_calibration": 35, "execution": 34, "mapping": 16, "possible_market_error": 1} | 7.6 | 0.2184 / 0.208 (2015) | 34.3% | 17.5% | 4.1% | 22.3% |
| DOUBLES | 1,809 | 47.7% | 47.4% | 7.1% | {"execution": 480, "mapping": 215, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.92 | 0.3106 / 0.2361 (437) | 12.9% | 0.0% | 100.0% | 6.6% |
| ITF_MEN | 14,962 | 25.5% | 17.7% | 31.4% | {"coverage": 1429, "execution": 727, "market_freshness": 651, "data": 500, "market_freshness/coverage": 333, "mapping": 176, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.95 | 0.2165 / 0.1985 (3333) | 37.4% | 70.1% | 19.9% | 22.3% |
| ITF_WOMEN | 19,996 | 27.1% | 19.9% | 44.6% | {"coverage": 1863, "market_freshness": 1187, "execution": 984, "data": 738, "market_freshness/coverage": 450, "mapping": 124, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.92 | 0.2032 / 0.196 (3822) | 39.6% | 56.8% | 10.2% | 21.9% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,357 | 5.4% | 4.9% | 1.5% | {"market_freshness": 63, "model_calibration_or_unknown": 38, "execution": 26, "model_calibration": 16, "data": 15, "coverage": 12, "market_freshness/coverage": 10, "mapping": 1} | 7.65 | 0.2318 / 0.2271 (527) | 24.5% | 1.2% | 1.6% | 3.3% |
| WTA125 | 1,558 | 12.6% | 10.3% | 1.6% | {"model_calibration_or_unknown": 41, "market_freshness": 40, "market_freshness/coverage": 38, "data": 28, "execution": 20, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.53 | 0.2178 / 0.2042 (502) | 23.0% | 11.6% | 6.9% | 8.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.968, "by_level_share_of_ge_25pp": {"ATP": 0.017, "CHALLENGER": 0.1194, "DOUBLES": 0.071, "ITF_MEN": 0.3142, "ITF_WOMEN": 0.4463, "OTHER": 0.001, "WTA": 0.0149, "WTA125": 0.0161}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5185, "share_primary_cause_market_settled_or_in_play": 0.43, "share_primary_cause_stale_quote_only": 0.1864}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 12157, "identity_ambiguous_share": 0.226, "ticker_orientation": {"VERIFIED": 12157}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7875, "with_external": 393, "coverage": 0.0499, "external_status": {"EXTERNAL_STALE": 235, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 235, "MODEL_LONE_OUTLIER": 149, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3791, "share_external_supports_model": 0.0229}, "pregame_clean_ge_25pp": {"n": 3841, "with_external": 370, "coverage": 0.0963, "external_status": {"EXTERNAL_STALE": 219, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 219, "MODEL_LONE_OUTLIER": 142, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3838, "share_external_supports_model": 0.0243}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 480.0, "median_sample_ratio": 2.42, "median_min_matches": 21.0, "median_max_days_since_last": 230.0, "share_severe_asymmetry": 0.2148, "data_status": {"POOR": 6738, "LIMITED": 3192, "ADEQUATE": 2227}, "comparison_lt_10pp": {"median_thinner_serve_points": 1765.0, "median_sample_ratio": 1.67, "median_min_matches": 98.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 901, "model_minus_observed": 0.0474, "kalshi_minus_observed": -0.0904, "brier_diff_model_minus_kalshi": -0.0042}, "4-10x": {"n": 610, "model_minus_observed": 0.0891, "kalshi_minus_observed": -0.0569, "brier_diff_model_minus_kalshi": 0.0092}, "<2x": {"n": 2235, "model_minus_observed": 0.0907, "kalshi_minus_observed": -0.0325, "brier_diff_model_minus_kalshi": 0.0116}, ">=10x": {"n": 823, "model_minus_observed": 0.1101, "kalshi_minus_observed": -0.0654, "brier_diff_model_minus_kalshi": 0.008}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4569, "model": {"intercept": -0.531, "slope": 0.828, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.209, "slope": 1.078, "slope_se": 0.043}, "mean_extremity_model": 0.1683, "mean_extremity_kalshi": 0.1638, "model_brier": 0.2341, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": 0.0275, "brier_diff_se": 0.0028, "model_logloss": 0.6651, "kalshi_logloss": 0.5962}, "fair_v1": {"n": 4569, "model": {"intercept": -0.418, "slope": 1.037, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.285, "slope": 1.111, "slope_se": 0.043}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.163, "model_brier": 0.2144, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0075, "brier_diff_se": 0.0023, "model_logloss": 0.6177, "kalshi_logloss": 0.5967}, "gen1_elo": {"n": 4569, "model": {"intercept": -0.393, "slope": 1.009, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.307, "slope": 1.108, "slope_se": 0.043}, "mean_extremity_model": 0.1751, "mean_extremity_kalshi": 0.1632, "model_brier": 0.2133, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0063, "brier_diff_se": 0.0023, "model_logloss": 0.6162, "kalshi_logloss": 0.5971}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2466, "share_ge_15": 0.4441, "median_abs_gap": 13.1, "n": 31931}, "gen1_elo": {"share_ge_25": 0.2446, "share_ge_15": 0.4435, "median_abs_gap": 12.99, "n": 31931}, "gen1_sr": {"share_ge_25": 0.3143, "share_ge_15": 0.5218, "median_abs_gap": 15.95, "n": 31931}, "gen2": {"share_ge_25": 0.3181, "share_ge_15": 0.5126, "median_abs_gap": 15.54, "n": 31931}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1546, "share_ge_15": 0.3602, "median_abs_gap": 10.91, "n": 24841}, "gen1_elo": {"share_ge_25": 0.1555, "share_ge_15": 0.3583, "median_abs_gap": 10.71, "n": 24838}, "gen1_sr": {"share_ge_25": 0.2213, "share_ge_15": 0.4437, "median_abs_gap": 13.02, "n": 24842}, "gen2": {"share_ge_25": 0.2378, "share_ge_15": 0.4444, "median_abs_gap": 13.03, "n": 24843}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.91, "share_ge_25_all": 0.0438, "share_ge_25_pregame_clean": 0.0389}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0539, "share_ge_25_pregame_clean": 0.049}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2345, "share_within_10pp_all": 0.4329, "share_within_10pp_pregame_clean": 0.4849, "corr_model_vs_mid_pregame_clean": 0.8431}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 668, "model_brier": 0.2018, "kalshi_brier": 0.2026, "brier_diff_model_minus_kalshi": -0.0008}, "10-15": {"n_settled": 795, "model_brier": 0.215, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": 0.0083}, "15-25": {"n_settled": 1037, "model_brier": 0.2257, "kalshi_brier": 0.2133, "brier_diff_model_minus_kalshi": 0.0124}, "25-40": {"n_settled": 590, "model_brier": 0.2216, "kalshi_brier": 0.2104, "brier_diff_model_minus_kalshi": 0.0111}, "3-5": {"n_settled": 421, "model_brier": 0.2055, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0008}, "40+": {"n_settled": 116, "model_brier": 0.2743, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0723}, "5-10": {"n_settled": 942, "model_brier": 0.2024, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.0}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.531, "slope": 0.828, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.209, "slope": 1.078, "slope_se": 0.043}, "n": 4569}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.502, "slope": 0.863, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.157, "slope": 1.066, "slope_se": 0.034}, "n": 6648}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 437, "model_brier": 0.3106, "kalshi_brier": 0.2361, "brier_diff_model_minus_kalshi": 0.0746, "brier_diff_se": 0.0144, "corr_model_outcome": 0.0381, "corr_kalshi_outcome": 0.2506}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
