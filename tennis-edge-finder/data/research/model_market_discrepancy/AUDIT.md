# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-05T15:50Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 13,023): 0-3 13.1%, 3-5 8.9%, 5-10 18.8%, 10-15 15.0%, 15-25 19.6%, 25-40 14.9%, 40+ 9.5%; median gap 12.84 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.3%, Challenger 14.1%, doubles 5.8%). Main tour: ATP 5.8% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 3,187): MARKET_ALREADY_SETTLED_WHEN_PRICED 46.1%, STALE_QUOTE 25.2%, POOR_DATA 6.5%, BOOK_QUALITY 6.1%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IN_PLAY_QUOTE 3.3%, LIMITED_DATA 2.9%, IDENTITY_AMBIGUOUS 2.7%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 46.1%, market_freshness 25.2%, data 9.3%, market_freshness/coverage 8.5%, execution 6.1%, mapping 2.7%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 70.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 54.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 3,187 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 15.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.5%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.1% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 779.0 points vs 1888.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.141, Gen-2 0.926, Gen-1 ledger 0.91 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 124 model 0.2295 vs Kalshi 0.1852; n 30 model 0.3354 vs Kalshi 0.1357.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 42,444 model-market comparisons (74,498 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 17,698 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-05T15:45:47.044919+00:00'], shadow board 12,864 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-05T15:45:50.967161+00:00'], Model 4 3,323 rows, 8,652 settled tickers, 1,942 tickers with an external scan.
* By model: {"gen1_ledger": 10161, "gen1_elo": 6467, "fair_v1": 6467, "gen2": 6467, "gen1_sr": 6467, "model4_fundamental": 3212, "model4_conditioned": 3203}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 13,023 | 13.1 | 8.9 | 18.8 | 15.0 | 19.6 | 14.9 | 9.5 | 12.84 | 44.1% | 24.5% |
| MW fair_v1 | 6,467 | 13.1 | 8.3 | 18.0 | 15.3 | 18.8 | 15.7 | 10.9 | 13.29 | 45.4% | 26.6% |
| MW gen1_elo | 6,467 | 13.1 | 8.7 | 19.6 | 14.4 | 18.5 | 15.5 | 10.2 | 12.82 | 44.3% | 25.7% |
| MW gen1_ledger | 6,556 | 13.2 | 9.6 | 19.7 | 14.8 | 20.4 | 14.2 | 8.2 | 12.27 | 42.9% | 22.4% |
| MW gen1_sr | 6,467 | 9.2 | 7.1 | 16.1 | 13.6 | 22.1 | 18.9 | 12.9 | 16.59 | 53.9% | 31.8% |
| MW gen2 | 6,467 | 11.0 | 6.6 | 16.1 | 14.1 | 20.3 | 17.7 | 14.3 | 15.92 | 52.2% | 32.0% |
| all families model4_conditioned | 3,203 | 18.6 | 15.9 | 28.7 | 22.3 | 10.7 | 2.2 | 1.7 | 7.34 | 14.5% | 3.9% |
| all families model4_fundamental | 3,212 | 14.4 | 10.3 | 28.4 | 21.6 | 16.0 | 6.5 | 2.8 | 9.46 | 25.3% | 9.3% |

