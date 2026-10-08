# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-08T10:09Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 24,488): 0-3 13.9%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 18.7%, 25-40 14.2%, 40+ 8.4%; median gap 12.01 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.5%, Challenger 12.5%, doubles 5.8%). Main tour: ATP 1.8% and WTA 8.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,511): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.2%, STALE_QUOTE 17.8%, BOOK_QUALITY 17.0%, POOR_DATA 8.4%, POSSIBLY_IN_PLAY_QUOTE 5.1%, LIMITED_DATA 4.3%, IN_PLAY_QUOTE 3.2%, IDENTITY_AMBIGUOUS 2.9%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.2%. By class: coverage 39.2%, market_freshness 17.8%, execution 17.0%, data 12.7%, market_freshness/coverage 8.2%, mapping 2.9%, model_calibration_or_unknown 2.1%, model_calibration 0.2%.
* **Stale / settled / in-play**: 56.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 47.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,511 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 10.5% of the time and with the model 0.3%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 605.0 points vs 1716.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.115, Gen-2 0.893, Gen-1 ledger 0.938 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 223 model 0.2166 vs Kalshi 0.2047; n 51 model 0.2726 vs Kalshi 0.1802.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 91,506 model-market comparisons (153,822 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 34,630 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-08T10:01:57.167934+00:00'], shadow board 25,500 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-08T10:02:01.202327+00:00'], Model 4 9,304 rows, 10,548 settled tickers, 2,871 tickers with an external scan.
* By model: {"gen1_ledger": 21921, "gen1_elo": 12812, "fair_v1": 12812, "gen2": 12812, "gen1_sr": 12812, "model4_fundamental": 9173, "model4_conditioned": 9164}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 24,488 | 13.9 | 9.6 | 19.9 | 15.4 | 18.7 | 14.2 | 8.4 | 12.01 | 41.2% | 22.5% |
| MW fair_v1 | 12,812 | 13.2 | 8.8 | 18.4 | 16.1 | 18.5 | 15.0 | 10.0 | 12.98 | 43.5% | 25.1% |
| MW gen1_elo | 12,812 | 12.8 | 8.8 | 20.0 | 15.0 | 19.3 | 14.7 | 9.4 | 12.53 | 43.4% | 24.1% |
| MW gen1_ledger | 11,676 | 14.7 | 10.5 | 21.6 | 14.6 | 18.9 | 13.2 | 6.5 | 10.89 | 38.6% | 19.7% |
| MW gen1_sr | 12,812 | 10.2 | 7.8 | 16.1 | 14.2 | 21.5 | 18.6 | 11.7 | 15.59 | 51.8% | 30.3% |
| MW gen2 | 12,812 | 12.0 | 7.2 | 16.1 | 14.3 | 19.8 | 17.5 | 13.2 | 15.26 | 50.5% | 30.7% |
| all families model4_conditioned | 9,164 | 21.9 | 20.6 | 35.4 | 15.9 | 4.5 | 0.9 | 0.8 | 5.71 | 6.2% | 1.7% |
| all families model4_fundamental | 9,173 | 16.4 | 13.3 | 34.9 | 20.4 | 10.9 | 3.0 | 1.2 | 7.77 | 15.1% | 4.2% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.6%, >=15pp 41.2%, >=20pp 30.8%, >=25pp 22.5%, >=30pp 16.4%, >=40pp 8.4%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.49pp; >=10pp 45.6%, >=25pp 18.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 919 | 26.4 | 15.9 | 24.1 | 17.9 | 13.1 | 1.4 | 1.2 | 6.01 | 15.7% | 2.6% |
| CHALLENGER | 2,208 | 15.2 | 11.0 | 18.5 | 16.1 | 13.0 | 13.3 | 13.0 | 11.95 | 39.3% | 26.3% |
| ITF_MEN | 3,700 | 11.1 | 8.6 | 18.8 | 14.8 | 19.4 | 15.1 | 12.3 | 13.77 | 46.8% | 27.4% |
| ITF_WOMEN | 5,133 | 10.5 | 6.8 | 16.1 | 16.2 | 21.5 | 19.1 | 9.9 | 15.19 | 50.5% | 29.0% |
| WTA | 537 | 23.8 | 9.5 | 25.1 | 16.2 | 17.1 | 6.2 | 2.0 | 8.09 | 25.3% | 8.2% |
| WTA125 | 315 | 12.1 | 6.7 | 21.6 | 26.0 | 14.6 | 16.5 | 2.5 | 11.33 | 33.7% | 19.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 919 | 21.9 | 14.2 | 24.1 | 18.8 | 17.2 | 2.4 | 1.4 | 6.9 | 21.0% | 3.8% |
| CHALLENGER | 2,208 | 15.2 | 7.5 | 17.8 | 13.4 | 18.2 | 14.4 | 13.4 | 13.15 | 46.0% | 27.8% |
| ITF_MEN | 3,700 | 10.7 | 7.4 | 16.8 | 14.6 | 19.8 | 17.6 | 13.0 | 15.29 | 50.4% | 30.6% |
| ITF_WOMEN | 5,133 | 9.1 | 6.0 | 13.0 | 13.1 | 20.8 | 21.3 | 16.6 | 18.87 | 58.7% | 37.9% |
| WTA | 537 | 22.2 | 5.2 | 18.2 | 15.1 | 21.0 | 16.2 | 2.0 | 12.38 | 39.3% | 18.2% |
| WTA125 | 315 | 4.8 | 2.9 | 17.1 | 22.2 | 20.6 | 20.3 | 12.1 | 16.84 | 53.0% | 32.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 919 | 25.9 | 12.1 | 29.8 | 16.4 | 11.1 | 3.4 | 1.3 | 6.65 | 15.8% | 4.7% |
| CHALLENGER | 2,208 | 15.8 | 10.9 | 19.8 | 14.0 | 14.1 | 12.4 | 12.9 | 10.95 | 39.5% | 25.4% |
| ITF_MEN | 3,700 | 10.1 | 8.8 | 18.6 | 14.1 | 20.5 | 15.5 | 12.4 | 14.18 | 48.4% | 27.9% |
| ITF_WOMEN | 5,133 | 9.6 | 6.7 | 17.0 | 15.7 | 23.4 | 18.9 | 8.6 | 15.42 | 50.9% | 27.5% |
| WTA | 537 | 22.9 | 13.0 | 35.4 | 14.5 | 9.3 | 3.5 | 1.3 | 6.99 | 14.1% | 4.8% |
| WTA125 | 315 | 20.9 | 11.8 | 29.5 | 17.1 | 14.9 | 5.1 | 0.6 | 7.99 | 20.6% | 5.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 453 | 28.0 | 21.9 | 37.3 | 11.0 | 1.6 | 0.2 | 0.0 | 5.02 | 1.8% | 0.2% |
| CHALLENGER | 1,429 | 22.9 | 17.1 | 26.0 | 14.1 | 12.3 | 5.5 | 2.1 | 6.68 | 19.9% | 7.6% |
| DOUBLES | 670 | 4.0 | 3.6 | 11.8 | 11.3 | 21.3 | 24.6 | 23.3 | 23.92 | 69.2% | 47.9% |
| ITF_MEN | 3,706 | 14.4 | 8.7 | 20.7 | 15.0 | 20.3 | 12.8 | 8.1 | 11.91 | 41.2% | 20.9% |
| ITF_WOMEN | 4,344 | 11.7 | 9.4 | 19.8 | 14.2 | 21.9 | 17.0 | 5.9 | 13.0 | 44.8% | 22.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 440 | 20.4 | 11.6 | 25.7 | 18.9 | 15.4 | 7.3 | 0.7 | 8.45 | 23.4% | 8.0% |
| WTA125 | 485 | 16.3 | 12.6 | 22.3 | 19.8 | 17.1 | 9.1 | 2.9 | 9.59 | 29.1% | 12.0% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 915 | 26.4 | 15.7 | 24.0 | 18.0 | 13.1 | 1.4 | 1.2 | 6.01 | 15.7% | 2.6% |
| CHALLENGER | 1,567 | 20.0 | 14.0 | 24.0 | 18.8 | 13.7 | 6.8 | 2.9 | 8.07 | 23.3% | 9.6% |
| ITF_MEN | 2,714 | 13.5 | 10.8 | 22.0 | 16.5 | 19.5 | 12.2 | 5.6 | 11.01 | 37.2% | 17.8% |
| ITF_WOMEN | 3,748 | 12.9 | 8.4 | 18.9 | 18.6 | 23.0 | 15.2 | 3.0 | 12.61 | 41.2% | 18.2% |
| WTA | 534 | 23.8 | 9.6 | 25.3 | 16.1 | 17.2 | 6.0 | 2.1 | 8.06 | 25.3% | 8.1% |
| WTA125 | 304 | 12.5 | 6.9 | 21.4 | 26.3 | 14.8 | 16.4 | 1.6 | 11.31 | 32.9% | 18.1% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 915 | 21.8 | 14.2 | 24.1 | 18.8 | 17.3 | 2.4 | 1.4 | 6.9 | 21.1% | 3.8% |
| CHALLENGER | 1,567 | 20.0 | 9.9 | 22.6 | 16.4 | 18.6 | 9.8 | 2.7 | 9.2 | 31.1% | 12.6% |
| ITF_MEN | 2,715 | 12.6 | 8.8 | 19.6 | 16.6 | 20.9 | 15.2 | 6.3 | 12.58 | 42.4% | 21.5% |
| ITF_WOMEN | 3,748 | 10.6 | 7.2 | 15.0 | 14.3 | 22.9 | 19.9 | 10.2 | 16.09 | 53.0% | 30.1% |
| WTA | 534 | 22.1 | 5.2 | 18.4 | 15.2 | 21.0 | 16.1 | 2.1 | 12.32 | 39.1% | 18.2% |
| WTA125 | 304 | 4.9 | 3.0 | 17.4 | 23.0 | 19.7 | 21.1 | 10.9 | 16.39 | 51.6% | 31.9% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 438 | 28.3 | 22.1 | 37.4 | 11.2 | 0.7 | 0.2 | 0.0 | 4.97 | 0.9% | 0.2% |
| CHALLENGER | 1,211 | 24.9 | 19.3 | 28.2 | 13.8 | 11.6 | 2.1 | 0.1 | 6.0 | 13.9% | 2.2% |
| DOUBLES | 616 | 4.1 | 3.6 | 12.0 | 11.2 | 21.6 | 24.5 | 23.1 | 23.82 | 69.2% | 47.6% |
| ITF_MEN | 3,000 | 16.1 | 9.7 | 23.0 | 16.0 | 20.0 | 10.4 | 4.7 | 10.25 | 35.1% | 15.1% |
| ITF_WOMEN | 3,545 | 13.1 | 10.2 | 21.7 | 15.2 | 22.1 | 15.3 | 2.5 | 11.41 | 39.9% | 17.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 410 | 21.0 | 12.2 | 26.3 | 19.0 | 15.8 | 5.6 | 0.0 | 8.37 | 21.5% | 5.6% |
| WTA125 | 402 | 18.4 | 13.9 | 24.9 | 22.6 | 15.2 | 4.7 | 0.2 | 8.29 | 20.2% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 670 | 4.0 | 3.6 | 11.8 | 11.3 | 21.3 | 24.6 | 23.3 | 23.92 | 69.2% | 47.9% |
| singles | 11,006 | 15.4 | 10.9 | 22.2 | 14.8 | 18.7 | 12.5 | 5.5 | 10.37 | 36.7% | 18.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 2,991 | 13.3 | 9.6 | 20.5 | 15.5 | 15.9 | 14.6 | 10.5 | 12.15 | 41.1% | 25.2% |
| Hard | 8,587 | 13.3 | 8.6 | 18.2 | 16.1 | 19.1 | 14.8 | 9.9 | 13.06 | 43.9% | 24.8% |
| UNKNOWN | 1,234 | 12.2 | 8.3 | 14.4 | 18.1 | 20.2 | 17.5 | 9.2 | 14.01 | 46.9% | 26.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,671 | 18.6 | 11.1 | 20.4 | 17.0 | 14.9 | 9.8 | 8.1 | 9.98 | 32.9% | 17.9% |
| B | 1,648 | 15.2 | 9.7 | 19.7 | 17.5 | 16.2 | 12.0 | 9.7 | 11.12 | 37.9% | 21.7% |
| C | 1,999 | 12.7 | 10.0 | 20.1 | 15.1 | 18.5 | 14.3 | 9.3 | 12.57 | 42.1% | 23.6% |
| D | 2,448 | 11.3 | 8.5 | 17.2 | 16.3 | 22.3 | 15.2 | 9.2 | 13.94 | 46.7% | 24.4% |
| F | 3,046 | 7.4 | 4.9 | 15.0 | 14.9 | 20.9 | 23.3 | 13.6 | 18.41 | 57.8% | 36.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,165 | 21.3 | 15.4 | 27.4 | 15.9 | 12.7 | 5.3 | 2.1 | 7.16 | 20.1% | 7.4% |
| B | 1,831 | 14.6 | 9.9 | 24.6 | 16.2 | 18.0 | 11.6 | 5.0 | 10.18 | 34.6% | 16.6% |
| C | 2,353 | 12.2 | 8.3 | 19.0 | 14.1 | 20.8 | 15.6 | 10.1 | 13.24 | 46.5% | 25.7% |
| D | 1,980 | 13.8 | 9.1 | 21.2 | 13.0 | 22.1 | 14.5 | 6.4 | 12.14 | 42.9% | 20.9% |
| F | 2,347 | 9.3 | 7.9 | 14.2 | 13.5 | 23.2 | 21.5 | 10.3 | 16.91 | 55.0% | 31.9% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,151 | 17.5 | 10.3 | 19.5 | 17.2 | 15.1 | 10.2 | 10.1 | 10.7 | 35.4% | 20.3% |
| LIMITED | 3,127 | 14.6 | 10.7 | 21.1 | 15.7 | 17.5 | 13.3 | 7.2 | 11.08 | 38.0% | 20.5% |
| POOR | 5,534 | 9.2 | 6.6 | 15.9 | 15.5 | 21.5 | 19.6 | 11.6 | 16.05 | 52.7% | 31.2% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,885 | 29.8 | 25.7 | 36.9 | 5.5 | 1.7 | 0.4 | 0.0 | 4.52 | 2.1% | 0.4% |
| GAME_SPREAD | 1,916 | 24.5 | 15.3 | 36.9 | 18.4 | 4.5 | 0.3 | 0.2 | 6.18 | 5.0% | 0.4% |
| MATCH_WINNER | 11,676 | 14.7 | 10.5 | 21.6 | 14.6 | 18.9 | 13.2 | 6.5 | 10.89 | 38.6% | 19.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 3,554 | 29.9 | 19.2 | 31.0 | 11.1 | 7.2 | 1.4 | 0.3 | 5.07 | 8.8% | 1.7% |
| TOTAL_GAMES | 2,866 | 7.4 | 9.1 | 38.2 | 30.1 | 9.7 | 3.2 | 2.2 | 9.45 | 15.1% | 5.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,384 | 24.1 | 39.5 | 30.0 | 0.3 | 5.5 | 0.6 | 0.2 | 4.34 | 6.2% | 0.7% |
| GAME_SPREAD | 2,344 | 46.2 | 14.2 | 29.2 | 8.2 | 1.2 | 0.7 | 0.3 | 3.49 | 2.2% | 1.0% |
| TOTAL_GAMES | 3,436 | 3.4 | 6.3 | 45.0 | 36.6 | 5.7 | 1.4 | 1.8 | 9.59 | 8.8% | 3.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 3,384 | 25.3 | 18.3 | 35.9 | 10.0 | 7.2 | 3.0 | 0.4 | 5.63 | 10.6% | 3.4% |
| GAME_SPREAD | 2,344 | 18.9 | 13.1 | 26.6 | 23.0 | 14.7 | 2.9 | 0.7 | 8.39 | 18.4% | 3.7% |
| TOTAL_GAMES | 3,445 | 5.9 | 8.5 | 39.6 | 28.8 | 12.0 | 3.1 | 2.1 | 9.58 | 17.2% | 5.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 12,812 | 43.5% | 25.1% | 12.98 | 33.7% | 14.7% | 10.45 |
| gen1_elo | 12,812 | 43.4% | 24.1% | 12.53 | 33.3% | 14.2% | 10.01 |
| gen1_sr | 12,812 | 51.8% | 30.3% | 15.59 | 43.0% | 20.1% | 12.77 |
| gen2 | 12,812 | 50.5% | 30.7% | 15.26 | 42.8% | 21.9% | 12.66 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 6,394 | 16.0 | 11.2 | 21.4 | 17.5 | 18.6 | 11.9 | 3.4 | 10.38 | 34.0% | 15.4% |
| STALE | 6,418 | 10.4 | 6.5 | 15.3 | 14.8 | 18.3 | 18.1 | 16.6 | 16.6 | 53.0% | 34.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 5,144 | 16.8 | 11.8 | 23.9 | 14.4 | 16.8 | 12.0 | 4.4 | 9.32 | 33.1% | 16.3% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 24,488 | 5144 | 9866 | 9478 | 25.5 | 159.1 | 1400.4 |
| ge_15pp | 10,080 | 1705 | 3461 | 4914 | 29.1 | 445.4 | 1380.4 |
| ge_25pp | 5,511 | 840 | 1573 | 3098 | 38.0 | 562.3 | 1380.4 |
| lt_10pp | 10,638 | 2700 | 4734 | 3204 | 24.0 | 51.3 | 1230.8 |

