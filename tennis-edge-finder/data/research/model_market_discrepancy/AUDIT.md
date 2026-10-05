# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-05T16:51Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 13,458): 0-3 13.1%, 3-5 9.0%, 5-10 18.8%, 10-15 15.1%, 15-25 19.5%, 25-40 15.0%, 40+ 9.6%; median gap 12.82 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.4%, Challenger 14.3%, doubles 5.7%). Main tour: ATP 4.9% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 3,310): MARKET_ALREADY_SETTLED_WHEN_PRICED 45.9%, STALE_QUOTE 24.5%, BOOK_QUALITY 7.4%, POOR_DATA 6.3%, POSSIBLY_IN_PLAY_QUOTE 5.0%, IN_PLAY_QUOTE 3.3%, LIMITED_DATA 2.8%, IDENTITY_AMBIGUOUS 2.7%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 45.9%, market_freshness 24.5%, data 9.1%, market_freshness/coverage 8.3%, execution 7.4%, mapping 2.7%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 69.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 54.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 3,310 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 15.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.6%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 6.3% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 766.0 points vs 1889.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.141, Gen-2 0.927, Gen-1 ledger 0.911 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 128 model 0.2287 vs Kalshi 0.1819; n 30 model 0.3354 vs Kalshi 0.1357.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 44,734 model-market comparisons (77,927 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 18,582 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-05T16:47:32.316174+00:00'], shadow board 13,339 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-05T16:47:35.813960+00:00'], Model 4 3,647 rows, 8,672 settled tickers, 1,937 tickers with an external scan.
* By model: {"gen1_ledger": 10853, "gen1_elo": 6705, "fair_v1": 6705, "gen2": 6705, "gen1_sr": 6705, "model4_fundamental": 3535, "model4_conditioned": 3526}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 13,458 | 13.1 | 9.0 | 18.8 | 15.1 | 19.5 | 15.0 | 9.6 | 12.82 | 44.1% | 24.6% |
| MW fair_v1 | 6,705 | 13.0 | 8.4 | 17.8 | 15.3 | 18.6 | 15.8 | 11.1 | 13.34 | 45.5% | 26.9% |
| MW gen1_elo | 6,705 | 13.0 | 8.7 | 19.5 | 14.4 | 18.4 | 15.6 | 10.4 | 12.85 | 44.4% | 26.0% |
| MW gen1_ledger | 6,753 | 13.2 | 9.6 | 19.8 | 14.8 | 20.4 | 14.3 | 8.1 | 12.23 | 42.7% | 22.4% |
| MW gen1_sr | 6,705 | 9.3 | 7.2 | 16.0 | 13.7 | 21.9 | 19.0 | 13.0 | 16.57 | 53.9% | 32.0% |
| MW gen2 | 6,705 | 11.1 | 6.6 | 16.1 | 13.9 | 20.2 | 17.8 | 14.4 | 15.98 | 52.3% | 32.2% |
| all families model4_conditioned | 3,526 | 19.3 | 16.7 | 29.5 | 21.1 | 9.8 | 2.0 | 1.6 | 6.97 | 13.4% | 3.5% |
| all families model4_fundamental | 3,535 | 14.8 | 10.8 | 29.1 | 21.4 | 15.2 | 6.2 | 2.6 | 9.14 | 24.0% | 8.7% |

