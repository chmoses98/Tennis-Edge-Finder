# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-28T14:17Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 65,274): 0-3 14.2%, 3-5 9.6%, 5-10 20.0%, 10-15 15.3%, 15-25 19.0%, 25-40 13.9%, 40+ 8.0%; median gap 11.87 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.4%, Challenger 11.2%, doubles 6.4%). Main tour: ATP 4.3% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 14,261): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.2%, STALE_QUOTE 18.9%, BOOK_QUALITY 18.8%, POOR_DATA 9.5%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.1%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.2%, market_freshness 18.9%, execution 18.8%, data 13.0%, market_freshness/coverage 9.0%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 14,261 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.9% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.7% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 451.0 points vs 1668.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.015, Gen-2 0.802, Gen-1 ledger 0.853 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 682 model 0.2246 vs Kalshi 0.2077; n 143 model 0.2752 vs Kalshi 0.1915.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 280,137 model-market comparisons (456,119 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 93,920 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-28T14:04:44.667155+00:00'], shadow board 74,564 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-28T14:04:47.916342+00:00'], Model 4 35,490 rows, 22,665 settled tickers, 8,275 tickers with an external scan.
* By model: {"gen1_ledger": 63421, "gen1_elo": 37484, "fair_v1": 37484, "gen2": 37484, "gen1_sr": 37484, "model4_fundamental": 33412, "model4_conditioned": 33368}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 65,274 | 14.2 | 9.6 | 20.0 | 15.3 | 19.0 | 13.9 | 8.0 | 11.87 | 40.9% | 21.9% |
| MW fair_v1 | 37,484 | 13.1 | 8.7 | 18.6 | 15.4 | 19.4 | 15.0 | 9.7 | 13.0 | 44.1% | 24.7% |
| MW gen1_elo | 37,484 | 12.8 | 8.6 | 19.3 | 15.4 | 19.5 | 14.9 | 9.6 | 12.85 | 44.0% | 24.5% |
| MW gen1_ledger | 27,790 | 15.7 | 10.7 | 21.9 | 15.2 | 18.5 | 12.4 | 5.6 | 10.41 | 36.5% | 18.0% |
| MW gen1_sr | 37,484 | 10.2 | 7.1 | 16.8 | 13.7 | 20.7 | 18.7 | 12.7 | 15.9 | 52.1% | 31.4% |
| MW gen2 | 37,484 | 11.1 | 7.5 | 16.4 | 13.9 | 19.4 | 17.9 | 13.8 | 15.48 | 51.1% | 31.7% |
| all families model4_conditioned | 33,368 | 22.2 | 18.2 | 34.4 | 17.3 | 4.9 | 1.9 | 1.1 | 6.02 | 7.9% | 3.0% |
| all families model4_fundamental | 33,412 | 17.2 | 13.2 | 34.0 | 20.3 | 10.2 | 3.6 | 1.4 | 7.72 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.2%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.27pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,321 | 27.1 | 15.6 | 27.4 | 13.5 | 11.7 | 4.1 | 0.6 | 5.92 | 16.4% | 4.7% |
| CHALLENGER | 5,754 | 16.2 | 9.8 | 20.5 | 15.4 | 15.4 | 11.9 | 10.7 | 10.95 | 38.0% | 22.6% |
| ITF_MEN | 10,306 | 10.0 | 7.3 | 16.8 | 15.2 | 21.0 | 17.7 | 12.1 | 15.23 | 50.8% | 29.7% |
| ITF_WOMEN | 14,689 | 9.8 | 7.1 | 15.9 | 15.1 | 22.0 | 18.3 | 11.8 | 15.64 | 52.1% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,372 | 17.9 | 13.8 | 24.4 | 20.2 | 16.4 | 6.6 | 0.7 | 8.25 | 23.6% | 7.2% |
| WTA125 | 1,036 | 16.0 | 7.6 | 22.7 | 19.2 | 20.2 | 12.6 | 1.6 | 10.7 | 34.5% | 14.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,321 | 25.8 | 15.6 | 25.2 | 16.4 | 12.0 | 4.1 | 0.8 | 6.23 | 17.0% | 4.9% |
| CHALLENGER | 5,754 | 15.2 | 8.9 | 18.0 | 14.5 | 18.1 | 13.7 | 11.6 | 12.67 | 43.4% | 25.4% |
| ITF_MEN | 10,306 | 7.9 | 6.1 | 14.7 | 13.6 | 19.7 | 20.8 | 17.2 | 18.19 | 57.7% | 38.0% |
| ITF_WOMEN | 14,689 | 8.0 | 5.7 | 14.1 | 12.7 | 20.6 | 21.4 | 17.4 | 19.19 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,372 | 15.0 | 10.8 | 21.9 | 15.6 | 22.2 | 12.9 | 1.6 | 10.66 | 36.7% | 14.5% |
| WTA125 | 1,036 | 9.4 | 6.3 | 16.3 | 16.8 | 24.5 | 17.9 | 8.9 | 15.57 | 51.2% | 26.7% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,321 | 22.5 | 12.9 | 24.4 | 16.1 | 16.2 | 6.6 | 1.4 | 7.58 | 24.1% | 7.9% |
| CHALLENGER | 5,754 | 15.0 | 9.3 | 21.2 | 15.8 | 15.6 | 12.2 | 10.9 | 11.21 | 38.8% | 23.2% |
| ITF_MEN | 10,306 | 9.4 | 7.1 | 17.2 | 14.2 | 21.6 | 18.1 | 12.2 | 15.76 | 52.0% | 30.4% |
| ITF_WOMEN | 14,689 | 9.6 | 6.8 | 16.4 | 15.8 | 22.2 | 18.1 | 11.1 | 15.47 | 51.4% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,372 | 23.6 | 16.4 | 31.8 | 14.9 | 9.6 | 2.6 | 1.2 | 6.08 | 13.3% | 3.8% |
| WTA125 | 1,036 | 22.2 | 12.9 | 26.5 | 16.6 | 15.0 | 6.4 | 0.4 | 7.96 | 21.7% | 6.8% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,924 | 24.6 | 19.1 | 30.9 | 12.8 | 9.0 | 3.1 | 0.5 | 5.67 | 12.6% | 3.6% |
| CHALLENGER | 3,922 | 22.5 | 14.5 | 26.9 | 14.6 | 13.8 | 6.1 | 1.6 | 7.14 | 21.4% | 7.6% |
| DOUBLES | 1,978 | 5.1 | 4.5 | 12.4 | 10.4 | 21.1 | 25.0 | 21.4 | 23.56 | 67.5% | 46.4% |
| ITF_MEN | 7,926 | 13.1 | 9.3 | 20.9 | 15.9 | 21.4 | 13.3 | 6.2 | 12.05 | 40.9% | 19.4% |
| ITF_WOMEN | 9,432 | 13.1 | 9.0 | 19.6 | 15.6 | 21.4 | 15.6 | 5.8 | 12.5 | 42.8% | 21.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,408 | 24.4 | 15.3 | 29.8 | 17.9 | 9.4 | 2.8 | 0.3 | 6.76 | 12.5% | 3.1% |
| WTA125 | 1,051 | 24.7 | 12.6 | 20.9 | 19.4 | 13.1 | 7.5 | 1.7 | 7.93 | 22.4% | 9.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,231 | 27.4 | 15.7 | 27.8 | 13.4 | 11.5 | 3.8 | 0.4 | 5.86 | 15.7% | 4.2% |
| CHALLENGER | 4,048 | 21.2 | 12.3 | 25.6 | 17.9 | 15.1 | 6.2 | 1.6 | 8.06 | 22.9% | 7.8% |
| ITF_MEN | 7,657 | 12.1 | 8.7 | 20.1 | 17.2 | 21.9 | 14.6 | 5.4 | 12.49 | 41.8% | 19.9% |
| ITF_WOMEN | 11,061 | 11.7 | 8.4 | 18.2 | 17.2 | 23.9 | 15.3 | 5.3 | 13.38 | 44.5% | 20.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,299 | 18.1 | 13.8 | 24.6 | 20.5 | 16.4 | 6.1 | 0.6 | 8.25 | 23.1% | 6.7% |
| WTA125 | 1,001 | 16.3 | 7.5 | 22.3 | 19.5 | 20.7 | 12.4 | 1.4 | 10.77 | 34.5% | 13.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,231 | 26.0 | 15.9 | 25.4 | 16.4 | 12.0 | 3.8 | 0.5 | 6.2 | 16.3% | 4.3% |
| CHALLENGER | 4,048 | 19.5 | 11.3 | 22.6 | 17.0 | 18.4 | 9.3 | 1.9 | 9.08 | 29.6% | 11.2% |
| ITF_MEN | 7,658 | 9.3 | 7.3 | 17.0 | 15.8 | 21.5 | 19.0 | 10.2 | 15.27 | 50.7% | 29.2% |
| ITF_WOMEN | 11,062 | 8.9 | 6.6 | 15.8 | 14.1 | 22.6 | 21.0 | 11.0 | 16.82 | 54.6% | 31.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,299 | 15.1 | 10.9 | 22.0 | 15.7 | 22.4 | 12.7 | 1.3 | 10.59 | 36.4% | 14.0% |
| WTA125 | 1,001 | 9.4 | 6.3 | 16.4 | 17.1 | 24.4 | 18.2 | 8.3 | 15.35 | 50.8% | 26.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,871 | 24.8 | 19.4 | 30.9 | 12.9 | 8.7 | 2.9 | 0.4 | 5.65 | 12.0% | 3.4% |
| CHALLENGER | 3,460 | 23.9 | 15.5 | 28.1 | 14.7 | 13.2 | 4.1 | 0.4 | 6.6 | 17.8% | 4.6% |
| DOUBLES | 1,852 | 5.0 | 4.6 | 12.6 | 10.6 | 21.0 | 24.9 | 21.2 | 23.51 | 67.1% | 46.1% |
| ITF_MEN | 6,787 | 14.0 | 9.9 | 22.4 | 16.5 | 21.4 | 11.8 | 4.0 | 11.05 | 37.1% | 15.8% |
| ITF_WOMEN | 8,027 | 13.8 | 9.4 | 20.9 | 16.3 | 21.5 | 14.5 | 3.6 | 11.66 | 39.6% | 18.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,354 | 24.8 | 15.7 | 29.8 | 17.9 | 9.4 | 2.2 | 0.1 | 6.59 | 11.7% | 2.3% |
| WTA125 | 929 | 26.3 | 13.3 | 22.0 | 20.7 | 11.9 | 5.3 | 0.5 | 7.35 | 17.8% | 5.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,978 | 5.1 | 4.5 | 12.4 | 10.4 | 21.1 | 25.0 | 21.4 | 23.56 | 67.5% | 46.4% |
| singles | 25,812 | 16.5 | 11.2 | 22.6 | 15.6 | 18.3 | 11.4 | 4.4 | 9.91 | 34.1% | 15.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,669 | 13.1 | 9.3 | 20.0 | 15.6 | 19.1 | 13.9 | 9.0 | 12.4 | 42.0% | 22.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 24,328 | 13.6 | 8.8 | 18.5 | 15.2 | 19.2 | 15.2 | 9.7 | 12.94 | 44.0% | 24.8% |
| UNKNOWN | 5,238 | 10.7 | 7.7 | 17.1 | 16.8 | 20.8 | 16.0 | 11.0 | 14.1 | 47.8% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,501 | 19.9 | 12.3 | 22.2 | 15.8 | 14.8 | 9.3 | 5.8 | 8.59 | 29.8% | 15.1% |
| B | 4,571 | 12.9 | 8.8 | 19.0 | 16.3 | 19.4 | 12.8 | 10.7 | 12.61 | 43.0% | 23.6% |
| C | 5,286 | 12.3 | 9.0 | 19.9 | 15.8 | 18.5 | 14.3 | 10.1 | 12.71 | 43.0% | 24.5% |
| D | 5,862 | 12.4 | 8.3 | 17.5 | 15.4 | 21.2 | 15.8 | 9.4 | 13.67 | 46.4% | 25.2% |
| F | 11,264 | 7.5 | 5.6 | 15.0 | 14.6 | 23.2 | 21.1 | 12.9 | 17.8 | 57.3% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,476 | 24.2 | 15.8 | 28.5 | 15.2 | 11.0 | 3.8 | 1.4 | 6.51 | 16.2% | 5.2% |
| B | 3,823 | 16.9 | 10.1 | 24.3 | 16.3 | 19.1 | 10.0 | 3.3 | 9.72 | 32.4% | 13.3% |
| C | 5,376 | 11.3 | 7.9 | 19.4 | 14.6 | 21.1 | 15.5 | 10.1 | 13.45 | 46.8% | 25.7% |
| D | 4,028 | 14.5 | 10.0 | 21.3 | 15.5 | 20.2 | 13.0 | 5.6 | 11.27 | 38.8% | 18.6% |
| F | 7,087 | 10.0 | 8.3 | 15.9 | 14.9 | 23.0 | 20.0 | 7.9 | 15.45 | 50.9% | 27.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,903 | 18.2 | 11.1 | 21.3 | 15.6 | 15.2 | 10.1 | 8.5 | 9.81 | 33.8% | 18.5% |
| LIMITED | 8,095 | 13.9 | 10.0 | 20.3 | 16.3 | 18.9 | 13.3 | 7.2 | 11.63 | 39.5% | 20.5% |
| POOR | 17,486 | 9.2 | 6.5 | 16.0 | 15.0 | 22.5 | 19.1 | 11.7 | 16.09 | 53.3% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,261 | 24.2 | 18.3 | 33.3 | 14.8 | 6.4 | 2.6 | 0.4 | 5.81 | 9.4% | 2.9% |
| GAME_SPREAD | 5,700 | 22.2 | 15.3 | 33.0 | 17.1 | 9.0 | 2.8 | 0.5 | 6.74 | 12.4% | 3.4% |
| MATCH_WINNER | 27,790 | 15.7 | 10.7 | 21.9 | 15.2 | 18.5 | 12.4 | 5.6 | 10.41 | 36.5% | 18.0% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,178 | 27.5 | 16.6 | 31.3 | 12.5 | 9.4 | 2.4 | 0.3 | 5.69 | 12.1% | 2.7% |
| TOTAL_GAMES | 9,468 | 9.2 | 10.3 | 36.1 | 26.9 | 10.6 | 4.1 | 2.8 | 9.34 | 17.5% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,846 | 24.5 | 30.4 | 33.0 | 7.1 | 3.9 | 0.8 | 0.2 | 4.68 | 5.0% | 1.0% |
| GAME_SPREAD | 7,812 | 47.0 | 16.2 | 25.6 | 7.3 | 2.1 | 1.2 | 0.6 | 3.29 | 3.9% | 1.8% |
| TOTAL_GAMES | 13,710 | 6.1 | 8.8 | 40.7 | 31.8 | 7.2 | 3.1 | 2.2 | 9.37 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,857 | 24.0 | 16.9 | 34.9 | 14.3 | 7.1 | 2.5 | 0.4 | 6.0 | 9.9% | 2.9% |
| GAME_SPREAD | 7,815 | 20.0 | 13.4 | 28.2 | 20.5 | 12.5 | 4.3 | 1.1 | 7.82 | 17.9% | 5.4% |
| TOTAL_GAMES | 13,740 | 9.9 | 10.0 | 36.4 | 25.4 | 11.6 | 4.2 | 2.4 | 9.23 | 18.2% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 37,484 | 44.1% | 24.7% | 13.0 | 35.6% | 15.5% | 10.78 |
| gen1_elo | 37,484 | 44.0% | 24.5% | 12.85 | 35.4% | 15.5% | 10.56 |
| gen1_sr | 37,484 | 52.1% | 31.4% | 15.9 | 44.4% | 22.2% | 13.05 |
| gen2 | 37,484 | 51.1% | 31.7% | 15.48 | 44.4% | 23.7% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,199 | 15.6 | 10.6 | 21.3 | 17.2 | 20.0 | 12.0 | 3.4 | 10.71 | 35.4% | 15.4% |
| STALE | 19,285 | 10.7 | 7.0 | 16.1 | 13.8 | 18.9 | 17.8 | 15.7 | 16.02 | 52.4% | 33.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 21,258 | 16.5 | 11.1 | 22.6 | 15.3 | 17.9 | 11.9 | 4.8 | 9.96 | 34.5% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 65,274 | 21258 | 21671 | 22345 | 24.1 | 114.1 | 1400.4 |
| ge_15pp | 26,678 | 7336 | 7724 | 11618 | 26.6 | 415.5 | 1399.2 |
| ge_25pp | 14,261 | 3536 | 3391 | 7334 | 31.4 | 568.2 | 1380.4 |
| lt_10pp | 28,579 | 10660 | 10268 | 7651 | 22.4 | 46.9 | 1341.5 |

