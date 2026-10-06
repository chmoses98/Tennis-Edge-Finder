# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-06T00:29Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 15,552): 0-3 13.0%, 3-5 9.2%, 5-10 19.1%, 10-15 15.1%, 15-25 19.1%, 25-40 15.1%, 40+ 9.4%; median gap 12.71 pp.
* **Where the extremes live**: 97.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.3%, Challenger 14.5%, doubles 5.0%). Main tour: ATP 3.2% and WTA 9.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 3,809): MARKET_ALREADY_SETTLED_WHEN_PRICED 43.5%, STALE_QUOTE 22.5%, BOOK_QUALITY 12.4%, POOR_DATA 6.3%, POSSIBLY_IN_PLAY_QUOTE 4.8%, IN_PLAY_QUOTE 3.1%, IDENTITY_AMBIGUOUS 2.6%, LIMITED_DATA 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 43.5%, market_freshness 22.5%, execution 12.4%, data 8.9%, market_freshness/coverage 7.9%, mapping 2.6%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 65.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 51.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 3,809 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 6.5% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 626.0 points vs 1869.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.135, Gen-2 0.93, Gen-1 ledger 0.911 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 131 model 0.2261 vs Kalshi 0.1818; n 30 model 0.3354 vs Kalshi 0.1357.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 54,717 model-market comparisons (93,400 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 22,415 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-06T00:24:13.933027+00:00'], shadow board 15,616 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-06T00:24:17.122370+00:00'], Model 4 4,920 rows, 8,740 settled tickers, 2,050 tickers with an external scan.
* By model: {"gen1_ledger": 13738, "gen1_elo": 7845, "fair_v1": 7845, "gen2": 7845, "gen1_sr": 7845, "model4_fundamental": 4804, "model4_conditioned": 4795}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 15,552 | 13.0 | 9.2 | 19.1 | 15.1 | 19.1 | 15.1 | 9.4 | 12.71 | 43.6% | 24.5% |
| MW fair_v1 | 7,845 | 12.7 | 8.9 | 17.8 | 15.3 | 18.2 | 15.9 | 11.1 | 13.27 | 45.2% | 27.0% |
| MW gen1_elo | 7,845 | 12.6 | 8.6 | 19.7 | 14.4 | 18.8 | 15.5 | 10.4 | 12.9 | 44.7% | 25.9% |
| MW gen1_ledger | 7,707 | 13.3 | 9.6 | 20.3 | 14.8 | 20.1 | 14.3 | 7.6 | 12.04 | 42.0% | 21.9% |
| MW gen1_sr | 7,845 | 9.6 | 7.4 | 16.0 | 13.8 | 21.7 | 18.9 | 12.7 | 16.3 | 53.3% | 31.6% |
| MW gen2 | 7,845 | 10.9 | 6.8 | 16.1 | 14.0 | 20.1 | 17.6 | 14.3 | 15.86 | 52.1% | 32.0% |
| all families model4_conditioned | 4,795 | 21.0 | 18.9 | 31.3 | 18.3 | 7.7 | 1.5 | 1.3 | 6.29 | 10.5% | 2.8% |
| all families model4_fundamental | 4,804 | 15.8 | 12.4 | 31.5 | 20.4 | 13.0 | 4.9 | 1.9 | 8.18 | 19.9% | 6.9% |

