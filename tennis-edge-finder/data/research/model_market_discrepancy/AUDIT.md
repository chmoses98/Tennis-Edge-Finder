# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-13T14:47Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 30,777): 0-3 14.5%, 3-5 9.6%, 5-10 20.2%, 10-15 15.4%, 15-25 18.6%, 25-40 13.5%, 40+ 8.1%; median gap 11.69 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.0%, Challenger 12.5%, doubles 7.1%). Main tour: ATP 1.4% and WTA 6.2% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 6,643): MARKET_ALREADY_SETTLED_WHEN_PRICED 38.4%, BOOK_QUALITY 17.6%, STALE_QUOTE 16.4%, POOR_DATA 8.1%, POSSIBLY_IN_PLAY_QUOTE 5.5%, LIMITED_DATA 4.2%, IDENTITY_AMBIGUOUS 3.9%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.4%. By class: coverage 38.4%, execution 17.6%, market_freshness 16.4%, data 12.4%, market_freshness/coverage 8.9%, mapping 3.9%, model_calibration_or_unknown 2.0%, model_calibration 0.4%.
* **Stale / settled / in-play**: 53.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 47.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 6,643 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 18.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 3.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 21.5% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 605.0 points vs 1892.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.07, Gen-2 0.873, Gen-1 ledger 0.877 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 292 model 0.2213 vs Kalshi 0.2044; n 68 model 0.2909 vs Kalshi 0.1768.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 122,735 model-market comparisons (202,022 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 45,280 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-13T14:40:11.462969+00:00'], shadow board 32,692 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-13T14:40:14.970603+00:00'], Model 4 13,754 rows, 13,550 settled tickers, 4,084 tickers with an external scan.
* By model: {"gen1_ledger": 29822, "gen1_elo": 16429, "fair_v1": 16429, "gen2": 16429, "gen1_sr": 16429, "model4_fundamental": 13603, "model4_conditioned": 13594}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 30,777 | 14.5 | 9.6 | 20.2 | 15.4 | 18.6 | 13.5 | 8.1 | 11.69 | 40.2% | 21.6% |
| MW fair_v1 | 16,429 | 13.8 | 8.7 | 18.7 | 16.0 | 18.8 | 14.4 | 9.7 | 12.72 | 42.8% | 24.1% |
| MW gen1_elo | 16,429 | 13.4 | 9.1 | 20.3 | 15.0 | 18.7 | 14.3 | 9.2 | 12.16 | 42.2% | 23.5% |
| MW gen1_ledger | 14,348 | 15.4 | 10.7 | 22.0 | 14.7 | 18.5 | 12.4 | 6.3 | 10.46 | 37.2% | 18.7% |
| MW gen1_sr | 16,429 | 10.0 | 7.9 | 16.6 | 14.4 | 21.6 | 18.0 | 11.5 | 15.42 | 51.1% | 29.5% |
| MW gen2 | 16,429 | 11.9 | 7.3 | 16.4 | 14.2 | 20.1 | 17.0 | 12.9 | 15.03 | 50.1% | 29.9% |
| all families model4_conditioned | 13,594 | 21.8 | 20.1 | 35.6 | 16.2 | 4.2 | 1.1 | 0.9 | 5.8 | 6.2% | 2.0% |
| all families model4_fundamental | 13,603 | 16.6 | 13.3 | 35.9 | 19.8 | 10.6 | 2.6 | 1.1 | 7.63 | 14.4% | 3.8% |

