# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-21T18:17Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 47,873): 0-3 14.1%, 3-5 9.4%, 5-10 19.7%, 10-15 15.3%, 15-25 19.4%, 25-40 14.1%, 40+ 8.1%; median gap 12.12 pp.
* **Where the extremes live**: 97.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.4%, Challenger 12.1%, doubles 6.8%). Main tour: ATP 5.0% and WTA 4.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 10,616): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.4%, BOOK_QUALITY 18.6%, STALE_QUOTE 18.0%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, LIMITED_DATA 3.7%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%. By class: coverage 34.4%, execution 18.6%, market_freshness 18.0%, data 12.7%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%.
* **Stale / settled / in-play**: 51.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 10,616 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1685.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.052, Gen-2 0.851, Gen-1 ledger 0.873 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 510 model 0.2243 vs Kalshi 0.2103; n 104 model 0.2868 vs Kalshi 0.1908.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 204,966 model-market comparisons (333,489 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 69,485 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-21T18:04:31.635468+00:00'], shadow board 54,366 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-21T18:04:37.805609+00:00'], Model 4 25,751 rows, 18,475 settled tickers, 6,393 tickers with an external scan.
* By model: {"gen1_ledger": 46939, "gen1_elo": 27339, "fair_v1": 27339, "gen2": 27339, "gen1_sr": 27339, "model4_fundamental": 24349, "model4_conditioned": 24322}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 47,873 | 14.1 | 9.4 | 19.7 | 15.3 | 19.4 | 14.1 | 8.1 | 12.12 | 41.6% | 22.2% |
| MW fair_v1 | 27,339 | 13.0 | 8.5 | 18.3 | 15.6 | 19.9 | 15.0 | 9.7 | 13.21 | 44.6% | 24.7% |
| MW gen1_elo | 27,339 | 12.9 | 8.6 | 18.9 | 15.1 | 20.0 | 15.0 | 9.4 | 13.0 | 44.4% | 24.4% |
| MW gen1_ledger | 20,534 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.9 | 6.0 | 10.57 | 37.5% | 18.8% |
| MW gen1_sr | 27,339 | 9.9 | 7.1 | 16.5 | 13.9 | 21.2 | 18.8 | 12.6 | 16.02 | 52.6% | 31.4% |
| MW gen2 | 27,339 | 11.0 | 7.2 | 16.2 | 14.2 | 19.8 | 17.9 | 13.8 | 15.6 | 51.4% | 31.6% |
| all families model4_conditioned | 24,322 | 21.8 | 19.2 | 34.5 | 17.7 | 4.4 | 1.4 | 1.0 | 5.95 | 6.9% | 2.5% |
| all families model4_fundamental | 24,349 | 16.5 | 13.1 | 34.0 | 20.4 | 11.1 | 3.5 | 1.3 | 7.85 | 15.9% | 4.8% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.8%, >=15pp 41.6%, >=20pp 30.9%, >=25pp 22.2%, >=30pp 15.9%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.46pp; >=10pp 45.4%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,368 | 28.8 | 14.0 | 24.2 | 14.7 | 12.4 | 5.2 | 0.7 | 6.17 | 18.3% | 5.9% |
| CHALLENGER | 4,390 | 15.7 | 10.0 | 20.3 | 15.7 | 14.8 | 12.5 | 11.0 | 11.18 | 38.3% | 23.5% |
| ITF_MEN | 7,413 | 10.6 | 7.5 | 16.8 | 14.6 | 21.4 | 17.2 | 11.9 | 15.17 | 50.5% | 29.1% |
| ITF_WOMEN | 10,879 | 9.5 | 6.9 | 15.7 | 15.5 | 22.7 | 18.3 | 11.5 | 15.8 | 52.4% | 29.8% |
| WTA | 1,629 | 17.0 | 12.7 | 25.4 | 20.0 | 19.7 | 4.5 | 0.7 | 8.47 | 24.9% | 5.2% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,368 | 23.6 | 14.8 | 24.8 | 17.1 | 13.8 | 5.1 | 1.0 | 6.72 | 19.8% | 6.0% |
| CHALLENGER | 4,390 | 14.7 | 8.4 | 18.7 | 14.7 | 17.5 | 14.0 | 11.9 | 12.68 | 43.5% | 25.9% |
| ITF_MEN | 7,413 | 8.7 | 6.2 | 14.5 | 13.2 | 19.9 | 20.3 | 17.3 | 18.15 | 57.5% | 37.6% |
| ITF_WOMEN | 10,879 | 8.1 | 5.6 | 13.7 | 13.5 | 21.0 | 21.0 | 17.1 | 18.92 | 59.1% | 38.1% |
| WTA | 1,629 | 14.4 | 9.6 | 21.1 | 16.5 | 23.9 | 13.8 | 0.7 | 11.28 | 38.4% | 14.5% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,368 | 24.3 | 12.8 | 24.0 | 15.9 | 14.9 | 7.0 | 1.2 | 7.3 | 23.1% | 8.2% |
| CHALLENGER | 4,390 | 14.2 | 9.5 | 20.8 | 15.2 | 16.4 | 12.8 | 11.2 | 11.42 | 40.4% | 24.0% |
| ITF_MEN | 7,413 | 10.0 | 7.5 | 17.0 | 14.0 | 21.9 | 17.5 | 12.1 | 15.51 | 51.5% | 29.6% |
| ITF_WOMEN | 10,879 | 9.6 | 6.6 | 16.2 | 15.5 | 23.1 | 18.4 | 10.6 | 15.77 | 52.1% | 29.1% |
| WTA | 1,629 | 24.4 | 16.7 | 29.6 | 16.3 | 10.2 | 2.3 | 0.4 | 6.04 | 13.0% | 2.8% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,361 | 25.9 | 19.3 | 30.6 | 11.9 | 8.9 | 3.1 | 0.4 | 5.53 | 12.3% | 3.5% |
| CHALLENGER | 3,042 | 21.3 | 14.9 | 26.7 | 14.0 | 14.7 | 6.6 | 1.9 | 7.27 | 23.2% | 8.5% |
| DOUBLES | 1,508 | 5.4 | 4.2 | 11.6 | 10.2 | 20.8 | 26.3 | 21.6 | 24.05 | 68.6% | 47.9% |
| ITF_MEN | 5,768 | 13.8 | 8.8 | 20.2 | 15.9 | 21.2 | 13.3 | 6.7 | 12.14 | 41.3% | 20.1% |
| ITF_WOMEN | 6,946 | 12.7 | 9.0 | 19.3 | 15.1 | 21.6 | 16.3 | 6.1 | 12.87 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,028 | 22.3 | 15.9 | 29.6 | 18.2 | 10.1 | 3.6 | 0.3 | 6.97 | 14.0% | 3.9% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,304 | 29.2 | 14.2 | 24.6 | 14.6 | 12.2 | 4.7 | 0.5 | 6.0 | 17.4% | 5.2% |
| CHALLENGER | 3,102 | 20.5 | 12.3 | 25.0 | 18.2 | 15.2 | 6.7 | 2.0 | 8.36 | 24.0% | 8.8% |
| ITF_MEN | 5,446 | 12.8 | 9.0 | 20.1 | 16.5 | 22.3 | 14.1 | 5.1 | 12.32 | 41.5% | 19.2% |
| ITF_WOMEN | 8,124 | 11.2 | 8.2 | 17.9 | 17.7 | 24.5 | 15.3 | 5.1 | 13.51 | 45.0% | 20.5% |
| WTA | 1,582 | 17.3 | 12.5 | 25.4 | 20.2 | 19.7 | 4.2 | 0.7 | 8.46 | 24.6% | 4.9% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,304 | 23.9 | 15.1 | 24.9 | 16.9 | 13.8 | 4.7 | 0.7 | 6.5 | 19.1% | 5.4% |
| CHALLENGER | 3,102 | 18.5 | 10.7 | 23.3 | 17.6 | 17.8 | 9.8 | 2.3 | 9.41 | 29.8% | 12.1% |
| ITF_MEN | 5,447 | 10.3 | 7.4 | 16.7 | 15.0 | 21.8 | 18.6 | 10.2 | 15.34 | 50.6% | 28.8% |
| ITF_WOMEN | 8,125 | 9.1 | 6.5 | 15.1 | 15.0 | 23.1 | 20.5 | 10.8 | 16.58 | 54.3% | 31.3% |
| WTA | 1,582 | 14.5 | 9.6 | 21.1 | 16.4 | 23.9 | 13.8 | 0.8 | 11.28 | 38.4% | 14.5% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,320 | 26.1 | 19.6 | 30.7 | 12.1 | 8.4 | 3.0 | 0.2 | 5.41 | 11.6% | 3.2% |
| CHALLENGER | 2,650 | 22.8 | 16.0 | 28.3 | 13.9 | 14.0 | 4.5 | 0.6 | 6.7 | 19.1% | 5.1% |
| DOUBLES | 1,403 | 5.3 | 4.3 | 11.8 | 10.4 | 20.8 | 26.2 | 21.1 | 23.85 | 68.1% | 47.3% |
| ITF_MEN | 4,817 | 15.0 | 9.5 | 21.9 | 16.7 | 21.1 | 11.6 | 4.2 | 11.12 | 36.9% | 15.8% |
| ITF_WOMEN | 5,780 | 13.6 | 9.5 | 20.6 | 15.9 | 21.8 | 15.1 | 3.4 | 11.73 | 40.4% | 18.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 978 | 22.8 | 16.5 | 29.6 | 18.2 | 10.1 | 2.9 | 0.0 | 6.82 | 13.0% | 2.9% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,508 | 5.4 | 4.2 | 11.6 | 10.2 | 20.8 | 26.3 | 21.6 | 24.05 | 68.6% | 47.9% |
| singles | 19,026 | 16.2 | 11.2 | 22.3 | 15.2 | 18.5 | 11.8 | 4.7 | 10.04 | 35.0% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 6,122 | 13.2 | 8.8 | 18.9 | 15.7 | 18.9 | 14.9 | 9.6 | 12.92 | 43.4% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 17,101 | 13.3 | 8.5 | 18.3 | 15.3 | 20.1 | 14.8 | 9.6 | 13.21 | 44.5% | 24.4% |
| UNKNOWN | 3,879 | 11.3 | 7.8 | 17.0 | 17.1 | 20.6 | 15.9 | 10.3 | 13.77 | 46.8% | 26.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,670 | 19.7 | 11.6 | 21.2 | 16.5 | 15.8 | 9.0 | 6.2 | 9.22 | 30.9% | 15.1% |
| B | 3,436 | 12.5 | 9.0 | 19.9 | 16.9 | 19.1 | 12.2 | 10.4 | 12.27 | 41.7% | 22.6% |
| C | 3,846 | 11.7 | 8.9 | 19.1 | 14.9 | 19.6 | 15.3 | 10.4 | 13.36 | 45.4% | 25.8% |
| D | 4,448 | 12.1 | 7.8 | 17.0 | 15.6 | 21.8 | 15.8 | 9.9 | 14.04 | 47.5% | 25.7% |
| F | 7,939 | 7.8 | 5.5 | 15.0 | 14.6 | 23.4 | 21.4 | 12.4 | 17.85 | 57.1% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,769 | 23.0 | 15.8 | 28.8 | 15.0 | 11.8 | 4.1 | 1.5 | 6.68 | 17.3% | 5.6% |
| B | 2,832 | 16.3 | 10.5 | 23.4 | 16.1 | 19.1 | 10.7 | 3.9 | 9.95 | 33.7% | 14.6% |
| C | 4,059 | 11.4 | 7.3 | 18.4 | 14.2 | 21.4 | 16.5 | 10.7 | 14.27 | 48.6% | 27.2% |
| D | 2,934 | 14.4 | 9.8 | 19.8 | 14.4 | 21.0 | 14.4 | 6.1 | 12.04 | 41.6% | 20.5% |
| F | 4,940 | 10.1 | 8.1 | 15.5 | 14.7 | 22.8 | 20.4 | 8.4 | 15.87 | 51.6% | 28.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 8,747 | 17.9 | 10.4 | 20.5 | 16.5 | 16.3 | 9.8 | 8.6 | 10.37 | 34.7% | 18.4% |
| LIMITED | 5,938 | 13.5 | 10.2 | 20.2 | 15.6 | 19.2 | 13.6 | 7.7 | 11.91 | 40.5% | 21.3% |
| POOR | 12,654 | 9.4 | 6.4 | 15.8 | 15.0 | 22.8 | 19.2 | 11.5 | 16.17 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,219 | 26.6 | 20.4 | 34.3 | 12.2 | 4.8 | 1.5 | 0.2 | 5.28 | 6.4% | 1.7% |
| GAME_SPREAD | 4,492 | 22.5 | 15.2 | 33.5 | 17.1 | 9.0 | 2.4 | 0.3 | 6.65 | 11.6% | 2.6% |
| MATCH_WINNER | 20,534 | 15.4 | 10.7 | 21.5 | 14.8 | 18.7 | 12.9 | 6.0 | 10.57 | 37.5% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 9,443 | 29.5 | 16.9 | 30.8 | 12.5 | 8.2 | 1.7 | 0.4 | 5.45 | 10.3% | 2.1% |
| TOTAL_GAMES | 7,227 | 8.4 | 9.5 | 36.5 | 29.0 | 10.7 | 3.3 | 2.7 | 9.53 | 16.7% | 6.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,500 | 25.3 | 34.2 | 32.5 | 4.2 | 3.0 | 0.6 | 0.2 | 4.48 | 3.8% | 0.7% |
| GAME_SPREAD | 5,821 | 45.6 | 17.1 | 26.9 | 7.6 | 1.8 | 0.8 | 0.2 | 3.46 | 2.8% | 1.0% |
| TOTAL_GAMES | 10,001 | 4.8 | 7.6 | 40.6 | 35.0 | 7.2 | 2.5 | 2.2 | 9.71 | 12.0% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,503 | 24.2 | 17.9 | 35.5 | 12.4 | 7.2 | 2.5 | 0.3 | 5.81 | 10.1% | 2.9% |
| GAME_SPREAD | 5,824 | 19.3 | 13.2 | 28.0 | 20.1 | 14.0 | 4.5 | 0.9 | 7.97 | 19.4% | 5.3% |
| TOTAL_GAMES | 10,022 | 8.3 | 9.1 | 36.4 | 27.4 | 12.7 | 3.8 | 2.4 | 9.58 | 18.9% | 6.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 27,339 | 44.6% | 24.7% | 13.21 | 36.2% | 15.4% | 10.98 |
| gen1_elo | 27,339 | 44.4% | 24.4% | 13.0 | 35.8% | 15.6% | 10.66 |
| gen1_sr | 27,339 | 52.6% | 31.4% | 16.02 | 44.9% | 22.1% | 13.25 |
| gen2 | 27,339 | 51.4% | 31.6% | 15.6 | 44.8% | 23.7% | 13.18 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 14,154 | 15.8 | 10.3 | 21.1 | 17.2 | 20.4 | 11.9 | 3.3 | 10.81 | 35.6% | 15.2% |
| STALE | 13,185 | 10.0 | 6.6 | 15.3 | 13.9 | 19.4 | 18.3 | 16.6 | 17.08 | 54.3% | 34.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,002 | 16.5 | 11.2 | 22.4 | 14.9 | 17.8 | 12.3 | 4.9 | 9.96 | 35.0% | 17.2% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 47,873 | 14002 | 17626 | 16245 | 23.9 | 135.1 | 1400.4 |
| ge_15pp | 19,896 | 4899 | 6332 | 8665 | 25.7 | 424.7 | 1380.4 |
| ge_25pp | 10,616 | 2402 | 2745 | 5469 | 31.4 | 567.1 | 1380.4 |
| lt_10pp | 20,663 | 7022 | 8308 | 5333 | 21.8 | 47.5 | 1341.5 |