Configurable thresholds (primary): >=5pp 77.8%, >=10pp 58.7%, >=15pp 43.6%, >=20pp 33.3%, >=25pp 24.5%, >=30pp 18.1%, >=40pp 9.4%, >=50pp 4.1%
Executable gap (model outside the book, before fees): median 9.31pp; >=10pp 48.0%, >=25pp 20.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 490 | 22.4 | 19.0 | 24.9 | 15.3 | 13.7 | 2.5 | 2.2 | 6.03 | 18.4% | 4.7% |
| CHALLENGER | 1,614 | 14.6 | 10.5 | 16.9 | 15.5 | 14.6 | 14.1 | 13.9 | 12.89 | 42.6% | 28.0% |
| ITF_MEN | 2,187 | 11.2 | 8.4 | 18.7 | 14.3 | 17.9 | 16.4 | 13.1 | 13.74 | 47.4% | 29.5% |
| ITF_WOMEN | 2,915 | 9.4 | 6.6 | 15.3 | 15.5 | 21.4 | 20.5 | 11.3 | 16.45 | 53.2% | 31.8% |
| WTA | 465 | 22.6 | 10.1 | 24.9 | 14.0 | 18.9 | 7.1 | 2.4 | 8.36 | 28.4% | 9.5% |
| WTA125 | 174 | 14.9 | 7.5 | 20.1 | 27.0 | 13.8 | 12.1 | 4.6 | 11.0 | 30.5% | 16.7% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 490 | 19.0 | 15.9 | 26.1 | 15.9 | 16.1 | 4.3 | 2.6 | 7.3 | 23.1% | 6.9% |
| CHALLENGER | 1,614 | 13.6 | 6.3 | 18.0 | 13.9 | 18.6 | 16.2 | 13.4 | 14.4 | 48.3% | 29.6% |
| ITF_MEN | 2,187 | 9.1 | 6.9 | 16.8 | 15.3 | 19.3 | 17.8 | 14.9 | 15.66 | 52.0% | 32.7% |
| ITF_WOMEN | 2,915 | 8.3 | 6.1 | 12.8 | 11.9 | 21.7 | 20.6 | 18.5 | 19.67 | 60.8% | 39.1% |
| WTA | 465 | 20.2 | 5.4 | 16.6 | 15.7 | 21.9 | 17.9 | 2.4 | 13.18 | 42.1% | 20.2% |
| WTA125 | 174 | 6.3 | 2.9 | 17.8 | 21.8 | 23.0 | 16.1 | 12.1 | 15.57 | 51.1% | 28.2% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 490 | 25.5 | 12.2 | 29.8 | 14.9 | 9.0 | 6.1 | 2.5 | 7.4 | 17.5% | 8.6% |
| CHALLENGER | 1,614 | 15.6 | 9.8 | 21.2 | 12.9 | 13.4 | 13.1 | 14.0 | 11.11 | 40.5% | 27.1% |
| ITF_MEN | 2,187 | 9.5 | 9.0 | 18.0 | 14.5 | 19.7 | 16.3 | 13.0 | 14.23 | 49.0% | 29.3% |
| ITF_WOMEN | 2,915 | 9.2 | 6.2 | 16.0 | 14.7 | 23.8 | 20.3 | 9.8 | 16.99 | 53.9% | 30.1% |
| WTA | 465 | 21.9 | 14.0 | 32.3 | 15.5 | 10.8 | 4.1 | 1.5 | 7.0 | 16.3% | 5.6% |
| WTA125 | 174 | 21.3 | 6.9 | 24.7 | 20.1 | 20.7 | 5.2 | 1.1 | 8.06 | 27.0% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 237 | 27.4 | 21.1 | 38.0 | 11.4 | 2.1 | 0.0 | 0.0 | 5.37 | 2.1% | 0.0% |
| CHALLENGER | 1,086 | 20.5 | 15.1 | 26.2 | 15.1 | 13.7 | 6.7 | 2.6 | 7.35 | 23.0% | 9.3% |
| DOUBLES | 421 | 5.2 | 3.6 | 11.6 | 11.2 | 23.0 | 20.4 | 24.9 | 23.51 | 68.4% | 45.4% |
| ITF_MEN | 2,441 | 13.6 | 8.6 | 18.7 | 14.7 | 20.7 | 14.4 | 9.3 | 12.74 | 44.5% | 23.7% |
| ITF_WOMEN | 2,601 | 9.0 | 8.0 | 17.2 | 14.2 | 24.0 | 19.8 | 7.8 | 15.66 | 51.6% | 27.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 393 | 18.1 | 8.7 | 26.2 | 20.9 | 17.3 | 8.1 | 0.8 | 9.3 | 26.2% | 8.9% |
| WTA125 | 379 | 14.0 | 10.0 | 21.6 | 19.3 | 20.8 | 10.8 | 3.4 | 10.81 | 35.1% | 14.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 489 | 22.3 | 19.0 | 24.9 | 15.3 | 13.7 | 2.5 | 2.2 | 6.04 | 18.4% | 4.7% |
| CHALLENGER | 1,124 | 18.9 | 13.2 | 21.5 | 18.3 | 16.2 | 8.0 | 3.8 | 9.04 | 28.0% | 11.8% |
| ITF_MEN | 1,498 | 14.0 | 11.2 | 22.6 | 15.6 | 18.3 | 12.4 | 5.9 | 10.47 | 36.6% | 18.3% |
| ITF_WOMEN | 2,053 | 11.9 | 8.5 | 18.1 | 17.7 | 23.1 | 16.5 | 4.2 | 13.3 | 43.8% | 20.8% |
| WTA | 464 | 22.6 | 10.1 | 25.0 | 14.0 | 19.0 | 6.9 | 2.4 | 8.36 | 28.2% | 9.3% |
| WTA125 | 168 | 15.5 | 7.7 | 20.8 | 28.0 | 13.7 | 11.3 | 3.0 | 10.7 | 28.0% | 14.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 489 | 19.0 | 15.8 | 26.2 | 15.9 | 16.2 | 4.3 | 2.7 | 7.4 | 23.1% | 7.0% |
| CHALLENGER | 1,124 | 17.6 | 8.1 | 22.6 | 17.5 | 19.6 | 11.3 | 3.3 | 10.32 | 34.2% | 14.6% |
| ITF_MEN | 1,498 | 11.7 | 8.3 | 20.0 | 17.6 | 20.3 | 14.3 | 7.8 | 12.55 | 42.5% | 22.2% |
| ITF_WOMEN | 2,053 | 10.2 | 7.5 | 14.4 | 12.0 | 24.5 | 19.1 | 12.4 | 17.12 | 56.0% | 31.5% |
| WTA | 464 | 20.3 | 5.4 | 16.6 | 15.7 | 22.0 | 17.7 | 2.4 | 13.18 | 42.0% | 20.0% |
| WTA125 | 168 | 6.5 | 3.0 | 17.9 | 22.6 | 23.8 | 16.7 | 9.5 | 15.09 | 50.0% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 227 | 27.8 | 22.0 | 38.3 | 11.4 | 0.4 | 0.0 | 0.0 | 5.22 | 0.4% | 0.0% |
| CHALLENGER | 888 | 22.6 | 17.4 | 29.2 | 14.8 | 13.3 | 2.6 | 0.1 | 6.68 | 16.0% | 2.7% |
| DOUBLES | 381 | 5.2 | 3.4 | 11.8 | 11.3 | 23.1 | 20.7 | 24.4 | 23.51 | 68.2% | 45.1% |
| ITF_MEN | 1,826 | 16.1 | 10.0 | 21.3 | 15.9 | 20.8 | 11.5 | 4.5 | 11.04 | 36.8% | 16.0% |
| ITF_WOMEN | 1,922 | 10.4 | 9.2 | 19.8 | 15.7 | 24.8 | 17.6 | 2.6 | 13.09 | 45.0% | 20.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 364 | 18.4 | 9.1 | 26.9 | 21.4 | 17.9 | 6.3 | 0.0 | 9.13 | 24.2% | 6.3% |
| WTA125 | 300 | 16.3 | 11.0 | 25.3 | 22.7 | 19.0 | 5.3 | 0.3 | 9.32 | 24.7% | 5.7% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 421 | 5.2 | 3.6 | 11.6 | 11.2 | 23.0 | 20.4 | 24.9 | 23.51 | 68.4% | 45.4% |
| singles | 7,286 | 13.8 | 9.9 | 20.8 | 15.0 | 19.9 | 14.0 | 6.6 | 11.67 | 40.5% | 20.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,784 | 13.8 | 9.1 | 17.5 | 15.4 | 16.6 | 14.6 | 12.9 | 12.95 | 44.1% | 27.5% |
| Hard | 5,404 | 12.4 | 9.1 | 18.4 | 15.1 | 18.9 | 15.8 | 10.3 | 13.24 | 45.0% | 26.1% |
| UNKNOWN | 657 | 11.7 | 6.8 | 14.3 | 17.1 | 17.1 | 20.2 | 12.8 | 15.19 | 50.1% | 33.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,336 | 16.9 | 11.1 | 19.6 | 15.8 | 15.8 | 11.1 | 9.6 | 10.65 | 36.6% | 20.8% |
| B | 1,077 | 15.8 | 10.6 | 18.9 | 17.6 | 16.3 | 10.2 | 10.7 | 11.01 | 37.2% | 20.9% |
| C | 1,166 | 12.9 | 10.3 | 20.3 | 13.8 | 16.3 | 15.9 | 10.5 | 12.63 | 42.6% | 26.3% |
| D | 1,402 | 10.6 | 8.0 | 16.6 | 14.9 | 22.5 | 16.1 | 11.3 | 14.98 | 49.9% | 27.4% |
| F | 1,864 | 7.0 | 5.0 | 14.4 | 14.7 | 20.3 | 25.1 | 13.5 | 19.43 | 58.9% | 38.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,297 | 19.6 | 13.0 | 26.7 | 16.6 | 14.9 | 6.5 | 2.7 | 7.99 | 24.1% | 9.2% |
| B | 1,170 | 13.4 | 9.3 | 22.3 | 16.1 | 19.8 | 12.0 | 7.1 | 11.5 | 38.9% | 19.1% |
| C | 1,490 | 11.2 | 8.3 | 16.6 | 14.3 | 22.9 | 15.2 | 11.5 | 14.85 | 49.7% | 26.7% |
| D | 1,204 | 11.1 | 8.0 | 20.9 | 12.5 | 23.4 | 16.7 | 7.3 | 13.74 | 47.4% | 24.0% |
| F | 1,546 | 7.8 | 7.1 | 12.3 | 13.4 | 22.6 | 25.1 | 11.6 | 18.7 | 59.3% | 36.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 2,820 | 16.3 | 10.3 | 18.9 | 16.4 | 16.1 | 11.3 | 10.8 | 11.23 | 38.1% | 22.1% |
| LIMITED | 1,736 | 14.5 | 11.7 | 21.0 | 14.6 | 15.7 | 13.5 | 9.0 | 11.02 | 38.2% | 22.5% |
| POOR | 3,289 | 8.6 | 6.2 | 15.3 | 14.8 | 21.4 | 21.1 | 12.5 | 17.32 | 55.1% | 33.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 989 | 31.4 | 26.0 | 35.8 | 5.0 | 1.5 | 0.3 | 0.0 | 4.37 | 1.8% | 0.3% |
| GAME_SPREAD | 870 | 22.5 | 16.2 | 36.1 | 18.4 | 5.9 | 0.6 | 0.3 | 6.15 | 6.8% | 0.9% |
| MATCH_WINNER | 7,707 | 13.3 | 9.6 | 20.3 | 14.8 | 20.1 | 14.3 | 7.6 | 12.04 | 42.0% | 21.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 2,470 | 27.0 | 16.5 | 31.1 | 13.5 | 9.5 | 1.9 | 0.5 | 5.74 | 11.8% | 2.4% |
| TOTAL_GAMES | 1,678 | 8.8 | 9.4 | 32.7 | 26.0 | 14.2 | 5.4 | 3.5 | 9.76 | 23.1% | 8.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,736 | 27.1 | 36.2 | 24.6 | 0.4 | 10.3 | 1.0 | 0.3 | 4.29 | 11.6% | 1.3% |
| GAME_SPREAD | 1,089 | 41.4 | 14.7 | 28.0 | 12.9 | 1.5 | 1.1 | 0.4 | 4.0 | 2.9% | 1.5% |
| TOTAL_GAMES | 1,970 | 4.3 | 6.0 | 39.0 | 37.0 | 8.8 | 2.2 | 2.6 | 10.07 | 13.7% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,736 | 25.5 | 17.2 | 32.7 | 9.3 | 9.5 | 5.0 | 0.9 | 5.79 | 15.3% | 5.8% |
| GAME_SPREAD | 1,089 | 18.1 | 11.9 | 27.2 | 23.4 | 13.4 | 4.6 | 1.4 | 8.81 | 19.4% | 6.0% |
| TOTAL_GAMES | 1,979 | 6.1 | 8.5 | 32.8 | 28.4 | 15.8 | 5.1 | 3.2 | 10.39 | 24.1% | 8.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7,845 | 45.2% | 27.0% | 13.27 | 35.0% | 15.9% | 10.54 |
| gen1_elo | 7,845 | 44.7% | 25.9% | 12.9 | 34.1% | 15.5% | 10.04 |
| gen1_sr | 7,845 | 53.3% | 31.6% | 16.3 | 44.0% | 20.5% | 13.18 |
| gen2 | 7,845 | 52.1% | 32.0% | 15.86 | 44.2% | 22.7% | 12.98 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,177 | 15.7 | 12.5 | 21.6 | 15.8 | 18.6 | 11.8 | 3.9 | 10.02 | 34.3% | 15.7% |
| STALE | 4,668 | 10.6 | 6.5 | 15.2 | 15.0 | 18.0 | 18.7 | 16.0 | 16.51 | 52.7% | 34.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 1,175 | 14.6 | 9.5 | 23.5 | 15.1 | 17.9 | 15.5 | 3.9 | 10.43 | 37.3% | 19.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 15,552 | 1175 | 6649 | 7728 | 29.6 | 211.8 | 1400.4 |
| ge_15pp | 6,787 | 438 | 2380 | 3969 | 34.6 | 457.8 | 1380.4 |
| ge_25pp | 3,809 | 228 | 1090 | 2491 | 48.3 | 562.8 | 1380.4 |
| lt_10pp | 6,421 | 560 | 3216 | 2645 | 27.6 | 55.8 | 1201.9 |

