# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-18T16:42Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 39,072): 0-3 14.5%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 18.9%, 25-40 13.7%, 40+ 8.2%; median gap 11.86 pp.
* **Where the extremes live**: 97.6% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.7%, Challenger 12.3%, doubles 7.4%). Main tour: ATP 3.3% and WTA 5.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,522): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.4%, BOOK_QUALITY 19.1%, STALE_QUOTE 17.8%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 35.4%, execution 19.1%, market_freshness 17.8%, data 12.4%, market_freshness/coverage 8.5%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%.
* **Stale / settled / in-play**: 52.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,522 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.0% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 541.0 points vs 1834.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.053, Gen-2 0.839, Gen-1 ledger 0.88 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 397 model 0.2201 vs Kalshi 0.2082; n 82 model 0.3038 vs Kalshi 0.1718.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 162,990 model-market comparisons (266,096 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 58,616 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-18T16:30:32.735939+00:00'], shadow board 43,184 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-18T16:30:37.790711+00:00'], Model 4 19,093 rows, 16,074 settled tickers, 5,450 tickers with an external scan.
* By model: {"gen1_ledger": 39538, "gen1_elo": 21717, "fair_v1": 21717, "gen2": 21717, "gen1_sr": 21717, "model4_fundamental": 18299, "model4_conditioned": 18285}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 39,072 | 14.5 | 9.6 | 19.9 | 15.4 | 18.9 | 13.7 | 8.2 | 11.86 | 40.7% | 21.8% |
| MW fair_v1 | 21,717 | 13.6 | 8.5 | 18.5 | 15.9 | 19.2 | 14.5 | 9.8 | 12.95 | 43.5% | 24.3% |
| MW gen1_elo | 21,717 | 13.1 | 9.1 | 19.5 | 15.2 | 19.4 | 14.3 | 9.4 | 12.52 | 43.1% | 23.7% |
| MW gen1_ledger | 17,355 | 15.6 | 10.8 | 21.6 | 14.8 | 18.5 | 12.6 | 6.2 | 10.48 | 37.2% | 18.7% |
| MW gen1_sr | 21,717 | 9.7 | 7.4 | 16.7 | 14.3 | 21.5 | 18.4 | 12.0 | 15.68 | 51.9% | 30.4% |
| MW gen2 | 21,717 | 11.5 | 7.1 | 16.5 | 14.2 | 19.9 | 17.5 | 13.2 | 15.37 | 50.7% | 30.8% |
| all families model4_conditioned | 18,285 | 21.7 | 19.0 | 34.5 | 17.3 | 4.7 | 1.5 | 1.2 | 5.94 | 7.4% | 2.7% |
| all families model4_fundamental | 18,299 | 16.2 | 13.0 | 34.7 | 20.1 | 11.1 | 3.4 | 1.4 | 7.87 | 16.0% | 4.9% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.2%, >=25pp 21.8%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.17pp; >=10pp 44.5%, >=25pp 16.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,799 | 29.5 | 13.3 | 24.4 | 17.2 | 11.7 | 3.2 | 0.7 | 6.17 | 15.6% | 3.9% |
| CHALLENGER | 3,601 | 15.9 | 10.1 | 20.3 | 15.7 | 14.4 | 12.4 | 11.2 | 11.17 | 38.0% | 23.6% |
| ITF_MEN | 5,924 | 11.0 | 8.0 | 17.4 | 14.9 | 19.9 | 16.3 | 12.5 | 14.52 | 48.6% | 28.7% |
| ITF_WOMEN | 8,478 | 10.2 | 6.8 | 15.8 | 15.6 | 22.3 | 18.2 | 11.1 | 15.61 | 51.6% | 29.3% |
| WTA | 1,255 | 19.0 | 12.3 | 25.3 | 18.8 | 19.1 | 4.7 | 0.9 | 8.18 | 24.7% | 5.6% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,799 | 23.7 | 14.3 | 24.5 | 18.1 | 14.1 | 4.3 | 1.0 | 6.9 | 19.4% | 5.3% |
| CHALLENGER | 3,601 | 14.8 | 8.1 | 19.0 | 13.6 | 18.1 | 14.3 | 12.1 | 12.77 | 44.5% | 26.4% |
| ITF_MEN | 5,924 | 9.3 | 6.7 | 15.7 | 13.6 | 19.8 | 19.3 | 15.6 | 16.99 | 54.7% | 34.9% |
| ITF_WOMEN | 8,478 | 8.5 | 5.6 | 13.7 | 13.6 | 21.1 | 20.7 | 16.9 | 18.82 | 58.7% | 37.6% |
| WTA | 1,255 | 17.2 | 7.9 | 20.2 | 16.3 | 22.6 | 14.7 | 1.0 | 11.55 | 38.3% | 15.7% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,799 | 25.4 | 13.7 | 25.6 | 17.0 | 13.6 | 4.0 | 0.7 | 6.62 | 18.3% | 4.7% |
| CHALLENGER | 3,601 | 14.9 | 10.2 | 20.7 | 15.0 | 15.6 | 12.1 | 11.5 | 11.09 | 39.2% | 23.6% |
| ITF_MEN | 5,924 | 10.0 | 8.1 | 17.8 | 14.2 | 20.8 | 16.7 | 12.4 | 14.98 | 49.9% | 29.1% |
| ITF_WOMEN | 8,478 | 9.6 | 7.0 | 16.4 | 15.6 | 22.9 | 18.3 | 10.3 | 15.57 | 51.5% | 28.6% |
| WTA | 1,255 | 23.6 | 17.1 | 30.8 | 15.1 | 11.0 | 1.9 | 0.6 | 6.0 | 13.5% | 2.5% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,113 | 27.8 | 20.2 | 31.8 | 11.6 | 6.3 | 2.2 | 0.1 | 5.22 | 8.6% | 2.3% |
| CHALLENGER | 2,512 | 22.2 | 15.3 | 26.6 | 14.2 | 14.0 | 5.8 | 1.9 | 7.04 | 21.8% | 7.8% |
| DOUBLES | 1,289 | 4.7 | 4.3 | 10.2 | 10.9 | 21.0 | 25.7 | 23.1 | 24.11 | 69.8% | 48.8% |
| ITF_MEN | 4,963 | 14.5 | 8.7 | 20.7 | 15.8 | 21.0 | 12.4 | 7.0 | 11.86 | 40.4% | 19.4% |
| ITF_WOMEN | 5,677 | 11.8 | 9.1 | 19.1 | 14.8 | 22.1 | 16.9 | 6.2 | 13.17 | 45.1% | 23.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 920 | 22.6 | 15.8 | 29.4 | 17.5 | 10.4 | 4.0 | 0.3 | 6.81 | 14.8% | 4.3% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,763 | 29.7 | 13.4 | 24.7 | 17.0 | 11.6 | 2.9 | 0.7 | 6.04 | 15.1% | 3.6% |
| CHALLENGER | 2,584 | 20.5 | 12.6 | 25.4 | 18.1 | 14.8 | 6.4 | 2.2 | 8.23 | 23.4% | 8.6% |
| ITF_MEN | 4,290 | 13.6 | 9.9 | 20.8 | 16.9 | 20.2 | 13.1 | 5.5 | 11.54 | 38.8% | 18.6% |
| ITF_WOMEN | 6,345 | 12.1 | 8.1 | 18.0 | 17.7 | 23.8 | 15.3 | 5.0 | 13.3 | 44.1% | 20.3% |
| WTA | 1,229 | 19.1 | 11.8 | 25.4 | 18.9 | 19.3 | 4.6 | 0.9 | 8.22 | 24.8% | 5.5% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,763 | 23.8 | 14.5 | 24.6 | 18.1 | 13.9 | 4.1 | 0.8 | 6.81 | 18.9% | 5.0% |
| CHALLENGER | 2,584 | 18.9 | 10.4 | 23.6 | 16.2 | 18.7 | 9.6 | 2.6 | 9.2 | 30.9% | 12.2% |
| ITF_MEN | 4,291 | 11.0 | 8.0 | 18.1 | 15.4 | 22.0 | 17.0 | 8.4 | 14.11 | 47.3% | 25.4% |
| ITF_WOMEN | 6,345 | 9.4 | 6.3 | 15.2 | 15.0 | 23.2 | 20.1 | 10.7 | 16.57 | 54.1% | 30.9% |
| WTA | 1,229 | 17.1 | 7.8 | 20.3 | 16.4 | 22.6 | 14.9 | 1.0 | 11.64 | 38.5% | 15.9% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,081 | 27.9 | 20.4 | 32.1 | 11.8 | 5.7 | 2.0 | 0.1 | 5.11 | 7.9% | 2.1% |
| CHALLENGER | 2,174 | 23.8 | 16.6 | 28.4 | 14.0 | 13.3 | 3.3 | 0.6 | 6.42 | 17.2% | 3.9% |
| DOUBLES | 1,196 | 4.8 | 4.5 | 10.3 | 11.1 | 20.9 | 25.8 | 22.6 | 24.07 | 69.3% | 48.4% |
| ITF_MEN | 4,104 | 15.9 | 9.4 | 22.6 | 16.7 | 20.7 | 10.6 | 4.1 | 10.59 | 35.4% | 14.7% |
| ITF_WOMEN | 4,692 | 12.6 | 9.8 | 20.7 | 15.6 | 22.3 | 15.6 | 3.4 | 11.9 | 41.3% | 19.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 881 | 22.9 | 16.2 | 29.6 | 17.5 | 10.6 | 3.2 | 0.0 | 6.68 | 13.7% | 3.2% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,289 | 4.7 | 4.3 | 10.2 | 10.9 | 21.0 | 25.7 | 23.1 | 24.11 | 69.8% | 48.8% |
| singles | 16,066 | 16.5 | 11.3 | 22.5 | 15.1 | 18.3 | 11.5 | 4.8 | 9.9 | 34.5% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,002 | 13.5 | 8.9 | 19.3 | 15.9 | 18.1 | 14.5 | 9.8 | 12.67 | 42.5% | 24.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 14,014 | 13.9 | 8.5 | 18.4 | 15.5 | 19.6 | 14.4 | 9.7 | 12.96 | 43.7% | 24.1% |
| UNKNOWN | 2,464 | 12.1 | 7.7 | 17.4 | 18.2 | 18.9 | 15.6 | 10.1 | 13.14 | 44.6% | 25.7% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,386 | 19.9 | 10.8 | 21.3 | 17.3 | 15.8 | 8.7 | 6.2 | 9.41 | 30.7% | 14.9% |
| B | 2,804 | 13.3 | 9.2 | 19.9 | 16.5 | 18.4 | 12.0 | 10.7 | 12.11 | 41.1% | 22.8% |
| C | 3,156 | 12.8 | 9.3 | 19.5 | 14.4 | 19.2 | 14.9 | 9.9 | 12.77 | 44.0% | 24.8% |
| D | 3,653 | 12.4 | 7.9 | 17.1 | 15.6 | 21.9 | 15.6 | 9.6 | 13.92 | 47.0% | 25.1% |
| F | 5,718 | 7.9 | 5.6 | 15.0 | 15.0 | 21.9 | 21.5 | 13.2 | 17.66 | 56.6% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,114 | 23.4 | 15.9 | 28.8 | 15.2 | 11.2 | 4.1 | 1.5 | 6.61 | 16.7% | 5.5% |
| B | 2,476 | 15.3 | 10.1 | 23.9 | 16.4 | 19.2 | 11.0 | 4.1 | 10.14 | 34.3% | 15.1% |
| C | 3,501 | 11.4 | 7.7 | 17.6 | 14.2 | 21.6 | 16.4 | 11.2 | 14.59 | 49.2% | 27.6% |
| D | 2,530 | 14.1 | 10.0 | 20.3 | 13.8 | 20.8 | 14.5 | 6.6 | 12.04 | 41.9% | 21.1% |
| F | 3,734 | 10.2 | 7.9 | 14.9 | 14.3 | 23.4 | 20.3 | 8.9 | 16.19 | 52.7% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,238 | 18.0 | 9.8 | 20.5 | 17.1 | 16.2 | 9.6 | 8.7 | 10.46 | 34.6% | 18.3% |
| LIMITED | 4,925 | 14.5 | 10.4 | 20.5 | 15.3 | 18.6 | 13.1 | 7.4 | 11.36 | 39.2% | 20.6% |
| POOR | 9,554 | 9.7 | 6.6 | 15.9 | 15.3 | 21.8 | 19.0 | 11.7 | 15.92 | 52.5% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,288 | 27.2 | 22.0 | 35.1 | 10.9 | 3.5 | 1.1 | 0.2 | 5.06 | 4.8% | 1.3% |
| GAME_SPREAD | 3,747 | 24.1 | 15.5 | 34.5 | 17.4 | 6.8 | 1.5 | 0.2 | 6.31 | 8.5% | 1.7% |
| MATCH_WINNER | 17,355 | 15.6 | 10.8 | 21.6 | 14.8 | 18.5 | 12.6 | 6.2 | 10.48 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,051 | 30.6 | 17.9 | 30.5 | 12.2 | 7.2 | 1.2 | 0.4 | 5.16 | 8.9% | 1.6% |
| TOTAL_GAMES | 6,073 | 7.1 | 8.8 | 37.1 | 28.8 | 11.4 | 3.6 | 3.1 | 9.65 | 18.2% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,415 | 25.1 | 34.9 | 32.2 | 3.5 | 3.6 | 0.7 | 0.2 | 4.46 | 4.4% | 0.8% |
| GAME_SPREAD | 4,412 | 46.0 | 16.8 | 27.5 | 7.2 | 1.7 | 0.7 | 0.3 | 3.45 | 2.6% | 0.9% |
| TOTAL_GAMES | 7,458 | 4.4 | 6.7 | 40.8 | 35.2 | 7.5 | 2.7 | 2.5 | 9.81 | 12.8% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,416 | 24.6 | 17.6 | 36.0 | 11.7 | 7.1 | 2.6 | 0.4 | 5.8 | 10.0% | 2.9% |
| GAME_SPREAD | 4,414 | 19.4 | 13.6 | 28.8 | 20.0 | 13.7 | 3.7 | 0.9 | 7.85 | 18.3% | 4.6% |
| TOTAL_GAMES | 7,469 | 7.2 | 8.6 | 37.0 | 27.3 | 13.1 | 4.0 | 2.7 | 9.69 | 19.8% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 21,717 | 43.5% | 24.3% | 12.95 | 34.8% | 15.0% | 10.65 |
| gen1_elo | 21,717 | 43.1% | 23.7% | 12.52 | 34.1% | 14.8% | 10.18 |
| gen1_sr | 21,717 | 51.9% | 30.4% | 15.68 | 44.1% | 21.1% | 13.07 |
| gen2 | 21,717 | 50.7% | 30.8% | 15.37 | 44.0% | 22.7% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 11,585 | 16.4 | 10.4 | 21.4 | 17.4 | 19.6 | 11.4 | 3.3 | 10.5 | 34.3% | 14.7% |
| STALE | 10,132 | 10.3 | 6.4 | 15.1 | 14.1 | 18.8 | 18.1 | 17.1 | 17.12 | 54.1% | 35.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 10,823 | 17.1 | 11.6 | 22.7 | 14.8 | 17.2 | 11.6 | 4.9 | 9.62 | 33.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 39,072 | 10823 | 15057 | 13192 | 23.7 | 140.5 | 1400.4 |
| ge_15pp | 15,901 | 3652 | 5262 | 6987 | 25.8 | 442.6 | 1380.4 |
| ge_25pp | 8,522 | 1785 | 2292 | 4445 | 32.8 | 581.6 | 1380.4 |
| lt_10pp | 17,156 | 5571 | 7224 | 4361 | 21.8 | 47.8 | 1341.5 |

