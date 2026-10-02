# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-02T06:12Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 10,381): 0-3 13.6%, 3-5 9.0%, 5-10 19.6%, 10-15 14.8%, 15-25 19.6%, 25-40 14.3%, 40+ 9.2%; median gap 12.44 pp.
* **Where the extremes live**: 96.6% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.0%, Challenger 11.8%, doubles 7.4%). Main tour: ATP 4.0% and WTA 9.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,443): MARKET_ALREADY_SETTLED_WHEN_PRICED 45.6%, STALE_QUOTE 23.6%, POOR_DATA 6.6%, BOOK_QUALITY 5.9%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IN_PLAY_QUOTE 5.2%, LIMITED_DATA 3.1%, IDENTITY_AMBIGUOUS 2.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%. By class: coverage 45.6%, market_freshness 23.6%, market_freshness/coverage 10.7%, data 9.7%, execution 5.9%, mapping 2.4%, model_calibration_or_unknown 2.2%.
* **Stale / settled / in-play**: 69.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 56.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,443 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 15.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 6.0% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 776.0 points vs 1970.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.184, Gen-2 0.982, Gen-1 ledger 0.906 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 80 model 0.2384 vs Kalshi 0.1762; n 21 model 0.2865 vs Kalshi 0.1302.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 32,800 model-market comparisons (56,414 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 16,212 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-02T06:09:09.086637+00:00'], shadow board 8,960 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-02T06:09:12.133291+00:00'], Model 4 2,756 rows, 7,992 settled tickers, 1,781 tickers with an external scan.
* By model: {"gen1_ledger": 9463, "gen1_elo": 4507, "fair_v1": 4507, "gen2": 4507, "gen1_sr": 4507, "model4_fundamental": 2659, "model4_conditioned": 2650}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 10,381 | 13.6 | 9.0 | 19.6 | 14.8 | 19.6 | 14.3 | 9.2 | 12.44 | 43.1% | 23.5% |
| MW fair_v1 | 4,507 | 13.9 | 8.4 | 18.9 | 14.9 | 18.6 | 14.9 | 10.4 | 12.81 | 43.9% | 25.3% |
| MW gen1_elo | 4,507 | 13.3 | 8.7 | 20.1 | 15.2 | 18.1 | 14.8 | 9.8 | 12.42 | 42.7% | 24.6% |
| MW gen1_ledger | 5,874 | 13.3 | 9.4 | 20.1 | 14.7 | 20.4 | 13.8 | 8.3 | 12.21 | 42.5% | 22.1% |
| MW gen1_sr | 4,507 | 9.9 | 7.1 | 17.0 | 13.2 | 22.2 | 18.4 | 12.2 | 16.1 | 52.8% | 30.6% |
| MW gen2 | 4,507 | 11.4 | 6.4 | 16.6 | 15.3 | 19.6 | 17.0 | 13.5 | 15.06 | 50.1% | 30.5% |
| all families model4_conditioned | 2,650 | 18.6 | 15.3 | 29.2 | 24.3 | 8.6 | 2.1 | 2.0 | 7.4 | 12.7% | 4.1% |
| all families model4_fundamental | 2,659 | 13.9 | 10.6 | 30.5 | 22.4 | 14.3 | 5.2 | 2.9 | 9.12 | 22.5% | 8.2% |

