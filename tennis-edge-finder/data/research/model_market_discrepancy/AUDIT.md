# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-29T06:48Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 67,210): 0-3 14.1%, 3-5 9.6%, 5-10 20.0%, 10-15 15.3%, 15-25 19.1%, 25-40 13.9%, 40+ 8.0%; median gap 11.88 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 11.0%, doubles 6.5%). Main tour: ATP 4.3% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 14,706): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.7%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.7%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.7%, market_freshness 18.8%, execution 18.7%, data 12.8%, market_freshness/coverage 9.0%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 14,706 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 458.0 points vs 1646.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.013, Gen-2 0.803, Gen-1 ledger 0.854 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 706 model 0.2244 vs Kalshi 0.2071; n 149 model 0.2799 vs Kalshi 0.1899.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 287,257 model-market comparisons (468,520 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 96,227 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-29T06:33:24.459874+00:00'], shadow board 76,814 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-29T06:33:27.847526+00:00'], Model 4 36,212 rows, 23,274 settled tickers, 8,511 tickers with an external scan.
* By model: {"gen1_ledger": 64903, "gen1_elo": 38615, "fair_v1": 38615, "gen2": 38615, "gen1_sr": 38615, "model4_fundamental": 33969, "model4_conditioned": 33925}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 67,210 | 14.1 | 9.6 | 20.0 | 15.3 | 19.1 | 13.9 | 8.0 | 11.88 | 40.9% | 21.9% |
| MW fair_v1 | 38,615 | 13.0 | 8.7 | 18.6 | 15.4 | 19.5 | 15.0 | 9.8 | 13.02 | 44.3% | 24.8% |
| MW gen1_elo | 38,615 | 12.6 | 8.6 | 19.3 | 15.4 | 19.5 | 14.9 | 9.7 | 12.93 | 44.1% | 24.6% |
| MW gen1_ledger | 28,595 | 15.6 | 10.7 | 22.0 | 15.2 | 18.5 | 12.4 | 5.6 | 10.41 | 36.4% | 17.9% |
| MW gen1_sr | 38,615 | 10.1 | 7.2 | 16.9 | 13.8 | 20.7 | 18.6 | 12.8 | 15.88 | 52.1% | 31.4% |
| MW gen2 | 38,615 | 11.2 | 7.5 | 16.5 | 13.8 | 19.4 | 17.9 | 13.8 | 15.48 | 51.1% | 31.7% |
| all families model4_conditioned | 33,925 | 22.3 | 18.2 | 34.3 | 17.3 | 4.9 | 1.9 | 1.1 | 6.02 | 7.9% | 3.0% |
| all families model4_fundamental | 33,969 | 17.3 | 13.3 | 33.8 | 20.4 | 10.2 | 3.6 | 1.4 | 7.71 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.3%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.28pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,373 | 27.2 | 15.5 | 27.4 | 13.5 | 11.7 | 4.1 | 0.6 | 5.93 | 16.4% | 4.7% |
| CHALLENGER | 5,816 | 16.2 | 9.8 | 20.8 | 15.3 | 15.3 | 11.9 | 10.7 | 10.91 | 37.9% | 22.6% |
| ITF_MEN | 10,752 | 9.9 | 7.4 | 16.9 | 15.2 | 21.1 | 17.6 | 12.0 | 15.22 | 50.7% | 29.6% |
| ITF_WOMEN | 15,206 | 9.8 | 7.0 | 15.8 | 15.1 | 22.1 | 18.3 | 12.0 | 15.71 | 52.3% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,411 | 18.3 | 13.7 | 24.4 | 20.2 | 16.1 | 6.5 | 0.8 | 8.25 | 23.4% | 7.3% |
| WTA125 | 1,051 | 16.0 | 7.8 | 22.6 | 19.3 | 20.2 | 12.6 | 1.6 | 10.7 | 34.4% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,373 | 25.9 | 15.4 | 25.4 | 16.3 | 12.0 | 4.2 | 0.8 | 6.23 | 17.0% | 5.0% |
| CHALLENGER | 5,816 | 15.1 | 8.9 | 18.2 | 14.4 | 18.1 | 13.7 | 11.6 | 12.63 | 43.4% | 25.3% |
| ITF_MEN | 10,752 | 8.0 | 6.1 | 15.0 | 13.6 | 19.6 | 20.6 | 17.0 | 18.05 | 57.3% | 37.6% |
| ITF_WOMEN | 15,206 | 8.1 | 5.8 | 14.0 | 12.6 | 20.6 | 21.4 | 17.5 | 19.2 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,411 | 15.3 | 10.9 | 21.8 | 15.6 | 22.1 | 12.7 | 1.7 | 10.62 | 36.5% | 14.4% |
| WTA125 | 1,051 | 9.6 | 6.3 | 16.3 | 16.8 | 24.4 | 17.8 | 8.8 | 15.49 | 51.1% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,373 | 22.4 | 13.0 | 24.4 | 16.0 | 16.2 | 6.7 | 1.3 | 7.58 | 24.2% | 8.0% |
| CHALLENGER | 5,816 | 15.0 | 9.3 | 21.1 | 15.8 | 15.5 | 12.3 | 10.9 | 11.21 | 38.7% | 23.2% |
| ITF_MEN | 10,752 | 9.3 | 7.1 | 17.4 | 14.4 | 21.6 | 18.0 | 12.3 | 15.68 | 51.8% | 30.2% |
| ITF_WOMEN | 15,206 | 9.5 | 6.8 | 16.3 | 15.8 | 22.1 | 18.1 | 11.3 | 15.51 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,411 | 23.6 | 16.6 | 31.6 | 14.7 | 9.4 | 2.7 | 1.3 | 6.08 | 13.4% | 4.0% |
| WTA125 | 1,051 | 22.1 | 13.0 | 26.6 | 16.8 | 14.8 | 6.3 | 0.4 | 7.99 | 21.5% | 6.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,961 | 24.4 | 19.0 | 31.1 | 12.9 | 9.0 | 3.0 | 0.5 | 5.74 | 12.5% | 3.5% |
| CHALLENGER | 3,944 | 22.5 | 14.6 | 26.9 | 14.7 | 13.7 | 6.1 | 1.6 | 7.16 | 21.4% | 7.6% |
| DOUBLES | 2,049 | 5.2 | 4.5 | 12.2 | 10.7 | 21.0 | 24.9 | 21.4 | 23.54 | 67.4% | 46.4% |
| ITF_MEN | 8,227 | 13.0 | 9.4 | 21.1 | 15.8 | 21.4 | 13.3 | 6.0 | 11.97 | 40.7% | 19.3% |
| ITF_WOMEN | 9,775 | 13.1 | 9.2 | 19.6 | 15.6 | 21.4 | 15.5 | 5.7 | 12.44 | 42.5% | 21.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,425 | 24.2 | 15.4 | 29.9 | 18.1 | 9.3 | 2.8 | 0.3 | 6.8 | 12.3% | 3.1% |
| WTA125 | 1,065 | 24.9 | 12.4 | 21.2 | 19.1 | 13.2 | 7.4 | 1.7 | 7.9 | 22.4% | 9.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,275 | 27.5 | 15.7 | 27.8 | 13.4 | 11.5 | 3.7 | 0.4 | 5.88 | 15.6% | 4.1% |
| CHALLENGER | 4,081 | 21.1 | 12.4 | 25.9 | 17.8 | 15.1 | 6.2 | 1.5 | 8.03 | 22.8% | 7.7% |
| ITF_MEN | 7,913 | 12.0 | 8.7 | 20.4 | 17.2 | 22.0 | 14.4 | 5.3 | 12.45 | 41.7% | 19.7% |
| ITF_WOMEN | 11,364 | 11.6 | 8.4 | 18.3 | 17.2 | 24.0 | 15.2 | 5.2 | 13.36 | 44.5% | 20.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,335 | 18.6 | 13.6 | 24.5 | 20.4 | 16.2 | 6.0 | 0.6 | 8.18 | 22.8% | 6.6% |
| WTA125 | 1,015 | 16.3 | 7.7 | 22.1 | 19.6 | 20.7 | 12.3 | 1.4 | 10.97 | 34.4% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,275 | 26.2 | 15.8 | 25.5 | 16.3 | 12.0 | 3.8 | 0.5 | 6.2 | 16.2% | 4.2% |
| CHALLENGER | 4,081 | 19.3 | 11.4 | 23.0 | 16.9 | 18.4 | 9.2 | 1.9 | 9.03 | 29.5% | 11.1% |
| ITF_MEN | 7,914 | 9.4 | 7.2 | 17.3 | 15.8 | 21.4 | 18.9 | 9.9 | 15.12 | 50.2% | 28.8% |
| ITF_WOMEN | 11,365 | 9.0 | 6.7 | 15.8 | 14.1 | 22.7 | 20.9 | 10.8 | 16.71 | 54.4% | 31.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,335 | 15.4 | 11.0 | 21.9 | 15.6 | 22.2 | 12.6 | 1.3 | 10.59 | 36.1% | 13.8% |
| WTA125 | 1,015 | 9.7 | 6.3 | 16.4 | 16.9 | 24.3 | 18.1 | 8.3 | 15.19 | 50.7% | 26.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,907 | 24.5 | 19.2 | 31.1 | 13.1 | 8.7 | 2.9 | 0.4 | 5.67 | 12.0% | 3.3% |
| CHALLENGER | 3,475 | 23.9 | 15.5 | 28.1 | 14.8 | 13.1 | 4.1 | 0.5 | 6.6 | 17.6% | 4.6% |
| DOUBLES | 1,922 | 5.1 | 4.6 | 12.4 | 10.9 | 20.9 | 24.8 | 21.3 | 23.35 | 67.0% | 46.1% |
| ITF_MEN | 7,030 | 13.9 | 9.9 | 22.7 | 16.5 | 21.3 | 11.8 | 3.9 | 11.02 | 37.0% | 15.7% |
| ITF_WOMEN | 8,316 | 13.7 | 9.6 | 20.9 | 16.2 | 21.5 | 14.4 | 3.6 | 11.61 | 39.5% | 18.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,371 | 24.6 | 15.8 | 29.9 | 18.2 | 9.3 | 2.2 | 0.1 | 6.68 | 11.5% | 2.3% |
| WTA125 | 941 | 26.2 | 13.2 | 22.3 | 20.4 | 12.1 | 5.2 | 0.5 | 7.35 | 17.8% | 5.7% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,049 | 5.2 | 4.5 | 12.2 | 10.7 | 21.0 | 24.9 | 21.4 | 23.54 | 67.4% | 46.4% |
| singles | 26,546 | 16.4 | 11.2 | 22.7 | 15.6 | 18.3 | 11.4 | 4.3 | 9.9 | 34.1% | 15.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,759 | 13.1 | 9.3 | 20.1 | 15.6 | 19.1 | 13.8 | 9.0 | 12.4 | 41.9% | 22.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 25,243 | 13.5 | 8.7 | 18.5 | 15.1 | 19.3 | 15.1 | 9.8 | 12.98 | 44.2% | 24.9% |
| UNKNOWN | 5,364 | 10.5 | 7.8 | 17.1 | 16.6 | 20.8 | 15.9 | 11.2 | 14.11 | 47.9% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,692 | 20.0 | 12.2 | 22.3 | 15.8 | 14.7 | 9.3 | 5.8 | 8.57 | 29.7% | 15.1% |
| B | 4,713 | 12.9 | 8.9 | 19.1 | 16.2 | 19.4 | 12.8 | 10.8 | 12.59 | 42.9% | 23.5% |
| C | 5,512 | 12.1 | 8.9 | 19.8 | 15.8 | 18.7 | 14.4 | 10.3 | 12.77 | 43.4% | 24.7% |
| D | 6,099 | 12.1 | 8.3 | 17.6 | 15.3 | 21.5 | 15.8 | 9.4 | 13.73 | 46.7% | 25.2% |
| F | 11,599 | 7.5 | 5.6 | 15.0 | 14.6 | 23.3 | 21.0 | 13.1 | 17.74 | 57.4% | 34.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,593 | 24.1 | 15.7 | 28.7 | 15.4 | 11.0 | 3.8 | 1.3 | 6.54 | 16.2% | 5.1% |
| B | 3,981 | 17.0 | 10.5 | 24.0 | 16.2 | 19.1 | 9.9 | 3.2 | 9.68 | 32.2% | 13.1% |
| C | 5,579 | 11.3 | 7.8 | 19.4 | 14.8 | 21.1 | 15.5 | 10.1 | 13.46 | 46.7% | 25.6% |
| D | 4,189 | 14.5 | 9.9 | 21.6 | 15.3 | 20.0 | 13.1 | 5.6 | 11.24 | 38.6% | 18.7% |
| F | 7,253 | 9.9 | 8.4 | 16.0 | 14.9 | 23.2 | 19.9 | 7.8 | 15.44 | 50.8% | 27.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,122 | 18.3 | 11.1 | 21.4 | 15.5 | 15.2 | 10.0 | 8.5 | 9.74 | 33.7% | 18.6% |
| LIMITED | 8,430 | 13.7 | 10.0 | 20.2 | 16.3 | 19.0 | 13.4 | 7.4 | 11.71 | 39.8% | 20.8% |
| POOR | 18,063 | 9.1 | 6.5 | 16.0 | 14.9 | 22.6 | 19.1 | 11.8 | 16.16 | 53.5% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,421 | 24.1 | 18.1 | 33.1 | 15.0 | 6.6 | 2.7 | 0.4 | 5.86 | 9.7% | 3.1% |
| GAME_SPREAD | 5,813 | 22.2 | 15.2 | 33.0 | 17.2 | 9.0 | 2.9 | 0.6 | 6.74 | 12.4% | 3.5% |
| MATCH_WINNER | 28,595 | 15.6 | 10.7 | 22.0 | 15.2 | 18.5 | 12.4 | 5.6 | 10.41 | 36.4% | 17.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,408 | 27.3 | 16.6 | 31.3 | 12.5 | 9.5 | 2.4 | 0.3 | 5.7 | 12.2% | 2.7% |
| TOTAL_GAMES | 9,642 | 9.4 | 10.3 | 36.1 | 26.8 | 10.5 | 4.0 | 2.8 | 9.3 | 17.3% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,023 | 24.4 | 30.2 | 32.9 | 7.4 | 4.0 | 0.9 | 0.2 | 4.7 | 5.2% | 1.1% |
| GAME_SPREAD | 7,943 | 47.2 | 16.1 | 25.5 | 7.3 | 2.2 | 1.2 | 0.6 | 3.28 | 4.0% | 1.8% |
| TOTAL_GAMES | 13,959 | 6.3 | 9.1 | 40.5 | 31.5 | 7.3 | 3.1 | 2.2 | 9.33 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,034 | 23.9 | 16.8 | 34.8 | 14.4 | 7.1 | 2.6 | 0.4 | 6.03 | 10.1% | 3.0% |
| GAME_SPREAD | 7,946 | 20.1 | 13.5 | 28.0 | 20.5 | 12.6 | 4.2 | 1.1 | 7.81 | 17.9% | 5.3% |
| TOTAL_GAMES | 13,989 | 9.9 | 10.2 | 36.3 | 25.4 | 11.6 | 4.2 | 2.4 | 9.2 | 18.2% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 38,615 | 44.3% | 24.8% | 13.02 | 35.6% | 15.4% | 10.77 |
| gen1_elo | 38,615 | 44.1% | 24.6% | 12.93 | 35.4% | 15.4% | 10.57 |
| gen1_sr | 38,615 | 52.1% | 31.4% | 15.88 | 44.3% | 21.9% | 13.03 |
| gen2 | 38,615 | 51.1% | 31.7% | 15.48 | 44.2% | 23.6% | 12.95 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,317 | 15.6 | 10.6 | 21.3 | 17.2 | 20.0 | 12.0 | 3.3 | 10.71 | 35.4% | 15.4% |
| STALE | 20,298 | 10.6 | 7.1 | 16.2 | 13.8 | 19.0 | 17.6 | 15.7 | 16.0 | 52.3% | 33.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 22,063 | 16.3 | 11.1 | 22.6 | 15.4 | 17.9 | 11.9 | 4.8 | 9.98 | 34.5% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 67,210 | 22063 | 21789 | 23358 | 24.3 | 122.2 | 1451.1 |
| ge_15pp | 27,516 | 7620 | 7768 | 12128 | 26.7 | 434.7 | 1451.1 |
| ge_25pp | 14,706 | 3667 | 3408 | 7631 | 31.7 | 582.7 | 1431.1 |
| lt_10pp | 29,383 | 11046 | 10324 | 8013 | 22.4 | 47.0 | 1421.1 |

