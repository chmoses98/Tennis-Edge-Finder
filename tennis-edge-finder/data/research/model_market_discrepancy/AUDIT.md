# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-09T13:52Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 26,666): 0-3 14.3%, 3-5 9.6%, 5-10 19.9%, 10-15 15.5%, 15-25 18.5%, 25-40 13.8%, 40+ 8.4%; median gap 11.91 pp.
* **Where the extremes live**: 98.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 12.0%, doubles 7.1%). Main tour: ATP 1.6% and WTA 7.8% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 5,929): MARKET_ALREADY_SETTLED_WHEN_PRICED 39.4%, STALE_QUOTE 16.8%, BOOK_QUALITY 16.7%, POOR_DATA 7.9%, POSSIBLY_IN_PLAY_QUOTE 5.5%, LIMITED_DATA 4.4%, IDENTITY_AMBIGUOUS 3.7%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.2%. By class: coverage 39.4%, market_freshness 16.8%, execution 16.7%, data 12.3%, market_freshness/coverage 8.9%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.2%.
* **Stale / settled / in-play**: 55.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 48.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 5,929 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 17.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 2.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 17.3% of the time and with the model 0.3%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 627.5 points vs 1824.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.072, Gen-2 0.864, Gen-1 ledger 0.908 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 250 model 0.2202 vs Kalshi 0.2008; n 55 model 0.2888 vs Kalshi 0.1716.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 103,065 model-market comparisons (171,101 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 38,952 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-09T13:47:29.348831+00:00'], shadow board 27,882 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-09T13:47:32.208312+00:00'], Model 4 11,049 rows, 11,575 settled tickers, 3,110 tickers with an external scan.
* By model: {"gen1_ledger": 25226, "gen1_elo": 14009, "fair_v1": 14009, "gen2": 14009, "gen1_sr": 14009, "model4_fundamental": 10906, "model4_conditioned": 10897}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 26,666 | 14.3 | 9.6 | 19.9 | 15.5 | 18.5 | 13.8 | 8.4 | 11.91 | 40.8% | 22.2% |
| MW fair_v1 | 14,009 | 13.6 | 8.7 | 18.3 | 16.3 | 18.4 | 14.7 | 10.1 | 12.85 | 43.1% | 24.8% |
| MW gen1_elo | 14,009 | 13.1 | 8.9 | 20.1 | 14.8 | 19.0 | 14.5 | 9.5 | 12.42 | 43.0% | 24.0% |
| MW gen1_ledger | 12,657 | 15.0 | 10.6 | 21.7 | 14.6 | 18.7 | 12.9 | 6.6 | 10.77 | 38.1% | 19.4% |
| MW gen1_sr | 14,009 | 10.2 | 7.9 | 16.2 | 14.2 | 21.4 | 18.3 | 11.7 | 15.51 | 51.5% | 30.1% |
| MW gen2 | 14,009 | 12.2 | 7.2 | 16.1 | 14.3 | 19.8 | 17.2 | 13.2 | 15.12 | 50.2% | 30.4% |
| all families model4_conditioned | 10,897 | 22.3 | 20.4 | 36.0 | 15.6 | 4.0 | 0.8 | 0.9 | 5.68 | 5.7% | 1.7% |
| all families model4_fundamental | 10,906 | 16.8 | 13.3 | 35.7 | 19.9 | 10.5 | 2.6 | 1.2 | 7.59 | 14.3% | 3.8% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.2%, >=15pp 40.8%, >=20pp 30.5%, >=25pp 22.2%, >=30pp 16.3%, >=40pp 8.4%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.6%, >=25pp 18.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,098 | 29.4 | 14.6 | 24.6 | 17.5 | 11.7 | 1.3 | 1.0 | 5.93 | 13.9% | 2.3% |
| CHALLENGER | 2,335 | 15.7 | 10.9 | 18.6 | 16.3 | 12.8 | 12.9 | 12.8 | 11.81 | 38.5% | 25.7% |
| ITF_MEN | 4,035 | 11.5 | 8.7 | 18.4 | 15.0 | 19.1 | 15.0 | 12.2 | 13.63 | 46.3% | 27.2% |
| ITF_WOMEN | 5,629 | 10.3 | 6.6 | 15.8 | 16.4 | 21.8 | 18.6 | 10.4 | 15.39 | 50.9% | 29.1% |
| WTA | 569 | 23.9 | 9.7 | 25.7 | 16.0 | 16.7 | 6.2 | 1.9 | 7.85 | 24.8% | 8.1% |
| WTA125 | 343 | 11.4 | 6.1 | 21.9 | 25.9 | 16.3 | 16.0 | 2.3 | 11.51 | 34.7% | 18.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,098 | 23.9 | 13.8 | 24.7 | 18.4 | 15.9 | 2.1 | 1.2 | 6.9 | 19.2% | 3.3% |
| CHALLENGER | 2,335 | 15.3 | 7.5 | 18.2 | 13.4 | 18.1 | 14.2 | 13.3 | 13.11 | 45.6% | 27.5% |
| ITF_MEN | 4,035 | 10.6 | 7.5 | 16.9 | 14.9 | 19.9 | 17.3 | 12.9 | 15.19 | 50.1% | 30.2% |
| ITF_WOMEN | 5,629 | 9.2 | 6.0 | 12.7 | 13.0 | 20.8 | 21.3 | 17.0 | 19.03 | 59.1% | 38.3% |
| WTA | 569 | 22.3 | 5.3 | 19.0 | 15.1 | 20.7 | 15.6 | 1.9 | 11.73 | 38.3% | 17.6% |
| WTA125 | 343 | 4.4 | 2.6 | 17.5 | 20.4 | 22.7 | 21.3 | 11.1 | 17.24 | 55.1% | 32.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,098 | 26.5 | 13.8 | 29.1 | 15.3 | 11.3 | 2.9 | 1.1 | 6.47 | 15.3% | 4.0% |
| CHALLENGER | 2,335 | 15.8 | 10.6 | 20.3 | 14.5 | 13.9 | 12.1 | 12.7 | 10.76 | 38.7% | 24.8% |
| ITF_MEN | 4,035 | 10.5 | 8.8 | 19.1 | 13.8 | 20.1 | 15.4 | 12.2 | 13.95 | 47.8% | 27.7% |
| ITF_WOMEN | 5,629 | 9.8 | 6.7 | 16.8 | 15.6 | 23.2 | 18.8 | 9.3 | 15.52 | 51.2% | 28.0% |
| WTA | 569 | 23.2 | 13.0 | 35.9 | 14.4 | 9.0 | 3.3 | 1.2 | 6.68 | 13.5% | 4.6% |
| WTA125 | 343 | 21.9 | 11.4 | 31.5 | 16.3 | 13.7 | 4.7 | 0.6 | 7.99 | 18.9% | 5.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 604 | 30.1 | 23.2 | 35.3 | 9.6 | 1.5 | 0.3 | 0.0 | 4.72 | 1.8% | 0.3% |
| CHALLENGER | 1,521 | 23.6 | 17.5 | 26.0 | 13.7 | 11.9 | 5.4 | 2.0 | 6.45 | 19.3% | 7.4% |
| DOUBLES | 819 | 4.0 | 3.3 | 10.6 | 11.6 | 19.3 | 24.4 | 26.7 | 25.63 | 70.5% | 51.2% |
| ITF_MEN | 3,935 | 14.8 | 8.5 | 21.1 | 15.2 | 20.4 | 12.3 | 7.7 | 11.76 | 40.4% | 20.0% |
| ITF_WOMEN | 4,651 | 11.5 | 9.3 | 19.9 | 14.6 | 22.4 | 16.7 | 5.6 | 13.01 | 44.7% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 465 | 21.3 | 12.0 | 26.0 | 18.3 | 14.8 | 6.9 | 0.7 | 8.27 | 22.4% | 7.5% |
| WTA125 | 513 | 16.6 | 13.1 | 22.6 | 20.3 | 16.2 | 8.6 | 2.7 | 9.21 | 27.5% | 11.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,089 | 29.4 | 14.4 | 24.7 | 17.5 | 11.7 | 1.3 | 1.0 | 5.93 | 14.0% | 2.3% |
| CHALLENGER | 1,648 | 20.7 | 14.0 | 23.9 | 19.3 | 13.0 | 6.4 | 2.8 | 7.97 | 22.2% | 9.2% |
| ITF_MEN | 2,873 | 14.3 | 10.9 | 21.9 | 16.7 | 19.0 | 11.9 | 5.1 | 10.81 | 36.1% | 17.1% |
| ITF_WOMEN | 4,004 | 12.8 | 8.3 | 18.6 | 18.9 | 23.4 | 14.7 | 3.2 | 12.63 | 41.4% | 18.0% |
| WTA | 566 | 23.9 | 9.7 | 25.8 | 15.9 | 16.8 | 6.0 | 1.9 | 7.81 | 24.7% | 8.0% |
| WTA125 | 330 | 11.8 | 6.4 | 21.2 | 26.4 | 16.7 | 16.1 | 1.5 | 11.49 | 34.2% | 17.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,089 | 23.9 | 13.8 | 24.7 | 18.4 | 16.0 | 2.1 | 1.2 | 6.9 | 19.3% | 3.3% |
| CHALLENGER | 1,648 | 20.2 | 9.8 | 22.9 | 16.4 | 18.5 | 9.4 | 2.7 | 9.08 | 30.6% | 12.1% |
| ITF_MEN | 2,874 | 12.6 | 9.2 | 19.4 | 16.7 | 21.4 | 14.8 | 5.9 | 12.46 | 42.1% | 20.7% |
| ITF_WOMEN | 4,004 | 10.7 | 7.2 | 14.4 | 14.2 | 23.2 | 20.2 | 10.1 | 16.26 | 53.4% | 30.2% |
| WTA | 566 | 22.3 | 5.3 | 19.1 | 15.2 | 20.7 | 15.6 | 1.9 | 11.69 | 38.2% | 17.5% |
| WTA125 | 330 | 4.5 | 2.7 | 17.6 | 21.2 | 22.1 | 21.8 | 10.0 | 17.02 | 53.9% | 31.8% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 584 | 30.1 | 23.5 | 35.6 | 9.8 | 0.7 | 0.3 | 0.0 | 4.7 | 1.0% | 0.3% |
| CHALLENGER | 1,289 | 25.7 | 19.8 | 28.2 | 13.3 | 10.9 | 2.1 | 0.1 | 5.76 | 13.1% | 2.2% |
| DOUBLES | 758 | 4.0 | 3.3 | 10.8 | 11.6 | 19.5 | 24.1 | 26.6 | 25.59 | 70.3% | 50.8% |
| ITF_MEN | 3,168 | 16.5 | 9.4 | 23.4 | 16.1 | 20.2 | 9.9 | 4.4 | 10.12 | 34.5% | 14.3% |
| ITF_WOMEN | 3,786 | 12.8 | 10.0 | 21.8 | 15.4 | 22.7 | 14.9 | 2.3 | 11.48 | 39.9% | 17.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 435 | 21.8 | 12.6 | 26.7 | 18.4 | 15.2 | 5.3 | 0.0 | 7.98 | 20.5% | 5.3% |
| WTA125 | 428 | 18.5 | 14.5 | 25.0 | 23.1 | 14.2 | 4.4 | 0.2 | 8.16 | 18.9% | 4.7% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 819 | 4.0 | 3.3 | 10.6 | 11.6 | 19.3 | 24.4 | 26.7 | 25.63 | 70.5% | 51.2% |
| singles | 11,838 | 15.8 | 11.1 | 22.4 | 14.8 | 18.7 | 12.1 | 5.2 | 10.16 | 35.9% | 17.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 3,230 | 13.6 | 9.6 | 20.1 | 16.0 | 16.1 | 14.2 | 10.3 | 12.14 | 40.6% | 24.5% |
| Hard | 9,391 | 13.9 | 8.4 | 18.1 | 16.1 | 18.9 | 14.6 | 10.0 | 12.92 | 43.5% | 24.5% |
| UNKNOWN | 1,388 | 11.5 | 8.2 | 15.2 | 18.2 | 20.0 | 16.7 | 10.2 | 13.98 | 46.8% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4,133 | 19.9 | 10.6 | 20.4 | 17.4 | 14.6 | 9.3 | 7.8 | 9.7 | 31.7% | 17.1% |
| B | 1,880 | 15.2 | 9.6 | 19.4 | 17.2 | 16.6 | 12.0 | 10.0 | 11.31 | 38.7% | 22.0% |
| C | 2,161 | 12.4 | 9.9 | 19.5 | 15.4 | 18.6 | 14.8 | 9.4 | 12.69 | 42.9% | 24.3% |
| D | 2,638 | 10.8 | 8.3 | 17.3 | 16.4 | 22.1 | 15.0 | 9.9 | 13.98 | 47.0% | 24.9% |
| F | 3,197 | 7.7 | 5.1 | 14.8 | 14.9 | 21.1 | 22.9 | 13.5 | 18.39 | 57.5% | 36.4% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 3,557 | 22.3 | 15.8 | 28.0 | 15.3 | 11.8 | 5.0 | 1.9 | 6.87 | 18.6% | 6.8% |
| B | 1,985 | 14.6 | 9.7 | 24.5 | 16.1 | 18.9 | 11.6 | 4.6 | 10.37 | 35.1% | 16.2% |
| C | 2,610 | 11.8 | 7.8 | 18.1 | 14.5 | 20.6 | 15.7 | 11.6 | 13.95 | 47.9% | 27.2% |
| D | 2,087 | 14.0 | 9.2 | 21.3 | 13.1 | 22.0 | 14.0 | 6.2 | 12.05 | 42.3% | 20.3% |
| F | 2,418 | 9.1 | 7.8 | 14.2 | 13.7 | 23.6 | 21.5 | 10.1 | 16.94 | 55.2% | 31.6% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 4,651 | 18.5 | 9.8 | 19.6 | 17.3 | 14.9 | 10.0 | 10.0 | 10.55 | 34.8% | 20.0% |
| LIMITED | 3,482 | 14.7 | 10.5 | 20.5 | 16.1 | 17.7 | 13.3 | 7.2 | 11.32 | 38.2% | 20.5% |
| POOR | 5,876 | 9.2 | 6.7 | 15.9 | 15.6 | 21.6 | 19.2 | 11.8 | 16.04 | 52.6% | 31.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 2,504 | 30.1 | 24.9 | 37.0 | 5.5 | 1.9 | 0.6 | 0.1 | 4.56 | 2.6% | 0.7% |
| GAME_SPREAD | 2,372 | 25.0 | 15.6 | 36.7 | 17.5 | 4.7 | 0.2 | 0.2 | 6.13 | 5.1% | 0.4% |
| MATCH_WINNER | 12,657 | 15.0 | 10.6 | 21.7 | 14.6 | 18.7 | 12.9 | 6.6 | 10.77 | 38.1% | 19.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 4,274 | 32.0 | 19.8 | 30.5 | 10.0 | 6.2 | 1.3 | 0.3 | 4.82 | 7.8% | 1.6% |
| TOTAL_GAMES | 3,395 | 7.2 | 9.4 | 38.6 | 30.5 | 9.1 | 2.8 | 2.4 | 9.43 | 14.3% | 5.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,047 | 24.9 | 38.0 | 31.6 | 0.2 | 4.6 | 0.5 | 0.1 | 4.34 | 5.3% | 0.7% |
| GAME_SPREAD | 2,834 | 45.4 | 14.6 | 29.7 | 8.0 | 1.2 | 0.8 | 0.3 | 3.58 | 2.3% | 1.1% |
| TOTAL_GAMES | 4,016 | 3.3 | 6.7 | 45.0 | 36.5 | 5.2 | 1.2 | 2.0 | 9.53 | 8.4% | 3.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,047 | 25.6 | 18.4 | 36.5 | 9.7 | 6.9 | 2.5 | 0.4 | 5.6 | 9.8% | 2.9% |
| GAME_SPREAD | 2,834 | 18.9 | 13.2 | 28.6 | 21.7 | 14.3 | 2.6 | 0.7 | 8.03 | 17.6% | 3.3% |
| TOTAL_GAMES | 4,025 | 6.4 | 8.3 | 39.9 | 28.9 | 11.5 | 2.7 | 2.3 | 9.5 | 16.5% | 5.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 14,009 | 43.1% | 24.8% | 12.85 | 33.0% | 14.2% | 10.31 |
| gen1_elo | 14,009 | 43.0% | 24.0% | 12.42 | 32.5% | 13.8% | 9.7 |
| gen1_sr | 14,009 | 51.5% | 30.1% | 15.51 | 42.4% | 19.6% | 12.64 |
| gen2 | 14,009 | 50.2% | 30.4% | 15.12 | 42.4% | 21.4% | 12.54 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 7,138 | 16.6 | 11.0 | 21.3 | 17.7 | 18.5 | 11.4 | 3.4 | 10.3 | 33.4% | 14.8% |
| STALE | 6,871 | 10.5 | 6.3 | 15.1 | 14.8 | 18.2 | 18.1 | 17.0 | 16.86 | 53.3% | 35.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 6,125 | 17.1 | 11.7 | 23.7 | 14.4 | 16.8 | 11.5 | 4.8 | 9.34 | 33.1% | 16.3% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 26,666 | 6125 | 10610 | 9931 | 24.9 | 159.4 | 1400.4 |
| ge_15pp | 10,872 | 2029 | 3671 | 5172 | 28.6 | 452.7 | 1380.4 |
| ge_25pp | 5,929 | 999 | 1651 | 3279 | 36.4 | 573.1 | 1380.4 |
| lt_10pp | 11,666 | 3215 | 5122 | 3329 | 23.2 | 49.5 | 1230.8 |

