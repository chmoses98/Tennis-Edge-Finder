# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-02T13:34Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 10,663): 0-3 13.5%, 3-5 8.9%, 5-10 19.5%, 10-15 14.7%, 15-25 19.6%, 25-40 14.4%, 40+ 9.4%; median gap 12.52 pp.
* **Where the extremes live**: 96.6% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.4%, Challenger 11.9%, doubles 7.2%). Main tour: ATP 3.9% and WTA 9.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,538): MARKET_ALREADY_SETTLED_WHEN_PRICED 46.3%, STALE_QUOTE 24.4%, POOR_DATA 6.4%, BOOK_QUALITY 5.8%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IN_PLAY_QUOTE 3.8%, LIMITED_DATA 3.1%, IDENTITY_AMBIGUOUS 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 46.3%, market_freshness 24.4%, data 9.5%, market_freshness/coverage 9.2%, execution 5.8%, mapping 2.6%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 69.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 55.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,538 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 14.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 6.2% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 804.0 points vs 1970.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.134, Gen-2 0.95, Gen-1 ledger 0.884 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 87 model 0.242 vs Kalshi 0.1797; n 23 model 0.3363 vs Kalshi 0.1395.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 34,021 model-market comparisons (58,524 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 16,390 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-02T13:30:06.576336+00:00'], shadow board 9,374 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-02T13:30:10.678097+00:00'], Model 4 2,910 rows, 8,106 settled tickers, 1,803 tickers with an external scan.
* By model: {"gen1_ledger": 9552, "gen1_elo": 4716, "fair_v1": 4716, "gen2": 4716, "gen1_sr": 4716, "model4_fundamental": 2807, "model4_conditioned": 2798}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 10,663 | 13.5 | 8.9 | 19.5 | 14.7 | 19.6 | 14.4 | 9.4 | 12.52 | 43.4% | 23.8% |
| MW fair_v1 | 4,716 | 13.7 | 8.4 | 18.7 | 14.8 | 18.6 | 15.0 | 10.7 | 12.95 | 44.3% | 25.7% |
| MW gen1_elo | 4,716 | 12.9 | 8.9 | 20.0 | 15.2 | 18.1 | 14.8 | 10.1 | 12.48 | 43.1% | 25.0% |
| MW gen1_ledger | 5,947 | 13.3 | 9.3 | 20.1 | 14.7 | 20.4 | 13.9 | 8.4 | 12.23 | 42.6% | 22.3% |
| MW gen1_sr | 4,716 | 9.8 | 7.1 | 16.9 | 13.1 | 22.3 | 18.5 | 12.4 | 16.29 | 53.2% | 30.9% |
| MW gen2 | 4,716 | 11.5 | 6.3 | 16.4 | 15.2 | 19.7 | 17.2 | 13.6 | 15.29 | 50.5% | 30.8% |
| all families model4_conditioned | 2,798 | 18.6 | 15.6 | 29.6 | 23.8 | 8.3 | 2.3 | 1.9 | 7.34 | 12.4% | 4.2% |
| all families model4_fundamental | 2,807 | 14.5 | 10.8 | 30.1 | 21.8 | 14.4 | 5.4 | 2.9 | 9.06 | 22.7% | 8.3% |

