# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-06T22:06Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 81,147): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.1%; median gap 11.82 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.7%, doubles 6.8%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,577): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.2%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.5%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.2%, market_freshness 19.4%, execution 17.5%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,577 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.8% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 491.0 points vs 1724.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.03, Gen-2 0.823, Gen-1 ledger 0.867 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 900 model 0.2227 vs Kalshi 0.2052; n 186 model 0.2966 vs Kalshi 0.1748.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 344,077 model-market comparisons (563,740 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 114,574 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-06T21:47:26.074256+00:00'], shadow board 93,231 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-06T21:47:30.310015+00:00'], Model 4 42,425 rows, 28,605 settled tickers, 10,740 tickers with an external scan.
* By model: {"gen1_ledger": 77164, "gen1_elo": 46854, "fair_v1": 46854, "gen2": 46854, "gen1_sr": 46854, "model4_fundamental": 39790, "model4_conditioned": 39707}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 81,147 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.1 | 11.82 | 40.8% | 21.7% |
| MW fair_v1 | 46,854 | 12.9 | 8.7 | 18.8 | 15.4 | 19.6 | 14.8 | 9.9 | 13.03 | 44.4% | 24.7% |
| MW gen1_elo | 46,854 | 12.6 | 8.8 | 19.2 | 15.4 | 19.6 | 14.6 | 9.8 | 12.81 | 44.0% | 24.4% |
| MW gen1_ledger | 34,293 | 15.7 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| MW gen1_sr | 46,854 | 10.1 | 7.3 | 16.7 | 14.0 | 20.7 | 18.7 | 12.6 | 15.8 | 52.0% | 31.3% |
| MW gen2 | 46,854 | 11.0 | 7.6 | 16.6 | 13.7 | 19.7 | 17.7 | 13.7 | 15.45 | 51.0% | 31.4% |
| all families model4_conditioned | 39,707 | 22.2 | 18.0 | 34.1 | 17.2 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 39,790 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.1%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.38pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,937 | 28.6 | 15.7 | 27.6 | 13.4 | 10.6 | 3.6 | 0.6 | 5.77 | 14.8% | 4.2% |
| CHALLENGER | 7,021 | 16.2 | 9.7 | 20.7 | 15.2 | 16.1 | 11.3 | 10.7 | 10.91 | 38.1% | 22.1% |
| ITF_MEN | 13,284 | 9.8 | 7.3 | 17.1 | 15.1 | 21.3 | 17.2 | 12.2 | 15.24 | 50.7% | 29.4% |
| ITF_WOMEN | 18,244 | 9.6 | 7.1 | 16.1 | 14.8 | 22.2 | 18.3 | 12.1 | 15.83 | 52.5% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,035 | 16.8 | 13.2 | 24.7 | 20.9 | 16.6 | 6.8 | 1.1 | 8.68 | 24.6% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,937 | 26.9 | 15.8 | 26.1 | 15.4 | 11.4 | 3.7 | 0.8 | 6.02 | 15.8% | 4.5% |
| CHALLENGER | 7,021 | 14.7 | 9.1 | 18.9 | 13.9 | 18.6 | 13.4 | 11.4 | 12.47 | 43.4% | 24.9% |
| ITF_MEN | 13,284 | 8.2 | 6.1 | 15.1 | 13.8 | 20.0 | 20.5 | 16.4 | 17.94 | 56.8% | 36.8% |
| ITF_WOMEN | 18,244 | 7.8 | 5.9 | 14.1 | 12.8 | 20.8 | 21.1 | 17.5 | 19.08 | 59.4% | 38.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,035 | 14.1 | 10.2 | 21.6 | 16.1 | 22.4 | 12.9 | 2.5 | 11.28 | 37.9% | 15.5% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,937 | 22.8 | 14.1 | 25.3 | 15.6 | 14.9 | 6.1 | 1.2 | 7.14 | 22.2% | 7.3% |
| CHALLENGER | 7,021 | 15.1 | 9.5 | 20.7 | 15.7 | 16.2 | 11.8 | 10.9 | 11.32 | 38.9% | 22.7% |
| ITF_MEN | 13,284 | 9.5 | 7.3 | 17.3 | 14.2 | 21.9 | 17.2 | 12.5 | 15.65 | 51.7% | 29.8% |
| ITF_WOMEN | 18,244 | 9.3 | 6.9 | 16.3 | 15.7 | 22.2 | 18.2 | 11.4 | 15.57 | 51.8% | 29.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,035 | 22.8 | 17.1 | 31.9 | 15.2 | 8.7 | 3.3 | 1.1 | 6.12 | 13.1% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,338 | 26.9 | 19.8 | 30.0 | 12.2 | 8.2 | 2.6 | 0.4 | 5.34 | 11.2% | 3.0% |
| CHALLENGER | 4,533 | 22.4 | 14.6 | 27.6 | 14.9 | 13.4 | 5.7 | 1.5 | 7.08 | 20.6% | 7.2% |
| DOUBLES | 2,554 | 4.9 | 4.5 | 12.9 | 11.1 | 20.2 | 24.4 | 22.1 | 23.31 | 66.6% | 46.5% |
| ITF_MEN | 9,842 | 12.9 | 9.6 | 21.4 | 15.7 | 21.6 | 12.9 | 5.8 | 11.76 | 40.3% | 18.7% |
| ITF_WOMEN | 11,842 | 13.4 | 9.3 | 20.0 | 15.7 | 21.4 | 14.9 | 5.4 | 12.21 | 41.7% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,779 | 23.8 | 16.1 | 31.2 | 17.0 | 9.1 | 2.6 | 0.2 | 6.57 | 11.9% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,822 | 29.0 | 15.8 | 28.0 | 13.3 | 10.3 | 3.2 | 0.3 | 5.64 | 13.9% | 3.5% |
| CHALLENGER | 4,965 | 20.9 | 12.0 | 25.6 | 18.0 | 16.0 | 5.9 | 1.6 | 8.23 | 23.5% | 7.5% |
| ITF_MEN | 9,690 | 12.0 | 8.7 | 20.7 | 17.4 | 22.1 | 14.0 | 5.2 | 12.39 | 41.3% | 19.2% |
| ITF_WOMEN | 13,418 | 11.4 | 8.6 | 18.9 | 17.1 | 24.0 | 15.1 | 4.9 | 13.16 | 44.0% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,922 | 17.1 | 13.2 | 25.0 | 21.2 | 16.6 | 6.3 | 0.6 | 8.51 | 23.5% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,822 | 27.2 | 16.2 | 26.4 | 15.3 | 11.3 | 3.3 | 0.4 | 5.95 | 15.0% | 3.7% |
| CHALLENGER | 4,965 | 18.4 | 11.4 | 23.8 | 16.2 | 19.1 | 9.2 | 1.9 | 8.99 | 30.1% | 11.0% |
| ITF_MEN | 9,691 | 9.7 | 7.2 | 17.6 | 16.0 | 21.7 | 18.7 | 9.1 | 14.86 | 49.5% | 27.8% |
| ITF_WOMEN | 13,419 | 8.9 | 6.9 | 16.1 | 14.4 | 22.7 | 20.4 | 10.7 | 16.5 | 53.8% | 31.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,922 | 14.3 | 10.3 | 21.9 | 16.3 | 22.6 | 12.6 | 1.9 | 11.03 | 37.1% | 14.5% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,281 | 27.1 | 19.9 | 29.9 | 12.4 | 7.9 | 2.5 | 0.3 | 5.3 | 10.7% | 2.8% |
| CHALLENGER | 4,006 | 23.7 | 15.5 | 28.7 | 15.1 | 12.7 | 4.0 | 0.4 | 6.6 | 17.1% | 4.4% |
| DOUBLES | 2,398 | 4.8 | 4.5 | 13.1 | 11.1 | 20.0 | 24.3 | 22.1 | 23.23 | 66.4% | 46.4% |
| ITF_MEN | 8,455 | 13.7 | 10.2 | 23.0 | 16.2 | 21.7 | 11.3 | 3.8 | 10.83 | 36.8% | 15.2% |
| ITF_WOMEN | 10,144 | 14.0 | 9.8 | 21.1 | 16.2 | 21.6 | 13.8 | 3.5 | 11.41 | 38.9% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,717 | 24.2 | 16.5 | 31.3 | 16.9 | 9.0 | 2.0 | 0.1 | 6.43 | 11.1% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,554 | 4.9 | 4.5 | 12.9 | 11.1 | 20.2 | 24.4 | 22.1 | 23.31 | 66.6% | 46.5% |
| singles | 31,739 | 16.6 | 11.5 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.72 | 33.5% | 15.1% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 168 | 8.3 | 9.5 | 11.9 | 7.7 | 19.1 | 29.2 | 14.3 | 21.18 | 62.5% | 43.5% |
| Clay | 9,634 | 12.8 | 9.1 | 19.9 | 15.6 | 19.7 | 13.8 | 9.2 | 12.59 | 42.7% | 23.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,491 | 13.4 | 8.7 | 18.8 | 15.2 | 19.2 | 14.8 | 9.9 | 12.87 | 43.9% | 24.7% |
| UNKNOWN | 6,324 | 10.6 | 7.6 | 17.0 | 16.3 | 21.5 | 16.0 | 11.1 | 14.32 | 48.6% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,300 | 19.6 | 11.9 | 22.4 | 15.8 | 14.9 | 9.2 | 6.2 | 8.88 | 30.3% | 15.4% |
| B | 5,732 | 12.7 | 8.7 | 19.7 | 15.7 | 19.8 | 12.7 | 10.8 | 12.67 | 43.3% | 23.5% |
| C | 6,641 | 12.1 | 8.9 | 19.5 | 15.7 | 18.6 | 14.6 | 10.7 | 12.91 | 43.9% | 25.3% |
| D | 7,616 | 11.7 | 8.3 | 17.9 | 15.3 | 21.7 | 15.7 | 9.4 | 13.84 | 46.8% | 25.1% |
| F | 13,565 | 7.4 | 5.6 | 14.8 | 14.7 | 23.6 | 20.8 | 13.1 | 17.79 | 57.5% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,181 | 24.5 | 16.1 | 29.1 | 15.0 | 10.6 | 3.4 | 1.2 | 6.37 | 15.2% | 4.6% |
| B | 4,814 | 16.6 | 10.8 | 24.2 | 16.9 | 18.8 | 9.6 | 3.0 | 9.67 | 31.5% | 12.7% |
| C | 6,770 | 11.1 | 7.8 | 19.6 | 14.7 | 20.9 | 15.6 | 10.4 | 13.59 | 47.0% | 26.0% |
| D | 5,145 | 14.5 | 10.1 | 21.4 | 15.3 | 20.8 | 12.5 | 5.3 | 11.19 | 38.6% | 17.8% |
| F | 8,383 | 10.1 | 8.4 | 16.2 | 14.6 | 23.4 | 19.5 | 7.8 | 15.33 | 50.6% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,025 | 17.8 | 10.9 | 21.5 | 15.7 | 15.3 | 10.0 | 8.8 | 9.97 | 34.1% | 18.9% |
| LIMITED | 10,258 | 13.7 | 9.8 | 20.4 | 15.8 | 19.4 | 13.3 | 7.6 | 11.84 | 40.2% | 20.9% |
| POOR | 21,571 | 9.0 | 6.6 | 16.0 | 14.9 | 22.8 | 18.8 | 11.8 | 16.15 | 53.4% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,738 | 23.8 | 17.9 | 33.1 | 15.6 | 6.4 | 2.9 | 0.4 | 5.9 | 9.7% | 3.3% |
| GAME_SPREAD | 6,627 | 22.6 | 15.4 | 32.1 | 16.9 | 9.0 | 3.4 | 0.7 | 6.71 | 13.0% | 4.1% |
| MATCH_WINNER | 34,293 | 15.7 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,292 | 27.9 | 16.7 | 30.8 | 12.7 | 9.1 | 2.4 | 0.3 | 5.64 | 11.9% | 2.7% |
| TOTAL_GAMES | 11,190 | 9.8 | 10.8 | 35.6 | 26.0 | 10.7 | 4.2 | 2.9 | 9.19 | 17.8% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,020 | 24.5 | 28.9 | 33.2 | 8.1 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,162 | 47.0 | 16.1 | 24.7 | 7.5 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,525 | 6.6 | 9.9 | 40.2 | 30.2 | 7.4 | 3.3 | 2.4 | 9.21 | 13.2% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,055 | 23.9 | 16.7 | 34.8 | 14.7 | 6.9 | 2.6 | 0.5 | 6.04 | 10.0% | 3.1% |
| GAME_SPREAD | 9,171 | 20.6 | 13.6 | 28.2 | 20.0 | 11.9 | 4.4 | 1.2 | 7.6 | 17.5% | 5.6% |
| TOTAL_GAMES | 16,564 | 10.0 | 10.8 | 36.2 | 24.3 | 11.6 | 4.5 | 2.6 | 9.06 | 18.6% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 46,854 | 44.4% | 24.7% | 13.03 | 35.3% | 15.0% | 10.67 |
| gen1_elo | 46,854 | 44.0% | 24.4% | 12.81 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 46,854 | 52.0% | 31.3% | 15.8 | 43.9% | 21.6% | 12.97 |
| gen2 | 46,854 | 51.0% | 31.4% | 15.45 | 43.8% | 23.0% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,974 | 15.6 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 26,880 | 10.9 | 7.3 | 16.8 | 14.0 | 19.3 | 16.9 | 14.8 | 15.41 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 27,761 | 16.3 | 11.3 | 22.8 | 15.3 | 18.0 | 11.5 | 4.8 | 9.87 | 34.3% | 16.3% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 81,147 | 27761 | 23446 | 29940 | 24.8 | 126.9 | 1451.1 |
| ge_15pp | 33,100 | 9519 | 8353 | 15228 | 28.2 | 434.3 | 1451.1 |
| ge_25pp | 17,577 | 4531 | 3645 | 9401 | 33.1 | 581.5 | 1431.1 |
| lt_10pp | 35,639 | 14002 | 11092 | 10545 | 22.7 | 47.9 | 1421.1 |

