# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-27T13:01Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 59,208): 0-3 14.0%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 19.2%, 25-40 13.9%, 40+ 8.0%; median gap 11.96 pp.
* **Where the extremes live**: 96.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.5%, Challenger 11.7%, doubles 6.7%). Main tour: ATP 4.5% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 12,981): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.1%, BOOK_QUALITY 19.1%, STALE_QUOTE 19.0%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.3%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.1%, execution 19.1%, market_freshness 19.0%, data 12.5%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.3%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 12,981 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 459.0 points vs 1774.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.029, Gen-2 0.816, Gen-1 ledger 0.861 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 626 model 0.2219 vs Kalshi 0.2098; n 129 model 0.2737 vs Kalshi 0.2.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 259,421 model-market comparisons (419,592 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 86,807 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-27T12:50:10.030826+00:00'], shadow board 68,026 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-27T12:50:13.617896+00:00'], Model 4 33,669 rows, 21,532 settled tickers, 7,738 tickers with an external scan.
* By model: {"gen1_ledger": 59203, "gen1_elo": 34203, "fair_v1": 34203, "gen2": 34203, "gen1_sr": 34203, "model4_fundamental": 31725, "model4_conditioned": 31681}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 59,208 | 14.0 | 9.6 | 19.9 | 15.4 | 19.2 | 13.9 | 8.0 | 11.96 | 41.1% | 21.9% |
| MW fair_v1 | 34,203 | 12.9 | 8.7 | 18.6 | 15.6 | 19.7 | 14.9 | 9.6 | 13.04 | 44.2% | 24.5% |
| MW gen1_elo | 34,203 | 12.8 | 8.5 | 19.2 | 15.4 | 19.8 | 14.7 | 9.5 | 12.86 | 44.0% | 24.2% |
| MW gen1_ledger | 25,005 | 15.5 | 10.7 | 21.8 | 15.2 | 18.4 | 12.7 | 5.7 | 10.49 | 36.8% | 18.4% |
| MW gen1_sr | 34,203 | 10.3 | 7.2 | 16.9 | 13.7 | 20.7 | 18.6 | 12.7 | 15.87 | 52.0% | 31.3% |
| MW gen2 | 34,203 | 11.2 | 7.4 | 16.3 | 13.9 | 19.5 | 17.9 | 13.8 | 15.5 | 51.2% | 31.7% |
| all families model4_conditioned | 31,681 | 22.0 | 18.3 | 34.5 | 17.4 | 4.9 | 1.8 | 1.1 | 6.05 | 7.8% | 2.9% |
| all families model4_fundamental | 31,725 | 16.9 | 13.2 | 34.0 | 20.5 | 10.3 | 3.7 | 1.4 | 7.77 | 15.3% | 5.0% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.5%, >=15pp 41.1%, >=20pp 30.5%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.33pp; >=10pp 44.9%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,161 | 27.2 | 15.3 | 26.8 | 14.2 | 11.5 | 4.3 | 0.6 | 5.96 | 16.4% | 4.9% |
| CHALLENGER | 5,418 | 15.9 | 9.9 | 20.3 | 15.8 | 15.5 | 12.0 | 10.5 | 11.02 | 38.0% | 22.5% |
| ITF_MEN | 9,113 | 10.0 | 7.2 | 16.6 | 14.7 | 21.7 | 17.6 | 12.3 | 15.53 | 51.6% | 29.9% |
| ITF_WOMEN | 13,330 | 9.6 | 7.0 | 15.9 | 15.2 | 22.4 | 18.3 | 11.7 | 15.68 | 52.3% | 29.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,252 | 16.9 | 13.8 | 25.1 | 20.6 | 16.6 | 6.4 | 0.6 | 8.39 | 23.6% | 7.0% |
| WTA125 | 923 | 14.8 | 7.4 | 22.5 | 20.5 | 20.7 | 12.2 | 1.8 | 11.07 | 34.8% | 14.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,161 | 25.2 | 15.3 | 25.4 | 17.1 | 11.9 | 4.3 | 0.8 | 6.4 | 17.0% | 5.1% |
| CHALLENGER | 5,418 | 15.1 | 8.8 | 18.1 | 14.7 | 18.1 | 13.8 | 11.4 | 12.68 | 43.4% | 25.2% |
| ITF_MEN | 9,113 | 8.0 | 5.9 | 14.1 | 12.9 | 20.0 | 21.1 | 17.9 | 18.84 | 59.0% | 39.1% |
| ITF_WOMEN | 13,330 | 8.1 | 5.6 | 13.9 | 12.9 | 20.6 | 21.3 | 17.6 | 19.2 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,252 | 14.3 | 10.7 | 22.5 | 15.9 | 22.3 | 12.9 | 1.3 | 10.74 | 36.5% | 14.2% |
| WTA125 | 923 | 8.4 | 6.4 | 16.4 | 17.7 | 24.2 | 18.2 | 8.8 | 15.49 | 51.1% | 27.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,161 | 22.8 | 12.5 | 24.7 | 16.1 | 16.1 | 6.5 | 1.4 | 7.58 | 23.9% | 7.9% |
| CHALLENGER | 5,418 | 14.5 | 9.2 | 21.2 | 16.0 | 15.9 | 12.4 | 10.7 | 11.34 | 39.0% | 23.1% |
| ITF_MEN | 9,113 | 9.7 | 7.1 | 16.6 | 13.9 | 22.2 | 17.9 | 12.5 | 16.01 | 52.6% | 30.4% |
| ITF_WOMEN | 13,330 | 9.4 | 6.7 | 16.4 | 16.0 | 22.6 | 18.1 | 10.9 | 15.51 | 51.6% | 29.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,252 | 23.7 | 16.5 | 31.4 | 15.2 | 9.6 | 2.5 | 1.1 | 6.07 | 13.2% | 3.6% |
| WTA125 | 923 | 22.4 | 11.7 | 26.8 | 16.7 | 15.8 | 6.2 | 0.4 | 7.99 | 22.4% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,855 | 24.7 | 19.1 | 30.6 | 12.8 | 9.2 | 3.2 | 0.5 | 5.74 | 12.8% | 3.7% |
| CHALLENGER | 3,749 | 21.8 | 14.3 | 26.9 | 14.9 | 14.2 | 6.3 | 1.6 | 7.31 | 22.1% | 7.9% |
| DOUBLES | 1,839 | 5.2 | 4.5 | 12.1 | 10.4 | 20.5 | 25.4 | 21.9 | 23.89 | 67.8% | 47.3% |
| ITF_MEN | 6,851 | 13.0 | 9.0 | 20.1 | 16.1 | 21.5 | 13.7 | 6.5 | 12.27 | 41.8% | 20.2% |
| ITF_WOMEN | 8,294 | 12.8 | 8.9 | 19.4 | 15.4 | 21.4 | 16.2 | 5.9 | 12.68 | 43.5% | 22.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,322 | 23.5 | 15.7 | 30.0 | 17.8 | 9.6 | 3.0 | 0.3 | 6.76 | 12.9% | 3.3% |
| WTA125 | 946 | 22.7 | 13.1 | 21.2 | 18.8 | 14.2 | 8.0 | 1.9 | 8.26 | 24.1% | 9.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,081 | 27.5 | 15.6 | 27.2 | 14.1 | 11.3 | 3.9 | 0.4 | 5.92 | 15.6% | 4.3% |
| CHALLENGER | 3,854 | 20.6 | 12.3 | 25.0 | 18.3 | 15.5 | 6.5 | 1.7 | 8.34 | 23.7% | 8.2% |
| ITF_MEN | 6,722 | 12.0 | 8.6 | 19.8 | 16.7 | 22.9 | 14.4 | 5.5 | 12.88 | 42.9% | 20.0% |
| ITF_WOMEN | 10,072 | 11.3 | 8.2 | 18.1 | 17.2 | 24.2 | 15.4 | 5.5 | 13.54 | 45.1% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,187 | 17.1 | 13.7 | 25.1 | 20.8 | 16.6 | 6.1 | 0.6 | 8.39 | 23.3% | 6.7% |
| WTA125 | 893 | 15.1 | 7.3 | 22.2 | 20.7 | 21.3 | 11.9 | 1.6 | 11.08 | 34.7% | 13.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,081 | 25.4 | 15.7 | 25.6 | 17.0 | 11.8 | 4.0 | 0.5 | 6.28 | 16.3% | 4.5% |
| CHALLENGER | 3,854 | 19.2 | 11.0 | 22.4 | 17.3 | 18.5 | 9.6 | 2.0 | 9.31 | 30.1% | 11.6% |
| ITF_MEN | 6,723 | 9.4 | 7.0 | 16.4 | 14.9 | 21.9 | 19.3 | 11.0 | 15.67 | 52.2% | 30.3% |
| ITF_WOMEN | 10,073 | 9.1 | 6.4 | 15.4 | 14.3 | 22.6 | 20.9 | 11.3 | 16.88 | 54.7% | 32.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,187 | 14.4 | 10.7 | 22.6 | 16.0 | 22.4 | 12.7 | 1.3 | 10.71 | 36.4% | 14.0% |
| WTA125 | 893 | 8.4 | 6.4 | 16.5 | 18.0 | 24.1 | 18.6 | 8.1 | 15.19 | 50.7% | 26.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,802 | 24.8 | 19.4 | 30.6 | 12.9 | 8.8 | 3.0 | 0.4 | 5.67 | 12.3% | 3.4% |
| CHALLENGER | 3,305 | 23.1 | 15.3 | 28.2 | 15.0 | 13.6 | 4.4 | 0.5 | 6.8 | 18.5% | 4.8% |
| DOUBLES | 1,719 | 5.2 | 4.6 | 12.3 | 10.5 | 20.4 | 25.4 | 21.6 | 23.85 | 67.4% | 47.0% |
| ITF_MEN | 5,792 | 14.0 | 9.6 | 21.8 | 16.9 | 21.4 | 12.2 | 4.1 | 11.38 | 37.7% | 16.3% |
| ITF_WOMEN | 6,995 | 13.6 | 9.3 | 20.7 | 16.1 | 21.6 | 15.1 | 3.5 | 11.8 | 40.2% | 18.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,268 | 23.9 | 16.2 | 30.1 | 17.8 | 9.6 | 2.4 | 0.1 | 6.59 | 12.1% | 2.4% |
| WTA125 | 831 | 24.4 | 14.2 | 22.4 | 20.0 | 12.9 | 5.5 | 0.6 | 7.5 | 19.0% | 6.1% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,839 | 5.2 | 4.5 | 12.1 | 10.4 | 20.5 | 25.4 | 21.9 | 23.89 | 67.8% | 47.3% |
| singles | 23,166 | 16.3 | 11.2 | 22.5 | 15.6 | 18.3 | 11.7 | 4.4 | 9.98 | 34.4% | 16.1% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,360 | 12.8 | 9.2 | 19.9 | 15.9 | 18.9 | 13.9 | 9.3 | 12.54 | 42.3% | 23.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 21,757 | 13.5 | 8.8 | 18.5 | 15.3 | 19.7 | 14.9 | 9.4 | 12.99 | 44.0% | 24.3% |
| UNKNOWN | 4,837 | 10.9 | 7.3 | 17.1 | 16.7 | 20.7 | 16.1 | 11.2 | 14.12 | 48.0% | 27.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,889 | 19.8 | 12.4 | 22.1 | 16.2 | 14.6 | 9.1 | 5.8 | 8.73 | 29.6% | 14.9% |
| B | 4,209 | 12.5 | 8.7 | 19.2 | 16.5 | 19.6 | 12.8 | 10.6 | 12.69 | 43.0% | 23.4% |
| C | 4,707 | 11.8 | 8.9 | 19.4 | 16.0 | 19.4 | 14.4 | 10.1 | 13.0 | 43.9% | 24.5% |
| D | 5,199 | 12.2 | 8.0 | 17.6 | 15.3 | 21.6 | 15.7 | 9.7 | 13.86 | 46.9% | 25.4% |
| F | 10,199 | 7.4 | 5.5 | 15.0 | 14.5 | 23.8 | 21.1 | 12.7 | 17.82 | 57.6% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,081 | 23.7 | 15.9 | 28.8 | 15.1 | 11.2 | 3.9 | 1.3 | 6.55 | 16.4% | 5.2% |
| B | 3,390 | 16.5 | 10.3 | 23.8 | 16.2 | 19.6 | 10.3 | 3.4 | 9.86 | 33.3% | 13.8% |
| C | 4,796 | 11.0 | 7.3 | 19.0 | 14.5 | 21.2 | 16.2 | 10.8 | 14.17 | 48.2% | 27.0% |
| D | 3,452 | 14.1 | 9.8 | 20.6 | 15.4 | 20.8 | 13.6 | 5.8 | 11.68 | 40.1% | 19.3% |
| F | 6,286 | 9.9 | 8.2 | 15.5 | 15.2 | 22.6 | 20.7 | 8.0 | 15.68 | 51.3% | 28.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,208 | 18.0 | 11.2 | 21.3 | 16.0 | 15.2 | 10.0 | 8.4 | 9.89 | 33.5% | 18.4% |
| LIMITED | 7,249 | 13.6 | 10.0 | 20.0 | 16.5 | 19.6 | 13.2 | 7.2 | 11.91 | 40.0% | 20.4% |
| POOR | 15,746 | 9.0 | 6.4 | 16.0 | 14.9 | 23.0 | 19.1 | 11.7 | 16.23 | 53.7% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,014 | 24.5 | 18.5 | 33.2 | 14.6 | 6.3 | 2.5 | 0.3 | 5.74 | 9.2% | 2.9% |
| GAME_SPREAD | 5,538 | 22.3 | 15.4 | 33.2 | 16.7 | 9.1 | 2.8 | 0.5 | 6.71 | 12.4% | 3.3% |
| MATCH_WINNER | 25,005 | 15.5 | 10.7 | 21.8 | 15.2 | 18.4 | 12.7 | 5.7 | 10.49 | 36.8% | 18.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,592 | 27.9 | 16.5 | 30.9 | 12.6 | 9.4 | 2.5 | 0.3 | 5.67 | 12.1% | 2.8% |
| TOTAL_GAMES | 9,030 | 9.2 | 10.1 | 36.3 | 27.1 | 10.5 | 4.0 | 2.8 | 9.33 | 17.3% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,301 | 24.5 | 30.8 | 32.8 | 6.9 | 4.0 | 0.8 | 0.2 | 4.67 | 5.0% | 1.0% |
| GAME_SPREAD | 7,426 | 46.6 | 16.5 | 25.8 | 7.5 | 1.9 | 1.1 | 0.5 | 3.33 | 3.6% | 1.7% |
| TOTAL_GAMES | 12,954 | 5.7 | 8.4 | 40.9 | 32.3 | 7.4 | 3.1 | 2.2 | 9.46 | 12.7% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,312 | 23.8 | 16.9 | 35.0 | 14.2 | 7.2 | 2.6 | 0.3 | 6.03 | 10.1% | 2.9% |
| GAME_SPREAD | 7,429 | 19.7 | 13.4 | 28.4 | 20.8 | 12.4 | 4.4 | 1.1 | 7.85 | 17.8% | 5.4% |
| TOTAL_GAMES | 12,984 | 9.4 | 9.9 | 36.5 | 25.8 | 11.8 | 4.3 | 2.4 | 9.31 | 18.4% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 34,203 | 44.2% | 24.5% | 13.04 | 36.0% | 15.5% | 10.87 |
| gen1_elo | 34,203 | 44.0% | 24.2% | 12.86 | 35.7% | 15.5% | 10.68 |
| gen1_sr | 34,203 | 52.0% | 31.3% | 15.87 | 44.4% | 22.2% | 13.02 |
| gen2 | 34,203 | 51.2% | 31.7% | 15.5 | 44.5% | 23.9% | 13.04 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 17,036 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.3 | 10.71 | 35.3% | 15.2% |
| STALE | 17,167 | 10.4 | 6.9 | 15.9 | 13.9 | 19.3 | 17.8 | 15.9 | 16.34 | 53.0% | 33.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 18,473 | 16.3 | 11.1 | 22.5 | 15.3 | 17.7 | 12.2 | 4.8 | 10.02 | 34.7% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 59,208 | 18473 | 20508 | 20227 | 24.1 | 120.0 | 1400.4 |
| ge_15pp | 24,329 | 6414 | 7307 | 10608 | 26.3 | 418.6 | 1399.2 |
| ge_25pp | 12,981 | 3141 | 3185 | 6655 | 31.4 | 564.5 | 1380.4 |
| lt_10pp | 25,751 | 9223 | 9701 | 6827 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261027T130058Z-e5a91af6`: 760 priced rows, quote age at build {'median': 11.2, 'max': 11.2}, freshness {'AGING': 760}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 30 | 0.0 | 0.0 | 20.0 | 10.0 | 43.3 | 26.7 | 0.0 | 20.48 | 70.0% | 26.7% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,382 | 19.7 | 11.2 | 25.0 | 18.6 | 17.7 | 7.1 | 0.7 | 8.74 | 25.5% | 7.8% |
| KALSHI_LONE_OUTLIER | 22 | 4.5 | 4.5 | 77.3 | 4.5 | 4.5 | 4.5 | 0.0 | 6.16 | 9.1% | 4.5% |
| MARKETS_AGREE | 661 | 65.5 | 34.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,436 | 0.0 | 2.6 | 34.8 | 27.0 | 24.7 | 10.2 | 0.7 | 12.14 | 35.6% | 10.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 34,203 | 5549 (16.2%) | 25.9% | 0.9% | {"EXTERNAL_STALE": 3382, "AGREES_WITH_KALSHI": 1436, "ALL_AGREE": 661, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 22, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 15,116 | 1395 (9.2%) | 36.6% | 1.7% | {"EXTERNAL_STALE": 861, "AGREES_WITH_KALSHI": 511, "SUPPORTS_MODEL_DIRECTION": 21, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 8,378 | 427 (5.1%) | 36.5% | 2.1% | {"EXTERNAL_STALE": 262, "AGREES_WITH_KALSHI": 156, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,161 | 403 (9.7%) | 37.0% | 2.2% | {"EXTERNAL_STALE": 245, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 13,759 | 3132 (22.8%) | 17.2% | 0.8% | {"EXTERNAL_STALE": 1891, "ALL_AGREE": 661, "AGREES_WITH_KALSHI": 537, "AGREES_WITH_MODEL": 19, "EXTERNAL_OUTLIER": 18, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,567 | 10.4 | 7.6 | 19.3 | 14.8 | 22.3 | 16.0 | 9.7 | 14.08 | 47.9% | 25.7% |
| 4-10x | 4,451 | 11.0 | 8.4 | 18.6 | 15.2 | 22.3 | 14.8 | 9.7 | 13.91 | 46.7% | 24.5% |
| <2x | 17,494 | 15.2 | 10.1 | 19.4 | 16.4 | 17.3 | 12.9 | 8.7 | 11.57 | 39.0% | 21.6% |
| >=10x | 5,691 | 10.6 | 6.1 | 15.2 | 14.2 | 22.0 | 19.5 | 12.5 | 16.51 | 53.9% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,674 | 12.8 | 8.5 | 19.3 | 16.3 | 19.2 | 13.6 | 10.3 | 12.81 | 43.0% | 23.9% |
| 300-1000 | 7,134 | 11.9 | 8.8 | 17.3 | 15.3 | 20.8 | 16.3 | 9.7 | 13.81 | 46.7% | 26.0% |
| <300 | 11,153 | 8.3 | 5.7 | 15.4 | 14.7 | 23.4 | 20.1 | 12.4 | 17.02 | 55.8% | 32.5% |
| >=3000 | 7,242 | 21.2 | 13.5 | 23.8 | 16.3 | 13.7 | 7.0 | 4.5 | 7.67 | 25.1% | 11.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 961 | 0.551 | 0.4128 | 0.5036 | +0.047 | -0.091 | -0.0037 ± 0.005 |
| ratio 4-10x | 649 | 0.5865 | 0.4383 | 0.5008 | +0.086 | -0.062 | 0.008 ± 0.0064 |
| ratio <2x | 2360 | 0.5389 | 0.4157 | 0.447 | +0.092 | -0.031 | 0.0114 ± 0.003 |
| ratio >=10x | 867 | 0.5714 | 0.3947 | 0.4556 | +0.116 | -0.061 | 0.011 ± 0.0062 |
| thinner_sample 1000-3000 | 1304 | 0.5399 | 0.4133 | 0.4494 | +0.090 | -0.036 | 0.0093 ± 0.004 |
| thinner_sample 300-1000 | 1080 | 0.5689 | 0.4257 | 0.4926 | +0.076 | -0.067 | 0.0009 ± 0.0049 |
| thinner_sample <300 | 1639 | 0.5626 | 0.3941 | 0.4643 | +0.098 | -0.070 | 0.0094 ± 0.0044 |
| thinner_sample >=3000 | 814 | 0.5368 | 0.4421 | 0.4668 | +0.070 | -0.025 | 0.0119 ± 0.004 |
| data_status ADEQUATE | 1390 | 0.5372 | 0.4333 | 0.4504 | +0.087 | -0.017 | 0.0121 ± 0.0033 |
| data_status LIMITED | 1112 | 0.5506 | 0.4172 | 0.4874 | +0.063 | -0.070 | 0.0024 ± 0.0045 |
| data_status POOR | 2335 | 0.5646 | 0.4019 | 0.4672 | +0.097 | -0.065 | 0.008 ± 0.0036 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 708 | 0.2017 | 0.2023 | -0.0006 ± 0.0006 | 0.5842 | 0.5854 | 0.5012 | 0.4862 | 0.5127 | -0.083 ± 0.0179 | -0.01 (5) |
| 3-5 | 435 | 0.2041 | 0.2037 | +0.0004 ± 0.0017 | 0.5911 | 0.5886 | 0.5043 | 0.4643 | 0.4782 | -0.103 ± 0.0222 | 0.02 (1) |
| 5-10 | 998 | 0.2026 | 0.203 | -0.0004 ± 0.0021 | 0.5917 | 0.5904 | 0.5153 | 0.4414 | 0.477 | -0.089 ± 0.0147 | -0.0167 (6) |
| 10-15 | 845 | 0.2197 | 0.2104 | +0.0093 ± 0.0039 | 0.6318 | 0.6038 | 0.532 | 0.4081 | 0.4308 | -0.109 ± 0.0158 | -0.048 (5) |
| 15-25 | 1096 | 0.2254 | 0.2129 | +0.0126 ± 0.0054 | 0.6466 | 0.6097 | 0.5769 | 0.3811 | 0.4471 | -0.097 ± 0.014 | -0.0033 (9) |
| 25-40 | 626 | 0.2219 | 0.2098 | +0.0121 ± 0.0109 | 0.6331 | 0.6027 | 0.6553 | 0.3457 | 0.4792 | -0.071 ± 0.0167 | -0.01 (1) |
| 40+ | 129 | 0.2737 | 0.2 | +0.0737 ± 0.0341 | 0.7479 | 0.5853 | 0.7515 | 0.3013 | 0.4496 | -0.063 ± 0.0334 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3660 | 0.185 | 0.1857 | -0.0007 ± 0.0002 | 0.5459 | 0.5465 | 0.4887 | 0.4736 | 0.5008 | -0.028 ± 0.0072 | -0.0129 (17) |
| 3-5 | 2446 | 0.1986 | 0.1969 | +0.0016 ± 0.0007 | 0.5777 | 0.5713 | 0.4859 | 0.446 | 0.4444 | -0.058 ± 0.0091 | 0.0 (2) |
| 5-10 | 5189 | 0.2006 | 0.1972 | +0.0034 ± 0.0009 | 0.5867 | 0.5745 | 0.4856 | 0.4117 | 0.4247 | -0.049 ± 0.0062 | -0.0119 (21) |
| 10-15 | 4467 | 0.2 | 0.1824 | +0.0176 ± 0.0016 | 0.5863 | 0.5363 | 0.4899 | 0.3656 | 0.3566 | -0.073 ± 0.0064 | -0.0281 (16) |
| 15-25 | 5621 | 0.208 | 0.1692 | +0.0388 ± 0.0022 | 0.6093 | 0.5004 | 0.5024 | 0.3061 | 0.3065 | -0.072 ± 0.0055 | -0.0025 (44) |
| 25-40 | 4366 | 0.2222 | 0.1275 | +0.0947 ± 0.0034 | 0.6385 | 0.3908 | 0.5294 | 0.2162 | 0.2256 | -0.060 ± 0.0052 | -0.01 (1) |
| 40+ | 2823 | 0.3781 | 0.0481 | +0.3300 ± 0.0046 | 0.9843 | 0.1826 | 0.6312 | 0.1065 | 0.0673 | -0.075 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 554 | 0.2061 | 0.2068 | -0.0007 ± 0.0007 | 0.5938 | 0.5955 | 0.5082 | 0.493 | 0.5162 | -0.107 ± 0.0209 | -0.01 (3) |
| 3-5 | 396 | 0.2272 | 0.2242 | +0.0030 ± 0.0019 | 0.641 | 0.635 | 0.5096 | 0.4698 | 0.447 | -0.137 ± 0.0254 | 0.02 (1) |
| 5-10 | 867 | 0.2071 | 0.2067 | +0.0004 ± 0.0023 | 0.6004 | 0.599 | 0.5487 | 0.4737 | 0.5121 | -0.086 ± 0.016 | -0.01 (4) |
| 10-15 | 795 | 0.2189 | 0.2121 | +0.0068 ± 0.0041 | 0.6292 | 0.6104 | 0.5677 | 0.4433 | 0.4805 | -0.106 ± 0.0171 | -0.04 (5) |
| 15-25 | 1133 | 0.2316 | 0.2135 | +0.0182 ± 0.0054 | 0.6576 | 0.6105 | 0.5871 | 0.3919 | 0.4466 | -0.102 ± 0.014 | -0.0133 (9) |
| 25-40 | 793 | 0.2646 | 0.1989 | +0.0657 ± 0.0099 | 0.7399 | 0.5792 | 0.6529 | 0.3387 | 0.3934 | -0.120 ± 0.0157 | -0.0075 (4) |
| 40+ | 299 | 0.3591 | 0.1704 | +0.1886 ± 0.0237 | 0.9849 | 0.5103 | 0.736 | 0.2506 | 0.3144 | -0.075 ± 0.023 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3101 | 0.1932 | 0.1934 | -0.0002 ± 0.0003 | 0.5632 | 0.5633 | 0.51 | 0.495 | 0.5063 | -0.047 ± 0.0082 | -0.0133 (15) |
| 3-5 | 2084 | 0.2009 | 0.1996 | +0.0013 ± 0.0008 | 0.5806 | 0.5768 | 0.5114 | 0.4715 | 0.4741 | -0.052 ± 0.01 | 0.02 (1) |
| 5-10 | 4635 | 0.1979 | 0.1954 | +0.0026 ± 0.001 | 0.5819 | 0.5705 | 0.514 | 0.4399 | 0.4626 | -0.038 ± 0.0066 | -0.0117 (6) |
| 10-15 | 4020 | 0.2039 | 0.1916 | +0.0123 ± 0.0017 | 0.597 | 0.5572 | 0.5169 | 0.393 | 0.4062 | -0.055 ± 0.007 | -0.0189 (18) |
| 15-25 | 5584 | 0.2166 | 0.1794 | +0.0372 ± 0.0022 | 0.6294 | 0.5265 | 0.5255 | 0.33 | 0.3365 | -0.067 ± 0.0057 | -0.0086 (42) |
| 25-40 | 5100 | 0.2505 | 0.1375 | +0.1130 ± 0.0033 | 0.7054 | 0.4215 | 0.5568 | 0.2401 | 0.2224 | -0.084 ± 0.0052 | -0.0044 (18) |
| 40+ | 4048 | 0.3951 | 0.0609 | +0.3342 ± 0.0044 | 1.0391 | 0.2181 | 0.6521 | 0.1198 | 0.0855 | -0.072 ± 0.0038 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 679 | 0.1987 | 0.2008 | -0.0021 ± 0.0006 | 0.5777 | 0.5827 | 0.4998 | 0.4846 | 0.5464 | -0.035 ± 0.0179 | -0.0137 (8) |
| 3-5 | 477 | 0.2031 | 0.2018 | +0.0013 ± 0.0017 | 0.5894 | 0.5846 | 0.5057 | 0.466 | 0.4717 | -0.116 ± 0.0214 | 0.0067 (3) |
| 5-10 | 1023 | 0.204 | 0.2016 | +0.0023 ± 0.0021 | 0.5945 | 0.586 | 0.5132 | 0.4392 | 0.4594 | -0.099 ± 0.0144 | -0.0071 (7) |
| 10-15 | 837 | 0.2101 | 0.2058 | +0.0044 ± 0.0039 | 0.6101 | 0.5939 | 0.541 | 0.4175 | 0.4624 | -0.094 ± 0.0157 | -0.0317 (6) |
| 15-25 | 1038 | 0.2324 | 0.2153 | +0.0171 ± 0.0056 | 0.6633 | 0.6149 | 0.5879 | 0.3933 | 0.4461 | -0.110 ± 0.0144 | -0.03 (1) |
| 25-40 | 644 | 0.214 | 0.2169 | -0.0029 ± 0.0107 | 0.6173 | 0.619 | 0.6656 | 0.3551 | 0.5124 | -0.056 ± 0.0165 | 0.015 (2) |
| 40+ | 139 | 0.2866 | 0.208 | +0.0785 ± 0.0337 | 0.7882 | 0.6019 | 0.7575 | 0.3062 | 0.4532 | -0.062 ± 0.0353 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3578 | 0.1859 | 0.1866 | -0.0007 ± 0.0003 | 0.547 | 0.548 | 0.4866 | 0.4715 | 0.4916 | -0.033 ± 0.0073 | -0.0163 (35) |
| 3-5 | 2423 | 0.1985 | 0.1964 | +0.0021 ± 0.0007 | 0.5803 | 0.5734 | 0.4864 | 0.4468 | 0.4416 | -0.065 ± 0.0092 | -0.0094 (18) |
| 5-10 | 5343 | 0.1961 | 0.1915 | +0.0046 ± 0.0009 | 0.5762 | 0.56 | 0.4874 | 0.4133 | 0.4196 | -0.053 ± 0.006 | -0.01 (31) |
| 10-15 | 4336 | 0.1927 | 0.1772 | +0.0154 ± 0.0016 | 0.5696 | 0.5234 | 0.4995 | 0.376 | 0.3748 | -0.067 ± 0.0064 | -0.015 (12) |
| 15-25 | 5755 | 0.2112 | 0.1719 | +0.0393 ± 0.0021 | 0.6165 | 0.507 | 0.5132 | 0.3181 | 0.3157 | -0.074 ± 0.0055 | -0.03 (2) |
| 25-40 | 4361 | 0.2194 | 0.1312 | +0.0882 ± 0.0034 | 0.633 | 0.3989 | 0.5342 | 0.2185 | 0.2385 | -0.052 ± 0.0053 | 0.01 (3) |
| 40+ | 2776 | 0.391 | 0.0529 | +0.3381 ± 0.0049 | 1.0212 | 0.1952 | 0.6427 | 0.1132 | 0.0728 | -0.077 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1068 | 0.1968 | 0.1969 | -0.0001 ± 0.0005 | 0.5732 | 0.573 | 0.5019 | 0.4868 | 0.4906 | -0.067 ± 0.0138 | -0.0224 (49) |
| 3-5 | 742 | 0.1934 | 0.1927 | +0.0006 ± 0.0013 | 0.5641 | 0.5616 | 0.4936 | 0.4538 | 0.4636 | -0.062 ± 0.0165 | -0.0194 (34) |
| 5-10 | 1549 | 0.2025 | 0.1965 | +0.0059 ± 0.0017 | 0.5951 | 0.5755 | 0.4974 | 0.4239 | 0.4216 | -0.078 ± 0.0115 | -0.005 (78) |
| 10-15 | 1049 | 0.2118 | 0.2004 | +0.0114 ± 0.0034 | 0.6149 | 0.5835 | 0.5279 | 0.405 | 0.4185 | -0.073 ± 0.0141 | 0.0014 (64) |
| 15-25 | 1384 | 0.2318 | 0.211 | +0.0208 ± 0.0048 | 0.6611 | 0.6069 | 0.5795 | 0.3847 | 0.4306 | -0.077 ± 0.0124 | -0.0214 (59) |
| 25-40 | 850 | 0.2428 | 0.2097 | +0.0330 ± 0.0096 | 0.693 | 0.6015 | 0.6779 | 0.3657 | 0.4682 | -0.085 ± 0.0146 | -0.0219 (26) |
| 40+ | 281 | 0.3422 | 0.1984 | +0.1438 ± 0.026 | 0.9866 | 0.5817 | 0.8062 | 0.3257 | 0.4342 | -0.093 ± 0.0238 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3597 | 0.1826 | 0.1827 | -0.0001 ± 0.0002 | 0.5376 | 0.5371 | 0.5033 | 0.488 | 0.4957 | -0.043 ± 0.0072 | -0.0157 (88) |
| 3-5 | 2519 | 0.1963 | 0.1943 | +0.0020 ± 0.0007 | 0.5705 | 0.5663 | 0.504 | 0.4642 | 0.4593 | -0.056 ± 0.0089 | -0.0209 (69) |
| 5-10 | 5031 | 0.1979 | 0.1897 | +0.0082 ± 0.0009 | 0.5832 | 0.5576 | 0.4929 | 0.4193 | 0.4029 | -0.073 ± 0.0062 | -0.0082 (132) |
| 10-15 | 3542 | 0.2083 | 0.1928 | +0.0154 ± 0.0018 | 0.6072 | 0.5649 | 0.5297 | 0.4069 | 0.4046 | -0.066 ± 0.0074 | -0.0053 (105) |
| 15-25 | 4339 | 0.2305 | 0.2002 | +0.0303 ± 0.0027 | 0.6641 | 0.5796 | 0.5683 | 0.3727 | 0.3943 | -0.067 ± 0.0068 | -0.0253 (107) |
| 25-40 | 2963 | 0.2579 | 0.1859 | +0.0720 ± 0.005 | 0.7311 | 0.5423 | 0.6334 | 0.3201 | 0.3642 | -0.076 ± 0.0077 | -0.0229 (51) |
| 40+ | 1293 | 0.3717 | 0.1467 | +0.2250 ± 0.0111 | 1.05 | 0.4424 | 0.7278 | 0.2258 | 0.266 | -0.067 ± 0.0099 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4837 | 1.029 ± 0.04 | 1.096 | 0.1677 | 0.1635 | 0.2152 | 0.2073 |
| gen2 | 4837 | 0.816 ± 0.037 | 1.058 | 0.1687 | 0.164 | 0.2352 | 0.2071 |
| gen1_elo | 4837 | 1.004 ± 0.039 | 1.097 | 0.1741 | 0.1636 | 0.214 | 0.2074 |
| gen1_sr | 4837 | 0.997 ± 0.048 | 1.12 | 0.1293 | 0.1659 | 0.2312 | 0.2067 |
| gen1_ledger | 6923 | 0.861 ± 0.029 | 1.061 | 0.1838 | 0.1766 | 0.2185 | 0.2014 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 24,329)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 5,349 | 22.0% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,343 | 22.0% |
| BOOK_QUALITY | execution | 4,713 | 19.4% |
| POOR_DATA | data | 2,795 | 11.5% |
| LIMITED_DATA | data | 1,513 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,312 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,146 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 1,030 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 697 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 430 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 22.0%, coverage 22.0%, execution 19.4%, data 17.7%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.0%, LOW_DATA_QUALITY 71.1%, THIN_PLAYER_HISTORY 60.2%, STALE_PLAYER_DATA 51.3%, STALE_KALSHI_QUOTE 43.6%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 25.5%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 16.3%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.4%, POST_SETTLEMENT_OBSERVATION 22.0%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 12,981)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,296 | 33.1% |
| BOOK_QUALITY | execution | 2,479 | 19.1% |
| STALE_QUOTE | market_freshness | 2,464 | 19.0% |
| POOR_DATA | data | 1,175 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 705 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 568 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 446 | 3.4% |
| LIMITED_DATA | data | 445 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 296 | 2.3% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 106 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.1%, execution 19.1%, market_freshness 19.0%, data 12.5%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.3%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.7%, LOW_DATA_QUALITY 74.6%, THIN_PLAYER_HISTORY 62.5%, STALE_KALSHI_QUOTE 51.3%, STALE_PLAYER_DATA 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.9%, WIDE_SPREAD 25.1%, PLAYER_IDENTITY_RISK 19.6%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 9.4%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.1%, POST_SETTLEMENT_OBSERVATION 33.1%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 10130, "IDENTITY_AMBIGUOUS": 2851}; ticker orientation: {"VERIFIED": 12981}.

Checks: discipline:AMBIGUOUS 870, discipline:PASS 12111, identity_confidence:AMBIGUOUS 2543, identity_confidence:PASS 10438, level_mapping:NA 882, level_mapping:PASS 12099, market_pair:AMBIGUOUS 466, market_pair:NA 310, market_pair:PASS 12205, model_complement:NA 275, model_complement:PASS 12706, namesake:AMBIGUOUS 6, namesake:PASS 12975, physical_match_id:NA 4603, physical_match_id:PASS 8378, player_ids:PASS 12981, same_pair_other_event:PASS 12981, ticker_orientation:PASS 12981

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,016 | 4.5% | 4.0% | 1.7% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 26, "execution": 24, "market_freshness/coverage": 15, "coverage": 13} | 5.86 | 0.2217 / 0.2194 (561) | 20.7% | 3.1% | 3.3% | 2.6% |
| CHALLENGER | 9,167 | 16.6% | 6.6% | 11.7% | {"coverage": 858, "market_freshness/coverage": 184, "market_freshness": 166, "data": 144, "model_calibration_or_unknown": 76, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.48 | 0.2189 / 0.2094 (2123) | 34.4% | 16.6% | 4.1% | 21.9% |
| DOUBLES | 1,839 | 47.3% | 47.0% | 6.7% | {"execution": 484, "mapping": 218, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.85 | 0.3098 / 0.2362 (444) | 12.7% | 0.0% | 100.0% | 6.5% |
| ITF_MEN | 15,964 | 25.7% | 18.3% | 31.6% | {"coverage": 1456, "execution": 797, "market_freshness": 725, "data": 577, "market_freshness/coverage": 363, "mapping": 182, "model_calibration": 4, "model_calibration_or_unknown": 2} | 12.09 | 0.2168 / 0.1985 (3445) | 37.0% | 70.4% | 19.0% | 21.6% |
| ITF_WOMEN | 21,624 | 27.0% | 20.0% | 44.9% | {"coverage": 1935, "market_freshness": 1284, "execution": 1085, "data": 812, "market_freshness/coverage": 481, "mapping": 145, "model_calibration_or_unknown": 73, "model_calibration": 12} | 12.85 | 0.2044 / 0.1971 (4028) | 39.1% | 57.9% | 10.3% | 21.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,574 | 5.7% | 5.1% | 1.6% | {"market_freshness": 72, "model_calibration_or_unknown": 42, "execution": 27, "data": 19, "model_calibration": 16, "coverage": 14, "market_freshness/coverage": 11, "mapping": 1} | 7.67 | 0.2327 / 0.2271 (573) | 25.3% | 1.2% | 1.5% | 3.3% |
| WTA125 | 1,869 | 12.0% | 9.9% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 48, "market_freshness/coverage": 41, "data": 32, "execution": 21, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.44 | 0.2162 / 0.2022 (544) | 25.1% | 11.6% | 5.7% | 7.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 37 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 38 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 39 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 40 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 42 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 43 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 44 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 45 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 47 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 48 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 49 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 50 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9673, "by_level_share_of_ge_25pp": {"ATP": 0.0172, "CHALLENGER": 0.1169, "DOUBLES": 0.067, "ITF_MEN": 0.3163, "ITF_WOMEN": 0.4489, "OTHER": 0.0009, "WTA": 0.0156, "WTA125": 0.0173}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5127, "share_primary_cause_market_settled_or_in_play": 0.4196, "share_primary_cause_stale_quote_only": 0.1898}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 12981, "identity_ambiguous_share": 0.2196, "ticker_orientation": {"VERIFIED": 12981}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 8378, "with_external": 427, "coverage": 0.051, "external_status": {"EXTERNAL_STALE": 262, "AGREES_WITH_KALSHI": 156, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 262, "MODEL_LONE_OUTLIER": 156, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3653, "share_external_supports_model": 0.0211}, "pregame_clean_ge_25pp": {"n": 4161, "with_external": 403, "coverage": 0.0969, "external_status": {"EXTERNAL_STALE": 245, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 245, "MODEL_LONE_OUTLIER": 149, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3697, "share_external_supports_model": 0.0223}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 459.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 237.0, "share_severe_asymmetry": 0.2163, "data_status": {"POOR": 7333, "LIMITED": 3312, "ADEQUATE": 2336}, "comparison_lt_10pp": {"median_thinner_serve_points": 1774.0, "median_sample_ratio": 1.67, "median_min_matches": 96.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 961, "model_minus_observed": 0.0474, "kalshi_minus_observed": -0.0909, "brier_diff_model_minus_kalshi": -0.0037}, "4-10x": {"n": 649, "model_minus_observed": 0.0858, "kalshi_minus_observed": -0.0625, "brier_diff_model_minus_kalshi": 0.008}, "<2x": {"n": 2360, "model_minus_observed": 0.0919, "kalshi_minus_observed": -0.0313, "brier_diff_model_minus_kalshi": 0.0114}, ">=10x": {"n": 867, "model_minus_observed": 0.1158, "kalshi_minus_observed": -0.0608, "brier_diff_model_minus_kalshi": 0.011}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4837, "model": {"intercept": -0.536, "slope": 0.816, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.194, "slope": 1.058, "slope_se": 0.041}, "mean_extremity_model": 0.1687, "mean_extremity_kalshi": 0.164, "model_brier": 0.2352, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.028, "brier_diff_se": 0.0027, "model_logloss": 0.6677, "kalshi_logloss": 0.5974}, "fair_v1": {"n": 4837, "model": {"intercept": -0.419, "slope": 1.029, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.28, "slope": 1.096, "slope_se": 0.042}, "mean_extremity_model": 0.1677, "mean_extremity_kalshi": 0.1635, "model_brier": 0.2152, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.0079, "brier_diff_se": 0.0022, "model_logloss": 0.6195, "kalshi_logloss": 0.5977}, "gen1_elo": {"n": 4837, "model": {"intercept": -0.391, "slope": 1.004, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.305, "slope": 1.097, "slope_se": 0.041}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1636, "model_brier": 0.214, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.0066, "brier_diff_se": 0.0023, "model_logloss": 0.6177, "kalshi_logloss": 0.5978}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2449, "share_ge_15": 0.4419, "median_abs_gap": 13.04, "n": 34203}, "gen1_elo": {"share_ge_25": 0.2421, "share_ge_15": 0.4402, "median_abs_gap": 12.86, "n": 34203}, "gen1_sr": {"share_ge_25": 0.313, "share_ge_15": 0.5202, "median_abs_gap": 15.87, "n": 34203}, "gen2": {"share_ge_25": 0.3169, "share_ge_15": 0.5117, "median_abs_gap": 15.5, "n": 34203}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1552, "share_ge_15": 0.3598, "median_abs_gap": 10.87, "n": 26815}, "gen1_elo": {"share_ge_25": 0.1551, "share_ge_15": 0.3569, "median_abs_gap": 10.68, "n": 26812}, "gen1_sr": {"share_ge_25": 0.2225, "share_ge_15": 0.4443, "median_abs_gap": 13.02, "n": 26816}, "gen2": {"share_ge_25": 0.2389, "share_ge_15": 0.4452, "median_abs_gap": 13.04, "n": 26817}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0445, "share_ge_25_pregame_clean": 0.0399}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.0565, "share_ge_25_pregame_clean": 0.0512}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2358, "share_within_10pp_all": 0.4349, "share_within_10pp_pregame_clean": 0.4855, "corr_model_vs_mid_pregame_clean": 0.8442}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 708, "model_brier": 0.2017, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": -0.0006}, "10-15": {"n_settled": 845, "model_brier": 0.2197, "kalshi_brier": 0.2104, "brier_diff_model_minus_kalshi": 0.0093}, "15-25": {"n_settled": 1096, "model_brier": 0.2254, "kalshi_brier": 0.2129, "brier_diff_model_minus_kalshi": 0.0126}, "25-40": {"n_settled": 626, "model_brier": 0.2219, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.0121}, "3-5": {"n_settled": 435, "model_brier": 0.2041, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 129, "model_brier": 0.2737, "kalshi_brier": 0.2, "brier_diff_model_minus_kalshi": 0.0737}, "5-10": {"n_settled": 998, "model_brier": 0.2026, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": -0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.536, "slope": 0.816, "slope_se": 0.037}, "kalshi_slope": {"intercept": 0.194, "slope": 1.058, "slope_se": 0.041}, "n": 4837}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.495, "slope": 0.861, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.16, "slope": 1.061, "slope_se": 0.033}, "n": 6923}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 444, "model_brier": 0.3098, "kalshi_brier": 0.2362, "brier_diff_model_minus_kalshi": 0.0736, "brier_diff_se": 0.0143, "corr_model_outcome": 0.0396, "corr_kalshi_outcome": 0.2498}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
