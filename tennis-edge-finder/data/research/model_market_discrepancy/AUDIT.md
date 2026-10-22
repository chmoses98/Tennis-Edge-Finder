# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-22T17:45Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 49,244): 0-3 14.0%, 3-5 9.4%, 5-10 19.7%, 10-15 15.3%, 15-25 19.4%, 25-40 14.1%, 40+ 8.2%; median gap 12.16 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 11.9%, doubles 6.8%). Main tour: ATP 4.9% and WTA 4.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 10,943): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.5%, STALE_QUOTE 18.5%, BOOK_QUALITY 18.3%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.6%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.5%, market_freshness 18.5%, execution 18.3%, data 12.5%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%.
* **Stale / settled / in-play**: 52.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 10,943 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.8% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.5 points vs 1667.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.041, Gen-2 0.846, Gen-1 ledger 0.867 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 539 model 0.2247 vs Kalshi 0.2098; n 108 model 0.2823 vs Kalshi 0.1929.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 211,564 model-market comparisons (344,598 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 70,697 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-22T17:31:35.955377+00:00'], shadow board 56,481 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-22T17:31:40.779052+00:00'], Model 4 26,522 rows, 19,072 settled tickers, 6,670 tickers with an external scan.
* By model: {"gen1_ledger": 47831, "gen1_elo": 28403, "fair_v1": 28403, "gen2": 28403, "gen1_sr": 28403, "model4_fundamental": 25074, "model4_conditioned": 25047}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 49,244 | 14.0 | 9.4 | 19.7 | 15.3 | 19.4 | 14.1 | 8.2 | 12.16 | 41.6% | 22.2% |
| MW fair_v1 | 28,403 | 12.9 | 8.5 | 18.3 | 15.6 | 19.9 | 15.0 | 9.8 | 13.23 | 44.7% | 24.8% |
| MW gen1_elo | 28,403 | 12.9 | 8.5 | 18.9 | 15.2 | 20.0 | 15.0 | 9.5 | 13.01 | 44.5% | 24.5% |
| MW gen1_ledger | 20,841 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.8 | 5.9 | 10.58 | 37.5% | 18.8% |
| MW gen1_sr | 28,403 | 9.9 | 7.0 | 16.5 | 13.8 | 21.2 | 18.9 | 12.8 | 16.12 | 52.8% | 31.6% |
| MW gen2 | 28,403 | 10.9 | 7.2 | 16.2 | 14.2 | 19.6 | 18.0 | 13.9 | 15.67 | 51.6% | 31.9% |
| all families model4_conditioned | 25,047 | 21.8 | 19.0 | 34.6 | 17.8 | 4.4 | 1.4 | 1.0 | 5.97 | 6.9% | 2.5% |
| all families model4_fundamental | 25,074 | 16.6 | 13.2 | 34.0 | 20.6 | 10.9 | 3.5 | 1.3 | 7.83 | 15.7% | 4.8% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.9%, >=15pp 41.6%, >=20pp 30.9%, >=25pp 22.2%, >=30pp 16.0%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.6%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,433 | 28.9 | 14.0 | 24.5 | 14.8 | 12.1 | 5.0 | 0.7 | 6.17 | 17.8% | 5.8% |
| CHALLENGER | 4,479 | 15.9 | 9.9 | 20.4 | 15.7 | 14.8 | 12.4 | 11.0 | 11.09 | 38.1% | 23.3% |
| ITF_MEN | 7,808 | 10.3 | 7.5 | 16.9 | 14.7 | 21.6 | 17.1 | 11.9 | 15.18 | 50.6% | 29.0% |
| ITF_WOMEN | 11,351 | 9.4 | 6.8 | 15.8 | 15.4 | 22.7 | 18.2 | 11.6 | 15.82 | 52.5% | 29.8% |
| WTA | 1,672 | 17.2 | 13.0 | 25.4 | 20.0 | 19.2 | 4.6 | 0.7 | 8.42 | 24.5% | 5.3% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,433 | 23.7 | 14.9 | 25.1 | 17.0 | 13.4 | 4.9 | 1.0 | 6.58 | 19.3% | 5.9% |
| CHALLENGER | 4,479 | 14.8 | 8.6 | 18.6 | 14.8 | 17.4 | 13.9 | 11.8 | 12.5 | 43.1% | 25.8% |
| ITF_MEN | 7,808 | 8.4 | 6.0 | 14.4 | 13.1 | 19.7 | 20.7 | 17.6 | 18.48 | 58.0% | 38.3% |
| ITF_WOMEN | 11,351 | 8.0 | 5.6 | 13.7 | 13.5 | 20.9 | 21.1 | 17.2 | 18.97 | 59.2% | 38.3% |
| WTA | 1,672 | 14.5 | 10.0 | 21.2 | 16.4 | 23.6 | 13.7 | 0.7 | 11.13 | 38.0% | 14.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,433 | 24.5 | 12.7 | 24.0 | 15.9 | 14.8 | 6.9 | 1.2 | 7.29 | 22.9% | 8.1% |
| CHALLENGER | 4,479 | 14.4 | 9.3 | 20.7 | 15.3 | 16.2 | 12.8 | 11.2 | 11.43 | 40.2% | 24.0% |
| ITF_MEN | 7,808 | 9.9 | 7.5 | 17.0 | 14.1 | 22.1 | 17.5 | 12.0 | 15.54 | 51.6% | 29.5% |
| ITF_WOMEN | 11,351 | 9.6 | 6.6 | 16.2 | 15.7 | 23.0 | 18.2 | 10.8 | 15.65 | 52.0% | 29.0% |
| WTA | 1,672 | 24.3 | 16.9 | 29.9 | 16.1 | 10.1 | 2.3 | 0.4 | 6.01 | 12.9% | 2.8% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,397 | 25.5 | 19.6 | 30.7 | 11.8 | 9.0 | 3.0 | 0.4 | 5.53 | 12.4% | 3.4% |
| CHALLENGER | 3,085 | 21.5 | 14.8 | 26.6 | 14.0 | 14.8 | 6.5 | 1.9 | 7.27 | 23.2% | 8.4% |
| DOUBLES | 1,547 | 5.4 | 4.1 | 11.5 | 10.2 | 20.9 | 26.4 | 21.4 | 24.04 | 68.7% | 47.8% |
| ITF_MEN | 5,920 | 13.8 | 8.8 | 20.1 | 16.0 | 21.3 | 13.3 | 6.6 | 12.16 | 41.2% | 20.0% |
| ITF_WOMEN | 6,983 | 12.7 | 9.1 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.86 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,028 | 22.3 | 15.9 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,367 | 29.3 | 14.2 | 24.9 | 14.7 | 11.8 | 4.6 | 0.5 | 5.98 | 16.9% | 5.1% |
| CHALLENGER | 3,166 | 20.7 | 12.3 | 25.1 | 18.1 | 15.3 | 6.6 | 2.0 | 8.35 | 23.8% | 8.6% |
| ITF_MEN | 5,749 | 12.5 | 9.0 | 20.2 | 16.5 | 22.6 | 14.1 | 5.1 | 12.45 | 41.8% | 19.2% |
| ITF_WOMEN | 8,480 | 11.1 | 8.2 | 18.0 | 17.5 | 24.6 | 15.4 | 5.2 | 13.54 | 45.1% | 20.5% |
| WTA | 1,623 | 17.4 | 12.8 | 25.4 | 20.2 | 19.2 | 4.3 | 0.7 | 8.39 | 24.1% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,367 | 24.0 | 15.2 | 25.3 | 16.9 | 13.4 | 4.6 | 0.6 | 6.48 | 18.6% | 5.2% |
| CHALLENGER | 3,166 | 18.7 | 11.0 | 23.1 | 17.7 | 17.6 | 9.6 | 2.2 | 9.21 | 29.4% | 11.8% |
| ITF_MEN | 5,750 | 10.0 | 7.2 | 16.7 | 14.9 | 21.5 | 19.2 | 10.5 | 15.48 | 51.2% | 29.7% |
| ITF_WOMEN | 8,481 | 9.0 | 6.4 | 15.2 | 15.0 | 23.0 | 20.6 | 10.8 | 16.62 | 54.4% | 31.4% |
| WTA | 1,623 | 14.5 | 10.0 | 21.2 | 16.3 | 23.6 | 13.6 | 0.7 | 11.18 | 38.0% | 14.4% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,354 | 25.7 | 19.9 | 30.7 | 12.0 | 8.6 | 2.9 | 0.2 | 5.42 | 11.7% | 3.1% |
| CHALLENGER | 2,688 | 22.9 | 15.9 | 28.1 | 13.9 | 14.1 | 4.4 | 0.6 | 6.68 | 19.1% | 5.0% |
| DOUBLES | 1,437 | 5.4 | 4.3 | 11.8 | 10.4 | 20.8 | 26.3 | 20.9 | 23.85 | 68.1% | 47.2% |
| ITF_MEN | 4,951 | 15.0 | 9.5 | 21.8 | 16.8 | 21.1 | 11.7 | 4.0 | 11.13 | 36.9% | 15.7% |
| ITF_WOMEN | 5,787 | 13.6 | 9.6 | 20.7 | 15.9 | 21.8 | 15.1 | 3.4 | 11.68 | 40.2% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 978 | 22.8 | 16.5 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,547 | 5.4 | 4.1 | 11.5 | 10.2 | 20.9 | 26.4 | 21.4 | 24.04 | 68.7% | 47.8% |
| singles | 19,294 | 16.2 | 11.2 | 22.3 | 15.2 | 18.5 | 11.8 | 4.7 | 10.04 | 35.0% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,338 | 13.2 | 8.8 | 19.0 | 15.6 | 18.9 | 14.8 | 9.7 | 12.92 | 43.4% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 17,655 | 13.3 | 8.5 | 18.4 | 15.3 | 20.1 | 14.8 | 9.7 | 13.17 | 44.5% | 24.5% |
| UNKNOWN | 4,173 | 10.8 | 7.8 | 17.1 | 17.0 | 20.8 | 16.0 | 10.4 | 13.95 | 47.3% | 26.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,891 | 19.7 | 11.6 | 21.3 | 16.5 | 15.7 | 9.0 | 6.2 | 9.22 | 30.9% | 15.2% |
| B | 3,543 | 12.5 | 8.9 | 19.8 | 16.6 | 19.4 | 12.3 | 10.5 | 12.41 | 42.2% | 22.8% |
| C | 4,011 | 11.6 | 8.8 | 19.6 | 15.1 | 19.5 | 15.0 | 10.4 | 13.15 | 44.9% | 25.4% |
| D | 4,562 | 12.1 | 7.8 | 17.2 | 15.5 | 21.6 | 15.7 | 10.1 | 14.01 | 47.4% | 25.8% |
| F | 8,396 | 7.7 | 5.6 | 15.0 | 14.6 | 23.5 | 21.3 | 12.4 | 17.79 | 57.2% | 33.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,834 | 23.0 | 15.9 | 28.8 | 15.0 | 11.8 | 4.0 | 1.5 | 6.65 | 17.3% | 5.5% |
| B | 2,857 | 16.3 | 10.4 | 23.4 | 16.0 | 19.3 | 10.7 | 3.9 | 9.99 | 33.9% | 14.6% |
| C | 4,116 | 11.4 | 7.4 | 18.3 | 14.2 | 21.4 | 16.7 | 10.6 | 14.33 | 48.8% | 27.3% |
| D | 2,958 | 14.5 | 9.8 | 19.9 | 14.4 | 21.0 | 14.3 | 6.1 | 11.93 | 41.3% | 20.4% |
| F | 5,076 | 10.2 | 8.2 | 15.5 | 14.8 | 22.8 | 20.3 | 8.2 | 15.68 | 51.3% | 28.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,048 | 17.8 | 10.4 | 20.6 | 16.4 | 16.2 | 9.8 | 8.7 | 10.36 | 34.8% | 18.5% |
| LIMITED | 6,111 | 13.4 | 10.1 | 20.4 | 15.6 | 19.3 | 13.5 | 7.7 | 11.91 | 40.4% | 21.2% |
| POOR | 13,244 | 9.3 | 6.4 | 15.9 | 15.0 | 22.8 | 19.1 | 11.5 | 16.17 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,398 | 26.4 | 20.4 | 34.2 | 12.6 | 4.8 | 1.4 | 0.2 | 5.33 | 6.4% | 1.6% |
| GAME_SPREAD | 4,604 | 22.3 | 15.2 | 33.5 | 17.4 | 9.0 | 2.4 | 0.3 | 6.71 | 11.7% | 2.7% |
| MATCH_WINNER | 20,841 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.8 | 5.9 | 10.58 | 37.5% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,621 | 29.3 | 16.9 | 31.1 | 12.5 | 8.1 | 1.7 | 0.4 | 5.47 | 10.2% | 2.1% |
| TOTAL_GAMES | 7,343 | 8.5 | 9.6 | 36.5 | 28.9 | 10.6 | 3.2 | 2.7 | 9.5 | 16.5% | 5.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,753 | 25.4 | 33.8 | 32.6 | 4.4 | 3.0 | 0.6 | 0.2 | 4.48 | 3.8% | 0.8% |
| GAME_SPREAD | 6,006 | 45.4 | 16.9 | 27.1 | 7.7 | 1.8 | 0.8 | 0.3 | 3.5 | 2.9% | 1.2% |
| TOTAL_GAMES | 10,288 | 4.9 | 7.7 | 40.7 | 34.9 | 7.1 | 2.5 | 2.2 | 9.66 | 11.8% | 4.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,756 | 24.2 | 17.8 | 35.4 | 12.7 | 7.1 | 2.5 | 0.3 | 5.82 | 9.9% | 2.8% |
| GAME_SPREAD | 6,009 | 19.3 | 13.3 | 28.0 | 20.4 | 13.7 | 4.5 | 0.9 | 7.97 | 19.1% | 5.4% |
| TOTAL_GAMES | 10,309 | 8.5 | 9.3 | 36.3 | 27.4 | 12.5 | 3.8 | 2.4 | 9.52 | 18.6% | 6.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 28,403 | 44.7% | 24.8% | 13.23 | 36.3% | 15.5% | 11.0 |
| gen1_elo | 28,403 | 44.5% | 24.5% | 13.01 | 35.9% | 15.6% | 10.71 |
| gen1_sr | 28,403 | 52.8% | 31.6% | 16.12 | 45.1% | 22.4% | 13.34 |
| gen2 | 28,403 | 51.6% | 31.9% | 15.67 | 44.9% | 24.0% | 13.21 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 14,438 | 15.8 | 10.3 | 21.1 | 17.2 | 20.4 | 11.9 | 3.3 | 10.81 | 35.6% | 15.2% |
| STALE | 13,965 | 9.9 | 6.7 | 15.5 | 13.9 | 19.5 | 18.1 | 16.5 | 16.96 | 54.0% | 34.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,309 | 16.5 | 11.3 | 22.3 | 14.9 | 17.9 | 12.3 | 4.9 | 9.99 | 35.0% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 49,244 | 14309 | 17910 | 17025 | 24.0 | 139.0 | 1400.4 |
| ge_15pp | 20,507 | 5015 | 6436 | 9056 | 25.9 | 433.3 | 1380.4 |
| ge_25pp | 10,943 | 2452 | 2792 | 5699 | 31.9 | 574.8 | 1380.4 |
| lt_10pp | 21,216 | 7165 | 8437 | 5614 | 22.1 | 47.5 | 1341.5 |

