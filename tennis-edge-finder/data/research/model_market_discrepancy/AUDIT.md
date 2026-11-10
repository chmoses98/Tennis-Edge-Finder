# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-10T08:24Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 84,845): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.2%, 15-25 19.1%, 25-40 13.6%, 40+ 8.2%; median gap 11.83 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 11.1%, doubles 6.6%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 18,491): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.3%, STALE_QUOTE 20.0%, BOOK_QUALITY 17.1%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.3%, market_freshness 20.0%, execution 17.1%, data 12.6%, market_freshness/coverage 9.1%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 54.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 18,491 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.0% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 485.0 points vs 1732.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.03, Gen-2 0.821, Gen-1 ledger 0.869 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 938 model 0.2238 vs Kalshi 0.2056; n 191 model 0.296 vs Kalshi 0.1751.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 357,937 model-market comparisons (587,996 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 118,776 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-10T08:06:29.740841+00:00'], shadow board 97,741 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-10T08:06:33.623042+00:00'], Model 4 43,483 rows, 29,583 settled tickers, 11,204 tickers with an external scan.
* By model: {"gen1_ledger": 79915, "gen1_elo": 49122, "fair_v1": 49122, "gen2": 49122, "gen1_sr": 49122, "model4_fundamental": 40809, "model4_conditioned": 40725}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 84,845 | 14.1 | 9.6 | 20.2 | 15.2 | 19.1 | 13.6 | 8.2 | 11.83 | 40.9% | 21.8% |
| MW fair_v1 | 49,122 | 12.8 | 8.6 | 18.8 | 15.3 | 19.6 | 14.8 | 10.1 | 13.05 | 44.5% | 24.9% |
| MW gen1_elo | 49,122 | 12.6 | 8.8 | 19.2 | 15.3 | 19.4 | 14.7 | 9.9 | 12.84 | 44.0% | 24.6% |
| MW gen1_ledger | 35,723 | 15.8 | 10.9 | 22.1 | 15.1 | 18.5 | 11.9 | 5.6 | 10.26 | 36.0% | 17.5% |
| MW gen1_sr | 49,122 | 10.0 | 7.2 | 16.7 | 13.9 | 20.7 | 18.7 | 12.7 | 15.84 | 52.1% | 31.3% |
| MW gen2 | 49,122 | 11.0 | 7.6 | 16.7 | 13.7 | 19.6 | 17.7 | 13.7 | 15.46 | 51.0% | 31.4% |
| all families model4_conditioned | 40,725 | 22.2 | 17.9 | 34.4 | 17.0 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 40,809 | 17.3 | 13.5 | 34.0 | 20.0 | 9.9 | 3.8 | 1.5 | 7.62 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.9%, >=20pp 30.1%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.41pp; >=10pp 45.1%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,057 | 28.1 | 15.7 | 27.9 | 13.3 | 10.7 | 3.6 | 0.6 | 5.84 | 14.9% | 4.2% |
| CHALLENGER | 7,736 | 16.2 | 9.7 | 20.7 | 15.3 | 16.1 | 11.2 | 10.9 | 10.89 | 38.1% | 22.1% |
| ITF_MEN | 13,893 | 9.8 | 7.3 | 17.1 | 15.0 | 21.1 | 17.3 | 12.6 | 15.39 | 50.9% | 29.9% |
| ITF_WOMEN | 19,029 | 9.6 | 7.0 | 16.0 | 14.8 | 22.2 | 18.4 | 11.9 | 15.92 | 52.6% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,074 | 16.7 | 13.1 | 25.1 | 20.8 | 16.5 | 6.8 | 1.1 | 8.64 | 24.4% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,057 | 26.6 | 15.6 | 26.2 | 15.8 | 11.3 | 3.9 | 0.8 | 6.09 | 16.0% | 4.7% |
| CHALLENGER | 7,736 | 14.4 | 9.2 | 19.1 | 13.8 | 18.6 | 13.4 | 11.5 | 12.49 | 43.5% | 24.9% |
| ITF_MEN | 13,893 | 8.1 | 6.2 | 15.0 | 13.7 | 20.0 | 20.5 | 16.5 | 18.0 | 57.0% | 37.0% |
| ITF_WOMEN | 19,029 | 7.9 | 5.8 | 14.1 | 12.7 | 20.7 | 21.2 | 17.5 | 19.07 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,074 | 14.1 | 10.3 | 21.7 | 16.3 | 22.4 | 12.8 | 2.5 | 11.21 | 37.7% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,057 | 23.1 | 14.1 | 25.6 | 15.5 | 14.5 | 6.0 | 1.1 | 7.1 | 21.7% | 7.1% |
| CHALLENGER | 7,736 | 15.2 | 9.8 | 20.6 | 15.8 | 16.0 | 11.9 | 10.8 | 11.2 | 38.7% | 22.7% |
| ITF_MEN | 13,893 | 9.5 | 7.3 | 17.2 | 14.2 | 21.7 | 17.3 | 12.9 | 15.75 | 51.9% | 30.2% |
| ITF_WOMEN | 19,029 | 9.3 | 6.9 | 16.3 | 15.7 | 22.2 | 18.4 | 11.3 | 15.58 | 51.8% | 29.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,074 | 22.6 | 17.0 | 31.9 | 15.3 | 8.8 | 3.2 | 1.0 | 6.12 | 13.1% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,437 | 27.9 | 19.5 | 29.3 | 12.3 | 8.0 | 2.5 | 0.5 | 5.27 | 11.0% | 3.0% |
| CHALLENGER | 4,834 | 22.8 | 14.5 | 27.7 | 14.7 | 13.3 | 5.6 | 1.6 | 7.03 | 20.4% | 7.1% |
| DOUBLES | 2,627 | 4.8 | 4.5 | 12.8 | 10.9 | 20.6 | 24.5 | 21.9 | 23.23 | 67.0% | 46.4% |
| ITF_MEN | 10,269 | 12.8 | 9.6 | 21.3 | 15.6 | 21.8 | 13.0 | 6.0 | 11.85 | 40.8% | 19.0% |
| ITF_WOMEN | 12,346 | 13.4 | 9.3 | 19.9 | 15.8 | 21.5 | 14.7 | 5.5 | 12.23 | 41.7% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,805 | 23.7 | 16.1 | 31.6 | 16.9 | 8.9 | 2.5 | 0.2 | 6.57 | 11.7% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,932 | 28.6 | 15.9 | 28.4 | 13.3 | 10.4 | 3.1 | 0.3 | 5.67 | 13.8% | 3.4% |
| CHALLENGER | 5,499 | 20.9 | 12.0 | 25.6 | 18.0 | 16.1 | 5.9 | 1.6 | 8.24 | 23.6% | 7.5% |
| ITF_MEN | 10,163 | 11.9 | 8.6 | 20.6 | 17.2 | 22.0 | 14.3 | 5.5 | 12.48 | 41.7% | 19.8% |
| ITF_WOMEN | 13,997 | 11.4 | 8.5 | 18.9 | 17.0 | 24.1 | 15.2 | 4.8 | 13.16 | 44.1% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,960 | 17.0 | 13.1 | 25.4 | 21.1 | 16.5 | 6.2 | 0.6 | 8.45 | 23.3% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,932 | 26.9 | 15.9 | 26.5 | 15.7 | 11.2 | 3.4 | 0.4 | 6.0 | 15.0% | 3.8% |
| CHALLENGER | 5,499 | 18.1 | 11.7 | 23.8 | 16.1 | 19.1 | 9.4 | 1.8 | 8.99 | 30.3% | 11.2% |
| ITF_MEN | 10,164 | 9.6 | 7.3 | 17.5 | 15.8 | 21.9 | 18.6 | 9.3 | 14.94 | 49.8% | 27.9% |
| ITF_WOMEN | 13,998 | 8.9 | 6.9 | 15.9 | 14.3 | 22.6 | 20.6 | 10.7 | 16.54 | 53.9% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,960 | 14.3 | 10.4 | 21.9 | 16.4 | 22.6 | 12.5 | 1.9 | 11.03 | 36.9% | 14.4% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,371 | 28.1 | 19.7 | 29.3 | 12.5 | 7.7 | 2.4 | 0.3 | 5.23 | 10.4% | 2.7% |
| CHALLENGER | 4,280 | 24.1 | 15.3 | 28.8 | 14.8 | 12.6 | 3.9 | 0.4 | 6.58 | 16.9% | 4.3% |
| DOUBLES | 2,462 | 4.7 | 4.5 | 13.0 | 11.0 | 20.4 | 24.4 | 21.9 | 23.2 | 66.8% | 46.3% |
| ITF_MEN | 8,861 | 13.6 | 10.2 | 22.8 | 16.1 | 21.9 | 11.5 | 4.1 | 10.99 | 37.4% | 15.6% |
| ITF_WOMEN | 10,621 | 14.1 | 9.8 | 20.9 | 16.3 | 21.6 | 13.7 | 3.7 | 11.44 | 39.0% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,742 | 24.1 | 16.5 | 31.6 | 16.9 | 8.9 | 2.0 | 0.1 | 6.43 | 11.0% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,627 | 4.8 | 4.5 | 12.8 | 10.9 | 20.6 | 24.5 | 21.9 | 23.23 | 67.0% | 46.4% |
| singles | 33,096 | 16.7 | 11.4 | 22.9 | 15.5 | 18.3 | 10.9 | 4.3 | 9.74 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 10,200 | 12.8 | 9.0 | 19.8 | 15.4 | 19.7 | 14.0 | 9.4 | 12.65 | 43.1% | 23.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 32,085 | 13.3 | 8.7 | 18.9 | 15.1 | 19.1 | 14.8 | 10.1 | 12.89 | 44.0% | 24.9% |
| UNKNOWN | 6,424 | 10.5 | 7.5 | 17.0 | 16.4 | 21.4 | 16.0 | 11.2 | 14.39 | 48.6% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,989 | 19.3 | 11.8 | 22.5 | 15.9 | 14.9 | 9.1 | 6.3 | 8.91 | 30.4% | 15.5% |
| B | 5,994 | 12.8 | 8.5 | 19.6 | 15.5 | 19.7 | 12.7 | 11.2 | 12.81 | 43.6% | 23.9% |
| C | 6,948 | 12.0 | 8.8 | 19.6 | 15.6 | 18.6 | 14.6 | 10.8 | 12.89 | 44.0% | 25.4% |
| D | 7,869 | 11.8 | 8.4 | 17.8 | 15.2 | 21.7 | 15.8 | 9.3 | 13.85 | 46.8% | 25.1% |
| F | 14,322 | 7.4 | 5.5 | 14.9 | 14.6 | 23.3 | 20.9 | 13.3 | 17.91 | 57.5% | 34.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,598 | 24.8 | 16.0 | 28.9 | 15.0 | 10.6 | 3.4 | 1.2 | 6.34 | 15.2% | 4.6% |
| B | 4,948 | 16.6 | 10.8 | 24.4 | 16.9 | 18.8 | 9.5 | 3.0 | 9.59 | 31.3% | 12.5% |
| C | 6,987 | 10.9 | 7.7 | 19.6 | 14.7 | 21.1 | 15.6 | 10.3 | 13.6 | 47.0% | 25.9% |
| D | 5,308 | 14.5 | 10.1 | 21.2 | 15.3 | 21.0 | 12.6 | 5.4 | 11.26 | 39.0% | 18.0% |
| F | 8,882 | 10.3 | 8.4 | 16.1 | 14.6 | 23.4 | 19.2 | 8.0 | 15.34 | 50.7% | 27.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,825 | 17.7 | 10.8 | 21.6 | 15.7 | 15.3 | 10.0 | 9.0 | 9.99 | 34.3% | 19.0% |
| LIMITED | 10,714 | 13.6 | 9.6 | 20.5 | 15.8 | 19.4 | 13.3 | 7.7 | 11.88 | 40.5% | 21.1% |
| POOR | 22,583 | 9.0 | 6.6 | 16.0 | 14.8 | 22.6 | 19.0 | 11.9 | 16.21 | 53.5% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,107 | 23.7 | 18.1 | 33.0 | 15.5 | 6.4 | 2.9 | 0.4 | 5.9 | 9.7% | 3.3% |
| GAME_SPREAD | 6,823 | 22.9 | 15.3 | 32.1 | 16.8 | 9.0 | 3.3 | 0.6 | 6.68 | 12.9% | 4.0% |
| MATCH_WINNER | 35,723 | 15.8 | 10.9 | 22.1 | 15.1 | 18.5 | 11.9 | 5.6 | 10.26 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,802 | 28.2 | 16.8 | 30.8 | 12.6 | 8.9 | 2.4 | 0.3 | 5.58 | 11.6% | 2.7% |
| TOTAL_GAMES | 11,436 | 9.8 | 10.8 | 36.0 | 25.9 | 10.5 | 4.2 | 2.9 | 9.17 | 17.6% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,481 | 24.4 | 28.7 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.8 | 5.4% | 1.4% |
| GAME_SPREAD | 9,407 | 46.9 | 15.9 | 25.0 | 7.4 | 2.3 | 1.9 | 0.6 | 3.3 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,837 | 6.6 | 9.8 | 40.6 | 30.0 | 7.3 | 3.3 | 2.4 | 9.18 | 13.0% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,517 | 23.8 | 16.6 | 34.7 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.1% | 3.2% |
| GAME_SPREAD | 9,416 | 20.5 | 13.5 | 28.4 | 20.2 | 12.0 | 4.3 | 1.1 | 7.64 | 17.5% | 5.5% |
| TOTAL_GAMES | 16,876 | 10.0 | 10.8 | 36.5 | 24.3 | 11.4 | 4.4 | 2.6 | 9.03 | 18.4% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 49,122 | 44.5% | 24.9% | 13.05 | 35.4% | 15.2% | 10.67 |
| gen1_elo | 49,122 | 44.0% | 24.6% | 12.84 | 34.8% | 14.9% | 10.49 |
| gen1_sr | 49,122 | 52.1% | 31.3% | 15.84 | 43.9% | 21.6% | 12.97 |
| gen2 | 49,122 | 51.0% | 31.4% | 15.46 | 43.9% | 23.1% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,098 | 15.5 | 10.4 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 29,024 | 10.9 | 7.3 | 17.0 | 13.9 | 19.2 | 16.9 | 14.7 | 15.32 | 50.8% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 29,191 | 16.4 | 11.2 | 22.7 | 15.2 | 18.1 | 11.4 | 5.0 | 9.91 | 34.5% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 84,845 | 29191 | 23570 | 32084 | 24.9 | 129.6 | 1451.1 |
| ge_15pp | 34,712 | 10062 | 8394 | 16256 | 28.6 | 437.7 | 1451.1 |
| ge_25pp | 18,491 | 4788 | 3666 | 10037 | 34.3 | 584.1 | 1431.1 |
| lt_10pp | 37,212 | 14687 | 11149 | 11376 | 22.7 | 48.5 | 1421.7 |

