# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-18T05:46Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 38,080): 0-3 14.5%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 18.9%, 25-40 13.7%, 40+ 8.2%; median gap 11.9 pp.
* **Where the extremes live**: 97.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.2%, Challenger 12.0%, doubles 7.2%). Main tour: ATP 2.9% and WTA 5.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,352): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.5%, BOOK_QUALITY 18.9%, STALE_QUOTE 18.1%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 5.2%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.2%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.5%. By class: coverage 35.5%, execution 18.9%, market_freshness 18.1%, data 12.3%, market_freshness/coverage 8.4%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%.
* **Stale / settled / in-play**: 52.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,352 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.2% of the time and with the model 0.7%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 546.0 points vs 1841.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.047, Gen-2 0.843, Gen-1 ledger 0.876 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 379 model 0.226 vs Kalshi 0.2072; n 78 model 0.3044 vs Kalshi 0.1729.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 156,930 model-market comparisons (257,352 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 56,622 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-18T05:36:49.249560+00:00'], shadow board 42,046 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-18T05:36:52.463753+00:00'], Model 4 17,874 rows, 15,662 settled tickers, 5,376 tickers with an external scan.
* By model: {"gen1_ledger": 38043, "gen1_elo": 21145, "fair_v1": 21145, "gen2": 21145, "gen1_sr": 21145, "model4_fundamental": 17158, "model4_conditioned": 17149}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 38,080 | 14.5 | 9.5 | 19.9 | 15.4 | 18.9 | 13.7 | 8.2 | 11.9 | 40.8% | 21.9% |
| MW fair_v1 | 21,145 | 13.5 | 8.5 | 18.4 | 15.8 | 19.2 | 14.6 | 9.9 | 12.99 | 43.7% | 24.4% |
| MW gen1_elo | 21,145 | 13.1 | 9.0 | 19.5 | 15.2 | 19.4 | 14.3 | 9.5 | 12.53 | 43.2% | 23.8% |
| MW gen1_ledger | 16,935 | 15.6 | 10.7 | 21.6 | 14.8 | 18.4 | 12.6 | 6.2 | 10.5 | 37.2% | 18.8% |
| MW gen1_sr | 21,145 | 9.7 | 7.4 | 16.5 | 14.2 | 21.6 | 18.6 | 12.0 | 15.79 | 52.1% | 30.6% |
| MW gen2 | 21,145 | 11.4 | 7.1 | 16.5 | 14.2 | 19.9 | 17.6 | 13.2 | 15.42 | 50.8% | 30.9% |
| all families model4_conditioned | 17,149 | 21.5 | 19.2 | 34.5 | 17.4 | 4.7 | 1.5 | 1.2 | 5.95 | 7.4% | 2.7% |
| all families model4_fundamental | 17,158 | 16.2 | 13.0 | 34.8 | 20.2 | 11.1 | 3.3 | 1.4 | 7.85 | 15.8% | 4.8% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.2%, >=15pp 40.8%, >=20pp 30.4%, >=25pp 21.9%, >=30pp 15.9%, >=40pp 8.2%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.24pp; >=10pp 44.7%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,692 | 29.4 | 13.6 | 24.6 | 17.3 | 11.6 | 2.7 | 0.7 | 6.15 | 15.1% | 3.4% |
| CHALLENGER | 3,468 | 16.0 | 10.1 | 20.0 | 15.9 | 14.3 | 12.4 | 11.3 | 11.32 | 38.0% | 23.7% |
| ITF_MEN | 5,875 | 11.0 | 8.0 | 17.5 | 15.0 | 19.9 | 16.2 | 12.5 | 14.45 | 48.5% | 28.7% |
| ITF_WOMEN | 8,266 | 10.2 | 6.7 | 15.9 | 15.4 | 22.4 | 18.2 | 11.2 | 15.69 | 51.8% | 29.4% |
| WTA | 1,187 | 19.5 | 12.0 | 24.7 | 18.4 | 19.6 | 5.0 | 0.9 | 8.22 | 25.4% | 5.9% |
| WTA125 | 657 | 13.4 | 7.5 | 23.6 | 20.2 | 19.8 | 13.6 | 2.0 | 11.2 | 35.3% | 15.5% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,692 | 23.5 | 14.4 | 24.6 | 18.3 | 14.4 | 3.8 | 1.1 | 6.9 | 19.3% | 4.9% |
| CHALLENGER | 3,468 | 14.7 | 8.1 | 19.2 | 13.7 | 18.0 | 14.3 | 12.0 | 12.7 | 44.3% | 26.3% |
| ITF_MEN | 5,875 | 9.4 | 6.7 | 15.7 | 13.6 | 19.8 | 19.4 | 15.4 | 16.93 | 54.6% | 34.8% |
| ITF_WOMEN | 8,266 | 8.5 | 5.6 | 13.6 | 13.4 | 21.1 | 20.9 | 16.9 | 18.87 | 58.8% | 37.7% |
| WTA | 1,187 | 17.3 | 7.8 | 20.2 | 15.8 | 22.8 | 15.1 | 1.0 | 11.71 | 38.9% | 16.1% |
| WTA125 | 657 | 6.8 | 4.7 | 17.1 | 17.5 | 25.9 | 19.2 | 8.8 | 16.84 | 53.9% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,692 | 26.1 | 13.7 | 26.1 | 16.7 | 13.4 | 3.4 | 0.8 | 6.54 | 17.5% | 4.1% |
| CHALLENGER | 3,468 | 15.0 | 10.2 | 20.6 | 15.1 | 15.5 | 12.1 | 11.5 | 11.05 | 39.1% | 23.6% |
| ITF_MEN | 5,875 | 10.0 | 8.1 | 17.9 | 14.2 | 20.7 | 16.7 | 12.4 | 14.97 | 49.8% | 29.1% |
| ITF_WOMEN | 8,266 | 9.7 | 6.9 | 16.3 | 15.6 | 22.9 | 18.3 | 10.3 | 15.59 | 51.6% | 28.6% |
| WTA | 1,187 | 23.2 | 16.8 | 31.2 | 15.3 | 10.9 | 2.0 | 0.6 | 6.05 | 13.5% | 2.6% |
| WTA125 | 657 | 22.8 | 12.2 | 29.2 | 15.8 | 13.8 | 5.8 | 0.3 | 7.73 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,067 | 28.0 | 20.2 | 32.2 | 11.6 | 5.7 | 2.1 | 0.1 | 5.11 | 7.9% | 2.2% |
| CHALLENGER | 2,415 | 22.2 | 15.1 | 27.2 | 14.1 | 13.8 | 5.6 | 2.0 | 7.0 | 21.4% | 7.6% |
| DOUBLES | 1,225 | 4.8 | 4.2 | 10.1 | 10.9 | 20.9 | 26.0 | 23.2 | 24.29 | 70.0% | 49.1% |
| ITF_MEN | 4,936 | 14.6 | 8.6 | 20.7 | 15.8 | 20.9 | 12.5 | 7.0 | 11.86 | 40.3% | 19.4% |
| ITF_WOMEN | 5,541 | 11.8 | 9.0 | 18.9 | 14.9 | 22.1 | 17.0 | 6.2 | 13.24 | 45.4% | 23.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 873 | 21.8 | 15.9 | 29.6 | 17.5 | 10.8 | 4.1 | 0.3 | 6.97 | 15.2% | 4.5% |
| WTA125 | 729 | 21.5 | 14.0 | 22.1 | 18.2 | 14.3 | 7.8 | 2.1 | 8.14 | 24.1% | 9.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,660 | 29.6 | 13.7 | 24.9 | 17.2 | 11.6 | 2.4 | 0.7 | 6.01 | 14.6% | 3.1% |
| CHALLENGER | 2,493 | 20.6 | 12.7 | 25.0 | 18.3 | 14.8 | 6.3 | 2.3 | 8.24 | 23.4% | 8.6% |
| ITF_MEN | 4,266 | 13.5 | 10.0 | 20.8 | 16.9 | 20.1 | 13.1 | 5.5 | 11.54 | 38.8% | 18.7% |
| ITF_WOMEN | 6,187 | 12.1 | 8.0 | 18.1 | 17.5 | 23.8 | 15.4 | 5.1 | 13.33 | 44.3% | 20.5% |
| WTA | 1,164 | 19.6 | 11.4 | 24.9 | 18.6 | 19.7 | 4.9 | 0.9 | 8.27 | 25.5% | 5.8% |
| WTA125 | 631 | 13.8 | 7.3 | 23.1 | 20.6 | 20.4 | 13.2 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,660 | 23.6 | 14.6 | 24.6 | 18.3 | 14.3 | 3.7 | 0.9 | 6.83 | 18.9% | 4.6% |
| CHALLENGER | 2,493 | 18.6 | 10.4 | 23.9 | 16.4 | 18.4 | 9.6 | 2.6 | 9.16 | 30.6% | 12.2% |
| ITF_MEN | 4,267 | 11.0 | 8.0 | 18.2 | 15.4 | 21.9 | 17.0 | 8.4 | 14.12 | 47.4% | 25.5% |
| ITF_WOMEN | 6,187 | 9.5 | 6.4 | 15.2 | 14.8 | 23.1 | 20.3 | 10.7 | 16.58 | 54.1% | 31.0% |
| WTA | 1,164 | 17.2 | 7.7 | 20.2 | 15.8 | 22.9 | 15.2 | 1.0 | 11.75 | 39.2% | 16.2% |
| WTA125 | 631 | 6.7 | 4.9 | 17.1 | 17.9 | 25.8 | 19.6 | 7.9 | 16.68 | 53.4% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,037 | 28.2 | 20.4 | 32.6 | 11.8 | 5.1 | 1.8 | 0.1 | 5.07 | 7.0% | 1.9% |
| CHALLENGER | 2,092 | 23.9 | 16.4 | 29.1 | 13.8 | 13.1 | 3.1 | 0.7 | 6.37 | 16.8% | 3.7% |
| DOUBLES | 1,134 | 4.8 | 4.3 | 10.3 | 11.0 | 20.7 | 26.2 | 22.6 | 24.11 | 69.5% | 48.8% |
| ITF_MEN | 4,086 | 16.0 | 9.4 | 22.5 | 16.7 | 20.7 | 10.6 | 4.1 | 10.61 | 35.4% | 14.7% |
| ITF_WOMEN | 4,585 | 12.8 | 9.7 | 20.4 | 15.7 | 22.3 | 15.6 | 3.5 | 11.94 | 41.4% | 19.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 835 | 22.2 | 16.4 | 29.8 | 17.5 | 10.9 | 3.2 | 0.0 | 6.82 | 14.1% | 3.2% |
| WTA125 | 619 | 23.6 | 15.5 | 23.6 | 19.7 | 12.6 | 4.7 | 0.3 | 7.2 | 17.6% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,225 | 4.8 | 4.2 | 10.1 | 10.9 | 20.9 | 26.0 | 23.2 | 24.29 | 70.0% | 49.1% |
| singles | 15,710 | 16.4 | 11.2 | 22.5 | 15.1 | 18.2 | 11.6 | 4.9 | 9.93 | 34.7% | 16.4% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 4,896 | 13.3 | 8.9 | 19.2 | 15.9 | 18.1 | 14.5 | 10.1 | 12.71 | 42.7% | 24.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 13,685 | 13.9 | 8.5 | 18.4 | 15.4 | 19.6 | 14.4 | 9.7 | 12.96 | 43.7% | 24.1% |
| UNKNOWN | 2,327 | 12.0 | 7.3 | 17.1 | 18.2 | 19.1 | 15.9 | 10.5 | 13.38 | 45.5% | 26.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,231 | 19.7 | 10.8 | 21.2 | 17.3 | 15.8 | 8.8 | 6.4 | 9.46 | 31.0% | 15.2% |
| B | 2,751 | 13.4 | 9.2 | 19.8 | 16.5 | 18.4 | 12.0 | 10.7 | 12.07 | 41.1% | 22.7% |
| C | 3,071 | 12.9 | 9.4 | 19.5 | 14.2 | 19.1 | 14.9 | 10.0 | 12.76 | 44.0% | 24.9% |
| D | 3,549 | 12.0 | 7.9 | 17.3 | 15.6 | 21.9 | 15.6 | 9.7 | 13.96 | 47.2% | 25.3% |
| F | 5,543 | 8.0 | 5.4 | 14.8 | 14.9 | 21.9 | 21.6 | 13.3 | 17.86 | 56.9% | 34.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,023 | 23.1 | 15.8 | 29.0 | 15.2 | 11.2 | 4.1 | 1.5 | 6.66 | 16.8% | 5.6% |
| B | 2,442 | 15.3 | 10.1 | 23.9 | 16.3 | 19.2 | 11.1 | 4.1 | 10.14 | 34.4% | 15.2% |
| C | 3,384 | 11.5 | 7.7 | 17.5 | 14.3 | 21.4 | 16.5 | 11.1 | 14.5 | 49.0% | 27.6% |
| D | 2,462 | 14.2 | 9.8 | 20.1 | 14.0 | 20.8 | 14.5 | 6.7 | 12.05 | 42.0% | 21.2% |
| F | 3,624 | 10.2 | 7.6 | 14.8 | 14.2 | 23.5 | 20.5 | 9.1 | 16.38 | 53.1% | 29.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,059 | 17.9 | 9.7 | 20.4 | 17.0 | 16.4 | 9.7 | 8.9 | 10.51 | 34.9% | 18.5% |
| LIMITED | 4,835 | 14.6 | 10.4 | 20.5 | 15.2 | 18.5 | 13.2 | 7.5 | 11.36 | 39.2% | 20.7% |
| POOR | 9,251 | 9.6 | 6.5 | 15.8 | 15.3 | 21.8 | 19.1 | 11.8 | 16.0 | 52.8% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,112 | 27.4 | 22.1 | 35.1 | 10.8 | 3.3 | 1.1 | 0.2 | 5.03 | 4.6% | 1.3% |
| GAME_SPREAD | 3,527 | 24.4 | 15.3 | 35.0 | 17.6 | 6.2 | 1.2 | 0.2 | 6.24 | 7.6% | 1.4% |
| MATCH_WINNER | 16,935 | 15.6 | 10.7 | 21.6 | 14.8 | 18.4 | 12.6 | 6.2 | 10.5 | 37.2% | 18.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 7,717 | 30.7 | 18.1 | 30.7 | 11.9 | 6.9 | 1.2 | 0.5 | 5.13 | 8.6% | 1.7% |
| TOTAL_GAMES | 5,728 | 6.8 | 8.8 | 37.2 | 28.7 | 11.5 | 3.8 | 3.1 | 9.68 | 18.4% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,011 | 24.9 | 35.6 | 31.6 | 3.3 | 3.8 | 0.7 | 0.2 | 4.44 | 4.7% | 0.9% |
| GAME_SPREAD | 4,146 | 46.0 | 16.6 | 27.7 | 7.3 | 1.5 | 0.7 | 0.3 | 3.46 | 2.5% | 1.0% |
| TOTAL_GAMES | 6,992 | 4.0 | 6.6 | 41.0 | 35.6 | 7.4 | 2.8 | 2.5 | 9.83 | 12.7% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,011 | 24.9 | 17.6 | 36.2 | 11.5 | 7.0 | 2.5 | 0.4 | 5.78 | 9.9% | 2.9% |
| GAME_SPREAD | 4,146 | 19.4 | 13.6 | 28.9 | 20.3 | 13.6 | 3.3 | 0.9 | 7.85 | 17.8% | 4.2% |
| TOTAL_GAMES | 7,001 | 6.8 | 8.7 | 37.0 | 27.6 | 13.0 | 4.1 | 2.7 | 9.7 | 19.8% | 6.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 21,145 | 43.7% | 24.4% | 12.99 | 35.0% | 15.2% | 10.71 |
| gen1_elo | 21,145 | 43.2% | 23.8% | 12.53 | 34.1% | 14.9% | 10.18 |
| gen1_sr | 21,145 | 52.1% | 30.6% | 15.79 | 44.4% | 21.3% | 13.18 |
| gen2 | 21,145 | 50.8% | 30.9% | 15.42 | 44.1% | 22.9% | 13.03 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 11,248 | 16.4 | 10.4 | 21.4 | 17.4 | 19.7 | 11.3 | 3.3 | 10.5 | 34.3% | 14.7% |
| STALE | 9,897 | 10.2 | 6.3 | 15.0 | 14.0 | 18.8 | 18.3 | 17.3 | 17.2 | 54.4% | 35.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 10,403 | 17.2 | 11.5 | 22.8 | 14.8 | 17.2 | 11.6 | 4.9 | 9.65 | 33.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 38,080 | 10403 | 14720 | 12957 | 23.8 | 144.3 | 1400.4 |
| ge_15pp | 15,544 | 3505 | 5150 | 6889 | 25.9 | 451.9 | 1380.4 |
| ge_25pp | 8,352 | 1719 | 2240 | 4393 | 33.0 | 586.4 | 1380.4 |
| lt_10pp | 16,679 | 5354 | 7059 | 4266 | 21.8 | 48.1 | 1341.5 |

