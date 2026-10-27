# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-27T13:53Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 59,832): 0-3 14.0%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 19.2%, 25-40 14.0%, 40+ 8.0%; median gap 11.96 pp.
* **Where the extremes live**: 96.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.6%, Challenger 11.7%, doubles 6.7%). Main tour: ATP 4.5% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 13,120): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.1%, BOOK_QUALITY 19.1%, STALE_QUOTE 18.9%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.3%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.1%, execution 19.1%, market_freshness 18.9%, data 12.7%, market_freshness/coverage 8.8%, mapping 4.3%, model_calibration_or_unknown 2.3%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 41.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 13,120 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.7% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 459.0 points vs 1763.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.027, Gen-2 0.814, Gen-1 ledger 0.857 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 626 model 0.2219 vs Kalshi 0.2098; n 129 model 0.2737 vs Kalshi 0.2.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 261,773 model-market comparisons (423,599 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 87,565 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-27T13:36:42.830142+00:00'], shadow board 68,719 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-27T13:36:47.540252+00:00'], Model 4 33,920 rows, 21,568 settled tickers, 7,752 tickers with an external scan.
* By model: {"gen1_ledger": 59673, "gen1_elo": 34551, "fair_v1": 34551, "gen2": 34551, "gen1_sr": 34551, "model4_fundamental": 31970, "model4_conditioned": 31926}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 59,832 | 14.0 | 9.6 | 19.9 | 15.4 | 19.2 | 14.0 | 8.0 | 11.96 | 41.1% | 21.9% |
| MW fair_v1 | 34,551 | 12.9 | 8.7 | 18.6 | 15.6 | 19.7 | 14.9 | 9.6 | 13.04 | 44.2% | 24.5% |
| MW gen1_elo | 34,551 | 12.8 | 8.5 | 19.2 | 15.4 | 19.8 | 14.7 | 9.5 | 12.85 | 44.0% | 24.2% |
| MW gen1_ledger | 25,281 | 15.5 | 10.7 | 21.8 | 15.2 | 18.4 | 12.7 | 5.7 | 10.49 | 36.8% | 18.4% |
| MW gen1_sr | 34,551 | 10.3 | 7.2 | 16.9 | 13.6 | 20.7 | 18.6 | 12.7 | 15.88 | 52.0% | 31.3% |
| MW gen2 | 34,551 | 11.2 | 7.5 | 16.3 | 13.9 | 19.5 | 17.9 | 13.8 | 15.5 | 51.2% | 31.7% |
| all families model4_conditioned | 31,926 | 22.1 | 18.3 | 34.5 | 17.4 | 4.9 | 1.8 | 1.1 | 6.04 | 7.8% | 2.9% |
| all families model4_fundamental | 31,970 | 17.0 | 13.2 | 34.0 | 20.5 | 10.3 | 3.7 | 1.4 | 7.76 | 15.3% | 5.0% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.5%, >=15pp 41.1%, >=20pp 30.5%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.35pp; >=10pp 44.9%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,182 | 27.2 | 15.5 | 26.9 | 14.1 | 11.5 | 4.3 | 0.6 | 5.94 | 16.4% | 4.9% |
| CHALLENGER | 5,469 | 15.9 | 9.9 | 20.3 | 15.8 | 15.5 | 12.0 | 10.6 | 11.06 | 38.1% | 22.6% |
| ITF_MEN | 9,214 | 9.9 | 7.2 | 16.5 | 14.8 | 21.7 | 17.6 | 12.2 | 15.53 | 51.5% | 29.9% |
| ITF_WOMEN | 13,463 | 9.6 | 7.0 | 15.9 | 15.3 | 22.4 | 18.3 | 11.7 | 15.67 | 52.3% | 30.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,266 | 17.0 | 13.8 | 25.1 | 20.5 | 16.6 | 6.5 | 0.6 | 8.39 | 23.7% | 7.1% |
| WTA125 | 951 | 14.8 | 7.3 | 23.0 | 20.1 | 20.8 | 12.2 | 1.8 | 11.03 | 34.8% | 14.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,182 | 25.3 | 15.4 | 25.3 | 17.0 | 11.9 | 4.3 | 0.8 | 6.38 | 17.0% | 5.1% |
| CHALLENGER | 5,469 | 15.1 | 8.7 | 18.1 | 14.7 | 18.1 | 13.9 | 11.5 | 12.69 | 43.4% | 25.3% |
| ITF_MEN | 9,214 | 8.0 | 6.0 | 14.2 | 12.9 | 20.0 | 21.1 | 17.9 | 18.84 | 59.0% | 39.0% |
| ITF_WOMEN | 13,463 | 8.1 | 5.6 | 13.9 | 12.9 | 20.6 | 21.4 | 17.5 | 19.21 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,266 | 14.4 | 10.7 | 22.4 | 15.9 | 22.4 | 12.8 | 1.4 | 10.77 | 36.6% | 14.2% |
| WTA125 | 951 | 8.4 | 6.2 | 16.6 | 17.5 | 24.3 | 18.3 | 8.7 | 15.68 | 51.3% | 27.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,182 | 22.8 | 12.5 | 24.6 | 16.1 | 16.1 | 6.5 | 1.4 | 7.58 | 24.0% | 7.9% |
| CHALLENGER | 5,469 | 14.6 | 9.2 | 21.2 | 16.0 | 15.9 | 12.3 | 10.8 | 11.34 | 39.0% | 23.2% |
| ITF_MEN | 9,214 | 9.7 | 7.1 | 16.6 | 14.0 | 22.2 | 18.0 | 12.4 | 16.01 | 52.6% | 30.4% |
| ITF_WOMEN | 13,463 | 9.4 | 6.7 | 16.4 | 15.9 | 22.6 | 18.1 | 10.9 | 15.51 | 51.6% | 29.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,266 | 23.7 | 16.4 | 31.5 | 15.2 | 9.6 | 2.5 | 1.1 | 6.08 | 13.2% | 3.6% |
| WTA125 | 951 | 22.4 | 11.9 | 27.0 | 16.5 | 15.6 | 6.2 | 0.4 | 7.99 | 22.2% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,864 | 24.7 | 19.1 | 30.7 | 12.8 | 9.1 | 3.2 | 0.5 | 5.75 | 12.8% | 3.7% |
| CHALLENGER | 3,773 | 21.8 | 14.3 | 26.9 | 14.9 | 14.2 | 6.3 | 1.6 | 7.3 | 22.0% | 7.9% |
| DOUBLES | 1,845 | 5.2 | 4.5 | 12.1 | 10.4 | 20.5 | 25.4 | 21.9 | 23.87 | 67.8% | 47.3% |
| ITF_MEN | 6,940 | 12.9 | 9.1 | 20.2 | 16.1 | 21.6 | 13.8 | 6.4 | 12.27 | 41.8% | 20.2% |
| ITF_WOMEN | 8,406 | 12.8 | 8.8 | 19.5 | 15.4 | 21.3 | 16.3 | 5.8 | 12.66 | 43.5% | 22.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,334 | 23.7 | 15.6 | 30.1 | 17.8 | 9.6 | 3.0 | 0.3 | 6.79 | 12.9% | 3.3% |
| WTA125 | 970 | 23.1 | 13.2 | 21.0 | 18.9 | 14.0 | 7.9 | 1.9 | 8.21 | 23.8% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,102 | 27.5 | 15.7 | 27.2 | 14.0 | 11.3 | 3.9 | 0.4 | 5.92 | 15.6% | 4.3% |
| CHALLENGER | 3,887 | 20.7 | 12.4 | 25.0 | 18.3 | 15.5 | 6.5 | 1.6 | 8.34 | 23.7% | 8.1% |
| ITF_MEN | 6,813 | 12.0 | 8.6 | 19.8 | 16.8 | 22.8 | 14.6 | 5.5 | 12.87 | 42.9% | 20.1% |
| ITF_WOMEN | 10,180 | 11.3 | 8.2 | 18.1 | 17.3 | 24.2 | 15.4 | 5.4 | 13.54 | 45.1% | 20.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,200 | 17.2 | 13.7 | 25.1 | 20.7 | 16.6 | 6.1 | 0.6 | 8.36 | 23.3% | 6.7% |
| WTA125 | 921 | 15.1 | 7.2 | 22.7 | 20.3 | 21.4 | 11.8 | 1.5 | 11.07 | 34.7% | 13.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,102 | 25.6 | 15.7 | 25.5 | 16.9 | 11.8 | 4.0 | 0.5 | 6.26 | 16.3% | 4.5% |
| CHALLENGER | 3,887 | 19.2 | 11.0 | 22.4 | 17.3 | 18.5 | 9.6 | 2.0 | 9.3 | 30.1% | 11.6% |
| ITF_MEN | 6,814 | 9.4 | 7.1 | 16.5 | 14.8 | 21.9 | 19.3 | 11.0 | 15.67 | 52.2% | 30.3% |
| ITF_WOMEN | 10,181 | 9.1 | 6.4 | 15.4 | 14.3 | 22.6 | 20.9 | 11.2 | 16.89 | 54.8% | 32.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,200 | 14.4 | 10.7 | 22.5 | 15.9 | 22.4 | 12.7 | 1.3 | 10.74 | 36.4% | 14.0% |
| WTA125 | 921 | 8.4 | 6.2 | 16.7 | 17.8 | 24.2 | 18.7 | 8.0 | 15.35 | 50.9% | 26.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,811 | 24.8 | 19.3 | 30.7 | 12.9 | 8.8 | 3.0 | 0.4 | 5.67 | 12.3% | 3.5% |
| CHALLENGER | 3,328 | 23.2 | 15.3 | 28.2 | 15.0 | 13.6 | 4.4 | 0.5 | 6.79 | 18.4% | 4.8% |
| DOUBLES | 1,725 | 5.2 | 4.6 | 12.3 | 10.6 | 20.4 | 25.3 | 21.7 | 23.84 | 67.4% | 47.0% |
| ITF_MEN | 5,881 | 13.8 | 9.6 | 21.8 | 16.9 | 21.5 | 12.2 | 4.1 | 11.43 | 37.9% | 16.3% |
| ITF_WOMEN | 7,107 | 13.6 | 9.3 | 20.8 | 16.1 | 21.5 | 15.2 | 3.5 | 11.78 | 40.2% | 18.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,280 | 24.1 | 16.0 | 30.1 | 17.8 | 9.6 | 2.3 | 0.1 | 6.64 | 12.0% | 2.4% |
| WTA125 | 855 | 24.8 | 14.3 | 22.1 | 20.0 | 12.8 | 5.5 | 0.6 | 7.39 | 18.8% | 6.1% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,845 | 5.2 | 4.5 | 12.1 | 10.4 | 20.5 | 25.4 | 21.9 | 23.87 | 67.8% | 47.3% |
| singles | 23,436 | 16.3 | 11.2 | 22.6 | 15.6 | 18.3 | 11.7 | 4.4 | 9.99 | 34.4% | 16.1% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,414 | 12.8 | 9.2 | 20.0 | 15.8 | 19.0 | 13.9 | 9.3 | 12.52 | 42.2% | 23.2% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 22,017 | 13.4 | 8.8 | 18.4 | 15.3 | 19.6 | 14.9 | 9.4 | 13.0 | 44.0% | 24.4% |
| UNKNOWN | 4,871 | 10.8 | 7.3 | 17.1 | 16.8 | 20.8 | 16.1 | 11.1 | 14.11 | 47.9% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,976 | 19.8 | 12.4 | 22.1 | 16.1 | 14.7 | 9.1 | 5.8 | 8.73 | 29.6% | 14.9% |
| B | 4,254 | 12.6 | 8.7 | 19.2 | 16.6 | 19.5 | 12.8 | 10.7 | 12.72 | 43.1% | 23.5% |
| C | 4,759 | 11.8 | 8.9 | 19.4 | 16.0 | 19.4 | 14.4 | 10.0 | 13.0 | 43.9% | 24.4% |
| D | 5,257 | 12.3 | 8.1 | 17.6 | 15.3 | 21.4 | 15.7 | 9.6 | 13.83 | 46.8% | 25.4% |
| F | 10,305 | 7.3 | 5.5 | 15.0 | 14.6 | 23.8 | 21.1 | 12.7 | 17.83 | 57.6% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,142 | 23.8 | 15.9 | 28.8 | 15.1 | 11.2 | 3.9 | 1.3 | 6.55 | 16.4% | 5.2% |
| B | 3,435 | 16.5 | 10.2 | 24.0 | 16.2 | 19.4 | 10.3 | 3.4 | 9.83 | 33.1% | 13.7% |
| C | 4,835 | 11.0 | 7.4 | 19.0 | 14.5 | 21.2 | 16.1 | 10.8 | 14.11 | 48.1% | 26.9% |
| D | 3,505 | 14.1 | 9.8 | 20.7 | 15.5 | 20.7 | 13.6 | 5.7 | 11.63 | 39.9% | 19.3% |
| F | 6,364 | 9.8 | 8.1 | 15.5 | 15.1 | 22.7 | 20.8 | 7.9 | 15.76 | 51.4% | 28.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,307 | 18.0 | 11.2 | 21.3 | 15.9 | 15.2 | 10.0 | 8.4 | 9.88 | 33.6% | 18.4% |
| LIMITED | 7,333 | 13.6 | 9.9 | 20.0 | 16.5 | 19.6 | 13.2 | 7.2 | 11.91 | 40.0% | 20.4% |
| POOR | 15,911 | 9.0 | 6.4 | 16.0 | 14.9 | 22.9 | 19.1 | 11.6 | 16.21 | 53.7% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,046 | 24.4 | 18.5 | 33.2 | 14.6 | 6.3 | 2.6 | 0.3 | 5.74 | 9.2% | 2.9% |
| GAME_SPREAD | 5,560 | 22.3 | 15.4 | 33.2 | 16.7 | 9.1 | 2.8 | 0.5 | 6.71 | 12.4% | 3.3% |
| MATCH_WINNER | 25,281 | 15.5 | 10.7 | 21.8 | 15.2 | 18.4 | 12.7 | 5.7 | 10.49 | 36.8% | 18.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,672 | 27.8 | 16.5 | 31.0 | 12.6 | 9.3 | 2.5 | 0.3 | 5.68 | 12.1% | 2.8% |
| TOTAL_GAMES | 9,090 | 9.2 | 10.1 | 36.2 | 27.1 | 10.5 | 4.0 | 2.8 | 9.34 | 17.3% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,384 | 24.6 | 30.8 | 32.8 | 6.9 | 4.0 | 0.8 | 0.2 | 4.67 | 5.0% | 1.0% |
| GAME_SPREAD | 7,484 | 46.7 | 16.4 | 25.8 | 7.5 | 1.9 | 1.1 | 0.5 | 3.32 | 3.6% | 1.7% |
| TOTAL_GAMES | 13,058 | 5.8 | 8.5 | 40.9 | 32.2 | 7.3 | 3.1 | 2.2 | 9.44 | 12.7% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,395 | 23.8 | 16.9 | 35.0 | 14.2 | 7.2 | 2.5 | 0.3 | 6.02 | 10.1% | 2.9% |
| GAME_SPREAD | 7,487 | 19.8 | 13.4 | 28.4 | 20.7 | 12.3 | 4.4 | 1.1 | 7.85 | 17.8% | 5.4% |
| TOTAL_GAMES | 13,088 | 9.4 | 9.9 | 36.5 | 25.7 | 11.8 | 4.3 | 2.4 | 9.29 | 18.4% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 34,551 | 44.2% | 24.5% | 13.04 | 36.0% | 15.5% | 10.88 |
| gen1_elo | 34,551 | 44.0% | 24.2% | 12.85 | 35.7% | 15.5% | 10.68 |
| gen1_sr | 34,551 | 52.0% | 31.3% | 15.88 | 44.5% | 22.3% | 13.03 |
| gen2 | 34,551 | 51.2% | 31.7% | 15.5 | 44.6% | 23.9% | 13.05 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 17,268 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.3 | 10.72 | 35.3% | 15.2% |
| STALE | 17,283 | 10.3 | 6.9 | 15.8 | 13.8 | 19.3 | 17.9 | 15.9 | 16.38 | 53.1% | 33.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 18,749 | 16.3 | 11.1 | 22.5 | 15.4 | 17.7 | 12.2 | 4.8 | 10.02 | 34.7% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 59,832 | 18749 | 20740 | 20343 | 24.0 | 118.2 | 1400.4 |
| ge_15pp | 24,581 | 6511 | 7389 | 10681 | 26.1 | 418.1 | 1399.2 |
| ge_25pp | 13,120 | 3189 | 3217 | 6714 | 31.4 | 562.6 | 1380.4 |
| lt_10pp | 26,020 | 9358 | 9806 | 6856 | 22.4 | 47.3 | 1341.5 |