Current slate `SL-20261009T135226Z-462f2865`: 521 priced rows, quote age at build {'median': 5.2, 'max': 5.3}, freshness {'FRESH': 521}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 4 | 0.0 | 0.0 | 25.0 | 0.0 | 75.0 | 0.0 | 0.0 | 20.45 | 75.0% | 0.0% |
| EXTERNAL_LONE_OUTLIER | 4 | 25.0 | 75.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 3.22 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 784 | 24.1 | 11.1 | 21.2 | 20.5 | 15.7 | 7.0 | 0.4 | 8.14 | 23.1% | 7.4% |
| MARKETS_AGREE | 119 | 78.2 | 21.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.6 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 190 | 0.0 | 3.7 | 33.7 | 35.3 | 18.4 | 8.4 | 0.5 | 11.66 | 27.4% | 8.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 14,009 | 1101 (7.9%) | 17.3% | 0.3% | {"EXTERNAL_STALE": 784, "AGREES_WITH_KALSHI": 190, "ALL_AGREE": 119, "EXTERNAL_OUTLIER": 4, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 6,044 | 236 (3.9%) | 22.0% | 1.3% | {"EXTERNAL_STALE": 181, "AGREES_WITH_KALSHI": 52, "SUPPORTS_MODEL_DIRECTION": 3} |
| fair_v1_ge_25pp | 3,468 | 75 (2.2%) | 22.7% | 0.0% | {"EXTERNAL_STALE": 58, "AGREES_WITH_KALSHI": 17} |
| fair_v1_ge_25pp_pregame_clean | 1,489 | 73 (4.9%) | 23.3% | 0.0% | {"EXTERNAL_STALE": 56, "AGREES_WITH_KALSHI": 17} |
| fair_v1_lt_10pp | 5,682 | 637 (11.2%) | 11.2% | 0.0% | {"EXTERNAL_STALE": 442, "ALL_AGREE": 119, "AGREES_WITH_KALSHI": 71, "EXTERNAL_OUTLIER": 4, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 2,849 | 11.7 | 8.3 | 19.7 | 15.6 | 20.6 | 13.8 | 10.2 | 13.02 | 44.7% | 24.1% |
| 4-10x | 1,976 | 11.2 | 9.2 | 18.3 | 15.4 | 20.1 | 16.5 | 9.2 | 13.56 | 45.8% | 25.7% |
| <2x | 7,431 | 15.7 | 9.2 | 18.4 | 17.3 | 16.7 | 13.2 | 9.7 | 11.95 | 39.5% | 22.8% |
| >=10x | 1,753 | 10.7 | 6.3 | 15.5 | 14.3 | 20.0 | 20.6 | 12.5 | 16.5 | 53.1% | 33.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 3,660 | 14.3 | 8.6 | 19.0 | 15.9 | 18.2 | 13.0 | 11.0 | 12.39 | 42.2% | 24.0% |
| 300-1000 | 3,453 | 11.8 | 9.1 | 16.6 | 16.4 | 20.9 | 16.0 | 9.2 | 13.73 | 46.0% | 25.1% |
| <300 | 3,685 | 8.2 | 5.9 | 15.7 | 15.0 | 21.1 | 21.0 | 13.1 | 17.18 | 55.2% | 34.1% |
| >=3000 | 3,211 | 21.1 | 11.4 | 22.1 | 18.1 | 12.8 | 8.0 | 6.5 | 8.73 | 27.3% | 14.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 451 | 0.5411 | 0.4086 | 0.4789 | +0.062 | -0.070 | 0.0043 ± 0.0069 |
| ratio 4-10x | 315 | 0.581 | 0.4397 | 0.527 | +0.054 | -0.087 | -0.0025 ± 0.0088 |
| ratio <2x | 971 | 0.5406 | 0.417 | 0.4521 | +0.088 | -0.035 | 0.013 ± 0.0046 |
| ratio >=10x | 298 | 0.5499 | 0.3798 | 0.4362 | +0.114 | -0.057 | 0.0164 ± 0.0102 |
| thinner_sample 1000-3000 | 557 | 0.5434 | 0.4193 | 0.4596 | +0.084 | -0.040 | 0.0082 ± 0.0061 |
| thinner_sample 300-1000 | 559 | 0.569 | 0.4285 | 0.4973 | +0.072 | -0.069 | 0.0022 ± 0.0066 |
| thinner_sample <300 | 605 | 0.5433 | 0.3826 | 0.4595 | +0.084 | -0.077 | 0.0108 ± 0.0069 |
| thinner_sample >=3000 | 314 | 0.5302 | 0.4341 | 0.4427 | +0.087 | -0.009 | 0.0201 ± 0.0065 |
| data_status ADEQUATE | 534 | 0.529 | 0.4254 | 0.4401 | +0.089 | -0.015 | 0.0139 ± 0.0053 |
| data_status LIMITED | 539 | 0.5605 | 0.4282 | 0.4861 | +0.074 | -0.058 | 0.0041 ± 0.0065 |
| data_status POOR | 962 | 0.5523 | 0.398 | 0.4719 | +0.080 | -0.074 | 0.0093 ± 0.0053 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 311 | 0.1904 | 0.1915 | -0.0010 ± 0.0009 | 0.5575 | 0.5602 | 0.4923 | 0.4777 | 0.5145 | -0.068 ± 0.026 | -0.01 (3) |
| 3-5 | 209 | 0.1873 | 0.1887 | -0.0014 ± 0.0024 | 0.5543 | 0.5557 | 0.5112 | 0.4714 | 0.5072 | -0.059 ± 0.0305 | 0.02 (1) |
| 5-10 | 411 | 0.2006 | 0.2029 | -0.0023 ± 0.0033 | 0.5875 | 0.5929 | 0.5228 | 0.4488 | 0.4915 | -0.084 ± 0.0232 | -0.0125 (4) |
| 10-15 | 366 | 0.2128 | 0.2074 | +0.0054 ± 0.006 | 0.6122 | 0.5962 | 0.5184 | 0.3946 | 0.4317 | -0.090 ± 0.0238 | -0.0633 (3) |
| 15-25 | 433 | 0.2266 | 0.2106 | +0.0160 ± 0.0086 | 0.6484 | 0.6084 | 0.5734 | 0.378 | 0.4342 | -0.093 ± 0.022 | -0.0133 (6) |
| 25-40 | 250 | 0.2202 | 0.2008 | +0.0194 ± 0.0168 | 0.6303 | 0.5771 | 0.6469 | 0.3379 | 0.46 | -0.074 ± 0.0252 | -0.01 (1) |
| 40+ | 55 | 0.2888 | 0.1716 | +0.1171 ± 0.0497 | 0.7822 | 0.5171 | 0.752 | 0.305 | 0.4 | -0.128 ± 0.0484 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1554 | 0.1693 | 0.1702 | -0.0010 ± 0.0004 | 0.5078 | 0.509 | 0.4736 | 0.459 | 0.4987 | -0.020 ± 0.0106 | -0.0188 (8) |
| 3-5 | 1000 | 0.1926 | 0.1895 | +0.0031 ± 0.0011 | 0.5664 | 0.5536 | 0.4787 | 0.4391 | 0.417 | -0.082 ± 0.014 | 0.02 (1) |
| 5-10 | 2113 | 0.1959 | 0.1935 | +0.0024 ± 0.0014 | 0.575 | 0.5676 | 0.4907 | 0.4171 | 0.4335 | -0.054 ± 0.0097 | -0.0082 (17) |
| 10-15 | 1934 | 0.1991 | 0.1825 | +0.0166 ± 0.0024 | 0.5826 | 0.536 | 0.4709 | 0.3463 | 0.3423 | -0.073 ± 0.0097 | -0.0475 (4) |
| 15-25 | 2243 | 0.2033 | 0.1635 | +0.0398 ± 0.0033 | 0.5987 | 0.4878 | 0.4911 | 0.2951 | 0.2925 | -0.078 ± 0.0085 | -0.0048 (29) |
| 25-40 | 1884 | 0.2178 | 0.123 | +0.0947 ± 0.0051 | 0.628 | 0.381 | 0.5267 | 0.213 | 0.2213 | -0.061 ± 0.0078 | -0.01 (1) |
| 40+ | 1295 | 0.3712 | 0.0448 | +0.3263 ± 0.0065 | 0.9675 | 0.1767 | 0.6226 | 0.1063 | 0.0587 | -0.083 ± 0.0055 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 239 | 0.1951 | 0.1954 | -0.0003 ± 0.001 | 0.5731 | 0.5741 | 0.4934 | 0.4783 | 0.4812 | -0.100 ± 0.0302 | -0.01 (1) |
| 3-5 | 160 | 0.2117 | 0.2126 | -0.0008 ± 0.003 | 0.605 | 0.6091 | 0.522 | 0.482 | 0.5062 | -0.062 ± 0.0382 | 0.02 (1) |
| 5-10 | 354 | 0.1923 | 0.1895 | +0.0028 ± 0.0035 | 0.5664 | 0.5603 | 0.5669 | 0.4922 | 0.5085 | -0.094 ± 0.0239 | -0.01 (4) |
| 10-15 | 344 | 0.2158 | 0.2084 | +0.0074 ± 0.0062 | 0.6176 | 0.6033 | 0.5782 | 0.4534 | 0.4913 | -0.098 ± 0.0256 | -0.05 (4) |
| 15-25 | 488 | 0.225 | 0.2057 | +0.0193 ± 0.0081 | 0.6386 | 0.5934 | 0.5964 | 0.3991 | 0.4549 | -0.096 ± 0.021 | -0.01 (5) |
| 25-40 | 327 | 0.2759 | 0.2008 | +0.0751 ± 0.0157 | 0.7741 | 0.5814 | 0.6724 | 0.3582 | 0.3976 | -0.143 ± 0.0247 | -0.025 (2) |
| 40+ | 123 | 0.341 | 0.1909 | +0.1501 ± 0.0381 | 0.9583 | 0.5575 | 0.7617 | 0.2833 | 0.3821 | -0.059 ± 0.0368 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1382 | 0.1751 | 0.1756 | -0.0006 ± 0.0004 | 0.5223 | 0.5237 | 0.4948 | 0.4806 | 0.5043 | -0.033 ± 0.0117 | -0.0217 (6) |
| 3-5 | 853 | 0.1941 | 0.1923 | +0.0018 ± 0.0012 | 0.5622 | 0.5584 | 0.5224 | 0.4825 | 0.4795 | -0.055 ± 0.0152 | 0.02 (1) |
| 5-10 | 1880 | 0.1857 | 0.1819 | +0.0039 ± 0.0015 | 0.5527 | 0.5396 | 0.5177 | 0.4446 | 0.4585 | -0.052 ± 0.01 | -0.01 (5) |
| 10-15 | 1675 | 0.1946 | 0.1806 | +0.0140 ± 0.0026 | 0.5748 | 0.5296 | 0.5157 | 0.3913 | 0.4006 | -0.065 ± 0.0106 | -0.02 (14) |
| 15-25 | 2364 | 0.2149 | 0.1728 | +0.0421 ± 0.0034 | 0.6254 | 0.5119 | 0.5284 | 0.3328 | 0.3266 | -0.083 ± 0.0086 | -0.0026 (27) |
| 25-40 | 2160 | 0.2511 | 0.1367 | +0.1145 ± 0.0051 | 0.7136 | 0.417 | 0.5619 | 0.2454 | 0.2241 | -0.093 ± 0.008 | -0.015 (6) |
| 40+ | 1709 | 0.4026 | 0.0689 | +0.3336 ± 0.0072 | 1.0549 | 0.2405 | 0.6691 | 0.1316 | 0.1042 | -0.069 ± 0.0062 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 318 | 0.1937 | 0.1962 | -0.0025 ± 0.0009 | 0.5661 | 0.5732 | 0.5001 | 0.4848 | 0.5472 | -0.023 ± 0.0251 | -0.0133 (6) |
| 3-5 | 216 | 0.1889 | 0.1874 | +0.0015 ± 0.0023 | 0.5539 | 0.55 | 0.4978 | 0.4586 | 0.463 | -0.116 ± 0.0311 | -0.01 (1) |
| 5-10 | 442 | 0.1973 | 0.197 | +0.0002 ± 0.0032 | 0.5804 | 0.5784 | 0.5084 | 0.4348 | 0.4661 | -0.085 ± 0.022 | -0.01 (4) |
| 10-15 | 339 | 0.2143 | 0.2119 | +0.0024 ± 0.0062 | 0.6181 | 0.6075 | 0.5356 | 0.4129 | 0.4661 | -0.084 ± 0.0247 | -0.044 (5) |
| 15-25 | 420 | 0.2294 | 0.2084 | +0.0209 ± 0.0087 | 0.6588 | 0.6018 | 0.5791 | 0.3857 | 0.4286 | -0.107 ± 0.022 | -0.03 (1) |
| 25-40 | 252 | 0.2016 | 0.2037 | -0.0021 ± 0.0166 | 0.5862 | 0.5857 | 0.6533 | 0.3418 | 0.496 | -0.050 ± 0.0243 | 0.0 (1) |
| 40+ | 48 | 0.3114 | 0.1729 | +0.1385 ± 0.0545 | 0.836 | 0.5193 | 0.7473 | 0.2942 | 0.375 | -0.138 ± 0.0544 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1467 | 0.1815 | 0.1825 | -0.0010 ± 0.0004 | 0.5362 | 0.5383 | 0.4848 | 0.4696 | 0.501 | -0.026 ± 0.0112 | -0.0183 (23) |
| 3-5 | 1015 | 0.1865 | 0.1836 | +0.0029 ± 0.0011 | 0.5483 | 0.5415 | 0.472 | 0.4327 | 0.4158 | -0.084 ± 0.0139 | -0.0243 (7) |
| 5-10 | 2297 | 0.1869 | 0.1826 | +0.0043 ± 0.0013 | 0.5555 | 0.5411 | 0.4785 | 0.4046 | 0.414 | -0.055 ± 0.009 | -0.01 (18) |
| 10-15 | 1770 | 0.1959 | 0.1797 | +0.0162 ± 0.0025 | 0.5759 | 0.5274 | 0.4894 | 0.366 | 0.3605 | -0.077 ± 0.01 | -0.03 (9) |
| 15-25 | 2411 | 0.2079 | 0.1686 | +0.0393 ± 0.0033 | 0.6107 | 0.5006 | 0.4946 | 0.2991 | 0.2978 | -0.073 ± 0.0084 | -0.03 (2) |
| 25-40 | 1833 | 0.2119 | 0.1181 | +0.0937 ± 0.0051 | 0.6143 | 0.3675 | 0.5226 | 0.2052 | 0.2193 | -0.059 ± 0.0076 | 0.0 (1) |
| 40+ | 1230 | 0.3849 | 0.0462 | +0.3387 ± 0.0069 | 1.0054 | 0.1809 | 0.63 | 0.1071 | 0.0561 | -0.086 ± 0.0058 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 599 | 0.2023 | 0.2024 | -0.0001 ± 0.0006 | 0.5877 | 0.5874 | 0.4989 | 0.484 | 0.4841 | -0.049 ± 0.0183 | -0.0226 (46) |
| 3-5 | 444 | 0.1967 | 0.1954 | +0.0013 ± 0.0017 | 0.5745 | 0.5695 | 0.4789 | 0.4393 | 0.4437 | -0.052 ± 0.021 | -0.0058 (33) |
| 5-10 | 911 | 0.1924 | 0.1873 | +0.0050 ± 0.0022 | 0.5691 | 0.5558 | 0.479 | 0.4055 | 0.4094 | -0.057 ± 0.0146 | -0.0049 (73) |
| 10-15 | 598 | 0.2026 | 0.1935 | +0.0091 ± 0.0045 | 0.5938 | 0.5687 | 0.486 | 0.3632 | 0.3863 | -0.041 ± 0.0179 | 0.0014 (64) |
| 15-25 | 801 | 0.2351 | 0.2081 | +0.0270 ± 0.0063 | 0.6686 | 0.6016 | 0.5496 | 0.3553 | 0.3845 | -0.060 ± 0.0162 | -0.0216 (58) |
| 25-40 | 454 | 0.2444 | 0.1859 | +0.0585 ± 0.0125 | 0.6883 | 0.5454 | 0.6292 | 0.3162 | 0.3767 | -0.075 ± 0.0189 | -0.0216 (25) |
| 40+ | 150 | 0.3521 | 0.1855 | +0.1666 ± 0.0357 | 1.0004 | 0.5492 | 0.7789 | 0.2874 | 0.3867 | -0.062 ± 0.0321 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1815 | 0.189 | 0.1888 | +0.0002 ± 0.0004 | 0.5538 | 0.5523 | 0.5023 | 0.4871 | 0.4848 | -0.046 ± 0.0101 | -0.0155 (82) |
| 3-5 | 1260 | 0.1883 | 0.1858 | +0.0025 ± 0.001 | 0.5512 | 0.5454 | 0.49 | 0.4505 | 0.4413 | -0.056 ± 0.0122 | -0.0148 (63) |
| 5-10 | 2599 | 0.1907 | 0.183 | +0.0077 ± 0.0013 | 0.5653 | 0.5437 | 0.476 | 0.4022 | 0.3913 | -0.063 ± 0.0085 | -0.0087 (125) |
| 10-15 | 1763 | 0.1988 | 0.1848 | +0.0140 ± 0.0026 | 0.5847 | 0.5475 | 0.4994 | 0.3764 | 0.3806 | -0.055 ± 0.0101 | -0.0053 (105) |
| 15-25 | 2283 | 0.229 | 0.1952 | +0.0337 ± 0.0036 | 0.6612 | 0.5694 | 0.5437 | 0.3485 | 0.3609 | -0.063 ± 0.0094 | -0.0255 (106) |
| 25-40 | 1574 | 0.2399 | 0.1605 | +0.0795 ± 0.0063 | 0.6815 | 0.4784 | 0.5906 | 0.2764 | 0.3088 | -0.062 ± 0.0098 | -0.0206 (47) |
| 40+ | 753 | 0.3677 | 0.1141 | +0.2536 ± 0.0131 | 1.0096 | 0.3565 | 0.6854 | 0.1803 | 0.1926 | -0.065 ± 0.0115 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 2035 | 1.072 ± 0.062 | 1.183 | 0.1706 | 0.1707 | 0.2102 | 0.201 |
| gen2 | 2035 | 0.864 ± 0.055 | 1.119 | 0.1868 | 0.1701 | 0.2284 | 0.201 |
| gen1_elo | 2035 | 1.066 ± 0.061 | 1.173 | 0.1747 | 0.1713 | 0.2085 | 0.201 |
| gen1_sr | 2035 | 1.06 ± 0.07 | 1.195 | 0.1447 | 0.1726 | 0.2234 | 0.2008 |
| gen1_ledger | 3957 | 0.908 ± 0.041 | 1.073 | 0.1735 | 0.1908 | 0.2166 | 0.1954 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 10,872)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,976 | 27.4% |
| STALE_QUOTE | market_freshness | 2,230 | 20.5% |
| BOOK_QUALITY | execution | 1,877 | 17.3% |
| POOR_DATA | data | 1,159 | 10.7% |
| LIMITED_DATA | data | 835 | 7.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 593 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 482 | 4.4% |
| IDENTITY_AMBIGUOUS | mapping | 340 | 3.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 328 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 52 | 0.5% |

Cause class: coverage 27.4%, market_freshness 20.5%, data 18.3%, execution 17.3%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.4%, mapping 3.1%, model_calibration 0.5%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.2%, START_UNVERIFIABLE 96.2%, LOW_DATA_QUALITY 68.7%, STALE_PLAYER_DATA 57.4%, THIN_PLAYER_HISTORY 56.9%, STALE_KALSHI_QUOTE 47.6%, MODEL_INTERNAL_DISAGREEMENT 37.3%, ASYMMETRIC_SAMPLE_SIZE 30.4%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 16.3%, PLAYER_IDENTITY_RISK 11.4%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.3%, MODEL_CALIBRATION_OUTLIER 3.4%, EXTERNAL_MARKET_REJECTION 0.8%, UNKNOWN 0.5%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 29.9%, POST_SETTLEMENT_OBSERVATION 27.4%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.6%

### >= ge_25 pp (N = 5,929)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 2,338 | 39.4% |
| STALE_QUOTE | market_freshness | 997 | 16.8% |
| BOOK_QUALITY | execution | 992 | 16.7% |
| POOR_DATA | data | 467 | 7.9% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 324 | 5.5% |
| LIMITED_DATA | data | 260 | 4.4% |
| IDENTITY_AMBIGUOUS | mapping | 218 | 3.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 206 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 112 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 15 | 0.2% |

Cause class: coverage 39.4%, market_freshness 16.8%, execution 16.7%, data 12.3%, market_freshness/coverage 8.9%, mapping 3.7%, model_calibration_or_unknown 1.9%, model_calibration 0.2%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.6%, START_UNVERIFIABLE 98.2%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 58.3%, STALE_KALSHI_QUOTE 55.3%, STALE_PLAYER_DATA 52.0%, MODEL_INTERNAL_DISAGREEMENT 38.5%, ASYMMETRIC_SAMPLE_SIZE 32.0%, WIDE_SPREAD 22.8%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 14.5%, EVENT_MAPPING_RISK 9.8%, LEVEL_TRANSFER_RISK 7.6%, LOW_DISPLAYED_LIQUIDITY 7.6%, MODEL_CALIBRATION_OUTLIER 4.2%, EXTERNAL_MARKET_REJECTION 0.4%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.0%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 42.4%, POST_SETTLEMENT_OBSERVATION 39.4%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.7%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 4906, "IDENTITY_AMBIGUOUS": 1023}; ticker orientation: {"VERIFIED": 5929}.