Current slate `SL-20261022T174520Z-3df9478a`: 351 priced rows, quote age at build {'median': 14.0, 'max': 14.1}, freshness {'AGING': 351}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 22 | 0.0 | 0.0 | 22.7 | 4.5 | 40.9 | 31.8 | 0.0 | 20.48 | 72.7% | 31.8% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,625 | 19.4 | 10.9 | 23.9 | 18.9 | 18.9 | 7.3 | 0.7 | 9.14 | 27.0% | 8.1% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 511 | 66.5 | 33.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,107 | 0.0 | 2.2 | 35.0 | 25.8 | 25.4 | 10.8 | 0.8 | 12.56 | 37.0% | 11.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 28,403 | 4294 (15.1%) | 25.8% | 0.9% | {"EXTERNAL_STALE": 2625, "AGREES_WITH_KALSHI": 1107, "ALL_AGREE": 511, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 12,693 | 1137 (9.0%) | 36.1% | 1.6% | {"EXTERNAL_STALE": 709, "AGREES_WITH_KALSHI": 410, "SUPPORTS_MODEL_DIRECTION": 16, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,029 | 349 (5.0%) | 37.0% | 2.3% | {"EXTERNAL_STALE": 212, "AGREES_WITH_KALSHI": 129, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,411 | 326 (9.6%) | 37.4% | 2.5% | {"EXTERNAL_STALE": 196, "AGREES_WITH_KALSHI": 122, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,282 | 2376 (21.1%) | 17.3% | 0.8% | {"EXTERNAL_STALE": 1421, "ALL_AGREE": 511, "AGREES_WITH_KALSHI": 412, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,414 | 10.4 | 7.5 | 19.3 | 14.4 | 22.5 | 15.9 | 10.0 | 14.18 | 48.4% | 25.9% |
| 4-10x | 3,715 | 10.9 | 8.4 | 19.1 | 15.3 | 21.2 | 14.8 | 10.2 | 13.75 | 46.3% | 25.0% |
| <2x | 14,396 | 14.9 | 9.6 | 18.9 | 16.6 | 18.0 | 13.2 | 8.9 | 11.97 | 40.1% | 22.1% |
| >=10x | 4,878 | 11.2 | 6.4 | 15.2 | 14.2 | 21.9 | 19.4 | 11.7 | 16.18 | 53.0% | 31.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,153 | 12.3 | 8.4 | 19.4 | 16.2 | 19.6 | 13.5 | 10.4 | 12.99 | 43.6% | 24.0% |
| 300-1000 | 6,147 | 11.6 | 8.7 | 17.2 | 15.2 | 20.7 | 16.3 | 10.2 | 14.0 | 47.3% | 26.5% |
| <300 | 9,345 | 8.8 | 5.7 | 15.4 | 14.8 | 23.1 | 20.1 | 12.1 | 16.86 | 55.2% | 32.2% |
| >=3000 | 5,758 | 21.6 | 12.9 | 22.9 | 16.5 | 14.4 | 7.0 | 4.7 | 8.01 | 26.2% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 824 | 0.5474 | 0.4095 | 0.5 | +0.047 | -0.090 | -0.0038 ± 0.0054 |
| ratio 4-10x | 562 | 0.5846 | 0.4385 | 0.4911 | +0.093 | -0.053 | 0.0132 ± 0.0068 |
| ratio <2x | 2029 | 0.5375 | 0.4136 | 0.447 | +0.090 | -0.033 | 0.0122 ± 0.0032 |
| ratio >=10x | 745 | 0.5672 | 0.3921 | 0.4604 | +0.107 | -0.068 | 0.0074 ± 0.0067 |
| thinner_sample 1000-3000 | 1123 | 0.5425 | 0.415 | 0.4497 | +0.093 | -0.035 | 0.0104 ± 0.0043 |
| thinner_sample 300-1000 | 958 | 0.5633 | 0.4201 | 0.4916 | +0.072 | -0.072 | 0.0007 ± 0.0052 |
| thinner_sample <300 | 1402 | 0.5571 | 0.3911 | 0.4622 | +0.095 | -0.071 | 0.0093 ± 0.0047 |
| thinner_sample >=3000 | 677 | 0.5358 | 0.4408 | 0.4638 | +0.072 | -0.023 | 0.0136 ± 0.0045 |
| data_status ADEQUATE | 1179 | 0.5386 | 0.4327 | 0.4504 | +0.088 | -0.018 | 0.0131 ± 0.0037 |
| data_status LIMITED | 975 | 0.549 | 0.4162 | 0.481 | +0.068 | -0.065 | 0.0038 ± 0.0048 |
| data_status POOR | 2006 | 0.5595 | 0.3985 | 0.4676 | +0.092 | -0.069 | 0.0077 ± 0.0039 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 613 | 0.1995 | 0.2005 | -0.0010 ± 0.0006 | 0.5793 | 0.5815 | 0.502 | 0.4871 | 0.5318 | -0.060 ± 0.019 | -0.01 (5) |
| 3-5 | 386 | 0.2021 | 0.2013 | +0.0007 ± 0.0018 | 0.5872 | 0.5838 | 0.5012 | 0.4611 | 0.4715 | -0.099 ± 0.0235 | 0.02 (1) |
| 5-10 | 850 | 0.2015 | 0.201 | +0.0005 ± 0.0023 | 0.5896 | 0.5852 | 0.5095 | 0.4353 | 0.4647 | -0.089 ± 0.016 | -0.0167 (6) |
| 10-15 | 720 | 0.2121 | 0.203 | +0.0091 ± 0.0042 | 0.6135 | 0.5872 | 0.5267 | 0.4025 | 0.4264 | -0.103 ± 0.0167 | -0.048 (5) |
| 15-25 | 944 | 0.2244 | 0.2135 | +0.0109 ± 0.0059 | 0.6436 | 0.6109 | 0.5767 | 0.3808 | 0.4513 | -0.089 ± 0.0149 | -0.0033 (9) |
| 25-40 | 539 | 0.2247 | 0.2098 | +0.0150 ± 0.0118 | 0.6379 | 0.603 | 0.6552 | 0.3456 | 0.4731 | -0.074 ± 0.0181 | -0.01 (1) |
| 40+ | 108 | 0.2823 | 0.1929 | +0.0894 ± 0.037 | 0.7723 | 0.5696 | 0.7554 | 0.3074 | 0.4352 | -0.086 ± 0.0361 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3133 | 0.1827 | 0.1837 | -0.0010 ± 0.0003 | 0.5401 | 0.5413 | 0.4914 | 0.4763 | 0.5148 | -0.017 ± 0.0077 | -0.0129 (17) |
| 3-5 | 2059 | 0.197 | 0.1957 | +0.0013 ± 0.0008 | 0.574 | 0.5679 | 0.4844 | 0.4444 | 0.4483 | -0.053 ± 0.0099 | 0.0 (2) |
| 5-10 | 4407 | 0.1982 | 0.1949 | +0.0033 ± 0.001 | 0.5805 | 0.5695 | 0.4812 | 0.4073 | 0.4211 | -0.048 ± 0.0067 | -0.0119 (21) |
| 10-15 | 3774 | 0.1987 | 0.181 | +0.0177 ± 0.0017 | 0.5835 | 0.5335 | 0.4858 | 0.3612 | 0.3519 | -0.073 ± 0.0069 | -0.0281 (16) |
| 15-25 | 4758 | 0.2085 | 0.1699 | +0.0385 ± 0.0023 | 0.6105 | 0.5029 | 0.5039 | 0.3075 | 0.3083 | -0.072 ± 0.0059 | -0.0025 (44) |
| 25-40 | 3698 | 0.224 | 0.1326 | +0.0914 ± 0.0037 | 0.6424 | 0.4036 | 0.532 | 0.2194 | 0.2328 | -0.057 ± 0.0058 | -0.01 (1) |
| 40+ | 2400 | 0.3808 | 0.0448 | +0.3360 ± 0.0049 | 0.9915 | 0.1741 | 0.6326 | 0.1072 | 0.0625 | -0.081 ± 0.004 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 468 | 0.2035 | 0.204 | -0.0005 ± 0.0007 | 0.5886 | 0.5896 | 0.5042 | 0.4891 | 0.5064 | -0.109 ± 0.0225 | -0.01 (3) |
| 3-5 | 342 | 0.2214 | 0.2198 | +0.0017 ± 0.002 | 0.6288 | 0.6252 | 0.5139 | 0.4739 | 0.4678 | -0.114 ± 0.0271 | 0.02 (1) |
| 5-10 | 733 | 0.2038 | 0.2038 | -0.0000 ± 0.0025 | 0.5931 | 0.5921 | 0.5461 | 0.4712 | 0.5102 | -0.077 ± 0.0172 | -0.01 (4) |
| 10-15 | 689 | 0.2175 | 0.2093 | +0.0083 ± 0.0044 | 0.6248 | 0.6043 | 0.5652 | 0.4408 | 0.4717 | -0.111 ± 0.0181 | -0.04 (5) |
| 15-25 | 977 | 0.2297 | 0.21 | +0.0197 ± 0.0058 | 0.6523 | 0.6028 | 0.5884 | 0.3925 | 0.4442 | -0.100 ± 0.0149 | -0.0133 (9) |
| 25-40 | 690 | 0.2619 | 0.1985 | +0.0634 ± 0.0107 | 0.7309 | 0.5777 | 0.6531 | 0.3375 | 0.3971 | -0.110 ± 0.0166 | -0.0075 (4) |
| 40+ | 261 | 0.3577 | 0.1752 | +0.1825 ± 0.0256 | 0.9859 | 0.5222 | 0.7337 | 0.249 | 0.318 | -0.067 ± 0.0248 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2626 | 0.1933 | 0.1935 | -0.0002 ± 0.0003 | 0.5633 | 0.5637 | 0.5099 | 0.495 | 0.5103 | -0.043 ± 0.0089 | -0.0133 (15) |
| 3-5 | 1768 | 0.1981 | 0.1977 | +0.0004 ± 0.0009 | 0.5737 | 0.5723 | 0.5149 | 0.475 | 0.4887 | -0.040 ± 0.0108 | 0.02 (1) |
| 5-10 | 3885 | 0.1941 | 0.1928 | +0.0013 ± 0.0011 | 0.5723 | 0.5645 | 0.5067 | 0.4328 | 0.4633 | -0.030 ± 0.0071 | -0.0117 (6) |
| 10-15 | 3422 | 0.2002 | 0.1872 | +0.0130 ± 0.0019 | 0.5874 | 0.5471 | 0.5138 | 0.3898 | 0.4006 | -0.059 ± 0.0075 | -0.0189 (18) |
| 15-25 | 4791 | 0.2161 | 0.1782 | +0.0379 ± 0.0024 | 0.628 | 0.5241 | 0.5259 | 0.3299 | 0.335 | -0.069 ± 0.0061 | -0.0086 (42) |
| 25-40 | 4332 | 0.2514 | 0.1403 | +0.1111 ± 0.0036 | 0.7079 | 0.4288 | 0.5594 | 0.2426 | 0.2283 | -0.081 ± 0.0057 | -0.0044 (18) |
| 40+ | 3405 | 0.3954 | 0.0634 | +0.3320 ± 0.0049 | 1.0416 | 0.224 | 0.6539 | 0.121 | 0.0893 | -0.070 ± 0.0042 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 585 | 0.2004 | 0.2027 | -0.0023 ± 0.0007 | 0.5819 | 0.5876 | 0.4981 | 0.4828 | 0.5504 | -0.024 ± 0.0192 | -0.0137 (8) |
| 3-5 | 417 | 0.2003 | 0.1984 | +0.0020 ± 0.0018 | 0.5825 | 0.5765 | 0.5063 | 0.4667 | 0.4628 | -0.119 ± 0.0227 | 0.0067 (3) |
| 5-10 | 876 | 0.1995 | 0.1962 | +0.0034 ± 0.0023 | 0.5853 | 0.5733 | 0.5071 | 0.4331 | 0.4452 | -0.100 ± 0.0154 | -0.0071 (7) |
| 10-15 | 725 | 0.2078 | 0.2045 | +0.0033 ± 0.0042 | 0.6029 | 0.591 | 0.5372 | 0.4135 | 0.4634 | -0.085 ± 0.0167 | -0.0317 (6) |
| 15-25 | 886 | 0.2313 | 0.2119 | +0.0195 ± 0.006 | 0.661 | 0.6068 | 0.5857 | 0.3914 | 0.4379 | -0.112 ± 0.0154 | -0.03 (1) |
| 25-40 | 558 | 0.2131 | 0.2181 | -0.0050 ± 0.0116 | 0.6138 | 0.6222 | 0.6666 | 0.3548 | 0.5161 | -0.049 ± 0.0178 | 0.015 (2) |
| 40+ | 113 | 0.2983 | 0.2041 | +0.0942 ± 0.0374 | 0.8195 | 0.5944 | 0.7633 | 0.3129 | 0.4425 | -0.083 ± 0.0388 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3070 | 0.187 | 0.1876 | -0.0006 ± 0.0003 | 0.549 | 0.5501 | 0.4916 | 0.4764 | 0.4925 | -0.036 ± 0.0079 | -0.0163 (35) |
| 3-5 | 2060 | 0.1939 | 0.1912 | +0.0026 ± 0.0008 | 0.5695 | 0.5614 | 0.489 | 0.4493 | 0.4369 | -0.072 ± 0.0098 | -0.0094 (18) |
| 5-10 | 4510 | 0.1947 | 0.1887 | +0.0060 ± 0.001 | 0.5734 | 0.5537 | 0.4848 | 0.4108 | 0.4067 | -0.063 ± 0.0065 | -0.01 (31) |
| 10-15 | 3644 | 0.1927 | 0.1765 | +0.0162 ± 0.0017 | 0.5688 | 0.5215 | 0.497 | 0.3735 | 0.3694 | -0.070 ± 0.0069 | -0.015 (12) |
| 15-25 | 4919 | 0.2112 | 0.1721 | +0.0390 ± 0.0023 | 0.6166 | 0.5081 | 0.5122 | 0.3172 | 0.3145 | -0.074 ± 0.0059 | -0.03 (2) |
| 25-40 | 3690 | 0.219 | 0.1357 | +0.0832 ± 0.0038 | 0.6319 | 0.4105 | 0.5372 | 0.2213 | 0.2491 | -0.046 ± 0.0058 | 0.01 (3) |
| 40+ | 2336 | 0.3951 | 0.0496 | +0.3455 ± 0.0052 | 1.0322 | 0.1864 | 0.6445 | 0.1135 | 0.0672 | -0.083 ± 0.0044 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 960 | 0.1943 | 0.1945 | -0.0001 ± 0.0005 | 0.5677 | 0.5676 | 0.5079 | 0.4928 | 0.4969 | -0.059 ± 0.0144 | -0.0224 (49) |
| 3-5 | 669 | 0.1922 | 0.1914 | +0.0007 ± 0.0014 | 0.5617 | 0.5587 | 0.4873 | 0.4475 | 0.4559 | -0.057 ± 0.0173 | -0.0194 (34) |
| 5-10 | 1405 | 0.2007 | 0.1943 | +0.0064 ± 0.0018 | 0.5908 | 0.5707 | 0.496 | 0.4227 | 0.4171 | -0.075 ± 0.012 | -0.005 (78) |
| 10-15 | 917 | 0.2091 | 0.1982 | +0.0109 ± 0.0037 | 0.6062 | 0.5781 | 0.5168 | 0.3936 | 0.4089 | -0.065 ± 0.015 | 0.0014 (64) |
| 15-25 | 1243 | 0.2302 | 0.2099 | +0.0203 ± 0.0051 | 0.6577 | 0.6047 | 0.5747 | 0.3798 | 0.4264 | -0.069 ± 0.013 | -0.0214 (59) |
| 25-40 | 759 | 0.249 | 0.2068 | +0.0422 ± 0.0102 | 0.7071 | 0.5948 | 0.6693 | 0.3569 | 0.4453 | -0.086 ± 0.0155 | -0.0219 (26) |
| 40+ | 256 | 0.3542 | 0.1961 | +0.1581 ± 0.0274 | 1.0227 | 0.5738 | 0.8081 | 0.3254 | 0.4219 | -0.098 ± 0.0249 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3143 | 0.1829 | 0.1831 | -0.0002 ± 0.0003 | 0.5389 | 0.5384 | 0.5074 | 0.492 | 0.5027 | -0.037 ± 0.0077 | -0.0157 (88) |
| 3-5 | 2169 | 0.1924 | 0.1907 | +0.0018 ± 0.0008 | 0.5627 | 0.5583 | 0.4942 | 0.4545 | 0.4514 | -0.053 ± 0.0095 | -0.0209 (69) |
| 5-10 | 4353 | 0.1979 | 0.1892 | +0.0087 ± 0.001 | 0.5817 | 0.5564 | 0.4915 | 0.418 | 0.3988 | -0.073 ± 0.0067 | -0.0082 (132) |
| 10-15 | 3000 | 0.2053 | 0.1895 | +0.0157 ± 0.002 | 0.5988 | 0.5573 | 0.524 | 0.4009 | 0.3977 | -0.065 ± 0.008 | -0.0053 (105) |
| 15-25 | 3794 | 0.2288 | 0.1996 | +0.0292 ± 0.0029 | 0.6603 | 0.5786 | 0.5678 | 0.3721 | 0.3962 | -0.062 ± 0.0073 | -0.0253 (107) |
| 25-40 | 2613 | 0.2598 | 0.1845 | +0.0754 ± 0.0053 | 0.7366 | 0.5379 | 0.6302 | 0.3161 | 0.3559 | -0.077 ± 0.0082 | -0.0229 (51) |
| 40+ | 1174 | 0.3782 | 0.143 | +0.2352 ± 0.0116 | 1.073 | 0.4316 | 0.7292 | 0.2255 | 0.2564 | -0.074 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4160 | 1.041 ± 0.044 | 1.139 | 0.1685 | 0.1654 | 0.2134 | 0.2051 |
| gen2 | 4160 | 0.846 ± 0.04 | 1.097 | 0.1696 | 0.1659 | 0.2329 | 0.2048 |
| gen1_elo | 4160 | 1.019 ± 0.042 | 1.128 | 0.1752 | 0.1655 | 0.2124 | 0.2053 |
| gen1_sr | 4160 | 1.039 ± 0.053 | 1.167 | 0.1302 | 0.1679 | 0.2291 | 0.2044 |
| gen1_ledger | 6209 | 0.867 ± 0.031 | 1.08 | 0.1828 | 0.1795 | 0.2182 | 0.1993 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 20,507)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,711 | 23.0% |
| STALE_QUOTE | market_freshness | 4,428 | 21.6% |
| BOOK_QUALITY | execution | 3,842 | 18.7% |
| POOR_DATA | data | 2,340 | 11.4% |
| LIMITED_DATA | data | 1,289 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,120 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 972 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 861 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 610 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 333 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 23.0%, market_freshness 21.6%, execution 18.7%, data 17.7%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.2%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 50.4%, STALE_KALSHI_QUOTE 44.2%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 16.2%, LEVEL_TRANSFER_RISK 11.0%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.6%, POST_SETTLEMENT_OBSERVATION 23.0%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 10,943)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,779 | 34.5% |
| STALE_QUOTE | market_freshness | 2,020 | 18.5% |
| BOOK_QUALITY | execution | 2,002 | 18.3% |
| POOR_DATA | data | 969 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 600 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 491 | 4.5% |
| LIMITED_DATA | data | 394 | 3.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 383 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 230 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 34.5%, market_freshness 18.5%, execution 18.3%, data 12.5%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.9%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 52.1%, STALE_PLAYER_DATA 45.3%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 24.3%, PLAYER_IDENTITY_RISK 19.5%, MODEL_HIGH_UNCERTAINTY 17.9%, LEVEL_TRANSFER_RISK 9.8%, EVENT_MAPPING_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.6%, POST_SETTLEMENT_OBSERVATION 34.5%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8535, "IDENTITY_AMBIGUOUS": 2408}; ticker orientation: {"VERIFIED": 10943}.

Checks: discipline:AMBIGUOUS 739, discipline:PASS 10204, identity_confidence:AMBIGUOUS 2133, identity_confidence:PASS 8810, level_mapping:NA 751, level_mapping:PASS 10192, market_pair:AMBIGUOUS 387, market_pair:NA 274, market_pair:PASS 10282, model_complement:NA 241, model_complement:PASS 10702, namesake:PASS 10943, physical_match_id:NA 3914, physical_match_id:PASS 7029, player_ids:PASS 10943, same_pair_other_event:PASS 10943, ticker_orientation:PASS 10943

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,830 | 4.9% | 4.4% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 19, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.84 | 0.2207 / 0.2149 (445) | 19.0% | 3.9% | 3.3% | 2.9% |
| CHALLENGER | 7,564 | 17.2% | 6.9% | 11.9% | {"coverage": 737, "market_freshness/coverage": 161, "market_freshness": 147, "data": 129, "model_calibration_or_unknown": 58, "execution": 30, "model_calibration": 27, "mapping": 15} | 7.44 | 0.2185 / 0.2073 (1828) | 35.1% | 17.5% | 3.9% | 22.6% |
| DOUBLES | 1,547 | 47.8% | 47.2% | 6.8% | {"execution": 379, "mapping": 194, "market_freshness": 106, "market_freshness/coverage": 53, "coverage": 7} | 23.85 | 0.3152 / 0.2362 (403) | 15.1% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 13,728 | 25.1% | 17.6% | 31.5% | {"coverage": 1276, "execution": 673, "market_freshness": 580, "data": 460, "market_freshness/coverage": 293, "mapping": 165, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.82 | 0.2145 / 0.1967 (3119) | 37.4% | 68.9% | 19.2% | 22.1% |
| ITF_WOMEN | 18,334 | 27.0% | 19.7% | 45.2% | {"coverage": 1726, "market_freshness": 1054, "execution": 870, "data": 705, "market_freshness/coverage": 414, "mapping": 111, "model_calibration_or_unknown": 58, "model_calibration": 11} | 12.87 | 0.2027 / 0.1938 (3593) | 39.5% | 56.7% | 9.9% | 22.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,700 | 4.7% | 4.2% | 1.2% | {"market_freshness": 40, "model_calibration_or_unknown": 28, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.81 | 0.2385 / 0.2306 (451) | 24.5% | 1.3% | 1.4% | 3.7% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 15 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 16 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 17 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 18 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 19 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 20 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 21 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 22 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 23 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 26 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 27 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 28 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 32 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 33 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 34 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 36 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 38 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 39 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 40 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 41 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 43 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 44 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 45 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 46 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 47 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 48 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 49 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 895 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 50 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 246 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9713, "by_level_share_of_ge_25pp": {"ATP": 0.0171, "CHALLENGER": 0.1192, "DOUBLES": 0.0675, "ITF_MEN": 0.3153, "ITF_WOMEN": 0.4523, "OTHER": 0.0011, "WTA": 0.0117, "WTA125": 0.0159}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5208, "share_primary_cause_market_settled_or_in_play": 0.4351, "share_primary_cause_stale_quote_only": 0.1846}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 10943, "identity_ambiguous_share": 0.22, "ticker_orientation": {"VERIFIED": 10943}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7029, "with_external": 349, "coverage": 0.0497, "external_status": {"EXTERNAL_STALE": 212, "AGREES_WITH_KALSHI": 129, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 212, "MODEL_LONE_OUTLIER": 129, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3696, "share_external_supports_model": 0.0229}, "pregame_clean_ge_25pp": {"n": 3411, "with_external": 326, "coverage": 0.0956, "external_status": {"EXTERNAL_STALE": 196, "AGREES_WITH_KALSHI": 122, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 196, "MODEL_LONE_OUTLIER": 122, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3742, "share_external_supports_model": 0.0245}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.5, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2136, "data_status": {"POOR": 6127, "LIMITED": 2906, "ADEQUATE": 1910}, "comparison_lt_10pp": {"median_thinner_serve_points": 1667.0, "median_sample_ratio": 1.71, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 824, "model_minus_observed": 0.0474, "kalshi_minus_observed": -0.0905, "brier_diff_model_minus_kalshi": -0.0038}, "4-10x": {"n": 562, "model_minus_observed": 0.0935, "kalshi_minus_observed": -0.0526, "brier_diff_model_minus_kalshi": 0.0132}, "<2x": {"n": 2029, "model_minus_observed": 0.0905, "kalshi_minus_observed": -0.0334, "brier_diff_model_minus_kalshi": 0.0122}, ">=10x": {"n": 745, "model_minus_observed": 0.1068, "kalshi_minus_observed": -0.0683, "brier_diff_model_minus_kalshi": 0.0074}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4160, "model": {"intercept": -0.546, "slope": 0.846, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.22, "slope": 1.097, "slope_se": 0.045}, "mean_extremity_model": 0.1696, "mean_extremity_kalshi": 0.1659, "model_brier": 0.2329, "kalshi_brier": 0.2048, "brier_diff_model_minus_kalshi": 0.028, "brier_diff_se": 0.003, "model_logloss": 0.6622, "kalshi_logloss": 0.5923}, "fair_v1": {"n": 4160, "model": {"intercept": -0.411, "slope": 1.041, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.309, "slope": 1.139, "slope_se": 0.046}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2134, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.0024, "model_logloss": 0.6152, "kalshi_logloss": 0.5926}, "gen1_elo": {"n": 4160, "model": {"intercept": -0.398, "slope": 1.019, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.128, "slope_se": 0.045}, "mean_extremity_model": 0.1752, "mean_extremity_kalshi": 0.1655, "model_brier": 0.2124, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.0072, "brier_diff_se": 0.0024, "model_logloss": 0.6139, "kalshi_logloss": 0.593}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2475, "share_ge_15": 0.4469, "median_abs_gap": 13.23, "n": 28403}, "gen1_elo": {"share_ge_25": 0.2449, "share_ge_15": 0.4451, "median_abs_gap": 13.01, "n": 28403}, "gen1_sr": {"share_ge_25": 0.3164, "share_ge_15": 0.528, "median_abs_gap": 16.12, "n": 28403}, "gen2": {"share_ge_25": 0.3192, "share_ge_15": 0.5156, "median_abs_gap": 15.67, "n": 28403}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1549, "share_ge_15": 0.3633, "median_abs_gap": 11.0, "n": 22019}, "gen1_elo": {"share_ge_25": 0.1563, "share_ge_15": 0.3592, "median_abs_gap": 10.71, "n": 22016}, "gen1_sr": {"share_ge_25": 0.2238, "share_ge_15": 0.451, "median_abs_gap": 13.34, "n": 22020}, "gen2": {"share_ge_25": 0.2396, "share_ge_15": 0.4486, "median_abs_gap": 13.21, "n": 22021}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0488, "share_ge_25_pregame_clean": 0.0438}, "WTA": {"median_abs_gap_pregame_clean": 7.81, "share_ge_25_all": 0.0474, "share_ge_25_pregame_clean": 0.0419}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2341, "share_within_10pp_all": 0.4308, "share_within_10pp_pregame_clean": 0.4837, "corr_model_vs_mid_pregame_clean": 0.8452}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 613, "model_brier": 0.1995, "kalshi_brier": 0.2005, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 720, "model_brier": 0.2121, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": 0.0091}, "15-25": {"n_settled": 944, "model_brier": 0.2244, "kalshi_brier": 0.2135, "brier_diff_model_minus_kalshi": 0.0109}, "25-40": {"n_settled": 539, "model_brier": 0.2247, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.015}, "3-5": {"n_settled": 386, "model_brier": 0.2021, "kalshi_brier": 0.2013, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 108, "model_brier": 0.2823, "kalshi_brier": 0.1929, "brier_diff_model_minus_kalshi": 0.0894}, "5-10": {"n_settled": 850, "model_brier": 0.2015, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.546, "slope": 0.846, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.22, "slope": 1.097, "slope_se": 0.045}, "n": 4160}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.511, "slope": 0.867, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.158, "slope": 1.08, "slope_se": 0.035}, "n": 6209}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 403, "model_brier": 0.3152, "kalshi_brier": 0.2362, "brier_diff_model_minus_kalshi": 0.079, "brier_diff_se": 0.0154, "corr_model_outcome": 0.0211, "corr_kalshi_outcome": 0.2513}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