Current slate `SL-20261027T135349Z-23b187c8`: 755 priced rows, quote age at build {'median': 17.7, 'max': 17.8}, freshness {'AGING': 755}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 33 | 0.0 | 0.0 | 21.2 | 9.1 | 45.5 | 24.2 | 0.0 | 20.49 | 69.7% | 24.2% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,437 | 19.7 | 11.2 | 25.1 | 18.4 | 17.8 | 7.1 | 0.7 | 8.73 | 25.6% | 7.8% |
| KALSHI_LONE_OUTLIER | 22 | 4.5 | 4.5 | 77.3 | 4.5 | 4.5 | 4.5 | 0.0 | 6.16 | 9.1% | 4.5% |
| MARKETS_AGREE | 661 | 65.5 | 34.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,441 | 0.0 | 2.6 | 34.9 | 26.9 | 24.8 | 10.1 | 0.7 | 12.12 | 35.6% | 10.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 34,551 | 5612 (16.2%) | 25.7% | 1.0% | {"EXTERNAL_STALE": 3437, "AGREES_WITH_KALSHI": 1441, "ALL_AGREE": 661, "SUPPORTS_MODEL_DIRECTION": 32, "AGREES_WITH_MODEL": 22, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 15,271 | 1417 (9.3%) | 36.2% | 1.8% | {"EXTERNAL_STALE": 879, "AGREES_WITH_KALSHI": 513, "SUPPORTS_MODEL_DIRECTION": 23, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 8,469 | 432 (5.1%) | 36.1% | 2.1% | {"EXTERNAL_STALE": 267, "AGREES_WITH_KALSHI": 156, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,206 | 408 (9.7%) | 36.5% | 2.2% | {"EXTERNAL_STALE": 250, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 13,893 | 3169 (22.8%) | 17.0% | 0.8% | {"EXTERNAL_STALE": 1924, "ALL_AGREE": 661, "AGREES_WITH_KALSHI": 540, "AGREES_WITH_MODEL": 19, "EXTERNAL_OUTLIER": 18, "SUPPORTS_MODEL_DIRECTION": 6, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,643 | 10.4 | 7.5 | 19.3 | 14.8 | 22.2 | 16.1 | 9.7 | 14.03 | 47.9% | 25.7% |
| 4-10x | 4,504 | 11.0 | 8.5 | 18.7 | 15.2 | 22.2 | 14.8 | 9.7 | 13.84 | 46.6% | 24.5% |
| <2x | 17,673 | 15.1 | 10.1 | 19.3 | 16.4 | 17.4 | 13.0 | 8.7 | 11.59 | 39.0% | 21.7% |
| >=10x | 5,731 | 10.5 | 6.1 | 15.2 | 14.2 | 22.1 | 19.4 | 12.5 | 16.5 | 54.0% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,758 | 12.8 | 8.5 | 19.2 | 16.3 | 19.2 | 13.5 | 10.3 | 12.83 | 43.1% | 23.8% |
| 300-1000 | 7,210 | 11.9 | 8.8 | 17.4 | 15.3 | 20.6 | 16.4 | 9.6 | 13.78 | 46.6% | 26.0% |
| <300 | 11,267 | 8.3 | 5.7 | 15.4 | 14.8 | 23.3 | 20.1 | 12.4 | 17.02 | 55.8% | 32.5% |
| >=3000 | 7,316 | 21.2 | 13.6 | 23.8 | 16.2 | 13.7 | 7.0 | 4.5 | 7.67 | 25.2% | 11.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 963 | 0.5509 | 0.4126 | 0.5026 | +0.048 | -0.090 | -0.0035 ± 0.005 |
| ratio 4-10x | 654 | 0.5864 | 0.4387 | 0.5 | +0.086 | -0.061 | 0.0082 ± 0.0063 |
| ratio <2x | 2366 | 0.5387 | 0.4155 | 0.4476 | +0.091 | -0.032 | 0.0112 ± 0.003 |
| ratio >=10x | 868 | 0.5709 | 0.3944 | 0.4551 | +0.116 | -0.061 | 0.011 ± 0.0062 |
| thinner_sample 1000-3000 | 1307 | 0.5395 | 0.4128 | 0.4499 | +0.090 | -0.037 | 0.0089 ± 0.004 |
| thinner_sample 300-1000 | 1080 | 0.5689 | 0.4257 | 0.4926 | +0.076 | -0.067 | 0.0009 ± 0.0049 |
| thinner_sample <300 | 1647 | 0.5623 | 0.3943 | 0.4639 | +0.098 | -0.070 | 0.0095 ± 0.0044 |
| thinner_sample >=3000 | 817 | 0.5365 | 0.4418 | 0.4663 | +0.070 | -0.025 | 0.0119 ± 0.004 |
| data_status ADEQUATE | 1394 | 0.5371 | 0.433 | 0.4505 | +0.087 | -0.018 | 0.0119 ± 0.0033 |
| data_status LIMITED | 1114 | 0.5502 | 0.4167 | 0.4874 | +0.063 | -0.071 | 0.0023 ± 0.0045 |
| data_status POOR | 2343 | 0.5644 | 0.4019 | 0.4669 | +0.098 | -0.065 | 0.008 ± 0.0036 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 709 | 0.2018 | 0.2024 | -0.0006 ± 0.0006 | 0.5843 | 0.5856 | 0.5012 | 0.4862 | 0.512 | -0.084 ± 0.0179 | -0.01 (5) |
| 3-5 | 436 | 0.204 | 0.2036 | +0.0003 ± 0.0017 | 0.5909 | 0.5885 | 0.5046 | 0.4645 | 0.4794 | -0.103 ± 0.0222 | 0.02 (1) |
| 5-10 | 1003 | 0.203 | 0.2033 | -0.0004 ± 0.0021 | 0.5927 | 0.591 | 0.5149 | 0.441 | 0.4766 | -0.089 ± 0.0147 | -0.0167 (6) |
| 10-15 | 850 | 0.2204 | 0.2111 | +0.0093 ± 0.0039 | 0.6333 | 0.6053 | 0.5317 | 0.4078 | 0.4306 | -0.109 ± 0.0158 | -0.048 (5) |
| 15-25 | 1098 | 0.2253 | 0.2129 | +0.0124 ± 0.0054 | 0.6462 | 0.6097 | 0.5766 | 0.3808 | 0.4472 | -0.097 ± 0.014 | -0.0033 (9) |
| 25-40 | 626 | 0.2219 | 0.2098 | +0.0121 ± 0.0109 | 0.6331 | 0.6027 | 0.6553 | 0.3457 | 0.4792 | -0.071 ± 0.0167 | -0.01 (1) |
| 40+ | 129 | 0.2737 | 0.2 | +0.0737 ± 0.0341 | 0.7479 | 0.5853 | 0.7515 | 0.3013 | 0.4496 | -0.063 ± 0.0334 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3662 | 0.185 | 0.1858 | -0.0007 ± 0.0002 | 0.546 | 0.5466 | 0.4888 | 0.4736 | 0.5005 | -0.029 ± 0.0072 | -0.0129 (17) |
| 3-5 | 2451 | 0.1985 | 0.197 | +0.0016 ± 0.0007 | 0.5776 | 0.5713 | 0.4857 | 0.4458 | 0.4447 | -0.057 ± 0.0091 | 0.0 (2) |
| 5-10 | 5209 | 0.2009 | 0.1974 | +0.0035 ± 0.0009 | 0.5875 | 0.575 | 0.4855 | 0.4116 | 0.4241 | -0.050 ± 0.0062 | -0.0119 (21) |
| 10-15 | 4483 | 0.2005 | 0.183 | +0.0175 ± 0.0016 | 0.5874 | 0.5377 | 0.49 | 0.3657 | 0.3571 | -0.072 ± 0.0064 | -0.0281 (16) |
| 15-25 | 5636 | 0.2078 | 0.1691 | +0.0387 ± 0.0022 | 0.6089 | 0.5001 | 0.5022 | 0.3059 | 0.3064 | -0.072 ± 0.0055 | -0.0025 (44) |
| 25-40 | 4393 | 0.222 | 0.1275 | +0.0945 ± 0.0034 | 0.638 | 0.3906 | 0.5288 | 0.2155 | 0.2254 | -0.060 ± 0.0052 | -0.01 (1) |
| 40+ | 2848 | 0.3784 | 0.0478 | +0.3306 ± 0.0046 | 0.985 | 0.1817 | 0.6312 | 0.1061 | 0.0667 | -0.075 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 554 | 0.2061 | 0.2068 | -0.0007 ± 0.0007 | 0.5938 | 0.5955 | 0.5082 | 0.493 | 0.5162 | -0.107 ± 0.0209 | -0.01 (3) |
| 3-5 | 396 | 0.2272 | 0.2242 | +0.0030 ± 0.0019 | 0.641 | 0.635 | 0.5096 | 0.4698 | 0.447 | -0.137 ± 0.0254 | 0.02 (1) |
| 5-10 | 873 | 0.2078 | 0.2073 | +0.0006 ± 0.0023 | 0.6021 | 0.6003 | 0.5482 | 0.4732 | 0.5109 | -0.086 ± 0.0159 | -0.01 (4) |
| 10-15 | 797 | 0.2189 | 0.2121 | +0.0068 ± 0.0041 | 0.6292 | 0.6104 | 0.5677 | 0.4433 | 0.4806 | -0.106 ± 0.017 | -0.04 (5) |
| 15-25 | 1136 | 0.2316 | 0.214 | +0.0176 ± 0.0054 | 0.6574 | 0.6116 | 0.5871 | 0.3919 | 0.4481 | -0.101 ± 0.014 | -0.0133 (9) |
| 25-40 | 796 | 0.2646 | 0.1988 | +0.0657 ± 0.0099 | 0.7398 | 0.5789 | 0.6526 | 0.3382 | 0.3932 | -0.119 ± 0.0157 | -0.0075 (4) |
| 40+ | 299 | 0.3591 | 0.1704 | +0.1886 ± 0.0237 | 0.9849 | 0.5103 | 0.736 | 0.2506 | 0.3144 | -0.075 ± 0.023 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3103 | 0.1931 | 0.1934 | -0.0002 ± 0.0003 | 0.5631 | 0.5633 | 0.5101 | 0.4951 | 0.5066 | -0.047 ± 0.0082 | -0.0133 (15) |
| 3-5 | 2086 | 0.2011 | 0.1997 | +0.0013 ± 0.0008 | 0.5809 | 0.5771 | 0.5114 | 0.4716 | 0.4741 | -0.052 ± 0.01 | 0.02 (1) |
| 5-10 | 4658 | 0.1984 | 0.1958 | +0.0027 ± 0.001 | 0.583 | 0.5714 | 0.5136 | 0.4396 | 0.4618 | -0.039 ± 0.0066 | -0.0117 (6) |
| 10-15 | 4031 | 0.2039 | 0.1915 | +0.0124 ± 0.0017 | 0.597 | 0.5569 | 0.5169 | 0.393 | 0.4056 | -0.056 ± 0.007 | -0.0189 (18) |
| 15-25 | 5596 | 0.2166 | 0.1797 | +0.0369 ± 0.0022 | 0.6293 | 0.5271 | 0.5254 | 0.33 | 0.3374 | -0.066 ± 0.0057 | -0.0086 (42) |
| 25-40 | 5125 | 0.2501 | 0.1372 | +0.1129 ± 0.0033 | 0.7046 | 0.4207 | 0.5562 | 0.2396 | 0.222 | -0.084 ± 0.0052 | -0.0044 (18) |
| 40+ | 4083 | 0.395 | 0.0611 | +0.3339 ± 0.0044 | 1.0387 | 0.2184 | 0.652 | 0.1196 | 0.0857 | -0.072 ± 0.0038 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 682 | 0.1988 | 0.2009 | -0.0021 ± 0.0006 | 0.5778 | 0.5828 | 0.5002 | 0.4849 | 0.5469 | -0.035 ± 0.0179 | -0.0137 (8) |
| 3-5 | 478 | 0.2036 | 0.2024 | +0.0012 ± 0.0017 | 0.5906 | 0.586 | 0.5053 | 0.4656 | 0.4728 | -0.114 ± 0.0214 | 0.0067 (3) |
| 5-10 | 1027 | 0.2041 | 0.2017 | +0.0024 ± 0.0021 | 0.5948 | 0.5861 | 0.5133 | 0.4392 | 0.4596 | -0.099 ± 0.0144 | -0.0071 (7) |
| 10-15 | 841 | 0.2104 | 0.2055 | +0.0049 ± 0.0039 | 0.6108 | 0.5935 | 0.5408 | 0.4173 | 0.4602 | -0.096 ± 0.0156 | -0.0317 (6) |
| 15-25 | 1040 | 0.2325 | 0.2159 | +0.0166 ± 0.0056 | 0.6636 | 0.6164 | 0.5876 | 0.393 | 0.4471 | -0.108 ± 0.0144 | -0.03 (1) |
| 25-40 | 644 | 0.214 | 0.2169 | -0.0029 ± 0.0107 | 0.6173 | 0.619 | 0.6656 | 0.3551 | 0.5124 | -0.056 ± 0.0165 | 0.015 (2) |
| 40+ | 139 | 0.2866 | 0.208 | +0.0785 ± 0.0337 | 0.7882 | 0.6019 | 0.7575 | 0.3062 | 0.4532 | -0.062 ± 0.0353 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3588 | 0.1859 | 0.1866 | -0.0007 ± 0.0003 | 0.547 | 0.548 | 0.487 | 0.4718 | 0.4925 | -0.032 ± 0.0073 | -0.0163 (35) |
| 3-5 | 2429 | 0.1988 | 0.1969 | +0.0020 ± 0.0007 | 0.581 | 0.5743 | 0.4859 | 0.4463 | 0.4422 | -0.064 ± 0.0092 | -0.0094 (18) |
| 5-10 | 5360 | 0.1964 | 0.1916 | +0.0047 ± 0.0009 | 0.5768 | 0.5601 | 0.4876 | 0.4135 | 0.419 | -0.054 ± 0.006 | -0.01 (31) |
| 10-15 | 4346 | 0.1928 | 0.1772 | +0.0156 ± 0.0016 | 0.5699 | 0.5233 | 0.4995 | 0.376 | 0.3739 | -0.067 ± 0.0064 | -0.015 (12) |
| 15-25 | 5773 | 0.2112 | 0.1723 | +0.0389 ± 0.0021 | 0.6165 | 0.5079 | 0.5129 | 0.3179 | 0.3165 | -0.073 ± 0.0055 | -0.03 (2) |
| 25-40 | 4383 | 0.2192 | 0.1311 | +0.0881 ± 0.0034 | 0.6325 | 0.3984 | 0.5336 | 0.2178 | 0.238 | -0.052 ± 0.0053 | 0.01 (3) |
| 40+ | 2803 | 0.3911 | 0.0525 | +0.3386 ± 0.0049 | 1.0215 | 0.1941 | 0.6425 | 0.1128 | 0.0721 | -0.077 ± 0.0041 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1071 | 0.1967 | 0.1968 | -0.0001 ± 0.0005 | 0.5728 | 0.5726 | 0.502 | 0.487 | 0.4902 | -0.067 ± 0.0138 | -0.0224 (49) |
| 3-5 | 743 | 0.1933 | 0.1926 | +0.0007 ± 0.0013 | 0.5639 | 0.5614 | 0.4934 | 0.4537 | 0.463 | -0.062 ± 0.0165 | -0.0194 (34) |
| 5-10 | 1553 | 0.2028 | 0.197 | +0.0058 ± 0.0017 | 0.5958 | 0.5766 | 0.4973 | 0.4238 | 0.4224 | -0.077 ± 0.0115 | -0.005 (78) |
| 10-15 | 1049 | 0.2118 | 0.2004 | +0.0114 ± 0.0034 | 0.6149 | 0.5835 | 0.5279 | 0.405 | 0.4185 | -0.073 ± 0.0141 | 0.0014 (64) |
| 15-25 | 1388 | 0.2322 | 0.2112 | +0.0210 ± 0.0048 | 0.6619 | 0.6072 | 0.5796 | 0.3848 | 0.4301 | -0.078 ± 0.0124 | -0.0214 (59) |
| 25-40 | 852 | 0.2433 | 0.2101 | +0.0332 ± 0.0096 | 0.695 | 0.6023 | 0.6783 | 0.3663 | 0.4683 | -0.085 ± 0.0146 | -0.0219 (26) |
| 40+ | 282 | 0.3442 | 0.1986 | +0.1457 ± 0.026 | 0.9942 | 0.5821 | 0.8067 | 0.3263 | 0.4326 | -0.096 ± 0.024 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3610 | 0.1824 | 0.1825 | -0.0001 ± 0.0002 | 0.5371 | 0.5365 | 0.5034 | 0.4881 | 0.4953 | -0.043 ± 0.0072 | -0.0157 (88) |
| 3-5 | 2526 | 0.1962 | 0.1942 | +0.0020 ± 0.0007 | 0.5703 | 0.566 | 0.5038 | 0.464 | 0.4584 | -0.057 ± 0.0089 | -0.0209 (69) |
| 5-10 | 5042 | 0.1983 | 0.1903 | +0.0080 ± 0.0009 | 0.5841 | 0.559 | 0.4926 | 0.419 | 0.4038 | -0.072 ± 0.0062 | -0.0082 (132) |
| 10-15 | 3548 | 0.2087 | 0.1933 | +0.0154 ± 0.0018 | 0.6081 | 0.5661 | 0.5295 | 0.4067 | 0.4047 | -0.065 ± 0.0074 | -0.0053 (105) |
| 15-25 | 4352 | 0.2306 | 0.2003 | +0.0303 ± 0.0027 | 0.6642 | 0.5797 | 0.5681 | 0.3724 | 0.3941 | -0.067 ± 0.0068 | -0.0253 (107) |
| 25-40 | 2969 | 0.2587 | 0.1862 | +0.0724 ± 0.005 | 0.7337 | 0.543 | 0.6337 | 0.3205 | 0.3638 | -0.077 ± 0.0077 | -0.0229 (51) |
| 40+ | 1300 | 0.3746 | 0.1472 | +0.2275 ± 0.0111 | 1.0612 | 0.4436 | 0.7291 | 0.2272 | 0.2646 | -0.071 ± 0.01 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4851 | 1.027 ± 0.04 | 1.093 | 0.1676 | 0.1635 | 0.2153 | 0.2075 |
| gen2 | 4851 | 0.814 ± 0.037 | 1.055 | 0.1686 | 0.1641 | 0.2352 | 0.2073 |
| gen1_elo | 4851 | 1.001 ± 0.039 | 1.093 | 0.1741 | 0.1637 | 0.2142 | 0.2076 |
| gen1_sr | 4851 | 0.995 ± 0.048 | 1.116 | 0.1293 | 0.1659 | 0.2312 | 0.2069 |
| gen1_ledger | 6938 | 0.857 ± 0.029 | 1.059 | 0.1839 | 0.1765 | 0.2188 | 0.2015 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 24,581)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,392 | 21.9% |
| STALE_QUOTE | market_freshness | 5,378 | 21.9% |
| BOOK_QUALITY | execution | 4,766 | 19.4% |
| POOR_DATA | data | 2,850 | 11.6% |
| LIMITED_DATA | data | 1,546 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,312 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,169 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,037 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 699 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 431 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 21.9%, market_freshness 21.9%, execution 19.4%, data 17.9%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.0%, LOW_DATA_QUALITY 71.1%, THIN_PLAYER_HISTORY 60.2%, STALE_PLAYER_DATA 51.4%, STALE_KALSHI_QUOTE 43.5%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 25.5%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 16.2%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.4%, POST_SETTLEMENT_OBSERVATION 21.9%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 13,120)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,342 | 33.1% |
| BOOK_QUALITY | execution | 2,502 | 19.1% |
| STALE_QUOTE | market_freshness | 2,482 | 18.9% |
| POOR_DATA | data | 1,207 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 705 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 568 | 4.3% |
| LIMITED_DATA | data | 457 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 447 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 303 | 2.3% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 106 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.1%, execution 19.1%, market_freshness 18.9%, data 12.7%, market_freshness/coverage 8.8%, mapping 4.3%, model_calibration_or_unknown 2.3%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.7%, LOW_DATA_QUALITY 74.6%, THIN_PLAYER_HISTORY 62.5%, STALE_KALSHI_QUOTE 51.2%, STALE_PLAYER_DATA 46.0%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.8%, WIDE_SPREAD 25.1%, PLAYER_IDENTITY_RISK 19.4%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 9.4%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.1%, POST_SETTLEMENT_OBSERVATION 33.1%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 10261, "IDENTITY_AMBIGUOUS": 2859}; ticker orientation: {"VERIFIED": 13120}.

Checks: discipline:AMBIGUOUS 872, discipline:PASS 12248, identity_confidence:AMBIGUOUS 2551, identity_confidence:PASS 10569, level_mapping:NA 884, level_mapping:PASS 12236, market_pair:AMBIGUOUS 466, market_pair:NA 313, market_pair:PASS 12341, model_complement:NA 278, model_complement:PASS 12842, namesake:AMBIGUOUS 6, namesake:PASS 13114, physical_match_id:NA 4651, physical_match_id:PASS 8469, player_ids:PASS 13120, same_pair_other_event:PASS 13120, ticker_orientation:PASS 13120

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,046 | 4.5% | 4.0% | 1.7% | {"market_freshness": 56, "model_calibration_or_unknown": 55, "data": 36, "model_calibration": 26, "execution": 24, "market_freshness/coverage": 15, "coverage": 13} | 5.85 | 0.2217 / 0.2194 (561) | 20.6% | 3.1% | 3.3% | 2.6% |
| CHALLENGER | 9,242 | 16.6% | 6.6% | 11.7% | {"coverage": 871, "market_freshness/coverage": 185, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 78, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.47 | 0.219 / 0.2095 (2129) | 34.4% | 16.5% | 4.1% | 21.9% |
| DOUBLES | 1,845 | 47.3% | 47.0% | 6.7% | {"execution": 486, "mapping": 218, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.84 | 0.3112 / 0.2362 (445) | 12.7% | 0.0% | 100.0% | 6.5% |
| ITF_MEN | 16,154 | 25.7% | 18.3% | 31.7% | {"coverage": 1464, "execution": 803, "market_freshness": 738, "data": 599, "market_freshness/coverage": 363, "mapping": 181, "model_calibration": 4, "model_calibration_or_unknown": 2} | 12.09 | 0.2166 / 0.1983 (3449) | 36.8% | 70.4% | 18.8% | 21.4% |
| ITF_WOMEN | 21,869 | 27.0% | 20.0% | 44.9% | {"coverage": 1959, "market_freshness": 1289, "execution": 1100, "data": 832, "market_freshness/coverage": 481, "mapping": 146, "model_calibration_or_unknown": 74, "model_calibration": 12} | 12.85 | 0.2051 / 0.1978 (4044) | 38.9% | 58.0% | 10.3% | 20.9% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,600 | 5.7% | 5.1% | 1.6% | {"market_freshness": 72, "model_calibration_or_unknown": 43, "execution": 27, "data": 19, "model_calibration": 16, "coverage": 15, "market_freshness/coverage": 11, "mapping": 1} | 7.67 | 0.2327 / 0.2271 (573) | 25.2% | 1.2% | 1.5% | 3.3% |
| WTA125 | 1,921 | 11.9% | 9.8% | 1.7% | {"market_freshness": 54, "model_calibration_or_unknown": 49, "market_freshness/coverage": 41, "data": 34, "execution": 21, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.4 | 0.2155 / 0.2015 (546) | 24.8% | 11.7% | 5.6% | 7.5% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 37 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 38 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 42 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 43 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 44 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 45 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 47 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 48 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 49 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 50 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9674, "by_level_share_of_ge_25pp": {"ATP": 0.0171, "CHALLENGER": 0.1168, "DOUBLES": 0.0665, "ITF_MEN": 0.3166, "ITF_WOMEN": 0.4492, "OTHER": 0.0009, "WTA": 0.0155, "WTA125": 0.0174}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5117, "share_primary_cause_market_settled_or_in_play": 0.4187, "share_primary_cause_stale_quote_only": 0.1892}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 13120, "identity_ambiguous_share": 0.2179, "ticker_orientation": {"VERIFIED": 13120}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 8469, "with_external": 432, "coverage": 0.051, "external_status": {"EXTERNAL_STALE": 267, "AGREES_WITH_KALSHI": 156, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 267, "MODEL_LONE_OUTLIER": 156, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3611, "share_external_supports_model": 0.0208}, "pregame_clean_ge_25pp": {"n": 4206, "with_external": 408, "coverage": 0.097, "external_status": {"EXTERNAL_STALE": 250, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 250, "MODEL_LONE_OUTLIER": 149, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3652, "share_external_supports_model": 0.0221}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 459.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 238.0, "share_severe_asymmetry": 0.2153, "data_status": {"POOR": 7423, "LIMITED": 3337, "ADEQUATE": 2360}, "comparison_lt_10pp": {"median_thinner_serve_points": 1763.0, "median_sample_ratio": 1.67, "median_min_matches": 96.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 963, "model_minus_observed": 0.0483, "kalshi_minus_observed": -0.09, "brier_diff_model_minus_kalshi": -0.0035}, "4-10x": {"n": 654, "model_minus_observed": 0.0864, "kalshi_minus_observed": -0.0613, "brier_diff_model_minus_kalshi": 0.0082}, "<2x": {"n": 2366, "model_minus_observed": 0.0911, "kalshi_minus_observed": -0.0321, "brier_diff_model_minus_kalshi": 0.0112}, ">=10x": {"n": 868, "model_minus_observed": 0.1158, "kalshi_minus_observed": -0.0607, "brier_diff_model_minus_kalshi": 0.011}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4851, "model": {"intercept": -0.534, "slope": 0.814, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.194, "slope": 1.055, "slope_se": 0.041}, "mean_extremity_model": 0.1686, "mean_extremity_kalshi": 0.1641, "model_brier": 0.2352, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.0279, "brier_diff_se": 0.0027, "model_logloss": 0.6679, "kalshi_logloss": 0.5978}, "fair_v1": {"n": 4851, "model": {"intercept": -0.417, "slope": 1.027, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.279, "slope": 1.093, "slope_se": 0.041}, "mean_extremity_model": 0.1676, "mean_extremity_kalshi": 0.1635, "model_brier": 0.2153, "kalshi_brier": 0.2075, "brier_diff_model_minus_kalshi": 0.0078, "brier_diff_se": 0.0022, "model_logloss": 0.6199, "kalshi_logloss": 0.5981}, "gen1_elo": {"n": 4851, "model": {"intercept": -0.389, "slope": 1.001, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.304, "slope": 1.093, "slope_se": 0.041}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1637, "model_brier": 0.2142, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": 0.0066, "brier_diff_se": 0.0023, "model_logloss": 0.618, "kalshi_logloss": 0.5983}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2451, "share_ge_15": 0.442, "median_abs_gap": 13.04, "n": 34551}, "gen1_elo": {"share_ge_25": 0.2422, "share_ge_15": 0.4401, "median_abs_gap": 12.85, "n": 34551}, "gen1_sr": {"share_ge_25": 0.3133, "share_ge_15": 0.5205, "median_abs_gap": 15.88, "n": 34551}, "gen2": {"share_ge_25": 0.3173, "share_ge_15": 0.512, "median_abs_gap": 15.5, "n": 34551}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1551, "share_ge_15": 0.3598, "median_abs_gap": 10.88, "n": 27109}, "gen1_elo": {"share_ge_25": 0.155, "share_ge_15": 0.3567, "median_abs_gap": 10.68, "n": 27106}, "gen1_sr": {"share_ge_25": 0.2229, "share_ge_15": 0.4448, "median_abs_gap": 13.03, "n": 27110}, "gen2": {"share_ge_25": 0.2392, "share_ge_15": 0.4456, "median_abs_gap": 13.05, "n": 27111}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.85, "share_ge_25_all": 0.0446, "share_ge_25_pregame_clean": 0.0401}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.0567, "share_ge_25_pregame_clean": 0.0511}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2356, "share_within_10pp_all": 0.4349, "share_within_10pp_pregame_clean": 0.4853, "corr_model_vs_mid_pregame_clean": 0.8447}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 709, "model_brier": 0.2018, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": -0.0006}, "10-15": {"n_settled": 850, "model_brier": 0.2204, "kalshi_brier": 0.2111, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 1098, "model_brier": 0.2253, "kalshi_brier": 0.2129, "brier_diff_model_minus_kalshi": 0.0124}, "25-40": {"n_settled": 626, "model_brier": 0.2219, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.0121}, "3-5": {"n_settled": 436, "model_brier": 0.204, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0003}, "40+": {"n_settled": 129, "model_brier": 0.2737, "kalshi_brier": 0.2, "brier_diff_model_minus_kalshi": 0.0737}, "5-10": {"n_settled": 1003, "model_brier": 0.203, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": -0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.534, "slope": 0.814, "slope_se": 0.037}, "kalshi_slope": {"intercept": 0.194, "slope": 1.055, "slope_se": 0.041}, "n": 4851}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.495, "slope": 0.857, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.158, "slope": 1.059, "slope_se": 0.033}, "n": 6938}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 445, "model_brier": 0.3112, "kalshi_brier": 0.2362, "brier_diff_model_minus_kalshi": 0.0749, "brier_diff_se": 0.0143, "corr_model_outcome": 0.0359, "corr_kalshi_outcome": 0.2487}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
