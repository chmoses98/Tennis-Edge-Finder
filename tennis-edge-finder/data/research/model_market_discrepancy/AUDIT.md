# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-21T12:38Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 46,868): 0-3 14.1%, 3-5 9.5%, 5-10 19.7%, 10-15 15.3%, 15-25 19.4%, 25-40 14.0%, 40+ 8.0%; median gap 12.05 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.0%, Challenger 12.3%, doubles 6.9%). Main tour: ATP 5.0% and WTA 4.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 10,279): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.8%, BOOK_QUALITY 18.9%, STALE_QUOTE 18.1%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 33.8%, execution 18.9%, market_freshness 18.1%, data 13.0%, market_freshness/coverage 8.7%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%.
* **Stale / settled / in-play**: 51.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 10,279 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.7% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 494.0 points vs 1704.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.053, Gen-2 0.852, Gen-1 ledger 0.877 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 494 model 0.2233 vs Kalshi 0.2112; n 99 model 0.2917 vs Kalshi 0.1892.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 200,439 model-market comparisons (325,806 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 68,551 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-21T12:24:47.918285+00:00'], shadow board 52,902 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-21T12:24:51.768297+00:00'], Model 4 25,137 rows, 18,136 settled tickers, 6,341 tickers with an external scan.
* By model: {"gen1_ledger": 46298, "gen1_elo": 26598, "fair_v1": 26598, "gen2": 26598, "gen1_sr": 26598, "model4_fundamental": 23888, "model4_conditioned": 23861}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 46,868 | 14.1 | 9.5 | 19.7 | 15.3 | 19.4 | 14.0 | 8.0 | 12.05 | 41.3% | 21.9% |
| MW fair_v1 | 26,598 | 13.1 | 8.6 | 18.3 | 15.7 | 20.0 | 14.9 | 9.5 | 13.12 | 44.3% | 24.3% |
| MW gen1_elo | 26,598 | 12.9 | 8.7 | 19.2 | 15.2 | 20.0 | 14.9 | 9.2 | 12.86 | 44.1% | 24.1% |
| MW gen1_ledger | 20,270 | 15.5 | 10.7 | 21.6 | 14.9 | 18.6 | 12.8 | 6.0 | 10.54 | 37.4% | 18.8% |
| MW gen1_sr | 26,598 | 10.0 | 7.1 | 16.6 | 14.0 | 21.4 | 18.7 | 12.2 | 15.93 | 52.3% | 31.0% |
| MW gen2 | 26,598 | 11.1 | 7.3 | 16.3 | 14.2 | 20.0 | 17.8 | 13.4 | 15.52 | 51.2% | 31.2% |
| all families model4_conditioned | 23,861 | 21.8 | 19.2 | 34.4 | 17.7 | 4.5 | 1.4 | 1.1 | 5.95 | 6.9% | 2.4% |
| all families model4_fundamental | 23,888 | 16.4 | 13.1 | 34.0 | 20.4 | 11.2 | 3.5 | 1.3 | 7.88 | 16.1% | 4.9% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.7%, >=15pp 41.3%, >=20pp 30.6%, >=25pp 21.9%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.42pp; >=10pp 45.2%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,321 | 28.7 | 13.8 | 24.2 | 14.8 | 12.6 | 5.2 | 0.6 | 6.19 | 18.4% | 5.8% |
| CHALLENGER | 4,335 | 15.6 | 10.1 | 20.2 | 15.8 | 14.9 | 12.5 | 10.9 | 11.22 | 38.3% | 23.4% |
| ITF_MEN | 7,137 | 10.7 | 7.6 | 17.0 | 14.5 | 21.3 | 17.1 | 11.8 | 15.05 | 50.2% | 28.9% |
| ITF_WOMEN | 10,543 | 9.6 | 6.9 | 15.8 | 15.6 | 22.9 | 18.1 | 11.1 | 15.68 | 52.1% | 29.2% |
| WTA | 1,602 | 17.1 | 12.6 | 25.1 | 20.2 | 20.0 | 4.4 | 0.7 | 8.65 | 25.1% | 5.1% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,321 | 23.5 | 14.8 | 24.4 | 17.2 | 14.0 | 5.2 | 0.9 | 6.81 | 20.0% | 6.0% |
| CHALLENGER | 4,335 | 14.6 | 8.4 | 18.8 | 14.6 | 17.7 | 14.0 | 11.9 | 12.67 | 43.6% | 25.9% |
| ITF_MEN | 7,137 | 8.7 | 6.3 | 14.7 | 13.2 | 19.9 | 20.4 | 16.7 | 18.03 | 57.0% | 37.1% |
| ITF_WOMEN | 10,543 | 8.3 | 5.6 | 13.8 | 13.4 | 21.3 | 20.8 | 16.8 | 18.71 | 58.9% | 37.6% |
| WTA | 1,602 | 14.5 | 9.6 | 20.7 | 16.6 | 24.1 | 13.9 | 0.8 | 11.38 | 38.7% | 14.6% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,321 | 24.2 | 12.8 | 24.2 | 15.9 | 15.0 | 6.9 | 1.1 | 7.3 | 23.0% | 8.0% |
| CHALLENGER | 4,335 | 14.1 | 9.6 | 20.8 | 15.2 | 16.4 | 12.8 | 11.1 | 11.42 | 40.3% | 23.9% |
| ITF_MEN | 7,137 | 10.1 | 7.6 | 17.2 | 13.9 | 21.9 | 17.4 | 11.8 | 15.47 | 51.2% | 29.3% |
| ITF_WOMEN | 10,543 | 9.5 | 6.7 | 16.4 | 15.7 | 23.1 | 18.4 | 10.2 | 15.57 | 51.7% | 28.6% |
| WTA | 1,602 | 24.4 | 16.6 | 30.0 | 16.2 | 10.2 | 2.2 | 0.4 | 6.04 | 12.9% | 2.6% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,333 | 26.3 | 19.6 | 29.9 | 11.9 | 8.8 | 3.1 | 0.4 | 5.42 | 12.4% | 3.5% |
| CHALLENGER | 3,015 | 21.3 | 14.8 | 26.7 | 14.1 | 14.7 | 6.5 | 1.9 | 7.27 | 23.1% | 8.4% |
| DOUBLES | 1,469 | 5.1 | 4.2 | 11.6 | 10.3 | 20.4 | 26.1 | 22.2 | 24.1 | 68.7% | 48.3% |
| ITF_MEN | 5,660 | 14.0 | 8.8 | 20.3 | 15.8 | 21.0 | 13.3 | 6.8 | 12.09 | 41.1% | 20.1% |
| ITF_WOMEN | 6,884 | 12.6 | 9.0 | 19.4 | 15.1 | 21.6 | 16.3 | 6.0 | 12.85 | 43.9% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,028 | 22.3 | 15.9 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,262 | 29.1 | 14.0 | 24.6 | 14.7 | 12.3 | 4.8 | 0.6 | 6.06 | 17.7% | 5.3% |
| CHALLENGER | 3,062 | 20.4 | 12.4 | 24.9 | 18.3 | 15.2 | 6.8 | 2.0 | 8.42 | 24.0% | 8.8% |
| ITF_MEN | 5,288 | 13.0 | 9.1 | 20.1 | 16.4 | 22.1 | 14.1 | 5.3 | 12.3 | 41.4% | 19.3% |
| ITF_WOMEN | 7,954 | 11.3 | 8.2 | 17.8 | 17.8 | 24.6 | 15.3 | 5.0 | 13.47 | 44.9% | 20.3% |
| WTA | 1,559 | 17.3 | 12.3 | 25.1 | 20.3 | 19.9 | 4.3 | 0.7 | 8.65 | 24.9% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,262 | 23.8 | 15.1 | 24.5 | 17.1 | 14.0 | 4.8 | 0.7 | 6.58 | 19.5% | 5.5% |
| CHALLENGER | 3,062 | 18.4 | 10.8 | 23.4 | 17.4 | 17.9 | 9.8 | 2.3 | 9.4 | 30.0% | 12.1% |
| ITF_MEN | 5,289 | 10.2 | 7.4 | 16.9 | 14.9 | 21.9 | 18.6 | 10.1 | 15.25 | 50.5% | 28.6% |
| ITF_WOMEN | 7,954 | 9.3 | 6.5 | 15.2 | 14.9 | 23.2 | 20.3 | 10.7 | 16.54 | 54.2% | 31.1% |
| WTA | 1,559 | 14.5 | 9.6 | 20.6 | 16.5 | 24.1 | 14.0 | 0.8 | 11.43 | 38.8% | 14.8% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,292 | 26.5 | 19.8 | 29.9 | 12.2 | 8.4 | 3.0 | 0.2 | 5.38 | 11.6% | 3.2% |
| CHALLENGER | 2,626 | 22.8 | 15.9 | 28.3 | 14.0 | 14.1 | 4.3 | 0.6 | 6.7 | 19.0% | 4.9% |
| DOUBLES | 1,366 | 5.0 | 4.4 | 11.9 | 10.5 | 20.4 | 26.1 | 21.7 | 23.93 | 68.2% | 47.8% |
| ITF_MEN | 4,730 | 15.2 | 9.5 | 22.0 | 16.6 | 20.9 | 11.7 | 4.1 | 11.02 | 36.7% | 15.8% |
| ITF_WOMEN | 5,756 | 13.5 | 9.5 | 20.7 | 15.9 | 21.8 | 15.1 | 3.5 | 11.73 | 40.4% | 18.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 979 | 22.8 | 16.4 | 29.5 | 18.3 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,469 | 5.1 | 4.2 | 11.6 | 10.3 | 20.4 | 26.1 | 22.2 | 24.1 | 68.7% | 48.3% |
| singles | 18,801 | 16.3 | 11.2 | 22.3 | 15.2 | 18.4 | 11.8 | 4.7 | 10.03 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,002 | 13.3 | 8.9 | 19.0 | 15.7 | 19.0 | 14.8 | 9.4 | 12.81 | 43.1% | 24.2% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 16,682 | 13.4 | 8.6 | 18.3 | 15.4 | 20.1 | 14.7 | 9.4 | 13.1 | 44.3% | 24.1% |
| UNKNOWN | 3,677 | 11.4 | 7.9 | 17.1 | 17.2 | 20.9 | 15.6 | 9.9 | 13.67 | 46.5% | 25.6% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,547 | 19.7 | 11.6 | 21.1 | 16.7 | 15.9 | 9.0 | 6.0 | 9.3 | 30.9% | 14.9% |
| B | 3,363 | 12.5 | 9.0 | 19.9 | 17.1 | 19.0 | 12.1 | 10.3 | 12.2 | 41.4% | 22.4% |
| C | 3,730 | 12.0 | 9.0 | 19.1 | 15.0 | 19.6 | 15.2 | 10.1 | 13.18 | 44.9% | 25.3% |
| D | 4,346 | 12.3 | 7.8 | 17.0 | 15.5 | 22.2 | 15.7 | 9.5 | 14.02 | 47.4% | 25.2% |
| F | 7,612 | 7.9 | 5.6 | 15.1 | 14.5 | 23.4 | 21.3 | 12.2 | 17.7 | 57.0% | 33.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,726 | 23.1 | 15.9 | 28.6 | 15.1 | 11.8 | 4.1 | 1.5 | 6.68 | 17.3% | 5.5% |
| B | 2,807 | 16.1 | 10.5 | 23.7 | 16.2 | 19.0 | 10.6 | 3.9 | 9.95 | 33.6% | 14.5% |
| C | 4,002 | 11.3 | 7.3 | 18.5 | 14.3 | 21.3 | 16.4 | 10.8 | 14.25 | 48.5% | 27.3% |
| D | 2,906 | 14.3 | 9.8 | 19.8 | 14.4 | 21.0 | 14.5 | 6.1 | 12.05 | 41.6% | 20.6% |
| F | 4,829 | 10.3 | 8.1 | 15.6 | 14.6 | 22.7 | 20.5 | 8.4 | 15.83 | 51.5% | 28.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,578 | 17.9 | 10.3 | 20.5 | 16.7 | 16.4 | 9.8 | 8.4 | 10.38 | 34.5% | 18.1% |
| LIMITED | 5,811 | 13.7 | 10.3 | 20.2 | 15.7 | 19.2 | 13.5 | 7.5 | 11.77 | 40.1% | 20.9% |
| POOR | 12,209 | 9.5 | 6.5 | 15.9 | 14.9 | 22.9 | 19.1 | 11.2 | 16.09 | 53.2% | 30.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,111 | 26.7 | 20.7 | 34.3 | 12.1 | 4.6 | 1.5 | 0.2 | 5.24 | 6.3% | 1.7% |
| GAME_SPREAD | 4,422 | 22.7 | 15.4 | 33.2 | 17.1 | 8.9 | 2.4 | 0.3 | 6.59 | 11.6% | 2.7% |
| MATCH_WINNER | 20,270 | 15.5 | 10.7 | 21.6 | 14.9 | 18.6 | 12.8 | 6.0 | 10.54 | 37.4% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,331 | 29.8 | 16.8 | 30.5 | 12.6 | 8.1 | 1.7 | 0.4 | 5.44 | 10.3% | 2.1% |
| TOTAL_GAMES | 7,140 | 8.3 | 9.4 | 36.4 | 29.1 | 10.8 | 3.3 | 2.7 | 9.54 | 16.8% | 6.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,335 | 25.3 | 34.5 | 32.3 | 4.1 | 3.1 | 0.6 | 0.2 | 4.46 | 3.8% | 0.7% |
| GAME_SPREAD | 5,714 | 45.7 | 17.0 | 26.9 | 7.7 | 1.8 | 0.7 | 0.2 | 3.44 | 2.7% | 0.9% |
| TOTAL_GAMES | 9,812 | 4.8 | 7.4 | 40.5 | 35.2 | 7.2 | 2.5 | 2.3 | 9.72 | 12.0% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,338 | 24.2 | 17.9 | 35.3 | 12.4 | 7.3 | 2.6 | 0.3 | 5.81 | 10.2% | 2.9% |
| GAME_SPREAD | 5,717 | 19.3 | 13.1 | 28.1 | 20.1 | 14.2 | 4.4 | 0.9 | 8.0 | 19.5% | 5.3% |
| TOTAL_GAMES | 9,833 | 8.1 | 8.9 | 36.4 | 27.5 | 12.8 | 3.8 | 2.5 | 9.61 | 19.1% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 26,598 | 44.3% | 24.3% | 13.12 | 36.2% | 15.4% | 10.98 |
| gen1_elo | 26,598 | 44.1% | 24.1% | 12.86 | 35.6% | 15.5% | 10.57 |
| gen1_sr | 26,598 | 52.3% | 31.0% | 15.93 | 44.9% | 22.0% | 13.25 |
| gen2 | 26,598 | 51.2% | 31.2% | 15.52 | 44.8% | 23.5% | 13.17 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 13,883 | 15.8 | 10.3 | 21.1 | 17.3 | 20.4 | 11.8 | 3.3 | 10.8 | 35.5% | 15.1% |
| STALE | 12,715 | 10.1 | 6.7 | 15.3 | 14.0 | 19.6 | 18.2 | 16.2 | 16.92 | 54.0% | 34.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 13,738 | 16.6 | 11.2 | 22.4 | 14.9 | 17.7 | 12.2 | 4.9 | 9.91 | 34.7% | 17.1% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 46,868 | 13738 | 17355 | 15775 | 23.9 | 124.5 | 1400.4 |
| ge_15pp | 19,366 | 4773 | 6222 | 8371 | 25.7 | 415.0 | 1380.4 |
| ge_25pp | 10,279 | 2346 | 2690 | 5243 | 31.1 | 560.9 | 1380.4 |
| lt_10pp | 20,314 | 6914 | 8184 | 5216 | 21.7 | 47.3 | 1341.5 |