Current slate `SL-20261018T164219Z-89f3c723`: 773 priced rows, quote age at build {'median': 12.1, 'max': 12.1}, freshness {'AGING': 773}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,004 | 21.2 | 10.7 | 23.3 | 19.1 | 18.5 | 6.7 | 0.5 | 8.66 | 25.7% | 7.2% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 350 | 70.6 | 29.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.06 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 715 | 0.0 | 2.9 | 35.2 | 28.5 | 23.4 | 9.2 | 0.7 | 11.98 | 33.3% | 9.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 21,717 | 3103 (14.3%) | 23.0% | 0.7% | {"EXTERNAL_STALE": 2004, "AGREES_WITH_KALSHI": 715, "ALL_AGREE": 350, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 9,450 | 762 (8.1%) | 31.2% | 1.2% | {"EXTERNAL_STALE": 515, "AGREES_WITH_KALSHI": 238, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,275 | 218 (4.1%) | 32.6% | 1.4% | {"EXTERNAL_STALE": 144, "AGREES_WITH_KALSHI": 71, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,531 | 206 (8.1%) | 33.5% | 1.5% | {"EXTERNAL_STALE": 134, "AGREES_WITH_KALSHI": 69, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,816 | 1755 (19.9%) | 15.6% | 0.7% | {"EXTERNAL_STALE": 1107, "ALL_AGREE": 350, "AGREES_WITH_KALSHI": 273, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,179 | 11.3 | 7.8 | 19.3 | 15.0 | 21.4 | 15.1 | 10.1 | 13.79 | 46.6% | 25.2% |
| 4-10x | 2,810 | 12.5 | 8.9 | 19.1 | 15.7 | 19.3 | 15.2 | 9.4 | 12.92 | 43.8% | 24.5% |
| <2x | 11,303 | 15.6 | 9.3 | 19.0 | 16.9 | 17.7 | 12.7 | 8.8 | 11.75 | 39.3% | 21.5% |
| >=10x | 3,425 | 10.8 | 6.5 | 15.3 | 13.9 | 21.4 | 19.5 | 12.6 | 16.36 | 53.5% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,644 | 13.1 | 8.5 | 19.4 | 15.9 | 19.6 | 13.2 | 10.3 | 12.82 | 43.1% | 23.5% |
| 300-1000 | 4,818 | 12.3 | 8.7 | 17.1 | 15.8 | 20.6 | 16.1 | 9.4 | 13.69 | 46.1% | 25.6% |
| <300 | 6,512 | 9.0 | 6.0 | 15.5 | 14.9 | 21.8 | 20.1 | 12.8 | 16.81 | 54.6% | 32.9% |
| >=3000 | 4,743 | 21.6 | 11.9 | 22.9 | 17.4 | 14.0 | 6.9 | 5.2 | 8.23 | 26.1% | 12.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 658 | 0.5404 | 0.4062 | 0.4863 | +0.054 | -0.080 | 0.0006 ± 0.0058 |
| ratio 4-10x | 440 | 0.5863 | 0.4472 | 0.5091 | +0.077 | -0.062 | 0.0078 ± 0.0074 |
| ratio <2x | 1650 | 0.5377 | 0.4164 | 0.4497 | +0.088 | -0.033 | 0.0129 ± 0.0035 |
| ratio >=10x | 549 | 0.5559 | 0.3846 | 0.4353 | +0.121 | -0.051 | 0.0137 ± 0.0077 |
| thinner_sample 1000-3000 | 926 | 0.5435 | 0.4176 | 0.4611 | +0.082 | -0.044 | 0.0083 ± 0.0047 |
| thinner_sample 300-1000 | 776 | 0.5626 | 0.4234 | 0.4897 | +0.073 | -0.066 | 0.0022 ± 0.0056 |
| thinner_sample <300 | 1021 | 0.5496 | 0.3875 | 0.4437 | +0.106 | -0.056 | 0.0148 ± 0.0054 |
| thinner_sample >=3000 | 574 | 0.5312 | 0.438 | 0.4617 | +0.070 | -0.024 | 0.0143 ± 0.0048 |
| data_status ADEQUATE | 973 | 0.5339 | 0.4294 | 0.4553 | +0.079 | -0.026 | 0.0112 ± 0.004 |
| data_status LIMITED | 821 | 0.5539 | 0.424 | 0.4872 | +0.067 | -0.063 | 0.0044 ± 0.0051 |
| data_status POOR | 1503 | 0.5534 | 0.3968 | 0.4538 | +0.100 | -0.057 | 0.0121 ± 0.0044 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 507 | 0.1945 | 0.1958 | -0.0013 ± 0.0007 | 0.5675 | 0.5702 | 0.4952 | 0.4804 | 0.5286 | -0.049 ± 0.0205 | -0.01 (5) |
| 3-5 | 320 | 0.1976 | 0.1971 | +0.0005 ± 0.002 | 0.5769 | 0.5744 | 0.5067 | 0.4668 | 0.4813 | -0.081 ± 0.0254 | 0.02 (1) |
| 5-10 | 687 | 0.1992 | 0.1987 | +0.0005 ± 0.0026 | 0.5841 | 0.5811 | 0.5114 | 0.4369 | 0.4658 | -0.086 ± 0.0176 | -0.0167 (6) |
| 10-15 | 586 | 0.2154 | 0.2055 | +0.0099 ± 0.0047 | 0.6209 | 0.593 | 0.5212 | 0.397 | 0.4181 | -0.093 ± 0.0188 | -0.048 (5) |
| 15-25 | 718 | 0.2289 | 0.2129 | +0.0161 ± 0.0067 | 0.652 | 0.611 | 0.5793 | 0.3843 | 0.4415 | -0.089 ± 0.0172 | -0.0033 (9) |
| 25-40 | 397 | 0.2201 | 0.2082 | +0.0119 ± 0.0136 | 0.628 | 0.5989 | 0.6513 | 0.3429 | 0.4786 | -0.060 ± 0.0205 | -0.01 (1) |
| 40+ | 82 | 0.3038 | 0.1718 | +0.1320 ± 0.0413 | 0.8184 | 0.5163 | 0.7489 | 0.299 | 0.378 | -0.123 ± 0.0397 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2393 | 0.1812 | 0.1824 | -0.0011 ± 0.0003 | 0.5374 | 0.5385 | 0.4792 | 0.4641 | 0.5002 | -0.020 ± 0.0088 | -0.0129 (17) |
| 3-5 | 1503 | 0.194 | 0.1919 | +0.0021 ± 0.0009 | 0.5687 | 0.5595 | 0.4798 | 0.4401 | 0.4325 | -0.065 ± 0.0115 | 0.0 (2) |
| 5-10 | 3207 | 0.1948 | 0.1918 | +0.0029 ± 0.0012 | 0.5722 | 0.5626 | 0.4836 | 0.4097 | 0.4247 | -0.049 ± 0.0079 | -0.0119 (21) |
| 10-15 | 2861 | 0.2024 | 0.1833 | +0.0192 ± 0.002 | 0.5927 | 0.5389 | 0.4821 | 0.3572 | 0.3432 | -0.077 ± 0.008 | -0.0281 (16) |
| 15-25 | 3454 | 0.2088 | 0.1706 | +0.0382 ± 0.0028 | 0.6093 | 0.5049 | 0.502 | 0.3058 | 0.3078 | -0.070 ± 0.007 | -0.0025 (44) |
| 25-40 | 2678 | 0.2214 | 0.1254 | +0.0960 ± 0.0043 | 0.6361 | 0.3872 | 0.5302 | 0.2169 | 0.2244 | -0.064 ± 0.0066 | -0.01 (1) |
| 40+ | 1819 | 0.3785 | 0.0421 | +0.3364 ± 0.0054 | 0.9848 | 0.1681 | 0.6278 | 0.1059 | 0.055 | -0.087 ± 0.0045 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 375 | 0.1996 | 0.2001 | -0.0005 ± 0.0008 | 0.5809 | 0.5821 | 0.5016 | 0.4866 | 0.5093 | -0.079 ± 0.0244 | -0.01 (3) |
| 3-5 | 272 | 0.2156 | 0.2151 | +0.0005 ± 0.0023 | 0.6145 | 0.6143 | 0.5164 | 0.4765 | 0.4853 | -0.087 ± 0.0296 | 0.02 (1) |
| 5-10 | 597 | 0.1995 | 0.1991 | +0.0004 ± 0.0028 | 0.5827 | 0.5818 | 0.5477 | 0.4729 | 0.5075 | -0.074 ± 0.0188 | -0.01 (4) |
| 10-15 | 543 | 0.2192 | 0.2117 | +0.0075 ± 0.0049 | 0.629 | 0.6096 | 0.5678 | 0.4435 | 0.4788 | -0.095 ± 0.0207 | -0.04 (5) |
| 15-25 | 791 | 0.2286 | 0.2077 | +0.0209 ± 0.0064 | 0.6486 | 0.5977 | 0.5888 | 0.3925 | 0.4412 | -0.091 ± 0.0164 | -0.0133 (9) |
| 25-40 | 525 | 0.2679 | 0.1955 | +0.0724 ± 0.0122 | 0.7463 | 0.5714 | 0.6614 | 0.3465 | 0.3905 | -0.122 ± 0.0191 | -0.0075 (4) |
| 40+ | 194 | 0.3662 | 0.1769 | +0.1892 ± 0.03 | 1.0198 | 0.5248 | 0.7424 | 0.2589 | 0.3196 | -0.073 ± 0.0291 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2013 | 0.1849 | 0.1854 | -0.0005 ± 0.0003 | 0.5457 | 0.5467 | 0.5027 | 0.488 | 0.5107 | -0.033 ± 0.0099 | -0.0133 (15) |
| 3-5 | 1278 | 0.1963 | 0.1951 | +0.0011 ± 0.001 | 0.5684 | 0.5655 | 0.5165 | 0.4766 | 0.482 | -0.048 ± 0.0126 | 0.02 (1) |
| 5-10 | 2868 | 0.1922 | 0.1895 | +0.0026 ± 0.0012 | 0.567 | 0.5576 | 0.5091 | 0.4351 | 0.4557 | -0.042 ± 0.0082 | -0.0117 (6) |
| 10-15 | 2507 | 0.1998 | 0.1888 | +0.0110 ± 0.0022 | 0.5883 | 0.5503 | 0.5196 | 0.395 | 0.4156 | -0.049 ± 0.0088 | -0.0189 (18) |
| 15-25 | 3595 | 0.2169 | 0.1773 | +0.0396 ± 0.0028 | 0.6287 | 0.5228 | 0.5308 | 0.3347 | 0.3352 | -0.073 ± 0.0071 | -0.0086 (42) |
| 25-40 | 3170 | 0.2505 | 0.1345 | +0.1159 ± 0.0041 | 0.7072 | 0.4142 | 0.5597 | 0.2437 | 0.2199 | -0.091 ± 0.0065 | -0.0044 (18) |
| 40+ | 2484 | 0.4024 | 0.0657 | +0.3368 ± 0.0059 | 1.0625 | 0.2299 | 0.6628 | 0.1251 | 0.0942 | -0.070 ± 0.005 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 493 | 0.1968 | 0.1993 | -0.0024 ± 0.0007 | 0.5742 | 0.5799 | 0.4989 | 0.4836 | 0.5517 | -0.016 ± 0.0205 | -0.0137 (8) |
| 3-5 | 358 | 0.1913 | 0.1892 | +0.0021 ± 0.0019 | 0.5596 | 0.5548 | 0.4985 | 0.4588 | 0.4553 | -0.113 ± 0.0241 | 0.0067 (3) |
| 5-10 | 717 | 0.202 | 0.198 | +0.0040 ± 0.0025 | 0.5912 | 0.5783 | 0.5045 | 0.4307 | 0.4379 | -0.098 ± 0.0171 | -0.0071 (7) |
| 10-15 | 572 | 0.2093 | 0.2063 | +0.0030 ± 0.0047 | 0.6067 | 0.5958 | 0.5389 | 0.4159 | 0.4685 | -0.074 ± 0.0188 | -0.0317 (6) |
| 15-25 | 668 | 0.2345 | 0.2102 | +0.0243 ± 0.0069 | 0.6683 | 0.6047 | 0.5885 | 0.3951 | 0.4281 | -0.111 ± 0.0176 | -0.03 (1) |
| 25-40 | 408 | 0.2074 | 0.2138 | -0.0064 ± 0.0133 | 0.6002 | 0.6115 | 0.6567 | 0.3472 | 0.5098 | -0.041 ± 0.0202 | 0.015 (2) |
| 40+ | 81 | 0.3193 | 0.1853 | +0.1340 ± 0.0433 | 0.8559 | 0.5469 | 0.7515 | 0.2974 | 0.3827 | -0.106 ± 0.0441 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2298 | 0.1886 | 0.1895 | -0.0009 ± 0.0003 | 0.5542 | 0.5559 | 0.4875 | 0.4721 | 0.497 | -0.029 ± 0.0091 | -0.0163 (35) |
| 3-5 | 1572 | 0.1874 | 0.1841 | +0.0034 ± 0.0009 | 0.5524 | 0.5442 | 0.4775 | 0.438 | 0.4167 | -0.082 ± 0.0111 | -0.0094 (18) |
| 5-10 | 3417 | 0.1952 | 0.1884 | +0.0069 ± 0.0011 | 0.5755 | 0.5532 | 0.4816 | 0.4077 | 0.3963 | -0.071 ± 0.0075 | -0.01 (31) |
| 10-15 | 2685 | 0.1964 | 0.18 | +0.0164 ± 0.002 | 0.5778 | 0.5294 | 0.4977 | 0.3743 | 0.3702 | -0.070 ± 0.0081 | -0.015 (12) |
| 15-25 | 3569 | 0.2085 | 0.1699 | +0.0386 ± 0.0027 | 0.6105 | 0.5036 | 0.5061 | 0.3112 | 0.3099 | -0.071 ± 0.0069 | -0.03 (2) |
| 25-40 | 2625 | 0.2166 | 0.1238 | +0.0928 ± 0.0043 | 0.6252 | 0.382 | 0.527 | 0.211 | 0.2263 | -0.059 ± 0.0065 | 0.01 (3) |
| 40+ | 1749 | 0.3933 | 0.0466 | +0.3468 ± 0.0058 | 1.0252 | 0.1801 | 0.639 | 0.1107 | 0.0583 | -0.088 ± 0.0049 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 834 | 0.1963 | 0.1964 | -0.0001 ± 0.0005 | 0.5733 | 0.5732 | 0.5081 | 0.4931 | 0.4952 | -0.055 ± 0.0154 | -0.0224 (49) |
| 3-5 | 586 | 0.1945 | 0.1938 | +0.0007 ± 0.0015 | 0.5673 | 0.5643 | 0.4804 | 0.4405 | 0.4488 | -0.051 ± 0.0183 | -0.0194 (34) |
| 5-10 | 1232 | 0.1989 | 0.1925 | +0.0064 ± 0.0019 | 0.5853 | 0.5671 | 0.4891 | 0.4157 | 0.4099 | -0.069 ± 0.0128 | -0.005 (78) |
| 10-15 | 783 | 0.2072 | 0.196 | +0.0112 ± 0.004 | 0.6025 | 0.5737 | 0.509 | 0.3859 | 0.401 | -0.058 ± 0.0159 | 0.0014 (64) |
| 15-25 | 1048 | 0.2341 | 0.212 | +0.0221 ± 0.0056 | 0.6665 | 0.6103 | 0.5678 | 0.3728 | 0.4151 | -0.060 ± 0.0143 | -0.0214 (59) |
| 25-40 | 613 | 0.245 | 0.1977 | +0.0473 ± 0.011 | 0.6932 | 0.5737 | 0.6534 | 0.341 | 0.4192 | -0.079 ± 0.0166 | -0.0219 (26) |
| 40+ | 211 | 0.362 | 0.1918 | +0.1702 ± 0.0305 | 1.0452 | 0.5644 | 0.7987 | 0.3099 | 0.4028 | -0.079 ± 0.0268 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2580 | 0.1878 | 0.1879 | -0.0001 ± 0.0003 | 0.5508 | 0.55 | 0.5047 | 0.4894 | 0.4977 | -0.037 ± 0.0085 | -0.0157 (88) |
| 3-5 | 1764 | 0.1894 | 0.187 | +0.0024 ± 0.0008 | 0.5543 | 0.5487 | 0.4859 | 0.4462 | 0.4365 | -0.056 ± 0.0104 | -0.0209 (69) |
| 5-10 | 3538 | 0.195 | 0.1865 | +0.0085 ± 0.0011 | 0.575 | 0.5513 | 0.4848 | 0.4113 | 0.3932 | -0.070 ± 0.0074 | -0.0082 (132) |
| 10-15 | 2412 | 0.2042 | 0.189 | +0.0152 ± 0.0022 | 0.5961 | 0.5562 | 0.5143 | 0.3913 | 0.3905 | -0.060 ± 0.0088 | -0.0053 (105) |
| 15-25 | 3004 | 0.2298 | 0.1982 | +0.0317 ± 0.0032 | 0.6618 | 0.5763 | 0.56 | 0.3644 | 0.3828 | -0.061 ± 0.0082 | -0.0253 (107) |
| 25-40 | 2018 | 0.2509 | 0.1703 | +0.0806 ± 0.0058 | 0.7115 | 0.5036 | 0.6122 | 0.2982 | 0.3295 | -0.074 ± 0.0088 | -0.0229 (51) |
| 40+ | 965 | 0.3848 | 0.131 | +0.2538 ± 0.0124 | 1.0901 | 0.401 | 0.7137 | 0.2083 | 0.2238 | -0.074 ± 0.0109 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3297 | 1.053 ± 0.049 | 1.17 | 0.1678 | 0.1679 | 0.2128 | 0.2029 |
| gen2 | 3297 | 0.839 ± 0.044 | 1.131 | 0.1737 | 0.1679 | 0.2318 | 0.2028 |
| gen1_elo | 3297 | 1.04 ± 0.048 | 1.156 | 0.1735 | 0.1683 | 0.2115 | 0.2028 |
| gen1_sr | 3297 | 1.037 ± 0.058 | 1.194 | 0.1339 | 0.1696 | 0.2277 | 0.2026 |
| gen1_ledger | 5307 | 0.88 ± 0.034 | 1.081 | 0.1779 | 0.183 | 0.218 | 0.1982 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 15,901)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,810 | 24.0% |
| STALE_QUOTE | market_freshness | 3,247 | 20.4% |
| BOOK_QUALITY | execution | 3,091 | 19.4% |
| POOR_DATA | data | 1,742 | 11.0% |
| LIMITED_DATA | data | 1,095 | 6.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 844 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 773 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 640 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 451 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 208 | 1.3% |

Cause class: coverage 24.0%, market_freshness 20.4%, execution 19.4%, data 17.8%, market_freshness/coverage 8.1%, model_calibration_or_unknown 4.9%, mapping 4.0%, model_calibration 1.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.7%, START_UNVERIFIABLE 94.8%, LOW_DATA_QUALITY 69.7%, THIN_PLAYER_HISTORY 57.9%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 43.9%, MODEL_INTERNAL_DISAGREEMENT 40.1%, ASYMMETRIC_SAMPLE_SIZE 32.1%, WIDE_SPREAD 25.4%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 14.9%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.5%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.2%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.4%, POST_SETTLEMENT_OBSERVATION 24.0%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,522)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,014 | 35.4% |
| BOOK_QUALITY | execution | 1,631 | 19.1% |
| STALE_QUOTE | market_freshness | 1,516 | 17.8% |
| POOR_DATA | data | 734 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 448 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 365 | 4.3% |
| LIMITED_DATA | data | 325 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 279 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 165 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 45 | 0.5% |

Cause class: coverage 35.4%, execution 19.1%, market_freshness 17.8%, data 12.4%, market_freshness/coverage 8.5%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.7%, START_UNVERIFIABLE 97.6%, LOW_DATA_QUALITY 73.6%, THIN_PLAYER_HISTORY 60.4%, STALE_KALSHI_QUOTE 52.2%, STALE_PLAYER_DATA 47.4%, MODEL_INTERNAL_DISAGREEMENT 41.0%, ASYMMETRIC_SAMPLE_SIZE 33.9%, WIDE_SPREAD 25.3%, PLAYER_IDENTITY_RISK 18.1%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 10.2%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.2%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.2%, POST_SETTLEMENT_OBSERVATION 35.4%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6761, "IDENTITY_AMBIGUOUS": 1761}; ticker orientation: {"VERIFIED": 8522}.

Checks: discipline:AMBIGUOUS 629, discipline:PASS 7893, identity_confidence:AMBIGUOUS 1547, identity_confidence:PASS 6975, level_mapping:NA 641, level_mapping:PASS 7881, market_pair:AMBIGUOUS 299, market_pair:NA 211, market_pair:PASS 8012, model_complement:NA 178, model_complement:PASS 8344, namesake:PASS 8522, physical_match_id:NA 3247, physical_match_id:PASS 5275, player_ids:PASS 8522, same_pair_other_event:PASS 8522, ticker_orientation:PASS 8522

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,912 | 3.3% | 3.0% | 1.1% | {"market_freshness": 34, "data": 24, "execution": 13, "model_calibration_or_unknown": 10, "market_freshness/coverage": 8, "model_calibration": 5, "coverage": 2} | 5.64 | 0.2118 / 0.2073 (319) | 17.2% | 2.9% | 4.3% | 2.3% |
| CHALLENGER | 6,113 | 17.1% | 6.5% | 12.3% | {"coverage": 606, "market_freshness/coverage": 133, "market_freshness": 130, "data": 88, "model_calibration_or_unknown": 46, "execution": 24, "model_calibration": 10, "mapping": 9} | 7.2 | 0.2176 / 0.2051 (1532) | 36.1% | 13.8% | 2.9% | 22.2% |
| DOUBLES | 1,289 | 48.8% | 48.4% | 7.4% | {"execution": 305, "mapping": 168, "market_freshness": 106, "market_freshness/coverage": 43, "coverage": 7} | 24.07 | 0.324 / 0.2339 (337) | 18.1% | 0.0% | 100.0% | 7.2% |
| ITF_MEN | 10,887 | 24.5% | 16.7% | 31.3% | {"coverage": 1052, "execution": 538, "market_freshness": 407, "data": 357, "market_freshness/coverage": 214, "mapping": 94, "model_calibration_or_unknown": 2} | 11.12 | 0.2138 / 0.1947 (2656) | 36.3% | 61.8% | 13.2% | 22.9% |
| ITF_WOMEN | 14,155 | 26.8% | 19.8% | 44.5% | {"coverage": 1330, "market_freshness": 763, "execution": 721, "data": 556, "market_freshness/coverage": 280, "mapping": 88, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.76 | 0.2023 / 0.1926 (2865) | 38.4% | 57.6% | 10.2% | 22.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,175 | 5.1% | 4.5% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 16, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.58 | 0.2413 / 0.234 (365) | 23.2% | 1.6% | 1.7% | 3.0% |
| WTA125 | 1,392 | 12.5% | 9.9% | 2.0% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 34 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 35 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 36 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 37 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 38 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 39 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 42 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 44 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 45 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 46 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 47 | `KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF` | DOUBLES | gen1_ledger | 90% / 15% | +75 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 49 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 50 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9757, "by_level_share_of_ge_25pp": {"ATP": 0.0113, "CHALLENGER": 0.1227, "DOUBLES": 0.0738, "ITF_MEN": 0.3126, "ITF_WOMEN": 0.4448, "OTHER": 0.0014, "WTA": 0.0129, "WTA125": 0.0204}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5216, "share_primary_cause_market_settled_or_in_play": 0.439, "share_primary_cause_stale_quote_only": 0.1779}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8522, "identity_ambiguous_share": 0.2066, "ticker_orientation": {"VERIFIED": 8522}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5275, "with_external": 218, "coverage": 0.0413, "external_status": {"EXTERNAL_STALE": 144, "AGREES_WITH_KALSHI": 71, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 144, "MODEL_LONE_OUTLIER": 71, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3257, "share_external_supports_model": 0.0138}, "pregame_clean_ge_25pp": {"n": 2531, "with_external": 206, "coverage": 0.0814, "external_status": {"EXTERNAL_STALE": 134, "AGREES_WITH_KALSHI": 69, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 134, "MODEL_LONE_OUTLIER": 69, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.335, "share_external_supports_model": 0.0146}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 541.0, "median_sample_ratio": 2.43, "median_min_matches": 21.0, "median_max_days_since_last": 213.0, "share_severe_asymmetry": 0.2056, "data_status": {"POOR": 4578, "LIMITED": 2432, "ADEQUATE": 1512}, "comparison_lt_10pp": {"median_thinner_serve_points": 1834.0, "median_sample_ratio": 1.67, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 658, "model_minus_observed": 0.0541, "kalshi_minus_observed": -0.0801, "brier_diff_model_minus_kalshi": 0.0006}, "4-10x": {"n": 440, "model_minus_observed": 0.0772, "kalshi_minus_observed": -0.0619, "brier_diff_model_minus_kalshi": 0.0078}, "<2x": {"n": 1650, "model_minus_observed": 0.088, "kalshi_minus_observed": -0.0333, "brier_diff_model_minus_kalshi": 0.0129}, ">=10x": {"n": 549, "model_minus_observed": 0.1206, "kalshi_minus_observed": -0.0507, "brier_diff_model_minus_kalshi": 0.0137}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3297, "model": {"intercept": -0.539, "slope": 0.839, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.223, "slope": 1.131, "slope_se": 0.051}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1679, "model_brier": 0.2318, "kalshi_brier": 0.2028, "brier_diff_model_minus_kalshi": 0.029, "brier_diff_se": 0.0033, "model_logloss": 0.6603, "kalshi_logloss": 0.5879}, "fair_v1": {"n": 3297, "model": {"intercept": -0.412, "slope": 1.053, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.3, "slope": 1.17, "slope_se": 0.052}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1679, "model_brier": 0.2128, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": 0.0099, "brier_diff_se": 0.0026, "model_logloss": 0.6133, "kalshi_logloss": 0.5879}, "gen1_elo": {"n": 3297, "model": {"intercept": -0.403, "slope": 1.04, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.295, "slope": 1.156, "slope_se": 0.051}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.1683, "model_brier": 0.2115, "kalshi_brier": 0.2028, "brier_diff_model_minus_kalshi": 0.0087, "brier_diff_se": 0.0026, "model_logloss": 0.6111, "kalshi_logloss": 0.5877}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2429, "share_ge_15": 0.4351, "median_abs_gap": 12.95, "n": 21717}, "gen1_elo": {"share_ge_25": 0.2372, "share_ge_15": 0.4311, "median_abs_gap": 12.52, "n": 21717}, "gen1_sr": {"share_ge_25": 0.3045, "share_ge_15": 0.5193, "median_abs_gap": 15.68, "n": 21717}, "gen2": {"share_ge_25": 0.3076, "share_ge_15": 0.507, "median_abs_gap": 15.37, "n": 21717}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1502, "share_ge_15": 0.348, "median_abs_gap": 10.65, "n": 16845}, "gen1_elo": {"share_ge_25": 0.1482, "share_ge_15": 0.3406, "median_abs_gap": 10.18, "n": 16844}, "gen1_sr": {"share_ge_25": 0.2114, "share_ge_15": 0.4414, "median_abs_gap": 13.07, "n": 16845}, "gen2": {"share_ge_25": 0.2268, "share_ge_15": 0.4397, "median_abs_gap": 13.0, "n": 16846}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.64, "share_ge_25_all": 0.033, "share_ge_25_pregame_clean": 0.0302}, "WTA": {"median_abs_gap_pregame_clean": 7.58, "share_ge_25_all": 0.0506, "share_ge_25_pregame_clean": 0.0455}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2404, "share_within_10pp_all": 0.4391, "share_within_10pp_pregame_clean": 0.4941, "corr_model_vs_mid_pregame_clean": 0.8424}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 507, "model_brier": 0.1945, "kalshi_brier": 0.1958, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 586, "model_brier": 0.2154, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.0099}, "15-25": {"n_settled": 718, "model_brier": 0.2289, "kalshi_brier": 0.2129, "brier_diff_model_minus_kalshi": 0.0161}, "25-40": {"n_settled": 397, "model_brier": 0.2201, "kalshi_brier": 0.2082, "brier_diff_model_minus_kalshi": 0.0119}, "3-5": {"n_settled": 320, "model_brier": 0.1976, "kalshi_brier": 0.1971, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 82, "model_brier": 0.3038, "kalshi_brier": 0.1718, "brier_diff_model_minus_kalshi": 0.132}, "5-10": {"n_settled": 687, "model_brier": 0.1992, "kalshi_brier": 0.1987, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.539, "slope": 0.839, "slope_se": 0.044}, "kalshi_slope": {"intercept": 0.223, "slope": 1.131, "slope_se": 0.051}, "n": 3297}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.519, "slope": 0.88, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.144, "slope": 1.081, "slope_se": 0.038}, "n": 5307}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 337, "model_brier": 0.324, "kalshi_brier": 0.2339, "brier_diff_model_minus_kalshi": 0.0902, "brier_diff_se": 0.0171, "corr_model_outcome": 0.0142, "corr_kalshi_outcome": 0.2577}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