Current slate `SL-20261008T100900Z-d58f8be2`: 621 priced rows, quote age at build {'median': 7.6, 'max': 7.6}, freshness {'FRESH': 621}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 2 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.87 | 100.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 3 | 33.3 | 66.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.05 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 622 | 23.0 | 11.7 | 21.5 | 20.6 | 15.8 | 6.9 | 0.5 | 8.0 | 23.2% | 7.4% |
| MARKETS_AGREE | 47 | 78.7 | 21.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.03 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 79 | 0.0 | 2.5 | 29.1 | 32.9 | 24.1 | 11.4 | 0.0 | 11.66 | 35.4% | 11.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 12,812 | 753 (5.9%) | 10.5% | 0.3% | {"EXTERNAL_STALE": 622, "AGREES_WITH_KALSHI": 79, "ALL_AGREE": 47, "EXTERNAL_OUTLIER": 3, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_15pp | 5,576 | 174 (3.1%) | 16.1% | 1.1% | {"EXTERNAL_STALE": 144, "AGREES_WITH_KALSHI": 28, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp | 3,209 | 55 (1.7%) | 16.4% | 0.0% | {"EXTERNAL_STALE": 46, "AGREES_WITH_KALSHI": 9} |
| fair_v1_ge_25pp_pregame_clean | 1,438 | 54 (3.8%) | 16.7% | 0.0% | {"EXTERNAL_STALE": 45, "AGREES_WITH_KALSHI": 9} |
| fair_v1_lt_10pp | 5,169 | 425 (8.2%) | 5.9% | 0.0% | {"EXTERNAL_STALE": 350, "ALL_AGREE": 47, "AGREES_WITH_KALSHI": 25, "EXTERNAL_OUTLIER": 3} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,606 | 11.5 | 8.5 | 20.1 | 15.7 | 20.9 | 14.2 | 9.1 | 12.84 | 44.2% | 23.2% |
| 4-10x | 1,861 | 11.3 | 9.3 | 18.1 | 14.7 | 20.4 | 17.1 | 9.1 | 13.92 | 46.6% | 26.2% |
| <2x | 6,681 | 15.1 | 9.4 | 18.3 | 17.1 | 16.8 | 13.3 | 9.9 | 12.13 | 40.1% | 23.3% |
| >=10x | 1,664 | 10.4 | 6.3 | 16.0 | 14.7 | 19.1 | 20.9 | 12.7 | 16.18 | 52.6% | 33.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,284 | 14.1 | 8.8 | 20.0 | 15.9 | 17.6 | 12.9 | 10.7 | 12.07 | 41.2% | 23.6% |
| 300-1000 | 3,161 | 12.2 | 9.3 | 16.7 | 16.1 | 21.1 | 16.1 | 8.6 | 13.67 | 45.8% | 24.7% |
| <300 | 3,531 | 8.0 | 6.0 | 15.7 | 15.0 | 20.8 | 21.3 | 13.1 | 17.2 | 55.2% | 34.4% |
| >=3000 | 2,836 | 19.7 | 11.8 | 21.6 | 17.8 | 13.7 | 8.5 | 6.9 | 9.16 | 29.1% | 15.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 388 | 0.5418 | 0.4089 | 0.4742 | +0.068 | -0.065 | 0.0035 ± 0.0074 |
| ratio 4-10x | 279 | 0.5892 | 0.4466 | 0.5376 | +0.051 | -0.091 | -0.0069 ± 0.0093 |
| ratio <2x | 809 | 0.5446 | 0.4163 | 0.4586 | +0.086 | -0.042 | 0.0106 ± 0.0052 |
| ratio >=10x | 263 | 0.5626 | 0.3872 | 0.4639 | +0.099 | -0.077 | 0.0112 ± 0.0113 |
| thinner_sample 1000-3000 | 455 | 0.5478 | 0.4203 | 0.4615 | +0.086 | -0.041 | 0.0058 ± 0.0068 |
| thinner_sample 300-1000 | 481 | 0.5752 | 0.4338 | 0.5052 | +0.070 | -0.071 | -0.0013 ± 0.0071 |
| thinner_sample <300 | 551 | 0.5523 | 0.3894 | 0.4809 | +0.071 | -0.092 | 0.0068 ± 0.0074 |
| thinner_sample >=3000 | 252 | 0.5275 | 0.4262 | 0.4325 | +0.095 | -0.006 | 0.0206 ± 0.0076 |
| data_status ADEQUATE | 460 | 0.5301 | 0.4225 | 0.437 | +0.093 | -0.015 | 0.0131 ± 0.0059 |
| data_status LIMITED | 422 | 0.5695 | 0.4325 | 0.4976 | +0.072 | -0.065 | 0.0002 ± 0.0075 |
| data_status POOR | 857 | 0.559 | 0.4026 | 0.4854 | +0.073 | -0.083 | 0.0057 ± 0.0057 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 249 | 0.1803 | 0.1813 | -0.0011 ± 0.0009 | 0.5343 | 0.537 | 0.4935 | 0.4791 | 0.51 | -0.086 ± 0.0285 | -0.01 (3) |
| 3-5 | 173 | 0.1872 | 0.1881 | -0.0009 ± 0.0027 | 0.5541 | 0.5535 | 0.5072 | 0.4673 | 0.4913 | -0.079 ± 0.0337 | 0.02 (1) |
| 5-10 | 357 | 0.2 | 0.2021 | -0.0021 ± 0.0035 | 0.5863 | 0.592 | 0.5194 | 0.4455 | 0.4874 | -0.094 ± 0.0248 | -0.0125 (4) |
| 10-15 | 303 | 0.2196 | 0.2178 | +0.0019 ± 0.0067 | 0.6279 | 0.6197 | 0.5335 | 0.4093 | 0.462 | -0.092 ± 0.0268 | -0.0633 (3) |
| 15-25 | 383 | 0.2228 | 0.2118 | +0.0109 ± 0.0092 | 0.6374 | 0.6113 | 0.5764 | 0.3809 | 0.4491 | -0.089 ± 0.0236 | -0.0133 (6) |
| 25-40 | 223 | 0.2166 | 0.2047 | +0.0119 ± 0.018 | 0.6228 | 0.586 | 0.655 | 0.3449 | 0.4798 | -0.074 ± 0.0268 | -0.01 (1) |
| 40+ | 51 | 0.2726 | 0.1802 | +0.0924 ± 0.0517 | 0.742 | 0.5366 | 0.757 | 0.311 | 0.4314 | -0.112 ± 0.051 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1168 | 0.1663 | 0.1669 | -0.0006 ± 0.0004 | 0.4992 | 0.4997 | 0.4777 | 0.4629 | 0.4966 | -0.034 ± 0.0122 | -0.0188 (8) |
| 3-5 | 830 | 0.1924 | 0.1876 | +0.0048 ± 0.0012 | 0.5674 | 0.5505 | 0.4779 | 0.4384 | 0.394 | -0.108 ± 0.0152 | 0.02 (1) |
| 5-10 | 1774 | 0.1917 | 0.1905 | +0.0012 ± 0.0015 | 0.5663 | 0.5622 | 0.4894 | 0.4156 | 0.4408 | -0.050 ± 0.0105 | -0.0082 (17) |
| 10-15 | 1554 | 0.2044 | 0.1892 | +0.0152 ± 0.0028 | 0.5953 | 0.5526 | 0.4777 | 0.3529 | 0.3552 | -0.073 ± 0.011 | -0.0475 (4) |
| 15-25 | 1931 | 0.2001 | 0.1636 | +0.0365 ± 0.0036 | 0.59 | 0.488 | 0.4909 | 0.2949 | 0.2998 | -0.074 ± 0.0092 | -0.0048 (29) |
| 25-40 | 1684 | 0.2155 | 0.1266 | +0.0889 ± 0.0054 | 0.6229 | 0.3898 | 0.5297 | 0.2162 | 0.2334 | -0.056 ± 0.0083 | -0.01 (1) |
| 40+ | 1163 | 0.3656 | 0.0469 | +0.3187 ± 0.007 | 0.9539 | 0.1816 | 0.6209 | 0.1061 | 0.0645 | -0.077 ± 0.0059 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 194 | 0.1952 | 0.1954 | -0.0003 ± 0.0011 | 0.5738 | 0.5741 | 0.4941 | 0.4791 | 0.4742 | -0.119 ± 0.0333 | -0.01 (1) |
| 3-5 | 128 | 0.2106 | 0.2102 | +0.0004 ± 0.0033 | 0.6021 | 0.6039 | 0.5097 | 0.4698 | 0.4766 | -0.085 ± 0.0432 | 0.02 (1) |
| 5-10 | 300 | 0.1923 | 0.1902 | +0.0021 ± 0.0038 | 0.5676 | 0.5626 | 0.5632 | 0.4878 | 0.5067 | -0.098 ± 0.0261 | -0.01 (4) |
| 10-15 | 297 | 0.2197 | 0.2099 | +0.0098 ± 0.0067 | 0.6264 | 0.6071 | 0.5871 | 0.4625 | 0.4916 | -0.117 ± 0.0278 | -0.05 (4) |
| 15-25 | 422 | 0.2225 | 0.2059 | +0.0166 ± 0.0088 | 0.6325 | 0.5928 | 0.6018 | 0.4041 | 0.4668 | -0.103 ± 0.0228 | -0.01 (5) |
| 25-40 | 289 | 0.2673 | 0.2054 | +0.0619 ± 0.0167 | 0.7478 | 0.5927 | 0.6746 | 0.3616 | 0.4187 | -0.140 ± 0.0268 | -0.025 (2) |
| 40+ | 109 | 0.336 | 0.1942 | +0.1418 ± 0.0408 | 0.9506 | 0.5648 | 0.7668 | 0.2858 | 0.3945 | -0.058 ± 0.0387 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1093 | 0.1754 | 0.1762 | -0.0008 ± 0.0004 | 0.523 | 0.5251 | 0.4963 | 0.482 | 0.5078 | -0.038 ± 0.0133 | -0.0217 (6) |
| 3-5 | 684 | 0.1925 | 0.1883 | +0.0042 ± 0.0013 | 0.5569 | 0.548 | 0.5211 | 0.4813 | 0.4488 | -0.086 ± 0.0168 | 0.02 (1) |
| 5-10 | 1528 | 0.1833 | 0.1805 | +0.0028 ± 0.0016 | 0.5494 | 0.5378 | 0.513 | 0.4391 | 0.4548 | -0.053 ± 0.0111 | -0.01 (5) |
| 10-15 | 1378 | 0.1964 | 0.1831 | +0.0133 ± 0.0029 | 0.5808 | 0.5363 | 0.5232 | 0.3991 | 0.4107 | -0.069 ± 0.0118 | -0.02 (14) |
| 15-25 | 2028 | 0.2121 | 0.1712 | +0.0409 ± 0.0036 | 0.6193 | 0.5075 | 0.5295 | 0.3342 | 0.3304 | -0.087 ± 0.0093 | -0.0026 (27) |
| 25-40 | 1886 | 0.2469 | 0.139 | +0.1079 ± 0.0055 | 0.6993 | 0.4229 | 0.5628 | 0.2461 | 0.2349 | -0.088 ± 0.0086 | -0.015 (6) |
| 40+ | 1507 | 0.3986 | 0.0719 | +0.3267 ± 0.0079 | 1.0443 | 0.2477 | 0.6699 | 0.132 | 0.1115 | -0.062 ± 0.0066 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 259 | 0.1892 | 0.1915 | -0.0023 ± 0.001 | 0.5556 | 0.5621 | 0.5042 | 0.4891 | 0.5444 | -0.041 ± 0.0275 | -0.0133 (6) |
| 3-5 | 190 | 0.1845 | 0.1829 | +0.0016 ± 0.0025 | 0.5444 | 0.5404 | 0.4915 | 0.4522 | 0.4526 | -0.128 ± 0.0331 | -0.01 (1) |
| 5-10 | 363 | 0.1967 | 0.1987 | -0.0019 ± 0.0035 | 0.5791 | 0.5825 | 0.5147 | 0.441 | 0.4848 | -0.083 ± 0.0242 | -0.01 (4) |
| 10-15 | 284 | 0.2165 | 0.2161 | +0.0004 ± 0.0069 | 0.6238 | 0.6176 | 0.5437 | 0.4204 | 0.4824 | -0.091 ± 0.0271 | -0.044 (5) |
| 15-25 | 376 | 0.225 | 0.2106 | +0.0144 ± 0.0092 | 0.6467 | 0.6064 | 0.5845 | 0.3908 | 0.4495 | -0.099 ± 0.0235 | -0.03 (1) |
| 25-40 | 222 | 0.2022 | 0.2104 | -0.0082 ± 0.0178 | 0.5885 | 0.6013 | 0.6599 | 0.3484 | 0.5135 | -0.054 ± 0.0261 | 0.0 (1) |
| 40+ | 45 | 0.2966 | 0.1799 | +0.1167 ± 0.0563 | 0.7985 | 0.5355 | 0.7496 | 0.2982 | 0.4 | -0.122 ± 0.0568 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1156 | 0.1773 | 0.1785 | -0.0012 ± 0.0004 | 0.5262 | 0.5291 | 0.4901 | 0.4749 | 0.513 | -0.026 ± 0.0125 | -0.0183 (23) |
| 3-5 | 863 | 0.1867 | 0.1839 | +0.0028 ± 0.0012 | 0.5499 | 0.544 | 0.472 | 0.4326 | 0.4171 | -0.087 ± 0.0152 | -0.0243 (7) |
| 5-10 | 1818 | 0.1831 | 0.1808 | +0.0023 ± 0.0015 | 0.5474 | 0.5373 | 0.482 | 0.4082 | 0.4268 | -0.053 ± 0.01 | -0.01 (18) |
| 10-15 | 1452 | 0.1991 | 0.1828 | +0.0164 ± 0.0028 | 0.5835 | 0.5349 | 0.4913 | 0.3679 | 0.3629 | -0.083 ± 0.0111 | -0.03 (9) |
| 15-25 | 2098 | 0.2057 | 0.1695 | +0.0362 ± 0.0035 | 0.6044 | 0.5031 | 0.4956 | 0.2993 | 0.307 | -0.067 ± 0.009 | -0.03 (2) |
| 25-40 | 1620 | 0.2133 | 0.1224 | +0.0909 ± 0.0055 | 0.6176 | 0.3778 | 0.5243 | 0.2068 | 0.2259 | -0.058 ± 0.0082 | 0.0 (1) |
| 40+ | 1097 | 0.3791 | 0.0479 | +0.3313 ± 0.0075 | 0.9921 | 0.185 | 0.6275 | 0.106 | 0.0611 | -0.080 ± 0.0062 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 539 | 0.2019 | 0.202 | -0.0000 ± 0.0007 | 0.5874 | 0.587 | 0.4999 | 0.4851 | 0.4879 | -0.047 ± 0.0193 | -0.0226 (46) |
| 3-5 | 405 | 0.1964 | 0.1955 | +0.0009 ± 0.0018 | 0.5745 | 0.5708 | 0.4816 | 0.442 | 0.4543 | -0.045 ± 0.0219 | -0.0058 (33) |
| 5-10 | 832 | 0.1917 | 0.1864 | +0.0053 ± 0.0023 | 0.5674 | 0.5539 | 0.4715 | 0.398 | 0.4002 | -0.059 ± 0.0153 | -0.0049 (73) |
| 10-15 | 547 | 0.2026 | 0.1919 | +0.0107 ± 0.0047 | 0.5941 | 0.5646 | 0.478 | 0.355 | 0.3729 | -0.047 ± 0.0187 | 0.0014 (64) |
| 15-25 | 752 | 0.2341 | 0.2099 | +0.0242 ± 0.0066 | 0.663 | 0.6055 | 0.5451 | 0.3507 | 0.387 | -0.054 ± 0.0168 | -0.0216 (58) |
| 25-40 | 419 | 0.2427 | 0.1832 | +0.0595 ± 0.013 | 0.6823 | 0.5394 | 0.6194 | 0.3059 | 0.3652 | -0.071 ± 0.0195 | -0.0216 (25) |
| 40+ | 143 | 0.3365 | 0.1855 | +0.1510 ± 0.0365 | 0.9568 | 0.5485 | 0.773 | 0.2806 | 0.3986 | -0.040 ± 0.032 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1509 | 0.1881 | 0.188 | +0.0001 ± 0.0004 | 0.5535 | 0.5521 | 0.4977 | 0.4824 | 0.4844 | -0.044 ± 0.0111 | -0.0155 (82) |
| 3-5 | 1079 | 0.1866 | 0.1844 | +0.0022 ± 0.0011 | 0.5483 | 0.5432 | 0.4897 | 0.4501 | 0.4467 | -0.053 ± 0.0131 | -0.0148 (63) |
| 5-10 | 2238 | 0.1884 | 0.181 | +0.0074 ± 0.0014 | 0.5598 | 0.5392 | 0.4722 | 0.3983 | 0.3892 | -0.064 ± 0.0091 | -0.0087 (125) |
| 10-15 | 1540 | 0.1979 | 0.1835 | +0.0144 ± 0.0027 | 0.5827 | 0.5441 | 0.4881 | 0.3651 | 0.3675 | -0.059 ± 0.0108 | -0.0053 (105) |
| 15-25 | 2053 | 0.2274 | 0.1982 | +0.0292 ± 0.0039 | 0.6538 | 0.5765 | 0.5383 | 0.3431 | 0.3663 | -0.055 ± 0.01 | -0.0255 (106) |
| 25-40 | 1432 | 0.2358 | 0.1578 | +0.0780 ± 0.0066 | 0.668 | 0.4721 | 0.5814 | 0.2662 | 0.3017 | -0.058 ± 0.0102 | -0.0206 (47) |
| 40+ | 698 | 0.3527 | 0.1071 | +0.2456 ± 0.0132 | 0.965 | 0.3379 | 0.6747 | 0.1695 | 0.192 | -0.054 ± 0.0114 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1739 | 1.115 ± 0.069 | 1.211 | 0.1699 | 0.1655 | 0.2086 | 0.2023 |
| gen2 | 1739 | 0.893 ± 0.061 | 1.135 | 0.1867 | 0.165 | 0.2275 | 0.2022 |
| gen1_elo | 1739 | 1.103 ± 0.068 | 1.201 | 0.1736 | 0.166 | 0.2069 | 0.2023 |
| gen1_sr | 1739 | 1.109 ± 0.078 | 1.215 | 0.1434 | 0.1674 | 0.2228 | 0.2021 |
| gen1_ledger | 3637 | 0.938 ± 0.044 | 1.088 | 0.1699 | 0.1912 | 0.2157 | 0.195 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 10,080)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,735 | 27.1% |
| STALE_QUOTE | market_freshness | 2,195 | 21.8% |
| BOOK_QUALITY | execution | 1,789 | 17.8% |
| POOR_DATA | data | 1,094 | 10.8% |
| LIMITED_DATA | data | 731 | 7.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 507 | 5.0% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 460 | 4.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 275 | 2.7% |
| IDENTITY_AMBIGUOUS | mapping | 267 | 2.6% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 27 | 0.3% |

Cause class: coverage 27.1%, market_freshness 21.8%, data 18.1%, execution 17.8%, market_freshness/coverage 7.8%, model_calibration_or_unknown 4.6%, mapping 2.6%, model_calibration 0.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.6%, START_UNVERIFIABLE 96.1%, LOW_DATA_QUALITY 69.2%, STALE_PLAYER_DATA 58.4%, THIN_PLAYER_HISTORY 58.1%, STALE_KALSHI_QUOTE 48.8%, MODEL_INTERNAL_DISAGREEMENT 37.4%, ASYMMETRIC_SAMPLE_SIZE 31.4%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 16.0%, PLAYER_IDENTITY_RISK 10.9%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 7.5%, LOW_DISPLAYED_LIQUIDITY 7.3%, MODEL_CALIBRATION_OUTLIER 3.0%, UNKNOWN 0.5%, EXTERNAL_MARKET_REJECTION 0.4%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.4%, POST_SETTLEMENT_OBSERVATION 27.1%, POSSIBLE_IN_PLAY_QUOTE 5.4%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,511)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,160 | 39.2% |
| STALE_QUOTE | market_freshness | 979 | 17.8% |
| BOOK_QUALITY | execution | 939 | 17.0% |
| POOR_DATA | data | 461 | 8.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 280 | 5.1% |
| LIMITED_DATA | data | 238 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 174 | 3.2% |
| IDENTITY_AMBIGUOUS | mapping | 157 | 2.9% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 113 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 10 | 0.2% |

