# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-08T10:33Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 24,879): 0-3 14.0%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 18.7%, 25-40 14.2%, 40+ 8.3%; median gap 12.02 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.3%, Challenger 12.4%, doubles 6.1%). Main tour: ATP 1.8% and WTA 8.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,596): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.1%, STALE_QUOTE 17.4%, BOOK_QUALITY 17.3%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 5.0%, LIMITED_DATA 4.5%, IN_PLAY_QUOTE 3.1%, IDENTITY_AMBIGUOUS 2.9%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.2%. By class: coverage 39.1%, market_freshness 17.4%, execution 17.3%, data 12.9%, market_freshness/coverage 8.1%, mapping 2.9%, model_calibration_or_unknown 2.1%, model_calibration 0.2%.
* **Stale / settled / in-play**: 55.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 47.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,596 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 11.9% of the time and with the model 0.2%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 611.0 points vs 1723.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.12, Gen-2 0.894, Gen-1 ledger 0.947 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 227 model 0.2162 vs Kalshi 0.2015; n 52 model 0.282 vs Kalshi 0.1791.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 93,212 model-market comparisons (156,541 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 35,273 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-08T10:27:43.079455+00:00'], shadow board 25,918 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-08T10:27:46.379319+00:00'], Model 4 9,522 rows, 10,725 settled tickers, 2,873 tickers with an external scan.
* By model: {"gen1_ledger": 22369, "gen1_elo": 13022, "fair_v1": 13022, "gen2": 13022, "gen1_sr": 13022, "model4_fundamental": 9382, "model4_conditioned": 9373}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 24,879 | 14.0 | 9.6 | 19.9 | 15.4 | 18.7 | 14.2 | 8.3 | 12.02 | 41.2% | 22.5% |
| MW fair_v1 | 13,022 | 13.2 | 8.8 | 18.4 | 16.2 | 18.5 | 15.0 | 10.0 | 12.95 | 43.4% | 25.0% |
| MW gen1_elo | 13,022 | 12.8 | 8.8 | 20.0 | 15.0 | 19.3 | 14.7 | 9.4 | 12.53 | 43.3% | 24.1% |
| MW gen1_ledger | 11,857 | 14.8 | 10.6 | 21.5 | 14.6 | 18.9 | 13.2 | 6.5 | 10.92 | 38.6% | 19.8% |
| MW gen1_sr | 13,022 | 10.2 | 7.8 | 16.1 | 14.1 | 21.5 | 18.6 | 11.7 | 15.59 | 51.7% | 30.2% |
| MW gen2 | 13,022 | 12.1 | 7.1 | 16.1 | 14.3 | 19.7 | 17.5 | 13.2 | 15.25 | 50.4% | 30.6% |
| all families model4_conditioned | 9,373 | 22.0 | 20.6 | 35.4 | 16.0 | 4.3 | 0.9 | 0.8 | 5.7 | 6.0% | 1.7% |
| all families model4_fundamental | 9,382 | 16.4 | 13.3 | 34.9 | 20.4 | 10.9 | 2.9 | 1.1 | 7.76 | 15.0% | 4.1% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.6%, >=15pp 41.2%, >=20pp 30.8%, >=25pp 22.5%, >=30pp 16.4%, >=40pp 8.3%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.49pp; >=10pp 45.6%, >=25pp 18.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 943 | 26.8 | 15.7 | 24.0 | 18.0 | 12.9 | 1.4 | 1.2 | 6.01 | 15.5% | 2.5% |
| CHALLENGER | 2,232 | 15.5 | 10.9 | 18.5 | 16.1 | 12.9 | 13.2 | 12.9 | 11.9 | 39.0% | 26.1% |
| ITF_MEN | 3,765 | 11.0 | 8.6 | 18.7 | 14.8 | 19.4 | 15.1 | 12.3 | 13.77 | 46.9% | 27.4% |
| ITF_WOMEN | 5,224 | 10.4 | 6.8 | 16.2 | 16.2 | 21.6 | 18.9 | 9.9 | 15.17 | 50.4% | 28.9% |
| WTA | 540 | 24.1 | 9.4 | 25.2 | 16.1 | 17.0 | 6.1 | 2.0 | 8.0 | 25.2% | 8.2% |
| WTA125 | 318 | 11.9 | 6.6 | 22.0 | 26.1 | 14.5 | 16.4 | 2.5 | 11.32 | 33.3% | 18.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 943 | 22.1 | 14.1 | 24.2 | 18.8 | 17.2 | 2.3 | 1.4 | 6.9 | 20.9% | 3.7% |
| CHALLENGER | 2,232 | 15.3 | 7.5 | 17.9 | 13.5 | 18.1 | 14.4 | 13.3 | 13.11 | 45.7% | 27.7% |
| ITF_MEN | 3,765 | 10.8 | 7.4 | 16.8 | 14.6 | 19.8 | 17.6 | 13.0 | 15.3 | 50.4% | 30.6% |
| ITF_WOMEN | 5,224 | 9.2 | 6.0 | 13.1 | 13.2 | 20.6 | 21.3 | 16.6 | 18.84 | 58.6% | 38.0% |
| WTA | 540 | 22.2 | 5.4 | 18.3 | 15.0 | 20.9 | 16.1 | 2.0 | 12.18 | 39.1% | 18.1% |
| WTA125 | 318 | 4.7 | 2.8 | 17.3 | 22.0 | 20.8 | 20.4 | 11.9 | 16.84 | 53.1% | 32.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 943 | 25.7 | 12.6 | 29.8 | 16.2 | 11.1 | 3.3 | 1.3 | 6.62 | 15.7% | 4.6% |
| CHALLENGER | 2,232 | 16.0 | 10.8 | 19.9 | 14.0 | 14.1 | 12.4 | 12.9 | 10.89 | 39.3% | 25.2% |
| ITF_MEN | 3,765 | 10.0 | 8.9 | 18.5 | 14.2 | 20.4 | 15.6 | 12.3 | 14.18 | 48.3% | 27.9% |
| ITF_WOMEN | 5,224 | 9.6 | 6.7 | 17.1 | 15.7 | 23.4 | 18.8 | 8.7 | 15.36 | 50.9% | 27.5% |
| WTA | 540 | 23.0 | 13.0 | 35.6 | 14.4 | 9.3 | 3.5 | 1.3 | 6.96 | 14.1% | 4.8% |
| WTA125 | 318 | 20.8 | 11.6 | 30.2 | 17.0 | 14.8 | 5.0 | 0.6 | 7.99 | 20.4% | 5.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 473 | 27.9 | 22.4 | 37.2 | 10.8 | 1.5 | 0.2 | 0.0 | 4.98 | 1.7% | 0.2% |
| CHALLENGER | 1,449 | 23.1 | 17.2 | 25.7 | 14.2 | 12.3 | 5.5 | 2.1 | 6.68 | 19.9% | 7.5% |
| DOUBLES | 697 | 4.0 | 3.4 | 11.3 | 11.2 | 20.8 | 25.2 | 24.0 | 24.29 | 70.0% | 49.2% |
| ITF_MEN | 3,755 | 14.5 | 8.7 | 20.7 | 14.9 | 20.4 | 12.8 | 8.0 | 11.89 | 41.2% | 20.8% |
| ITF_WOMEN | 4,405 | 11.7 | 9.4 | 19.7 | 14.3 | 22.1 | 17.0 | 5.9 | 13.08 | 44.9% | 22.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 441 | 20.6 | 11.6 | 25.6 | 18.8 | 15.4 | 7.3 | 0.7 | 8.44 | 23.4% | 7.9% |
| WTA125 | 488 | 16.4 | 12.5 | 22.3 | 19.9 | 17.0 | 9.0 | 2.9 | 9.57 | 28.9% | 11.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 939 | 26.8 | 15.6 | 24.0 | 18.1 | 13.0 | 1.4 | 1.2 | 6.01 | 15.6% | 2.6% |
| CHALLENGER | 1,587 | 20.4 | 13.9 | 23.8 | 18.8 | 13.5 | 6.8 | 2.8 | 8.03 | 23.1% | 9.6% |
| ITF_MEN | 2,752 | 13.3 | 10.9 | 21.9 | 16.5 | 19.7 | 12.3 | 5.5 | 11.04 | 37.4% | 17.7% |
| ITF_WOMEN | 3,802 | 12.8 | 8.4 | 19.0 | 18.6 | 23.0 | 15.2 | 3.0 | 12.62 | 41.2% | 18.2% |
| WTA | 537 | 24.0 | 9.5 | 25.3 | 16.0 | 17.1 | 6.0 | 2.0 | 7.97 | 25.1% | 8.0% |
| WTA125 | 307 | 12.4 | 6.8 | 21.8 | 26.4 | 14.7 | 16.3 | 1.6 | 11.31 | 32.6% | 17.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 939 | 21.9 | 14.1 | 24.3 | 18.7 | 17.2 | 2.3 | 1.4 | 6.9 | 21.0% | 3.7% |
| CHALLENGER | 1,587 | 20.2 | 9.9 | 22.6 | 16.4 | 18.4 | 9.8 | 2.7 | 9.13 | 30.9% | 12.5% |
| ITF_MEN | 2,753 | 12.7 | 8.7 | 19.5 | 16.5 | 21.0 | 15.3 | 6.2 | 12.58 | 42.5% | 21.5% |
| ITF_WOMEN | 3,802 | 10.7 | 7.0 | 14.8 | 14.3 | 22.8 | 20.1 | 10.2 | 16.13 | 53.1% | 30.3% |
| WTA | 537 | 22.2 | 5.4 | 18.4 | 15.1 | 20.9 | 16.0 | 2.0 | 12.12 | 38.9% | 18.1% |
| WTA125 | 307 | 4.9 | 2.9 | 17.6 | 22.8 | 19.9 | 21.2 | 10.8 | 16.64 | 51.8% | 31.9% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 458 | 28.2 | 22.7 | 37.3 | 10.9 | 0.7 | 0.2 | 0.0 | 4.92 | 0.9% | 0.2% |
| CHALLENGER | 1,231 | 24.9 | 19.4 | 27.9 | 13.8 | 11.7 | 2.2 | 0.1 | 5.99 | 14.0% | 2.3% |
| DOUBLES | 643 | 4.0 | 3.4 | 11.5 | 11.0 | 21.0 | 25.2 | 23.8 | 24.18 | 70.0% | 49.0% |
| ITF_MEN | 3,049 | 16.2 | 9.6 | 23.0 | 15.9 | 20.1 | 10.5 | 4.7 | 10.24 | 35.2% | 15.2% |
| ITF_WOMEN | 3,606 | 13.0 | 10.2 | 21.5 | 15.2 | 22.3 | 15.3 | 2.5 | 11.5 | 40.1% | 17.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 411 | 21.2 | 12.2 | 26.3 | 19.0 | 15.8 | 5.6 | 0.0 | 8.34 | 21.4% | 5.6% |
| WTA125 | 405 | 18.5 | 13.8 | 24.9 | 22.7 | 15.1 | 4.7 | 0.2 | 8.27 | 20.0% | 4.9% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 697 | 4.0 | 3.4 | 11.3 | 11.2 | 20.8 | 25.2 | 24.0 | 24.29 | 70.0% | 49.2% |
| singles | 11,160 | 15.4 | 11.0 | 22.1 | 14.8 | 18.8 | 12.5 | 5.5 | 10.37 | 36.7% | 17.9% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,038 | 13.4 | 9.6 | 20.5 | 15.5 | 15.9 | 14.7 | 10.4 | 12.12 | 41.0% | 25.1% |
| Hard | 8,717 | 13.3 | 8.6 | 18.2 | 16.2 | 19.1 | 14.7 | 9.9 | 13.02 | 43.8% | 24.7% |
| UNKNOWN | 1,267 | 12.2 | 8.1 | 14.5 | 18.1 | 20.4 | 17.5 | 9.2 | 14.1 | 47.1% | 26.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,733 | 19.0 | 11.0 | 20.3 | 17.1 | 14.8 | 9.8 | 8.1 | 9.97 | 32.6% | 17.8% |
| B | 1,689 | 15.0 | 9.6 | 19.8 | 17.6 | 16.2 | 12.1 | 9.5 | 11.17 | 37.9% | 21.7% |
| C | 2,025 | 12.5 | 10.1 | 20.0 | 15.3 | 18.5 | 14.3 | 9.3 | 12.62 | 42.1% | 23.6% |
| D | 2,489 | 11.2 | 8.4 | 17.3 | 16.4 | 22.3 | 15.1 | 9.4 | 13.94 | 46.7% | 24.5% |
| F | 3,086 | 7.4 | 5.0 | 15.1 | 14.8 | 21.1 | 23.2 | 13.5 | 18.4 | 57.7% | 36.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,220 | 21.3 | 15.5 | 27.3 | 15.9 | 12.6 | 5.3 | 2.0 | 7.13 | 20.0% | 7.4% |
| B | 1,865 | 14.5 | 9.8 | 24.6 | 16.4 | 18.2 | 11.7 | 4.9 | 10.34 | 34.8% | 16.6% |
| C | 2,402 | 12.2 | 8.2 | 18.7 | 13.9 | 20.8 | 15.9 | 10.4 | 13.47 | 47.0% | 26.2% |
| D | 2,003 | 14.0 | 9.2 | 21.1 | 12.9 | 22.1 | 14.4 | 6.4 | 12.12 | 42.9% | 20.8% |
| F | 2,367 | 9.3 | 7.9 | 14.2 | 13.5 | 23.2 | 21.5 | 10.3 | 16.88 | 55.0% | 31.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,221 | 17.8 | 10.2 | 19.5 | 17.3 | 15.0 | 10.2 | 10.0 | 10.65 | 35.2% | 20.2% |
| LIMITED | 3,185 | 14.5 | 10.6 | 21.0 | 15.9 | 17.5 | 13.4 | 7.1 | 11.16 | 38.0% | 20.5% |
| POOR | 5,616 | 9.1 | 6.6 | 16.0 | 15.5 | 21.6 | 19.5 | 11.6 | 16.04 | 52.7% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,968 | 29.8 | 25.5 | 37.1 | 5.6 | 1.7 | 0.4 | 0.0 | 4.54 | 2.0% | 0.4% |
| GAME_SPREAD | 1,958 | 24.5 | 15.4 | 36.8 | 18.3 | 4.6 | 0.3 | 0.1 | 6.18 | 5.0% | 0.4% |
| MATCH_WINNER | 11,857 | 14.8 | 10.6 | 21.5 | 14.6 | 18.9 | 13.2 | 6.5 | 10.92 | 38.6% | 19.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,642 | 30.1 | 19.4 | 30.9 | 10.9 | 7.0 | 1.4 | 0.3 | 5.04 | 8.7% | 1.7% |
| TOTAL_GAMES | 2,920 | 7.4 | 9.1 | 38.1 | 30.4 | 9.7 | 3.2 | 2.2 | 9.52 | 15.0% | 5.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,476 | 24.1 | 39.3 | 30.3 | 0.3 | 5.3 | 0.6 | 0.2 | 4.34 | 6.0% | 0.7% |
| GAME_SPREAD | 2,395 | 46.2 | 14.2 | 29.2 | 8.2 | 1.2 | 0.7 | 0.2 | 3.49 | 2.1% | 1.0% |
| TOTAL_GAMES | 3,502 | 3.4 | 6.3 | 44.7 | 36.9 | 5.6 | 1.3 | 1.8 | 9.61 | 8.7% | 3.1% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,476 | 25.3 | 18.3 | 36.0 | 9.9 | 7.2 | 2.9 | 0.4 | 5.63 | 10.6% | 3.3% |
| GAME_SPREAD | 2,395 | 18.9 | 13.1 | 26.7 | 23.0 | 14.7 | 2.9 | 0.7 | 8.39 | 18.3% | 3.6% |
| TOTAL_GAMES | 3,511 | 5.9 | 8.5 | 39.5 | 29.0 | 12.0 | 3.0 | 2.1 | 9.59 | 17.1% | 5.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 13,022 | 43.4% | 25.0% | 12.95 | 33.7% | 14.7% | 10.45 |
| gen1_elo | 13,022 | 43.3% | 24.1% | 12.53 | 33.2% | 14.2% | 10.0 |
| gen1_sr | 13,022 | 51.7% | 30.2% | 15.59 | 43.0% | 20.1% | 12.77 |
| gen2 | 13,022 | 50.4% | 30.6% | 15.25 | 42.8% | 21.9% | 12.66 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 6,554 | 16.0 | 11.1 | 21.4 | 17.5 | 18.6 | 11.9 | 3.5 | 10.39 | 34.0% | 15.4% |
| STALE | 6,468 | 10.4 | 6.4 | 15.3 | 14.8 | 18.3 | 18.1 | 16.6 | 16.58 | 53.0% | 34.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 5,325 | 16.8 | 11.8 | 23.7 | 14.3 | 16.9 | 12.1 | 4.5 | 9.38 | 33.5% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 24,879 | 5325 | 10026 | 9528 | 25.2 | 154.0 | 1400.4 |
| ge_15pp | 10,239 | 1783 | 3519 | 4937 | 28.8 | 440.2 | 1380.4 |
| ge_25pp | 5,596 | 883 | 1599 | 3114 | 37.4 | 560.5 | 1380.4 |
| lt_10pp | 10,806 | 2780 | 4807 | 3219 | 23.9 | 50.6 | 1230.8 |