Configurable thresholds (primary): >=5pp 78.0%, >=10pp 59.1%, >=15pp 44.1%, >=20pp 33.5%, >=25pp 24.5%, >=30pp 17.9%, >=40pp 9.5%, >=50pp 4.3%
Executable gap (model outside the book, before fees): median 10.32pp; >=10pp 50.9%, >=25pp 21.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 328 | 20.1 | 14.9 | 24.7 | 15.8 | 17.4 | 3.7 | 3.4 | 7.36 | 24.4% | 7.0% |
| CHALLENGER | 1,395 | 15.6 | 10.6 | 16.7 | 16.1 | 15.6 | 13.7 | 11.8 | 12.62 | 41.1% | 25.5% |
| ITF_MEN | 1,843 | 11.8 | 8.1 | 19.2 | 14.5 | 18.1 | 15.5 | 12.8 | 13.25 | 46.4% | 28.3% |
| ITF_WOMEN | 2,363 | 9.7 | 5.9 | 15.5 | 15.3 | 21.5 | 20.5 | 11.6 | 16.53 | 53.6% | 32.1% |
| WTA | 435 | 23.0 | 10.6 | 25.8 | 12.6 | 18.9 | 6.7 | 2.5 | 8.16 | 28.1% | 9.2% |
| WTA125 | 103 | 13.6 | 3.9 | 16.5 | 28.2 | 17.5 | 12.6 | 7.8 | 12.85 | 37.9% | 20.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 328 | 19.2 | 12.8 | 23.8 | 15.6 | 19.5 | 5.5 | 3.7 | 8.77 | 28.7% | 9.2% |
| CHALLENGER | 1,395 | 14.1 | 6.2 | 18.4 | 14.4 | 19.1 | 16.2 | 11.5 | 13.87 | 46.8% | 27.7% |
| ITF_MEN | 1,843 | 9.1 | 6.8 | 17.3 | 15.3 | 20.0 | 17.2 | 14.3 | 15.55 | 51.5% | 31.5% |
| ITF_WOMEN | 2,363 | 8.1 | 6.0 | 12.5 | 12.3 | 20.8 | 20.7 | 19.5 | 19.92 | 61.1% | 40.2% |
| WTA | 435 | 20.5 | 5.5 | 16.8 | 15.6 | 22.3 | 16.8 | 2.5 | 12.98 | 41.6% | 19.3% |
| WTA125 | 103 | 5.8 | 4.8 | 14.6 | 18.4 | 22.3 | 19.4 | 14.6 | 19.08 | 56.3% | 34.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 328 | 25.6 | 12.8 | 28.7 | 9.8 | 10.4 | 9.2 | 3.7 | 7.4 | 23.2% | 12.8% |
| CHALLENGER | 1,395 | 16.1 | 10.0 | 22.1 | 13.4 | 13.2 | 12.9 | 12.2 | 10.53 | 38.3% | 25.1% |
| ITF_MEN | 1,843 | 10.4 | 8.9 | 18.1 | 15.2 | 19.1 | 15.6 | 12.7 | 13.68 | 47.4% | 28.3% |
| ITF_WOMEN | 2,363 | 9.7 | 6.2 | 16.1 | 14.1 | 23.7 | 20.3 | 9.9 | 17.17 | 54.0% | 30.2% |
| WTA | 435 | 23.4 | 14.0 | 29.4 | 15.6 | 11.5 | 4.4 | 1.6 | 6.99 | 17.5% | 6.0% |
| WTA125 | 103 | 14.6 | 5.8 | 21.4 | 32.0 | 15.5 | 8.7 | 1.9 | 12.01 | 26.2% | 10.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 996 | 20.9 | 14.6 | 25.2 | 15.8 | 14.2 | 6.6 | 2.8 | 7.45 | 23.6% | 9.4% |
| DOUBLES | 384 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.8 | 27.3 | 24.07 | 70.0% | 48.2% |
| ITF_MEN | 2,110 | 14.1 | 9.1 | 18.6 | 13.9 | 20.9 | 13.9 | 9.5 | 12.54 | 44.3% | 23.4% |
| ITF_WOMEN | 2,142 | 8.8 | 8.1 | 17.0 | 14.5 | 23.8 | 19.1 | 8.6 | 15.64 | 51.6% | 27.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 340 | 13.2 | 10.0 | 21.5 | 16.8 | 22.6 | 12.1 | 3.8 | 11.33 | 38.5% | 15.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 327 | 19.9 | 15.0 | 24.8 | 15.9 | 17.4 | 3.7 | 3.4 | 7.38 | 24.5% | 7.0% |
| CHALLENGER | 1,035 | 19.9 | 12.9 | 19.9 | 18.4 | 16.7 | 8.2 | 4.0 | 9.19 | 28.9% | 12.2% |
| ITF_MEN | 1,184 | 15.5 | 11.2 | 24.0 | 15.9 | 18.4 | 10.6 | 4.5 | 9.89 | 33.5% | 15.0% |
| ITF_WOMEN | 1,637 | 12.6 | 7.5 | 18.4 | 17.6 | 22.9 | 16.5 | 4.6 | 13.35 | 43.9% | 21.1% |
| WTA | 434 | 23.0 | 10.6 | 25.8 | 12.7 | 18.9 | 6.5 | 2.5 | 8.16 | 27.9% | 9.0% |
| WTA125 | 97 | 14.4 | 4.1 | 17.5 | 29.9 | 17.5 | 11.3 | 5.2 | 12.01 | 34.0% | 16.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 327 | 19.3 | 12.5 | 23.9 | 15.6 | 19.6 | 5.5 | 3.7 | 8.82 | 28.7% | 9.2% |
| CHALLENGER | 1,035 | 17.8 | 7.6 | 22.3 | 17.1 | 19.9 | 11.9 | 3.4 | 10.57 | 35.2% | 15.3% |
| ITF_MEN | 1,184 | 12.1 | 8.5 | 21.2 | 17.8 | 21.1 | 12.9 | 6.3 | 12.13 | 40.4% | 19.3% |
| ITF_WOMEN | 1,637 | 9.8 | 7.6 | 14.0 | 12.3 | 23.5 | 19.5 | 13.4 | 17.27 | 56.4% | 32.9% |
| WTA | 434 | 20.5 | 5.5 | 16.8 | 15.7 | 22.4 | 16.6 | 2.5 | 12.96 | 41.5% | 19.1% |
| WTA125 | 97 | 6.2 | 5.2 | 14.4 | 19.6 | 23.7 | 20.6 | 10.3 | 18.48 | 54.6% | 30.9% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 818 | 23.1 | 17.0 | 27.9 | 15.5 | 13.4 | 2.8 | 0.2 | 6.69 | 16.5% | 3.1% |
| DOUBLES | 345 | 5.8 | 3.8 | 10.1 | 10.4 | 21.7 | 21.2 | 27.0 | 24.1 | 69.9% | 48.1% |
| ITF_MEN | 1,501 | 17.3 | 10.9 | 21.7 | 15.1 | 20.9 | 10.5 | 3.6 | 10.03 | 35.0% | 14.1% |
| ITF_WOMEN | 1,483 | 10.7 | 9.6 | 20.3 | 16.5 | 24.8 | 15.9 | 2.2 | 12.49 | 43.0% | 18.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 334 | 15.6 | 9.9 | 26.4 | 23.1 | 18.3 | 6.9 | 0.0 | 9.55 | 25.1% | 6.9% |
| WTA125 | 261 | 15.7 | 11.1 | 25.7 | 19.9 | 21.1 | 6.1 | 0.4 | 9.33 | 27.6% | 6.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 384 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.8 | 27.3 | 24.07 | 70.0% | 48.2% |
| singles | 6,172 | 13.6 | 9.9 | 20.3 | 15.0 | 20.4 | 13.8 | 7.0 | 11.86 | 41.1% | 20.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,459 | 14.9 | 9.1 | 18.5 | 15.2 | 16.4 | 13.6 | 12.4 | 12.54 | 42.4% | 26.0% |
| Hard | 4,470 | 12.5 | 8.3 | 18.2 | 15.0 | 19.7 | 15.9 | 10.4 | 13.55 | 46.0% | 26.3% |
| UNKNOWN | 538 | 12.6 | 6.3 | 14.9 | 17.8 | 18.0 | 19.5 | 10.8 | 14.25 | 48.3% | 30.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,944 | 16.8 | 9.9 | 20.1 | 15.6 | 17.2 | 11.5 | 8.9 | 10.83 | 37.6% | 20.4% |
| B | 952 | 16.2 | 10.1 | 17.2 | 17.5 | 16.5 | 10.8 | 11.7 | 11.57 | 39.0% | 22.5% |
| C | 987 | 12.8 | 9.2 | 21.8 | 13.8 | 16.1 | 15.3 | 11.0 | 12.59 | 42.4% | 26.3% |
| D | 1,154 | 11.2 | 8.2 | 17.1 | 14.3 | 21.4 | 15.8 | 12.1 | 14.5 | 49.2% | 27.8% |
| F | 1,430 | 7.6 | 4.3 | 13.7 | 15.2 | 22.4 | 24.8 | 12.0 | 19.03 | 59.2% | 36.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,987 | 18.7 | 12.3 | 25.3 | 17.0 | 16.5 | 7.2 | 3.2 | 8.71 | 26.8% | 10.3% |
| B | 1,068 | 13.5 | 9.7 | 21.4 | 15.6 | 19.9 | 12.4 | 7.3 | 11.66 | 39.7% | 19.8% |
| C | 1,296 | 11.1 | 8.9 | 15.5 | 14.1 | 22.1 | 15.3 | 13.0 | 15.17 | 50.4% | 28.2% |
| D | 1,011 | 11.7 | 8.2 | 20.4 | 11.7 | 24.2 | 15.5 | 8.3 | 14.21 | 48.1% | 23.8% |
| F | 1,194 | 7.2 | 6.7 | 12.7 | 13.7 | 22.5 | 25.0 | 12.2 | 18.82 | 59.8% | 37.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 2,428 | 16.4 | 9.3 | 19.1 | 16.2 | 17.1 | 11.7 | 10.2 | 11.27 | 39.0% | 21.9% |
| LIMITED | 1,437 | 14.2 | 10.7 | 21.2 | 14.6 | 15.9 | 13.3 | 10.1 | 11.43 | 39.2% | 23.4% |
| POOR | 2,602 | 9.3 | 6.0 | 15.1 | 14.8 | 22.1 | 20.7 | 11.9 | 17.19 | 54.8% | 32.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 341 | 34.3 | 22.9 | 33.1 | 6.5 | 2.4 | 0.9 | 0.0 | 4.16 | 3.2% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 6,556 | 13.2 | 9.6 | 19.7 | 14.8 | 20.4 | 14.2 | 8.2 | 12.27 | 42.9% | 22.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,702 | 21.7 | 13.4 | 30.6 | 17.2 | 13.6 | 2.8 | 0.7 | 7.04 | 17.0% | 3.4% |
| TOTAL_GAMES | 1,132 | 9.9 | 9.4 | 26.5 | 24.9 | 17.0 | 8.0 | 4.4 | 10.66 | 29.3% | 12.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,148 | 26.8 | 30.5 | 24.5 | 0.6 | 15.6 | 1.5 | 0.5 | 4.47 | 17.6% | 2.0% |
| GAME_SPREAD | 628 | 35.7 | 15.3 | 26.4 | 17.8 | 2.4 | 1.8 | 0.6 | 4.68 | 4.8% | 2.4% |
| TOTAL_GAMES | 1,427 | 4.4 | 4.5 | 33.1 | 41.6 | 10.3 | 2.9 | 3.1 | 10.67 | 16.3% | 6.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,148 | 23.9 | 14.6 | 30.3 | 9.8 | 13.2 | 7.1 | 1.3 | 6.38 | 21.5% | 8.4% |
| GAME_SPREAD | 628 | 17.0 | 10.0 | 24.2 | 22.9 | 17.4 | 6.2 | 2.2 | 9.82 | 25.8% | 8.4% |
| TOTAL_GAMES | 1,436 | 5.7 | 7.0 | 28.8 | 30.4 | 17.6 | 6.3 | 4.2 | 10.98 | 28.1% | 10.5% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6,467 | 45.4% | 26.6% | 13.29 | 35.0% | 15.4% | 10.48 |
| gen1_elo | 6,467 | 44.3% | 25.7% | 12.82 | 33.3% | 15.2% | 9.71 |
| gen1_sr | 6,467 | 53.9% | 31.8% | 16.59 | 44.6% | 20.9% | 13.37 |
| gen2 | 6,467 | 52.2% | 32.0% | 15.92 | 44.4% | 22.6% | 13.07 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 2,344 | 17.1 | 11.4 | 22.4 | 15.6 | 19.2 | 10.9 | 3.5 | 9.83 | 33.5% | 14.3% |
| STALE | 4,123 | 10.8 | 6.5 | 15.5 | 15.1 | 18.6 | 18.4 | 15.1 | 16.24 | 52.2% | 33.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 24 | 25.0 | 8.3 | 8.3 | 16.7 | 16.7 | 25.0 | 0.0 | 11.21 | 41.7% | 25.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 13,023 | 24 | 5816 | 7183 | 32.0 | 222.5 | 1400.4 |
| ge_15pp | 5,745 | 10 | 2074 | 3661 | 39.8 | 479.1 | 1380.4 |
| ge_25pp | 3,187 | 6 | 927 | 2254 | 53.8 | 609.3 | 1380.4 |
| lt_10pp | 5,321 | 10 | 2825 | 2486 | 29.1 | 60.7 | 1201.9 |

