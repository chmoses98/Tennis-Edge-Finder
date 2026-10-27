# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-27T00:09Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 56,917): 0-3 14.0%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 19.2%, 25-40 13.9%, 40+ 8.1%; median gap 11.97 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.2%, Challenger 11.8%, doubles 6.9%). Main tour: ATP 4.4% and WTA 5.5% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 12,518): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.7%, STALE_QUOTE 19.1%, BOOK_QUALITY 18.9%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.7%, market_freshness 19.1%, execution 18.9%, data 12.0%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 12,518 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.2% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 473.0 points vs 1787.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.033, Gen-2 0.825, Gen-1 ledger 0.864 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 607 model 0.2212 vs Kalshi 0.2095; n 120 model 0.2698 vs Kalshi 0.2022.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 250,916 model-market comparisons (405,098 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 84,092 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-26T23:55:07.472707+00:00'], shadow board 65,552 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-26T23:55:12.776454+00:00'], Model 4 32,664 rows, 21,188 settled tickers, 7,505 tickers with an external scan.
* By model: {"gen1_ledger": 57600, "gen1_elo": 32964, "fair_v1": 32964, "gen2": 32964, "gen1_sr": 32964, "model4_fundamental": 30752, "model4_conditioned": 30708}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 56,917 | 14.0 | 9.6 | 19.9 | 15.4 | 19.2 | 13.9 | 8.1 | 11.97 | 41.2% | 22.0% |
| MW fair_v1 | 32,964 | 12.9 | 8.7 | 18.6 | 15.5 | 19.7 | 14.8 | 9.7 | 13.05 | 44.3% | 24.6% |
| MW gen1_elo | 32,964 | 12.8 | 8.5 | 19.2 | 15.3 | 19.9 | 14.8 | 9.5 | 12.95 | 44.2% | 24.3% |
| MW gen1_ledger | 23,953 | 15.5 | 10.8 | 21.6 | 15.1 | 18.5 | 12.6 | 5.8 | 10.5 | 36.9% | 18.4% |
| MW gen1_sr | 32,964 | 10.2 | 7.1 | 17.0 | 13.6 | 20.7 | 18.6 | 12.7 | 15.89 | 52.0% | 31.3% |
| MW gen2 | 32,964 | 11.1 | 7.4 | 16.4 | 13.9 | 19.4 | 17.9 | 13.9 | 15.51 | 51.2% | 31.7% |
| all families model4_conditioned | 30,708 | 21.9 | 18.3 | 34.5 | 17.6 | 4.8 | 1.8 | 1.1 | 6.06 | 7.7% | 2.9% |
| all families model4_fundamental | 30,752 | 16.7 | 13.1 | 34.1 | 20.7 | 10.4 | 3.7 | 1.4 | 7.83 | 15.4% | 5.0% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.5%, >=15pp 41.2%, >=20pp 30.6%, >=25pp 22.0%, >=30pp 15.8%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.33pp; >=10pp 44.9%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,076 | 27.1 | 15.1 | 26.7 | 14.6 | 11.7 | 4.3 | 0.7 | 6.04 | 16.6% | 4.9% |
| CHALLENGER | 5,235 | 15.9 | 10.0 | 20.2 | 15.6 | 15.6 | 12.2 | 10.5 | 11.06 | 38.3% | 22.6% |
| ITF_MEN | 8,771 | 10.0 | 7.2 | 16.6 | 14.6 | 21.6 | 17.6 | 12.4 | 15.53 | 51.6% | 30.0% |
| ITF_WOMEN | 12,848 | 9.5 | 7.0 | 15.9 | 15.2 | 22.4 | 18.2 | 11.8 | 15.77 | 52.5% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,190 | 16.9 | 13.9 | 25.2 | 20.6 | 16.8 | 6.1 | 0.6 | 8.39 | 23.5% | 6.7% |
| WTA125 | 838 | 14.3 | 7.5 | 22.2 | 21.6 | 19.8 | 12.5 | 2.0 | 11.13 | 34.4% | 14.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,076 | 24.6 | 15.2 | 25.6 | 17.4 | 12.1 | 4.3 | 0.8 | 6.49 | 17.2% | 5.1% |
| CHALLENGER | 5,235 | 15.0 | 8.8 | 18.1 | 14.6 | 18.2 | 14.0 | 11.3 | 12.69 | 43.5% | 25.3% |
| ITF_MEN | 8,771 | 8.0 | 5.8 | 14.3 | 12.9 | 19.7 | 21.3 | 18.0 | 18.86 | 58.9% | 39.3% |
| ITF_WOMEN | 12,848 | 8.1 | 5.6 | 13.8 | 12.9 | 20.8 | 21.2 | 17.7 | 19.3 | 59.7% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,190 | 14.3 | 10.6 | 22.6 | 16.0 | 22.5 | 13.0 | 1.1 | 10.74 | 36.6% | 14.1% |
| WTA125 | 838 | 7.8 | 6.4 | 16.1 | 18.6 | 24.2 | 17.8 | 9.1 | 15.44 | 51.1% | 26.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,076 | 22.9 | 12.3 | 24.6 | 16.2 | 16.1 | 6.5 | 1.3 | 7.58 | 23.9% | 7.8% |
| CHALLENGER | 5,235 | 14.3 | 9.2 | 21.2 | 15.8 | 16.2 | 12.6 | 10.7 | 11.41 | 39.5% | 23.3% |
| ITF_MEN | 8,771 | 9.6 | 7.2 | 16.7 | 13.8 | 22.1 | 17.9 | 12.6 | 16.01 | 52.6% | 30.5% |
| ITF_WOMEN | 12,848 | 9.3 | 6.6 | 16.3 | 15.9 | 22.7 | 18.2 | 11.0 | 15.57 | 51.8% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,190 | 23.9 | 16.7 | 31.1 | 15.2 | 9.5 | 2.6 | 1.0 | 6.05 | 13.1% | 3.6% |
| WTA125 | 838 | 22.8 | 11.8 | 26.0 | 16.6 | 16.5 | 6.0 | 0.4 | 8.01 | 22.8% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,829 | 24.8 | 19.4 | 30.1 | 12.9 | 9.3 | 3.2 | 0.3 | 5.67 | 12.8% | 3.5% |
| CHALLENGER | 3,638 | 21.5 | 14.2 | 26.8 | 14.9 | 14.6 | 6.4 | 1.6 | 7.37 | 22.6% | 8.1% |
| DOUBLES | 1,822 | 5.2 | 4.5 | 12.2 | 10.2 | 20.4 | 25.6 | 21.9 | 23.93 | 67.9% | 47.5% |
| ITF_MEN | 6,512 | 13.4 | 9.2 | 19.9 | 16.1 | 21.4 | 13.5 | 6.6 | 12.23 | 41.5% | 20.0% |
| ITF_WOMEN | 7,849 | 12.7 | 9.0 | 19.3 | 15.3 | 21.6 | 16.2 | 6.0 | 12.78 | 43.7% | 22.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,289 | 23.2 | 15.7 | 30.3 | 17.9 | 9.5 | 3.1 | 0.3 | 6.8 | 13.0% | 3.4% |
| WTA125 | 865 | 21.4 | 13.4 | 21.7 | 18.5 | 14.4 | 8.6 | 2.0 | 8.37 | 25.0% | 10.5% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,996 | 27.4 | 15.3 | 27.1 | 14.4 | 11.5 | 3.9 | 0.4 | 5.93 | 15.8% | 4.3% |
| CHALLENGER | 3,713 | 20.6 | 12.4 | 24.9 | 18.1 | 15.7 | 6.7 | 1.7 | 8.36 | 24.0% | 8.3% |
| ITF_MEN | 6,415 | 12.1 | 8.7 | 20.0 | 16.6 | 22.8 | 14.4 | 5.5 | 12.76 | 42.7% | 19.9% |
| ITF_WOMEN | 9,640 | 11.3 | 8.3 | 18.1 | 17.2 | 24.3 | 15.5 | 5.4 | 13.54 | 45.2% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,129 | 17.1 | 13.8 | 25.2 | 20.8 | 16.7 | 5.8 | 0.6 | 8.34 | 23.2% | 6.4% |
| WTA125 | 809 | 14.6 | 7.4 | 21.8 | 21.9 | 20.4 | 12.2 | 1.7 | 11.13 | 34.4% | 14.0% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,996 | 24.8 | 15.5 | 25.9 | 17.3 | 12.1 | 4.0 | 0.5 | 6.36 | 16.5% | 4.5% |
| CHALLENGER | 3,713 | 19.1 | 11.1 | 22.3 | 17.3 | 18.5 | 9.7 | 1.9 | 9.36 | 30.1% | 11.6% |
| ITF_MEN | 6,416 | 9.5 | 7.0 | 16.7 | 14.9 | 21.6 | 19.4 | 10.9 | 15.59 | 51.8% | 30.3% |
| ITF_WOMEN | 9,641 | 9.1 | 6.4 | 15.3 | 14.3 | 22.7 | 20.8 | 11.3 | 16.9 | 54.9% | 32.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,129 | 14.3 | 10.6 | 22.6 | 16.0 | 22.5 | 12.8 | 1.2 | 10.77 | 36.4% | 14.0% |
| WTA125 | 809 | 7.7 | 6.4 | 16.2 | 19.0 | 24.1 | 18.2 | 8.4 | 15.19 | 50.7% | 26.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,776 | 24.9 | 19.6 | 30.1 | 13.1 | 8.9 | 3.0 | 0.2 | 5.64 | 12.2% | 3.3% |
| CHALLENGER | 3,201 | 22.8 | 15.2 | 28.1 | 15.0 | 14.0 | 4.5 | 0.5 | 6.86 | 18.9% | 4.9% |
| DOUBLES | 1,702 | 5.2 | 4.6 | 12.5 | 10.3 | 20.2 | 25.6 | 21.7 | 23.86 | 67.5% | 47.2% |
| ITF_MEN | 5,476 | 14.4 | 9.8 | 21.6 | 16.9 | 21.4 | 11.8 | 4.2 | 11.32 | 37.3% | 16.0% |
| ITF_WOMEN | 6,566 | 13.5 | 9.5 | 20.6 | 16.1 | 21.8 | 15.0 | 3.5 | 11.81 | 40.3% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,236 | 23.6 | 16.1 | 30.3 | 18.0 | 9.6 | 2.4 | 0.1 | 6.68 | 12.1% | 2.5% |
| WTA125 | 751 | 23.0 | 14.7 | 23.0 | 19.7 | 13.1 | 6.0 | 0.5 | 7.74 | 19.6% | 6.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,822 | 5.2 | 4.5 | 12.2 | 10.2 | 20.4 | 25.6 | 21.9 | 23.93 | 67.9% | 47.5% |
| singles | 22,131 | 16.3 | 11.3 | 22.4 | 15.6 | 18.3 | 11.6 | 4.5 | 9.97 | 34.4% | 16.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,180 | 12.7 | 9.2 | 19.7 | 15.9 | 18.9 | 14.1 | 9.5 | 12.6 | 42.5% | 23.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 20,815 | 13.4 | 8.8 | 18.5 | 15.2 | 19.7 | 14.8 | 9.5 | 12.99 | 44.0% | 24.3% |
| UNKNOWN | 4,720 | 10.9 | 7.4 | 17.0 | 16.7 | 20.5 | 16.2 | 11.3 | 14.12 | 48.0% | 27.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,560 | 19.6 | 12.3 | 22.0 | 16.4 | 14.6 | 9.1 | 6.0 | 8.82 | 29.7% | 15.0% |
| B | 4,060 | 12.4 | 8.7 | 19.5 | 16.3 | 19.7 | 12.8 | 10.7 | 12.64 | 43.1% | 23.4% |
| C | 4,552 | 11.8 | 9.1 | 19.4 | 15.7 | 19.3 | 14.5 | 10.3 | 13.01 | 44.1% | 24.7% |
| D | 5,009 | 12.1 | 7.8 | 17.5 | 15.3 | 21.8 | 15.7 | 9.9 | 13.98 | 47.3% | 25.5% |
| F | 9,783 | 7.5 | 5.5 | 14.9 | 14.5 | 23.7 | 21.1 | 12.7 | 17.79 | 57.5% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,853 | 23.5 | 16.1 | 28.9 | 15.1 | 11.2 | 4.0 | 1.3 | 6.56 | 16.5% | 5.3% |
| B | 3,226 | 16.2 | 10.3 | 23.2 | 16.4 | 19.8 | 10.4 | 3.6 | 10.04 | 33.8% | 14.0% |
| C | 4,675 | 10.9 | 7.3 | 18.7 | 14.5 | 21.1 | 16.5 | 11.0 | 14.28 | 48.6% | 27.5% |
| D | 3,275 | 14.2 | 9.8 | 20.2 | 15.2 | 20.9 | 13.9 | 5.8 | 11.85 | 40.6% | 19.7% |
| F | 5,924 | 10.1 | 8.3 | 15.6 | 15.1 | 22.8 | 20.1 | 8.1 | 15.47 | 50.9% | 28.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,865 | 17.9 | 11.1 | 21.2 | 16.1 | 15.3 | 9.9 | 8.5 | 9.96 | 33.7% | 18.4% |
| LIMITED | 6,963 | 13.5 | 10.1 | 20.1 | 16.2 | 19.4 | 13.2 | 7.4 | 11.8 | 40.0% | 20.6% |
| POOR | 15,136 | 9.1 | 6.4 | 15.9 | 14.8 | 23.0 | 19.1 | 11.7 | 16.26 | 53.8% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,914 | 24.7 | 18.6 | 33.2 | 14.5 | 6.2 | 2.5 | 0.3 | 5.71 | 9.0% | 2.8% |
| GAME_SPREAD | 5,460 | 22.4 | 15.4 | 33.3 | 16.7 | 9.1 | 2.7 | 0.4 | 6.7 | 12.2% | 3.1% |
| MATCH_WINNER | 23,953 | 15.5 | 10.8 | 21.6 | 15.1 | 18.5 | 12.6 | 5.8 | 10.5 | 36.9% | 18.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,393 | 28.0 | 16.4 | 30.9 | 12.6 | 9.4 | 2.3 | 0.3 | 5.66 | 12.1% | 2.7% |
| TOTAL_GAMES | 8,856 | 9.0 | 10.2 | 36.4 | 27.2 | 10.5 | 3.9 | 2.7 | 9.32 | 17.2% | 6.7% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,969 | 24.5 | 31.0 | 32.7 | 6.8 | 3.9 | 0.8 | 0.2 | 4.66 | 5.0% | 1.0% |
| GAME_SPREAD | 7,195 | 46.4 | 16.5 | 26.0 | 7.7 | 1.9 | 1.1 | 0.5 | 3.37 | 3.5% | 1.6% |
| TOTAL_GAMES | 12,544 | 5.5 | 8.3 | 40.9 | 32.7 | 7.3 | 3.1 | 2.2 | 9.49 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,980 | 23.6 | 16.8 | 35.1 | 14.3 | 7.2 | 2.6 | 0.4 | 6.05 | 10.2% | 2.9% |
| GAME_SPREAD | 7,198 | 19.5 | 13.2 | 28.3 | 21.1 | 12.6 | 4.3 | 1.0 | 7.92 | 17.9% | 5.3% |
| TOTAL_GAMES | 12,574 | 9.1 | 9.8 | 36.5 | 26.1 | 11.8 | 4.3 | 2.4 | 9.36 | 18.5% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 32,964 | 44.3% | 24.6% | 13.05 | 35.9% | 15.5% | 10.85 |
| gen1_elo | 32,964 | 44.2% | 24.3% | 12.95 | 35.7% | 15.5% | 10.69 |
| gen1_sr | 32,964 | 52.0% | 31.3% | 15.89 | 44.3% | 22.1% | 13.01 |
| gen2 | 32,964 | 51.2% | 31.7% | 15.51 | 44.4% | 23.8% | 13.03 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 16,374 | 15.6 | 10.6 | 21.4 | 17.3 | 20.1 | 11.8 | 3.3 | 10.68 | 35.2% | 15.1% |
| STALE | 16,590 | 10.3 | 6.9 | 15.8 | 13.8 | 19.3 | 17.8 | 16.1 | 16.45 | 53.2% | 33.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 17,421 | 16.4 | 11.3 | 22.4 | 15.3 | 17.7 | 12.1 | 4.9 | 9.99 | 34.7% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 56,917 | 17421 | 19846 | 19650 | 24.2 | 131.1 | 1400.4 |
| ge_15pp | 23,435 | 6044 | 7054 | 10337 | 26.3 | 434.1 | 1399.2 |
| ge_25pp | 12,518 | 2954 | 3066 | 6498 | 31.7 | 575.0 | 1380.4 |
| lt_10pp | 24,732 | 8714 | 9410 | 6608 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261027T000929Z-84f534ba`: 667 priced rows, quote age at build {'median': 14.7, 'max': 14.8}, freshness {'AGING': 667}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 28 | 0.0 | 0.0 | 21.4 | 10.7 | 39.3 | 28.6 | 0.0 | 20.48 | 67.9% | 28.6% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,206 | 19.5 | 11.3 | 25.0 | 18.9 | 17.8 | 6.9 | 0.7 | 8.77 | 25.3% | 7.6% |
| KALSHI_LONE_OUTLIER | 22 | 4.5 | 4.5 | 77.3 | 4.5 | 4.5 | 4.5 | 0.0 | 6.16 | 9.1% | 4.5% |
| MARKETS_AGREE | 649 | 65.3 | 34.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,395 | 0.0 | 2.6 | 35.1 | 26.7 | 24.9 | 10.0 | 0.7 | 12.0 | 35.6% | 10.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 32,964 | 5318 (16.1%) | 26.2% | 0.9% | {"EXTERNAL_STALE": 3206, "AGREES_WITH_KALSHI": 1395, "ALL_AGREE": 649, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 22, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 14,592 | 1329 (9.1%) | 37.3% | 1.6% | {"EXTERNAL_STALE": 812, "AGREES_WITH_KALSHI": 496, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 8,102 | 401 (5.0%) | 37.2% | 2.2% | {"EXTERNAL_STALE": 243, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,979 | 378 (9.5%) | 37.6% | 2.4% | {"EXTERNAL_STALE": 227, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 13,249 | 3006 (22.7%) | 17.5% | 0.8% | {"EXTERNAL_STALE": 1788, "ALL_AGREE": 649, "AGREES_WITH_KALSHI": 526, "AGREES_WITH_MODEL": 19, "EXTERNAL_OUTLIER": 18, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,317 | 10.3 | 7.6 | 19.4 | 14.6 | 22.4 | 15.9 | 9.8 | 14.09 | 48.1% | 25.7% |
| 4-10x | 4,260 | 11.0 | 8.5 | 18.6 | 15.3 | 22.2 | 14.7 | 9.7 | 13.84 | 46.6% | 24.4% |
| <2x | 16,863 | 15.1 | 10.1 | 19.4 | 16.4 | 17.3 | 12.9 | 8.8 | 11.58 | 39.1% | 21.8% |
| >=10x | 5,524 | 10.6 | 6.2 | 15.1 | 14.2 | 21.9 | 19.7 | 12.4 | 16.52 | 53.9% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,387 | 12.8 | 8.6 | 19.3 | 16.2 | 19.1 | 13.6 | 10.5 | 12.81 | 43.2% | 24.1% |
| 300-1000 | 6,896 | 11.8 | 8.7 | 17.4 | 15.2 | 20.9 | 16.1 | 9.9 | 13.83 | 46.9% | 26.0% |
| <300 | 10,714 | 8.4 | 5.7 | 15.3 | 14.7 | 23.3 | 20.1 | 12.5 | 17.02 | 55.9% | 32.6% |
| >=3000 | 6,967 | 21.2 | 13.5 | 23.8 | 16.4 | 13.8 | 6.9 | 4.5 | 7.71 | 25.1% | 11.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 938 | 0.5529 | 0.4147 | 0.5064 | +0.046 | -0.092 | -0.0038 ± 0.005 |
| ratio 4-10x | 631 | 0.5873 | 0.4416 | 0.504 | +0.083 | -0.062 | 0.0079 ± 0.0063 |
| ratio <2x | 2309 | 0.5392 | 0.4164 | 0.4495 | +0.090 | -0.033 | 0.0109 ± 0.003 |
| ratio >=10x | 847 | 0.5724 | 0.3971 | 0.4616 | +0.111 | -0.065 | 0.0088 ± 0.0063 |
| thinner_sample 1000-3000 | 1280 | 0.5417 | 0.4151 | 0.4539 | +0.088 | -0.039 | 0.0083 ± 0.004 |
| thinner_sample 300-1000 | 1058 | 0.5695 | 0.4267 | 0.4934 | +0.076 | -0.067 | 0.0009 ± 0.005 |
| thinner_sample <300 | 1596 | 0.5633 | 0.3968 | 0.4687 | +0.095 | -0.072 | 0.0084 ± 0.0044 |
| thinner_sample >=3000 | 791 | 0.5362 | 0.4416 | 0.469 | +0.067 | -0.027 | 0.0114 ± 0.0041 |
| data_status ADEQUATE | 1358 | 0.5379 | 0.4337 | 0.4536 | +0.084 | -0.020 | 0.0116 ± 0.0034 |
| data_status LIMITED | 1092 | 0.5514 | 0.4185 | 0.4899 | +0.061 | -0.071 | 0.0012 ± 0.0045 |
| data_status POOR | 2275 | 0.5655 | 0.4042 | 0.4708 | +0.095 | -0.067 | 0.0074 ± 0.0037 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 694 | 0.2024 | 0.2031 | -0.0007 ± 0.0006 | 0.586 | 0.5876 | 0.502 | 0.4871 | 0.5187 | -0.078 ± 0.0181 | -0.01 (5) |
| 3-5 | 432 | 0.2044 | 0.2039 | +0.0005 ± 0.0018 | 0.5917 | 0.589 | 0.5044 | 0.4644 | 0.4769 | -0.105 ± 0.0223 | 0.02 (1) |
| 5-10 | 977 | 0.2017 | 0.2023 | -0.0006 ± 0.0022 | 0.5898 | 0.5885 | 0.515 | 0.4411 | 0.477 | -0.089 ± 0.0148 | -0.0167 (6) |
| 10-15 | 825 | 0.2176 | 0.2089 | +0.0087 ± 0.004 | 0.6267 | 0.6005 | 0.5323 | 0.4083 | 0.4339 | -0.107 ± 0.0159 | -0.048 (5) |
| 15-25 | 1070 | 0.2257 | 0.214 | +0.0116 ± 0.0055 | 0.6472 | 0.6118 | 0.5783 | 0.3824 | 0.4514 | -0.095 ± 0.0142 | -0.0033 (9) |
| 25-40 | 607 | 0.2212 | 0.2095 | +0.0118 ± 0.011 | 0.6315 | 0.6018 | 0.659 | 0.349 | 0.4827 | -0.072 ± 0.0169 | -0.01 (1) |
| 40+ | 120 | 0.2698 | 0.2022 | +0.0676 ± 0.0353 | 0.7405 | 0.5909 | 0.763 | 0.316 | 0.4667 | -0.071 ± 0.0345 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3593 | 0.185 | 0.1858 | -0.0007 ± 0.0003 | 0.5456 | 0.5463 | 0.4891 | 0.474 | 0.5018 | -0.028 ± 0.0073 | -0.0129 (17) |
| 3-5 | 2385 | 0.1993 | 0.1976 | +0.0017 ± 0.0007 | 0.579 | 0.5725 | 0.4859 | 0.446 | 0.444 | -0.059 ± 0.0092 | 0.0 (2) |
| 5-10 | 5108 | 0.2 | 0.1968 | +0.0032 ± 0.0009 | 0.5855 | 0.5735 | 0.4853 | 0.4114 | 0.4254 | -0.048 ± 0.0063 | -0.0119 (21) |
| 10-15 | 4352 | 0.1981 | 0.1806 | +0.0175 ± 0.0016 | 0.5821 | 0.5325 | 0.4886 | 0.3643 | 0.3562 | -0.072 ± 0.0064 | -0.0281 (16) |
| 15-25 | 5483 | 0.2078 | 0.1695 | +0.0384 ± 0.0022 | 0.6091 | 0.5007 | 0.5032 | 0.3068 | 0.3088 | -0.071 ± 0.0055 | -0.0025 (44) |
| 25-40 | 4253 | 0.2226 | 0.1281 | +0.0944 ± 0.0034 | 0.6392 | 0.3925 | 0.5313 | 0.2179 | 0.2276 | -0.060 ± 0.0053 | -0.01 (1) |
| 40+ | 2747 | 0.3787 | 0.0476 | +0.3311 ± 0.0047 | 0.9859 | 0.1812 | 0.6321 | 0.1072 | 0.067 | -0.076 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 544 | 0.2081 | 0.2089 | -0.0008 ± 0.0007 | 0.5986 | 0.6005 | 0.5073 | 0.4922 | 0.5184 | -0.105 ± 0.0212 | -0.01 (3) |
| 3-5 | 390 | 0.2259 | 0.223 | +0.0030 ± 0.0019 | 0.6378 | 0.6315 | 0.5108 | 0.4711 | 0.4487 | -0.135 ± 0.0255 | 0.02 (1) |
| 5-10 | 849 | 0.2075 | 0.2071 | +0.0004 ± 0.0024 | 0.6016 | 0.6 | 0.5479 | 0.473 | 0.5112 | -0.086 ± 0.0161 | -0.01 (4) |
| 10-15 | 780 | 0.2164 | 0.2098 | +0.0066 ± 0.0041 | 0.6222 | 0.6053 | 0.566 | 0.4416 | 0.4795 | -0.107 ± 0.0172 | -0.04 (5) |
| 15-25 | 1102 | 0.231 | 0.2138 | +0.0172 ± 0.0055 | 0.6563 | 0.6106 | 0.5896 | 0.394 | 0.4519 | -0.099 ± 0.0142 | -0.0133 (9) |
| 25-40 | 770 | 0.2642 | 0.1978 | +0.0665 ± 0.0101 | 0.7395 | 0.5762 | 0.6551 | 0.3406 | 0.3948 | -0.121 ± 0.0158 | -0.0075 (4) |
| 40+ | 290 | 0.354 | 0.1748 | +0.1793 ± 0.0241 | 0.9724 | 0.521 | 0.7368 | 0.2538 | 0.3241 | -0.071 ± 0.0236 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3037 | 0.1947 | 0.195 | -0.0003 ± 0.0003 | 0.5662 | 0.5666 | 0.5119 | 0.4969 | 0.5104 | -0.045 ± 0.0083 | -0.0133 (15) |
| 3-5 | 2040 | 0.2014 | 0.2001 | +0.0013 ± 0.0008 | 0.5814 | 0.5776 | 0.512 | 0.4721 | 0.475 | -0.051 ± 0.0101 | 0.02 (1) |
| 5-10 | 4539 | 0.1981 | 0.1952 | +0.0028 ± 0.001 | 0.5823 | 0.5702 | 0.5125 | 0.4385 | 0.4594 | -0.040 ± 0.0066 | -0.0117 (6) |
| 10-15 | 3920 | 0.2017 | 0.1898 | +0.0119 ± 0.0017 | 0.5919 | 0.553 | 0.5151 | 0.3912 | 0.4056 | -0.055 ± 0.0071 | -0.0189 (18) |
| 15-25 | 5448 | 0.2162 | 0.1795 | +0.0367 ± 0.0023 | 0.6284 | 0.5266 | 0.5261 | 0.3304 | 0.3387 | -0.066 ± 0.0058 | -0.0086 (42) |
| 25-40 | 4983 | 0.2507 | 0.1366 | +0.1141 ± 0.0033 | 0.7062 | 0.4194 | 0.5578 | 0.241 | 0.222 | -0.086 ± 0.0052 | -0.0044 (18) |
| 40+ | 3954 | 0.3938 | 0.0618 | +0.3320 ± 0.0045 | 1.0357 | 0.2202 | 0.6518 | 0.1201 | 0.0873 | -0.071 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 664 | 0.2 | 0.2021 | -0.0022 ± 0.0006 | 0.5808 | 0.5861 | 0.5021 | 0.4869 | 0.5512 | -0.033 ± 0.0181 | -0.0137 (8) |
| 3-5 | 469 | 0.2028 | 0.2017 | +0.0011 ± 0.0017 | 0.5889 | 0.5846 | 0.507 | 0.4673 | 0.4755 | -0.114 ± 0.0216 | 0.0067 (3) |
| 5-10 | 1003 | 0.2029 | 0.2005 | +0.0024 ± 0.0021 | 0.5921 | 0.5832 | 0.5123 | 0.4383 | 0.4576 | -0.100 ± 0.0145 | -0.0071 (7) |
| 10-15 | 820 | 0.2093 | 0.2056 | +0.0037 ± 0.0039 | 0.6078 | 0.5936 | 0.5416 | 0.4181 | 0.4659 | -0.092 ± 0.0158 | -0.0317 (6) |
| 15-25 | 1012 | 0.2319 | 0.2151 | +0.0167 ± 0.0057 | 0.6624 | 0.6138 | 0.5891 | 0.3945 | 0.4486 | -0.108 ± 0.0146 | -0.03 (1) |
| 25-40 | 629 | 0.214 | 0.2172 | -0.0031 ± 0.0109 | 0.6173 | 0.6196 | 0.6683 | 0.3577 | 0.5151 | -0.057 ± 0.0167 | 0.015 (2) |
| 40+ | 128 | 0.2828 | 0.2132 | +0.0696 ± 0.0352 | 0.7821 | 0.6144 | 0.7707 | 0.3221 | 0.4766 | -0.065 ± 0.037 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3493 | 0.1858 | 0.1865 | -0.0007 ± 0.0003 | 0.5464 | 0.5475 | 0.4882 | 0.473 | 0.4921 | -0.034 ± 0.0074 | -0.0163 (35) |
| 3-5 | 2389 | 0.1987 | 0.1967 | +0.0020 ± 0.0007 | 0.5809 | 0.5743 | 0.4878 | 0.4482 | 0.4441 | -0.064 ± 0.0093 | -0.0094 (18) |
| 5-10 | 5211 | 0.1953 | 0.1904 | +0.0050 ± 0.0009 | 0.5745 | 0.5572 | 0.4867 | 0.4126 | 0.4164 | -0.056 ± 0.0061 | -0.01 (31) |
| 10-15 | 4239 | 0.1919 | 0.1769 | +0.0149 ± 0.0016 | 0.5676 | 0.5226 | 0.5002 | 0.3767 | 0.3774 | -0.065 ± 0.0065 | -0.015 (12) |
| 15-25 | 5636 | 0.2107 | 0.1715 | +0.0392 ± 0.0022 | 0.6157 | 0.5057 | 0.5135 | 0.3185 | 0.3165 | -0.073 ± 0.0055 | -0.03 (2) |
| 25-40 | 4276 | 0.2196 | 0.1321 | +0.0875 ± 0.0035 | 0.6335 | 0.4011 | 0.5354 | 0.2196 | 0.2406 | -0.052 ± 0.0053 | 0.01 (3) |
| 40+ | 2677 | 0.3926 | 0.0528 | +0.3398 ± 0.005 | 1.0252 | 0.1945 | 0.6445 | 0.114 | 0.0732 | -0.078 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1053 | 0.1965 | 0.1965 | -0.0000 ± 0.0005 | 0.5725 | 0.5722 | 0.5027 | 0.4876 | 0.4891 | -0.068 ± 0.0139 | -0.0224 (49) |
| 3-5 | 724 | 0.1931 | 0.1925 | +0.0006 ± 0.0013 | 0.564 | 0.5613 | 0.4918 | 0.452 | 0.4627 | -0.060 ± 0.0167 | -0.0194 (34) |
| 5-10 | 1525 | 0.2021 | 0.1965 | +0.0056 ± 0.0017 | 0.5933 | 0.5754 | 0.4977 | 0.4243 | 0.4236 | -0.075 ± 0.0115 | -0.005 (78) |
| 10-15 | 1034 | 0.2117 | 0.2002 | +0.0115 ± 0.0035 | 0.6147 | 0.5829 | 0.5275 | 0.4047 | 0.4178 | -0.073 ± 0.0142 | 0.0014 (64) |
| 15-25 | 1365 | 0.2312 | 0.2109 | +0.0203 ± 0.0049 | 0.6598 | 0.6067 | 0.58 | 0.3851 | 0.4322 | -0.075 ± 0.0125 | -0.0214 (59) |
| 25-40 | 832 | 0.2427 | 0.2094 | +0.0333 ± 0.0097 | 0.693 | 0.6007 | 0.6788 | 0.3664 | 0.4688 | -0.083 ± 0.0147 | -0.0219 (26) |
| 40+ | 275 | 0.343 | 0.2025 | +0.1405 ± 0.0265 | 0.9905 | 0.5924 | 0.8118 | 0.3309 | 0.4436 | -0.092 ± 0.0244 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3523 | 0.1819 | 0.182 | -0.0001 ± 0.0003 | 0.536 | 0.5355 | 0.5047 | 0.4895 | 0.4959 | -0.044 ± 0.0072 | -0.0157 (88) |
| 3-5 | 2467 | 0.1966 | 0.1947 | +0.0019 ± 0.0007 | 0.5718 | 0.5675 | 0.5021 | 0.4624 | 0.4585 | -0.054 ± 0.009 | -0.0209 (69) |
| 5-10 | 4920 | 0.197 | 0.1889 | +0.0082 ± 0.0009 | 0.58 | 0.5553 | 0.4937 | 0.4201 | 0.4041 | -0.072 ± 0.0062 | -0.0082 (132) |
| 10-15 | 3456 | 0.2072 | 0.1916 | +0.0156 ± 0.0018 | 0.6049 | 0.5616 | 0.5304 | 0.4075 | 0.4048 | -0.065 ± 0.0075 | -0.0053 (105) |
| 15-25 | 4242 | 0.2298 | 0.2004 | +0.0294 ± 0.0027 | 0.6626 | 0.5803 | 0.5694 | 0.3737 | 0.3979 | -0.064 ± 0.0069 | -0.0253 (107) |
| 25-40 | 2905 | 0.2575 | 0.1864 | +0.0711 ± 0.005 | 0.7303 | 0.5434 | 0.634 | 0.3206 | 0.3663 | -0.075 ± 0.0078 | -0.0229 (51) |
| 40+ | 1263 | 0.3732 | 0.1474 | +0.2258 ± 0.0113 | 1.0554 | 0.4441 | 0.7318 | 0.2288 | 0.2692 | -0.068 ± 0.0101 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4725 | 1.033 ± 0.041 | 1.108 | 0.1683 | 0.1627 | 0.2145 | 0.2073 |
| gen2 | 4725 | 0.825 ± 0.038 | 1.07 | 0.1687 | 0.1633 | 0.2343 | 0.2071 |
| gen1_elo | 4725 | 1.006 ± 0.04 | 1.107 | 0.1748 | 0.1629 | 0.2134 | 0.2074 |
| gen1_sr | 4725 | 1.009 ± 0.049 | 1.133 | 0.1295 | 0.1652 | 0.2306 | 0.2067 |
| gen1_ledger | 6808 | 0.864 ± 0.029 | 1.065 | 0.1842 | 0.1766 | 0.2182 | 0.2013 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 23,435)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,259 | 22.4% |
| STALE_QUOTE | market_freshness | 5,163 | 22.0% |
| BOOK_QUALITY | execution | 4,505 | 19.2% |
| POOR_DATA | data | 2,602 | 11.1% |
| LIMITED_DATA | data | 1,441 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,267 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,101 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 992 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 689 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 415 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.4%, market_freshness 22.0%, execution 19.2%, data 17.2%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 93.9%, LOW_DATA_QUALITY 70.9%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 50.3%, STALE_KALSHI_QUOTE 44.1%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.4%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.6%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.4%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 12,518)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,219 | 33.7% |
| STALE_QUOTE | market_freshness | 2,386 | 19.1% |
| BOOK_QUALITY | execution | 2,366 | 18.9% |
| POOR_DATA | data | 1,072 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 679 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 550 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 439 | 3.5% |
| LIMITED_DATA | data | 429 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 279 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 98 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.7%, market_freshness 19.1%, execution 18.9%, data 12.0%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.4%, THIN_PLAYER_HISTORY 62.0%, STALE_KALSHI_QUOTE 51.9%, STALE_PLAYER_DATA 44.9%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.9%, PLAYER_IDENTITY_RISK 20.0%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 9.8%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.8%, POST_SETTLEMENT_OBSERVATION 33.7%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9711, "IDENTITY_AMBIGUOUS": 2807}; ticker orientation: {"VERIFIED": 12518}.

Checks: discipline:AMBIGUOUS 866, discipline:PASS 11652, identity_confidence:AMBIGUOUS 2499, identity_confidence:PASS 10019, level_mapping:NA 878, level_mapping:PASS 11640, market_pair:AMBIGUOUS 466, market_pair:NA 304, market_pair:PASS 11748, model_complement:NA 271, model_complement:PASS 12247, namesake:AMBIGUOUS 6, namesake:PASS 12512, physical_match_id:NA 4416, physical_match_id:PASS 8102, player_ids:PASS 12518, same_pair_other_event:PASS 12518, ticker_orientation:PASS 12518

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,905 | 4.4% | 3.9% | 1.7% | {"market_freshness": 56, "model_calibration_or_unknown": 50, "data": 36, "execution": 24, "model_calibration": 21, "market_freshness/coverage": 15, "coverage": 13} | 5.87 | 0.2217 / 0.2194 (561) | 20.6% | 3.2% | 3.3% | 2.7% |
| CHALLENGER | 8,873 | 16.7% | 6.8% | 11.8% | {"coverage": 831, "market_freshness/coverage": 179, "market_freshness": 167, "data": 144, "model_calibration_or_unknown": 69, "execution": 36, "model_calibration": 35, "mapping": 16, "possible_market_error": 1} | 7.59 | 0.2187 / 0.2099 (2079) | 34.6% | 17.1% | 4.2% | 22.1% |
| DOUBLES | 1,822 | 47.5% | 47.2% | 6.9% | {"execution": 481, "mapping": 217, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.86 | 0.3088 / 0.2362 (441) | 12.8% | 0.0% | 100.0% | 6.6% |
| ITF_MEN | 15,283 | 25.8% | 18.1% | 31.4% | {"coverage": 1443, "execution": 752, "market_freshness": 695, "data": 521, "market_freshness/coverage": 344, "mapping": 178, "model_calibration_or_unknown": 2, "model_calibration": 2} | 12.01 | 0.2168 / 0.199 (3377) | 37.6% | 70.4% | 19.6% | 22.2% |
| ITF_WOMEN | 20,697 | 27.1% | 19.9% | 44.8% | {"coverage": 1900, "market_freshness": 1241, "execution": 1022, "data": 755, "market_freshness/coverage": 474, "mapping": 133, "model_calibration_or_unknown": 70, "model_calibration": 11} | 12.88 | 0.2034 / 0.1964 (3954) | 39.8% | 57.5% | 10.4% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,479 | 5.5% | 5.0% | 1.5% | {"market_freshness": 70, "model_calibration_or_unknown": 39, "execution": 26, "model_calibration": 16, "data": 16, "coverage": 12, "market_freshness/coverage": 11, "mapping": 1} | 7.67 | 0.2318 / 0.2259 (541) | 25.6% | 1.2% | 1.5% | 3.3% |
| WTA125 | 1,703 | 12.5% | 10.4% | 1.7% | {"market_freshness": 49, "model_calibration_or_unknown": 47, "market_freshness/coverage": 39, "data": 29, "execution": 20, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.52 | 0.2164 / 0.2034 (538) | 24.7% | 11.5% | 6.3% | 8.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9676, "by_level_share_of_ge_25pp": {"ATP": 0.0172, "CHALLENGER": 0.1181, "DOUBLES": 0.0692, "ITF_MEN": 0.3145, "ITF_WOMEN": 0.4478, "OTHER": 0.001, "WTA": 0.0153, "WTA125": 0.017}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5191, "share_primary_cause_market_settled_or_in_play": 0.4263, "share_primary_cause_stale_quote_only": 0.1906}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 12518, "identity_ambiguous_share": 0.2242, "ticker_orientation": {"VERIFIED": 12518}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 8102, "with_external": 401, "coverage": 0.0495, "external_status": {"EXTERNAL_STALE": 243, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 243, "MODEL_LONE_OUTLIER": 149, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3716, "share_external_supports_model": 0.0224}, "pregame_clean_ge_25pp": {"n": 3979, "with_external": 378, "coverage": 0.095, "external_status": {"EXTERNAL_STALE": 227, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 227, "MODEL_LONE_OUTLIER": 142, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3757, "share_external_supports_model": 0.0238}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 473.0, "median_sample_ratio": 2.45, "median_min_matches": 20.0, "median_max_days_since_last": 231.0, "share_severe_asymmetry": 0.2166, "data_status": {"POOR": 7005, "LIMITED": 3242, "ADEQUATE": 2271}, "comparison_lt_10pp": {"median_thinner_serve_points": 1787.0, "median_sample_ratio": 1.67, "median_min_matches": 98.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 938, "model_minus_observed": 0.0465, "kalshi_minus_observed": -0.0917, "brier_diff_model_minus_kalshi": -0.0038}, "4-10x": {"n": 631, "model_minus_observed": 0.0834, "kalshi_minus_observed": -0.0624, "brier_diff_model_minus_kalshi": 0.0079}, "<2x": {"n": 2309, "model_minus_observed": 0.0897, "kalshi_minus_observed": -0.0331, "brier_diff_model_minus_kalshi": 0.0109}, ">=10x": {"n": 847, "model_minus_observed": 0.1107, "kalshi_minus_observed": -0.0646, "brier_diff_model_minus_kalshi": 0.0088}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4725, "model": {"intercept": -0.531, "slope": 0.825, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.203, "slope": 1.07, "slope_se": 0.042}, "mean_extremity_model": 0.1687, "mean_extremity_kalshi": 0.1633, "model_brier": 0.2343, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0272, "brier_diff_se": 0.0028, "model_logloss": 0.6656, "kalshi_logloss": 0.5973}, "fair_v1": {"n": 4725, "model": {"intercept": -0.409, "slope": 1.033, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.29, "slope": 1.108, "slope_se": 0.042}, "mean_extremity_model": 0.1683, "mean_extremity_kalshi": 0.1627, "model_brier": 0.2145, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.0072, "brier_diff_se": 0.0023, "model_logloss": 0.6181, "kalshi_logloss": 0.5976}, "gen1_elo": {"n": 4725, "model": {"intercept": -0.382, "slope": 1.006, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.314, "slope": 1.107, "slope_se": 0.042}, "mean_extremity_model": 0.1748, "mean_extremity_kalshi": 0.1629, "model_brier": 0.2134, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.006, "brier_diff_se": 0.0023, "model_logloss": 0.6165, "kalshi_logloss": 0.5978}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2458, "share_ge_15": 0.4427, "median_abs_gap": 13.05, "n": 32964}, "gen1_elo": {"share_ge_25": 0.2433, "share_ge_15": 0.4417, "median_abs_gap": 12.95, "n": 32964}, "gen1_sr": {"share_ge_25": 0.3134, "share_ge_15": 0.5204, "median_abs_gap": 15.89, "n": 32964}, "gen2": {"share_ge_25": 0.3174, "share_ge_15": 0.512, "median_abs_gap": 15.51, "n": 32964}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1548, "share_ge_15": 0.3592, "median_abs_gap": 10.85, "n": 25708}, "gen1_elo": {"share_ge_25": 0.1551, "share_ge_15": 0.3572, "median_abs_gap": 10.69, "n": 25705}, "gen1_sr": {"share_ge_25": 0.2213, "share_ge_15": 0.443, "median_abs_gap": 13.01, "n": 25709}, "gen2": {"share_ge_25": 0.2381, "share_ge_15": 0.4442, "median_abs_gap": 13.03, "n": 25710}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.87, "share_ge_25_all": 0.0438, "share_ge_25_pregame_clean": 0.0392}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.0549, "share_ge_25_pregame_clean": 0.0499}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2359, "share_within_10pp_all": 0.4345, "share_within_10pp_pregame_clean": 0.4861, "corr_model_vs_mid_pregame_clean": 0.8432}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 694, "model_brier": 0.2024, "kalshi_brier": 0.2031, "brier_diff_model_minus_kalshi": -0.0007}, "10-15": {"n_settled": 825, "model_brier": 0.2176, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1070, "model_brier": 0.2257, "kalshi_brier": 0.214, "brier_diff_model_minus_kalshi": 0.0116}, "25-40": {"n_settled": 607, "model_brier": 0.2212, "kalshi_brier": 0.2095, "brier_diff_model_minus_kalshi": 0.0118}, "3-5": {"n_settled": 432, "model_brier": 0.2044, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 120, "model_brier": 0.2698, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0676}, "5-10": {"n_settled": 977, "model_brier": 0.2017, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": -0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.531, "slope": 0.825, "slope_se": 0.038}, "kalshi_slope": {"intercept": 0.203, "slope": 1.07, "slope_se": 0.042}, "n": 4725}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.494, "slope": 0.864, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.163, "slope": 1.065, "slope_se": 0.034}, "n": 6808}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 441, "model_brier": 0.3088, "kalshi_brier": 0.2362, "brier_diff_model_minus_kalshi": 0.0726, "brier_diff_se": 0.0144, "corr_model_outcome": 0.0389, "corr_kalshi_outcome": 0.2525}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