Current slate `SL-20261008T103306Z-ea0dfcba`: 606 priced rows, quote age at build {'median': 5.8, 'max': 5.8}, freshness {'FRESH': 606}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 2 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.87 | 100.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 3 | 33.3 | 66.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.05 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 657 | 23.6 | 11.4 | 21.6 | 20.4 | 15.4 | 7.2 | 0.5 | 7.98 | 23.0% | 7.6% |
| MARKETS_AGREE | 61 | 78.7 | 21.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.99 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 98 | 0.0 | 2.0 | 28.6 | 34.7 | 22.4 | 12.2 | 0.0 | 12.53 | 34.7% | 12.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 13,022 | 821 (6.3%) | 11.9% | 0.2% | {"EXTERNAL_STALE": 657, "AGREES_WITH_KALSHI": 98, "ALL_AGREE": 61, "EXTERNAL_OUTLIER": 3, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_15pp | 5,657 | 187 (3.3%) | 18.2% | 1.1% | {"EXTERNAL_STALE": 151, "AGREES_WITH_KALSHI": 34, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp | 3,251 | 62 (1.9%) | 19.4% | 0.0% | {"EXTERNAL_STALE": 50, "AGREES_WITH_KALSHI": 12} |
| fair_v1_ge_25pp_pregame_clean | 1,455 | 61 (4.2%) | 19.7% | 0.0% | {"EXTERNAL_STALE": 49, "AGREES_WITH_KALSHI": 12} |
| fair_v1_lt_10pp | 5,257 | 466 (8.9%) | 6.4% | 0.0% | {"EXTERNAL_STALE": 372, "ALL_AGREE": 61, "AGREES_WITH_KALSHI": 30, "EXTERNAL_OUTLIER": 3} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,653 | 11.5 | 8.5 | 20.0 | 15.6 | 21.1 | 14.1 | 9.2 | 12.9 | 44.4% | 23.3% |
| 4-10x | 1,881 | 11.3 | 9.2 | 18.3 | 14.8 | 20.3 | 17.0 | 9.1 | 13.76 | 46.4% | 26.2% |
| <2x | 6,797 | 15.2 | 9.3 | 18.4 | 17.2 | 16.7 | 13.3 | 9.9 | 12.1 | 40.0% | 23.2% |
| >=10x | 1,691 | 10.3 | 6.5 | 16.0 | 14.6 | 19.3 | 20.8 | 12.5 | 16.18 | 52.7% | 33.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,346 | 14.1 | 8.7 | 20.0 | 16.0 | 17.6 | 13.0 | 10.6 | 12.11 | 41.2% | 23.6% |
| 300-1000 | 3,216 | 12.0 | 9.2 | 16.7 | 16.3 | 21.1 | 16.0 | 8.7 | 13.69 | 45.8% | 24.7% |
| <300 | 3,572 | 8.0 | 6.0 | 15.8 | 14.9 | 20.9 | 21.2 | 13.1 | 17.2 | 55.2% | 34.3% |
| >=3000 | 2,888 | 20.1 | 11.7 | 21.5 | 17.9 | 13.5 | 8.5 | 6.8 | 9.14 | 28.8% | 15.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 397 | 0.5427 | 0.4109 | 0.4811 | +0.062 | -0.070 | 0.0025 ± 0.0073 |
| ratio 4-10x | 286 | 0.5862 | 0.4422 | 0.5245 | +0.062 | -0.082 | -0.0022 ± 0.0094 |
| ratio <2x | 832 | 0.5456 | 0.4185 | 0.4591 | +0.086 | -0.041 | 0.0109 ± 0.0051 |
| ratio >=10x | 269 | 0.5592 | 0.3837 | 0.4572 | +0.102 | -0.074 | 0.0123 ± 0.0111 |
| thinner_sample 1000-3000 | 469 | 0.5492 | 0.4233 | 0.4627 | +0.086 | -0.039 | 0.0065 ± 0.0066 |
| thinner_sample 300-1000 | 493 | 0.5727 | 0.4314 | 0.501 | +0.072 | -0.070 | 0.0001 ± 0.0071 |
| thinner_sample <300 | 560 | 0.5506 | 0.3872 | 0.475 | +0.076 | -0.088 | 0.0081 ± 0.0073 |
| thinner_sample >=3000 | 262 | 0.5314 | 0.4312 | 0.4427 | +0.089 | -0.012 | 0.0193 ± 0.0074 |
| data_status ADEQUATE | 468 | 0.5312 | 0.4243 | 0.4402 | +0.091 | -0.016 | 0.0128 ± 0.0058 |
| data_status LIMITED | 445 | 0.5677 | 0.4335 | 0.4944 | +0.073 | -0.061 | 0.0014 ± 0.0072 |
| data_status POOR | 871 | 0.5582 | 0.4013 | 0.4822 | +0.076 | -0.081 | 0.007 ± 0.0057 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 260 | 0.1816 | 0.1827 | -0.0011 ± 0.0009 | 0.537 | 0.5396 | 0.4939 | 0.4793 | 0.5115 | -0.086 ± 0.0279 | -0.01 (3) |
| 3-5 | 179 | 0.1859 | 0.1867 | -0.0008 ± 0.0026 | 0.5514 | 0.5507 | 0.508 | 0.4679 | 0.4916 | -0.077 ± 0.0329 | 0.02 (1) |
| 5-10 | 364 | 0.1993 | 0.2013 | -0.0020 ± 0.0035 | 0.5844 | 0.5899 | 0.5212 | 0.4473 | 0.489 | -0.094 ± 0.0245 | -0.0125 (4) |
| 10-15 | 312 | 0.2177 | 0.2154 | +0.0023 ± 0.0066 | 0.6234 | 0.6142 | 0.532 | 0.408 | 0.4583 | -0.092 ± 0.0264 | -0.0633 (3) |
| 15-25 | 390 | 0.223 | 0.2115 | +0.0114 ± 0.0091 | 0.6377 | 0.6108 | 0.5773 | 0.3817 | 0.4487 | -0.091 ± 0.0232 | -0.0133 (6) |
| 25-40 | 227 | 0.2162 | 0.2015 | +0.0146 ± 0.0177 | 0.6219 | 0.5781 | 0.6509 | 0.3411 | 0.4714 | -0.075 ± 0.0264 | -0.01 (1) |
| 40+ | 52 | 0.282 | 0.1791 | +0.1028 ± 0.0518 | 0.7673 | 0.5347 | 0.7592 | 0.3118 | 0.4231 | -0.120 ± 0.0507 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1248 | 0.1648 | 0.1656 | -0.0008 ± 0.0004 | 0.4966 | 0.4976 | 0.4787 | 0.4637 | 0.5024 | -0.028 ± 0.0117 | -0.0188 (8) |
| 3-5 | 872 | 0.1927 | 0.1892 | +0.0034 ± 0.0012 | 0.5678 | 0.554 | 0.4812 | 0.4416 | 0.414 | -0.090 ± 0.015 | 0.02 (1) |
| 5-10 | 1826 | 0.1921 | 0.1906 | +0.0015 ± 0.0015 | 0.5669 | 0.562 | 0.491 | 0.4171 | 0.4414 | -0.051 ± 0.0104 | -0.0082 (17) |
| 10-15 | 1629 | 0.2059 | 0.1888 | +0.0171 ± 0.0027 | 0.598 | 0.5516 | 0.48 | 0.3554 | 0.3499 | -0.080 ± 0.0107 | -0.0475 (4) |
| 15-25 | 1961 | 0.2006 | 0.163 | +0.0377 ± 0.0036 | 0.5911 | 0.4864 | 0.491 | 0.2949 | 0.2968 | -0.078 ± 0.0091 | -0.0048 (29) |
| 25-40 | 1708 | 0.2153 | 0.1251 | +0.0901 ± 0.0054 | 0.6225 | 0.3863 | 0.5284 | 0.215 | 0.2301 | -0.057 ± 0.0082 | -0.01 (1) |
| 40+ | 1183 | 0.3669 | 0.0468 | +0.3201 ± 0.0069 | 0.9575 | 0.1815 | 0.6213 | 0.1067 | 0.0634 | -0.080 ± 0.0059 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 203 | 0.192 | 0.1923 | -0.0003 ± 0.0011 | 0.566 | 0.5667 | 0.4982 | 0.483 | 0.4828 | -0.113 ± 0.0325 | -0.01 (1) |
| 3-5 | 134 | 0.2078 | 0.2079 | -0.0002 ± 0.0032 | 0.5954 | 0.5987 | 0.5171 | 0.4772 | 0.4925 | -0.080 ± 0.0415 | 0.02 (1) |
| 5-10 | 306 | 0.1932 | 0.1908 | +0.0024 ± 0.0038 | 0.5693 | 0.5635 | 0.564 | 0.4885 | 0.5065 | -0.100 ± 0.0259 | -0.01 (4) |
| 10-15 | 305 | 0.2174 | 0.2088 | +0.0086 ± 0.0066 | 0.621 | 0.6045 | 0.5888 | 0.4643 | 0.4984 | -0.112 ± 0.0273 | -0.05 (4) |
| 15-25 | 428 | 0.2233 | 0.2063 | +0.0170 ± 0.0087 | 0.6341 | 0.5938 | 0.6028 | 0.4052 | 0.4673 | -0.103 ± 0.0226 | -0.01 (5) |
| 25-40 | 298 | 0.2687 | 0.2022 | +0.0665 ± 0.0164 | 0.7508 | 0.5848 | 0.6721 | 0.3585 | 0.4094 | -0.142 ± 0.0261 | -0.025 (2) |
| 40+ | 110 | 0.3403 | 0.1936 | +0.1468 ± 0.0408 | 0.9629 | 0.5637 | 0.7681 | 0.2864 | 0.3909 | -0.063 ± 0.0386 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1150 | 0.173 | 0.1738 | -0.0008 ± 0.0004 | 0.5177 | 0.5197 | 0.496 | 0.4816 | 0.5078 | -0.036 ± 0.0129 | -0.0217 (6) |
| 3-5 | 735 | 0.1909 | 0.1875 | +0.0034 ± 0.0013 | 0.554 | 0.5466 | 0.5172 | 0.4773 | 0.4558 | -0.075 ± 0.0162 | 0.02 (1) |
| 5-10 | 1600 | 0.1837 | 0.181 | +0.0027 ± 0.0016 | 0.5499 | 0.5387 | 0.5173 | 0.4435 | 0.4625 | -0.050 ± 0.0108 | -0.01 (5) |
| 10-15 | 1442 | 0.1984 | 0.1828 | +0.0156 ± 0.0028 | 0.5845 | 0.536 | 0.5258 | 0.4017 | 0.4043 | -0.077 ± 0.0115 | -0.02 (14) |
| 15-25 | 2048 | 0.2132 | 0.1717 | +0.0414 ± 0.0036 | 0.6215 | 0.5087 | 0.5305 | 0.3352 | 0.3301 | -0.088 ± 0.0093 | -0.0026 (27) |
| 25-40 | 1923 | 0.2477 | 0.1376 | +0.1101 ± 0.0054 | 0.701 | 0.4195 | 0.5621 | 0.2452 | 0.2309 | -0.091 ± 0.0085 | -0.015 (6) |
| 40+ | 1529 | 0.3997 | 0.0715 | +0.3283 ± 0.0078 | 1.0477 | 0.2467 | 0.67 | 0.1322 | 0.1099 | -0.064 ± 0.0066 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 266 | 0.1887 | 0.1913 | -0.0026 ± 0.001 | 0.5544 | 0.5613 | 0.4999 | 0.4847 | 0.5451 | -0.035 ± 0.0271 | -0.0133 (6) |
| 3-5 | 193 | 0.1829 | 0.1816 | +0.0014 ± 0.0024 | 0.5402 | 0.5367 | 0.4918 | 0.4525 | 0.456 | -0.125 ± 0.0326 | -0.01 (1) |
| 5-10 | 377 | 0.1958 | 0.1975 | -0.0017 ± 0.0034 | 0.5771 | 0.58 | 0.5139 | 0.4402 | 0.4828 | -0.084 ± 0.0239 | -0.01 (4) |
| 10-15 | 291 | 0.2185 | 0.2161 | +0.0024 ± 0.0068 | 0.6283 | 0.6174 | 0.5437 | 0.4204 | 0.4742 | -0.099 ± 0.0268 | -0.044 (5) |
| 15-25 | 383 | 0.2242 | 0.2096 | +0.0145 ± 0.0091 | 0.6448 | 0.6043 | 0.5846 | 0.3911 | 0.4491 | -0.100 ± 0.0232 | -0.03 (1) |
| 25-40 | 228 | 0.2018 | 0.2068 | -0.0050 ± 0.0175 | 0.5876 | 0.5926 | 0.6558 | 0.3448 | 0.5044 | -0.056 ± 0.0255 | 0.0 (1) |
| 40+ | 46 | 0.3062 | 0.1787 | +0.1275 ± 0.0561 | 0.8241 | 0.5334 | 0.752 | 0.2995 | 0.3913 | -0.131 ± 0.0563 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1187 | 0.1766 | 0.1779 | -0.0013 ± 0.0004 | 0.5248 | 0.5278 | 0.486 | 0.4708 | 0.5088 | -0.026 ± 0.0123 | -0.0183 (23) |
| 3-5 | 874 | 0.1855 | 0.1827 | +0.0028 ± 0.0012 | 0.5466 | 0.5407 | 0.4725 | 0.4332 | 0.4176 | -0.088 ± 0.0151 | -0.0243 (7) |
| 5-10 | 1922 | 0.184 | 0.1812 | +0.0027 ± 0.0015 | 0.5491 | 0.5387 | 0.4853 | 0.4113 | 0.4298 | -0.051 ± 0.0098 | -0.01 (18) |
| 10-15 | 1518 | 0.201 | 0.183 | +0.0179 ± 0.0027 | 0.5874 | 0.5357 | 0.4952 | 0.3719 | 0.3603 | -0.089 ± 0.0108 | -0.03 (9) |
| 15-25 | 2159 | 0.2051 | 0.1691 | +0.0360 ± 0.0035 | 0.6029 | 0.5021 | 0.4966 | 0.3006 | 0.308 | -0.067 ± 0.0089 | -0.03 (2) |
| 25-40 | 1652 | 0.2128 | 0.1206 | +0.0922 ± 0.0054 | 0.6166 | 0.3736 | 0.5226 | 0.2055 | 0.2222 | -0.060 ± 0.008 | 0.0 (1) |
| 40+ | 1115 | 0.381 | 0.048 | +0.3330 ± 0.0074 | 0.9968 | 0.1854 | 0.6285 | 0.1071 | 0.0601 | -0.082 ± 0.0062 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 547 | 0.2019 | 0.2019 | +0.0000 ± 0.0007 | 0.5872 | 0.5866 | 0.5008 | 0.4861 | 0.4863 | -0.050 ± 0.0192 | -0.0226 (46) |
| 3-5 | 412 | 0.1961 | 0.195 | +0.0012 ± 0.0017 | 0.5737 | 0.5694 | 0.482 | 0.4424 | 0.4515 | -0.048 ± 0.0217 | -0.0058 (33) |
| 5-10 | 848 | 0.1901 | 0.185 | +0.0051 ± 0.0022 | 0.5634 | 0.5503 | 0.4737 | 0.4003 | 0.4033 | -0.059 ± 0.0151 | -0.0049 (73) |
| 10-15 | 554 | 0.2026 | 0.1922 | +0.0104 ± 0.0047 | 0.5941 | 0.5654 | 0.4798 | 0.3569 | 0.3755 | -0.046 ± 0.0186 | 0.0014 (64) |
| 15-25 | 756 | 0.2339 | 0.2098 | +0.0241 ± 0.0065 | 0.6624 | 0.6053 | 0.5458 | 0.3514 | 0.3876 | -0.054 ± 0.0168 | -0.0216 (58) |
| 25-40 | 423 | 0.2423 | 0.1825 | +0.0599 ± 0.0129 | 0.6814 | 0.5377 | 0.6191 | 0.3057 | 0.3641 | -0.072 ± 0.0194 | -0.0216 (25) |
| 40+ | 144 | 0.3394 | 0.185 | +0.1544 ± 0.0364 | 0.9642 | 0.5477 | 0.7737 | 0.2811 | 0.3958 | -0.043 ± 0.032 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1549 | 0.1883 | 0.1881 | +0.0002 ± 0.0004 | 0.5538 | 0.5522 | 0.4982 | 0.4829 | 0.4797 | -0.049 ± 0.011 | -0.0155 (82) |
| 3-5 | 1121 | 0.1873 | 0.1844 | +0.0029 ± 0.001 | 0.5493 | 0.5429 | 0.4934 | 0.4538 | 0.4416 | -0.061 ± 0.0128 | -0.0148 (63) |
| 5-10 | 2291 | 0.1874 | 0.1797 | +0.0077 ± 0.0013 | 0.5575 | 0.5362 | 0.4717 | 0.398 | 0.3859 | -0.067 ± 0.009 | -0.0087 (125) |
| 10-15 | 1573 | 0.1973 | 0.1832 | +0.0140 ± 0.0027 | 0.581 | 0.5436 | 0.4909 | 0.3679 | 0.3719 | -0.057 ± 0.0107 | -0.0053 (105) |
| 15-25 | 2059 | 0.2272 | 0.1981 | +0.0291 ± 0.0038 | 0.6534 | 0.5763 | 0.5388 | 0.3435 | 0.3667 | -0.055 ± 0.0099 | -0.0255 (106) |
| 25-40 | 1442 | 0.2357 | 0.1575 | +0.0782 ± 0.0066 | 0.6677 | 0.4714 | 0.5811 | 0.2661 | 0.301 | -0.059 ± 0.0101 | -0.0206 (47) |
| 40+ | 703 | 0.3544 | 0.1069 | +0.2474 ± 0.0132 | 0.9692 | 0.3377 | 0.6752 | 0.1702 | 0.1906 | -0.056 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1784 | 1.12 ± 0.069 | 1.224 | 0.1699 | 0.1659 | 0.2083 | 0.2012 |
| gen2 | 1784 | 0.894 ± 0.06 | 1.151 | 0.1868 | 0.1654 | 0.2272 | 0.2011 |
| gen1_elo | 1784 | 1.106 ± 0.067 | 1.216 | 0.1735 | 0.1665 | 0.2068 | 0.2012 |
| gen1_sr | 1784 | 1.109 ± 0.077 | 1.23 | 0.1439 | 0.1679 | 0.2227 | 0.2009 |
| gen1_ledger | 3684 | 0.947 ± 0.043 | 1.094 | 0.1703 | 0.1911 | 0.2152 | 0.1945 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 10,239)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,771 | 27.1% |
| STALE_QUOTE | market_freshness | 2,188 | 21.4% |
| BOOK_QUALITY | execution | 1,839 | 18.0% |
| POOR_DATA | data | 1,122 | 11.0% |
| LIMITED_DATA | data | 759 | 7.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 507 | 5.0% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 469 | 4.6% |
| IDENTITY_AMBIGUOUS | mapping | 276 | 2.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 275 | 2.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 33 | 0.3% |

Cause class: coverage 27.1%, market_freshness 21.4%, data 18.4%, execution 18.0%, market_freshness/coverage 7.6%, model_calibration_or_unknown 4.6%, mapping 2.7%, model_calibration 0.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.5%, START_UNVERIFIABLE 96.2%, LOW_DATA_QUALITY 69.2%, STALE_PLAYER_DATA 58.4%, THIN_PLAYER_HISTORY 58.0%, STALE_KALSHI_QUOTE 48.2%, MODEL_INTERNAL_DISAGREEMENT 37.4%, ASYMMETRIC_SAMPLE_SIZE 31.2%, WIDE_SPREAD 23.9%, MODEL_HIGH_UNCERTAINTY 16.0%, PLAYER_IDENTITY_RISK 11.1%, LEVEL_TRANSFER_RISK 9.0%, EVENT_MAPPING_RISK 7.6%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.1%, EXTERNAL_MARKET_REJECTION 0.5%, UNKNOWN 0.5%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.3%, POST_SETTLEMENT_OBSERVATION 27.1%, POSSIBLE_IN_PLAY_QUOTE 5.3%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,596)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,185 | 39.1% |
| STALE_QUOTE | market_freshness | 976 | 17.4% |
| BOOK_QUALITY | execution | 970 | 17.3% |
| POOR_DATA | data | 473 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 280 | 5.0% |
| LIMITED_DATA | data | 249 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 174 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 161 | 2.9% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 117 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 11 | 0.2% |

