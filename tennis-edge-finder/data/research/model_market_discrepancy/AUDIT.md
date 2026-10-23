# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-23T12:33Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 50,495): 0-3 13.9%, 3-5 9.4%, 5-10 19.7%, 10-15 15.3%, 15-25 19.3%, 25-40 14.1%, 40+ 8.2%; median gap 12.14 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.9%, Challenger 11.9%, doubles 6.7%). Main tour: ATP 4.8% and WTA 5.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,251): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.4%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.1%, POOR_DATA 8.8%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.6%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.4%, market_freshness 18.8%, execution 18.1%, data 12.4%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,251 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.8% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 484.0 points vs 1667.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.047, Gen-2 0.848, Gen-1 ledger 0.869 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 551 model 0.2232 vs Kalshi 0.2089; n 112 model 0.2783 vs Kalshi 0.1982.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 218,046 model-market comparisons (355,039 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 72,301 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-23T12:20:19.240840+00:00'], shadow board 58,298 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-23T12:20:22.786992+00:00'], Model 4 27,309 rows, 19,338 settled tickers, 6,832 tickers with an external scan.
* By model: {"gen1_ledger": 49091, "gen1_elo": 29315, "fair_v1": 29315, "gen2": 29315, "gen1_sr": 29315, "model4_fundamental": 25861, "model4_conditioned": 25834}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 50,495 | 13.9 | 9.4 | 19.7 | 15.3 | 19.3 | 14.1 | 8.2 | 12.14 | 41.6% | 22.3% |
| MW fair_v1 | 29,315 | 12.8 | 8.5 | 18.4 | 15.6 | 19.8 | 15.0 | 9.9 | 13.19 | 44.7% | 24.9% |
| MW gen1_elo | 29,315 | 12.7 | 8.5 | 18.9 | 15.3 | 20.0 | 15.0 | 9.6 | 13.02 | 44.6% | 24.6% |
| MW gen1_ledger | 21,180 | 15.4 | 10.8 | 21.4 | 14.9 | 18.7 | 12.8 | 5.9 | 10.59 | 37.4% | 18.7% |
| MW gen1_sr | 29,315 | 10.1 | 7.0 | 16.5 | 13.6 | 21.0 | 18.9 | 12.9 | 16.08 | 52.7% | 31.7% |
| MW gen2 | 29,315 | 11.0 | 7.2 | 16.2 | 14.1 | 19.5 | 18.0 | 14.0 | 15.65 | 51.5% | 32.0% |
| all families model4_conditioned | 25,834 | 21.9 | 18.9 | 34.8 | 17.6 | 4.3 | 1.4 | 1.0 | 5.95 | 6.7% | 2.5% |
| all families model4_fundamental | 25,861 | 16.6 | 13.3 | 34.1 | 20.6 | 10.6 | 3.4 | 1.3 | 7.79 | 15.3% | 4.7% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.9%, >=15pp 41.6%, >=20pp 30.9%, >=25pp 22.3%, >=30pp 16.1%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.6%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,503 | 28.5 | 14.2 | 24.9 | 14.9 | 11.8 | 4.9 | 0.7 | 6.14 | 17.4% | 5.6% |
| CHALLENGER | 4,578 | 15.8 | 10.0 | 20.5 | 15.6 | 14.7 | 12.3 | 11.0 | 11.02 | 38.1% | 23.3% |
| ITF_MEN | 8,129 | 10.2 | 7.3 | 16.9 | 14.8 | 21.5 | 17.3 | 12.0 | 15.22 | 50.8% | 29.2% |
| ITF_WOMEN | 11,715 | 9.4 | 6.8 | 16.0 | 15.4 | 22.5 | 18.2 | 11.7 | 15.76 | 52.3% | 29.9% |
| WTA | 1,730 | 17.2 | 13.1 | 25.6 | 19.8 | 18.7 | 4.9 | 0.8 | 8.36 | 24.3% | 5.7% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,503 | 24.1 | 15.1 | 24.9 | 17.1 | 13.0 | 4.8 | 1.0 | 6.51 | 18.8% | 5.8% |
| CHALLENGER | 4,578 | 15.1 | 8.7 | 18.6 | 14.6 | 17.3 | 13.8 | 11.9 | 12.47 | 43.0% | 25.7% |
| ITF_MEN | 8,129 | 8.3 | 5.9 | 14.5 | 13.1 | 19.8 | 20.9 | 17.6 | 18.5 | 58.3% | 38.5% |
| ITF_WOMEN | 11,715 | 8.1 | 5.6 | 13.8 | 13.4 | 20.6 | 21.0 | 17.4 | 18.96 | 59.1% | 38.4% |
| WTA | 1,730 | 14.3 | 10.1 | 21.8 | 16.1 | 23.3 | 13.6 | 0.9 | 10.97 | 37.8% | 14.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,503 | 24.4 | 12.9 | 23.6 | 16.1 | 14.9 | 7.0 | 1.2 | 7.3 | 23.0% | 8.1% |
| CHALLENGER | 4,578 | 14.3 | 9.2 | 20.6 | 15.7 | 16.3 | 12.8 | 11.2 | 11.47 | 40.3% | 24.0% |
| ITF_MEN | 8,129 | 9.8 | 7.4 | 16.9 | 14.1 | 22.1 | 17.6 | 12.1 | 15.61 | 51.8% | 29.8% |
| ITF_WOMEN | 11,715 | 9.4 | 6.6 | 16.2 | 15.8 | 22.9 | 18.1 | 10.9 | 15.59 | 51.9% | 29.0% |
| WTA | 1,730 | 24.2 | 16.5 | 30.5 | 15.8 | 10.0 | 2.5 | 0.5 | 6.04 | 13.1% | 3.1% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,439 | 25.4 | 19.5 | 31.0 | 11.9 | 8.9 | 3.0 | 0.3 | 5.54 | 12.2% | 3.3% |
| CHALLENGER | 3,143 | 21.3 | 14.7 | 26.5 | 14.4 | 14.6 | 6.7 | 1.9 | 7.3 | 23.1% | 8.5% |
| DOUBLES | 1,580 | 5.4 | 4.3 | 11.5 | 10.3 | 21.1 | 26.1 | 21.2 | 23.86 | 68.4% | 47.3% |
| ITF_MEN | 6,037 | 13.8 | 9.0 | 19.9 | 16.1 | 21.3 | 13.3 | 6.6 | 12.21 | 41.2% | 19.9% |
| ITF_WOMEN | 7,045 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.2 | 6.1 | 12.83 | 43.9% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,055 | 22.3 | 16.0 | 29.6 | 18.1 | 10.1 | 3.6 | 0.4 | 6.86 | 14.0% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,435 | 28.8 | 14.5 | 25.4 | 14.9 | 11.6 | 4.5 | 0.5 | 5.96 | 16.6% | 5.0% |
| CHALLENGER | 3,232 | 20.7 | 12.5 | 25.1 | 17.9 | 15.1 | 6.6 | 2.0 | 8.32 | 23.7% | 8.6% |
| ITF_MEN | 5,994 | 12.3 | 8.8 | 20.2 | 16.6 | 22.5 | 14.3 | 5.2 | 12.52 | 42.0% | 19.5% |
| ITF_WOMEN | 8,778 | 11.2 | 8.2 | 18.2 | 17.4 | 24.4 | 15.3 | 5.4 | 13.52 | 45.1% | 20.7% |
| WTA | 1,681 | 17.4 | 13.0 | 25.6 | 20.0 | 18.6 | 4.6 | 0.8 | 8.25 | 24.0% | 5.4% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,435 | 24.4 | 15.4 | 25.1 | 17.0 | 13.0 | 4.5 | 0.6 | 6.45 | 18.1% | 5.1% |
| CHALLENGER | 3,232 | 19.2 | 11.2 | 23.0 | 17.4 | 17.5 | 9.4 | 2.2 | 9.08 | 29.1% | 11.6% |
| ITF_MEN | 5,995 | 9.9 | 7.1 | 16.7 | 14.9 | 21.6 | 19.3 | 10.5 | 15.49 | 51.4% | 29.8% |
| ITF_WOMEN | 8,779 | 9.2 | 6.5 | 15.3 | 15.0 | 22.6 | 20.4 | 11.1 | 16.57 | 54.1% | 31.5% |
| WTA | 1,681 | 14.4 | 10.1 | 21.8 | 16.0 | 23.3 | 13.5 | 0.9 | 10.97 | 37.7% | 14.4% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,394 | 25.6 | 19.7 | 31.1 | 12.1 | 8.4 | 2.9 | 0.2 | 5.49 | 11.5% | 3.1% |
| CHALLENGER | 2,739 | 22.8 | 15.8 | 28.0 | 14.3 | 14.0 | 4.6 | 0.6 | 6.72 | 19.1% | 5.1% |
| DOUBLES | 1,467 | 5.5 | 4.5 | 11.8 | 10.5 | 20.9 | 26.0 | 20.8 | 23.62 | 67.8% | 46.8% |
| ITF_MEN | 5,056 | 14.9 | 9.7 | 21.5 | 16.9 | 21.2 | 11.6 | 4.0 | 11.21 | 36.9% | 15.7% |
| ITF_WOMEN | 5,840 | 13.7 | 9.6 | 20.7 | 16.0 | 21.8 | 15.0 | 3.4 | 11.67 | 40.1% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,005 | 22.8 | 16.5 | 29.6 | 18.1 | 10.1 | 2.9 | 0.1 | 6.79 | 13.0% | 3.0% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,580 | 5.4 | 4.3 | 11.5 | 10.3 | 21.1 | 26.1 | 21.2 | 23.86 | 68.4% | 47.3% |
| singles | 19,600 | 16.2 | 11.3 | 22.3 | 15.3 | 18.5 | 11.7 | 4.7 | 10.04 | 34.9% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,525 | 13.0 | 8.9 | 19.2 | 15.7 | 18.7 | 14.6 | 9.8 | 12.8 | 43.2% | 24.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 18,118 | 13.2 | 8.5 | 18.5 | 15.2 | 19.9 | 14.8 | 9.8 | 13.15 | 44.5% | 24.6% |
| UNKNOWN | 4,435 | 10.8 | 7.7 | 17.2 | 17.0 | 20.7 | 16.2 | 10.5 | 14.01 | 47.4% | 26.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,159 | 19.6 | 11.8 | 21.4 | 16.5 | 15.4 | 9.0 | 6.3 | 9.16 | 30.7% | 15.3% |
| B | 3,647 | 12.4 | 8.8 | 20.1 | 16.3 | 19.2 | 12.5 | 10.7 | 12.5 | 42.4% | 23.2% |
| C | 4,140 | 11.5 | 8.7 | 19.8 | 15.1 | 19.5 | 14.8 | 10.6 | 13.18 | 44.9% | 25.4% |
| D | 4,623 | 12.2 | 7.7 | 17.2 | 15.5 | 21.5 | 15.7 | 10.2 | 14.0 | 47.4% | 25.9% |
| F | 8,746 | 7.7 | 5.5 | 15.0 | 14.7 | 23.4 | 21.3 | 12.4 | 17.71 | 57.1% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,942 | 22.9 | 15.9 | 28.9 | 15.1 | 11.6 | 4.1 | 1.5 | 6.68 | 17.2% | 5.6% |
| B | 2,903 | 16.2 | 10.4 | 23.3 | 16.3 | 19.3 | 10.6 | 3.9 | 10.03 | 33.9% | 14.5% |
| C | 4,178 | 11.4 | 7.4 | 18.2 | 14.2 | 21.6 | 16.7 | 10.6 | 14.36 | 48.8% | 27.3% |
| D | 2,975 | 14.4 | 9.8 | 19.8 | 14.5 | 21.0 | 14.3 | 6.1 | 12.04 | 41.4% | 20.4% |
| F | 5,182 | 10.2 | 8.4 | 15.4 | 14.9 | 22.8 | 20.1 | 8.2 | 15.52 | 51.0% | 28.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,375 | 17.7 | 10.6 | 20.8 | 16.3 | 15.9 | 9.9 | 8.8 | 10.23 | 34.6% | 18.6% |
| LIMITED | 6,254 | 13.3 | 10.0 | 20.5 | 15.7 | 19.3 | 13.5 | 7.8 | 11.95 | 40.6% | 21.3% |
| POOR | 13,686 | 9.2 | 6.4 | 15.9 | 15.1 | 22.7 | 19.2 | 11.6 | 16.17 | 53.4% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,657 | 26.5 | 20.2 | 34.5 | 12.6 | 4.7 | 1.4 | 0.2 | 5.35 | 6.3% | 1.6% |
| GAME_SPREAD | 4,724 | 22.2 | 15.2 | 33.5 | 17.4 | 9.0 | 2.3 | 0.3 | 6.72 | 11.7% | 2.6% |
| MATCH_WINNER | 21,180 | 15.4 | 10.8 | 21.4 | 14.9 | 18.7 | 12.8 | 5.9 | 10.59 | 37.4% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,997 | 29.3 | 17.1 | 31.0 | 12.5 | 8.0 | 1.8 | 0.4 | 5.46 | 10.2% | 2.2% |
| TOTAL_GAMES | 7,509 | 8.6 | 9.7 | 36.6 | 28.9 | 10.5 | 3.2 | 2.6 | 9.44 | 16.3% | 5.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,033 | 25.6 | 33.6 | 32.7 | 4.5 | 2.9 | 0.5 | 0.2 | 4.48 | 3.6% | 0.8% |
| GAME_SPREAD | 6,210 | 45.5 | 16.7 | 27.0 | 7.9 | 1.7 | 0.9 | 0.3 | 3.49 | 2.9% | 1.2% |
| TOTAL_GAMES | 10,591 | 5.0 | 7.8 | 41.0 | 34.6 | 7.0 | 2.5 | 2.1 | 9.59 | 11.6% | 4.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,036 | 24.2 | 17.8 | 35.7 | 12.6 | 6.9 | 2.4 | 0.3 | 5.81 | 9.7% | 2.8% |
| GAME_SPREAD | 6,213 | 19.3 | 13.3 | 27.9 | 20.8 | 13.3 | 4.4 | 0.9 | 7.97 | 18.6% | 5.3% |
| TOTAL_GAMES | 10,612 | 8.5 | 9.6 | 36.5 | 27.3 | 12.1 | 3.7 | 2.3 | 9.47 | 18.1% | 6.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 29,315 | 44.7% | 24.9% | 13.19 | 36.3% | 15.7% | 10.98 |
| gen1_elo | 29,315 | 44.6% | 24.6% | 13.02 | 36.1% | 15.8% | 10.82 |
| gen1_sr | 29,315 | 52.7% | 31.7% | 16.08 | 45.0% | 22.5% | 13.26 |
| gen2 | 29,315 | 51.5% | 32.0% | 15.65 | 44.8% | 24.0% | 13.14 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 14,862 | 15.7 | 10.3 | 21.2 | 17.2 | 20.2 | 12.0 | 3.4 | 10.79 | 35.6% | 15.3% |
| STALE | 14,453 | 9.9 | 6.6 | 15.6 | 13.9 | 19.4 | 18.1 | 16.6 | 16.91 | 54.0% | 34.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,648 | 16.4 | 11.3 | 22.2 | 15.0 | 17.9 | 12.2 | 4.8 | 10.0 | 35.0% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 50,495 | 14648 | 18334 | 17513 | 24.1 | 142.9 | 1400.4 |
| ge_15pp | 21,013 | 5123 | 6576 | 9314 | 26.0 | 437.7 | 1380.4 |
| ge_25pp | 11,251 | 2503 | 2871 | 5877 | 32.2 | 576.8 | 1380.4 |
| lt_10pp | 21,745 | 7322 | 8646 | 5777 | 22.4 | 48.3 | 1341.5 |

