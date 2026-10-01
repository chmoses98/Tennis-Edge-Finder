# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-01T06:37Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 9,289): 0-3 13.4%, 3-5 9.4%, 5-10 19.8%, 10-15 14.7%, 15-25 19.8%, 25-40 14.0%, 40+ 8.9%; median gap 12.27 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.0%, Challenger 11.5%, doubles 8.2%). Main tour: ATP 3.2% and WTA 7.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,123): MARKET_ALREADY_SETTLED_WHEN_PRICED 42.2%, STALE_QUOTE 24.3%, POOR_DATA 7.3%, BOOK_QUALITY 6.3%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IN_PLAY_QUOTE 5.7%, LIMITED_DATA 3.6%, IDENTITY_AMBIGUOUS 2.7%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%. By class: coverage 42.2%, market_freshness 24.3%, market_freshness/coverage 11.6%, data 10.9%, execution 6.3%, mapping 2.7%, model_calibration_or_unknown 2.0%.
* **Stale / settled / in-play**: 66.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 53.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,123 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.4%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.5% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 668.0 points vs 1937.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.198, Gen-2 0.933, Gen-1 ledger 0.901 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 68 model 0.2385 vs Kalshi 0.1851; n 16 model 0.3076 vs Kalshi 0.132.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 27,615 model-market comparisons (47,577 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 15,684 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-01T06:33:01.837258+00:00'], shadow board 7,223 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-01T06:33:05.413610+00:00'], Model 4 1,992 rows, 7,566 settled tickers, 1,772 tickers with an external scan.
* By model: {"gen1_ledger": 9207, "gen1_elo": 3631, "fair_v1": 3631, "gen2": 3631, "gen1_sr": 3631, "model4_fundamental": 1943, "model4_conditioned": 1941}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 9,289 | 13.4 | 9.4 | 19.8 | 14.7 | 19.8 | 14.0 | 8.9 | 12.27 | 42.7% | 22.9% |
| MW fair_v1 | 3,631 | 13.5 | 9.4 | 19.1 | 14.7 | 19.0 | 14.5 | 9.8 | 12.62 | 43.4% | 24.3% |
| MW gen1_elo | 3,631 | 14.2 | 8.7 | 19.7 | 15.2 | 18.6 | 14.5 | 9.1 | 12.1 | 42.2% | 23.6% |
| MW gen1_ledger | 5,658 | 13.3 | 9.5 | 20.2 | 14.7 | 20.3 | 13.6 | 8.3 | 12.16 | 42.2% | 21.9% |
| MW gen1_sr | 3,631 | 10.1 | 6.8 | 17.2 | 13.9 | 21.3 | 18.4 | 12.4 | 15.68 | 52.0% | 30.8% |
| MW gen2 | 3,631 | 11.1 | 6.6 | 16.4 | 15.5 | 20.0 | 17.0 | 13.6 | 15.31 | 50.5% | 30.5% |
| all families model4_conditioned | 1,941 | 19.5 | 14.9 | 29.6 | 22.1 | 10.1 | 1.9 | 2.0 | 7.29 | 13.9% | 3.9% |
| all families model4_fundamental | 1,943 | 13.8 | 10.8 | 31.2 | 22.0 | 13.9 | 5.6 | 2.7 | 8.99 | 22.2% | 8.3% |