Checks: discipline:AMBIGUOUS 419, discipline:PASS 5510, identity_confidence:AMBIGUOUS 860, identity_confidence:PASS 5069, level_mapping:NA 431, level_mapping:PASS 5498, market_pair:AMBIGUOUS 220, market_pair:NA 132, market_pair:PASS 5577, model_complement:NA 99, model_complement:PASS 5830, namesake:PASS 5929, physical_match_id:NA 2461, physical_match_id:PASS 3468, player_ids:PASS 5929, same_pair_other_event:PASS 5929, ticker_orientation:PASS 5929

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,702 | 1.6% | 1.6% | 0.5% | {"market_freshness": 20, "execution": 7} | 5.38 | 0.2186 / 0.2092 (167) | 18.1% | 0.1% | 5.8% | 1.7% |
| CHALLENGER | 3,856 | 18.5% | 6.1% | 12.0% | {"coverage": 447, "market_freshness": 107, "market_freshness/coverage": 86, "model_calibration_or_unknown": 41, "data": 25, "execution": 4, "model_calibration": 3} | 6.7 | 0.2242 / 0.2061 (902) | 45.1% | 4.6% | 1.7% | 23.8% |
| DOUBLES | 819 | 51.2% | 50.8% | 7.1% | {"execution": 152, "mapping": 127, "market_freshness": 106, "market_freshness/coverage": 27, "coverage": 7} | 25.59 | 0.318 / 0.2265 (219) | 28.6% | 0.0% | 100.0% | 7.4% |
| ITF_MEN | 7,970 | 23.6% | 15.6% | 31.8% | {"coverage": 778, "execution": 385, "data": 271, "market_freshness": 267, "market_freshness/coverage": 163, "mapping": 19, "model_calibration_or_unknown": 1} | 10.46 | 0.2096 / 0.1929 (1987) | 38.1% | 53.9% | 6.2% | 24.2% |
| ITF_WOMEN | 10,280 | 26.0% | 17.6% | 45.1% | {"coverage": 1089, "market_freshness": 439, "execution": 427, "data": 407, "market_freshness/coverage": 213, "mapping": 66, "model_calibration_or_unknown": 22, "model_calibration": 9} | 12.16 | 0.2038 / 0.1918 (2227) | 39.1% | 57.3% | 9.6% | 24.2% |
| OTHER | 149 | 8.1% | 7.3% | 0.2% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 1,034 | 7.8% | 6.8% | 1.4% | {"market_freshness": 34, "model_calibration_or_unknown": 18, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 7.96 | 0.21 / 0.2073 (153) | 32.3% | 2.0% | 1.2% | 3.2% |
| WTA125 | 856 | 14.1% | 10.3% | 2.0% | {"market_freshness/coverage": 31, "model_calibration_or_unknown": 28, "market_freshness": 22, "data": 13, "coverage": 12, "execution": 8, "mapping": 4, "model_calibration": 3} | 10.01 | 0.2303 / 0.2151 (295) | 25.5% | 6.2% | 4.0% | 11.5% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 3 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 4 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 5 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 6 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 8 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 9 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 10 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 11 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 12 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 14 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 15 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 18 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 19 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 21 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 22 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 23 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 24 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 25 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 26 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 27 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 28 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 29 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 30 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 31 | `KXITFWMATCH-26OCT07VELDES-DES` | ITF_WOMEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 64 min (STALE); no external reference |
| 32 | `KXITFMATCH-26OCT04SURLOK-LOK` | ITF_MEN | gen1_ledger | 76% / 2% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 76 min (STALE); data POOR (grade F, thinner serve sample 75.0, ratio 16.01); no external reference |
| 33 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 34 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 110 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 35 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 37 | `KXATPCHALLENGERMATCH-26OCT04BAYICH-ICH` | CHALLENGER | fair_v1 | 82% / 9% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 799 min (STALE); data POOR (grade D, thinner serve sample 357.0, ratio 8.77); no external reference |
| 38 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 39 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 347 min (STALE); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 40 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 41 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 42 | `KXITFWMATCH-26OCT08ARISAV-SAV` | ITF_WOMEN | fair_v1 | 75% / 2% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 826 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 44 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 687 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 45 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 46 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 47 | `KXITFMATCH-26OCT09DELSTE-DEL` | ITF_MEN | fair_v1 | 78% / 6% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 229 min (STALE); data POOR (grade F, thinner serve sample 477.0, ratio 8.93); no external reference |
| 48 | `KXITFWMATCH-26OCT08ARAWAN-ARA` | ITF_WOMEN | fair_v1 | 77% / 6% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 341 min (STALE); data POOR (grade D, thinner serve sample 553.0, ratio 3.97); no external reference |
| 49 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9819, "by_level_share_of_ge_25pp": {"ATP": 0.0046, "CHALLENGER": 0.1203, "DOUBLES": 0.0707, "ITF_MEN": 0.3178, "ITF_WOMEN": 0.4507, "OTHER": 0.002, "WTA": 0.0137, "WTA125": 0.0204}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.553, "share_primary_cause_market_settled_or_in_play": 0.4836, "share_primary_cause_stale_quote_only": 0.1682}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 5929, "identity_ambiguous_share": 0.1725, "ticker_orientation": {"VERIFIED": 5929}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 3468, "with_external": 75, "coverage": 0.0216, "external_status": {"EXTERNAL_STALE": 58, "AGREES_WITH_KALSHI": 17}, "triangulation": {"INSUFFICIENT_INPUTS": 58, "MODEL_LONE_OUTLIER": 17}, "share_external_agrees_with_kalshi": 0.2267, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 1489, "with_external": 73, "coverage": 0.049, "external_status": {"EXTERNAL_STALE": 56, "AGREES_WITH_KALSHI": 17}, "triangulation": {"INSUFFICIENT_INPUTS": 56, "MODEL_LONE_OUTLIER": 17}, "share_external_agrees_with_kalshi": 0.2329, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 627.5, "median_sample_ratio": 2.31, "median_min_matches": 21.0, "median_max_days_since_last": 196.0, "share_severe_asymmetry": 0.1725, "data_status": {"POOR": 3025, "LIMITED": 1827, "ADEQUATE": 1077}, "comparison_lt_10pp": {"median_thinner_serve_points": 1824.0, "median_sample_ratio": 1.71, "median_min_matches": 81.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 451, "model_minus_observed": 0.0622, "kalshi_minus_observed": -0.0703, "brier_diff_model_minus_kalshi": 0.0043}, "4-10x": {"n": 315, "model_minus_observed": 0.054, "kalshi_minus_observed": -0.0873, "brier_diff_model_minus_kalshi": -0.0025}, "<2x": {"n": 971, "model_minus_observed": 0.0885, "kalshi_minus_observed": -0.0351, "brier_diff_model_minus_kalshi": 0.013}, ">=10x": {"n": 298, "model_minus_observed": 0.1136, "kalshi_minus_observed": -0.0565, "brier_diff_model_minus_kalshi": 0.0164}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 2035, "model": {"intercept": -0.568, "slope": 0.864, "slope_se": 0.055}, "kalshi_mid_same_rows": {"intercept": 0.21, "slope": 1.119, "slope_se": 0.063}, "mean_extremity_model": 0.1868, "mean_extremity_kalshi": 0.1701, "model_brier": 0.2284, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0274, "brier_diff_se": 0.0042, "model_logloss": 0.6533, "kalshi_logloss": 0.5842}, "fair_v1": {"n": 2035, "model": {"intercept": -0.407, "slope": 1.072, "slope_se": 0.062}, "kalshi_mid_same_rows": {"intercept": 0.325, "slope": 1.183, "slope_se": 0.065}, "mean_extremity_model": 0.1706, "mean_extremity_kalshi": 0.1707, "model_brier": 0.2102, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0092, "brier_diff_se": 0.0034, "model_logloss": 0.6074, "kalshi_logloss": 0.584}, "gen1_elo": {"n": 2035, "model": {"intercept": -0.383, "slope": 1.066, "slope_se": 0.061}, "kalshi_mid_same_rows": {"intercept": 0.33, "slope": 1.173, "slope_se": 0.064}, "mean_extremity_model": 0.1747, "mean_extremity_kalshi": 0.1713, "model_brier": 0.2085, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0075, "brier_diff_se": 0.0033, "model_logloss": 0.6046, "kalshi_logloss": 0.5838}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2476, "share_ge_15": 0.4314, "median_abs_gap": 12.85, "n": 14009}, "gen1_elo": {"share_ge_25": 0.2399, "share_ge_15": 0.4299, "median_abs_gap": 12.42, "n": 14009}, "gen1_sr": {"share_ge_25": 0.3007, "share_ge_15": 0.5148, "median_abs_gap": 15.51, "n": 14009}, "gen2": {"share_ge_25": 0.3044, "share_ge_15": 0.502, "median_abs_gap": 15.12, "n": 14009}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1417, "share_ge_15": 0.3296, "median_abs_gap": 10.31, "n": 10510}, "gen1_elo": {"share_ge_25": 0.138, "share_ge_15": 0.3248, "median_abs_gap": 9.7, "n": 10509}, "gen1_sr": {"share_ge_25": 0.1959, "share_ge_15": 0.4236, "median_abs_gap": 12.64, "n": 10510}, "gen2": {"share_ge_25": 0.2136, "share_ge_15": 0.424, "median_abs_gap": 12.54, "n": 10511}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.38, "share_ge_25_all": 0.0159, "share_ge_25_pregame_clean": 0.0161}, "WTA": {"median_abs_gap_pregame_clean": 7.96, "share_ge_25_all": 0.0783, "share_ge_25_pregame_clean": 0.0679}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2387, "share_within_10pp_all": 0.4375, "share_within_10pp_pregame_clean": 0.5018, "corr_model_vs_mid_pregame_clean": 0.85}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 311, "model_brier": 0.1904, "kalshi_brier": 0.1915, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 366, "model_brier": 0.2128, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.0054}, "15-25": {"n_settled": 433, "model_brier": 0.2266, "kalshi_brier": 0.2106, "brier_diff_model_minus_kalshi": 0.016}, "25-40": {"n_settled": 250, "model_brier": 0.2202, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": 0.0194}, "3-5": {"n_settled": 209, "model_brier": 0.1873, "kalshi_brier": 0.1887, "brier_diff_model_minus_kalshi": -0.0014}, "40+": {"n_settled": 55, "model_brier": 0.2888, "kalshi_brier": 0.1716, "brier_diff_model_minus_kalshi": 0.1171}, "5-10": {"n_settled": 411, "model_brier": 0.2006, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": -0.0023}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.568, "slope": 0.864, "slope_se": 0.055}, "kalshi_slope": {"intercept": 0.21, "slope": 1.119, "slope_se": 0.063}, "n": 2035}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.538, "slope": 0.908, "slope_se": 0.041}, "kalshi_slope": {"intercept": 0.135, "slope": 1.073, "slope_se": 0.044}, "n": 3957}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 219, "model_brier": 0.318, "kalshi_brier": 0.2265, "brier_diff_model_minus_kalshi": 0.0916, "brier_diff_se": 0.0213, "corr_model_outcome": 0.0053, "corr_kalshi_outcome": 0.3239}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