Current slate `SL-20261021T181708Z-fae2089e`: 544 priced rows, quote age at build {'median': 12.9, 'max': 12.9}, freshness {'AGING': 544}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 22 | 0.0 | 0.0 | 22.7 | 4.5 | 40.9 | 31.8 | 0.0 | 20.48 | 72.7% | 31.8% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,522 | 19.7 | 10.8 | 23.7 | 18.8 | 18.9 | 7.3 | 0.8 | 9.1 | 27.0% | 8.1% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 481 | 65.9 | 34.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.23 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,069 | 0.0 | 2.2 | 34.1 | 25.9 | 26.0 | 10.8 | 0.8 | 12.77 | 37.7% | 11.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 27,339 | 4123 (15.1%) | 25.9% | 0.9% | {"EXTERNAL_STALE": 2522, "AGREES_WITH_KALSHI": 1069, "ALL_AGREE": 481, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 12, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 12,198 | 1102 (9.0%) | 36.6% | 1.6% | {"EXTERNAL_STALE": 681, "AGREES_WITH_KALSHI": 403, "SUPPORTS_MODEL_DIRECTION": 16, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 6,752 | 336 (5.0%) | 37.2% | 2.4% | {"EXTERNAL_STALE": 203, "AGREES_WITH_KALSHI": 125, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,275 | 313 (9.6%) | 37.7% | 2.6% | {"EXTERNAL_STALE": 187, "AGREES_WITH_KALSHI": 118, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 10,872 | 2269 (20.9%) | 17.1% | 0.8% | {"EXTERNAL_STALE": 1367, "ALL_AGREE": 481, "AGREES_WITH_KALSHI": 389, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 12, "SUPPORTS_MODEL_DIRECTION": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,214 | 10.6 | 7.7 | 19.3 | 14.4 | 22.2 | 15.9 | 9.9 | 14.09 | 48.1% | 25.8% |
| 4-10x | 3,581 | 11.1 | 8.4 | 18.7 | 15.5 | 21.1 | 14.9 | 10.2 | 13.77 | 46.3% | 25.2% |
| <2x | 13,932 | 15.0 | 9.6 | 18.8 | 16.6 | 18.0 | 13.2 | 8.8 | 11.97 | 40.0% | 22.0% |
| >=10x | 4,612 | 11.1 | 6.3 | 15.1 | 14.1 | 22.1 | 19.4 | 11.8 | 16.28 | 53.2% | 31.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 6,890 | 12.3 | 8.5 | 19.4 | 16.2 | 19.6 | 13.6 | 10.3 | 12.98 | 43.6% | 23.9% |
| 300-1000 | 5,941 | 11.7 | 8.8 | 16.9 | 15.3 | 20.8 | 16.5 | 10.0 | 14.03 | 47.3% | 26.5% |
| <300 | 8,877 | 8.9 | 5.7 | 15.3 | 14.8 | 23.0 | 20.1 | 12.1 | 16.92 | 55.3% | 32.3% |
| >=3000 | 5,631 | 21.6 | 12.8 | 22.8 | 16.5 | 14.5 | 6.9 | 4.8 | 8.01 | 26.2% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 788 | 0.5461 | 0.4087 | 0.5 | +0.046 | -0.091 | -0.0039 ± 0.0055 |
| ratio 4-10x | 546 | 0.5835 | 0.4382 | 0.4908 | +0.093 | -0.053 | 0.0133 ± 0.0069 |
| ratio <2x | 1953 | 0.536 | 0.4121 | 0.446 | +0.090 | -0.034 | 0.0124 ± 0.0032 |
| ratio >=10x | 697 | 0.5653 | 0.3896 | 0.4591 | +0.106 | -0.070 | 0.0065 ± 0.0069 |
| thinner_sample 1000-3000 | 1079 | 0.5411 | 0.4135 | 0.4486 | +0.092 | -0.035 | 0.0102 ± 0.0044 |
| thinner_sample 300-1000 | 925 | 0.5639 | 0.421 | 0.493 | +0.071 | -0.072 | 0.0006 ± 0.0053 |
| thinner_sample <300 | 1322 | 0.5544 | 0.3884 | 0.4592 | +0.095 | -0.071 | 0.0098 ± 0.0049 |
| thinner_sample >=3000 | 658 | 0.5342 | 0.4386 | 0.465 | +0.069 | -0.026 | 0.0131 ± 0.0046 |
| data_status ADEQUATE | 1132 | 0.5365 | 0.4301 | 0.4523 | +0.084 | -0.022 | 0.0125 ± 0.0037 |
| data_status LIMITED | 946 | 0.5491 | 0.4163 | 0.4778 | +0.071 | -0.061 | 0.0043 ± 0.0049 |
| data_status POOR | 1906 | 0.5577 | 0.3971 | 0.4664 | +0.091 | -0.069 | 0.0078 ± 0.004 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 585 | 0.1978 | 0.199 | -0.0012 ± 0.0006 | 0.5745 | 0.5769 | 0.498 | 0.4831 | 0.5316 | -0.056 ± 0.0192 | -0.01 (5) |
| 3-5 | 373 | 0.2018 | 0.2011 | +0.0007 ± 0.0019 | 0.5871 | 0.5839 | 0.5014 | 0.4613 | 0.4718 | -0.096 ± 0.0239 | 0.02 (1) |
| 5-10 | 813 | 0.2022 | 0.2017 | +0.0006 ± 0.0024 | 0.5904 | 0.5868 | 0.5115 | 0.437 | 0.4662 | -0.089 ± 0.0164 | -0.0167 (6) |
| 10-15 | 690 | 0.2126 | 0.2034 | +0.0092 ± 0.0043 | 0.6147 | 0.588 | 0.5236 | 0.3996 | 0.4232 | -0.101 ± 0.0171 | -0.048 (5) |
| 15-25 | 909 | 0.2232 | 0.2127 | +0.0105 ± 0.0059 | 0.6409 | 0.6091 | 0.5742 | 0.3785 | 0.4499 | -0.084 ± 0.0151 | -0.0033 (9) |
| 25-40 | 510 | 0.2243 | 0.2103 | +0.0140 ± 0.0121 | 0.6368 | 0.6041 | 0.6554 | 0.3456 | 0.4745 | -0.071 ± 0.0186 | -0.01 (1) |
| 40+ | 104 | 0.2868 | 0.1908 | +0.0961 ± 0.0376 | 0.7842 | 0.5653 | 0.7516 | 0.3041 | 0.4231 | -0.092 ± 0.0368 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2955 | 0.1832 | 0.1842 | -0.0010 ± 0.0003 | 0.5406 | 0.5416 | 0.4842 | 0.4691 | 0.5036 | -0.022 ± 0.008 | -0.0129 (17) |
| 3-5 | 1949 | 0.1985 | 0.197 | +0.0014 ± 0.0008 | 0.5777 | 0.5709 | 0.4842 | 0.4443 | 0.4454 | -0.056 ± 0.0102 | 0.0 (2) |
| 5-10 | 4139 | 0.1978 | 0.1949 | +0.0029 ± 0.001 | 0.5782 | 0.5686 | 0.4815 | 0.4076 | 0.4243 | -0.045 ± 0.007 | -0.0119 (21) |
| 10-15 | 3590 | 0.2005 | 0.1826 | +0.0179 ± 0.0018 | 0.5878 | 0.5372 | 0.4842 | 0.3597 | 0.3499 | -0.073 ± 0.0071 | -0.0281 (16) |
| 15-25 | 4537 | 0.2065 | 0.1698 | +0.0367 ± 0.0024 | 0.606 | 0.5027 | 0.5004 | 0.304 | 0.3095 | -0.068 ± 0.0061 | -0.0025 (44) |
| 25-40 | 3523 | 0.2237 | 0.1303 | +0.0933 ± 0.0038 | 0.6416 | 0.3984 | 0.5312 | 0.2182 | 0.2285 | -0.061 ± 0.0059 | -0.01 (1) |
| 40+ | 2289 | 0.3796 | 0.0446 | +0.3350 ± 0.005 | 0.9885 | 0.1738 | 0.6314 | 0.1065 | 0.062 | -0.081 ± 0.0041 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 442 | 0.2037 | 0.2042 | -0.0005 ± 0.0008 | 0.5895 | 0.5904 | 0.504 | 0.489 | 0.5068 | -0.102 ± 0.0231 | -0.01 (3) |
| 3-5 | 324 | 0.2205 | 0.2192 | +0.0013 ± 0.0021 | 0.6261 | 0.6235 | 0.5118 | 0.4717 | 0.4691 | -0.108 ± 0.028 | 0.02 (1) |
| 5-10 | 703 | 0.2021 | 0.2028 | -0.0007 ± 0.0026 | 0.5885 | 0.5897 | 0.5441 | 0.4693 | 0.5121 | -0.073 ± 0.0174 | -0.01 (4) |
| 10-15 | 659 | 0.2164 | 0.2095 | +0.0069 ± 0.0045 | 0.6226 | 0.6049 | 0.5627 | 0.4386 | 0.475 | -0.102 ± 0.0185 | -0.04 (5) |
| 15-25 | 948 | 0.2294 | 0.2086 | +0.0208 ± 0.0058 | 0.6517 | 0.5991 | 0.5899 | 0.3937 | 0.443 | -0.100 ± 0.0151 | -0.0133 (9) |
| 25-40 | 662 | 0.2608 | 0.2007 | +0.0601 ± 0.011 | 0.7285 | 0.5831 | 0.6558 | 0.3401 | 0.4048 | -0.105 ± 0.0171 | -0.0075 (4) |
| 40+ | 246 | 0.3589 | 0.1731 | +0.1858 ± 0.0262 | 0.9917 | 0.5168 | 0.7336 | 0.2501 | 0.313 | -0.073 ± 0.0253 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2491 | 0.1938 | 0.194 | -0.0002 ± 0.0003 | 0.5651 | 0.5653 | 0.507 | 0.4921 | 0.509 | -0.041 ± 0.0092 | -0.0133 (15) |
| 3-5 | 1676 | 0.201 | 0.2007 | +0.0003 ± 0.0009 | 0.5806 | 0.5793 | 0.5104 | 0.4704 | 0.4857 | -0.038 ± 0.0112 | 0.02 (1) |
| 5-10 | 3685 | 0.193 | 0.1921 | +0.0009 ± 0.0011 | 0.5684 | 0.5623 | 0.5024 | 0.4285 | 0.4611 | -0.029 ± 0.0073 | -0.0117 (6) |
| 10-15 | 3235 | 0.1984 | 0.1877 | +0.0108 ± 0.0019 | 0.5838 | 0.5478 | 0.512 | 0.3879 | 0.4077 | -0.050 ± 0.0077 | -0.0189 (18) |
| 15-25 | 4580 | 0.215 | 0.1769 | +0.0381 ± 0.0025 | 0.626 | 0.5205 | 0.526 | 0.33 | 0.3336 | -0.070 ± 0.0063 | -0.0086 (42) |
| 25-40 | 4095 | 0.2501 | 0.1399 | +0.1102 ± 0.0037 | 0.7054 | 0.4273 | 0.5611 | 0.2444 | 0.232 | -0.080 ± 0.0058 | -0.0044 (18) |
| 40+ | 3220 | 0.3956 | 0.0631 | +0.3325 ± 0.0051 | 1.0424 | 0.2233 | 0.6547 | 0.1207 | 0.0894 | -0.069 ± 0.0043 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 557 | 0.197 | 0.1994 | -0.0024 ± 0.0007 | 0.5739 | 0.5795 | 0.4961 | 0.4809 | 0.553 | -0.017 ± 0.0193 | -0.0137 (8) |
| 3-5 | 403 | 0.1978 | 0.1958 | +0.0020 ± 0.0018 | 0.5744 | 0.5697 | 0.5025 | 0.4629 | 0.4591 | -0.117 ± 0.0229 | 0.0067 (3) |
| 5-10 | 844 | 0.2019 | 0.1985 | +0.0035 ± 0.0023 | 0.5909 | 0.5789 | 0.5092 | 0.4352 | 0.4467 | -0.100 ± 0.0158 | -0.0071 (7) |
| 10-15 | 694 | 0.2094 | 0.2061 | +0.0033 ± 0.0043 | 0.6064 | 0.595 | 0.5385 | 0.4153 | 0.4654 | -0.084 ± 0.0172 | -0.0317 (6) |
| 15-25 | 847 | 0.2309 | 0.2112 | +0.0197 ± 0.0061 | 0.6602 | 0.6052 | 0.5824 | 0.3886 | 0.4345 | -0.110 ± 0.0157 | -0.03 (1) |
| 25-40 | 530 | 0.2134 | 0.2172 | -0.0038 ± 0.0119 | 0.6142 | 0.6201 | 0.6654 | 0.3538 | 0.5132 | -0.050 ± 0.0182 | 0.015 (2) |
| 40+ | 109 | 0.2955 | 0.2042 | +0.0913 ± 0.038 | 0.81 | 0.5948 | 0.7583 | 0.3085 | 0.4404 | -0.074 ± 0.0392 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2871 | 0.1871 | 0.1878 | -0.0008 ± 0.0003 | 0.5488 | 0.5503 | 0.4909 | 0.4757 | 0.4946 | -0.034 ± 0.0081 | -0.0163 (35) |
| 3-5 | 1961 | 0.19 | 0.1875 | +0.0025 ± 0.0008 | 0.5578 | 0.5516 | 0.4851 | 0.4456 | 0.434 | -0.071 ± 0.01 | -0.0094 (18) |
| 5-10 | 4304 | 0.1958 | 0.19 | +0.0058 ± 0.001 | 0.5754 | 0.5562 | 0.4846 | 0.4107 | 0.408 | -0.062 ± 0.0067 | -0.01 (31) |
| 10-15 | 3438 | 0.1958 | 0.1794 | +0.0164 ± 0.0018 | 0.5758 | 0.5283 | 0.499 | 0.3755 | 0.3709 | -0.071 ± 0.0072 | -0.015 (12) |
| 15-25 | 4663 | 0.2103 | 0.172 | +0.0383 ± 0.0024 | 0.6149 | 0.5079 | 0.5085 | 0.3137 | 0.3127 | -0.072 ± 0.0061 | -0.03 (2) |
| 25-40 | 3517 | 0.2194 | 0.133 | +0.0864 ± 0.0039 | 0.6327 | 0.404 | 0.5352 | 0.2193 | 0.2428 | -0.051 ± 0.0059 | 0.01 (3) |
| 40+ | 2228 | 0.3941 | 0.0496 | +0.3445 ± 0.0053 | 1.0296 | 0.1868 | 0.6438 | 0.1131 | 0.0673 | -0.083 ± 0.0045 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 929 | 0.1951 | 0.1953 | -0.0002 ± 0.0005 | 0.5693 | 0.5695 | 0.5074 | 0.4923 | 0.4952 | -0.059 ± 0.0147 | -0.0224 (49) |
| 3-5 | 647 | 0.1915 | 0.1909 | +0.0005 ± 0.0014 | 0.5599 | 0.5575 | 0.485 | 0.4452 | 0.456 | -0.052 ± 0.0174 | -0.0194 (34) |
| 5-10 | 1371 | 0.1999 | 0.1935 | +0.0064 ± 0.0018 | 0.5884 | 0.5688 | 0.4942 | 0.4208 | 0.4158 | -0.073 ± 0.0121 | -0.005 (78) |
| 10-15 | 901 | 0.2091 | 0.1985 | +0.0106 ± 0.0037 | 0.6062 | 0.579 | 0.5169 | 0.3937 | 0.4107 | -0.063 ± 0.0151 | 0.0014 (64) |
| 15-25 | 1200 | 0.2313 | 0.2107 | +0.0205 ± 0.0052 | 0.6602 | 0.6068 | 0.5721 | 0.3773 | 0.4233 | -0.066 ± 0.0133 | -0.0214 (59) |
| 25-40 | 730 | 0.2484 | 0.2049 | +0.0434 ± 0.0103 | 0.7045 | 0.59 | 0.6658 | 0.3532 | 0.4384 | -0.084 ± 0.0157 | -0.0219 (26) |
| 40+ | 248 | 0.3521 | 0.1965 | +0.1557 ± 0.0279 | 1.0173 | 0.5747 | 0.8068 | 0.3228 | 0.4234 | -0.089 ± 0.0251 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3039 | 0.1835 | 0.1836 | -0.0001 ± 0.0003 | 0.5397 | 0.5392 | 0.5072 | 0.4918 | 0.4995 | -0.040 ± 0.0078 | -0.0157 (88) |
| 3-5 | 2086 | 0.1907 | 0.1887 | +0.0020 ± 0.0008 | 0.5576 | 0.5535 | 0.4902 | 0.4505 | 0.4453 | -0.054 ± 0.0096 | -0.0209 (69) |
| 5-10 | 4222 | 0.1976 | 0.1888 | +0.0088 ± 0.001 | 0.5805 | 0.5551 | 0.4896 | 0.4161 | 0.396 | -0.074 ± 0.0068 | -0.0082 (132) |
| 10-15 | 2913 | 0.2058 | 0.191 | +0.0148 ± 0.002 | 0.6001 | 0.5606 | 0.5233 | 0.4002 | 0.4006 | -0.061 ± 0.0081 | -0.0053 (105) |
| 15-25 | 3623 | 0.2282 | 0.198 | +0.0302 ± 0.0029 | 0.6588 | 0.5753 | 0.5649 | 0.3695 | 0.3911 | -0.064 ± 0.0074 | -0.0253 (107) |
| 25-40 | 2534 | 0.2586 | 0.1826 | +0.0760 ± 0.0054 | 0.7329 | 0.5335 | 0.6276 | 0.3132 | 0.352 | -0.076 ± 0.0083 | -0.0229 (51) |
| 40+ | 1146 | 0.3772 | 0.1429 | +0.2343 ± 0.0118 | 1.0706 | 0.4311 | 0.7283 | 0.2241 | 0.2565 | -0.071 ± 0.0105 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3984 | 1.052 ± 0.045 | 1.15 | 0.1675 | 0.1657 | 0.2132 | 0.2049 |
| gen2 | 3984 | 0.851 ± 0.041 | 1.11 | 0.1703 | 0.1661 | 0.2321 | 0.2046 |
| gen1_elo | 3984 | 1.027 ± 0.043 | 1.136 | 0.1743 | 0.1658 | 0.2124 | 0.205 |
| gen1_sr | 3984 | 1.049 ± 0.054 | 1.18 | 0.1309 | 0.1682 | 0.2286 | 0.2042 |
| gen1_ledger | 6026 | 0.873 ± 0.031 | 1.081 | 0.1817 | 0.1803 | 0.218 | 0.1992 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 19,896)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,567 | 22.9% |
| STALE_QUOTE | market_freshness | 4,174 | 21.0% |
| BOOK_QUALITY | execution | 3,799 | 19.1% |
| POOR_DATA | data | 2,279 | 11.5% |
| LIMITED_DATA | data | 1,282 | 6.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,077 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 962 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 837 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 593 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 326 | 1.6% |

Cause class: coverage 22.9%, market_freshness 21.0%, execution 19.1%, data 17.9%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 71.1%, THIN_PLAYER_HISTORY 59.8%, STALE_PLAYER_DATA 51.3%, STALE_KALSHI_QUOTE 43.5%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 16.0%, LEVEL_TRANSFER_RISK 10.9%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.5%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 10,616)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,654 | 34.4% |
| BOOK_QUALITY | execution | 1,977 | 18.6% |
| STALE_QUOTE | market_freshness | 1,912 | 18.0% |
| POOR_DATA | data | 954 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 575 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 476 | 4.5% |
| LIMITED_DATA | data | 391 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 372 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 230 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 75 | 0.7% |

Cause class: coverage 34.4%, execution 18.6%, market_freshness 18.0%, data 12.7%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.1%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 62.3%, STALE_KALSHI_QUOTE 51.5%, STALE_PLAYER_DATA 46.3%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.6%, PLAYER_IDENTITY_RISK 19.3%, MODEL_HIGH_UNCERTAINTY 18.0%, EVENT_MAPPING_RISK 9.7%, LEVEL_TRANSFER_RISK 9.7%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.4%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8301, "IDENTITY_AMBIGUOUS": 2315}; ticker orientation: {"VERIFIED": 10616}.

Checks: discipline:AMBIGUOUS 722, discipline:PASS 9894, identity_confidence:AMBIGUOUS 2048, identity_confidence:PASS 8568, level_mapping:NA 734, level_mapping:PASS 9882, market_pair:AMBIGUOUS 374, market_pair:NA 262, market_pair:PASS 9980, model_complement:NA 229, model_complement:PASS 10387, namesake:PASS 10616, physical_match_id:NA 3864, physical_match_id:PASS 6752, player_ids:PASS 10616, same_pair_other_event:PASS 10616, ticker_orientation:PASS 10616

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,729 | 5.0% | 4.5% | 1.8% | {"market_freshness": 53, "model_calibration_or_unknown": 43, "data": 35, "execution": 19, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 10} | 5.86 | 0.2265 / 0.2173 (421) | 18.7% | 4.0% | 3.4% | 2.8% |
| CHALLENGER | 7,432 | 17.3% | 7.1% | 12.1% | {"coverage": 724, "market_freshness/coverage": 159, "market_freshness": 147, "data": 129, "model_calibration_or_unknown": 58, "execution": 30, "model_calibration": 27, "mapping": 15} | 7.45 | 0.2176 / 0.2068 (1788) | 35.0% | 17.4% | 3.9% | 22.6% |
| DOUBLES | 1,508 | 47.9% | 47.3% | 6.8% | {"execution": 370, "mapping": 187, "market_freshness": 106, "market_freshness/coverage": 52, "coverage": 7} | 23.85 | 0.3169 / 0.2355 (384) | 15.5% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 13,181 | 25.2% | 17.6% | 31.2% | {"coverage": 1226, "execution": 660, "market_freshness": 539, "data": 448, "market_freshness/coverage": 282, "mapping": 158, "model_calibration_or_unknown": 2, "model_calibration": 1} | 11.74 | 0.2137 / 0.1955 (2967) | 36.7% | 67.9% | 18.4% | 22.1% |
| ITF_WOMEN | 17,825 | 26.9% | 19.7% | 45.1% | {"coverage": 1666, "market_freshness": 989, "execution": 867, "data": 699, "market_freshness/coverage": 392, "mapping": 110, "model_calibration_or_unknown": 59, "model_calibration": 11} | 12.84 | 0.2027 / 0.1943 (3485) | 38.6% | 57.2% | 10.0% | 22.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,657 | 4.7% | 4.1% | 1.2% | {"market_freshness": 38, "model_calibration_or_unknown": 27, "execution": 17, "model_calibration": 12, "data": 11, "market_freshness/coverage": 10, "coverage": 8, "mapping": 1} | 7.85 | 0.2379 / 0.2309 (435) | 24.0% | 1.3% | 1.4% | 3.6% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 15 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 16 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 17 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 18 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 19 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 20 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 21 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 22 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 23 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 24 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 25 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 26 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 27 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 28 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 29 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 30 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 31 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 32 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 34 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 35 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 36 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 37 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 38 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 39 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 41 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 42 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 43 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 44 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 45 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 46 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 47 | `KXITFWMATCH-26OCT20CHAAPI-CHA` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 555 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 122.0, ratio 20.3); no external reference |
| 48 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 730 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 49 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 50 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9708, "by_level_share_of_ge_25pp": {"ATP": 0.0175, "CHALLENGER": 0.1214, "DOUBLES": 0.068, "ITF_MEN": 0.3124, "ITF_WOMEN": 0.4515, "OTHER": 0.0011, "WTA": 0.0117, "WTA125": 0.0164}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5152, "share_primary_cause_market_settled_or_in_play": 0.4334, "share_primary_cause_stale_quote_only": 0.1801}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 10616, "identity_ambiguous_share": 0.2181, "ticker_orientation": {"VERIFIED": 10616}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 6752, "with_external": 336, "coverage": 0.0498, "external_status": {"EXTERNAL_STALE": 203, "AGREES_WITH_KALSHI": 125, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 203, "MODEL_LONE_OUTLIER": 125, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.372, "share_external_supports_model": 0.0238}, "pregame_clean_ge_25pp": {"n": 3275, "with_external": 313, "coverage": 0.0956, "external_status": {"EXTERNAL_STALE": 187, "AGREES_WITH_KALSHI": 118, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 187, "MODEL_LONE_OUTLIER": 118, "ALL_THREE_DISAGREE": 7, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.377, "share_external_supports_model": 0.0256}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.44, "median_min_matches": 20.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2115, "data_status": {"POOR": 5923, "LIMITED": 2851, "ADEQUATE": 1842}, "comparison_lt_10pp": {"median_thinner_serve_points": 1685.0, "median_sample_ratio": 1.7, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 788, "model_minus_observed": 0.0461, "kalshi_minus_observed": -0.0913, "brier_diff_model_minus_kalshi": -0.0039}, "4-10x": {"n": 546, "model_minus_observed": 0.0927, "kalshi_minus_observed": -0.0526, "brier_diff_model_minus_kalshi": 0.0133}, "<2x": {"n": 1953, "model_minus_observed": 0.09, "kalshi_minus_observed": -0.0339, "brier_diff_model_minus_kalshi": 0.0124}, ">=10x": {"n": 697, "model_minus_observed": 0.1062, "kalshi_minus_observed": -0.0695, "brier_diff_model_minus_kalshi": 0.0065}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3984, "model": {"intercept": -0.54, "slope": 0.851, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.233, "slope": 1.11, "slope_se": 0.046}, "mean_extremity_model": 0.1703, "mean_extremity_kalshi": 0.1661, "model_brier": 0.2321, "kalshi_brier": 0.2046, "brier_diff_model_minus_kalshi": 0.0275, "brier_diff_se": 0.003, "model_logloss": 0.6605, "kalshi_logloss": 0.5917}, "fair_v1": {"n": 3984, "model": {"intercept": -0.41, "slope": 1.052, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.15, "slope_se": 0.047}, "mean_extremity_model": 0.1675, "mean_extremity_kalshi": 0.1657, "model_brier": 0.2132, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.0025, "model_logloss": 0.6145, "kalshi_logloss": 0.592}, "gen1_elo": {"n": 3984, "model": {"intercept": -0.398, "slope": 1.027, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.317, "slope": 1.136, "slope_se": 0.046}, "mean_extremity_model": 0.1743, "mean_extremity_kalshi": 0.1658, "model_brier": 0.2124, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0074, "brier_diff_se": 0.0025, "model_logloss": 0.6134, "kalshi_logloss": 0.5923}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.247, "share_ge_15": 0.4462, "median_abs_gap": 13.21, "n": 27339}, "gen1_elo": {"share_ge_25": 0.2445, "share_ge_15": 0.4444, "median_abs_gap": 13.0, "n": 27339}, "gen1_sr": {"share_ge_25": 0.3137, "share_ge_15": 0.5261, "median_abs_gap": 16.02, "n": 27339}, "gen2": {"share_ge_25": 0.316, "share_ge_15": 0.5141, "median_abs_gap": 15.6, "n": 27339}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1545, "share_ge_15": 0.3621, "median_abs_gap": 10.98, "n": 21192}, "gen1_elo": {"share_ge_25": 0.1559, "share_ge_15": 0.358, "median_abs_gap": 10.66, "n": 21189}, "gen1_sr": {"share_ge_25": 0.2212, "share_ge_15": 0.4491, "median_abs_gap": 13.25, "n": 21193}, "gen2": {"share_ge_25": 0.2366, "share_ge_15": 0.4476, "median_abs_gap": 13.18, "n": 21194}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0499, "share_ge_25_pregame_clean": 0.045}, "WTA": {"median_abs_gap_pregame_clean": 7.85, "share_ge_25_all": 0.0467, "share_ge_25_pregame_clean": 0.0414}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.235, "share_within_10pp_all": 0.4316, "share_within_10pp_pregame_clean": 0.4842, "corr_model_vs_mid_pregame_clean": 0.8442}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 585, "model_brier": 0.1978, "kalshi_brier": 0.199, "brier_diff_model_minus_kalshi": -0.0012}, "10-15": {"n_settled": 690, "model_brier": 0.2126, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0092}, "15-25": {"n_settled": 909, "model_brier": 0.2232, "kalshi_brier": 0.2127, "brier_diff_model_minus_kalshi": 0.0105}, "25-40": {"n_settled": 510, "model_brier": 0.2243, "kalshi_brier": 0.2103, "brier_diff_model_minus_kalshi": 0.014}, "3-5": {"n_settled": 373, "model_brier": 0.2018, "kalshi_brier": 0.2011, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 104, "model_brier": 0.2868, "kalshi_brier": 0.1908, "brier_diff_model_minus_kalshi": 0.0961}, "5-10": {"n_settled": 813, "model_brier": 0.2022, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.54, "slope": 0.851, "slope_se": 0.041}, "kalshi_slope": {"intercept": 0.233, "slope": 1.11, "slope_se": 0.046}, "n": 3984}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.513, "slope": 0.873, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.157, "slope": 1.081, "slope_se": 0.036}, "n": 6026}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 384, "model_brier": 0.3169, "kalshi_brier": 0.2355, "brier_diff_model_minus_kalshi": 0.0815, "brier_diff_se": 0.0158, "corr_model_outcome": 0.0242, "corr_kalshi_outcome": 0.2545}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