Current slate `SL-20261029T064845Z-e07329a8`: 599 priced rows, quote age at build {'median': 15.8, 'max': 15.9}, freshness {'AGING': 599}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 43 | 0.0 | 0.0 | 32.6 | 7.0 | 34.9 | 23.3 | 2.3 | 20.19 | 60.5% | 25.6% |
| EXTERNAL_LONE_OUTLIER | 23 | 69.6 | 30.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,779 | 19.8 | 11.3 | 25.1 | 18.0 | 17.8 | 7.2 | 0.8 | 8.62 | 25.8% | 8.0% |
| KALSHI_LONE_OUTLIER | 26 | 3.9 | 3.9 | 76.9 | 7.7 | 3.9 | 3.9 | 0.0 | 6.31 | 7.7% | 3.9% |
| MARKETS_AGREE | 745 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.25 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,609 | 0.0 | 2.5 | 35.9 | 25.7 | 24.6 | 10.4 | 0.8 | 12.12 | 35.9% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 38,615 | 6225 (16.1%) | 25.9% | 1.1% | {"EXTERNAL_STALE": 3779, "AGREES_WITH_KALSHI": 1609, "ALL_AGREE": 745, "SUPPORTS_MODEL_DIRECTION": 42, "AGREES_WITH_MODEL": 26, "EXTERNAL_OUTLIER": 23, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 17,097 | 1580 (9.2%) | 36.5% | 1.8% | {"EXTERNAL_STALE": 975, "AGREES_WITH_KALSHI": 577, "SUPPORTS_MODEL_DIRECTION": 26, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,577 | 496 (5.2%) | 36.5% | 2.4% | {"EXTERNAL_STALE": 303, "AGREES_WITH_KALSHI": 181, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,624 | 471 (10.2%) | 36.9% | 2.5% | {"EXTERNAL_STALE": 285, "AGREES_WITH_KALSHI": 174, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 15,568 | 3546 (22.8%) | 17.4% | 1.0% | {"EXTERNAL_STALE": 2124, "ALL_AGREE": 745, "AGREES_WITH_KALSHI": 618, "EXTERNAL_OUTLIER": 23, "AGREES_WITH_MODEL": 22, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,571 | 10.4 | 7.4 | 19.8 | 14.3 | 21.6 | 16.6 | 9.9 | 14.11 | 48.1% | 26.5% |
| 4-10x | 5,202 | 11.2 | 8.6 | 18.4 | 15.6 | 21.8 | 14.5 | 9.9 | 13.67 | 46.2% | 24.4% |
| <2x | 19,482 | 15.2 | 10.0 | 19.4 | 16.1 | 17.4 | 13.2 | 8.8 | 11.57 | 39.3% | 21.9% |
| >=10x | 6,360 | 10.7 | 6.4 | 15.2 | 14.4 | 21.5 | 19.1 | 12.7 | 16.19 | 53.3% | 31.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,784 | 12.8 | 8.7 | 19.6 | 16.2 | 18.9 | 13.6 | 10.3 | 12.69 | 42.9% | 23.9% |
| 300-1000 | 8,327 | 12.1 | 8.7 | 17.8 | 15.2 | 20.3 | 16.4 | 9.5 | 13.59 | 46.2% | 25.9% |
| <300 | 12,609 | 8.3 | 5.8 | 15.2 | 14.8 | 22.9 | 20.0 | 12.9 | 17.03 | 55.9% | 32.9% |
| >=3000 | 7,895 | 21.6 | 13.4 | 23.8 | 15.7 | 13.7 | 7.2 | 4.7 | 7.53 | 25.6% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1097 | 0.5501 | 0.4114 | 0.4968 | +0.053 | -0.085 | -0.0018 ± 0.0047 |
| ratio 4-10x | 757 | 0.5802 | 0.434 | 0.4954 | +0.085 | -0.061 | 0.0078 ± 0.0058 |
| ratio <2x | 2635 | 0.5374 | 0.4139 | 0.4493 | +0.088 | -0.035 | 0.0112 ± 0.0028 |
| ratio >=10x | 959 | 0.5659 | 0.391 | 0.4453 | +0.121 | -0.054 | 0.0147 ± 0.0059 |
| thinner_sample 1000-3000 | 1461 | 0.5392 | 0.4122 | 0.4511 | +0.088 | -0.039 | 0.0089 ± 0.0038 |
| thinner_sample 300-1000 | 1237 | 0.5681 | 0.4263 | 0.4883 | +0.080 | -0.062 | 0.0026 ± 0.0045 |
| thinner_sample <300 | 1852 | 0.558 | 0.3902 | 0.4595 | +0.099 | -0.069 | 0.0108 ± 0.0041 |
| thinner_sample >=3000 | 898 | 0.5319 | 0.4379 | 0.4644 | +0.068 | -0.026 | 0.0127 ± 0.0038 |
| data_status ADEQUATE | 1491 | 0.5341 | 0.4307 | 0.45 | +0.084 | -0.019 | 0.0126 ± 0.0032 |
| data_status LIMITED | 1296 | 0.5488 | 0.4158 | 0.4769 | +0.072 | -0.061 | 0.0051 ± 0.0042 |
| data_status POOR | 2661 | 0.5614 | 0.4 | 0.4667 | +0.095 | -0.067 | 0.0084 ± 0.0034 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 803 | 0.1974 | 0.1979 | -0.0005 ± 0.0005 | 0.5735 | 0.5748 | 0.5035 | 0.4884 | 0.5093 | -0.087 ± 0.0167 | -0.01 (5) |
| 3-5 | 489 | 0.2058 | 0.2063 | -0.0005 ± 0.0017 | 0.5951 | 0.5948 | 0.5034 | 0.4635 | 0.4888 | -0.094 ± 0.0211 | 0.02 (1) |
| 5-10 | 1140 | 0.2013 | 0.2017 | -0.0004 ± 0.002 | 0.5886 | 0.5866 | 0.5104 | 0.4367 | 0.4737 | -0.087 ± 0.0137 | -0.0167 (6) |
| 10-15 | 953 | 0.2222 | 0.2133 | +0.0089 ± 0.0037 | 0.6375 | 0.6127 | 0.526 | 0.4024 | 0.4271 | -0.109 ± 0.0151 | -0.048 (5) |
| 15-25 | 1208 | 0.2245 | 0.2124 | +0.0120 ± 0.0052 | 0.6445 | 0.6093 | 0.5752 | 0.3796 | 0.447 | -0.098 ± 0.0133 | -0.0033 (9) |
| 25-40 | 706 | 0.2244 | 0.2071 | +0.0174 ± 0.0103 | 0.6391 | 0.5961 | 0.655 | 0.3442 | 0.4717 | -0.074 ± 0.0157 | -0.01 (1) |
| 40+ | 149 | 0.2799 | 0.1899 | +0.0900 ± 0.0311 | 0.7641 | 0.5593 | 0.7421 | 0.2932 | 0.4228 | -0.074 ± 0.0308 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4317 | 0.1811 | 0.1818 | -0.0007 ± 0.0002 | 0.5361 | 0.5368 | 0.4869 | 0.4717 | 0.4971 | -0.028 ± 0.0066 | -0.0129 (17) |
| 3-5 | 2917 | 0.195 | 0.1927 | +0.0022 ± 0.0007 | 0.569 | 0.5612 | 0.4819 | 0.4421 | 0.4333 | -0.064 ± 0.0082 | 0.0 (2) |
| 5-10 | 6138 | 0.2016 | 0.1981 | +0.0035 ± 0.0008 | 0.589 | 0.5767 | 0.4837 | 0.4101 | 0.4244 | -0.046 ± 0.0057 | -0.0119 (21) |
| 10-15 | 5164 | 0.2028 | 0.1868 | +0.0160 ± 0.0015 | 0.5921 | 0.5483 | 0.4827 | 0.3587 | 0.3557 | -0.067 ± 0.006 | -0.0281 (16) |
| 15-25 | 6433 | 0.2066 | 0.1688 | +0.0378 ± 0.002 | 0.6058 | 0.5005 | 0.4997 | 0.3035 | 0.3061 | -0.069 ± 0.0051 | -0.0025 (44) |
| 25-40 | 5135 | 0.2225 | 0.1253 | +0.0972 ± 0.0031 | 0.6395 | 0.3851 | 0.5264 | 0.2122 | 0.2189 | -0.060 ± 0.0048 | -0.01 (1) |
| 40+ | 3334 | 0.3829 | 0.0448 | +0.3381 ± 0.0042 | 0.9971 | 0.1733 | 0.6319 | 0.1041 | 0.0603 | -0.078 ± 0.0035 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 622 | 0.2053 | 0.206 | -0.0007 ± 0.0006 | 0.5921 | 0.5941 | 0.5104 | 0.4954 | 0.5209 | -0.105 ± 0.0197 | -0.01 (3) |
| 3-5 | 442 | 0.2235 | 0.2206 | +0.0029 ± 0.0018 | 0.6322 | 0.6264 | 0.5133 | 0.4735 | 0.4525 | -0.134 ± 0.0238 | 0.02 (1) |
| 5-10 | 991 | 0.208 | 0.2077 | +0.0003 ± 0.0022 | 0.6022 | 0.6004 | 0.5463 | 0.4713 | 0.5086 | -0.085 ± 0.0149 | -0.01 (4) |
| 10-15 | 891 | 0.2178 | 0.2104 | +0.0074 ± 0.0039 | 0.6269 | 0.6078 | 0.5652 | 0.4409 | 0.4759 | -0.111 ± 0.0161 | -0.04 (5) |
| 15-25 | 1267 | 0.2297 | 0.2141 | +0.0156 ± 0.0051 | 0.6541 | 0.6125 | 0.5816 | 0.3863 | 0.4467 | -0.096 ± 0.0132 | -0.0133 (9) |
| 25-40 | 899 | 0.2686 | 0.1962 | +0.0723 ± 0.0093 | 0.7496 | 0.573 | 0.6552 | 0.341 | 0.386 | -0.131 ± 0.0148 | -0.0075 (4) |
| 40+ | 336 | 0.3602 | 0.1683 | +0.1919 ± 0.0222 | 0.9902 | 0.5046 | 0.7329 | 0.248 | 0.3065 | -0.080 ± 0.0216 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3684 | 0.1879 | 0.1883 | -0.0003 ± 0.0002 | 0.5507 | 0.5512 | 0.5089 | 0.4938 | 0.5103 | -0.040 ± 0.0074 | -0.0133 (15) |
| 3-5 | 2502 | 0.1974 | 0.1961 | +0.0014 ± 0.0007 | 0.5724 | 0.5683 | 0.5138 | 0.4742 | 0.476 | -0.051 ± 0.0091 | 0.02 (1) |
| 5-10 | 5459 | 0.1985 | 0.1947 | +0.0038 ± 0.0009 | 0.5826 | 0.5685 | 0.5128 | 0.4387 | 0.4532 | -0.045 ± 0.006 | -0.0117 (6) |
| 10-15 | 4629 | 0.2059 | 0.1933 | +0.0126 ± 0.0016 | 0.6019 | 0.5637 | 0.5125 | 0.3886 | 0.4001 | -0.056 ± 0.0066 | -0.0189 (18) |
| 15-25 | 6491 | 0.2172 | 0.1812 | +0.0360 ± 0.0021 | 0.6319 | 0.5317 | 0.5227 | 0.3273 | 0.3366 | -0.062 ± 0.0053 | -0.0086 (42) |
| 25-40 | 5956 | 0.2516 | 0.1355 | +0.1161 ± 0.003 | 0.7096 | 0.4161 | 0.5563 | 0.2396 | 0.2179 | -0.087 ± 0.0048 | -0.0044 (18) |
| 40+ | 4717 | 0.3963 | 0.0589 | +0.3374 ± 0.0041 | 1.0448 | 0.2119 | 0.6504 | 0.1169 | 0.081 | -0.073 ± 0.0035 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 769 | 0.1957 | 0.1979 | -0.0021 ± 0.0006 | 0.5701 | 0.5755 | 0.5 | 0.4847 | 0.5436 | -0.039 ± 0.0168 | -0.0137 (8) |
| 3-5 | 530 | 0.2045 | 0.2026 | +0.0019 ± 0.0016 | 0.5918 | 0.585 | 0.4955 | 0.4559 | 0.4528 | -0.123 ± 0.0203 | 0.0067 (3) |
| 5-10 | 1171 | 0.2027 | 0.2009 | +0.0018 ± 0.002 | 0.5914 | 0.5846 | 0.5083 | 0.4344 | 0.4594 | -0.094 ± 0.0135 | -0.0071 (7) |
| 10-15 | 952 | 0.2099 | 0.2057 | +0.0042 ± 0.0036 | 0.6097 | 0.5956 | 0.5393 | 0.416 | 0.4611 | -0.095 ± 0.0148 | -0.0317 (6) |
| 15-25 | 1147 | 0.2325 | 0.2169 | +0.0157 ± 0.0054 | 0.663 | 0.6191 | 0.5867 | 0.3923 | 0.4499 | -0.108 ± 0.0138 | -0.03 (1) |
| 25-40 | 720 | 0.2143 | 0.2143 | -0.0000 ± 0.0101 | 0.6179 | 0.6129 | 0.6642 | 0.3532 | 0.5069 | -0.058 ± 0.0156 | 0.015 (2) |
| 40+ | 159 | 0.2959 | 0.197 | +0.0989 ± 0.031 | 0.8067 | 0.5752 | 0.7484 | 0.2975 | 0.4214 | -0.073 ± 0.0322 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4183 | 0.1829 | 0.1835 | -0.0005 ± 0.0002 | 0.5391 | 0.54 | 0.4815 | 0.4662 | 0.4824 | -0.035 ± 0.0067 | -0.0163 (35) |
| 3-5 | 2856 | 0.1994 | 0.1974 | +0.0020 ± 0.0007 | 0.581 | 0.5737 | 0.4811 | 0.4417 | 0.4359 | -0.063 ± 0.0085 | -0.0094 (18) |
| 5-10 | 6287 | 0.1942 | 0.19 | +0.0042 ± 0.0008 | 0.5718 | 0.5573 | 0.4836 | 0.4096 | 0.4188 | -0.050 ± 0.0055 | -0.01 (31) |
| 10-15 | 5120 | 0.1919 | 0.1784 | +0.0135 ± 0.0015 | 0.5673 | 0.5287 | 0.493 | 0.3696 | 0.3762 | -0.058 ± 0.0059 | -0.015 (12) |
| 15-25 | 6576 | 0.2125 | 0.1738 | +0.0386 ± 0.002 | 0.6185 | 0.5119 | 0.5124 | 0.3177 | 0.3174 | -0.070 ± 0.0051 | -0.03 (2) |
| 25-40 | 5107 | 0.2164 | 0.1292 | +0.0872 ± 0.0032 | 0.6264 | 0.3937 | 0.53 | 0.2143 | 0.2365 | -0.047 ± 0.0049 | 0.01 (3) |
| 40+ | 3309 | 0.3947 | 0.05 | +0.3447 ± 0.0044 | 1.0292 | 0.1872 | 0.6424 | 0.1112 | 0.0659 | -0.080 ± 0.0037 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1157 | 0.1957 | 0.1959 | -0.0002 ± 0.0005 | 0.5702 | 0.5704 | 0.5054 | 0.4903 | 0.497 | -0.066 ± 0.0132 | -0.0224 (49) |
| 3-5 | 811 | 0.1879 | 0.1872 | +0.0007 ± 0.0012 | 0.5508 | 0.5484 | 0.4969 | 0.4571 | 0.4661 | -0.065 ± 0.0156 | -0.0194 (34) |
| 5-10 | 1699 | 0.2012 | 0.1964 | +0.0048 ± 0.0016 | 0.5916 | 0.5761 | 0.5013 | 0.4276 | 0.4326 | -0.073 ± 0.011 | -0.005 (78) |
| 10-15 | 1162 | 0.2165 | 0.2044 | +0.0121 ± 0.0033 | 0.6253 | 0.593 | 0.5348 | 0.4121 | 0.4225 | -0.084 ± 0.0136 | 0.0014 (64) |
| 15-25 | 1500 | 0.2312 | 0.211 | +0.0201 ± 0.0047 | 0.6592 | 0.6069 | 0.5811 | 0.3863 | 0.434 | -0.080 ± 0.012 | -0.0214 (59) |
| 25-40 | 936 | 0.2447 | 0.21 | +0.0347 ± 0.0092 | 0.6991 | 0.602 | 0.6816 | 0.3697 | 0.4701 | -0.093 ± 0.0141 | -0.0219 (26) |
| 40+ | 313 | 0.3401 | 0.2012 | +0.1389 ± 0.0245 | 0.9813 | 0.5876 | 0.8127 | 0.3352 | 0.4441 | -0.103 ± 0.0229 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4261 | 0.1754 | 0.1756 | -0.0002 ± 0.0002 | 0.5199 | 0.5201 | 0.5118 | 0.4966 | 0.5081 | -0.038 ± 0.0065 | -0.0157 (88) |
| 3-5 | 2912 | 0.1932 | 0.1917 | +0.0016 ± 0.0007 | 0.5628 | 0.5596 | 0.5061 | 0.4663 | 0.4663 | -0.051 ± 0.0082 | -0.0209 (69) |
| 5-10 | 5947 | 0.1982 | 0.1911 | +0.0071 ± 0.0009 | 0.5835 | 0.5627 | 0.4966 | 0.4229 | 0.4128 | -0.067 ± 0.0057 | -0.0082 (132) |
| 10-15 | 4168 | 0.2119 | 0.1963 | +0.0156 ± 0.0017 | 0.6148 | 0.5741 | 0.5329 | 0.41 | 0.4074 | -0.068 ± 0.0069 | -0.0053 (105) |
| 15-25 | 5063 | 0.2292 | 0.2014 | +0.0278 ± 0.0025 | 0.6597 | 0.5823 | 0.5671 | 0.3718 | 0.3988 | -0.061 ± 0.0063 | -0.0253 (107) |
| 25-40 | 3423 | 0.2609 | 0.1863 | +0.0746 ± 0.0046 | 0.7382 | 0.5438 | 0.6352 | 0.3223 | 0.3623 | -0.080 ± 0.0072 | -0.0229 (51) |
| 40+ | 1477 | 0.3811 | 0.1506 | +0.2305 ± 0.0105 | 1.0752 | 0.4526 | 0.7364 | 0.2356 | 0.2668 | -0.080 ± 0.0096 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5448 | 1.013 ± 0.038 | 1.09 | 0.1689 | 0.1664 | 0.2151 | 0.2063 |
| gen2 | 5448 | 0.803 ± 0.034 | 1.049 | 0.1705 | 0.1669 | 0.235 | 0.2062 |
| gen1_elo | 5448 | 0.994 ± 0.036 | 1.088 | 0.1755 | 0.1666 | 0.2137 | 0.2065 |
| gen1_sr | 5448 | 0.983 ± 0.045 | 1.11 | 0.1308 | 0.1688 | 0.2308 | 0.2058 |
| gen1_ledger | 7578 | 0.854 ± 0.027 | 1.054 | 0.187 | 0.1769 | 0.2183 | 0.2013 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 27,516)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,127 | 22.3% |
| STALE_QUOTE | market_freshness | 6,031 | 21.9% |
| BOOK_QUALITY | execution | 5,270 | 19.1% |
| POOR_DATA | data | 3,227 | 11.7% |
| LIMITED_DATA | data | 1,713 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,548 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,210 | 4.4% |
| IDENTITY_AMBIGUOUS | mapping | 1,126 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 795 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 468 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.3%, market_freshness 21.9%, execution 19.1%, data 17.9%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.4%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 72.0%, THIN_PLAYER_HISTORY 60.9%, STALE_PLAYER_DATA 52.5%, STALE_KALSHI_QUOTE 44.1%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 15.7%, LEVEL_TRANSFER_RISK 10.4%, LOW_DISPLAYED_LIQUIDITY 7.9%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.8%, POST_SETTLEMENT_OBSERVATION 22.3%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 14,706)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,950 | 33.7% |
| STALE_QUOTE | market_freshness | 2,766 | 18.8% |
| BOOK_QUALITY | execution | 2,748 | 18.7% |
| POOR_DATA | data | 1,377 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 819 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 599 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 512 | 3.5% |
| LIMITED_DATA | data | 506 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 306 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 122 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.7%, market_freshness 18.8%, execution 18.7%, data 12.8%, market_freshness/coverage 9.0%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.3%, THIN_PLAYER_HISTORY 63.1%, STALE_KALSHI_QUOTE 51.9%, STALE_PLAYER_DATA 46.7%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.5%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.8%, POST_SETTLEMENT_OBSERVATION 33.7%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 11663, "IDENTITY_AMBIGUOUS": 3043}; ticker orientation: {"VERIFIED": 14706}.

Checks: discipline:AMBIGUOUS 950, discipline:PASS 13756, identity_confidence:AMBIGUOUS 2724, identity_confidence:PASS 11982, level_mapping:NA 962, level_mapping:PASS 13744, market_pair:AMBIGUOUS 478, market_pair:NA 347, market_pair:PASS 13881, model_complement:NA 311, model_complement:PASS 14395, namesake:AMBIGUOUS 6, namesake:PASS 14700, physical_match_id:NA 5129, physical_match_id:PASS 9577, player_ids:PASS 14706, same_pair_other_event:PASS 14706, ticker_orientation:PASS 14706

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,334 | 4.3% | 3.8% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.84 | 0.22 / 0.2173 (611) | 21.6% | 2.9% | 3.3% | 2.9% |
| CHALLENGER | 9,760 | 16.5% | 6.3% | 11.0% | {"coverage": 946, "market_freshness/coverage": 195, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 74, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.26 | 0.2192 / 0.2102 (2239) | 35.2% | 15.8% | 4.1% | 22.6% |
| DOUBLES | 2,049 | 46.4% | 46.1% | 6.5% | {"execution": 538, "mapping": 241, "market_freshness": 106, "market_freshness/coverage": 58, "coverage": 7} | 23.35 | 0.3095 / 0.2375 (489) | 11.4% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 18,979 | 25.1% | 17.8% | 32.4% | {"coverage": 1659, "execution": 897, "market_freshness": 869, "data": 705, "market_freshness/coverage": 447, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.76 | 0.2165 / 0.1996 (3880) | 37.4% | 70.2% | 17.0% | 21.3% |
| ITF_WOMEN | 24,981 | 26.7% | 19.4% | 45.4% | {"coverage": 2288, "market_freshness": 1426, "execution": 1199, "data": 941, "market_freshness/coverage": 561, "mapping": 152, "model_calibration_or_unknown": 81, "model_calibration": 21} | 12.64 | 0.2053 / 0.1967 (4540) | 39.4% | 57.8% | 10.1% | 21.2% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,836 | 5.7% | 5.0% | 1.5% | {"market_freshness": 77, "model_calibration_or_unknown": 43, "execution": 27, "coverage": 24, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.58 | 0.2351 / 0.2283 (593) | 26.2% | 1.1% | 1.4% | 3.4% |
| WTA125 | 2,116 | 11.6% | 9.9% | 1.7% | {"market_freshness": 65, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.21 | 0.2094 / 0.192 (632) | 25.4% | 11.6% | 5.1% | 7.6% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 286 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 869 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 658 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 49 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 50 | `KXITFMATCH-26OCT28DELBAR-BAR` | ITF_MEN | fair_v1 | 84% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 599 min (STALE); data POOR (grade F, thinner serve sample 803.0, ratio 2.48); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9696, "by_level_share_of_ge_25pp": {"ATP": 0.0154, "CHALLENGER": 0.1098, "DOUBLES": 0.0646, "ITF_MEN": 0.3242, "ITF_WOMEN": 0.4535, "OTHER": 0.0008, "WTA": 0.015, "WTA125": 0.0167}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5189, "share_primary_cause_market_settled_or_in_play": 0.4271, "share_primary_cause_stale_quote_only": 0.1881}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 14706, "identity_ambiguous_share": 0.2069, "ticker_orientation": {"VERIFIED": 14706}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9577, "with_external": 496, "coverage": 0.0518, "external_status": {"EXTERNAL_STALE": 303, "AGREES_WITH_KALSHI": 181, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 303, "MODEL_LONE_OUTLIER": 181, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3649, "share_external_supports_model": 0.0242}, "pregame_clean_ge_25pp": {"n": 4624, "with_external": 471, "coverage": 0.1019, "external_status": {"EXTERNAL_STALE": 285, "AGREES_WITH_KALSHI": 174, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 285, "MODEL_LONE_OUTLIER": 174, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3694, "share_external_supports_model": 0.0255}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 458.0, "median_sample_ratio": 2.5, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2122, "data_status": {"POOR": 8395, "LIMITED": 3763, "ADEQUATE": 2548}, "comparison_lt_10pp": {"median_thinner_serve_points": 1646.0, "median_sample_ratio": 1.73, "median_min_matches": 88.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1097, "model_minus_observed": 0.0533, "kalshi_minus_observed": -0.0854, "brier_diff_model_minus_kalshi": -0.0018}, "4-10x": {"n": 757, "model_minus_observed": 0.0849, "kalshi_minus_observed": -0.0614, "brier_diff_model_minus_kalshi": 0.0078}, "<2x": {"n": 2635, "model_minus_observed": 0.0881, "kalshi_minus_observed": -0.0354, "brier_diff_model_minus_kalshi": 0.0112}, ">=10x": {"n": 959, "model_minus_observed": 0.1206, "kalshi_minus_observed": -0.0543, "brier_diff_model_minus_kalshi": 0.0147}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5448, "model": {"intercept": -0.536, "slope": 0.803, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.19, "slope": 1.049, "slope_se": 0.038}, "mean_extremity_model": 0.1705, "mean_extremity_kalshi": 0.1669, "model_brier": 0.235, "kalshi_brier": 0.2062, "brier_diff_model_minus_kalshi": 0.0288, "brier_diff_se": 0.0026, "model_logloss": 0.6678, "kalshi_logloss": 0.5954}, "fair_v1": {"n": 5448, "model": {"intercept": -0.411, "slope": 1.013, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.283, "slope": 1.09, "slope_se": 0.039}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1664, "model_brier": 0.2151, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0087, "brier_diff_se": 0.0021, "model_logloss": 0.6193, "kalshi_logloss": 0.5957}, "gen1_elo": {"n": 5448, "model": {"intercept": -0.387, "slope": 0.994, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.306, "slope": 1.088, "slope_se": 0.038}, "mean_extremity_model": 0.1755, "mean_extremity_kalshi": 0.1666, "model_brier": 0.2137, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0072, "brier_diff_se": 0.0021, "model_logloss": 0.6165, "kalshi_logloss": 0.596}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.248, "share_ge_15": 0.4428, "median_abs_gap": 13.02, "n": 38615}, "gen1_elo": {"share_ge_25": 0.2463, "share_ge_15": 0.441, "median_abs_gap": 12.93, "n": 38615}, "gen1_sr": {"share_ge_25": 0.3135, "share_ge_15": 0.5206, "median_abs_gap": 15.88, "n": 38615}, "gen2": {"share_ge_25": 0.3166, "share_ge_15": 0.5107, "median_abs_gap": 15.48, "n": 38615}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1542, "share_ge_15": 0.356, "median_abs_gap": 10.77, "n": 29989}, "gen1_elo": {"share_ge_25": 0.1544, "share_ge_15": 0.3535, "median_abs_gap": 10.57, "n": 29988}, "gen1_sr": {"share_ge_25": 0.2195, "share_ge_15": 0.4427, "median_abs_gap": 13.03, "n": 29990}, "gen2": {"share_ge_25": 0.2358, "share_ge_15": 0.4421, "median_abs_gap": 12.95, "n": 29991}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0426, "share_ge_25_pregame_clean": 0.038}, "WTA": {"median_abs_gap_pregame_clean": 7.58, "share_ge_25_all": 0.0574, "share_ge_25_pregame_clean": 0.0499}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2368, "share_within_10pp_all": 0.4372, "share_within_10pp_pregame_clean": 0.489, "corr_model_vs_mid_pregame_clean": 0.8501}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 803, "model_brier": 0.1974, "kalshi_brier": 0.1979, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 953, "model_brier": 0.2222, "kalshi_brier": 0.2133, "brier_diff_model_minus_kalshi": 0.0089}, "15-25": {"n_settled": 1208, "model_brier": 0.2245, "kalshi_brier": 0.2124, "brier_diff_model_minus_kalshi": 0.012}, "25-40": {"n_settled": 706, "model_brier": 0.2244, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0174}, "3-5": {"n_settled": 489, "model_brier": 0.2058, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": -0.0005}, "40+": {"n_settled": 149, "model_brier": 0.2799, "kalshi_brier": 0.1899, "brier_diff_model_minus_kalshi": 0.09}, "5-10": {"n_settled": 1140, "model_brier": 0.2013, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": -0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.536, "slope": 0.803, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.19, "slope": 1.049, "slope_se": 0.038}, "n": 5448}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.488, "slope": 0.854, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.165, "slope": 1.054, "slope_se": 0.031}, "n": 7578}, "NO_SKILL:gen2|WTA": {"n_settled": 236, "model_brier": 0.2571, "kalshi_brier": 0.2366, "brier_diff_model_minus_kalshi": 0.0205, "brier_diff_se": 0.0102, "corr_model_outcome": 0.2159, "corr_kalshi_outcome": 0.2512}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 489, "model_brier": 0.3095, "kalshi_brier": 0.2375, "brier_diff_model_minus_kalshi": 0.0721, "brier_diff_se": 0.0136, "corr_model_outcome": 0.059, "corr_kalshi_outcome": 0.2351}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