Current slate `SL-20261106T220649Z-bbef89d5`: 150 priced rows, quote age at build {'median': 19.7, 'max': 19.7}, freshness {'AGING': 150}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,622 | 19.3 | 10.9 | 25.4 | 17.8 | 18.1 | 7.5 | 1.0 | 8.82 | 26.6% | 8.5% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 978 | 66.8 | 33.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,085 | 0.0 | 2.2 | 37.4 | 26.3 | 24.0 | 9.2 | 0.9 | 11.8 | 34.1% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 46,854 | 7793 (16.6%) | 26.8% | 1.0% | {"EXTERNAL_STALE": 4622, "AGREES_WITH_KALSHI": 2085, "ALL_AGREE": 978, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,782 | 1969 (9.5%) | 36.1% | 1.5% | {"EXTERNAL_STALE": 1228, "AGREES_WITH_KALSHI": 711, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,584 | 614 (5.3%) | 34.2% | 2.1% | {"EXTERNAL_STALE": 391, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,431 | 584 (10.8%) | 34.8% | 2.2% | {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,868 | 4447 (23.6%) | 18.6% | 1.0% | {"EXTERNAL_STALE": 2570, "ALL_AGREE": 978, "AGREES_WITH_KALSHI": 826, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,194 | 10.5 | 7.7 | 19.5 | 14.6 | 21.6 | 16.2 | 9.8 | 14.08 | 47.7% | 26.1% |
| 4-10x | 6,284 | 11.3 | 8.5 | 18.4 | 15.2 | 22.1 | 14.2 | 10.2 | 13.78 | 46.6% | 24.5% |
| <2x | 23,908 | 14.9 | 9.8 | 19.7 | 16.0 | 17.6 | 13.1 | 8.9 | 11.56 | 39.6% | 22.0% |
| >=10x | 7,468 | 10.4 | 6.4 | 15.0 | 14.4 | 21.8 | 18.9 | 13.1 | 16.38 | 53.7% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,291 | 12.4 | 8.6 | 19.9 | 16.1 | 19.1 | 13.5 | 10.4 | 12.72 | 42.9% | 23.9% |
| 300-1000 | 10,163 | 11.8 | 8.8 | 17.7 | 15.2 | 20.7 | 16.3 | 9.5 | 13.73 | 46.5% | 25.8% |
| <300 | 14,673 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 19.8 | 13.1 | 17.12 | 56.0% | 32.9% |
| >=3000 | 9,727 | 21.4 | 12.9 | 23.9 | 15.6 | 13.9 | 7.3 | 5.1 | 7.75 | 26.3% | 12.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1438 | 0.548 | 0.4091 | 0.4861 | +0.062 | -0.077 | 0.0014 ± 0.004 |
| ratio 4-10x | 976 | 0.5767 | 0.432 | 0.4887 | +0.088 | -0.057 | 0.0084 ± 0.0051 |
| ratio <2x | 3489 | 0.5364 | 0.4136 | 0.4377 | +0.099 | -0.024 | 0.0145 ± 0.0024 |
| ratio >=10x | 1201 | 0.5643 | 0.3917 | 0.448 | +0.116 | -0.056 | 0.0147 ± 0.0052 |
| thinner_sample 1000-3000 | 1970 | 0.539 | 0.412 | 0.4477 | +0.091 | -0.036 | 0.0115 ± 0.0033 |
| thinner_sample 300-1000 | 1616 | 0.5637 | 0.4234 | 0.474 | +0.090 | -0.051 | 0.0048 ± 0.0039 |
| thinner_sample <300 | 2301 | 0.5576 | 0.39 | 0.455 | +0.102 | -0.065 | 0.013 ± 0.0037 |
| thinner_sample >=3000 | 1217 | 0.5294 | 0.4356 | 0.4486 | +0.081 | -0.013 | 0.0148 ± 0.0033 |
| data_status ADEQUATE | 1964 | 0.5321 | 0.4289 | 0.4414 | +0.091 | -0.013 | 0.0152 ± 0.0028 |
| data_status LIMITED | 1735 | 0.5471 | 0.4149 | 0.4674 | +0.080 | -0.052 | 0.0071 ± 0.0036 |
| data_status POOR | 3405 | 0.5597 | 0.3998 | 0.459 | +0.101 | -0.059 | 0.0106 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1024 | 0.1974 | 0.1978 | -0.0004 ± 0.0005 | 0.5745 | 0.5754 | 0.5027 | 0.4875 | 0.5029 | -0.092 ± 0.0147 | -0.0087 (8) |
| 3-5 | 658 | 0.2047 | 0.2047 | -0.0000 ± 0.0014 | 0.5936 | 0.5921 | 0.5036 | 0.4638 | 0.4833 | -0.094 ± 0.0181 | 0.01 (2) |
| 5-10 | 1529 | 0.201 | 0.2002 | +0.0008 ± 0.0017 | 0.5881 | 0.5838 | 0.5113 | 0.4375 | 0.467 | -0.089 ± 0.0119 | -0.0143 (7) |
| 10-15 | 1231 | 0.2188 | 0.2095 | +0.0093 ± 0.0032 | 0.6295 | 0.6023 | 0.5233 | 0.3999 | 0.4232 | -0.105 ± 0.0133 | -0.048 (5) |
| 15-25 | 1576 | 0.2253 | 0.2077 | +0.0176 ± 0.0045 | 0.6457 | 0.5988 | 0.5752 | 0.3806 | 0.4327 | -0.104 ± 0.0115 | -0.0045 (11) |
| 25-40 | 900 | 0.2227 | 0.2052 | +0.0175 ± 0.009 | 0.6353 | 0.5914 | 0.6507 | 0.3409 | 0.4678 | -0.066 ± 0.0138 | -0.06 (2) |
| 40+ | 186 | 0.2966 | 0.1748 | +0.1217 ± 0.0275 | 0.7985 | 0.5224 | 0.73 | 0.2752 | 0.3763 | -0.084 ± 0.0267 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5377 | 0.1853 | 0.1862 | -0.0009 ± 0.0002 | 0.5466 | 0.5477 | 0.4903 | 0.475 | 0.5075 | -0.020 ± 0.006 | -0.01 (28) |
| 3-5 | 3594 | 0.1974 | 0.1958 | +0.0016 ± 0.0006 | 0.5749 | 0.569 | 0.4819 | 0.4421 | 0.4416 | -0.055 ± 0.0075 | 0.0 (3) |
| 5-10 | 7787 | 0.2007 | 0.1975 | +0.0031 ± 0.0008 | 0.5871 | 0.5761 | 0.4842 | 0.4105 | 0.4264 | -0.043 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6433 | 0.2021 | 0.1862 | +0.0159 ± 0.0013 | 0.5909 | 0.546 | 0.4852 | 0.3613 | 0.3591 | -0.064 ± 0.0054 | -0.0281 (16) |
| 15-25 | 8144 | 0.2061 | 0.1667 | +0.0394 ± 0.0018 | 0.6041 | 0.4955 | 0.4992 | 0.3037 | 0.3016 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6274 | 0.2229 | 0.1264 | +0.0965 ± 0.0028 | 0.6401 | 0.3884 | 0.5266 | 0.213 | 0.2201 | -0.058 ± 0.0044 | -0.0733 (3) |
| 40+ | 4171 | 0.3822 | 0.0439 | +0.3383 ± 0.0037 | 0.9957 | 0.1704 | 0.6304 | 0.1014 | 0.058 | -0.076 ± 0.0031 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 820 | 0.2043 | 0.2047 | -0.0004 ± 0.0005 | 0.5892 | 0.5904 | 0.507 | 0.4922 | 0.5146 | -0.103 ± 0.017 | -0.0117 (6) |
| 3-5 | 585 | 0.2107 | 0.2079 | +0.0028 ± 0.0015 | 0.6038 | 0.5979 | 0.5117 | 0.4721 | 0.453 | -0.129 ± 0.0203 | 0.01 (2) |
| 5-10 | 1315 | 0.2063 | 0.2046 | +0.0017 ± 0.0019 | 0.5987 | 0.594 | 0.5397 | 0.4651 | 0.4935 | -0.087 ± 0.0129 | -0.01 (4) |
| 10-15 | 1142 | 0.2126 | 0.2069 | +0.0057 ± 0.0034 | 0.6179 | 0.5995 | 0.5633 | 0.4389 | 0.4807 | -0.099 ± 0.0141 | -0.04 (5) |
| 15-25 | 1668 | 0.2317 | 0.2124 | +0.0193 ± 0.0044 | 0.6593 | 0.6093 | 0.5847 | 0.3891 | 0.4388 | -0.099 ± 0.0116 | -0.0118 (11) |
| 25-40 | 1158 | 0.2663 | 0.197 | +0.0693 ± 0.0082 | 0.7432 | 0.5739 | 0.6581 | 0.3439 | 0.3929 | -0.119 ± 0.013 | -0.008 (5) |
| 40+ | 416 | 0.3729 | 0.1618 | +0.2111 ± 0.0197 | 1.0165 | 0.4896 | 0.7351 | 0.2464 | 0.2885 | -0.088 ± 0.019 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4603 | 0.1918 | 0.192 | -0.0002 ± 0.0002 | 0.5591 | 0.5594 | 0.5072 | 0.4921 | 0.5084 | -0.039 ± 0.0067 | -0.0154 (26) |
| 3-5 | 3140 | 0.1926 | 0.1916 | +0.0010 ± 0.0006 | 0.5615 | 0.5583 | 0.5113 | 0.4716 | 0.4783 | -0.045 ± 0.008 | 0.01 (2) |
| 5-10 | 6939 | 0.1969 | 0.1936 | +0.0033 ± 0.0008 | 0.5788 | 0.5666 | 0.5086 | 0.4345 | 0.4518 | -0.040 ± 0.0053 | -0.0117 (6) |
| 10-15 | 5779 | 0.2025 | 0.1916 | +0.0109 ± 0.0014 | 0.5944 | 0.5602 | 0.5107 | 0.3867 | 0.4056 | -0.046 ± 0.0058 | -0.0189 (18) |
| 15-25 | 8211 | 0.217 | 0.1816 | +0.0354 ± 0.0019 | 0.6312 | 0.5324 | 0.5249 | 0.3294 | 0.3392 | -0.059 ± 0.0047 | -0.0094 (49) |
| 25-40 | 7368 | 0.2509 | 0.1369 | +0.1141 ± 0.0027 | 0.7088 | 0.4186 | 0.5593 | 0.2424 | 0.2245 | -0.081 ± 0.0043 | -0.0095 (20) |
| 40+ | 5740 | 0.4013 | 0.0585 | +0.3428 ± 0.0037 | 1.0581 | 0.2113 | 0.6539 | 0.1183 | 0.0796 | -0.074 ± 0.0031 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1001 | 0.1957 | 0.1972 | -0.0015 ± 0.0005 | 0.5711 | 0.5747 | 0.5028 | 0.4874 | 0.5345 | -0.050 ± 0.0147 | -0.012 (10) |
| 3-5 | 702 | 0.2068 | 0.2053 | +0.0016 ± 0.0014 | 0.5995 | 0.5943 | 0.4961 | 0.4565 | 0.4587 | -0.111 ± 0.0178 | -0.0 (4) |
| 5-10 | 1560 | 0.2022 | 0.1988 | +0.0034 ± 0.0017 | 0.5894 | 0.5797 | 0.5119 | 0.4381 | 0.4513 | -0.103 ± 0.0117 | -0.01 (10) |
| 10-15 | 1250 | 0.211 | 0.2017 | +0.0094 ± 0.0031 | 0.6125 | 0.5853 | 0.5366 | 0.4134 | 0.4392 | -0.108 ± 0.0128 | -0.0286 (7) |
| 15-25 | 1507 | 0.2314 | 0.2125 | +0.0189 ± 0.0046 | 0.6606 | 0.6093 | 0.5855 | 0.3914 | 0.4393 | -0.108 ± 0.0119 | -0.03 (1) |
| 25-40 | 889 | 0.2123 | 0.2101 | +0.0022 ± 0.009 | 0.6133 | 0.6026 | 0.659 | 0.3481 | 0.4983 | -0.052 ± 0.0139 | -0.0267 (3) |
| 40+ | 195 | 0.3097 | 0.1824 | +0.1274 ± 0.0275 | 0.8383 | 0.5387 | 0.7419 | 0.2873 | 0.3846 | -0.087 ± 0.0282 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5188 | 0.1855 | 0.1862 | -0.0007 ± 0.0002 | 0.5465 | 0.5474 | 0.4859 | 0.4706 | 0.4907 | -0.031 ± 0.0061 | -0.0137 (41) |
| 3-5 | 3695 | 0.2034 | 0.2017 | +0.0017 ± 0.0006 | 0.5914 | 0.5856 | 0.4781 | 0.4386 | 0.4376 | -0.055 ± 0.0075 | -0.01 (19) |
| 5-10 | 7940 | 0.1957 | 0.1906 | +0.0051 ± 0.0007 | 0.5746 | 0.5585 | 0.4871 | 0.4131 | 0.416 | -0.055 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6384 | 0.1936 | 0.1782 | +0.0154 ± 0.0013 | 0.572 | 0.5276 | 0.4942 | 0.3709 | 0.3701 | -0.063 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8241 | 0.2119 | 0.1722 | +0.0397 ± 0.0018 | 0.6178 | 0.5079 | 0.5121 | 0.3176 | 0.3136 | -0.071 ± 0.0046 | -0.0533 (3) |
| 25-40 | 6213 | 0.2166 | 0.1275 | +0.0891 ± 0.0028 | 0.6265 | 0.3904 | 0.529 | 0.2133 | 0.2323 | -0.047 ± 0.0044 | -0.02 (4) |
| 40+ | 4119 | 0.3915 | 0.049 | +0.3425 ± 0.0039 | 1.0205 | 0.1832 | 0.6399 | 0.1077 | 0.0651 | -0.076 ± 0.0033 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1430 | 0.1978 | 0.1979 | -0.0000 ± 0.0004 | 0.5741 | 0.574 | 0.5086 | 0.4936 | 0.4979 | -0.068 ± 0.012 | -0.0213 (54) |
| 3-5 | 1032 | 0.1882 | 0.188 | +0.0002 ± 0.0011 | 0.5542 | 0.552 | 0.4964 | 0.4565 | 0.4729 | -0.057 ± 0.0138 | -0.0194 (34) |
| 5-10 | 2081 | 0.1991 | 0.1944 | +0.0047 ± 0.0015 | 0.5874 | 0.5716 | 0.5072 | 0.4336 | 0.4392 | -0.076 ± 0.0099 | -0.005 (78) |
| 10-15 | 1437 | 0.2141 | 0.2017 | +0.0125 ± 0.0029 | 0.6216 | 0.5868 | 0.5423 | 0.4195 | 0.4287 | -0.090 ± 0.0122 | 0.0012 (66) |
| 15-25 | 1857 | 0.2307 | 0.207 | +0.0238 ± 0.0042 | 0.6589 | 0.5977 | 0.5903 | 0.3954 | 0.434 | -0.089 ± 0.0107 | -0.0214 (59) |
| 25-40 | 1123 | 0.2402 | 0.2102 | +0.0300 ± 0.0083 | 0.686 | 0.6034 | 0.6886 | 0.3765 | 0.4844 | -0.087 ± 0.0129 | -0.0252 (27) |
| 40+ | 397 | 0.3284 | 0.2014 | +0.1270 ± 0.0216 | 0.9461 | 0.5865 | 0.8163 | 0.3397 | 0.461 | -0.098 ± 0.0202 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5278 | 0.1779 | 0.178 | -0.0002 ± 0.0002 | 0.5261 | 0.5259 | 0.5114 | 0.4962 | 0.5068 | -0.038 ± 0.0058 | -0.0145 (98) |
| 3-5 | 3662 | 0.1951 | 0.1943 | +0.0008 ± 0.0006 | 0.5691 | 0.5665 | 0.501 | 0.4613 | 0.4711 | -0.040 ± 0.0074 | -0.0204 (72) |
| 5-10 | 7446 | 0.196 | 0.1896 | +0.0064 ± 0.0008 | 0.5787 | 0.5591 | 0.5008 | 0.4272 | 0.4218 | -0.062 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5110 | 0.2089 | 0.1929 | +0.0161 ± 0.0015 | 0.6086 | 0.5663 | 0.5368 | 0.4139 | 0.4086 | -0.071 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6192 | 0.2312 | 0.1998 | +0.0315 ± 0.0022 | 0.6646 | 0.5789 | 0.5762 | 0.3808 | 0.3989 | -0.067 ± 0.0057 | -0.026 (108) |
| 25-40 | 4049 | 0.2572 | 0.1902 | +0.0669 ± 0.0043 | 0.7277 | 0.554 | 0.6402 | 0.3276 | 0.3796 | -0.066 ± 0.0067 | -0.0246 (52) |
| 40+ | 1786 | 0.3722 | 0.1592 | +0.2130 ± 0.0098 | 1.0507 | 0.4742 | 0.7449 | 0.2437 | 0.2923 | -0.065 ± 0.009 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7104 | 1.03 ± 0.033 | 1.106 | 0.169 | 0.1691 | 0.2145 | 0.2035 |
| gen2 | 7104 | 0.823 ± 0.03 | 1.077 | 0.1733 | 0.1694 | 0.2329 | 0.2033 |
| gen1_elo | 7104 | 1.011 ± 0.032 | 1.094 | 0.1755 | 0.1692 | 0.2137 | 0.2036 |
| gen1_sr | 7104 | 1.009 ± 0.039 | 1.135 | 0.1333 | 0.1711 | 0.2292 | 0.203 |
| gen1_ledger | 9357 | 0.867 ± 0.024 | 1.078 | 0.1898 | 0.176 | 0.2167 | 0.2 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 33,100)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,632 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,499 | 22.7% |
| BOOK_QUALITY | execution | 5,924 | 17.9% |
| POOR_DATA | data | 3,841 | 11.6% |
| LIMITED_DATA | data | 2,059 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,915 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,375 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,360 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 946 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 548 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.7%, execution 17.9%, data 17.8%, market_freshness/coverage 8.6%, mapping 4.2%, model_calibration_or_unknown 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.8%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 46.0%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.1%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.1%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,577)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,004 | 34.2% |
| STALE_QUOTE | market_freshness | 3,405 | 19.4% |
| BOOK_QUALITY | execution | 3,072 | 17.5% |
| POOR_DATA | data | 1,616 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,021 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 764 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 620 | 3.5% |
| LIMITED_DATA | data | 603 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 336 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 135 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.2%, market_freshness 19.4%, execution 17.5%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 61.7%, STALE_KALSHI_QUOTE 53.5%, STALE_PLAYER_DATA 45.7%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 19.4%, PLAYER_IDENTITY_RISK 18.4%, EVENT_MAPPING_RISK 8.9%, LEVEL_TRANSFER_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.2%, POST_SETTLEMENT_OBSERVATION 34.2%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14021, "IDENTITY_AMBIGUOUS": 3556}; ticker orientation: {"VERIFIED": 17577}.

Checks: discipline:AMBIGUOUS 1187, discipline:PASS 16390, identity_confidence:AMBIGUOUS 3225, identity_confidence:PASS 14352, level_mapping:NA 1199, level_mapping:PASS 16378, market_pair:AMBIGUOUS 492, market_pair:NA 392, market_pair:PASS 16693, model_complement:NA 354, model_complement:PASS 17223, namesake:AMBIGUOUS 6, namesake:PASS 17571, physical_match_id:NA 5993, physical_match_id:PASS 11584, player_ids:PASS 17577, same_pair_other_event:PASS 17577, ticker_orientation:PASS 17577

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,275 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.52 | 0.2264 / 0.2216 (797) | 24.6% | 2.5% | 3.1% | 2.7% |
| CHALLENGER | 11,554 | 16.2% | 6.1% | 10.7% | {"coverage": 1110, "market_freshness/coverage": 220, "market_freshness": 218, "data": 157, "model_calibration_or_unknown": 78, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.36 | 0.2197 / 0.2096 (2714) | 37.8% | 15.2% | 4.1% | 22.4% |
| DOUBLES | 2,554 | 46.5% | 46.4% | 6.8% | {"execution": 664, "mapping": 343, "market_freshness": 106, "market_freshness/coverage": 67, "coverage": 7} | 23.23 | 0.2987 / 0.2327 (634) | 9.2% | 0.0% | 100.0% | 6.1% |
| ITF_MEN | 23,126 | 24.8% | 17.3% | 32.7% | {"coverage": 2013, "market_freshness": 1112, "execution": 979, "data": 842, "market_freshness/coverage": 584, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.66 | 0.2165 / 0.1988 (4902) | 39.9% | 68.8% | 15.1% | 21.5% |
| ITF_WOMEN | 30,086 | 26.4% | 18.9% | 45.2% | {"coverage": 2798, "market_freshness": 1708, "execution": 1305, "data": 1119, "market_freshness/coverage": 696, "mapping": 194, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.49 | 0.2027 / 0.1934 (5818) | 41.0% | 57.1% | 9.8% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,814 | 6.0% | 5.1% | 1.7% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.69 | 0.2292 / 0.22 (784) | 29.8% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 519 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 628 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 21.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1282 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 163 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.97, "by_level_share_of_ge_25pp": {"ATP": 0.0135, "CHALLENGER": 0.1068, "DOUBLES": 0.0675, "ITF_MEN": 0.3267, "ITF_WOMEN": 0.4516, "OTHER": 0.0007, "WTA": 0.0166, "WTA125": 0.0167}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5348, "share_primary_cause_market_settled_or_in_play": 0.435, "share_primary_cause_stale_quote_only": 0.1937}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17577, "identity_ambiguous_share": 0.2023, "ticker_orientation": {"VERIFIED": 17577}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11584, "with_external": 614, "coverage": 0.053, "external_status": {"EXTERNAL_STALE": 391, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 391, "MODEL_LONE_OUTLIER": 210, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.342, "share_external_supports_model": 0.0212}, "pregame_clean_ge_25pp": {"n": 5431, "with_external": 584, "coverage": 0.1075, "external_status": {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 368, "MODEL_LONE_OUTLIER": 203, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3476, "share_external_supports_model": 0.0223}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 491.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2082, "data_status": {"POOR": 9844, "LIMITED": 4568, "ADEQUATE": 3165}, "comparison_lt_10pp": {"median_thinner_serve_points": 1724.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1438, "model_minus_observed": 0.0619, "kalshi_minus_observed": -0.0769, "brier_diff_model_minus_kalshi": 0.0014}, "4-10x": {"n": 976, "model_minus_observed": 0.088, "kalshi_minus_observed": -0.0567, "brier_diff_model_minus_kalshi": 0.0084}, "<2x": {"n": 3489, "model_minus_observed": 0.0987, "kalshi_minus_observed": -0.0241, "brier_diff_model_minus_kalshi": 0.0145}, ">=10x": {"n": 1201, "model_minus_observed": 0.1164, "kalshi_minus_observed": -0.0563, "brier_diff_model_minus_kalshi": 0.0147}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7104, "model": {"intercept": -0.555, "slope": 0.823, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.185, "slope": 1.077, "slope_se": 0.034}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1694, "model_brier": 0.2329, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0296, "brier_diff_se": 0.0022, "model_logloss": 0.6634, "kalshi_logloss": 0.589}, "fair_v1": {"n": 7104, "model": {"intercept": -0.445, "slope": 1.03, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.254, "slope": 1.106, "slope_se": 0.034}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1691, "model_brier": 0.2145, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.011, "brier_diff_se": 0.0018, "model_logloss": 0.6181, "kalshi_logloss": 0.5892}, "gen1_elo": {"n": 7104, "model": {"intercept": -0.438, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.25, "slope": 1.094, "slope_se": 0.033}, "mean_extremity_model": 0.1755, "mean_extremity_kalshi": 0.1692, "model_brier": 0.2137, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0101, "brier_diff_se": 0.0018, "model_logloss": 0.6168, "kalshi_logloss": 0.5894}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2472, "share_ge_15": 0.4435, "median_abs_gap": 13.03, "n": 46854}, "gen1_elo": {"share_ge_25": 0.2441, "share_ge_15": 0.4396, "median_abs_gap": 12.81, "n": 46854}, "gen1_sr": {"share_ge_25": 0.3132, "share_ge_15": 0.5198, "median_abs_gap": 15.8, "n": 46854}, "gen2": {"share_ge_25": 0.3135, "share_ge_15": 0.5101, "median_abs_gap": 15.45, "n": 46854}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1504, "share_ge_15": 0.3529, "median_abs_gap": 10.67, "n": 36101}, "gen1_elo": {"share_ge_25": 0.1482, "share_ge_15": 0.3481, "median_abs_gap": 10.49, "n": 36101}, "gen1_sr": {"share_ge_25": 0.2157, "share_ge_15": 0.4388, "median_abs_gap": 12.97, "n": 36103}, "gen2": {"share_ge_25": 0.2303, "share_ge_15": 0.4382, "median_abs_gap": 12.83, "n": 36103}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0378, "share_ge_25_pregame_clean": 0.0326}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0604, "share_ge_25_pregame_clean": 0.0513}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.237, "share_within_10pp_all": 0.4392, "share_within_10pp_pregame_clean": 0.4923, "corr_model_vs_mid_pregame_clean": 0.8512}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1024, "model_brier": 0.1974, "kalshi_brier": 0.1978, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1231, "model_brier": 0.2188, "kalshi_brier": 0.2095, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 1576, "model_brier": 0.2253, "kalshi_brier": 0.2077, "brier_diff_model_minus_kalshi": 0.0176}, "25-40": {"n_settled": 900, "model_brier": 0.2227, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0175}, "3-5": {"n_settled": 658, "model_brier": 0.2047, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": -0.0}, "40+": {"n_settled": 186, "model_brier": 0.2966, "kalshi_brier": 0.1748, "brier_diff_model_minus_kalshi": 0.1217}, "5-10": {"n_settled": 1529, "model_brier": 0.201, "kalshi_brier": 0.2002, "brier_diff_model_minus_kalshi": 0.0008}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.555, "slope": 0.823, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.185, "slope": 1.077, "slope_se": 0.034}, "n": 7104}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.487, "slope": 0.867, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.174, "slope": 1.078, "slope_se": 0.029}, "n": 9357}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 634, "model_brier": 0.2987, "kalshi_brier": 0.2327, "brier_diff_model_minus_kalshi": 0.0659, "brier_diff_se": 0.0117, "corr_model_outcome": 0.098, "corr_kalshi_outcome": 0.2776}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