Cause class: coverage 39.2%, market_freshness 17.8%, execution 17.0%, data 12.7%, market_freshness/coverage 8.2%, mapping 2.9%, model_calibration_or_unknown 2.1%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.8%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.8%, THIN_PLAYER_HISTORY 59.9%, STALE_KALSHI_QUOTE 56.2%, STALE_PLAYER_DATA 53.6%, MODEL_INTERNAL_DISAGREEMENT 39.1%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 17.2%, PLAYER_IDENTITY_RISK 13.7%, EVENT_MAPPING_RISK 8.8%, LOW_DISPLAYED_LIQUIDITY 7.7%, LEVEL_TRANSFER_RISK 7.6%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 0.2%, UNKNOWN 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 41.8%, POST_SETTLEMENT_OBSERVATION 39.2%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4599, "IDENTITY_AMBIGUOUS": 912}; ticker orientation: {"VERIFIED": 5511}.

Checks: discipline:AMBIGUOUS 321, discipline:PASS 5190, identity_confidence:AMBIGUOUS 752, identity_confidence:PASS 4759, level_mapping:NA 333, level_mapping:PASS 5178, market_pair:AMBIGUOUS 207, market_pair:NA 127, market_pair:PASS 5177, model_complement:NA 94, model_complement:PASS 5417, namesake:PASS 5511, physical_match_id:NA 2302, physical_match_id:PASS 3209, player_ids:PASS 5511, same_pair_other_event:PASS 5511, ticker_orientation:PASS 5511

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,372 | 1.8% | 1.8% | 0.4% | {"market_freshness": 20, "execution": 5} | 5.58 | 0.213 / 0.2053 (117) | 20.8% | 0.1% | 6.1% | 1.4% |
| CHALLENGER | 3,637 | 18.9% | 6.4% | 12.5% | {"coverage": 429, "market_freshness": 107, "market_freshness/coverage": 81, "model_calibration_or_unknown": 39, "data": 25, "execution": 4, "model_calibration": 3} | 6.81 | 0.2231 / 0.2042 (848) | 46.7% | 4.9% | 1.6% | 23.6% |
| DOUBLES | 670 | 47.9% | 47.6% | 5.8% | {"execution": 116, "market_freshness": 106, "mapping": 71, "market_freshness/coverage": 21, "coverage": 7} | 23.82 | 0.3089 / 0.2242 (195) | 34.9% | 0.0% | 100.0% | 8.1% |
| ITF_MEN | 7,406 | 24.1% | 16.4% | 32.4% | {"coverage": 713, "execution": 380, "data": 266, "market_freshness": 266, "market_freshness/coverage": 139, "mapping": 19, "model_calibration_or_unknown": 4} | 10.64 | 0.2123 / 0.1932 (1783) | 38.8% | 55.3% | 6.3% | 22.9% |
| ITF_WOMEN | 9,477 | 26.2% | 18.0% | 45.0% | {"coverage": 994, "market_freshness": 423, "execution": 417, "data": 384, "market_freshness/coverage": 172, "mapping": 61, "model_calibration_or_unknown": 24, "model_calibration": 6} | 12.11 | 0.2014 / 0.1938 (1969) | 40.0% | 58.8% | 10.1% | 23.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 977 | 8.1% | 7.0% | 1.4% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.24 | 0.2008 / 0.1978 (145) | 34.1% | 2.1% | 1.2% | 3.4% |
| WTA125 | 800 | 14.8% | 10.6% | 2.1% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 21, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 1} | 9.93 | 0.2265 / 0.2129 (277) | 26.8% | 6.1% | 4.2% | 11.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 9 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 10 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 11 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 12 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 13 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 15 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 16 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 18 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 19 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 20 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 21 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 22 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 23 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 24 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 25 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 26 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 27 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 28 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 29 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 30 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 22% | +74 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 32 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 33 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 36 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
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

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9811, "by_level_share_of_ge_25pp": {"ATP": 0.0045, "CHALLENGER": 0.1248, "DOUBLES": 0.0582, "ITF_MEN": 0.3243, "ITF_WOMEN": 0.4502, "OTHER": 0.0022, "WTA": 0.0143, "WTA125": 0.0214}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5621, "share_primary_cause_market_settled_or_in_play": 0.4743, "share_primary_cause_stale_quote_only": 0.1776}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5511, "identity_ambiguous_share": 0.1655, "ticker_orientation": {"VERIFIED": 5511}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3209, "with_external": 55, "coverage": 0.0171, "external_status": {"EXTERNAL_STALE": 46, "AGREES_WITH_KALSHI": 9}, "triangulation": {"INSUFFICIENT_INPUTS": 46, "MODEL_LONE_OUTLIER": 9}, "share_external_agrees_with_kalshi": 0.1636, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1438, "with_external": 54, "coverage": 0.0376, "external_status": {"EXTERNAL_STALE": 45, "AGREES_WITH_KALSHI": 9}, "triangulation": {"INSUFFICIENT_INPUTS": 45, "MODEL_LONE_OUTLIER": 9}, "share_external_agrees_with_kalshi": 0.1667, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 605.0, "median_sample_ratio": 2.35, "median_min_matches": 20.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.1795, "data_status": {"POOR": 2899, "LIMITED": 1629, "ADEQUATE": 983}, "comparison_lt_10pp": {"median_thinner_serve_points": 1716.0, "median_sample_ratio": 1.77, "median_min_matches": 72.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 388, "model_minus_observed": 0.0675, "kalshi_minus_observed": -0.0654, "brier_diff_model_minus_kalshi": 0.0035}, "4-10x": {"n": 279, "model_minus_observed": 0.0515, "kalshi_minus_observed": -0.0911, "brier_diff_model_minus_kalshi": -0.0069}, "<2x": {"n": 809, "model_minus_observed": 0.0861, "kalshi_minus_observed": -0.0423, "brier_diff_model_minus_kalshi": 0.0106}, ">=10x": {"n": 263, "model_minus_observed": 0.0987, "kalshi_minus_observed": -0.0767, "brier_diff_model_minus_kalshi": 0.0112}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1739, "model": {"intercept": -0.579, "slope": 0.893, "slope_se": 0.061}, "kalshi_mid_same_rows": {"intercept": 0.228, "slope": 1.135, "slope_se": 0.07}, "mean_extremity_model": 0.1867, "mean_extremity_kalshi": 0.165, "model_brier": 0.2275, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0252, "brier_diff_se": 0.0046, "model_logloss": 0.6506, "kalshi_logloss": 0.587}, "fair_v1": {"n": 1739, "model": {"intercept": -0.407, "slope": 1.115, "slope_se": 0.069}, "kalshi_mid_same_rows": {"intercept": 0.361, "slope": 1.211, "slope_se": 0.073}, "mean_extremity_model": 0.1699, "mean_extremity_kalshi": 0.1655, "model_brier": 0.2086, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.0063, "brier_diff_se": 0.0037, "model_logloss": 0.6034, "kalshi_logloss": 0.587}, "gen1_elo": {"n": 1739, "model": {"intercept": -0.369, "slope": 1.103, "slope_se": 0.068}, "kalshi_mid_same_rows": {"intercept": 0.376, "slope": 1.201, "slope_se": 0.071}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.166, "model_brier": 0.2069, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.0046, "brier_diff_se": 0.0036, "model_logloss": 0.6006, "kalshi_logloss": 0.587}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2505, "share_ge_15": 0.4352, "median_abs_gap": 12.98, "n": 12812}, "gen1_elo": {"share_ge_25": 0.2413, "share_ge_15": 0.434, "median_abs_gap": 12.53, "n": 12812}, "gen1_sr": {"share_ge_25": 0.303, "share_ge_15": 0.5176, "median_abs_gap": 15.59, "n": 12812}, "gen2": {"share_ge_25": 0.3067, "share_ge_15": 0.5048, "median_abs_gap": 15.26, "n": 12812}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.147, "share_ge_15": 0.3372, "median_abs_gap": 10.45, "n": 9782}, "gen1_elo": {"share_ge_25": 0.1422, "share_ge_15": 0.3334, "median_abs_gap": 10.01, "n": 9781}, "gen1_sr": {"share_ge_25": 0.2013, "share_ge_15": 0.4297, "median_abs_gap": 12.77, "n": 9782}, "gen2": {"share_ge_25": 0.2187, "share_ge_15": 0.4279, "median_abs_gap": 12.66, "n": 9783}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.58, "share_ge_25_all": 0.0182, "share_ge_25_pregame_clean": 0.0185}, "WTA": {"median_abs_gap_pregame_clean": 8.24, "share_ge_25_all": 0.0809, "share_ge_25_pregame_clean": 0.0699}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2355, "share_within_10pp_all": 0.4344, "share_within_10pp_pregame_clean": 0.4973, "corr_model_vs_mid_pregame_clean": 0.8517}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 249, "model_brier": 0.1803, "kalshi_brier": 0.1813, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 303, "model_brier": 0.2196, "kalshi_brier": 0.2178, "brier_diff_model_minus_kalshi": 0.0019}, "15-25": {"n_settled": 383, "model_brier": 0.2228, "kalshi_brier": 0.2118, "brier_diff_model_minus_kalshi": 0.0109}, "25-40": {"n_settled": 223, "model_brier": 0.2166, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0119}, "3-5": {"n_settled": 173, "model_brier": 0.1872, "kalshi_brier": 0.1881, "brier_diff_model_minus_kalshi": -0.0009}, "40+": {"n_settled": 51, "model_brier": 0.2726, "kalshi_brier": 0.1802, "brier_diff_model_minus_kalshi": 0.0924}, "5-10": {"n_settled": 357, "model_brier": 0.2, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": -0.0021}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 195, "model_brier": 0.3089, "kalshi_brier": 0.2242, "brier_diff_model_minus_kalshi": 0.0847, "brier_diff_se": 0.0226, "corr_model_outcome": 0.0227, "corr_kalshi_outcome": 0.3519}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
