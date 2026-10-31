# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-31T22:46Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 71,576): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.0%, 25-40 13.7%, 40+ 8.0%; median gap 11.82 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.7%, doubles 6.7%). Main tour: ATP 4.0% and WTA 5.8% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,592): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.2%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.3%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.2%, market_freshness 18.7%, execution 18.3%, data 12.7%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,592 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.6% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 484.0 points vs 1736.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.016, Gen-2 0.805, Gen-1 ledger 0.854 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 756 model 0.2235 vs Kalshi 0.2061; n 159 model 0.2822 vs Kalshi 0.1885.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 305,182 model-market comparisons (498,143 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 103,107 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-31T22:30:38.359793+00:00'], shadow board 81,714 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-31T22:30:43.472890+00:00'], Model 4 38,025 rows, 24,933 settled tickers, 9,124 tickers with an external scan.
* By model: {"gen1_ledger": 69628, "gen1_elo": 41068, "fair_v1": 41068, "gen2": 41068, "gen1_sr": 41068, "model4_fundamental": 35663, "model4_conditioned": 35619}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 71,576 | 14.1 | 9.6 | 20.2 | 15.3 | 19.0 | 13.7 | 8.0 | 11.82 | 40.8% | 21.8% |
| MW fair_v1 | 41,068 | 13.0 | 8.7 | 18.8 | 15.3 | 19.4 | 14.8 | 9.9 | 13.0 | 44.2% | 24.8% |
| MW gen1_elo | 41,068 | 12.5 | 8.7 | 19.4 | 15.4 | 19.5 | 14.8 | 9.8 | 12.92 | 44.1% | 24.6% |
| MW gen1_ledger | 30,508 | 15.7 | 10.8 | 22.1 | 15.2 | 18.3 | 12.3 | 5.5 | 10.31 | 36.1% | 17.8% |
| MW gen1_sr | 41,068 | 10.2 | 7.2 | 16.9 | 13.9 | 20.6 | 18.5 | 12.7 | 15.77 | 51.9% | 31.2% |
| MW gen2 | 41,068 | 11.1 | 7.6 | 16.6 | 13.8 | 19.4 | 17.7 | 13.8 | 15.41 | 50.9% | 31.5% |
| all families model4_conditioned | 35,619 | 22.4 | 18.3 | 34.1 | 17.1 | 4.9 | 2.1 | 1.2 | 5.99 | 8.2% | 3.2% |
| all families model4_fundamental | 35,663 | 17.4 | 13.3 | 33.8 | 20.2 | 10.1 | 3.7 | 1.4 | 7.65 | 15.2% | 5.2% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.0%, >=15pp 40.8%, >=20pp 30.1%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.26pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,580 | 27.4 | 15.4 | 28.2 | 13.3 | 11.4 | 3.9 | 0.6 | 5.93 | 15.8% | 4.4% |
| CHALLENGER | 6,051 | 16.4 | 9.8 | 20.8 | 15.1 | 15.3 | 11.7 | 10.9 | 10.91 | 37.9% | 22.6% |
| ITF_MEN | 11,529 | 9.8 | 7.4 | 17.0 | 15.0 | 21.2 | 17.6 | 12.0 | 15.23 | 50.7% | 29.5% |
| ITF_WOMEN | 16,151 | 9.6 | 7.1 | 16.0 | 15.1 | 22.0 | 18.1 | 12.2 | 15.73 | 52.3% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,599 | 18.2 | 13.4 | 25.3 | 19.9 | 15.8 | 6.2 | 1.1 | 8.2 | 23.1% | 7.3% |
| WTA125 | 1,152 | 16.5 | 7.2 | 22.4 | 19.2 | 20.8 | 12.1 | 1.8 | 10.7 | 34.7% | 13.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,580 | 26.0 | 15.4 | 26.3 | 15.9 | 11.7 | 3.9 | 0.8 | 6.22 | 16.4% | 4.7% |
| CHALLENGER | 6,051 | 15.2 | 9.1 | 18.2 | 14.2 | 18.1 | 13.4 | 11.8 | 12.49 | 43.3% | 25.2% |
| ITF_MEN | 11,529 | 8.1 | 6.2 | 15.1 | 13.8 | 19.5 | 20.7 | 16.5 | 17.91 | 56.7% | 37.2% |
| ITF_WOMEN | 16,151 | 8.0 | 5.8 | 14.0 | 12.7 | 20.7 | 21.2 | 17.7 | 19.12 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,599 | 15.3 | 10.9 | 22.3 | 15.1 | 21.8 | 12.5 | 2.0 | 10.53 | 36.3% | 14.5% |
| WTA125 | 1,152 | 9.7 | 6.8 | 17.0 | 15.7 | 24.3 | 17.8 | 8.7 | 15.21 | 50.8% | 26.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,580 | 22.1 | 13.6 | 24.7 | 16.0 | 15.8 | 6.5 | 1.3 | 7.52 | 23.6% | 7.8% |
| CHALLENGER | 6,051 | 15.1 | 9.2 | 20.9 | 16.1 | 15.6 | 12.1 | 11.1 | 11.33 | 38.7% | 23.2% |
| ITF_MEN | 11,529 | 9.3 | 7.2 | 17.3 | 14.2 | 21.8 | 17.7 | 12.4 | 15.75 | 52.0% | 30.1% |
| ITF_WOMEN | 16,151 | 9.4 | 6.9 | 16.4 | 15.8 | 22.1 | 18.0 | 11.5 | 15.51 | 51.5% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,599 | 23.1 | 16.4 | 32.2 | 14.5 | 9.4 | 3.1 | 1.2 | 6.17 | 13.7% | 4.3% |
| WTA125 | 1,152 | 21.4 | 12.9 | 27.2 | 17.7 | 14.8 | 5.7 | 0.3 | 7.99 | 20.8% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,150 | 25.2 | 19.4 | 30.7 | 12.8 | 8.7 | 2.7 | 0.5 | 5.62 | 11.9% | 3.2% |
| CHALLENGER | 4,104 | 22.7 | 14.6 | 27.3 | 14.4 | 13.5 | 5.9 | 1.6 | 7.07 | 21.0% | 7.5% |
| DOUBLES | 2,221 | 5.2 | 4.3 | 11.9 | 10.5 | 20.9 | 25.3 | 22.0 | 23.73 | 68.1% | 47.2% |
| ITF_MEN | 8,693 | 13.0 | 9.5 | 21.3 | 15.8 | 21.4 | 13.2 | 5.8 | 11.87 | 40.4% | 19.0% |
| ITF_WOMEN | 10,432 | 13.1 | 9.1 | 19.9 | 15.8 | 21.2 | 15.4 | 5.5 | 12.33 | 42.1% | 20.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,590 | 24.3 | 16.2 | 30.3 | 17.1 | 9.0 | 2.9 | 0.2 | 6.49 | 12.1% | 3.1% |
| WTA125 | 1,169 | 24.8 | 12.8 | 21.1 | 19.6 | 13.3 | 6.8 | 1.5 | 7.88 | 21.6% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,481 | 27.7 | 15.5 | 28.5 | 13.2 | 11.2 | 3.5 | 0.3 | 5.9 | 15.0% | 3.9% |
| CHALLENGER | 4,239 | 21.3 | 12.3 | 25.9 | 17.7 | 15.2 | 6.0 | 1.6 | 7.99 | 22.8% | 7.6% |
| ITF_MEN | 8,400 | 12.1 | 8.8 | 20.6 | 17.1 | 22.0 | 14.2 | 5.2 | 12.34 | 41.4% | 19.4% |
| ITF_WOMEN | 11,966 | 11.5 | 8.5 | 18.6 | 17.2 | 24.0 | 15.1 | 5.1 | 13.25 | 44.1% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,510 | 18.6 | 13.3 | 25.6 | 20.3 | 15.7 | 5.8 | 0.7 | 8.15 | 22.2% | 6.5% |
| WTA125 | 1,113 | 16.7 | 7.1 | 21.9 | 19.5 | 21.3 | 11.9 | 1.6 | 10.8 | 34.8% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,481 | 26.3 | 15.7 | 26.5 | 15.8 | 11.7 | 3.6 | 0.4 | 6.18 | 15.7% | 4.0% |
| CHALLENGER | 4,239 | 19.3 | 11.6 | 22.9 | 16.7 | 18.5 | 9.0 | 1.9 | 8.99 | 29.4% | 10.9% |
| ITF_MEN | 8,401 | 9.6 | 7.4 | 17.6 | 16.1 | 21.3 | 18.7 | 9.4 | 14.85 | 49.5% | 28.1% |
| ITF_WOMEN | 11,967 | 8.9 | 6.8 | 15.9 | 14.3 | 22.8 | 20.6 | 10.7 | 16.58 | 54.1% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,510 | 15.6 | 11.0 | 22.5 | 15.2 | 21.9 | 12.5 | 1.3 | 10.29 | 35.7% | 13.8% |
| WTA125 | 1,113 | 9.7 | 6.8 | 17.2 | 15.8 | 24.3 | 18.1 | 8.2 | 15.14 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,093 | 25.3 | 19.6 | 30.7 | 13.0 | 8.4 | 2.6 | 0.4 | 5.54 | 11.4% | 3.0% |
| CHALLENGER | 3,621 | 24.2 | 15.5 | 28.5 | 14.6 | 12.8 | 4.0 | 0.5 | 6.58 | 17.3% | 4.5% |
| DOUBLES | 2,083 | 5.1 | 4.4 | 12.2 | 10.7 | 20.6 | 25.2 | 21.9 | 23.62 | 67.7% | 47.1% |
| ITF_MEN | 7,420 | 13.8 | 10.1 | 22.9 | 16.4 | 21.3 | 11.7 | 3.8 | 10.88 | 36.7% | 15.4% |
| ITF_WOMEN | 8,894 | 13.7 | 9.6 | 21.2 | 16.4 | 21.3 | 14.3 | 3.5 | 11.53 | 39.1% | 17.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,532 | 24.6 | 16.6 | 30.3 | 17.2 | 9.0 | 2.3 | 0.1 | 6.36 | 11.4% | 2.4% |
| WTA125 | 1,039 | 26.0 | 13.6 | 22.2 | 20.7 | 12.3 | 4.7 | 0.5 | 7.42 | 17.5% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,221 | 5.2 | 4.3 | 11.9 | 10.5 | 20.9 | 25.3 | 22.0 | 23.73 | 68.1% | 47.2% |
| singles | 28,287 | 16.5 | 11.4 | 22.9 | 15.6 | 18.1 | 11.3 | 4.2 | 9.78 | 33.6% | 15.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 8,052 | 13.2 | 9.4 | 20.2 | 15.8 | 18.9 | 13.7 | 8.9 | 12.27 | 41.5% | 22.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 27,062 | 13.4 | 8.7 | 18.8 | 15.0 | 19.2 | 14.9 | 10.1 | 12.95 | 44.1% | 24.9% |
| UNKNOWN | 5,705 | 10.4 | 7.8 | 17.1 | 16.2 | 21.3 | 16.1 | 11.1 | 14.27 | 48.5% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 11,518 | 20.1 | 12.0 | 22.6 | 15.5 | 14.7 | 9.0 | 6.1 | 8.52 | 29.8% | 15.1% |
| B | 5,135 | 12.9 | 8.9 | 19.5 | 15.8 | 19.4 | 12.6 | 10.9 | 12.54 | 42.9% | 23.5% |
| C | 5,881 | 11.8 | 8.9 | 19.9 | 15.7 | 18.5 | 14.6 | 10.8 | 12.89 | 43.8% | 25.3% |
| D | 6,483 | 11.8 | 8.4 | 17.5 | 15.3 | 21.6 | 15.9 | 9.5 | 13.85 | 47.0% | 25.4% |
| F | 12,051 | 7.4 | 5.6 | 15.0 | 14.8 | 23.3 | 20.9 | 13.0 | 17.65 | 57.2% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,228 | 24.4 | 15.9 | 29.1 | 15.0 | 10.8 | 3.6 | 1.3 | 6.42 | 15.6% | 4.8% |
| B | 4,358 | 16.7 | 10.8 | 24.1 | 16.9 | 18.8 | 9.7 | 3.1 | 9.68 | 31.5% | 12.8% |
| C | 5,977 | 11.3 | 7.8 | 19.2 | 14.5 | 21.0 | 15.9 | 10.3 | 13.67 | 47.1% | 26.1% |
| D | 4,457 | 14.2 | 9.8 | 21.6 | 15.5 | 20.0 | 13.4 | 5.4 | 11.27 | 38.9% | 18.8% |
| F | 7,488 | 9.9 | 8.3 | 16.0 | 14.9 | 23.2 | 19.9 | 7.7 | 15.41 | 50.8% | 27.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 13,030 | 18.3 | 10.9 | 21.8 | 15.3 | 15.1 | 9.8 | 8.9 | 9.71 | 33.8% | 18.7% |
| LIMITED | 9,125 | 13.6 | 9.9 | 20.4 | 16.0 | 19.1 | 13.3 | 7.6 | 11.76 | 40.0% | 20.9% |
| POOR | 18,913 | 9.0 | 6.6 | 16.0 | 15.0 | 22.6 | 19.0 | 11.8 | 16.15 | 53.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,095 | 24.1 | 18.1 | 33.1 | 15.3 | 6.3 | 2.7 | 0.4 | 5.88 | 9.4% | 3.1% |
| GAME_SPREAD | 6,122 | 22.3 | 15.1 | 32.7 | 16.9 | 9.1 | 3.3 | 0.6 | 6.75 | 13.0% | 3.9% |
| MATCH_WINNER | 30,508 | 15.7 | 10.8 | 22.1 | 15.2 | 18.3 | 12.3 | 5.5 | 10.31 | 36.1% | 17.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 14,697 | 27.7 | 16.8 | 30.9 | 12.5 | 9.4 | 2.5 | 0.3 | 5.65 | 12.2% | 2.8% |
| TOTAL_GAMES | 10,182 | 9.9 | 10.7 | 35.6 | 26.4 | 10.4 | 4.1 | 2.9 | 9.23 | 17.4% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,767 | 24.3 | 29.7 | 33.0 | 7.7 | 4.1 | 0.9 | 0.3 | 4.76 | 5.3% | 1.2% |
| GAME_SPREAD | 8,280 | 47.2 | 16.1 | 25.0 | 7.1 | 2.2 | 1.7 | 0.6 | 3.28 | 4.6% | 2.4% |
| TOTAL_GAMES | 14,572 | 6.6 | 9.5 | 40.2 | 30.9 | 7.2 | 3.2 | 2.2 | 9.27 | 12.7% | 5.5% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,778 | 23.9 | 16.7 | 34.8 | 14.6 | 7.0 | 2.6 | 0.4 | 6.03 | 10.0% | 3.0% |
| GAME_SPREAD | 8,283 | 20.2 | 13.6 | 28.0 | 20.2 | 12.3 | 4.5 | 1.1 | 7.75 | 18.0% | 5.7% |
| TOTAL_GAMES | 14,602 | 10.2 | 10.3 | 36.3 | 25.0 | 11.4 | 4.3 | 2.5 | 9.15 | 18.2% | 6.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 41,068 | 44.2% | 24.8% | 13.0 | 35.3% | 15.2% | 10.65 |
| gen1_elo | 41,068 | 44.1% | 24.6% | 12.92 | 35.1% | 15.1% | 10.51 |
| gen1_sr | 41,068 | 51.9% | 31.2% | 15.77 | 43.8% | 21.6% | 12.95 |
| gen2 | 41,068 | 50.9% | 31.5% | 15.41 | 43.8% | 23.2% | 12.8 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,801 | 15.7 | 10.5 | 21.4 | 17.2 | 20.0 | 11.9 | 3.3 | 10.68 | 35.3% | 15.2% |
| STALE | 22,267 | 10.7 | 7.2 | 16.6 | 13.7 | 19.0 | 17.3 | 15.6 | 15.66 | 51.8% | 32.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 23,976 | 16.4 | 11.2 | 22.8 | 15.4 | 17.8 | 11.8 | 4.7 | 9.89 | 34.2% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 71,576 | 23976 | 22273 | 25327 | 24.4 | 125.2 | 1451.1 |
| ge_15pp | 29,172 | 8211 | 7921 | 13040 | 27.0 | 437.7 | 1451.1 |
| ge_25pp | 15,592 | 3955 | 3457 | 8180 | 32.1 | 588.6 | 1431.1 |
| lt_10pp | 31,468 | 12081 | 10573 | 8814 | 22.4 | 46.9 | 1421.1 |

