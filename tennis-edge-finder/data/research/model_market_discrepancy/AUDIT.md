# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-26T14:32Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 56,121): 0-3 14.0%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 19.2%, 25-40 13.9%, 40+ 8.1%; median gap 11.98 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.1%, Challenger 11.9%, doubles 7.0%). Main tour: ATP 4.3% and WTA 5.5% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 12,336): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.8%, BOOK_QUALITY 18.9%, STALE_QUOTE 18.8%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.8%, execution 18.9%, market_freshness 18.8%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 12,336 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.4% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 476.0 points vs 1776.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.041, Gen-2 0.834, Gen-1 ledger 0.868 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 595 model 0.2214 vs Kalshi 0.2097; n 116 model 0.2743 vs Kalshi 0.202.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 247,278 model-market comparisons (399,291 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 83,154 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-26T14:17:06.977517+00:00'], shadow board 64,625 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-26T14:17:11.291834+00:00'], Model 4 32,060 rows, 20,854 settled tickers, 7,416 tickers with an external scan.
* By model: {"gen1_ledger": 56998, "gen1_elo": 32497, "fair_v1": 32497, "gen2": 32497, "gen1_sr": 32497, "model4_fundamental": 30168, "model4_conditioned": 30124}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 56,121 | 14.0 | 9.6 | 19.9 | 15.4 | 19.2 | 13.9 | 8.1 | 11.98 | 41.2% | 22.0% |
| MW fair_v1 | 32,497 | 12.9 | 8.7 | 18.6 | 15.6 | 19.7 | 14.9 | 9.7 | 13.06 | 44.3% | 24.6% |
| MW gen1_elo | 32,497 | 12.8 | 8.6 | 19.2 | 15.3 | 19.9 | 14.8 | 9.5 | 12.96 | 44.2% | 24.3% |
| MW gen1_ledger | 23,624 | 15.5 | 10.8 | 21.6 | 15.2 | 18.5 | 12.6 | 5.8 | 10.51 | 36.9% | 18.4% |
| MW gen1_sr | 32,497 | 10.2 | 7.1 | 17.0 | 13.6 | 20.7 | 18.6 | 12.7 | 15.89 | 52.0% | 31.3% |
| MW gen2 | 32,497 | 11.1 | 7.4 | 16.4 | 13.9 | 19.4 | 17.9 | 13.9 | 15.51 | 51.2% | 31.7% |
| all families model4_conditioned | 30,124 | 21.9 | 18.4 | 34.5 | 17.6 | 4.8 | 1.8 | 1.1 | 6.06 | 7.7% | 2.9% |
| all families model4_fundamental | 30,168 | 16.7 | 13.1 | 34.1 | 20.7 | 10.4 | 3.6 | 1.4 | 7.83 | 15.4% | 5.0% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.6%, >=15pp 41.2%, >=20pp 30.6%, >=25pp 22.0%, >=30pp 15.8%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.35pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,026 | 27.0 | 14.9 | 26.6 | 14.8 | 11.7 | 4.3 | 0.7 | 6.07 | 16.7% | 4.9% |
| CHALLENGER | 5,158 | 15.9 | 10.0 | 20.2 | 15.6 | 15.6 | 12.2 | 10.5 | 11.06 | 38.3% | 22.7% |
| ITF_MEN | 8,668 | 10.0 | 7.2 | 16.7 | 14.6 | 21.6 | 17.6 | 12.3 | 15.52 | 51.5% | 29.9% |
| ITF_WOMEN | 12,674 | 9.5 | 6.9 | 15.8 | 15.2 | 22.4 | 18.3 | 11.8 | 15.78 | 52.5% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,154 | 16.9 | 13.7 | 25.4 | 20.3 | 16.9 | 6.0 | 0.6 | 8.35 | 23.6% | 6.6% |
| WTA125 | 811 | 14.2 | 7.6 | 21.8 | 21.9 | 19.9 | 12.6 | 2.0 | 11.31 | 34.4% | 14.5% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,026 | 24.3 | 15.1 | 25.7 | 17.5 | 12.2 | 4.3 | 0.9 | 6.54 | 17.4% | 5.2% |
| CHALLENGER | 5,158 | 15.0 | 8.9 | 18.1 | 14.5 | 18.1 | 14.0 | 11.3 | 12.67 | 43.5% | 25.3% |
| ITF_MEN | 8,668 | 8.0 | 5.9 | 14.4 | 13.0 | 19.6 | 21.3 | 17.9 | 18.84 | 58.8% | 39.2% |
| ITF_WOMEN | 12,674 | 8.1 | 5.6 | 13.7 | 12.9 | 20.7 | 21.1 | 17.7 | 19.23 | 59.6% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,154 | 14.3 | 10.5 | 22.5 | 16.0 | 22.4 | 13.1 | 1.2 | 10.79 | 36.7% | 14.2% |
| WTA125 | 811 | 7.5 | 6.3 | 16.3 | 18.5 | 24.4 | 18.1 | 8.9 | 15.68 | 51.4% | 27.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,026 | 23.1 | 12.3 | 24.5 | 16.3 | 16.0 | 6.6 | 1.3 | 7.56 | 23.9% | 7.8% |
| CHALLENGER | 5,158 | 14.3 | 9.2 | 21.1 | 15.7 | 16.1 | 12.7 | 10.7 | 11.43 | 39.6% | 23.5% |
| ITF_MEN | 8,668 | 9.6 | 7.3 | 16.7 | 13.8 | 22.2 | 17.9 | 12.5 | 16.01 | 52.6% | 30.4% |
| ITF_WOMEN | 12,674 | 9.3 | 6.6 | 16.3 | 15.9 | 22.7 | 18.2 | 10.9 | 15.58 | 51.9% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,154 | 23.9 | 16.9 | 30.9 | 15.2 | 9.5 | 2.6 | 0.9 | 6.05 | 13.1% | 3.6% |
| WTA125 | 811 | 22.6 | 12.0 | 26.4 | 16.5 | 16.3 | 5.9 | 0.4 | 7.99 | 22.6% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,815 | 24.9 | 19.5 | 29.9 | 13.0 | 9.4 | 3.1 | 0.3 | 5.66 | 12.7% | 3.4% |
| CHALLENGER | 3,583 | 21.2 | 14.3 | 26.7 | 15.0 | 14.7 | 6.5 | 1.7 | 7.41 | 22.8% | 8.2% |
| DOUBLES | 1,817 | 5.2 | 4.5 | 12.2 | 10.2 | 20.2 | 25.7 | 21.9 | 24.04 | 67.9% | 47.6% |
| ITF_MEN | 6,423 | 13.5 | 9.2 | 19.9 | 16.1 | 21.5 | 13.4 | 6.5 | 12.22 | 41.4% | 19.9% |
| ITF_WOMEN | 7,710 | 12.7 | 8.9 | 19.3 | 15.4 | 21.6 | 16.2 | 6.0 | 12.8 | 43.8% | 22.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,279 | 23.1 | 15.6 | 30.3 | 17.9 | 9.6 | 3.1 | 0.3 | 6.82 | 13.1% | 3.4% |
| WTA125 | 848 | 21.2 | 13.6 | 21.8 | 18.5 | 14.5 | 8.4 | 2.0 | 8.35 | 24.9% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,946 | 27.3 | 15.2 | 27.0 | 14.7 | 11.5 | 3.9 | 0.4 | 5.94 | 15.8% | 4.3% |
| CHALLENGER | 3,655 | 20.6 | 12.4 | 24.8 | 18.0 | 15.7 | 6.7 | 1.7 | 8.34 | 24.1% | 8.4% |
| ITF_MEN | 6,336 | 12.1 | 8.7 | 20.1 | 16.5 | 22.8 | 14.4 | 5.3 | 12.67 | 42.5% | 19.7% |
| ITF_WOMEN | 9,519 | 11.2 | 8.2 | 18.0 | 17.2 | 24.3 | 15.5 | 5.5 | 13.56 | 45.2% | 21.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,093 | 17.1 | 13.6 | 25.5 | 20.5 | 16.9 | 5.7 | 0.6 | 8.28 | 23.3% | 6.3% |
| WTA125 | 785 | 14.5 | 7.5 | 21.4 | 22.3 | 20.4 | 12.2 | 1.7 | 11.31 | 34.3% | 13.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,946 | 24.5 | 15.4 | 26.0 | 17.4 | 12.2 | 4.0 | 0.5 | 6.46 | 16.7% | 4.5% |
| CHALLENGER | 3,655 | 19.1 | 11.2 | 22.3 | 17.3 | 18.4 | 9.7 | 1.9 | 9.32 | 30.1% | 11.6% |
| ITF_MEN | 6,337 | 9.6 | 7.0 | 16.8 | 15.0 | 21.5 | 19.4 | 10.7 | 15.53 | 51.6% | 30.1% |
| ITF_WOMEN | 9,520 | 9.2 | 6.4 | 15.2 | 14.3 | 22.7 | 20.7 | 11.4 | 16.89 | 54.8% | 32.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,093 | 14.3 | 10.6 | 22.6 | 16.0 | 22.5 | 12.9 | 1.2 | 10.79 | 36.5% | 14.1% |
| WTA125 | 785 | 7.4 | 6.5 | 16.3 | 18.9 | 24.3 | 18.5 | 8.2 | 15.35 | 51.0% | 26.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,764 | 25.0 | 19.8 | 29.9 | 13.2 | 9.0 | 3.0 | 0.2 | 5.6 | 12.1% | 3.1% |
| CHALLENGER | 3,146 | 22.6 | 15.3 | 28.0 | 15.1 | 14.1 | 4.5 | 0.5 | 6.92 | 19.1% | 5.0% |
| DOUBLES | 1,697 | 5.2 | 4.6 | 12.5 | 10.3 | 20.1 | 25.6 | 21.7 | 23.89 | 67.4% | 47.3% |
| ITF_MEN | 5,394 | 14.6 | 9.8 | 21.5 | 16.9 | 21.4 | 11.7 | 4.1 | 11.27 | 37.2% | 15.8% |
| ITF_WOMEN | 6,443 | 13.6 | 9.4 | 20.6 | 16.2 | 21.8 | 14.9 | 3.5 | 11.82 | 40.3% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,226 | 23.5 | 16.1 | 30.3 | 17.9 | 9.6 | 2.5 | 0.1 | 6.7 | 12.2% | 2.5% |
| WTA125 | 737 | 22.9 | 14.8 | 23.1 | 19.8 | 13.0 | 5.8 | 0.5 | 7.74 | 19.4% | 6.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,817 | 5.2 | 4.5 | 12.2 | 10.2 | 20.2 | 25.7 | 21.9 | 24.04 | 67.9% | 47.6% |
| singles | 21,807 | 16.3 | 11.3 | 22.4 | 15.6 | 18.4 | 11.5 | 4.5 | 9.97 | 34.3% | 16.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,105 | 12.8 | 9.1 | 19.6 | 15.9 | 19.0 | 14.1 | 9.5 | 12.64 | 42.6% | 23.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 20,444 | 13.4 | 8.8 | 18.5 | 15.2 | 19.8 | 14.8 | 9.4 | 12.99 | 44.0% | 24.3% |
| UNKNOWN | 4,699 | 10.9 | 7.5 | 17.0 | 16.7 | 20.5 | 16.3 | 11.2 | 14.12 | 48.0% | 27.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,421 | 19.6 | 12.2 | 21.9 | 16.4 | 14.8 | 9.1 | 6.0 | 8.87 | 29.9% | 15.1% |
| B | 4,008 | 12.3 | 8.8 | 19.5 | 16.4 | 19.6 | 12.8 | 10.8 | 12.64 | 43.1% | 23.5% |
| C | 4,501 | 11.8 | 9.1 | 19.4 | 15.6 | 19.3 | 14.5 | 10.3 | 13.0 | 44.1% | 24.8% |
| D | 4,943 | 12.1 | 7.8 | 17.4 | 15.4 | 21.8 | 15.6 | 9.9 | 13.98 | 47.3% | 25.5% |
| F | 9,624 | 7.5 | 5.6 | 15.0 | 14.5 | 23.8 | 21.2 | 12.5 | 17.79 | 57.5% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,771 | 23.4 | 16.1 | 28.8 | 15.2 | 11.3 | 4.0 | 1.3 | 6.58 | 16.6% | 5.3% |
| B | 3,181 | 16.2 | 10.3 | 23.2 | 16.4 | 19.9 | 10.4 | 3.6 | 10.05 | 33.9% | 14.0% |
| C | 4,634 | 10.9 | 7.2 | 18.7 | 14.4 | 21.1 | 16.6 | 11.1 | 14.34 | 48.7% | 27.6% |
| D | 3,227 | 14.3 | 9.7 | 20.1 | 15.2 | 20.9 | 13.9 | 5.8 | 11.86 | 40.7% | 19.7% |
| F | 5,811 | 10.1 | 8.3 | 15.6 | 15.1 | 22.8 | 20.1 | 8.0 | 15.41 | 50.8% | 28.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,718 | 17.8 | 11.0 | 21.2 | 16.1 | 15.4 | 10.0 | 8.5 | 9.99 | 33.9% | 18.5% |
| LIMITED | 6,868 | 13.5 | 10.2 | 20.1 | 16.2 | 19.4 | 13.2 | 7.4 | 11.77 | 40.0% | 20.6% |
| POOR | 14,911 | 9.1 | 6.4 | 15.9 | 14.9 | 23.0 | 19.1 | 11.6 | 16.26 | 53.8% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,858 | 24.8 | 18.7 | 33.4 | 14.4 | 6.1 | 2.4 | 0.3 | 5.68 | 8.8% | 2.7% |
| GAME_SPREAD | 5,417 | 22.4 | 15.4 | 33.3 | 16.8 | 9.1 | 2.6 | 0.4 | 6.69 | 12.0% | 2.9% |
| MATCH_WINNER | 23,624 | 15.5 | 10.8 | 21.6 | 15.2 | 18.5 | 12.6 | 5.8 | 10.51 | 36.9% | 18.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,297 | 28.0 | 16.4 | 31.0 | 12.6 | 9.4 | 2.3 | 0.3 | 5.68 | 12.0% | 2.6% |
| TOTAL_GAMES | 8,778 | 9.0 | 10.2 | 36.4 | 27.2 | 10.5 | 3.9 | 2.8 | 9.33 | 17.1% | 6.7% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,777 | 24.5 | 31.2 | 32.8 | 6.7 | 3.8 | 0.8 | 0.2 | 4.66 | 4.8% | 1.0% |
| GAME_SPREAD | 7,057 | 46.3 | 16.6 | 26.1 | 7.7 | 1.8 | 1.1 | 0.4 | 3.38 | 3.4% | 1.6% |
| TOTAL_GAMES | 12,290 | 5.5 | 8.2 | 40.9 | 32.9 | 7.3 | 3.1 | 2.3 | 9.51 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,788 | 23.6 | 16.9 | 35.2 | 14.2 | 7.2 | 2.5 | 0.4 | 6.03 | 10.1% | 2.9% |
| GAME_SPREAD | 7,060 | 19.5 | 13.1 | 28.2 | 21.2 | 12.7 | 4.2 | 1.0 | 7.92 | 17.9% | 5.2% |
| TOTAL_GAMES | 12,320 | 9.0 | 9.8 | 36.4 | 26.2 | 11.8 | 4.3 | 2.5 | 9.39 | 18.6% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 32,497 | 44.3% | 24.6% | 13.06 | 35.9% | 15.5% | 10.86 |
| gen1_elo | 32,497 | 44.2% | 24.3% | 12.96 | 35.8% | 15.5% | 10.7 |
| gen1_sr | 32,497 | 52.0% | 31.3% | 15.89 | 44.3% | 22.1% | 13.01 |
| gen2 | 32,497 | 51.2% | 31.7% | 15.51 | 44.4% | 23.8% | 13.02 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 16,374 | 15.6 | 10.6 | 21.4 | 17.3 | 20.1 | 11.8 | 3.3 | 10.68 | 35.2% | 15.1% |
| STALE | 16,123 | 10.2 | 6.8 | 15.7 | 13.8 | 19.3 | 18.0 | 16.2 | 16.58 | 53.5% | 34.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 17,092 | 16.4 | 11.3 | 22.4 | 15.3 | 17.8 | 12.0 | 4.9 | 9.99 | 34.6% | 16.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 56,121 | 17092 | 19846 | 19183 | 24.1 | 132.3 | 1400.4 |
| ge_15pp | 23,114 | 5923 | 7054 | 10137 | 26.2 | 434.7 | 1380.4 |
| ge_25pp | 12,336 | 2888 | 3066 | 6382 | 31.5 | 575.6 | 1380.4 |
| lt_10pp | 24,369 | 8550 | 9410 | 6409 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261026T143243Z-fbed786f`: 572 priced rows, quote age at build {'median': 16.0, 'max': 16.1}, freshness {'AGING': 572}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 28 | 0.0 | 0.0 | 21.4 | 10.7 | 39.3 | 28.6 | 0.0 | 20.48 | 67.9% | 28.6% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,145 | 19.4 | 11.3 | 25.0 | 18.9 | 17.9 | 7.0 | 0.6 | 8.77 | 25.5% | 7.6% |
| KALSHI_LONE_OUTLIER | 21 | 4.8 | 4.8 | 76.2 | 4.8 | 4.8 | 4.8 | 0.0 | 6.11 | 9.5% | 4.8% |
| MARKETS_AGREE | 645 | 65.1 | 34.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,385 | 0.0 | 2.6 | 35.0 | 26.7 | 24.9 | 10.1 | 0.7 | 12.02 | 35.7% | 10.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 32,497 | 5242 (16.1%) | 26.4% | 0.9% | {"EXTERNAL_STALE": 3145, "AGREES_WITH_KALSHI": 1385, "ALL_AGREE": 645, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 21, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 14,392 | 1317 (9.2%) | 37.5% | 1.6% | {"EXTERNAL_STALE": 802, "AGREES_WITH_KALSHI": 494, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,986 | 397 (5.0%) | 37.5% | 2.3% | {"EXTERNAL_STALE": 239, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,921 | 374 (9.5%) | 38.0% | 2.4% | {"EXTERNAL_STALE": 223, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 13,050 | 2958 (22.7%) | 17.6% | 0.8% | {"EXTERNAL_STALE": 1750, "ALL_AGREE": 645, "AGREES_WITH_KALSHI": 521, "EXTERNAL_OUTLIER": 18, "AGREES_WITH_MODEL": 18, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,215 | 10.2 | 7.6 | 19.4 | 14.6 | 22.4 | 15.9 | 9.8 | 14.09 | 48.1% | 25.7% |
| 4-10x | 4,190 | 11.1 | 8.5 | 18.6 | 15.4 | 22.1 | 14.7 | 9.7 | 13.76 | 46.4% | 24.4% |
| <2x | 16,623 | 15.1 | 10.0 | 19.3 | 16.4 | 17.4 | 12.9 | 8.8 | 11.61 | 39.2% | 21.8% |
| >=10x | 5,469 | 10.6 | 6.2 | 15.2 | 14.2 | 21.9 | 19.8 | 12.2 | 16.5 | 53.9% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,286 | 12.7 | 8.6 | 19.3 | 16.2 | 19.0 | 13.7 | 10.5 | 12.84 | 43.2% | 24.2% |
| 300-1000 | 6,805 | 11.8 | 8.7 | 17.4 | 15.3 | 20.8 | 16.1 | 9.9 | 13.81 | 46.8% | 26.0% |
| <300 | 10,554 | 8.4 | 5.7 | 15.3 | 14.7 | 23.4 | 20.2 | 12.3 | 17.02 | 55.9% | 32.5% |
| >=3000 | 6,852 | 21.1 | 13.4 | 23.7 | 16.4 | 13.9 | 6.9 | 4.5 | 7.73 | 25.3% | 11.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 915 | 0.5513 | 0.4133 | 0.5049 | +0.046 | -0.092 | -0.0041 ± 0.0051 |
| ratio 4-10x | 619 | 0.5898 | 0.4444 | 0.504 | +0.086 | -0.060 | 0.0088 ± 0.0064 |
| ratio <2x | 2264 | 0.5393 | 0.4161 | 0.4488 | +0.090 | -0.033 | 0.0114 ± 0.003 |
| ratio >=10x | 830 | 0.5708 | 0.3958 | 0.4614 | +0.109 | -0.066 | 0.0081 ± 0.0063 |
| thinner_sample 1000-3000 | 1259 | 0.5427 | 0.4159 | 0.4527 | +0.090 | -0.037 | 0.009 ± 0.004 |
| thinner_sample 300-1000 | 1034 | 0.5677 | 0.4244 | 0.4942 | +0.073 | -0.070 | 0.0002 ± 0.005 |
| thinner_sample <300 | 1561 | 0.563 | 0.3967 | 0.4676 | +0.095 | -0.071 | 0.0085 ± 0.0045 |
| thinner_sample >=3000 | 774 | 0.5363 | 0.4422 | 0.4677 | +0.069 | -0.025 | 0.0121 ± 0.0042 |
| data_status ADEQUATE | 1338 | 0.5381 | 0.434 | 0.4529 | +0.085 | -0.019 | 0.0115 ± 0.0034 |
| data_status LIMITED | 1067 | 0.5516 | 0.4181 | 0.4873 | +0.064 | -0.069 | 0.0026 ± 0.0046 |
| data_status POOR | 2223 | 0.5649 | 0.4036 | 0.471 | +0.094 | -0.067 | 0.0072 ± 0.0037 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 675 | 0.2018 | 0.2026 | -0.0008 ± 0.0006 | 0.5846 | 0.5865 | 0.5019 | 0.4871 | 0.5215 | -0.074 ± 0.0182 | -0.01 (5) |
| 3-5 | 424 | 0.2053 | 0.2046 | +0.0007 ± 0.0018 | 0.5938 | 0.5907 | 0.5041 | 0.4641 | 0.4741 | -0.107 ± 0.0226 | 0.02 (1) |
| 5-10 | 959 | 0.202 | 0.2024 | -0.0004 ± 0.0022 | 0.5905 | 0.5886 | 0.5149 | 0.441 | 0.4755 | -0.088 ± 0.015 | -0.0167 (6) |
| 10-15 | 807 | 0.2157 | 0.2067 | +0.0089 ± 0.004 | 0.622 | 0.5959 | 0.5325 | 0.4084 | 0.4337 | -0.106 ± 0.016 | -0.048 (5) |
| 15-25 | 1052 | 0.2247 | 0.2131 | +0.0116 ± 0.0056 | 0.6447 | 0.6097 | 0.5781 | 0.3823 | 0.4506 | -0.095 ± 0.0142 | -0.0033 (9) |
| 25-40 | 595 | 0.2214 | 0.2097 | +0.0117 ± 0.0112 | 0.6321 | 0.6026 | 0.6588 | 0.3488 | 0.4824 | -0.071 ± 0.0171 | -0.01 (1) |
| 40+ | 116 | 0.2743 | 0.202 | +0.0723 ± 0.036 | 0.7526 | 0.5904 | 0.7587 | 0.3114 | 0.4569 | -0.070 ± 0.0354 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3481 | 0.1849 | 0.1858 | -0.0009 ± 0.0003 | 0.5455 | 0.5465 | 0.4913 | 0.4762 | 0.5085 | -0.023 ± 0.0074 | -0.0129 (17) |
| 3-5 | 2305 | 0.2005 | 0.199 | +0.0015 ± 0.0008 | 0.582 | 0.5759 | 0.486 | 0.4461 | 0.4469 | -0.056 ± 0.0094 | 0.0 (2) |
| 5-10 | 4975 | 0.1985 | 0.1953 | +0.0032 ± 0.0009 | 0.5816 | 0.5702 | 0.4839 | 0.41 | 0.4243 | -0.048 ± 0.0063 | -0.0119 (21) |
| 10-15 | 4240 | 0.1981 | 0.1804 | +0.0177 ± 0.0016 | 0.5817 | 0.532 | 0.4887 | 0.3642 | 0.3554 | -0.073 ± 0.0065 | -0.0281 (16) |
| 15-25 | 5370 | 0.2082 | 0.1688 | +0.0394 ± 0.0022 | 0.6098 | 0.4994 | 0.5039 | 0.3073 | 0.3067 | -0.074 ± 0.0056 | -0.0025 (44) |
| 25-40 | 4180 | 0.2228 | 0.1286 | +0.0943 ± 0.0035 | 0.6398 | 0.3936 | 0.5317 | 0.2183 | 0.2282 | -0.060 ± 0.0054 | -0.01 (1) |
| 40+ | 2674 | 0.3791 | 0.0452 | +0.3339 ± 0.0046 | 0.9873 | 0.1739 | 0.6318 | 0.1063 | 0.0639 | -0.078 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 533 | 0.2086 | 0.2093 | -0.0007 ± 0.0007 | 0.5995 | 0.6012 | 0.5077 | 0.4926 | 0.5178 | -0.105 ± 0.0214 | -0.01 (3) |
| 3-5 | 382 | 0.2282 | 0.2254 | +0.0029 ± 0.002 | 0.6433 | 0.6375 | 0.5138 | 0.474 | 0.4529 | -0.134 ± 0.0259 | 0.02 (1) |
| 5-10 | 829 | 0.2069 | 0.2065 | +0.0005 ± 0.0024 | 0.6002 | 0.5986 | 0.5473 | 0.4725 | 0.5103 | -0.084 ± 0.0163 | -0.01 (4) |
| 10-15 | 766 | 0.2154 | 0.2093 | +0.0061 ± 0.0041 | 0.6198 | 0.6041 | 0.5651 | 0.4409 | 0.4804 | -0.106 ± 0.0172 | -0.04 (5) |
| 15-25 | 1077 | 0.2285 | 0.2104 | +0.0182 ± 0.0055 | 0.6496 | 0.603 | 0.5885 | 0.3928 | 0.4485 | -0.100 ± 0.0143 | -0.0133 (9) |
| 25-40 | 759 | 0.2652 | 0.1984 | +0.0668 ± 0.0102 | 0.7418 | 0.5779 | 0.6561 | 0.3411 | 0.3953 | -0.120 ± 0.0159 | -0.0075 (4) |
| 40+ | 282 | 0.3529 | 0.1747 | +0.1782 ± 0.0245 | 0.9703 | 0.5206 | 0.734 | 0.2505 | 0.3227 | -0.066 ± 0.0238 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2966 | 0.1947 | 0.1949 | -0.0002 ± 0.0003 | 0.5659 | 0.5663 | 0.5128 | 0.4979 | 0.5108 | -0.046 ± 0.0084 | -0.0133 (15) |
| 3-5 | 1983 | 0.2016 | 0.2002 | +0.0015 ± 0.0008 | 0.5819 | 0.578 | 0.5146 | 0.4748 | 0.4755 | -0.054 ± 0.0103 | 0.02 (1) |
| 5-10 | 4404 | 0.1973 | 0.195 | +0.0023 ± 0.001 | 0.5806 | 0.5697 | 0.5117 | 0.4377 | 0.4623 | -0.036 ± 0.0067 | -0.0117 (6) |
| 10-15 | 3819 | 0.201 | 0.1891 | +0.0118 ± 0.0018 | 0.59 | 0.5515 | 0.5147 | 0.3908 | 0.4056 | -0.055 ± 0.0071 | -0.0189 (18) |
| 15-25 | 5318 | 0.2153 | 0.1778 | +0.0374 ± 0.0023 | 0.6256 | 0.523 | 0.5251 | 0.3293 | 0.3357 | -0.067 ± 0.0058 | -0.0086 (42) |
| 25-40 | 4889 | 0.2522 | 0.137 | +0.1153 ± 0.0034 | 0.7096 | 0.4206 | 0.5593 | 0.2423 | 0.2215 | -0.087 ± 0.0053 | -0.0044 (18) |
| 40+ | 3846 | 0.3929 | 0.0605 | +0.3324 ± 0.0045 | 1.0337 | 0.216 | 0.6505 | 0.1187 | 0.0853 | -0.071 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 648 | 0.1997 | 0.2019 | -0.0022 ± 0.0006 | 0.5802 | 0.5856 | 0.502 | 0.4867 | 0.5509 | -0.032 ± 0.0183 | -0.0137 (8) |
| 3-5 | 460 | 0.2026 | 0.2011 | +0.0014 ± 0.0017 | 0.5884 | 0.5835 | 0.507 | 0.4673 | 0.4717 | -0.117 ± 0.0218 | 0.0067 (3) |
| 5-10 | 985 | 0.2028 | 0.1997 | +0.0031 ± 0.0022 | 0.592 | 0.5814 | 0.511 | 0.437 | 0.4518 | -0.103 ± 0.0146 | -0.0071 (7) |
| 10-15 | 800 | 0.2082 | 0.2048 | +0.0034 ± 0.004 | 0.6052 | 0.5919 | 0.5418 | 0.4182 | 0.4675 | -0.089 ± 0.0159 | -0.0317 (6) |
| 15-25 | 991 | 0.2308 | 0.2142 | +0.0165 ± 0.0057 | 0.6593 | 0.612 | 0.5883 | 0.3938 | 0.448 | -0.107 ± 0.0147 | -0.03 (1) |
| 25-40 | 620 | 0.2138 | 0.2175 | -0.0037 ± 0.011 | 0.617 | 0.6206 | 0.6688 | 0.3579 | 0.5161 | -0.055 ± 0.0168 | 0.015 (2) |
| 40+ | 124 | 0.2877 | 0.2134 | +0.0743 ± 0.036 | 0.7955 | 0.6147 | 0.767 | 0.3181 | 0.4677 | -0.064 ± 0.038 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3406 | 0.1861 | 0.1868 | -0.0007 ± 0.0003 | 0.5472 | 0.5484 | 0.4891 | 0.4739 | 0.4932 | -0.034 ± 0.0075 | -0.0163 (35) |
| 3-5 | 2321 | 0.1972 | 0.1951 | +0.0021 ± 0.0007 | 0.5776 | 0.5709 | 0.4891 | 0.4495 | 0.4442 | -0.065 ± 0.0094 | -0.0094 (18) |
| 5-10 | 5078 | 0.1955 | 0.1899 | +0.0056 ± 0.0009 | 0.5746 | 0.5561 | 0.4841 | 0.4101 | 0.41 | -0.060 ± 0.0062 | -0.01 (31) |
| 10-15 | 4106 | 0.1913 | 0.1766 | +0.0147 ± 0.0016 | 0.5661 | 0.522 | 0.5002 | 0.3768 | 0.3782 | -0.064 ± 0.0066 | -0.015 (12) |
| 15-25 | 5495 | 0.2106 | 0.1713 | +0.0393 ± 0.0022 | 0.6155 | 0.5055 | 0.5134 | 0.3182 | 0.3157 | -0.074 ± 0.0056 | -0.03 (2) |
| 25-40 | 4207 | 0.2196 | 0.1319 | +0.0877 ± 0.0035 | 0.6335 | 0.4009 | 0.5362 | 0.2204 | 0.241 | -0.052 ± 0.0054 | 0.01 (3) |
| 40+ | 2612 | 0.3932 | 0.0507 | +0.3425 ± 0.005 | 1.0275 | 0.1881 | 0.6445 | 0.1135 | 0.0704 | -0.079 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1034 | 0.1963 | 0.1964 | -0.0001 ± 0.0005 | 0.5723 | 0.572 | 0.502 | 0.487 | 0.4913 | -0.064 ± 0.014 | -0.0224 (49) |
| 3-5 | 715 | 0.1927 | 0.1919 | +0.0008 ± 0.0013 | 0.563 | 0.5598 | 0.491 | 0.4512 | 0.4587 | -0.062 ± 0.0167 | -0.0194 (34) |
| 5-10 | 1508 | 0.2019 | 0.1962 | +0.0056 ± 0.0017 | 0.5928 | 0.5749 | 0.4971 | 0.4237 | 0.4231 | -0.074 ± 0.0116 | -0.005 (78) |
| 10-15 | 1014 | 0.2097 | 0.1981 | +0.0117 ± 0.0035 | 0.6085 | 0.5781 | 0.5261 | 0.4031 | 0.4152 | -0.072 ± 0.0143 | 0.0014 (64) |
| 15-25 | 1349 | 0.2315 | 0.2109 | +0.0206 ± 0.0049 | 0.6609 | 0.6068 | 0.5791 | 0.3844 | 0.4307 | -0.075 ± 0.0125 | -0.0214 (59) |
| 25-40 | 821 | 0.2443 | 0.2093 | +0.0350 ± 0.0098 | 0.6968 | 0.6006 | 0.678 | 0.3655 | 0.4653 | -0.084 ± 0.0149 | -0.0219 (26) |
| 40+ | 270 | 0.3441 | 0.2026 | +0.1415 ± 0.0268 | 0.9951 | 0.5926 | 0.8095 | 0.3289 | 0.4407 | -0.089 ± 0.0246 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3429 | 0.1823 | 0.1825 | -0.0002 ± 0.0003 | 0.5373 | 0.5368 | 0.503 | 0.4878 | 0.4969 | -0.041 ± 0.0073 | -0.0157 (88) |
| 3-5 | 2389 | 0.1962 | 0.1942 | +0.0021 ± 0.0007 | 0.5717 | 0.5668 | 0.4986 | 0.4588 | 0.4529 | -0.057 ± 0.0091 | -0.0209 (69) |
| 5-10 | 4808 | 0.1957 | 0.1877 | +0.0080 ± 0.0009 | 0.577 | 0.5528 | 0.4929 | 0.4194 | 0.4045 | -0.071 ± 0.0063 | -0.0082 (132) |
| 10-15 | 3362 | 0.2064 | 0.1908 | +0.0155 ± 0.0019 | 0.6014 | 0.56 | 0.5297 | 0.4067 | 0.4042 | -0.065 ± 0.0076 | -0.0053 (105) |
| 15-25 | 4176 | 0.2304 | 0.1997 | +0.0307 ± 0.0027 | 0.664 | 0.5787 | 0.5691 | 0.3734 | 0.3944 | -0.067 ± 0.0069 | -0.0253 (107) |
| 25-40 | 2837 | 0.2578 | 0.1862 | +0.0715 ± 0.0051 | 0.7314 | 0.5428 | 0.6341 | 0.3207 | 0.3655 | -0.076 ± 0.0079 | -0.0229 (51) |
| 40+ | 1236 | 0.3736 | 0.1468 | +0.2268 ± 0.0114 | 1.0583 | 0.4418 | 0.7323 | 0.229 | 0.2686 | -0.069 ± 0.0102 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4628 | 1.041 ± 0.041 | 1.115 | 0.1683 | 0.163 | 0.2141 | 0.2067 |
| gen2 | 4628 | 0.834 ± 0.038 | 1.081 | 0.1685 | 0.1636 | 0.2338 | 0.2065 |
| gen1_elo | 4628 | 1.014 ± 0.04 | 1.113 | 0.1748 | 0.1632 | 0.213 | 0.2069 |
| gen1_sr | 4628 | 1.02 ± 0.05 | 1.148 | 0.1294 | 0.1655 | 0.2302 | 0.206 |
| gen1_ledger | 6711 | 0.868 ± 0.029 | 1.07 | 0.1839 | 0.1769 | 0.2181 | 0.2009 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 23,114)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,196 | 22.5% |
| STALE_QUOTE | market_freshness | 5,027 | 21.8% |
| BOOK_QUALITY | execution | 4,443 | 19.2% |
| POOR_DATA | data | 2,587 | 11.2% |
| LIMITED_DATA | data | 1,433 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,252 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,096 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 986 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 680 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 413 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.5%, market_freshness 21.8%, execution 19.2%, data 17.4%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.3%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 93.9%, LOW_DATA_QUALITY 70.8%, THIN_PLAYER_HISTORY 59.7%, STALE_PLAYER_DATA 50.0%, STALE_KALSHI_QUOTE 43.9%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.3%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.6%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.9%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 12,336)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,169 | 33.8% |
| BOOK_QUALITY | execution | 2,332 | 18.9% |
| STALE_QUOTE | market_freshness | 2,321 | 18.8% |
| POOR_DATA | data | 1,066 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 668 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 545 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 432 | 3.5% |
| LIMITED_DATA | data | 429 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 276 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 97 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.8%, execution 18.9%, market_freshness 18.8%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.3%, THIN_PLAYER_HISTORY 61.8%, STALE_KALSHI_QUOTE 51.7%, STALE_PLAYER_DATA 44.6%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.8%, PLAYER_IDENTITY_RISK 20.1%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.9%, POST_SETTLEMENT_OBSERVATION 33.8%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9553, "IDENTITY_AMBIGUOUS": 2783}; ticker orientation: {"VERIFIED": 12336}.

Checks: discipline:AMBIGUOUS 865, discipline:PASS 11471, identity_confidence:AMBIGUOUS 2476, identity_confidence:PASS 9860, level_mapping:NA 877, level_mapping:PASS 11459, market_pair:AMBIGUOUS 465, market_pair:NA 302, market_pair:PASS 11569, model_complement:NA 269, model_complement:PASS 12067, namesake:AMBIGUOUS 6, namesake:PASS 12330, physical_match_id:NA 4350, physical_match_id:PASS 7986, player_ids:PASS 12336, same_pair_other_event:PASS 12336, ticker_orientation:PASS 12336

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,841 | 4.3% | 3.9% | 1.7% | {"market_freshness": 54, "model_calibration_or_unknown": 48, "data": 36, "execution": 24, "model_calibration": 20, "market_freshness/coverage": 15, "coverage": 13} | 5.87 | 0.2239 / 0.2208 (539) | 19.9% | 3.2% | 3.3% | 2.7% |
| CHALLENGER | 8,741 | 16.7% | 6.8% | 11.9% | {"coverage": 819, "market_freshness/coverage": 179, "market_freshness": 164, "data": 144, "model_calibration_or_unknown": 70, "execution": 35, "model_calibration": 35, "mapping": 16, "possible_market_error": 1} | 7.6 | 0.2182 / 0.2086 (2051) | 34.2% | 17.2% | 4.1% | 22.2% |
| DOUBLES | 1,817 | 47.6% | 47.3% | 7.0% | {"execution": 481, "mapping": 216, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.89 | 0.3088 / 0.2362 (441) | 12.9% | 0.0% | 100.0% | 6.6% |
| ITF_MEN | 15,091 | 25.6% | 17.9% | 31.4% | {"coverage": 1433, "execution": 739, "market_freshness": 667, "data": 513, "market_freshness/coverage": 338, "mapping": 176, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.99 | 0.2164 / 0.1985 (3351) | 37.4% | 70.3% | 19.8% | 22.3% |
| ITF_WOMEN | 20,384 | 27.1% | 20.0% | 44.8% | {"coverage": 1872, "market_freshness": 1217, "execution": 1002, "data": 758, "market_freshness/coverage": 463, "mapping": 131, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.89 | 0.2026 / 0.1957 (3872) | 39.5% | 57.2% | 10.4% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,433 | 5.5% | 4.9% | 1.5% | {"market_freshness": 66, "model_calibration_or_unknown": 39, "execution": 26, "model_calibration": 16, "data": 16, "coverage": 12, "market_freshness/coverage": 11, "mapping": 1} | 7.67 | 0.2318 / 0.2259 (541) | 24.9% | 1.2% | 1.5% | 3.3% |
| WTA125 | 1,659 | 12.4% | 10.2% | 1.7% | {"model_calibration_or_unknown": 46, "market_freshness": 45, "market_freshness/coverage": 38, "data": 28, "execution": 20, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.52 | 0.2178 / 0.2042 (502) | 23.7% | 11.5% | 6.5% | 8.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9678, "by_level_share_of_ge_25pp": {"ATP": 0.017, "CHALLENGER": 0.1186, "DOUBLES": 0.0701, "ITF_MEN": 0.3137, "ITF_WOMEN": 0.4477, "OTHER": 0.001, "WTA": 0.0152, "WTA125": 0.0167}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5173, "share_primary_cause_market_settled_or_in_play": 0.4272, "share_primary_cause_stale_quote_only": 0.1881}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 12336, "identity_ambiguous_share": 0.2256, "ticker_orientation": {"VERIFIED": 12336}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7986, "with_external": 397, "coverage": 0.0497, "external_status": {"EXTERNAL_STALE": 239, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 239, "MODEL_LONE_OUTLIER": 149, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3753, "share_external_supports_model": 0.0227}, "pregame_clean_ge_25pp": {"n": 3921, "with_external": 374, "coverage": 0.0954, "external_status": {"EXTERNAL_STALE": 223, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 223, "MODEL_LONE_OUTLIER": 142, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3797, "share_external_supports_model": 0.0241}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 476.0, "median_sample_ratio": 2.43, "median_min_matches": 20.0, "median_max_days_since_last": 231.0, "share_severe_asymmetry": 0.2164, "data_status": {"POOR": 6873, "LIMITED": 3213, "ADEQUATE": 2250}, "comparison_lt_10pp": {"median_thinner_serve_points": 1776.0, "median_sample_ratio": 1.67, "median_min_matches": 98.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 915, "model_minus_observed": 0.0464, "kalshi_minus_observed": -0.0916, "brier_diff_model_minus_kalshi": -0.0041}, "4-10x": {"n": 619, "model_minus_observed": 0.0858, "kalshi_minus_observed": -0.0596, "brier_diff_model_minus_kalshi": 0.0088}, "<2x": {"n": 2264, "model_minus_observed": 0.0905, "kalshi_minus_observed": -0.0326, "brier_diff_model_minus_kalshi": 0.0114}, ">=10x": {"n": 830, "model_minus_observed": 0.1094, "kalshi_minus_observed": -0.0657, "brier_diff_model_minus_kalshi": 0.0081}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4628, "model": {"intercept": -0.533, "slope": 0.834, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.21, "slope": 1.081, "slope_se": 0.043}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1636, "model_brier": 0.2338, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0273, "brier_diff_se": 0.0028, "model_logloss": 0.6642, "kalshi_logloss": 0.5959}, "fair_v1": {"n": 4628, "model": {"intercept": -0.415, "slope": 1.041, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.29, "slope": 1.115, "slope_se": 0.043}, "mean_extremity_model": 0.1683, "mean_extremity_kalshi": 0.163, "model_brier": 0.2141, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.0023, "model_logloss": 0.6172, "kalshi_logloss": 0.5964}, "gen1_elo": {"n": 4628, "model": {"intercept": -0.388, "slope": 1.014, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.313, "slope": 1.113, "slope_se": 0.042}, "mean_extremity_model": 0.1748, "mean_extremity_kalshi": 0.1632, "model_brier": 0.213, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0061, "brier_diff_se": 0.0023, "model_logloss": 0.6155, "kalshi_logloss": 0.5967}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2457, "share_ge_15": 0.4429, "median_abs_gap": 13.06, "n": 32497}, "gen1_elo": {"share_ge_25": 0.2435, "share_ge_15": 0.4422, "median_abs_gap": 12.96, "n": 32497}, "gen1_sr": {"share_ge_25": 0.3134, "share_ge_15": 0.5203, "median_abs_gap": 15.89, "n": 32497}, "gen2": {"share_ge_25": 0.3174, "share_ge_15": 0.5116, "median_abs_gap": 15.51, "n": 32497}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1547, "share_ge_15": 0.3594, "median_abs_gap": 10.86, "n": 25340}, "gen1_elo": {"share_ge_25": 0.1553, "share_ge_15": 0.3577, "median_abs_gap": 10.7, "n": 25337}, "gen1_sr": {"share_ge_25": 0.2214, "share_ge_15": 0.4428, "median_abs_gap": 13.01, "n": 25341}, "gen2": {"share_ge_25": 0.238, "share_ge_15": 0.444, "median_abs_gap": 13.02, "n": 25342}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.87, "share_ge_25_all": 0.0434, "share_ge_25_pregame_clean": 0.0386}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.0545, "share_ge_25_pregame_clean": 0.0494}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2358, "share_within_10pp_all": 0.4342, "share_within_10pp_pregame_clean": 0.4859, "corr_model_vs_mid_pregame_clean": 0.8432}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 675, "model_brier": 0.2018, "kalshi_brier": 0.2026, "brier_diff_model_minus_kalshi": -0.0008}, "10-15": {"n_settled": 807, "model_brier": 0.2157, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.0089}, "15-25": {"n_settled": 1052, "model_brier": 0.2247, "kalshi_brier": 0.2131, "brier_diff_model_minus_kalshi": 0.0116}, "25-40": {"n_settled": 595, "model_brier": 0.2214, "kalshi_brier": 0.2097, "brier_diff_model_minus_kalshi": 0.0117}, "3-5": {"n_settled": 424, "model_brier": 0.2053, "kalshi_brier": 0.2046, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 116, "model_brier": 0.2743, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0723}, "5-10": {"n_settled": 959, "model_brier": 0.202, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": -0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.533, "slope": 0.834, "slope_se": 0.038}, "kalshi_slope": {"intercept": 0.21, "slope": 1.081, "slope_se": 0.043}, "n": 4628}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.498, "slope": 0.868, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.163, "slope": 1.07, "slope_se": 0.034}, "n": 6711}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 441, "model_brier": 0.3088, "kalshi_brier": 0.2362, "brier_diff_model_minus_kalshi": 0.0726, "brier_diff_se": 0.0144, "corr_model_outcome": 0.0389, "corr_kalshi_outcome": 0.2525}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