Current slate `SL-20261018T054601Z-abf19855`: 1080 priced rows, quote age at build {'median': 9.8, 'max': 9.8}, freshness {'FRESH': 1080}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 1,914 | 21.6 | 10.6 | 22.9 | 18.8 | 18.8 | 6.8 | 0.5 | 8.65 | 26.1% | 7.3% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 339 | 69.6 | 30.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.1 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 692 | 0.0 | 3.0 | 35.4 | 29.1 | 23.1 | 8.7 | 0.7 | 11.84 | 32.5% | 9.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 21,145 | 2979 (14.1%) | 23.2% | 0.7% | {"EXTERNAL_STALE": 1914, "AGREES_WITH_KALSHI": 692, "ALL_AGREE": 339, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 9,240 | 733 (7.9%) | 30.7% | 1.2% | {"EXTERNAL_STALE": 499, "AGREES_WITH_KALSHI": 225, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,171 | 208 (4.0%) | 31.2% | 1.4% | {"EXTERNAL_STALE": 140, "AGREES_WITH_KALSHI": 65, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,490 | 196 (7.9%) | 32.1% | 1.5% | {"EXTERNAL_STALE": 130, "AGREES_WITH_KALSHI": 63, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 8,556 | 1685 (19.7%) | 15.8% | 0.7% | {"EXTERNAL_STALE": 1055, "ALL_AGREE": 339, "AGREES_WITH_KALSHI": 266, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,076 | 11.3 | 7.8 | 19.2 | 14.9 | 21.6 | 14.8 | 10.3 | 13.81 | 46.7% | 25.1% |
| 4-10x | 2,716 | 12.6 | 8.8 | 19.3 | 15.3 | 19.4 | 15.3 | 9.4 | 12.95 | 44.1% | 24.7% |
| <2x | 11,039 | 15.4 | 9.3 | 18.9 | 16.9 | 17.8 | 12.8 | 8.9 | 11.85 | 39.5% | 21.7% |
| >=10x | 3,314 | 10.8 | 6.3 | 15.2 | 13.9 | 21.2 | 19.6 | 12.9 | 16.43 | 53.7% | 32.5% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,570 | 13.2 | 8.4 | 19.3 | 16.0 | 19.6 | 13.1 | 10.4 | 12.82 | 43.1% | 23.5% |
| 300-1000 | 4,679 | 12.2 | 8.7 | 17.2 | 15.7 | 20.6 | 16.2 | 9.5 | 13.73 | 46.3% | 25.6% |
| <300 | 6,299 | 9.1 | 5.9 | 15.4 | 14.8 | 21.7 | 20.2 | 12.9 | 16.9 | 54.9% | 33.2% |
| >=3000 | 4,597 | 21.5 | 11.9 | 22.8 | 17.3 | 14.0 | 7.1 | 5.4 | 8.27 | 26.5% | 12.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 644 | 0.5381 | 0.4045 | 0.4845 | +0.054 | -0.080 | 0.0014 ± 0.0059 |
| ratio 4-10x | 428 | 0.5842 | 0.4473 | 0.5047 | +0.080 | -0.057 | 0.0087 ± 0.0075 |
| ratio <2x | 1602 | 0.537 | 0.4154 | 0.4501 | +0.087 | -0.035 | 0.0128 ± 0.0036 |
| ratio >=10x | 520 | 0.5468 | 0.3784 | 0.4192 | +0.128 | -0.041 | 0.0173 ± 0.0078 |
| thinner_sample 1000-3000 | 909 | 0.5431 | 0.4174 | 0.462 | +0.081 | -0.045 | 0.0079 ± 0.0048 |
| thinner_sample 300-1000 | 754 | 0.5614 | 0.4224 | 0.4854 | +0.076 | -0.063 | 0.0029 ± 0.0057 |
| thinner_sample <300 | 976 | 0.5431 | 0.383 | 0.4314 | +0.112 | -0.048 | 0.0177 ± 0.0055 |
| thinner_sample >=3000 | 555 | 0.53 | 0.437 | 0.4685 | +0.062 | -0.031 | 0.0136 ± 0.0049 |
| data_status ADEQUATE | 947 | 0.5334 | 0.4292 | 0.4593 | +0.074 | -0.030 | 0.0104 ± 0.004 |
| data_status LIMITED | 797 | 0.5521 | 0.4229 | 0.4856 | +0.067 | -0.063 | 0.0046 ± 0.0052 |
| data_status POOR | 1450 | 0.549 | 0.3936 | 0.4448 | +0.104 | -0.051 | 0.0142 ± 0.0044 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 495 | 0.1924 | 0.1937 | -0.0013 ± 0.0007 | 0.5628 | 0.5655 | 0.494 | 0.4792 | 0.5293 | -0.042 ± 0.0207 | -0.01 (5) |
| 3-5 | 311 | 0.195 | 0.1946 | +0.0004 ± 0.002 | 0.5712 | 0.5688 | 0.5052 | 0.4653 | 0.4791 | -0.078 ± 0.0256 | 0.02 (1) |
| 5-10 | 672 | 0.1977 | 0.1972 | +0.0005 ± 0.0026 | 0.581 | 0.5777 | 0.5105 | 0.4362 | 0.4643 | -0.083 ± 0.0177 | -0.0167 (6) |
| 10-15 | 564 | 0.2153 | 0.2058 | +0.0095 ± 0.0048 | 0.6208 | 0.5938 | 0.5196 | 0.3956 | 0.4184 | -0.089 ± 0.0191 | -0.048 (5) |
| 15-25 | 695 | 0.2296 | 0.2129 | +0.0167 ± 0.0068 | 0.6537 | 0.611 | 0.5761 | 0.3812 | 0.4374 | -0.085 ± 0.0175 | -0.0033 (9) |
| 25-40 | 379 | 0.226 | 0.2072 | +0.0188 ± 0.014 | 0.6414 | 0.5966 | 0.6466 | 0.3379 | 0.4617 | -0.064 ± 0.0214 | -0.01 (1) |
| 40+ | 78 | 0.3044 | 0.1729 | +0.1315 ± 0.0422 | 0.8211 | 0.5186 | 0.7435 | 0.296 | 0.3718 | -0.122 ± 0.0414 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2319 | 0.18 | 0.1812 | -0.0012 ± 0.0003 | 0.5349 | 0.5361 | 0.4788 | 0.4638 | 0.4985 | -0.020 ± 0.009 | -0.0129 (17) |
| 3-5 | 1449 | 0.1929 | 0.191 | +0.0020 ± 0.0009 | 0.5662 | 0.5573 | 0.4792 | 0.4395 | 0.4334 | -0.062 ± 0.0117 | 0.0 (2) |
| 5-10 | 3123 | 0.1937 | 0.1913 | +0.0025 ± 0.0012 | 0.5701 | 0.5616 | 0.4822 | 0.4084 | 0.4272 | -0.044 ± 0.0079 | -0.0119 (21) |
| 10-15 | 2716 | 0.2028 | 0.1831 | +0.0197 ± 0.0021 | 0.5939 | 0.5386 | 0.4801 | 0.3554 | 0.3391 | -0.078 ± 0.0082 | -0.0281 (16) |
| 15-25 | 3310 | 0.2086 | 0.1696 | +0.0390 ± 0.0028 | 0.6091 | 0.5021 | 0.5022 | 0.306 | 0.3063 | -0.071 ± 0.0071 | -0.0025 (44) |
| 25-40 | 2603 | 0.2228 | 0.1255 | +0.0973 ± 0.0043 | 0.6395 | 0.3875 | 0.5288 | 0.2156 | 0.2209 | -0.064 ± 0.0067 | -0.01 (1) |
| 40+ | 1771 | 0.3784 | 0.042 | +0.3364 ± 0.0055 | 0.9849 | 0.168 | 0.6267 | 0.1054 | 0.0536 | -0.087 ± 0.0045 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 366 | 0.1976 | 0.198 | -0.0004 ± 0.0008 | 0.5765 | 0.5774 | 0.5015 | 0.4863 | 0.5055 | -0.081 ± 0.0245 | -0.01 (3) |
| 3-5 | 256 | 0.2117 | 0.2109 | +0.0007 ± 0.0023 | 0.6059 | 0.6053 | 0.5153 | 0.4753 | 0.4805 | -0.079 ± 0.0303 | 0.02 (1) |
| 5-10 | 584 | 0.199 | 0.1985 | +0.0005 ± 0.0028 | 0.5816 | 0.5804 | 0.5476 | 0.4728 | 0.5068 | -0.070 ± 0.019 | -0.01 (4) |
| 10-15 | 527 | 0.219 | 0.2108 | +0.0082 ± 0.005 | 0.6285 | 0.6077 | 0.5677 | 0.4433 | 0.4763 | -0.091 ± 0.021 | -0.04 (5) |
| 15-25 | 763 | 0.2291 | 0.2074 | +0.0217 ± 0.0065 | 0.6499 | 0.597 | 0.5877 | 0.3912 | 0.4377 | -0.090 ± 0.0168 | -0.0133 (9) |
| 25-40 | 507 | 0.2686 | 0.1958 | +0.0727 ± 0.0124 | 0.7485 | 0.5721 | 0.6594 | 0.3444 | 0.3886 | -0.118 ± 0.0196 | -0.0075 (4) |
| 40+ | 191 | 0.3649 | 0.1779 | +0.1870 ± 0.0301 | 1.0145 | 0.527 | 0.741 | 0.2585 | 0.3194 | -0.071 ± 0.0295 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1951 | 0.183 | 0.1834 | -0.0004 ± 0.0003 | 0.5414 | 0.5422 | 0.5018 | 0.4871 | 0.5085 | -0.034 ± 0.01 | -0.0133 (15) |
| 3-5 | 1233 | 0.1942 | 0.1932 | +0.0010 ± 0.001 | 0.5637 | 0.5612 | 0.5147 | 0.4748 | 0.4818 | -0.043 ± 0.0128 | 0.02 (1) |
| 5-10 | 2797 | 0.1917 | 0.1892 | +0.0025 ± 0.0012 | 0.5661 | 0.557 | 0.5094 | 0.4354 | 0.4569 | -0.039 ± 0.0083 | -0.0117 (6) |
| 10-15 | 2402 | 0.1997 | 0.1882 | +0.0115 ± 0.0022 | 0.5883 | 0.5489 | 0.5202 | 0.3957 | 0.4147 | -0.049 ± 0.009 | -0.0189 (18) |
| 15-25 | 3443 | 0.2169 | 0.1756 | +0.0413 ± 0.0028 | 0.629 | 0.5185 | 0.5313 | 0.3351 | 0.3311 | -0.077 ± 0.0072 | -0.0086 (42) |
| 25-40 | 3062 | 0.2512 | 0.1352 | +0.1160 ± 0.0042 | 0.7093 | 0.4155 | 0.5595 | 0.2436 | 0.2198 | -0.090 ± 0.0066 | -0.0044 (18) |
| 40+ | 2403 | 0.4018 | 0.0659 | +0.3359 ± 0.006 | 1.0601 | 0.2307 | 0.6627 | 0.1254 | 0.0945 | -0.069 ± 0.0051 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 475 | 0.1953 | 0.1974 | -0.0021 ± 0.0007 | 0.5709 | 0.576 | 0.498 | 0.4827 | 0.5453 | -0.017 ± 0.0208 | -0.0137 (8) |
| 3-5 | 353 | 0.1893 | 0.1877 | +0.0016 ± 0.0019 | 0.5553 | 0.5514 | 0.4974 | 0.4578 | 0.4589 | -0.108 ± 0.0242 | 0.0067 (3) |
| 5-10 | 703 | 0.2016 | 0.1976 | +0.0040 ± 0.0025 | 0.5905 | 0.5774 | 0.503 | 0.4292 | 0.4353 | -0.095 ± 0.0172 | -0.0071 (7) |
| 10-15 | 551 | 0.2069 | 0.2055 | +0.0014 ± 0.0048 | 0.6012 | 0.5939 | 0.5375 | 0.4146 | 0.4737 | -0.065 ± 0.0191 | -0.0317 (6) |
| 15-25 | 645 | 0.235 | 0.2092 | +0.0257 ± 0.007 | 0.6697 | 0.6024 | 0.5845 | 0.3912 | 0.4202 | -0.110 ± 0.0179 | -0.03 (1) |
| 25-40 | 392 | 0.2125 | 0.2128 | -0.0003 ± 0.0136 | 0.6121 | 0.6092 | 0.6516 | 0.3422 | 0.4949 | -0.043 ± 0.0209 | 0.015 (2) |
| 40+ | 75 | 0.3237 | 0.1866 | +0.1371 ± 0.045 | 0.8679 | 0.5501 | 0.7473 | 0.2945 | 0.3733 | -0.107 ± 0.0471 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2209 | 0.187 | 0.1878 | -0.0008 ± 0.0003 | 0.5511 | 0.5524 | 0.4853 | 0.4701 | 0.4925 | -0.029 ± 0.0093 | -0.0163 (35) |
| 3-5 | 1532 | 0.1874 | 0.1841 | +0.0033 ± 0.0009 | 0.5525 | 0.5445 | 0.4775 | 0.438 | 0.4171 | -0.082 ± 0.0113 | -0.0094 (18) |
| 5-10 | 3324 | 0.1947 | 0.1885 | +0.0062 ± 0.0011 | 0.5746 | 0.5536 | 0.4808 | 0.4069 | 0.3995 | -0.066 ± 0.0076 | -0.01 (31) |
| 10-15 | 2561 | 0.1957 | 0.1804 | +0.0153 ± 0.0021 | 0.5759 | 0.53 | 0.4964 | 0.373 | 0.3733 | -0.065 ± 0.0083 | -0.015 (12) |
| 15-25 | 3424 | 0.2073 | 0.1679 | +0.0394 ± 0.0027 | 0.6084 | 0.4986 | 0.5042 | 0.3091 | 0.3064 | -0.071 ± 0.007 | -0.03 (2) |
| 25-40 | 2546 | 0.2177 | 0.1235 | +0.0942 ± 0.0044 | 0.6279 | 0.3811 | 0.5256 | 0.2095 | 0.2227 | -0.059 ± 0.0066 | 0.01 (3) |
| 40+ | 1695 | 0.3942 | 0.0461 | +0.3481 ± 0.0059 | 1.0279 | 0.179 | 0.6382 | 0.1099 | 0.056 | -0.089 ± 0.0049 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 825 | 0.195 | 0.1952 | -0.0001 ± 0.0005 | 0.5705 | 0.5705 | 0.5079 | 0.4929 | 0.497 | -0.051 ± 0.0154 | -0.0224 (49) |
| 3-5 | 577 | 0.1948 | 0.1939 | +0.0010 ± 0.0015 | 0.5679 | 0.5645 | 0.4795 | 0.4397 | 0.4454 | -0.052 ± 0.0185 | -0.0194 (34) |
| 5-10 | 1215 | 0.1977 | 0.1918 | +0.0059 ± 0.0019 | 0.5826 | 0.5655 | 0.4879 | 0.4144 | 0.4123 | -0.064 ± 0.0128 | -0.005 (78) |
| 10-15 | 772 | 0.2075 | 0.1962 | +0.0113 ± 0.004 | 0.6034 | 0.5741 | 0.5071 | 0.3841 | 0.399 | -0.056 ± 0.0161 | 0.0014 (64) |
| 15-25 | 1022 | 0.2336 | 0.2119 | +0.0217 ± 0.0057 | 0.6656 | 0.6098 | 0.5659 | 0.371 | 0.4139 | -0.056 ± 0.0144 | -0.0214 (59) |
| 25-40 | 593 | 0.2486 | 0.1956 | +0.0530 ± 0.0112 | 0.702 | 0.569 | 0.6487 | 0.3366 | 0.4064 | -0.081 ± 0.0168 | -0.0219 (26) |
| 40+ | 198 | 0.3755 | 0.1901 | +0.1854 ± 0.0316 | 1.081 | 0.5609 | 0.7922 | 0.3012 | 0.3788 | -0.081 ± 0.0284 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2497 | 0.1872 | 0.1872 | -0.0000 ± 0.0003 | 0.5503 | 0.5494 | 0.5042 | 0.4889 | 0.4986 | -0.035 ± 0.0086 | -0.0157 (88) |
| 3-5 | 1705 | 0.1901 | 0.1875 | +0.0025 ± 0.0008 | 0.5557 | 0.5499 | 0.4854 | 0.4457 | 0.4346 | -0.057 ± 0.0106 | -0.0209 (69) |
| 5-10 | 3435 | 0.1945 | 0.1864 | +0.0081 ± 0.0011 | 0.5744 | 0.5512 | 0.4828 | 0.4092 | 0.3942 | -0.066 ± 0.0075 | -0.0082 (132) |
| 10-15 | 2318 | 0.2041 | 0.1897 | +0.0143 ± 0.0023 | 0.596 | 0.5577 | 0.5105 | 0.3876 | 0.3909 | -0.055 ± 0.009 | -0.0053 (105) |
| 15-25 | 2884 | 0.229 | 0.1976 | +0.0314 ± 0.0033 | 0.6606 | 0.5747 | 0.5576 | 0.3622 | 0.3811 | -0.059 ± 0.0083 | -0.0253 (107) |
| 25-40 | 1953 | 0.2545 | 0.1689 | +0.0856 ± 0.0059 | 0.7204 | 0.5002 | 0.6084 | 0.2943 | 0.318 | -0.078 ± 0.009 | -0.0229 (51) |
| 40+ | 932 | 0.3875 | 0.13 | +0.2576 ± 0.0126 | 1.0967 | 0.398 | 0.7093 | 0.2029 | 0.2146 | -0.072 ± 0.0112 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3194 | 1.047 ± 0.05 | 1.166 | 0.1681 | 0.1708 | 0.2126 | 0.2019 |
| gen2 | 3194 | 0.843 ± 0.045 | 1.123 | 0.1751 | 0.1708 | 0.2313 | 0.2019 |
| gen1_elo | 3194 | 1.039 ± 0.049 | 1.152 | 0.1735 | 0.1712 | 0.2112 | 0.2018 |
| gen1_sr | 3194 | 1.039 ± 0.058 | 1.182 | 0.1348 | 0.1725 | 0.2273 | 0.2017 |
| gen1_ledger | 5202 | 0.876 ± 0.034 | 1.079 | 0.1773 | 0.185 | 0.218 | 0.1975 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 15,544)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,746 | 24.1% |
| STALE_QUOTE | market_freshness | 3,206 | 20.6% |
| BOOK_QUALITY | execution | 2,985 | 19.2% |
| POOR_DATA | data | 1,698 | 10.9% |
| LIMITED_DATA | data | 1,077 | 6.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 812 | 5.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 766 | 4.9% |
| IDENTITY_AMBIGUOUS | mapping | 626 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 434 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 194 | 1.2% |

Cause class: coverage 24.1%, market_freshness 20.6%, execution 19.2%, data 17.8%, market_freshness/coverage 8.0%, model_calibration_or_unknown 4.9%, mapping 4.0%, model_calibration 1.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 95.0%, LOW_DATA_QUALITY 69.5%, THIN_PLAYER_HISTORY 57.8%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 44.3%, MODEL_INTERNAL_DISAGREEMENT 40.0%, ASYMMETRIC_SAMPLE_SIZE 32.1%, WIDE_SPREAD 25.2%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.7%, LEVEL_TRANSFER_RISK 8.7%, EVENT_MAPPING_RISK 8.3%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 2.1%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.5%, POST_SETTLEMENT_OBSERVATION 24.1%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,352)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,963 | 35.5% |
| BOOK_QUALITY | execution | 1,581 | 18.9% |
| STALE_QUOTE | market_freshness | 1,511 | 18.1% |
| POOR_DATA | data | 706 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 436 | 5.2% |
| IDENTITY_AMBIGUOUS | mapping | 362 | 4.3% |
| LIMITED_DATA | data | 321 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 268 | 3.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 163 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 41 | 0.5% |

Cause class: coverage 35.5%, execution 18.9%, market_freshness 18.1%, data 12.3%, market_freshness/coverage 8.4%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.8%, START_UNVERIFIABLE 97.7%, LOW_DATA_QUALITY 73.4%, THIN_PLAYER_HISTORY 60.2%, STALE_KALSHI_QUOTE 52.6%, STALE_PLAYER_DATA 47.6%, MODEL_INTERNAL_DISAGREEMENT 41.0%, ASYMMETRIC_SAMPLE_SIZE 34.0%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 18.0%, EVENT_MAPPING_RISK 10.1%, LOW_DISPLAYED_LIQUIDITY 7.8%, LEVEL_TRANSFER_RISK 7.8%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.1%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.2%, POST_SETTLEMENT_OBSERVATION 35.5%, POSSIBLE_IN_PLAY_QUOTE 5.6%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6640, "IDENTITY_AMBIGUOUS": 1712}; ticker orientation: {"VERIFIED": 8352}.

Checks: discipline:AMBIGUOUS 602, discipline:PASS 7750, identity_confidence:AMBIGUOUS 1501, identity_confidence:PASS 6851, level_mapping:NA 614, level_mapping:PASS 7738, market_pair:AMBIGUOUS 296, market_pair:NA 207, market_pair:PASS 7849, model_complement:NA 174, model_complement:PASS 8178, namesake:PASS 8352, physical_match_id:NA 3181, physical_match_id:PASS 5171, player_ids:PASS 8352, same_pair_other_event:PASS 8352, ticker_orientation:PASS 8352

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,759 | 2.9% | 2.6% | 1.0% | {"market_freshness": 33, "data": 19, "execution": 13, "market_freshness/coverage": 8, "model_calibration_or_unknown": 4, "model_calibration": 2, "coverage": 2} | 5.61 | 0.2088 / 0.2068 (295) | 16.9% | 2.6% | 4.5% | 2.2% |
| CHALLENGER | 5,883 | 17.1% | 6.4% | 12.0% | {"coverage": 588, "market_freshness": 128, "market_freshness/coverage": 125, "data": 75, "model_calibration_or_unknown": 50, "execution": 24, "model_calibration": 9, "mapping": 7} | 7.18 | 0.217 / 0.2049 (1485) | 36.4% | 11.5% | 2.5% | 22.1% |
| DOUBLES | 1,225 | 49.1% | 48.8% | 7.2% | {"execution": 279, "mapping": 168, "market_freshness": 106, "market_freshness/coverage": 42, "coverage": 7} | 24.11 | 0.323 / 0.2339 (334) | 19.1% | 0.0% | 100.0% | 7.4% |
| ITF_MEN | 10,811 | 24.5% | 16.7% | 31.7% | {"coverage": 1040, "execution": 535, "market_freshness": 407, "data": 358, "market_freshness/coverage": 209, "mapping": 94, "model_calibration_or_unknown": 2} | 11.13 | 0.2135 / 0.194 (2624) | 36.3% | 61.7% | 13.0% | 22.8% |
| ITF_WOMEN | 13,807 | 27.0% | 19.9% | 44.6% | {"coverage": 1309, "market_freshness": 761, "execution": 701, "data": 541, "market_freshness/coverage": 271, "mapping": 87, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.8 | 0.2035 / 0.1913 (2785) | 38.8% | 57.3% | 10.1% | 22.0% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,060 | 5.3% | 4.8% | 1.3% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 15, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.64 | 0.2391 / 0.2332 (349) | 23.1% | 1.7% | 1.8% | 3.0% |
| WTA125 | 1,386 | 12.6% | 9.9% | 2.1% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.2185 / 0.2069 (482) | 22.9% | 7.4% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 9 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 10 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 11 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 12 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 13 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 14 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 15 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 16 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 17 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 18 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 19 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 23 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 24 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 25 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 27 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 29 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 30 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 31 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 33 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 34 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 35 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 36 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 37 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 38 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 39 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 547 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 42 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 44 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 45 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 624 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 46 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 47 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 48 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 49 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 50 | `KXATPCHALLENGERMATCH-26OCT13GIUSEA-SEA` | CHALLENGER | fair_v1 | 76% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 243 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9773, "by_level_share_of_ge_25pp": {"ATP": 0.0097, "CHALLENGER": 0.1205, "DOUBLES": 0.0721, "ITF_MEN": 0.3167, "ITF_WOMEN": 0.4458, "OTHER": 0.0014, "WTA": 0.0131, "WTA125": 0.0208}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.526, "share_primary_cause_market_settled_or_in_play": 0.4391, "share_primary_cause_stale_quote_only": 0.1809}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8352, "identity_ambiguous_share": 0.205, "ticker_orientation": {"VERIFIED": 8352}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5171, "with_external": 208, "coverage": 0.0402, "external_status": {"EXTERNAL_STALE": 140, "AGREES_WITH_KALSHI": 65, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 140, "MODEL_LONE_OUTLIER": 65, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3125, "share_external_supports_model": 0.0144}, "pregame_clean_ge_25pp": {"n": 2490, "with_external": 196, "coverage": 0.0787, "external_status": {"EXTERNAL_STALE": 130, "AGREES_WITH_KALSHI": 63, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 130, "MODEL_LONE_OUTLIER": 63, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3214, "share_external_supports_model": 0.0153}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 546.0, "median_sample_ratio": 2.42, "median_min_matches": 21.0, "median_max_days_since_last": 211.0, "share_severe_asymmetry": 0.2063, "data_status": {"POOR": 4472, "LIMITED": 2386, "ADEQUATE": 1494}, "comparison_lt_10pp": {"median_thinner_serve_points": 1841.0, "median_sample_ratio": 1.67, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 644, "model_minus_observed": 0.0537, "kalshi_minus_observed": -0.08, "brier_diff_model_minus_kalshi": 0.0014}, "4-10x": {"n": 428, "model_minus_observed": 0.0796, "kalshi_minus_observed": -0.0574, "brier_diff_model_minus_kalshi": 0.0087}, "<2x": {"n": 1602, "model_minus_observed": 0.0869, "kalshi_minus_observed": -0.0346, "brier_diff_model_minus_kalshi": 0.0128}, ">=10x": {"n": 520, "model_minus_observed": 0.1276, "kalshi_minus_observed": -0.0408, "brier_diff_model_minus_kalshi": 0.0173}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3194, "model": {"intercept": -0.551, "slope": 0.843, "slope_se": 0.045}, "kalshi_mid_same_rows": {"intercept": 0.214, "slope": 1.123, "slope_se": 0.051}, "mean_extremity_model": 0.1751, "mean_extremity_kalshi": 0.1708, "model_brier": 0.2313, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0294, "brier_diff_se": 0.0033, "model_logloss": 0.6594, "kalshi_logloss": 0.586}, "fair_v1": {"n": 3194, "model": {"intercept": -0.415, "slope": 1.047, "slope_se": 0.05}, "kalshi_mid_same_rows": {"intercept": 0.293, "slope": 1.166, "slope_se": 0.052}, "mean_extremity_model": 0.1681, "mean_extremity_kalshi": 0.1708, "model_brier": 0.2126, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0107, "brier_diff_se": 0.0027, "model_logloss": 0.6131, "kalshi_logloss": 0.5858}, "gen1_elo": {"n": 3194, "model": {"intercept": -0.408, "slope": 1.039, "slope_se": 0.049}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.152, "slope_se": 0.051}, "mean_extremity_model": 0.1735, "mean_extremity_kalshi": 0.1712, "model_brier": 0.2112, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0094, "brier_diff_se": 0.0027, "model_logloss": 0.6107, "kalshi_logloss": 0.5855}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2445, "share_ge_15": 0.437, "median_abs_gap": 12.99, "n": 21145}, "gen1_elo": {"share_ge_25": 0.2381, "share_ge_15": 0.4318, "median_abs_gap": 12.53, "n": 21145}, "gen1_sr": {"share_ge_25": 0.3057, "share_ge_15": 0.5214, "median_abs_gap": 15.79, "n": 21145}, "gen2": {"share_ge_25": 0.3089, "share_ge_15": 0.5084, "median_abs_gap": 15.42, "n": 21145}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1518, "share_ge_15": 0.35, "median_abs_gap": 10.71, "n": 16401}, "gen1_elo": {"share_ge_25": 0.1491, "share_ge_15": 0.3411, "median_abs_gap": 10.18, "n": 16400}, "gen1_sr": {"share_ge_25": 0.213, "share_ge_15": 0.444, "median_abs_gap": 13.18, "n": 16401}, "gen2": {"share_ge_25": 0.2286, "share_ge_15": 0.4415, "median_abs_gap": 13.03, "n": 16402}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.61, "share_ge_25_all": 0.0294, "share_ge_25_pregame_clean": 0.0263}, "WTA": {"median_abs_gap_pregame_clean": 7.64, "share_ge_25_all": 0.0529, "share_ge_25_pregame_clean": 0.0475}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2394, "share_within_10pp_all": 0.438, "share_within_10pp_pregame_clean": 0.4933, "corr_model_vs_mid_pregame_clean": 0.8414}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 495, "model_brier": 0.1924, "kalshi_brier": 0.1937, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 564, "model_brier": 0.2153, "kalshi_brier": 0.2058, "brier_diff_model_minus_kalshi": 0.0095}, "15-25": {"n_settled": 695, "model_brier": 0.2296, "kalshi_brier": 0.2129, "brier_diff_model_minus_kalshi": 0.0167}, "25-40": {"n_settled": 379, "model_brier": 0.226, "kalshi_brier": 0.2072, "brier_diff_model_minus_kalshi": 0.0188}, "3-5": {"n_settled": 311, "model_brier": 0.195, "kalshi_brier": 0.1946, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 78, "model_brier": 0.3044, "kalshi_brier": 0.1729, "brier_diff_model_minus_kalshi": 0.1315}, "5-10": {"n_settled": 672, "model_brier": 0.1977, "kalshi_brier": 0.1972, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.551, "slope": 0.843, "slope_se": 0.045}, "kalshi_slope": {"intercept": 0.214, "slope": 1.123, "slope_se": 0.051}, "n": 3194}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.518, "slope": 0.876, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.139, "slope": 1.079, "slope_se": 0.038}, "n": 5202}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 334, "model_brier": 0.323, "kalshi_brier": 0.2339, "brier_diff_model_minus_kalshi": 0.0891, "brier_diff_se": 0.0171, "corr_model_outcome": 0.015, "corr_kalshi_outcome": 0.2585}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