Configurable thresholds (primary): >=5pp 78.0%, >=10pp 59.1%, >=15pp 44.1%, >=20pp 33.5%, >=25pp 24.6%, >=30pp 18.1%, >=40pp 9.6%, >=50pp 4.3%
Executable gap (model outside the book, before fees): median 10.14pp; >=10pp 50.3%, >=25pp 21.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 362 | 20.4 | 16.0 | 24.6 | 15.8 | 16.9 | 3.3 | 3.0 | 7.27 | 23.2% | 6.3% |
| CHALLENGER | 1,440 | 15.3 | 10.5 | 16.7 | 15.9 | 15.3 | 13.9 | 12.4 | 12.68 | 41.6% | 26.3% |
| ITF_MEN | 1,893 | 11.8 | 8.1 | 18.8 | 14.6 | 18.1 | 15.5 | 13.1 | 13.42 | 46.7% | 28.6% |
| ITF_WOMEN | 2,455 | 9.7 | 6.0 | 15.3 | 15.4 | 21.3 | 20.7 | 11.7 | 16.55 | 53.7% | 32.4% |
| WTA | 441 | 22.9 | 10.7 | 25.4 | 12.9 | 18.8 | 6.8 | 2.5 | 8.17 | 28.1% | 9.3% |
| WTA125 | 114 | 14.0 | 4.4 | 18.4 | 28.1 | 16.7 | 11.4 | 7.0 | 12.4 | 35.1% | 18.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 362 | 19.6 | 12.7 | 24.3 | 15.8 | 18.8 | 5.2 | 3.6 | 8.38 | 27.6% | 8.8% |
| CHALLENGER | 1,440 | 14.0 | 6.2 | 18.3 | 14.2 | 19.0 | 16.2 | 12.1 | 14.02 | 47.4% | 28.3% |
| ITF_MEN | 1,893 | 9.1 | 6.8 | 17.3 | 15.2 | 19.7 | 17.4 | 14.5 | 15.59 | 51.7% | 32.0% |
| ITF_WOMEN | 2,455 | 8.2 | 6.0 | 12.6 | 12.0 | 20.9 | 20.9 | 19.4 | 20.0 | 61.2% | 40.3% |
| WTA | 441 | 20.4 | 5.7 | 16.6 | 15.7 | 22.2 | 17.0 | 2.5 | 12.98 | 41.7% | 19.5% |
| WTA125 | 114 | 6.1 | 4.4 | 15.8 | 18.4 | 23.7 | 18.4 | 13.2 | 17.86 | 55.3% | 31.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 362 | 25.7 | 12.4 | 28.4 | 12.2 | 9.7 | 8.3 | 3.3 | 7.48 | 21.3% | 11.6% |
| CHALLENGER | 1,440 | 15.9 | 10.0 | 22.0 | 13.2 | 13.1 | 13.2 | 12.6 | 10.71 | 38.9% | 25.8% |
| ITF_MEN | 1,893 | 10.2 | 9.0 | 17.8 | 15.1 | 19.3 | 15.6 | 13.0 | 13.95 | 47.9% | 28.6% |
| ITF_WOMEN | 2,455 | 9.6 | 6.3 | 15.9 | 14.2 | 23.6 | 20.4 | 10.1 | 17.18 | 54.1% | 30.5% |
| WTA | 441 | 23.1 | 14.1 | 29.9 | 15.7 | 11.3 | 4.3 | 1.6 | 6.99 | 17.2% | 5.9% |
| WTA125 | 114 | 15.8 | 5.3 | 22.8 | 28.9 | 17.5 | 7.9 | 1.8 | 11.54 | 27.2% | 9.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 107 | 26.2 | 18.7 | 36.5 | 14.0 | 4.7 | 0.0 | 0.0 | 5.9 | 4.7% | 0.0% |
| CHALLENGER | 1,011 | 20.7 | 14.6 | 25.6 | 15.5 | 14.1 | 6.7 | 2.8 | 7.45 | 23.5% | 9.5% |
| DOUBLES | 391 | 5.6 | 3.8 | 10.2 | 10.7 | 21.7 | 21.0 | 26.9 | 23.94 | 69.6% | 47.8% |
| ITF_MEN | 2,160 | 14.0 | 9.1 | 18.6 | 13.9 | 20.9 | 14.0 | 9.5 | 12.54 | 44.4% | 23.5% |
| ITF_WOMEN | 2,221 | 8.7 | 8.1 | 17.0 | 14.4 | 23.9 | 19.4 | 8.5 | 15.77 | 51.8% | 27.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 369 | 16.0 | 9.2 | 25.8 | 21.9 | 17.6 | 8.7 | 0.8 | 9.7 | 27.1% | 9.5% |
| WTA125 | 345 | 13.3 | 9.9 | 21.7 | 17.1 | 22.3 | 11.9 | 3.8 | 11.31 | 38.0% | 15.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 359 | 20.3 | 16.2 | 24.8 | 15.6 | 16.7 | 3.3 | 3.1 | 7.19 | 23.1% | 6.4% |
| CHALLENGER | 1,049 | 19.8 | 12.8 | 20.2 | 18.4 | 16.6 | 8.2 | 4.0 | 9.19 | 28.8% | 12.2% |
| ITF_MEN | 1,226 | 15.3 | 11.3 | 23.3 | 16.1 | 18.5 | 10.5 | 5.0 | 10.0 | 34.0% | 15.5% |
| ITF_WOMEN | 1,698 | 12.5 | 7.7 | 18.2 | 17.7 | 22.6 | 16.8 | 4.5 | 13.34 | 43.9% | 21.3% |
| WTA | 440 | 22.9 | 10.7 | 25.4 | 12.9 | 18.9 | 6.6 | 2.5 | 8.16 | 28.0% | 9.1% |
| WTA125 | 108 | 14.8 | 4.6 | 19.4 | 29.6 | 16.7 | 10.2 | 4.6 | 11.58 | 31.5% | 14.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 359 | 19.8 | 12.5 | 24.5 | 15.9 | 18.7 | 5.3 | 3.3 | 8.33 | 27.3% | 8.6% |
| CHALLENGER | 1,049 | 17.7 | 7.6 | 22.3 | 17.2 | 19.9 | 11.7 | 3.4 | 10.57 | 35.1% | 15.2% |
| ITF_MEN | 1,226 | 12.1 | 8.4 | 21.1 | 17.7 | 20.8 | 13.4 | 6.5 | 12.18 | 40.7% | 19.9% |
| ITF_WOMEN | 1,698 | 9.9 | 7.6 | 14.1 | 12.0 | 23.7 | 19.6 | 13.2 | 17.29 | 56.5% | 32.8% |
| WTA | 440 | 20.4 | 5.7 | 16.6 | 15.7 | 22.3 | 16.8 | 2.5 | 12.98 | 41.6% | 19.3% |
| WTA125 | 108 | 6.5 | 4.6 | 15.7 | 19.4 | 25.0 | 19.4 | 9.3 | 16.39 | 53.7% | 28.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 97 | 26.8 | 20.6 | 37.1 | 14.4 | 1.0 | 0.0 | 0.0 | 5.4 | 1.0% | 0.0% |
| CHALLENGER | 829 | 22.9 | 17.1 | 28.4 | 15.2 | 13.4 | 2.9 | 0.1 | 6.71 | 16.4% | 3.0% |
| DOUBLES | 352 | 5.7 | 3.7 | 10.5 | 10.8 | 21.6 | 21.3 | 26.4 | 23.93 | 69.3% | 47.7% |
| ITF_MEN | 1,550 | 17.0 | 11.0 | 21.6 | 15.1 | 20.9 | 10.7 | 3.8 | 10.11 | 35.4% | 14.4% |
| ITF_WOMEN | 1,559 | 10.5 | 9.5 | 20.1 | 16.4 | 24.8 | 16.5 | 2.2 | 12.63 | 43.5% | 18.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 340 | 16.2 | 9.7 | 26.5 | 22.6 | 18.2 | 6.8 | 0.0 | 9.54 | 25.0% | 6.8% |
| WTA125 | 266 | 15.8 | 10.9 | 25.9 | 20.3 | 20.7 | 6.0 | 0.4 | 9.32 | 27.1% | 6.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 391 | 5.6 | 3.8 | 10.2 | 10.7 | 21.7 | 21.0 | 26.9 | 23.94 | 69.6% | 47.8% |
| singles | 6,362 | 13.6 | 9.9 | 20.4 | 15.0 | 20.3 | 13.8 | 7.0 | 11.83 | 41.1% | 20.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,509 | 14.7 | 9.1 | 18.2 | 15.2 | 16.4 | 13.8 | 12.7 | 12.66 | 42.9% | 26.6% |
| Hard | 4,638 | 12.6 | 8.4 | 18.1 | 15.1 | 19.5 | 15.9 | 10.5 | 13.52 | 45.9% | 26.4% |
| UNKNOWN | 558 | 12.2 | 6.3 | 14.5 | 17.9 | 17.7 | 19.9 | 11.5 | 14.52 | 49.1% | 31.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,022 | 16.7 | 10.0 | 20.0 | 15.7 | 17.0 | 11.5 | 9.2 | 10.83 | 37.6% | 20.6% |
| B | 969 | 16.1 | 10.3 | 17.4 | 17.4 | 16.4 | 10.7 | 11.6 | 11.51 | 38.7% | 22.3% |
| C | 1,013 | 12.9 | 9.3 | 21.4 | 13.8 | 16.1 | 15.4 | 11.1 | 12.61 | 42.5% | 26.5% |
| D | 1,194 | 11.2 | 8.0 | 16.8 | 14.7 | 21.5 | 15.7 | 12.1 | 14.53 | 49.2% | 27.7% |
| F | 1,507 | 7.4 | 4.5 | 13.6 | 15.1 | 21.7 | 25.1 | 12.6 | 19.46 | 59.4% | 37.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,045 | 18.9 | 12.3 | 25.7 | 17.0 | 16.1 | 7.0 | 3.1 | 8.56 | 26.2% | 10.1% |
| B | 1,079 | 13.6 | 9.6 | 21.5 | 15.7 | 19.9 | 12.4 | 7.2 | 11.56 | 39.6% | 19.7% |
| C | 1,328 | 11.1 | 8.8 | 15.5 | 14.2 | 22.4 | 15.4 | 12.7 | 15.18 | 50.4% | 28.1% |
| D | 1,044 | 11.3 | 8.4 | 20.6 | 11.9 | 23.9 | 15.8 | 8.1 | 14.05 | 47.8% | 23.8% |
| F | 1,257 | 7.2 | 6.8 | 12.7 | 13.4 | 22.6 | 25.1 | 12.2 | 18.91 | 59.9% | 37.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 2,506 | 16.3 | 9.5 | 19.0 | 16.2 | 16.9 | 11.7 | 10.4 | 11.27 | 39.0% | 22.1% |
| LIMITED | 1,479 | 14.3 | 10.8 | 21.1 | 14.6 | 15.8 | 13.4 | 9.9 | 11.39 | 39.1% | 23.3% |
| POOR | 2,720 | 9.2 | 6.0 | 14.9 | 14.9 | 21.8 | 20.9 | 12.3 | 17.26 | 54.9% | 33.2% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 477 | 33.5 | 23.7 | 34.2 | 5.9 | 2.1 | 0.6 | 0.0 | 4.32 | 2.7% | 0.6% |
| GAME_SPREAD | 498 | 21.5 | 17.1 | 35.3 | 16.9 | 7.8 | 1.0 | 0.4 | 6.31 | 9.2% | 1.4% |
| MATCH_WINNER | 6,753 | 13.2 | 9.6 | 19.8 | 14.8 | 20.4 | 14.3 | 8.1 | 12.23 | 42.7% | 22.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,862 | 23.2 | 14.3 | 30.6 | 16.2 | 12.5 | 2.5 | 0.6 | 6.63 | 15.6% | 3.1% |
| TOTAL_GAMES | 1,239 | 9.5 | 9.4 | 28.3 | 25.1 | 16.2 | 7.3 | 4.1 | 10.48 | 27.6% | 11.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,272 | 27.0 | 32.0 | 24.6 | 0.6 | 14.1 | 1.3 | 0.5 | 4.37 | 15.9% | 1.8% |
| GAME_SPREAD | 720 | 37.6 | 15.0 | 26.8 | 16.4 | 2.1 | 1.5 | 0.6 | 4.41 | 4.2% | 2.1% |
| TOTAL_GAMES | 1,534 | 4.4 | 4.8 | 34.9 | 40.3 | 9.9 | 2.7 | 2.9 | 10.54 | 15.6% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,272 | 24.3 | 15.0 | 31.0 | 9.8 | 12.1 | 6.6 | 1.2 | 6.18 | 19.9% | 7.8% |
| GAME_SPREAD | 720 | 17.4 | 10.6 | 24.2 | 23.3 | 16.7 | 5.8 | 2.1 | 9.69 | 24.6% | 7.9% |
| TOTAL_GAMES | 1,543 | 5.8 | 7.4 | 29.8 | 30.0 | 17.1 | 6.0 | 4.0 | 10.84 | 27.0% | 9.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6,705 | 45.5% | 26.9% | 13.34 | 34.9% | 15.6% | 10.48 |
| gen1_elo | 6,705 | 44.4% | 26.0% | 12.85 | 33.4% | 15.4% | 9.77 |
| gen1_sr | 6,705 | 53.9% | 32.0% | 16.57 | 44.3% | 20.9% | 13.3 |
| gen2 | 6,705 | 52.3% | 32.2% | 15.98 | 44.4% | 22.7% | 13.04 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 2,468 | 16.8 | 11.6 | 22.0 | 15.9 | 19.0 | 11.0 | 3.7 | 9.95 | 33.7% | 14.7% |
| STALE | 4,237 | 10.8 | 6.5 | 15.4 | 15.0 | 18.4 | 18.5 | 15.4 | 16.4 | 52.3% | 33.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 221 | 14.5 | 9.5 | 22.6 | 14.5 | 17.2 | 18.1 | 3.6 | 10.99 | 38.9% | 21.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 13,458 | 221 | 5940 | 7297 | 31.5 | 222.5 | 1400.4 |
| ge_15pp | 5,934 | 86 | 2120 | 3728 | 39.7 | 475.9 | 1380.4 |
| ge_25pp | 3,310 | 48 | 954 | 2308 | 53.0 | 603.1 | 1380.4 |
| lt_10pp | 5,499 | 103 | 2877 | 2519 | 28.8 | 59.8 | 1201.9 |