Current slate `SL-20261005T155056Z-4c7d0dd4`: 234 priced rows, quote age at build {'median': 5.7, 'max': 5.7}, freshness {'FRESH': 234}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 147 | 23.1 | 12.2 | 19.1 | 20.4 | 19.7 | 4.8 | 0.7 | 7.69 | 25.2% | 5.4% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 8.3 | 50.0 | 41.7 | 0.0 | 0.0 | 14.32 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 6,467 | 168 (2.6%) | 7.1% | 0.0% | {"EXTERNAL_STALE": 147, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,936 | 42 (1.4%) | 11.9% | 0.0% | {"EXTERNAL_STALE": 37, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,719 | 8 (0.5%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 8} |
| fair_v1_ge_25pp_pregame_clean | 727 | 8 (1.1%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 8} |
| fair_v1_lt_10pp | 2,542 | 90 (3.5%) | 1.1% | 0.0% | {"EXTERNAL_STALE": 80, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,305 | 12.2 | 7.2 | 19.9 | 16.4 | 20.0 | 14.8 | 9.5 | 12.82 | 44.3% | 24.3% |
| 4-10x | 875 | 12.7 | 10.9 | 17.0 | 14.2 | 17.6 | 17.1 | 10.5 | 13.45 | 45.3% | 27.7% |
| <2x | 3,478 | 14.1 | 8.9 | 18.4 | 15.2 | 18.5 | 13.8 | 11.2 | 12.78 | 43.4% | 25.0% |
| >=10x | 809 | 10.4 | 4.7 | 14.1 | 15.1 | 19.6 | 23.7 | 12.4 | 17.69 | 55.8% | 36.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,785 | 14.2 | 8.7 | 19.9 | 16.0 | 16.8 | 12.5 | 11.9 | 12.01 | 41.2% | 24.4% |
| 300-1000 | 1,512 | 13.0 | 8.5 | 16.9 | 15.5 | 20.3 | 15.5 | 10.3 | 13.67 | 46.2% | 25.9% |
| <300 | 1,664 | 8.3 | 5.3 | 14.4 | 14.1 | 21.8 | 23.6 | 12.6 | 18.88 | 57.9% | 36.2% |
| >=3000 | 1,506 | 16.9 | 10.9 | 20.8 | 15.6 | 16.5 | 11.0 | 8.3 | 10.41 | 35.8% | 19.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 243 | 0.5172 | 0.3862 | 0.4239 | +0.093 | -0.038 | 0.0097 ± 0.0091 |
| ratio 4-10x | 164 | 0.5716 | 0.4317 | 0.4756 | +0.096 | -0.044 | 0.0142 ± 0.0117 |
| ratio <2x | 490 | 0.5353 | 0.412 | 0.4694 | +0.066 | -0.057 | 0.0113 ± 0.0064 |
| ratio >=10x | 171 | 0.5513 | 0.3807 | 0.462 | +0.089 | -0.081 | 0.0124 ± 0.0144 |
| thinner_sample 1000-3000 | 288 | 0.5391 | 0.4197 | 0.4549 | +0.084 | -0.035 | 0.0088 ± 0.0082 |
| thinner_sample 300-1000 | 286 | 0.5515 | 0.4204 | 0.4685 | +0.083 | -0.048 | 0.0064 ± 0.0085 |
| thinner_sample <300 | 353 | 0.5368 | 0.3706 | 0.4533 | +0.084 | -0.083 | 0.0169 ± 0.0094 |
| thinner_sample >=3000 | 141 | 0.5214 | 0.4236 | 0.461 | +0.060 | -0.037 | 0.0144 ± 0.0095 |
| data_status ADEQUATE | 314 | 0.5279 | 0.4192 | 0.4554 | +0.072 | -0.036 | 0.0078 ± 0.0071 |
| data_status LIMITED | 219 | 0.5543 | 0.4292 | 0.4886 | +0.066 | -0.059 | 0.0044 ± 0.0099 |
| data_status POOR | 535 | 0.5399 | 0.3851 | 0.4486 | +0.091 | -0.064 | 0.0167 ± 0.0071 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 169 | 0.1788 | 0.18 | -0.0012 ± 0.0011 | 0.5307 | 0.5341 | 0.4917 | 0.4773 | 0.503 | -0.077 ± 0.0349 | -0.01 (3) |
| 3-5 | 106 | 0.1755 | 0.1754 | +0.0001 ± 0.0034 | 0.5305 | 0.5268 | 0.5138 | 0.4728 | 0.4906 | -0.072 ± 0.0429 | 0.02 (1) |
| 5-10 | 216 | 0.1946 | 0.1993 | -0.0047 ± 0.0045 | 0.5741 | 0.5838 | 0.513 | 0.4388 | 0.5 | -0.041 ± 0.0304 | -0.0167 (3) |
| 10-15 | 186 | 0.2106 | 0.2074 | +0.0032 ± 0.0083 | 0.605 | 0.5952 | 0.5173 | 0.3939 | 0.4409 | -0.066 ± 0.0333 | -0.0633 (3) |
| 15-25 | 237 | 0.2163 | 0.21 | +0.0063 ± 0.0117 | 0.6203 | 0.6046 | 0.5581 | 0.3614 | 0.4473 | -0.031 ± 0.0295 | -0.02 (4) |
| 25-40 | 124 | 0.2295 | 0.1852 | +0.0444 ± 0.0237 | 0.6483 | 0.5421 | 0.6276 | 0.3155 | 0.3952 | -0.073 ± 0.036 | -0.01 (1) |
| 40+ | 30 | 0.3354 | 0.1357 | +0.1998 ± 0.0606 | 0.9067 | 0.4279 | 0.7106 | 0.2678 | 0.2667 | -0.167 ± 0.0655 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 544 | 0.1608 | 0.1621 | -0.0013 ± 0.0006 | 0.487 | 0.4901 | 0.5025 | 0.4876 | 0.5349 | -0.014 ± 0.0178 | -0.0188 (8) |
| 3-5 | 349 | 0.1712 | 0.1701 | +0.0011 ± 0.0018 | 0.5187 | 0.5112 | 0.4784 | 0.4384 | 0.447 | -0.047 ± 0.0225 | 0.02 (1) |
| 5-10 | 796 | 0.1781 | 0.1784 | -0.0004 ± 0.0022 | 0.5356 | 0.5335 | 0.4758 | 0.4019 | 0.4397 | -0.019 ± 0.015 | -0.0129 (7) |
| 10-15 | 689 | 0.1842 | 0.1718 | +0.0125 ± 0.0039 | 0.5482 | 0.5067 | 0.4722 | 0.3488 | 0.3585 | -0.052 ± 0.0158 | -0.0633 (3) |
| 15-25 | 893 | 0.1971 | 0.162 | +0.0351 ± 0.0054 | 0.5829 | 0.4813 | 0.4798 | 0.2817 | 0.2923 | -0.048 ± 0.0134 | -0.017 (10) |
| 25-40 | 828 | 0.2104 | 0.0986 | +0.1118 ± 0.0069 | 0.6125 | 0.3192 | 0.5081 | 0.1929 | 0.1751 | -0.070 ± 0.0106 | -0.01 (1) |
| 40+ | 587 | 0.3741 | 0.0336 | +0.3406 ± 0.0083 | 0.9728 | 0.149 | 0.6181 | 0.1029 | 0.0392 | -0.094 ± 0.007 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 110 | 0.173 | 0.1746 | -0.0016 ± 0.0014 | 0.5162 | 0.5181 | 0.5067 | 0.4917 | 0.5364 | -0.045 ± 0.0398 | -0.01 (1) |
| 3-5 | 83 | 0.1999 | 0.1985 | +0.0014 ± 0.0039 | 0.5774 | 0.5799 | 0.4998 | 0.4605 | 0.4578 | -0.082 ± 0.0518 | 0.02 (1) |
| 5-10 | 202 | 0.1848 | 0.1855 | -0.0008 ± 0.0046 | 0.5512 | 0.5514 | 0.5691 | 0.4939 | 0.5297 | -0.067 ± 0.0311 | -0.01 (4) |
| 10-15 | 175 | 0.22 | 0.2085 | +0.0115 ± 0.0088 | 0.6278 | 0.6023 | 0.5807 | 0.4563 | 0.48 | -0.085 ± 0.0355 | -0.0667 (3) |
| 15-25 | 267 | 0.2237 | 0.199 | +0.0247 ± 0.0109 | 0.6338 | 0.5758 | 0.5816 | 0.3841 | 0.427 | -0.082 ± 0.0284 | -0.0167 (3) |
| 25-40 | 159 | 0.2651 | 0.2006 | +0.0645 ± 0.022 | 0.7346 | 0.5822 | 0.6517 | 0.3405 | 0.3899 | -0.097 ± 0.0373 | -0.025 (2) |
| 40+ | 72 | 0.3808 | 0.1738 | +0.2069 ± 0.0498 | 1.046 | 0.5196 | 0.7461 | 0.253 | 0.3056 | -0.070 ± 0.0471 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 437 | 0.1496 | 0.1513 | -0.0017 ± 0.0006 | 0.4569 | 0.4607 | 0.5251 | 0.5104 | 0.5561 | -0.004 ± 0.0188 | -0.0217 (6) |
| 3-5 | 294 | 0.167 | 0.1649 | +0.0021 ± 0.0019 | 0.5002 | 0.4989 | 0.5291 | 0.4895 | 0.483 | -0.059 ± 0.0243 | 0.02 (1) |
| 5-10 | 719 | 0.1723 | 0.1741 | -0.0018 ± 0.0024 | 0.5197 | 0.5207 | 0.5234 | 0.4482 | 0.4924 | -0.012 ± 0.0157 | -0.01 (5) |
| 10-15 | 623 | 0.1877 | 0.1748 | +0.0130 ± 0.0042 | 0.558 | 0.5154 | 0.5103 | 0.3865 | 0.4029 | -0.046 ± 0.017 | -0.0575 (4) |
| 15-25 | 964 | 0.2043 | 0.1611 | +0.0433 ± 0.0052 | 0.5973 | 0.4806 | 0.5147 | 0.3174 | 0.3112 | -0.072 ± 0.013 | -0.0143 (7) |
| 25-40 | 875 | 0.2313 | 0.1218 | +0.1095 ± 0.0075 | 0.6656 | 0.378 | 0.5446 | 0.2278 | 0.2149 | -0.068 ± 0.0121 | -0.015 (6) |
| 40+ | 774 | 0.412 | 0.0567 | +0.3553 ± 0.0099 | 1.0785 | 0.2117 | 0.6634 | 0.1229 | 0.0775 | -0.079 ± 0.0082 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 172 | 0.1877 | 0.1896 | -0.0019 ± 0.0012 | 0.5502 | 0.5557 | 0.5166 | 0.502 | 0.5349 | -0.051 ± 0.033 | -0.01 (5) |
| 3-5 | 112 | 0.1689 | 0.166 | +0.0029 ± 0.0031 | 0.5103 | 0.5034 | 0.501 | 0.4617 | 0.4464 | -0.117 ± 0.0408 | -- (0) |
| 5-10 | 215 | 0.1968 | 0.1954 | +0.0014 ± 0.0045 | 0.5825 | 0.5733 | 0.4981 | 0.4251 | 0.4465 | -0.072 ± 0.0302 | -0.01 (3) |
| 10-15 | 181 | 0.2121 | 0.2094 | +0.0027 ± 0.0085 | 0.6118 | 0.6032 | 0.542 | 0.4187 | 0.4751 | -0.069 ± 0.0341 | -0.044 (5) |
| 15-25 | 234 | 0.21 | 0.201 | +0.0090 ± 0.0114 | 0.6099 | 0.5821 | 0.5694 | 0.3744 | 0.4487 | -0.045 ± 0.0284 | -0.03 (1) |
| 25-40 | 130 | 0.2249 | 0.1988 | +0.0261 ± 0.0238 | 0.6419 | 0.5751 | 0.6264 | 0.3139 | 0.4231 | -0.049 ± 0.036 | 0.0 (1) |
| 40+ | 24 | 0.3687 | 0.1424 | +0.2263 ± 0.0696 | 0.9809 | 0.4437 | 0.7189 | 0.2665 | 0.25 | -0.186 ± 0.0793 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 548 | 0.1689 | 0.1691 | -0.0003 ± 0.0006 | 0.5078 | 0.509 | 0.5072 | 0.4927 | 0.5018 | -0.049 ± 0.0175 | -0.0162 (13) |
| 3-5 | 377 | 0.1684 | 0.1642 | +0.0042 ± 0.0017 | 0.5084 | 0.4975 | 0.4886 | 0.4493 | 0.4218 | -0.086 ± 0.0212 | -0.01 (2) |
| 5-10 | 810 | 0.1826 | 0.1758 | +0.0068 ± 0.0022 | 0.5473 | 0.5223 | 0.4625 | 0.3889 | 0.3802 | -0.062 ± 0.0148 | -0.01 (3) |
| 10-15 | 658 | 0.1878 | 0.1772 | +0.0106 ± 0.0041 | 0.5569 | 0.5249 | 0.4833 | 0.3597 | 0.3799 | -0.044 ± 0.0164 | -0.03 (9) |
| 15-25 | 941 | 0.187 | 0.1509 | +0.0361 ± 0.0051 | 0.5624 | 0.4538 | 0.4866 | 0.287 | 0.2965 | -0.049 ± 0.0124 | -0.03 (2) |
| 25-40 | 803 | 0.2104 | 0.0986 | +0.1118 ± 0.007 | 0.6133 | 0.317 | 0.5035 | 0.1854 | 0.1706 | -0.070 ± 0.0106 | 0.0 (1) |
| 40+ | 549 | 0.3883 | 0.035 | +0.3532 ± 0.009 | 1.013 | 0.1528 | 0.6243 | 0.1022 | 0.0364 | -0.095 ± 0.0075 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 445 | 0.2022 | 0.2021 | +0.0001 ± 0.0007 | 0.5858 | 0.5858 | 0.498 | 0.4834 | 0.4854 | -0.041 ± 0.0214 | -0.0226 (46) |
| 3-5 | 331 | 0.1955 | 0.1942 | +0.0014 ± 0.0019 | 0.5725 | 0.5664 | 0.4674 | 0.4277 | 0.435 | -0.041 ± 0.0241 | -0.0059 (32) |
| 5-10 | 681 | 0.1866 | 0.1822 | +0.0044 ± 0.0025 | 0.5565 | 0.5443 | 0.4586 | 0.3853 | 0.3921 | -0.038 ± 0.0164 | -0.005 (72) |
| 10-15 | 458 | 0.2029 | 0.1917 | +0.0113 ± 0.0051 | 0.5951 | 0.5636 | 0.4587 | 0.3354 | 0.3515 | -0.034 ± 0.0203 | 0.0016 (63) |
| 15-25 | 615 | 0.2319 | 0.2086 | +0.0233 ± 0.0072 | 0.6572 | 0.6023 | 0.5271 | 0.3339 | 0.3707 | -0.024 ± 0.0184 | -0.0216 (58) |
| 25-40 | 306 | 0.2634 | 0.1671 | +0.0964 ± 0.0146 | 0.73 | 0.5029 | 0.5733 | 0.2622 | 0.2614 | -0.066 ± 0.023 | -0.0216 (25) |
| 40+ | 97 | 0.4256 | 0.1565 | +0.2690 ± 0.0431 | 1.1917 | 0.4837 | 0.7341 | 0.2251 | 0.2371 | -0.062 ± 0.0416 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 833 | 0.191 | 0.1904 | +0.0006 ± 0.0005 | 0.5595 | 0.5577 | 0.4919 | 0.4773 | 0.4646 | -0.053 ± 0.0151 | -0.0155 (82) |
| 3-5 | 607 | 0.1952 | 0.1933 | +0.0019 ± 0.0014 | 0.5701 | 0.5631 | 0.4712 | 0.4314 | 0.43 | -0.044 ± 0.0179 | -0.018 (54) |
| 5-10 | 1252 | 0.1845 | 0.1782 | +0.0063 ± 0.0018 | 0.5511 | 0.5318 | 0.4431 | 0.3692 | 0.3666 | -0.043 ± 0.012 | -0.0089 (122) |
| 10-15 | 933 | 0.1957 | 0.1825 | +0.0132 ± 0.0035 | 0.5774 | 0.54 | 0.4483 | 0.325 | 0.3333 | -0.036 ± 0.0139 | -0.0053 (99) |
| 15-25 | 1298 | 0.2189 | 0.1849 | +0.0340 ± 0.0047 | 0.6329 | 0.543 | 0.5017 | 0.3062 | 0.3166 | -0.039 ± 0.012 | -0.0255 (106) |
| 25-40 | 906 | 0.2407 | 0.1256 | +0.1152 ± 0.0074 | 0.6815 | 0.3938 | 0.527 | 0.2119 | 0.1876 | -0.071 ± 0.0116 | -0.0206 (47) |
| 40+ | 517 | 0.3873 | 0.0782 | +0.3091 ± 0.0135 | 1.0562 | 0.2649 | 0.6506 | 0.1344 | 0.1044 | -0.072 ± 0.0125 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1068 | 1.141 ± 0.089 | 1.265 | 0.1702 | 0.1819 | 0.2058 | 0.1942 |
| gen2 | 1068 | 0.926 ± 0.078 | 1.183 | 0.1855 | 0.1816 | 0.2254 | 0.194 |
| gen1_elo | 1068 | 1.131 ± 0.087 | 1.215 | 0.1751 | 0.1823 | 0.2052 | 0.1942 |
| gen1_sr | 1068 | 1.155 ± 0.102 | 1.24 | 0.1422 | 0.1836 | 0.2209 | 0.1938 |
| gen1_ledger | 2933 | 0.91 ± 0.05 | 1.073 | 0.1623 | 0.2008 | 0.2179 | 0.1911 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 5,745)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,881 | 32.7% |
| STALE_QUOTE | market_freshness | 1,765 | 30.7% |
| POOR_DATA | data | 468 | 8.2% |
| BOOK_QUALITY | execution | 411 | 7.1% |
| LIMITED_DATA | data | 331 | 5.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 313 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 271 | 4.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 181 | 3.1% |
| IDENTITY_AMBIGUOUS | mapping | 121 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 32.7%, market_freshness 30.7%, data 13.9%, market_freshness/coverage 8.6%, execution 7.1%, model_calibration_or_unknown 4.7%, mapping 2.1%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.7%, LOW_DATA_QUALITY 64.2%, STALE_KALSHI_QUOTE 63.7%, THIN_PLAYER_HISTORY 53.2%, STALE_PLAYER_DATA 52.3%, MODEL_INTERNAL_DISAGREEMENT 34.3%, ASYMMETRIC_SAMPLE_SIZE 28.9%, WIDE_SPREAD 15.8%, MODEL_HIGH_UNCERTAINTY 14.8%, PLAYER_IDENTITY_RISK 11.0%, LEVEL_TRANSFER_RISK 8.4%, EVENT_MAPPING_RISK 6.0%, LOW_DISPLAYED_LIQUIDITY 5.5%, MODEL_CALIBRATION_OUTLIER 1.9%, UNKNOWN 0.7%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 35.1%, POST_SETTLEMENT_OBSERVATION 32.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 1.0%

### >= ge_25 pp (N = 3,187)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,468 | 46.1% |
| STALE_QUOTE | market_freshness | 802 | 25.2% |
| POOR_DATA | data | 207 | 6.5% |
| BOOK_QUALITY | execution | 193 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 165 | 5.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 106 | 3.3% |
| LIMITED_DATA | data | 91 | 2.9% |
| IDENTITY_AMBIGUOUS | mapping | 87 | 2.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 68 | 2.1% |

Cause class: coverage 46.1%, market_freshness 25.2%, data 9.3%, market_freshness/coverage 8.5%, execution 6.1%, mapping 2.7%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.9%, STALE_KALSHI_QUOTE 70.7%, LOW_DATA_QUALITY 67.8%, THIN_PLAYER_HISTORY 55.4%, STALE_PLAYER_DATA 50.0%, MODEL_INTERNAL_DISAGREEMENT 35.7%, ASYMMETRIC_SAMPLE_SIZE 31.7%, MODEL_HIGH_UNCERTAINTY 16.0%, WIDE_SPREAD 14.3%, PLAYER_IDENTITY_RISK 13.8%, LEVEL_TRANSFER_RISK 8.4%, EVENT_MAPPING_RISK 7.2%, LOW_DISPLAYED_LIQUIDITY 6.1%, MODEL_CALIBRATION_OUTLIER 2.7%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 48.5%, POST_SETTLEMENT_OBSERVATION 46.1%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 1.2%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2703, "IDENTITY_AMBIGUOUS": 484}; ticker orientation: {"VERIFIED": 3187}.

Checks: discipline:AMBIGUOUS 185, discipline:PASS 3002, identity_confidence:AMBIGUOUS 438, identity_confidence:PASS 2749, level_mapping:NA 197, level_mapping:PASS 2990, market_pair:AMBIGUOUS 75, market_pair:NA 85, market_pair:PASS 3027, model_complement:NA 54, model_complement:PASS 3133, namesake:AMBIGUOUS 1, namesake:PASS 3186, physical_match_id:NA 1468, physical_match_id:PASS 1719, player_ids:PASS 3187, same_pair_other_event:PASS 3187, ticker_orientation:PASS 3187

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 400 | 5.8% | 5.9% | 0.7% | {"market_freshness": 20, "execution": 3} | 7.02 | 0.1791 / 0.1823 (49) | 45.2% | 0.0% | 0.8% | 2.8% |
| CHALLENGER | 2,391 | 18.8% | 8.2% | 14.1% | {"coverage": 246, "market_freshness": 101, "market_freshness/coverage": 53, "data": 24, "model_calibration_or_unknown": 20, "execution": 5, "mapping": 1} | 7.56 | 0.2178 / 0.2027 (670) | 56.5% | 5.9% | 1.7% | 22.5% |
| DOUBLES | 384 | 48.2% | 48.1% | 5.8% | {"market_freshness": 106, "execution": 32, "mapping": 28, "market_freshness/coverage": 12, "coverage": 7} | 24.1 | 0.3208 / 0.2301 (163) | 60.9% | 0.0% | 100.0% | 10.2% |
| ITF_MEN | 3,953 | 25.7% | 14.5% | 31.8% | {"coverage": 551, "market_freshness": 194, "data": 96, "execution": 88, "market_freshness/coverage": 74, "mapping": 10, "model_calibration_or_unknown": 1} | 9.95 | 0.2148 / 0.1882 (1380) | 55.9% | 50.3% | 5.4% | 32.1% |
| ITF_WOMEN | 4,505 | 30.0% | 19.7% | 42.4% | {"coverage": 647, "market_freshness": 333, "data": 158, "market_freshness/coverage": 92, "execution": 56, "mapping": 46, "model_calibration_or_unknown": 21} | 12.98 | 0.2031 / 0.1851 (1347) | 59.5% | 58.9% | 8.9% | 30.7% |
| OTHER | 149 | 8.1% | 7.3% | 0.4% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 798 | 9.4% | 8.1% | 2.4% | {"market_freshness": 34, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.66 | 0.2006 / 0.1964 (129) | 40.5% | 2.6% | 1.5% | 3.8% |
| WTA125 | 443 | 16.9% | 9.2% | 2.4% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 12, "coverage": 12, "data": 9} | 10.39 | 0.2273 / 0.204 (221) | 36.1% | 8.6% | 1.4% | 19.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 5 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 6 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 7 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 9 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 11 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 12 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 14 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 15 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 16 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 17 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 18 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 19 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 20 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 21 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 23 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 24 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 25 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 26 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 27 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 28 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 29 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 30 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 31 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 32 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 708 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 33 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
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
| 45 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +69 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 42 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 4.16); no external reference |
| 46 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 86 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 47 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 48 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 49 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 50 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9692, "by_level_share_of_ge_25pp": {"ATP": 0.0072, "CHALLENGER": 0.1412, "DOUBLES": 0.058, "ITF_MEN": 0.3182, "ITF_WOMEN": 0.4245, "OTHER": 0.0038, "WTA": 0.0235, "WTA125": 0.0235}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.7072, "share_primary_cause_market_settled_or_in_play": 0.5457, "share_primary_cause_stale_quote_only": 0.2516}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 3187, "identity_ambiguous_share": 0.1519, "ticker_orientation": {"VERIFIED": 3187}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1719, "with_external": 8, "coverage": 0.0047, "external_status": {"EXTERNAL_STALE": 8}, "triangulation": {"INSUFFICIENT_INPUTS": 8}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 727, "with_external": 8, "coverage": 0.011, "external_status": {"EXTERNAL_STALE": 8}, "triangulation": {"INSUFFICIENT_INPUTS": 8}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 779.0, "median_sample_ratio": 2.27, "median_min_matches": 24.0, "median_max_days_since_last": 178.0, "share_severe_asymmetry": 0.1804, "data_status": {"POOR": 1547, "LIMITED": 985, "ADEQUATE": 655}, "comparison_lt_10pp": {"median_thinner_serve_points": 1888.0, "median_sample_ratio": 1.76, "median_min_matches": 77.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 243, "model_minus_observed": 0.0934, "kalshi_minus_observed": -0.0377, "brier_diff_model_minus_kalshi": 0.0097}, "4-10x": {"n": 164, "model_minus_observed": 0.096, "kalshi_minus_observed": -0.0439, "brier_diff_model_minus_kalshi": 0.0142}, "<2x": {"n": 490, "model_minus_observed": 0.0659, "kalshi_minus_observed": -0.0574, "brier_diff_model_minus_kalshi": 0.0113}, ">=10x": {"n": 171, "model_minus_observed": 0.0893, "kalshi_minus_observed": -0.0813, "brier_diff_model_minus_kalshi": 0.0124}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1068, "model": {"intercept": -0.613, "slope": 0.926, "slope_se": 0.078}, "kalshi_mid_same_rows": {"intercept": 0.238, "slope": 1.183, "slope_se": 0.087}, "mean_extremity_model": 0.1855, "mean_extremity_kalshi": 0.1816, "model_brier": 0.2254, "kalshi_brier": 0.194, "brier_diff_model_minus_kalshi": 0.0314, "brier_diff_se": 0.0059, "model_logloss": 0.6435, "kalshi_logloss": 0.5671}, "fair_v1": {"n": 1068, "model": {"intercept": -0.406, "slope": 1.141, "slope_se": 0.089}, "kalshi_mid_same_rows": {"intercept": 0.386, "slope": 1.265, "slope_se": 0.091}, "mean_extremity_model": 0.1702, "mean_extremity_kalshi": 0.1819, "model_brier": 0.2058, "kalshi_brier": 0.1942, "brier_diff_model_minus_kalshi": 0.0116, "brier_diff_se": 0.0046, "model_logloss": 0.5965, "kalshi_logloss": 0.5676}, "gen1_elo": {"n": 1068, "model": {"intercept": -0.443, "slope": 1.131, "slope_se": 0.087}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.215, "slope_se": 0.088}, "mean_extremity_model": 0.1751, "mean_extremity_kalshi": 0.1823, "model_brier": 0.2052, "kalshi_brier": 0.1942, "brier_diff_model_minus_kalshi": 0.011, "brier_diff_se": 0.0046, "model_logloss": 0.5969, "kalshi_logloss": 0.5674}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2658, "share_ge_15": 0.454, "median_abs_gap": 13.29, "n": 6467}, "gen1_elo": {"share_ge_25": 0.2573, "share_ge_15": 0.4426, "median_abs_gap": 12.82, "n": 6467}, "gen1_sr": {"share_ge_25": 0.3179, "share_ge_15": 0.5392, "median_abs_gap": 16.59, "n": 6467}, "gen2": {"share_ge_25": 0.3198, "share_ge_15": 0.5223, "median_abs_gap": 15.92, "n": 6467}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1542, "share_ge_15": 0.3496, "median_abs_gap": 10.48, "n": 4714}, "gen1_elo": {"share_ge_25": 0.1525, "share_ge_15": 0.3333, "median_abs_gap": 9.71, "n": 4714}, "gen1_sr": {"share_ge_25": 0.2087, "share_ge_15": 0.4457, "median_abs_gap": 13.37, "n": 4714}, "gen2": {"share_ge_25": 0.2263, "share_ge_15": 0.4438, "median_abs_gap": 13.07, "n": 4714}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 7.02, "share_ge_25_all": 0.0575, "share_ge_25_pregame_clean": 0.0591}, "WTA": {"median_abs_gap_pregame_clean": 8.66, "share_ge_25_all": 0.094, "share_ge_25_pregame_clean": 0.0807}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2202, "share_within_10pp_all": 0.4086, "share_within_10pp_pregame_clean": 0.4859, "corr_model_vs_mid_pregame_clean": 0.8304}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 169, "model_brier": 0.1788, "kalshi_brier": 0.18, "brier_diff_model_minus_kalshi": -0.0012}, "10-15": {"n_settled": 186, "model_brier": 0.2106, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.0032}, "15-25": {"n_settled": 237, "model_brier": 0.2163, "kalshi_brier": 0.21, "brier_diff_model_minus_kalshi": 0.0063}, "25-40": {"n_settled": 124, "model_brier": 0.2295, "kalshi_brier": 0.1852, "brier_diff_model_minus_kalshi": 0.0444}, "3-5": {"n_settled": 106, "model_brier": 0.1755, "kalshi_brier": 0.1754, "brier_diff_model_minus_kalshi": 0.0001}, "40+": {"n_settled": 30, "model_brier": 0.3354, "kalshi_brier": 0.1357, "brier_diff_model_minus_kalshi": 0.1998}, "5-10": {"n_settled": 216, "model_brier": 0.1946, "kalshi_brier": 0.1993, "brier_diff_model_minus_kalshi": -0.0047}}}`

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
