# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-27T19:16Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 61,091): 0-3 14.0%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 19.1%, 25-40 14.0%, 40+ 8.0%; median gap 11.97 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.7%, Challenger 11.7%, doubles 6.6%). Main tour: ATP 4.4% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 13,439): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.4%, BOOK_QUALITY 18.9%, STALE_QUOTE 18.8%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.4%, execution 18.9%, market_freshness 18.8%, data 12.7%, market_freshness/coverage 8.9%, mapping 4.3%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 13,439 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.1%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 458.0 points vs 1759.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.026, Gen-2 0.812, Gen-1 ledger 0.859 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 636 model 0.2229 vs Kalshi 0.209; n 134 model 0.2706 vs Kalshi 0.2006.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 266,165 model-market comparisons (431,382 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 88,917 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-27T18:58:20.417124+00:00'], shadow board 70,157 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-27T18:58:25.596583+00:00'], Model 4 34,330 rows, 21,929 settled tickers, 7,858 tickers with an external scan.
* By model: {"gen1_ledger": 60465, "gen1_elo": 35275, "fair_v1": 35275, "gen2": 35275, "gen1_sr": 35275, "model4_fundamental": 32322, "model4_conditioned": 32278}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 61,091 | 14.0 | 9.6 | 19.9 | 15.4 | 19.1 | 14.0 | 8.0 | 11.97 | 41.1% | 22.0% |
| MW fair_v1 | 35,275 | 12.9 | 8.7 | 18.5 | 15.6 | 19.6 | 14.9 | 9.7 | 13.07 | 44.3% | 24.7% |
| MW gen1_elo | 35,275 | 12.8 | 8.5 | 19.3 | 15.4 | 19.6 | 14.8 | 9.6 | 12.89 | 44.0% | 24.4% |
| MW gen1_ledger | 25,816 | 15.6 | 10.7 | 21.8 | 15.2 | 18.5 | 12.7 | 5.7 | 10.48 | 36.8% | 18.3% |
| MW gen1_sr | 35,275 | 10.2 | 7.2 | 16.9 | 13.5 | 20.8 | 18.7 | 12.8 | 15.95 | 52.2% | 31.4% |
| MW gen2 | 35,275 | 11.1 | 7.5 | 16.3 | 13.8 | 19.5 | 17.9 | 13.9 | 15.55 | 51.3% | 31.8% |
| all families model4_conditioned | 32,278 | 22.1 | 18.2 | 34.5 | 17.4 | 4.9 | 1.9 | 1.1 | 6.05 | 7.8% | 3.0% |
| all families model4_fundamental | 32,322 | 17.0 | 13.2 | 34.1 | 20.4 | 10.2 | 3.7 | 1.4 | 7.76 | 15.3% | 5.1% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.5%, >=15pp 41.1%, >=20pp 30.5%, >=25pp 22.0%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.35pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,214 | 27.0 | 15.6 | 27.0 | 13.9 | 11.5 | 4.2 | 0.6 | 5.93 | 16.4% | 4.9% |
| CHALLENGER | 5,585 | 16.0 | 9.9 | 20.1 | 15.7 | 15.5 | 12.0 | 10.7 | 11.09 | 38.2% | 22.7% |
| ITF_MEN | 9,456 | 9.9 | 7.2 | 16.4 | 14.9 | 21.6 | 17.7 | 12.3 | 15.53 | 51.5% | 29.9% |
| ITF_WOMEN | 13,746 | 9.6 | 7.0 | 15.9 | 15.2 | 22.2 | 18.4 | 11.8 | 15.74 | 52.4% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,294 | 17.0 | 13.9 | 24.9 | 20.4 | 16.6 | 6.6 | 0.6 | 8.39 | 23.8% | 7.1% |
| WTA125 | 974 | 15.1 | 7.2 | 23.2 | 19.7 | 20.7 | 12.3 | 1.8 | 11.03 | 34.8% | 14.1% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,214 | 25.4 | 15.4 | 25.3 | 16.9 | 11.9 | 4.3 | 0.8 | 6.31 | 17.0% | 5.1% |
| CHALLENGER | 5,585 | 15.1 | 8.8 | 17.9 | 14.7 | 18.1 | 13.9 | 11.6 | 12.75 | 43.6% | 25.5% |
| ITF_MEN | 9,456 | 7.9 | 6.0 | 14.2 | 12.9 | 19.9 | 21.2 | 17.8 | 18.82 | 59.0% | 39.0% |
| ITF_WOMEN | 13,746 | 8.0 | 5.6 | 13.9 | 12.8 | 20.6 | 21.4 | 17.6 | 19.32 | 59.7% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,294 | 14.5 | 10.7 | 22.2 | 15.8 | 22.4 | 12.9 | 1.5 | 10.79 | 36.8% | 14.3% |
| WTA125 | 974 | 8.2 | 6.1 | 17.0 | 17.0 | 24.7 | 18.1 | 8.8 | 15.8 | 51.6% | 26.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,214 | 22.7 | 12.6 | 24.7 | 16.1 | 16.1 | 6.5 | 1.4 | 7.58 | 24.0% | 7.9% |
| CHALLENGER | 5,585 | 14.6 | 9.1 | 21.3 | 16.0 | 15.8 | 12.3 | 10.9 | 11.34 | 39.1% | 23.3% |
| ITF_MEN | 9,456 | 9.6 | 7.0 | 16.7 | 14.1 | 22.1 | 18.1 | 12.4 | 15.99 | 52.5% | 30.5% |
| ITF_WOMEN | 13,746 | 9.3 | 6.7 | 16.4 | 15.9 | 22.4 | 18.1 | 11.1 | 15.52 | 51.6% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,294 | 23.7 | 16.3 | 31.7 | 15.1 | 9.7 | 2.5 | 1.1 | 6.08 | 13.2% | 3.6% |
| WTA125 | 974 | 22.5 | 12.1 | 26.8 | 16.5 | 15.2 | 6.5 | 0.4 | 7.99 | 22.1% | 6.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,872 | 24.6 | 19.1 | 30.7 | 12.8 | 9.1 | 3.1 | 0.5 | 5.74 | 12.8% | 3.7% |
| CHALLENGER | 3,828 | 22.1 | 14.4 | 26.9 | 14.8 | 14.0 | 6.2 | 1.6 | 7.25 | 21.8% | 7.8% |
| DOUBLES | 1,868 | 5.1 | 4.5 | 12.1 | 10.5 | 20.6 | 25.3 | 21.8 | 23.85 | 67.7% | 47.1% |
| ITF_MEN | 7,144 | 12.9 | 9.0 | 20.2 | 16.0 | 21.8 | 13.8 | 6.3 | 12.27 | 41.9% | 20.1% |
| ITF_WOMEN | 8,610 | 12.9 | 8.8 | 19.5 | 15.4 | 21.3 | 16.2 | 5.9 | 12.61 | 43.3% | 22.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,358 | 23.8 | 15.5 | 30.1 | 17.8 | 9.6 | 3.0 | 0.3 | 6.8 | 12.8% | 3.2% |
| WTA125 | 987 | 23.6 | 13.1 | 21.0 | 18.6 | 13.9 | 8.0 | 1.8 | 8.14 | 23.7% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,129 | 27.3 | 15.8 | 27.4 | 13.8 | 11.4 | 3.9 | 0.4 | 5.91 | 15.7% | 4.3% |
| CHALLENGER | 3,944 | 20.9 | 12.4 | 25.0 | 18.2 | 15.5 | 6.4 | 1.6 | 8.29 | 23.4% | 8.0% |
| ITF_MEN | 6,991 | 12.0 | 8.6 | 19.7 | 16.9 | 22.8 | 14.5 | 5.5 | 12.84 | 42.8% | 20.0% |
| ITF_WOMEN | 10,355 | 11.3 | 8.2 | 18.2 | 17.3 | 24.1 | 15.4 | 5.4 | 13.52 | 45.0% | 20.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,226 | 17.2 | 13.8 | 25.0 | 20.6 | 16.6 | 6.1 | 0.6 | 8.32 | 23.3% | 6.7% |
| WTA125 | 942 | 15.4 | 7.0 | 22.9 | 20.0 | 21.2 | 12.0 | 1.5 | 11.03 | 34.7% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,129 | 25.7 | 15.8 | 25.4 | 16.8 | 11.9 | 4.0 | 0.5 | 6.23 | 16.3% | 4.4% |
| CHALLENGER | 3,944 | 19.4 | 11.1 | 22.3 | 17.2 | 18.5 | 9.6 | 1.9 | 9.2 | 29.9% | 11.5% |
| ITF_MEN | 6,992 | 9.3 | 7.2 | 16.5 | 14.9 | 21.8 | 19.4 | 10.9 | 15.66 | 52.1% | 30.2% |
| ITF_WOMEN | 10,356 | 9.0 | 6.4 | 15.5 | 14.3 | 22.6 | 20.9 | 11.1 | 16.89 | 54.7% | 32.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,226 | 14.6 | 10.7 | 22.3 | 15.8 | 22.6 | 12.7 | 1.3 | 10.77 | 36.6% | 14.0% |
| WTA125 | 942 | 8.2 | 6.0 | 17.2 | 17.3 | 24.7 | 18.4 | 8.2 | 15.66 | 51.3% | 26.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,819 | 24.7 | 19.4 | 30.7 | 13.0 | 8.7 | 3.0 | 0.4 | 5.67 | 12.2% | 3.5% |
| CHALLENGER | 3,378 | 23.4 | 15.3 | 28.1 | 14.9 | 13.4 | 4.3 | 0.4 | 6.69 | 18.1% | 4.7% |
| DOUBLES | 1,748 | 5.1 | 4.6 | 12.4 | 10.6 | 20.5 | 25.2 | 21.6 | 23.73 | 67.3% | 46.8% |
| ITF_MEN | 6,064 | 13.9 | 9.6 | 21.8 | 16.7 | 21.8 | 12.2 | 4.0 | 11.42 | 38.0% | 16.2% |
| ITF_WOMEN | 7,276 | 13.6 | 9.3 | 20.8 | 16.2 | 21.4 | 15.1 | 3.7 | 11.75 | 40.1% | 18.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,304 | 24.2 | 15.9 | 30.1 | 17.8 | 9.6 | 2.3 | 0.1 | 6.68 | 12.0% | 2.4% |
| WTA125 | 868 | 25.2 | 13.9 | 22.1 | 19.8 | 12.7 | 5.7 | 0.6 | 7.33 | 18.9% | 6.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,868 | 5.1 | 4.5 | 12.1 | 10.5 | 20.6 | 25.3 | 21.8 | 23.85 | 67.7% | 47.1% |
| singles | 23,948 | 16.4 | 11.2 | 22.5 | 15.5 | 18.3 | 11.7 | 4.4 | 9.97 | 34.4% | 16.1% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,482 | 12.9 | 9.3 | 19.9 | 15.8 | 19.0 | 13.9 | 9.2 | 12.51 | 42.1% | 23.1% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 22,592 | 13.4 | 8.8 | 18.3 | 15.3 | 19.5 | 15.1 | 9.6 | 13.02 | 44.2% | 24.7% |
| UNKNOWN | 4,952 | 10.7 | 7.3 | 17.1 | 16.8 | 21.0 | 16.0 | 11.1 | 14.16 | 48.1% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,134 | 19.7 | 12.4 | 22.1 | 16.1 | 14.8 | 9.2 | 5.8 | 8.74 | 29.8% | 15.0% |
| B | 4,338 | 12.6 | 8.6 | 19.0 | 16.5 | 19.5 | 12.9 | 10.8 | 12.75 | 43.2% | 23.7% |
| C | 4,872 | 11.8 | 8.9 | 19.6 | 16.0 | 19.2 | 14.4 | 10.1 | 12.98 | 43.7% | 24.5% |
| D | 5,391 | 12.3 | 8.1 | 17.4 | 15.4 | 21.4 | 15.8 | 9.7 | 13.83 | 46.8% | 25.4% |
| F | 10,540 | 7.3 | 5.5 | 14.9 | 14.6 | 23.6 | 21.2 | 12.9 | 17.95 | 57.7% | 34.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,237 | 23.9 | 15.9 | 28.7 | 15.1 | 11.1 | 3.9 | 1.4 | 6.53 | 16.4% | 5.2% |
| B | 3,515 | 16.7 | 10.1 | 24.1 | 16.2 | 19.4 | 10.1 | 3.4 | 9.81 | 32.9% | 13.5% |
| C | 4,936 | 11.0 | 7.4 | 19.1 | 14.6 | 21.2 | 16.1 | 10.6 | 14.05 | 47.9% | 26.7% |
| D | 3,618 | 14.3 | 9.9 | 20.6 | 15.6 | 20.5 | 13.4 | 5.7 | 11.58 | 39.7% | 19.1% |
| F | 6,510 | 9.8 | 8.2 | 15.5 | 15.0 | 22.8 | 20.8 | 7.9 | 15.82 | 51.6% | 28.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,502 | 18.0 | 11.2 | 21.2 | 15.8 | 15.2 | 10.1 | 8.5 | 9.92 | 33.8% | 18.5% |
| LIMITED | 7,489 | 13.7 | 10.0 | 20.0 | 16.5 | 19.5 | 13.2 | 7.2 | 11.91 | 39.9% | 20.4% |
| POOR | 16,284 | 9.0 | 6.4 | 15.9 | 14.9 | 22.8 | 19.2 | 11.8 | 16.27 | 53.8% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,070 | 24.4 | 18.5 | 33.3 | 14.6 | 6.3 | 2.6 | 0.3 | 5.76 | 9.2% | 2.9% |
| GAME_SPREAD | 5,576 | 22.2 | 15.4 | 33.1 | 16.8 | 9.1 | 2.8 | 0.5 | 6.72 | 12.4% | 3.3% |
| MATCH_WINNER | 25,816 | 15.6 | 10.7 | 21.8 | 15.2 | 18.5 | 12.7 | 5.7 | 10.48 | 36.8% | 18.3% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,796 | 27.7 | 16.5 | 31.1 | 12.6 | 9.3 | 2.4 | 0.3 | 5.68 | 12.1% | 2.8% |
| TOTAL_GAMES | 9,183 | 9.2 | 10.1 | 36.1 | 27.1 | 10.6 | 4.0 | 2.8 | 9.36 | 17.4% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,498 | 24.5 | 30.6 | 32.9 | 7.0 | 4.0 | 0.8 | 0.2 | 4.67 | 5.0% | 1.0% |
| GAME_SPREAD | 7,558 | 46.8 | 16.4 | 25.7 | 7.4 | 1.9 | 1.2 | 0.6 | 3.31 | 3.7% | 1.8% |
| TOTAL_GAMES | 13,222 | 5.8 | 8.5 | 40.9 | 32.1 | 7.3 | 3.1 | 2.2 | 9.43 | 12.7% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,509 | 23.8 | 16.9 | 35.0 | 14.3 | 7.2 | 2.5 | 0.4 | 6.02 | 10.1% | 2.9% |
| GAME_SPREAD | 7,561 | 19.8 | 13.4 | 28.4 | 20.6 | 12.3 | 4.4 | 1.1 | 7.84 | 17.8% | 5.5% |
| TOTAL_GAMES | 13,252 | 9.4 | 9.9 | 36.6 | 25.6 | 11.7 | 4.3 | 2.4 | 9.28 | 18.4% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 35,275 | 44.3% | 24.7% | 13.07 | 35.9% | 15.5% | 10.86 |
| gen1_elo | 35,275 | 44.0% | 24.4% | 12.89 | 35.6% | 15.5% | 10.67 |
| gen1_sr | 35,275 | 52.2% | 31.4% | 15.95 | 44.6% | 22.2% | 13.03 |
| gen2 | 35,275 | 51.3% | 31.8% | 15.55 | 44.6% | 23.9% | 13.06 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 17,538 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.3 | 10.72 | 35.3% | 15.2% |
| STALE | 17,737 | 10.3 | 6.9 | 15.8 | 13.8 | 19.1 | 18.0 | 16.1 | 16.44 | 53.2% | 34.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 19,284 | 16.4 | 11.1 | 22.5 | 15.3 | 17.8 | 12.2 | 4.8 | 10.02 | 34.8% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 61,091 | 19284 | 21010 | 20797 | 24.1 | 119.8 | 1400.4 |
| ge_15pp | 25,128 | 6701 | 7487 | 10940 | 26.6 | 419.8 | 1399.2 |
| ge_25pp | 13,439 | 3272 | 3263 | 6904 | 31.2 | 569.9 | 1380.4 |
| lt_10pp | 26,554 | 9629 | 9936 | 6989 | 22.4 | 47.1 | 1341.5 |

