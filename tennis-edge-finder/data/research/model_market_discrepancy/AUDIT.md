# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-18T11:09Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 38,842): 0-3 14.5%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 18.9%, 25-40 13.7%, 40+ 8.2%; median gap 11.86 pp.
* **Where the extremes live**: 97.6% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.8%, Challenger 12.2%, doubles 7.4%). Main tour: ATP 3.2% and WTA 5.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,472): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.3%, BOOK_QUALITY 19.2%, STALE_QUOTE 17.9%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.9%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 35.3%, execution 19.2%, market_freshness 17.9%, data 12.4%, market_freshness/coverage 8.5%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%.
* **Stale / settled / in-play**: 52.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,472 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 22.9% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 543.0 points vs 1840.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.045, Gen-2 0.838, Gen-1 ledger 0.874 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 385 model 0.2242 vs Kalshi 0.2076; n 80 model 0.3113 vs Kalshi 0.1698.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 161,430 model-market comparisons (263,776 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 58,390 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-18T10:57:46.222979+00:00'], shadow board 42,824 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-18T10:57:49.960556+00:00'], Model 4 18,716 rows, 15,830 settled tickers, 5,434 tickers with an external scan.
* By model: {"gen1_ledger": 39382, "gen1_elo": 21535, "fair_v1": 21535, "gen2": 21535, "gen1_sr": 21535, "model4_fundamental": 17961, "model4_conditioned": 17947}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 38,842 | 14.5 | 9.6 | 19.9 | 15.4 | 18.9 | 13.7 | 8.2 | 11.86 | 40.7% | 21.8% |
| MW fair_v1 | 21,535 | 13.6 | 8.5 | 18.5 | 15.9 | 19.2 | 14.5 | 9.8 | 12.95 | 43.5% | 24.3% |
| MW gen1_elo | 21,535 | 13.1 | 9.1 | 19.4 | 15.2 | 19.4 | 14.3 | 9.4 | 12.52 | 43.1% | 23.7% |
| MW gen1_ledger | 17,307 | 15.6 | 10.8 | 21.6 | 14.8 | 18.4 | 12.6 | 6.2 | 10.48 | 37.2% | 18.7% |
| MW gen1_sr | 21,535 | 9.7 | 7.4 | 16.6 | 14.2 | 21.5 | 18.5 | 12.0 | 15.71 | 52.0% | 30.4% |
| MW gen2 | 21,535 | 11.4 | 7.1 | 16.5 | 14.2 | 20.0 | 17.6 | 13.2 | 15.37 | 50.7% | 30.8% |
| all families model4_conditioned | 17,947 | 21.7 | 19.1 | 34.6 | 17.3 | 4.7 | 1.5 | 1.2 | 5.94 | 7.4% | 2.7% |
| all families model4_fundamental | 17,961 | 16.2 | 13.0 | 34.8 | 20.1 | 11.1 | 3.4 | 1.4 | 7.87 | 15.9% | 4.9% |