Configurable thresholds (primary): >=5pp 77.6%, >=10pp 58.1%, >=15pp 43.4%, >=20pp 32.8%, >=25pp 23.8%, >=30pp 17.5%, >=40pp 9.4%, >=50pp 4.3%
Executable gap (model outside the book, before fees): median 10.15pp; >=10pp 50.4%, >=25pp 21.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 240 | 22.5 | 17.5 | 27.5 | 12.9 | 14.6 | 1.2 | 3.8 | 6.14 | 19.6% | 5.0% |
| CHALLENGER | 818 | 15.2 | 9.2 | 16.3 | 15.9 | 15.5 | 14.9 | 13.1 | 13.03 | 43.5% | 28.0% |
| ITF_MEN | 1,505 | 11.9 | 8.2 | 19.6 | 14.6 | 18.1 | 15.1 | 12.4 | 13.12 | 45.6% | 27.5% |
| ITF_WOMEN | 1,636 | 10.9 | 6.5 | 16.1 | 14.7 | 21.1 | 19.2 | 11.5 | 15.78 | 51.8% | 30.7% |
| WTA | 433 | 23.1 | 10.6 | 25.9 | 12.7 | 18.7 | 6.7 | 2.3 | 8.16 | 27.7% | 9.0% |
| WTA125 | 84 | 14.3 | 4.8 | 17.9 | 23.8 | 20.2 | 14.3 | 4.8 | 12.4 | 39.3% | 19.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 240 | 23.3 | 12.9 | 25.0 | 16.2 | 16.7 | 1.7 | 4.2 | 7.06 | 22.5% | 5.8% |
| CHALLENGER | 818 | 11.0 | 5.4 | 18.0 | 17.1 | 18.1 | 17.9 | 12.6 | 14.84 | 48.5% | 30.4% |
| ITF_MEN | 1,505 | 10.0 | 6.0 | 16.8 | 16.1 | 20.2 | 16.6 | 14.3 | 15.45 | 51.1% | 30.9% |
| ITF_WOMEN | 1,636 | 9.3 | 6.4 | 14.0 | 13.0 | 19.6 | 19.9 | 18.0 | 18.23 | 57.4% | 37.8% |
| WTA | 433 | 20.6 | 5.5 | 16.9 | 15.7 | 22.4 | 16.6 | 2.3 | 12.93 | 41.3% | 18.9% |
| WTA125 | 84 | 6.0 | 6.0 | 16.7 | 20.2 | 22.6 | 15.5 | 13.1 | 15.56 | 51.2% | 28.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 240 | 28.3 | 12.9 | 28.8 | 10.8 | 9.2 | 6.2 | 3.8 | 6.53 | 19.2% | 10.0% |
| CHALLENGER | 818 | 14.6 | 8.1 | 21.1 | 14.4 | 13.8 | 14.2 | 13.8 | 11.99 | 41.8% | 28.0% |
| ITF_MEN | 1,505 | 10.0 | 9.6 | 18.5 | 16.1 | 18.2 | 15.9 | 11.7 | 13.08 | 45.8% | 27.6% |
| ITF_WOMEN | 1,636 | 9.3 | 6.9 | 16.8 | 14.4 | 23.5 | 18.5 | 10.4 | 16.46 | 52.5% | 29.0% |
| WTA | 433 | 23.6 | 13.9 | 29.6 | 15.7 | 11.6 | 4.2 | 1.6 | 6.99 | 17.3% | 5.8% |
| WTA125 | 84 | 16.7 | 6.0 | 22.6 | 29.8 | 13.1 | 10.7 | 1.2 | 10.92 | 25.0% | 11.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 794 | 21.4 | 13.6 | 26.6 | 15.9 | 13.5 | 6.4 | 2.6 | 7.45 | 22.5% | 9.1% |
| DOUBLES | 373 | 5.4 | 3.8 | 9.7 | 10.5 | 22.0 | 20.9 | 27.9 | 24.15 | 70.8% | 48.8% |
| ITF_MEN | 2,013 | 14.4 | 8.9 | 19.0 | 13.7 | 21.0 | 13.7 | 9.4 | 12.51 | 44.0% | 23.1% |
| ITF_WOMEN | 1,846 | 8.9 | 8.3 | 17.5 | 14.2 | 23.5 | 18.5 | 9.0 | 15.32 | 51.0% | 27.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 337 | 13.3 | 9.5 | 21.7 | 16.9 | 22.9 | 11.9 | 3.9 | 11.35 | 38.6% | 15.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 239 | 22.2 | 17.6 | 27.6 | 13.0 | 14.6 | 1.3 | 3.8 | 6.16 | 19.7% | 5.0% |
| CHALLENGER | 607 | 18.9 | 11.4 | 19.6 | 18.9 | 16.5 | 9.2 | 5.4 | 10.11 | 31.1% | 14.7% |
| ITF_MEN | 966 | 15.9 | 11.5 | 24.5 | 15.8 | 18.1 | 10.1 | 3.9 | 9.63 | 32.2% | 14.1% |
| ITF_WOMEN | 1,096 | 14.8 | 8.7 | 19.4 | 17.1 | 22.4 | 13.5 | 4.1 | 12.39 | 40.0% | 17.6% |
| WTA | 432 | 23.1 | 10.7 | 25.9 | 12.7 | 18.8 | 6.5 | 2.3 | 8.12 | 27.6% | 8.8% |
| WTA125 | 81 | 14.8 | 4.9 | 18.5 | 24.7 | 19.8 | 12.3 | 4.9 | 11.65 | 37.0% | 17.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 239 | 23.4 | 12.6 | 25.1 | 16.3 | 16.7 | 1.7 | 4.2 | 7.08 | 22.6% | 5.9% |
| CHALLENGER | 607 | 13.5 | 6.8 | 22.6 | 20.6 | 19.3 | 12.8 | 4.5 | 11.82 | 36.6% | 17.3% |
| ITF_MEN | 966 | 13.2 | 7.7 | 20.3 | 18.9 | 20.9 | 13.3 | 5.6 | 12.21 | 39.9% | 18.9% |
| ITF_WOMEN | 1,096 | 11.4 | 8.3 | 16.1 | 12.8 | 22.6 | 17.5 | 11.3 | 15.54 | 51.5% | 28.8% |
| WTA | 432 | 20.6 | 5.6 | 16.9 | 15.7 | 22.4 | 16.4 | 2.3 | 12.85 | 41.2% | 18.8% |
| WTA125 | 81 | 6.2 | 6.2 | 16.1 | 21.0 | 23.5 | 16.1 | 11.1 | 15.33 | 50.6% | 27.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 652 | 23.9 | 15.8 | 29.3 | 15.5 | 12.7 | 2.5 | 0.3 | 6.68 | 15.5% | 2.8% |
| DOUBLES | 339 | 5.6 | 3.5 | 9.7 | 10.6 | 21.8 | 21.2 | 27.4 | 24.15 | 70.5% | 48.7% |
| ITF_MEN | 1,440 | 17.6 | 10.7 | 22.3 | 14.7 | 20.8 | 10.3 | 3.5 | 9.87 | 34.7% | 13.9% |
| ITF_WOMEN | 1,250 | 11.0 | 9.8 | 21.4 | 16.4 | 24.5 | 15.0 | 2.1 | 12.12 | 41.5% | 17.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 334 | 15.6 | 9.9 | 26.4 | 23.1 | 18.3 | 6.9 | 0.0 | 9.55 | 25.1% | 6.9% |
| WTA125 | 259 | 15.8 | 10.4 | 25.9 | 20.1 | 21.2 | 6.2 | 0.4 | 9.54 | 27.8% | 6.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 373 | 5.4 | 3.8 | 9.7 | 10.5 | 22.0 | 20.9 | 27.9 | 24.15 | 70.8% | 48.8% |
| singles | 5,574 | 13.8 | 9.7 | 20.8 | 14.9 | 20.2 | 13.4 | 7.1 | 11.79 | 40.8% | 20.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,019 | 15.7 | 8.3 | 18.8 | 14.3 | 16.1 | 14.2 | 12.5 | 12.29 | 42.8% | 26.7% |
| Hard | 3,386 | 13.1 | 8.7 | 19.0 | 14.5 | 19.2 | 15.2 | 10.2 | 12.99 | 44.6% | 25.4% |
| UNKNOWN | 311 | 13.5 | 5.8 | 15.4 | 19.0 | 20.6 | 15.4 | 10.3 | 13.77 | 46.3% | 25.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,469 | 18.0 | 10.1 | 21.0 | 14.6 | 17.1 | 11.0 | 8.2 | 10.19 | 36.3% | 19.2% |
| B | 658 | 17.0 | 10.8 | 18.1 | 17.0 | 15.1 | 10.2 | 11.8 | 11.17 | 37.1% | 22.0% |
| C | 788 | 12.3 | 8.1 | 22.7 | 13.4 | 16.9 | 15.6 | 10.9 | 12.85 | 43.4% | 26.5% |
| D | 871 | 11.7 | 8.2 | 17.6 | 13.9 | 20.9 | 15.7 | 12.1 | 14.44 | 48.7% | 27.8% |
| F | 930 | 7.6 | 4.7 | 13.4 | 15.3 | 23.0 | 23.4 | 12.5 | 18.88 | 58.9% | 35.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,828 | 18.9 | 11.8 | 26.2 | 16.7 | 16.4 | 7.0 | 3.0 | 8.66 | 26.4% | 10.0% |
| B | 985 | 13.8 | 9.3 | 21.4 | 16.2 | 19.3 | 12.6 | 7.3 | 11.64 | 39.2% | 19.9% |
| C | 1,227 | 11.2 | 8.2 | 15.7 | 13.8 | 22.2 | 15.6 | 13.2 | 15.42 | 51.0% | 28.8% |
| D | 915 | 11.3 | 8.2 | 20.8 | 11.9 | 23.6 | 15.4 | 8.8 | 14.12 | 47.9% | 24.3% |
| F | 992 | 6.8 | 7.2 | 12.4 | 12.9 | 23.3 | 24.3 | 13.2 | 19.19 | 60.8% | 37.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,808 | 17.1 | 9.6 | 20.3 | 15.8 | 16.4 | 11.1 | 9.7 | 10.71 | 37.2% | 20.8% |
| LIMITED | 1,089 | 14.8 | 10.1 | 21.9 | 13.2 | 16.4 | 13.7 | 10.0 | 11.67 | 40.0% | 23.7% |
| POOR | 1,819 | 9.7 | 6.3 | 15.3 | 14.6 | 22.2 | 19.6 | 12.2 | 16.86 | 54.0% | 31.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 341 | 34.3 | 22.9 | 33.1 | 6.5 | 2.4 | 0.9 | 0.0 | 4.16 | 3.2% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 5,947 | 13.3 | 9.3 | 20.1 | 14.7 | 20.4 | 13.9 | 8.4 | 12.23 | 42.6% | 22.3% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,702 | 21.7 | 13.4 | 30.6 | 17.2 | 13.6 | 2.8 | 0.7 | 7.04 | 17.0% | 3.4% |
| TOTAL_GAMES | 1,132 | 9.9 | 9.4 | 26.5 | 24.9 | 17.0 | 8.0 | 4.4 | 10.66 | 29.3% | 12.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 880 | 28.6 | 32.8 | 26.9 | 0.7 | 8.8 | 1.7 | 0.5 | 4.27 | 10.9% | 2.2% |
| GAME_SPREAD | 562 | 36.8 | 15.1 | 25.1 | 18.0 | 2.5 | 1.8 | 0.7 | 4.5 | 5.0% | 2.5% |
| TOTAL_GAMES | 1,356 | 4.6 | 4.5 | 33.1 | 41.3 | 10.3 | 3.0 | 3.2 | 10.7 | 16.5% | 6.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 880 | 26.0 | 16.8 | 33.9 | 8.2 | 9.8 | 4.3 | 1.0 | 5.79 | 15.1% | 5.3% |
| GAME_SPREAD | 562 | 17.6 | 10.3 | 25.6 | 23.3 | 15.8 | 5.0 | 2.3 | 9.54 | 23.1% | 7.3% |
| TOTAL_GAMES | 1,365 | 5.9 | 7.0 | 29.6 | 30.0 | 16.9 | 6.2 | 4.4 | 10.89 | 27.5% | 10.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4,716 | 44.3% | 25.7% | 12.95 | 33.1% | 14.1% | 9.95 |
| gen1_elo | 4,716 | 43.1% | 25.0% | 12.48 | 31.3% | 14.0% | 9.53 |
| gen1_sr | 4,716 | 53.2% | 30.9% | 16.29 | 43.5% | 19.7% | 12.68 |
| gen2 | 4,716 | 50.5% | 30.8% | 15.29 | 42.2% | 21.1% | 12.76 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,773 | 18.0 | 12.2 | 23.4 | 15.3 | 18.3 | 9.8 | 3.1 | 9.13 | 31.1% | 12.9% |
| STALE | 2,943 | 11.2 | 6.2 | 16.0 | 14.4 | 18.9 | 18.1 | 15.3 | 16.25 | 52.3% | 33.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,201 | 15.3 | 10.2 | 22.0 | 15.9 | 19.8 | 12.2 | 4.6 | 10.71 | 36.6% | 16.8% |
| STALE | 2,746 | 11.0 | 8.2 | 17.9 | 13.2 | 21.0 | 15.9 | 12.9 | 14.82 | 49.7% | 28.7% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 10,663 | 0 | 4974 | 5689 | 31.2 | 199.5 | 1400.4 |
| ge_15pp | 4,627 | 0 | 1723 | 2904 | 38.8 | 466.9 | 1380.4 |
| ge_25pp | 2,538 | 0 | 765 | 1773 | 53.6 | 608.5 | 1380.4 |
| lt_10pp | 4,469 | 0 | 2470 | 1999 | 28.7 | 54.8 | 1130.0 |