Current slate `SL-20261005T165107Z-ca4fa10d`: 859 priced rows, quote age at build {'median': 8.5, 'max': 8.5}, freshness {'FRESH': 859}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 168 | 22.0 | 11.3 | 23.2 | 20.2 | 17.3 | 5.4 | 0.6 | 7.54 | 23.2% | 5.9% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 8.3 | 50.0 | 41.7 | 0.0 | 0.0 | 14.32 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 6,705 | 189 (2.8%) | 6.3% | 0.0% | {"EXTERNAL_STALE": 168, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 3,049 | 44 (1.4%) | 11.4% | 0.0% | {"EXTERNAL_STALE": 39, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,800 | 10 (0.6%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 10} |
| fair_v1_ge_25pp_pregame_clean | 759 | 10 (1.3%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 10} |
| fair_v1_lt_10pp | 2,627 | 105 (4.0%) | 0.9% | 0.0% | {"EXTERNAL_STALE": 95, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,348 | 12.0 | 7.5 | 19.9 | 16.2 | 20.0 | 14.7 | 9.6 | 12.82 | 44.4% | 24.3% |
| 4-10x | 914 | 12.6 | 10.7 | 16.6 | 14.7 | 17.3 | 17.6 | 10.5 | 13.57 | 45.4% | 28.1% |
| <2x | 3,604 | 14.1 | 8.9 | 18.2 | 15.3 | 18.3 | 13.8 | 11.3 | 12.79 | 43.5% | 25.2% |
| >=10x | 839 | 10.1 | 4.8 | 14.3 | 14.9 | 19.2 | 23.7 | 13.0 | 17.89 | 55.9% | 36.7% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,823 | 14.0 | 8.7 | 20.0 | 16.0 | 16.6 | 12.6 | 12.2 | 12.12 | 41.4% | 24.7% |
| 300-1000 | 1,562 | 13.1 | 8.4 | 16.6 | 15.6 | 20.4 | 15.5 | 10.4 | 13.67 | 46.3% | 25.9% |
| <300 | 1,751 | 8.2 | 5.4 | 14.2 | 14.2 | 21.2 | 23.7 | 13.1 | 18.9 | 58.0% | 36.8% |
| >=3000 | 1,569 | 17.0 | 11.2 | 20.6 | 15.7 | 16.2 | 10.9 | 8.3 | 10.39 | 35.4% | 19.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 244 | 0.5174 | 0.3867 | 0.4221 | +0.095 | -0.035 | 0.0099 ± 0.009 |
| ratio 4-10x | 167 | 0.5754 | 0.4365 | 0.479 | +0.096 | -0.043 | 0.0146 ± 0.0115 |
| ratio <2x | 495 | 0.5358 | 0.4112 | 0.4687 | +0.067 | -0.058 | 0.0117 ± 0.0064 |
| ratio >=10x | 172 | 0.551 | 0.3792 | 0.4593 | +0.092 | -0.080 | 0.0138 ± 0.0143 |
| thinner_sample 1000-3000 | 290 | 0.5393 | 0.419 | 0.4552 | +0.084 | -0.036 | 0.0089 ± 0.0081 |
| thinner_sample 300-1000 | 290 | 0.5543 | 0.4223 | 0.469 | +0.085 | -0.047 | 0.0072 ± 0.0085 |
| thinner_sample <300 | 356 | 0.5369 | 0.3706 | 0.4522 | +0.085 | -0.082 | 0.0174 ± 0.0093 |
| thinner_sample >=3000 | 142 | 0.5213 | 0.423 | 0.4577 | +0.064 | -0.035 | 0.0154 ± 0.0094 |
| data_status ADEQUATE | 316 | 0.5282 | 0.4191 | 0.4557 | +0.073 | -0.037 | 0.0077 ± 0.0071 |
| data_status LIMITED | 222 | 0.5564 | 0.4303 | 0.491 | +0.066 | -0.061 | 0.0043 ± 0.0099 |
| data_status POOR | 540 | 0.5405 | 0.3852 | 0.4463 | +0.094 | -0.061 | 0.0178 ± 0.0071 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 169 | 0.1788 | 0.18 | -0.0012 ± 0.0011 | 0.5307 | 0.5341 | 0.4917 | 0.4773 | 0.503 | -0.077 ± 0.0349 | -0.01 (3) |
| 3-5 | 107 | 0.1739 | 0.1739 | -0.0000 ± 0.0034 | 0.5264 | 0.5231 | 0.5175 | 0.4766 | 0.4953 | -0.071 ± 0.0425 | 0.02 (1) |
| 5-10 | 218 | 0.195 | 0.1998 | -0.0047 ± 0.0045 | 0.575 | 0.5848 | 0.5136 | 0.4394 | 0.5 | -0.045 ± 0.0304 | -0.0167 (3) |
| 10-15 | 187 | 0.2132 | 0.209 | +0.0042 ± 0.0083 | 0.6115 | 0.5985 | 0.519 | 0.3955 | 0.4385 | -0.070 ± 0.0334 | -0.0633 (3) |
| 15-25 | 239 | 0.2161 | 0.2098 | +0.0063 ± 0.0116 | 0.6199 | 0.6043 | 0.5584 | 0.3618 | 0.4477 | -0.031 ± 0.0293 | -0.02 (4) |
| 25-40 | 128 | 0.2287 | 0.1819 | +0.0469 ± 0.0232 | 0.6466 | 0.5342 | 0.6255 | 0.3129 | 0.3906 | -0.075 ± 0.0349 | -0.01 (1) |
| 40+ | 30 | 0.3354 | 0.1357 | +0.1998 ± 0.0606 | 0.9067 | 0.4279 | 0.7106 | 0.2678 | 0.2667 | -0.167 ± 0.0655 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 548 | 0.1612 | 0.1624 | -0.0013 ± 0.0006 | 0.4879 | 0.491 | 0.5024 | 0.4876 | 0.5347 | -0.014 ± 0.0178 | -0.0188 (8) |
| 3-5 | 355 | 0.1693 | 0.1683 | +0.0010 ± 0.0018 | 0.5135 | 0.5063 | 0.4775 | 0.4375 | 0.4479 | -0.045 ± 0.0222 | 0.02 (1) |
| 5-10 | 803 | 0.178 | 0.1783 | -0.0002 ± 0.0022 | 0.5356 | 0.5331 | 0.476 | 0.4021 | 0.4384 | -0.022 ± 0.0149 | -0.0129 (7) |
| 10-15 | 695 | 0.1841 | 0.1713 | +0.0129 ± 0.0039 | 0.5481 | 0.5054 | 0.4719 | 0.3484 | 0.3568 | -0.053 ± 0.0157 | -0.0633 (3) |
| 15-25 | 902 | 0.1966 | 0.1614 | +0.0353 ± 0.0053 | 0.5819 | 0.4797 | 0.4795 | 0.2813 | 0.2916 | -0.048 ± 0.0133 | -0.017 (10) |
| 25-40 | 857 | 0.2105 | 0.0974 | +0.1131 ± 0.0067 | 0.6128 | 0.3166 | 0.5075 | 0.1917 | 0.1727 | -0.071 ± 0.0103 | -0.01 (1) |
| 40+ | 617 | 0.3738 | 0.0326 | +0.3412 ± 0.0079 | 0.9721 | 0.1467 | 0.6171 | 0.1025 | 0.0373 | -0.095 ± 0.0067 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 111 | 0.1716 | 0.1732 | -0.0016 ± 0.0014 | 0.5128 | 0.5145 | 0.5032 | 0.4883 | 0.5315 | -0.046 ± 0.0394 | -0.01 (1) |
| 3-5 | 83 | 0.1999 | 0.1985 | +0.0014 ± 0.0039 | 0.5774 | 0.5799 | 0.4998 | 0.4605 | 0.4578 | -0.082 ± 0.0518 | 0.02 (1) |
| 5-10 | 202 | 0.1848 | 0.1855 | -0.0008 ± 0.0046 | 0.5512 | 0.5514 | 0.5691 | 0.4939 | 0.5297 | -0.067 ± 0.0311 | -0.01 (4) |
| 10-15 | 176 | 0.2226 | 0.2102 | +0.0125 ± 0.0088 | 0.6341 | 0.6058 | 0.5821 | 0.4577 | 0.4773 | -0.089 ± 0.0355 | -0.0667 (3) |
| 15-25 | 272 | 0.2237 | 0.1995 | +0.0242 ± 0.0108 | 0.634 | 0.577 | 0.5833 | 0.3856 | 0.4301 | -0.084 ± 0.0281 | -0.0167 (3) |
| 25-40 | 161 | 0.2641 | 0.1983 | +0.0657 ± 0.0218 | 0.7323 | 0.5767 | 0.6488 | 0.338 | 0.3851 | -0.098 ± 0.0368 | -0.025 (2) |
| 40+ | 73 | 0.381 | 0.1718 | +0.2092 ± 0.0492 | 1.0454 | 0.5148 | 0.7445 | 0.2517 | 0.3014 | -0.073 ± 0.0465 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 442 | 0.1484 | 0.1501 | -0.0017 ± 0.0006 | 0.4543 | 0.4581 | 0.5257 | 0.5109 | 0.5566 | -0.004 ± 0.0186 | -0.0217 (6) |
| 3-5 | 297 | 0.1675 | 0.1652 | +0.0024 ± 0.0019 | 0.5013 | 0.4992 | 0.5278 | 0.4882 | 0.4781 | -0.062 ± 0.0241 | 0.02 (1) |
| 5-10 | 727 | 0.171 | 0.1727 | -0.0017 ± 0.0024 | 0.5168 | 0.5174 | 0.5213 | 0.4461 | 0.4897 | -0.013 ± 0.0156 | -0.01 (5) |
| 10-15 | 626 | 0.1881 | 0.1748 | +0.0133 ± 0.0042 | 0.5588 | 0.5151 | 0.5098 | 0.386 | 0.401 | -0.047 ± 0.0169 | -0.0575 (4) |
| 15-25 | 981 | 0.2044 | 0.1609 | +0.0435 ± 0.0051 | 0.5975 | 0.4802 | 0.515 | 0.3176 | 0.3109 | -0.073 ± 0.0129 | -0.0143 (7) |
| 25-40 | 899 | 0.2301 | 0.1202 | +0.1099 ± 0.0074 | 0.6628 | 0.3738 | 0.5419 | 0.2251 | 0.2113 | -0.068 ± 0.0118 | -0.015 (6) |
| 40+ | 805 | 0.412 | 0.0552 | +0.3568 ± 0.0096 | 1.0776 | 0.2083 | 0.6623 | 0.1225 | 0.0745 | -0.082 ± 0.0079 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 172 | 0.1877 | 0.1896 | -0.0019 ± 0.0012 | 0.5502 | 0.5557 | 0.5166 | 0.502 | 0.5349 | -0.051 ± 0.033 | -0.01 (5) |
| 3-5 | 114 | 0.1686 | 0.1654 | +0.0031 ± 0.0031 | 0.5088 | 0.5017 | 0.5051 | 0.4657 | 0.4474 | -0.123 ± 0.0408 | -- (0) |
| 5-10 | 217 | 0.1966 | 0.1953 | +0.0013 ± 0.0045 | 0.5821 | 0.5731 | 0.4981 | 0.425 | 0.447 | -0.073 ± 0.03 | -0.01 (3) |
| 10-15 | 182 | 0.2149 | 0.211 | +0.0039 ± 0.0085 | 0.6186 | 0.6066 | 0.5437 | 0.4202 | 0.4725 | -0.072 ± 0.0341 | -0.044 (5) |
| 15-25 | 235 | 0.2096 | 0.2013 | +0.0083 ± 0.0114 | 0.609 | 0.5827 | 0.5698 | 0.3749 | 0.4511 | -0.043 ± 0.0284 | -0.03 (1) |
| 25-40 | 133 | 0.2238 | 0.1966 | +0.0272 ± 0.0234 | 0.6395 | 0.5699 | 0.6252 | 0.3129 | 0.4211 | -0.051 ± 0.0353 | 0.0 (1) |
| 40+ | 25 | 0.3648 | 0.1373 | +0.2275 ± 0.0667 | 0.9712 | 0.4311 | 0.711 | 0.2606 | 0.24 | -0.185 ± 0.0761 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 554 | 0.1685 | 0.1687 | -0.0002 ± 0.0006 | 0.5066 | 0.5076 | 0.5044 | 0.4898 | 0.4982 | -0.049 ± 0.0174 | -0.0162 (13) |
| 3-5 | 382 | 0.1679 | 0.1639 | +0.0040 ± 0.0017 | 0.5069 | 0.4966 | 0.4917 | 0.4523 | 0.4267 | -0.085 ± 0.0211 | -0.01 (2) |
| 5-10 | 818 | 0.1823 | 0.1754 | +0.0070 ± 0.0022 | 0.5468 | 0.5214 | 0.4625 | 0.3889 | 0.379 | -0.064 ± 0.0147 | -0.01 (3) |
| 10-15 | 661 | 0.1882 | 0.1772 | +0.0110 ± 0.0041 | 0.558 | 0.5248 | 0.4831 | 0.3595 | 0.3782 | -0.045 ± 0.0164 | -0.03 (9) |
| 15-25 | 954 | 0.1861 | 0.1498 | +0.0362 ± 0.005 | 0.5604 | 0.4512 | 0.486 | 0.2862 | 0.2956 | -0.049 ± 0.0123 | -0.03 (2) |
| 25-40 | 830 | 0.2101 | 0.0975 | +0.1126 ± 0.0069 | 0.6126 | 0.3144 | 0.5028 | 0.184 | 0.1687 | -0.070 ± 0.0104 | 0.0 (1) |
| 40+ | 578 | 0.3891 | 0.034 | +0.3551 ± 0.0087 | 1.015 | 0.1506 | 0.6243 | 0.1022 | 0.0346 | -0.096 ± 0.0072 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 447 | 0.2019 | 0.2018 | +0.0001 ± 0.0007 | 0.5852 | 0.5852 | 0.4973 | 0.4827 | 0.4832 | -0.043 ± 0.0213 | -0.0226 (46) |
| 3-5 | 331 | 0.1955 | 0.1942 | +0.0014 ± 0.0019 | 0.5725 | 0.5664 | 0.4674 | 0.4277 | 0.435 | -0.041 ± 0.0241 | -0.0059 (32) |
| 5-10 | 682 | 0.1873 | 0.1827 | +0.0046 ± 0.0025 | 0.558 | 0.5452 | 0.4591 | 0.3857 | 0.3915 | -0.039 ± 0.0164 | -0.005 (72) |
| 10-15 | 460 | 0.2027 | 0.1911 | +0.0116 ± 0.0051 | 0.5946 | 0.5625 | 0.4583 | 0.335 | 0.35 | -0.035 ± 0.0203 | 0.0016 (63) |
| 15-25 | 616 | 0.2317 | 0.2087 | +0.0230 ± 0.0072 | 0.6567 | 0.6025 | 0.5273 | 0.3342 | 0.3718 | -0.024 ± 0.0184 | -0.0216 (58) |
| 25-40 | 309 | 0.263 | 0.1656 | +0.0974 ± 0.0145 | 0.729 | 0.4992 | 0.5723 | 0.2607 | 0.2589 | -0.067 ± 0.0228 | -0.0216 (25) |
| 40+ | 98 | 0.424 | 0.155 | +0.2689 ± 0.0426 | 1.187 | 0.48 | 0.7319 | 0.2239 | 0.2347 | -0.063 ± 0.0412 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 835 | 0.1909 | 0.1903 | +0.0006 ± 0.0005 | 0.5592 | 0.5574 | 0.4915 | 0.477 | 0.4635 | -0.054 ± 0.0151 | -0.0155 (82) |
| 3-5 | 607 | 0.1952 | 0.1933 | +0.0019 ± 0.0014 | 0.5701 | 0.5631 | 0.4712 | 0.4314 | 0.43 | -0.044 ± 0.0179 | -0.018 (54) |
| 5-10 | 1254 | 0.1849 | 0.1784 | +0.0065 ± 0.0018 | 0.552 | 0.5324 | 0.4435 | 0.3695 | 0.366 | -0.044 ± 0.012 | -0.0089 (122) |
| 10-15 | 936 | 0.1956 | 0.1821 | +0.0135 ± 0.0035 | 0.5773 | 0.5393 | 0.4481 | 0.3249 | 0.3323 | -0.037 ± 0.0138 | -0.0053 (99) |
| 15-25 | 1301 | 0.2188 | 0.1848 | +0.0340 ± 0.0047 | 0.6326 | 0.5427 | 0.5017 | 0.3062 | 0.3167 | -0.039 ± 0.0119 | -0.0255 (106) |
| 25-40 | 911 | 0.2406 | 0.125 | +0.1156 ± 0.0074 | 0.6813 | 0.3923 | 0.5266 | 0.2114 | 0.1866 | -0.072 ± 0.0115 | -0.0206 (47) |
| 40+ | 520 | 0.3873 | 0.0779 | +0.3094 ± 0.0134 | 1.056 | 0.2643 | 0.6504 | 0.1345 | 0.1038 | -0.073 ± 0.0125 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1078 | 1.141 ± 0.088 | 1.265 | 0.1699 | 0.1819 | 0.2061 | 0.194 |
| gen2 | 1078 | 0.927 ± 0.077 | 1.184 | 0.1856 | 0.1817 | 0.2257 | 0.1938 |
| gen1_elo | 1078 | 1.131 ± 0.086 | 1.216 | 0.1748 | 0.1823 | 0.2054 | 0.194 |
| gen1_sr | 1078 | 1.156 ± 0.102 | 1.24 | 0.1423 | 0.1836 | 0.2211 | 0.1936 |
| gen1_ledger | 2943 | 0.911 ± 0.05 | 1.073 | 0.1622 | 0.2011 | 0.218 | 0.1909 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 5,934)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,935 | 32.6% |
| STALE_QUOTE | market_freshness | 1,784 | 30.1% |
| BOOK_QUALITY | execution | 499 | 8.4% |
| POOR_DATA | data | 476 | 8.0% |
| LIMITED_DATA | data | 333 | 5.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 316 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 277 | 4.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 185 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 125 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |
| IDENTITY_OR_ORIENTATION_FAILURE | mapping | 1 | 0.0% |

Cause class: coverage 32.6%, market_freshness 30.1%, data 13.6%, market_freshness/coverage 8.4%, execution 8.4%, model_calibration_or_unknown 4.7%, mapping 2.1%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.7%, LOW_DATA_QUALITY 64.6%, STALE_KALSHI_QUOTE 62.8%, THIN_PLAYER_HISTORY 53.8%, STALE_PLAYER_DATA 52.7%, MODEL_INTERNAL_DISAGREEMENT 34.6%, ASYMMETRIC_SAMPLE_SIZE 29.3%, WIDE_SPREAD 17.0%, MODEL_HIGH_UNCERTAINTY 14.6%, PLAYER_IDENTITY_RISK 11.1%, LEVEL_TRANSFER_RISK 8.4%, EVENT_MAPPING_RISK 6.2%, LOW_DISPLAYED_LIQUIDITY 5.7%, MODEL_CALIBRATION_OUTLIER 1.9%, UNKNOWN 0.7%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 35.0%, POST_SETTLEMENT_OBSERVATION 32.6%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 1.0%

### >= ge_25 pp (N = 3,310)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,518 | 45.9% |
| STALE_QUOTE | market_freshness | 812 | 24.5% |
| BOOK_QUALITY | execution | 244 | 7.4% |
| POOR_DATA | data | 209 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 166 | 5.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 108 | 3.3% |
| LIMITED_DATA | data | 93 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 90 | 2.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 70 | 2.1% |

Cause class: coverage 45.9%, market_freshness 24.5%, data 9.1%, market_freshness/coverage 8.3%, execution 7.4%, mapping 2.7%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.0%, STALE_KALSHI_QUOTE 69.7%, LOW_DATA_QUALITY 68.2%, THIN_PLAYER_HISTORY 56.1%, STALE_PLAYER_DATA 50.3%, MODEL_INTERNAL_DISAGREEMENT 36.1%, ASYMMETRIC_SAMPLE_SIZE 32.2%, MODEL_HIGH_UNCERTAINTY 15.7%, WIDE_SPREAD 15.5%, PLAYER_IDENTITY_RISK 13.9%, LEVEL_TRANSFER_RISK 8.3%, EVENT_MAPPING_RISK 7.4%, LOW_DISPLAYED_LIQUIDITY 6.2%, MODEL_CALIBRATION_OUTLIER 2.8%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 48.3%, POST_SETTLEMENT_OBSERVATION 45.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 1.1%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2793, "IDENTITY_AMBIGUOUS": 517}; ticker orientation: {"VERIFIED": 3310}.

Checks: discipline:AMBIGUOUS 187, discipline:PASS 3123, identity_confidence:AMBIGUOUS 458, identity_confidence:PASS 2852, level_mapping:NA 199, level_mapping:PASS 3111, market_pair:AMBIGUOUS 88, market_pair:NA 86, market_pair:PASS 3136, model_complement:NA 55, model_complement:PASS 3255, namesake:AMBIGUOUS 1, namesake:PASS 3309, physical_match_id:NA 1510, physical_match_id:PASS 1800, player_ids:PASS 3310, same_pair_other_event:PASS 3310, ticker_orientation:PASS 3310

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 469 | 4.9% | 5.0% | 0.7% | {"market_freshness": 20, "execution": 3} | 6.67 | 0.1791 / 0.1823 (49) | 40.5% | 0.4% | 2.6% | 2.4% |
| CHALLENGER | 2,451 | 19.4% | 8.2% | 14.3% | {"coverage": 266, "market_freshness": 102, "market_freshness/coverage": 56, "data": 25, "model_calibration_or_unknown": 21, "execution": 5} | 7.56 | 0.2183 / 0.2024 (680) | 56.3% | 6.0% | 1.7% | 23.3% |
| DOUBLES | 391 | 47.8% | 47.7% | 5.7% | {"market_freshness": 106, "execution": 33, "mapping": 29, "market_freshness/coverage": 12, "coverage": 7} | 23.93 | 0.3208 / 0.2301 (163) | 59.9% | 0.0% | 100.0% | 10.0% |
| ITF_MEN | 4,053 | 25.9% | 14.9% | 31.7% | {"coverage": 560, "market_freshness": 194, "execution": 111, "data": 96, "market_freshness/coverage": 74, "mapping": 12, "model_calibration_or_unknown": 1} | 10.04 | 0.2148 / 0.1879 (1382) | 55.0% | 51.0% | 5.9% | 31.5% |
| ITF_WOMEN | 4,676 | 30.2% | 20.1% | 42.7% | {"coverage": 668, "market_freshness": 342, "data": 161, "market_freshness/coverage": 92, "execution": 83, "mapping": 47, "model_calibration_or_unknown": 21} | 13.08 | 0.2031 / 0.1848 (1355) | 58.4% | 59.5% | 9.2% | 30.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.4% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 810 | 9.4% | 8.1% | 2.3% | {"market_freshness": 34, "model_calibration_or_unknown": 13, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.63 | 0.2006 / 0.1964 (129) | 39.9% | 2.6% | 1.5% | 3.7% |
| WTA125 | 459 | 16.3% | 8.8% | 2.3% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 12, "coverage": 12, "data": 9} | 10.16 | 0.2273 / 0.204 (221) | 36.2% | 8.3% | 1.7% | 18.5% |

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
| 25 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 26 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 27 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 28 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 29 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 30 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 31 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 32 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 34 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 35 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 36 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 37 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 671 min (STALE); no external reference |
| 39 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 732 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 40 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 41 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 43 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 45 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 103 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.93); no external reference |
| 46 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 553 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 47 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 48 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 49 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 50 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9701, "by_level_share_of_ge_25pp": {"ATP": 0.0069, "CHALLENGER": 0.1435, "DOUBLES": 0.0565, "ITF_MEN": 0.3166, "ITF_WOMEN": 0.4272, "OTHER": 0.0036, "WTA": 0.023, "WTA125": 0.0227}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6973, "share_primary_cause_market_settled_or_in_play": 0.5414, "share_primary_cause_stale_quote_only": 0.2453}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 3310, "identity_ambiguous_share": 0.1562, "ticker_orientation": {"VERIFIED": 3310}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1800, "with_external": 10, "coverage": 0.0056, "external_status": {"EXTERNAL_STALE": 10}, "triangulation": {"INSUFFICIENT_INPUTS": 10}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 759, "with_external": 10, "coverage": 0.0132, "external_status": {"EXTERNAL_STALE": 10}, "triangulation": {"INSUFFICIENT_INPUTS": 10}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 766.0, "median_sample_ratio": 2.28, "median_min_matches": 23.0, "median_max_days_since_last": 182.0, "share_severe_asymmetry": 0.1819, "data_status": {"POOR": 1631, "LIMITED": 1003, "ADEQUATE": 676}, "comparison_lt_10pp": {"median_thinner_serve_points": 1889.0, "median_sample_ratio": 1.75, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 244, "model_minus_observed": 0.0953, "kalshi_minus_observed": -0.0355, "brier_diff_model_minus_kalshi": 0.0099}, "4-10x": {"n": 167, "model_minus_observed": 0.0963, "kalshi_minus_observed": -0.0426, "brier_diff_model_minus_kalshi": 0.0146}, "<2x": {"n": 495, "model_minus_observed": 0.0671, "kalshi_minus_observed": -0.0575, "brier_diff_model_minus_kalshi": 0.0117}, ">=10x": {"n": 172, "model_minus_observed": 0.0917, "kalshi_minus_observed": -0.0801, "brier_diff_model_minus_kalshi": 0.0138}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1078, "model": {"intercept": -0.62, "slope": 0.927, "slope_se": 0.077}, "kalshi_mid_same_rows": {"intercept": 0.235, "slope": 1.184, "slope_se": 0.087}, "mean_extremity_model": 0.1856, "mean_extremity_kalshi": 0.1817, "model_brier": 0.2257, "kalshi_brier": 0.1938, "brier_diff_model_minus_kalshi": 0.0319, "brier_diff_se": 0.0059, "model_logloss": 0.6442, "kalshi_logloss": 0.5665}, "fair_v1": {"n": 1078, "model": {"intercept": -0.413, "slope": 1.141, "slope_se": 0.088}, "kalshi_mid_same_rows": {"intercept": 0.381, "slope": 1.265, "slope_se": 0.09}, "mean_extremity_model": 0.1699, "mean_extremity_kalshi": 0.1819, "model_brier": 0.2061, "kalshi_brier": 0.194, "brier_diff_model_minus_kalshi": 0.0121, "brier_diff_se": 0.0046, "model_logloss": 0.5972, "kalshi_logloss": 0.567}, "gen1_elo": {"n": 1078, "model": {"intercept": -0.45, "slope": 1.131, "slope_se": 0.086}, "kalshi_mid_same_rows": {"intercept": 0.311, "slope": 1.216, "slope_se": 0.088}, "mean_extremity_model": 0.1748, "mean_extremity_kalshi": 0.1823, "model_brier": 0.2054, "kalshi_brier": 0.194, "brier_diff_model_minus_kalshi": 0.0114, "brier_diff_se": 0.0046, "model_logloss": 0.5974, "kalshi_logloss": 0.5668}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2685, "share_ge_15": 0.4547, "median_abs_gap": 13.34, "n": 6705}, "gen1_elo": {"share_ge_25": 0.2598, "share_ge_15": 0.4443, "median_abs_gap": 12.85, "n": 6705}, "gen1_sr": {"share_ge_25": 0.3199, "share_ge_15": 0.5386, "median_abs_gap": 16.57, "n": 6705}, "gen2": {"share_ge_25": 0.3216, "share_ge_15": 0.5235, "median_abs_gap": 15.98, "n": 6705}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1555, "share_ge_15": 0.3494, "median_abs_gap": 10.48, "n": 4880}, "gen1_elo": {"share_ge_25": 0.1539, "share_ge_15": 0.3342, "median_abs_gap": 9.77, "n": 4880}, "gen1_sr": {"share_ge_25": 0.209, "share_ge_15": 0.4434, "median_abs_gap": 13.3, "n": 4880}, "gen2": {"share_ge_25": 0.2268, "share_ge_15": 0.4436, "median_abs_gap": 13.04, "n": 4880}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.67, "share_ge_25_all": 0.049, "share_ge_25_pregame_clean": 0.0504}, "WTA": {"median_abs_gap_pregame_clean": 8.63, "share_ge_25_all": 0.0938, "share_ge_25_pregame_clean": 0.0808}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2204, "share_within_10pp_all": 0.4086, "share_within_10pp_pregame_clean": 0.4854, "corr_model_vs_mid_pregame_clean": 0.8301}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 169, "model_brier": 0.1788, "kalshi_brier": 0.18, "brier_diff_model_minus_kalshi": -0.0012}, "10-15": {"n_settled": 187, "model_brier": 0.2132, "kalshi_brier": 0.209, "brier_diff_model_minus_kalshi": 0.0042}, "15-25": {"n_settled": 239, "model_brier": 0.2161, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.0063}, "25-40": {"n_settled": 128, "model_brier": 0.2287, "kalshi_brier": 0.1819, "brier_diff_model_minus_kalshi": 0.0469}, "3-5": {"n_settled": 107, "model_brier": 0.1739, "kalshi_brier": 0.1739, "brier_diff_model_minus_kalshi": -0.0}, "40+": {"n_settled": 30, "model_brier": 0.3354, "kalshi_brier": 0.1357, "brier_diff_model_minus_kalshi": 0.1998}, "5-10": {"n_settled": 218, "model_brier": 0.195, "kalshi_brier": 0.1998, "brier_diff_model_minus_kalshi": -0.0047}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 163, "model_brier": 0.3208, "kalshi_brier": 0.2301, "brier_diff_model_minus_kalshi": 0.0907, "brier_diff_se": 0.0257, "corr_model_outcome": -0.1018, "corr_kalshi_outcome": 0.3278}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