Configurable thresholds (primary): >=5pp 76.0%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.2%, >=25pp 21.8%, >=30pp 15.8%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.17pp; >=10pp 44.5%, >=25pp 16.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,766 | 29.4 | 13.5 | 24.4 | 17.3 | 11.7 | 3.1 | 0.7 | 6.19 | 15.4% | 3.7% |
| CHALLENGER | 3,561 | 15.9 | 10.1 | 20.2 | 15.8 | 14.3 | 12.4 | 11.2 | 11.17 | 37.9% | 23.6% |
| ITF_MEN | 5,907 | 11.0 | 8.0 | 17.4 | 14.9 | 19.9 | 16.2 | 12.4 | 14.47 | 48.6% | 28.6% |
| ITF_WOMEN | 8,410 | 10.3 | 6.7 | 15.8 | 15.6 | 22.3 | 18.2 | 11.1 | 15.62 | 51.6% | 29.3% |
| WTA | 1,231 | 19.1 | 12.3 | 25.4 | 18.4 | 19.2 | 4.8 | 0.9 | 8.17 | 24.9% | 5.7% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,766 | 23.5 | 14.4 | 24.5 | 18.2 | 14.2 | 4.2 | 1.0 | 6.9 | 19.4% | 5.2% |
| CHALLENGER | 3,561 | 14.8 | 8.1 | 19.1 | 13.6 | 18.1 | 14.3 | 12.0 | 12.73 | 44.3% | 26.2% |
| ITF_MEN | 5,907 | 9.3 | 6.7 | 15.7 | 13.6 | 19.8 | 19.3 | 15.5 | 16.94 | 54.6% | 34.8% |
| ITF_WOMEN | 8,410 | 8.4 | 5.6 | 13.7 | 13.5 | 21.2 | 20.8 | 16.8 | 18.83 | 58.8% | 37.6% |
| WTA | 1,231 | 17.4 | 7.8 | 20.2 | 16.2 | 22.8 | 14.7 | 1.0 | 11.62 | 38.4% | 15.7% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,766 | 25.5 | 13.8 | 25.6 | 17.0 | 13.6 | 3.7 | 0.7 | 6.62 | 18.0% | 4.4% |
| CHALLENGER | 3,561 | 15.0 | 10.2 | 20.7 | 14.9 | 15.6 | 12.1 | 11.5 | 11.08 | 39.2% | 23.6% |
| ITF_MEN | 5,907 | 10.0 | 8.1 | 17.9 | 14.2 | 20.8 | 16.6 | 12.4 | 14.97 | 49.8% | 29.0% |
| ITF_WOMEN | 8,410 | 9.7 | 6.9 | 16.3 | 15.6 | 22.9 | 18.2 | 10.3 | 15.57 | 51.5% | 28.5% |
| WTA | 1,231 | 23.5 | 16.9 | 30.9 | 15.1 | 11.1 | 1.9 | 0.6 | 6.01 | 13.6% | 2.5% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,109 | 27.9 | 20.3 | 31.8 | 11.4 | 6.2 | 2.2 | 0.1 | 5.11 | 8.6% | 2.3% |
| CHALLENGER | 2,491 | 22.2 | 15.3 | 26.7 | 14.2 | 13.9 | 5.9 | 2.0 | 7.03 | 21.7% | 7.8% |
| DOUBLES | 1,281 | 4.8 | 4.3 | 10.2 | 10.8 | 21.0 | 25.8 | 23.1 | 24.15 | 69.9% | 48.9% |
| ITF_MEN | 4,960 | 14.5 | 8.7 | 20.7 | 15.8 | 21.0 | 12.5 | 7.0 | 11.86 | 40.4% | 19.4% |
| ITF_WOMEN | 5,665 | 11.8 | 9.1 | 19.1 | 14.8 | 22.1 | 16.9 | 6.2 | 13.17 | 45.1% | 23.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 920 | 22.6 | 15.8 | 29.4 | 17.5 | 10.4 | 4.0 | 0.3 | 6.81 | 14.8% | 4.3% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,734 | 29.6 | 13.6 | 24.7 | 17.2 | 11.6 | 2.7 | 0.7 | 6.11 | 15.0% | 3.4% |
| CHALLENGER | 2,567 | 20.5 | 12.7 | 25.2 | 18.1 | 14.8 | 6.4 | 2.2 | 8.23 | 23.4% | 8.6% |
| ITF_MEN | 4,291 | 13.6 | 9.9 | 20.8 | 16.9 | 20.2 | 13.1 | 5.5 | 11.55 | 38.8% | 18.6% |
| ITF_WOMEN | 6,304 | 12.1 | 8.1 | 18.0 | 17.7 | 23.8 | 15.3 | 5.0 | 13.3 | 44.1% | 20.3% |
| WTA | 1,206 | 19.2 | 11.8 | 25.5 | 18.5 | 19.3 | 4.7 | 0.9 | 8.18 | 25.0% | 5.6% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,734 | 23.6 | 14.6 | 24.6 | 18.2 | 14.1 | 4.0 | 0.9 | 6.86 | 19.0% | 4.9% |
| CHALLENGER | 2,567 | 18.7 | 10.4 | 23.8 | 16.3 | 18.6 | 9.6 | 2.6 | 9.19 | 30.8% | 12.2% |
| ITF_MEN | 4,292 | 11.0 | 8.0 | 18.2 | 15.4 | 21.9 | 17.0 | 8.5 | 14.11 | 47.3% | 25.5% |
| ITF_WOMEN | 6,304 | 9.4 | 6.3 | 15.2 | 14.9 | 23.2 | 20.2 | 10.6 | 16.57 | 54.1% | 30.9% |
| WTA | 1,206 | 17.3 | 7.7 | 20.2 | 16.2 | 22.7 | 14.8 | 1.0 | 11.64 | 38.6% | 15.8% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,079 | 28.0 | 20.5 | 32.2 | 11.6 | 5.7 | 2.0 | 0.1 | 5.09 | 7.8% | 2.1% |
| CHALLENGER | 2,161 | 23.9 | 16.6 | 28.4 | 13.9 | 13.2 | 3.4 | 0.6 | 6.38 | 17.2% | 4.0% |
| DOUBLES | 1,189 | 4.8 | 4.5 | 10.4 | 11.0 | 20.9 | 25.9 | 22.5 | 24.07 | 69.3% | 48.4% |
| ITF_MEN | 4,108 | 15.9 | 9.4 | 22.5 | 16.7 | 20.7 | 10.6 | 4.1 | 10.61 | 35.4% | 14.7% |
| ITF_WOMEN | 4,697 | 12.7 | 9.7 | 20.7 | 15.7 | 22.3 | 15.5 | 3.4 | 11.88 | 41.2% | 18.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 882 | 23.0 | 16.2 | 29.6 | 17.5 | 10.5 | 3.2 | 0.0 | 6.68 | 13.7% | 3.2% |
| WTA125 | 622 | 23.6 | 15.6 | 23.5 | 19.6 | 12.7 | 4.7 | 0.3 | 7.08 | 17.7% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,281 | 4.8 | 4.3 | 10.2 | 10.8 | 21.0 | 25.8 | 23.1 | 24.15 | 69.9% | 48.9% |
| singles | 16,026 | 16.5 | 11.3 | 22.5 | 15.1 | 18.2 | 11.5 | 4.8 | 9.9 | 34.6% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,972 | 13.4 | 8.9 | 19.3 | 15.9 | 18.1 | 14.5 | 9.9 | 12.71 | 42.5% | 24.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 13,902 | 13.9 | 8.5 | 18.4 | 15.5 | 19.6 | 14.4 | 9.7 | 12.96 | 43.6% | 24.1% |
| UNKNOWN | 2,424 | 12.2 | 7.6 | 17.2 | 18.1 | 19.2 | 15.6 | 10.1 | 13.17 | 44.8% | 25.6% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,338 | 19.8 | 10.8 | 21.3 | 17.3 | 15.8 | 8.7 | 6.3 | 9.42 | 30.8% | 15.0% |
| B | 2,787 | 13.3 | 9.3 | 19.9 | 16.5 | 18.4 | 12.0 | 10.7 | 12.05 | 41.1% | 22.6% |
| C | 3,130 | 12.8 | 9.4 | 19.5 | 14.4 | 19.1 | 14.9 | 9.9 | 12.76 | 43.9% | 24.8% |
| D | 3,618 | 12.3 | 7.9 | 17.1 | 15.6 | 21.8 | 15.6 | 9.6 | 13.93 | 47.0% | 25.2% |
| F | 5,662 | 8.0 | 5.5 | 15.0 | 15.0 | 21.9 | 21.5 | 13.2 | 17.66 | 56.5% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,109 | 23.4 | 15.9 | 28.9 | 15.2 | 11.2 | 4.1 | 1.5 | 6.6 | 16.7% | 5.5% |
| B | 2,472 | 15.3 | 10.1 | 23.9 | 16.4 | 19.2 | 11.0 | 4.1 | 10.14 | 34.3% | 15.1% |
| C | 3,489 | 11.4 | 7.7 | 17.6 | 14.2 | 21.5 | 16.4 | 11.2 | 14.54 | 49.1% | 27.6% |
| D | 2,520 | 14.1 | 10.0 | 20.1 | 13.8 | 20.8 | 14.6 | 6.6 | 12.04 | 42.0% | 21.2% |
| F | 3,717 | 10.2 | 7.9 | 14.9 | 14.3 | 23.5 | 20.3 | 9.0 | 16.21 | 52.8% | 29.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,179 | 18.0 | 9.8 | 20.5 | 17.0 | 16.3 | 9.6 | 8.8 | 10.47 | 34.6% | 18.4% |
| LIMITED | 4,901 | 14.6 | 10.4 | 20.5 | 15.3 | 18.6 | 13.1 | 7.4 | 11.32 | 39.1% | 20.5% |
| POOR | 9,455 | 9.7 | 6.6 | 15.9 | 15.3 | 21.8 | 19.0 | 11.8 | 15.92 | 52.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,277 | 27.3 | 22.0 | 35.1 | 10.8 | 3.4 | 1.1 | 0.2 | 5.05 | 4.7% | 1.3% |
| GAME_SPREAD | 3,711 | 24.1 | 15.5 | 34.5 | 17.4 | 6.8 | 1.4 | 0.2 | 6.31 | 8.5% | 1.6% |
| MATCH_WINNER | 17,307 | 15.6 | 10.8 | 21.6 | 14.8 | 18.4 | 12.6 | 6.2 | 10.48 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,037 | 30.6 | 17.9 | 30.6 | 12.1 | 7.2 | 1.2 | 0.4 | 5.16 | 8.8% | 1.6% |
| TOTAL_GAMES | 6,026 | 7.0 | 8.8 | 37.1 | 28.8 | 11.4 | 3.6 | 3.1 | 9.67 | 18.2% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,300 | 24.9 | 35.1 | 32.0 | 3.5 | 3.6 | 0.7 | 0.2 | 4.47 | 4.5% | 0.8% |
| GAME_SPREAD | 4,342 | 46.0 | 16.8 | 27.4 | 7.2 | 1.7 | 0.7 | 0.3 | 3.44 | 2.6% | 1.0% |
| TOTAL_GAMES | 7,305 | 4.4 | 6.6 | 41.0 | 35.3 | 7.4 | 2.7 | 2.6 | 9.81 | 12.7% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,301 | 24.7 | 17.6 | 36.1 | 11.7 | 7.0 | 2.5 | 0.4 | 5.79 | 9.9% | 2.9% |
| GAME_SPREAD | 4,344 | 19.3 | 13.6 | 28.8 | 20.1 | 13.8 | 3.5 | 0.9 | 7.86 | 18.2% | 4.5% |
| TOTAL_GAMES | 7,316 | 7.1 | 8.6 | 37.2 | 27.4 | 13.0 | 4.1 | 2.7 | 9.69 | 19.8% | 6.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 21,535 | 43.5% | 24.3% | 12.95 | 34.8% | 15.0% | 10.66 |
| gen1_elo | 21,535 | 43.1% | 23.7% | 12.52 | 34.1% | 14.8% | 10.18 |
| gen1_sr | 21,535 | 52.0% | 30.4% | 15.71 | 44.2% | 21.2% | 13.12 |
| gen2 | 21,535 | 50.7% | 30.8% | 15.37 | 44.0% | 22.7% | 13.01 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 11,479 | 16.4 | 10.4 | 21.4 | 17.4 | 19.6 | 11.4 | 3.3 | 10.5 | 34.3% | 14.7% |
| STALE | 10,056 | 10.3 | 6.4 | 15.2 | 14.1 | 18.8 | 18.1 | 17.1 | 17.12 | 54.0% | 35.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 10,775 | 17.1 | 11.6 | 22.8 | 14.8 | 17.2 | 11.6 | 4.9 | 9.61 | 33.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 38,842 | 10775 | 14951 | 13116 | 23.7 | 139.0 | 1400.4 |
| ge_15pp | 15,805 | 3635 | 5225 | 6945 | 25.8 | 442.4 | 1380.4 |
| ge_25pp | 8,472 | 1778 | 2274 | 4420 | 32.8 | 582.7 | 1380.4 |
| lt_10pp | 17,059 | 5548 | 7172 | 4339 | 21.8 | 47.7 | 1341.5 |