Configurable thresholds (primary): >=5pp 77.2%, >=10pp 57.4%, >=15pp 42.7%, >=20pp 31.7%, >=25pp 22.9%, >=30pp 17.0%, >=40pp 8.9%, >=50pp 4.0%
Executable gap (model outside the book, before fees): median 9.85pp; >=10pp 49.6%, >=25pp 20.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 182 | 22.5 | 20.9 | 22.5 | 12.1 | 17.6 | 1.6 | 2.8 | 5.95 | 22.0% | 4.4% |
| CHALLENGER | 676 | 16.4 | 9.0 | 15.8 | 16.0 | 16.9 | 13.3 | 12.6 | 13.16 | 42.8% | 25.9% |
| ITF_MEN | 1,143 | 12.2 | 9.4 | 20.2 | 13.5 | 18.5 | 15.1 | 11.3 | 12.26 | 44.8% | 26.3% |
| ITF_WOMEN | 1,275 | 10.8 | 7.5 | 16.7 | 15.0 | 21.0 | 18.6 | 10.5 | 15.04 | 50.1% | 29.1% |
| WTA | 283 | 19.4 | 12.4 | 31.8 | 13.1 | 17.7 | 5.7 | 0.0 | 7.76 | 23.3% | 5.7% |
| WTA125 | 72 | 9.7 | 5.6 | 18.1 | 27.8 | 22.2 | 11.1 | 5.6 | 12.8 | 38.9% | 16.7% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 182 | 23.6 | 13.7 | 23.1 | 15.9 | 18.1 | 2.2 | 3.3 | 6.75 | 23.6% | 5.5% |
| CHALLENGER | 676 | 11.1 | 6.1 | 18.6 | 17.5 | 17.3 | 16.9 | 12.6 | 14.44 | 46.8% | 29.4% |
| ITF_MEN | 1,143 | 10.6 | 6.0 | 16.6 | 16.2 | 19.8 | 17.1 | 13.7 | 15.32 | 50.6% | 30.8% |
| ITF_WOMEN | 1,275 | 8.8 | 6.6 | 13.5 | 13.2 | 19.9 | 19.8 | 18.2 | 18.32 | 58.0% | 38.0% |
| WTA | 283 | 17.0 | 5.7 | 18.7 | 16.6 | 26.9 | 14.1 | 1.1 | 13.64 | 42.0% | 15.2% |
| WTA125 | 72 | 4.2 | 5.6 | 15.3 | 20.8 | 26.4 | 15.3 | 12.5 | 16.39 | 54.2% | 27.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 182 | 33.5 | 13.2 | 24.7 | 9.9 | 9.3 | 6.6 | 2.8 | 5.46 | 18.7% | 9.3% |
| CHALLENGER | 676 | 16.1 | 7.8 | 19.8 | 15.7 | 15.7 | 13.6 | 11.2 | 11.54 | 40.5% | 24.9% |
| ITF_MEN | 1,143 | 11.3 | 9.9 | 18.3 | 15.5 | 18.3 | 15.7 | 11.1 | 12.77 | 45.1% | 26.8% |
| ITF_WOMEN | 1,275 | 10.3 | 6.9 | 17.4 | 14.6 | 23.1 | 18.2 | 9.5 | 15.38 | 50.8% | 27.7% |
| WTA | 283 | 26.1 | 11.3 | 31.8 | 14.8 | 14.1 | 1.8 | 0.0 | 6.73 | 15.9% | 1.8% |
| WTA125 | 72 | 18.1 | 5.6 | 22.2 | 30.6 | 13.9 | 9.7 | 0.0 | 10.72 | 23.6% | 9.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 71 | 23.9 | 22.5 | 35.2 | 11.3 | 7.0 | 0.0 | 0.0 | 6.19 | 7.0% | 0.0% |
| CHALLENGER | 772 | 21.2 | 13.7 | 26.4 | 15.9 | 13.6 | 6.5 | 2.6 | 7.45 | 22.7% | 9.1% |
| DOUBLES | 358 | 5.6 | 3.6 | 9.8 | 10.3 | 21.8 | 20.4 | 28.5 | 24.23 | 70.7% | 48.9% |
| ITF_MEN | 1,889 | 14.2 | 9.1 | 19.1 | 13.6 | 21.2 | 13.6 | 9.3 | 12.5 | 44.0% | 22.8% |
| ITF_WOMEN | 1,725 | 9.0 | 8.4 | 17.8 | 14.4 | 23.2 | 18.3 | 8.8 | 15.13 | 50.3% | 27.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 331 | 13.6 | 9.7 | 21.1 | 17.2 | 23.3 | 11.2 | 3.9 | 11.35 | 38.4% | 15.1% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 181 | 22.1 | 21.0 | 22.6 | 12.2 | 17.7 | 1.7 | 2.8 | 6.01 | 22.1% | 4.4% |
| CHALLENGER | 506 | 20.4 | 11.5 | 18.6 | 18.8 | 17.6 | 8.3 | 4.9 | 9.95 | 30.8% | 13.2% |
| ITF_MEN | 819 | 16.1 | 11.8 | 24.5 | 14.8 | 18.4 | 10.3 | 4.0 | 9.28 | 32.7% | 14.3% |
| ITF_WOMEN | 922 | 14.2 | 9.1 | 19.2 | 17.6 | 22.0 | 13.8 | 4.1 | 12.43 | 39.9% | 17.9% |
| WTA | 282 | 19.5 | 12.4 | 31.9 | 13.1 | 17.7 | 5.3 | 0.0 | 7.61 | 23.1% | 5.3% |
| WTA125 | 71 | 9.9 | 5.6 | 18.3 | 28.2 | 22.5 | 9.9 | 5.6 | 12.79 | 38.0% | 15.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 181 | 23.8 | 13.3 | 23.2 | 16.0 | 18.2 | 2.2 | 3.3 | 6.93 | 23.8% | 5.5% |
| CHALLENGER | 506 | 13.4 | 7.5 | 22.9 | 20.9 | 19.0 | 12.2 | 4.0 | 11.57 | 35.2% | 16.2% |
| ITF_MEN | 819 | 13.2 | 7.6 | 20.0 | 18.1 | 21.6 | 13.4 | 6.1 | 12.46 | 41.1% | 19.5% |
| ITF_WOMEN | 922 | 10.1 | 8.5 | 15.4 | 13.6 | 22.6 | 18.0 | 11.9 | 15.86 | 52.5% | 29.9% |
| WTA | 282 | 17.0 | 5.7 | 18.8 | 16.7 | 26.9 | 13.8 | 1.1 | 13.61 | 41.8% | 14.9% |
| WTA125 | 71 | 4.2 | 5.6 | 15.5 | 21.1 | 26.8 | 15.5 | 11.3 | 16.14 | 53.5% | 26.8% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 59 | 25.4 | 25.4 | 35.6 | 11.9 | 1.7 | 0.0 | 0.0 | 4.87 | 1.7% | 0.0% |
| CHALLENGER | 636 | 23.6 | 16.0 | 29.2 | 15.4 | 12.7 | 2.8 | 0.2 | 6.68 | 15.7% | 3.0% |
| DOUBLES | 277 | 6.1 | 3.2 | 9.8 | 10.5 | 22.0 | 21.3 | 27.1 | 24.11 | 70.4% | 48.4% |
| ITF_MEN | 1,369 | 17.2 | 10.7 | 22.5 | 14.5 | 20.9 | 10.4 | 3.6 | 9.9 | 35.0% | 14.1% |
| ITF_WOMEN | 1,195 | 11.0 | 9.6 | 21.4 | 16.4 | 24.2 | 15.1 | 2.3 | 12.17 | 41.6% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 255 | 15.3 | 9.0 | 25.5 | 23.5 | 19.6 | 7.1 | 0.0 | 10.01 | 26.7% | 7.1% |
| WTA125 | 252 | 16.3 | 10.7 | 25.4 | 19.8 | 21.0 | 6.3 | 0.4 | 9.32 | 27.8% | 6.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 358 | 5.6 | 3.6 | 9.8 | 10.3 | 21.8 | 20.4 | 28.5 | 24.23 | 70.7% | 48.9% |
| singles | 5,300 | 13.9 | 9.9 | 21.0 | 15.0 | 20.2 | 13.2 | 6.9 | 11.66 | 40.3% | 20.1% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 814 | 16.2 | 8.5 | 19.2 | 14.0 | 17.7 | 12.9 | 11.6 | 11.8 | 42.1% | 24.4% |
| Hard | 2,580 | 12.6 | 9.9 | 19.5 | 14.5 | 19.4 | 14.7 | 9.3 | 12.71 | 43.5% | 24.1% |
| UNKNOWN | 237 | 13.9 | 6.8 | 15.2 | 18.1 | 19.4 | 17.3 | 9.3 | 13.49 | 46.0% | 26.6% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,042 | 18.0 | 11.9 | 21.4 | 15.4 | 17.1 | 10.0 | 6.2 | 9.88 | 33.3% | 16.2% |
| B | 466 | 14.2 | 11.8 | 16.7 | 18.9 | 16.7 | 10.3 | 11.4 | 12.12 | 38.4% | 21.7% |
| C | 618 | 13.9 | 9.1 | 25.1 | 12.8 | 15.4 | 13.4 | 10.4 | 10.83 | 39.2% | 23.8% |
| D | 695 | 12.2 | 9.2 | 17.4 | 13.7 | 21.1 | 14.8 | 11.5 | 14.1 | 47.5% | 26.3% |
| F | 810 | 8.0 | 5.1 | 14.6 | 13.6 | 23.8 | 23.2 | 11.7 | 18.69 | 58.8% | 34.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,736 | 18.9 | 12.0 | 26.6 | 16.9 | 16.5 | 6.5 | 2.5 | 8.5 | 25.6% | 9.0% |
| B | 937 | 14.2 | 9.1 | 21.8 | 16.6 | 19.0 | 12.2 | 7.2 | 11.46 | 38.3% | 19.3% |
| C | 1,166 | 11.2 | 8.5 | 15.7 | 14.2 | 21.8 | 15.1 | 13.6 | 15.18 | 50.4% | 28.6% |
| D | 870 | 11.5 | 8.4 | 20.5 | 11.7 | 23.9 | 15.5 | 8.5 | 14.13 | 47.9% | 24.0% |
| F | 949 | 6.6 | 7.4 | 12.6 | 12.1 | 23.4 | 24.6 | 13.3 | 19.55 | 61.2% | 37.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,262 | 16.0 | 10.9 | 20.1 | 16.7 | 17.3 | 10.4 | 8.6 | 10.71 | 36.3% | 19.0% |
| LIMITED | 849 | 15.8 | 11.4 | 23.8 | 13.7 | 14.7 | 12.0 | 8.6 | 9.86 | 35.3% | 20.6% |
| POOR | 1,520 | 10.1 | 6.9 | 15.8 | 13.5 | 22.9 | 19.3 | 11.5 | 16.61 | 53.7% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 325 | 34.8 | 23.1 | 32.9 | 5.8 | 2.5 | 0.9 | 0.0 | 4.14 | 3.4% | 0.9% |
| GAME_SPREAD | 394 | 20.3 | 16.5 | 36.3 | 16.0 | 9.1 | 1.3 | 0.5 | 6.5 | 10.9% | 1.8% |
| MATCH_WINNER | 5,658 | 13.3 | 9.5 | 20.2 | 14.7 | 20.3 | 13.6 | 8.3 | 12.16 | 42.2% | 21.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,686 | 21.9 | 13.5 | 29.9 | 17.4 | 13.8 | 2.8 | 0.7 | 7.06 | 17.2% | 3.4% |
| TOTAL_GAMES | 1,120 | 9.9 | 9.0 | 26.2 | 25.2 | 17.1 | 8.0 | 4.5 | 10.68 | 29.6% | 12.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 686 | 28.4 | 30.3 | 26.5 | 0.9 | 11.2 | 2.2 | 0.4 | 4.37 | 13.9% | 2.6% |
| GAME_SPREAD | 398 | 37.7 | 12.1 | 24.1 | 21.1 | 3.0 | 1.5 | 0.5 | 5.03 | 5.0% | 2.0% |
| TOTAL_GAMES | 857 | 3.9 | 4.0 | 34.5 | 39.6 | 12.4 | 1.8 | 4.0 | 10.66 | 18.1% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 686 | 23.0 | 17.4 | 32.9 | 8.9 | 11.1 | 5.5 | 1.2 | 6.02 | 17.8% | 6.7% |
| GAME_SPREAD | 398 | 17.6 | 11.3 | 23.9 | 22.1 | 17.1 | 5.8 | 2.3 | 9.63 | 25.1% | 8.0% |
| TOTAL_GAMES | 859 | 4.7 | 5.4 | 33.2 | 32.5 | 14.7 | 5.5 | 4.2 | 10.9 | 24.3% | 9.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3,631 | 43.4% | 24.3% | 12.62 | 33.2% | 13.8% | 9.98 |
| gen1_elo | 3,631 | 42.2% | 23.6% | 12.1 | 31.8% | 13.7% | 9.56 |
| gen1_sr | 3,631 | 52.0% | 30.8% | 15.68 | 43.6% | 20.3% | 13.03 |
| gen2 | 3,631 | 50.5% | 30.5% | 15.31 | 43.1% | 21.2% | 13.04 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,530 | 17.2 | 12.6 | 23.0 | 15.4 | 19.1 | 9.7 | 3.1 | 9.33 | 31.9% | 12.8% |
| STALE | 2,101 | 10.8 | 7.0 | 16.3 | 14.1 | 19.0 | 18.0 | 14.7 | 15.97 | 51.7% | 32.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,110 | 15.1 | 10.3 | 21.9 | 15.9 | 20.0 | 12.2 | 4.7 | 10.78 | 36.8% | 16.8% |
| STALE | 2,548 | 11.2 | 8.5 | 18.3 | 13.2 | 20.7 | 15.4 | 12.7 | 14.42 | 48.8% | 28.1% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 9,289 | 0 | 4640 | 4649 | 30.6 | 129.5 | 1400.4 |
| ge_15pp | 3,963 | 0 | 1633 | 2330 | 34.5 | 353.6 | 1380.4 |
| ge_25pp | 2,123 | 0 | 719 | 1404 | 44.7 | 574.6 | 1380.4 |
| lt_10pp | 3,962 | 0 | 2277 | 1685 | 27.9 | 53.7 | 1102.2 |