Configurable thresholds (primary): >=5pp 77.5%, >=10pp 57.9%, >=15pp 43.1%, >=20pp 32.4%, >=25pp 23.5%, >=30pp 17.3%, >=40pp 9.2%, >=50pp 4.2%
Executable gap (model outside the book, before fees): median 10.01pp; >=10pp 50.1%, >=25pp 20.8%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 228 | 22.8 | 18.0 | 25.9 | 13.6 | 14.5 | 1.3 | 4.0 | 6.03 | 19.7% | 5.3% |
| CHALLENGER | 781 | 15.4 | 8.7 | 16.3 | 15.9 | 15.9 | 14.8 | 13.1 | 13.16 | 43.8% | 27.9% |
| ITF_MEN | 1,434 | 11.8 | 8.5 | 20.1 | 14.6 | 18.3 | 14.7 | 11.9 | 12.78 | 45.0% | 26.6% |
| ITF_WOMEN | 1,561 | 11.2 | 6.5 | 16.1 | 14.8 | 20.8 | 19.3 | 11.3 | 15.62 | 51.4% | 30.6% |
| WTA | 419 | 23.4 | 10.5 | 26.2 | 13.1 | 17.9 | 6.9 | 1.9 | 7.97 | 26.7% | 8.8% |
| WTA125 | 84 | 14.3 | 4.8 | 17.9 | 23.8 | 20.2 | 14.3 | 4.8 | 12.4 | 39.3% | 19.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 228 | 22.8 | 13.2 | 25.9 | 15.3 | 16.7 | 1.8 | 4.4 | 7.06 | 22.8% | 6.1% |
| CHALLENGER | 781 | 10.8 | 5.6 | 17.7 | 17.4 | 18.4 | 17.5 | 12.6 | 14.84 | 48.5% | 30.1% |
| ITF_MEN | 1,434 | 10.1 | 5.9 | 17.1 | 16.5 | 19.9 | 16.3 | 14.2 | 15.29 | 50.4% | 30.5% |
| ITF_WOMEN | 1,561 | 9.0 | 6.7 | 14.2 | 12.9 | 19.4 | 20.0 | 17.9 | 18.11 | 57.2% | 37.9% |
| WTA | 419 | 21.2 | 5.2 | 17.4 | 15.8 | 22.7 | 15.8 | 1.9 | 12.72 | 40.3% | 17.7% |
| WTA125 | 84 | 6.0 | 6.0 | 16.7 | 20.2 | 22.6 | 15.5 | 13.1 | 15.56 | 51.2% | 28.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 228 | 28.1 | 12.7 | 29.4 | 11.4 | 8.8 | 5.7 | 4.0 | 6.59 | 18.4% | 9.7% |
| CHALLENGER | 781 | 15.1 | 7.7 | 20.9 | 14.6 | 14.1 | 14.3 | 13.3 | 11.99 | 41.7% | 27.7% |
| ITF_MEN | 1,434 | 10.5 | 9.6 | 18.6 | 16.2 | 18.1 | 15.8 | 11.2 | 12.92 | 45.1% | 27.0% |
| ITF_WOMEN | 1,561 | 9.8 | 6.5 | 17.0 | 14.3 | 23.5 | 18.5 | 10.4 | 16.46 | 52.4% | 28.9% |
| WTA | 419 | 23.9 | 13.4 | 30.1 | 15.3 | 11.9 | 3.8 | 1.7 | 6.99 | 17.4% | 5.5% |
| WTA125 | 84 | 16.7 | 6.0 | 22.6 | 29.8 | 13.1 | 10.7 | 1.2 | 10.92 | 25.0% | 11.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 787 | 21.2 | 13.7 | 26.7 | 15.9 | 13.5 | 6.5 | 2.5 | 7.45 | 22.5% | 9.0% |
| DOUBLES | 369 | 5.4 | 3.8 | 9.8 | 10.3 | 21.7 | 20.9 | 28.2 | 24.32 | 70.7% | 49.0% |
| ITF_MEN | 1,979 | 14.3 | 9.0 | 18.9 | 13.6 | 21.2 | 13.6 | 9.4 | 12.51 | 44.2% | 23.0% |
| ITF_WOMEN | 1,818 | 9.1 | 8.3 | 17.6 | 14.5 | 23.4 | 18.4 | 8.8 | 15.21 | 50.6% | 27.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 337 | 13.3 | 9.5 | 21.7 | 16.9 | 22.9 | 11.9 | 3.9 | 11.35 | 38.6% | 15.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 227 | 22.5 | 18.1 | 26.0 | 13.7 | 14.5 | 1.3 | 4.0 | 6.04 | 19.8% | 5.3% |
| CHALLENGER | 576 | 19.3 | 10.8 | 19.8 | 19.1 | 16.8 | 9.0 | 5.2 | 10.14 | 31.1% | 14.2% |
| ITF_MEN | 935 | 15.7 | 11.7 | 24.7 | 15.6 | 18.1 | 10.1 | 4.2 | 9.61 | 32.3% | 14.2% |
| ITF_WOMEN | 1,055 | 15.0 | 8.5 | 19.5 | 17.6 | 22.3 | 13.2 | 3.9 | 12.37 | 39.3% | 17.1% |
| WTA | 418 | 23.4 | 10.5 | 26.3 | 13.2 | 17.9 | 6.7 | 1.9 | 7.96 | 26.6% | 8.6% |
| WTA125 | 83 | 14.5 | 4.8 | 18.1 | 24.1 | 20.5 | 13.2 | 4.8 | 12.01 | 38.6% | 18.1% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 227 | 22.9 | 12.8 | 26.0 | 15.4 | 16.7 | 1.8 | 4.4 | 7.08 | 22.9% | 6.2% |
| CHALLENGER | 576 | 13.2 | 7.1 | 22.2 | 21.2 | 19.8 | 12.3 | 4.2 | 11.79 | 36.3% | 16.5% |
| ITF_MEN | 935 | 13.2 | 7.4 | 20.4 | 19.0 | 20.8 | 13.4 | 5.9 | 12.2 | 40.0% | 19.2% |
| ITF_WOMEN | 1,055 | 10.8 | 8.6 | 16.3 | 13.0 | 22.6 | 17.6 | 11.1 | 15.52 | 51.3% | 28.7% |
| WTA | 418 | 21.3 | 5.3 | 17.5 | 15.8 | 22.7 | 15.6 | 1.9 | 12.6 | 40.2% | 17.5% |
| WTA125 | 83 | 6.0 | 6.0 | 16.9 | 20.5 | 22.9 | 15.7 | 12.1 | 15.33 | 50.6% | 27.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 60 | 25.0 | 25.0 | 35.0 | 13.3 | 1.7 | 0.0 | 0.0 | 5.38 | 1.7% | 0.0% |
| CHALLENGER | 647 | 23.6 | 15.9 | 29.7 | 15.5 | 12.7 | 2.5 | 0.1 | 6.68 | 15.3% | 2.6% |
| DOUBLES | 287 | 5.9 | 3.5 | 9.8 | 10.4 | 21.9 | 21.6 | 26.8 | 24.11 | 70.4% | 48.4% |
| ITF_MEN | 1,417 | 17.5 | 10.9 | 22.2 | 14.6 | 21.0 | 10.3 | 3.6 | 9.9 | 34.9% | 13.9% |
| ITF_WOMEN | 1,239 | 11.1 | 9.7 | 21.2 | 16.6 | 24.5 | 14.8 | 2.1 | 12.14 | 41.4% | 17.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 255 | 15.3 | 9.0 | 25.5 | 23.5 | 19.6 | 7.1 | 0.0 | 10.01 | 26.7% | 7.1% |
| WTA125 | 258 | 15.9 | 10.5 | 26.0 | 19.4 | 20.5 | 7.4 | 0.4 | 9.43 | 28.3% | 7.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 369 | 5.4 | 3.8 | 9.8 | 10.3 | 21.7 | 20.9 | 28.2 | 24.32 | 70.7% | 49.0% |
| singles | 5,505 | 13.8 | 9.8 | 20.8 | 15.0 | 20.3 | 13.3 | 7.0 | 11.74 | 40.6% | 20.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 972 | 15.9 | 8.0 | 19.0 | 14.3 | 16.5 | 13.9 | 12.3 | 12.18 | 42.7% | 26.2% |
| Hard | 3,238 | 13.2 | 8.9 | 19.1 | 14.6 | 19.1 | 15.2 | 9.9 | 12.92 | 44.2% | 25.1% |
| UNKNOWN | 297 | 14.1 | 5.4 | 16.2 | 19.9 | 19.5 | 15.5 | 9.4 | 13.49 | 44.4% | 24.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,386 | 18.4 | 10.0 | 21.3 | 15.1 | 17.0 | 10.8 | 7.4 | 10.07 | 35.2% | 18.2% |
| B | 622 | 17.0 | 10.8 | 18.3 | 17.5 | 14.6 | 10.4 | 11.2 | 11.17 | 36.3% | 21.7% |
| C | 758 | 12.3 | 8.3 | 23.0 | 13.6 | 16.6 | 15.2 | 11.1 | 12.71 | 42.9% | 26.2% |
| D | 829 | 12.2 | 8.4 | 17.2 | 14.1 | 20.9 | 15.2 | 11.9 | 14.17 | 48.0% | 27.1% |
| F | 912 | 7.8 | 4.6 | 13.7 | 14.5 | 23.2 | 23.7 | 12.5 | 19.02 | 59.4% | 36.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,796 | 18.9 | 12.0 | 26.3 | 16.8 | 16.4 | 7.0 | 2.7 | 8.59 | 26.1% | 9.6% |
| B | 972 | 14.0 | 9.3 | 21.7 | 16.5 | 19.0 | 12.1 | 7.4 | 11.54 | 38.6% | 19.6% |
| C | 1,211 | 11.3 | 8.3 | 15.5 | 13.9 | 22.2 | 15.4 | 13.4 | 15.42 | 50.9% | 28.7% |
| D | 907 | 11.4 | 8.3 | 20.5 | 12.0 | 23.8 | 15.6 | 8.5 | 14.12 | 47.9% | 24.0% |
| F | 988 | 6.8 | 7.2 | 12.4 | 12.6 | 23.4 | 24.4 | 13.3 | 19.38 | 61.0% | 37.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,709 | 17.1 | 9.5 | 20.5 | 16.2 | 16.4 | 11.1 | 9.1 | 10.65 | 36.6% | 20.2% |
| LIMITED | 1,039 | 15.1 | 10.3 | 22.2 | 13.6 | 15.7 | 13.4 | 9.7 | 11.07 | 38.8% | 23.1% |
| POOR | 1,759 | 10.0 | 6.4 | 15.3 | 14.3 | 22.3 | 19.6 | 12.1 | 16.92 | 54.0% | 31.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 333 | 34.5 | 22.8 | 33.3 | 6.0 | 2.4 | 0.9 | 0.0 | 4.16 | 3.3% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 5,874 | 13.3 | 9.4 | 20.1 | 14.7 | 20.4 | 13.8 | 8.3 | 12.21 | 42.5% | 22.1% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,694 | 21.8 | 13.5 | 30.3 | 17.3 | 13.7 | 2.8 | 0.7 | 7.06 | 17.1% | 3.4% |
| TOTAL_GAMES | 1,132 | 9.9 | 9.4 | 26.5 | 24.9 | 17.0 | 8.0 | 4.4 | 10.66 | 29.3% | 12.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 836 | 28.8 | 32.2 | 26.8 | 0.7 | 9.2 | 1.8 | 0.5 | 4.29 | 11.5% | 2.3% |
| GAME_SPREAD | 526 | 36.9 | 14.4 | 24.9 | 18.8 | 2.7 | 1.5 | 0.8 | 4.6 | 4.9% | 2.3% |
| TOTAL_GAMES | 1,288 | 4.4 | 4.7 | 32.5 | 41.8 | 10.6 | 2.6 | 3.4 | 10.75 | 16.6% | 6.1% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 836 | 25.0 | 17.2 | 33.7 | 8.6 | 9.8 | 4.5 | 1.1 | 5.88 | 15.4% | 5.6% |
| GAME_SPREAD | 526 | 16.5 | 10.3 | 26.2 | 23.8 | 16.2 | 4.9 | 2.1 | 9.62 | 23.2% | 7.0% |
| TOTAL_GAMES | 1,297 | 5.8 | 6.5 | 30.2 | 30.7 | 16.5 | 5.8 | 4.5 | 10.84 | 26.8% | 10.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4,507 | 43.9% | 25.3% | 12.81 | 32.9% | 13.9% | 9.95 |
| gen1_elo | 4,507 | 42.7% | 24.6% | 12.42 | 31.2% | 13.8% | 9.51 |
| gen1_sr | 4,507 | 52.8% | 30.6% | 16.1 | 43.5% | 19.6% | 12.7 |
| gen2 | 4,507 | 50.1% | 30.5% | 15.06 | 42.1% | 20.9% | 12.75 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,721 | 18.0 | 12.1 | 23.2 | 15.4 | 18.2 | 9.9 | 3.1 | 9.14 | 31.3% | 13.0% |
| STALE | 2,786 | 11.3 | 6.2 | 16.2 | 14.5 | 18.8 | 18.0 | 14.9 | 16.0 | 51.7% | 33.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,182 | 15.3 | 10.3 | 21.9 | 15.9 | 19.8 | 12.2 | 4.6 | 10.71 | 36.6% | 16.8% |
| STALE | 2,692 | 11.0 | 8.4 | 18.0 | 13.2 | 21.0 | 15.8 | 12.7 | 14.77 | 49.5% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 10,381 | 0 | 4903 | 5478 | 31.0 | 190.7 | 1400.4 |
| ge_15pp | 4,476 | 0 | 1703 | 2773 | 36.8 | 466.9 | 1380.4 |
| ge_25pp | 2,443 | 0 | 758 | 1685 | 51.6 | 616.2 | 1380.4 |
| lt_10pp | 4,373 | 0 | 2428 | 1945 | 28.6 | 54.8 | 1130.0 |