Current slate `SL-20261021T123805Z-1b0616b7`: 687 priced rows, quote age at build {'median': 13.8, 'max': 13.8}, freshness {'AGING': 687}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 20 | 0.0 | 0.0 | 25.0 | 0.0 | 40.0 | 35.0 | 0.0 | 20.49 | 75.0% | 35.0% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,486 | 19.8 | 10.8 | 23.5 | 18.7 | 19.2 | 7.3 | 0.7 | 9.14 | 27.2% | 8.0% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 462 | 66.2 | 33.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.22 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,039 | 0.0 | 2.3 | 33.6 | 26.2 | 26.2 | 10.9 | 0.9 | 12.8 | 37.9% | 11.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 26,598 | 4036 (15.2%) | 25.7% | 0.9% | {"EXTERNAL_STALE": 2486, "AGREES_WITH_KALSHI": 1039, "ALL_AGREE": 462, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 11,794 | 1087 (9.2%) | 36.2% | 1.6% | {"EXTERNAL_STALE": 676, "AGREES_WITH_KALSHI": 394, "SUPPORTS_MODEL_DIRECTION": 15, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,471 | 329 (5.1%) | 37.1% | 2.4% | {"EXTERNAL_STALE": 199, "AGREES_WITH_KALSHI": 122, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,196 | 309 (9.7%) | 37.5% | 2.6% | {"EXTERNAL_STALE": 185, "AGREES_WITH_KALSHI": 116, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 10,631 | 2211 (20.8%) | 16.9% | 0.9% | {"EXTERNAL_STALE": 1344, "ALL_AGREE": 462, "AGREES_WITH_KALSHI": 373, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,093 | 10.7 | 7.7 | 19.3 | 14.6 | 22.3 | 15.7 | 9.8 | 14.0 | 47.8% | 25.5% |
| 4-10x | 3,467 | 11.3 | 8.5 | 18.9 | 15.5 | 21.1 | 14.8 | 9.9 | 13.6 | 45.8% | 24.7% |
| <2x | 13,611 | 15.1 | 9.6 | 18.8 | 16.7 | 18.2 | 13.1 | 8.5 | 11.91 | 39.8% | 21.6% |
| >=10x | 4,427 | 11.2 | 6.4 | 15.2 | 14.0 | 22.1 | 19.4 | 11.8 | 16.24 | 53.2% | 31.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,725 | 12.4 | 8.5 | 19.5 | 16.4 | 19.7 | 13.5 | 10.0 | 12.88 | 43.2% | 23.5% |
| 300-1000 | 5,782 | 11.8 | 8.7 | 17.0 | 15.5 | 21.0 | 16.2 | 9.8 | 13.92 | 47.0% | 26.0% |
| <300 | 8,535 | 9.0 | 5.8 | 15.4 | 14.6 | 23.1 | 20.2 | 11.9 | 16.85 | 55.2% | 32.0% |
| >=3000 | 5,556 | 21.5 | 12.7 | 22.7 | 16.7 | 14.7 | 7.0 | 4.8 | 8.07 | 26.4% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 776 | 0.5459 | 0.4094 | 0.5 | +0.046 | -0.091 | -0.003 ± 0.0055 |
| ratio 4-10x | 530 | 0.5868 | 0.4414 | 0.4981 | +0.089 | -0.057 | 0.0119 ± 0.007 |
| ratio <2x | 1905 | 0.5368 | 0.4136 | 0.4504 | +0.086 | -0.037 | 0.0122 ± 0.0033 |
| ratio >=10x | 669 | 0.5668 | 0.3916 | 0.4649 | +0.102 | -0.073 | 0.004 ± 0.0071 |
| thinner_sample 1000-3000 | 1058 | 0.5418 | 0.4144 | 0.4499 | +0.092 | -0.035 | 0.0103 ± 0.0044 |
| thinner_sample 300-1000 | 903 | 0.5651 | 0.4229 | 0.5006 | +0.065 | -0.078 | -0.0009 ± 0.0053 |
| thinner_sample <300 | 1274 | 0.5558 | 0.3907 | 0.4615 | +0.094 | -0.071 | 0.0091 ± 0.0049 |
| thinner_sample >=3000 | 645 | 0.5344 | 0.4392 | 0.4729 | +0.061 | -0.034 | 0.0127 ± 0.0046 |
| data_status ADEQUATE | 1109 | 0.5369 | 0.4312 | 0.4572 | +0.080 | -0.026 | 0.0122 ± 0.0038 |
| data_status LIMITED | 931 | 0.5494 | 0.417 | 0.4791 | +0.070 | -0.062 | 0.0045 ± 0.0049 |
| data_status POOR | 1840 | 0.5594 | 0.3994 | 0.4717 | +0.088 | -0.072 | 0.0067 ± 0.004 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 573 | 0.1962 | 0.1976 | -0.0014 ± 0.0006 | 0.5707 | 0.5736 | 0.497 | 0.4823 | 0.5358 | -0.050 ± 0.0193 | -0.01 (5) |
| 3-5 | 365 | 0.1996 | 0.1994 | +0.0001 ± 0.0019 | 0.5819 | 0.5801 | 0.5025 | 0.4624 | 0.4795 | -0.089 ± 0.024 | 0.02 (1) |
| 5-10 | 797 | 0.2031 | 0.203 | +0.0001 ± 0.0024 | 0.5923 | 0.5901 | 0.5136 | 0.439 | 0.4718 | -0.086 ± 0.0166 | -0.0167 (6) |
| 10-15 | 676 | 0.2122 | 0.2032 | +0.0090 ± 0.0043 | 0.6138 | 0.5879 | 0.5236 | 0.3996 | 0.4246 | -0.099 ± 0.0173 | -0.048 (5) |
| 15-25 | 876 | 0.2239 | 0.2142 | +0.0097 ± 0.0061 | 0.6425 | 0.6128 | 0.5774 | 0.3815 | 0.4543 | -0.084 ± 0.0154 | -0.0033 (9) |
| 25-40 | 494 | 0.2233 | 0.2112 | +0.0121 ± 0.0123 | 0.6341 | 0.6064 | 0.6575 | 0.3485 | 0.4798 | -0.070 ± 0.0188 | -0.01 (1) |
| 40+ | 99 | 0.2917 | 0.1892 | +0.1024 ± 0.0386 | 0.7974 | 0.5624 | 0.7503 | 0.3029 | 0.4141 | -0.099 ± 0.0381 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2871 | 0.1808 | 0.1819 | -0.0011 ± 0.0003 | 0.5351 | 0.5364 | 0.482 | 0.467 | 0.5057 | -0.018 ± 0.008 | -0.0129 (17) |
| 3-5 | 1876 | 0.1949 | 0.194 | +0.0010 ± 0.0008 | 0.5703 | 0.5646 | 0.484 | 0.4441 | 0.4515 | -0.050 ± 0.0104 | 0.0 (2) |
| 5-10 | 3996 | 0.1969 | 0.1938 | +0.0032 ± 0.001 | 0.5766 | 0.5667 | 0.484 | 0.41 | 0.4244 | -0.049 ± 0.0071 | -0.0119 (21) |
| 10-15 | 3478 | 0.202 | 0.1837 | +0.0182 ± 0.0018 | 0.5911 | 0.5403 | 0.4857 | 0.3612 | 0.3499 | -0.075 ± 0.0072 | -0.0281 (16) |
| 15-25 | 4390 | 0.2078 | 0.1711 | +0.0367 ± 0.0024 | 0.6087 | 0.5059 | 0.5013 | 0.3049 | 0.3098 | -0.069 ± 0.0062 | -0.0025 (44) |
| 25-40 | 3368 | 0.2235 | 0.1321 | +0.0914 ± 0.0039 | 0.6411 | 0.403 | 0.5333 | 0.2204 | 0.2337 | -0.059 ± 0.0061 | -0.01 (1) |
| 40+ | 2158 | 0.3783 | 0.0455 | +0.3328 ± 0.0052 | 0.9856 | 0.1759 | 0.6311 | 0.107 | 0.0639 | -0.080 ± 0.0043 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 434 | 0.2037 | 0.2042 | -0.0005 ± 0.0008 | 0.5899 | 0.5908 | 0.5039 | 0.489 | 0.5069 | -0.101 ± 0.0234 | -0.01 (3) |
| 3-5 | 320 | 0.2214 | 0.2204 | +0.0011 ± 0.0021 | 0.6286 | 0.6265 | 0.5115 | 0.4714 | 0.4719 | -0.105 ± 0.0283 | 0.02 (1) |
| 5-10 | 680 | 0.1997 | 0.2007 | -0.0010 ± 0.0026 | 0.5828 | 0.585 | 0.5455 | 0.4705 | 0.5147 | -0.072 ± 0.0177 | -0.01 (4) |
| 10-15 | 640 | 0.2171 | 0.2107 | +0.0063 ± 0.0045 | 0.6241 | 0.6076 | 0.5629 | 0.4386 | 0.4781 | -0.098 ± 0.0188 | -0.04 (5) |
| 15-25 | 929 | 0.2302 | 0.2094 | +0.0208 ± 0.0059 | 0.6535 | 0.6012 | 0.5918 | 0.3955 | 0.4446 | -0.100 ± 0.0153 | -0.0133 (9) |
| 25-40 | 647 | 0.2607 | 0.2014 | +0.0593 ± 0.0111 | 0.7285 | 0.5846 | 0.6578 | 0.3419 | 0.408 | -0.105 ± 0.0172 | -0.0075 (4) |
| 40+ | 230 | 0.3617 | 0.1723 | +0.1894 ± 0.0271 | 0.9991 | 0.5155 | 0.7366 | 0.2534 | 0.313 | -0.077 ± 0.0262 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2392 | 0.1915 | 0.1918 | -0.0003 ± 0.0003 | 0.5611 | 0.5615 | 0.504 | 0.4891 | 0.5067 | -0.041 ± 0.0093 | -0.0133 (15) |
| 3-5 | 1627 | 0.1989 | 0.199 | -0.0001 ± 0.0009 | 0.576 | 0.5758 | 0.5095 | 0.4695 | 0.4892 | -0.034 ± 0.0113 | 0.02 (1) |
| 5-10 | 3537 | 0.1908 | 0.1898 | +0.0011 ± 0.0011 | 0.5636 | 0.5571 | 0.5016 | 0.4277 | 0.4591 | -0.030 ± 0.0074 | -0.0117 (6) |
| 10-15 | 3144 | 0.199 | 0.1889 | +0.0101 ± 0.0019 | 0.585 | 0.5508 | 0.513 | 0.3888 | 0.4119 | -0.046 ± 0.0079 | -0.0189 (18) |
| 15-25 | 4465 | 0.2167 | 0.1789 | +0.0377 ± 0.0025 | 0.6298 | 0.5256 | 0.5294 | 0.3331 | 0.338 | -0.069 ± 0.0064 | -0.0086 (42) |
| 25-40 | 3953 | 0.25 | 0.1408 | +0.1091 ± 0.0038 | 0.7045 | 0.4298 | 0.5627 | 0.2462 | 0.235 | -0.080 ± 0.0059 | -0.0044 (18) |
| 40+ | 3019 | 0.3979 | 0.063 | +0.3349 ± 0.0052 | 1.0477 | 0.2233 | 0.6573 | 0.1217 | 0.0898 | -0.070 ± 0.0045 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 548 | 0.1959 | 0.1983 | -0.0025 ± 0.0007 | 0.5714 | 0.5772 | 0.4952 | 0.48 | 0.5566 | -0.012 ± 0.0193 | -0.0137 (8) |
| 3-5 | 396 | 0.1962 | 0.1942 | +0.0019 ± 0.0018 | 0.5704 | 0.5661 | 0.5038 | 0.4642 | 0.4621 | -0.117 ± 0.023 | 0.0067 (3) |
| 5-10 | 829 | 0.2026 | 0.1993 | +0.0033 ± 0.0023 | 0.5927 | 0.5812 | 0.5104 | 0.4364 | 0.4487 | -0.099 ± 0.016 | -0.0071 (7) |
| 10-15 | 677 | 0.2088 | 0.2058 | +0.0031 ± 0.0043 | 0.6051 | 0.5942 | 0.5387 | 0.4154 | 0.4668 | -0.083 ± 0.0173 | -0.0317 (6) |
| 15-25 | 818 | 0.2321 | 0.2121 | +0.0200 ± 0.0063 | 0.6631 | 0.6073 | 0.5852 | 0.3913 | 0.4364 | -0.112 ± 0.0159 | -0.03 (1) |
| 25-40 | 510 | 0.2114 | 0.2185 | -0.0071 ± 0.0121 | 0.6089 | 0.6237 | 0.6669 | 0.3553 | 0.5196 | -0.046 ± 0.0185 | 0.015 (2) |
| 40+ | 102 | 0.3011 | 0.207 | +0.0940 ± 0.0397 | 0.8253 | 0.6027 | 0.762 | 0.3114 | 0.4412 | -0.077 ± 0.0414 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2784 | 0.1827 | 0.1835 | -0.0008 ± 0.0003 | 0.5391 | 0.5408 | 0.4899 | 0.4747 | 0.495 | -0.033 ± 0.0082 | -0.0163 (35) |
| 3-5 | 1907 | 0.1869 | 0.1846 | +0.0024 ± 0.0008 | 0.5513 | 0.5455 | 0.4843 | 0.4447 | 0.4358 | -0.069 ± 0.0101 | -0.0094 (18) |
| 5-10 | 4194 | 0.1966 | 0.1909 | +0.0057 ± 0.001 | 0.5775 | 0.5587 | 0.4855 | 0.4116 | 0.4094 | -0.062 ± 0.0068 | -0.01 (31) |
| 10-15 | 3323 | 0.1969 | 0.1804 | +0.0165 ± 0.0018 | 0.5784 | 0.5311 | 0.5016 | 0.378 | 0.3732 | -0.071 ± 0.0073 | -0.015 (12) |
| 15-25 | 4484 | 0.2124 | 0.1734 | +0.0390 ± 0.0024 | 0.6195 | 0.5113 | 0.5091 | 0.3146 | 0.3111 | -0.075 ± 0.0062 | -0.03 (2) |
| 25-40 | 3355 | 0.2191 | 0.1331 | +0.0859 ± 0.004 | 0.6314 | 0.4047 | 0.5352 | 0.219 | 0.2429 | -0.051 ± 0.006 | 0.01 (3) |
| 40+ | 2090 | 0.3936 | 0.0508 | +0.3428 ± 0.0056 | 1.0287 | 0.1897 | 0.6442 | 0.114 | 0.0694 | -0.082 ± 0.0047 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 911 | 0.1956 | 0.1958 | -0.0002 ± 0.0005 | 0.5708 | 0.5709 | 0.5071 | 0.492 | 0.4951 | -0.059 ± 0.0149 | -0.0224 (49) |
| 3-5 | 636 | 0.191 | 0.1906 | +0.0004 ± 0.0014 | 0.5591 | 0.5571 | 0.4848 | 0.445 | 0.4575 | -0.051 ± 0.0175 | -0.0194 (34) |
| 5-10 | 1345 | 0.1996 | 0.1932 | +0.0065 ± 0.0018 | 0.5875 | 0.568 | 0.4926 | 0.4192 | 0.4134 | -0.073 ± 0.0122 | -0.005 (78) |
| 10-15 | 883 | 0.2095 | 0.199 | +0.0105 ± 0.0037 | 0.6072 | 0.5804 | 0.516 | 0.3929 | 0.41 | -0.064 ± 0.0153 | 0.0014 (64) |
| 15-25 | 1175 | 0.231 | 0.2109 | +0.0201 ± 0.0053 | 0.6593 | 0.6075 | 0.5728 | 0.3781 | 0.4255 | -0.065 ± 0.0134 | -0.0214 (59) |
| 25-40 | 717 | 0.249 | 0.2055 | +0.0435 ± 0.0104 | 0.7062 | 0.5914 | 0.6653 | 0.3524 | 0.4379 | -0.083 ± 0.0158 | -0.0219 (26) |
| 40+ | 243 | 0.3489 | 0.1972 | +0.1516 ± 0.0283 | 1.0078 | 0.5765 | 0.8065 | 0.3219 | 0.428 | -0.084 ± 0.0253 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2969 | 0.1829 | 0.1831 | -0.0002 ± 0.0003 | 0.5387 | 0.5383 | 0.507 | 0.4917 | 0.5002 | -0.038 ± 0.0079 | -0.0157 (88) |
| 3-5 | 2050 | 0.1904 | 0.1885 | +0.0020 ± 0.0008 | 0.557 | 0.553 | 0.4904 | 0.4507 | 0.4459 | -0.054 ± 0.0097 | -0.0209 (69) |
| 5-10 | 4132 | 0.1968 | 0.1882 | +0.0086 ± 0.001 | 0.5787 | 0.5539 | 0.4881 | 0.4147 | 0.3957 | -0.072 ± 0.0068 | -0.0082 (132) |
| 10-15 | 2864 | 0.2056 | 0.191 | +0.0146 ± 0.002 | 0.5998 | 0.5609 | 0.523 | 0.4 | 0.4012 | -0.060 ± 0.0082 | -0.0053 (105) |
| 15-25 | 3540 | 0.2292 | 0.1983 | +0.0309 ± 0.0029 | 0.6608 | 0.5761 | 0.5653 | 0.37 | 0.3901 | -0.065 ± 0.0075 | -0.0253 (107) |
| 25-40 | 2470 | 0.2599 | 0.1823 | +0.0776 ± 0.0054 | 0.7362 | 0.5328 | 0.626 | 0.3114 | 0.3482 | -0.075 ± 0.0084 | -0.0229 (51) |
| 40+ | 1112 | 0.3756 | 0.1402 | +0.2354 ± 0.0118 | 1.0631 | 0.4246 | 0.7258 | 0.2227 | 0.2536 | -0.072 ± 0.0104 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3880 | 1.053 ± 0.046 | 1.162 | 0.1674 | 0.1645 | 0.2129 | 0.2051 |
| gen2 | 3880 | 0.852 ± 0.042 | 1.117 | 0.1704 | 0.165 | 0.2319 | 0.2049 |
| gen1_elo | 3880 | 1.029 ± 0.044 | 1.145 | 0.174 | 0.1647 | 0.212 | 0.2052 |
| gen1_sr | 3880 | 1.051 ± 0.055 | 1.191 | 0.1311 | 0.167 | 0.2283 | 0.2045 |
| gen1_ledger | 5910 | 0.877 ± 0.032 | 1.084 | 0.1809 | 0.1799 | 0.2179 | 0.1994 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 19,366)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,362 | 22.5% |
| STALE_QUOTE | market_freshness | 4,083 | 21.1% |
| BOOK_QUALITY | execution | 3,722 | 19.2% |
| POOR_DATA | data | 2,247 | 11.6% |
| LIMITED_DATA | data | 1,272 | 6.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,037 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 951 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 813 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 559 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 320 | 1.7% |

Cause class: coverage 22.5%, market_freshness 21.1%, execution 19.2%, data 18.2%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.9%, mapping 4.2%, model_calibration 1.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 70.8%, THIN_PLAYER_HISTORY 59.5%, STALE_PLAYER_DATA 51.9%, STALE_KALSHI_QUOTE 43.2%, MODEL_INTERNAL_DISAGREEMENT 42.0%, ASYMMETRIC_SAMPLE_SIZE 33.0%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 15.7%, LEVEL_TRANSFER_RISK 10.7%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 10,279)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,475 | 33.8% |
| BOOK_QUALITY | execution | 1,946 | 18.9% |
| STALE_QUOTE | market_freshness | 1,863 | 18.1% |
| POOR_DATA | data | 944 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 548 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 463 | 4.5% |
| LIMITED_DATA | data | 391 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 350 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 224 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 33.8%, execution 18.9%, market_freshness 18.1%, data 13.0%, market_freshness/coverage 8.7%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.7%, THIN_PLAYER_HISTORY 62.0%, STALE_KALSHI_QUOTE 51.0%, STALE_PLAYER_DATA 47.1%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.9%, PLAYER_IDENTITY_RISK 19.1%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.8%, POST_SETTLEMENT_OBSERVATION 33.8%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8049, "IDENTITY_AMBIGUOUS": 2230}; ticker orientation: {"VERIFIED": 10279}.

Checks: discipline:AMBIGUOUS 710, discipline:PASS 9569, identity_confidence:AMBIGUOUS 1963, identity_confidence:PASS 8316, level_mapping:NA 722, level_mapping:PASS 9557, market_pair:AMBIGUOUS 373, market_pair:NA 247, market_pair:PASS 9659, model_complement:NA 214, model_complement:PASS 10065, namesake:PASS 10279, physical_match_id:NA 3808, physical_match_id:PASS 6471, player_ids:PASS 10279, same_pair_other_event:PASS 10279, ticker_orientation:PASS 10279

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,654 | 5.0% | 4.6% | 1.8% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 19, "model_calibration": 13, "market_freshness/coverage": 12, "coverage": 7} | 5.86 | 0.2239 / 0.2151 (407) | 18.6% | 4.1% | 3.4% | 2.7% |
| CHALLENGER | 7,350 | 17.2% | 7.0% | 12.3% | {"coverage": 712, "market_freshness/coverage": 158, "market_freshness": 146, "data": 122, "model_calibration_or_unknown": 58, "execution": 30, "model_calibration": 27, "mapping": 14} | 7.46 | 0.2177 / 0.2069 (1780) | 35.0% | 17.3% | 3.9% | 22.6% |
| DOUBLES | 1,469 | 48.3% | 47.8% | 6.9% | {"execution": 364, "mapping": 183, "market_freshness": 106, "market_freshness/coverage": 50, "coverage": 7} | 23.93 | 0.3195 / 0.2349 (372) | 15.9% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 12,797 | 25.0% | 17.7% | 31.1% | {"coverage": 1165, "execution": 644, "market_freshness": 525, "data": 443, "market_freshness/coverage": 261, "mapping": 156, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.68 | 0.2133 / 0.1955 (2895) | 36.4% | 67.0% | 17.8% | 21.7% |
| ITF_WOMEN | 17,427 | 26.5% | 19.6% | 44.9% | {"coverage": 1566, "market_freshness": 955, "execution": 858, "data": 701, "market_freshness/coverage": 368, "mapping": 104, "model_calibration_or_unknown": 53, "model_calibration": 11} | 12.83 | 0.2027 / 0.1951 (3375) | 38.1% | 57.4% | 10.0% | 21.3% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,630 | 4.6% | 4.2% | 1.2% | {"market_freshness": 38, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 5, "mapping": 1} | 7.91 | 0.2359 / 0.2297 (431) | 23.7% | 1.3% | 1.4% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.7% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 15 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 16 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 17 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 18 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 19 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 20 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 21 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 22 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 23 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 24 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 25 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 26 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 27 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 30 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 31 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 32 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 36 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 37 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 38 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 39 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 41 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 42 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 43 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 44 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 45 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 46 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 47 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 134 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 48 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 20.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 1255 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 49 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 50 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9706, "by_level_share_of_ge_25pp": {"ATP": 0.0177, "CHALLENGER": 0.1233, "DOUBLES": 0.0691, "ITF_MEN": 0.311, "ITF_WOMEN": 0.4491, "OTHER": 0.0012, "WTA": 0.0118, "WTA125": 0.0169}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5101, "share_primary_cause_market_settled_or_in_play": 0.4255, "share_primary_cause_stale_quote_only": 0.1812}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 10279, "identity_ambiguous_share": 0.2169, "ticker_orientation": {"VERIFIED": 10279}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6471, "with_external": 329, "coverage": 0.0508, "external_status": {"EXTERNAL_STALE": 199, "AGREES_WITH_KALSHI": 122, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 199, "MODEL_LONE_OUTLIER": 122, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3708, "share_external_supports_model": 0.0243}, "pregame_clean_ge_25pp": {"n": 3196, "with_external": 309, "coverage": 0.0967, "external_status": {"EXTERNAL_STALE": 185, "AGREES_WITH_KALSHI": 116, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 185, "MODEL_LONE_OUTLIER": 116, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3754, "share_external_supports_model": 0.0259}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 494.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 224.0, "share_severe_asymmetry": 0.2108, "data_status": {"POOR": 5710, "LIMITED": 2785, "ADEQUATE": 1784}, "comparison_lt_10pp": {"median_thinner_serve_points": 1704.0, "median_sample_ratio": 1.7, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 776, "model_minus_observed": 0.0459, "kalshi_minus_observed": -0.0906, "brier_diff_model_minus_kalshi": -0.003}, "4-10x": {"n": 530, "model_minus_observed": 0.0887, "kalshi_minus_observed": -0.0568, "brier_diff_model_minus_kalshi": 0.0119}, "<2x": {"n": 1905, "model_minus_observed": 0.0864, "kalshi_minus_observed": -0.0368, "brier_diff_model_minus_kalshi": 0.0122}, ">=10x": {"n": 669, "model_minus_observed": 0.1019, "kalshi_minus_observed": -0.0733, "brier_diff_model_minus_kalshi": 0.004}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3880, "model": {"intercept": -0.532, "slope": 0.852, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.239, "slope": 1.117, "slope_se": 0.047}, "mean_extremity_model": 0.1704, "mean_extremity_kalshi": 0.165, "model_brier": 0.2319, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.027, "brier_diff_se": 0.0031, "model_logloss": 0.6601, "kalshi_logloss": 0.5925}, "fair_v1": {"n": 3880, "model": {"intercept": -0.394, "slope": 1.053, "slope_se": 0.046}, "kalshi_mid_same_rows": {"intercept": 0.33, "slope": 1.162, "slope_se": 0.048}, "mean_extremity_model": 0.1674, "mean_extremity_kalshi": 0.1645, "model_brier": 0.2129, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0077, "brier_diff_se": 0.0025, "model_logloss": 0.6138, "kalshi_logloss": 0.5928}, "gen1_elo": {"n": 3880, "model": {"intercept": -0.387, "slope": 1.029, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.325, "slope": 1.145, "slope_se": 0.047}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1647, "model_brier": 0.212, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0068, "brier_diff_se": 0.0025, "model_logloss": 0.6127, "kalshi_logloss": 0.593}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2433, "share_ge_15": 0.4434, "median_abs_gap": 13.12, "n": 26598}, "gen1_elo": {"share_ge_25": 0.2409, "share_ge_15": 0.4406, "median_abs_gap": 12.86, "n": 26598}, "gen1_sr": {"share_ge_25": 0.3097, "share_ge_15": 0.5233, "median_abs_gap": 15.93, "n": 26598}, "gen2": {"share_ge_25": 0.3118, "share_ge_15": 0.5116, "median_abs_gap": 15.52, "n": 26598}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1539, "share_ge_15": 0.3616, "median_abs_gap": 10.98, "n": 20759}, "gen1_elo": {"share_ge_25": 0.1551, "share_ge_15": 0.3564, "median_abs_gap": 10.57, "n": 20757}, "gen1_sr": {"share_ge_25": 0.2201, "share_ge_15": 0.4487, "median_abs_gap": 13.25, "n": 20760}, "gen2": {"share_ge_25": 0.2353, "share_ge_15": 0.4475, "median_abs_gap": 13.17, "n": 20760}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0498, "share_ge_25_pregame_clean": 0.0459}, "WTA": {"median_abs_gap_pregame_clean": 7.91, "share_ge_25_all": 0.046, "share_ge_25_pregame_clean": 0.0418}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2363, "share_within_10pp_all": 0.4334, "share_within_10pp_pregame_clean": 0.4846, "corr_model_vs_mid_pregame_clean": 0.8443}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 573, "model_brier": 0.1962, "kalshi_brier": 0.1976, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 676, "model_brier": 0.2122, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.009}, "15-25": {"n_settled": 876, "model_brier": 0.2239, "kalshi_brier": 0.2142, "brier_diff_model_minus_kalshi": 0.0097}, "25-40": {"n_settled": 494, "model_brier": 0.2233, "kalshi_brier": 0.2112, "brier_diff_model_minus_kalshi": 0.0121}, "3-5": {"n_settled": 365, "model_brier": 0.1996, "kalshi_brier": 0.1994, "brier_diff_model_minus_kalshi": 0.0001}, "40+": {"n_settled": 99, "model_brier": 0.2917, "kalshi_brier": 0.1892, "brier_diff_model_minus_kalshi": 0.1024}, "5-10": {"n_settled": 797, "model_brier": 0.2031, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": 0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.532, "slope": 0.852, "slope_se": 0.042}, "kalshi_slope": {"intercept": 0.239, "slope": 1.117, "slope_se": 0.047}, "n": 3880}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.51, "slope": 0.877, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.161, "slope": 1.084, "slope_se": 0.036}, "n": 5910}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 372, "model_brier": 0.3195, "kalshi_brier": 0.2349, "brier_diff_model_minus_kalshi": 0.0846, "brier_diff_se": 0.0161, "corr_model_outcome": 0.0184, "corr_kalshi_outcome": 0.2558}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
