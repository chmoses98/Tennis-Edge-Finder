# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-21T05:36Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 45,892): 0-3 14.1%, 3-5 9.5%, 5-10 19.7%, 10-15 15.4%, 15-25 19.4%, 25-40 14.0%, 40+ 7.9%; median gap 12.03 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.9%, Challenger 12.5%, doubles 6.9%). Main tour: ATP 5.0% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 10,050): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.1%, BOOK_QUALITY 19.0%, STALE_QUOTE 18.1%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%. By class: coverage 34.1%, execution 19.0%, market_freshness 18.1%, data 12.8%, market_freshness/coverage 8.7%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%.
* **Stale / settled / in-play**: 51.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 10,050 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.5% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 499.0 points vs 1732.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.044, Gen-2 0.843, Gen-1 ledger 0.873 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 479 model 0.2268 vs Kalshi 0.2105; n 95 model 0.3 vs Kalshi 0.1766.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 196,670 model-market comparisons (319,478 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 67,271 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-21T05:23:16.579029+00:00'], shadow board 51,835 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-21T05:23:20.135090+00:00'], Model 4 24,690 rows, 17,843 settled tickers, 6,242 tickers with an external scan.
* By model: {"gen1_ledger": 45485, "gen1_elo": 26061, "fair_v1": 26061, "gen2": 26061, "gen1_sr": 26061, "model4_fundamental": 23484, "model4_conditioned": 23457}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 45,892 | 14.1 | 9.5 | 19.7 | 15.4 | 19.4 | 14.0 | 7.9 | 12.03 | 41.2% | 21.9% |
| MW fair_v1 | 26,061 | 13.1 | 8.6 | 18.3 | 15.7 | 20.0 | 14.9 | 9.4 | 13.11 | 44.3% | 24.3% |
| MW gen1_elo | 26,061 | 12.9 | 8.7 | 19.2 | 15.2 | 19.9 | 14.9 | 9.2 | 12.81 | 43.9% | 24.0% |
| MW gen1_ledger | 19,831 | 15.5 | 10.7 | 21.6 | 14.9 | 18.5 | 12.8 | 6.0 | 10.53 | 37.2% | 18.8% |
| MW gen1_sr | 26,061 | 10.0 | 7.2 | 16.6 | 14.0 | 21.4 | 18.7 | 12.1 | 15.89 | 52.2% | 30.8% |
| MW gen2 | 26,061 | 11.1 | 7.3 | 16.2 | 14.2 | 20.1 | 17.8 | 13.3 | 15.51 | 51.1% | 31.1% |
| all families model4_conditioned | 23,457 | 21.8 | 19.2 | 34.4 | 17.8 | 4.5 | 1.4 | 1.1 | 5.95 | 6.9% | 2.4% |
| all families model4_fundamental | 23,484 | 16.3 | 13.1 | 34.0 | 20.4 | 11.3 | 3.5 | 1.3 | 7.91 | 16.1% | 4.8% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.6%, >=15pp 41.2%, >=20pp 30.6%, >=25pp 21.9%, >=30pp 15.7%, >=40pp 7.9%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.41pp; >=10pp 45.1%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,284 | 28.6 | 13.9 | 24.3 | 14.9 | 12.5 | 5.2 | 0.6 | 6.21 | 18.3% | 5.7% |
| CHALLENGER | 4,296 | 15.6 | 10.1 | 20.2 | 15.8 | 14.9 | 12.6 | 10.9 | 11.3 | 38.4% | 23.4% |
| ITF_MEN | 6,953 | 10.8 | 7.7 | 17.1 | 14.5 | 21.0 | 17.0 | 11.8 | 14.98 | 49.9% | 28.8% |
| ITF_WOMEN | 10,287 | 9.6 | 6.8 | 15.7 | 15.6 | 23.0 | 18.2 | 11.0 | 15.76 | 52.3% | 29.2% |
| WTA | 1,581 | 17.2 | 12.4 | 24.9 | 20.2 | 20.2 | 4.4 | 0.7 | 8.74 | 25.3% | 5.1% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,284 | 23.4 | 15.0 | 24.3 | 17.2 | 14.1 | 5.2 | 0.8 | 6.83 | 20.1% | 6.0% |
| CHALLENGER | 4,296 | 14.6 | 8.4 | 18.7 | 14.6 | 17.8 | 14.0 | 11.9 | 12.69 | 43.7% | 25.9% |
| ITF_MEN | 6,953 | 8.9 | 6.4 | 14.8 | 13.2 | 19.9 | 20.4 | 16.5 | 17.92 | 56.7% | 36.9% |
| ITF_WOMEN | 10,287 | 8.3 | 5.6 | 13.7 | 13.4 | 21.5 | 20.9 | 16.6 | 18.84 | 59.0% | 37.5% |
| WTA | 1,581 | 14.6 | 9.5 | 20.3 | 16.7 | 24.2 | 14.0 | 0.8 | 11.5 | 39.0% | 14.7% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,284 | 24.1 | 12.9 | 24.2 | 15.9 | 15.1 | 6.7 | 1.1 | 7.28 | 22.8% | 7.8% |
| CHALLENGER | 4,296 | 14.2 | 9.5 | 20.8 | 15.2 | 16.3 | 12.8 | 11.1 | 11.41 | 40.2% | 23.9% |
| ITF_MEN | 6,953 | 10.1 | 7.7 | 17.4 | 13.9 | 21.7 | 17.3 | 11.9 | 15.38 | 50.9% | 29.2% |
| ITF_WOMEN | 10,287 | 9.5 | 6.7 | 16.4 | 15.7 | 23.2 | 18.4 | 10.2 | 15.6 | 51.8% | 28.6% |
| WTA | 1,581 | 24.5 | 16.5 | 30.1 | 16.1 | 10.2 | 2.1 | 0.4 | 6.01 | 12.8% | 2.6% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,307 | 26.5 | 19.8 | 29.5 | 11.9 | 8.7 | 3.2 | 0.4 | 5.4 | 12.3% | 3.6% |
| CHALLENGER | 2,988 | 21.2 | 14.7 | 26.7 | 14.2 | 14.8 | 6.4 | 1.9 | 7.29 | 23.1% | 8.3% |
| DOUBLES | 1,428 | 4.9 | 4.2 | 11.8 | 10.4 | 20.5 | 25.9 | 22.3 | 24.07 | 68.7% | 48.2% |
| ITF_MEN | 5,520 | 14.0 | 8.8 | 20.5 | 15.9 | 20.6 | 13.3 | 6.8 | 12.02 | 40.7% | 20.1% |
| ITF_WOMEN | 6,683 | 12.4 | 8.9 | 19.3 | 15.2 | 21.8 | 16.4 | 6.0 | 12.96 | 44.2% | 22.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,024 | 22.4 | 15.8 | 29.7 | 18.1 | 10.2 | 3.6 | 0.3 | 6.97 | 14.1% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,227 | 29.0 | 14.1 | 24.6 | 14.8 | 12.3 | 4.8 | 0.5 | 6.13 | 17.6% | 5.3% |
| CHALLENGER | 3,030 | 20.3 | 12.4 | 24.8 | 18.4 | 15.3 | 6.7 | 2.1 | 8.43 | 24.1% | 8.8% |
| ITF_MEN | 5,158 | 13.0 | 9.2 | 20.3 | 16.4 | 21.8 | 14.0 | 5.3 | 12.14 | 41.0% | 19.3% |
| ITF_WOMEN | 7,755 | 11.3 | 8.2 | 17.8 | 17.8 | 24.8 | 15.3 | 4.9 | 13.48 | 45.0% | 20.2% |
| WTA | 1,540 | 17.4 | 12.1 | 24.8 | 20.4 | 20.2 | 4.3 | 0.7 | 8.81 | 25.3% | 5.1% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,227 | 23.7 | 15.3 | 24.5 | 17.0 | 14.0 | 4.9 | 0.7 | 6.63 | 19.6% | 5.6% |
| CHALLENGER | 3,030 | 18.3 | 10.8 | 23.3 | 17.4 | 18.0 | 9.8 | 2.3 | 9.44 | 30.2% | 12.2% |
| ITF_MEN | 5,159 | 10.4 | 7.5 | 16.9 | 14.9 | 21.9 | 18.5 | 9.8 | 15.12 | 50.2% | 28.3% |
| ITF_WOMEN | 7,755 | 9.3 | 6.5 | 15.1 | 14.9 | 23.4 | 20.3 | 10.6 | 16.57 | 54.4% | 30.9% |
| WTA | 1,540 | 14.6 | 9.5 | 20.3 | 16.6 | 24.2 | 14.2 | 0.8 | 11.62 | 39.2% | 14.9% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,267 | 26.7 | 20.1 | 29.6 | 12.1 | 8.3 | 3.1 | 0.2 | 5.34 | 11.6% | 3.3% |
| CHALLENGER | 2,601 | 22.7 | 15.8 | 28.4 | 14.1 | 14.2 | 4.2 | 0.6 | 6.72 | 19.0% | 4.8% |
| DOUBLES | 1,329 | 4.9 | 4.4 | 12.0 | 10.6 | 20.5 | 26.0 | 21.7 | 23.92 | 68.2% | 47.7% |
| ITF_MEN | 4,609 | 15.3 | 9.6 | 22.3 | 16.7 | 20.4 | 11.7 | 4.1 | 10.82 | 36.1% | 15.8% |
| ITF_WOMEN | 5,578 | 13.2 | 9.5 | 20.7 | 16.0 | 21.9 | 15.2 | 3.4 | 11.84 | 40.6% | 18.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 977 | 22.8 | 16.3 | 29.8 | 18.1 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,428 | 4.9 | 4.2 | 11.8 | 10.4 | 20.5 | 25.9 | 22.3 | 24.07 | 68.7% | 48.2% |
| singles | 18,403 | 16.3 | 11.2 | 22.4 | 15.3 | 18.3 | 11.8 | 4.7 | 10.02 | 34.8% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,880 | 13.3 | 8.8 | 19.1 | 15.7 | 18.9 | 14.8 | 9.4 | 12.8 | 43.1% | 24.2% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 16,424 | 13.5 | 8.6 | 18.3 | 15.4 | 20.2 | 14.7 | 9.3 | 13.09 | 44.2% | 24.0% |
| UNKNOWN | 3,520 | 11.3 | 8.0 | 16.9 | 17.2 | 20.8 | 15.8 | 10.0 | 13.72 | 46.6% | 25.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,449 | 19.7 | 11.5 | 21.1 | 16.8 | 16.0 | 9.0 | 5.9 | 9.32 | 30.9% | 14.9% |
| B | 3,309 | 12.4 | 9.1 | 19.9 | 17.2 | 18.9 | 12.1 | 10.3 | 12.18 | 41.3% | 22.4% |
| C | 3,653 | 12.0 | 9.0 | 19.1 | 14.9 | 19.7 | 15.3 | 10.1 | 13.18 | 45.0% | 25.3% |
| D | 4,261 | 12.2 | 7.7 | 16.9 | 15.6 | 22.2 | 15.9 | 9.4 | 14.04 | 47.5% | 25.3% |
| F | 7,389 | 7.9 | 5.7 | 15.1 | 14.4 | 23.4 | 21.2 | 12.3 | 17.65 | 56.9% | 33.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,663 | 23.2 | 15.9 | 28.5 | 15.1 | 11.8 | 4.0 | 1.5 | 6.68 | 17.3% | 5.5% |
| B | 2,754 | 15.9 | 10.5 | 24.0 | 16.2 | 18.8 | 10.8 | 3.9 | 9.92 | 33.4% | 14.6% |
| C | 3,915 | 11.1 | 7.3 | 18.5 | 14.4 | 21.5 | 16.4 | 10.8 | 14.32 | 48.7% | 27.2% |
| D | 2,840 | 14.0 | 9.8 | 19.8 | 14.6 | 21.1 | 14.6 | 6.1 | 12.09 | 41.8% | 20.7% |
| F | 4,659 | 10.3 | 8.0 | 15.7 | 14.7 | 22.3 | 20.6 | 8.4 | 15.69 | 51.3% | 29.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,479 | 17.9 | 10.3 | 20.4 | 16.8 | 16.4 | 9.8 | 8.3 | 10.4 | 34.6% | 18.1% |
| LIMITED | 5,692 | 13.7 | 10.3 | 20.2 | 15.7 | 19.1 | 13.5 | 7.5 | 11.75 | 40.1% | 21.0% |
| POOR | 11,890 | 9.5 | 6.5 | 15.8 | 14.9 | 22.9 | 19.1 | 11.2 | 16.09 | 53.2% | 30.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,020 | 26.8 | 20.8 | 34.2 | 12.0 | 4.5 | 1.5 | 0.2 | 5.2 | 6.2% | 1.7% |
| GAME_SPREAD | 4,346 | 22.8 | 15.4 | 33.3 | 17.0 | 8.8 | 2.4 | 0.3 | 6.54 | 11.5% | 2.7% |
| MATCH_WINNER | 19,831 | 15.5 | 10.7 | 21.6 | 14.9 | 18.5 | 12.8 | 6.0 | 10.53 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,212 | 29.9 | 16.9 | 30.4 | 12.6 | 8.1 | 1.7 | 0.4 | 5.41 | 10.3% | 2.1% |
| TOTAL_GAMES | 7,052 | 8.1 | 9.3 | 36.4 | 29.2 | 10.9 | 3.3 | 2.8 | 9.57 | 17.0% | 6.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,197 | 25.3 | 34.7 | 32.2 | 4.0 | 3.1 | 0.6 | 0.1 | 4.45 | 3.8% | 0.7% |
| GAME_SPREAD | 5,607 | 45.8 | 17.0 | 27.0 | 7.6 | 1.8 | 0.6 | 0.2 | 3.42 | 2.6% | 0.8% |
| TOTAL_GAMES | 9,653 | 4.8 | 7.4 | 40.5 | 35.3 | 7.3 | 2.5 | 2.3 | 9.73 | 12.0% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,200 | 24.2 | 18.0 | 35.3 | 12.3 | 7.3 | 2.6 | 0.3 | 5.81 | 10.2% | 2.9% |
| GAME_SPREAD | 5,610 | 19.2 | 13.2 | 28.2 | 19.9 | 14.3 | 4.3 | 0.9 | 8.0 | 19.6% | 5.2% |
| TOTAL_GAMES | 9,674 | 8.0 | 8.8 | 36.4 | 27.6 | 13.0 | 3.8 | 2.5 | 9.65 | 19.2% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 26,061 | 44.3% | 24.3% | 13.11 | 36.1% | 15.3% | 10.95 |
| gen1_elo | 26,061 | 43.9% | 24.0% | 12.81 | 35.4% | 15.4% | 10.53 |
| gen1_sr | 26,061 | 52.2% | 30.8% | 15.89 | 44.8% | 21.9% | 13.2 |
| gen2 | 26,061 | 51.1% | 31.1% | 15.51 | 44.7% | 23.4% | 13.16 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 13,627 | 15.9 | 10.3 | 21.0 | 17.3 | 20.4 | 11.8 | 3.3 | 10.8 | 35.5% | 15.0% |
| STALE | 12,434 | 10.1 | 6.6 | 15.3 | 13.9 | 19.5 | 18.3 | 16.2 | 16.92 | 53.9% | 34.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 13,299 | 16.6 | 11.3 | 22.6 | 15.0 | 17.5 | 12.2 | 4.8 | 9.86 | 34.5% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 45,892 | 13299 | 17099 | 15494 | 23.9 | 125.9 | 1400.4 |
| ge_15pp | 18,930 | 4588 | 6124 | 8218 | 25.7 | 421.9 | 1380.4 |
| ge_25pp | 10,050 | 2256 | 2642 | 5152 | 31.4 | 569.9 | 1380.4 |
| lt_10pp | 19,907 | 6714 | 8065 | 5128 | 21.7 | 47.4 | 1341.5 |

