# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-11T13:27Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 29,198): 0-3 14.6%, 3-5 9.7%, 5-10 20.2%, 10-15 15.4%, 15-25 18.4%, 25-40 13.5%, 40+ 8.2%; median gap 11.67 pp.
* **Where the extremes live**: 98.1% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.4%, Challenger 12.1%, doubles 7.2%). Main tour: ATP 1.4% and WTA 6.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,332): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.1%, BOOK_QUALITY 17.5%, STALE_QUOTE 16.1%, POOR_DATA 7.8%, POSSIBLY_IN_PLAY_QUOTE 5.7%, LIMITED_DATA 4.3%, IDENTITY_AMBIGUOUS 3.7%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 39.1%, execution 17.5%, market_freshness 16.1%, data 12.1%, market_freshness/coverage 9.2%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.4%.
* **Stale / settled / in-play**: 54.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,332 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.7%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 20.1% of the time and with the model 0.5%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 623.0 points vs 1937.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.072, Gen-2 0.873, Gen-1 ledger 0.871 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 265 model 0.2199 vs Kalshi 0.1977; n 58 model 0.3011 vs Kalshi 0.1684.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA125. Not implemented here.

## 1. Observations

* 116,074 model-market comparisons (190,701 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 43,727 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-11T13:22:46.891810+00:00'], shadow board 30,618 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-11T13:22:49.336947+00:00'], Model 4 13,018 rows, 12,628 settled tickers, 3,532 tickers with an external scan.
* By model: {"gen1_ledger": 28805, "gen1_elo": 15386, "fair_v1": 15386, "gen2": 15386, "gen1_sr": 15386, "model4_fundamental": 12867, "model4_conditioned": 12858}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 29,198 | 14.6 | 9.7 | 20.2 | 15.4 | 18.4 | 13.5 | 8.2 | 11.67 | 40.1% | 21.7% |
| MW fair_v1 | 15,386 | 13.9 | 8.7 | 18.7 | 16.1 | 18.4 | 14.4 | 9.8 | 12.69 | 42.6% | 24.2% |
| MW gen1_elo | 15,386 | 13.4 | 9.0 | 20.3 | 15.0 | 18.7 | 14.3 | 9.3 | 12.16 | 42.3% | 23.6% |
| MW gen1_ledger | 13,812 | 15.4 | 10.7 | 21.8 | 14.6 | 18.5 | 12.5 | 6.4 | 10.48 | 37.4% | 18.9% |
| MW gen1_sr | 15,386 | 10.2 | 7.8 | 16.6 | 14.5 | 21.6 | 17.9 | 11.5 | 15.37 | 50.9% | 29.3% |
| MW gen2 | 15,386 | 12.1 | 7.3 | 16.4 | 14.2 | 20.1 | 16.9 | 12.9 | 14.95 | 49.9% | 29.8% |
| all families model4_conditioned | 12,858 | 21.9 | 20.2 | 35.8 | 16.0 | 4.2 | 1.0 | 0.9 | 5.76 | 6.1% | 1.9% |
| all families model4_fundamental | 12,867 | 16.7 | 13.3 | 35.9 | 19.8 | 10.6 | 2.6 | 1.2 | 7.62 | 14.3% | 3.7% |