Current slate `SL-20261018T110906Z-0fe71728`: 946 priced rows, quote age at build {'median': 11.9, 'max': 11.9}, freshness {'AGING': 946}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,991 | 21.4 | 10.7 | 23.1 | 19.0 | 18.6 | 6.8 | 0.5 | 8.73 | 25.9% | 7.3% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 346 | 70.2 | 29.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.09 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 704 | 0.0 | 3.0 | 35.5 | 28.8 | 23.3 | 8.7 | 0.7 | 11.87 | 32.7% | 9.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 21,535 | 3075 (14.3%) | 22.9% | 0.7% | {"EXTERNAL_STALE": 1991, "AGREES_WITH_KALSHI": 704, "ALL_AGREE": 346, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 9,371 | 755 (8.1%) | 30.5% | 1.2% | {"EXTERNAL_STALE": 516, "AGREES_WITH_KALSHI": 230, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,232 | 215 (4.1%) | 30.7% | 1.4% | {"EXTERNAL_STALE": 146, "AGREES_WITH_KALSHI": 66, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,518 | 203 (8.1%) | 31.5% | 1.5% | {"EXTERNAL_STALE": 136, "AGREES_WITH_KALSHI": 64, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,742 | 1739 (19.9%) | 15.6% | 0.7% | {"EXTERNAL_STALE": 1097, "ALL_AGREE": 346, "AGREES_WITH_KALSHI": 271, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,147 | 11.3 | 7.8 | 19.2 | 15.1 | 21.4 | 15.0 | 10.2 | 13.77 | 46.6% | 25.1% |
| 4-10x | 2,779 | 12.5 | 8.8 | 19.1 | 15.7 | 19.3 | 15.1 | 9.4 | 12.92 | 43.8% | 24.5% |
| <2x | 11,221 | 15.5 | 9.3 | 19.0 | 16.8 | 17.7 | 12.7 | 8.8 | 11.79 | 39.3% | 21.6% |
| >=10x | 3,388 | 10.8 | 6.4 | 15.3 | 13.9 | 21.3 | 19.5 | 12.7 | 16.38 | 53.5% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,623 | 13.1 | 8.5 | 19.4 | 15.9 | 19.6 | 13.2 | 10.3 | 12.82 | 43.1% | 23.5% |
| 300-1000 | 4,775 | 12.3 | 8.8 | 17.1 | 15.8 | 20.5 | 16.1 | 9.4 | 13.68 | 46.1% | 25.6% |
| <300 | 6,441 | 9.1 | 5.9 | 15.5 | 14.9 | 21.7 | 20.0 | 12.8 | 16.81 | 54.6% | 32.9% |
| >=3000 | 4,696 | 21.6 | 11.9 | 22.9 | 17.3 | 14.0 | 7.0 | 5.3 | 8.23 | 26.2% | 12.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 648 | 0.5389 | 0.4055 | 0.4846 | +0.054 | -0.079 | 0.0012 ± 0.0059 |
| ratio 4-10x | 433 | 0.5845 | 0.4465 | 0.5035 | +0.081 | -0.057 | 0.0094 ± 0.0075 |
| ratio <2x | 1622 | 0.5374 | 0.416 | 0.4501 | +0.087 | -0.034 | 0.0129 ± 0.0035 |
| ratio >=10x | 533 | 0.5503 | 0.3805 | 0.4259 | +0.124 | -0.045 | 0.0166 ± 0.0078 |
| thinner_sample 1000-3000 | 917 | 0.5437 | 0.4181 | 0.4635 | +0.080 | -0.045 | 0.0076 ± 0.0047 |
| thinner_sample 300-1000 | 759 | 0.5616 | 0.4229 | 0.4862 | +0.075 | -0.063 | 0.0027 ± 0.0056 |
| thinner_sample <300 | 997 | 0.5454 | 0.3844 | 0.4353 | +0.110 | -0.051 | 0.0175 ± 0.0055 |
| thinner_sample >=3000 | 563 | 0.5303 | 0.4371 | 0.4636 | +0.067 | -0.026 | 0.0144 ± 0.0049 |
| data_status ADEQUATE | 959 | 0.5335 | 0.4293 | 0.4578 | +0.076 | -0.029 | 0.0108 ± 0.004 |
| data_status LIMITED | 803 | 0.553 | 0.4238 | 0.4869 | +0.066 | -0.063 | 0.0041 ± 0.0052 |
| data_status POOR | 1474 | 0.5506 | 0.3946 | 0.4471 | +0.103 | -0.052 | 0.0142 ± 0.0044 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 499 | 0.1934 | 0.1947 | -0.0013 ± 0.0007 | 0.565 | 0.5678 | 0.4947 | 0.4799 | 0.5291 | -0.044 ± 0.0206 | -0.01 (5) |
| 3-5 | 315 | 0.1965 | 0.1959 | +0.0006 ± 0.002 | 0.5745 | 0.5717 | 0.507 | 0.4671 | 0.4794 | -0.082 ± 0.0256 | 0.02 (1) |
| 5-10 | 682 | 0.1987 | 0.1983 | +0.0004 ± 0.0026 | 0.5831 | 0.5802 | 0.5114 | 0.4369 | 0.4663 | -0.084 ± 0.0176 | -0.0167 (6) |
| 10-15 | 572 | 0.215 | 0.2053 | +0.0097 ± 0.0048 | 0.6203 | 0.5927 | 0.5199 | 0.3959 | 0.4178 | -0.091 ± 0.019 | -0.048 (5) |
| 15-25 | 703 | 0.2295 | 0.213 | +0.0164 ± 0.0068 | 0.6535 | 0.6113 | 0.5767 | 0.3818 | 0.4381 | -0.086 ± 0.0174 | -0.0033 (9) |
| 25-40 | 385 | 0.2242 | 0.2076 | +0.0166 ± 0.0139 | 0.6374 | 0.5976 | 0.6481 | 0.3395 | 0.4675 | -0.062 ± 0.0211 | -0.01 (1) |
| 40+ | 80 | 0.3113 | 0.1698 | +0.1415 ± 0.0418 | 0.8377 | 0.5117 | 0.7438 | 0.294 | 0.3625 | -0.127 ± 0.0406 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2330 | 0.1809 | 0.1821 | -0.0012 ± 0.0003 | 0.5368 | 0.5381 | 0.4789 | 0.4639 | 0.4991 | -0.019 ± 0.009 | -0.0129 (17) |
| 3-5 | 1471 | 0.1935 | 0.1914 | +0.0021 ± 0.0009 | 0.5676 | 0.5583 | 0.4808 | 0.4411 | 0.433 | -0.065 ± 0.0116 | 0.0 (2) |
| 5-10 | 3158 | 0.1949 | 0.1923 | +0.0026 ± 0.0012 | 0.5728 | 0.5639 | 0.4831 | 0.4093 | 0.4269 | -0.046 ± 0.0079 | -0.0119 (21) |
| 10-15 | 2776 | 0.2026 | 0.183 | +0.0196 ± 0.002 | 0.5933 | 0.5386 | 0.482 | 0.3573 | 0.3415 | -0.078 ± 0.0081 | -0.0281 (16) |
| 15-25 | 3369 | 0.2089 | 0.1704 | +0.0386 ± 0.0028 | 0.6097 | 0.5043 | 0.5019 | 0.3058 | 0.3069 | -0.070 ± 0.0071 | -0.0025 (44) |
| 25-40 | 2637 | 0.2225 | 0.125 | +0.0974 ± 0.0043 | 0.6386 | 0.3865 | 0.5291 | 0.2158 | 0.2211 | -0.064 ± 0.0066 | -0.01 (1) |
| 40+ | 1800 | 0.3793 | 0.0419 | +0.3374 ± 0.0054 | 0.987 | 0.1679 | 0.6272 | 0.1054 | 0.0533 | -0.088 ± 0.0045 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 371 | 0.1993 | 0.1997 | -0.0004 ± 0.0008 | 0.5802 | 0.5812 | 0.5013 | 0.4863 | 0.5067 | -0.080 ± 0.0244 | -0.01 (3) |
| 3-5 | 261 | 0.2135 | 0.2122 | +0.0013 ± 0.0023 | 0.6099 | 0.6082 | 0.5161 | 0.4762 | 0.4751 | -0.090 ± 0.0303 | 0.02 (1) |
| 5-10 | 590 | 0.1992 | 0.1989 | +0.0002 ± 0.0028 | 0.582 | 0.5814 | 0.5477 | 0.4728 | 0.5085 | -0.071 ± 0.0189 | -0.01 (4) |
| 10-15 | 533 | 0.2199 | 0.2109 | +0.0091 ± 0.005 | 0.6304 | 0.6079 | 0.5679 | 0.4435 | 0.4728 | -0.097 ± 0.0209 | -0.04 (5) |
| 15-25 | 773 | 0.2291 | 0.2076 | +0.0215 ± 0.0065 | 0.6499 | 0.5976 | 0.5882 | 0.3918 | 0.4386 | -0.090 ± 0.0166 | -0.0133 (9) |
| 25-40 | 516 | 0.2689 | 0.1955 | +0.0734 ± 0.0123 | 0.749 | 0.5714 | 0.6601 | 0.3451 | 0.3876 | -0.121 ± 0.0194 | -0.0075 (4) |
| 40+ | 192 | 0.3677 | 0.1772 | +0.1905 ± 0.0302 | 1.0243 | 0.5254 | 0.742 | 0.2582 | 0.3177 | -0.073 ± 0.0294 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1970 | 0.1849 | 0.1853 | -0.0004 ± 0.0003 | 0.5455 | 0.5462 | 0.5024 | 0.4877 | 0.5086 | -0.034 ± 0.01 | -0.0133 (15) |
| 3-5 | 1243 | 0.1956 | 0.1943 | +0.0012 ± 0.001 | 0.5667 | 0.5636 | 0.5154 | 0.4755 | 0.4787 | -0.048 ± 0.0128 | 0.02 (1) |
| 5-10 | 2823 | 0.1921 | 0.1896 | +0.0025 ± 0.0012 | 0.5669 | 0.558 | 0.5096 | 0.4356 | 0.4573 | -0.040 ± 0.0083 | -0.0117 (6) |
| 10-15 | 2433 | 0.2003 | 0.1881 | +0.0122 ± 0.0022 | 0.5896 | 0.5489 | 0.5204 | 0.3958 | 0.4118 | -0.052 ± 0.009 | -0.0189 (18) |
| 15-25 | 3511 | 0.2173 | 0.1768 | +0.0405 ± 0.0028 | 0.6298 | 0.5217 | 0.5322 | 0.336 | 0.3335 | -0.075 ± 0.0072 | -0.0086 (42) |
| 25-40 | 3113 | 0.2507 | 0.1348 | +0.1160 ± 0.0042 | 0.708 | 0.4149 | 0.5598 | 0.244 | 0.22 | -0.091 ± 0.0066 | -0.0044 (18) |
| 40+ | 2448 | 0.4031 | 0.0656 | +0.3375 ± 0.006 | 1.0644 | 0.2299 | 0.6634 | 0.1256 | 0.094 | -0.070 ± 0.0051 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 479 | 0.1956 | 0.1978 | -0.0021 ± 0.0007 | 0.5717 | 0.5768 | 0.4988 | 0.4835 | 0.547 | -0.018 ± 0.0207 | -0.0137 (8) |
| 3-5 | 357 | 0.1909 | 0.189 | +0.0019 ± 0.0019 | 0.5588 | 0.5543 | 0.4983 | 0.4587 | 0.4566 | -0.112 ± 0.0241 | 0.0067 (3) |
| 5-10 | 712 | 0.2016 | 0.1976 | +0.0040 ± 0.0025 | 0.5904 | 0.5775 | 0.504 | 0.4302 | 0.4368 | -0.097 ± 0.0171 | -0.0071 (7) |
| 10-15 | 561 | 0.2087 | 0.2066 | +0.0021 ± 0.0047 | 0.6055 | 0.5966 | 0.5379 | 0.415 | 0.4706 | -0.069 ± 0.019 | -0.0317 (6) |
| 15-25 | 650 | 0.2348 | 0.2095 | +0.0253 ± 0.007 | 0.6694 | 0.603 | 0.5851 | 0.3918 | 0.4215 | -0.111 ± 0.0178 | -0.03 (1) |
| 25-40 | 400 | 0.2108 | 0.2132 | -0.0024 ± 0.0135 | 0.6081 | 0.6101 | 0.6534 | 0.3439 | 0.5 | -0.042 ± 0.0206 | 0.015 (2) |
| 40+ | 77 | 0.3303 | 0.183 | +0.1473 ± 0.0445 | 0.8835 | 0.5422 | 0.7475 | 0.2925 | 0.3636 | -0.113 ± 0.0461 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2224 | 0.1878 | 0.1885 | -0.0007 ± 0.0003 | 0.5528 | 0.5541 | 0.4862 | 0.4709 | 0.4928 | -0.030 ± 0.0093 | -0.0163 (35) |
| 3-5 | 1542 | 0.1877 | 0.1843 | +0.0033 ± 0.0009 | 0.5531 | 0.545 | 0.478 | 0.4385 | 0.417 | -0.083 ± 0.0112 | -0.0094 (18) |
| 5-10 | 3375 | 0.1947 | 0.1881 | +0.0066 ± 0.0011 | 0.5746 | 0.5529 | 0.4812 | 0.4073 | 0.3976 | -0.069 ± 0.0075 | -0.01 (31) |
| 10-15 | 2616 | 0.1978 | 0.1816 | +0.0162 ± 0.0021 | 0.581 | 0.5329 | 0.4984 | 0.375 | 0.3716 | -0.069 ± 0.0083 | -0.015 (12) |
| 15-25 | 3476 | 0.2079 | 0.169 | +0.0389 ± 0.0027 | 0.6094 | 0.5014 | 0.5045 | 0.3096 | 0.3075 | -0.071 ± 0.007 | -0.03 (2) |
| 25-40 | 2584 | 0.2175 | 0.1234 | +0.0941 ± 0.0044 | 0.6272 | 0.381 | 0.526 | 0.2099 | 0.2233 | -0.060 ± 0.0066 | 0.01 (3) |
| 40+ | 1724 | 0.3948 | 0.046 | +0.3488 ± 0.0058 | 1.0291 | 0.1787 | 0.6385 | 0.1099 | 0.0557 | -0.089 ± 0.0049 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 828 | 0.1955 | 0.1955 | -0.0001 ± 0.0005 | 0.5714 | 0.5713 | 0.5081 | 0.493 | 0.4952 | -0.054 ± 0.0155 | -0.0224 (49) |
| 3-5 | 582 | 0.1947 | 0.194 | +0.0007 ± 0.0015 | 0.5678 | 0.5649 | 0.4797 | 0.4399 | 0.4485 | -0.051 ± 0.0184 | -0.0194 (34) |
| 5-10 | 1221 | 0.1984 | 0.1923 | +0.0061 ± 0.0019 | 0.5842 | 0.5666 | 0.4889 | 0.4154 | 0.412 | -0.066 ± 0.0128 | -0.005 (78) |
| 10-15 | 776 | 0.2075 | 0.196 | +0.0115 ± 0.004 | 0.6034 | 0.5736 | 0.5071 | 0.3841 | 0.3982 | -0.057 ± 0.016 | 0.0014 (64) |
| 15-25 | 1033 | 0.2334 | 0.2121 | +0.0214 ± 0.0056 | 0.6652 | 0.6103 | 0.5664 | 0.3714 | 0.4153 | -0.056 ± 0.0144 | -0.0214 (59) |
| 25-40 | 603 | 0.2476 | 0.1967 | +0.0508 ± 0.0111 | 0.6994 | 0.5714 | 0.6506 | 0.3384 | 0.4113 | -0.080 ± 0.0168 | -0.0219 (26) |
| 40+ | 202 | 0.3763 | 0.1902 | +0.1862 ± 0.0313 | 1.0849 | 0.561 | 0.7945 | 0.3032 | 0.3812 | -0.083 ± 0.028 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2512 | 0.1876 | 0.1876 | -0.0000 ± 0.0003 | 0.551 | 0.55 | 0.5044 | 0.4891 | 0.4976 | -0.036 ± 0.0086 | -0.0157 (88) |
| 3-5 | 1725 | 0.1905 | 0.1881 | +0.0024 ± 0.0008 | 0.5567 | 0.5512 | 0.4864 | 0.4467 | 0.4371 | -0.056 ± 0.0105 | -0.0209 (69) |
| 5-10 | 3469 | 0.195 | 0.1869 | +0.0081 ± 0.0011 | 0.5754 | 0.5524 | 0.4842 | 0.4106 | 0.3952 | -0.067 ± 0.0074 | -0.0082 (132) |
| 10-15 | 2367 | 0.2049 | 0.1896 | +0.0153 ± 0.0022 | 0.5984 | 0.5578 | 0.5106 | 0.3877 | 0.387 | -0.059 ± 0.0089 | -0.0053 (105) |
| 15-25 | 2936 | 0.2293 | 0.1974 | +0.0319 ± 0.0032 | 0.661 | 0.5745 | 0.5581 | 0.3627 | 0.3804 | -0.060 ± 0.0083 | -0.0253 (107) |
| 25-40 | 1990 | 0.2523 | 0.17 | +0.0823 ± 0.0058 | 0.7151 | 0.5029 | 0.6109 | 0.297 | 0.3256 | -0.075 ± 0.0089 | -0.0229 (51) |
| 40+ | 951 | 0.3895 | 0.1297 | +0.2598 ± 0.0125 | 1.103 | 0.3976 | 0.711 | 0.2046 | 0.2145 | -0.075 ± 0.0111 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3236 | 1.045 ± 0.049 | 1.166 | 0.1678 | 0.1697 | 0.2131 | 0.2024 |
| gen2 | 3236 | 0.838 ± 0.045 | 1.122 | 0.1745 | 0.1697 | 0.232 | 0.2023 |
| gen1_elo | 3236 | 1.037 ± 0.048 | 1.15 | 0.1732 | 0.1701 | 0.2117 | 0.2022 |
| gen1_sr | 3236 | 1.03 ± 0.058 | 1.182 | 0.1344 | 0.1714 | 0.2279 | 0.2021 |
| gen1_ledger | 5245 | 0.874 ± 0.034 | 1.078 | 0.1774 | 0.1843 | 0.2183 | 0.1979 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 15,805)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,775 | 23.9% |
| STALE_QUOTE | market_freshness | 3,237 | 20.5% |
| BOOK_QUALITY | execution | 3,081 | 19.5% |
| POOR_DATA | data | 1,728 | 10.9% |
| LIMITED_DATA | data | 1,099 | 7.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 827 | 5.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 770 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 640 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 446 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 202 | 1.3% |

Cause class: coverage 23.9%, market_freshness 20.5%, execution 19.5%, data 17.9%, market_freshness/coverage 8.1%, model_calibration_or_unknown 4.9%, mapping 4.0%, model_calibration 1.3%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.7%, START_UNVERIFIABLE 94.9%, LOW_DATA_QUALITY 69.7%, THIN_PLAYER_HISTORY 57.9%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 43.9%, MODEL_INTERNAL_DISAGREEMENT 40.1%, ASYMMETRIC_SAMPLE_SIZE 32.1%, WIDE_SPREAD 25.4%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.8%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.5%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.2%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.3%, POST_SETTLEMENT_OBSERVATION 23.9%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,472)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,988 | 35.3% |
| BOOK_QUALITY | execution | 1,624 | 19.2% |
| STALE_QUOTE | market_freshness | 1,515 | 17.9% |
| POOR_DATA | data | 725 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 442 | 5.2% |
| IDENTITY_AMBIGUOUS | mapping | 368 | 4.3% |
| LIMITED_DATA | data | 327 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 277 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 163 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 43 | 0.5% |

Cause class: coverage 35.3%, execution 19.2%, market_freshness 17.9%, data 12.4%, market_freshness/coverage 8.5%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.8%, START_UNVERIFIABLE 97.6%, LOW_DATA_QUALITY 73.6%, THIN_PLAYER_HISTORY 60.3%, STALE_KALSHI_QUOTE 52.2%, STALE_PLAYER_DATA 47.6%, MODEL_INTERNAL_DISAGREEMENT 41.0%, ASYMMETRIC_SAMPLE_SIZE 33.9%, WIDE_SPREAD 25.3%, PLAYER_IDENTITY_RISK 18.1%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 10.2%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.1%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.1%, POST_SETTLEMENT_OBSERVATION 35.3%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6723, "IDENTITY_AMBIGUOUS": 1749}; ticker orientation: {"VERIFIED": 8472}.

Checks: discipline:AMBIGUOUS 626, discipline:PASS 7846, identity_confidence:AMBIGUOUS 1536, identity_confidence:PASS 6936, level_mapping:NA 638, level_mapping:PASS 7834, market_pair:AMBIGUOUS 298, market_pair:NA 209, market_pair:PASS 7965, model_complement:NA 176, model_complement:PASS 8296, namesake:PASS 8472, physical_match_id:NA 3240, physical_match_id:PASS 5232, player_ids:PASS 8472, same_pair_other_event:PASS 8472, ticker_orientation:PASS 8472

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,875 | 3.2% | 2.9% | 1.1% | {"market_freshness": 34, "data": 23, "execution": 13, "market_freshness/coverage": 8, "model_calibration_or_unknown": 8, "model_calibration": 4, "coverage": 2} | 5.63 | 0.2102 / 0.2058 (301) | 17.1% | 2.9% | 4.3% | 2.2% |
| CHALLENGER | 6,052 | 17.1% | 6.5% | 12.2% | {"coverage": 599, "market_freshness": 129, "market_freshness/coverage": 129, "data": 90, "model_calibration_or_unknown": 46, "execution": 24, "model_calibration": 9, "mapping": 9} | 7.2 | 0.2179 / 0.205 (1502) | 36.1% | 13.2% | 2.8% | 21.9% |
| DOUBLES | 1,281 | 48.9% | 48.4% | 7.4% | {"execution": 302, "mapping": 168, "market_freshness": 106, "market_freshness/coverage": 43, "coverage": 7} | 24.07 | 0.3238 / 0.2338 (336) | 18.3% | 0.0% | 100.0% | 7.2% |
| ITF_MEN | 10,867 | 24.4% | 16.7% | 31.3% | {"coverage": 1042, "execution": 539, "market_freshness": 407, "data": 357, "market_freshness/coverage": 210, "mapping": 98, "model_calibration_or_unknown": 2} | 11.13 | 0.2131 / 0.1944 (2634) | 36.3% | 61.8% | 13.2% | 22.7% |
| ITF_WOMEN | 14,075 | 26.8% | 19.7% | 44.5% | {"coverage": 1321, "market_freshness": 763, "execution": 716, "data": 548, "market_freshness/coverage": 280, "mapping": 87, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.73 | 0.2038 / 0.1918 (2821) | 38.4% | 57.5% | 10.2% | 21.8% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,151 | 5.1% | 4.6% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 16, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.5 | 0.2403 / 0.2336 (361) | 23.2% | 1.6% | 1.7% | 2.9% |
| WTA125 | 1,392 | 12.5% | 9.9% | 2.1% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.2192 / 0.2076 (484) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 34 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 35 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 36 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 37 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 38 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
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

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9762, "by_level_share_of_ge_25pp": {"ATP": 0.0109, "CHALLENGER": 0.1222, "DOUBLES": 0.0739, "ITF_MEN": 0.3134, "ITF_WOMEN": 0.4448, "OTHER": 0.0014, "WTA": 0.013, "WTA125": 0.0205}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5217, "share_primary_cause_market_settled_or_in_play": 0.4376, "share_primary_cause_stale_quote_only": 0.1788}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8472, "identity_ambiguous_share": 0.2064, "ticker_orientation": {"VERIFIED": 8472}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5232, "with_external": 215, "coverage": 0.0411, "external_status": {"EXTERNAL_STALE": 146, "AGREES_WITH_KALSHI": 66, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 146, "MODEL_LONE_OUTLIER": 66, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.307, "share_external_supports_model": 0.014}, "pregame_clean_ge_25pp": {"n": 2518, "with_external": 203, "coverage": 0.0806, "external_status": {"EXTERNAL_STALE": 136, "AGREES_WITH_KALSHI": 64, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 136, "MODEL_LONE_OUTLIER": 64, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3153, "share_external_supports_model": 0.0148}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 543.0, "median_sample_ratio": 2.43, "median_min_matches": 21.0, "median_max_days_since_last": 213.0, "share_severe_asymmetry": 0.2055, "data_status": {"POOR": 4545, "LIMITED": 2422, "ADEQUATE": 1505}, "comparison_lt_10pp": {"median_thinner_serve_points": 1840.0, "median_sample_ratio": 1.67, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 648, "model_minus_observed": 0.0543, "kalshi_minus_observed": -0.0791, "brier_diff_model_minus_kalshi": 0.0012}, "4-10x": {"n": 433, "model_minus_observed": 0.081, "kalshi_minus_observed": -0.057, "brier_diff_model_minus_kalshi": 0.0094}, "<2x": {"n": 1622, "model_minus_observed": 0.0873, "kalshi_minus_observed": -0.034, "brier_diff_model_minus_kalshi": 0.0129}, ">=10x": {"n": 533, "model_minus_observed": 0.1244, "kalshi_minus_observed": -0.0454, "brier_diff_model_minus_kalshi": 0.0166}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3236, "model": {"intercept": -0.553, "slope": 0.838, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.208, "slope": 1.122, "slope_se": 0.051}, "mean_extremity_model": 0.1745, "mean_extremity_kalshi": 0.1697, "model_brier": 0.232, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.0297, "brier_diff_se": 0.0033, "model_logloss": 0.6611, "kalshi_logloss": 0.5868}, "fair_v1": {"n": 3236, "model": {"intercept": -0.413, "slope": 1.045, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.293, "slope": 1.166, "slope_se": 0.052}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1697, "model_brier": 0.2131, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.0107, "brier_diff_se": 0.0027, "model_logloss": 0.6141, "kalshi_logloss": 0.5868}, "gen1_elo": {"n": 3236, "model": {"intercept": -0.41, "slope": 1.037, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.283, "slope": 1.15, "slope_se": 0.051}, "mean_extremity_model": 0.1732, "mean_extremity_kalshi": 0.1701, "model_brier": 0.2117, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0094, "brier_diff_se": 0.0027, "model_logloss": 0.6118, "kalshi_logloss": 0.5865}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.243, "share_ge_15": 0.4352, "median_abs_gap": 12.95, "n": 21535}, "gen1_elo": {"share_ge_25": 0.237, "share_ge_15": 0.431, "median_abs_gap": 12.52, "n": 21535}, "gen1_sr": {"share_ge_25": 0.3045, "share_ge_15": 0.5198, "median_abs_gap": 15.71, "n": 21535}, "gen2": {"share_ge_25": 0.3075, "share_ge_15": 0.5072, "median_abs_gap": 15.37, "n": 21535}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1504, "share_ge_15": 0.3483, "median_abs_gap": 10.66, "n": 16736}, "gen1_elo": {"share_ge_25": 0.1482, "share_ge_15": 0.3408, "median_abs_gap": 10.18, "n": 16735}, "gen1_sr": {"share_ge_25": 0.212, "share_ge_15": 0.4425, "median_abs_gap": 13.12, "n": 16736}, "gen2": {"share_ge_25": 0.2272, "share_ge_15": 0.4402, "median_abs_gap": 13.01, "n": 16737}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.63, "share_ge_25_all": 0.032, "share_ge_25_pregame_clean": 0.0292}, "WTA": {"median_abs_gap_pregame_clean": 7.5, "share_ge_25_all": 0.0511, "share_ge_25_pregame_clean": 0.046}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2404, "share_within_10pp_all": 0.4392, "share_within_10pp_pregame_clean": 0.4942, "corr_model_vs_mid_pregame_clean": 0.8424}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 499, "model_brier": 0.1934, "kalshi_brier": 0.1947, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 572, "model_brier": 0.215, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 703, "model_brier": 0.2295, "kalshi_brier": 0.213, "brier_diff_model_minus_kalshi": 0.0164}, "25-40": {"n_settled": 385, "model_brier": 0.2242, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": 0.0166}, "3-5": {"n_settled": 315, "model_brier": 0.1965, "kalshi_brier": 0.1959, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 80, "model_brier": 0.3113, "kalshi_brier": 0.1698, "brier_diff_model_minus_kalshi": 0.1415}, "5-10": {"n_settled": 682, "model_brier": 0.1987, "kalshi_brier": 0.1983, "brier_diff_model_minus_kalshi": 0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.553, "slope": 0.838, "slope_se": 0.045}, "kalshi_slope": {"intercept": 0.208, "slope": 1.122, "slope_se": 0.051}, "n": 3236}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.517, "slope": 0.874, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.14, "slope": 1.078, "slope_se": 0.038}, "n": 5245}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 336, "model_brier": 0.3238, "kalshi_brier": 0.2338, "brier_diff_model_minus_kalshi": 0.09, "brier_diff_se": 0.0171, "corr_model_outcome": 0.0133, "corr_kalshi_outcome": 0.2592}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