Current slate `SL-20261006T002937Z-e0e35b29`: 1089 priced rows, quote age at build {'median': 6.1, 'max': 6.1}, freshness {'FRESH': 1089}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 207 | 20.3 | 10.6 | 24.1 | 20.3 | 16.9 | 7.2 | 0.5 | 8.01 | 24.6% | 7.7% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 15 | 0.0 | 6.7 | 20.0 | 40.0 | 33.3 | 0.0 | 0.0 | 13.33 | 33.3% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 7,845 | 231 (2.9%) | 6.5% | 0.0% | {"EXTERNAL_STALE": 207, "AGREES_WITH_KALSHI": 15, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 3,550 | 56 (1.6%) | 8.9% | 0.0% | {"EXTERNAL_STALE": 51, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 2,119 | 16 (0.8%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 16} |
| fair_v1_ge_25pp_pregame_clean | 923 | 16 (1.7%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 16} |
| fair_v1_lt_10pp | 3,092 | 127 (4.1%) | 3.1% | 0.0% | {"EXTERNAL_STALE": 114, "ALL_AGREE": 8, "AGREES_WITH_KALSHI": 4, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,571 | 11.3 | 8.3 | 20.0 | 15.3 | 20.2 | 15.0 | 9.7 | 13.06 | 45.0% | 24.8% |
| 4-10x | 1,101 | 12.0 | 10.8 | 17.5 | 14.3 | 17.5 | 17.9 | 9.9 | 13.37 | 45.3% | 27.8% |
| <2x | 4,198 | 14.2 | 9.5 | 18.0 | 15.7 | 17.5 | 14.0 | 11.2 | 12.71 | 42.7% | 25.2% |
| >=10x | 975 | 9.2 | 5.0 | 14.2 | 15.0 | 19.2 | 23.3 | 14.2 | 18.24 | 56.6% | 37.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 2,039 | 13.6 | 9.0 | 19.9 | 15.8 | 16.6 | 12.7 | 12.4 | 12.14 | 41.7% | 25.1% |
| 300-1000 | 1,821 | 12.5 | 9.1 | 16.7 | 15.2 | 20.5 | 16.1 | 9.8 | 13.73 | 46.5% | 26.0% |
| <300 | 2,163 | 7.8 | 5.8 | 14.5 | 14.4 | 20.6 | 23.4 | 13.6 | 18.52 | 57.5% | 36.9% |
| >=3000 | 1,822 | 17.7 | 12.2 | 20.7 | 16.0 | 15.0 | 10.4 | 8.0 | 9.97 | 33.4% | 18.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 252 | 0.5211 | 0.3899 | 0.4286 | +0.093 | -0.039 | 0.0081 ± 0.0089 |
| ratio 4-10x | 174 | 0.5757 | 0.4383 | 0.4828 | +0.093 | -0.044 | 0.0141 ± 0.0112 |
| ratio <2x | 509 | 0.5361 | 0.4121 | 0.4656 | +0.070 | -0.053 | 0.0124 ± 0.0063 |
| ratio >=10x | 174 | 0.5525 | 0.3805 | 0.4655 | +0.087 | -0.085 | 0.012 ± 0.0142 |
| thinner_sample 1000-3000 | 294 | 0.5409 | 0.4211 | 0.4524 | +0.089 | -0.031 | 0.01 ± 0.0081 |
| thinner_sample 300-1000 | 299 | 0.5575 | 0.425 | 0.4783 | +0.079 | -0.053 | 0.0055 ± 0.0084 |
| thinner_sample <300 | 367 | 0.5384 | 0.3735 | 0.455 | +0.083 | -0.082 | 0.0165 ± 0.0091 |
| thinner_sample >=3000 | 149 | 0.5182 | 0.4197 | 0.4497 | +0.069 | -0.030 | 0.0151 ± 0.0092 |
| data_status ADEQUATE | 323 | 0.529 | 0.4205 | 0.4489 | +0.080 | -0.028 | 0.0087 ± 0.007 |
| data_status LIMITED | 227 | 0.5552 | 0.4291 | 0.4934 | +0.062 | -0.064 | 0.0041 ± 0.0097 |
| data_status POOR | 559 | 0.5432 | 0.3887 | 0.4526 | +0.091 | -0.064 | 0.0164 ± 0.007 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 174 | 0.1821 | 0.1832 | -0.0010 ± 0.0011 | 0.5393 | 0.5421 | 0.4977 | 0.4834 | 0.5 | -0.086 ± 0.0348 | -0.01 (3) |
| 3-5 | 110 | 0.175 | 0.1754 | -0.0004 ± 0.0033 | 0.529 | 0.5265 | 0.5167 | 0.476 | 0.5 | -0.071 ± 0.0415 | 0.02 (1) |
| 5-10 | 224 | 0.1958 | 0.2005 | -0.0047 ± 0.0045 | 0.5767 | 0.5863 | 0.5139 | 0.4398 | 0.5 | -0.052 ± 0.0303 | -0.0167 (3) |
| 10-15 | 193 | 0.2134 | 0.2111 | +0.0023 ± 0.0082 | 0.6123 | 0.6041 | 0.518 | 0.3945 | 0.4456 | -0.065 ± 0.0327 | -0.0633 (3) |
| 15-25 | 247 | 0.2176 | 0.2098 | +0.0078 ± 0.0114 | 0.6232 | 0.6044 | 0.5608 | 0.3647 | 0.4453 | -0.043 ± 0.029 | -0.02 (4) |
| 25-40 | 131 | 0.2261 | 0.1818 | +0.0443 ± 0.0228 | 0.6406 | 0.5342 | 0.6273 | 0.3148 | 0.3969 | -0.074 ± 0.0342 | -0.01 (1) |
| 40+ | 30 | 0.3354 | 0.1357 | +0.1998 ± 0.0606 | 0.9067 | 0.4279 | 0.7106 | 0.2678 | 0.2667 | -0.167 ± 0.0655 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 577 | 0.1659 | 0.167 | -0.0011 ± 0.0006 | 0.4996 | 0.5019 | 0.5008 | 0.486 | 0.5286 | -0.019 ± 0.0175 | -0.0188 (8) |
| 3-5 | 374 | 0.1686 | 0.1679 | +0.0007 ± 0.0017 | 0.5119 | 0.5052 | 0.4757 | 0.4358 | 0.4492 | -0.044 ± 0.0215 | 0.02 (1) |
| 5-10 | 824 | 0.1791 | 0.1789 | +0.0002 ± 0.0022 | 0.5378 | 0.5343 | 0.477 | 0.4032 | 0.4357 | -0.029 ± 0.0148 | -0.0129 (7) |
| 10-15 | 746 | 0.183 | 0.1705 | +0.0125 ± 0.0037 | 0.5459 | 0.5043 | 0.4692 | 0.3455 | 0.3566 | -0.051 ± 0.015 | -0.0633 (3) |
| 15-25 | 956 | 0.1975 | 0.1627 | +0.0347 ± 0.0052 | 0.5835 | 0.4835 | 0.4762 | 0.2778 | 0.2897 | -0.048 ± 0.013 | -0.017 (10) |
| 25-40 | 949 | 0.211 | 0.0998 | +0.1113 ± 0.0065 | 0.614 | 0.3226 | 0.5065 | 0.19 | 0.1749 | -0.066 ± 0.0099 | -0.01 (1) |
| 40+ | 713 | 0.3725 | 0.0365 | +0.3360 ± 0.0077 | 0.9688 | 0.1572 | 0.6154 | 0.1027 | 0.0407 | -0.090 ± 0.0067 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 116 | 0.1778 | 0.1788 | -0.0010 ± 0.0013 | 0.5291 | 0.5296 | 0.5042 | 0.4894 | 0.5172 | -0.064 ± 0.039 | -0.01 (1) |
| 3-5 | 86 | 0.1995 | 0.1972 | +0.0024 ± 0.0038 | 0.576 | 0.576 | 0.4957 | 0.4565 | 0.4419 | -0.102 ± 0.0519 | 0.02 (1) |
| 5-10 | 204 | 0.1855 | 0.1856 | -0.0001 ± 0.0046 | 0.5528 | 0.5517 | 0.5685 | 0.4933 | 0.5245 | -0.072 ± 0.0311 | -0.01 (4) |
| 10-15 | 183 | 0.2259 | 0.2133 | +0.0125 ± 0.0086 | 0.641 | 0.6137 | 0.5806 | 0.4563 | 0.4754 | -0.095 ± 0.0356 | -0.0667 (3) |
| 15-25 | 280 | 0.2252 | 0.1999 | +0.0253 ± 0.0107 | 0.6374 | 0.578 | 0.5847 | 0.3874 | 0.4286 | -0.092 ± 0.0278 | -0.0167 (3) |
| 25-40 | 167 | 0.2593 | 0.1981 | +0.0612 ± 0.0214 | 0.721 | 0.5764 | 0.6522 | 0.3403 | 0.3952 | -0.098 ± 0.0356 | -0.025 (2) |
| 40+ | 73 | 0.381 | 0.1718 | +0.2092 ± 0.0492 | 1.0454 | 0.5148 | 0.7445 | 0.2517 | 0.3014 | -0.073 ± 0.0465 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 465 | 0.1545 | 0.1556 | -0.0011 ± 0.0006 | 0.4704 | 0.4727 | 0.5231 | 0.5084 | 0.5398 | -0.018 ± 0.0185 | -0.0217 (6) |
| 3-5 | 312 | 0.1727 | 0.1688 | +0.0039 ± 0.0019 | 0.5119 | 0.506 | 0.5251 | 0.4854 | 0.4583 | -0.082 ± 0.024 | 0.02 (1) |
| 5-10 | 747 | 0.1699 | 0.1708 | -0.0009 ± 0.0023 | 0.5139 | 0.5123 | 0.5167 | 0.4417 | 0.4793 | -0.019 ± 0.0153 | -0.01 (5) |
| 10-15 | 669 | 0.1891 | 0.1762 | +0.0130 ± 0.0041 | 0.561 | 0.5187 | 0.5071 | 0.3831 | 0.3991 | -0.048 ± 0.0165 | -0.0575 (4) |
| 15-25 | 1050 | 0.204 | 0.1609 | +0.0431 ± 0.0049 | 0.5967 | 0.4798 | 0.5103 | 0.3132 | 0.3076 | -0.073 ± 0.0125 | -0.0143 (7) |
| 25-40 | 988 | 0.2304 | 0.1204 | +0.1100 ± 0.007 | 0.6626 | 0.3758 | 0.537 | 0.2203 | 0.2075 | -0.067 ± 0.0112 | -0.015 (6) |
| 40+ | 908 | 0.4083 | 0.0569 | +0.3513 ± 0.0092 | 1.0661 | 0.2129 | 0.6609 | 0.1216 | 0.0749 | -0.079 ± 0.0075 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 178 | 0.1908 | 0.1927 | -0.0018 ± 0.0012 | 0.5583 | 0.5635 | 0.5203 | 0.5056 | 0.5337 | -0.059 ± 0.0328 | -0.01 (5) |
| 3-5 | 118 | 0.1685 | 0.1652 | +0.0033 ± 0.003 | 0.509 | 0.5013 | 0.5014 | 0.4619 | 0.4407 | -0.132 ± 0.0402 | -- (0) |
| 5-10 | 225 | 0.1973 | 0.1963 | +0.0010 ± 0.0044 | 0.5836 | 0.5754 | 0.4994 | 0.4262 | 0.4489 | -0.079 ± 0.0295 | -0.01 (3) |
| 10-15 | 185 | 0.2154 | 0.2138 | +0.0016 ± 0.0085 | 0.6197 | 0.6136 | 0.5435 | 0.42 | 0.4811 | -0.064 ± 0.034 | -0.044 (5) |
| 15-25 | 241 | 0.2097 | 0.2023 | +0.0074 ± 0.0112 | 0.6094 | 0.5851 | 0.5724 | 0.3779 | 0.4564 | -0.049 ± 0.0281 | -0.03 (1) |
| 25-40 | 137 | 0.2223 | 0.1956 | +0.0266 ± 0.0229 | 0.6356 | 0.568 | 0.6268 | 0.315 | 0.4234 | -0.053 ± 0.0344 | 0.0 (1) |
| 40+ | 25 | 0.3648 | 0.1373 | +0.2275 ± 0.0667 | 0.9712 | 0.4311 | 0.711 | 0.2606 | 0.24 | -0.185 ± 0.0761 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 590 | 0.1722 | 0.1724 | -0.0002 ± 0.0006 | 0.5155 | 0.5162 | 0.5026 | 0.4879 | 0.4983 | -0.049 ± 0.017 | -0.0162 (13) |
| 3-5 | 396 | 0.1668 | 0.1629 | +0.0039 ± 0.0016 | 0.5047 | 0.4947 | 0.4906 | 0.4512 | 0.4268 | -0.087 ± 0.0207 | -0.01 (2) |
| 5-10 | 855 | 0.1833 | 0.1757 | +0.0076 ± 0.0022 | 0.5488 | 0.5223 | 0.4639 | 0.3902 | 0.3743 | -0.072 ± 0.0144 | -0.01 (3) |
| 10-15 | 686 | 0.1879 | 0.179 | +0.0090 ± 0.004 | 0.5575 | 0.5287 | 0.4803 | 0.3567 | 0.3834 | -0.037 ± 0.0161 | -0.03 (9) |
| 15-25 | 1030 | 0.1845 | 0.1491 | +0.0354 ± 0.0048 | 0.5567 | 0.4504 | 0.4813 | 0.2817 | 0.2942 | -0.046 ± 0.0118 | -0.03 (2) |
| 25-40 | 914 | 0.2104 | 0.1004 | +0.1099 ± 0.0067 | 0.6132 | 0.3211 | 0.5027 | 0.1825 | 0.1729 | -0.064 ± 0.0101 | 0.0 (1) |
| 40+ | 668 | 0.39 | 0.0382 | +0.3518 ± 0.0085 | 1.0169 | 0.1623 | 0.6249 | 0.103 | 0.0389 | -0.092 ± 0.0072 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 452 | 0.2034 | 0.2034 | +0.0000 ± 0.0007 | 0.5886 | 0.589 | 0.497 | 0.4824 | 0.4845 | -0.041 ± 0.0212 | -0.0226 (46) |
| 3-5 | 334 | 0.1946 | 0.1935 | +0.0011 ± 0.0019 | 0.5707 | 0.5652 | 0.4695 | 0.4297 | 0.4401 | -0.039 ± 0.0239 | -0.0059 (32) |
| 5-10 | 688 | 0.1873 | 0.1828 | +0.0045 ± 0.0025 | 0.5581 | 0.5456 | 0.4596 | 0.3863 | 0.3924 | -0.040 ± 0.0164 | -0.005 (72) |
| 10-15 | 464 | 0.2027 | 0.1912 | +0.0115 ± 0.0051 | 0.5943 | 0.5624 | 0.4595 | 0.3362 | 0.3513 | -0.035 ± 0.0201 | 0.0016 (63) |
| 15-25 | 627 | 0.2314 | 0.2088 | +0.0227 ± 0.0071 | 0.656 | 0.6029 | 0.5275 | 0.3345 | 0.3732 | -0.025 ± 0.0182 | -0.0216 (58) |
| 25-40 | 313 | 0.2622 | 0.1668 | +0.0954 ± 0.0144 | 0.7272 | 0.5019 | 0.5719 | 0.2606 | 0.262 | -0.065 ± 0.0226 | -0.0216 (25) |
| 40+ | 98 | 0.424 | 0.155 | +0.2689 ± 0.0426 | 1.187 | 0.48 | 0.7319 | 0.2239 | 0.2347 | -0.063 ± 0.0412 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 859 | 0.1963 | 0.1957 | +0.0006 ± 0.0005 | 0.5731 | 0.5712 | 0.4923 | 0.4778 | 0.4645 | -0.054 ± 0.0151 | -0.0155 (82) |
| 3-5 | 621 | 0.1932 | 0.1914 | +0.0017 ± 0.0014 | 0.5656 | 0.5588 | 0.47 | 0.4301 | 0.43 | -0.044 ± 0.0176 | -0.018 (54) |
| 5-10 | 1277 | 0.1858 | 0.1799 | +0.0059 ± 0.0018 | 0.554 | 0.5362 | 0.4441 | 0.3701 | 0.3696 | -0.042 ± 0.012 | -0.0089 (122) |
| 10-15 | 962 | 0.1956 | 0.1824 | +0.0132 ± 0.0034 | 0.5767 | 0.5399 | 0.4503 | 0.3271 | 0.3358 | -0.035 ± 0.0136 | -0.0053 (99) |
| 15-25 | 1331 | 0.218 | 0.1853 | +0.0327 ± 0.0046 | 0.6308 | 0.5441 | 0.5011 | 0.3058 | 0.3193 | -0.037 ± 0.0118 | -0.0255 (106) |
| 25-40 | 937 | 0.2405 | 0.128 | +0.1125 ± 0.0074 | 0.6809 | 0.3995 | 0.5271 | 0.212 | 0.1921 | -0.067 ± 0.0115 | -0.0206 (47) |
| 40+ | 523 | 0.3869 | 0.0789 | +0.3080 ± 0.0135 | 1.0548 | 0.2672 | 0.6502 | 0.1347 | 0.1052 | -0.072 ± 0.0125 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1109 | 1.135 ± 0.087 | 1.25 | 0.1688 | 0.1795 | 0.2069 | 0.1953 |
| gen2 | 1109 | 0.93 ± 0.077 | 1.167 | 0.1847 | 0.1792 | 0.2265 | 0.1949 |
| gen1_elo | 1109 | 1.128 ± 0.086 | 1.207 | 0.1739 | 0.1798 | 0.2058 | 0.1952 |
| gen1_sr | 1109 | 1.149 ± 0.1 | 1.22 | 0.1418 | 0.1811 | 0.2218 | 0.1948 |
| gen1_ledger | 2976 | 0.911 ± 0.05 | 1.074 | 0.1619 | 0.2009 | 0.2179 | 0.1913 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 6,787)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,090 | 30.8% |
| STALE_QUOTE | market_freshness | 1,873 | 27.6% |
| BOOK_QUALITY | execution | 918 | 13.5% |
| POOR_DATA | data | 540 | 8.0% |
| LIMITED_DATA | data | 357 | 5.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 341 | 5.0% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 316 | 4.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 198 | 2.9% |
| IDENTITY_AMBIGUOUS | mapping | 151 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.0% |

Cause class: coverage 30.8%, market_freshness 27.6%, execution 13.5%, data 13.2%, market_freshness/coverage 7.9%, model_calibration_or_unknown 4.7%, mapping 2.2%, model_calibration 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 95.1%, LOW_DATA_QUALITY 66.6%, STALE_KALSHI_QUOTE 58.5%, THIN_PLAYER_HISTORY 56.0%, STALE_PLAYER_DATA 55.0%, MODEL_INTERNAL_DISAGREEMENT 36.1%, ASYMMETRIC_SAMPLE_SIZE 30.3%, WIDE_SPREAD 21.9%, MODEL_HIGH_UNCERTAINTY 14.4%, PLAYER_IDENTITY_RISK 11.1%, LEVEL_TRANSFER_RISK 8.2%, EVENT_MAPPING_RISK 6.8%, LOW_DISPLAYED_LIQUIDITY 6.3%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 33.1%, POST_SETTLEMENT_OBSERVATION 30.8%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.9%

### >= ge_25 pp (N = 3,809)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,658 | 43.5% |
| STALE_QUOTE | market_freshness | 857 | 22.5% |
| BOOK_QUALITY | execution | 473 | 12.4% |
| POOR_DATA | data | 239 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 184 | 4.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 118 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 100 | 2.6% |
| LIMITED_DATA | data | 99 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 81 | 2.1% |

Cause class: coverage 43.5%, market_freshness 22.5%, execution 12.4%, data 8.9%, market_freshness/coverage 7.9%, mapping 2.6%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.3%, LOW_DATA_QUALITY 69.9%, STALE_KALSHI_QUOTE 65.4%, THIN_PLAYER_HISTORY 58.6%, STALE_PLAYER_DATA 52.2%, MODEL_INTERNAL_DISAGREEMENT 38.0%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 20.5%, MODEL_HIGH_UNCERTAINTY 15.5%, PLAYER_IDENTITY_RISK 13.8%, LEVEL_TRANSFER_RISK 7.9%, EVENT_MAPPING_RISK 7.7%, LOW_DISPLAYED_LIQUIDITY 6.8%, MODEL_CALIBRATION_OUTLIER 3.1%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 45.9%, POST_SETTLEMENT_OBSERVATION 43.5%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 1.0%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 3184, "IDENTITY_AMBIGUOUS": 625}; ticker orientation: {"VERIFIED": 3809}.

Checks: discipline:AMBIGUOUS 191, discipline:PASS 3618, identity_confidence:AMBIGUOUS 524, identity_confidence:PASS 3285, level_mapping:NA 203, level_mapping:PASS 3606, market_pair:AMBIGUOUS 132, market_pair:NA 93, market_pair:PASS 3584, model_complement:NA 62, model_complement:PASS 3747, namesake:PASS 3809, physical_match_id:NA 1690, physical_match_id:PASS 2119, player_ids:PASS 3809, same_pair_other_event:PASS 3809, ticker_orientation:PASS 3809

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 727 | 3.2% | 3.2% | 0.6% | {"market_freshness": 20, "execution": 3} | 5.89 | 0.1791 / 0.1823 (49) | 29.7% | 0.3% | 4.7% | 1.5% |
| CHALLENGER | 2,700 | 20.5% | 7.8% | 14.5% | {"coverage": 329, "market_freshness": 104, "market_freshness/coverage": 67, "model_calibration_or_unknown": 26, "data": 23, "execution": 4} | 7.54 | 0.2202 / 0.2044 (702) | 54.9% | 5.8% | 1.4% | 25.5% |
| DOUBLES | 421 | 45.4% | 45.1% | 5.0% | {"market_freshness": 106, "mapping": 33, "execution": 33, "market_freshness/coverage": 12, "coverage": 7} | 23.51 | 0.3189 / 0.2288 (164) | 55.6% | 0.0% | 100.0% | 9.5% |
| ITF_MEN | 4,628 | 26.5% | 17.0% | 32.1% | {"coverage": 578, "market_freshness": 220, "execution": 216, "data": 115, "market_freshness/coverage": 80, "mapping": 14, "model_calibration_or_unknown": 1} | 10.63 | 0.2149 / 0.1882 (1391) | 50.5% | 53.8% | 7.0% | 28.2% |
| ITF_WOMEN | 5,516 | 29.8% | 20.5% | 43.2% | {"coverage": 727, "market_freshness": 358, "execution": 207, "data": 179, "market_freshness/coverage": 103, "mapping": 49, "model_calibration_or_unknown": 21} | 13.19 | 0.2028 / 0.1855 (1387) | 52.8% | 61.0% | 10.7% | 27.9% |
| OTHER | 149 | 8.1% | 7.3% | 0.3% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 858 | 9.2% | 8.0% | 2.1% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.47 | 0.2006 / 0.1964 (129) | 37.8% | 2.5% | 1.4% | 3.5% |
| WTA125 | 553 | 15.0% | 8.8% | 2.2% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 15, "market_freshness": 13, "coverage": 12, "data": 10, "mapping": 2, "execution": 1} | 10.01 | 0.2273 / 0.204 (221) | 32.0% | 7.0% | 3.4% | 15.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 5 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 6 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 9 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 11 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 12 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 14 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 15 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 16 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 17 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 18 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 19 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 20 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 21 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 23 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 24 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 25 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 26 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 27 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 28 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 256 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 29 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 30 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 31 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 32 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 33 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 34 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 36 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 37 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 39 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 732 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 40 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 41 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 192 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.76); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 44 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 46 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 18.1h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 1101 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 47 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 48 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 49 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 50 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9732, "by_level_share_of_ge_25pp": {"ATP": 0.006, "CHALLENGER": 0.1452, "DOUBLES": 0.0501, "ITF_MEN": 0.3213, "ITF_WOMEN": 0.4316, "OTHER": 0.0032, "WTA": 0.0207, "WTA125": 0.0218}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.654, "share_primary_cause_market_settled_or_in_play": 0.5146, "share_primary_cause_stale_quote_only": 0.225}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 3809, "identity_ambiguous_share": 0.1641, "ticker_orientation": {"VERIFIED": 3809}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 2119, "with_external": 16, "coverage": 0.0076, "external_status": {"EXTERNAL_STALE": 16}, "triangulation": {"INSUFFICIENT_INPUTS": 16}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 923, "with_external": 16, "coverage": 0.0173, "external_status": {"EXTERNAL_STALE": 16}, "triangulation": {"INSUFFICIENT_INPUTS": 16}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 626.0, "median_sample_ratio": 2.34, "median_min_matches": 21.0, "median_max_days_since_last": 190.5, "share_severe_asymmetry": 0.1835, "data_status": {"POOR": 1974, "LIMITED": 1087, "ADEQUATE": 748}, "comparison_lt_10pp": {"median_thinner_serve_points": 1869.0, "median_sample_ratio": 1.73, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 252, "model_minus_observed": 0.0926, "kalshi_minus_observed": -0.0386, "brier_diff_model_minus_kalshi": 0.0081}, "4-10x": {"n": 174, "model_minus_observed": 0.0929, "kalshi_minus_observed": -0.0444, "brier_diff_model_minus_kalshi": 0.0141}, "<2x": {"n": 509, "model_minus_observed": 0.0705, "kalshi_minus_observed": -0.0535, "brier_diff_model_minus_kalshi": 0.0124}, ">=10x": {"n": 174, "model_minus_observed": 0.087, "kalshi_minus_observed": -0.085, "brier_diff_model_minus_kalshi": 0.012}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1109, "model": {"intercept": -0.633, "slope": 0.93, "slope_se": 0.077}, "kalshi_mid_same_rows": {"intercept": 0.212, "slope": 1.167, "slope_se": 0.085}, "mean_extremity_model": 0.1847, "mean_extremity_kalshi": 0.1792, "model_brier": 0.2265, "kalshi_brier": 0.1949, "brier_diff_model_minus_kalshi": 0.0315, "brier_diff_se": 0.0058, "model_logloss": 0.6458, "kalshi_logloss": 0.5694}, "fair_v1": {"n": 1109, "model": {"intercept": -0.41, "slope": 1.135, "slope_se": 0.087}, "kalshi_mid_same_rows": {"intercept": 0.372, "slope": 1.25, "slope_se": 0.089}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1795, "model_brier": 0.2069, "kalshi_brier": 0.1953, "brier_diff_model_minus_kalshi": 0.0116, "brier_diff_se": 0.0045, "model_logloss": 0.5991, "kalshi_logloss": 0.5701}, "gen1_elo": {"n": 1109, "model": {"intercept": -0.441, "slope": 1.128, "slope_se": 0.086}, "kalshi_mid_same_rows": {"intercept": 0.311, "slope": 1.207, "slope_se": 0.087}, "mean_extremity_model": 0.1739, "mean_extremity_kalshi": 0.1798, "model_brier": 0.2058, "kalshi_brier": 0.1952, "brier_diff_model_minus_kalshi": 0.0106, "brier_diff_se": 0.0045, "model_logloss": 0.5984, "kalshi_logloss": 0.5699}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2701, "share_ge_15": 0.4525, "median_abs_gap": 13.27, "n": 7845}, "gen1_elo": {"share_ge_25": 0.2594, "share_ge_15": 0.4469, "median_abs_gap": 12.9, "n": 7845}, "gen1_sr": {"share_ge_25": 0.316, "share_ge_15": 0.5327, "median_abs_gap": 16.3, "n": 7845}, "gen2": {"share_ge_25": 0.3199, "share_ge_15": 0.521, "median_abs_gap": 15.86, "n": 7845}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1592, "share_ge_15": 0.3504, "median_abs_gap": 10.54, "n": 5796}, "gen1_elo": {"share_ge_25": 0.1548, "share_ge_15": 0.3406, "median_abs_gap": 10.04, "n": 5796}, "gen1_sr": {"share_ge_25": 0.205, "share_ge_15": 0.44, "median_abs_gap": 13.18, "n": 5796}, "gen2": {"share_ge_25": 0.2265, "share_ge_15": 0.4419, "median_abs_gap": 12.98, "n": 5796}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.89, "share_ge_25_all": 0.0316, "share_ge_25_pregame_clean": 0.0321}, "WTA": {"median_abs_gap_pregame_clean": 8.47, "share_ge_25_all": 0.0921, "share_ge_25_pregame_clean": 0.0797}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2224, "share_within_10pp_all": 0.4129, "share_within_10pp_pregame_clean": 0.4844, "corr_model_vs_mid_pregame_clean": 0.8291}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 174, "model_brier": 0.1821, "kalshi_brier": 0.1832, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 193, "model_brier": 0.2134, "kalshi_brier": 0.2111, "brier_diff_model_minus_kalshi": 0.0023}, "15-25": {"n_settled": 247, "model_brier": 0.2176, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.0078}, "25-40": {"n_settled": 131, "model_brier": 0.2261, "kalshi_brier": 0.1818, "brier_diff_model_minus_kalshi": 0.0443}, "3-5": {"n_settled": 110, "model_brier": 0.175, "kalshi_brier": 0.1754, "brier_diff_model_minus_kalshi": -0.0004}, "40+": {"n_settled": 30, "model_brier": 0.3354, "kalshi_brier": 0.1357, "brier_diff_model_minus_kalshi": 0.1998}, "5-10": {"n_settled": 224, "model_brier": 0.1958, "kalshi_brier": 0.2005, "brier_diff_model_minus_kalshi": -0.0047}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 164, "model_brier": 0.3189, "kalshi_brier": 0.2288, "brier_diff_model_minus_kalshi": 0.0901, "brier_diff_se": 0.0256, "corr_model_outcome": -0.0904, "corr_kalshi_outcome": 0.3354}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