Current slate `SL-20261001T063726Z-932c4fe4`: 493 priced rows, quote age at build {'median': 53.9, 'max': 88.1}, freshness {'STALE': 493}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 151 | 19.2 | 9.9 | 24.5 | 19.9 | 23.8 | 2.6 | 0.0 | 8.28 | 26.5% | 2.6% |
| MARKETS_AGREE | 9 | 55.6 | 44.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.19 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 13 | 0.0 | 0.0 | 15.4 | 46.1 | 38.5 | 0.0 | 0.0 | 13.33 | 38.5% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 3,631 | 174 (4.8%) | 7.5% | 0.0% | {"EXTERNAL_STALE": 151, "AGREES_WITH_KALSHI": 13, "ALL_AGREE": 9, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 1,574 | 45 (2.9%) | 11.1% | 0.0% | {"EXTERNAL_STALE": 40, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 883 | 4 (0.4%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 4} |
| fair_v1_ge_25pp_pregame_clean | 383 | 4 (1.0%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 4} |
| fair_v1_lt_10pp | 1,525 | 93 (6.1%) | 2.1% | 0.0% | {"EXTERNAL_STALE": 81, "ALL_AGREE": 9, "AGREES_WITH_KALSHI": 2, "EXTERNAL_OUTLIER": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 726 | 12.9 | 8.4 | 18.7 | 15.6 | 20.4 | 14.6 | 9.4 | 13.25 | 44.4% | 24.0% |
| 4-10x | 520 | 12.7 | 10.0 | 19.0 | 14.2 | 18.5 | 14.2 | 11.3 | 12.6 | 44.0% | 25.6% |
| <2x | 1,924 | 14.4 | 10.4 | 20.1 | 15.2 | 18.1 | 12.7 | 9.1 | 11.51 | 39.9% | 21.8% |
| >=10x | 461 | 11.3 | 5.9 | 16.1 | 11.3 | 21.5 | 22.1 | 11.9 | 18.17 | 55.5% | 34.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 901 | 13.1 | 10.1 | 22.4 | 15.3 | 17.8 | 11.5 | 9.8 | 11.93 | 39.1% | 21.3% |
| 300-1000 | 906 | 14.7 | 8.9 | 18.2 | 15.7 | 19.3 | 14.3 | 8.8 | 12.62 | 42.5% | 23.2% |
| <300 | 980 | 8.8 | 6.0 | 15.3 | 11.8 | 22.6 | 21.9 | 13.6 | 18.73 | 58.1% | 35.5% |
| >=3000 | 844 | 18.1 | 12.9 | 21.1 | 16.1 | 16.0 | 9.1 | 6.6 | 9.66 | 31.8% | 15.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 136 | 0.5273 | 0.3971 | 0.4412 | +0.086 | -0.044 | 0.0109 ± 0.0127 |
| ratio 4-10x | 103 | 0.5795 | 0.4469 | 0.4951 | +0.084 | -0.048 | 0.0086 ± 0.0142 |
| ratio <2x | 261 | 0.5369 | 0.4159 | 0.4789 | +0.058 | -0.063 | 0.0075 ± 0.0081 |
| ratio >=10x | 96 | 0.5315 | 0.3612 | 0.4479 | +0.084 | -0.087 | 0.0174 ± 0.0195 |
| thinner_sample 1000-3000 | 137 | 0.5559 | 0.4376 | 0.4818 | +0.074 | -0.044 | -0.0005 ± 0.0113 |
| thinner_sample 300-1000 | 170 | 0.5561 | 0.4306 | 0.5118 | +0.044 | -0.081 | -0.0041 ± 0.0107 |
| thinner_sample <300 | 219 | 0.5321 | 0.3709 | 0.4384 | +0.094 | -0.067 | 0.0245 ± 0.0117 |
| thinner_sample >=3000 | 70 | 0.5046 | 0.4124 | 0.4286 | +0.076 | -0.016 | 0.0197 ± 0.0122 |
| data_status ADEQUATE | 139 | 0.5257 | 0.4203 | 0.4604 | +0.065 | -0.040 | 0.0046 ± 0.0098 |
| data_status LIMITED | 135 | 0.5731 | 0.4575 | 0.5185 | +0.055 | -0.061 | -0.0014 ± 0.0118 |
| data_status POOR | 322 | 0.5346 | 0.3822 | 0.4503 | +0.084 | -0.068 | 0.0171 ± 0.0092 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 99 | 0.1894 | 0.191 | -0.0016 ± 0.0016 | 0.5568 | 0.561 | 0.4992 | 0.4842 | 0.5051 | -0.104 ± 0.0477 | -0.01 (3) |
| 3-5 | 65 | 0.1653 | 0.1641 | +0.0011 ± 0.0042 | 0.5062 | 0.5002 | 0.5347 | 0.4938 | 0.4923 | -0.097 ± 0.0538 | 0.02 (1) |
| 5-10 | 122 | 0.2011 | 0.207 | -0.0059 ± 0.0062 | 0.5854 | 0.5959 | 0.5272 | 0.4525 | 0.5328 | -0.047 ± 0.042 | -0.02 (1) |
| 10-15 | 99 | 0.2156 | 0.215 | +0.0007 ± 0.0117 | 0.6162 | 0.6141 | 0.5276 | 0.4026 | 0.4646 | -0.058 ± 0.0469 | -0.0633 (3) |
| 15-25 | 127 | 0.2071 | 0.2049 | +0.0022 ± 0.0155 | 0.5991 | 0.5869 | 0.5519 | 0.3561 | 0.4567 | -0.019 ± 0.0379 | -0.015 (2) |
| 25-40 | 68 | 0.2385 | 0.1851 | +0.0533 ± 0.0328 | 0.6675 | 0.5431 | 0.6053 | 0.2866 | 0.3529 | -0.073 ± 0.05 | -0.01 (1) |
| 40+ | 16 | 0.3076 | 0.132 | +0.1756 ± 0.0837 | 0.7987 | 0.4203 | 0.6612 | 0.2147 | 0.25 | -0.080 ± 0.0809 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 242 | 0.1821 | 0.1828 | -0.0008 ± 0.001 | 0.5385 | 0.5397 | 0.5213 | 0.5064 | 0.5372 | -0.045 ± 0.0287 | -0.0188 (8) |
| 3-5 | 174 | 0.1774 | 0.1765 | +0.0009 ± 0.0026 | 0.5319 | 0.5239 | 0.4918 | 0.4515 | 0.454 | -0.058 ± 0.0331 | 0.02 (1) |
| 5-10 | 351 | 0.1841 | 0.1901 | -0.0059 ± 0.0034 | 0.5449 | 0.5536 | 0.4831 | 0.4095 | 0.49 | +0.008 ± 0.0233 | -0.015 (2) |
| 10-15 | 282 | 0.1833 | 0.1751 | +0.0082 ± 0.0062 | 0.5438 | 0.5127 | 0.4671 | 0.3425 | 0.3723 | -0.038 ± 0.0249 | -0.0633 (3) |
| 15-25 | 413 | 0.1854 | 0.1529 | +0.0324 ± 0.0077 | 0.5556 | 0.4561 | 0.4648 | 0.2673 | 0.2857 | -0.043 ± 0.0188 | -0.02 (3) |
| 25-40 | 410 | 0.2134 | 0.0852 | +0.1282 ± 0.0092 | 0.619 | 0.2853 | 0.4904 | 0.1701 | 0.1317 | -0.084 ± 0.0139 | -0.01 (1) |
| 40+ | 293 | 0.3594 | 0.0335 | +0.3259 ± 0.0112 | 0.9283 | 0.1447 | 0.6067 | 0.0933 | 0.041 | -0.077 ± 0.0098 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 58 | 0.1698 | 0.1716 | -0.0018 ± 0.0018 | 0.5115 | 0.5153 | 0.4904 | 0.4757 | 0.5517 | -0.036 ± 0.0529 | -0.01 (1) |
| 3-5 | 41 | 0.2315 | 0.2299 | +0.0016 ± 0.0061 | 0.6414 | 0.642 | 0.5081 | 0.4689 | 0.4634 | -0.098 ± 0.0806 | 0.02 (1) |
| 5-10 | 113 | 0.1945 | 0.1891 | +0.0054 ± 0.0062 | 0.5754 | 0.5586 | 0.5667 | 0.4909 | 0.4779 | -0.131 ± 0.0417 | -0.01 (3) |
| 10-15 | 111 | 0.208 | 0.2017 | +0.0063 ± 0.0107 | 0.6003 | 0.5851 | 0.5855 | 0.4614 | 0.5045 | -0.066 ± 0.0442 | -0.0667 (3) |
| 15-25 | 147 | 0.2244 | 0.2117 | +0.0127 ± 0.015 | 0.6375 | 0.6008 | 0.5804 | 0.3829 | 0.4558 | -0.058 ± 0.0388 | -0.01 (1) |
| 25-40 | 87 | 0.2679 | 0.1704 | +0.0976 ± 0.0276 | 0.7378 | 0.5081 | 0.6386 | 0.3282 | 0.3218 | -0.168 ± 0.0451 | -0.02 (1) |
| 40+ | 39 | 0.3609 | 0.2109 | +0.1500 ± 0.0742 | 0.9958 | 0.615 | 0.7456 | 0.2533 | 0.359 | +0.001 ± 0.0679 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 190 | 0.1426 | 0.1443 | -0.0017 ± 0.001 | 0.4401 | 0.4445 | 0.5314 | 0.5167 | 0.5632 | -0.012 ± 0.027 | -0.0217 (6) |
| 3-5 | 101 | 0.1787 | 0.1772 | +0.0015 ± 0.0034 | 0.5199 | 0.519 | 0.5493 | 0.5093 | 0.505 | -0.064 ± 0.0431 | 0.02 (1) |
| 5-10 | 320 | 0.1993 | 0.2007 | -0.0014 ± 0.0038 | 0.5852 | 0.5797 | 0.5265 | 0.4513 | 0.4938 | -0.023 ± 0.0253 | -0.01 (4) |
| 10-15 | 330 | 0.1846 | 0.177 | +0.0077 ± 0.0058 | 0.5485 | 0.5196 | 0.5179 | 0.3938 | 0.4333 | -0.024 ± 0.0236 | -0.0575 (4) |
| 15-25 | 402 | 0.1976 | 0.1642 | +0.0333 ± 0.008 | 0.5809 | 0.4854 | 0.5047 | 0.3094 | 0.3308 | -0.052 ± 0.0203 | -0.01 (1) |
| 25-40 | 426 | 0.2277 | 0.1002 | +0.1274 ± 0.0097 | 0.655 | 0.3225 | 0.5245 | 0.2081 | 0.169 | -0.097 ± 0.0156 | -0.02 (1) |
| 40+ | 396 | 0.3976 | 0.0595 | +0.3381 ± 0.0142 | 1.0445 | 0.2148 | 0.6536 | 0.117 | 0.0808 | -0.066 ± 0.0117 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 92 | 0.1687 | 0.1718 | -0.0031 ± 0.0015 | 0.5067 | 0.5142 | 0.526 | 0.5121 | 0.5652 | -0.046 ± 0.043 | 0.0 (3) |
| 3-5 | 62 | 0.1663 | 0.1643 | +0.0020 ± 0.0042 | 0.504 | 0.4987 | 0.53 | 0.4907 | 0.4839 | -0.134 ± 0.0566 | -- (0) |
| 5-10 | 118 | 0.203 | 0.2047 | -0.0017 ± 0.0061 | 0.5938 | 0.5923 | 0.524 | 0.4535 | 0.5085 | -0.049 ± 0.0418 | -0.01 (2) |
| 10-15 | 112 | 0.2235 | 0.2256 | -0.0021 ± 0.0112 | 0.6391 | 0.6377 | 0.551 | 0.4263 | 0.5089 | -0.051 ± 0.0449 | -0.05 (4) |
| 15-25 | 125 | 0.2035 | 0.207 | -0.0035 ± 0.0154 | 0.5966 | 0.5931 | 0.5746 | 0.3813 | 0.488 | -0.022 ± 0.0384 | -0.03 (1) |
| 25-40 | 74 | 0.2405 | 0.1815 | +0.0590 ± 0.0315 | 0.6765 | 0.5349 | 0.5948 | 0.2775 | 0.3378 | -0.076 ± 0.0478 | 0.0 (1) |
| 40+ | 13 | 0.3177 | 0.1578 | +0.1599 ± 0.1041 | 0.8214 | 0.4818 | 0.6902 | 0.2304 | 0.3077 | -0.055 ± 0.0988 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 225 | 0.1661 | 0.1671 | -0.0010 ± 0.001 | 0.5019 | 0.5037 | 0.5347 | 0.5202 | 0.5378 | -0.053 ± 0.0276 | -0.015 (8) |
| 3-5 | 156 | 0.1921 | 0.1906 | +0.0015 ± 0.0028 | 0.5618 | 0.5581 | 0.5118 | 0.4724 | 0.4744 | -0.077 ± 0.0361 | -- (0) |
| 5-10 | 357 | 0.1813 | 0.1784 | +0.0029 ± 0.0033 | 0.5422 | 0.5224 | 0.4778 | 0.4055 | 0.4286 | -0.034 ± 0.0225 | -0.01 (2) |
| 10-15 | 302 | 0.1959 | 0.1845 | +0.0114 ± 0.0062 | 0.5758 | 0.5362 | 0.4872 | 0.3631 | 0.3841 | -0.053 ± 0.0247 | -0.042 (5) |
| 15-25 | 448 | 0.1747 | 0.1457 | +0.0290 ± 0.0071 | 0.5338 | 0.44 | 0.4719 | 0.2744 | 0.3013 | -0.035 ± 0.0175 | -0.03 (2) |
| 25-40 | 407 | 0.2166 | 0.0925 | +0.1240 ± 0.0096 | 0.6272 | 0.3016 | 0.4929 | 0.1712 | 0.14 | -0.078 ± 0.0146 | 0.0 (1) |
| 40+ | 270 | 0.3751 | 0.0338 | +0.3413 ± 0.0124 | 0.9768 | 0.1458 | 0.6109 | 0.0916 | 0.0333 | -0.084 ± 0.0101 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 370 | 0.2067 | 0.2066 | +0.0001 ± 0.0008 | 0.5956 | 0.5956 | 0.5076 | 0.4929 | 0.4865 | -0.051 ± 0.0237 | -0.0226 (46) |
| 3-5 | 273 | 0.1934 | 0.1938 | -0.0004 ± 0.0021 | 0.5676 | 0.5652 | 0.4657 | 0.4258 | 0.4542 | -0.024 ± 0.0265 | -0.0059 (32) |
| 5-10 | 581 | 0.1876 | 0.1829 | +0.0047 ± 0.0027 | 0.5584 | 0.5453 | 0.4649 | 0.3917 | 0.3976 | -0.041 ± 0.0178 | -0.0049 (70) |
| 10-15 | 381 | 0.2019 | 0.1885 | +0.0134 ± 0.0056 | 0.5919 | 0.5551 | 0.4519 | 0.3284 | 0.336 | -0.045 ± 0.0221 | 0.002 (61) |
| 15-25 | 513 | 0.234 | 0.2097 | +0.0243 ± 0.0079 | 0.6609 | 0.6055 | 0.5311 | 0.3378 | 0.3723 | -0.031 ± 0.0202 | -0.0216 (58) |
| 25-40 | 251 | 0.2624 | 0.1673 | +0.0951 ± 0.0162 | 0.7248 | 0.5043 | 0.5678 | 0.2561 | 0.259 | -0.061 ± 0.0256 | -0.0216 (25) |
| 40+ | 90 | 0.4349 | 0.1592 | +0.2757 ± 0.0452 | 1.223 | 0.4921 | 0.7344 | 0.2252 | 0.2333 | -0.065 ± 0.044 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 672 | 0.1982 | 0.1976 | +0.0005 ± 0.0006 | 0.5761 | 0.5744 | 0.501 | 0.4862 | 0.4673 | -0.062 ± 0.0171 | -0.0155 (82) |
| 3-5 | 496 | 0.1992 | 0.1986 | +0.0006 ± 0.0016 | 0.5786 | 0.5743 | 0.4729 | 0.4329 | 0.4456 | -0.034 ± 0.02 | -0.018 (54) |
| 5-10 | 1042 | 0.1857 | 0.1794 | +0.0062 ± 0.002 | 0.5544 | 0.5352 | 0.4497 | 0.3759 | 0.3752 | -0.043 ± 0.0133 | -0.0089 (119) |
| 10-15 | 759 | 0.1963 | 0.1815 | +0.0149 ± 0.0039 | 0.5774 | 0.5366 | 0.4445 | 0.3208 | 0.3228 | -0.044 ± 0.0153 | -0.0051 (95) |
| 15-25 | 1054 | 0.2221 | 0.1881 | +0.0340 ± 0.0053 | 0.6399 | 0.5513 | 0.5054 | 0.3097 | 0.3207 | -0.042 ± 0.0134 | -0.0255 (106) |
| 25-40 | 735 | 0.2451 | 0.1284 | +0.1167 ± 0.0084 | 0.6911 | 0.4016 | 0.5274 | 0.2117 | 0.1864 | -0.071 ± 0.0131 | -0.0206 (47) |
| 40+ | 445 | 0.3949 | 0.0831 | +0.3118 ± 0.0148 | 1.079 | 0.2777 | 0.6567 | 0.1404 | 0.1079 | -0.077 ± 0.014 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 596 | 1.198 ± 0.125 | 1.254 | 0.1642 | 0.1821 | 0.2061 | 0.196 |
| gen2 | 596 | 0.933 ± 0.106 | 1.158 | 0.1828 | 0.1808 | 0.2261 | 0.1968 |
| gen1_elo | 596 | 1.157 ± 0.121 | 1.237 | 0.1715 | 0.1822 | 0.205 | 0.1959 |
| gen1_sr | 596 | 1.135 ± 0.137 | 1.223 | 0.1403 | 0.183 | 0.223 | 0.1961 |
| gen1_ledger | 2459 | 0.901 ± 0.055 | 1.075 | 0.161 | 0.1995 | 0.2197 | 0.1917 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 3,963)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 1,158 | 29.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,141 | 28.8% |
| POOR_DATA | data | 358 | 9.0% |
| BOOK_QUALITY | execution | 284 | 7.2% |
| LIMITED_DATA | data | 273 | 6.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 255 | 6.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 206 | 5.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 202 | 5.1% |
| IDENTITY_AMBIGUOUS | mapping | 83 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: market_freshness 29.2%, coverage 28.8%, data 15.9%, market_freshness/coverage 11.6%, execution 7.2%, model_calibration_or_unknown 5.1%, mapping 2.1%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.7%, LOW_DATA_QUALITY 66.5%, STALE_KALSHI_QUOTE 58.8%, STALE_PLAYER_DATA 58.5%, THIN_PLAYER_HISTORY 53.7%, MODEL_INTERNAL_DISAGREEMENT 32.5%, ASYMMETRIC_SAMPLE_SIZE 29.8%, WIDE_SPREAD 15.8%, PLAYER_IDENTITY_RISK 12.2%, MODEL_HIGH_UNCERTAINTY 10.3%, LEVEL_TRANSFER_RISK 9.5%, EVENT_MAPPING_RISK 7.6%, LOW_DISPLAYED_LIQUIDITY 4.1%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.9%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 31.7%, POST_SETTLEMENT_OBSERVATION 28.8%, POSSIBLE_IN_PLAY_QUOTE 7.3%, CONFIRMED_IN_PLAY_QUOTE 2.8%

### >= ge_25 pp (N = 2,123)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 895 | 42.2% |
| STALE_QUOTE | market_freshness | 516 | 24.3% |
| POOR_DATA | data | 155 | 7.3% |
| BOOK_QUALITY | execution | 134 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 126 | 5.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 120 | 5.7% |
| LIMITED_DATA | data | 77 | 3.6% |
| IDENTITY_AMBIGUOUS | mapping | 58 | 2.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 42 | 2.0% |

Cause class: coverage 42.2%, market_freshness 24.3%, market_freshness/coverage 11.6%, data 10.9%, execution 6.3%, mapping 2.7%, model_calibration_or_unknown 2.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.2%, LOW_DATA_QUALITY 71.4%, STALE_KALSHI_QUOTE 66.1%, THIN_PLAYER_HISTORY 57.0%, STALE_PLAYER_DATA 56.9%, MODEL_INTERNAL_DISAGREEMENT 33.2%, ASYMMETRIC_SAMPLE_SIZE 32.5%, PLAYER_IDENTITY_RISK 15.4%, WIDE_SPREAD 14.5%, MODEL_HIGH_UNCERTAINTY 11.1%, EVENT_MAPPING_RISK 9.5%, LEVEL_TRANSFER_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 4.2%, MODEL_CALIBRATION_OUTLIER 3.1%, UNKNOWN 0.3%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 45.4%, POST_SETTLEMENT_OBSERVATION 42.2%, POSSIBLE_IN_PLAY_QUOTE 6.9%, CONFIRMED_IN_PLAY_QUOTE 3.2%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 1768, "IDENTITY_AMBIGUOUS": 355}; ticker orientation: {"VERIFIED": 2123}.

Checks: discipline:AMBIGUOUS 175, discipline:PASS 1948, identity_confidence:AMBIGUOUS 328, identity_confidence:PASS 1795, level_mapping:NA 187, level_mapping:PASS 1936, market_pair:AMBIGUOUS 57, market_pair:NA 54, market_pair:PASS 2012, model_complement:NA 30, model_complement:PASS 2093, namesake:PASS 2123, physical_match_id:NA 1240, physical_match_id:PASS 883, player_ids:PASS 2123, same_pair_other_event:PASS 2123, ticker_orientation:PASS 2123

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 253 | 3.2% | 3.3% | 0.4% | {"market_freshness": 8} | 5.89 | 0.1838 / 0.1834 (45) | 35.2% | 0.0% | 0.8% | 5.1% |
| CHALLENGER | 1,448 | 16.9% | 7.5% | 11.5% | {"coverage": 127, "market_freshness": 55, "market_freshness/coverage": 32, "data": 15, "model_calibration_or_unknown": 13, "execution": 3} | 7.53 | 0.2197 / 0.1998 (482) | 50.4% | 4.3% | 0.8% | 21.1% |
| DOUBLES | 358 | 48.9% | 48.4% | 8.2% | {"market_freshness": 86, "market_freshness/coverage": 36, "execution": 28, "mapping": 20, "coverage": 5} | 24.11 | 0.3236 / 0.2197 (143) | 60.1% | 0.0% | 100.0% | 22.6% |
| ITF_MEN | 3,032 | 24.1% | 14.2% | 34.5% | {"coverage": 356, "market_freshness": 154, "data": 83, "market_freshness/coverage": 66, "execution": 62, "mapping": 10, "model_calibration_or_unknown": 1} | 9.68 | 0.2126 / 0.1851 (1068) | 52.0% | 52.3% | 5.7% | 27.8% |
| ITF_WOMEN | 3,000 | 27.9% | 17.6% | 39.5% | {"coverage": 395, "market_freshness": 187, "data": 117, "market_freshness/coverage": 70, "execution": 32, "mapping": 26, "model_calibration_or_unknown": 11} | 12.28 | 0.2086 / 0.1921 (959) | 54.6% | 55.5% | 7.0% | 29.4% |
| OTHER | 149 | 8.1% | 7.3% | 0.6% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 646 | 7.9% | 6.2% | 2.4% | {"market_freshness/coverage": 14, "market_freshness": 13, "data": 9, "model_calibration_or_unknown": 6, "execution": 4, "coverage": 4, "mapping": 1} | 8.47 | 0.1995 / 0.1973 (113) | 33.9% | 3.2% | 1.9% | 16.9% |
| WTA125 | 403 | 15.4% | 8.7% | 2.9% | {"market_freshness/coverage": 27, "market_freshness": 11, "model_calibration_or_unknown": 9, "data": 8, "coverage": 7} | 10.53 | 0.2317 / 0.2049 (203) | 34.5% | 9.4% | 0.5% | 19.9% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 2 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 3 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 4 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 5 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 6 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 8 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 9 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 11 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 12 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 13 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 14 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 15 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 17 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 18 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 19 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 20 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 21 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 22 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 23 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 24 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 25 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 26 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 27 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 29 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 30 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 31 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 33 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 86 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 34 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 35 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 36 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 37 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 38 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 819 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 39 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26SEP24BOUKUR-BOU` | ITF_WOMEN | gen1_ledger | 76% / 8% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 1497.0, ratio 2.48); no external reference |
| 42 | `KXATPCHALLENGERMATCH-26SEP28TABSAN-SAN` | CHALLENGER | gen1_ledger | 70% / 4% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 48 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26SEP22SHCPAS-PAS` | ITF_WOMEN | gen1_ledger | 69% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 199 min (STALE); data POOR (grade F, thinner serve sample 239.0, ratio 5.93); no external reference |
| 44 | `KXWTADOUBLES-26SEP20DETKHRPRETAR-PRETAR` | DOUBLES | gen1_ledger | 84% / 18% | +66 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFWMATCH-26SEP29KRURAY-KRU` | ITF_WOMEN | fair_v1 | 78% / 12% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 126 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 223.0); no external reference |
| 46 | `KXITFWMATCH-26SEP30BIOKRO-KRO` | ITF_WOMEN | fair_v1 | 68% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 170 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 3.24); no external reference |
| 47 | `KXITFMATCH-26SEP12EFSMOR-MOR` | ITF_MEN | gen1_ledger | 67% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 36 min (STALE); data LIMITED (grade B, thinner serve sample 3783.0, ratio 1.33); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26SEP17TROUCHBAYKAD-TROUCH` | DOUBLES | gen1_ledger | 87% / 21% | +66 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 21 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26SEP30BRAKUH-BRA` | ITF_WOMEN | fair_v1 | 82% / 16% | +65 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 50 | `KXITFMATCH-26SEP23BAKBAL-BAK` | ITF_MEN | gen1_ledger | 69% / 4% | +65 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 89.0, ratio 20.62); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9722, "by_level_share_of_ge_25pp": {"ATP": 0.0038, "CHALLENGER": 0.1154, "DOUBLES": 0.0824, "ITF_MEN": 0.3448, "ITF_WOMEN": 0.3947, "OTHER": 0.0057, "WTA": 0.024, "WTA125": 0.0292}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6613, "share_primary_cause_market_settled_or_in_play": 0.5374, "share_primary_cause_stale_quote_only": 0.2431}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2123, "identity_ambiguous_share": 0.1672, "ticker_orientation": {"VERIFIED": 2123}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 883, "with_external": 4, "coverage": 0.0045, "external_status": {"EXTERNAL_STALE": 4}, "triangulation": {"INSUFFICIENT_INPUTS": 4}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 383, "with_external": 4, "coverage": 0.0104, "external_status": {"EXTERNAL_STALE": 4}, "triangulation": {"INSUFFICIENT_INPUTS": 4}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 668.0, "median_sample_ratio": 2.5, "median_min_matches": 23.0, "median_max_days_since_last": 177.0, "share_severe_asymmetry": 0.1809, "data_status": {"POOR": 1047, "LIMITED": 741, "ADEQUATE": 335}, "comparison_lt_10pp": {"median_thinner_serve_points": 1937.0, "median_sample_ratio": 1.73, "median_min_matches": 78.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 136, "model_minus_observed": 0.0862, "kalshi_minus_observed": -0.0441, "brier_diff_model_minus_kalshi": 0.0109}, "4-10x": {"n": 103, "model_minus_observed": 0.0844, "kalshi_minus_observed": -0.0483, "brier_diff_model_minus_kalshi": 0.0086}, "<2x": {"n": 261, "model_minus_observed": 0.058, "kalshi_minus_observed": -0.0631, "brier_diff_model_minus_kalshi": 0.0075}, ">=10x": {"n": 96, "model_minus_observed": 0.0836, "kalshi_minus_observed": -0.0867, "brier_diff_model_minus_kalshi": 0.0174}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 596, "model": {"intercept": -0.61, "slope": 0.933, "slope_se": 0.106}, "kalshi_mid_same_rows": {"intercept": 0.232, "slope": 1.158, "slope_se": 0.115}, "mean_extremity_model": 0.1828, "mean_extremity_kalshi": 0.1808, "model_brier": 0.2261, "kalshi_brier": 0.1968, "brier_diff_model_minus_kalshi": 0.0293, "brier_diff_se": 0.0078, "model_logloss": 0.6449, "kalshi_logloss": 0.5718}, "fair_v1": {"n": 596, "model": {"intercept": -0.381, "slope": 1.198, "slope_se": 0.125}, "kalshi_mid_same_rows": {"intercept": 0.403, "slope": 1.254, "slope_se": 0.12}, "mean_extremity_model": 0.1642, "mean_extremity_kalshi": 0.1821, "model_brier": 0.2061, "kalshi_brier": 0.196, "brier_diff_model_minus_kalshi": 0.01, "brier_diff_se": 0.0061, "model_logloss": 0.5951, "kalshi_logloss": 0.57}, "gen1_elo": {"n": 596, "model": {"intercept": -0.363, "slope": 1.157, "slope_se": 0.121}, "kalshi_mid_same_rows": {"intercept": 0.412, "slope": 1.237, "slope_se": 0.117}, "mean_extremity_model": 0.1715, "mean_extremity_kalshi": 0.1822, "model_brier": 0.205, "kalshi_brier": 0.1959, "brier_diff_model_minus_kalshi": 0.0091, "brier_diff_se": 0.0062, "model_logloss": 0.5954, "kalshi_logloss": 0.5697}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2432, "share_ge_15": 0.4335, "median_abs_gap": 12.62, "n": 3631}, "gen1_elo": {"share_ge_25": 0.2357, "share_ge_15": 0.4222, "median_abs_gap": 12.1, "n": 3631}, "gen1_sr": {"share_ge_25": 0.3076, "share_ge_15": 0.5202, "median_abs_gap": 15.68, "n": 3631}, "gen2": {"share_ge_25": 0.3054, "share_ge_15": 0.5051, "median_abs_gap": 15.31, "n": 3631}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1377, "share_ge_15": 0.3323, "median_abs_gap": 9.98, "n": 2781}, "gen1_elo": {"share_ge_25": 0.1374, "share_ge_15": 0.3175, "median_abs_gap": 9.56, "n": 2781}, "gen1_sr": {"share_ge_25": 0.2032, "share_ge_15": 0.4365, "median_abs_gap": 13.03, "n": 2781}, "gen2": {"share_ge_25": 0.2118, "share_ge_15": 0.4308, "median_abs_gap": 13.04, "n": 2781}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.89, "share_ge_25_all": 0.0316, "share_ge_25_pregame_clean": 0.0333}, "WTA": {"median_abs_gap_pregame_clean": 8.47, "share_ge_25_all": 0.0789, "share_ge_25_pregame_clean": 0.0615}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2283, "share_within_10pp_all": 0.4265, "share_within_10pp_pregame_clean": 0.5005, "corr_model_vs_mid_pregame_clean": 0.8349}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 99, "model_brier": 0.1894, "kalshi_brier": 0.191, "brier_diff_model_minus_kalshi": -0.0016}, "10-15": {"n_settled": 99, "model_brier": 0.2156, "kalshi_brier": 0.215, "brier_diff_model_minus_kalshi": 0.0007}, "15-25": {"n_settled": 127, "model_brier": 0.2071, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0022}, "25-40": {"n_settled": 68, "model_brier": 0.2385, "kalshi_brier": 0.1851, "brier_diff_model_minus_kalshi": 0.0533}, "3-5": {"n_settled": 65, "model_brier": 0.1653, "kalshi_brier": 0.1641, "brier_diff_model_minus_kalshi": 0.0011}, "40+": {"n_settled": 16, "model_brier": 0.3076, "kalshi_brier": 0.132, "brier_diff_model_minus_kalshi": 0.1756}, "5-10": {"n_settled": 122, "model_brier": 0.2011, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": -0.0059}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 143, "model_brier": 0.3236, "kalshi_brier": 0.2197, "brier_diff_model_minus_kalshi": 0.1038, "brier_diff_se": 0.0277, "corr_model_outcome": -0.059, "corr_kalshi_outcome": 0.3814}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
