# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-06T04:54Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 16,186): 0-3 13.1%, 3-5 9.3%, 5-10 19.2%, 10-15 15.2%, 15-25 19.0%, 25-40 15.0%, 40+ 9.1%; median gap 12.58 pp.
* **Where the extremes live**: 97.4% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.5%, Challenger 14.3%, doubles 4.9%). Main tour: ATP 2.9% and WTA 9.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 3,904): MARKET_ALREADY_SETTLED_WHEN_PRICED 42.6%, STALE_QUOTE 21.9%, BOOK_QUALITY 13.1%, POOR_DATA 7.0%, POSSIBLY_IN_PLAY_QUOTE 4.7%, IN_PLAY_QUOTE 3.0%, LIMITED_DATA 2.8%, IDENTITY_AMBIGUOUS 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%. By class: coverage 42.6%, market_freshness 21.9%, execution 13.1%, data 9.8%, market_freshness/coverage 7.8%, mapping 2.6%, model_calibration_or_unknown 2.2%.
* **Stale / settled / in-play**: 63.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 50.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 3,904 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 1.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 4.1% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 616.0 points vs 1868.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.117, Gen-2 0.917, Gen-1 ledger 0.899 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 134 model 0.2264 vs Kalshi 0.1785; n 30 model 0.3354 vs Kalshi 0.1357.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 57,327 model-market comparisons (97,600 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 23,486 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-06T04:49:34.990783+00:00'], shadow board 16,254 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-06T04:49:38.131147+00:00'], Model 4 5,209 rows, 8,776 settled tickers, 2,124 tickers with an external scan.
* By model: {"gen1_ledger": 14494, "gen1_elo": 8164, "fair_v1": 8164, "gen2": 8164, "gen1_sr": 8164, "model4_fundamental": 5093, "model4_conditioned": 5084}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 16,186 | 13.1 | 9.3 | 19.2 | 15.2 | 19.0 | 15.0 | 9.1 | 12.58 | 43.1% | 24.1% |
| MW fair_v1 | 8,164 | 12.7 | 9.0 | 18.1 | 15.4 | 18.2 | 15.8 | 10.8 | 13.14 | 44.8% | 26.6% |
| MW gen1_elo | 8,164 | 12.7 | 8.7 | 19.8 | 14.6 | 18.8 | 15.3 | 10.2 | 12.78 | 44.3% | 25.5% |
| MW gen1_ledger | 8,022 | 13.6 | 9.7 | 20.4 | 14.9 | 19.9 | 14.2 | 7.4 | 11.9 | 41.5% | 21.6% |
| MW gen1_sr | 8,164 | 9.6 | 7.5 | 16.0 | 13.9 | 21.7 | 18.8 | 12.5 | 16.16 | 52.9% | 31.2% |
| MW gen2 | 8,164 | 11.0 | 6.9 | 16.3 | 14.1 | 20.1 | 17.6 | 14.1 | 15.67 | 51.7% | 31.7% |
| all families model4_conditioned | 5,084 | 21.1 | 19.1 | 31.7 | 18.0 | 7.3 | 1.4 | 1.3 | 6.2 | 10.0% | 2.7% |
| all families model4_fundamental | 5,093 | 16.0 | 12.6 | 32.1 | 20.2 | 12.6 | 4.7 | 1.9 | 8.09 | 19.2% | 6.6% |