Current slate `SL-20261027T191631Z-26644360`: 704 priced rows, quote age at build {'median': 18.7, 'max': 18.8}, freshness {'AGING': 704}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 38 | 0.0 | 0.0 | 31.6 | 7.9 | 39.5 | 21.1 | 0.0 | 20.05 | 60.5% | 21.1% |
| EXTERNAL_LONE_OUTLIER | 19 | 79.0 | 21.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,469 | 19.9 | 11.2 | 24.9 | 18.3 | 17.8 | 7.1 | 0.7 | 8.71 | 25.7% | 7.8% |
| KALSHI_LONE_OUTLIER | 22 | 4.5 | 4.5 | 77.3 | 4.5 | 4.5 | 4.5 | 0.0 | 6.16 | 9.1% | 4.5% |
| MARKETS_AGREE | 681 | 65.0 | 35.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.23 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,481 | 0.0 | 2.5 | 35.0 | 26.9 | 24.9 | 10.1 | 0.7 | 12.22 | 35.6% | 10.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 35,275 | 5710 (16.2%) | 25.9% | 1.0% | {"EXTERNAL_STALE": 3469, "AGREES_WITH_KALSHI": 1481, "ALL_AGREE": 681, "SUPPORTS_MODEL_DIRECTION": 37, "AGREES_WITH_MODEL": 22, "EXTERNAL_OUTLIER": 19, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 15,628 | 1444 (9.2%) | 36.6% | 1.7% | {"EXTERNAL_STALE": 891, "AGREES_WITH_KALSHI": 528, "SUPPORTS_MODEL_DIRECTION": 23, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 8,705 | 441 (5.1%) | 36.3% | 2.0% | {"EXTERNAL_STALE": 272, "AGREES_WITH_KALSHI": 160, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,277 | 417 (9.8%) | 36.7% | 2.2% | {"EXTERNAL_STALE": 255, "AGREES_WITH_KALSHI": 153, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 14,156 | 3228 (22.8%) | 17.2% | 0.9% | {"EXTERNAL_STALE": 1942, "ALL_AGREE": 681, "AGREES_WITH_KALSHI": 555, "EXTERNAL_OUTLIER": 19, "AGREES_WITH_MODEL": 19, "SUPPORTS_MODEL_DIRECTION": 11, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,799 | 10.4 | 7.5 | 19.3 | 14.7 | 22.0 | 16.3 | 9.8 | 14.09 | 48.1% | 26.1% |
| 4-10x | 4,623 | 11.1 | 8.5 | 18.6 | 15.4 | 21.9 | 14.7 | 9.8 | 13.76 | 46.4% | 24.6% |
| <2x | 18,029 | 15.1 | 10.1 | 19.2 | 16.4 | 17.4 | 13.1 | 8.7 | 11.65 | 39.2% | 21.8% |
| >=10x | 5,824 | 10.6 | 6.1 | 15.2 | 14.2 | 22.0 | 19.4 | 12.6 | 16.48 | 53.9% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,916 | 12.8 | 8.5 | 19.2 | 16.3 | 19.2 | 13.5 | 10.4 | 12.82 | 43.1% | 23.9% |
| 300-1000 | 7,391 | 11.9 | 8.8 | 17.4 | 15.3 | 20.5 | 16.5 | 9.7 | 13.8 | 46.7% | 26.2% |
| <300 | 11,512 | 8.3 | 5.7 | 15.3 | 14.8 | 23.2 | 20.1 | 12.6 | 17.09 | 55.9% | 32.7% |
| >=3000 | 7,456 | 21.1 | 13.6 | 23.7 | 16.1 | 13.8 | 7.2 | 4.6 | 7.67 | 25.5% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 989 | 0.5508 | 0.4132 | 0.5035 | +0.047 | -0.090 | -0.0038 ± 0.0049 |
| ratio 4-10x | 672 | 0.5854 | 0.4377 | 0.494 | +0.091 | -0.056 | 0.0096 ± 0.0062 |
| ratio <2x | 2428 | 0.538 | 0.415 | 0.4485 | +0.089 | -0.034 | 0.011 ± 0.0029 |
| ratio >=10x | 883 | 0.57 | 0.3934 | 0.4541 | +0.116 | -0.061 | 0.0117 ± 0.0062 |
| thinner_sample 1000-3000 | 1340 | 0.5387 | 0.4123 | 0.4507 | +0.088 | -0.038 | 0.0083 ± 0.0039 |
| thinner_sample 300-1000 | 1102 | 0.5695 | 0.4266 | 0.4927 | +0.077 | -0.066 | 0.0012 ± 0.0049 |
| thinner_sample <300 | 1690 | 0.561 | 0.3932 | 0.4627 | +0.098 | -0.070 | 0.0096 ± 0.0043 |
| thinner_sample >=3000 | 840 | 0.5359 | 0.4414 | 0.4655 | +0.070 | -0.024 | 0.0129 ± 0.004 |
| data_status ADEQUATE | 1417 | 0.5369 | 0.4333 | 0.451 | +0.086 | -0.018 | 0.0124 ± 0.0033 |
| data_status LIMITED | 1155 | 0.549 | 0.4157 | 0.4848 | +0.064 | -0.069 | 0.0027 ± 0.0044 |
| data_status POOR | 2400 | 0.5636 | 0.4015 | 0.4671 | +0.097 | -0.066 | 0.0079 ± 0.0036 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 728 | 0.2004 | 0.2009 | -0.0005 ± 0.0006 | 0.5809 | 0.5821 | 0.5019 | 0.487 | 0.5124 | -0.085 ± 0.0177 | -0.01 (5) |
| 3-5 | 451 | 0.2048 | 0.2049 | -0.0002 ± 0.0017 | 0.5927 | 0.5918 | 0.5052 | 0.4652 | 0.4856 | -0.097 ± 0.0219 | 0.02 (1) |
| 5-10 | 1026 | 0.2038 | 0.2042 | -0.0004 ± 0.0021 | 0.5942 | 0.5928 | 0.5144 | 0.4405 | 0.4766 | -0.088 ± 0.0146 | -0.0167 (6) |
| 10-15 | 876 | 0.2204 | 0.2109 | +0.0095 ± 0.0039 | 0.6334 | 0.6051 | 0.5298 | 0.4059 | 0.4281 | -0.109 ± 0.0156 | -0.048 (5) |
| 15-25 | 1121 | 0.2244 | 0.212 | +0.0125 ± 0.0054 | 0.6444 | 0.6074 | 0.5762 | 0.3805 | 0.4469 | -0.097 ± 0.0137 | -0.0033 (9) |
| 25-40 | 636 | 0.2229 | 0.209 | +0.0139 ± 0.0108 | 0.6353 | 0.6009 | 0.6552 | 0.3454 | 0.4764 | -0.073 ± 0.0166 | -0.01 (1) |
| 40+ | 134 | 0.2706 | 0.2006 | +0.0700 ± 0.0333 | 0.7412 | 0.5849 | 0.7452 | 0.2961 | 0.4478 | -0.055 ± 0.0329 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3802 | 0.1845 | 0.1852 | -0.0007 ± 0.0002 | 0.5447 | 0.5453 | 0.4877 | 0.4725 | 0.4982 | -0.030 ± 0.0071 | -0.0129 (17) |
| 3-5 | 2547 | 0.1989 | 0.1973 | +0.0016 ± 0.0007 | 0.5787 | 0.5725 | 0.4844 | 0.4445 | 0.4425 | -0.058 ± 0.0089 | 0.0 (2) |
| 5-10 | 5396 | 0.2002 | 0.1966 | +0.0036 ± 0.0009 | 0.5857 | 0.5732 | 0.4863 | 0.4124 | 0.4249 | -0.049 ± 0.0061 | -0.0119 (21) |
| 10-15 | 4633 | 0.2014 | 0.1839 | +0.0174 ± 0.0016 | 0.5892 | 0.54 | 0.4898 | 0.3655 | 0.357 | -0.072 ± 0.0063 | -0.0281 (16) |
| 15-25 | 5773 | 0.2075 | 0.1683 | +0.0391 ± 0.0021 | 0.6082 | 0.4982 | 0.502 | 0.3058 | 0.305 | -0.073 ± 0.0054 | -0.0025 (44) |
| 25-40 | 4531 | 0.2221 | 0.126 | +0.0961 ± 0.0033 | 0.6383 | 0.3869 | 0.5281 | 0.2143 | 0.2222 | -0.061 ± 0.0051 | -0.01 (1) |
| 40+ | 2955 | 0.3778 | 0.0472 | +0.3306 ± 0.0045 | 0.9838 | 0.1799 | 0.6303 | 0.105 | 0.066 | -0.074 ± 0.0038 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 571 | 0.2055 | 0.2062 | -0.0007 ± 0.0007 | 0.5925 | 0.5942 | 0.5097 | 0.4945 | 0.5149 | -0.109 ± 0.0206 | -0.01 (3) |
| 3-5 | 403 | 0.2268 | 0.2235 | +0.0033 ± 0.0019 | 0.6404 | 0.6336 | 0.5114 | 0.4717 | 0.4442 | -0.140 ± 0.0251 | 0.02 (1) |
| 5-10 | 894 | 0.2086 | 0.2084 | +0.0002 ± 0.0023 | 0.6037 | 0.6029 | 0.5492 | 0.4743 | 0.5134 | -0.085 ± 0.0158 | -0.01 (4) |
| 10-15 | 812 | 0.2197 | 0.2125 | +0.0072 ± 0.0041 | 0.6309 | 0.6112 | 0.5676 | 0.4434 | 0.4791 | -0.109 ± 0.0169 | -0.04 (5) |
| 15-25 | 1165 | 0.2297 | 0.2132 | +0.0166 ± 0.0053 | 0.6537 | 0.6094 | 0.5855 | 0.3902 | 0.4489 | -0.098 ± 0.0138 | -0.0133 (9) |
| 25-40 | 820 | 0.2665 | 0.1976 | +0.0689 ± 0.0098 | 0.7451 | 0.5759 | 0.6525 | 0.3382 | 0.389 | -0.122 ± 0.0154 | -0.0075 (4) |
| 40+ | 307 | 0.3586 | 0.1708 | +0.1878 ± 0.0234 | 0.9831 | 0.5103 | 0.7342 | 0.2481 | 0.3127 | -0.072 ± 0.0227 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3237 | 0.193 | 0.1931 | -0.0002 ± 0.0003 | 0.5632 | 0.5632 | 0.5126 | 0.4976 | 0.5076 | -0.048 ± 0.008 | -0.0133 (15) |
| 3-5 | 2170 | 0.1994 | 0.1977 | +0.0017 ± 0.0008 | 0.5776 | 0.5729 | 0.5141 | 0.4743 | 0.4719 | -0.056 ± 0.0098 | 0.02 (1) |
| 5-10 | 4796 | 0.198 | 0.1954 | +0.0026 ± 0.001 | 0.5818 | 0.5706 | 0.5146 | 0.4406 | 0.4633 | -0.038 ± 0.0065 | -0.0117 (6) |
| 10-15 | 4135 | 0.2045 | 0.1921 | +0.0124 ± 0.0017 | 0.5985 | 0.5583 | 0.5166 | 0.3927 | 0.4056 | -0.056 ± 0.0069 | -0.0189 (18) |
| 15-25 | 5764 | 0.2155 | 0.179 | +0.0366 ± 0.0022 | 0.6273 | 0.525 | 0.5244 | 0.3289 | 0.3369 | -0.065 ± 0.0056 | -0.0086 (42) |
| 25-40 | 5305 | 0.2516 | 0.1366 | +0.1150 ± 0.0032 | 0.7093 | 0.4191 | 0.5569 | 0.2402 | 0.2198 | -0.086 ± 0.0051 | -0.0044 (18) |
| 40+ | 4230 | 0.3945 | 0.0609 | +0.3335 ± 0.0043 | 1.0376 | 0.2175 | 0.6512 | 0.1186 | 0.0853 | -0.070 ± 0.0037 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 710 | 0.198 | 0.2 | -0.0021 ± 0.0006 | 0.5754 | 0.5805 | 0.5014 | 0.486 | 0.5465 | -0.037 ± 0.0175 | -0.0137 (8) |
| 3-5 | 489 | 0.2024 | 0.2009 | +0.0015 ± 0.0016 | 0.5879 | 0.5825 | 0.5031 | 0.4633 | 0.4663 | -0.119 ± 0.0211 | 0.0067 (3) |
| 5-10 | 1051 | 0.2042 | 0.2021 | +0.0021 ± 0.0021 | 0.5948 | 0.5871 | 0.5126 | 0.4384 | 0.4605 | -0.096 ± 0.0142 | -0.0071 (7) |
| 10-15 | 867 | 0.2115 | 0.2064 | +0.0050 ± 0.0038 | 0.6129 | 0.5957 | 0.5402 | 0.4169 | 0.4591 | -0.097 ± 0.0155 | -0.0317 (6) |
| 15-25 | 1059 | 0.2319 | 0.216 | +0.0159 ± 0.0056 | 0.6621 | 0.6164 | 0.587 | 0.3925 | 0.4485 | -0.107 ± 0.0143 | -0.03 (1) |
| 25-40 | 653 | 0.2143 | 0.2159 | -0.0016 ± 0.0106 | 0.6178 | 0.6167 | 0.665 | 0.3543 | 0.51 | -0.057 ± 0.0164 | 0.015 (2) |
| 40+ | 143 | 0.2872 | 0.2065 | +0.0807 ± 0.0331 | 0.7899 | 0.5974 | 0.7546 | 0.3038 | 0.4476 | -0.061 ± 0.0347 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3749 | 0.185 | 0.1856 | -0.0006 ± 0.0002 | 0.5447 | 0.5456 | 0.4862 | 0.471 | 0.4884 | -0.035 ± 0.0071 | -0.0163 (35) |
| 3-5 | 2498 | 0.199 | 0.1969 | +0.0021 ± 0.0007 | 0.5812 | 0.5741 | 0.4847 | 0.445 | 0.44 | -0.064 ± 0.0091 | -0.0094 (18) |
| 5-10 | 5552 | 0.1953 | 0.1908 | +0.0045 ± 0.0009 | 0.5741 | 0.5583 | 0.4892 | 0.415 | 0.422 | -0.052 ± 0.0059 | -0.01 (31) |
| 10-15 | 4496 | 0.1932 | 0.1779 | +0.0154 ± 0.0016 | 0.5706 | 0.525 | 0.4992 | 0.3758 | 0.3748 | -0.066 ± 0.0063 | -0.015 (12) |
| 15-25 | 5926 | 0.2121 | 0.1726 | +0.0395 ± 0.0021 | 0.6183 | 0.5086 | 0.5124 | 0.3175 | 0.3145 | -0.074 ± 0.0054 | -0.03 (2) |
| 25-40 | 4498 | 0.2186 | 0.1293 | +0.0893 ± 0.0034 | 0.6313 | 0.394 | 0.5322 | 0.2161 | 0.235 | -0.052 ± 0.0052 | 0.01 (3) |
| 40+ | 2918 | 0.3907 | 0.052 | +0.3387 ± 0.0047 | 1.0206 | 0.1926 | 0.6417 | 0.1126 | 0.0709 | -0.077 ± 0.004 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1094 | 0.196 | 0.1961 | -0.0002 ± 0.0005 | 0.5709 | 0.5708 | 0.5026 | 0.4875 | 0.4927 | -0.065 ± 0.0136 | -0.0224 (49) |
| 3-5 | 755 | 0.1915 | 0.191 | +0.0005 ± 0.0013 | 0.5597 | 0.5576 | 0.495 | 0.4552 | 0.4662 | -0.061 ± 0.0163 | -0.0194 (34) |
| 5-10 | 1579 | 0.2022 | 0.1963 | +0.0058 ± 0.0017 | 0.5943 | 0.575 | 0.4971 | 0.4236 | 0.4212 | -0.078 ± 0.0114 | -0.005 (78) |
| 10-15 | 1074 | 0.2151 | 0.203 | +0.0120 ± 0.0034 | 0.6221 | 0.5892 | 0.5299 | 0.4071 | 0.4181 | -0.077 ± 0.0141 | 0.0014 (64) |
| 15-25 | 1401 | 0.2317 | 0.2107 | +0.0210 ± 0.0048 | 0.6608 | 0.6062 | 0.5798 | 0.3849 | 0.4304 | -0.078 ± 0.0123 | -0.0214 (59) |
| 25-40 | 871 | 0.2434 | 0.2096 | +0.0339 ± 0.0095 | 0.6953 | 0.601 | 0.6779 | 0.366 | 0.4673 | -0.087 ± 0.0145 | -0.0219 (26) |
| 40+ | 285 | 0.3408 | 0.1997 | +0.1411 ± 0.0258 | 0.9851 | 0.5846 | 0.8075 | 0.3276 | 0.4386 | -0.093 ± 0.0238 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3749 | 0.1807 | 0.1809 | -0.0002 ± 0.0002 | 0.5326 | 0.5323 | 0.5053 | 0.4901 | 0.4999 | -0.040 ± 0.007 | -0.0157 (88) |
| 3-5 | 2582 | 0.1943 | 0.1924 | +0.0019 ± 0.0007 | 0.566 | 0.5618 | 0.5037 | 0.4639 | 0.4593 | -0.056 ± 0.0087 | -0.0209 (69) |
| 5-10 | 5208 | 0.1983 | 0.1902 | +0.0081 ± 0.0009 | 0.5843 | 0.5588 | 0.4937 | 0.4201 | 0.4038 | -0.072 ± 0.0061 | -0.0082 (132) |
| 10-15 | 3653 | 0.2112 | 0.1956 | +0.0155 ± 0.0018 | 0.6134 | 0.5717 | 0.5308 | 0.408 | 0.4057 | -0.066 ± 0.0074 | -0.0053 (105) |
| 15-25 | 4450 | 0.2303 | 0.2001 | +0.0303 ± 0.0027 | 0.6634 | 0.5791 | 0.5682 | 0.3725 | 0.3937 | -0.067 ± 0.0067 | -0.0253 (107) |
| 25-40 | 3057 | 0.2588 | 0.1849 | +0.0739 ± 0.0049 | 0.7338 | 0.5398 | 0.6332 | 0.32 | 0.3611 | -0.078 ± 0.0076 | -0.0229 (51) |
| 40+ | 1319 | 0.3739 | 0.1479 | +0.2261 ± 0.011 | 1.0584 | 0.4453 | 0.7297 | 0.2284 | 0.2669 | -0.070 ± 0.01 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4972 | 1.026 ± 0.04 | 1.094 | 0.1676 | 0.1641 | 0.2152 | 0.2072 |
| gen2 | 4972 | 0.812 ± 0.037 | 1.055 | 0.1688 | 0.1646 | 0.2353 | 0.2071 |
| gen1_elo | 4972 | 1.002 ± 0.039 | 1.093 | 0.1741 | 0.1642 | 0.214 | 0.2073 |
| gen1_sr | 4972 | 0.991 ± 0.048 | 1.119 | 0.1294 | 0.1665 | 0.2313 | 0.2067 |
| gen1_ledger | 7059 | 0.859 ± 0.028 | 1.06 | 0.1843 | 0.1767 | 0.2186 | 0.2014 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 25,128)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,555 | 22.1% |
| STALE_QUOTE | market_freshness | 5,469 | 21.8% |
| BOOK_QUALITY | execution | 4,855 | 19.3% |
| POOR_DATA | data | 2,930 | 11.7% |
| LIMITED_DATA | data | 1,564 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,357 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,181 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 1,055 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 719 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 442 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.1%, market_freshness 21.8%, execution 19.3%, data 17.9%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 71.2%, THIN_PLAYER_HISTORY 60.4%, STALE_PLAYER_DATA 51.6%, STALE_KALSHI_QUOTE 43.5%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 16.1%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.7%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.6%, POST_SETTLEMENT_OBSERVATION 22.1%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 13,439)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,489 | 33.4% |
| BOOK_QUALITY | execution | 2,545 | 18.9% |
| STALE_QUOTE | market_freshness | 2,522 | 18.8% |
| POOR_DATA | data | 1,236 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 729 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 576 | 4.3% |
| LIMITED_DATA | data | 466 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 462 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 302 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 111 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.4%, execution 18.9%, market_freshness 18.8%, data 12.7%, market_freshness/coverage 8.9%, mapping 4.3%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.7%, THIN_PLAYER_HISTORY 62.8%, STALE_KALSHI_QUOTE 51.4%, STALE_PLAYER_DATA 46.1%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 24.8%, PLAYER_IDENTITY_RISK 19.2%, MODEL_HIGH_UNCERTAINTY 18.1%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.4%, POST_SETTLEMENT_OBSERVATION 33.4%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 10549, "IDENTITY_AMBIGUOUS": 2890}; ticker orientation: {"VERIFIED": 13439}.

Checks: discipline:AMBIGUOUS 880, discipline:PASS 12559, identity_confidence:AMBIGUOUS 2579, identity_confidence:PASS 10860, level_mapping:NA 892, level_mapping:PASS 12547, market_pair:AMBIGUOUS 469, market_pair:NA 323, market_pair:PASS 12647, model_complement:NA 288, model_complement:PASS 13151, namesake:AMBIGUOUS 6, namesake:PASS 13433, physical_match_id:NA 4734, physical_match_id:PASS 8705, player_ids:PASS 13439, same_pair_other_event:PASS 13439, ticker_orientation:PASS 13439

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,086 | 4.4% | 4.0% | 1.7% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 15, "coverage": 13} | 5.84 | 0.2207 / 0.2168 (577) | 20.8% | 3.1% | 3.3% | 2.7% |
| CHALLENGER | 9,413 | 16.7% | 6.5% | 11.7% | {"coverage": 904, "market_freshness/coverage": 190, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 75, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.219 / 0.2092 (2155) | 34.7% | 16.3% | 4.1% | 22.2% |
| DOUBLES | 1,868 | 47.1% | 46.8% | 6.6% | {"execution": 493, "mapping": 219, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.73 | 0.3112 / 0.2362 (445) | 12.5% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 16,600 | 25.7% | 18.2% | 31.8% | {"coverage": 1503, "execution": 827, "market_freshness": 755, "data": 610, "market_freshness/coverage": 382, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 12.09 | 0.2171 / 0.1992 (3517) | 36.7% | 70.4% | 18.5% | 21.4% |
| ITF_WOMEN | 22,356 | 27.0% | 20.0% | 45.0% | {"coverage": 2032, "market_freshness": 1309, "execution": 1112, "data": 857, "market_freshness/coverage": 496, "mapping": 151, "model_calibration_or_unknown": 76, "model_calibration": 12} | 12.83 | 0.2048 / 0.1978 (4142) | 38.9% | 58.1% | 10.2% | 21.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,652 | 5.7% | 5.1% | 1.6% | {"market_freshness": 73, "model_calibration_or_unknown": 44, "execution": 27, "data": 19, "coverage": 17, "model_calibration": 16, "market_freshness/coverage": 11, "mapping": 1} | 7.65 | 0.2336 / 0.2276 (575) | 25.3% | 1.1% | 1.5% | 3.3% |
| WTA125 | 1,961 | 11.9% | 10.0% | 1.7% | {"market_freshness": 56, "model_calibration_or_unknown": 50, "market_freshness/coverage": 41, "data": 36, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.38 | 0.2129 / 0.197 (578) | 24.9% | 11.9% | 5.5% | 7.7% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 20 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 21 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 22 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 23 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 24 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | LIMITED_DATA | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 25 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 26 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 27 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 28 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 29 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 30 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 31 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 32 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 33 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 34 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 35 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 36 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 37 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 38 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 124 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 39 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 40 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 41 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 42 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 44 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 45 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 46 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 47 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 49 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 50 | `KXITFMATCH-26OCT27GHESAD-GHE` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.2h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 197 min (STALE); data POOR (grade F, thinner serve sample 276.0, ratio 6.69); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9678, "by_level_share_of_ge_25pp": {"ATP": 0.0167, "CHALLENGER": 0.1166, "DOUBLES": 0.0655, "ITF_MEN": 0.3176, "ITF_WOMEN": 0.4498, "OTHER": 0.0009, "WTA": 0.0155, "WTA125": 0.0174}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5137, "share_primary_cause_market_settled_or_in_play": 0.4226, "share_primary_cause_stale_quote_only": 0.1877}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 13439, "identity_ambiguous_share": 0.215, "ticker_orientation": {"VERIFIED": 13439}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 8705, "with_external": 441, "coverage": 0.0507, "external_status": {"EXTERNAL_STALE": 272, "AGREES_WITH_KALSHI": 160, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 272, "MODEL_LONE_OUTLIER": 160, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3628, "share_external_supports_model": 0.0204}, "pregame_clean_ge_25pp": {"n": 4277, "with_external": 417, "coverage": 0.0975, "external_status": {"EXTERNAL_STALE": 255, "AGREES_WITH_KALSHI": 153, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 255, "MODEL_LONE_OUTLIER": 153, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3669, "share_external_supports_model": 0.0216}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 458.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 238.0, "share_severe_asymmetry": 0.2137, "data_status": {"POOR": 7629, "LIMITED": 3395, "ADEQUATE": 2415}, "comparison_lt_10pp": {"median_thinner_serve_points": 1759.0, "median_sample_ratio": 1.68, "median_min_matches": 95.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 989, "model_minus_observed": 0.0473, "kalshi_minus_observed": -0.0904, "brier_diff_model_minus_kalshi": -0.0038}, "4-10x": {"n": 672, "model_minus_observed": 0.0913, "kalshi_minus_observed": -0.0564, "brier_diff_model_minus_kalshi": 0.0096}, "<2x": {"n": 2428, "model_minus_observed": 0.0894, "kalshi_minus_observed": -0.0335, "brier_diff_model_minus_kalshi": 0.011}, ">=10x": {"n": 883, "model_minus_observed": 0.1159, "kalshi_minus_observed": -0.0607, "brier_diff_model_minus_kalshi": 0.0117}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4972, "model": {"intercept": -0.536, "slope": 0.812, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.192, "slope": 1.055, "slope_se": 0.041}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1646, "model_brier": 0.2353, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.0282, "brier_diff_se": 0.0027, "model_logloss": 0.6683, "kalshi_logloss": 0.5971}, "fair_v1": {"n": 4972, "model": {"intercept": -0.414, "slope": 1.026, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.282, "slope": 1.094, "slope_se": 0.041}, "mean_extremity_model": 0.1676, "mean_extremity_kalshi": 0.1641, "model_brier": 0.2152, "kalshi_brier": 0.2072, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0022, "model_logloss": 0.6196, "kalshi_logloss": 0.5974}, "gen1_elo": {"n": 4972, "model": {"intercept": -0.388, "slope": 1.002, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.303, "slope": 1.093, "slope_se": 0.04}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1642, "model_brier": 0.214, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.0067, "brier_diff_se": 0.0022, "model_logloss": 0.6175, "kalshi_logloss": 0.5976}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2468, "share_ge_15": 0.443, "median_abs_gap": 13.07, "n": 35275}, "gen1_elo": {"share_ge_25": 0.244, "share_ge_15": 0.4405, "median_abs_gap": 12.89, "n": 35275}, "gen1_sr": {"share_ge_25": 0.3145, "share_ge_15": 0.5222, "median_abs_gap": 15.95, "n": 35275}, "gen2": {"share_ge_25": 0.3184, "share_ge_15": 0.5133, "median_abs_gap": 15.55, "n": 35275}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.155, "share_ge_15": 0.3593, "median_abs_gap": 10.86, "n": 27593}, "gen1_elo": {"share_ge_25": 0.1549, "share_ge_15": 0.3556, "median_abs_gap": 10.67, "n": 27591}, "gen1_sr": {"share_ge_25": 0.2225, "share_ge_15": 0.4456, "median_abs_gap": 13.03, "n": 27594}, "gen2": {"share_ge_25": 0.2389, "share_ge_15": 0.4458, "median_abs_gap": 13.06, "n": 27595}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0442, "share_ge_25_pregame_clean": 0.0398}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.057, "share_ge_25_pregame_clean": 0.051}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2358, "share_within_10pp_all": 0.4347, "share_within_10pp_pregame_clean": 0.4857, "corr_model_vs_mid_pregame_clean": 0.8449}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 728, "model_brier": 0.2004, "kalshi_brier": 0.2009, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 876, "model_brier": 0.2204, "kalshi_brier": 0.2109, "brier_diff_model_minus_kalshi": 0.0095}, "15-25": {"n_settled": 1121, "model_brier": 0.2244, "kalshi_brier": 0.212, "brier_diff_model_minus_kalshi": 0.0125}, "25-40": {"n_settled": 636, "model_brier": 0.2229, "kalshi_brier": 0.209, "brier_diff_model_minus_kalshi": 0.0139}, "3-5": {"n_settled": 451, "model_brier": 0.2048, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": -0.0002}, "40+": {"n_settled": 134, "model_brier": 0.2706, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.07}, "5-10": {"n_settled": 1026, "model_brier": 0.2038, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": -0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.536, "slope": 0.812, "slope_se": 0.037}, "kalshi_slope": {"intercept": 0.192, "slope": 1.055, "slope_se": 0.041}, "n": 4972}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.495, "slope": 0.859, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.158, "slope": 1.06, "slope_se": 0.033}, "n": 7059}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 445, "model_brier": 0.3112, "kalshi_brier": 0.2362, "brier_diff_model_minus_kalshi": 0.0749, "brier_diff_se": 0.0143, "corr_model_outcome": 0.0359, "corr_kalshi_outcome": 0.2487}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
