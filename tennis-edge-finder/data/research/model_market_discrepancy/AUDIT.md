# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-19T01:32Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 39,525): 0-3 14.4%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 18.9%, 25-40 13.7%, 40+ 8.1%; median gap 11.88 pp.
* **Where the extremes live**: 97.5% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.6%, Challenger 12.4%, doubles 7.4%). Main tour: ATP 3.5% and WTA 5.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,616): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.4%, BOOK_QUALITY 19.2%, STALE_QUOTE 17.8%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.2%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 35.4%, execution 19.2%, market_freshness 17.8%, data 12.3%, market_freshness/coverage 8.5%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.5%.
* **Stale / settled / in-play**: 52.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,616 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.1% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 535.0 points vs 1834.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.061, Gen-2 0.842, Gen-1 ledger 0.886 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 414 model 0.219 vs Kalshi 0.2106; n 84 model 0.2967 vs Kalshi 0.1739.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 166,215 model-market comparisons (270,858 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 59,158 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-19T01:24:00.843431+00:00'], shadow board 43,915 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-19T01:24:04.005789+00:00'], Model 4 19,815 rows, 16,277 settled tickers, 5,509 tickers with an external scan.
* By model: {"gen1_ledger": 39959, "gen1_elo": 22085, "fair_v1": 22085, "gen2": 22085, "gen1_sr": 22085, "model4_fundamental": 18967, "model4_conditioned": 18949}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 39,525 | 14.4 | 9.5 | 19.9 | 15.4 | 18.9 | 13.7 | 8.1 | 11.88 | 40.7% | 21.8% |
| MW fair_v1 | 22,085 | 13.5 | 8.5 | 18.5 | 15.9 | 19.3 | 14.5 | 9.7 | 12.95 | 43.5% | 24.2% |
| MW gen1_elo | 22,085 | 13.1 | 9.1 | 19.5 | 15.2 | 19.5 | 14.3 | 9.4 | 12.54 | 43.2% | 23.7% |
| MW gen1_ledger | 17,440 | 15.6 | 10.8 | 21.6 | 14.8 | 18.5 | 12.6 | 6.1 | 10.48 | 37.2% | 18.7% |
| MW gen1_sr | 22,085 | 9.8 | 7.3 | 16.8 | 14.3 | 21.4 | 18.4 | 12.1 | 15.64 | 51.8% | 30.4% |
| MW gen2 | 22,085 | 11.4 | 7.2 | 16.4 | 14.2 | 19.9 | 17.5 | 13.3 | 15.37 | 50.7% | 30.8% |
| all families model4_conditioned | 18,949 | 21.7 | 18.9 | 34.5 | 17.5 | 4.8 | 1.5 | 1.1 | 5.97 | 7.4% | 2.6% |
| all families model4_fundamental | 18,967 | 16.1 | 12.9 | 34.6 | 20.3 | 11.2 | 3.4 | 1.4 | 7.9 | 16.1% | 4.9% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.3%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.17pp; >=10pp 44.5%, >=25pp 16.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,863 | 29.5 | 13.2 | 24.5 | 17.0 | 11.7 | 3.5 | 0.6 | 6.31 | 15.8% | 4.1% |
| CHALLENGER | 3,679 | 15.7 | 10.1 | 20.2 | 15.8 | 14.5 | 12.4 | 11.1 | 11.32 | 38.1% | 23.6% |
| ITF_MEN | 5,959 | 11.0 | 7.9 | 17.3 | 14.9 | 20.0 | 16.3 | 12.5 | 14.55 | 48.9% | 28.8% |
| ITF_WOMEN | 8,621 | 10.1 | 6.8 | 15.9 | 15.5 | 22.5 | 18.2 | 11.0 | 15.61 | 51.7% | 29.2% |
| WTA | 1,303 | 18.8 | 12.2 | 25.2 | 19.3 | 19.0 | 4.5 | 0.8 | 8.25 | 24.4% | 5.4% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,863 | 23.8 | 14.6 | 24.1 | 18.0 | 14.2 | 4.3 | 1.0 | 6.86 | 19.4% | 5.3% |
| CHALLENGER | 3,679 | 14.7 | 8.2 | 18.9 | 13.7 | 18.1 | 14.3 | 12.2 | 12.84 | 44.5% | 26.5% |
| ITF_MEN | 5,959 | 9.3 | 6.7 | 15.6 | 13.5 | 19.8 | 19.3 | 15.7 | 17.02 | 54.8% | 35.0% |
| ITF_WOMEN | 8,621 | 8.4 | 5.5 | 13.7 | 13.6 | 21.1 | 20.8 | 16.9 | 18.87 | 58.8% | 37.7% |
| WTA | 1,303 | 16.6 | 8.4 | 20.4 | 16.5 | 22.6 | 14.7 | 0.9 | 11.46 | 38.1% | 15.6% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,863 | 25.0 | 13.6 | 25.7 | 16.9 | 13.8 | 4.3 | 0.7 | 6.8 | 18.8% | 5.1% |
| CHALLENGER | 3,679 | 14.7 | 10.1 | 20.8 | 15.0 | 15.8 | 12.2 | 11.4 | 11.16 | 39.4% | 23.6% |
| ITF_MEN | 5,959 | 10.0 | 8.0 | 17.7 | 14.1 | 20.8 | 16.8 | 12.5 | 15.01 | 50.1% | 29.2% |
| ITF_WOMEN | 8,621 | 9.5 | 6.9 | 16.3 | 15.6 | 23.1 | 18.3 | 10.2 | 15.59 | 51.6% | 28.6% |
| WTA | 1,303 | 23.9 | 17.3 | 30.4 | 15.1 | 10.7 | 2.0 | 0.5 | 6.0 | 13.3% | 2.5% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,129 | 27.6 | 20.3 | 31.5 | 11.6 | 6.5 | 2.4 | 0.1 | 5.23 | 9.0% | 2.5% |
| CHALLENGER | 2,562 | 22.1 | 15.0 | 26.8 | 14.2 | 14.1 | 5.9 | 1.9 | 7.08 | 21.9% | 7.8% |
| DOUBLES | 1,305 | 4.7 | 4.3 | 10.3 | 10.8 | 21.1 | 25.8 | 23.1 | 24.22 | 70.0% | 48.9% |
| ITF_MEN | 4,965 | 14.5 | 8.7 | 20.7 | 15.8 | 21.0 | 12.4 | 7.0 | 11.86 | 40.4% | 19.4% |
| ITF_WOMEN | 5,678 | 11.8 | 9.1 | 19.1 | 14.8 | 22.1 | 16.9 | 6.2 | 13.17 | 45.1% | 23.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 920 | 22.6 | 15.8 | 29.4 | 17.5 | 10.4 | 4.0 | 0.3 | 6.81 | 14.8% | 4.3% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,824 | 29.7 | 13.3 | 24.8 | 16.8 | 11.5 | 3.2 | 0.7 | 6.17 | 15.3% | 3.8% |
| CHALLENGER | 2,625 | 20.4 | 12.7 | 25.3 | 18.4 | 14.7 | 6.4 | 2.1 | 8.23 | 23.2% | 8.5% |
| ITF_MEN | 4,314 | 13.6 | 9.9 | 20.7 | 16.8 | 20.4 | 13.1 | 5.6 | 11.6 | 39.0% | 18.7% |
| ITF_WOMEN | 6,448 | 12.0 | 8.1 | 18.0 | 17.6 | 24.1 | 15.3 | 4.9 | 13.33 | 44.3% | 20.3% |
| WTA | 1,277 | 18.9 | 11.8 | 25.4 | 19.4 | 19.2 | 4.5 | 0.9 | 8.28 | 24.5% | 5.3% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,824 | 24.0 | 14.8 | 24.2 | 18.0 | 14.0 | 4.1 | 0.8 | 6.75 | 19.0% | 4.9% |
| CHALLENGER | 2,625 | 18.9 | 10.4 | 23.6 | 16.4 | 18.6 | 9.4 | 2.6 | 9.23 | 30.7% | 12.0% |
| ITF_MEN | 4,315 | 11.0 | 8.0 | 18.1 | 15.4 | 22.0 | 17.0 | 8.5 | 14.12 | 47.5% | 25.5% |
| ITF_WOMEN | 6,448 | 9.3 | 6.3 | 15.1 | 14.9 | 23.2 | 20.4 | 10.7 | 16.62 | 54.3% | 31.1% |
| WTA | 1,277 | 16.4 | 8.3 | 20.4 | 16.5 | 22.6 | 14.8 | 0.9 | 11.5 | 38.3% | 15.7% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,096 | 27.7 | 20.4 | 31.8 | 11.8 | 6.0 | 2.2 | 0.1 | 5.11 | 8.3% | 2.3% |
| CHALLENGER | 2,219 | 23.7 | 16.3 | 28.7 | 14.1 | 13.3 | 3.4 | 0.6 | 6.45 | 17.3% | 4.0% |
| DOUBLES | 1,212 | 4.7 | 4.5 | 10.4 | 11.0 | 21.0 | 25.9 | 22.6 | 24.09 | 69.5% | 48.5% |
| ITF_MEN | 4,106 | 15.9 | 9.4 | 22.6 | 16.7 | 20.7 | 10.6 | 4.1 | 10.61 | 35.4% | 14.7% |
| ITF_WOMEN | 4,685 | 12.6 | 9.8 | 20.7 | 15.6 | 22.3 | 15.6 | 3.4 | 11.9 | 41.3% | 19.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 881 | 22.9 | 16.2 | 29.6 | 17.5 | 10.6 | 3.2 | 0.0 | 6.68 | 13.7% | 3.2% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,305 | 4.7 | 4.3 | 10.3 | 10.8 | 21.1 | 25.8 | 23.1 | 24.22 | 70.0% | 48.9% |
| singles | 16,135 | 16.5 | 11.3 | 22.6 | 15.1 | 18.3 | 11.5 | 4.8 | 9.9 | 34.5% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,054 | 13.5 | 8.9 | 19.3 | 15.9 | 18.1 | 14.5 | 9.8 | 12.66 | 42.4% | 24.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 14,247 | 13.9 | 8.5 | 18.5 | 15.5 | 19.6 | 14.3 | 9.7 | 12.96 | 43.6% | 24.0% |
| UNKNOWN | 2,547 | 11.9 | 7.7 | 17.1 | 18.2 | 19.4 | 15.8 | 10.0 | 13.2 | 45.1% | 25.8% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,489 | 19.9 | 10.9 | 21.4 | 17.4 | 15.7 | 8.7 | 6.2 | 9.34 | 30.5% | 14.8% |
| B | 2,854 | 13.2 | 9.2 | 19.9 | 16.8 | 18.3 | 12.0 | 10.7 | 12.11 | 41.0% | 22.7% |
| C | 3,202 | 12.7 | 9.3 | 19.4 | 14.6 | 19.3 | 14.9 | 9.9 | 12.8 | 44.1% | 24.8% |
| D | 3,705 | 12.4 | 7.9 | 17.2 | 15.5 | 21.9 | 15.5 | 9.5 | 13.9 | 46.9% | 25.0% |
| F | 5,835 | 7.9 | 5.5 | 14.9 | 14.9 | 22.1 | 21.5 | 13.2 | 17.84 | 56.8% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,149 | 23.3 | 15.9 | 28.8 | 15.2 | 11.2 | 4.0 | 1.5 | 6.61 | 16.7% | 5.5% |
| B | 2,483 | 15.4 | 10.1 | 23.8 | 16.4 | 19.3 | 11.0 | 4.1 | 10.14 | 34.4% | 15.1% |
| C | 3,522 | 11.3 | 7.6 | 17.6 | 14.2 | 21.6 | 16.4 | 11.2 | 14.62 | 49.2% | 27.7% |
| D | 2,535 | 14.1 | 9.9 | 20.4 | 13.7 | 20.8 | 14.5 | 6.6 | 12.04 | 41.9% | 21.1% |
| F | 3,751 | 10.2 | 7.9 | 14.9 | 14.3 | 23.4 | 20.3 | 8.9 | 16.15 | 52.6% | 29.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,378 | 18.1 | 9.8 | 20.6 | 17.2 | 16.2 | 9.5 | 8.6 | 10.43 | 34.3% | 18.1% |
| LIMITED | 4,974 | 14.5 | 10.4 | 20.4 | 15.4 | 18.7 | 13.2 | 7.4 | 11.42 | 39.3% | 20.6% |
| POOR | 9,733 | 9.7 | 6.6 | 15.9 | 15.2 | 22.0 | 19.0 | 11.7 | 15.96 | 52.7% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,346 | 27.0 | 21.9 | 34.9 | 11.1 | 3.8 | 1.2 | 0.2 | 5.08 | 5.1% | 1.4% |
| GAME_SPREAD | 3,839 | 23.9 | 15.5 | 34.4 | 17.4 | 7.0 | 1.7 | 0.2 | 6.36 | 8.9% | 1.9% |
| MATCH_WINNER | 17,440 | 15.6 | 10.8 | 21.6 | 14.8 | 18.5 | 12.6 | 6.1 | 10.48 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,123 | 30.4 | 17.8 | 30.4 | 12.2 | 7.5 | 1.2 | 0.4 | 5.2 | 9.1% | 1.6% |
| TOTAL_GAMES | 6,187 | 7.2 | 8.8 | 37.2 | 28.9 | 11.3 | 3.6 | 3.1 | 9.65 | 18.0% | 6.7% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,638 | 25.0 | 34.6 | 32.4 | 3.6 | 3.5 | 0.6 | 0.2 | 4.48 | 4.3% | 0.8% |
| GAME_SPREAD | 4,554 | 45.9 | 16.9 | 27.5 | 7.1 | 1.7 | 0.6 | 0.3 | 3.44 | 2.7% | 0.9% |
| TOTAL_GAMES | 7,757 | 4.6 | 6.7 | 40.4 | 35.5 | 7.7 | 2.7 | 2.5 | 9.83 | 12.9% | 5.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,641 | 24.4 | 17.6 | 36.0 | 11.9 | 7.0 | 2.6 | 0.4 | 5.84 | 10.0% | 2.9% |
| GAME_SPREAD | 4,557 | 19.3 | 13.6 | 28.8 | 19.9 | 13.7 | 3.8 | 0.9 | 7.88 | 18.4% | 4.7% |
| TOTAL_GAMES | 7,769 | 7.2 | 8.5 | 36.8 | 27.6 | 13.3 | 4.0 | 2.6 | 9.7 | 19.9% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 22,085 | 43.5% | 24.2% | 12.95 | 34.8% | 15.0% | 10.68 |
| gen1_elo | 22,085 | 43.2% | 23.7% | 12.54 | 34.2% | 14.8% | 10.19 |
| gen1_sr | 22,085 | 51.8% | 30.4% | 15.64 | 44.0% | 21.1% | 13.04 |
| gen2 | 22,085 | 50.7% | 30.8% | 15.37 | 44.0% | 22.7% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 11,792 | 16.4 | 10.4 | 21.5 | 17.5 | 19.7 | 11.4 | 3.3 | 10.5 | 34.3% | 14.6% |
| STALE | 10,293 | 10.3 | 6.4 | 15.1 | 14.1 | 18.9 | 18.1 | 17.1 | 17.14 | 54.1% | 35.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 10,908 | 17.1 | 11.6 | 22.8 | 14.8 | 17.3 | 11.6 | 4.9 | 9.65 | 33.8% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 39,525 | 10908 | 15264 | 13353 | 23.7 | 141.6 | 1400.4 |
| ge_15pp | 16,100 | 3686 | 5335 | 7079 | 25.8 | 443.7 | 1380.4 |
| ge_25pp | 8,616 | 1800 | 2319 | 4497 | 32.8 | 583.5 | 1380.4 |
| lt_10pp | 17,337 | 5611 | 7319 | 4407 | 21.7 | 47.9 | 1341.5 |