Configurable thresholds (primary): >=5pp 77.5%, >=10pp 58.3%, >=15pp 43.1%, >=20pp 32.8%, >=25pp 24.1%, >=30pp 17.8%, >=40pp 9.1%, >=50pp 4.0%
Executable gap (model outside the book, before fees): median 9.18pp; >=10pp 47.7%, >=25pp 20.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 518 | 22.8 | 19.3 | 25.3 | 15.2 | 12.9 | 2.3 | 2.1 | 5.98 | 17.4% | 4.4% |
| CHALLENGER | 1,668 | 14.5 | 10.7 | 17.3 | 15.7 | 14.3 | 13.8 | 13.6 | 12.64 | 41.8% | 27.5% |
| ITF_MEN | 2,270 | 11.1 | 8.5 | 18.7 | 14.4 | 17.9 | 16.4 | 13.0 | 13.75 | 47.4% | 29.5% |
| ITF_WOMEN | 3,043 | 9.6 | 6.6 | 15.6 | 15.6 | 21.6 | 20.1 | 10.8 | 16.05 | 52.5% | 31.0% |
| WTA | 472 | 22.5 | 10.2 | 24.8 | 14.4 | 18.9 | 7.0 | 2.3 | 8.38 | 28.2% | 9.3% |
| WTA125 | 193 | 14.5 | 7.8 | 19.2 | 26.9 | 14.0 | 13.5 | 4.2 | 11.2 | 31.6% | 17.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 518 | 18.9 | 16.0 | 26.6 | 16.2 | 15.6 | 4.0 | 2.5 | 7.06 | 22.2% | 6.6% |
| CHALLENGER | 1,668 | 13.8 | 6.4 | 18.0 | 14.0 | 18.7 | 15.9 | 13.2 | 14.11 | 47.8% | 29.1% |
| ITF_MEN | 2,270 | 9.3 | 6.9 | 16.7 | 15.2 | 19.4 | 17.8 | 14.7 | 15.66 | 52.0% | 32.6% |
| ITF_WOMEN | 3,043 | 8.2 | 6.2 | 13.1 | 12.3 | 21.6 | 20.6 | 18.1 | 19.42 | 60.3% | 38.7% |
| WTA | 472 | 20.3 | 5.3 | 16.5 | 15.7 | 22.0 | 17.8 | 2.3 | 13.18 | 42.2% | 20.1% |
| WTA125 | 193 | 6.2 | 2.6 | 17.6 | 22.3 | 22.3 | 16.6 | 12.4 | 15.79 | 51.3% | 29.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 518 | 25.1 | 12.6 | 30.1 | 15.1 | 9.1 | 5.8 | 2.3 | 7.38 | 17.2% | 8.1% |
| CHALLENGER | 1,668 | 15.7 | 10.1 | 21.2 | 13.1 | 13.4 | 12.8 | 13.7 | 10.93 | 39.9% | 26.4% |
| ITF_MEN | 2,270 | 9.4 | 8.9 | 18.1 | 14.5 | 19.7 | 16.3 | 12.9 | 14.25 | 49.0% | 29.3% |
| ITF_WOMEN | 3,043 | 9.3 | 6.3 | 16.0 | 14.9 | 24.0 | 20.0 | 9.4 | 16.66 | 53.4% | 29.4% |
| WTA | 472 | 22.0 | 13.8 | 32.8 | 15.2 | 10.6 | 4.0 | 1.5 | 7.0 | 16.1% | 5.5% |
| WTA125 | 193 | 21.2 | 8.3 | 24.9 | 19.2 | 20.2 | 5.2 | 1.0 | 8.06 | 26.4% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 265 | 27.9 | 21.1 | 38.5 | 10.6 | 1.9 | 0.0 | 0.0 | 5.34 | 1.9% | 0.0% |
| CHALLENGER | 1,136 | 20.8 | 15.3 | 26.3 | 15.1 | 13.5 | 6.5 | 2.5 | 7.31 | 22.4% | 9.0% |
| DOUBLES | 430 | 5.1 | 3.5 | 11.9 | 11.4 | 23.3 | 20.5 | 24.4 | 23.23 | 68.1% | 44.9% |
| ITF_MEN | 2,522 | 13.7 | 8.4 | 18.6 | 14.8 | 20.7 | 14.4 | 9.3 | 12.75 | 44.5% | 23.7% |
| ITF_WOMEN | 2,724 | 9.4 | 8.1 | 17.4 | 14.3 | 23.7 | 19.6 | 7.5 | 15.29 | 50.8% | 27.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 400 | 18.2 | 9.0 | 26.2 | 20.8 | 17.0 | 8.0 | 0.8 | 9.26 | 25.8% | 8.8% |
| WTA125 | 396 | 13.9 | 10.6 | 21.7 | 19.7 | 20.2 | 10.6 | 3.3 | 10.66 | 34.1% | 13.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 517 | 22.6 | 19.3 | 25.3 | 15.3 | 13.0 | 2.3 | 2.1 | 6.01 | 17.4% | 4.5% |
| CHALLENGER | 1,175 | 18.7 | 13.4 | 22.0 | 18.5 | 15.7 | 8.0 | 3.7 | 8.88 | 27.4% | 11.7% |
| ITF_MEN | 1,580 | 13.7 | 11.2 | 22.4 | 15.6 | 18.2 | 12.7 | 6.1 | 10.62 | 37.1% | 18.9% |
| ITF_WOMEN | 2,171 | 12.1 | 8.4 | 18.4 | 17.6 | 23.1 | 16.3 | 4.0 | 13.12 | 43.4% | 20.3% |
| WTA | 471 | 22.5 | 10.2 | 24.8 | 14.4 | 18.9 | 6.8 | 2.3 | 8.36 | 28.0% | 9.1% |
| WTA125 | 187 | 15.0 | 8.0 | 19.8 | 27.8 | 13.9 | 12.8 | 2.7 | 10.97 | 29.4% | 15.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 517 | 19.0 | 15.9 | 26.7 | 16.2 | 15.7 | 4.1 | 2.5 | 7.08 | 22.2% | 6.6% |
| CHALLENGER | 1,175 | 17.9 | 8.3 | 22.5 | 17.4 | 19.7 | 11.2 | 3.2 | 10.26 | 34.0% | 14.4% |
| ITF_MEN | 1,580 | 11.8 | 8.3 | 19.7 | 17.3 | 20.4 | 14.6 | 8.0 | 12.65 | 42.9% | 22.5% |
| ITF_WOMEN | 2,171 | 9.9 | 7.5 | 14.7 | 12.5 | 24.1 | 19.3 | 12.0 | 17.07 | 55.5% | 31.3% |
| WTA | 471 | 20.4 | 5.3 | 16.6 | 15.7 | 22.1 | 17.6 | 2.3 | 13.18 | 42.0% | 20.0% |
| WTA125 | 187 | 6.4 | 2.7 | 17.6 | 23.0 | 23.0 | 17.1 | 10.2 | 15.33 | 50.3% | 27.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 255 | 28.2 | 22.0 | 38.8 | 10.6 | 0.4 | 0.0 | 0.0 | 4.99 | 0.4% | 0.0% |
| CHALLENGER | 938 | 22.8 | 17.6 | 29.1 | 14.8 | 13.0 | 2.6 | 0.1 | 6.56 | 15.7% | 2.7% |
| DOUBLES | 390 | 5.1 | 3.3 | 12.1 | 11.5 | 23.3 | 20.8 | 23.9 | 23.05 | 68.0% | 44.6% |
| ITF_MEN | 1,907 | 16.1 | 9.8 | 21.1 | 16.0 | 20.8 | 11.7 | 4.6 | 11.12 | 37.1% | 16.3% |
| ITF_WOMEN | 2,042 | 10.8 | 9.3 | 19.9 | 15.8 | 24.3 | 17.4 | 2.5 | 12.75 | 44.2% | 19.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 371 | 18.6 | 9.4 | 26.9 | 21.3 | 17.5 | 6.2 | 0.0 | 9.03 | 23.7% | 6.2% |
| WTA125 | 317 | 16.1 | 11.7 | 25.2 | 23.0 | 18.3 | 5.4 | 0.3 | 9.21 | 24.0% | 5.7% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 430 | 5.1 | 3.5 | 11.9 | 11.4 | 23.3 | 20.5 | 24.4 | 23.23 | 68.1% | 44.9% |
| singles | 7,592 | 14.1 | 10.0 | 20.9 | 15.1 | 19.7 | 13.9 | 6.4 | 11.54 | 40.0% | 20.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,876 | 13.7 | 9.3 | 18.1 | 15.6 | 16.4 | 14.6 | 12.4 | 12.77 | 43.3% | 26.9% |
| Hard | 5,602 | 12.5 | 9.1 | 18.5 | 15.2 | 18.9 | 15.7 | 10.1 | 13.14 | 44.8% | 25.9% |
| UNKNOWN | 686 | 12.1 | 7.1 | 14.7 | 17.1 | 17.2 | 19.5 | 12.2 | 14.57 | 49.0% | 31.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,430 | 16.9 | 11.4 | 19.9 | 16.0 | 15.5 | 11.0 | 9.3 | 10.49 | 35.8% | 20.3% |
| B | 1,108 | 15.8 | 10.4 | 19.4 | 17.6 | 16.2 | 10.3 | 10.4 | 10.94 | 36.8% | 20.7% |
| C | 1,214 | 12.8 | 10.5 | 20.5 | 13.8 | 16.7 | 15.5 | 10.1 | 12.61 | 42.3% | 25.6% |
| D | 1,464 | 10.8 | 8.3 | 16.5 | 15.1 | 22.5 | 16.1 | 10.9 | 14.55 | 49.4% | 26.9% |
| F | 1,948 | 7.0 | 4.9 | 14.6 | 14.8 | 20.4 | 24.9 | 13.3 | 19.03 | 58.6% | 38.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 2,392 | 19.9 | 13.2 | 26.8 | 16.6 | 14.6 | 6.3 | 2.6 | 7.91 | 23.4% | 8.9% |
| B | 1,207 | 13.8 | 9.4 | 22.5 | 16.1 | 19.6 | 11.8 | 6.9 | 11.35 | 38.3% | 18.7% |
| C | 1,538 | 11.2 | 8.3 | 16.9 | 14.4 | 22.8 | 15.2 | 11.1 | 14.63 | 49.1% | 26.3% |
| D | 1,262 | 11.6 | 7.9 | 21.1 | 12.8 | 22.9 | 16.7 | 7.0 | 13.55 | 46.7% | 23.8% |
| F | 1,623 | 8.0 | 7.3 | 12.2 | 13.6 | 22.7 | 24.8 | 11.5 | 18.42 | 59.0% | 36.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 2,907 | 16.3 | 10.5 | 19.1 | 16.6 | 15.8 | 11.1 | 10.5 | 11.07 | 37.4% | 21.6% |
| LIMITED | 1,821 | 14.5 | 11.6 | 21.5 | 14.6 | 15.9 | 13.4 | 8.6 | 10.83 | 37.9% | 22.0% |
| POOR | 3,436 | 8.7 | 6.3 | 15.3 | 14.9 | 21.4 | 21.0 | 12.2 | 17.11 | 54.7% | 33.2% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,101 | 31.1 | 26.2 | 36.0 | 5.0 | 1.4 | 0.3 | 0.0 | 4.35 | 1.7% | 0.3% |
| GAME_SPREAD | 954 | 22.8 | 16.2 | 36.8 | 17.8 | 5.6 | 0.5 | 0.3 | 6.15 | 6.4% | 0.8% |
| MATCH_WINNER | 8,022 | 13.6 | 9.7 | 20.4 | 14.9 | 19.9 | 14.2 | 7.4 | 11.9 | 41.5% | 21.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 2,610 | 27.5 | 17.3 | 30.9 | 12.9 | 9.2 | 1.8 | 0.4 | 5.62 | 11.4% | 2.2% |
| TOTAL_GAMES | 1,783 | 8.8 | 9.5 | 33.3 | 26.4 | 13.6 | 5.0 | 3.4 | 9.72 | 22.0% | 8.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,836 | 27.0 | 36.7 | 25.0 | 0.4 | 9.8 | 0.9 | 0.3 | 4.29 | 11.0% | 1.2% |
| GAME_SPREAD | 1,173 | 41.9 | 14.8 | 28.0 | 12.4 | 1.4 | 1.0 | 0.3 | 3.91 | 2.8% | 1.4% |
| TOTAL_GAMES | 2,075 | 4.2 | 6.0 | 39.8 | 36.7 | 8.5 | 2.1 | 2.6 | 9.99 | 13.2% | 4.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 1,836 | 25.6 | 17.5 | 33.2 | 9.0 | 9.2 | 4.7 | 0.8 | 5.7 | 14.6% | 5.5% |
| GAME_SPREAD | 1,173 | 18.2 | 12.4 | 27.5 | 23.3 | 13.0 | 4.3 | 1.3 | 8.54 | 18.7% | 5.6% |
| TOTAL_GAMES | 2,084 | 6.2 | 8.3 | 33.6 | 28.3 | 15.5 | 4.9 | 3.1 | 10.26 | 23.5% | 8.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8,164 | 44.8% | 26.6% | 13.14 | 34.9% | 15.9% | 10.52 |
| gen1_elo | 8,164 | 44.3% | 25.5% | 12.78 | 34.0% | 15.4% | 10.06 |
| gen1_sr | 8,164 | 52.9% | 31.2% | 16.16 | 44.0% | 20.5% | 13.17 |
| gen2 | 8,164 | 51.7% | 31.7% | 15.67 | 44.1% | 22.7% | 12.93 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,483 | 15.6 | 12.5 | 21.8 | 16.0 | 18.5 | 11.9 | 3.8 | 10.02 | 34.1% | 15.7% |
| STALE | 4,681 | 10.6 | 6.4 | 15.2 | 15.0 | 18.0 | 18.7 | 16.0 | 16.51 | 52.7% | 34.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 1,490 | 15.6 | 10.1 | 23.5 | 15.4 | 17.2 | 14.6 | 3.6 | 10.15 | 35.4% | 18.2% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 16,186 | 1490 | 6955 | 7741 | 29.1 | 197.5 | 1400.4 |
| ge_15pp | 6,982 | 527 | 2478 | 3977 | 34.5 | 452.7 | 1380.4 |
| ge_25pp | 3,904 | 271 | 1137 | 2496 | 45.8 | 560.1 | 1380.4 |
| lt_10pp | 6,749 | 733 | 3368 | 2648 | 26.9 | 54.8 | 1201.9 |