Current slate `SL-20261031T224617Z-a289d9fa`: 563 priced rows, quote age at build {'median': 16.1, 'max': 16.1}, freshness {'AGING': 563}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 47 | 0.0 | 0.0 | 34.0 | 6.4 | 34.0 | 21.3 | 4.3 | 19.92 | 59.6% | 25.5% |
| EXTERNAL_LONE_OUTLIER | 25 | 64.0 | 36.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,057 | 19.7 | 11.0 | 25.4 | 17.9 | 17.9 | 7.2 | 0.9 | 8.62 | 26.0% | 8.1% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 844 | 66.2 | 33.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,814 | 0.0 | 2.3 | 37.4 | 25.6 | 24.1 | 9.7 | 0.9 | 11.84 | 34.7% | 10.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 41,068 | 6814 (16.6%) | 26.6% | 1.1% | {"EXTERNAL_STALE": 4057, "AGREES_WITH_KALSHI": 1814, "ALL_AGREE": 844, "SUPPORTS_MODEL_DIRECTION": 46, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 25, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 18,162 | 1713 (9.4%) | 36.7% | 1.8% | {"EXTERNAL_STALE": 1054, "AGREES_WITH_KALSHI": 629, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,175 | 533 (5.2%) | 35.8% | 2.4% | {"EXTERNAL_STALE": 329, "AGREES_WITH_KALSHI": 191, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,807 | 506 (10.5%) | 36.4% | 2.6% | {"EXTERNAL_STALE": 309, "AGREES_WITH_KALSHI": 184, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 16,618 | 3906 (23.5%) | 18.4% | 1.0% | {"EXTERNAL_STALE": 2278, "ALL_AGREE": 844, "AGREES_WITH_KALSHI": 720, "EXTERNAL_OUTLIER": 25, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 15, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,976 | 10.5 | 7.6 | 19.4 | 14.4 | 21.4 | 16.6 | 10.0 | 14.1 | 48.0% | 26.6% |
| 4-10x | 5,504 | 11.0 | 8.5 | 18.8 | 15.5 | 21.9 | 14.3 | 10.1 | 13.64 | 46.2% | 24.4% |
| <2x | 20,968 | 15.2 | 9.9 | 19.8 | 15.9 | 17.3 | 13.0 | 9.0 | 11.52 | 39.3% | 21.9% |
| >=10x | 6,620 | 10.4 | 6.4 | 15.1 | 14.5 | 21.8 | 19.1 | 12.8 | 16.35 | 53.7% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,741 | 12.8 | 8.8 | 19.8 | 15.8 | 19.1 | 13.4 | 10.4 | 12.66 | 42.9% | 23.8% |
| 300-1000 | 8,822 | 11.9 | 8.8 | 17.8 | 15.3 | 20.3 | 16.4 | 9.6 | 13.61 | 46.3% | 26.0% |
| <300 | 13,043 | 8.2 | 5.8 | 15.2 | 14.8 | 23.0 | 20.0 | 13.0 | 17.07 | 56.0% | 33.0% |
| >=3000 | 8,462 | 21.6 | 12.9 | 24.3 | 15.5 | 13.6 | 7.1 | 5.0 | 7.57 | 25.7% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1186 | 0.5494 | 0.4114 | 0.4933 | +0.056 | -0.082 | -0.0016 ± 0.0045 |
| ratio 4-10x | 816 | 0.5812 | 0.4351 | 0.4951 | +0.086 | -0.060 | 0.0081 ± 0.0056 |
| ratio <2x | 2908 | 0.537 | 0.4151 | 0.4436 | +0.093 | -0.029 | 0.0125 ± 0.0026 |
| ratio >=10x | 1011 | 0.5678 | 0.3927 | 0.45 | +0.118 | -0.057 | 0.0143 ± 0.0057 |
| thinner_sample 1000-3000 | 1643 | 0.5385 | 0.4124 | 0.4486 | +0.090 | -0.036 | 0.0097 ± 0.0035 |
| thinner_sample 300-1000 | 1335 | 0.5682 | 0.4267 | 0.4854 | +0.083 | -0.059 | 0.0029 ± 0.0043 |
| thinner_sample <300 | 1940 | 0.5596 | 0.3918 | 0.4582 | +0.101 | -0.066 | 0.0116 ± 0.004 |
| thinner_sample >=3000 | 1003 | 0.5311 | 0.4382 | 0.4586 | +0.072 | -0.021 | 0.0134 ± 0.0036 |
| data_status ADEQUATE | 1637 | 0.5328 | 0.431 | 0.4453 | +0.087 | -0.014 | 0.0134 ± 0.003 |
| data_status LIMITED | 1459 | 0.5491 | 0.4165 | 0.4722 | +0.077 | -0.056 | 0.0064 ± 0.0039 |
| data_status POOR | 2825 | 0.5622 | 0.4013 | 0.4658 | +0.096 | -0.065 | 0.0086 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 872 | 0.2005 | 0.2009 | -0.0004 ± 0.0005 | 0.5814 | 0.5825 | 0.503 | 0.4878 | 0.5069 | -0.088 ± 0.0161 | -0.01 (5) |
| 3-5 | 543 | 0.2053 | 0.2052 | +0.0000 ± 0.0016 | 0.5926 | 0.5915 | 0.5044 | 0.4646 | 0.4825 | -0.103 ± 0.02 | 0.02 (1) |
| 5-10 | 1259 | 0.2021 | 0.2015 | +0.0006 ± 0.0019 | 0.5906 | 0.5871 | 0.51 | 0.4363 | 0.467 | -0.092 ± 0.0131 | -0.0167 (6) |
| 10-15 | 1030 | 0.2201 | 0.2112 | +0.0089 ± 0.0036 | 0.6326 | 0.6074 | 0.5285 | 0.4048 | 0.4291 | -0.108 ± 0.0144 | -0.048 (5) |
| 15-25 | 1302 | 0.2257 | 0.2118 | +0.0139 ± 0.005 | 0.647 | 0.6076 | 0.576 | 0.3809 | 0.4432 | -0.101 ± 0.0128 | -0.0033 (9) |
| 25-40 | 756 | 0.2235 | 0.2061 | +0.0174 ± 0.0099 | 0.6372 | 0.5941 | 0.6551 | 0.3451 | 0.4722 | -0.075 ± 0.0151 | -0.01 (1) |
| 40+ | 159 | 0.2822 | 0.1885 | +0.0938 ± 0.03 | 0.7687 | 0.5556 | 0.7384 | 0.2904 | 0.4151 | -0.073 ± 0.0297 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4737 | 0.1855 | 0.1864 | -0.0009 ± 0.0002 | 0.5463 | 0.5474 | 0.4871 | 0.4718 | 0.5031 | -0.022 ± 0.0064 | -0.0129 (17) |
| 3-5 | 3178 | 0.1954 | 0.1935 | +0.0019 ± 0.0006 | 0.5696 | 0.5627 | 0.4828 | 0.443 | 0.4377 | -0.060 ± 0.0079 | 0.0 (2) |
| 5-10 | 6811 | 0.2019 | 0.1983 | +0.0036 ± 0.0008 | 0.5898 | 0.5779 | 0.4853 | 0.4118 | 0.4245 | -0.047 ± 0.0055 | -0.0119 (21) |
| 10-15 | 5609 | 0.2017 | 0.1857 | +0.0160 ± 0.0014 | 0.5897 | 0.5459 | 0.4854 | 0.3614 | 0.3582 | -0.066 ± 0.0058 | -0.0281 (16) |
| 15-25 | 7024 | 0.2068 | 0.1684 | +0.0385 ± 0.0019 | 0.6062 | 0.4993 | 0.4993 | 0.3036 | 0.3041 | -0.069 ± 0.0049 | -0.0025 (44) |
| 25-40 | 5479 | 0.2218 | 0.1251 | +0.0966 ± 0.003 | 0.6378 | 0.3852 | 0.5258 | 0.2118 | 0.2192 | -0.059 ± 0.0046 | -0.01 (1) |
| 40+ | 3641 | 0.384 | 0.045 | +0.3390 ± 0.004 | 1.0006 | 0.1734 | 0.6333 | 0.104 | 0.0607 | -0.077 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 690 | 0.2072 | 0.2078 | -0.0007 ± 0.0006 | 0.5966 | 0.5985 | 0.5069 | 0.492 | 0.5246 | -0.096 ± 0.0188 | -0.01 (3) |
| 3-5 | 493 | 0.2178 | 0.2155 | +0.0023 ± 0.0017 | 0.6192 | 0.6149 | 0.5156 | 0.476 | 0.4625 | -0.125 ± 0.0224 | 0.02 (1) |
| 5-10 | 1095 | 0.208 | 0.206 | +0.0021 ± 0.0021 | 0.6025 | 0.5966 | 0.5406 | 0.4658 | 0.4913 | -0.096 ± 0.0142 | -0.01 (4) |
| 10-15 | 955 | 0.2148 | 0.2099 | +0.0050 ± 0.0037 | 0.6204 | 0.6068 | 0.5647 | 0.4404 | 0.4859 | -0.101 ± 0.0155 | -0.04 (5) |
| 15-25 | 1371 | 0.2299 | 0.2135 | +0.0164 ± 0.0049 | 0.6545 | 0.6116 | 0.5833 | 0.388 | 0.4457 | -0.097 ± 0.0127 | -0.0133 (9) |
| 25-40 | 961 | 0.2685 | 0.1992 | +0.0693 ± 0.009 | 0.7502 | 0.5794 | 0.6602 | 0.3461 | 0.3954 | -0.129 ± 0.0144 | -0.0075 (4) |
| 40+ | 356 | 0.3672 | 0.1647 | +0.2025 ± 0.0213 | 1.004 | 0.4966 | 0.7325 | 0.2473 | 0.2949 | -0.086 ± 0.0208 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4068 | 0.1918 | 0.1921 | -0.0003 ± 0.0002 | 0.5595 | 0.5599 | 0.5076 | 0.4926 | 0.5106 | -0.038 ± 0.0071 | -0.0133 (15) |
| 3-5 | 2786 | 0.1948 | 0.1937 | +0.0011 ± 0.0007 | 0.5658 | 0.5625 | 0.5114 | 0.4717 | 0.4763 | -0.047 ± 0.0085 | 0.02 (1) |
| 5-10 | 6070 | 0.1989 | 0.1954 | +0.0035 ± 0.0009 | 0.5831 | 0.5704 | 0.5095 | 0.4355 | 0.4517 | -0.042 ± 0.0057 | -0.0117 (6) |
| 10-15 | 5037 | 0.2033 | 0.1921 | +0.0112 ± 0.0015 | 0.5959 | 0.562 | 0.5119 | 0.3882 | 0.4058 | -0.049 ± 0.0063 | -0.0189 (18) |
| 15-25 | 7046 | 0.2168 | 0.1804 | +0.0363 ± 0.002 | 0.6307 | 0.53 | 0.5225 | 0.3274 | 0.3349 | -0.063 ± 0.0051 | -0.0086 (42) |
| 25-40 | 6416 | 0.2511 | 0.1365 | +0.1146 ± 0.0029 | 0.709 | 0.418 | 0.5581 | 0.2414 | 0.2224 | -0.084 ± 0.0046 | -0.0044 (18) |
| 40+ | 5056 | 0.4002 | 0.0586 | +0.3415 ± 0.0039 | 1.056 | 0.2114 | 0.6537 | 0.1179 | 0.0809 | -0.073 ± 0.0033 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 821 | 0.196 | 0.1981 | -0.0021 ± 0.0005 | 0.5715 | 0.5767 | 0.5025 | 0.4871 | 0.5469 | -0.039 ± 0.0163 | -0.0137 (8) |
| 3-5 | 587 | 0.2057 | 0.2037 | +0.0021 ± 0.0015 | 0.595 | 0.5889 | 0.4971 | 0.4575 | 0.4532 | -0.122 ± 0.0194 | 0.0067 (3) |
| 5-10 | 1302 | 0.2038 | 0.2013 | +0.0025 ± 0.0019 | 0.5933 | 0.5854 | 0.5116 | 0.4379 | 0.4562 | -0.101 ± 0.0129 | -0.0071 (7) |
| 10-15 | 1035 | 0.2091 | 0.2037 | +0.0054 ± 0.0035 | 0.6081 | 0.5908 | 0.5403 | 0.417 | 0.458 | -0.098 ± 0.014 | -0.0317 (6) |
| 15-25 | 1238 | 0.2356 | 0.2172 | +0.0183 ± 0.0052 | 0.6704 | 0.6197 | 0.5888 | 0.3946 | 0.4443 | -0.114 ± 0.0133 | -0.03 (1) |
| 25-40 | 770 | 0.2128 | 0.212 | +0.0008 ± 0.0097 | 0.6141 | 0.608 | 0.6625 | 0.3522 | 0.5039 | -0.059 ± 0.015 | 0.015 (2) |
| 40+ | 168 | 0.3002 | 0.1961 | +0.1040 ± 0.0301 | 0.8181 | 0.5732 | 0.7497 | 0.3001 | 0.4167 | -0.080 ± 0.0314 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4521 | 0.1843 | 0.185 | -0.0007 ± 0.0002 | 0.5423 | 0.5436 | 0.4824 | 0.4671 | 0.4886 | -0.030 ± 0.0065 | -0.0163 (35) |
| 3-5 | 3165 | 0.2025 | 0.2002 | +0.0023 ± 0.0006 | 0.5886 | 0.5813 | 0.4814 | 0.442 | 0.4335 | -0.064 ± 0.0081 | -0.0094 (18) |
| 5-10 | 6957 | 0.1944 | 0.19 | +0.0044 ± 0.0008 | 0.5718 | 0.5574 | 0.4877 | 0.4137 | 0.4213 | -0.051 ± 0.0053 | -0.01 (31) |
| 10-15 | 5582 | 0.1922 | 0.1791 | +0.0132 ± 0.0014 | 0.5688 | 0.5301 | 0.4957 | 0.3723 | 0.3798 | -0.056 ± 0.0057 | -0.015 (12) |
| 15-25 | 7171 | 0.2142 | 0.1742 | +0.0400 ± 0.0019 | 0.623 | 0.5127 | 0.5139 | 0.3194 | 0.3153 | -0.073 ± 0.0049 | -0.03 (2) |
| 25-40 | 5477 | 0.2165 | 0.1279 | +0.0885 ± 0.003 | 0.6262 | 0.3916 | 0.529 | 0.2134 | 0.233 | -0.049 ± 0.0047 | 0.01 (3) |
| 40+ | 3606 | 0.3935 | 0.0505 | +0.3430 ± 0.0042 | 1.0263 | 0.1876 | 0.6424 | 0.1107 | 0.0674 | -0.078 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1242 | 0.1951 | 0.1952 | -0.0001 ± 0.0004 | 0.5685 | 0.5685 | 0.5065 | 0.4914 | 0.496 | -0.069 ± 0.0128 | -0.0224 (49) |
| 3-5 | 875 | 0.1895 | 0.1891 | +0.0003 ± 0.0012 | 0.5556 | 0.5537 | 0.4966 | 0.4568 | 0.4709 | -0.061 ± 0.015 | -0.0194 (34) |
| 5-10 | 1825 | 0.2015 | 0.1969 | +0.0046 ± 0.0016 | 0.5915 | 0.5771 | 0.5034 | 0.4297 | 0.4356 | -0.076 ± 0.0106 | -0.005 (78) |
| 10-15 | 1241 | 0.2171 | 0.2039 | +0.0133 ± 0.0032 | 0.6268 | 0.5919 | 0.5394 | 0.4166 | 0.4222 | -0.092 ± 0.0132 | 0.0014 (64) |
| 15-25 | 1592 | 0.2317 | 0.2099 | +0.0218 ± 0.0045 | 0.6603 | 0.6044 | 0.5842 | 0.3893 | 0.434 | -0.086 ± 0.0116 | -0.0214 (59) |
| 25-40 | 990 | 0.2438 | 0.2109 | +0.0329 ± 0.0089 | 0.6969 | 0.6045 | 0.6848 | 0.3727 | 0.4768 | -0.094 ± 0.0137 | -0.0219 (26) |
| 40+ | 334 | 0.3367 | 0.2039 | +0.1328 ± 0.0238 | 0.9776 | 0.5933 | 0.8173 | 0.341 | 0.4551 | -0.103 ± 0.0225 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4679 | 0.1757 | 0.1759 | -0.0002 ± 0.0002 | 0.5206 | 0.5207 | 0.5105 | 0.4953 | 0.5076 | -0.037 ± 0.0062 | -0.0157 (88) |
| 3-5 | 3221 | 0.1947 | 0.1938 | +0.0010 ± 0.0006 | 0.5672 | 0.5651 | 0.5023 | 0.4626 | 0.4704 | -0.043 ± 0.0079 | -0.0209 (69) |
| 5-10 | 6594 | 0.1989 | 0.1924 | +0.0065 ± 0.0008 | 0.5843 | 0.5653 | 0.4999 | 0.4262 | 0.4205 | -0.063 ± 0.0055 | -0.0082 (132) |
| 10-15 | 4555 | 0.2116 | 0.1957 | +0.0159 ± 0.0016 | 0.614 | 0.5729 | 0.5371 | 0.4142 | 0.4097 | -0.070 ± 0.0066 | -0.0053 (105) |
| 15-25 | 5476 | 0.2302 | 0.2005 | +0.0297 ± 0.0024 | 0.662 | 0.5804 | 0.5718 | 0.3763 | 0.3996 | -0.064 ± 0.0061 | -0.0253 (107) |
| 25-40 | 3677 | 0.2602 | 0.1882 | +0.0721 ± 0.0045 | 0.7362 | 0.549 | 0.6368 | 0.3242 | 0.368 | -0.076 ± 0.007 | -0.0229 (51) |
| 40+ | 1579 | 0.3769 | 0.1569 | +0.2200 ± 0.0103 | 1.0679 | 0.4672 | 0.7433 | 0.2411 | 0.2837 | -0.070 ± 0.0095 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5921 | 1.016 ± 0.036 | 1.09 | 0.1687 | 0.1659 | 0.2153 | 0.2059 |
| gen2 | 5921 | 0.805 ± 0.033 | 1.06 | 0.1713 | 0.1663 | 0.2343 | 0.2058 |
| gen1_elo | 5921 | 0.993 ± 0.035 | 1.084 | 0.1754 | 0.166 | 0.2144 | 0.2061 |
| gen1_sr | 5921 | 0.99 ± 0.043 | 1.119 | 0.1316 | 0.1682 | 0.2303 | 0.2055 |
| gen1_ledger | 8099 | 0.854 ± 0.026 | 1.06 | 0.1876 | 0.1753 | 0.2183 | 0.2014 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 29,172)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,599 | 22.6% |
| STALE_QUOTE | market_freshness | 6,445 | 22.1% |
| BOOK_QUALITY | execution | 5,467 | 18.7% |
| POOR_DATA | data | 3,384 | 11.6% |
| LIMITED_DATA | data | 1,819 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,673 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,242 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 1,203 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 840 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 499 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.6%, market_freshness 22.1%, execution 18.7%, data 17.8%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.3%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.4%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 44.7%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 24.8%, MODEL_HIGH_UNCERTAINTY 18.4%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.4%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.6%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 15,592)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,327 | 34.2% |
| STALE_QUOTE | market_freshness | 2,921 | 18.7% |
| BOOK_QUALITY | execution | 2,851 | 18.3% |
| POOR_DATA | data | 1,449 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 880 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 651 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 545 | 3.5% |
| LIMITED_DATA | data | 536 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 307 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 124 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.2%, market_freshness 18.7%, execution 18.3%, data 12.7%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 62.1%, STALE_KALSHI_QUOTE 52.5%, STALE_PLAYER_DATA 46.1%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 24.3%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.1%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.2%, POST_SETTLEMENT_OBSERVATION 34.2%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12397, "IDENTITY_AMBIGUOUS": 3195}; ticker orientation: {"VERIFIED": 15592}.

Checks: discipline:AMBIGUOUS 1049, discipline:PASS 14543, identity_confidence:AMBIGUOUS 2871, identity_confidence:PASS 12721, level_mapping:NA 1061, level_mapping:PASS 14531, market_pair:AMBIGUOUS 483, market_pair:NA 352, market_pair:PASS 14757, model_complement:NA 315, model_complement:PASS 15277, namesake:AMBIGUOUS 6, namesake:PASS 15586, physical_match_id:NA 5417, physical_match_id:PASS 10175, player_ids:PASS 15592, same_pair_other_event:PASS 15592, ticker_orientation:PASS 15592

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,730 | 4.0% | 3.5% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.77 | 0.2217 / 0.2167 (687) | 22.7% | 2.7% | 3.1% | 2.7% |
| CHALLENGER | 10,155 | 16.5% | 6.2% | 10.7% | {"coverage": 990, "market_freshness/coverage": 200, "market_freshness": 173, "data": 147, "model_calibration_or_unknown": 74, "execution": 38, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.24 | 0.2214 / 0.2118 (2325) | 35.8% | 15.5% | 4.1% | 22.6% |
| DOUBLES | 2,221 | 47.2% | 47.1% | 6.7% | {"execution": 590, "mapping": 285, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.62 | 0.307 / 0.2392 (538) | 10.5% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 20,222 | 25.0% | 17.5% | 32.5% | {"coverage": 1799, "market_freshness": 928, "execution": 915, "data": 739, "market_freshness/coverage": 488, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.66 | 0.2165 / 0.2 (4173) | 38.2% | 68.9% | 16.2% | 21.8% |
| ITF_WOMEN | 26,583 | 26.6% | 19.1% | 45.4% | {"coverage": 2475, "market_freshness": 1497, "execution": 1230, "data": 1001, "market_freshness/coverage": 605, "mapping": 160, "model_calibration_or_unknown": 82, "model_calibration": 21} | 12.54 | 0.2046 / 0.1954 (4904) | 39.9% | 56.9% | 9.9% | 21.5% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,189 | 5.8% | 4.9% | 1.6% | {"market_freshness": 85, "model_calibration_or_unknown": 43, "coverage": 30, "execution": 28, "data": 24, "model_calibration": 18, "market_freshness/coverage": 12, "mapping": 1} | 7.44 | 0.2304 / 0.2244 (661) | 27.4% | 1.7% | 1.4% | 3.5% |
| WTA125 | 2,321 | 11.1% | 9.5% | 1.7% | {"market_freshness": 74, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 16, "coverage": 12, "mapping": 4} | 9.17 | 0.2116 / 0.1932 (690) | 26.7% | 10.6% | 4.6% | 7.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 286 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 164 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 547 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT31KUHDEK-KUH` | ITF_WOMEN | fair_v1 | 84% / 6% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 773 min (STALE); data LIMITED (grade C, thinner serve sample 1253.0, ratio 1.41); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.97, "by_level_share_of_ge_25pp": {"ATP": 0.0146, "CHALLENGER": 0.1074, "DOUBLES": 0.0673, "ITF_MEN": 0.3245, "ITF_WOMEN": 0.4535, "OTHER": 0.0008, "WTA": 0.0155, "WTA125": 0.0165}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5246, "share_primary_cause_market_settled_or_in_play": 0.433, "share_primary_cause_stale_quote_only": 0.1873}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15592, "identity_ambiguous_share": 0.2049, "ticker_orientation": {"VERIFIED": 15592}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10175, "with_external": 533, "coverage": 0.0524, "external_status": {"EXTERNAL_STALE": 329, "AGREES_WITH_KALSHI": 191, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 329, "MODEL_LONE_OUTLIER": 191, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3583, "share_external_supports_model": 0.0244}, "pregame_clean_ge_25pp": {"n": 4807, "with_external": 506, "coverage": 0.1053, "external_status": {"EXTERNAL_STALE": 309, "AGREES_WITH_KALSHI": 184, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 309, "MODEL_LONE_OUTLIER": 184, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3636, "share_external_supports_model": 0.0257}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 484.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 237.0, "share_severe_asymmetry": 0.2082, "data_status": {"POOR": 8772, "LIMITED": 4078, "ADEQUATE": 2742}, "comparison_lt_10pp": {"median_thinner_serve_points": 1736.0, "median_sample_ratio": 1.7, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1186, "model_minus_observed": 0.0561, "kalshi_minus_observed": -0.0819, "brier_diff_model_minus_kalshi": -0.0016}, "4-10x": {"n": 816, "model_minus_observed": 0.0861, "kalshi_minus_observed": -0.06, "brier_diff_model_minus_kalshi": 0.0081}, "<2x": {"n": 2908, "model_minus_observed": 0.0934, "kalshi_minus_observed": -0.0286, "brier_diff_model_minus_kalshi": 0.0125}, ">=10x": {"n": 1011, "model_minus_observed": 0.1178, "kalshi_minus_observed": -0.0574, "brier_diff_model_minus_kalshi": 0.0143}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5921, "model": {"intercept": -0.528, "slope": 0.805, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.195, "slope": 1.06, "slope_se": 0.037}, "mean_extremity_model": 0.1713, "mean_extremity_kalshi": 0.1663, "model_brier": 0.2343, "kalshi_brier": 0.2058, "brier_diff_model_minus_kalshi": 0.0285, "brier_diff_se": 0.0025, "model_logloss": 0.6662, "kalshi_logloss": 0.5947}, "fair_v1": {"n": 5921, "model": {"intercept": -0.424, "slope": 1.016, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.264, "slope": 1.09, "slope_se": 0.037}, "mean_extremity_model": 0.1687, "mean_extremity_kalshi": 0.1659, "model_brier": 0.2153, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0094, "brier_diff_se": 0.002, "model_logloss": 0.6199, "kalshi_logloss": 0.5949}, "gen1_elo": {"n": 5921, "model": {"intercept": -0.405, "slope": 0.993, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.279, "slope": 1.084, "slope_se": 0.037}, "mean_extremity_model": 0.1754, "mean_extremity_kalshi": 0.166, "model_brier": 0.2144, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.002, "model_logloss": 0.6182, "kalshi_logloss": 0.5953}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2478, "share_ge_15": 0.4422, "median_abs_gap": 13.0, "n": 41068}, "gen1_elo": {"share_ge_25": 0.246, "share_ge_15": 0.4409, "median_abs_gap": 12.92, "n": 41068}, "gen1_sr": {"share_ge_25": 0.3125, "share_ge_15": 0.5186, "median_abs_gap": 15.77, "n": 41068}, "gen2": {"share_ge_25": 0.3151, "share_ge_15": 0.5087, "median_abs_gap": 15.41, "n": 41068}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1515, "share_ge_15": 0.353, "median_abs_gap": 10.65, "n": 31715}, "gen1_elo": {"share_ge_25": 0.1514, "share_ge_15": 0.3508, "median_abs_gap": 10.51, "n": 31714}, "gen1_sr": {"share_ge_25": 0.2156, "share_ge_15": 0.4379, "median_abs_gap": 12.95, "n": 31717}, "gen2": {"share_ge_25": 0.2318, "share_ge_15": 0.4379, "median_abs_gap": 12.8, "n": 31717}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.77, "share_ge_25_all": 0.0396, "share_ge_25_pregame_clean": 0.0353}, "WTA": {"median_abs_gap_pregame_clean": 7.44, "share_ge_25_all": 0.0575, "share_ge_25_pregame_clean": 0.0492}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2373, "share_within_10pp_all": 0.4396, "share_within_10pp_pregame_clean": 0.4928, "corr_model_vs_mid_pregame_clean": 0.8504}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 872, "model_brier": 0.2005, "kalshi_brier": 0.2009, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1030, "model_brier": 0.2201, "kalshi_brier": 0.2112, "brier_diff_model_minus_kalshi": 0.0089}, "15-25": {"n_settled": 1302, "model_brier": 0.2257, "kalshi_brier": 0.2118, "brier_diff_model_minus_kalshi": 0.0139}, "25-40": {"n_settled": 756, "model_brier": 0.2235, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0174}, "3-5": {"n_settled": 543, "model_brier": 0.2053, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0}, "40+": {"n_settled": 159, "model_brier": 0.2822, "kalshi_brier": 0.1885, "brier_diff_model_minus_kalshi": 0.0938}, "5-10": {"n_settled": 1259, "model_brier": 0.2021, "kalshi_brier": 0.2015, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.528, "slope": 0.805, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.195, "slope": 1.06, "slope_se": 0.037}, "n": 5921}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.486, "slope": 0.854, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.164, "slope": 1.06, "slope_se": 0.031}, "n": 8099}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 538, "model_brier": 0.307, "kalshi_brier": 0.2392, "brier_diff_model_minus_kalshi": 0.0677, "brier_diff_se": 0.0129, "corr_model_outcome": 0.0537, "corr_kalshi_outcome": 0.2246}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