Current slate `SL-20261028T141706Z-e40d793c`: 631 priced rows, quote age at build {'median': 12.7, 'max': 12.8}, freshness {'AGING': 631}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 43 | 0.0 | 0.0 | 32.6 | 7.0 | 34.9 | 23.3 | 2.3 | 20.19 | 60.5% | 25.6% |
| EXTERNAL_LONE_OUTLIER | 22 | 72.7 | 27.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,707 | 20.0 | 11.2 | 24.9 | 17.9 | 17.8 | 7.2 | 0.8 | 8.62 | 25.8% | 8.1% |
| KALSHI_LONE_OUTLIER | 26 | 3.9 | 3.9 | 76.9 | 7.7 | 3.9 | 3.9 | 0.0 | 6.31 | 7.7% | 3.9% |
| MARKETS_AGREE | 728 | 65.1 | 34.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.26 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,567 | 0.0 | 2.5 | 35.6 | 26.2 | 24.5 | 10.4 | 0.8 | 12.19 | 35.7% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 37,484 | 6093 (16.2%) | 25.7% | 1.1% | {"EXTERNAL_STALE": 3707, "AGREES_WITH_KALSHI": 1567, "ALL_AGREE": 728, "SUPPORTS_MODEL_DIRECTION": 42, "AGREES_WITH_MODEL": 26, "EXTERNAL_OUTLIER": 22, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 16,543 | 1545 (9.3%) | 36.2% | 1.8% | {"EXTERNAL_STALE": 957, "AGREES_WITH_KALSHI": 560, "SUPPORTS_MODEL_DIRECTION": 26, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,263 | 487 (5.3%) | 36.1% | 2.5% | {"EXTERNAL_STALE": 299, "AGREES_WITH_KALSHI": 176, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,549 | 462 (10.2%) | 36.6% | 2.6% | {"EXTERNAL_STALE": 281, "AGREES_WITH_KALSHI": 169, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 15,150 | 3468 (22.9%) | 17.2% | 1.0% | {"EXTERNAL_STALE": 2085, "ALL_AGREE": 728, "AGREES_WITH_KALSHI": 597, "EXTERNAL_OUTLIER": 22, "AGREES_WITH_MODEL": 22, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,314 | 10.6 | 7.4 | 19.7 | 14.5 | 21.5 | 16.6 | 9.8 | 14.0 | 47.8% | 26.3% |
| 4-10x | 5,005 | 11.4 | 8.6 | 18.5 | 15.4 | 21.6 | 14.7 | 9.8 | 13.57 | 46.1% | 24.5% |
| <2x | 18,996 | 15.2 | 10.1 | 19.4 | 16.2 | 17.4 | 13.1 | 8.7 | 11.57 | 39.2% | 21.8% |
| >=10x | 6,169 | 10.7 | 6.4 | 15.1 | 14.5 | 21.4 | 19.3 | 12.6 | 16.24 | 53.3% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,461 | 12.8 | 8.7 | 19.5 | 16.2 | 19.0 | 13.6 | 10.2 | 12.68 | 42.8% | 23.8% |
| 300-1000 | 8,005 | 12.4 | 8.7 | 17.7 | 15.3 | 20.1 | 16.3 | 9.4 | 13.49 | 45.8% | 25.8% |
| <300 | 12,268 | 8.4 | 5.8 | 15.2 | 14.8 | 22.9 | 20.2 | 12.7 | 17.04 | 55.8% | 32.9% |
| >=3000 | 7,750 | 21.5 | 13.5 | 23.8 | 15.7 | 13.8 | 7.2 | 4.6 | 7.57 | 25.6% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1046 | 0.548 | 0.4094 | 0.4962 | +0.052 | -0.087 | -0.0019 ± 0.0048 |
| ratio 4-10x | 721 | 0.5821 | 0.4362 | 0.4965 | +0.086 | -0.060 | 0.0087 ± 0.0059 |
| ratio <2x | 2549 | 0.5374 | 0.4132 | 0.4492 | +0.088 | -0.036 | 0.0112 ± 0.0029 |
| ratio >=10x | 926 | 0.5682 | 0.3922 | 0.4503 | +0.118 | -0.058 | 0.0131 ± 0.006 |
| thinner_sample 1000-3000 | 1406 | 0.5378 | 0.4105 | 0.4523 | +0.086 | -0.042 | 0.0081 ± 0.0039 |
| thinner_sample 300-1000 | 1177 | 0.5675 | 0.4248 | 0.4894 | +0.078 | -0.065 | 0.0024 ± 0.0047 |
| thinner_sample <300 | 1785 | 0.5594 | 0.3912 | 0.4599 | +0.099 | -0.069 | 0.0108 ± 0.0042 |
| thinner_sample >=3000 | 874 | 0.5335 | 0.4391 | 0.4645 | +0.069 | -0.025 | 0.0132 ± 0.0039 |
| data_status ADEQUATE | 1462 | 0.5344 | 0.4306 | 0.4473 | +0.087 | -0.017 | 0.0133 ± 0.0032 |
| data_status LIMITED | 1232 | 0.5488 | 0.415 | 0.4862 | +0.063 | -0.071 | 0.0028 ± 0.0043 |
| data_status POOR | 2548 | 0.5618 | 0.3997 | 0.4655 | +0.096 | -0.066 | 0.0086 ± 0.0035 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 765 | 0.2003 | 0.2009 | -0.0006 ± 0.0006 | 0.5806 | 0.5822 | 0.5032 | 0.4882 | 0.515 | -0.082 ± 0.0173 | -0.01 (5) |
| 3-5 | 470 | 0.207 | 0.2076 | -0.0007 ± 0.0017 | 0.5979 | 0.5979 | 0.5043 | 0.4644 | 0.4915 | -0.092 ± 0.0215 | 0.02 (1) |
| 5-10 | 1089 | 0.2021 | 0.2023 | -0.0002 ± 0.0021 | 0.5901 | 0.5879 | 0.5101 | 0.4362 | 0.4711 | -0.090 ± 0.0141 | -0.0167 (6) |
| 10-15 | 924 | 0.2211 | 0.2126 | +0.0085 ± 0.0038 | 0.6351 | 0.6113 | 0.527 | 0.4032 | 0.4297 | -0.106 ± 0.0153 | -0.048 (5) |
| 15-25 | 1169 | 0.2243 | 0.2119 | +0.0124 ± 0.0053 | 0.644 | 0.6081 | 0.5749 | 0.3791 | 0.4457 | -0.098 ± 0.0135 | -0.0033 (9) |
| 25-40 | 682 | 0.2246 | 0.2077 | +0.0169 ± 0.0104 | 0.6393 | 0.5974 | 0.6551 | 0.3449 | 0.4721 | -0.075 ± 0.0161 | -0.01 (1) |
| 40+ | 143 | 0.2752 | 0.1915 | +0.0836 ± 0.0318 | 0.7497 | 0.5632 | 0.7392 | 0.2903 | 0.4266 | -0.064 ± 0.0311 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4045 | 0.183 | 0.1836 | -0.0007 ± 0.0002 | 0.541 | 0.5416 | 0.4856 | 0.4704 | 0.4952 | -0.030 ± 0.0068 | -0.0129 (17) |
| 3-5 | 2727 | 0.1966 | 0.195 | +0.0016 ± 0.0007 | 0.5729 | 0.5666 | 0.4846 | 0.4449 | 0.443 | -0.058 ± 0.0086 | 0.0 (2) |
| 5-10 | 5780 | 0.2022 | 0.1983 | +0.0039 ± 0.0009 | 0.5901 | 0.5768 | 0.4841 | 0.4102 | 0.4202 | -0.051 ± 0.0059 | -0.0119 (21) |
| 10-15 | 4964 | 0.203 | 0.1871 | +0.0159 ± 0.0015 | 0.5928 | 0.5499 | 0.485 | 0.3608 | 0.3584 | -0.066 ± 0.0062 | -0.0281 (16) |
| 15-25 | 6128 | 0.2081 | 0.1686 | +0.0395 ± 0.0021 | 0.6092 | 0.5003 | 0.5001 | 0.3036 | 0.3017 | -0.074 ± 0.0052 | -0.0025 (44) |
| 25-40 | 4898 | 0.223 | 0.1259 | +0.0970 ± 0.0032 | 0.6401 | 0.3871 | 0.5273 | 0.2135 | 0.2201 | -0.061 ± 0.0049 | -0.01 (1) |
| 40+ | 3155 | 0.3796 | 0.0451 | +0.3345 ± 0.0043 | 0.9882 | 0.1741 | 0.6302 | 0.1036 | 0.0621 | -0.076 ± 0.0036 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 601 | 0.2078 | 0.2085 | -0.0007 ± 0.0007 | 0.598 | 0.5999 | 0.5089 | 0.4938 | 0.5191 | -0.105 ± 0.0202 | -0.01 (3) |
| 3-5 | 422 | 0.2275 | 0.2244 | +0.0031 ± 0.0018 | 0.6421 | 0.6355 | 0.5104 | 0.4706 | 0.4455 | -0.140 ± 0.0246 | 0.02 (1) |
| 5-10 | 944 | 0.2079 | 0.2073 | +0.0006 ± 0.0022 | 0.6015 | 0.5998 | 0.5498 | 0.4748 | 0.5106 | -0.087 ± 0.0153 | -0.01 (4) |
| 10-15 | 858 | 0.218 | 0.2115 | +0.0065 ± 0.0039 | 0.627 | 0.6102 | 0.5636 | 0.4394 | 0.4779 | -0.106 ± 0.0164 | -0.04 (5) |
| 15-25 | 1226 | 0.2296 | 0.2131 | +0.0165 ± 0.0052 | 0.6536 | 0.6102 | 0.5819 | 0.3867 | 0.4454 | -0.098 ± 0.0134 | -0.0133 (9) |
| 25-40 | 865 | 0.2678 | 0.1981 | +0.0697 ± 0.0095 | 0.7474 | 0.5775 | 0.6546 | 0.3405 | 0.3896 | -0.126 ± 0.0151 | -0.0075 (4) |
| 40+ | 326 | 0.3621 | 0.1658 | +0.1963 ± 0.0224 | 0.9902 | 0.4984 | 0.7315 | 0.2463 | 0.3006 | -0.081 ± 0.0218 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3453 | 0.1918 | 0.192 | -0.0002 ± 0.0003 | 0.5603 | 0.5605 | 0.5088 | 0.4938 | 0.5056 | -0.046 ± 0.0077 | -0.0133 (15) |
| 3-5 | 2323 | 0.1991 | 0.1976 | +0.0015 ± 0.0007 | 0.5761 | 0.5723 | 0.5138 | 0.474 | 0.474 | -0.054 ± 0.0095 | 0.02 (1) |
| 5-10 | 5142 | 0.199 | 0.1954 | +0.0035 ± 0.0009 | 0.5834 | 0.5701 | 0.5161 | 0.4419 | 0.4582 | -0.044 ± 0.0062 | -0.0117 (6) |
| 10-15 | 4426 | 0.2059 | 0.1936 | +0.0122 ± 0.0017 | 0.6019 | 0.5648 | 0.5124 | 0.3885 | 0.4019 | -0.054 ± 0.0067 | -0.0189 (18) |
| 15-25 | 6172 | 0.2173 | 0.18 | +0.0373 ± 0.0021 | 0.6315 | 0.5289 | 0.5217 | 0.3262 | 0.3325 | -0.066 ± 0.0054 | -0.0086 (42) |
| 25-40 | 5679 | 0.2521 | 0.1371 | +0.1151 ± 0.0031 | 0.7098 | 0.4205 | 0.5569 | 0.2404 | 0.2199 | -0.086 ± 0.0049 | -0.0044 (18) |
| 40+ | 4502 | 0.3958 | 0.0589 | +0.3369 ± 0.0042 | 1.0413 | 0.2123 | 0.6504 | 0.1177 | 0.0813 | -0.073 ± 0.0035 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 737 | 0.1979 | 0.1999 | -0.0021 ± 0.0006 | 0.5752 | 0.5803 | 0.5008 | 0.4856 | 0.5441 | -0.039 ± 0.0172 | -0.0137 (8) |
| 3-5 | 509 | 0.2044 | 0.2028 | +0.0016 ± 0.0016 | 0.5922 | 0.5863 | 0.4995 | 0.4598 | 0.4617 | -0.119 ± 0.0208 | 0.0067 (3) |
| 5-10 | 1126 | 0.2031 | 0.2014 | +0.0017 ± 0.002 | 0.592 | 0.5856 | 0.509 | 0.4351 | 0.46 | -0.095 ± 0.0137 | -0.0071 (7) |
| 10-15 | 917 | 0.2114 | 0.2075 | +0.0040 ± 0.0037 | 0.613 | 0.5999 | 0.5381 | 0.4149 | 0.4613 | -0.093 ± 0.0151 | -0.0317 (6) |
| 15-25 | 1104 | 0.232 | 0.2156 | +0.0164 ± 0.0054 | 0.6619 | 0.6163 | 0.5873 | 0.3927 | 0.4484 | -0.109 ± 0.014 | -0.03 (1) |
| 25-40 | 695 | 0.215 | 0.2144 | +0.0006 ± 0.0103 | 0.6196 | 0.6129 | 0.6633 | 0.3526 | 0.505 | -0.060 ± 0.016 | 0.015 (2) |
| 40+ | 154 | 0.292 | 0.1999 | +0.0922 ± 0.0315 | 0.7982 | 0.5818 | 0.7481 | 0.2977 | 0.4286 | -0.066 ± 0.0328 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3975 | 0.1846 | 0.1852 | -0.0005 ± 0.0002 | 0.5435 | 0.5444 | 0.4849 | 0.4696 | 0.4845 | -0.037 ± 0.0069 | -0.0163 (35) |
| 3-5 | 2669 | 0.2007 | 0.1986 | +0.0021 ± 0.0007 | 0.5846 | 0.5775 | 0.4857 | 0.4461 | 0.441 | -0.063 ± 0.0088 | -0.0094 (18) |
| 5-10 | 5993 | 0.1947 | 0.1904 | +0.0043 ± 0.0008 | 0.5726 | 0.5577 | 0.4851 | 0.411 | 0.4192 | -0.051 ± 0.0057 | -0.01 (31) |
| 10-15 | 4852 | 0.1941 | 0.1805 | +0.0136 ± 0.0015 | 0.5725 | 0.5342 | 0.4952 | 0.372 | 0.378 | -0.059 ± 0.0061 | -0.015 (12) |
| 15-25 | 6227 | 0.2129 | 0.1727 | +0.0403 ± 0.0021 | 0.62 | 0.5096 | 0.5115 | 0.3164 | 0.3117 | -0.076 ± 0.0053 | -0.03 (2) |
| 25-40 | 4848 | 0.2186 | 0.1289 | +0.0897 ± 0.0032 | 0.6313 | 0.3933 | 0.53 | 0.2143 | 0.2323 | -0.052 ± 0.005 | 0.01 (3) |
| 40+ | 3133 | 0.3919 | 0.0507 | +0.3412 ± 0.0045 | 1.0228 | 0.1891 | 0.6413 | 0.1113 | 0.0683 | -0.078 ± 0.0038 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1130 | 0.1961 | 0.1962 | -0.0001 ± 0.0005 | 0.5713 | 0.5711 | 0.5053 | 0.4902 | 0.4947 | -0.067 ± 0.0134 | -0.0224 (49) |
| 3-5 | 786 | 0.1884 | 0.188 | +0.0004 ± 0.0012 | 0.5522 | 0.5503 | 0.495 | 0.4552 | 0.4682 | -0.060 ± 0.0158 | -0.0194 (34) |
| 5-10 | 1647 | 0.2029 | 0.1976 | +0.0053 ± 0.0017 | 0.596 | 0.5793 | 0.4986 | 0.425 | 0.4268 | -0.076 ± 0.0112 | -0.005 (78) |
| 10-15 | 1125 | 0.2152 | 0.2035 | +0.0117 ± 0.0033 | 0.6225 | 0.5911 | 0.5321 | 0.4094 | 0.4213 | -0.081 ± 0.0138 | 0.0014 (64) |
| 15-25 | 1454 | 0.2321 | 0.2114 | +0.0206 ± 0.0047 | 0.6613 | 0.6079 | 0.5794 | 0.3846 | 0.4312 | -0.079 ± 0.0122 | -0.0214 (59) |
| 25-40 | 910 | 0.2438 | 0.2095 | +0.0343 ± 0.0093 | 0.6967 | 0.6008 | 0.6791 | 0.3673 | 0.4681 | -0.090 ± 0.0142 | -0.0219 (26) |
| 40+ | 302 | 0.3403 | 0.2009 | +0.1393 ± 0.025 | 0.983 | 0.5869 | 0.8093 | 0.3306 | 0.4404 | -0.099 ± 0.0234 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4022 | 0.1778 | 0.1779 | -0.0002 ± 0.0002 | 0.5259 | 0.5258 | 0.5069 | 0.4917 | 0.5012 | -0.040 ± 0.0067 | -0.0157 (88) |
| 3-5 | 2749 | 0.1939 | 0.1924 | +0.0015 ± 0.0007 | 0.5647 | 0.5616 | 0.5032 | 0.4634 | 0.4645 | -0.050 ± 0.0085 | -0.0209 (69) |
| 5-10 | 5606 | 0.1994 | 0.1918 | +0.0076 ± 0.0009 | 0.5869 | 0.5645 | 0.4953 | 0.4217 | 0.4081 | -0.070 ± 0.0059 | -0.0082 (132) |
| 10-15 | 3940 | 0.2126 | 0.1966 | +0.0160 ± 0.0018 | 0.6168 | 0.5751 | 0.5312 | 0.4084 | 0.4041 | -0.069 ± 0.0071 | -0.0053 (105) |
| 15-25 | 4815 | 0.2299 | 0.2006 | +0.0293 ± 0.0025 | 0.6616 | 0.5803 | 0.5658 | 0.3703 | 0.3942 | -0.063 ± 0.0065 | -0.0253 (107) |
| 25-40 | 3281 | 0.2594 | 0.1854 | +0.0740 ± 0.0047 | 0.7346 | 0.5415 | 0.6323 | 0.3193 | 0.3603 | -0.079 ± 0.0073 | -0.0229 (51) |
| 40+ | 1413 | 0.3765 | 0.1489 | +0.2275 ± 0.0107 | 1.0639 | 0.4479 | 0.7324 | 0.2311 | 0.2668 | -0.075 ± 0.0097 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5242 | 1.015 ± 0.039 | 1.088 | 0.1679 | 0.1655 | 0.2155 | 0.2069 |
| gen2 | 5242 | 0.802 ± 0.035 | 1.046 | 0.1694 | 0.166 | 0.2357 | 0.2067 |
| gen1_elo | 5242 | 0.993 ± 0.037 | 1.087 | 0.1746 | 0.1657 | 0.2142 | 0.207 |
| gen1_sr | 5242 | 0.978 ± 0.046 | 1.109 | 0.1298 | 0.1679 | 0.2315 | 0.2064 |
| gen1_ledger | 7354 | 0.853 ± 0.028 | 1.051 | 0.1854 | 0.1769 | 0.2187 | 0.2016 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 26,678)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,855 | 21.9% |
| STALE_QUOTE | market_freshness | 5,824 | 21.8% |
| BOOK_QUALITY | execution | 5,148 | 19.3% |
| POOR_DATA | data | 3,160 | 11.8% |
| LIMITED_DATA | data | 1,665 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,471 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,209 | 4.5% |
| IDENTITY_AMBIGUOUS | mapping | 1,109 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 774 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 462 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 21.9%, market_freshness 21.8%, execution 19.3%, data 18.1%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.5%, mapping 4.2%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.7%, THIN_PLAYER_HISTORY 60.7%, STALE_PLAYER_DATA 52.4%, STALE_KALSHI_QUOTE 43.5%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.2%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 15.8%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.5%, POST_SETTLEMENT_OBSERVATION 21.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 14,261)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,735 | 33.2% |
| STALE_QUOTE | market_freshness | 2,697 | 18.9% |
| BOOK_QUALITY | execution | 2,681 | 18.8% |
| POOR_DATA | data | 1,352 | 9.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 781 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 589 | 4.1% |
| LIMITED_DATA | data | 500 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 499 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 307 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 119 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.2%, market_freshness 18.9%, execution 18.8%, data 13.0%, market_freshness/coverage 9.0%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 63.1%, STALE_KALSHI_QUOTE 51.4%, STALE_PLAYER_DATA 46.8%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 24.6%, PLAYER_IDENTITY_RISK 18.7%, MODEL_HIGH_UNCERTAINTY 18.3%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.3%, POST_SETTLEMENT_OBSERVATION 33.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 11280, "IDENTITY_AMBIGUOUS": 2981}; ticker orientation: {"VERIFIED": 14261}.

Checks: discipline:AMBIGUOUS 918, discipline:PASS 13343, identity_confidence:AMBIGUOUS 2665, identity_confidence:PASS 11596, level_mapping:NA 930, level_mapping:PASS 13331, market_pair:AMBIGUOUS 475, market_pair:NA 335, market_pair:PASS 13451, model_complement:NA 299, model_complement:PASS 13962, namesake:AMBIGUOUS 6, namesake:PASS 14255, physical_match_id:NA 4998, physical_match_id:PASS 9263, player_ids:PASS 14261, same_pair_other_event:PASS 14261, ticker_orientation:PASS 14261

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,245 | 4.3% | 3.9% | 1.6% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 15, "coverage": 13} | 5.81 | 0.2198 / 0.2156 (589) | 21.2% | 3.0% | 3.3% | 2.7% |
| CHALLENGER | 9,676 | 16.6% | 6.3% | 11.2% | {"coverage": 934, "market_freshness/coverage": 193, "market_freshness": 167, "data": 144, "model_calibration_or_unknown": 74, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.29 | 0.2196 / 0.2106 (2209) | 35.0% | 15.9% | 4.1% | 22.4% |
| DOUBLES | 1,978 | 46.4% | 46.1% | 6.4% | {"execution": 518, "mapping": 230, "market_freshness": 106, "market_freshness/coverage": 57, "coverage": 7} | 23.51 | 0.3104 / 0.2375 (471) | 11.8% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 18,232 | 25.3% | 18.0% | 32.3% | {"coverage": 1586, "execution": 880, "market_freshness": 838, "data": 685, "market_freshness/coverage": 424, "mapping": 186, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.82 | 0.2169 / 0.2 (3734) | 36.8% | 70.5% | 17.4% | 20.8% |
| ITF_WOMEN | 24,121 | 26.7% | 19.6% | 45.1% | {"coverage": 2161, "market_freshness": 1387, "execution": 1170, "data": 930, "market_freshness/coverage": 538, "mapping": 150, "model_calibration_or_unknown": 82, "model_calibration": 18} | 12.66 | 0.2053 / 0.197 (4350) | 38.8% | 58.1% | 10.2% | 20.9% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,780 | 5.7% | 5.0% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "execution": 27, "coverage": 21, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.59 | 0.2347 / 0.2278 (591) | 25.7% | 1.1% | 1.4% | 3.4% |
| WTA125 | 2,087 | 11.7% | 10.0% | 1.7% | {"market_freshness": 64, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.18 | 0.2114 / 0.195 (610) | 25.2% | 11.7% | 5.1% | 7.5% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 172 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 6 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 7 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 517 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 8 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 9 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 12 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 13 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 16 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 17 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 18 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 19 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 20 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 21 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 22 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 23 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 24 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 25 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 26 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 27 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 30 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 33 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 34 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 35 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 36 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 37 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 39 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 40 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 41 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 42 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 43 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 44 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 46 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 48 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 49 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 50 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.969, "by_level_share_of_ge_25pp": {"ATP": 0.0158, "CHALLENGER": 0.1123, "DOUBLES": 0.0644, "ITF_MEN": 0.323, "ITF_WOMEN": 0.4513, "OTHER": 0.0008, "WTA": 0.0151, "WTA125": 0.0172}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5143, "share_primary_cause_market_settled_or_in_play": 0.4218, "share_primary_cause_stale_quote_only": 0.1891}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 14261, "identity_ambiguous_share": 0.209, "ticker_orientation": {"VERIFIED": 14261}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9263, "with_external": 487, "coverage": 0.0526, "external_status": {"EXTERNAL_STALE": 299, "AGREES_WITH_KALSHI": 176, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 299, "MODEL_LONE_OUTLIER": 176, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3614, "share_external_supports_model": 0.0246}, "pregame_clean_ge_25pp": {"n": 4549, "with_external": 462, "coverage": 0.1016, "external_status": {"EXTERNAL_STALE": 281, "AGREES_WITH_KALSHI": 169, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 281, "MODEL_LONE_OUTLIER": 169, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3658, "share_external_supports_model": 0.026}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 451.0, "median_sample_ratio": 2.5, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2132, "data_status": {"POOR": 8144, "LIMITED": 3614, "ADEQUATE": 2503}, "comparison_lt_10pp": {"median_thinner_serve_points": 1668.0, "median_sample_ratio": 1.72, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1046, "model_minus_observed": 0.0519, "kalshi_minus_observed": -0.0868, "brier_diff_model_minus_kalshi": -0.0019}, "4-10x": {"n": 721, "model_minus_observed": 0.0856, "kalshi_minus_observed": -0.0603, "brier_diff_model_minus_kalshi": 0.0087}, "<2x": {"n": 2549, "model_minus_observed": 0.0882, "kalshi_minus_observed": -0.036, "brier_diff_model_minus_kalshi": 0.0112}, ">=10x": {"n": 926, "model_minus_observed": 0.1178, "kalshi_minus_observed": -0.0581, "brier_diff_model_minus_kalshi": 0.0131}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5242, "model": {"intercept": -0.535, "slope": 0.802, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.19, "slope": 1.046, "slope_se": 0.039}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.166, "model_brier": 0.2357, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.0289, "brier_diff_se": 0.0026, "model_logloss": 0.669, "kalshi_logloss": 0.5968}, "fair_v1": {"n": 5242, "model": {"intercept": -0.409, "slope": 1.015, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.088, "slope_se": 0.04}, "mean_extremity_model": 0.1679, "mean_extremity_kalshi": 0.1655, "model_brier": 0.2155, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0086, "brier_diff_se": 0.0022, "model_logloss": 0.6201, "kalshi_logloss": 0.5972}, "gen1_elo": {"n": 5242, "model": {"intercept": -0.384, "slope": 0.993, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.307, "slope": 1.087, "slope_se": 0.039}, "mean_extremity_model": 0.1746, "mean_extremity_kalshi": 0.1657, "model_brier": 0.2142, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0072, "brier_diff_se": 0.0022, "model_logloss": 0.6178, "kalshi_logloss": 0.5974}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2471, "share_ge_15": 0.4413, "median_abs_gap": 13.0, "n": 37484}, "gen1_elo": {"share_ge_25": 0.2449, "share_ge_15": 0.4398, "median_abs_gap": 12.85, "n": 37484}, "gen1_sr": {"share_ge_25": 0.3135, "share_ge_15": 0.521, "median_abs_gap": 15.9, "n": 37484}, "gen2": {"share_ge_25": 0.3166, "share_ge_15": 0.5109, "median_abs_gap": 15.48, "n": 37484}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1552, "share_ge_15": 0.3564, "median_abs_gap": 10.78, "n": 29303}, "gen1_elo": {"share_ge_25": 0.155, "share_ge_15": 0.3539, "median_abs_gap": 10.56, "n": 29301}, "gen1_sr": {"share_ge_25": 0.2218, "share_ge_15": 0.4443, "median_abs_gap": 13.05, "n": 29304}, "gen2": {"share_ge_25": 0.2373, "share_ge_15": 0.4435, "median_abs_gap": 13.0, "n": 29305}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.81, "share_ge_25_all": 0.0431, "share_ge_25_pregame_clean": 0.0388}, "WTA": {"median_abs_gap_pregame_clean": 7.59, "share_ge_25_all": 0.0571, "share_ge_25_pregame_clean": 0.0504}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2377, "share_within_10pp_all": 0.4378, "share_within_10pp_pregame_clean": 0.489, "corr_model_vs_mid_pregame_clean": 0.849}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 765, "model_brier": 0.2003, "kalshi_brier": 0.2009, "brier_diff_model_minus_kalshi": -0.0006}, "10-15": {"n_settled": 924, "model_brier": 0.2211, "kalshi_brier": 0.2126, "brier_diff_model_minus_kalshi": 0.0085}, "15-25": {"n_settled": 1169, "model_brier": 0.2243, "kalshi_brier": 0.2119, "brier_diff_model_minus_kalshi": 0.0124}, "25-40": {"n_settled": 682, "model_brier": 0.2246, "kalshi_brier": 0.2077, "brier_diff_model_minus_kalshi": 0.0169}, "3-5": {"n_settled": 470, "model_brier": 0.207, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": -0.0007}, "40+": {"n_settled": 143, "model_brier": 0.2752, "kalshi_brier": 0.1915, "brier_diff_model_minus_kalshi": 0.0836}, "5-10": {"n_settled": 1089, "model_brier": 0.2021, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": -0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.535, "slope": 0.802, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.19, "slope": 1.046, "slope_se": 0.039}, "n": 5242}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.489, "slope": 0.853, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.162, "slope": 1.051, "slope_se": 0.032}, "n": 7354}, "NO_SKILL:gen2|WTA": {"n_settled": 235, "model_brier": 0.2568, "kalshi_brier": 0.2361, "brier_diff_model_minus_kalshi": 0.0207, "brier_diff_se": 0.0103, "corr_model_outcome": 0.2213, "corr_kalshi_outcome": 0.2536}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 471, "model_brier": 0.3104, "kalshi_brier": 0.2375, "brier_diff_model_minus_kalshi": 0.0729, "brier_diff_se": 0.0139, "corr_model_outcome": 0.0487, "corr_kalshi_outcome": 0.2375}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