Current slate `SL-20261019T013250Z-0b49a9b2`: 861 priced rows, quote age at build {'median': 9.1, 'max': 9.2}, freshness {'FRESH': 861}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,048 | 21.2 | 10.7 | 23.5 | 19.2 | 18.3 | 6.6 | 0.5 | 8.64 | 25.4% | 7.1% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 356 | 70.2 | 29.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.09 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 733 | 0.0 | 2.9 | 35.5 | 28.6 | 23.1 | 9.3 | 0.7 | 11.92 | 33.0% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 22,085 | 3171 (14.4%) | 23.1% | 0.7% | {"EXTERNAL_STALE": 2048, "AGREES_WITH_KALSHI": 733, "ALL_AGREE": 356, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 9,615 | 771 (8.0%) | 31.4% | 1.2% | {"EXTERNAL_STALE": 520, "AGREES_WITH_KALSHI": 242, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,354 | 221 (4.1%) | 33.0% | 1.4% | {"EXTERNAL_STALE": 145, "AGREES_WITH_KALSHI": 73, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,566 | 209 (8.1%) | 34.0% | 1.4% | {"EXTERNAL_STALE": 135, "AGREES_WITH_KALSHI": 71, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,957 | 1797 (20.1%) | 15.6% | 0.7% | {"EXTERNAL_STALE": 1135, "ALL_AGREE": 356, "AGREES_WITH_KALSHI": 281, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,243 | 11.2 | 7.8 | 19.3 | 15.1 | 21.4 | 15.1 | 10.0 | 13.77 | 46.6% | 25.1% |
| 4-10x | 2,870 | 12.3 | 8.9 | 19.0 | 15.7 | 19.5 | 15.2 | 9.4 | 13.02 | 44.1% | 24.7% |
| <2x | 11,484 | 15.6 | 9.3 | 19.0 | 16.9 | 17.7 | 12.6 | 8.8 | 11.71 | 39.2% | 21.4% |
| >=10x | 3,488 | 10.7 | 6.4 | 15.3 | 13.8 | 21.7 | 19.5 | 12.6 | 16.44 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,707 | 13.1 | 8.5 | 19.4 | 16.1 | 19.5 | 13.1 | 10.3 | 12.8 | 42.9% | 23.4% |
| 300-1000 | 4,896 | 12.2 | 8.7 | 17.1 | 15.7 | 20.7 | 16.1 | 9.4 | 13.72 | 46.2% | 25.6% |
| <300 | 6,645 | 8.9 | 5.9 | 15.5 | 14.8 | 21.9 | 20.2 | 12.8 | 16.88 | 54.9% | 32.9% |
| >=3000 | 4,837 | 21.7 | 11.9 | 22.9 | 17.4 | 14.0 | 6.9 | 5.1 | 8.18 | 26.0% | 12.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 673 | 0.5417 | 0.407 | 0.4889 | +0.053 | -0.082 | -0.0007 ± 0.0058 |
| ratio 4-10x | 459 | 0.5903 | 0.4489 | 0.5163 | +0.074 | -0.067 | 0.0071 ± 0.0074 |
| ratio <2x | 1667 | 0.538 | 0.4167 | 0.4511 | +0.087 | -0.034 | 0.0121 ± 0.0035 |
| ratio >=10x | 563 | 0.5601 | 0.3879 | 0.4458 | +0.114 | -0.058 | 0.0105 ± 0.0076 |
| thinner_sample 1000-3000 | 935 | 0.5435 | 0.4172 | 0.462 | +0.082 | -0.045 | 0.0079 ± 0.0047 |
| thinner_sample 300-1000 | 799 | 0.5654 | 0.4247 | 0.4956 | +0.070 | -0.071 | -0.0003 ± 0.0056 |
| thinner_sample <300 | 1051 | 0.5531 | 0.3908 | 0.452 | +0.101 | -0.061 | 0.013 ± 0.0054 |
| thinner_sample >=3000 | 577 | 0.5312 | 0.4382 | 0.461 | +0.070 | -0.023 | 0.0142 ± 0.0048 |
| data_status ADEQUATE | 978 | 0.5342 | 0.4297 | 0.455 | +0.079 | -0.025 | 0.0114 ± 0.004 |
| data_status LIMITED | 834 | 0.5543 | 0.424 | 0.4904 | +0.064 | -0.066 | 0.0029 ± 0.0051 |
| data_status POOR | 1550 | 0.5568 | 0.3994 | 0.4613 | +0.096 | -0.062 | 0.0099 ± 0.0043 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 514 | 0.1956 | 0.1968 | -0.0013 ± 0.0007 | 0.5697 | 0.5723 | 0.4955 | 0.4807 | 0.5292 | -0.051 ± 0.0205 | -0.01 (5) |
| 3-5 | 323 | 0.1973 | 0.1966 | +0.0007 ± 0.002 | 0.5764 | 0.5734 | 0.5057 | 0.4658 | 0.4768 | -0.084 ± 0.0252 | 0.02 (1) |
| 5-10 | 701 | 0.1988 | 0.1986 | +0.0002 ± 0.0026 | 0.583 | 0.5806 | 0.5133 | 0.4388 | 0.4693 | -0.085 ± 0.0175 | -0.0167 (6) |
| 10-15 | 595 | 0.2155 | 0.2066 | +0.0089 ± 0.0047 | 0.6212 | 0.5954 | 0.5227 | 0.3986 | 0.4235 | -0.093 ± 0.0186 | -0.048 (5) |
| 15-25 | 731 | 0.2271 | 0.2132 | +0.0139 ± 0.0067 | 0.6482 | 0.6117 | 0.5803 | 0.3851 | 0.4473 | -0.087 ± 0.017 | -0.0033 (9) |
| 25-40 | 414 | 0.219 | 0.2106 | +0.0084 ± 0.0133 | 0.6256 | 0.6042 | 0.6557 | 0.3472 | 0.4879 | -0.063 ± 0.0203 | -0.01 (1) |
| 40+ | 84 | 0.2967 | 0.1739 | +0.1228 ± 0.0408 | 0.801 | 0.521 | 0.7529 | 0.3035 | 0.3929 | -0.119 ± 0.0388 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2438 | 0.1817 | 0.1829 | -0.0012 ± 0.0003 | 0.5384 | 0.5398 | 0.4797 | 0.4646 | 0.5033 | -0.019 ± 0.0088 | -0.0129 (17) |
| 3-5 | 1531 | 0.1939 | 0.1919 | +0.0020 ± 0.0009 | 0.5684 | 0.5596 | 0.478 | 0.4383 | 0.4311 | -0.065 ± 0.0114 | 0.0 (2) |
| 5-10 | 3300 | 0.1928 | 0.1899 | +0.0029 ± 0.0011 | 0.5675 | 0.5581 | 0.4853 | 0.4115 | 0.4264 | -0.050 ± 0.0077 | -0.0119 (21) |
| 10-15 | 2921 | 0.2026 | 0.1843 | +0.0183 ± 0.002 | 0.593 | 0.5413 | 0.4831 | 0.3584 | 0.3475 | -0.075 ± 0.0079 | -0.0281 (16) |
| 15-25 | 3524 | 0.2078 | 0.1716 | +0.0362 ± 0.0027 | 0.6071 | 0.5073 | 0.5029 | 0.3067 | 0.3133 | -0.068 ± 0.0069 | -0.0025 (44) |
| 25-40 | 2767 | 0.2207 | 0.1274 | +0.0934 ± 0.0042 | 0.6348 | 0.3916 | 0.5328 | 0.2196 | 0.2309 | -0.064 ± 0.0065 | -0.01 (1) |
| 40+ | 1842 | 0.3777 | 0.0425 | +0.3352 ± 0.0054 | 0.9828 | 0.169 | 0.628 | 0.1061 | 0.0565 | -0.086 ± 0.0044 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 382 | 0.2013 | 0.2019 | -0.0005 ± 0.0008 | 0.5848 | 0.5861 | 0.5026 | 0.4875 | 0.5105 | -0.083 ± 0.0243 | -0.01 (3) |
| 3-5 | 276 | 0.2148 | 0.2146 | +0.0001 ± 0.0023 | 0.6128 | 0.6132 | 0.5154 | 0.4755 | 0.4891 | -0.082 ± 0.0294 | 0.02 (1) |
| 5-10 | 604 | 0.1989 | 0.1982 | +0.0007 ± 0.0027 | 0.5814 | 0.5795 | 0.5457 | 0.4708 | 0.5033 | -0.077 ± 0.0187 | -0.01 (4) |
| 10-15 | 554 | 0.2181 | 0.2124 | +0.0057 ± 0.0049 | 0.6266 | 0.6111 | 0.5687 | 0.4445 | 0.4874 | -0.092 ± 0.0203 | -0.04 (5) |
| 15-25 | 806 | 0.2297 | 0.209 | +0.0207 ± 0.0063 | 0.6511 | 0.6004 | 0.5896 | 0.3935 | 0.4429 | -0.093 ± 0.0163 | -0.0133 (9) |
| 25-40 | 543 | 0.2653 | 0.1976 | +0.0676 ± 0.012 | 0.7401 | 0.5762 | 0.6658 | 0.3505 | 0.4015 | -0.123 ± 0.0188 | -0.0075 (4) |
| 40+ | 197 | 0.363 | 0.1769 | +0.1861 ± 0.0297 | 1.0109 | 0.5248 | 0.744 | 0.2609 | 0.3249 | -0.074 ± 0.0287 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2060 | 0.1851 | 0.1857 | -0.0006 ± 0.0003 | 0.5463 | 0.5474 | 0.5028 | 0.488 | 0.5112 | -0.034 ± 0.0098 | -0.0133 (15) |
| 3-5 | 1304 | 0.1951 | 0.1943 | +0.0008 ± 0.001 | 0.566 | 0.5637 | 0.5169 | 0.477 | 0.4862 | -0.044 ± 0.0124 | 0.02 (1) |
| 5-10 | 2929 | 0.1912 | 0.1887 | +0.0025 ± 0.0012 | 0.5647 | 0.5556 | 0.5071 | 0.4331 | 0.4544 | -0.041 ± 0.0081 | -0.0117 (6) |
| 10-15 | 2567 | 0.1994 | 0.1891 | +0.0103 ± 0.0022 | 0.5873 | 0.5509 | 0.5205 | 0.396 | 0.4196 | -0.049 ± 0.0087 | -0.0189 (18) |
| 15-25 | 3669 | 0.2179 | 0.1786 | +0.0393 ± 0.0028 | 0.6308 | 0.5256 | 0.5316 | 0.3355 | 0.3369 | -0.074 ± 0.007 | -0.0086 (42) |
| 25-40 | 3259 | 0.2496 | 0.1367 | +0.1129 ± 0.0041 | 0.7051 | 0.4194 | 0.5628 | 0.2468 | 0.2277 | -0.090 ± 0.0064 | -0.0044 (18) |
| 40+ | 2535 | 0.4008 | 0.0655 | +0.3353 ± 0.0059 | 1.0581 | 0.2293 | 0.6625 | 0.1251 | 0.0955 | -0.069 ± 0.005 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 498 | 0.1976 | 0.2001 | -0.0025 ± 0.0007 | 0.5759 | 0.5818 | 0.499 | 0.4837 | 0.5542 | -0.015 ± 0.0204 | -0.0137 (8) |
| 3-5 | 363 | 0.1921 | 0.1898 | +0.0023 ± 0.0018 | 0.5613 | 0.556 | 0.4985 | 0.4588 | 0.4518 | -0.119 ± 0.024 | 0.0067 (3) |
| 5-10 | 728 | 0.2012 | 0.1981 | +0.0030 ± 0.0025 | 0.5892 | 0.5785 | 0.5066 | 0.4327 | 0.4464 | -0.093 ± 0.0169 | -0.0071 (7) |
| 10-15 | 582 | 0.2091 | 0.2066 | +0.0026 ± 0.0047 | 0.6063 | 0.5962 | 0.5398 | 0.4167 | 0.4708 | -0.075 ± 0.0186 | -0.0317 (6) |
| 15-25 | 682 | 0.2353 | 0.2107 | +0.0246 ± 0.0069 | 0.6699 | 0.6057 | 0.5888 | 0.3954 | 0.4282 | -0.115 ± 0.0176 | -0.03 (1) |
| 25-40 | 426 | 0.2041 | 0.2159 | -0.0118 ± 0.013 | 0.5928 | 0.616 | 0.6617 | 0.3519 | 0.5235 | -0.040 ± 0.0197 | 0.015 (2) |
| 40+ | 83 | 0.3118 | 0.1871 | +0.1247 ± 0.0428 | 0.8371 | 0.5509 | 0.7556 | 0.302 | 0.3976 | -0.102 ± 0.0431 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2324 | 0.1884 | 0.1893 | -0.0009 ± 0.0003 | 0.5537 | 0.5553 | 0.4875 | 0.4721 | 0.4957 | -0.031 ± 0.0091 | -0.0163 (35) |
| 3-5 | 1607 | 0.188 | 0.1846 | +0.0034 ± 0.0009 | 0.5538 | 0.5456 | 0.4767 | 0.4372 | 0.4151 | -0.085 ± 0.011 | -0.0094 (18) |
| 5-10 | 3503 | 0.194 | 0.1876 | +0.0065 ± 0.0011 | 0.5724 | 0.5512 | 0.4835 | 0.4096 | 0.4008 | -0.070 ± 0.0074 | -0.01 (31) |
| 10-15 | 2749 | 0.1967 | 0.1804 | +0.0163 ± 0.002 | 0.5782 | 0.5304 | 0.4992 | 0.3758 | 0.3721 | -0.071 ± 0.008 | -0.015 (12) |
| 15-25 | 3659 | 0.2089 | 0.1712 | +0.0377 ± 0.0027 | 0.6112 | 0.5067 | 0.5068 | 0.312 | 0.3132 | -0.070 ± 0.0069 | -0.03 (2) |
| 25-40 | 2710 | 0.2147 | 0.1255 | +0.0892 ± 0.0043 | 0.621 | 0.3857 | 0.53 | 0.2139 | 0.2347 | -0.058 ± 0.0064 | 0.01 (3) |
| 40+ | 1771 | 0.3922 | 0.047 | +0.3452 ± 0.0058 | 1.0224 | 0.1809 | 0.639 | 0.1109 | 0.0599 | -0.088 ± 0.0048 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 840 | 0.1962 | 0.1963 | -0.0001 ± 0.0005 | 0.573 | 0.5729 | 0.5074 | 0.4923 | 0.4929 | -0.058 ± 0.0154 | -0.0224 (49) |
| 3-5 | 591 | 0.1945 | 0.1937 | +0.0008 ± 0.0015 | 0.5673 | 0.5643 | 0.4808 | 0.4409 | 0.4484 | -0.053 ± 0.0183 | -0.0194 (34) |
| 5-10 | 1238 | 0.199 | 0.1928 | +0.0062 ± 0.0019 | 0.5855 | 0.5677 | 0.4896 | 0.4161 | 0.4111 | -0.069 ± 0.0127 | -0.005 (78) |
| 10-15 | 791 | 0.2072 | 0.1966 | +0.0106 ± 0.0039 | 0.6024 | 0.5748 | 0.5106 | 0.3874 | 0.4046 | -0.058 ± 0.0159 | 0.0014 (64) |
| 15-25 | 1062 | 0.2335 | 0.2125 | +0.0210 ± 0.0056 | 0.6651 | 0.6112 | 0.5692 | 0.3742 | 0.419 | -0.061 ± 0.0142 | -0.0214 (59) |
| 25-40 | 631 | 0.2437 | 0.2003 | +0.0434 ± 0.0109 | 0.6903 | 0.5793 | 0.6571 | 0.3446 | 0.4295 | -0.079 ± 0.0165 | -0.0219 (26) |
| 40+ | 219 | 0.3522 | 0.1941 | +0.1581 ± 0.0299 | 1.0177 | 0.5694 | 0.8035 | 0.3161 | 0.4201 | -0.079 ± 0.0262 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2607 | 0.1875 | 0.1875 | -0.0000 ± 0.0003 | 0.55 | 0.5491 | 0.5047 | 0.4894 | 0.4964 | -0.040 ± 0.0085 | -0.0157 (88) |
| 3-5 | 1801 | 0.1909 | 0.1881 | +0.0027 ± 0.0008 | 0.5581 | 0.5517 | 0.4878 | 0.4481 | 0.4342 | -0.061 ± 0.0103 | -0.0209 (69) |
| 5-10 | 3594 | 0.1952 | 0.1866 | +0.0086 ± 0.0011 | 0.5752 | 0.5514 | 0.4872 | 0.4137 | 0.394 | -0.072 ± 0.0073 | -0.0082 (132) |
| 10-15 | 2455 | 0.203 | 0.1886 | +0.0145 ± 0.0022 | 0.5932 | 0.5552 | 0.5178 | 0.3948 | 0.3967 | -0.059 ± 0.0087 | -0.0053 (105) |
| 15-25 | 3069 | 0.229 | 0.1982 | +0.0308 ± 0.0032 | 0.6596 | 0.5763 | 0.5616 | 0.3661 | 0.3864 | -0.062 ± 0.0081 | -0.0253 (107) |
| 25-40 | 2094 | 0.2492 | 0.1737 | +0.0755 ± 0.0057 | 0.7077 | 0.5113 | 0.6161 | 0.3025 | 0.3419 | -0.071 ± 0.0088 | -0.0229 (51) |
| 40+ | 984 | 0.3789 | 0.1335 | +0.2455 ± 0.0124 | 1.0741 | 0.4069 | 0.7178 | 0.2136 | 0.2368 | -0.073 ± 0.0108 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3362 | 1.061 ± 0.049 | 1.177 | 0.168 | 0.1659 | 0.2122 | 0.2036 |
| gen2 | 3362 | 0.842 ± 0.044 | 1.135 | 0.174 | 0.166 | 0.2314 | 0.2035 |
| gen1_elo | 3362 | 1.044 ± 0.048 | 1.163 | 0.1736 | 0.1664 | 0.2111 | 0.2035 |
| gen1_sr | 3362 | 1.044 ± 0.057 | 1.205 | 0.1341 | 0.1677 | 0.2274 | 0.2033 |
| gen1_ledger | 5372 | 0.886 ± 0.034 | 1.083 | 0.1784 | 0.1814 | 0.2176 | 0.1988 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 16,100)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,859 | 24.0% |
| STALE_QUOTE | market_freshness | 3,295 | 20.5% |
| BOOK_QUALITY | execution | 3,143 | 19.5% |
| POOR_DATA | data | 1,751 | 10.9% |
| LIMITED_DATA | data | 1,097 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 858 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 788 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 640 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 456 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 213 | 1.3% |

Cause class: coverage 24.0%, market_freshness 20.5%, execution 19.5%, data 17.7%, market_freshness/coverage 8.2%, model_calibration_or_unknown 4.9%, mapping 4.0%, model_calibration 1.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.6%, START_UNVERIFIABLE 94.7%, LOW_DATA_QUALITY 69.8%, THIN_PLAYER_HISTORY 58.1%, STALE_PLAYER_DATA 51.6%, STALE_KALSHI_QUOTE 44.0%, MODEL_INTERNAL_DISAGREEMENT 40.2%, ASYMMETRIC_SAMPLE_SIZE 32.2%, WIDE_SPREAD 25.6%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 8.8%, EVENT_MAPPING_RISK 8.6%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.3%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.4%, POST_SETTLEMENT_OBSERVATION 24.0%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,616)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,053 | 35.4% |
| BOOK_QUALITY | execution | 1,654 | 19.2% |
| STALE_QUOTE | market_freshness | 1,534 | 17.8% |
| POOR_DATA | data | 736 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 453 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 364 | 4.2% |
| LIMITED_DATA | data | 324 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 281 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 170 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 47 | 0.5% |

Cause class: coverage 35.4%, execution 19.2%, market_freshness 17.8%, data 12.3%, market_freshness/coverage 8.5%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.7%, START_UNVERIFIABLE 97.5%, LOW_DATA_QUALITY 73.7%, THIN_PLAYER_HISTORY 60.5%, STALE_KALSHI_QUOTE 52.2%, STALE_PLAYER_DATA 47.0%, MODEL_INTERNAL_DISAGREEMENT 41.1%, ASYMMETRIC_SAMPLE_SIZE 34.0%, WIDE_SPREAD 25.4%, PLAYER_IDENTITY_RISK 18.2%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 10.3%, LOW_DISPLAYED_LIQUIDITY 7.8%, LEVEL_TRANSFER_RISK 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.2%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.2%, POST_SETTLEMENT_OBSERVATION 35.4%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6822, "IDENTITY_AMBIGUOUS": 1794}; ticker orientation: {"VERIFIED": 8616}.

Checks: discipline:AMBIGUOUS 638, discipline:PASS 7978, identity_confidence:AMBIGUOUS 1570, identity_confidence:PASS 7046, level_mapping:NA 650, level_mapping:PASS 7966, market_pair:AMBIGUOUS 311, market_pair:NA 213, market_pair:PASS 8092, model_complement:NA 180, model_complement:PASS 8436, namesake:PASS 8616, physical_match_id:NA 3262, physical_match_id:PASS 5354, player_ids:PASS 8616, same_pair_other_event:PASS 8616, ticker_orientation:PASS 8616

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,992 | 3.5% | 3.2% | 1.2% | {"market_freshness": 35, "data": 25, "execution": 14, "model_calibration_or_unknown": 14, "market_freshness/coverage": 8, "model_calibration": 7, "coverage": 2} | 5.67 | 0.2142 / 0.2101 (329) | 17.3% | 3.1% | 4.2% | 2.4% |
| CHALLENGER | 6,241 | 17.1% | 6.4% | 12.4% | {"coverage": 621, "market_freshness/coverage": 134, "market_freshness": 131, "data": 90, "model_calibration_or_unknown": 47, "execution": 25, "model_calibration": 10, "mapping": 9} | 7.24 | 0.2162 / 0.2059 (1574) | 35.9% | 14.5% | 3.1% | 22.4% |
| DOUBLES | 1,305 | 48.9% | 48.5% | 7.4% | {"execution": 314, "mapping": 168, "market_freshness": 106, "market_freshness/coverage": 43, "coverage": 7} | 24.09 | 0.324 / 0.2339 (337) | 17.9% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 10,924 | 24.6% | 16.7% | 31.1% | {"coverage": 1061, "execution": 540, "market_freshness": 414, "data": 357, "market_freshness/coverage": 214, "mapping": 94, "model_calibration_or_unknown": 2} | 11.16 | 0.214 / 0.1949 (2662) | 36.4% | 62.0% | 13.4% | 22.9% |
| ITF_WOMEN | 14,299 | 26.8% | 19.7% | 44.4% | {"coverage": 1345, "market_freshness": 772, "execution": 731, "data": 554, "market_freshness/coverage": 286, "mapping": 87, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.8 | 0.2016 / 0.1938 (2937) | 38.5% | 57.7% | 10.3% | 22.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,223 | 5.0% | 4.5% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 16, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.63 | 0.2413 / 0.234 (365) | 23.2% | 1.5% | 1.6% | 2.9% |
| WTA125 | 1,392 | 12.5% | 9.9% | 2.0% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
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
| 45 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 624 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 46 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 47 | `KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF` | DOUBLES | gen1_ledger | 90% / 15% | +75 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 49 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 50 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.975, "by_level_share_of_ge_25pp": {"ATP": 0.0122, "CHALLENGER": 0.1238, "DOUBLES": 0.074, "ITF_MEN": 0.3113, "ITF_WOMEN": 0.4443, "OTHER": 0.0014, "WTA": 0.0128, "WTA125": 0.0202}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5219, "share_primary_cause_market_settled_or_in_play": 0.4395, "share_primary_cause_stale_quote_only": 0.178}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8616, "identity_ambiguous_share": 0.2082, "ticker_orientation": {"VERIFIED": 8616}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5354, "with_external": 221, "coverage": 0.0413, "external_status": {"EXTERNAL_STALE": 145, "AGREES_WITH_KALSHI": 73, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 145, "MODEL_LONE_OUTLIER": 73, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3303, "share_external_supports_model": 0.0136}, "pregame_clean_ge_25pp": {"n": 2566, "with_external": 209, "coverage": 0.0814, "external_status": {"EXTERNAL_STALE": 135, "AGREES_WITH_KALSHI": 71, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 135, "MODEL_LONE_OUTLIER": 71, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3397, "share_external_supports_model": 0.0144}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 535.0, "median_sample_ratio": 2.43, "median_min_matches": 21.0, "median_max_days_since_last": 213.0, "share_severe_asymmetry": 0.2057, "data_status": {"POOR": 4637, "LIMITED": 2455, "ADEQUATE": 1524}, "comparison_lt_10pp": {"median_thinner_serve_points": 1834.0, "median_sample_ratio": 1.67, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 673, "model_minus_observed": 0.0528, "kalshi_minus_observed": -0.0819, "brier_diff_model_minus_kalshi": -0.0007}, "4-10x": {"n": 459, "model_minus_observed": 0.074, "kalshi_minus_observed": -0.0674, "brier_diff_model_minus_kalshi": 0.0071}, "<2x": {"n": 1667, "model_minus_observed": 0.0869, "kalshi_minus_observed": -0.0344, "brier_diff_model_minus_kalshi": 0.0121}, ">=10x": {"n": 563, "model_minus_observed": 0.1143, "kalshi_minus_observed": -0.058, "brier_diff_model_minus_kalshi": 0.0105}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3362, "model": {"intercept": -0.529, "slope": 0.842, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.238, "slope": 1.135, "slope_se": 0.051}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.166, "model_brier": 0.2314, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0278, "brier_diff_se": 0.0033, "model_logloss": 0.6593, "kalshi_logloss": 0.5895}, "fair_v1": {"n": 3362, "model": {"intercept": -0.401, "slope": 1.061, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.318, "slope": 1.177, "slope_se": 0.052}, "mean_extremity_model": 0.168, "mean_extremity_kalshi": 0.1659, "model_brier": 0.2122, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0086, "brier_diff_se": 0.0026, "model_logloss": 0.612, "kalshi_logloss": 0.5894}, "gen1_elo": {"n": 3362, "model": {"intercept": -0.391, "slope": 1.044, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.314, "slope": 1.163, "slope_se": 0.051}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.1664, "model_brier": 0.2111, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0075, "brier_diff_se": 0.0026, "model_logloss": 0.6101, "kalshi_logloss": 0.5892}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2424, "share_ge_15": 0.4354, "median_abs_gap": 12.95, "n": 22085}, "gen1_elo": {"share_ge_25": 0.2372, "share_ge_15": 0.4318, "median_abs_gap": 12.54, "n": 22085}, "gen1_sr": {"share_ge_25": 0.3045, "share_ge_15": 0.5184, "median_abs_gap": 15.64, "n": 22085}, "gen2": {"share_ge_25": 0.3079, "share_ge_15": 0.5069, "median_abs_gap": 15.37, "n": 22085}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1499, "share_ge_15": 0.3484, "median_abs_gap": 10.68, "n": 17122}, "gen1_elo": {"share_ge_25": 0.1484, "share_ge_15": 0.3418, "median_abs_gap": 10.19, "n": 17121}, "gen1_sr": {"share_ge_25": 0.2114, "share_ge_15": 0.4402, "median_abs_gap": 13.04, "n": 17122}, "gen2": {"share_ge_25": 0.2269, "share_ge_15": 0.4397, "median_abs_gap": 13.0, "n": 17123}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.67, "share_ge_25_all": 0.0351, "share_ge_25_pregame_clean": 0.0325}, "WTA": {"median_abs_gap_pregame_clean": 7.63, "share_ge_25_all": 0.0495, "share_ge_25_pregame_clean": 0.0445}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2398, "share_within_10pp_all": 0.4386, "share_within_10pp_pregame_clean": 0.4936, "corr_model_vs_mid_pregame_clean": 0.842}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 514, "model_brier": 0.1956, "kalshi_brier": 0.1968, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 595, "model_brier": 0.2155, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": 0.0089}, "15-25": {"n_settled": 731, "model_brier": 0.2271, "kalshi_brier": 0.2132, "brier_diff_model_minus_kalshi": 0.0139}, "25-40": {"n_settled": 414, "model_brier": 0.219, "kalshi_brier": 0.2106, "brier_diff_model_minus_kalshi": 0.0084}, "3-5": {"n_settled": 323, "model_brier": 0.1973, "kalshi_brier": 0.1966, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 84, "model_brier": 0.2967, "kalshi_brier": 0.1739, "brier_diff_model_minus_kalshi": 0.1228}, "5-10": {"n_settled": 701, "model_brier": 0.1988, "kalshi_brier": 0.1986, "brier_diff_model_minus_kalshi": 0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.529, "slope": 0.842, "slope_se": 0.044}, "kalshi_slope": {"intercept": 0.238, "slope": 1.135, "slope_se": 0.051}, "n": 3362}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.516, "slope": 0.886, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.153, "slope": 1.083, "slope_se": 0.038}, "n": 5372}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 337, "model_brier": 0.324, "kalshi_brier": 0.2339, "brier_diff_model_minus_kalshi": 0.0902, "brier_diff_se": 0.0171, "corr_model_outcome": 0.0142, "corr_kalshi_outcome": 0.2577}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