Current slate `SL-20261002T061255Z-456d5bef`: 473 priced rows, quote age at build {'median': 34.0, 'max': 73.8}, freshness {'STALE': 473}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 163 | 24.5 | 10.4 | 20.2 | 20.9 | 18.4 | 5.5 | 0.0 | 7.89 | 23.9% | 5.5% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 11 | 0.0 | 0.0 | 9.1 | 45.5 | 45.5 | 0.0 | 0.0 | 13.64 | 45.5% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 4,507 | 183 (4.1%) | 6.0% | 0.0% | {"EXTERNAL_STALE": 163, "AGREES_WITH_KALSHI": 11, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 1,979 | 44 (2.2%) | 11.4% | 0.0% | {"EXTERNAL_STALE": 39, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,142 | 9 (0.8%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 9} |
| fair_v1_ge_25pp_pregame_clean | 458 | 9 (2.0%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 9} |
| fair_v1_lt_10pp | 1,858 | 100 (5.4%) | 1.0% | 0.0% | {"EXTERNAL_STALE": 90, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 886 | 12.0 | 7.5 | 18.7 | 15.5 | 20.6 | 15.1 | 10.6 | 13.61 | 46.4% | 25.7% |
| 4-10x | 609 | 12.3 | 9.5 | 18.6 | 14.1 | 18.1 | 16.6 | 10.8 | 13.37 | 45.5% | 27.4% |
| <2x | 2,474 | 15.6 | 9.1 | 19.7 | 15.2 | 17.5 | 12.9 | 9.9 | 11.72 | 40.4% | 22.9% |
| >=10x | 538 | 11.2 | 5.8 | 15.6 | 13.4 | 20.4 | 21.8 | 11.9 | 17.05 | 54.1% | 33.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,170 | 14.4 | 8.9 | 21.9 | 15.4 | 16.6 | 12.0 | 10.9 | 11.84 | 39.5% | 22.9% |
| 300-1000 | 1,109 | 13.5 | 7.8 | 17.1 | 15.8 | 20.1 | 15.6 | 10.0 | 13.67 | 45.7% | 25.6% |
| <300 | 1,098 | 8.8 | 5.9 | 14.8 | 12.8 | 22.1 | 22.1 | 13.5 | 18.73 | 57.7% | 35.6% |
| >=3000 | 1,130 | 18.7 | 11.1 | 21.5 | 15.5 | 15.7 | 10.3 | 7.3 | 9.92 | 33.3% | 17.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 175 | 0.5172 | 0.3881 | 0.4 | +0.117 | -0.012 | 0.0194 ± 0.0108 |
| ratio 4-10x | 129 | 0.5797 | 0.4468 | 0.4884 | +0.091 | -0.042 | 0.0085 ± 0.0125 |
| ratio <2x | 339 | 0.5304 | 0.4106 | 0.4661 | +0.064 | -0.056 | 0.0069 ± 0.0072 |
| ratio >=10x | 126 | 0.5482 | 0.387 | 0.4524 | +0.096 | -0.065 | 0.018 ± 0.0158 |
| thinner_sample 1000-3000 | 195 | 0.5369 | 0.4171 | 0.4615 | +0.075 | -0.044 | 0.0028 ± 0.0096 |
| thinner_sample 300-1000 | 225 | 0.553 | 0.431 | 0.4622 | +0.091 | -0.031 | 0.0079 ± 0.009 |
| thinner_sample <300 | 260 | 0.5352 | 0.3751 | 0.4423 | +0.093 | -0.067 | 0.0201 ± 0.0106 |
| thinner_sample >=3000 | 89 | 0.5155 | 0.4234 | 0.4382 | +0.077 | -0.015 | 0.0176 ± 0.0114 |
| data_status ADEQUATE | 195 | 0.5205 | 0.4123 | 0.4513 | +0.069 | -0.039 | 0.0051 ± 0.0088 |
| data_status LIMITED | 174 | 0.5592 | 0.4442 | 0.4943 | +0.065 | -0.050 | 0.0013 ± 0.01 |
| data_status POOR | 400 | 0.5384 | 0.3896 | 0.435 | +0.103 | -0.045 | 0.0198 ± 0.008 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 130 | 0.1778 | 0.1788 | -0.0010 ± 0.0013 | 0.5283 | 0.5312 | 0.4936 | 0.4789 | 0.5077 | -0.081 ± 0.0403 | -0.01 (3) |
| 3-5 | 80 | 0.1678 | 0.1642 | +0.0035 ± 0.0038 | 0.5151 | 0.5021 | 0.5167 | 0.4758 | 0.45 | -0.116 ± 0.0481 | 0.02 (1) |
| 5-10 | 165 | 0.1934 | 0.1945 | -0.0011 ± 0.0051 | 0.5712 | 0.5726 | 0.5204 | 0.4457 | 0.4909 | -0.063 ± 0.0348 | -0.02 (2) |
| 10-15 | 127 | 0.2153 | 0.2067 | +0.0086 ± 0.0101 | 0.6134 | 0.5941 | 0.531 | 0.4069 | 0.4331 | -0.082 ± 0.0405 | -0.0633 (3) |
| 15-25 | 166 | 0.2122 | 0.2134 | -0.0012 ± 0.014 | 0.6123 | 0.6078 | 0.5588 | 0.3616 | 0.4639 | -0.010 ± 0.0345 | -0.02 (4) |
| 25-40 | 80 | 0.2384 | 0.1762 | +0.0623 ± 0.0294 | 0.6668 | 0.5224 | 0.6041 | 0.2877 | 0.3375 | -0.086 ± 0.0443 | -0.01 (1) |
| 40+ | 21 | 0.2865 | 0.1302 | +0.1564 ± 0.0712 | 0.746 | 0.4159 | 0.6795 | 0.2345 | 0.2857 | -0.076 ± 0.0648 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 387 | 0.1615 | 0.1624 | -0.0009 ± 0.0007 | 0.4858 | 0.4879 | 0.5085 | 0.4934 | 0.5323 | -0.026 ± 0.0216 | -0.0188 (8) |
| 3-5 | 244 | 0.167 | 0.1656 | +0.0014 ± 0.0021 | 0.5104 | 0.5013 | 0.4915 | 0.4513 | 0.4549 | -0.054 ± 0.0268 | 0.02 (1) |
| 5-10 | 539 | 0.178 | 0.1771 | +0.0009 ± 0.0027 | 0.5332 | 0.5276 | 0.472 | 0.3987 | 0.4323 | -0.029 ± 0.0183 | -0.0133 (6) |
| 10-15 | 430 | 0.1921 | 0.1761 | +0.0160 ± 0.0051 | 0.5641 | 0.5167 | 0.4802 | 0.3562 | 0.3512 | -0.070 ± 0.0201 | -0.0633 (3) |
| 15-25 | 604 | 0.1901 | 0.1609 | +0.0292 ± 0.0065 | 0.5676 | 0.4751 | 0.4778 | 0.2804 | 0.303 | -0.036 ± 0.016 | -0.017 (10) |
| 25-40 | 547 | 0.2118 | 0.0909 | +0.1208 ± 0.0082 | 0.6139 | 0.3017 | 0.4972 | 0.1806 | 0.1499 | -0.078 ± 0.0125 | -0.01 (1) |
| 40+ | 395 | 0.3644 | 0.0361 | +0.3283 ± 0.0103 | 0.9451 | 0.1528 | 0.6144 | 0.1016 | 0.0481 | -0.082 ± 0.0086 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 80 | 0.1717 | 0.1744 | -0.0027 ± 0.0015 | 0.5161 | 0.5206 | 0.5203 | 0.5057 | 0.5875 | -0.009 ± 0.0455 | -0.01 (1) |
| 3-5 | 61 | 0.2099 | 0.2088 | +0.0010 ± 0.0047 | 0.5992 | 0.6046 | 0.4952 | 0.4563 | 0.459 | -0.073 ± 0.0621 | 0.02 (1) |
| 5-10 | 146 | 0.1842 | 0.1768 | +0.0075 ± 0.0053 | 0.55 | 0.5308 | 0.5721 | 0.4962 | 0.4726 | -0.129 ± 0.0351 | -0.01 (3) |
| 10-15 | 138 | 0.218 | 0.2051 | +0.0129 ± 0.0098 | 0.6234 | 0.595 | 0.5827 | 0.4578 | 0.4783 | -0.084 ± 0.0397 | -0.0667 (3) |
| 15-25 | 181 | 0.2176 | 0.196 | +0.0216 ± 0.013 | 0.6194 | 0.5658 | 0.5807 | 0.3841 | 0.4309 | -0.074 ± 0.0337 | -0.0167 (3) |
| 25-40 | 115 | 0.2564 | 0.1906 | +0.0659 ± 0.0251 | 0.7162 | 0.5548 | 0.6483 | 0.3398 | 0.3826 | -0.109 ± 0.0415 | -0.025 (2) |
| 40+ | 48 | 0.3647 | 0.1956 | +0.1691 ± 0.0647 | 0.9908 | 0.5767 | 0.7362 | 0.2401 | 0.3333 | -0.004 ± 0.0591 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 313 | 0.1492 | 0.1509 | -0.0017 ± 0.0007 | 0.4526 | 0.4565 | 0.5553 | 0.5407 | 0.5847 | -0.009 ± 0.0222 | -0.0217 (6) |
| 3-5 | 181 | 0.1704 | 0.1701 | +0.0003 ± 0.0024 | 0.5069 | 0.5136 | 0.5485 | 0.5094 | 0.5249 | -0.037 ± 0.0309 | 0.02 (1) |
| 5-10 | 482 | 0.1754 | 0.1732 | +0.0023 ± 0.0029 | 0.5269 | 0.5154 | 0.5236 | 0.4482 | 0.4668 | -0.040 ± 0.0191 | -0.01 (4) |
| 10-15 | 462 | 0.1863 | 0.1732 | +0.0131 ± 0.0049 | 0.5512 | 0.5124 | 0.5206 | 0.3961 | 0.4156 | -0.042 ± 0.0196 | -0.0575 (4) |
| 15-25 | 607 | 0.2002 | 0.1585 | +0.0416 ± 0.0064 | 0.5865 | 0.4734 | 0.5078 | 0.3127 | 0.3081 | -0.074 ± 0.0162 | -0.0143 (7) |
| 25-40 | 585 | 0.2225 | 0.1137 | +0.1088 ± 0.0088 | 0.644 | 0.3557 | 0.5371 | 0.2227 | 0.2103 | -0.071 ± 0.0141 | -0.015 (6) |
| 40+ | 516 | 0.4005 | 0.0635 | +0.3370 ± 0.0129 | 1.0492 | 0.2271 | 0.661 | 0.1228 | 0.093 | -0.061 ± 0.0105 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 125 | 0.1731 | 0.1749 | -0.0018 ± 0.0013 | 0.5151 | 0.5202 | 0.5112 | 0.497 | 0.536 | -0.049 ± 0.0379 | -0.01 (5) |
| 3-5 | 85 | 0.1633 | 0.1598 | +0.0034 ± 0.0036 | 0.4975 | 0.4887 | 0.5107 | 0.4711 | 0.4471 | -0.133 ± 0.0466 | -- (0) |
| 5-10 | 154 | 0.1978 | 0.1974 | +0.0004 ± 0.0053 | 0.5862 | 0.5778 | 0.5062 | 0.4343 | 0.4675 | -0.062 ± 0.036 | -0.01 (2) |
| 10-15 | 137 | 0.212 | 0.2105 | +0.0015 ± 0.0098 | 0.6105 | 0.6031 | 0.5552 | 0.4316 | 0.4964 | -0.057 ± 0.0394 | -0.044 (5) |
| 15-25 | 162 | 0.2149 | 0.2069 | +0.0080 ± 0.0138 | 0.6226 | 0.5945 | 0.5748 | 0.3811 | 0.4568 | -0.037 ± 0.0343 | -0.03 (1) |
| 25-40 | 90 | 0.2356 | 0.1841 | +0.0514 ± 0.0283 | 0.6636 | 0.5442 | 0.5998 | 0.2851 | 0.3556 | -0.071 ± 0.0425 | 0.0 (1) |
| 40+ | 16 | 0.2995 | 0.1454 | +0.1541 ± 0.0887 | 0.7771 | 0.4518 | 0.6921 | 0.2369 | 0.3125 | -0.064 ± 0.0806 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 369 | 0.1598 | 0.16 | -0.0001 ± 0.0007 | 0.4843 | 0.4847 | 0.5078 | 0.4933 | 0.5068 | -0.049 ± 0.021 | -0.0162 (13) |
| 3-5 | 251 | 0.1708 | 0.1673 | +0.0035 ± 0.0021 | 0.5117 | 0.5025 | 0.4866 | 0.4474 | 0.4263 | -0.084 ± 0.0264 | -0.01 (2) |
| 5-10 | 533 | 0.1828 | 0.1786 | +0.0042 ± 0.0028 | 0.5465 | 0.5258 | 0.4611 | 0.3876 | 0.3996 | -0.044 ± 0.0184 | -0.01 (2) |
| 10-15 | 444 | 0.1939 | 0.1815 | +0.0124 ± 0.005 | 0.5717 | 0.532 | 0.4959 | 0.3725 | 0.3851 | -0.056 ± 0.0202 | -0.03 (9) |
| 15-25 | 638 | 0.181 | 0.1463 | +0.0347 ± 0.006 | 0.5483 | 0.4419 | 0.4844 | 0.2856 | 0.2978 | -0.045 ± 0.0148 | -0.03 (2) |
| 25-40 | 542 | 0.2156 | 0.0972 | +0.1184 ± 0.0085 | 0.6244 | 0.3155 | 0.4965 | 0.1782 | 0.1531 | -0.076 ± 0.0129 | 0.0 (1) |
| 40+ | 369 | 0.3805 | 0.0357 | +0.3448 ± 0.0109 | 0.9914 | 0.1531 | 0.6187 | 0.1009 | 0.0379 | -0.091 ± 0.0087 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 405 | 0.2021 | 0.202 | +0.0001 ± 0.0008 | 0.5845 | 0.5844 | 0.501 | 0.4864 | 0.484 | -0.046 ± 0.0224 | -0.0226 (46) |
| 3-5 | 287 | 0.1914 | 0.1908 | +0.0005 ± 0.0021 | 0.5629 | 0.5583 | 0.4618 | 0.422 | 0.439 | -0.034 ± 0.0256 | -0.0059 (32) |
| 5-10 | 617 | 0.1868 | 0.1818 | +0.0050 ± 0.0026 | 0.5566 | 0.5428 | 0.4587 | 0.3854 | 0.389 | -0.042 ± 0.0172 | -0.0049 (71) |
| 10-15 | 409 | 0.2026 | 0.1904 | +0.0122 ± 0.0054 | 0.5948 | 0.5588 | 0.4568 | 0.3334 | 0.3447 | -0.041 ± 0.0214 | 0.0016 (63) |
| 15-25 | 551 | 0.2354 | 0.2099 | +0.0255 ± 0.0076 | 0.6644 | 0.6066 | 0.529 | 0.3359 | 0.3666 | -0.034 ± 0.0195 | -0.0216 (58) |
| 25-40 | 265 | 0.2623 | 0.1664 | +0.0959 ± 0.0157 | 0.7251 | 0.502 | 0.5718 | 0.2603 | 0.2604 | -0.066 ± 0.0247 | -0.0216 (25) |
| 40+ | 92 | 0.4281 | 0.1583 | +0.2698 ± 0.0445 | 1.2043 | 0.4894 | 0.7341 | 0.2267 | 0.2391 | -0.064 ± 0.043 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 756 | 0.193 | 0.1924 | +0.0006 ± 0.0005 | 0.5632 | 0.5613 | 0.4969 | 0.4823 | 0.4683 | -0.055 ± 0.0159 | -0.0155 (82) |
| 3-5 | 532 | 0.1967 | 0.1954 | +0.0013 ± 0.0016 | 0.5729 | 0.5669 | 0.4694 | 0.4296 | 0.4342 | -0.041 ± 0.0192 | -0.018 (54) |
| 5-10 | 1131 | 0.1851 | 0.1785 | +0.0065 ± 0.0019 | 0.5527 | 0.5329 | 0.4432 | 0.3692 | 0.366 | -0.045 ± 0.0127 | -0.0089 (121) |
| 10-15 | 833 | 0.1979 | 0.1835 | +0.0144 ± 0.0037 | 0.5824 | 0.5406 | 0.4505 | 0.327 | 0.3301 | -0.043 ± 0.0147 | -0.0053 (99) |
| 15-25 | 1164 | 0.2225 | 0.1879 | +0.0346 ± 0.005 | 0.6408 | 0.551 | 0.5029 | 0.3074 | 0.3162 | -0.043 ± 0.0127 | -0.0255 (106) |
| 25-40 | 798 | 0.2452 | 0.1298 | +0.1155 ± 0.008 | 0.6919 | 0.4053 | 0.53 | 0.2148 | 0.1905 | -0.071 ± 0.0126 | -0.0206 (47) |
| 40+ | 471 | 0.3902 | 0.0807 | +0.3095 ± 0.0143 | 1.0658 | 0.2706 | 0.6544 | 0.1386 | 0.1083 | -0.075 ± 0.0133 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 769 | 1.184 ± 0.105 | 1.237 | 0.1725 | 0.1884 | 0.203 | 0.1911 |
| gen2 | 769 | 0.982 ± 0.092 | 1.166 | 0.1888 | 0.1876 | 0.2209 | 0.1919 |
| gen1_elo | 769 | 1.147 ± 0.102 | 1.22 | 0.1782 | 0.1888 | 0.2026 | 0.1913 |
| gen1_sr | 769 | 1.193 ± 0.12 | 1.222 | 0.145 | 0.19 | 0.2179 | 0.1911 |
| gen1_ledger | 2626 | 0.906 ± 0.053 | 1.074 | 0.1626 | 0.2008 | 0.2184 | 0.1908 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 4,476)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,434 | 32.0% |
| STALE_QUOTE | market_freshness | 1,306 | 29.2% |
| POOR_DATA | data | 367 | 8.2% |
| BOOK_QUALITY | execution | 298 | 6.7% |
| LIMITED_DATA | data | 279 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 268 | 6.0% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 224 | 5.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 213 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 84 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 32.0%, market_freshness 29.2%, data 14.4%, market_freshness/coverage 10.8%, execution 6.7%, model_calibration_or_unknown 5.0%, mapping 1.9%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 65.2%, STALE_KALSHI_QUOTE 62.0%, STALE_PLAYER_DATA 55.5%, THIN_PLAYER_HISTORY 52.8%, MODEL_INTERNAL_DISAGREEMENT 33.0%, ASYMMETRIC_SAMPLE_SIZE 28.8%, WIDE_SPREAD 15.3%, MODEL_HIGH_UNCERTAINTY 12.5%, PLAYER_IDENTITY_RISK 11.3%, LEVEL_TRANSFER_RISK 8.8%, EVENT_MAPPING_RISK 7.0%, LOW_DISPLAYED_LIQUIDITY 4.7%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.8%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 34.7%, POST_SETTLEMENT_OBSERVATION 32.0%, POSSIBLE_IN_PLAY_QUOTE 6.8%, CONFIRMED_IN_PLAY_QUOTE 2.5%

### >= ge_25 pp (N = 2,443)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,113 | 45.6% |
| STALE_QUOTE | market_freshness | 576 | 23.6% |
| POOR_DATA | data | 161 | 6.6% |
| BOOK_QUALITY | execution | 144 | 5.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 135 | 5.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 126 | 5.2% |
| LIMITED_DATA | data | 76 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 59 | 2.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 53 | 2.2% |

Cause class: coverage 45.6%, market_freshness 23.6%, market_freshness/coverage 10.7%, data 9.7%, execution 5.9%, mapping 2.4%, model_calibration_or_unknown 2.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.6%, LOW_DATA_QUALITY 69.3%, STALE_KALSHI_QUOTE 69.0%, THIN_PLAYER_HISTORY 55.3%, STALE_PLAYER_DATA 53.2%, MODEL_INTERNAL_DISAGREEMENT 33.8%, ASYMMETRIC_SAMPLE_SIZE 31.2%, PLAYER_IDENTITY_RISK 14.1%, WIDE_SPREAD 14.0%, MODEL_HIGH_UNCERTAINTY 13.8%, EVENT_MAPPING_RISK 8.7%, LEVEL_TRANSFER_RISK 8.4%, LOW_DISPLAYED_LIQUIDITY 5.1%, MODEL_CALIBRATION_OUTLIER 3.1%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 48.5%, POST_SETTLEMENT_OBSERVATION 45.6%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 2.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2067, "IDENTITY_AMBIGUOUS": 376}; ticker orientation: {"VERIFIED": 2443}.

Checks: discipline:AMBIGUOUS 181, discipline:PASS 2262, identity_confidence:AMBIGUOUS 344, identity_confidence:PASS 2099, level_mapping:NA 193, level_mapping:PASS 2250, market_pair:AMBIGUOUS 62, market_pair:NA 68, market_pair:PASS 2313, model_complement:NA 41, model_complement:PASS 2402, namesake:PASS 2443, physical_match_id:NA 1301, physical_match_id:PASS 1142, player_ids:PASS 2443, same_pair_other_event:PASS 2443, ticker_orientation:PASS 2443

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 300 | 4.0% | 4.2% | 0.5% | {"market_freshness": 12} | 6.01 | 0.1838 / 0.1834 (45) | 38.3% | 0.0% | 0.7% | 4.3% |
| CHALLENGER | 1,568 | 18.4% | 8.1% | 11.8% | {"coverage": 153, "market_freshness": 67, "market_freshness/coverage": 37, "data": 17, "model_calibration_or_unknown": 12, "execution": 3} | 7.67 | 0.2243 / 0.2064 (515) | 52.4% | 4.2% | 0.7% | 22.0% |
| DOUBLES | 369 | 49.0% | 48.4% | 7.4% | {"market_freshness": 89, "market_freshness/coverage": 36, "execution": 29, "mapping": 21, "coverage": 6} | 24.11 | 0.3222 / 0.2257 (150) | 60.7% | 0.0% | 100.0% | 22.2% |
| ITF_MEN | 3,413 | 24.5% | 14.0% | 34.3% | {"coverage": 437, "market_freshness": 162, "data": 86, "execution": 71, "market_freshness/coverage": 70, "mapping": 10, "model_calibration_or_unknown": 1} | 9.78 | 0.2089 / 0.183 (1230) | 54.7% | 50.4% | 5.6% | 31.1% |
| ITF_WOMEN | 3,379 | 28.7% | 17.0% | 39.8% | {"coverage": 505, "market_freshness": 203, "data": 117, "market_freshness/coverage": 76, "execution": 32, "mapping": 26, "model_calibration_or_unknown": 12} | 12.21 | 0.2057 / 0.1861 (1091) | 57.8% | 54.6% | 6.5% | 32.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.5% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 782 | 9.2% | 8.0% | 2.9% | {"market_freshness": 29, "market_freshness/coverage": 14, "model_calibration_or_unknown": 11, "data": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.47 | 0.1995 / 0.1973 (113) | 39.9% | 2.7% | 1.5% | 13.9% |
| WTA125 | 421 | 16.4% | 10.3% | 2.8% | {"market_freshness/coverage": 27, "model_calibration_or_unknown": 15, "market_freshness": 12, "data": 8, "coverage": 7} | 10.43 | 0.2278 / 0.204 (209) | 34.4% | 9.0% | 0.5% | 19.0% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 5 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 6 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 7 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 8 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 9 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 10 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 11 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 13 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 14 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 15 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 16 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 17 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 18 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 20 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 21 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 22 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 23 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 24 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 25 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 26 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 29 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 30 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 31 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 34 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 35 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 37 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 39 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 40 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 41 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 42 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 43 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 44 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.1h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 793 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 45 | `KXITFWMATCH-26OCT01TANVED-TAN` | ITF_WOMEN | fair_v1 | 76% / 8% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 167 min (STALE); no external reference |
| 46 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26SEP24BOUKUR-BOU` | ITF_WOMEN | gen1_ledger | 76% / 8% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 1497.0, ratio 2.48); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26SEP28TABSAN-SAN` | CHALLENGER | gen1_ledger | 70% / 4% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 48 min (STALE); no external reference |
| 50 | `KXITFWMATCH-26OCT01UEMSIM-SIM` | ITF_WOMEN | fair_v1 | 71% / 4% | +66 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 51 min (STALE); data POOR (grade D, thinner serve sample 824.0, ratio 1.14); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9656, "by_level_share_of_ge_25pp": {"ATP": 0.0049, "CHALLENGER": 0.1183, "DOUBLES": 0.0741, "ITF_MEN": 0.3426, "ITF_WOMEN": 0.3975, "OTHER": 0.0049, "WTA": 0.0295, "WTA125": 0.0282}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6897, "share_primary_cause_market_settled_or_in_play": 0.5625, "share_primary_cause_stale_quote_only": 0.2358}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2443, "identity_ambiguous_share": 0.1539, "ticker_orientation": {"VERIFIED": 2443}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1142, "with_external": 9, "coverage": 0.0079, "external_status": {"EXTERNAL_STALE": 9}, "triangulation": {"INSUFFICIENT_INPUTS": 9}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 458, "with_external": 9, "coverage": 0.0197, "external_status": {"EXTERNAL_STALE": 9}, "triangulation": {"INSUFFICIENT_INPUTS": 9}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 776.0, "median_sample_ratio": 2.33, "median_min_matches": 24.0, "median_max_days_since_last": 175.0, "share_severe_asymmetry": 0.1699, "data_status": {"POOR": 1158, "LIMITED": 836, "ADEQUATE": 449}, "comparison_lt_10pp": {"median_thinner_serve_points": 1970.0, "median_sample_ratio": 1.7, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 175, "model_minus_observed": 0.1172, "kalshi_minus_observed": -0.0119, "brier_diff_model_minus_kalshi": 0.0194}, "4-10x": {"n": 129, "model_minus_observed": 0.0913, "kalshi_minus_observed": -0.0416, "brier_diff_model_minus_kalshi": 0.0085}, "<2x": {"n": 339, "model_minus_observed": 0.0643, "kalshi_minus_observed": -0.0555, "brier_diff_model_minus_kalshi": 0.0069}, ">=10x": {"n": 126, "model_minus_observed": 0.0958, "kalshi_minus_observed": -0.0654, "brier_diff_model_minus_kalshi": 0.018}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 769, "model": {"intercept": -0.656, "slope": 0.982, "slope_se": 0.092}, "kalshi_mid_same_rows": {"intercept": 0.205, "slope": 1.166, "slope_se": 0.1}, "mean_extremity_model": 0.1888, "mean_extremity_kalshi": 0.1876, "model_brier": 0.2209, "kalshi_brier": 0.1919, "brier_diff_model_minus_kalshi": 0.029, "brier_diff_se": 0.0068, "model_logloss": 0.6323, "kalshi_logloss": 0.5618}, "fair_v1": {"n": 769, "model": {"intercept": -0.448, "slope": 1.184, "slope_se": 0.105}, "kalshi_mid_same_rows": {"intercept": 0.322, "slope": 1.237, "slope_se": 0.103}, "mean_extremity_model": 0.1725, "mean_extremity_kalshi": 0.1884, "model_brier": 0.203, "kalshi_brier": 0.1911, "brier_diff_model_minus_kalshi": 0.0119, "brier_diff_se": 0.0052, "model_logloss": 0.5887, "kalshi_logloss": 0.5599}, "gen1_elo": {"n": 769, "model": {"intercept": -0.429, "slope": 1.147, "slope_se": 0.102}, "kalshi_mid_same_rows": {"intercept": 0.326, "slope": 1.22, "slope_se": 0.101}, "mean_extremity_model": 0.1782, "mean_extremity_kalshi": 0.1888, "model_brier": 0.2026, "kalshi_brier": 0.1913, "brier_diff_model_minus_kalshi": 0.0114, "brier_diff_se": 0.0053, "model_logloss": 0.5899, "kalshi_logloss": 0.5601}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2534, "share_ge_15": 0.4391, "median_abs_gap": 12.81, "n": 4507}, "gen1_elo": {"share_ge_25": 0.2461, "share_ge_15": 0.4273, "median_abs_gap": 12.42, "n": 4507}, "gen1_sr": {"share_ge_25": 0.3062, "share_ge_15": 0.5285, "median_abs_gap": 16.1, "n": 4507}, "gen2": {"share_ge_25": 0.3051, "share_ge_15": 0.5012, "median_abs_gap": 15.06, "n": 4507}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.139, "share_ge_15": 0.3291, "median_abs_gap": 9.95, "n": 3294}, "gen1_elo": {"share_ge_25": 0.1378, "share_ge_15": 0.3118, "median_abs_gap": 9.51, "n": 3294}, "gen1_sr": {"share_ge_25": 0.1961, "share_ge_15": 0.4353, "median_abs_gap": 12.7, "n": 3294}, "gen2": {"share_ge_25": 0.2089, "share_ge_15": 0.4208, "median_abs_gap": 12.75, "n": 3294}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.01, "share_ge_25_all": 0.04, "share_ge_25_pregame_clean": 0.0418}, "WTA": {"median_abs_gap_pregame_clean": 8.47, "share_ge_25_all": 0.0921, "share_ge_25_pregame_clean": 0.0802}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2255, "share_within_10pp_all": 0.4213, "share_within_10pp_pregame_clean": 0.5009, "corr_model_vs_mid_pregame_clean": 0.8335}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 130, "model_brier": 0.1778, "kalshi_brier": 0.1788, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 127, "model_brier": 0.2153, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.0086}, "15-25": {"n_settled": 166, "model_brier": 0.2122, "kalshi_brier": 0.2134, "brier_diff_model_minus_kalshi": -0.0012}, "25-40": {"n_settled": 80, "model_brier": 0.2384, "kalshi_brier": 0.1762, "brier_diff_model_minus_kalshi": 0.0623}, "3-5": {"n_settled": 80, "model_brier": 0.1678, "kalshi_brier": 0.1642, "brier_diff_model_minus_kalshi": 0.0035}, "40+": {"n_settled": 21, "model_brier": 0.2865, "kalshi_brier": 0.1302, "brier_diff_model_minus_kalshi": 0.1564}, "5-10": {"n_settled": 165, "model_brier": 0.1934, "kalshi_brier": 0.1945, "brier_diff_model_minus_kalshi": -0.0011}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 150, "model_brier": 0.3222, "kalshi_brier": 0.2257, "brier_diff_model_minus_kalshi": 0.0965, "brier_diff_se": 0.0268, "corr_model_outcome": -0.0804, "corr_kalshi_outcome": 0.3499}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