Current slate `SL-20261002T133430Z-a8b7327a`: 275 priced rows, quote age at build {'median': 31.2, 'max': 83.6}, freshness {'STALE': 275}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 173 | 21.4 | 13.9 | 24.3 | 19.6 | 17.3 | 3.5 | 0.0 | 7.82 | 20.8% | 3.5% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 16.7 | 41.7 | 41.7 | 0.0 | 0.0 | 13.48 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 4,716 | 194 (4.1%) | 6.2% | 0.0% | {"EXTERNAL_STALE": 173, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,091 | 41 (2.0%) | 12.2% | 0.0% | {"EXTERNAL_STALE": 36, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,212 | 6 (0.5%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_ge_25pp_pregame_clean | 482 | 6 (1.2%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 6} |
| fair_v1_lt_10pp | 1,929 | 114 (5.9%) | 1.8% | 0.0% | {"EXTERNAL_STALE": 103, "ALL_AGREE": 8, "AGREES_WITH_KALSHI": 2, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 927 | 11.9 | 7.3 | 18.6 | 15.4 | 20.2 | 16.1 | 10.6 | 13.77 | 46.8% | 26.7% |
| 4-10x | 633 | 12.3 | 9.3 | 18.8 | 14.2 | 18.0 | 16.6 | 10.7 | 13.37 | 45.3% | 27.3% |
| <2x | 2,598 | 15.4 | 9.2 | 19.4 | 14.7 | 17.9 | 12.9 | 10.4 | 11.96 | 41.3% | 23.4% |
| >=10x | 558 | 10.8 | 5.9 | 15.8 | 14.3 | 20.1 | 21.0 | 12.2 | 16.66 | 53.2% | 33.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,240 | 14.5 | 8.6 | 21.4 | 15.2 | 16.9 | 12.0 | 11.4 | 11.94 | 40.3% | 23.5% |
| 300-1000 | 1,157 | 13.2 | 7.6 | 16.9 | 15.6 | 20.1 | 16.4 | 10.1 | 13.99 | 46.6% | 26.5% |
| <300 | 1,124 | 8.6 | 6.0 | 15.0 | 13.2 | 21.8 | 21.8 | 13.5 | 18.5 | 57.1% | 35.3% |
| >=3000 | 1,195 | 18.2 | 11.3 | 21.3 | 15.0 | 16.1 | 10.3 | 7.9 | 9.97 | 34.3% | 18.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 185 | 0.5142 | 0.3829 | 0.4054 | +0.109 | -0.022 | 0.0175 ± 0.0107 |
| ratio 4-10x | 133 | 0.5822 | 0.4488 | 0.4887 | +0.093 | -0.040 | 0.0103 ± 0.0125 |
| ratio <2x | 366 | 0.5335 | 0.413 | 0.4617 | +0.072 | -0.049 | 0.0099 ± 0.0071 |
| ratio >=10x | 132 | 0.557 | 0.3936 | 0.4545 | +0.102 | -0.061 | 0.0204 ± 0.016 |
| thinner_sample 1000-3000 | 214 | 0.5395 | 0.4204 | 0.4579 | +0.082 | -0.037 | 0.0058 ± 0.0092 |
| thinner_sample 300-1000 | 238 | 0.5539 | 0.4278 | 0.4622 | +0.092 | -0.034 | 0.0094 ± 0.0092 |
| thinner_sample <300 | 266 | 0.5399 | 0.3796 | 0.4436 | +0.096 | -0.064 | 0.022 ± 0.0106 |
| thinner_sample >=3000 | 98 | 0.5145 | 0.4172 | 0.4388 | +0.076 | -0.021 | 0.016 ± 0.0113 |
| data_status ADEQUATE | 220 | 0.5244 | 0.4141 | 0.45 | +0.074 | -0.036 | 0.0077 ± 0.0085 |
| data_status LIMITED | 180 | 0.5592 | 0.4414 | 0.4944 | +0.065 | -0.053 | 0.0028 ± 0.0105 |
| data_status POOR | 416 | 0.5415 | 0.392 | 0.4351 | +0.106 | -0.043 | 0.021 ± 0.0079 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 135 | 0.1754 | 0.1763 | -0.0008 ± 0.0012 | 0.5233 | 0.5257 | 0.4959 | 0.4813 | 0.5037 | -0.089 ± 0.0396 | -0.01 (3) |
| 3-5 | 83 | 0.1682 | 0.1652 | +0.0031 ± 0.0037 | 0.5161 | 0.5045 | 0.5204 | 0.4794 | 0.4578 | -0.120 ± 0.0477 | 0.02 (1) |
| 5-10 | 173 | 0.198 | 0.2002 | -0.0022 ± 0.0051 | 0.5812 | 0.5856 | 0.5178 | 0.4431 | 0.4913 | -0.058 ± 0.0344 | -0.02 (2) |
| 10-15 | 139 | 0.2155 | 0.2086 | +0.0069 ± 0.0097 | 0.6142 | 0.5987 | 0.5283 | 0.4041 | 0.4388 | -0.076 ± 0.0382 | -0.0633 (3) |
| 15-25 | 176 | 0.2126 | 0.2112 | +0.0014 ± 0.0135 | 0.613 | 0.6031 | 0.5619 | 0.3657 | 0.4602 | -0.023 ± 0.0337 | -0.02 (4) |
| 25-40 | 87 | 0.242 | 0.1797 | +0.0623 ± 0.0282 | 0.6747 | 0.5304 | 0.6108 | 0.2961 | 0.3448 | -0.089 ± 0.043 | -0.01 (1) |
| 40+ | 23 | 0.3363 | 0.1395 | +0.1968 ± 0.0707 | 0.9094 | 0.4379 | 0.701 | 0.2565 | 0.2609 | -0.150 ± 0.0784 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 407 | 0.1659 | 0.167 | -0.0011 ± 0.0007 | 0.4979 | 0.5007 | 0.5078 | 0.4929 | 0.5356 | -0.022 ± 0.0214 | -0.0188 (8) |
| 3-5 | 253 | 0.1717 | 0.1699 | +0.0019 ± 0.0021 | 0.5236 | 0.5127 | 0.4974 | 0.4572 | 0.4545 | -0.063 ± 0.0267 | 0.02 (1) |
| 5-10 | 580 | 0.1834 | 0.1815 | +0.0019 ± 0.0026 | 0.547 | 0.5384 | 0.4725 | 0.3988 | 0.4259 | -0.034 ± 0.0178 | -0.0133 (6) |
| 10-15 | 469 | 0.1909 | 0.175 | +0.0159 ± 0.0048 | 0.5612 | 0.5136 | 0.4754 | 0.3515 | 0.3475 | -0.069 ± 0.0191 | -0.0633 (3) |
| 15-25 | 642 | 0.1914 | 0.1593 | +0.0321 ± 0.0063 | 0.5702 | 0.4717 | 0.48 | 0.2828 | 0.2975 | -0.045 ± 0.0155 | -0.017 (10) |
| 25-40 | 583 | 0.2141 | 0.096 | +0.1181 ± 0.0081 | 0.6207 | 0.3133 | 0.501 | 0.1858 | 0.1578 | -0.076 ± 0.0125 | -0.01 (1) |
| 40+ | 424 | 0.3673 | 0.0357 | +0.3316 ± 0.0099 | 0.9571 | 0.1521 | 0.6148 | 0.103 | 0.0448 | -0.088 ± 0.0085 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 82 | 0.1742 | 0.1765 | -0.0023 ± 0.0016 | 0.5217 | 0.5254 | 0.5205 | 0.5059 | 0.5854 | -0.015 ± 0.0449 | -0.01 (1) |
| 3-5 | 62 | 0.2111 | 0.211 | +0.0001 ± 0.0047 | 0.6018 | 0.6091 | 0.4947 | 0.4556 | 0.4677 | -0.064 ± 0.0619 | 0.02 (1) |
| 5-10 | 156 | 0.1862 | 0.1788 | +0.0074 ± 0.0052 | 0.5544 | 0.5351 | 0.5767 | 0.501 | 0.4808 | -0.131 ± 0.0341 | -0.01 (3) |
| 10-15 | 150 | 0.2165 | 0.2062 | +0.0103 ± 0.0094 | 0.6196 | 0.5979 | 0.5755 | 0.4508 | 0.48 | -0.072 ± 0.0381 | -0.0667 (3) |
| 15-25 | 194 | 0.2209 | 0.1963 | +0.0247 ± 0.0126 | 0.6266 | 0.567 | 0.5839 | 0.3869 | 0.4278 | -0.084 ± 0.0326 | -0.0167 (3) |
| 25-40 | 120 | 0.2554 | 0.1921 | +0.0633 ± 0.0246 | 0.7132 | 0.5586 | 0.654 | 0.3452 | 0.3917 | -0.106 ± 0.0409 | -0.025 (2) |
| 40+ | 52 | 0.3781 | 0.1949 | +0.1832 ± 0.0617 | 1.0423 | 0.5744 | 0.7455 | 0.2528 | 0.3269 | -0.042 ± 0.0601 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 325 | 0.1567 | 0.1585 | -0.0018 ± 0.0007 | 0.4735 | 0.4785 | 0.5527 | 0.538 | 0.5938 | +0.003 ± 0.0222 | -0.0217 (6) |
| 3-5 | 194 | 0.1745 | 0.1739 | +0.0006 ± 0.0024 | 0.5168 | 0.5222 | 0.5551 | 0.5157 | 0.5258 | -0.041 ± 0.0302 | 0.02 (1) |
| 5-10 | 517 | 0.1783 | 0.1747 | +0.0035 ± 0.0028 | 0.5328 | 0.5183 | 0.5205 | 0.445 | 0.4565 | -0.048 ± 0.0185 | -0.01 (4) |
| 10-15 | 503 | 0.1875 | 0.1751 | +0.0125 ± 0.0047 | 0.5568 | 0.5173 | 0.5173 | 0.3933 | 0.4135 | -0.039 ± 0.0189 | -0.0575 (4) |
| 15-25 | 651 | 0.2027 | 0.1564 | +0.0462 ± 0.0062 | 0.5915 | 0.4686 | 0.5095 | 0.3136 | 0.2995 | -0.084 ± 0.0155 | -0.0143 (7) |
| 25-40 | 624 | 0.2232 | 0.118 | +0.1052 ± 0.0087 | 0.6475 | 0.3654 | 0.542 | 0.2269 | 0.2196 | -0.065 ± 0.0139 | -0.015 (6) |
| 40+ | 544 | 0.4021 | 0.0624 | +0.3397 ± 0.0124 | 1.0554 | 0.2247 | 0.6613 | 0.1242 | 0.0901 | -0.067 ± 0.0103 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 129 | 0.1717 | 0.1737 | -0.0020 ± 0.0013 | 0.5121 | 0.5175 | 0.5154 | 0.501 | 0.5426 | -0.046 ± 0.037 | -0.01 (5) |
| 3-5 | 89 | 0.1694 | 0.1678 | +0.0017 ± 0.0035 | 0.5119 | 0.5077 | 0.5098 | 0.4703 | 0.4719 | -0.109 ± 0.0465 | -- (0) |
| 5-10 | 167 | 0.2033 | 0.2027 | +0.0006 ± 0.0052 | 0.5974 | 0.5895 | 0.5083 | 0.436 | 0.4671 | -0.067 ± 0.0351 | -0.01 (2) |
| 10-15 | 147 | 0.2099 | 0.2049 | +0.0050 ± 0.0093 | 0.6062 | 0.591 | 0.5498 | 0.426 | 0.4762 | -0.073 ± 0.0378 | -0.044 (5) |
| 15-25 | 170 | 0.2136 | 0.2056 | +0.0080 ± 0.0134 | 0.6196 | 0.5915 | 0.5755 | 0.3822 | 0.4588 | -0.042 ± 0.0334 | -0.03 (1) |
| 25-40 | 96 | 0.2381 | 0.1897 | +0.0484 ± 0.0276 | 0.6691 | 0.5569 | 0.6037 | 0.2904 | 0.3646 | -0.070 ± 0.0414 | 0.0 (1) |
| 40+ | 18 | 0.3586 | 0.1556 | +0.2030 ± 0.0855 | 0.9645 | 0.4759 | 0.7164 | 0.2647 | 0.2778 | -0.161 ± 0.0975 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 389 | 0.1653 | 0.1654 | -0.0001 ± 0.0007 | 0.4987 | 0.4996 | 0.5073 | 0.4927 | 0.5064 | -0.048 ± 0.0208 | -0.0162 (13) |
| 3-5 | 266 | 0.1804 | 0.1764 | +0.0040 ± 0.0021 | 0.5364 | 0.5248 | 0.4892 | 0.4501 | 0.4248 | -0.088 ± 0.0262 | -0.01 (2) |
| 5-10 | 573 | 0.1875 | 0.1827 | +0.0048 ± 0.0027 | 0.5577 | 0.5359 | 0.466 | 0.3923 | 0.3997 | -0.049 ± 0.018 | -0.01 (2) |
| 10-15 | 487 | 0.1904 | 0.174 | +0.0164 ± 0.0047 | 0.5638 | 0.5146 | 0.4887 | 0.3651 | 0.3614 | -0.070 ± 0.0189 | -0.03 (9) |
| 15-25 | 675 | 0.1841 | 0.1505 | +0.0336 ± 0.006 | 0.5558 | 0.4513 | 0.4867 | 0.2877 | 0.3037 | -0.042 ± 0.0146 | -0.03 (2) |
| 25-40 | 574 | 0.215 | 0.0971 | +0.1180 ± 0.0082 | 0.6232 | 0.3146 | 0.4964 | 0.1788 | 0.1533 | -0.077 ± 0.0125 | 0.0 (1) |
| 40+ | 394 | 0.3842 | 0.0356 | +0.3486 ± 0.0104 | 1.0043 | 0.1532 | 0.6204 | 0.1028 | 0.0355 | -0.097 ± 0.0088 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 414 | 0.2046 | 0.2047 | -0.0000 ± 0.0007 | 0.5918 | 0.5922 | 0.4988 | 0.4842 | 0.4855 | -0.042 ± 0.0223 | -0.0226 (46) |
| 3-5 | 296 | 0.1951 | 0.194 | +0.0011 ± 0.0021 | 0.572 | 0.5659 | 0.4657 | 0.4259 | 0.4358 | -0.040 ± 0.0254 | -0.0059 (32) |
| 5-10 | 630 | 0.1865 | 0.1812 | +0.0053 ± 0.0025 | 0.556 | 0.5417 | 0.459 | 0.3856 | 0.3873 | -0.044 ± 0.017 | -0.0049 (71) |
| 10-15 | 418 | 0.2037 | 0.1911 | +0.0126 ± 0.0054 | 0.597 | 0.5606 | 0.4583 | 0.3347 | 0.3445 | -0.042 ± 0.0213 | 0.0016 (63) |
| 15-25 | 564 | 0.2347 | 0.2092 | +0.0255 ± 0.0075 | 0.6627 | 0.6048 | 0.5292 | 0.3362 | 0.367 | -0.033 ± 0.0192 | -0.0216 (58) |
| 25-40 | 273 | 0.2696 | 0.17 | +0.0996 ± 0.0156 | 0.7445 | 0.5104 | 0.5765 | 0.2652 | 0.2601 | -0.070 ± 0.0246 | -0.0216 (25) |
| 40+ | 93 | 0.4235 | 0.1616 | +0.2619 ± 0.0447 | 1.192 | 0.4964 | 0.7363 | 0.2277 | 0.2473 | -0.056 ± 0.0433 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 762 | 0.1943 | 0.1938 | +0.0005 ± 0.0005 | 0.567 | 0.5654 | 0.4956 | 0.4811 | 0.4698 | -0.052 ± 0.0159 | -0.0155 (82) |
| 3-5 | 537 | 0.1987 | 0.1969 | +0.0017 ± 0.0016 | 0.5777 | 0.5706 | 0.4707 | 0.4309 | 0.4302 | -0.046 ± 0.0192 | -0.018 (54) |
| 5-10 | 1145 | 0.1854 | 0.1786 | +0.0068 ± 0.0019 | 0.5535 | 0.5331 | 0.4435 | 0.3695 | 0.3642 | -0.047 ± 0.0126 | -0.0089 (121) |
| 10-15 | 844 | 0.1977 | 0.1832 | +0.0145 ± 0.0037 | 0.5819 | 0.5399 | 0.4503 | 0.3267 | 0.3294 | -0.043 ± 0.0146 | -0.0053 (99) |
| 15-25 | 1179 | 0.2221 | 0.1873 | +0.0348 ± 0.005 | 0.6399 | 0.5496 | 0.5034 | 0.308 | 0.3164 | -0.043 ± 0.0126 | -0.0255 (106) |
| 25-40 | 813 | 0.2454 | 0.1295 | +0.1159 ± 0.008 | 0.6924 | 0.4041 | 0.5293 | 0.2142 | 0.1894 | -0.071 ± 0.0125 | -0.0206 (47) |
| 40+ | 482 | 0.3893 | 0.08 | +0.3093 ± 0.0141 | 1.0649 | 0.2682 | 0.6537 | 0.1374 | 0.1079 | -0.073 ± 0.0131 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 816 | 1.134 ± 0.1 | 1.227 | 0.1723 | 0.1854 | 0.206 | 0.1926 |
| gen2 | 816 | 0.95 ± 0.088 | 1.166 | 0.1892 | 0.1845 | 0.2231 | 0.1932 |
| gen1_elo | 816 | 1.104 ± 0.098 | 1.215 | 0.1772 | 0.1858 | 0.2055 | 0.1927 |
| gen1_sr | 816 | 1.16 ± 0.115 | 1.213 | 0.145 | 0.1869 | 0.2197 | 0.1926 |
| gen1_ledger | 2688 | 0.884 ± 0.052 | 1.056 | 0.1628 | 0.2 | 0.2197 | 0.1918 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 4,627)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,518 | 32.8% |
| STALE_QUOTE | market_freshness | 1,386 | 29.9% |
| POOR_DATA | data | 371 | 8.0% |
| BOOK_QUALITY | execution | 302 | 6.5% |
| LIMITED_DATA | data | 289 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 271 | 5.9% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 235 | 5.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 161 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 91 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 32.8%, market_freshness 29.9%, data 14.3%, market_freshness/coverage 9.3%, execution 6.5%, model_calibration_or_unknown 5.1%, mapping 2.0%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 64.4%, STALE_KALSHI_QUOTE 62.8%, STALE_PLAYER_DATA 54.9%, THIN_PLAYER_HISTORY 52.1%, MODEL_INTERNAL_DISAGREEMENT 32.8%, ASYMMETRIC_SAMPLE_SIZE 28.2%, WIDE_SPREAD 14.9%, MODEL_HIGH_UNCERTAINTY 13.0%, PLAYER_IDENTITY_RISK 11.0%, LEVEL_TRANSFER_RISK 8.5%, EVENT_MAPPING_RISK 6.9%, LOW_DISPLAYED_LIQUIDITY 4.8%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.8%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 35.4%, POST_SETTLEMENT_OBSERVATION 32.8%, POSSIBLE_IN_PLAY_QUOTE 6.7%, CONFIRMED_IN_PLAY_QUOTE 1.3%

### >= ge_25 pp (N = 2,538)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,176 | 46.3% |
| STALE_QUOTE | market_freshness | 620 | 24.4% |
| POOR_DATA | data | 162 | 6.4% |
| BOOK_QUALITY | execution | 147 | 5.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 138 | 5.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 96 | 3.8% |
| LIMITED_DATA | data | 80 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 65 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 54 | 2.1% |

Cause class: coverage 46.3%, market_freshness 24.4%, data 9.5%, market_freshness/coverage 9.2%, execution 5.8%, mapping 2.6%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.6%, STALE_KALSHI_QUOTE 69.9%, LOW_DATA_QUALITY 68.2%, THIN_PLAYER_HISTORY 54.6%, STALE_PLAYER_DATA 52.8%, MODEL_INTERNAL_DISAGREEMENT 33.5%, ASYMMETRIC_SAMPLE_SIZE 30.5%, MODEL_HIGH_UNCERTAINTY 14.1%, PLAYER_IDENTITY_RISK 13.6%, WIDE_SPREAD 13.5%, EVENT_MAPPING_RISK 8.4%, LEVEL_TRANSFER_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 5.3%, MODEL_CALIBRATION_OUTLIER 3.2%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 49.1%, POST_SETTLEMENT_OBSERVATION 46.3%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 1.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2161, "IDENTITY_AMBIGUOUS": 377}; ticker orientation: {"VERIFIED": 2538}.

Checks: discipline:AMBIGUOUS 182, discipline:PASS 2356, identity_confidence:AMBIGUOUS 345, identity_confidence:PASS 2193, level_mapping:NA 194, level_mapping:PASS 2344, market_pair:AMBIGUOUS 62, market_pair:NA 74, market_pair:PASS 2402, model_complement:NA 45, model_complement:PASS 2493, namesake:PASS 2538, physical_match_id:NA 1326, physical_match_id:PASS 1212, player_ids:PASS 2538, same_pair_other_event:PASS 2538, ticker_orientation:PASS 2538

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 312 | 3.9% | 4.0% | 0.5% | {"market_freshness": 12} | 6.13 | 0.181 / 0.1824 (47) | 39.1% | 0.0% | 0.6% | 3.5% |
| CHALLENGER | 1,612 | 18.7% | 8.5% | 11.9% | {"coverage": 157, "market_freshness": 73, "market_freshness/coverage": 37, "data": 17, "model_calibration_or_unknown": 14, "execution": 3} | 7.74 | 0.2246 / 0.207 (523) | 52.7% | 4.1% | 0.7% | 21.9% |
| DOUBLES | 373 | 48.8% | 48.7% | 7.2% | {"market_freshness": 106, "execution": 32, "mapping": 27, "market_freshness/coverage": 11, "coverage": 6} | 24.15 | 0.3289 / 0.2278 (156) | 60.9% | 0.0% | 100.0% | 9.1% |
| ITF_MEN | 3,518 | 25.0% | 14.0% | 34.6% | {"coverage": 472, "market_freshness": 167, "data": 87, "execution": 71, "market_freshness/coverage": 70, "mapping": 10, "model_calibration_or_unknown": 1} | 9.78 | 0.2131 / 0.1867 (1268) | 55.4% | 49.8% | 5.4% | 31.6% |
| ITF_WOMEN | 3,482 | 29.0% | 17.3% | 39.8% | {"coverage": 528, "market_freshness": 216, "data": 119, "market_freshness/coverage": 76, "execution": 32, "mapping": 26, "model_calibration_or_unknown": 13} | 12.22 | 0.2053 / 0.1854 (1126) | 58.4% | 54.1% | 6.3% | 32.6% |
| OTHER | 149 | 8.1% | 7.3% | 0.5% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 796 | 9.3% | 8.0% | 2.9% | {"market_freshness": 33, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.63 | 0.2006 / 0.1964 (129) | 40.3% | 2.6% | 1.5% | 3.8% |
| WTA125 | 421 | 16.4% | 9.1% | 2.7% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 11, "data": 8, "coverage": 8} | 10.39 | 0.2259 / 0.2023 (213) | 34.4% | 9.0% | 0.5% | 19.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 5 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 6 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 7 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 8 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 9 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 10 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 11 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 12 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 13 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
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
| 24 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 25 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 26 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 27 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 28 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 29 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 30 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 31 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 32 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 34 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 407 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 35 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 36 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 38 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 40 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 18.1h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 1101 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 41 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 42 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 43 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 44 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 45 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 819 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 46 | `KXITFWMATCH-26OCT01TANVED-TAN` | ITF_WOMEN | fair_v1 | 76% / 8% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 8.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 492 min (STALE); no external reference |
| 47 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26SEP24BOUKUR-BOU` | ITF_WOMEN | gen1_ledger | 76% / 8% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 1497.0, ratio 2.48); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26SEP28TABSAN-SAN` | CHALLENGER | gen1_ledger | 70% / 4% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 48 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9661, "by_level_share_of_ge_25pp": {"ATP": 0.0047, "CHALLENGER": 0.1186, "DOUBLES": 0.0717, "ITF_MEN": 0.3459, "ITF_WOMEN": 0.398, "OTHER": 0.0047, "WTA": 0.0292, "WTA125": 0.0272}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6986, "share_primary_cause_market_settled_or_in_play": 0.5556, "share_primary_cause_stale_quote_only": 0.2443}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2538, "identity_ambiguous_share": 0.1485, "ticker_orientation": {"VERIFIED": 2538}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1212, "with_external": 6, "coverage": 0.005, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 482, "with_external": 6, "coverage": 0.0124, "external_status": {"EXTERNAL_STALE": 6}, "triangulation": {"INSUFFICIENT_INPUTS": 6}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 804.0, "median_sample_ratio": 2.27, "median_min_matches": 26.0, "median_max_days_since_last": 172.0, "share_severe_asymmetry": 0.1659, "data_status": {"POOR": 1183, "LIMITED": 872, "ADEQUATE": 483}, "comparison_lt_10pp": {"median_thinner_serve_points": 1970.0, "median_sample_ratio": 1.7, "median_min_matches": 79.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 185, "model_minus_observed": 0.1088, "kalshi_minus_observed": -0.0225, "brier_diff_model_minus_kalshi": 0.0175}, "4-10x": {"n": 133, "model_minus_observed": 0.0934, "kalshi_minus_observed": -0.04, "brier_diff_model_minus_kalshi": 0.0103}, "<2x": {"n": 366, "model_minus_observed": 0.0717, "kalshi_minus_observed": -0.0488, "brier_diff_model_minus_kalshi": 0.0099}, ">=10x": {"n": 132, "model_minus_observed": 0.1024, "kalshi_minus_observed": -0.061, "brier_diff_model_minus_kalshi": 0.0204}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 816, "model": {"intercept": -0.64, "slope": 0.95, "slope_se": 0.088}, "kalshi_mid_same_rows": {"intercept": 0.205, "slope": 1.166, "slope_se": 0.097}, "mean_extremity_model": 0.1892, "mean_extremity_kalshi": 0.1845, "model_brier": 0.2231, "kalshi_brier": 0.1932, "brier_diff_model_minus_kalshi": 0.03, "brier_diff_se": 0.0066, "model_logloss": 0.6383, "kalshi_logloss": 0.5648}, "fair_v1": {"n": 816, "model": {"intercept": -0.451, "slope": 1.134, "slope_se": 0.1}, "kalshi_mid_same_rows": {"intercept": 0.308, "slope": 1.227, "slope_se": 0.101}, "mean_extremity_model": 0.1723, "mean_extremity_kalshi": 0.1854, "model_brier": 0.206, "kalshi_brier": 0.1926, "brier_diff_model_minus_kalshi": 0.0134, "brier_diff_se": 0.0052, "model_logloss": 0.5967, "kalshi_logloss": 0.5634}, "gen1_elo": {"n": 816, "model": {"intercept": -0.423, "slope": 1.104, "slope_se": 0.098}, "kalshi_mid_same_rows": {"intercept": 0.319, "slope": 1.215, "slope_se": 0.099}, "mean_extremity_model": 0.1772, "mean_extremity_kalshi": 0.1858, "model_brier": 0.2055, "kalshi_brier": 0.1927, "brier_diff_model_minus_kalshi": 0.0127, "brier_diff_se": 0.0052, "model_logloss": 0.5973, "kalshi_logloss": 0.5635}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.257, "share_ge_15": 0.4434, "median_abs_gap": 12.95, "n": 4716}, "gen1_elo": {"share_ge_25": 0.2496, "share_ge_15": 0.4309, "median_abs_gap": 12.48, "n": 4716}, "gen1_sr": {"share_ge_25": 0.3085, "share_ge_15": 0.5318, "median_abs_gap": 16.29, "n": 4716}, "gen2": {"share_ge_25": 0.3081, "share_ge_15": 0.5049, "median_abs_gap": 15.29, "n": 4716}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1409, "share_ge_15": 0.3315, "median_abs_gap": 9.95, "n": 3421}, "gen1_elo": {"share_ge_25": 0.1403, "share_ge_15": 0.3134, "median_abs_gap": 9.53, "n": 3421}, "gen1_sr": {"share_ge_25": 0.1967, "share_ge_15": 0.435, "median_abs_gap": 12.68, "n": 3421}, "gen2": {"share_ge_25": 0.2108, "share_ge_15": 0.4221, "median_abs_gap": 12.76, "n": 3421}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.13, "share_ge_25_all": 0.0385, "share_ge_25_pregame_clean": 0.0399}, "WTA": {"median_abs_gap_pregame_clean": 8.63, "share_ge_25_all": 0.093, "share_ge_25_pregame_clean": 0.0796}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.224, "share_within_10pp_all": 0.4191, "share_within_10pp_pregame_clean": 0.4996, "corr_model_vs_mid_pregame_clean": 0.8281}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 135, "model_brier": 0.1754, "kalshi_brier": 0.1763, "brier_diff_model_minus_kalshi": -0.0008}, "10-15": {"n_settled": 139, "model_brier": 0.2155, "kalshi_brier": 0.2086, "brier_diff_model_minus_kalshi": 0.0069}, "15-25": {"n_settled": 176, "model_brier": 0.2126, "kalshi_brier": 0.2112, "brier_diff_model_minus_kalshi": 0.0014}, "25-40": {"n_settled": 87, "model_brier": 0.242, "kalshi_brier": 0.1797, "brier_diff_model_minus_kalshi": 0.0623}, "3-5": {"n_settled": 83, "model_brier": 0.1682, "kalshi_brier": 0.1652, "brier_diff_model_minus_kalshi": 0.0031}, "40+": {"n_settled": 23, "model_brier": 0.3363, "kalshi_brier": 0.1395, "brier_diff_model_minus_kalshi": 0.1968}, "5-10": {"n_settled": 173, "model_brier": 0.198, "kalshi_brier": 0.2002, "brier_diff_model_minus_kalshi": -0.0022}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.574, "slope": 0.884, "slope_se": 0.052}, "kalshi_slope": {"intercept": 0.076, "slope": 1.056, "slope_se": 0.053}, "n": 2688}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 156, "model_brier": 0.3289, "kalshi_brier": 0.2278, "brier_diff_model_minus_kalshi": 0.101, "brier_diff_se": 0.0265, "corr_model_outcome": -0.0853, "corr_kalshi_outcome": 0.3248}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