Current slate `SL-20261023T123316Z-a45d4c06`: 471 priced rows, quote age at build {'median': 13.3, 'max': 13.4}, freshness {'AGING': 471}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 23 | 0.0 | 0.0 | 21.7 | 4.3 | 39.1 | 34.8 | 0.0 | 20.49 | 73.9% | 34.8% |
| EXTERNAL_LONE_OUTLIER | 13 | 69.2 | 30.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,743 | 19.2 | 11.2 | 24.3 | 18.8 | 18.4 | 7.4 | 0.7 | 8.97 | 26.5% | 8.1% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 541 | 65.2 | 34.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.26 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,157 | 0.0 | 2.2 | 35.4 | 26.2 | 24.7 | 10.6 | 0.8 | 12.28 | 36.1% | 11.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 29,315 | 4494 (15.3%) | 25.8% | 0.9% | {"EXTERNAL_STALE": 2743, "AGREES_WITH_KALSHI": 1157, "ALL_AGREE": 541, "SUPPORTS_MODEL_DIRECTION": 22, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 13, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,091 | 1164 (8.9%) | 35.9% | 1.6% | {"EXTERNAL_STALE": 727, "AGREES_WITH_KALSHI": 418, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,286 | 362 (5.0%) | 36.5% | 2.5% | {"EXTERNAL_STALE": 221, "AGREES_WITH_KALSHI": 132, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,568 | 339 (9.5%) | 36.9% | 2.6% | {"EXTERNAL_STALE": 205, "AGREES_WITH_KALSHI": 125, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,654 | 2511 (21.6%) | 17.4% | 0.8% | {"EXTERNAL_STALE": 1501, "ALL_AGREE": 541, "AGREES_WITH_KALSHI": 436, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 13, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,585 | 10.2 | 7.5 | 19.4 | 14.4 | 22.5 | 16.0 | 10.1 | 14.28 | 48.6% | 26.1% |
| 4-10x | 3,838 | 11.1 | 8.3 | 19.1 | 15.4 | 21.1 | 15.0 | 10.1 | 13.75 | 46.2% | 25.1% |
| <2x | 14,813 | 14.9 | 9.7 | 19.0 | 16.5 | 17.7 | 13.1 | 9.1 | 11.89 | 39.9% | 22.2% |
| >=10x | 5,079 | 11.0 | 6.3 | 15.1 | 14.4 | 21.9 | 19.4 | 11.7 | 16.18 | 53.0% | 31.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,415 | 12.3 | 8.5 | 19.6 | 16.0 | 19.4 | 13.6 | 10.6 | 12.96 | 43.6% | 24.2% |
| 300-1000 | 6,310 | 11.7 | 8.5 | 17.3 | 15.3 | 20.7 | 16.3 | 10.2 | 13.99 | 47.2% | 26.5% |
| <300 | 9,681 | 8.7 | 5.7 | 15.5 | 14.9 | 23.0 | 20.0 | 12.2 | 16.86 | 55.2% | 32.2% |
| >=3000 | 5,909 | 21.5 | 13.0 | 23.1 | 16.5 | 14.2 | 7.0 | 4.7 | 7.96 | 26.0% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 835 | 0.5484 | 0.4096 | 0.5006 | +0.048 | -0.091 | -0.0034 ± 0.0054 |
| ratio 4-10x | 574 | 0.5866 | 0.4403 | 0.4965 | +0.090 | -0.056 | 0.0123 ± 0.0067 |
| ratio <2x | 2056 | 0.5378 | 0.4137 | 0.4465 | +0.091 | -0.033 | 0.0123 ± 0.0032 |
| ratio >=10x | 764 | 0.5694 | 0.3936 | 0.4647 | +0.105 | -0.071 | 0.0059 ± 0.0066 |
| thinner_sample 1000-3000 | 1141 | 0.5423 | 0.4145 | 0.4479 | +0.095 | -0.033 | 0.0109 ± 0.0042 |
| thinner_sample 300-1000 | 972 | 0.5651 | 0.4216 | 0.4938 | +0.071 | -0.072 | 0.0001 ± 0.0052 |
| thinner_sample <300 | 1430 | 0.5591 | 0.3921 | 0.4657 | +0.093 | -0.074 | 0.0085 ± 0.0047 |
| thinner_sample >=3000 | 686 | 0.5362 | 0.4413 | 0.465 | +0.071 | -0.024 | 0.0136 ± 0.0045 |
| data_status ADEQUATE | 1196 | 0.539 | 0.4331 | 0.4523 | +0.087 | -0.019 | 0.0126 ± 0.0036 |
| data_status LIMITED | 985 | 0.5496 | 0.416 | 0.4792 | +0.070 | -0.063 | 0.0044 ± 0.0048 |
| data_status POOR | 2048 | 0.5612 | 0.3996 | 0.4702 | +0.091 | -0.071 | 0.0071 ± 0.0039 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 616 | 0.1987 | 0.1998 | -0.0010 ± 0.0006 | 0.5776 | 0.5799 | 0.5021 | 0.4872 | 0.5325 | -0.059 ± 0.0189 | -0.01 (5) |
| 3-5 | 395 | 0.2022 | 0.2016 | +0.0006 ± 0.0018 | 0.5875 | 0.5843 | 0.5025 | 0.4625 | 0.4734 | -0.099 ± 0.0233 | 0.02 (1) |
| 5-10 | 861 | 0.201 | 0.2008 | +0.0002 ± 0.0023 | 0.5883 | 0.5846 | 0.5099 | 0.4356 | 0.4669 | -0.088 ± 0.0158 | -0.0167 (6) |
| 10-15 | 728 | 0.213 | 0.2036 | +0.0094 ± 0.0042 | 0.6165 | 0.5887 | 0.5285 | 0.4044 | 0.4272 | -0.103 ± 0.0167 | -0.048 (5) |
| 15-25 | 966 | 0.224 | 0.2131 | +0.0109 ± 0.0058 | 0.6425 | 0.6099 | 0.5773 | 0.3815 | 0.4513 | -0.090 ± 0.0147 | -0.0033 (9) |
| 25-40 | 551 | 0.2232 | 0.2089 | +0.0143 ± 0.0116 | 0.6341 | 0.6009 | 0.6561 | 0.3464 | 0.4755 | -0.074 ± 0.0179 | -0.01 (1) |
| 40+ | 112 | 0.2783 | 0.1982 | +0.0800 ± 0.0365 | 0.7629 | 0.5814 | 0.7564 | 0.3087 | 0.4464 | -0.077 ± 0.0358 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3178 | 0.1813 | 0.1824 | -0.0011 ± 0.0003 | 0.5371 | 0.5383 | 0.4918 | 0.4767 | 0.5148 | -0.017 ± 0.0077 | -0.0129 (17) |
| 3-5 | 2089 | 0.1968 | 0.1956 | +0.0013 ± 0.0008 | 0.5737 | 0.5677 | 0.4849 | 0.445 | 0.4485 | -0.053 ± 0.0098 | 0.0 (2) |
| 5-10 | 4518 | 0.1971 | 0.1942 | +0.0030 ± 0.001 | 0.5783 | 0.5677 | 0.4801 | 0.4062 | 0.4225 | -0.045 ± 0.0066 | -0.0119 (21) |
| 10-15 | 3878 | 0.1969 | 0.1788 | +0.0181 ± 0.0017 | 0.5794 | 0.5281 | 0.4849 | 0.3603 | 0.3494 | -0.074 ± 0.0068 | -0.0281 (16) |
| 15-25 | 4919 | 0.2078 | 0.1689 | +0.0389 ± 0.0023 | 0.6087 | 0.5004 | 0.5048 | 0.3084 | 0.3086 | -0.073 ± 0.0058 | -0.0025 (44) |
| 25-40 | 3813 | 0.223 | 0.1308 | +0.0922 ± 0.0037 | 0.6401 | 0.3995 | 0.5317 | 0.2189 | 0.2313 | -0.058 ± 0.0057 | -0.01 (1) |
| 40+ | 2465 | 0.3809 | 0.0454 | +0.3355 ± 0.0048 | 0.9922 | 0.1754 | 0.6332 | 0.1078 | 0.0637 | -0.080 ± 0.004 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 476 | 0.204 | 0.2044 | -0.0005 ± 0.0007 | 0.5896 | 0.5905 | 0.504 | 0.4889 | 0.5063 | -0.109 ± 0.0222 | -0.01 (3) |
| 3-5 | 345 | 0.2214 | 0.2197 | +0.0017 ± 0.002 | 0.6288 | 0.6251 | 0.5134 | 0.4735 | 0.4667 | -0.115 ± 0.027 | 0.02 (1) |
| 5-10 | 749 | 0.2048 | 0.2044 | +0.0004 ± 0.0025 | 0.5959 | 0.5936 | 0.547 | 0.4722 | 0.5087 | -0.082 ± 0.017 | -0.01 (4) |
| 10-15 | 703 | 0.2175 | 0.2091 | +0.0084 ± 0.0043 | 0.6247 | 0.6039 | 0.5661 | 0.4418 | 0.4723 | -0.112 ± 0.0179 | -0.04 (5) |
| 15-25 | 991 | 0.23 | 0.2097 | +0.0202 ± 0.0057 | 0.6529 | 0.6021 | 0.588 | 0.3921 | 0.443 | -0.102 ± 0.0148 | -0.0133 (9) |
| 25-40 | 700 | 0.2609 | 0.1984 | +0.0625 ± 0.0106 | 0.7282 | 0.5773 | 0.6532 | 0.3375 | 0.3986 | -0.109 ± 0.0165 | -0.0075 (4) |
| 40+ | 265 | 0.3585 | 0.1732 | +0.1854 ± 0.0253 | 0.9868 | 0.5172 | 0.7322 | 0.2478 | 0.3132 | -0.070 ± 0.0245 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2673 | 0.1925 | 0.1928 | -0.0002 ± 0.0003 | 0.5617 | 0.5621 | 0.51 | 0.4951 | 0.5103 | -0.044 ± 0.0088 | -0.0133 (15) |
| 3-5 | 1793 | 0.1977 | 0.1971 | +0.0006 ± 0.0008 | 0.5732 | 0.5712 | 0.5142 | 0.4742 | 0.4858 | -0.042 ± 0.0107 | 0.02 (1) |
| 5-10 | 3983 | 0.1935 | 0.1921 | +0.0014 ± 0.001 | 0.5708 | 0.5627 | 0.5071 | 0.433 | 0.463 | -0.030 ± 0.007 | -0.0117 (6) |
| 10-15 | 3522 | 0.2003 | 0.1873 | +0.0130 ± 0.0018 | 0.5873 | 0.547 | 0.5123 | 0.3884 | 0.3989 | -0.059 ± 0.0074 | -0.0189 (18) |
| 15-25 | 4869 | 0.2159 | 0.1775 | +0.0384 ± 0.0024 | 0.6275 | 0.5226 | 0.5256 | 0.3297 | 0.3333 | -0.070 ± 0.0061 | -0.0086 (42) |
| 25-40 | 4499 | 0.2518 | 0.1383 | +0.1135 ± 0.0035 | 0.7083 | 0.4239 | 0.5586 | 0.2418 | 0.2238 | -0.084 ± 0.0055 | -0.0044 (18) |
| 40+ | 3521 | 0.3947 | 0.0619 | +0.3328 ± 0.0048 | 1.0392 | 0.2203 | 0.6522 | 0.1203 | 0.0863 | -0.072 ± 0.0041 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 592 | 0.1993 | 0.2016 | -0.0022 ± 0.0007 | 0.5794 | 0.585 | 0.4993 | 0.484 | 0.5507 | -0.024 ± 0.019 | -0.0137 (8) |
| 3-5 | 423 | 0.1999 | 0.1982 | +0.0017 ± 0.0018 | 0.5814 | 0.5761 | 0.5052 | 0.4655 | 0.4657 | -0.117 ± 0.0224 | 0.0067 (3) |
| 5-10 | 887 | 0.1996 | 0.1964 | +0.0032 ± 0.0022 | 0.5853 | 0.5736 | 0.5072 | 0.4332 | 0.4464 | -0.100 ± 0.0153 | -0.0071 (7) |
| 10-15 | 734 | 0.2085 | 0.2054 | +0.0032 ± 0.0042 | 0.6062 | 0.5931 | 0.5389 | 0.4152 | 0.4659 | -0.084 ± 0.0166 | -0.0317 (6) |
| 15-25 | 906 | 0.2303 | 0.2115 | +0.0188 ± 0.0059 | 0.6584 | 0.6062 | 0.5872 | 0.3928 | 0.4404 | -0.112 ± 0.0152 | -0.03 (1) |
| 25-40 | 569 | 0.2128 | 0.2173 | -0.0045 ± 0.0114 | 0.6131 | 0.6204 | 0.6676 | 0.356 | 0.5167 | -0.052 ± 0.0176 | 0.015 (2) |
| 40+ | 118 | 0.2919 | 0.209 | +0.0829 ± 0.0368 | 0.8038 | 0.6052 | 0.7657 | 0.3158 | 0.4576 | -0.070 ± 0.0381 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3134 | 0.1846 | 0.1852 | -0.0006 ± 0.0003 | 0.5435 | 0.5445 | 0.4911 | 0.476 | 0.492 | -0.036 ± 0.0077 | -0.0163 (35) |
| 3-5 | 2097 | 0.1926 | 0.1902 | +0.0024 ± 0.0008 | 0.5667 | 0.5591 | 0.4883 | 0.4487 | 0.4397 | -0.069 ± 0.0097 | -0.0094 (18) |
| 5-10 | 4598 | 0.1949 | 0.1889 | +0.0059 ± 0.001 | 0.5737 | 0.5541 | 0.4831 | 0.4091 | 0.4058 | -0.062 ± 0.0064 | -0.01 (31) |
| 10-15 | 3753 | 0.1908 | 0.1746 | +0.0162 ± 0.0017 | 0.565 | 0.5169 | 0.4967 | 0.3731 | 0.3688 | -0.069 ± 0.0068 | -0.015 (12) |
| 15-25 | 5065 | 0.2098 | 0.171 | +0.0388 ± 0.0023 | 0.6131 | 0.5053 | 0.5131 | 0.3181 | 0.3161 | -0.074 ± 0.0058 | -0.03 (2) |
| 25-40 | 3812 | 0.2193 | 0.1342 | +0.0850 ± 0.0037 | 0.6325 | 0.407 | 0.5377 | 0.2218 | 0.2469 | -0.049 ± 0.0057 | 0.01 (3) |
| 40+ | 2401 | 0.3949 | 0.0502 | +0.3447 ± 0.0052 | 1.0319 | 0.1878 | 0.6452 | 0.1142 | 0.0687 | -0.082 ± 0.0043 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 976 | 0.1937 | 0.1938 | -0.0001 ± 0.0005 | 0.5662 | 0.5661 | 0.5058 | 0.4907 | 0.4949 | -0.059 ± 0.0143 | -0.0224 (49) |
| 3-5 | 678 | 0.1907 | 0.19 | +0.0007 ± 0.0014 | 0.5583 | 0.5553 | 0.488 | 0.4482 | 0.4572 | -0.057 ± 0.0171 | -0.0194 (34) |
| 5-10 | 1412 | 0.2006 | 0.1945 | +0.0062 ± 0.0018 | 0.5904 | 0.571 | 0.4964 | 0.4231 | 0.4193 | -0.073 ± 0.0119 | -0.005 (78) |
| 10-15 | 935 | 0.2093 | 0.1982 | +0.0111 ± 0.0036 | 0.6076 | 0.5784 | 0.5192 | 0.396 | 0.4107 | -0.066 ± 0.0148 | 0.0014 (64) |
| 15-25 | 1257 | 0.2307 | 0.2095 | +0.0212 ± 0.0051 | 0.659 | 0.6038 | 0.5755 | 0.3805 | 0.4248 | -0.070 ± 0.0129 | -0.0214 (59) |
| 25-40 | 770 | 0.2479 | 0.2069 | +0.0410 ± 0.0101 | 0.7041 | 0.5949 | 0.6706 | 0.3583 | 0.4481 | -0.085 ± 0.0154 | -0.0219 (26) |
| 40+ | 257 | 0.3553 | 0.1958 | +0.1595 ± 0.0273 | 1.0249 | 0.5732 | 0.808 | 0.3255 | 0.4202 | -0.099 ± 0.0249 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3183 | 0.1821 | 0.1822 | -0.0002 ± 0.0003 | 0.5369 | 0.5363 | 0.5058 | 0.4904 | 0.5008 | -0.038 ± 0.0076 | -0.0157 (88) |
| 3-5 | 2198 | 0.1914 | 0.1896 | +0.0018 ± 0.0007 | 0.5601 | 0.5559 | 0.4948 | 0.455 | 0.4527 | -0.052 ± 0.0094 | -0.0209 (69) |
| 5-10 | 4390 | 0.1973 | 0.1888 | +0.0085 ± 0.001 | 0.5804 | 0.5554 | 0.4916 | 0.4181 | 0.4002 | -0.072 ± 0.0066 | -0.0082 (132) |
| 10-15 | 3048 | 0.2047 | 0.1891 | +0.0156 ± 0.002 | 0.5978 | 0.5564 | 0.5258 | 0.4026 | 0.3999 | -0.064 ± 0.0079 | -0.0053 (105) |
| 15-25 | 3837 | 0.2292 | 0.1991 | +0.0301 ± 0.0028 | 0.6612 | 0.5774 | 0.5679 | 0.3723 | 0.3941 | -0.065 ± 0.0072 | -0.0253 (107) |
| 25-40 | 2657 | 0.2593 | 0.1843 | +0.0749 ± 0.0053 | 0.7348 | 0.5377 | 0.6312 | 0.3173 | 0.3572 | -0.077 ± 0.0081 | -0.0229 (51) |
| 40+ | 1181 | 0.3779 | 0.1438 | +0.2341 ± 0.0116 | 1.0718 | 0.4336 | 0.729 | 0.2256 | 0.2574 | -0.072 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4229 | 1.047 ± 0.043 | 1.144 | 0.1689 | 0.1651 | 0.213 | 0.205 |
| gen2 | 4229 | 0.848 ± 0.04 | 1.099 | 0.1693 | 0.1656 | 0.233 | 0.2047 |
| gen1_elo | 4229 | 1.021 ± 0.042 | 1.133 | 0.1758 | 0.1651 | 0.2121 | 0.2053 |
| gen1_sr | 4229 | 1.042 ± 0.052 | 1.171 | 0.13 | 0.1676 | 0.2292 | 0.2043 |
| gen1_ledger | 6285 | 0.869 ± 0.03 | 1.084 | 0.1834 | 0.1795 | 0.2179 | 0.199 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 21,013)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,818 | 22.9% |
| STALE_QUOTE | market_freshness | 4,578 | 21.8% |
| BOOK_QUALITY | execution | 3,911 | 18.6% |
| POOR_DATA | data | 2,391 | 11.4% |
| LIMITED_DATA | data | 1,317 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,143 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 986 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 898 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 628 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 342 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.9%, market_freshness 21.8%, execution 18.6%, data 17.6%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.3%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.2%, THIN_PLAYER_HISTORY 60.1%, STALE_PLAYER_DATA 49.9%, STALE_KALSHI_QUOTE 44.3%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 24.8%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 16.3%, LEVEL_TRANSFER_RISK 11.1%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 8.0%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.5%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,251)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,867 | 34.4% |
| STALE_QUOTE | market_freshness | 2,110 | 18.8% |
| BOOK_QUALITY | execution | 2,037 | 18.1% |
| POOR_DATA | data | 993 | 8.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 613 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 512 | 4.5% |
| LIMITED_DATA | data | 404 | 3.6% |
| IN_PLAY_QUOTE | market_freshness/coverage | 397 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 240 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 77 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.4%, market_freshness 18.8%, execution 18.1%, data 12.4%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.1%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.7%, THIN_PLAYER_HISTORY 62.3%, STALE_KALSHI_QUOTE 52.2%, STALE_PLAYER_DATA 44.7%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 34.8%, WIDE_SPREAD 24.1%, PLAYER_IDENTITY_RISK 19.6%, MODEL_HIGH_UNCERTAINTY 18.1%, LEVEL_TRANSFER_RISK 9.8%, EVENT_MAPPING_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.4%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8764, "IDENTITY_AMBIGUOUS": 2487}; ticker orientation: {"VERIFIED": 11251}.

Checks: discipline:AMBIGUOUS 748, discipline:PASS 10503, identity_confidence:AMBIGUOUS 2207, identity_confidence:PASS 9044, level_mapping:NA 760, level_mapping:PASS 10491, market_pair:AMBIGUOUS 395, market_pair:NA 281, market_pair:PASS 10575, model_complement:NA 248, model_complement:PASS 11003, namesake:PASS 11251, physical_match_id:NA 3965, physical_match_id:PASS 7286, player_ids:PASS 11251, same_pair_other_event:PASS 11251, ticker_orientation:PASS 11251

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,942 | 4.8% | 4.3% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 20, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11} | 5.86 | 0.2176 / 0.2117 (457) | 19.0% | 3.8% | 3.2% | 2.9% |
| CHALLENGER | 7,721 | 17.3% | 7.0% | 11.9% | {"coverage": 753, "market_freshness/coverage": 164, "market_freshness": 148, "data": 136, "model_calibration_or_unknown": 60, "execution": 31, "model_calibration": 27, "mapping": 15, "possible_market_error": 1} | 7.44 | 0.22 / 0.2081 (1854) | 35.0% | 17.7% | 3.8% | 22.7% |
| DOUBLES | 1,580 | 47.3% | 46.8% | 6.7% | {"execution": 383, "mapping": 198, "market_freshness": 106, "market_freshness/coverage": 54, "coverage": 7} | 23.62 | 0.313 / 0.2359 (415) | 14.8% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 14,166 | 25.3% | 17.8% | 31.8% | {"coverage": 1317, "execution": 687, "market_freshness": 616, "data": 479, "market_freshness/coverage": 304, "mapping": 175, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.91 | 0.2141 / 0.1967 (3175) | 37.6% | 69.6% | 19.8% | 22.0% |
| ITF_WOMEN | 18,760 | 27.0% | 19.8% | 45.1% | {"coverage": 1757, "market_freshness": 1102, "execution": 879, "data": 713, "market_freshness/coverage": 426, "mapping": 118, "model_calibration_or_unknown": 66, "model_calibration": 11} | 12.84 | 0.2018 / 0.1932 (3632) | 39.8% | 56.1% | 9.9% | 22.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,785 | 5.0% | 4.5% | 1.2% | {"market_freshness": 45, "model_calibration_or_unknown": 28, "execution": 23, "model_calibration": 13, "data": 11, "market_freshness/coverage": 10, "coverage": 9, "mapping": 1} | 7.71 | 0.2385 / 0.2306 (451) | 24.5% | 1.3% | 1.4% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 15 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 16 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 17 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 18 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 19 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 20 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 21 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 22 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 23 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 26 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 27 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 28 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 30 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 32 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 33 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 34 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 36 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 38 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 39 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 40 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 41 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 43 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 44 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 45 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 46 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 47 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 48 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 49 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 812 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 50 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 770 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.971, "by_level_share_of_ge_25pp": {"ATP": 0.0167, "CHALLENGER": 0.1187, "DOUBLES": 0.0665, "ITF_MEN": 0.3184, "ITF_WOMEN": 0.4508, "OTHER": 0.0011, "WTA": 0.0124, "WTA125": 0.0155}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5224, "share_primary_cause_market_settled_or_in_play": 0.4335, "share_primary_cause_stale_quote_only": 0.1875}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11251, "identity_ambiguous_share": 0.221, "ticker_orientation": {"VERIFIED": 11251}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7286, "with_external": 362, "coverage": 0.0497, "external_status": {"EXTERNAL_STALE": 221, "AGREES_WITH_KALSHI": 132, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 221, "MODEL_LONE_OUTLIER": 132, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3646, "share_external_supports_model": 0.0249}, "pregame_clean_ge_25pp": {"n": 3568, "with_external": 339, "coverage": 0.095, "external_status": {"EXTERNAL_STALE": 205, "AGREES_WITH_KALSHI": 125, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 205, "MODEL_LONE_OUTLIER": 125, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3687, "share_external_supports_model": 0.0265}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 484.0, "median_sample_ratio": 2.45, "median_min_matches": 21.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2145, "data_status": {"POOR": 6300, "LIMITED": 2961, "ADEQUATE": 1990}, "comparison_lt_10pp": {"median_thinner_serve_points": 1667.0, "median_sample_ratio": 1.71, "median_min_matches": 93.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 835, "model_minus_observed": 0.0478, "kalshi_minus_observed": -0.091, "brier_diff_model_minus_kalshi": -0.0034}, "4-10x": {"n": 574, "model_minus_observed": 0.0901, "kalshi_minus_observed": -0.0562, "brier_diff_model_minus_kalshi": 0.0123}, "<2x": {"n": 2056, "model_minus_observed": 0.0913, "kalshi_minus_observed": -0.0328, "brier_diff_model_minus_kalshi": 0.0123}, ">=10x": {"n": 764, "model_minus_observed": 0.1047, "kalshi_minus_observed": -0.071, "brier_diff_model_minus_kalshi": 0.0059}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4229, "model": {"intercept": -0.549, "slope": 0.848, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.217, "slope": 1.099, "slope_se": 0.045}, "mean_extremity_model": 0.1693, "mean_extremity_kalshi": 0.1656, "model_brier": 0.233, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0282, "brier_diff_se": 0.0029, "model_logloss": 0.6624, "kalshi_logloss": 0.5921}, "fair_v1": {"n": 4229, "model": {"intercept": -0.411, "slope": 1.047, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.314, "slope": 1.144, "slope_se": 0.045}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1651, "model_brier": 0.213, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0024, "model_logloss": 0.6145, "kalshi_logloss": 0.5924}, "gen1_elo": {"n": 4229, "model": {"intercept": -0.396, "slope": 1.021, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.322, "slope": 1.133, "slope_se": 0.045}, "mean_extremity_model": 0.1758, "mean_extremity_kalshi": 0.1651, "model_brier": 0.2121, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.0068, "brier_diff_se": 0.0024, "model_logloss": 0.6132, "kalshi_logloss": 0.593}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2485, "share_ge_15": 0.4466, "median_abs_gap": 13.19, "n": 29315}, "gen1_elo": {"share_ge_25": 0.246, "share_ge_15": 0.4459, "median_abs_gap": 13.02, "n": 29315}, "gen1_sr": {"share_ge_25": 0.3173, "share_ge_15": 0.527, "median_abs_gap": 16.08, "n": 29315}, "gen2": {"share_ge_25": 0.3202, "share_ge_15": 0.5151, "median_abs_gap": 15.65, "n": 29315}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1568, "share_ge_15": 0.3634, "median_abs_gap": 10.98, "n": 22754}, "gen1_elo": {"share_ge_25": 0.1581, "share_ge_15": 0.3613, "median_abs_gap": 10.82, "n": 22751}, "gen1_sr": {"share_ge_25": 0.2247, "share_ge_15": 0.4497, "median_abs_gap": 13.26, "n": 22755}, "gen2": {"share_ge_25": 0.2403, "share_ge_15": 0.4478, "median_abs_gap": 13.14, "n": 22756}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0477, "share_ge_25_pregame_clean": 0.0428}, "WTA": {"median_abs_gap_pregame_clean": 7.71, "share_ge_25_all": 0.0503, "share_ge_25_pregame_clean": 0.045}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2336, "share_within_10pp_all": 0.4306, "share_within_10pp_pregame_clean": 0.4834, "corr_model_vs_mid_pregame_clean": 0.8437}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 616, "model_brier": 0.1987, "kalshi_brier": 0.1998, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 728, "model_brier": 0.213, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0094}, "15-25": {"n_settled": 966, "model_brier": 0.224, "kalshi_brier": 0.2131, "brier_diff_model_minus_kalshi": 0.0109}, "25-40": {"n_settled": 551, "model_brier": 0.2232, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.0143}, "3-5": {"n_settled": 395, "model_brier": 0.2022, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 112, "model_brier": 0.2783, "kalshi_brier": 0.1982, "brier_diff_model_minus_kalshi": 0.08}, "5-10": {"n_settled": 861, "model_brier": 0.201, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": 0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.549, "slope": 0.848, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.217, "slope": 1.099, "slope_se": 0.045}, "n": 4229}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.511, "slope": 0.869, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.159, "slope": 1.084, "slope_se": 0.035}, "n": 6285}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 415, "model_brier": 0.313, "kalshi_brier": 0.2359, "brier_diff_model_minus_kalshi": 0.0771, "brier_diff_se": 0.015, "corr_model_outcome": 0.037, "corr_kalshi_outcome": 0.2513}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