Cause class: coverage 39.1%, market_freshness 17.4%, execution 17.3%, data 12.9%, market_freshness/coverage 8.1%, mapping 2.9%, model_calibration_or_unknown 2.1%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.7%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.8%, THIN_PLAYER_HISTORY 59.6%, STALE_KALSHI_QUOTE 55.6%, STALE_PLAYER_DATA 53.5%, MODEL_INTERNAL_DISAGREEMENT 39.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 17.2%, PLAYER_IDENTITY_RISK 13.8%, EVENT_MAPPING_RISK 9.0%, LEVEL_TRANSFER_RISK 7.7%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 0.3%, UNKNOWN 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 41.6%, POST_SETTLEMENT_OBSERVATION 39.1%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4661, "IDENTITY_AMBIGUOUS": 935}; ticker orientation: {"VERIFIED": 5596}.

Checks: discipline:AMBIGUOUS 343, discipline:PASS 5253, identity_confidence:AMBIGUOUS 774, identity_confidence:PASS 4822, level_mapping:NA 355, level_mapping:PASS 5241, market_pair:AMBIGUOUS 217, market_pair:NA 128, market_pair:PASS 5251, model_complement:NA 95, model_complement:PASS 5501, namesake:PASS 5596, physical_match_id:NA 2345, physical_match_id:PASS 3251, player_ids:PASS 5596, same_pair_other_event:PASS 5596, ticker_orientation:PASS 5596

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,416 | 1.8% | 1.8% | 0.4% | {"market_freshness": 20, "execution": 5} | 5.52 | 0.2128 / 0.2061 (131) | 20.5% | 0.1% | 6.0% | 1.3% |
| CHALLENGER | 3,681 | 18.8% | 6.4% | 12.4% | {"coverage": 430, "market_freshness": 107, "market_freshness/coverage": 81, "model_calibration_or_unknown": 42, "data": 25, "execution": 4, "model_calibration": 3} | 6.8 | 0.2227 / 0.204 (850) | 46.3% | 4.9% | 1.7% | 23.4% |
| DOUBLES | 697 | 49.2% | 49.0% | 6.1% | {"execution": 133, "market_freshness": 106, "mapping": 76, "market_freshness/coverage": 21, "coverage": 7} | 24.18 | 0.3077 / 0.224 (197) | 33.6% | 0.0% | 100.0% | 7.8% |
| ITF_MEN | 7,520 | 24.1% | 16.4% | 32.4% | {"coverage": 725, "execution": 385, "data": 278, "market_freshness": 264, "market_freshness/coverage": 139, "mapping": 19, "model_calibration_or_unknown": 4} | 10.65 | 0.2117 / 0.1927 (1817) | 38.4% | 55.1% | 6.2% | 22.9% |
| ITF_WOMEN | 9,629 | 26.1% | 18.0% | 44.9% | {"coverage": 1006, "execution": 426, "market_freshness": 422, "data": 395, "market_freshness/coverage": 172, "mapping": 60, "model_calibration_or_unknown": 25, "model_calibration": 7} | 12.14 | 0.2009 / 0.1922 (2007) | 39.6% | 58.6% | 10.0% | 23.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 981 | 8.1% | 7.0% | 1.4% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.16 | 0.2058 / 0.2016 (147) | 34.1% | 2.1% | 1.2% | 3.4% |
| WTA125 | 806 | 14.6% | 10.5% | 2.1% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 21, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 1} | 9.91 | 0.2265 / 0.2129 (277) | 26.7% | 6.3% | 4.2% | 11.7% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 9 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 10 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 11 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 12 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 13 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 15 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 16 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 18 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 19 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 20 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 21 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 22 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 23 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 24 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 25 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 26 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 27 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 28 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 760 min (STALE); no external reference |
| 29 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 30 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 22% | +74 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 32 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 33 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 36 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 38 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 39 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 40 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 230 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 41 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 42 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 43 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 44 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 45 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 47 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 48 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26OCT06BARSAM-SAM` | CHALLENGER | fair_v1 | 84% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 139 min (STALE); no external reference |
| 50 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9815, "by_level_share_of_ge_25pp": {"ATP": 0.0045, "CHALLENGER": 0.1237, "DOUBLES": 0.0613, "ITF_MEN": 0.3242, "ITF_WOMEN": 0.4491, "OTHER": 0.0021, "WTA": 0.0141, "WTA125": 0.0211}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5565, "share_primary_cause_market_settled_or_in_play": 0.4716, "share_primary_cause_stale_quote_only": 0.1744}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5596, "identity_ambiguous_share": 0.1671, "ticker_orientation": {"VERIFIED": 5596}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3251, "with_external": 62, "coverage": 0.0191, "external_status": {"EXTERNAL_STALE": 50, "AGREES_WITH_KALSHI": 12}, "triangulation": {"INSUFFICIENT_INPUTS": 50, "MODEL_LONE_OUTLIER": 12}, "share_external_agrees_with_kalshi": 0.1935, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1455, "with_external": 61, "coverage": 0.0419, "external_status": {"EXTERNAL_STALE": 49, "AGREES_WITH_KALSHI": 12}, "triangulation": {"INSUFFICIENT_INPUTS": 49, "MODEL_LONE_OUTLIER": 12}, "share_external_agrees_with_kalshi": 0.1967, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 611.0, "median_sample_ratio": 2.35, "median_min_matches": 20.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1782, "data_status": {"POOR": 2927, "LIMITED": 1672, "ADEQUATE": 997}, "comparison_lt_10pp": {"median_thinner_serve_points": 1723.0, "median_sample_ratio": 1.76, "median_min_matches": 72.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 397, "model_minus_observed": 0.0616, "kalshi_minus_observed": -0.0702, "brier_diff_model_minus_kalshi": 0.0025}, "4-10x": {"n": 286, "model_minus_observed": 0.0618, "kalshi_minus_observed": -0.0823, "brier_diff_model_minus_kalshi": -0.0022}, "<2x": {"n": 832, "model_minus_observed": 0.0864, "kalshi_minus_observed": -0.0407, "brier_diff_model_minus_kalshi": 0.0109}, ">=10x": {"n": 269, "model_minus_observed": 0.102, "kalshi_minus_observed": -0.0736, "brier_diff_model_minus_kalshi": 0.0123}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1784, "model": {"intercept": -0.576, "slope": 0.894, "slope_se": 0.06}, "kalshi_mid_same_rows": {"intercept": 0.233, "slope": 1.151, "slope_se": 0.069}, "mean_extremity_model": 0.1868, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2272, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.0261, "brier_diff_se": 0.0045, "model_logloss": 0.6498, "kalshi_logloss": 0.5844}, "fair_v1": {"n": 1784, "model": {"intercept": -0.413, "slope": 1.12, "slope_se": 0.069}, "kalshi_mid_same_rows": {"intercept": 0.358, "slope": 1.224, "slope_se": 0.072}, "mean_extremity_model": 0.1699, "mean_extremity_kalshi": 0.1659, "model_brier": 0.2083, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0071, "brier_diff_se": 0.0037, "model_logloss": 0.6028, "kalshi_logloss": 0.5843}, "gen1_elo": {"n": 1784, "model": {"intercept": -0.376, "slope": 1.106, "slope_se": 0.067}, "kalshi_mid_same_rows": {"intercept": 0.374, "slope": 1.216, "slope_se": 0.071}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.1665, "model_brier": 0.2068, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0056, "brier_diff_se": 0.0036, "model_logloss": 0.6003, "kalshi_logloss": 0.5842}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2497, "share_ge_15": 0.4344, "median_abs_gap": 12.95, "n": 13022}, "gen1_elo": {"share_ge_25": 0.2407, "share_ge_15": 0.4333, "median_abs_gap": 12.53, "n": 13022}, "gen1_sr": {"share_ge_25": 0.3024, "share_ge_15": 0.5173, "median_abs_gap": 15.59, "n": 13022}, "gen2": {"share_ge_25": 0.3064, "share_ge_15": 0.5038, "median_abs_gap": 15.25, "n": 13022}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1466, "share_ge_15": 0.3369, "median_abs_gap": 10.45, "n": 9924}, "gen1_elo": {"share_ge_25": 0.1419, "share_ge_15": 0.3325, "median_abs_gap": 10.0, "n": 9923}, "gen1_sr": {"share_ge_25": 0.2012, "share_ge_15": 0.4301, "median_abs_gap": 12.77, "n": 9924}, "gen2": {"share_ge_25": 0.2189, "share_ge_15": 0.4279, "median_abs_gap": 12.66, "n": 9925}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0177, "share_ge_25_pregame_clean": 0.0179}, "WTA": {"median_abs_gap_pregame_clean": 8.16, "share_ge_25_all": 0.0805, "share_ge_25_pregame_clean": 0.0696}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2357, "share_within_10pp_all": 0.4343, "share_within_10pp_pregame_clean": 0.4968, "corr_model_vs_mid_pregame_clean": 0.8518}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 260, "model_brier": 0.1816, "kalshi_brier": 0.1827, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 312, "model_brier": 0.2177, "kalshi_brier": 0.2154, "brier_diff_model_minus_kalshi": 0.0023}, "15-25": {"n_settled": 390, "model_brier": 0.223, "kalshi_brier": 0.2115, "brier_diff_model_minus_kalshi": 0.0114}, "25-40": {"n_settled": 227, "model_brier": 0.2162, "kalshi_brier": 0.2015, "brier_diff_model_minus_kalshi": 0.0146}, "3-5": {"n_settled": 179, "model_brier": 0.1859, "kalshi_brier": 0.1867, "brier_diff_model_minus_kalshi": -0.0008}, "40+": {"n_settled": 52, "model_brier": 0.282, "kalshi_brier": 0.1791, "brier_diff_model_minus_kalshi": 0.1028}, "5-10": {"n_settled": 364, "model_brier": 0.1993, "kalshi_brier": 0.2013, "brier_diff_model_minus_kalshi": -0.002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 197, "model_brier": 0.3077, "kalshi_brier": 0.224, "brier_diff_model_minus_kalshi": 0.0837, "brier_diff_se": 0.0224, "corr_model_outcome": 0.0271, "corr_kalshi_outcome": 0.3525}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