Configurable thresholds (primary): >=5pp 75.8%, >=10pp 55.6%, >=15pp 40.2%, >=20pp 29.8%, >=25pp 21.6%, >=30pp 15.8%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.27pp; >=10pp 44.8%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,303 | 30.2 | 14.7 | 24.8 | 17.9 | 10.5 | 1.1 | 0.8 | 5.84 | 12.5% | 2.0% |
| CHALLENGER | 2,930 | 15.6 | 10.1 | 20.1 | 15.9 | 14.7 | 12.0 | 11.6 | 11.51 | 38.3% | 23.6% |
| ITF_MEN | 4,530 | 11.4 | 8.7 | 18.2 | 14.8 | 19.4 | 15.4 | 12.2 | 13.88 | 47.0% | 27.6% |
| ITF_WOMEN | 6,272 | 10.2 | 6.5 | 15.9 | 16.1 | 21.8 | 18.7 | 10.7 | 15.49 | 51.2% | 29.4% |
| WTA | 863 | 21.4 | 11.0 | 25.3 | 16.0 | 19.6 | 5.5 | 1.3 | 8.09 | 26.3% | 6.7% |
| WTA125 | 531 | 13.4 | 8.1 | 23.5 | 19.6 | 19.0 | 14.3 | 2.1 | 11.08 | 35.4% | 16.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,303 | 23.9 | 14.7 | 24.5 | 19.3 | 14.7 | 1.9 | 1.0 | 6.9 | 17.6% | 2.9% |
| CHALLENGER | 2,930 | 15.3 | 7.6 | 19.3 | 13.3 | 18.2 | 14.1 | 12.2 | 12.73 | 44.5% | 26.2% |
| ITF_MEN | 4,530 | 10.2 | 7.3 | 16.5 | 14.5 | 19.7 | 18.1 | 13.7 | 15.59 | 51.5% | 31.7% |
| ITF_WOMEN | 6,272 | 8.8 | 5.8 | 12.8 | 12.8 | 21.7 | 21.0 | 17.0 | 19.18 | 59.8% | 38.1% |
| WTA | 863 | 18.5 | 8.2 | 18.7 | 16.0 | 22.8 | 14.5 | 1.3 | 11.64 | 38.6% | 15.8% |
| WTA125 | 531 | 5.8 | 4.3 | 19.0 | 18.3 | 23.9 | 18.6 | 10.0 | 16.74 | 52.5% | 28.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,303 | 27.4 | 14.3 | 29.2 | 15.2 | 10.4 | 2.5 | 0.9 | 6.1 | 13.9% | 3.5% |
| CHALLENGER | 2,930 | 15.2 | 10.1 | 21.0 | 15.4 | 15.0 | 11.8 | 11.6 | 10.85 | 38.4% | 23.4% |
| ITF_MEN | 4,530 | 10.4 | 8.7 | 18.9 | 13.8 | 20.0 | 15.8 | 12.3 | 14.18 | 48.2% | 28.2% |
| ITF_WOMEN | 6,272 | 9.8 | 6.8 | 16.6 | 15.6 | 22.6 | 19.1 | 9.6 | 15.51 | 51.2% | 28.6% |
| WTA | 863 | 22.6 | 15.4 | 33.4 | 15.4 | 10.1 | 2.3 | 0.8 | 6.12 | 13.2% | 3.1% |
| WTA125 | 531 | 22.2 | 11.7 | 29.2 | 15.2 | 14.5 | 6.8 | 0.4 | 7.71 | 21.7% | 7.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 710 | 30.7 | 22.8 | 35.8 | 9.0 | 1.3 | 0.4 | 0.0 | 4.72 | 1.7% | 0.4% |
| CHALLENGER | 2,014 | 22.0 | 15.7 | 27.4 | 14.9 | 13.0 | 5.0 | 2.1 | 6.94 | 20.0% | 7.0% |
| DOUBLES | 934 | 4.4 | 3.3 | 11.5 | 11.2 | 19.3 | 24.7 | 25.6 | 25.4 | 69.6% | 50.3% |
| ITF_MEN | 4,288 | 14.8 | 8.5 | 21.1 | 15.4 | 20.6 | 12.3 | 7.3 | 11.77 | 40.2% | 19.7% |
| ITF_WOMEN | 4,960 | 11.7 | 9.3 | 19.5 | 14.7 | 22.5 | 16.6 | 5.8 | 13.07 | 44.9% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 645 | 21.6 | 14.9 | 27.3 | 17.2 | 13.6 | 5.0 | 0.5 | 7.7 | 19.1% | 5.4% |
| WTA125 | 648 | 19.9 | 14.0 | 22.1 | 18.5 | 14.7 | 8.5 | 2.3 | 8.32 | 25.5% | 10.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,289 | 30.1 | 14.6 | 25.0 | 17.9 | 10.5 | 1.1 | 0.8 | 5.84 | 12.4% | 1.9% |
| CHALLENGER | 2,134 | 19.9 | 12.5 | 25.0 | 18.6 | 15.3 | 6.1 | 2.6 | 8.38 | 24.0% | 8.8% |
| ITF_MEN | 3,228 | 14.2 | 10.9 | 21.7 | 16.5 | 19.4 | 12.2 | 5.0 | 10.89 | 36.7% | 17.2% |
| ITF_WOMEN | 4,501 | 12.5 | 8.2 | 18.5 | 18.7 | 23.4 | 15.0 | 3.6 | 12.77 | 42.0% | 18.6% |
| WTA | 850 | 21.5 | 10.5 | 25.6 | 16.1 | 19.6 | 5.3 | 1.3 | 8.11 | 26.2% | 6.6% |
| WTA125 | 509 | 13.9 | 7.9 | 23.0 | 19.8 | 19.6 | 14.2 | 1.6 | 11.08 | 35.4% | 15.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,289 | 23.8 | 14.7 | 24.6 | 19.2 | 14.7 | 1.9 | 1.0 | 6.9 | 17.6% | 2.9% |
| CHALLENGER | 2,134 | 19.4 | 9.6 | 23.9 | 15.9 | 18.7 | 9.8 | 2.8 | 9.19 | 31.2% | 12.5% |
| ITF_MEN | 3,229 | 12.2 | 8.9 | 19.1 | 16.3 | 21.4 | 15.4 | 6.7 | 12.83 | 43.5% | 22.1% |
| ITF_WOMEN | 4,501 | 10.3 | 6.8 | 14.4 | 14.0 | 24.4 | 19.8 | 10.3 | 16.62 | 54.5% | 30.0% |
| WTA | 850 | 18.4 | 8.0 | 18.8 | 16.2 | 22.8 | 14.5 | 1.3 | 11.74 | 38.6% | 15.8% |
| WTA125 | 509 | 5.9 | 4.5 | 19.1 | 18.7 | 23.6 | 19.2 | 9.0 | 16.14 | 51.9% | 28.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 690 | 30.7 | 23.0 | 36.1 | 9.1 | 0.6 | 0.4 | 0.0 | 4.7 | 1.0% | 0.4% |
| CHALLENGER | 1,741 | 23.8 | 17.2 | 29.5 | 14.8 | 12.0 | 2.2 | 0.6 | 6.33 | 14.8% | 2.8% |
| DOUBLES | 866 | 4.4 | 3.4 | 11.8 | 11.2 | 19.4 | 24.6 | 25.3 | 24.87 | 69.3% | 49.9% |
| ITF_MEN | 3,486 | 16.4 | 9.3 | 23.2 | 16.3 | 20.4 | 10.1 | 4.2 | 10.23 | 34.7% | 14.3% |
| ITF_WOMEN | 4,063 | 12.8 | 10.0 | 21.3 | 15.5 | 22.7 | 14.9 | 2.6 | 11.65 | 40.3% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 611 | 22.1 | 15.6 | 27.5 | 17.2 | 13.9 | 3.8 | 0.0 | 7.21 | 17.7% | 3.8% |
| WTA125 | 548 | 21.9 | 15.5 | 23.5 | 20.4 | 13.0 | 5.3 | 0.4 | 7.42 | 18.6% | 5.7% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 934 | 4.4 | 3.3 | 11.5 | 11.2 | 19.3 | 24.7 | 25.6 | 25.4 | 69.6% | 50.3% |
| singles | 13,414 | 16.2 | 11.2 | 22.7 | 14.9 | 18.4 | 11.6 | 5.0 | 9.95 | 34.9% | 16.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,793 | 13.4 | 9.2 | 20.4 | 15.8 | 17.2 | 13.9 | 9.9 | 12.22 | 41.1% | 23.9% |
| Grass | 112 | 11.6 | 17.9 | 17.0 | 9.8 | 24.1 | 15.2 | 4.5 | 11.99 | 43.8% | 19.6% |
| Hard | 10,886 | 14.3 | 8.5 | 18.6 | 15.8 | 19.1 | 14.2 | 9.5 | 12.69 | 42.8% | 23.7% |
| UNKNOWN | 1,638 | 11.6 | 8.0 | 15.6 | 17.6 | 19.8 | 16.7 | 10.7 | 14.09 | 47.2% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,071 | 20.0 | 10.8 | 21.2 | 17.0 | 15.4 | 8.6 | 7.1 | 9.45 | 31.1% | 15.8% |
| B | 2,218 | 14.3 | 9.2 | 19.9 | 17.1 | 17.6 | 12.0 | 9.7 | 11.47 | 39.4% | 21.8% |
| C | 2,397 | 13.3 | 9.7 | 19.4 | 14.6 | 19.2 | 14.6 | 9.2 | 12.66 | 43.0% | 23.8% |
| D | 2,891 | 10.8 | 8.4 | 17.9 | 16.0 | 22.3 | 14.9 | 9.9 | 13.94 | 47.0% | 24.7% |
| F | 3,852 | 7.9 | 5.2 | 15.0 | 14.8 | 20.9 | 22.8 | 13.3 | 18.24 | 57.0% | 36.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,221 | 22.4 | 15.9 | 28.8 | 15.2 | 11.5 | 4.5 | 1.7 | 6.75 | 17.6% | 6.1% |
| B | 2,218 | 15.1 | 10.0 | 24.1 | 16.2 | 19.2 | 11.2 | 4.3 | 10.17 | 34.6% | 15.5% |
| C | 2,842 | 12.2 | 7.6 | 18.0 | 14.5 | 20.4 | 15.8 | 11.5 | 13.75 | 47.7% | 27.2% |
| D | 2,213 | 14.1 | 9.8 | 20.9 | 13.4 | 21.6 | 13.9 | 6.3 | 11.85 | 41.8% | 20.2% |
| F | 2,854 | 9.5 | 7.4 | 15.1 | 14.0 | 23.8 | 20.7 | 9.5 | 16.63 | 54.0% | 30.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 5,609 | 18.3 | 9.8 | 20.3 | 16.9 | 15.6 | 9.6 | 9.4 | 10.43 | 34.6% | 19.0% |
| LIMITED | 4,017 | 15.3 | 10.5 | 20.7 | 15.7 | 18.4 | 12.8 | 6.7 | 11.05 | 37.9% | 19.4% |
| POOR | 6,803 | 9.1 | 6.7 | 16.2 | 15.4 | 21.5 | 19.3 | 11.8 | 15.99 | 52.5% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,938 | 31.4 | 24.1 | 36.5 | 5.5 | 1.8 | 0.7 | 0.1 | 4.51 | 2.5% | 0.8% |
| GAME_SPREAD | 2,838 | 25.6 | 15.9 | 36.8 | 16.8 | 4.2 | 0.4 | 0.2 | 6.02 | 4.8% | 0.6% |
| MATCH_WINNER | 14,348 | 15.4 | 10.7 | 22.0 | 14.7 | 18.5 | 12.4 | 6.3 | 10.46 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 5,389 | 33.1 | 19.5 | 31.1 | 9.7 | 5.2 | 1.2 | 0.2 | 4.76 | 6.6% | 1.4% |
| TOTAL_GAMES | 4,285 | 6.7 | 9.1 | 39.1 | 29.6 | 10.4 | 2.7 | 2.4 | 9.46 | 15.5% | 5.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,817 | 25.6 | 38.0 | 31.6 | 0.3 | 3.9 | 0.4 | 0.1 | 4.32 | 4.5% | 0.6% |
| GAME_SPREAD | 3,431 | 45.1 | 16.3 | 29.1 | 7.3 | 1.1 | 0.7 | 0.4 | 3.59 | 2.2% | 1.1% |
| TOTAL_GAMES | 5,346 | 3.4 | 6.5 | 43.4 | 36.3 | 6.5 | 1.9 | 2.0 | 9.72 | 10.4% | 3.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,817 | 26.2 | 18.5 | 37.3 | 9.3 | 6.3 | 2.1 | 0.3 | 5.52 | 8.8% | 2.4% |
| GAME_SPREAD | 3,431 | 19.0 | 13.2 | 30.3 | 21.3 | 13.1 | 2.4 | 0.7 | 7.85 | 16.2% | 3.1% |
| TOTAL_GAMES | 5,355 | 6.5 | 8.7 | 38.1 | 28.4 | 12.8 | 3.2 | 2.2 | 9.67 | 18.2% | 5.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 16,429 | 42.8% | 24.1% | 12.72 | 33.2% | 13.9% | 10.28 |
| gen1_elo | 16,429 | 42.2% | 23.5% | 12.16 | 32.2% | 13.8% | 9.64 |
| gen1_sr | 16,429 | 51.1% | 29.5% | 15.42 | 42.4% | 19.4% | 12.61 |
| gen2 | 16,429 | 50.1% | 29.9% | 15.03 | 42.7% | 21.2% | 12.59 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 8,756 | 16.7 | 10.8 | 21.7 | 17.4 | 19.0 | 11.1 | 3.3 | 10.21 | 33.4% | 14.4% |
| STALE | 7,673 | 10.5 | 6.2 | 15.3 | 14.3 | 18.5 | 18.1 | 17.1 | 17.02 | 53.7% | 35.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 7,816 | 17.3 | 11.7 | 23.9 | 14.7 | 16.8 | 11.0 | 4.7 | 9.27 | 32.5% | 15.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 30,777 | 7816 | 12228 | 10733 | 23.9 | 142.9 | 1400.4 |
| ge_15pp | 12,374 | 2536 | 4210 | 5628 | 26.9 | 440.0 | 1380.4 |
| ge_25pp | 6,643 | 1223 | 1848 | 3572 | 34.5 | 571.4 | 1380.4 |
| lt_10pp | 13,671 | 4135 | 5943 | 3593 | 22.4 | 48.8 | 1341.5 |