Current slate `SL-20261110T082431Z-f5656424`: 638 priced rows, quote age at build {'median': 18.5, 'max': 18.5}, freshness {'AGING': 638}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 51 | 0.0 | 0.0 | 35.3 | 9.8 | 31.4 | 19.6 | 3.9 | 18.34 | 54.9% | 23.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,846 | 19.4 | 11.1 | 25.5 | 18.0 | 17.8 | 7.3 | 0.9 | 8.75 | 26.0% | 8.2% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,023 | 66.9 | 33.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.16 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,208 | 0.0 | 2.2 | 38.1 | 26.1 | 23.8 | 8.9 | 0.9 | 11.68 | 33.6% | 9.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 49,122 | 8189 (16.7%) | 27.0% | 1.0% | {"EXTERNAL_STALE": 4846, "AGREES_WITH_KALSHI": 2208, "ALL_AGREE": 1023, "SUPPORTS_MODEL_DIRECTION": 49, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 21,851 | 2033 (9.3%) | 36.5% | 1.5% | {"EXTERNAL_STALE": 1261, "AGREES_WITH_KALSHI": 742, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 12,241 | 628 (5.1%) | 34.5% | 2.1% | {"EXTERNAL_STALE": 398, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,733 | 597 (10.4%) | 35.2% | 2.2% | {"EXTERNAL_STALE": 374, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 19,756 | 4699 (23.8%) | 18.9% | 1.0% | {"EXTERNAL_STALE": 2711, "ALL_AGREE": 1023, "AGREES_WITH_KALSHI": 890, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,605 | 10.7 | 7.7 | 19.2 | 14.5 | 21.5 | 16.3 | 10.2 | 14.13 | 48.0% | 26.5% |
| 4-10x | 6,535 | 11.2 | 8.5 | 18.2 | 15.1 | 21.9 | 14.8 | 10.4 | 13.94 | 47.1% | 25.2% |
| <2x | 25,174 | 14.8 | 9.7 | 19.9 | 16.0 | 17.6 | 13.0 | 9.0 | 11.55 | 39.6% | 22.0% |
| >=10x | 7,808 | 10.4 | 6.4 | 15.0 | 14.3 | 21.7 | 18.9 | 13.2 | 16.44 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,930 | 12.5 | 8.6 | 19.8 | 16.2 | 19.1 | 13.5 | 10.4 | 12.71 | 43.0% | 23.9% |
| 300-1000 | 10,518 | 11.8 | 8.8 | 17.7 | 15.0 | 20.7 | 16.4 | 9.6 | 13.76 | 46.7% | 26.0% |
| <300 | 15,442 | 8.3 | 5.8 | 15.2 | 14.7 | 22.9 | 20.0 | 13.2 | 17.23 | 56.1% | 33.2% |
| >=3000 | 10,232 | 21.1 | 12.8 | 24.1 | 15.5 | 14.0 | 7.3 | 5.2 | 7.82 | 26.5% | 12.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1496 | 0.5497 | 0.4106 | 0.4833 | +0.066 | -0.073 | 0.0025 ± 0.004 |
| ratio 4-10x | 1009 | 0.5776 | 0.433 | 0.4876 | +0.090 | -0.055 | 0.0091 ± 0.005 |
| ratio <2x | 3676 | 0.5361 | 0.4137 | 0.4374 | +0.099 | -0.024 | 0.0142 ± 0.0024 |
| ratio >=10x | 1240 | 0.5663 | 0.3931 | 0.4452 | +0.121 | -0.052 | 0.0152 ± 0.0051 |
| thinner_sample 1000-3000 | 2069 | 0.5398 | 0.4125 | 0.4471 | +0.093 | -0.035 | 0.0115 ± 0.0032 |
| thinner_sample 300-1000 | 1664 | 0.5656 | 0.4255 | 0.4766 | +0.089 | -0.051 | 0.0046 ± 0.0038 |
| thinner_sample <300 | 2388 | 0.5582 | 0.3906 | 0.4518 | +0.106 | -0.061 | 0.0137 ± 0.0036 |
| thinner_sample >=3000 | 1300 | 0.5286 | 0.4348 | 0.4446 | +0.084 | -0.010 | 0.0153 ± 0.0032 |
| data_status ADEQUATE | 2081 | 0.5317 | 0.4288 | 0.4387 | +0.093 | -0.010 | 0.0156 ± 0.0027 |
| data_status LIMITED | 1818 | 0.5489 | 0.4158 | 0.467 | +0.082 | -0.051 | 0.0073 ± 0.0035 |
| data_status POOR | 3522 | 0.5605 | 0.4006 | 0.458 | +0.102 | -0.057 | 0.0109 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1070 | 0.1973 | 0.1976 | -0.0003 ± 0.0005 | 0.5744 | 0.5752 | 0.5036 | 0.4885 | 0.5019 | -0.093 ± 0.0144 | -0.0087 (8) |
| 3-5 | 683 | 0.2064 | 0.2059 | +0.0006 ± 0.0014 | 0.5977 | 0.5948 | 0.504 | 0.4643 | 0.4773 | -0.101 ± 0.0179 | 0.01 (3) |
| 5-10 | 1602 | 0.2034 | 0.202 | +0.0014 ± 0.0017 | 0.5934 | 0.5879 | 0.5122 | 0.4384 | 0.4638 | -0.093 ± 0.0116 | -0.0143 (7) |
| 10-15 | 1290 | 0.2183 | 0.2092 | +0.0092 ± 0.0032 | 0.6283 | 0.602 | 0.5244 | 0.401 | 0.4248 | -0.106 ± 0.013 | -0.055 (6) |
| 15-25 | 1647 | 0.2258 | 0.2079 | +0.0179 ± 0.0044 | 0.6466 | 0.5991 | 0.5758 | 0.3811 | 0.4323 | -0.105 ± 0.0113 | -0.0045 (11) |
| 25-40 | 938 | 0.2238 | 0.2056 | +0.0182 ± 0.0088 | 0.6375 | 0.5921 | 0.6506 | 0.341 | 0.4659 | -0.068 ± 0.0136 | -0.06 (2) |
| 40+ | 191 | 0.296 | 0.1751 | +0.1210 ± 0.0272 | 0.7965 | 0.5226 | 0.7305 | 0.2751 | 0.377 | -0.082 ± 0.0262 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5560 | 0.1852 | 0.1861 | -0.0009 ± 0.0002 | 0.5463 | 0.5475 | 0.491 | 0.4757 | 0.5086 | -0.019 ± 0.0059 | -0.01 (28) |
| 3-5 | 3691 | 0.1982 | 0.1963 | +0.0019 ± 0.0006 | 0.5771 | 0.5703 | 0.4829 | 0.4431 | 0.4389 | -0.059 ± 0.0074 | 0.005 (6) |
| 5-10 | 8115 | 0.2012 | 0.1974 | +0.0037 ± 0.0007 | 0.588 | 0.5758 | 0.4843 | 0.4106 | 0.4224 | -0.046 ± 0.005 | -0.0114 (22) |
| 10-15 | 6647 | 0.2019 | 0.1858 | +0.0161 ± 0.0013 | 0.5905 | 0.5455 | 0.4854 | 0.3616 | 0.3591 | -0.064 ± 0.0053 | -0.0379 (19) |
| 15-25 | 8426 | 0.2065 | 0.1668 | +0.0397 ± 0.0017 | 0.6049 | 0.4959 | 0.4999 | 0.3044 | 0.3016 | -0.070 ± 0.0044 | -0.0043 (51) |
| 25-40 | 6547 | 0.2238 | 0.1255 | +0.0983 ± 0.0027 | 0.6419 | 0.3862 | 0.5269 | 0.2132 | 0.2174 | -0.060 ± 0.0042 | -0.0733 (3) |
| 40+ | 4429 | 0.3814 | 0.0435 | +0.3379 ± 0.0036 | 0.993 | 0.1692 | 0.6298 | 0.1007 | 0.0576 | -0.075 ± 0.003 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 862 | 0.2057 | 0.2061 | -0.0004 ± 0.0005 | 0.5922 | 0.5935 | 0.5056 | 0.4908 | 0.5162 | -0.099 ± 0.0166 | -0.0117 (6) |
| 3-5 | 611 | 0.2111 | 0.208 | +0.0031 ± 0.0015 | 0.6051 | 0.5985 | 0.5149 | 0.4754 | 0.4517 | -0.134 ± 0.0199 | 0.01 (3) |
| 5-10 | 1371 | 0.2074 | 0.2058 | +0.0016 ± 0.0018 | 0.6012 | 0.5967 | 0.5403 | 0.4658 | 0.4945 | -0.086 ± 0.0126 | -0.01 (4) |
| 10-15 | 1197 | 0.2137 | 0.2062 | +0.0076 ± 0.0033 | 0.6201 | 0.598 | 0.5612 | 0.4368 | 0.4712 | -0.105 ± 0.0137 | -0.04 (5) |
| 15-25 | 1734 | 0.2318 | 0.2119 | +0.0199 ± 0.0043 | 0.6594 | 0.6082 | 0.5857 | 0.39 | 0.4383 | -0.102 ± 0.0113 | -0.0183 (12) |
| 25-40 | 1217 | 0.2676 | 0.1992 | +0.0684 ± 0.008 | 0.746 | 0.5787 | 0.6609 | 0.347 | 0.3969 | -0.118 ± 0.0128 | -0.008 (5) |
| 40+ | 429 | 0.3712 | 0.1622 | +0.2089 ± 0.0194 | 1.0114 | 0.4905 | 0.7358 | 0.2473 | 0.2914 | -0.088 ± 0.0186 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4763 | 0.1917 | 0.1918 | -0.0002 ± 0.0002 | 0.559 | 0.5591 | 0.5063 | 0.4912 | 0.5062 | -0.040 ± 0.0065 | -0.0154 (26) |
| 3-5 | 3253 | 0.1926 | 0.1914 | +0.0012 ± 0.0006 | 0.5618 | 0.5581 | 0.5125 | 0.4729 | 0.4765 | -0.048 ± 0.0079 | 0.01 (5) |
| 5-10 | 7214 | 0.1967 | 0.1935 | +0.0032 ± 0.0008 | 0.5782 | 0.5661 | 0.5086 | 0.4345 | 0.4522 | -0.039 ± 0.0052 | -0.0117 (6) |
| 10-15 | 5984 | 0.2027 | 0.1905 | +0.0122 ± 0.0014 | 0.5947 | 0.5577 | 0.5092 | 0.3853 | 0.3989 | -0.051 ± 0.0057 | -0.0189 (18) |
| 15-25 | 8494 | 0.2168 | 0.1805 | +0.0364 ± 0.0018 | 0.6305 | 0.5298 | 0.5255 | 0.3299 | 0.3372 | -0.061 ± 0.0046 | -0.014 (52) |
| 25-40 | 7682 | 0.2516 | 0.1376 | +0.1139 ± 0.0027 | 0.7101 | 0.4203 | 0.5613 | 0.2441 | 0.2268 | -0.080 ± 0.0042 | -0.0095 (20) |
| 40+ | 6025 | 0.4022 | 0.0584 | +0.3439 ± 0.0036 | 1.0592 | 0.2107 | 0.6546 | 0.118 | 0.0793 | -0.074 ± 0.003 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1049 | 0.1956 | 0.1969 | -0.0012 ± 0.0005 | 0.5706 | 0.5736 | 0.5023 | 0.4868 | 0.5281 | -0.056 ± 0.0143 | -0.0191 (11) |
| 3-5 | 747 | 0.2075 | 0.2057 | +0.0018 ± 0.0013 | 0.6017 | 0.5957 | 0.4992 | 0.4596 | 0.4592 | -0.115 ± 0.0174 | 0.002 (5) |
| 5-10 | 1623 | 0.2039 | 0.2 | +0.0039 ± 0.0017 | 0.5931 | 0.5823 | 0.513 | 0.4393 | 0.4486 | -0.107 ± 0.0115 | -0.01 (10) |
| 10-15 | 1309 | 0.212 | 0.2031 | +0.0089 ± 0.0031 | 0.6143 | 0.589 | 0.5387 | 0.4155 | 0.4431 | -0.107 ± 0.0126 | -0.0286 (7) |
| 15-25 | 1571 | 0.231 | 0.2125 | +0.0185 ± 0.0045 | 0.6592 | 0.6093 | 0.5862 | 0.3921 | 0.4411 | -0.107 ± 0.0116 | -0.03 (1) |
| 25-40 | 920 | 0.2134 | 0.2101 | +0.0033 ± 0.0089 | 0.6154 | 0.6024 | 0.6586 | 0.3478 | 0.4957 | -0.055 ± 0.0137 | -0.0267 (3) |
| 40+ | 202 | 0.3075 | 0.1822 | +0.1252 ± 0.0269 | 0.832 | 0.5377 | 0.7415 | 0.2865 | 0.3861 | -0.083 ± 0.0276 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5379 | 0.1848 | 0.1853 | -0.0005 ± 0.0002 | 0.5448 | 0.5453 | 0.4849 | 0.4696 | 0.4863 | -0.035 ± 0.0059 | -0.0189 (44) |
| 3-5 | 3839 | 0.204 | 0.202 | +0.0020 ± 0.0006 | 0.5931 | 0.5866 | 0.4807 | 0.4412 | 0.4371 | -0.059 ± 0.0074 | -0.0073 (22) |
| 5-10 | 8216 | 0.196 | 0.1905 | +0.0055 ± 0.0007 | 0.5752 | 0.5583 | 0.4877 | 0.4137 | 0.4136 | -0.057 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6621 | 0.1943 | 0.1794 | +0.0149 ± 0.0013 | 0.5733 | 0.5305 | 0.4959 | 0.3726 | 0.3738 | -0.061 ± 0.0052 | -0.0136 (14) |
| 15-25 | 8496 | 0.2121 | 0.1724 | +0.0397 ± 0.0018 | 0.618 | 0.5086 | 0.5124 | 0.3179 | 0.3139 | -0.071 ± 0.0045 | -0.0533 (3) |
| 25-40 | 6505 | 0.2172 | 0.1256 | +0.0916 ± 0.0028 | 0.6277 | 0.3858 | 0.5282 | 0.2127 | 0.2271 | -0.051 ± 0.0042 | -0.02 (4) |
| 40+ | 4359 | 0.3895 | 0.0482 | +0.3413 ± 0.0038 | 1.0153 | 0.1809 | 0.6385 | 0.1066 | 0.0645 | -0.075 ± 0.0032 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1494 | 0.1978 | 0.1978 | +0.0000 ± 0.0004 | 0.5741 | 0.5739 | 0.5092 | 0.4942 | 0.498 | -0.069 ± 0.0117 | -0.0221 (56) |
| 3-5 | 1066 | 0.1889 | 0.189 | -0.0000 ± 0.0011 | 0.556 | 0.5544 | 0.4987 | 0.4588 | 0.4775 | -0.055 ± 0.0136 | -0.0194 (34) |
| 5-10 | 2151 | 0.1994 | 0.1946 | +0.0048 ± 0.0014 | 0.5883 | 0.5723 | 0.5077 | 0.4342 | 0.4384 | -0.077 ± 0.0097 | -0.005 (78) |
| 10-15 | 1467 | 0.2145 | 0.2022 | +0.0123 ± 0.0029 | 0.6225 | 0.588 | 0.5416 | 0.4188 | 0.4288 | -0.088 ± 0.0121 | 0.0012 (66) |
| 15-25 | 1934 | 0.2306 | 0.2074 | +0.0232 ± 0.0041 | 0.6583 | 0.5987 | 0.5914 | 0.3966 | 0.4359 | -0.089 ± 0.0104 | -0.0214 (59) |
| 25-40 | 1152 | 0.2405 | 0.2105 | +0.0299 ± 0.0082 | 0.6863 | 0.604 | 0.6884 | 0.3763 | 0.4844 | -0.086 ± 0.0127 | -0.0252 (27) |
| 40+ | 416 | 0.3254 | 0.2004 | +0.1250 ± 0.021 | 0.9364 | 0.5839 | 0.8171 | 0.341 | 0.4639 | -0.097 ± 0.0195 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5453 | 0.1779 | 0.178 | -0.0001 ± 0.0002 | 0.5263 | 0.5261 | 0.512 | 0.4967 | 0.506 | -0.039 ± 0.0058 | -0.0154 (103) |
| 3-5 | 3763 | 0.1952 | 0.1944 | +0.0008 ± 0.0006 | 0.5695 | 0.567 | 0.5022 | 0.4624 | 0.4725 | -0.040 ± 0.0073 | -0.0212 (73) |
| 5-10 | 7655 | 0.1968 | 0.1903 | +0.0065 ± 0.0007 | 0.5807 | 0.5608 | 0.5016 | 0.4281 | 0.4218 | -0.062 ± 0.005 | -0.0084 (134) |
| 10-15 | 5219 | 0.2095 | 0.1931 | +0.0163 ± 0.0015 | 0.6101 | 0.5668 | 0.5363 | 0.4134 | 0.407 | -0.072 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6385 | 0.2317 | 0.1998 | +0.0319 ± 0.0022 | 0.6653 | 0.579 | 0.5767 | 0.3814 | 0.3981 | -0.068 ± 0.0056 | -0.026 (108) |
| 25-40 | 4152 | 0.2573 | 0.1902 | +0.0671 ± 0.0042 | 0.7275 | 0.5538 | 0.6401 | 0.3277 | 0.3793 | -0.065 ± 0.0066 | -0.0277 (53) |
| 40+ | 1855 | 0.3697 | 0.1589 | +0.2108 ± 0.0096 | 1.0443 | 0.4734 | 0.7452 | 0.2444 | 0.2949 | -0.063 ± 0.0088 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7421 | 1.03 ± 0.033 | 1.1 | 0.1682 | 0.1677 | 0.2153 | 0.204 |
| gen2 | 7421 | 0.821 ± 0.029 | 1.073 | 0.1733 | 0.1681 | 0.2336 | 0.2039 |
| gen1_elo | 7421 | 1.015 ± 0.032 | 1.09 | 0.1745 | 0.1678 | 0.2142 | 0.2041 |
| gen1_sr | 7421 | 1.006 ± 0.038 | 1.127 | 0.1332 | 0.1696 | 0.2297 | 0.2036 |
| gen1_ledger | 9680 | 0.869 ± 0.024 | 1.08 | 0.1892 | 0.175 | 0.2168 | 0.2003 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 34,712)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 8,253 | 23.8% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,886 | 22.7% |
| BOOK_QUALITY | execution | 6,113 | 17.6% |
| POOR_DATA | data | 3,999 | 11.5% |
| LIMITED_DATA | data | 2,124 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,977 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 1,443 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,388 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 967 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 561 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.8%, coverage 22.7%, data 17.6%, execution 17.6%, market_freshness/coverage 8.5%, mapping 4.2%, model_calibration_or_unknown 4.0%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.7%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.8%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 46.8%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.0%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.2%, LEVEL_TRANSFER_RISK 9.8%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.1%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 18,491)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,341 | 34.3% |
| STALE_QUOTE | market_freshness | 3,695 | 20.0% |
| BOOK_QUALITY | execution | 3,163 | 17.1% |
| POOR_DATA | data | 1,696 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,054 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 803 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 634 | 3.4% |
| LIMITED_DATA | data | 625 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 341 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 138 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.3%, market_freshness 20.0%, execution 17.1%, data 12.6%, market_freshness/coverage 9.1%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 54.3%, STALE_PLAYER_DATA 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.3%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 18.2%, EVENT_MAPPING_RISK 8.7%, LEVEL_TRANSFER_RISK 8.6%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.3%, POST_SETTLEMENT_OBSERVATION 34.3%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14780, "IDENTITY_AMBIGUOUS": 3711}; ticker orientation: {"VERIFIED": 18491}.

Checks: discipline:AMBIGUOUS 1218, discipline:PASS 17273, identity_confidence:AMBIGUOUS 3373, identity_confidence:PASS 15118, level_mapping:NA 1230, level_mapping:PASS 17261, market_pair:AMBIGUOUS 500, market_pair:NA 411, market_pair:PASS 17580, model_complement:NA 373, model_complement:PASS 18118, namesake:AMBIGUOUS 6, namesake:PASS 18485, physical_match_id:NA 6250, physical_match_id:PASS 12241, player_ids:PASS 18491, same_pair_other_event:PASS 18491, ticker_orientation:PASS 18491

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,494 | 3.8% | 3.2% | 1.3% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 21} | 5.51 | 0.2217 / 0.2172 (841) | 25.3% | 2.4% | 3.0% | 2.9% |
| CHALLENGER | 12,570 | 16.3% | 6.1% | 11.1% | {"coverage": 1225, "market_freshness": 252, "market_freshness/coverage": 232, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 39, "mapping": 17, "possible_market_error": 1} | 7.36 | 0.2209 / 0.2101 (2909) | 40.0% | 14.4% | 4.0% | 22.2% |
| DOUBLES | 2,627 | 46.4% | 46.3% | 6.6% | {"execution": 674, "mapping": 361, "market_freshness": 106, "market_freshness/coverage": 70, "coverage": 7} | 23.2 | 0.2987 / 0.2321 (652) | 8.9% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 24,162 | 25.2% | 17.8% | 33.0% | {"coverage": 2112, "market_freshness": 1249, "execution": 1009, "data": 905, "market_freshness/coverage": 597, "mapping": 214, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.76 | 0.2181 / 0.1996 (5053) | 40.6% | 69.4% | 15.2% | 21.3% |
| ITF_WOMEN | 31,375 | 26.4% | 18.9% | 44.8% | {"coverage": 2918, "market_freshness": 1827, "execution": 1356, "data": 1151, "market_freshness/coverage": 711, "mapping": 205, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.49 | 0.2024 / 0.1941 (6030) | 41.7% | 57.2% | 9.9% | 21.5% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,879 | 6.0% | 5.1% | 1.6% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.67 | 0.2307 / 0.2205 (804) | 30.1% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.6% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 638 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 869 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 194 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.971, "by_level_share_of_ge_25pp": {"ATP": 0.0132, "CHALLENGER": 0.1109, "DOUBLES": 0.0659, "ITF_MEN": 0.3297, "ITF_WOMEN": 0.4481, "OTHER": 0.0006, "WTA": 0.0157, "WTA125": 0.0158}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5428, "share_primary_cause_market_settled_or_in_play": 0.4342, "share_primary_cause_stale_quote_only": 0.1998}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 18491, "identity_ambiguous_share": 0.2007, "ticker_orientation": {"VERIFIED": 18491}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 12241, "with_external": 628, "coverage": 0.0513, "external_status": {"EXTERNAL_STALE": 398, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 398, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3455, "share_external_supports_model": 0.0207}, "pregame_clean_ge_25pp": {"n": 5733, "with_external": 597, "coverage": 0.1041, "external_status": {"EXTERNAL_STALE": 374, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 374, "MODEL_LONE_OUTLIER": 210, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3518, "share_external_supports_model": 0.0218}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 485.0, "median_sample_ratio": 2.44, "median_min_matches": 18.0, "median_max_days_since_last": 241.5, "share_severe_asymmetry": 0.2082, "data_status": {"POOR": 10395, "LIMITED": 4750, "ADEQUATE": 3346}, "comparison_lt_10pp": {"median_thinner_serve_points": 1732.0, "median_sample_ratio": 1.69, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1496, "model_minus_observed": 0.0664, "kalshi_minus_observed": -0.0726, "brier_diff_model_minus_kalshi": 0.0025}, "4-10x": {"n": 1009, "model_minus_observed": 0.0899, "kalshi_minus_observed": -0.0547, "brier_diff_model_minus_kalshi": 0.0091}, "<2x": {"n": 3676, "model_minus_observed": 0.0987, "kalshi_minus_observed": -0.0238, "brier_diff_model_minus_kalshi": 0.0142}, ">=10x": {"n": 1240, "model_minus_observed": 0.1212, "kalshi_minus_observed": -0.052, "brier_diff_model_minus_kalshi": 0.0152}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7421, "model": {"intercept": -0.556, "slope": 0.821, "slope_se": 0.029}, "kalshi_mid_same_rows": {"intercept": 0.177, "slope": 1.073, "slope_se": 0.033}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1681, "model_brier": 0.2336, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0297, "brier_diff_se": 0.0022, "model_logloss": 0.6646, "kalshi_logloss": 0.5903}, "fair_v1": {"n": 7421, "model": {"intercept": -0.454, "slope": 1.03, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.24, "slope": 1.1, "slope_se": 0.033}, "mean_extremity_model": 0.1682, "mean_extremity_kalshi": 0.1677, "model_brier": 0.2153, "kalshi_brier": 0.204, "brier_diff_model_minus_kalshi": 0.0113, "brier_diff_se": 0.0018, "model_logloss": 0.6197, "kalshi_logloss": 0.5905}, "gen1_elo": {"n": 7421, "model": {"intercept": -0.444, "slope": 1.015, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.239, "slope": 1.09, "slope_se": 0.033}, "mean_extremity_model": 0.1745, "mean_extremity_kalshi": 0.1678, "model_brier": 0.2142, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0101, "brier_diff_se": 0.0018, "model_logloss": 0.6178, "kalshi_logloss": 0.5906}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2492, "share_ge_15": 0.4448, "median_abs_gap": 13.05, "n": 49122}, "gen1_elo": {"share_ge_25": 0.2463, "share_ge_15": 0.4405, "median_abs_gap": 12.84, "n": 49122}, "gen1_sr": {"share_ge_25": 0.3134, "share_ge_15": 0.5207, "median_abs_gap": 15.84, "n": 49122}, "gen2": {"share_ge_25": 0.3145, "share_ge_15": 0.5105, "median_abs_gap": 15.46, "n": 49122}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1515, "share_ge_15": 0.3539, "median_abs_gap": 10.67, "n": 37835}, "gen1_elo": {"share_ge_25": 0.1494, "share_ge_15": 0.3484, "median_abs_gap": 10.49, "n": 37835}, "gen1_sr": {"share_ge_25": 0.2159, "share_ge_15": 0.439, "median_abs_gap": 12.97, "n": 37837}, "gen2": {"share_ge_25": 0.2311, "share_ge_15": 0.4387, "median_abs_gap": 12.84, "n": 37837}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.51, "share_ge_25_all": 0.0376, "share_ge_25_pregame_clean": 0.0316}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.0596, "share_ge_25_pregame_clean": 0.0506}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2365, "share_within_10pp_all": 0.4386, "share_within_10pp_pregame_clean": 0.4917, "corr_model_vs_mid_pregame_clean": 0.8489}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1070, "model_brier": 0.1973, "kalshi_brier": 0.1976, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1290, "model_brier": 0.2183, "kalshi_brier": 0.2092, "brier_diff_model_minus_kalshi": 0.0092}, "15-25": {"n_settled": 1647, "model_brier": 0.2258, "kalshi_brier": 0.2079, "brier_diff_model_minus_kalshi": 0.0179}, "25-40": {"n_settled": 938, "model_brier": 0.2238, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0182}, "3-5": {"n_settled": 683, "model_brier": 0.2064, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 191, "model_brier": 0.296, "kalshi_brier": 0.1751, "brier_diff_model_minus_kalshi": 0.121}, "5-10": {"n_settled": 1602, "model_brier": 0.2034, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0014}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.556, "slope": 0.821, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.177, "slope": 1.073, "slope_se": 0.033}, "n": 7421}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.487, "slope": 0.869, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.173, "slope": 1.08, "slope_se": 0.028}, "n": 9680}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 652, "model_brier": 0.2987, "kalshi_brier": 0.2321, "brier_diff_model_minus_kalshi": 0.0666, "brier_diff_se": 0.0115, "corr_model_outcome": 0.1023, "corr_kalshi_outcome": 0.2813}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