Current slate `SL-20261006T045445Z-a5edf79e`: 1062 priced rows, quote age at build {'median': 5.8, 'max': 5.8}, freshness {'FRESH': 1062}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 271 | 18.4 | 12.6 | 25.8 | 20.3 | 14.4 | 8.1 | 0.4 | 8.01 | 22.9% | 8.5% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 8.3 | 50.0 | 41.7 | 0.0 | 0.0 | 14.32 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 8,164 | 292 (3.6%) | 4.1% | 0.0% | {"EXTERNAL_STALE": 271, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 3,656 | 67 (1.8%) | 7.5% | 0.0% | {"EXTERNAL_STALE": 62, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 2,171 | 23 (1.1%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 23} |
| fair_v1_ge_25pp_pregame_clean | 970 | 23 (2.4%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 23} |
| fair_v1_lt_10pp | 3,247 | 164 (5.1%) | 0.6% | 0.0% | {"EXTERNAL_STALE": 154, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,634 | 11.0 | 8.5 | 20.4 | 15.2 | 20.5 | 14.8 | 9.6 | 12.96 | 44.9% | 24.4% |
| 4-10x | 1,153 | 11.9 | 10.9 | 17.4 | 14.4 | 17.9 | 17.7 | 9.7 | 13.34 | 45.4% | 27.4% |
| <2x | 4,364 | 14.3 | 9.6 | 18.2 | 15.9 | 17.2 | 13.9 | 10.8 | 12.55 | 41.9% | 24.8% |
| >=10x | 1,013 | 9.5 | 4.9 | 14.4 | 14.9 | 19.1 | 23.1 | 14.0 | 18.17 | 56.3% | 37.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 2,106 | 13.7 | 9.0 | 20.3 | 15.9 | 16.6 | 12.5 | 12.1 | 12.01 | 41.2% | 24.6% |
| 300-1000 | 1,895 | 12.3 | 9.4 | 16.8 | 15.2 | 20.6 | 16.1 | 9.5 | 13.67 | 46.2% | 25.6% |
| <300 | 2,264 | 8.0 | 5.8 | 14.6 | 14.5 | 20.6 | 23.1 | 13.3 | 18.37 | 57.1% | 36.5% |
| >=3000 | 1,899 | 17.7 | 12.3 | 21.0 | 16.3 | 14.6 | 10.3 | 7.7 | 9.85 | 32.6% | 18.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 255 | 0.5214 | 0.391 | 0.4353 | +0.086 | -0.044 | 0.0073 ± 0.0088 |
| ratio 4-10x | 178 | 0.578 | 0.4411 | 0.4775 | +0.101 | -0.036 | 0.0166 ± 0.011 |
| ratio <2x | 513 | 0.5352 | 0.4112 | 0.4639 | +0.071 | -0.053 | 0.0128 ± 0.0062 |
| ratio >=10x | 178 | 0.5544 | 0.3821 | 0.4607 | +0.094 | -0.079 | 0.0145 ± 0.014 |
| thinner_sample 1000-3000 | 296 | 0.5406 | 0.4211 | 0.4561 | +0.085 | -0.035 | 0.0094 ± 0.008 |
| thinner_sample 300-1000 | 302 | 0.557 | 0.425 | 0.4768 | +0.080 | -0.052 | 0.006 ± 0.0083 |
| thinner_sample <300 | 375 | 0.5409 | 0.3764 | 0.4507 | +0.090 | -0.074 | 0.0187 ± 0.009 |
| thinner_sample >=3000 | 151 | 0.5166 | 0.4175 | 0.4503 | +0.066 | -0.033 | 0.0155 ± 0.0091 |
| data_status ADEQUATE | 327 | 0.528 | 0.4195 | 0.4526 | +0.075 | -0.033 | 0.0083 ± 0.0069 |
| data_status LIMITED | 230 | 0.5546 | 0.4289 | 0.4913 | +0.063 | -0.062 | 0.0047 ± 0.0096 |
| data_status POOR | 567 | 0.5448 | 0.3904 | 0.4497 | +0.095 | -0.059 | 0.0179 ± 0.0069 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 175 | 0.1826 | 0.1836 | -0.0010 ± 0.0011 | 0.5403 | 0.5429 | 0.4978 | 0.4835 | 0.4971 | -0.091 ± 0.035 | -0.01 (3) |
| 3-5 | 113 | 0.1755 | 0.1765 | -0.0010 ± 0.0033 | 0.5301 | 0.5289 | 0.5149 | 0.4742 | 0.5044 | -0.067 ± 0.041 | 0.02 (1) |
| 5-10 | 228 | 0.1962 | 0.2017 | -0.0055 ± 0.0044 | 0.5778 | 0.5912 | 0.5163 | 0.4424 | 0.5088 | -0.045 ± 0.0301 | -0.0167 (3) |
| 10-15 | 196 | 0.2176 | 0.2127 | +0.0049 ± 0.0082 | 0.6215 | 0.6074 | 0.5207 | 0.3969 | 0.4388 | -0.075 ± 0.0327 | -0.0633 (3) |
| 15-25 | 248 | 0.2181 | 0.2096 | +0.0085 ± 0.0114 | 0.6242 | 0.6041 | 0.5608 | 0.3648 | 0.4435 | -0.045 ± 0.029 | -0.02 (4) |
| 25-40 | 134 | 0.2264 | 0.1785 | +0.0479 ± 0.0224 | 0.6414 | 0.5268 | 0.6241 | 0.3119 | 0.3881 | -0.078 ± 0.0335 | -0.01 (1) |
| 40+ | 30 | 0.3354 | 0.1357 | +0.1998 ± 0.0606 | 0.9067 | 0.4279 | 0.7106 | 0.2678 | 0.2667 | -0.167 ± 0.0655 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 585 | 0.1659 | 0.167 | -0.0011 ± 0.0006 | 0.4996 | 0.502 | 0.5004 | 0.4856 | 0.5282 | -0.020 ± 0.0175 | -0.0188 (8) |
| 3-5 | 384 | 0.1703 | 0.1704 | -0.0001 ± 0.0017 | 0.5163 | 0.5121 | 0.4768 | 0.4369 | 0.4609 | -0.034 ± 0.0213 | 0.02 (1) |
| 5-10 | 863 | 0.1833 | 0.1843 | -0.0010 ± 0.0022 | 0.5469 | 0.5495 | 0.48 | 0.4064 | 0.4473 | -0.020 ± 0.0147 | -0.0129 (7) |
| 10-15 | 763 | 0.1885 | 0.1736 | +0.0149 ± 0.0037 | 0.5583 | 0.5124 | 0.472 | 0.3483 | 0.3499 | -0.060 ± 0.015 | -0.0633 (3) |
| 15-25 | 970 | 0.1983 | 0.1619 | +0.0364 ± 0.0051 | 0.5854 | 0.4818 | 0.4763 | 0.2779 | 0.2856 | -0.052 ± 0.0128 | -0.017 (10) |
| 25-40 | 966 | 0.2109 | 0.0985 | +0.1123 ± 0.0064 | 0.6136 | 0.32 | 0.5054 | 0.1895 | 0.1718 | -0.069 ± 0.0098 | -0.01 (1) |
| 40+ | 721 | 0.3728 | 0.0364 | +0.3364 ± 0.0077 | 0.9695 | 0.1572 | 0.6155 | 0.1031 | 0.0402 | -0.092 ± 0.0066 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 119 | 0.1798 | 0.181 | -0.0012 ± 0.0013 | 0.5335 | 0.5343 | 0.5056 | 0.4907 | 0.521 | -0.062 ± 0.039 | -0.01 (1) |
| 3-5 | 86 | 0.1995 | 0.1972 | +0.0024 ± 0.0038 | 0.576 | 0.576 | 0.4957 | 0.4565 | 0.4419 | -0.102 ± 0.0519 | 0.02 (1) |
| 5-10 | 207 | 0.1835 | 0.184 | -0.0006 ± 0.0045 | 0.5475 | 0.548 | 0.5724 | 0.4971 | 0.5314 | -0.070 ± 0.0307 | -0.01 (4) |
| 10-15 | 187 | 0.2291 | 0.2189 | +0.0102 ± 0.0086 | 0.6482 | 0.6288 | 0.578 | 0.4538 | 0.4813 | -0.088 ± 0.0359 | -0.0667 (3) |
| 15-25 | 280 | 0.2252 | 0.1999 | +0.0253 ± 0.0107 | 0.6374 | 0.578 | 0.5847 | 0.3874 | 0.4286 | -0.092 ± 0.0278 | -0.0167 (3) |
| 25-40 | 170 | 0.2612 | 0.1959 | +0.0653 ± 0.0212 | 0.7253 | 0.5714 | 0.651 | 0.3386 | 0.3882 | -0.102 ± 0.0351 | -0.025 (2) |
| 40+ | 75 | 0.3809 | 0.1679 | +0.2130 ± 0.0479 | 1.0429 | 0.5054 | 0.741 | 0.2489 | 0.2933 | -0.076 ± 0.0454 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 471 | 0.1552 | 0.1564 | -0.0012 ± 0.0006 | 0.4718 | 0.4742 | 0.5249 | 0.5101 | 0.5414 | -0.019 ± 0.0185 | -0.0217 (6) |
| 3-5 | 323 | 0.1778 | 0.1757 | +0.0021 ± 0.0019 | 0.5231 | 0.5208 | 0.5222 | 0.4824 | 0.4768 | -0.060 ± 0.0242 | 0.02 (1) |
| 5-10 | 774 | 0.1677 | 0.1696 | -0.0019 ± 0.0023 | 0.508 | 0.5092 | 0.5202 | 0.4453 | 0.4897 | -0.012 ± 0.0149 | -0.01 (5) |
| 10-15 | 682 | 0.1907 | 0.1794 | +0.0112 ± 0.004 | 0.5642 | 0.5272 | 0.5073 | 0.3834 | 0.4062 | -0.043 ± 0.0165 | -0.0575 (4) |
| 15-25 | 1071 | 0.2074 | 0.1656 | +0.0418 ± 0.0049 | 0.6044 | 0.4941 | 0.5103 | 0.3136 | 0.3119 | -0.068 ± 0.0125 | -0.0143 (7) |
| 25-40 | 1004 | 0.2319 | 0.1194 | +0.1126 ± 0.0069 | 0.6657 | 0.3739 | 0.5373 | 0.2203 | 0.2042 | -0.071 ± 0.0111 | -0.015 (6) |
| 40+ | 927 | 0.4083 | 0.0563 | +0.3520 ± 0.009 | 1.0654 | 0.2116 | 0.6603 | 0.122 | 0.0734 | -0.082 ± 0.0074 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 180 | 0.1948 | 0.1967 | -0.0019 ± 0.0012 | 0.5694 | 0.5755 | 0.5179 | 0.5032 | 0.5333 | -0.058 ± 0.0333 | -0.01 (5) |
| 3-5 | 119 | 0.1674 | 0.1642 | +0.0032 ± 0.003 | 0.5063 | 0.4991 | 0.5042 | 0.4646 | 0.4454 | -0.131 ± 0.0399 | -- (0) |
| 5-10 | 230 | 0.1957 | 0.1946 | +0.0011 ± 0.0044 | 0.5796 | 0.5716 | 0.5019 | 0.4289 | 0.4522 | -0.080 ± 0.029 | -0.01 (3) |
| 10-15 | 187 | 0.2149 | 0.2138 | +0.0011 ± 0.0084 | 0.6186 | 0.6133 | 0.5416 | 0.4183 | 0.4813 | -0.061 ± 0.0339 | -0.044 (5) |
| 15-25 | 244 | 0.2134 | 0.2037 | +0.0098 ± 0.0112 | 0.6175 | 0.588 | 0.5741 | 0.38 | 0.4508 | -0.057 ± 0.0282 | -0.03 (1) |
| 25-40 | 139 | 0.2231 | 0.1934 | +0.0297 ± 0.0227 | 0.6374 | 0.5631 | 0.6254 | 0.3133 | 0.4173 | -0.057 ± 0.0339 | 0.0 (1) |
| 40+ | 25 | 0.3648 | 0.1373 | +0.2275 ± 0.0667 | 0.9712 | 0.4311 | 0.711 | 0.2606 | 0.24 | -0.185 ± 0.0761 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 602 | 0.1737 | 0.174 | -0.0003 ± 0.0006 | 0.5204 | 0.5214 | 0.5013 | 0.4866 | 0.5 | -0.047 ± 0.017 | -0.0162 (13) |
| 3-5 | 406 | 0.1749 | 0.1726 | +0.0024 ± 0.0017 | 0.5277 | 0.5263 | 0.4873 | 0.4478 | 0.4409 | -0.069 ± 0.0211 | -0.01 (2) |
| 5-10 | 881 | 0.1822 | 0.1742 | +0.0080 ± 0.0021 | 0.5455 | 0.5184 | 0.4683 | 0.3947 | 0.3768 | -0.075 ± 0.0141 | -0.01 (3) |
| 10-15 | 712 | 0.1915 | 0.1823 | +0.0091 ± 0.004 | 0.5653 | 0.5357 | 0.4813 | 0.3577 | 0.3834 | -0.037 ± 0.016 | -0.03 (9) |
| 15-25 | 1049 | 0.1872 | 0.1499 | +0.0374 ± 0.0048 | 0.563 | 0.4521 | 0.4826 | 0.2832 | 0.2898 | -0.052 ± 0.0118 | -0.03 (2) |
| 25-40 | 927 | 0.2105 | 0.0995 | +0.1111 ± 0.0066 | 0.6135 | 0.3193 | 0.5022 | 0.1823 | 0.1704 | -0.066 ± 0.0099 | 0.0 (1) |
| 40+ | 675 | 0.3902 | 0.0381 | +0.3521 ± 0.0084 | 1.0177 | 0.1622 | 0.625 | 0.1034 | 0.0385 | -0.093 ± 0.0071 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 452 | 0.2034 | 0.2034 | +0.0000 ± 0.0007 | 0.5886 | 0.589 | 0.497 | 0.4824 | 0.4845 | -0.041 ± 0.0212 | -0.0226 (46) |
| 3-5 | 336 | 0.1962 | 0.1954 | +0.0008 ± 0.0019 | 0.5755 | 0.5717 | 0.469 | 0.4293 | 0.4435 | -0.035 ± 0.0239 | -0.0059 (32) |
| 5-10 | 694 | 0.1865 | 0.1821 | +0.0044 ± 0.0024 | 0.556 | 0.5437 | 0.4595 | 0.3862 | 0.3934 | -0.039 ± 0.0163 | -0.005 (72) |
| 10-15 | 465 | 0.2028 | 0.1916 | +0.0112 ± 0.0051 | 0.5946 | 0.5633 | 0.4596 | 0.3363 | 0.3527 | -0.034 ± 0.0201 | 0.0016 (63) |
| 15-25 | 631 | 0.2324 | 0.2085 | +0.0239 ± 0.0071 | 0.6584 | 0.6023 | 0.5278 | 0.3347 | 0.3708 | -0.028 ± 0.0181 | -0.0216 (58) |
| 25-40 | 315 | 0.2642 | 0.1672 | +0.0970 ± 0.0144 | 0.7336 | 0.5027 | 0.573 | 0.2616 | 0.2603 | -0.068 ± 0.0226 | -0.0216 (25) |
| 40+ | 98 | 0.424 | 0.155 | +0.2689 ± 0.0426 | 1.187 | 0.48 | 0.7319 | 0.2239 | 0.2347 | -0.063 ± 0.0412 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 863 | 0.1976 | 0.197 | +0.0005 ± 0.0005 | 0.5769 | 0.5752 | 0.4928 | 0.4783 | 0.4658 | -0.053 ± 0.0151 | -0.0155 (82) |
| 3-5 | 633 | 0.1944 | 0.1932 | +0.0011 ± 0.0014 | 0.5703 | 0.5667 | 0.4715 | 0.4316 | 0.4392 | -0.036 ± 0.0175 | -0.018 (54) |
| 5-10 | 1301 | 0.1848 | 0.1792 | +0.0055 ± 0.0018 | 0.5513 | 0.5341 | 0.4452 | 0.3712 | 0.3736 | -0.039 ± 0.0118 | -0.0089 (122) |
| 10-15 | 969 | 0.1955 | 0.183 | +0.0125 ± 0.0034 | 0.5763 | 0.541 | 0.4511 | 0.3279 | 0.3395 | -0.033 ± 0.0136 | -0.0053 (99) |
| 15-25 | 1351 | 0.221 | 0.1855 | +0.0355 ± 0.0046 | 0.6386 | 0.5444 | 0.5027 | 0.3071 | 0.3146 | -0.043 ± 0.0117 | -0.0255 (106) |
| 25-40 | 945 | 0.2431 | 0.1285 | +0.1146 ± 0.0074 | 0.6884 | 0.4007 | 0.5287 | 0.2134 | 0.1905 | -0.070 ± 0.0115 | -0.0206 (47) |
| 40+ | 523 | 0.3869 | 0.0789 | +0.3080 ± 0.0135 | 1.0548 | 0.2672 | 0.6502 | 0.1347 | 0.1052 | -0.072 ± 0.0125 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 1124 | 1.117 ± 0.086 | 1.235 | 0.1689 | 0.1797 | 0.2079 | 0.1955 |
| gen2 | 1124 | 0.917 ± 0.076 | 1.157 | 0.1847 | 0.1798 | 0.2272 | 0.1952 |
| gen1_elo | 1124 | 1.108 ± 0.084 | 1.193 | 0.1741 | 0.18 | 0.2067 | 0.1955 |
| gen1_sr | 1124 | 1.136 ± 0.099 | 1.208 | 0.1417 | 0.1818 | 0.2223 | 0.1952 |
| gen1_ledger | 2991 | 0.899 ± 0.049 | 1.069 | 0.1623 | 0.2011 | 0.2183 | 0.1914 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 6,982)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,098 | 30.0% |
| STALE_QUOTE | market_freshness | 1,873 | 26.8% |
| BOOK_QUALITY | execution | 986 | 14.1% |
| POOR_DATA | data | 606 | 8.7% |
| LIMITED_DATA | data | 385 | 5.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 345 | 4.9% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 330 | 4.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 198 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 158 | 2.3% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.0% |

Cause class: coverage 30.0%, market_freshness 26.8%, data 14.2%, execution 14.1%, market_freshness/coverage 7.8%, model_calibration_or_unknown 4.7%, mapping 2.3%, model_calibration 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 95.3%, LOW_DATA_QUALITY 67.0%, STALE_KALSHI_QUOTE 57.0%, THIN_PLAYER_HISTORY 56.5%, STALE_PLAYER_DATA 55.8%, MODEL_INTERNAL_DISAGREEMENT 36.2%, ASYMMETRIC_SAMPLE_SIZE 30.5%, WIDE_SPREAD 22.1%, MODEL_HIGH_UNCERTAINTY 14.4%, PLAYER_IDENTITY_RISK 11.1%, LEVEL_TRANSFER_RISK 8.2%, EVENT_MAPPING_RISK 6.7%, LOW_DISPLAYED_LIQUIDITY 6.3%, MODEL_CALIBRATION_OUTLIER 2.3%, UNKNOWN 0.6%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 32.3%, POST_SETTLEMENT_OBSERVATION 30.0%, POSSIBLE_IN_PLAY_QUOTE 5.5%, CONFIRMED_IN_PLAY_QUOTE 0.9%

### >= ge_25 pp (N = 3,904)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,663 | 42.6% |
| STALE_QUOTE | market_freshness | 857 | 21.9% |
| BOOK_QUALITY | execution | 511 | 13.1% |
| POOR_DATA | data | 273 | 7.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 185 | 4.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 118 | 3.0% |
| LIMITED_DATA | data | 109 | 2.8% |
| IDENTITY_AMBIGUOUS | mapping | 102 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 86 | 2.2% |

Cause class: coverage 42.6%, market_freshness 21.9%, execution 13.1%, data 9.8%, market_freshness/coverage 7.8%, mapping 2.6%, model_calibration_or_unknown 2.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.4%, LOW_DATA_QUALITY 70.2%, STALE_KALSHI_QUOTE 63.9%, THIN_PLAYER_HISTORY 59.0%, STALE_PLAYER_DATA 53.0%, MODEL_INTERNAL_DISAGREEMENT 38.2%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 20.8%, MODEL_HIGH_UNCERTAINTY 15.6%, PLAYER_IDENTITY_RISK 13.7%, LEVEL_TRANSFER_RISK 7.8%, EVENT_MAPPING_RISK 7.6%, LOW_DISPLAYED_LIQUIDITY 6.8%, MODEL_CALIBRATION_OUTLIER 3.1%, UNKNOWN 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 44.9%, POST_SETTLEMENT_OBSERVATION 42.6%, POSSIBLE_IN_PLAY_QUOTE 5.4%, CONFIRMED_IN_PLAY_QUOTE 0.9%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 3267, "IDENTITY_AMBIGUOUS": 637}; ticker orientation: {"VERIFIED": 3904}.

Checks: discipline:AMBIGUOUS 193, discipline:PASS 3711, identity_confidence:AMBIGUOUS 535, identity_confidence:PASS 3369, level_mapping:NA 205, level_mapping:PASS 3699, market_pair:AMBIGUOUS 134, market_pair:NA 93, market_pair:PASS 3677, model_complement:NA 62, model_complement:PASS 3842, namesake:PASS 3904, physical_match_id:NA 1733, physical_match_id:PASS 2171, player_ids:PASS 3904, same_pair_other_event:PASS 3904, ticker_orientation:PASS 3904

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 783 | 2.9% | 3.0% | 0.6% | {"market_freshness": 20, "execution": 3} | 5.84 | 0.1791 / 0.1823 (49) | 27.6% | 0.3% | 5.1% | 1.4% |
| CHALLENGER | 2,804 | 20.0% | 7.7% | 14.3% | {"coverage": 331, "market_freshness": 104, "market_freshness/coverage": 67, "model_calibration_or_unknown": 29, "data": 25, "execution": 4} | 7.45 | 0.2216 / 0.2064 (708) | 53.0% | 5.7% | 1.4% | 24.6% |
| DOUBLES | 430 | 44.9% | 44.6% | 4.9% | {"market_freshness": 106, "mapping": 34, "execution": 34, "market_freshness/coverage": 12, "coverage": 7} | 23.05 | 0.3189 / 0.2288 (164) | 54.4% | 0.0% | 100.0% | 9.3% |
| ITF_MEN | 4,792 | 26.4% | 17.5% | 32.5% | {"coverage": 578, "execution": 233, "market_freshness": 220, "data": 140, "market_freshness/coverage": 80, "mapping": 15, "model_calibration_or_unknown": 1} | 10.83 | 0.2148 / 0.1881 (1393) | 48.8% | 54.5% | 7.0% | 27.2% |
| ITF_WOMEN | 5,767 | 29.1% | 20.1% | 43.1% | {"coverage": 730, "market_freshness": 358, "execution": 224, "data": 195, "market_freshness/coverage": 104, "mapping": 49, "model_calibration_or_unknown": 21} | 12.98 | 0.2042 / 0.1854 (1407) | 50.7% | 61.1% | 10.8% | 27.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.3% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 872 | 9.1% | 7.8% | 2.0% | {"market_freshness": 34, "model_calibration_or_unknown": 16, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.47 | 0.1994 / 0.1937 (131) | 37.2% | 2.4% | 1.4% | 3.4% |
| WTA125 | 589 | 15.1% | 9.3% | 2.3% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 17, "market_freshness": 13, "coverage": 12, "data": 11, "execution": 4, "mapping": 2} | 10.08 | 0.2273 / 0.204 (221) | 30.2% | 6.8% | 3.6% | 14.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 4 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 5 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 6 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 7 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 8 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 9 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 10 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 12 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 13 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 15 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 16 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 17 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 18 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 19 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 20 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 21 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 22 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 23 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 24 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 253 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 25 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 26 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 27 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 28 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 29 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 30 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 31 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 32 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 37 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 38 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 40 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 732 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 41 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 42 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT05CASMUN-CAS` | CHALLENGER | fair_v1 | 83% / 14% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 192 min (STALE); data POOR (grade D, thinner serve sample 814.0, ratio 3.76); no external reference |
| 44 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 45 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 47 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 48 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 49 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 50 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9738, "by_level_share_of_ge_25pp": {"ATP": 0.0059, "CHALLENGER": 0.1434, "DOUBLES": 0.0494, "ITF_MEN": 0.3245, "ITF_WOMEN": 0.4306, "OTHER": 0.0031, "WTA": 0.0202, "WTA125": 0.0228}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6393, "share_primary_cause_market_settled_or_in_play": 0.5036, "share_primary_cause_stale_quote_only": 0.2195}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 3904, "identity_ambiguous_share": 0.1632, "ticker_orientation": {"VERIFIED": 3904}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 2171, "with_external": 23, "coverage": 0.0106, "external_status": {"EXTERNAL_STALE": 23}, "triangulation": {"INSUFFICIENT_INPUTS": 23}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 970, "with_external": 23, "coverage": 0.0237, "external_status": {"EXTERNAL_STALE": 23}, "triangulation": {"INSUFFICIENT_INPUTS": 23}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 616.0, "median_sample_ratio": 2.35, "median_min_matches": 21.0, "median_max_days_since_last": 191.0, "share_severe_asymmetry": 0.1834, "data_status": {"POOR": 2041, "LIMITED": 1107, "ADEQUATE": 756}, "comparison_lt_10pp": {"median_thinner_serve_points": 1868.0, "median_sample_ratio": 1.73, "median_min_matches": 79.5}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 255, "model_minus_observed": 0.0861, "kalshi_minus_observed": -0.0443, "brier_diff_model_minus_kalshi": 0.0073}, "4-10x": {"n": 178, "model_minus_observed": 0.1005, "kalshi_minus_observed": -0.0364, "brier_diff_model_minus_kalshi": 0.0166}, "<2x": {"n": 513, "model_minus_observed": 0.0713, "kalshi_minus_observed": -0.0528, "brier_diff_model_minus_kalshi": 0.0128}, ">=10x": {"n": 178, "model_minus_observed": 0.0937, "kalshi_minus_observed": -0.0785, "brier_diff_model_minus_kalshi": 0.0145}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 1124, "model": {"intercept": -0.622, "slope": 0.917, "slope_se": 0.076}, "kalshi_mid_same_rows": {"intercept": 0.214, "slope": 1.157, "slope_se": 0.084}, "mean_extremity_model": 0.1847, "mean_extremity_kalshi": 0.1798, "model_brier": 0.2272, "kalshi_brier": 0.1952, "brier_diff_model_minus_kalshi": 0.0321, "brier_diff_se": 0.0057, "model_logloss": 0.6473, "kalshi_logloss": 0.5703}, "fair_v1": {"n": 1124, "model": {"intercept": -0.412, "slope": 1.117, "slope_se": 0.086}, "kalshi_mid_same_rows": {"intercept": 0.359, "slope": 1.235, "slope_se": 0.088}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1797, "model_brier": 0.2079, "kalshi_brier": 0.1955, "brier_diff_model_minus_kalshi": 0.0124, "brier_diff_se": 0.0045, "model_logloss": 0.6014, "kalshi_logloss": 0.5711}, "gen1_elo": {"n": 1124, "model": {"intercept": -0.441, "slope": 1.108, "slope_se": 0.084}, "kalshi_mid_same_rows": {"intercept": 0.3, "slope": 1.193, "slope_se": 0.085}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.18, "model_brier": 0.2067, "kalshi_brier": 0.1955, "brier_diff_model_minus_kalshi": 0.0113, "brier_diff_se": 0.0044, "model_logloss": 0.6008, "kalshi_logloss": 0.5709}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2659, "share_ge_15": 0.4478, "median_abs_gap": 13.14, "n": 8164}, "gen1_elo": {"share_ge_25": 0.2549, "share_ge_15": 0.4432, "median_abs_gap": 12.78, "n": 8164}, "gen1_sr": {"share_ge_25": 0.3125, "share_ge_15": 0.5295, "median_abs_gap": 16.16, "n": 8164}, "gen2": {"share_ge_25": 0.3169, "share_ge_15": 0.5174, "median_abs_gap": 15.67, "n": 8164}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.159, "share_ge_15": 0.3486, "median_abs_gap": 10.52, "n": 6101}, "gen1_elo": {"share_ge_25": 0.1537, "share_ge_15": 0.3403, "median_abs_gap": 10.06, "n": 6101}, "gen1_sr": {"share_ge_25": 0.2054, "share_ge_15": 0.4401, "median_abs_gap": 13.17, "n": 6101}, "gen2": {"share_ge_25": 0.2268, "share_ge_15": 0.4407, "median_abs_gap": 12.93, "n": 6101}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0294, "share_ge_25_pregame_clean": 0.0298}, "WTA": {"median_abs_gap_pregame_clean": 8.47, "share_ge_25_all": 0.0906, "share_ge_25_pregame_clean": 0.0784}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2247, "share_within_10pp_all": 0.417, "share_within_10pp_pregame_clean": 0.4865, "corr_model_vs_mid_pregame_clean": 0.8311}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 175, "model_brier": 0.1826, "kalshi_brier": 0.1836, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 196, "model_brier": 0.2176, "kalshi_brier": 0.2127, "brier_diff_model_minus_kalshi": 0.0049}, "15-25": {"n_settled": 248, "model_brier": 0.2181, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.0085}, "25-40": {"n_settled": 134, "model_brier": 0.2264, "kalshi_brier": 0.1785, "brier_diff_model_minus_kalshi": 0.0479}, "3-5": {"n_settled": 113, "model_brier": 0.1755, "kalshi_brier": 0.1765, "brier_diff_model_minus_kalshi": -0.001}, "40+": {"n_settled": 30, "model_brier": 0.3354, "kalshi_brier": 0.1357, "brier_diff_model_minus_kalshi": 0.1998}, "5-10": {"n_settled": 228, "model_brier": 0.1962, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": -0.0055}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.554, "slope": 0.899, "slope_se": 0.049}, "kalshi_slope": {"intercept": 0.107, "slope": 1.069, "slope_se": 0.05}, "n": 2991}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 164, "model_brier": 0.3189, "kalshi_brier": 0.2288, "brier_diff_model_minus_kalshi": 0.0901, "brier_diff_se": 0.0256, "corr_model_outcome": -0.0904, "corr_kalshi_outcome": 0.3354}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