Current slate `SL-20261013T144733Z-9dcf4e58`: 443 priced rows, quote age at build {'median': 7.7, 'max': 7.8}, freshness {'FRESH': 443}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 8 | 0.0 | 0.0 | 37.5 | 0.0 | 37.5 | 25.0 | 0.0 | 20.45 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 9 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,228 | 22.1 | 11.0 | 22.9 | 18.8 | 18.3 | 6.4 | 0.5 | 8.59 | 25.2% | 6.9% |
| KALSHI_LONE_OUTLIER | 5 | 20.0 | 0.0 | 60.0 | 0.0 | 20.0 | 0.0 | 0.0 | 5.14 | 20.0% | 0.0% |
| MARKETS_AGREE | 215 | 71.6 | 28.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.03 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 402 | 0.0 | 4.2 | 35.3 | 29.6 | 21.9 | 8.2 | 0.8 | 11.46 | 30.9% | 9.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 16,429 | 1867 (11.4%) | 21.5% | 0.6% | {"EXTERNAL_STALE": 1228, "AGREES_WITH_KALSHI": 402, "ALL_AGREE": 215, "EXTERNAL_OUTLIER": 9, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 5, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 7,039 | 440 (6.2%) | 28.2% | 1.4% | {"EXTERNAL_STALE": 310, "AGREES_WITH_KALSHI": 124, "SUPPORTS_MODEL_DIRECTION": 5, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp | 3,958 | 123 (3.1%) | 29.3% | 1.6% | {"EXTERNAL_STALE": 85, "AGREES_WITH_KALSHI": 36, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_ge_25pp_pregame_clean | 1,741 | 117 (6.7%) | 29.1% | 1.7% | {"EXTERNAL_STALE": 81, "AGREES_WITH_KALSHI": 34, "SUPPORTS_MODEL_DIRECTION": 2} |
| fair_v1_lt_10pp | 6,767 | 1077 (15.9%) | 14.8% | 0.6% | {"EXTERNAL_STALE": 687, "ALL_AGREE": 215, "AGREES_WITH_KALSHI": 159, "EXTERNAL_OUTLIER": 9, "AGREES_WITH_MODEL": 4, "SUPPORTS_MODEL_DIRECTION": 2, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 3,259 | 11.8 | 8.3 | 19.7 | 14.9 | 21.4 | 14.0 | 10.0 | 13.27 | 45.4% | 24.0% |
| 4-10x | 2,191 | 12.0 | 8.8 | 19.1 | 15.4 | 19.7 | 15.9 | 9.2 | 13.12 | 44.7% | 25.1% |
| <2x | 8,797 | 15.8 | 9.3 | 18.9 | 17.1 | 17.2 | 12.6 | 9.1 | 11.7 | 38.9% | 21.7% |
| >=10x | 2,182 | 10.5 | 6.7 | 16.2 | 13.5 | 20.0 | 20.7 | 12.3 | 16.45 | 53.1% | 33.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 4,333 | 14.1 | 8.3 | 19.4 | 16.0 | 18.9 | 12.7 | 10.6 | 12.51 | 42.2% | 23.3% |
| 300-1000 | 3,824 | 12.0 | 8.8 | 17.3 | 16.0 | 21.2 | 15.6 | 9.0 | 13.64 | 45.8% | 24.6% |
| <300 | 4,396 | 8.5 | 6.2 | 15.9 | 14.6 | 20.8 | 21.1 | 12.8 | 17.09 | 54.8% | 34.0% |
| >=3000 | 3,876 | 21.1 | 11.8 | 22.6 | 17.5 | 13.8 | 7.4 | 5.8 | 8.5 | 27.0% | 13.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 535 | 0.5355 | 0.4034 | 0.4804 | +0.055 | -0.077 | 0.0024 ± 0.0063 |
| ratio 4-10x | 358 | 0.5841 | 0.4438 | 0.5196 | +0.065 | -0.076 | 0.0039 ± 0.0084 |
| ratio <2x | 1283 | 0.5392 | 0.4176 | 0.4567 | +0.082 | -0.039 | 0.0115 ± 0.004 |
| ratio >=10x | 382 | 0.5479 | 0.3802 | 0.4424 | +0.105 | -0.062 | 0.0089 ± 0.0091 |
| thinner_sample 1000-3000 | 718 | 0.5447 | 0.4192 | 0.4749 | +0.070 | -0.056 | 0.0052 ± 0.0054 |
| thinner_sample 300-1000 | 644 | 0.5609 | 0.4222 | 0.4845 | +0.076 | -0.062 | 0.0042 ± 0.0061 |
| thinner_sample <300 | 741 | 0.5458 | 0.3857 | 0.4588 | +0.087 | -0.073 | 0.0097 ± 0.0063 |
| thinner_sample >=3000 | 455 | 0.5274 | 0.433 | 0.4505 | +0.077 | -0.018 | 0.0159 ± 0.0054 |
| data_status ADEQUATE | 732 | 0.531 | 0.4275 | 0.4522 | +0.079 | -0.025 | 0.0097 ± 0.0046 |
| data_status LIMITED | 684 | 0.5541 | 0.4245 | 0.4942 | +0.060 | -0.070 | 0.0022 ± 0.0056 |
| data_status POOR | 1142 | 0.5508 | 0.3962 | 0.4632 | +0.088 | -0.067 | 0.0108 ± 0.005 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 392 | 0.1924 | 0.1938 | -0.0014 ± 0.0008 | 0.5631 | 0.5661 | 0.4895 | 0.4746 | 0.5179 | -0.054 ± 0.0234 | -0.01 (3) |
| 3-5 | 262 | 0.1895 | 0.1907 | -0.0011 ± 0.0021 | 0.5589 | 0.5602 | 0.5071 | 0.4673 | 0.4962 | -0.066 ± 0.0275 | 0.02 (1) |
| 5-10 | 533 | 0.198 | 0.2007 | -0.0026 ± 0.0029 | 0.5802 | 0.586 | 0.5139 | 0.4398 | 0.4859 | -0.074 ± 0.0202 | -0.0125 (4) |
| 10-15 | 460 | 0.2108 | 0.2033 | +0.0074 ± 0.0053 | 0.6087 | 0.5876 | 0.5227 | 0.3989 | 0.4283 | -0.091 ± 0.0209 | -0.0633 (3) |
| 15-25 | 551 | 0.2276 | 0.2148 | +0.0127 ± 0.0077 | 0.6495 | 0.6166 | 0.5753 | 0.3806 | 0.4465 | -0.080 ± 0.0197 | -0.0133 (6) |
| 25-40 | 292 | 0.2213 | 0.2044 | +0.0170 ± 0.0158 | 0.6336 | 0.5867 | 0.6491 | 0.3389 | 0.4658 | -0.070 ± 0.0238 | -0.01 (1) |
| 40+ | 68 | 0.2909 | 0.1768 | +0.1141 ± 0.0454 | 0.7906 | 0.5286 | 0.7508 | 0.3033 | 0.3971 | -0.121 ± 0.0447 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1918 | 0.1765 | 0.1776 | -0.0011 ± 0.0003 | 0.5271 | 0.5281 | 0.4774 | 0.4624 | 0.4969 | -0.023 ± 0.0098 | -0.0188 (8) |
| 3-5 | 1210 | 0.1946 | 0.193 | +0.0015 ± 0.001 | 0.5704 | 0.5624 | 0.48 | 0.4404 | 0.4372 | -0.063 ± 0.0129 | 0.02 (1) |
| 5-10 | 2615 | 0.1936 | 0.1922 | +0.0014 ± 0.0013 | 0.5689 | 0.564 | 0.487 | 0.4132 | 0.4371 | -0.043 ± 0.0087 | -0.0082 (17) |
| 10-15 | 2272 | 0.2014 | 0.1834 | +0.0180 ± 0.0023 | 0.5886 | 0.5388 | 0.4797 | 0.3554 | 0.3455 | -0.076 ± 0.009 | -0.0475 (4) |
| 15-25 | 2677 | 0.2063 | 0.1705 | +0.0358 ± 0.0031 | 0.6045 | 0.5041 | 0.4987 | 0.3031 | 0.3115 | -0.066 ± 0.008 | -0.0048 (29) |
| 25-40 | 2133 | 0.2194 | 0.1242 | +0.0952 ± 0.0048 | 0.632 | 0.3837 | 0.5289 | 0.2149 | 0.2236 | -0.063 ± 0.0074 | -0.01 (1) |
| 40+ | 1458 | 0.3708 | 0.0448 | +0.3260 ± 0.0061 | 0.9671 | 0.1759 | 0.6239 | 0.1074 | 0.0604 | -0.085 ± 0.0052 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 298 | 0.1964 | 0.1967 | -0.0003 ± 0.0009 | 0.5754 | 0.5762 | 0.4963 | 0.4813 | 0.4933 | -0.089 ± 0.0275 | -0.01 (1) |
| 3-5 | 201 | 0.2125 | 0.2118 | +0.0007 ± 0.0026 | 0.6073 | 0.6072 | 0.5194 | 0.4793 | 0.4876 | -0.077 ± 0.0342 | 0.02 (1) |
| 5-10 | 469 | 0.1959 | 0.1963 | -0.0004 ± 0.0031 | 0.5734 | 0.5748 | 0.5546 | 0.4794 | 0.5181 | -0.067 ± 0.0212 | -0.01 (4) |
| 10-15 | 429 | 0.2167 | 0.2055 | +0.0111 ± 0.0055 | 0.62 | 0.5966 | 0.5779 | 0.4533 | 0.4755 | -0.106 ± 0.0228 | -0.05 (4) |
| 15-25 | 613 | 0.2242 | 0.2076 | +0.0165 ± 0.0073 | 0.637 | 0.5977 | 0.5926 | 0.3955 | 0.4568 | -0.085 ± 0.0187 | -0.01 (5) |
| 25-40 | 400 | 0.2706 | 0.1959 | +0.0748 ± 0.014 | 0.7579 | 0.5702 | 0.6689 | 0.3545 | 0.395 | -0.137 ± 0.0219 | -0.025 (2) |
| 40+ | 148 | 0.3439 | 0.195 | +0.1489 ± 0.035 | 0.9629 | 0.5677 | 0.7527 | 0.2745 | 0.3716 | -0.054 ± 0.0345 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1650 | 0.1821 | 0.1825 | -0.0004 ± 0.0004 | 0.5399 | 0.5406 | 0.4941 | 0.4795 | 0.5036 | -0.032 ± 0.0109 | -0.0217 (6) |
| 3-5 | 1054 | 0.1951 | 0.1946 | +0.0006 ± 0.0011 | 0.5655 | 0.5642 | 0.5166 | 0.4767 | 0.4886 | -0.039 ± 0.0138 | 0.02 (1) |
| 5-10 | 2292 | 0.1892 | 0.1871 | +0.0020 ± 0.0014 | 0.5599 | 0.552 | 0.5145 | 0.4407 | 0.4655 | -0.038 ± 0.0092 | -0.01 (5) |
| 10-15 | 2009 | 0.1974 | 0.1819 | +0.0155 ± 0.0024 | 0.5803 | 0.5335 | 0.5248 | 0.4005 | 0.4037 | -0.067 ± 0.0097 | -0.02 (14) |
| 15-25 | 2870 | 0.2153 | 0.1759 | +0.0395 ± 0.0031 | 0.6261 | 0.5195 | 0.5347 | 0.3386 | 0.3394 | -0.076 ± 0.0079 | -0.0026 (27) |
| 25-40 | 2484 | 0.2489 | 0.1371 | +0.1118 ± 0.0047 | 0.707 | 0.418 | 0.5622 | 0.2464 | 0.2291 | -0.089 ± 0.0075 | -0.015 (6) |
| 40+ | 1924 | 0.4009 | 0.0693 | +0.3316 ± 0.0068 | 1.0505 | 0.2405 | 0.6674 | 0.1304 | 0.104 | -0.068 ± 0.0058 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 388 | 0.1941 | 0.1967 | -0.0026 ± 0.0008 | 0.568 | 0.5749 | 0.4961 | 0.4809 | 0.5593 | -0.003 ± 0.0228 | -0.0133 (6) |
| 3-5 | 279 | 0.1866 | 0.1853 | +0.0013 ± 0.002 | 0.5492 | 0.5463 | 0.4982 | 0.4589 | 0.4624 | -0.113 ± 0.0272 | -0.01 (1) |
| 5-10 | 575 | 0.2003 | 0.1995 | +0.0008 ± 0.0028 | 0.5868 | 0.5825 | 0.508 | 0.4344 | 0.4626 | -0.082 ± 0.0192 | -0.01 (4) |
| 10-15 | 438 | 0.2081 | 0.2098 | -0.0017 ± 0.0054 | 0.6039 | 0.602 | 0.5388 | 0.4163 | 0.4863 | -0.063 ± 0.0217 | -0.044 (5) |
| 15-25 | 515 | 0.2303 | 0.2073 | +0.0230 ± 0.0078 | 0.6597 | 0.5984 | 0.5798 | 0.3868 | 0.4252 | -0.108 ± 0.0198 | -0.03 (1) |
| 25-40 | 302 | 0.2077 | 0.2131 | -0.0054 ± 0.0156 | 0.6022 | 0.6082 | 0.6544 | 0.3418 | 0.5033 | -0.040 ± 0.0232 | 0.0 (1) |
| 40+ | 61 | 0.3195 | 0.1777 | +0.1418 ± 0.0492 | 0.8584 | 0.5313 | 0.7574 | 0.3028 | 0.377 | -0.134 ± 0.0497 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1822 | 0.1854 | 0.1866 | -0.0012 ± 0.0004 | 0.547 | 0.5495 | 0.4852 | 0.47 | 0.506 | -0.018 ± 0.0102 | -0.0183 (23) |
| 3-5 | 1269 | 0.1871 | 0.1851 | +0.0020 ± 0.001 | 0.5511 | 0.5466 | 0.4784 | 0.4391 | 0.4342 | -0.070 ± 0.0125 | -0.0243 (7) |
| 5-10 | 2811 | 0.193 | 0.1879 | +0.0050 ± 0.0012 | 0.5694 | 0.5529 | 0.483 | 0.4094 | 0.4109 | -0.061 ± 0.0082 | -0.01 (18) |
| 10-15 | 2133 | 0.1947 | 0.1807 | +0.0140 ± 0.0023 | 0.5738 | 0.5304 | 0.4941 | 0.371 | 0.3755 | -0.065 ± 0.0091 | -0.03 (9) |
| 15-25 | 2754 | 0.2085 | 0.1703 | +0.0382 ± 0.0031 | 0.6117 | 0.5047 | 0.5022 | 0.3069 | 0.309 | -0.070 ± 0.0079 | -0.03 (2) |
| 25-40 | 2105 | 0.2137 | 0.122 | +0.0916 ± 0.0048 | 0.6189 | 0.3767 | 0.5237 | 0.207 | 0.2242 | -0.057 ± 0.0072 | 0.0 (1) |
| 40+ | 1389 | 0.3853 | 0.0466 | +0.3387 ± 0.0065 | 1.0072 | 0.1813 | 0.6323 | 0.1096 | 0.0583 | -0.088 ± 0.0055 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 696 | 0.2017 | 0.2024 | -0.0007 ± 0.0006 | 0.5856 | 0.587 | 0.5006 | 0.4855 | 0.5029 | -0.036 ± 0.017 | -0.0226 (46) |
| 3-5 | 513 | 0.1972 | 0.1968 | +0.0004 ± 0.0016 | 0.5744 | 0.5715 | 0.4804 | 0.4407 | 0.4522 | -0.045 ± 0.0197 | -0.0058 (33) |
| 5-10 | 1055 | 0.1909 | 0.1853 | +0.0056 ± 0.002 | 0.5656 | 0.551 | 0.4803 | 0.4068 | 0.4066 | -0.063 ± 0.0135 | -0.0049 (73) |
| 10-15 | 672 | 0.2041 | 0.1948 | +0.0094 ± 0.0043 | 0.596 | 0.571 | 0.4967 | 0.3737 | 0.3958 | -0.046 ± 0.017 | 0.0014 (64) |
| 15-25 | 903 | 0.2344 | 0.2123 | +0.0221 ± 0.006 | 0.6676 | 0.611 | 0.5578 | 0.3635 | 0.4053 | -0.054 ± 0.0154 | -0.0216 (58) |
| 25-40 | 512 | 0.2534 | 0.1914 | +0.0620 ± 0.012 | 0.7138 | 0.5581 | 0.6421 | 0.3287 | 0.3848 | -0.088 ± 0.018 | -0.0216 (25) |
| 40+ | 175 | 0.3608 | 0.1929 | +0.1680 ± 0.034 | 1.0498 | 0.5667 | 0.7949 | 0.3003 | 0.4 | -0.066 ± 0.0304 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2152 | 0.1912 | 0.1915 | -0.0003 ± 0.0003 | 0.5584 | 0.5579 | 0.5024 | 0.4871 | 0.5005 | -0.031 ± 0.0094 | -0.0155 (82) |
| 3-5 | 1493 | 0.1893 | 0.1868 | +0.0026 ± 0.0009 | 0.5536 | 0.5474 | 0.4866 | 0.447 | 0.4354 | -0.058 ± 0.0112 | -0.0148 (63) |
| 5-10 | 3040 | 0.1907 | 0.1828 | +0.0079 ± 0.0012 | 0.565 | 0.543 | 0.4762 | 0.4025 | 0.3891 | -0.066 ± 0.0079 | -0.0087 (125) |
| 10-15 | 2046 | 0.1996 | 0.1866 | +0.0131 ± 0.0024 | 0.5858 | 0.5511 | 0.5056 | 0.3826 | 0.391 | -0.051 ± 0.0095 | -0.0053 (105) |
| 15-25 | 2580 | 0.2304 | 0.1988 | +0.0316 ± 0.0034 | 0.6648 | 0.5774 | 0.5526 | 0.3577 | 0.3756 | -0.060 ± 0.0088 | -0.0255 (106) |
| 25-40 | 1740 | 0.2537 | 0.166 | +0.0877 ± 0.0062 | 0.7201 | 0.4917 | 0.604 | 0.289 | 0.3098 | -0.079 ± 0.0095 | -0.0206 (47) |
| 40+ | 856 | 0.3847 | 0.1266 | +0.2580 ± 0.0131 | 1.094 | 0.3891 | 0.7087 | 0.1993 | 0.2138 | -0.071 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2558 | 1.07 ± 0.056 | 1.195 | 0.169 | 0.1696 | 0.2101 | 0.2019 |
| gen2 | 2558 | 0.873 ± 0.05 | 1.134 | 0.1818 | 0.1694 | 0.2278 | 0.2017 |
| gen1_elo | 2558 | 1.052 ± 0.055 | 1.185 | 0.1732 | 0.1699 | 0.2089 | 0.2019 |
| gen1_sr | 2558 | 1.078 ± 0.064 | 1.214 | 0.1407 | 0.1713 | 0.2236 | 0.2014 |
| gen1_ledger | 4526 | 0.877 ± 0.037 | 1.085 | 0.1753 | 0.1869 | 0.2176 | 0.197 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 12,374)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,229 | 26.1% |
| STALE_QUOTE | market_freshness | 2,450 | 19.8% |
| BOOK_QUALITY | execution | 2,245 | 18.1% |
| POOR_DATA | data | 1,315 | 10.6% |
| LIMITED_DATA | data | 956 | 7.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 682 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 604 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 420 | 3.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 362 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 111 | 0.9% |

Cause class: coverage 26.1%, market_freshness 19.8%, data 18.4%, execution 18.1%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.9%, mapping 3.4%, model_calibration 0.9%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.4%, START_UNVERIFIABLE 95.8%, LOW_DATA_QUALITY 68.0%, THIN_PLAYER_HISTORY 56.5%, STALE_PLAYER_DATA 56.1%, STALE_KALSHI_QUOTE 45.5%, MODEL_INTERNAL_DISAGREEMENT 38.2%, ASYMMETRIC_SAMPLE_SIZE 30.6%, WIDE_SPREAD 24.0%, MODEL_HIGH_UNCERTAINTY 16.5%, PLAYER_IDENTITY_RISK 12.2%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 1.5%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 28.6%, POST_SETTLEMENT_OBSERVATION 26.1%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 6,643)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,549 | 38.4% |
| BOOK_QUALITY | execution | 1,168 | 17.6% |
| STALE_QUOTE | market_freshness | 1,093 | 16.4% |
| POOR_DATA | data | 540 | 8.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 369 | 5.5% |
| LIMITED_DATA | data | 281 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 260 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 225 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 133 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 25 | 0.4% |

Cause class: coverage 38.4%, execution 17.6%, market_freshness 16.4%, data 12.4%, market_freshness/coverage 8.9%, mapping 3.9%, model_calibration_or_unknown 2.0%, model_calibration 0.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.2%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 71.7%, THIN_PLAYER_HISTORY 58.8%, STALE_KALSHI_QUOTE 53.8%, STALE_PLAYER_DATA 50.8%, MODEL_INTERNAL_DISAGREEMENT 39.5%, ASYMMETRIC_SAMPLE_SIZE 32.7%, WIDE_SPREAD 23.7%, MODEL_HIGH_UNCERTAINTY 17.4%, PLAYER_IDENTITY_RISK 15.6%, EVENT_MAPPING_RISK 9.7%, LEVEL_TRANSFER_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.7%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 41.2%, POST_SETTLEMENT_OBSERVATION 38.4%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 5438, "IDENTITY_AMBIGUOUS": 1205}; ticker orientation: {"VERIFIED": 6643}.

Checks: discipline:AMBIGUOUS 470, discipline:PASS 6173, identity_confidence:AMBIGUOUS 1037, identity_confidence:PASS 5606, level_mapping:NA 482, level_mapping:PASS 6161, market_pair:AMBIGUOUS 230, market_pair:NA 161, market_pair:PASS 6252, model_complement:NA 128, model_complement:PASS 6515, namesake:PASS 6643, physical_match_id:NA 2685, physical_match_id:PASS 3958, player_ids:PASS 6643, same_pair_other_event:PASS 6643, ticker_orientation:PASS 6643

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,013 | 1.4% | 1.4% | 0.4% | {"market_freshness": 20, "execution": 8, "market_freshness/coverage": 1} | 5.28 | 0.2116 / 0.2133 (241) | 16.4% | 0.5% | 5.5% | 1.7% |
| CHALLENGER | 4,944 | 16.9% | 6.1% | 12.5% | {"coverage": 496, "market_freshness": 111, "market_freshness/coverage": 102, "data": 55, "model_calibration_or_unknown": 47, "execution": 12, "mapping": 6, "model_calibration": 4} | 7.24 | 0.2156 / 0.2016 (1231) | 38.1% | 8.5% | 2.5% | 21.6% |
| DOUBLES | 934 | 50.3% | 49.9% | 7.1% | {"execution": 183, "mapping": 143, "market_freshness": 106, "market_freshness/coverage": 31, "coverage": 7} | 24.87 | 0.3363 / 0.2321 (264) | 25.1% | 0.0% | 100.0% | 7.3% |
| ITF_MEN | 8,818 | 23.8% | 15.7% | 31.5% | {"coverage": 857, "execution": 441, "market_freshness": 294, "data": 283, "market_freshness/coverage": 183, "mapping": 34, "model_calibration_or_unknown": 2} | 10.59 | 0.2106 / 0.1932 (2208) | 36.9% | 55.4% | 8.0% | 23.9% |
| ITF_WOMEN | 11,232 | 26.3% | 18.1% | 44.5% | {"coverage": 1172, "execution": 504, "market_freshness": 491, "data": 449, "market_freshness/coverage": 232, "mapping": 71, "model_calibration_or_unknown": 26, "model_calibration": 10} | 12.32 | 0.2038 / 0.1931 (2446) | 38.4% | 57.9% | 9.7% | 23.8% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,508 | 6.2% | 5.4% | 1.4% | {"market_freshness": 36, "model_calibration_or_unknown": 20, "data": 11, "market_freshness/coverage": 10, "execution": 6, "model_calibration": 5, "coverage": 4, "mapping": 1} | 7.78 | 0.2314 / 0.2235 (249) | 26.7% | 1.4% | 1.8% | 3.1% |
| WTA125 | 1,179 | 13.3% | 10.5% | 2.4% | {"model_calibration_or_unknown": 36, "market_freshness/coverage": 34, "market_freshness": 33, "data": 23, "coverage": 12, "execution": 9, "model_calibration": 6, "mapping": 4} | 9.2 | 0.223 / 0.2145 (403) | 23.3% | 8.6% | 4.1% | 10.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 8 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 9 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 10 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 11 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 12 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 13 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 14 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 15 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 16 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 17 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 19 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 20 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 21 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 22 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 23 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 24 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 25 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 26 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 27 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 28 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 29 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 30 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 31 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 32 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 33 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 34 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 35 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 36 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |
| 37 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 189 min (STALE); no external reference |
| 38 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 39 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 40 | `KXITFMATCH-26OCT13VISMUE-MUE` | ITF_MEN | fair_v1 | 25% / 98% | -74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 103 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 0.0); no external reference |
| 41 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 42 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 44 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 153 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 45 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 47 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 48 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 49 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 26 min (AGING); no external reference |
| 50 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9816, "by_level_share_of_ge_25pp": {"ATP": 0.0044, "CHALLENGER": 0.1254, "DOUBLES": 0.0708, "ITF_MEN": 0.3152, "ITF_WOMEN": 0.4448, "OTHER": 0.0018, "WTA": 0.014, "WTA125": 0.0236}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5377, "share_primary_cause_market_settled_or_in_play": 0.4731, "share_primary_cause_stale_quote_only": 0.1645}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 6643, "identity_ambiguous_share": 0.1814, "ticker_orientation": {"VERIFIED": 6643}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3958, "with_external": 123, "coverage": 0.0311, "external_status": {"EXTERNAL_STALE": 85, "AGREES_WITH_KALSHI": 36, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 85, "MODEL_LONE_OUTLIER": 36, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2927, "share_external_supports_model": 0.0163}, "pregame_clean_ge_25pp": {"n": 1741, "with_external": 117, "coverage": 0.0672, "external_status": {"EXTERNAL_STALE": 81, "AGREES_WITH_KALSHI": 34, "SUPPORTS_MODEL_DIRECTION": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 81, "MODEL_LONE_OUTLIER": 34, "ALL_THREE_DISAGREE": 2}, "share_external_agrees_with_kalshi": 0.2906, "share_external_supports_model": 0.0171}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 605.0, "median_sample_ratio": 2.33, "median_min_matches": 21.0, "median_max_days_since_last": 198.0, "share_severe_asymmetry": 0.1868, "data_status": {"POOR": 3437, "LIMITED": 1978, "ADEQUATE": 1228}, "comparison_lt_10pp": {"median_thinner_serve_points": 1892.0, "median_sample_ratio": 1.66, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 535, "model_minus_observed": 0.0552, "kalshi_minus_observed": -0.077, "brier_diff_model_minus_kalshi": 0.0024}, "4-10x": {"n": 358, "model_minus_observed": 0.0646, "kalshi_minus_observed": -0.0758, "brier_diff_model_minus_kalshi": 0.0039}, "<2x": {"n": 1283, "model_minus_observed": 0.0824, "kalshi_minus_observed": -0.0391, "brier_diff_model_minus_kalshi": 0.0115}, ">=10x": {"n": 382, "model_minus_observed": 0.1055, "kalshi_minus_observed": -0.0622, "brier_diff_model_minus_kalshi": 0.0089}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2558, "model": {"intercept": -0.544, "slope": 0.873, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.233, "slope": 1.134, "slope_se": 0.057}, "mean_extremity_model": 0.1818, "mean_extremity_kalshi": 0.1694, "model_brier": 0.2278, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0261, "brier_diff_se": 0.0037, "model_logloss": 0.6507, "kalshi_logloss": 0.5855}, "fair_v1": {"n": 2558, "model": {"intercept": -0.382, "slope": 1.07, "slope_se": 0.056}, "kalshi_mid_same_rows": {"intercept": 0.342, "slope": 1.195, "slope_se": 0.059}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1696, "model_brier": 0.2101, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.003, "model_logloss": 0.6071, "kalshi_logloss": 0.5857}, "gen1_elo": {"n": 2558, "model": {"intercept": -0.35, "slope": 1.052, "slope_se": 0.055}, "kalshi_mid_same_rows": {"intercept": 0.354, "slope": 1.185, "slope_se": 0.058}, "mean_extremity_model": 0.1732, "mean_extremity_kalshi": 0.1699, "model_brier": 0.2089, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.007, "brier_diff_se": 0.003, "model_logloss": 0.6057, "kalshi_logloss": 0.5858}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2409, "share_ge_15": 0.4284, "median_abs_gap": 12.72, "n": 16429}, "gen1_elo": {"share_ge_25": 0.2354, "share_ge_15": 0.422, "median_abs_gap": 12.16, "n": 16429}, "gen1_sr": {"share_ge_25": 0.2953, "share_ge_15": 0.5115, "median_abs_gap": 15.42, "n": 16429}, "gen2": {"share_ge_25": 0.2995, "share_ge_15": 0.5008, "median_abs_gap": 15.03, "n": 16429}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1391, "share_ge_15": 0.3318, "median_abs_gap": 10.28, "n": 12511}, "gen1_elo": {"share_ge_25": 0.1375, "share_ge_15": 0.3217, "median_abs_gap": 9.64, "n": 12510}, "gen1_sr": {"share_ge_25": 0.1937, "share_ge_15": 0.4242, "median_abs_gap": 12.61, "n": 12511}, "gen2": {"share_ge_25": 0.2117, "share_ge_15": 0.427, "median_abs_gap": 12.59, "n": 12512}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.28, "share_ge_25_all": 0.0144, "share_ge_25_pregame_clean": 0.0141}, "WTA": {"median_abs_gap_pregame_clean": 7.78, "share_ge_25_all": 0.0617, "share_ge_25_pregame_clean": 0.0541}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2418, "share_within_10pp_all": 0.4442, "share_within_10pp_pregame_clean": 0.5053, "corr_model_vs_mid_pregame_clean": 0.8508}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 392, "model_brier": 0.1924, "kalshi_brier": 0.1938, "brier_diff_model_minus_kalshi": -0.0014}, "10-15": {"n_settled": 460, "model_brier": 0.2108, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0074}, "15-25": {"n_settled": 551, "model_brier": 0.2276, "kalshi_brier": 0.2148, "brier_diff_model_minus_kalshi": 0.0127}, "25-40": {"n_settled": 292, "model_brier": 0.2213, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.017}, "3-5": {"n_settled": 262, "model_brier": 0.1895, "kalshi_brier": 0.1907, "brier_diff_model_minus_kalshi": -0.0011}, "40+": {"n_settled": 68, "model_brier": 0.2909, "kalshi_brier": 0.1768, "brier_diff_model_minus_kalshi": 0.1141}, "5-10": {"n_settled": 533, "model_brier": 0.198, "kalshi_brier": 0.2007, "brier_diff_model_minus_kalshi": -0.0026}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.544, "slope": 0.873, "slope_se": 0.05}, "kalshi_slope": {"intercept": 0.233, "slope": 1.134, "slope_se": 0.057}, "n": 2558}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.508, "slope": 0.877, "slope_se": 0.037}, "kalshi_slope": {"intercept": 0.159, "slope": 1.085, "slope_se": 0.041}, "n": 4526}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 264, "model_brier": 0.3363, "kalshi_brier": 0.2321, "brier_diff_model_minus_kalshi": 0.1041, "brier_diff_se": 0.02, "corr_model_outcome": -0.0325, "corr_kalshi_outcome": 0.2671}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