Configurable thresholds (primary): >=5pp 75.7%, >=10pp 55.5%, >=15pp 40.1%, >=20pp 29.9%, >=25pp 21.7%, >=30pp 15.9%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.25pp; >=10pp 44.8%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,257 | 30.6 | 14.3 | 24.8 | 17.4 | 10.8 | 1.1 | 0.9 | 5.84 | 12.8% | 2.0% |
| CHALLENGER | 2,669 | 15.9 | 10.3 | 19.7 | 15.9 | 14.2 | 12.4 | 11.5 | 11.62 | 38.1% | 23.9% |
| ITF_MEN | 4,300 | 11.6 | 8.7 | 18.3 | 14.8 | 19.1 | 15.3 | 12.3 | 13.74 | 46.6% | 27.5% |
| ITF_WOMEN | 5,966 | 10.2 | 6.6 | 16.0 | 16.3 | 21.5 | 18.6 | 10.7 | 15.41 | 50.9% | 29.4% |
| WTA | 749 | 22.3 | 10.8 | 25.2 | 16.7 | 17.5 | 6.0 | 1.5 | 7.82 | 25.0% | 7.5% |
| WTA125 | 445 | 13.0 | 8.5 | 23.6 | 21.6 | 16.9 | 14.6 | 1.8 | 11.03 | 33.3% | 16.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,257 | 24.0 | 14.4 | 24.7 | 18.9 | 15.0 | 1.9 | 1.0 | 6.9 | 17.9% | 2.9% |
| CHALLENGER | 2,669 | 15.6 | 7.5 | 19.2 | 13.1 | 18.4 | 13.9 | 12.3 | 12.84 | 44.6% | 26.2% |
| ITF_MEN | 4,300 | 10.3 | 7.4 | 16.8 | 14.7 | 19.9 | 17.7 | 13.2 | 15.41 | 50.8% | 30.9% |
| ITF_WOMEN | 5,966 | 8.9 | 5.9 | 12.8 | 12.8 | 21.6 | 20.8 | 17.1 | 19.08 | 59.6% | 37.9% |
| WTA | 749 | 20.0 | 8.1 | 18.2 | 15.5 | 21.4 | 15.3 | 1.5 | 11.5 | 38.2% | 16.8% |
| WTA125 | 445 | 4.9 | 3.8 | 18.6 | 20.0 | 24.5 | 18.0 | 10.1 | 16.74 | 52.6% | 28.1% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,257 | 27.1 | 14.2 | 29.6 | 15.0 | 10.6 | 2.5 | 0.9 | 6.23 | 14.1% | 3.5% |
| CHALLENGER | 2,669 | 15.4 | 10.4 | 20.5 | 15.5 | 14.9 | 11.9 | 11.4 | 10.86 | 38.2% | 23.3% |
| ITF_MEN | 4,300 | 10.5 | 8.8 | 19.0 | 13.7 | 19.9 | 15.7 | 12.4 | 14.02 | 48.0% | 28.1% |
| ITF_WOMEN | 5,966 | 9.8 | 6.7 | 16.7 | 15.7 | 22.7 | 18.9 | 9.6 | 15.51 | 51.2% | 28.5% |
| WTA | 749 | 22.3 | 14.7 | 33.8 | 15.5 | 10.2 | 2.7 | 0.9 | 6.35 | 13.8% | 3.6% |
| WTA125 | 445 | 24.0 | 10.3 | 30.6 | 15.5 | 12.8 | 6.3 | 0.5 | 7.5 | 19.6% | 6.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 691 | 30.8 | 22.7 | 35.6 | 9.1 | 1.3 | 0.4 | 0.0 | 4.7 | 1.7% | 0.4% |
| CHALLENGER | 1,829 | 22.5 | 16.2 | 26.6 | 14.7 | 13.0 | 5.1 | 1.9 | 6.8 | 20.0% | 6.9% |
| DOUBLES | 907 | 4.5 | 3.2 | 11.2 | 11.2 | 19.4 | 24.8 | 25.6 | 25.42 | 69.8% | 50.4% |
| ITF_MEN | 4,124 | 14.9 | 8.6 | 21.1 | 15.4 | 20.3 | 12.2 | 7.5 | 11.71 | 40.0% | 19.6% |
| ITF_WOMEN | 4,872 | 11.6 | 9.3 | 19.6 | 14.5 | 22.5 | 16.7 | 5.8 | 13.09 | 45.0% | 22.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 625 | 21.1 | 14.9 | 27.0 | 17.3 | 14.1 | 5.1 | 0.5 | 7.78 | 19.7% | 5.6% |
| WTA125 | 615 | 20.3 | 13.7 | 21.8 | 18.4 | 15.0 | 8.5 | 2.4 | 8.37 | 25.9% | 10.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,245 | 30.5 | 14.2 | 25.0 | 17.5 | 10.8 | 1.1 | 0.9 | 5.85 | 12.8% | 2.0% |
| CHALLENGER | 1,936 | 20.5 | 12.9 | 24.7 | 18.5 | 14.8 | 6.2 | 2.4 | 8.3 | 23.4% | 8.6% |
| ITF_MEN | 3,033 | 14.5 | 11.1 | 22.0 | 16.6 | 19.1 | 11.8 | 5.0 | 10.62 | 35.9% | 16.8% |
| ITF_WOMEN | 4,228 | 12.7 | 8.4 | 18.8 | 19.0 | 23.1 | 14.8 | 3.3 | 12.61 | 41.2% | 18.1% |
| WTA | 744 | 22.2 | 10.9 | 25.4 | 16.7 | 17.5 | 5.9 | 1.5 | 7.82 | 24.9% | 7.4% |
| WTA125 | 426 | 13.6 | 8.7 | 22.8 | 22.1 | 17.4 | 14.3 | 1.2 | 11.05 | 32.9% | 15.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,245 | 23.9 | 14.5 | 24.8 | 19.0 | 14.9 | 1.9 | 1.0 | 6.9 | 17.9% | 3.0% |
| CHALLENGER | 1,936 | 20.1 | 9.6 | 23.9 | 15.7 | 18.8 | 9.3 | 2.7 | 9.02 | 30.8% | 12.0% |
| ITF_MEN | 3,034 | 12.5 | 9.1 | 19.6 | 16.5 | 21.6 | 14.8 | 5.9 | 12.48 | 42.3% | 20.7% |
| ITF_WOMEN | 4,228 | 10.5 | 7.0 | 14.6 | 14.1 | 24.4 | 19.4 | 10.0 | 16.32 | 53.9% | 29.4% |
| WTA | 744 | 20.0 | 8.2 | 18.1 | 15.6 | 21.2 | 15.3 | 1.5 | 11.46 | 38.0% | 16.8% |
| WTA125 | 426 | 4.9 | 4.0 | 18.8 | 20.7 | 24.2 | 18.5 | 8.9 | 16.0 | 51.6% | 27.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 671 | 30.9 | 22.9 | 35.9 | 9.2 | 0.6 | 0.5 | 0.0 | 4.69 | 1.0% | 0.4% |
| CHALLENGER | 1,563 | 24.5 | 17.9 | 28.7 | 14.6 | 12.0 | 2.0 | 0.3 | 6.11 | 14.3% | 2.3% |
| DOUBLES | 840 | 4.5 | 3.2 | 11.6 | 11.3 | 19.5 | 24.6 | 25.2 | 24.87 | 69.4% | 49.9% |
| ITF_MEN | 3,327 | 16.7 | 9.5 | 23.4 | 16.4 | 20.1 | 9.8 | 4.2 | 10.07 | 34.1% | 14.0% |
| ITF_WOMEN | 3,984 | 12.8 | 10.0 | 21.5 | 15.4 | 22.8 | 15.0 | 2.7 | 11.64 | 40.4% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 595 | 21.5 | 15.5 | 27.6 | 17.3 | 14.3 | 3.9 | 0.0 | 7.33 | 18.1% | 3.9% |
| WTA125 | 520 | 22.5 | 15.2 | 23.5 | 20.2 | 13.3 | 5.0 | 0.4 | 7.42 | 18.6% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 907 | 4.5 | 3.2 | 11.2 | 11.2 | 19.4 | 24.8 | 25.6 | 25.42 | 69.8% | 50.4% |
| singles | 12,905 | 16.2 | 11.3 | 22.6 | 14.8 | 18.4 | 11.6 | 5.0 | 9.98 | 35.1% | 16.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,520 | 13.5 | 9.5 | 20.6 | 15.8 | 16.9 | 13.7 | 9.9 | 12.03 | 40.5% | 23.6% |
| Grass | 48 | 12.5 | 33.3 | 12.5 | 8.3 | 20.8 | 12.5 | 0.0 | 6.49 | 33.3% | 12.5% |
| Hard | 10,307 | 14.4 | 8.4 | 18.4 | 16.0 | 18.7 | 14.3 | 9.7 | 12.71 | 42.7% | 24.1% |
| UNKNOWN | 1,511 | 11.4 | 8.2 | 15.7 | 17.7 | 19.7 | 16.9 | 10.3 | 14.04 | 46.9% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,786 | 20.2 | 10.7 | 21.1 | 17.1 | 14.8 | 8.8 | 7.3 | 9.45 | 30.9% | 16.1% |
| B | 2,084 | 14.4 | 9.4 | 19.6 | 17.3 | 17.3 | 12.1 | 9.8 | 11.5 | 39.2% | 22.0% |
| C | 2,295 | 13.2 | 9.8 | 19.4 | 14.7 | 19.0 | 14.7 | 9.2 | 12.66 | 43.0% | 24.0% |
| D | 2,761 | 10.8 | 8.4 | 18.0 | 16.1 | 21.9 | 14.9 | 9.8 | 13.76 | 46.6% | 24.7% |
| F | 3,460 | 7.9 | 5.2 | 14.8 | 14.8 | 20.7 | 23.0 | 13.6 | 18.39 | 57.3% | 36.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,082 | 22.4 | 16.0 | 28.4 | 15.3 | 11.6 | 4.6 | 1.7 | 6.78 | 17.9% | 6.3% |
| B | 2,155 | 15.2 | 9.8 | 24.0 | 16.1 | 19.3 | 11.2 | 4.4 | 10.19 | 34.9% | 15.6% |
| C | 2,761 | 12.2 | 7.6 | 17.8 | 14.4 | 20.6 | 15.9 | 11.4 | 13.82 | 47.9% | 27.3% |
| D | 2,169 | 14.2 | 9.7 | 21.2 | 13.3 | 21.6 | 13.9 | 6.2 | 11.83 | 41.7% | 20.1% |
| F | 2,645 | 9.3 | 7.5 | 14.7 | 13.7 | 23.7 | 21.1 | 10.0 | 16.88 | 54.9% | 31.1% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,251 | 18.6 | 9.8 | 20.2 | 17.2 | 14.9 | 9.8 | 9.6 | 10.42 | 34.3% | 19.4% |
| LIMITED | 3,873 | 15.2 | 10.6 | 20.6 | 15.7 | 18.4 | 12.8 | 6.7 | 11.08 | 38.0% | 19.5% |
| POOR | 6,262 | 9.2 | 6.7 | 16.2 | 15.4 | 21.2 | 19.3 | 11.9 | 15.99 | 52.4% | 31.2% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,846 | 30.9 | 24.4 | 36.5 | 5.5 | 1.9 | 0.7 | 0.1 | 4.54 | 2.6% | 0.8% |
| GAME_SPREAD | 2,751 | 25.4 | 15.8 | 37.0 | 16.9 | 4.3 | 0.4 | 0.2 | 6.05 | 4.9% | 0.6% |
| MATCH_WINNER | 13,812 | 15.4 | 10.7 | 21.8 | 14.6 | 18.5 | 12.5 | 6.4 | 10.48 | 37.4% | 18.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,217 | 32.8 | 19.4 | 31.0 | 10.0 | 5.4 | 1.2 | 0.2 | 4.79 | 6.8% | 1.4% |
| TOTAL_GAMES | 4,155 | 6.7 | 8.9 | 38.6 | 30.1 | 10.5 | 2.8 | 2.4 | 9.54 | 15.7% | 5.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,646 | 25.4 | 37.9 | 31.7 | 0.3 | 4.1 | 0.5 | 0.1 | 4.32 | 4.7% | 0.6% |
| GAME_SPREAD | 3,296 | 44.9 | 15.7 | 29.5 | 7.6 | 1.2 | 0.8 | 0.4 | 3.59 | 2.3% | 1.1% |
| TOTAL_GAMES | 4,916 | 3.2 | 6.5 | 43.9 | 36.4 | 6.4 | 1.6 | 2.0 | 9.65 | 10.0% | 3.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,646 | 25.9 | 18.7 | 37.0 | 9.5 | 6.5 | 2.2 | 0.3 | 5.54 | 8.9% | 2.5% |
| GAME_SPREAD | 3,296 | 18.9 | 12.9 | 30.5 | 21.1 | 13.5 | 2.4 | 0.7 | 7.92 | 16.6% | 3.1% |
| TOTAL_GAMES | 4,925 | 6.5 | 8.5 | 38.6 | 28.7 | 12.4 | 3.0 | 2.2 | 9.64 | 17.7% | 5.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 15,386 | 42.6% | 24.2% | 12.69 | 32.4% | 13.7% | 10.1 |
| gen1_elo | 15,386 | 42.3% | 23.6% | 12.16 | 31.8% | 13.4% | 9.56 |
| gen1_sr | 15,386 | 50.9% | 29.3% | 15.37 | 41.7% | 18.7% | 12.47 |
| gen2 | 15,386 | 49.9% | 29.8% | 14.95 | 42.1% | 20.5% | 12.38 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 8,124 | 16.9 | 11.0 | 21.7 | 17.5 | 18.6 | 11.1 | 3.3 | 10.11 | 32.9% | 14.4% |
| STALE | 7,262 | 10.6 | 6.2 | 15.3 | 14.5 | 18.2 | 18.2 | 17.1 | 16.92 | 53.4% | 35.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 7,280 | 17.5 | 11.8 | 23.7 | 14.5 | 16.8 | 11.0 | 4.7 | 9.23 | 32.5% | 15.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 29,198 | 7280 | 11596 | 10322 | 24.4 | 145.6 | 1400.4 |
| ge_15pp | 11,716 | 2363 | 3964 | 5389 | 27.8 | 450.1 | 1380.4 |
| ge_25pp | 6,332 | 1143 | 1758 | 3431 | 34.6 | 574.8 | 1380.4 |
| lt_10pp | 12,989 | 3863 | 5656 | 3470 | 22.7 | 49.2 | 1341.5 |