Current slate `SL-20261021T053622Z-360f7d46`: 804 priced rows, quote age at build {'median': 13.7, 'max': 13.8}, freshness {'AGING': 804}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 20 | 0.0 | 0.0 | 25.0 | 0.0 | 40.0 | 35.0 | 0.0 | 20.49 | 75.0% | 35.0% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,422 | 19.6 | 11.0 | 23.4 | 18.6 | 19.3 | 7.3 | 0.7 | 9.14 | 27.3% | 8.0% |
| KALSHI_LONE_OUTLIER | 16 | 6.2 | 6.2 | 75.0 | 0.0 | 6.2 | 6.2 | 0.0 | 5.8 | 12.5% | 6.2% |
| MARKETS_AGREE | 441 | 68.0 | 32.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.16 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 995 | 0.0 | 2.4 | 33.3 | 26.7 | 26.3 | 10.4 | 0.8 | 12.8 | 37.6% | 11.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 26,061 | 3906 (15.0%) | 25.5% | 0.9% | {"EXTERNAL_STALE": 2422, "AGREES_WITH_KALSHI": 995, "ALL_AGREE": 441, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 16, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 11,543 | 1052 (9.1%) | 35.5% | 1.6% | {"EXTERNAL_STALE": 661, "AGREES_WITH_KALSHI": 374, "SUPPORTS_MODEL_DIRECTION": 15, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,332 | 313 (4.9%) | 35.8% | 2.6% | {"EXTERNAL_STALE": 193, "AGREES_WITH_KALSHI": 112, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,116 | 295 (9.5%) | 36.6% | 2.7% | {"EXTERNAL_STALE": 179, "AGREES_WITH_KALSHI": 108, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 10,424 | 2138 (20.5%) | 16.6% | 0.8% | {"EXTERNAL_STALE": 1311, "ALL_AGREE": 441, "AGREES_WITH_KALSHI": 355, "AGREES_WITH_MODEL": 14, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,012 | 10.6 | 7.7 | 19.3 | 14.7 | 22.2 | 15.7 | 9.8 | 13.98 | 47.7% | 25.5% |
| 4-10x | 3,396 | 11.4 | 8.4 | 18.9 | 15.5 | 21.1 | 14.8 | 9.8 | 13.59 | 45.8% | 24.7% |
| <2x | 13,364 | 15.2 | 9.6 | 18.8 | 16.7 | 18.2 | 13.1 | 8.4 | 11.89 | 39.8% | 21.5% |
| >=10x | 4,289 | 11.2 | 6.5 | 15.2 | 13.9 | 22.0 | 19.4 | 11.9 | 16.21 | 53.2% | 31.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,603 | 12.5 | 8.5 | 19.4 | 16.4 | 19.7 | 13.6 | 9.9 | 12.87 | 43.2% | 23.5% |
| 300-1000 | 5,668 | 11.8 | 8.6 | 16.9 | 15.6 | 21.0 | 16.3 | 9.8 | 13.97 | 47.1% | 26.1% |
| <300 | 8,299 | 9.0 | 5.9 | 15.4 | 14.6 | 23.1 | 20.2 | 11.8 | 16.82 | 55.1% | 32.0% |
| >=3000 | 5,491 | 21.5 | 12.6 | 22.7 | 16.8 | 14.7 | 6.9 | 4.8 | 8.08 | 26.4% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 762 | 0.5452 | 0.4094 | 0.4948 | +0.050 | -0.085 | -0.0007 ± 0.0055 |
| ratio 4-10x | 519 | 0.5899 | 0.4447 | 0.501 | +0.089 | -0.056 | 0.0126 ± 0.0071 |
| ratio <2x | 1862 | 0.5372 | 0.4144 | 0.4511 | +0.086 | -0.037 | 0.0123 ± 0.0033 |
| ratio >=10x | 646 | 0.5645 | 0.3906 | 0.4582 | +0.106 | -0.068 | 0.0075 ± 0.0072 |
| thinner_sample 1000-3000 | 1038 | 0.5422 | 0.4157 | 0.4538 | +0.088 | -0.038 | 0.0102 ± 0.0044 |
| thinner_sample 300-1000 | 887 | 0.5663 | 0.4243 | 0.4983 | +0.068 | -0.074 | 0.0003 ± 0.0054 |
| thinner_sample <300 | 1227 | 0.5548 | 0.3902 | 0.4556 | +0.099 | -0.065 | 0.0122 ± 0.005 |
| thinner_sample >=3000 | 637 | 0.5346 | 0.4396 | 0.4725 | +0.062 | -0.033 | 0.0126 ± 0.0046 |
| data_status ADEQUATE | 1087 | 0.5374 | 0.4323 | 0.4609 | +0.076 | -0.029 | 0.0114 ± 0.0038 |
| data_status LIMITED | 920 | 0.5515 | 0.4191 | 0.4804 | +0.071 | -0.061 | 0.0049 ± 0.0049 |
| data_status POOR | 1782 | 0.5583 | 0.3991 | 0.4658 | +0.093 | -0.067 | 0.0095 ± 0.0041 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 563 | 0.1969 | 0.1982 | -0.0014 ± 0.0007 | 0.5723 | 0.5753 | 0.4991 | 0.4842 | 0.5364 | -0.049 ± 0.0196 | -0.01 (5) |
| 3-5 | 359 | 0.1996 | 0.1994 | +0.0002 ± 0.0019 | 0.5819 | 0.58 | 0.5035 | 0.4634 | 0.4791 | -0.088 ± 0.0243 | 0.02 (1) |
| 5-10 | 785 | 0.2009 | 0.2011 | -0.0002 ± 0.0024 | 0.5875 | 0.5861 | 0.5138 | 0.4393 | 0.4739 | -0.084 ± 0.0166 | -0.0167 (6) |
| 10-15 | 657 | 0.2136 | 0.2039 | +0.0096 ± 0.0044 | 0.6167 | 0.5893 | 0.5242 | 0.4 | 0.4231 | -0.100 ± 0.0176 | -0.048 (5) |
| 15-25 | 851 | 0.2257 | 0.2153 | +0.0104 ± 0.0062 | 0.6465 | 0.6154 | 0.5779 | 0.382 | 0.4536 | -0.084 ± 0.0157 | -0.0033 (9) |
| 25-40 | 479 | 0.2268 | 0.2105 | +0.0163 ± 0.0125 | 0.6423 | 0.6049 | 0.6554 | 0.347 | 0.4718 | -0.075 ± 0.0192 | -0.01 (1) |
| 40+ | 95 | 0.3 | 0.1766 | +0.1234 ± 0.0386 | 0.818 | 0.5257 | 0.7498 | 0.3018 | 0.3895 | -0.119 ± 0.0373 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2779 | 0.1826 | 0.1837 | -0.0011 ± 0.0003 | 0.5402 | 0.5415 | 0.4799 | 0.4648 | 0.5027 | -0.018 ± 0.0082 | -0.0129 (17) |
| 3-5 | 1830 | 0.1952 | 0.194 | +0.0012 ± 0.0008 | 0.5712 | 0.565 | 0.4832 | 0.4432 | 0.4475 | -0.053 ± 0.0105 | 0.0 (2) |
| 5-10 | 3886 | 0.1963 | 0.1933 | +0.0031 ± 0.0011 | 0.5753 | 0.5655 | 0.4859 | 0.4119 | 0.4269 | -0.048 ± 0.0072 | -0.0119 (21) |
| 10-15 | 3394 | 0.2029 | 0.1849 | +0.0180 ± 0.0019 | 0.5934 | 0.5432 | 0.4863 | 0.3618 | 0.3518 | -0.074 ± 0.0074 | -0.0281 (16) |
| 15-25 | 4260 | 0.2093 | 0.172 | +0.0373 ± 0.0025 | 0.6123 | 0.5081 | 0.5019 | 0.3055 | 0.3089 | -0.070 ± 0.0063 | -0.0025 (44) |
| 25-40 | 3280 | 0.2248 | 0.1301 | +0.0947 ± 0.0039 | 0.6441 | 0.398 | 0.532 | 0.2194 | 0.2277 | -0.063 ± 0.0061 | -0.01 (1) |
| 40+ | 2118 | 0.3796 | 0.0445 | +0.3352 ± 0.0052 | 0.9888 | 0.173 | 0.6316 | 0.107 | 0.0619 | -0.082 ± 0.0043 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 420 | 0.2006 | 0.2012 | -0.0006 ± 0.0008 | 0.583 | 0.5843 | 0.501 | 0.4861 | 0.5119 | -0.086 ± 0.0235 | -0.01 (3) |
| 3-5 | 314 | 0.2202 | 0.219 | +0.0012 ± 0.0021 | 0.6259 | 0.6236 | 0.5129 | 0.4728 | 0.4713 | -0.107 ± 0.0285 | 0.02 (1) |
| 5-10 | 668 | 0.1992 | 0.2002 | -0.0010 ± 0.0026 | 0.5817 | 0.5836 | 0.5476 | 0.4726 | 0.5165 | -0.070 ± 0.0178 | -0.01 (4) |
| 10-15 | 629 | 0.2181 | 0.2122 | +0.0059 ± 0.0046 | 0.6264 | 0.6112 | 0.5645 | 0.4401 | 0.4817 | -0.095 ± 0.019 | -0.04 (5) |
| 15-25 | 905 | 0.2312 | 0.2111 | +0.0201 ± 0.006 | 0.656 | 0.605 | 0.5917 | 0.3953 | 0.4464 | -0.098 ± 0.0155 | -0.0133 (9) |
| 25-40 | 629 | 0.2633 | 0.2004 | +0.0629 ± 0.0112 | 0.7345 | 0.5825 | 0.6576 | 0.3419 | 0.4022 | -0.110 ± 0.0175 | -0.0075 (4) |
| 40+ | 224 | 0.3659 | 0.1664 | +0.1995 ± 0.027 | 1.0106 | 0.4988 | 0.7375 | 0.2547 | 0.3036 | -0.088 ± 0.0261 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2319 | 0.1891 | 0.1895 | -0.0004 ± 0.0003 | 0.5556 | 0.5563 | 0.5017 | 0.4868 | 0.508 | -0.036 ± 0.0094 | -0.0133 (15) |
| 3-5 | 1590 | 0.198 | 0.1983 | -0.0002 ± 0.0009 | 0.5742 | 0.5745 | 0.5111 | 0.4711 | 0.4931 | -0.031 ± 0.0114 | 0.02 (1) |
| 5-10 | 3446 | 0.1923 | 0.1914 | +0.0009 ± 0.0011 | 0.5674 | 0.5616 | 0.5055 | 0.4315 | 0.4643 | -0.028 ± 0.0075 | -0.0117 (6) |
| 10-15 | 3067 | 0.2001 | 0.1897 | +0.0104 ± 0.002 | 0.5878 | 0.5524 | 0.5142 | 0.3901 | 0.4118 | -0.048 ± 0.008 | -0.0189 (18) |
| 15-25 | 4336 | 0.2172 | 0.1801 | +0.0372 ± 0.0025 | 0.6316 | 0.5281 | 0.5294 | 0.3331 | 0.3397 | -0.068 ± 0.0065 | -0.0086 (42) |
| 25-40 | 3855 | 0.2517 | 0.1396 | +0.1121 ± 0.0038 | 0.7085 | 0.4272 | 0.5624 | 0.2459 | 0.2301 | -0.084 ± 0.006 | -0.0044 (18) |
| 40+ | 2934 | 0.3993 | 0.0621 | +0.3372 ± 0.0053 | 1.0517 | 0.2206 | 0.6584 | 0.1224 | 0.0886 | -0.072 ± 0.0045 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 537 | 0.1977 | 0.2001 | -0.0024 ± 0.0007 | 0.5755 | 0.5812 | 0.4952 | 0.4798 | 0.5531 | -0.013 ± 0.0197 | -0.0137 (8) |
| 3-5 | 392 | 0.194 | 0.1918 | +0.0022 ± 0.0018 | 0.5656 | 0.5605 | 0.5041 | 0.4646 | 0.4592 | -0.118 ± 0.0231 | 0.0067 (3) |
| 5-10 | 811 | 0.2015 | 0.1985 | +0.0030 ± 0.0024 | 0.59 | 0.5795 | 0.511 | 0.4371 | 0.4513 | -0.096 ± 0.0161 | -0.0071 (7) |
| 10-15 | 660 | 0.2097 | 0.2057 | +0.0040 ± 0.0044 | 0.6072 | 0.5941 | 0.5391 | 0.4158 | 0.4636 | -0.084 ± 0.0175 | -0.0317 (6) |
| 15-25 | 798 | 0.2334 | 0.2126 | +0.0208 ± 0.0064 | 0.666 | 0.6087 | 0.5855 | 0.3916 | 0.4348 | -0.112 ± 0.0162 | -0.03 (1) |
| 25-40 | 493 | 0.2147 | 0.2183 | -0.0036 ± 0.0123 | 0.6167 | 0.6233 | 0.6648 | 0.3539 | 0.5132 | -0.049 ± 0.0189 | 0.015 (2) |
| 40+ | 98 | 0.3093 | 0.1956 | +0.1137 ± 0.0399 | 0.8461 | 0.5688 | 0.7622 | 0.3107 | 0.4184 | -0.098 ± 0.0411 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2698 | 0.1857 | 0.1864 | -0.0007 ± 0.0003 | 0.547 | 0.5483 | 0.4865 | 0.4711 | 0.4885 | -0.035 ± 0.0084 | -0.0163 (35) |
| 3-5 | 1858 | 0.1865 | 0.1836 | +0.0030 ± 0.0008 | 0.5504 | 0.5432 | 0.4833 | 0.4437 | 0.4273 | -0.077 ± 0.0102 | -0.0094 (18) |
| 5-10 | 4069 | 0.197 | 0.1914 | +0.0056 ± 0.001 | 0.5784 | 0.5597 | 0.4872 | 0.4133 | 0.4109 | -0.062 ± 0.0069 | -0.01 (31) |
| 10-15 | 3243 | 0.1967 | 0.18 | +0.0167 ± 0.0019 | 0.5781 | 0.5303 | 0.5022 | 0.3786 | 0.3731 | -0.071 ± 0.0074 | -0.015 (12) |
| 15-25 | 4371 | 0.2137 | 0.174 | +0.0397 ± 0.0025 | 0.6223 | 0.5129 | 0.5093 | 0.3148 | 0.3098 | -0.076 ± 0.0063 | -0.03 (2) |
| 25-40 | 3257 | 0.2204 | 0.1316 | +0.0888 ± 0.004 | 0.6347 | 0.4007 | 0.5343 | 0.2182 | 0.2379 | -0.055 ± 0.0061 | 0.01 (3) |
| 40+ | 2051 | 0.3947 | 0.0494 | +0.3453 ± 0.0056 | 1.0317 | 0.1859 | 0.6443 | 0.1139 | 0.0668 | -0.085 ± 0.0047 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 901 | 0.1956 | 0.1958 | -0.0002 ± 0.0005 | 0.571 | 0.5712 | 0.5061 | 0.491 | 0.4939 | -0.059 ± 0.015 | -0.0224 (49) |
| 3-5 | 626 | 0.1926 | 0.1921 | +0.0005 ± 0.0014 | 0.5626 | 0.5604 | 0.4836 | 0.4438 | 0.4553 | -0.052 ± 0.0177 | -0.0194 (34) |
| 5-10 | 1327 | 0.2 | 0.1937 | +0.0064 ± 0.0018 | 0.5879 | 0.569 | 0.4911 | 0.4178 | 0.413 | -0.071 ± 0.0123 | -0.005 (78) |
| 10-15 | 867 | 0.2092 | 0.1986 | +0.0106 ± 0.0038 | 0.6066 | 0.5793 | 0.5164 | 0.3934 | 0.4106 | -0.064 ± 0.0154 | 0.0014 (64) |
| 15-25 | 1156 | 0.2313 | 0.2114 | +0.0199 ± 0.0053 | 0.6601 | 0.6088 | 0.5727 | 0.3778 | 0.4256 | -0.065 ± 0.0136 | -0.0214 (59) |
| 25-40 | 703 | 0.2497 | 0.2043 | +0.0454 ± 0.0105 | 0.7079 | 0.5887 | 0.6639 | 0.3511 | 0.4339 | -0.086 ± 0.0159 | -0.0219 (26) |
| 40+ | 241 | 0.3517 | 0.1964 | +0.1553 ± 0.0284 | 1.0155 | 0.5747 | 0.8055 | 0.3208 | 0.4232 | -0.085 ± 0.0255 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2950 | 0.1833 | 0.1835 | -0.0002 ± 0.0003 | 0.5398 | 0.5394 | 0.5064 | 0.4911 | 0.4997 | -0.038 ± 0.0079 | -0.0157 (88) |
| 3-5 | 2027 | 0.1911 | 0.1891 | +0.0020 ± 0.0008 | 0.5586 | 0.5546 | 0.4898 | 0.4501 | 0.445 | -0.053 ± 0.0097 | -0.0209 (69) |
| 5-10 | 4080 | 0.1971 | 0.1884 | +0.0088 ± 0.001 | 0.5794 | 0.5545 | 0.4872 | 0.4137 | 0.3939 | -0.072 ± 0.0069 | -0.0082 (132) |
| 10-15 | 2836 | 0.2051 | 0.1904 | +0.0147 ± 0.002 | 0.5983 | 0.5595 | 0.5233 | 0.4003 | 0.4016 | -0.060 ± 0.0082 | -0.0053 (105) |
| 15-25 | 3502 | 0.2293 | 0.1988 | +0.0306 ± 0.003 | 0.6614 | 0.5772 | 0.5654 | 0.3701 | 0.3909 | -0.064 ± 0.0076 | -0.0253 (107) |
| 25-40 | 2431 | 0.2599 | 0.1823 | +0.0776 ± 0.0055 | 0.736 | 0.5328 | 0.6246 | 0.3101 | 0.3468 | -0.075 ± 0.0084 | -0.0229 (51) |
| 40+ | 1098 | 0.3766 | 0.1398 | +0.2368 ± 0.0119 | 1.0665 | 0.4236 | 0.725 | 0.2217 | 0.2514 | -0.073 ± 0.0105 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3789 | 1.044 ± 0.046 | 1.165 | 0.167 | 0.1647 | 0.2137 | 0.2048 |
| gen2 | 3789 | 0.843 ± 0.042 | 1.127 | 0.1705 | 0.1652 | 0.2324 | 0.2045 |
| gen1_elo | 3789 | 1.022 ± 0.045 | 1.147 | 0.1736 | 0.165 | 0.2128 | 0.2048 |
| gen1_sr | 3789 | 1.044 ± 0.055 | 1.204 | 0.1312 | 0.167 | 0.2286 | 0.2041 |
| gen1_ledger | 5821 | 0.873 ± 0.032 | 1.085 | 0.1802 | 0.1796 | 0.2184 | 0.1995 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 18,930)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,302 | 22.7% |
| STALE_QUOTE | market_freshness | 3,985 | 21.1% |
| BOOK_QUALITY | execution | 3,638 | 19.2% |
| POOR_DATA | data | 2,179 | 11.5% |
| LIMITED_DATA | data | 1,247 | 6.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,010 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 944 | 5.0% |
| IDENTITY_AMBIGUOUS | mapping | 770 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 541 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 314 | 1.7% |

Cause class: coverage 22.7%, market_freshness 21.1%, execution 19.2%, data 18.1%, market_freshness/coverage 8.2%, model_calibration_or_unknown 5.0%, mapping 4.1%, model_calibration 1.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.9%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 70.6%, THIN_PLAYER_HISTORY 59.4%, STALE_PLAYER_DATA 51.7%, STALE_KALSHI_QUOTE 43.4%, MODEL_INTERNAL_DISAGREEMENT 41.9%, ASYMMETRIC_SAMPLE_SIZE 32.8%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 15.5%, LEVEL_TRANSFER_RISK 10.4%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.0%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.2%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 10,050)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,425 | 34.1% |
| BOOK_QUALITY | execution | 1,909 | 19.0% |
| STALE_QUOTE | market_freshness | 1,817 | 18.1% |
| POOR_DATA | data | 911 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 533 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 441 | 4.4% |
| LIMITED_DATA | data | 380 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 338 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 221 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.8% |

Cause class: coverage 34.1%, execution 19.0%, market_freshness 18.1%, data 12.8%, market_freshness/coverage 8.7%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.5%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 51.3%, STALE_PLAYER_DATA 47.0%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 25.0%, PLAYER_IDENTITY_RISK 18.9%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.0%, POST_SETTLEMENT_OBSERVATION 34.1%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 7888, "IDENTITY_AMBIGUOUS": 2162}; ticker orientation: {"VERIFIED": 10050}.

Checks: discipline:AMBIGUOUS 688, discipline:PASS 9362, identity_confidence:AMBIGUOUS 1896, identity_confidence:PASS 8154, level_mapping:NA 700, level_mapping:PASS 9350, market_pair:AMBIGUOUS 369, market_pair:NA 241, market_pair:PASS 9440, model_complement:NA 208, model_complement:PASS 9842, namesake:PASS 10050, physical_match_id:NA 3718, physical_match_id:PASS 6332, player_ids:PASS 10050, same_pair_other_event:PASS 10050, ticker_orientation:PASS 10050

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,591 | 5.0% | 4.6% | 1.8% | {"market_freshness": 53, "model_calibration_or_unknown": 40, "data": 35, "execution": 19, "model_calibration": 13, "market_freshness/coverage": 11, "coverage": 7} | 5.86 | 0.2252 / 0.2154 (397) | 18.7% | 4.0% | 3.5% | 2.7% |
| CHALLENGER | 7,284 | 17.2% | 6.9% | 12.5% | {"coverage": 706, "market_freshness/coverage": 157, "market_freshness": 146, "data": 115, "model_calibration_or_unknown": 59, "execution": 30, "model_calibration": 27, "mapping": 14} | 7.48 | 0.2178 / 0.2073 (1772) | 35.1% | 17.2% | 3.9% | 22.7% |
| DOUBLES | 1,428 | 48.2% | 47.7% | 6.9% | {"execution": 351, "mapping": 177, "market_freshness": 106, "market_freshness/coverage": 47, "coverage": 7} | 23.92 | 0.3213 / 0.2344 (363) | 16.4% | 0.0% | 100.0% | 6.9% |
| ITF_MEN | 12,473 | 25.0% | 17.6% | 31.0% | {"coverage": 1144, "execution": 629, "market_freshness": 514, "data": 430, "market_freshness/coverage": 251, "mapping": 145, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.55 | 0.2143 / 0.1952 (2826) | 36.5% | 66.2% | 17.1% | 21.7% |
| ITF_WOMEN | 16,970 | 26.6% | 19.6% | 44.9% | {"coverage": 1544, "market_freshness": 920, "execution": 849, "data": 677, "market_freshness/coverage": 356, "mapping": 99, "model_calibration_or_unknown": 52, "model_calibration": 11} | 12.87 | 0.2032 / 0.1949 (3299) | 38.3% | 57.6% | 10.1% | 21.4% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,605 | 4.6% | 4.2% | 1.2% | {"market_freshness": 38, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 4, "mapping": 1} | 7.91 | 0.2366 / 0.2303 (423) | 23.8% | 1.3% | 1.4% | 3.4% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.7% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 15 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 16 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 17 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 18 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 19 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 20 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 21 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 22 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 23 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 24 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 25 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 26 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 27 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 30 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 31 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 32 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 36 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 37 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 38 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 39 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 41 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 42 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 43 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 44 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 45 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 46 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 134 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 47 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 535 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 48 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 49 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9704, "by_level_share_of_ge_25pp": {"ATP": 0.0177, "CHALLENGER": 0.1248, "DOUBLES": 0.0685, "ITF_MEN": 0.31, "ITF_WOMEN": 0.4486, "OTHER": 0.0012, "WTA": 0.0119, "WTA125": 0.0173}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5126, "share_primary_cause_market_settled_or_in_play": 0.4274, "share_primary_cause_stale_quote_only": 0.1808}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 10050, "identity_ambiguous_share": 0.2151, "ticker_orientation": {"VERIFIED": 10050}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6332, "with_external": 313, "coverage": 0.0494, "external_status": {"EXTERNAL_STALE": 193, "AGREES_WITH_KALSHI": 112, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 193, "MODEL_LONE_OUTLIER": 112, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3578, "share_external_supports_model": 0.0256}, "pregame_clean_ge_25pp": {"n": 3116, "with_external": 295, "coverage": 0.0947, "external_status": {"EXTERNAL_STALE": 179, "AGREES_WITH_KALSHI": 108, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 179, "MODEL_LONE_OUTLIER": 108, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3661, "share_external_supports_model": 0.0271}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 499.0, "median_sample_ratio": 2.43, "median_min_matches": 20.0, "median_max_days_since_last": 223.0, "share_severe_asymmetry": 0.2096, "data_status": {"POOR": 5561, "LIMITED": 2729, "ADEQUATE": 1760}, "comparison_lt_10pp": {"median_thinner_serve_points": 1732.0, "median_sample_ratio": 1.69, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 762, "model_minus_observed": 0.0504, "kalshi_minus_observed": -0.0854, "brier_diff_model_minus_kalshi": -0.0007}, "4-10x": {"n": 519, "model_minus_observed": 0.089, "kalshi_minus_observed": -0.0563, "brier_diff_model_minus_kalshi": 0.0126}, "<2x": {"n": 1862, "model_minus_observed": 0.086, "kalshi_minus_observed": -0.0368, "brier_diff_model_minus_kalshi": 0.0123}, ">=10x": {"n": 646, "model_minus_observed": 0.1063, "kalshi_minus_observed": -0.0676, "brier_diff_model_minus_kalshi": 0.0075}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3789, "model": {"intercept": -0.528, "slope": 0.843, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.241, "slope": 1.127, "slope_se": 0.048}, "mean_extremity_model": 0.1705, "mean_extremity_kalshi": 0.1652, "model_brier": 0.2324, "kalshi_brier": 0.2045, "brier_diff_model_minus_kalshi": 0.0279, "brier_diff_se": 0.0031, "model_logloss": 0.6614, "kalshi_logloss": 0.5915}, "fair_v1": {"n": 3789, "model": {"intercept": -0.398, "slope": 1.044, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.32, "slope": 1.165, "slope_se": 0.049}, "mean_extremity_model": 0.167, "mean_extremity_kalshi": 0.1647, "model_brier": 0.2137, "kalshi_brier": 0.2048, "brier_diff_model_minus_kalshi": 0.0089, "brier_diff_se": 0.0025, "model_logloss": 0.6157, "kalshi_logloss": 0.5919}, "gen1_elo": {"n": 3789, "model": {"intercept": -0.395, "slope": 1.022, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.311, "slope": 1.147, "slope_se": 0.048}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.165, "model_brier": 0.2128, "kalshi_brier": 0.2048, "brier_diff_model_minus_kalshi": 0.0081, "brier_diff_se": 0.0025, "model_logloss": 0.6145, "kalshi_logloss": 0.5919}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.243, "share_ge_15": 0.4429, "median_abs_gap": 13.11, "n": 26061}, "gen1_elo": {"share_ge_25": 0.2402, "share_ge_15": 0.4394, "median_abs_gap": 12.81, "n": 26061}, "gen1_sr": {"share_ge_25": 0.3084, "share_ge_15": 0.5224, "median_abs_gap": 15.89, "n": 26061}, "gen2": {"share_ge_25": 0.3107, "share_ge_15": 0.5114, "median_abs_gap": 15.51, "n": 26061}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1532, "share_ge_15": 0.3606, "median_abs_gap": 10.95, "n": 20344}, "gen1_elo": {"share_ge_25": 0.1539, "share_ge_15": 0.3545, "median_abs_gap": 10.53, "n": 20342}, "gen1_sr": {"share_ge_25": 0.2185, "share_ge_15": 0.4475, "median_abs_gap": 13.2, "n": 20345}, "gen2": {"share_ge_25": 0.2337, "share_ge_15": 0.4471, "median_abs_gap": 13.16, "n": 20345}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0496, "share_ge_25_pregame_clean": 0.0458}, "WTA": {"median_abs_gap_pregame_clean": 7.91, "share_ge_25_all": 0.0461, "share_ge_25_pregame_clean": 0.0421}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2364, "share_within_10pp_all": 0.4338, "share_within_10pp_pregame_clean": 0.4855, "corr_model_vs_mid_pregame_clean": 0.8445}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 563, "model_brier": 0.1969, "kalshi_brier": 0.1982, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 657, "model_brier": 0.2136, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0096}, "15-25": {"n_settled": 851, "model_brier": 0.2257, "kalshi_brier": 0.2153, "brier_diff_model_minus_kalshi": 0.0104}, "25-40": {"n_settled": 479, "model_brier": 0.2268, "kalshi_brier": 0.2105, "brier_diff_model_minus_kalshi": 0.0163}, "3-5": {"n_settled": 359, "model_brier": 0.1996, "kalshi_brier": 0.1994, "brier_diff_model_minus_kalshi": 0.0002}, "40+": {"n_settled": 95, "model_brier": 0.3, "kalshi_brier": 0.1766, "brier_diff_model_minus_kalshi": 0.1234}, "5-10": {"n_settled": 785, "model_brier": 0.2009, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": -0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.528, "slope": 0.843, "slope_se": 0.042}, "kalshi_slope": {"intercept": 0.241, "slope": 1.127, "slope_se": 0.048}, "n": 3789}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.51, "slope": 0.873, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.16, "slope": 1.085, "slope_se": 0.037}, "n": 5821}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 363, "model_brier": 0.3213, "kalshi_brier": 0.2344, "brier_diff_model_minus_kalshi": 0.0869, "brier_diff_se": 0.0164, "corr_model_outcome": 0.0116, "corr_kalshi_outcome": 0.2588}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