Current slate `SL-20261011T132728Z-14745856`: 475 priced rows, quote age at build {'median': 5.0, 'max': 5.0}, freshness {'FRESH': 475}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 8 | 0.0 | 0.0 | 37.5 | 0.0 | 37.5 | 25.0 | 0.0 | 20.45 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 7 | 57.1 | 42.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,083 | 23.2 | 11.3 | 23.1 | 18.8 | 17.2 | 6.1 | 0.4 | 8.23 | 23.6% | 6.5% |
| KALSHI_LONE_OUTLIER | 1 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 5.14 | 0.0% | 0.0% |
| MARKETS_AGREE | 188 | 72.3 | 27.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.98 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 323 | 0.0 | 4.0 | 36.5 | 31.3 | 19.8 | 8.1 | 0.3 | 11.28 | 28.2% | 8.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 15,386 | 1610 (10.5%) | 20.1% | 0.5% | {"EXTERNAL_STALE": 1083, "AGREES_WITH_KALSHI": 323, "ALL_AGREE": 188, "SUPPORTS_MODEL_DIRECTION": 7, "EXTERNAL_OUTLIER": 7, "ALL_DISAGREE": 1, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_15pp | 6,554 | 352 (5.4%) | 25.9% | 1.4% | {"EXTERNAL_STALE": 256, "AGREES_WITH_KALSHI": 91, "SUPPORTS_MODEL_DIRECTION": 5} |
| fair_v1_ge_25pp | 3,727 | 99 (2.7%) | 27.3% | 2.0% | {"EXTERNAL_STALE": 70, "AGREES_WITH_KALSHI": 27, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp_pregame_clean | 1,587 | 94 (5.9%) | 26.6% | 2.1% | {"EXTERNAL_STALE": 67, "AGREES_WITH_KALSHI": 25, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_lt_10pp | 6,357 | 953 (15.0%) | 13.8% | 0.3% | {"EXTERNAL_STALE": 623, "ALL_AGREE": 188, "AGREES_WITH_KALSHI": 131, "EXTERNAL_OUTLIER": 7, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1, "AGREES_WITH_MODEL": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,073 | 11.7 | 8.5 | 19.7 | 15.3 | 20.9 | 13.9 | 10.0 | 13.14 | 44.8% | 23.9% |
| 4-10x | 2,082 | 11.6 | 9.0 | 19.3 | 15.2 | 19.7 | 15.9 | 9.2 | 13.12 | 44.9% | 25.2% |
| <2x | 8,282 | 16.0 | 9.3 | 18.8 | 17.2 | 16.8 | 12.8 | 9.2 | 11.7 | 38.8% | 21.9% |
| >=10x | 1,949 | 11.1 | 6.4 | 15.8 | 13.7 | 19.6 | 20.8 | 12.7 | 16.48 | 53.0% | 33.5% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,090 | 14.1 | 8.5 | 19.4 | 16.0 | 18.5 | 12.8 | 10.8 | 12.44 | 42.0% | 23.5% |
| 300-1000 | 3,629 | 12.0 | 9.0 | 17.1 | 16.1 | 21.0 | 15.9 | 9.0 | 13.67 | 45.9% | 24.9% |
| <300 | 3,986 | 8.5 | 6.1 | 15.8 | 14.7 | 20.7 | 21.1 | 13.1 | 17.12 | 54.9% | 34.2% |
| >=3000 | 3,681 | 21.4 | 11.7 | 22.5 | 17.7 | 13.2 | 7.6 | 6.0 | 8.45 | 26.7% | 13.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 489 | 0.5374 | 0.4055 | 0.4765 | +0.061 | -0.071 | 0.0025 ± 0.0066 |
| ratio 4-10x | 332 | 0.5791 | 0.4378 | 0.5151 | +0.064 | -0.077 | 0.0035 ± 0.0087 |
| ratio <2x | 1133 | 0.5389 | 0.4177 | 0.451 | +0.088 | -0.033 | 0.0126 ± 0.0042 |
| ratio >=10x | 317 | 0.5462 | 0.3797 | 0.4259 | +0.120 | -0.046 | 0.0186 ± 0.0098 |
| thinner_sample 1000-3000 | 633 | 0.5439 | 0.4202 | 0.466 | +0.078 | -0.046 | 0.0073 ± 0.0056 |
| thinner_sample 300-1000 | 592 | 0.5636 | 0.4239 | 0.4865 | +0.077 | -0.063 | 0.0027 ± 0.0064 |
| thinner_sample <300 | 644 | 0.5413 | 0.382 | 0.4457 | +0.096 | -0.064 | 0.0151 ± 0.0067 |
| thinner_sample >=3000 | 402 | 0.5279 | 0.4337 | 0.4478 | +0.080 | -0.014 | 0.0163 ± 0.0056 |
| data_status ADEQUATE | 637 | 0.5301 | 0.4286 | 0.4443 | +0.086 | -0.016 | 0.0125 ± 0.0048 |
| data_status LIMITED | 618 | 0.555 | 0.424 | 0.4854 | +0.070 | -0.061 | 0.0031 ± 0.006 |
| data_status POOR | 1016 | 0.5493 | 0.3959 | 0.4596 | +0.090 | -0.064 | 0.0125 ± 0.0052 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 351 | 0.1909 | 0.192 | -0.0011 ± 0.0008 | 0.5582 | 0.5611 | 0.4901 | 0.4753 | 0.5157 | -0.056 ± 0.0244 | -0.01 (3) |
| 3-5 | 237 | 0.1869 | 0.1878 | -0.0008 ± 0.0022 | 0.5531 | 0.5534 | 0.5102 | 0.4704 | 0.4979 | -0.066 ± 0.0285 | 0.02 (1) |
| 5-10 | 470 | 0.201 | 0.2021 | -0.0011 ± 0.0031 | 0.5876 | 0.5901 | 0.5188 | 0.4447 | 0.4809 | -0.084 ± 0.0215 | -0.0125 (4) |
| 10-15 | 410 | 0.2132 | 0.2051 | +0.0081 ± 0.0056 | 0.6146 | 0.5914 | 0.5158 | 0.3918 | 0.4171 | -0.097 ± 0.0223 | -0.0633 (3) |
| 15-25 | 480 | 0.228 | 0.2139 | +0.0141 ± 0.0083 | 0.6512 | 0.6153 | 0.5754 | 0.38 | 0.4417 | -0.084 ± 0.021 | -0.0133 (6) |
| 25-40 | 265 | 0.2199 | 0.1977 | +0.0222 ± 0.0162 | 0.6291 | 0.57 | 0.6448 | 0.3366 | 0.4528 | -0.077 ± 0.0243 | -0.01 (1) |
| 40+ | 58 | 0.3011 | 0.1684 | +0.1326 ± 0.0481 | 0.819 | 0.5095 | 0.7496 | 0.3043 | 0.3793 | -0.146 ± 0.0481 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1752 | 0.1732 | 0.1739 | -0.0007 ± 0.0003 | 0.5171 | 0.5177 | 0.4748 | 0.4601 | 0.488 | -0.029 ± 0.0101 | -0.0188 (8) |
| 3-5 | 1103 | 0.1905 | 0.1874 | +0.0031 ± 0.001 | 0.5616 | 0.5493 | 0.4793 | 0.4397 | 0.417 | -0.082 ± 0.0132 | 0.02 (1) |
| 5-10 | 2385 | 0.1959 | 0.1932 | +0.0027 ± 0.0013 | 0.5747 | 0.5661 | 0.4875 | 0.4138 | 0.4289 | -0.052 ± 0.0091 | -0.0082 (17) |
| 10-15 | 2116 | 0.2007 | 0.1818 | +0.0189 ± 0.0023 | 0.5873 | 0.5349 | 0.475 | 0.3505 | 0.337 | -0.080 ± 0.0092 | -0.0475 (4) |
| 15-25 | 2440 | 0.2037 | 0.1669 | +0.0368 ± 0.0032 | 0.5994 | 0.4957 | 0.4966 | 0.3005 | 0.3061 | -0.068 ± 0.0083 | -0.0048 (29) |
| 25-40 | 2022 | 0.2191 | 0.1218 | +0.0973 ± 0.0048 | 0.631 | 0.3779 | 0.5256 | 0.212 | 0.2166 | -0.063 ± 0.0075 | -0.01 (1) |
| 40+ | 1384 | 0.3717 | 0.0429 | +0.3287 ± 0.0062 | 0.9693 | 0.1715 | 0.6213 | 0.105 | 0.0549 | -0.085 ± 0.0053 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 268 | 0.1935 | 0.1938 | -0.0003 ± 0.0009 | 0.5676 | 0.5687 | 0.4927 | 0.4778 | 0.4851 | -0.090 ± 0.0285 | -0.01 (1) |
| 3-5 | 180 | 0.2063 | 0.2062 | +0.0000 ± 0.0028 | 0.5926 | 0.5944 | 0.5247 | 0.4847 | 0.5 | -0.067 ± 0.0355 | 0.02 (1) |
| 5-10 | 402 | 0.1962 | 0.1932 | +0.0031 ± 0.0033 | 0.5747 | 0.5679 | 0.5574 | 0.4824 | 0.4975 | -0.090 ± 0.0227 | -0.01 (4) |
| 10-15 | 385 | 0.2154 | 0.2046 | +0.0108 ± 0.0058 | 0.6173 | 0.5949 | 0.5741 | 0.4496 | 0.4727 | -0.105 ± 0.0238 | -0.05 (4) |
| 15-25 | 553 | 0.2249 | 0.2093 | +0.0157 ± 0.0077 | 0.6388 | 0.6012 | 0.5984 | 0.4014 | 0.4665 | -0.080 ± 0.0198 | -0.01 (5) |
| 25-40 | 351 | 0.274 | 0.2 | +0.0740 ± 0.0151 | 0.7681 | 0.5799 | 0.6723 | 0.3584 | 0.3989 | -0.137 ± 0.0237 | -0.025 (2) |
| 40+ | 132 | 0.3493 | 0.1857 | +0.1636 ± 0.0364 | 0.9817 | 0.5447 | 0.758 | 0.2807 | 0.3636 | -0.073 ± 0.0355 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1525 | 0.1765 | 0.1768 | -0.0002 ± 0.0004 | 0.5249 | 0.5257 | 0.4909 | 0.4764 | 0.4964 | -0.035 ± 0.0112 | -0.0217 (6) |
| 3-5 | 956 | 0.1912 | 0.1901 | +0.0011 ± 0.0011 | 0.5562 | 0.5536 | 0.519 | 0.4791 | 0.4833 | -0.046 ± 0.0143 | 0.02 (1) |
| 5-10 | 2087 | 0.1877 | 0.1834 | +0.0043 ± 0.0014 | 0.5573 | 0.543 | 0.5135 | 0.44 | 0.4509 | -0.052 ± 0.0095 | -0.01 (5) |
| 10-15 | 1847 | 0.1962 | 0.1807 | +0.0156 ± 0.0025 | 0.5784 | 0.5305 | 0.5193 | 0.3949 | 0.3974 | -0.068 ± 0.01 | -0.02 (14) |
| 15-25 | 2634 | 0.2148 | 0.175 | +0.0398 ± 0.0032 | 0.6257 | 0.5172 | 0.535 | 0.3392 | 0.339 | -0.075 ± 0.0082 | -0.0026 (27) |
| 25-40 | 2326 | 0.2493 | 0.1375 | +0.1118 ± 0.0049 | 0.7088 | 0.4186 | 0.5618 | 0.2456 | 0.2287 | -0.087 ± 0.0077 | -0.015 (6) |
| 40+ | 1827 | 0.4033 | 0.0667 | +0.3366 ± 0.0069 | 1.0571 | 0.2349 | 0.6673 | 0.1305 | 0.0991 | -0.072 ± 0.0059 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 355 | 0.1913 | 0.1939 | -0.0026 ± 0.0008 | 0.5599 | 0.5668 | 0.4992 | 0.484 | 0.5577 | -0.008 ± 0.0235 | -0.0133 (6) |
| 3-5 | 248 | 0.1885 | 0.1873 | +0.0011 ± 0.0022 | 0.5531 | 0.5502 | 0.499 | 0.4597 | 0.4677 | -0.107 ± 0.0288 | -0.01 (1) |
| 5-10 | 505 | 0.2014 | 0.1989 | +0.0025 ± 0.003 | 0.5904 | 0.5822 | 0.5089 | 0.4351 | 0.4515 | -0.092 ± 0.0206 | -0.01 (4) |
| 10-15 | 386 | 0.2132 | 0.2119 | +0.0013 ± 0.0058 | 0.616 | 0.6073 | 0.5372 | 0.4148 | 0.4715 | -0.075 ± 0.0233 | -0.044 (5) |
| 15-25 | 457 | 0.2305 | 0.2087 | +0.0218 ± 0.0083 | 0.6612 | 0.6021 | 0.5789 | 0.3856 | 0.4267 | -0.105 ± 0.0211 | -0.03 (1) |
| 25-40 | 270 | 0.2029 | 0.202 | +0.0009 ± 0.016 | 0.5885 | 0.582 | 0.6508 | 0.3396 | 0.4889 | -0.052 ± 0.0235 | 0.0 (1) |
| 40+ | 50 | 0.3214 | 0.1713 | +0.1501 ± 0.0531 | 0.8683 | 0.515 | 0.7463 | 0.2948 | 0.36 | -0.154 ± 0.0547 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1660 | 0.1805 | 0.1813 | -0.0009 ± 0.0004 | 0.5331 | 0.5348 | 0.4836 | 0.4685 | 0.5012 | -0.023 ± 0.0105 | -0.0183 (23) |
| 3-5 | 1159 | 0.1858 | 0.1833 | +0.0026 ± 0.001 | 0.5478 | 0.5414 | 0.4787 | 0.4395 | 0.4271 | -0.077 ± 0.013 | -0.0243 (7) |
| 5-10 | 2548 | 0.1913 | 0.1858 | +0.0055 ± 0.0013 | 0.5665 | 0.5486 | 0.4812 | 0.4074 | 0.4066 | -0.063 ± 0.0086 | -0.01 (18) |
| 10-15 | 1969 | 0.1962 | 0.1809 | +0.0153 ± 0.0024 | 0.5773 | 0.5306 | 0.4929 | 0.3698 | 0.3677 | -0.071 ± 0.0095 | -0.03 (9) |
| 15-25 | 2573 | 0.2082 | 0.1696 | +0.0386 ± 0.0032 | 0.6115 | 0.5032 | 0.4993 | 0.3041 | 0.3047 | -0.070 ± 0.0082 | -0.03 (2) |
| 25-40 | 1979 | 0.2127 | 0.1164 | +0.0964 ± 0.0048 | 0.616 | 0.3634 | 0.5202 | 0.2033 | 0.2127 | -0.062 ± 0.0073 | 0.0 (1) |
| 40+ | 1314 | 0.3856 | 0.045 | +0.3405 ± 0.0066 | 1.008 | 0.1773 | 0.6291 | 0.1064 | 0.0533 | -0.088 ± 0.0056 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 654 | 0.2016 | 0.2021 | -0.0005 ± 0.0006 | 0.5852 | 0.5859 | 0.5016 | 0.4866 | 0.5 | -0.037 ± 0.0176 | -0.0226 (46) |
| 3-5 | 480 | 0.198 | 0.1965 | +0.0015 ± 0.0016 | 0.5765 | 0.571 | 0.4799 | 0.4403 | 0.4396 | -0.055 ± 0.0202 | -0.0058 (33) |
| 5-10 | 983 | 0.1924 | 0.1868 | +0.0056 ± 0.0021 | 0.5691 | 0.5546 | 0.4798 | 0.4062 | 0.4059 | -0.063 ± 0.014 | -0.0049 (73) |
| 10-15 | 626 | 0.204 | 0.1937 | +0.0102 ± 0.0044 | 0.5963 | 0.569 | 0.4901 | 0.3672 | 0.3866 | -0.046 ± 0.0175 | 0.0014 (64) |
| 15-25 | 845 | 0.2352 | 0.2089 | +0.0263 ± 0.0062 | 0.6699 | 0.6032 | 0.5533 | 0.3591 | 0.3905 | -0.060 ± 0.0158 | -0.0216 (58) |
| 25-40 | 476 | 0.2537 | 0.1884 | +0.0653 ± 0.0124 | 0.7147 | 0.5511 | 0.6374 | 0.3238 | 0.3739 | -0.088 ± 0.0186 | -0.0216 (25) |
| 40+ | 160 | 0.3684 | 0.1874 | +0.1810 ± 0.0354 | 1.0745 | 0.5537 | 0.7872 | 0.2916 | 0.3812 | -0.069 ± 0.0314 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2024 | 0.1908 | 0.1909 | -0.0001 ± 0.0003 | 0.5578 | 0.5566 | 0.5033 | 0.488 | 0.4946 | -0.037 ± 0.0097 | -0.0155 (82) |
| 3-5 | 1416 | 0.1897 | 0.1868 | +0.0029 ± 0.0009 | 0.5546 | 0.5476 | 0.4883 | 0.4487 | 0.4329 | -0.061 ± 0.0115 | -0.0148 (63) |
| 5-10 | 2830 | 0.1906 | 0.1825 | +0.0081 ± 0.0012 | 0.5652 | 0.5426 | 0.4752 | 0.4015 | 0.3869 | -0.067 ± 0.0081 | -0.0087 (125) |
| 10-15 | 1906 | 0.2009 | 0.1865 | +0.0144 ± 0.0025 | 0.5892 | 0.5514 | 0.5027 | 0.3796 | 0.3825 | -0.056 ± 0.0098 | -0.0053 (105) |
| 15-25 | 2440 | 0.2307 | 0.1969 | +0.0338 ± 0.0035 | 0.6663 | 0.573 | 0.5482 | 0.3532 | 0.366 | -0.062 ± 0.0091 | -0.0255 (106) |
| 25-40 | 1671 | 0.2528 | 0.1635 | +0.0893 ± 0.0063 | 0.7178 | 0.4857 | 0.6 | 0.2851 | 0.3028 | -0.078 ± 0.0096 | -0.0206 (47) |
| 40+ | 819 | 0.3919 | 0.1197 | +0.2721 ± 0.0131 | 1.1142 | 0.3722 | 0.7013 | 0.1908 | 0.1929 | -0.076 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2271 | 1.072 ± 0.059 | 1.19 | 0.1689 | 0.1704 | 0.2106 | 0.2007 |
| gen2 | 2271 | 0.873 ± 0.052 | 1.133 | 0.1852 | 0.1698 | 0.2279 | 0.2008 |
| gen1_elo | 2271 | 1.063 ± 0.058 | 1.179 | 0.1729 | 0.1708 | 0.2091 | 0.2008 |
| gen1_sr | 2271 | 1.065 ± 0.067 | 1.211 | 0.1436 | 0.1721 | 0.2234 | 0.2006 |
| gen1_ledger | 4224 | 0.871 ± 0.038 | 1.077 | 0.1742 | 0.1886 | 0.2183 | 0.1959 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 11,716)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,141 | 26.8% |
| STALE_QUOTE | market_freshness | 2,294 | 19.6% |
| BOOK_QUALITY | execution | 2,099 | 17.9% |
| POOR_DATA | data | 1,219 | 10.4% |
| LIMITED_DATA | data | 927 | 7.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 664 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 540 | 4.6% |
| IDENTITY_AMBIGUOUS | mapping | 382 | 3.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 356 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 94 | 0.8% |

Cause class: coverage 26.8%, market_freshness 19.6%, data 18.3%, execution 17.9%, market_freshness/coverage 8.7%, model_calibration_or_unknown 4.6%, mapping 3.3%, model_calibration 0.8%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.7%, START_UNVERIFIABLE 95.9%, LOW_DATA_QUALITY 67.7%, STALE_PLAYER_DATA 57.1%, THIN_PLAYER_HISTORY 56.0%, STALE_KALSHI_QUOTE 46.0%, MODEL_INTERNAL_DISAGREEMENT 37.4%, ASYMMETRIC_SAMPLE_SIZE 30.2%, WIDE_SPREAD 23.7%, MODEL_HIGH_UNCERTAINTY 16.3%, PLAYER_IDENTITY_RISK 11.8%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 1.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.4%, POST_SETTLEMENT_OBSERVATION 26.8%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,332)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,477 | 39.1% |
| BOOK_QUALITY | execution | 1,110 | 17.5% |
| STALE_QUOTE | market_freshness | 1,021 | 16.1% |
| POOR_DATA | data | 497 | 7.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 360 | 5.7% |
| LIMITED_DATA | data | 270 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 235 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 222 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 118 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 22 | 0.4% |

Cause class: coverage 39.1%, execution 17.5%, market_freshness 16.1%, data 12.1%, market_freshness/coverage 9.2%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.3%, START_UNVERIFIABLE 98.1%, LOW_DATA_QUALITY 71.2%, THIN_PLAYER_HISTORY 58.1%, STALE_KALSHI_QUOTE 54.2%, STALE_PLAYER_DATA 51.6%, MODEL_INTERNAL_DISAGREEMENT 38.7%, ASYMMETRIC_SAMPLE_SIZE 32.3%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 17.5%, PLAYER_IDENTITY_RISK 15.0%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 0.6%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.1%, POST_SETTLEMENT_OBSERVATION 39.1%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5215, "IDENTITY_AMBIGUOUS": 1117}; ticker orientation: {"VERIFIED": 6332}.

Checks: discipline:AMBIGUOUS 457, discipline:PASS 5875, identity_confidence:AMBIGUOUS 953, identity_confidence:PASS 5379, level_mapping:NA 469, level_mapping:PASS 5863, market_pair:AMBIGUOUS 224, market_pair:NA 150, market_pair:PASS 5958, model_complement:NA 117, model_complement:PASS 6215, namesake:PASS 6332, physical_match_id:NA 2605, physical_match_id:PASS 3727, player_ids:PASS 6332, same_pair_other_event:PASS 6332, ticker_orientation:PASS 6332

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,948 | 1.4% | 1.5% | 0.4% | {"market_freshness": 20, "execution": 8} | 5.29 | 0.2049 / 0.2032 (217) | 16.8% | 0.1% | 5.7% | 1.6% |
| CHALLENGER | 4,498 | 17.0% | 5.8% | 12.1% | {"coverage": 463, "market_freshness": 109, "market_freshness/coverage": 99, "model_calibration_or_unknown": 41, "data": 33, "execution": 12, "model_calibration": 4, "mapping": 4} | 6.98 | 0.221 / 0.2031 (1004) | 39.7% | 6.6% | 2.2% | 22.2% |
| DOUBLES | 907 | 50.4% | 49.9% | 7.2% | {"execution": 176, "mapping": 137, "market_freshness": 106, "market_freshness/coverage": 31, "coverage": 7} | 24.87 | 0.3344 / 0.2293 (250) | 25.8% | 0.0% | 100.0% | 7.4% |
| ITF_MEN | 8,424 | 23.6% | 15.3% | 31.5% | {"coverage": 835, "execution": 411, "data": 272, "market_freshness": 271, "market_freshness/coverage": 182, "mapping": 19, "model_calibration_or_unknown": 2} | 10.38 | 0.2102 / 0.1931 (2089) | 37.5% | 53.4% | 6.5% | 24.5% |
| ITF_WOMEN | 10,838 | 26.3% | 17.8% | 45.0% | {"coverage": 1155, "execution": 484, "market_freshness": 450, "data": 430, "market_freshness/coverage": 226, "mapping": 69, "model_calibration_or_unknown": 24, "model_calibration": 9} | 12.2 | 0.2056 / 0.1927 (2351) | 38.4% | 57.5% | 9.6% | 24.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,374 | 6.6% | 5.8% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 20, "data": 11, "market_freshness/coverage": 9, "execution": 6, "model_calibration": 4, "coverage": 4, "mapping": 1} | 7.69 | 0.2208 / 0.2187 (205) | 26.9% | 1.5% | 1.6% | 2.5% |
| WTA125 | 1,060 | 13.2% | 9.9% | 2.2% | {"market_freshness/coverage": 34, "model_calibration_or_unknown": 29, "market_freshness": 27, "data": 21, "coverage": 12, "execution": 8, "model_calibration": 5, "mapping": 4} | 9.01 | 0.228 / 0.2088 (337) | 23.2% | 7.8% | 4.2% | 10.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 8 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 9 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 10 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 11 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 12 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 13 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 14 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 15 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 16 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 19 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 20 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 22 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 23 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 24 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 25 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 26 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 28 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 29 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 30 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 31 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 32 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 760 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 34 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 35 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 36 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 37 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 38 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 39 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 40 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 41 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 42 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 43 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 26 min (AGING); no external reference |
| 44 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 826 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 45 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.2h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 141 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 46 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 47 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 48 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.9h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 780 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |
| 49 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 208 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 156 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9812, "by_level_share_of_ge_25pp": {"ATP": 0.0044, "CHALLENGER": 0.1208, "DOUBLES": 0.0722, "ITF_MEN": 0.3146, "ITF_WOMEN": 0.4496, "OTHER": 0.0019, "WTA": 0.0144, "WTA125": 0.0221}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5419, "share_primary_cause_market_settled_or_in_play": 0.4832, "share_primary_cause_stale_quote_only": 0.1612}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6332, "identity_ambiguous_share": 0.1764, "ticker_orientation": {"VERIFIED": 6332}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3727, "with_external": 99, "coverage": 0.0266, "external_status": {"EXTERNAL_STALE": 70, "AGREES_WITH_KALSHI": 27, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 70, "MODEL_LONE_OUTLIER": 27, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2727, "share_external_supports_model": 0.0202}, "pregame_clean_ge_25pp": {"n": 1587, "with_external": 94, "coverage": 0.0592, "external_status": {"EXTERNAL_STALE": 67, "AGREES_WITH_KALSHI": 25, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 67, "MODEL_LONE_OUTLIER": 25, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.266, "share_external_supports_model": 0.0213}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 623.0, "median_sample_ratio": 2.31, "median_min_matches": 21.0, "median_max_days_since_last": 197.0, "share_severe_asymmetry": 0.181, "data_status": {"POOR": 3225, "LIMITED": 1930, "ADEQUATE": 1177}, "comparison_lt_10pp": {"median_thinner_serve_points": 1937.0, "median_sample_ratio": 1.66, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 489, "model_minus_observed": 0.0609, "kalshi_minus_observed": -0.071, "brier_diff_model_minus_kalshi": 0.0025}, "4-10x": {"n": 332, "model_minus_observed": 0.064, "kalshi_minus_observed": -0.0772, "brier_diff_model_minus_kalshi": 0.0035}, "<2x": {"n": 1133, "model_minus_observed": 0.0879, "kalshi_minus_observed": -0.0333, "brier_diff_model_minus_kalshi": 0.0126}, ">=10x": {"n": 317, "model_minus_observed": 0.1203, "kalshi_minus_observed": -0.0462, "brier_diff_model_minus_kalshi": 0.0186}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2271, "model": {"intercept": -0.57, "slope": 0.873, "slope_se": 0.052}, "kalshi_mid_same_rows": {"intercept": 0.206, "slope": 1.133, "slope_se": 0.06}, "mean_extremity_model": 0.1852, "mean_extremity_kalshi": 0.1698, "model_brier": 0.2279, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": 0.0271, "brier_diff_se": 0.0039, "model_logloss": 0.6517, "kalshi_logloss": 0.5833}, "fair_v1": {"n": 2271, "model": {"intercept": -0.416, "slope": 1.072, "slope_se": 0.059}, "kalshi_mid_same_rows": {"intercept": 0.304, "slope": 1.19, "slope_se": 0.063}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1704, "model_brier": 0.2106, "kalshi_brier": 0.2007, "brier_diff_model_minus_kalshi": 0.0099, "brier_diff_se": 0.0031, "model_logloss": 0.6085, "kalshi_logloss": 0.5829}, "gen1_elo": {"n": 2271, "model": {"intercept": -0.384, "slope": 1.063, "slope_se": 0.058}, "kalshi_mid_same_rows": {"intercept": 0.315, "slope": 1.179, "slope_se": 0.061}, "mean_extremity_model": 0.1729, "mean_extremity_kalshi": 0.1708, "model_brier": 0.2091, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.0031, "model_logloss": 0.606, "kalshi_logloss": 0.5831}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2422, "share_ge_15": 0.426, "median_abs_gap": 12.69, "n": 15386}, "gen1_elo": {"share_ge_25": 0.236, "share_ge_15": 0.4226, "median_abs_gap": 12.16, "n": 15386}, "gen1_sr": {"share_ge_25": 0.2934, "share_ge_15": 0.5093, "median_abs_gap": 15.37, "n": 15386}, "gen2": {"share_ge_25": 0.2976, "share_ge_15": 0.4986, "median_abs_gap": 14.95, "n": 15386}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1367, "share_ge_15": 0.3243, "median_abs_gap": 10.1, "n": 11612}, "gen1_elo": {"share_ge_25": 0.1343, "share_ge_15": 0.3182, "median_abs_gap": 9.56, "n": 11611}, "gen1_sr": {"share_ge_25": 0.1874, "share_ge_15": 0.4173, "median_abs_gap": 12.47, "n": 11612}, "gen2": {"share_ge_25": 0.2055, "share_ge_15": 0.4206, "median_abs_gap": 12.38, "n": 11613}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.29, "share_ge_25_all": 0.0144, "share_ge_25_pregame_clean": 0.0146}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0662, "share_ge_25_pregame_clean": 0.0583}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2432, "share_within_10pp_all": 0.4449, "share_within_10pp_pregame_clean": 0.5086, "corr_model_vs_mid_pregame_clean": 0.8526}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 351, "model_brier": 0.1909, "kalshi_brier": 0.192, "brier_diff_model_minus_kalshi": -0.0011}, "10-15": {"n_settled": 410, "model_brier": 0.2132, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0081}, "15-25": {"n_settled": 480, "model_brier": 0.228, "kalshi_brier": 0.2139, "brier_diff_model_minus_kalshi": 0.0141}, "25-40": {"n_settled": 265, "model_brier": 0.2199, "kalshi_brier": 0.1977, "brier_diff_model_minus_kalshi": 0.0222}, "3-5": {"n_settled": 237, "model_brier": 0.1869, "kalshi_brier": 0.1878, "brier_diff_model_minus_kalshi": -0.0008}, "40+": {"n_settled": 58, "model_brier": 0.3011, "kalshi_brier": 0.1684, "brier_diff_model_minus_kalshi": 0.1326}, "5-10": {"n_settled": 470, "model_brier": 0.201, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": -0.0011}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA125
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA125', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.57, "slope": 0.873, "slope_se": 0.052}, "kalshi_slope": {"intercept": 0.206, "slope": 1.133, "slope_se": 0.06}, "n": 2271}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.532, "slope": 0.871, "slope_se": 0.038}, "kalshi_slope": {"intercept": 0.128, "slope": 1.077, "slope_se": 0.043}, "n": 4224}, "NO_SKILL:gen2|WTA125": {"n_settled": 87, "model_brier": 0.2612, "kalshi_brier": 0.2131, "brier_diff_model_minus_kalshi": 0.0481, "brier_diff_se": 0.0218, "corr_model_outcome": 0.2659, "corr_kalshi_outcome": 0.311}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 250, "model_brier": 0.3344, "kalshi_brier": 0.2293, "brier_diff_model_minus_kalshi": 0.1051, "brier_diff_se": 0.0206, "corr_model_outcome": -0.0224, "corr_kalshi_outcome": 0.2891}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
