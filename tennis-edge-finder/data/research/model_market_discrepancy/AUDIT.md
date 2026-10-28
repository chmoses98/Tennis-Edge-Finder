# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-28T23:21Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 66,263): 0-3 14.2%, 3-5 9.6%, 5-10 20.0%, 10-15 15.3%, 15-25 19.0%, 25-40 13.9%, 40+ 8.0%; median gap 11.88 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.6%, Challenger 11.1%, doubles 6.4%). Main tour: ATP 4.3% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 14,514): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.5%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.7%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.5%, market_freshness 18.7%, execution 18.7%, data 12.8%, market_freshness/coverage 9.2%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 14,514 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.0% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 454.0 points vs 1651.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.017, Gen-2 0.808, Gen-1 ledger 0.854 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 701 model 0.2234 vs Kalshi 0.2076; n 147 model 0.2778 vs Kalshi 0.1891.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 283,787 model-market comparisons (462,511 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 95,030 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-28T23:09:42.200562+00:00'], shadow board 75,746 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-28T23:09:46.593898+00:00'], Model 4 35,876 rows, 23,137 settled tickers, 8,352 tickers with an external scan.
* By model: {"gen1_ledger": 64127, "gen1_elo": 38079, "fair_v1": 38079, "gen2": 38079, "gen1_sr": 38079, "model4_fundamental": 33694, "model4_conditioned": 33650}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 66,263 | 14.2 | 9.6 | 20.0 | 15.3 | 19.0 | 13.9 | 8.0 | 11.88 | 40.9% | 21.9% |
| MW fair_v1 | 38,079 | 13.0 | 8.7 | 18.6 | 15.4 | 19.4 | 15.0 | 9.8 | 13.01 | 44.2% | 24.8% |
| MW gen1_elo | 38,079 | 12.7 | 8.6 | 19.3 | 15.4 | 19.5 | 14.9 | 9.7 | 12.93 | 44.1% | 24.6% |
| MW gen1_ledger | 28,184 | 15.7 | 10.7 | 21.9 | 15.2 | 18.4 | 12.4 | 5.6 | 10.41 | 36.4% | 18.0% |
| MW gen1_sr | 38,079 | 10.2 | 7.2 | 16.8 | 13.8 | 20.7 | 18.6 | 12.8 | 15.9 | 52.1% | 31.4% |
| MW gen2 | 38,079 | 11.1 | 7.5 | 16.4 | 13.8 | 19.4 | 17.9 | 13.8 | 15.49 | 51.1% | 31.7% |
| all families model4_conditioned | 33,650 | 22.3 | 18.2 | 34.3 | 17.3 | 4.9 | 1.9 | 1.1 | 6.02 | 7.9% | 3.0% |
| all families model4_fundamental | 33,694 | 17.3 | 13.3 | 33.9 | 20.4 | 10.2 | 3.6 | 1.4 | 7.72 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.3%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.28pp; >=10pp 44.7%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,348 | 27.1 | 15.6 | 27.4 | 13.5 | 11.7 | 4.1 | 0.6 | 5.92 | 16.4% | 4.7% |
| CHALLENGER | 5,787 | 16.2 | 9.8 | 20.6 | 15.4 | 15.4 | 11.9 | 10.7 | 10.93 | 38.0% | 22.6% |
| ITF_MEN | 10,547 | 9.9 | 7.4 | 16.8 | 15.1 | 21.1 | 17.7 | 12.1 | 15.26 | 50.8% | 29.7% |
| ITF_WOMEN | 14,955 | 9.8 | 7.0 | 15.8 | 15.0 | 22.0 | 18.3 | 11.9 | 15.69 | 52.3% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,392 | 18.2 | 13.7 | 24.4 | 20.2 | 16.2 | 6.5 | 0.8 | 8.25 | 23.5% | 7.3% |
| WTA125 | 1,044 | 16.0 | 7.7 | 22.6 | 19.4 | 20.2 | 12.6 | 1.6 | 10.7 | 34.4% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,348 | 25.8 | 15.5 | 25.3 | 16.4 | 12.0 | 4.2 | 0.8 | 6.23 | 17.0% | 5.0% |
| CHALLENGER | 5,787 | 15.1 | 8.9 | 18.1 | 14.4 | 18.1 | 13.7 | 11.6 | 12.65 | 43.4% | 25.3% |
| ITF_MEN | 10,547 | 8.0 | 6.1 | 14.8 | 13.6 | 19.7 | 20.7 | 17.1 | 18.13 | 57.5% | 37.8% |
| ITF_WOMEN | 14,955 | 8.0 | 5.8 | 14.1 | 12.7 | 20.6 | 21.4 | 17.5 | 19.21 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,392 | 15.1 | 10.9 | 21.8 | 15.6 | 22.1 | 12.8 | 1.7 | 10.62 | 36.5% | 14.4% |
| WTA125 | 1,044 | 9.5 | 6.3 | 16.2 | 16.7 | 24.6 | 17.9 | 8.8 | 15.5 | 51.3% | 26.7% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,348 | 22.4 | 13.0 | 24.4 | 16.0 | 16.2 | 6.6 | 1.3 | 7.58 | 24.2% | 8.0% |
| CHALLENGER | 5,787 | 15.0 | 9.3 | 21.2 | 15.8 | 15.6 | 12.3 | 10.9 | 11.2 | 38.7% | 23.2% |
| ITF_MEN | 10,547 | 9.3 | 7.1 | 17.3 | 14.3 | 21.6 | 18.1 | 12.3 | 15.75 | 52.0% | 30.4% |
| ITF_WOMEN | 14,955 | 9.6 | 6.8 | 16.3 | 15.8 | 22.1 | 18.1 | 11.3 | 15.5 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,392 | 23.7 | 16.5 | 31.6 | 14.8 | 9.5 | 2.6 | 1.2 | 6.08 | 13.4% | 3.9% |
| WTA125 | 1,044 | 22.1 | 12.9 | 26.6 | 16.8 | 14.8 | 6.3 | 0.4 | 7.96 | 21.6% | 6.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,941 | 24.5 | 19.1 | 31.0 | 12.9 | 9.0 | 3.0 | 0.5 | 5.73 | 12.6% | 3.5% |
| CHALLENGER | 3,932 | 22.5 | 14.6 | 26.9 | 14.7 | 13.8 | 6.1 | 1.6 | 7.14 | 21.4% | 7.6% |
| DOUBLES | 2,016 | 5.1 | 4.6 | 12.3 | 10.5 | 21.1 | 25.1 | 21.3 | 23.54 | 67.5% | 46.4% |
| ITF_MEN | 8,082 | 13.1 | 9.3 | 21.0 | 15.9 | 21.3 | 13.3 | 6.1 | 12.0 | 40.7% | 19.4% |
| ITF_WOMEN | 9,590 | 13.1 | 9.0 | 19.6 | 15.6 | 21.3 | 15.6 | 5.8 | 12.49 | 42.6% | 21.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,416 | 24.4 | 15.4 | 29.8 | 18.0 | 9.3 | 2.8 | 0.3 | 6.79 | 12.4% | 3.1% |
| WTA125 | 1,058 | 24.9 | 12.5 | 21.1 | 19.3 | 13.1 | 7.5 | 1.7 | 7.89 | 22.3% | 9.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,251 | 27.5 | 15.7 | 27.8 | 13.4 | 11.5 | 3.8 | 0.4 | 5.87 | 15.6% | 4.1% |
| CHALLENGER | 4,062 | 21.2 | 12.4 | 25.8 | 17.9 | 15.1 | 6.2 | 1.5 | 8.04 | 22.8% | 7.7% |
| ITF_MEN | 7,764 | 12.1 | 8.8 | 20.2 | 17.2 | 21.9 | 14.5 | 5.3 | 12.47 | 41.7% | 19.8% |
| ITF_WOMEN | 11,188 | 11.7 | 8.4 | 18.2 | 17.2 | 24.0 | 15.3 | 5.3 | 13.38 | 44.5% | 20.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,317 | 18.5 | 13.6 | 24.6 | 20.5 | 16.3 | 6.0 | 0.6 | 8.22 | 22.9% | 6.6% |
| WTA125 | 1,008 | 16.3 | 7.5 | 22.1 | 19.6 | 20.7 | 12.3 | 1.4 | 10.97 | 34.4% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,251 | 26.1 | 15.8 | 25.5 | 16.3 | 12.0 | 3.8 | 0.5 | 6.2 | 16.3% | 4.3% |
| CHALLENGER | 4,062 | 19.4 | 11.3 | 22.8 | 16.9 | 18.4 | 9.3 | 1.9 | 9.08 | 29.5% | 11.2% |
| ITF_MEN | 7,765 | 9.3 | 7.2 | 17.2 | 15.8 | 21.5 | 18.9 | 10.1 | 15.17 | 50.5% | 29.0% |
| ITF_WOMEN | 11,189 | 8.9 | 6.7 | 15.8 | 14.1 | 22.6 | 20.9 | 10.9 | 16.76 | 54.5% | 31.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,317 | 15.3 | 11.0 | 21.9 | 15.7 | 22.3 | 12.7 | 1.2 | 10.59 | 36.2% | 13.9% |
| WTA125 | 1,008 | 9.5 | 6.3 | 16.3 | 16.9 | 24.5 | 18.2 | 8.2 | 15.37 | 51.0% | 26.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,887 | 24.6 | 19.3 | 31.0 | 13.0 | 8.7 | 2.9 | 0.4 | 5.67 | 12.0% | 3.3% |
| CHALLENGER | 3,464 | 24.0 | 15.5 | 28.0 | 14.8 | 13.1 | 4.1 | 0.4 | 6.59 | 17.7% | 4.6% |
| DOUBLES | 1,889 | 5.0 | 4.7 | 12.6 | 10.7 | 21.0 | 24.9 | 21.2 | 23.41 | 67.1% | 46.1% |
| ITF_MEN | 6,893 | 14.0 | 9.9 | 22.7 | 16.5 | 21.3 | 11.7 | 4.0 | 11.02 | 37.0% | 15.7% |
| ITF_WOMEN | 8,136 | 13.8 | 9.5 | 20.9 | 16.3 | 21.4 | 14.5 | 3.6 | 11.62 | 39.5% | 18.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,362 | 24.7 | 15.8 | 29.8 | 18.1 | 9.3 | 2.2 | 0.1 | 6.64 | 11.6% | 2.3% |
| WTA125 | 935 | 26.3 | 13.3 | 22.1 | 20.5 | 12.0 | 5.2 | 0.5 | 7.32 | 17.8% | 5.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,016 | 5.1 | 4.6 | 12.3 | 10.5 | 21.1 | 25.1 | 21.3 | 23.54 | 67.5% | 46.4% |
| singles | 26,168 | 16.5 | 11.2 | 22.7 | 15.6 | 18.2 | 11.4 | 4.4 | 9.91 | 34.0% | 15.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,711 | 13.1 | 9.3 | 20.0 | 15.6 | 19.1 | 13.9 | 9.0 | 12.41 | 42.0% | 22.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 24,813 | 13.6 | 8.7 | 18.4 | 15.1 | 19.2 | 15.2 | 9.8 | 12.96 | 44.2% | 24.9% |
| UNKNOWN | 5,306 | 10.6 | 7.8 | 17.0 | 16.7 | 20.8 | 15.9 | 11.2 | 14.11 | 47.9% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,594 | 20.0 | 12.2 | 22.2 | 15.8 | 14.7 | 9.3 | 5.8 | 8.59 | 29.8% | 15.1% |
| B | 4,640 | 12.9 | 8.8 | 19.1 | 16.2 | 19.4 | 12.8 | 10.8 | 12.61 | 43.0% | 23.6% |
| C | 5,408 | 12.2 | 8.9 | 19.8 | 15.8 | 18.6 | 14.4 | 10.2 | 12.73 | 43.2% | 24.6% |
| D | 5,994 | 12.2 | 8.3 | 17.5 | 15.3 | 21.4 | 15.8 | 9.4 | 13.71 | 46.6% | 25.2% |
| F | 11,443 | 7.5 | 5.6 | 14.9 | 14.6 | 23.2 | 21.1 | 13.1 | 17.82 | 57.4% | 34.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,526 | 24.2 | 15.7 | 28.5 | 15.4 | 11.0 | 3.8 | 1.3 | 6.52 | 16.2% | 5.2% |
| B | 3,897 | 17.0 | 10.2 | 24.1 | 16.4 | 19.1 | 10.0 | 3.3 | 9.72 | 32.3% | 13.2% |
| C | 5,483 | 11.3 | 7.9 | 19.4 | 14.7 | 21.1 | 15.5 | 10.1 | 13.46 | 46.7% | 25.6% |
| D | 4,112 | 14.5 | 10.0 | 21.4 | 15.4 | 20.0 | 13.1 | 5.6 | 11.26 | 38.7% | 18.7% |
| F | 7,166 | 10.0 | 8.3 | 16.0 | 14.9 | 23.0 | 19.9 | 7.8 | 15.41 | 50.7% | 27.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,017 | 18.3 | 11.1 | 21.3 | 15.5 | 15.2 | 10.1 | 8.5 | 9.78 | 33.8% | 18.6% |
| LIMITED | 8,263 | 13.8 | 10.0 | 20.2 | 16.3 | 19.0 | 13.3 | 7.4 | 11.68 | 39.7% | 20.7% |
| POOR | 17,799 | 9.1 | 6.5 | 15.9 | 14.9 | 22.5 | 19.1 | 11.8 | 16.15 | 53.4% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,333 | 24.1 | 18.2 | 33.1 | 15.0 | 6.5 | 2.7 | 0.4 | 5.85 | 9.6% | 3.0% |
| GAME_SPREAD | 5,751 | 22.2 | 15.3 | 32.9 | 17.1 | 9.0 | 2.9 | 0.6 | 6.74 | 12.5% | 3.5% |
| MATCH_WINNER | 28,184 | 15.7 | 10.7 | 21.9 | 15.2 | 18.4 | 12.4 | 5.6 | 10.41 | 36.4% | 18.0% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,286 | 27.4 | 16.6 | 31.3 | 12.5 | 9.5 | 2.4 | 0.3 | 5.69 | 12.2% | 2.7% |
| TOTAL_GAMES | 9,549 | 9.3 | 10.3 | 36.0 | 26.9 | 10.6 | 4.0 | 2.8 | 9.33 | 17.4% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,935 | 24.4 | 30.3 | 32.9 | 7.3 | 4.0 | 0.9 | 0.2 | 4.7 | 5.1% | 1.1% |
| GAME_SPREAD | 7,878 | 47.2 | 16.1 | 25.5 | 7.3 | 2.1 | 1.2 | 0.6 | 3.28 | 4.0% | 1.8% |
| TOTAL_GAMES | 13,837 | 6.2 | 9.0 | 40.5 | 31.6 | 7.3 | 3.1 | 2.2 | 9.35 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,946 | 23.9 | 16.8 | 34.8 | 14.4 | 7.1 | 2.6 | 0.4 | 6.02 | 10.1% | 3.0% |
| GAME_SPREAD | 7,881 | 20.1 | 13.5 | 28.0 | 20.5 | 12.6 | 4.3 | 1.1 | 7.82 | 17.9% | 5.3% |
| TOTAL_GAMES | 13,867 | 9.9 | 10.1 | 36.4 | 25.4 | 11.6 | 4.2 | 2.4 | 9.21 | 18.2% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 38,079 | 44.2% | 24.8% | 13.01 | 35.6% | 15.5% | 10.77 |
| gen1_elo | 38,079 | 44.1% | 24.6% | 12.93 | 35.4% | 15.5% | 10.56 |
| gen1_sr | 38,079 | 52.1% | 31.4% | 15.9 | 44.3% | 22.1% | 13.04 |
| gen2 | 38,079 | 51.1% | 31.7% | 15.49 | 44.3% | 23.6% | 12.98 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,317 | 15.6 | 10.6 | 21.3 | 17.2 | 20.0 | 12.0 | 3.3 | 10.71 | 35.4% | 15.4% |
| STALE | 19,762 | 10.6 | 7.0 | 16.1 | 13.8 | 18.9 | 17.8 | 15.8 | 16.06 | 52.5% | 33.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 21,652 | 16.4 | 11.1 | 22.6 | 15.4 | 17.8 | 11.9 | 4.8 | 9.97 | 34.5% | 16.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 66,263 | 21652 | 21789 | 22822 | 24.2 | 119.4 | 1400.4 |
| ge_15pp | 27,116 | 7468 | 7768 | 11880 | 26.7 | 429.9 | 1399.2 |
| ge_25pp | 14,514 | 3606 | 3408 | 7500 | 31.5 | 575.6 | 1380.4 |
| lt_10pp | 28,979 | 10850 | 10324 | 7805 | 22.4 | 46.9 | 1341.8 |

Current slate `SL-20261028T232149Z-f6e2ddc5`: 600 priced rows, quote age at build {'median': 12.4, 'max': 12.5}, freshness {'AGING': 600}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 43 | 0.0 | 0.0 | 32.6 | 7.0 | 34.9 | 23.3 | 2.3 | 20.19 | 60.5% | 25.6% |
| EXTERNAL_LONE_OUTLIER | 23 | 69.6 | 30.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,728 | 20.0 | 11.2 | 25.1 | 18.0 | 17.7 | 7.2 | 0.9 | 8.61 | 25.8% | 8.0% |
| KALSHI_LONE_OUTLIER | 26 | 3.9 | 3.9 | 76.9 | 7.7 | 3.9 | 3.9 | 0.0 | 6.31 | 7.7% | 3.9% |
| MARKETS_AGREE | 744 | 65.3 | 34.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.25 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,602 | 0.0 | 2.5 | 35.7 | 25.8 | 24.7 | 10.5 | 0.8 | 12.2 | 36.0% | 11.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 38,079 | 6166 (16.2%) | 26.0% | 1.1% | {"EXTERNAL_STALE": 3728, "AGREES_WITH_KALSHI": 1602, "ALL_AGREE": 744, "SUPPORTS_MODEL_DIRECTION": 42, "AGREES_WITH_MODEL": 26, "EXTERNAL_OUTLIER": 23, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 16,849 | 1565 (9.3%) | 36.9% | 1.8% | {"EXTERNAL_STALE": 960, "AGREES_WITH_KALSHI": 577, "SUPPORTS_MODEL_DIRECTION": 26, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,446 | 492 (5.2%) | 36.8% | 2.4% | {"EXTERNAL_STALE": 299, "AGREES_WITH_KALSHI": 181, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,577 | 467 (10.2%) | 37.3% | 2.6% | {"EXTERNAL_STALE": 281, "AGREES_WITH_KALSHI": 174, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 15,360 | 3512 (22.9%) | 17.4% | 1.0% | {"EXTERNAL_STALE": 2097, "ALL_AGREE": 744, "AGREES_WITH_KALSHI": 612, "EXTERNAL_OUTLIER": 23, "AGREES_WITH_MODEL": 22, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,455 | 10.5 | 7.4 | 19.7 | 14.3 | 21.6 | 16.6 | 9.8 | 14.09 | 48.0% | 26.5% |
| 4-10x | 5,109 | 11.3 | 8.7 | 18.4 | 15.4 | 21.8 | 14.6 | 9.9 | 13.65 | 46.2% | 24.5% |
| <2x | 19,242 | 15.2 | 10.0 | 19.3 | 16.1 | 17.4 | 13.1 | 8.8 | 11.58 | 39.3% | 21.9% |
| >=10x | 6,273 | 10.7 | 6.4 | 15.1 | 14.5 | 21.4 | 19.2 | 12.7 | 16.21 | 53.3% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,625 | 12.8 | 8.6 | 19.5 | 16.2 | 19.0 | 13.6 | 10.3 | 12.69 | 42.9% | 23.9% |
| 300-1000 | 8,179 | 12.3 | 8.8 | 17.7 | 15.3 | 20.2 | 16.4 | 9.5 | 13.54 | 46.0% | 25.9% |
| <300 | 12,456 | 8.4 | 5.8 | 15.2 | 14.8 | 22.9 | 20.1 | 12.8 | 17.05 | 55.8% | 33.0% |
| >=3000 | 7,819 | 21.6 | 13.4 | 23.8 | 15.7 | 13.8 | 7.2 | 4.6 | 7.56 | 25.6% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1085 | 0.5491 | 0.4105 | 0.4986 | +0.051 | -0.088 | -0.0023 ± 0.0047 |
| ratio 4-10x | 745 | 0.5798 | 0.4339 | 0.494 | +0.086 | -0.060 | 0.0086 ± 0.0058 |
| ratio <2x | 2615 | 0.5372 | 0.4136 | 0.4489 | +0.088 | -0.035 | 0.0109 ± 0.0028 |
| ratio >=10x | 950 | 0.5663 | 0.3911 | 0.4453 | +0.121 | -0.054 | 0.0146 ± 0.0059 |
| thinner_sample 1000-3000 | 1446 | 0.5381 | 0.4112 | 0.4509 | +0.087 | -0.040 | 0.0082 ± 0.0038 |
| thinner_sample 300-1000 | 1222 | 0.5676 | 0.4262 | 0.4894 | +0.078 | -0.063 | 0.0022 ± 0.0046 |
| thinner_sample <300 | 1834 | 0.558 | 0.3899 | 0.4586 | +0.099 | -0.069 | 0.0111 ± 0.0042 |
| thinner_sample >=3000 | 893 | 0.5324 | 0.4382 | 0.4647 | +0.068 | -0.026 | 0.0126 ± 0.0038 |
| data_status ADEQUATE | 1484 | 0.5342 | 0.4305 | 0.4495 | +0.085 | -0.019 | 0.0126 ± 0.0032 |
| data_status LIMITED | 1277 | 0.5474 | 0.4149 | 0.4785 | +0.069 | -0.064 | 0.0039 ± 0.0042 |
| data_status POOR | 2634 | 0.5614 | 0.3999 | 0.4662 | +0.095 | -0.066 | 0.0086 ± 0.0034 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 799 | 0.1978 | 0.1982 | -0.0004 ± 0.0006 | 0.5745 | 0.5756 | 0.5024 | 0.4873 | 0.5069 | -0.089 ± 0.0167 | -0.01 (5) |
| 3-5 | 483 | 0.2057 | 0.2064 | -0.0007 ± 0.0017 | 0.5949 | 0.595 | 0.503 | 0.4631 | 0.4907 | -0.092 ± 0.0212 | 0.02 (1) |
| 5-10 | 1127 | 0.201 | 0.2016 | -0.0006 ± 0.002 | 0.5875 | 0.5862 | 0.5101 | 0.4364 | 0.4747 | -0.086 ± 0.0138 | -0.0167 (6) |
| 10-15 | 942 | 0.222 | 0.2133 | +0.0087 ± 0.0037 | 0.637 | 0.6129 | 0.5271 | 0.4035 | 0.4289 | -0.108 ± 0.0152 | -0.048 (5) |
| 15-25 | 1196 | 0.2251 | 0.2122 | +0.0129 ± 0.0052 | 0.6459 | 0.6087 | 0.5745 | 0.3789 | 0.444 | -0.099 ± 0.0134 | -0.0033 (9) |
| 25-40 | 701 | 0.2234 | 0.2076 | +0.0158 ± 0.0103 | 0.637 | 0.5972 | 0.6545 | 0.3442 | 0.4736 | -0.072 ± 0.0158 | -0.01 (1) |
| 40+ | 147 | 0.2778 | 0.1891 | +0.0887 ± 0.0313 | 0.7558 | 0.5575 | 0.7395 | 0.2904 | 0.4218 | -0.069 ± 0.0306 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4267 | 0.1811 | 0.1818 | -0.0006 ± 0.0002 | 0.5362 | 0.5367 | 0.4861 | 0.4709 | 0.4943 | -0.031 ± 0.0066 | -0.0129 (17) |
| 3-5 | 2877 | 0.1955 | 0.1933 | +0.0022 ± 0.0007 | 0.5703 | 0.5627 | 0.4824 | 0.4425 | 0.4345 | -0.063 ± 0.0083 | 0.0 (2) |
| 5-10 | 6070 | 0.2016 | 0.1982 | +0.0034 ± 0.0009 | 0.5888 | 0.5769 | 0.4834 | 0.4097 | 0.4244 | -0.046 ± 0.0058 | -0.0119 (21) |
| 10-15 | 5093 | 0.2024 | 0.1862 | +0.0162 ± 0.0015 | 0.5912 | 0.5471 | 0.4832 | 0.3592 | 0.3554 | -0.068 ± 0.0061 | -0.0281 (16) |
| 15-25 | 6342 | 0.2072 | 0.1694 | +0.0377 ± 0.002 | 0.6072 | 0.5021 | 0.5 | 0.3037 | 0.3064 | -0.069 ± 0.0052 | -0.0025 (44) |
| 25-40 | 5073 | 0.222 | 0.1255 | +0.0965 ± 0.0031 | 0.638 | 0.3856 | 0.5266 | 0.2124 | 0.2202 | -0.059 ± 0.0048 | -0.01 (1) |
| 40+ | 3268 | 0.3815 | 0.0448 | +0.3367 ± 0.0042 | 0.9932 | 0.1734 | 0.6311 | 0.1039 | 0.0609 | -0.077 ± 0.0035 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 615 | 0.2055 | 0.2062 | -0.0007 ± 0.0006 | 0.5925 | 0.5945 | 0.5093 | 0.4942 | 0.5203 | -0.104 ± 0.0198 | -0.01 (3) |
| 3-5 | 438 | 0.2238 | 0.2209 | +0.0029 ± 0.0018 | 0.6333 | 0.6275 | 0.5131 | 0.4734 | 0.4521 | -0.135 ± 0.024 | 0.02 (1) |
| 5-10 | 977 | 0.2082 | 0.208 | +0.0002 ± 0.0022 | 0.602 | 0.6009 | 0.5469 | 0.4719 | 0.5097 | -0.084 ± 0.0151 | -0.01 (4) |
| 10-15 | 885 | 0.2178 | 0.2106 | +0.0072 ± 0.0039 | 0.6271 | 0.6081 | 0.5646 | 0.4403 | 0.4757 | -0.110 ± 0.0161 | -0.04 (5) |
| 15-25 | 1258 | 0.2288 | 0.2134 | +0.0154 ± 0.0051 | 0.6518 | 0.6109 | 0.5811 | 0.3858 | 0.4467 | -0.096 ± 0.0132 | -0.0133 (9) |
| 25-40 | 891 | 0.2689 | 0.1965 | +0.0724 ± 0.0093 | 0.7506 | 0.5736 | 0.6541 | 0.3401 | 0.385 | -0.131 ± 0.0149 | -0.0075 (4) |
| 40+ | 331 | 0.3599 | 0.1682 | +0.1917 ± 0.0223 | 0.9845 | 0.5044 | 0.7313 | 0.246 | 0.3051 | -0.076 ± 0.0218 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3644 | 0.1887 | 0.189 | -0.0003 ± 0.0003 | 0.5526 | 0.553 | 0.5095 | 0.4944 | 0.5102 | -0.041 ± 0.0075 | -0.0133 (15) |
| 3-5 | 2461 | 0.1969 | 0.1954 | +0.0014 ± 0.0007 | 0.5711 | 0.5672 | 0.5148 | 0.4752 | 0.4762 | -0.052 ± 0.0091 | 0.02 (1) |
| 5-10 | 5374 | 0.1988 | 0.195 | +0.0038 ± 0.0009 | 0.5831 | 0.5693 | 0.5133 | 0.4391 | 0.4533 | -0.045 ± 0.0061 | -0.0117 (6) |
| 10-15 | 4590 | 0.2063 | 0.1935 | +0.0127 ± 0.0016 | 0.6027 | 0.5644 | 0.5127 | 0.3888 | 0.4 | -0.056 ± 0.0066 | -0.0189 (18) |
| 15-25 | 6405 | 0.2167 | 0.1807 | +0.0360 ± 0.0021 | 0.6305 | 0.5305 | 0.5214 | 0.326 | 0.3352 | -0.062 ± 0.0053 | -0.0086 (42) |
| 25-40 | 5880 | 0.2513 | 0.1359 | +0.1154 ± 0.0031 | 0.7082 | 0.4171 | 0.556 | 0.2392 | 0.2185 | -0.086 ± 0.0048 | -0.0044 (18) |
| 40+ | 4636 | 0.3958 | 0.0593 | +0.3365 ± 0.0041 | 1.0418 | 0.213 | 0.6503 | 0.1171 | 0.0818 | -0.072 ± 0.0035 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 765 | 0.1956 | 0.1976 | -0.0020 ± 0.0006 | 0.5695 | 0.5746 | 0.5003 | 0.485 | 0.5425 | -0.040 ± 0.0168 | -0.0137 (8) |
| 3-5 | 526 | 0.2043 | 0.2026 | +0.0017 ± 0.0016 | 0.5916 | 0.5852 | 0.496 | 0.4563 | 0.4563 | -0.120 ± 0.0204 | 0.0067 (3) |
| 5-10 | 1160 | 0.2031 | 0.2012 | +0.0019 ± 0.002 | 0.5922 | 0.5853 | 0.508 | 0.4341 | 0.4586 | -0.095 ± 0.0135 | -0.0071 (7) |
| 10-15 | 940 | 0.2103 | 0.2064 | +0.0039 ± 0.0037 | 0.6104 | 0.5972 | 0.5394 | 0.4162 | 0.4628 | -0.094 ± 0.0149 | -0.0317 (6) |
| 15-25 | 1131 | 0.2323 | 0.2159 | +0.0164 ± 0.0054 | 0.6626 | 0.617 | 0.5863 | 0.3919 | 0.4474 | -0.109 ± 0.0139 | -0.03 (1) |
| 25-40 | 716 | 0.2138 | 0.2147 | -0.0009 ± 0.0101 | 0.6169 | 0.6138 | 0.664 | 0.3531 | 0.5084 | -0.057 ± 0.0157 | 0.015 (2) |
| 40+ | 157 | 0.2959 | 0.1972 | +0.0987 ± 0.0312 | 0.8075 | 0.5755 | 0.7471 | 0.2961 | 0.4204 | -0.071 ± 0.0325 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4151 | 0.1828 | 0.1833 | -0.0005 ± 0.0002 | 0.5387 | 0.5395 | 0.482 | 0.4667 | 0.4821 | -0.036 ± 0.0067 | -0.0163 (35) |
| 3-5 | 2817 | 0.1994 | 0.1976 | +0.0018 ± 0.0007 | 0.5814 | 0.5746 | 0.4815 | 0.442 | 0.4395 | -0.060 ± 0.0085 | -0.0094 (18) |
| 5-10 | 6227 | 0.1945 | 0.1903 | +0.0042 ± 0.0008 | 0.5725 | 0.5579 | 0.4832 | 0.4092 | 0.418 | -0.050 ± 0.0056 | -0.01 (31) |
| 10-15 | 5026 | 0.1918 | 0.1783 | +0.0135 ± 0.0015 | 0.5672 | 0.5286 | 0.4935 | 0.3701 | 0.3766 | -0.058 ± 0.006 | -0.015 (12) |
| 15-25 | 6474 | 0.2122 | 0.1738 | +0.0385 ± 0.002 | 0.6181 | 0.5119 | 0.5124 | 0.3176 | 0.3176 | -0.070 ± 0.0052 | -0.03 (2) |
| 25-40 | 5048 | 0.2165 | 0.1297 | +0.0868 ± 0.0032 | 0.6265 | 0.395 | 0.5308 | 0.215 | 0.2379 | -0.047 ± 0.0049 | 0.01 (3) |
| 40+ | 3247 | 0.3939 | 0.0503 | +0.3436 ± 0.0044 | 1.0275 | 0.188 | 0.642 | 0.1115 | 0.0665 | -0.080 ± 0.0038 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1152 | 0.1958 | 0.1959 | -0.0002 ± 0.0005 | 0.5704 | 0.5705 | 0.5058 | 0.4907 | 0.4965 | -0.066 ± 0.0133 | -0.0224 (49) |
| 3-5 | 804 | 0.1883 | 0.1877 | +0.0006 ± 0.0012 | 0.5518 | 0.5495 | 0.496 | 0.4562 | 0.4664 | -0.064 ± 0.0157 | -0.0194 (34) |
| 5-10 | 1685 | 0.2014 | 0.1966 | +0.0048 ± 0.0016 | 0.5918 | 0.5766 | 0.5009 | 0.4273 | 0.4326 | -0.073 ± 0.011 | -0.005 (78) |
| 10-15 | 1157 | 0.2162 | 0.2042 | +0.0120 ± 0.0033 | 0.6244 | 0.5926 | 0.5343 | 0.4116 | 0.4226 | -0.083 ± 0.0137 | 0.0014 (64) |
| 15-25 | 1484 | 0.2319 | 0.2115 | +0.0205 ± 0.0047 | 0.661 | 0.6079 | 0.5805 | 0.3856 | 0.4326 | -0.081 ± 0.012 | -0.0214 (59) |
| 25-40 | 927 | 0.2433 | 0.2096 | +0.0336 ± 0.0092 | 0.696 | 0.6011 | 0.6811 | 0.3691 | 0.4714 | -0.091 ± 0.0141 | -0.0219 (26) |
| 40+ | 310 | 0.3392 | 0.2016 | +0.1376 ± 0.0247 | 0.9803 | 0.5885 | 0.8122 | 0.3347 | 0.4452 | -0.101 ± 0.0231 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4220 | 0.1751 | 0.1753 | -0.0002 ± 0.0002 | 0.519 | 0.5193 | 0.5117 | 0.4966 | 0.5076 | -0.038 ± 0.0065 | -0.0157 (88) |
| 3-5 | 2873 | 0.1933 | 0.1918 | +0.0015 ± 0.0007 | 0.5628 | 0.5598 | 0.5047 | 0.4648 | 0.4657 | -0.050 ± 0.0083 | -0.0209 (69) |
| 5-10 | 5858 | 0.1986 | 0.1915 | +0.0072 ± 0.0009 | 0.5844 | 0.5637 | 0.4967 | 0.423 | 0.4128 | -0.067 ± 0.0058 | -0.0082 (132) |
| 10-15 | 4122 | 0.2119 | 0.1965 | +0.0154 ± 0.0017 | 0.6149 | 0.5747 | 0.532 | 0.4091 | 0.4071 | -0.068 ± 0.007 | -0.0053 (105) |
| 15-25 | 4996 | 0.2294 | 0.2015 | +0.0280 ± 0.0025 | 0.6605 | 0.5823 | 0.566 | 0.3705 | 0.3973 | -0.061 ± 0.0064 | -0.0253 (107) |
| 25-40 | 3381 | 0.2596 | 0.1854 | +0.0742 ± 0.0047 | 0.7354 | 0.5415 | 0.6344 | 0.3214 | 0.362 | -0.080 ± 0.0072 | -0.0229 (51) |
| 40+ | 1463 | 0.3794 | 0.1506 | +0.2288 ± 0.0105 | 1.0721 | 0.4524 | 0.7355 | 0.2348 | 0.2679 | -0.079 ± 0.0096 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5395 | 1.017 ± 0.038 | 1.09 | 0.1687 | 0.1664 | 0.215 | 0.2064 |
| gen2 | 5395 | 0.808 ± 0.035 | 1.049 | 0.1701 | 0.1669 | 0.2349 | 0.2062 |
| gen1_elo | 5395 | 0.996 ± 0.037 | 1.088 | 0.1754 | 0.1666 | 0.2136 | 0.2065 |
| gen1_sr | 5395 | 0.989 ± 0.045 | 1.11 | 0.1305 | 0.1688 | 0.2307 | 0.2058 |
| gen1_ledger | 7519 | 0.854 ± 0.027 | 1.053 | 0.1866 | 0.1768 | 0.2183 | 0.2015 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 27,116)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,022 | 22.2% |
| STALE_QUOTE | market_freshness | 5,891 | 21.7% |
| BOOK_QUALITY | execution | 5,215 | 19.2% |
| POOR_DATA | data | 3,185 | 11.8% |
| LIMITED_DATA | data | 1,677 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,539 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,208 | 4.5% |
| IDENTITY_AMBIGUOUS | mapping | 1,115 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 795 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 468 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.2%, market_freshness 21.7%, execution 19.2%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.5%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.9%, THIN_PLAYER_HISTORY 60.8%, STALE_PLAYER_DATA 52.4%, STALE_KALSHI_QUOTE 43.8%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 25.2%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 15.8%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.8%, POST_SETTLEMENT_OBSERVATION 22.2%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 14,514)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,867 | 33.5% |
| STALE_QUOTE | market_freshness | 2,717 | 18.7% |
| BOOK_QUALITY | execution | 2,717 | 18.7% |
| POOR_DATA | data | 1,361 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 818 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 593 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 512 | 3.5% |
| LIMITED_DATA | data | 500 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 306 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 122 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.5%, market_freshness 18.7%, execution 18.7%, data 12.8%, market_freshness/coverage 9.2%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 63.1%, STALE_KALSHI_QUOTE 51.7%, STALE_PLAYER_DATA 46.7%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 24.5%, PLAYER_IDENTITY_RISK 18.6%, MODEL_HIGH_UNCERTAINTY 18.5%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.7%, POST_SETTLEMENT_OBSERVATION 33.5%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 11495, "IDENTITY_AMBIGUOUS": 3019}; ticker orientation: {"VERIFIED": 14514}.

Checks: discipline:AMBIGUOUS 935, discipline:PASS 13579, identity_confidence:AMBIGUOUS 2700, identity_confidence:PASS 11814, level_mapping:NA 947, level_mapping:PASS 13567, market_pair:AMBIGUOUS 478, market_pair:NA 343, market_pair:PASS 13693, model_complement:NA 307, model_complement:PASS 14207, namesake:AMBIGUOUS 6, namesake:PASS 14508, physical_match_id:NA 5068, physical_match_id:PASS 9446, player_ids:PASS 14514, same_pair_other_event:PASS 14514, ticker_orientation:PASS 14514

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,289 | 4.3% | 3.8% | 1.6% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.83 | 0.2196 / 0.2168 (609) | 21.3% | 3.0% | 3.3% | 2.9% |
| CHALLENGER | 9,719 | 16.5% | 6.3% | 11.1% | {"coverage": 941, "market_freshness/coverage": 195, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 74, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.27 | 0.2193 / 0.2104 (2231) | 35.1% | 15.8% | 4.1% | 22.6% |
| DOUBLES | 2,016 | 46.4% | 46.1% | 6.4% | {"execution": 529, "mapping": 235, "market_freshness": 106, "market_freshness/coverage": 58, "coverage": 7} | 23.41 | 0.3103 / 0.2379 (483) | 11.6% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 18,629 | 25.2% | 17.9% | 32.4% | {"coverage": 1633, "execution": 892, "market_freshness": 847, "data": 690, "market_freshness/coverage": 446, "mapping": 184, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.77 | 0.2169 / 0.2 (3840) | 37.0% | 70.4% | 17.2% | 21.3% |
| ITF_WOMEN | 24,545 | 26.8% | 19.5% | 45.3% | {"coverage": 2237, "market_freshness": 1401, "execution": 1183, "data": 934, "market_freshness/coverage": 561, "mapping": 151, "model_calibration_or_unknown": 81, "model_calibration": 21} | 12.65 | 0.2048 / 0.1965 (4492) | 39.1% | 57.9% | 10.2% | 21.3% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,808 | 5.7% | 5.0% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "execution": 27, "coverage": 23, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.58 | 0.2347 / 0.2278 (591) | 25.9% | 1.1% | 1.4% | 3.4% |
| WTA125 | 2,102 | 11.7% | 9.9% | 1.7% | {"market_freshness": 64, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.2 | 0.2082 / 0.1918 (626) | 25.3% | 11.7% | 5.1% | 7.6% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 172 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 6 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 7 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 8 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 9 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 20.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1203 min (STALE); no external reference |
| 12 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 13 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 16 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 17 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 18 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 19 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 20 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 21 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 22 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 23 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 24 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 25 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 26 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 27 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 30 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 31 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 32 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 33 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 34 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 35 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 36 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 37 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 39 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 40 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 41 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 42 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 43 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 44 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 46 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 48 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 49 | `KXITFMATCH-26OCT28DELBAR-BAR` | ITF_MEN | fair_v1 | 84% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.5h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 216 min (STALE); data POOR (grade F, thinner serve sample 803.0, ratio 2.48); no external reference |
| 50 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9693, "by_level_share_of_ge_25pp": {"ATP": 0.0156, "CHALLENGER": 0.1108, "DOUBLES": 0.0644, "ITF_MEN": 0.3238, "ITF_WOMEN": 0.4526, "OTHER": 0.0008, "WTA": 0.015, "WTA125": 0.0169}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5167, "share_primary_cause_market_settled_or_in_play": 0.427, "share_primary_cause_stale_quote_only": 0.1872}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 14514, "identity_ambiguous_share": 0.208, "ticker_orientation": {"VERIFIED": 14514}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9446, "with_external": 492, "coverage": 0.0521, "external_status": {"EXTERNAL_STALE": 299, "AGREES_WITH_KALSHI": 181, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 299, "MODEL_LONE_OUTLIER": 181, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3679, "share_external_supports_model": 0.0244}, "pregame_clean_ge_25pp": {"n": 4577, "with_external": 467, "coverage": 0.102, "external_status": {"EXTERNAL_STALE": 281, "AGREES_WITH_KALSHI": 174, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 281, "MODEL_LONE_OUTLIER": 174, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3726, "share_external_supports_model": 0.0257}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 454.0, "median_sample_ratio": 2.5, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2128, "data_status": {"POOR": 8291, "LIMITED": 3693, "ADEQUATE": 2530}, "comparison_lt_10pp": {"median_thinner_serve_points": 1651.0, "median_sample_ratio": 1.73, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1085, "model_minus_observed": 0.0505, "kalshi_minus_observed": -0.0881, "brier_diff_model_minus_kalshi": -0.0023}, "4-10x": {"n": 745, "model_minus_observed": 0.0858, "kalshi_minus_observed": -0.06, "brier_diff_model_minus_kalshi": 0.0086}, "<2x": {"n": 2615, "model_minus_observed": 0.0882, "kalshi_minus_observed": -0.0353, "brier_diff_model_minus_kalshi": 0.0109}, ">=10x": {"n": 950, "model_minus_observed": 0.121, "kalshi_minus_observed": -0.0541, "brier_diff_model_minus_kalshi": 0.0146}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5395, "model": {"intercept": -0.536, "slope": 0.808, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.192, "slope": 1.049, "slope_se": 0.038}, "mean_extremity_model": 0.1701, "mean_extremity_kalshi": 0.1669, "model_brier": 0.2349, "kalshi_brier": 0.2062, "brier_diff_model_minus_kalshi": 0.0287, "brier_diff_se": 0.0026, "model_logloss": 0.6672, "kalshi_logloss": 0.5954}, "fair_v1": {"n": 5395, "model": {"intercept": -0.411, "slope": 1.017, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.285, "slope": 1.09, "slope_se": 0.039}, "mean_extremity_model": 0.1687, "mean_extremity_kalshi": 0.1664, "model_brier": 0.215, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": 0.0086, "brier_diff_se": 0.0021, "model_logloss": 0.6188, "kalshi_logloss": 0.5957}, "gen1_elo": {"n": 5395, "model": {"intercept": -0.386, "slope": 0.996, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.306, "slope": 1.088, "slope_se": 0.038}, "mean_extremity_model": 0.1754, "mean_extremity_kalshi": 0.1666, "model_brier": 0.2136, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0071, "brier_diff_se": 0.0021, "model_logloss": 0.6164, "kalshi_logloss": 0.596}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2481, "share_ge_15": 0.4425, "median_abs_gap": 13.01, "n": 38079}, "gen1_elo": {"share_ge_25": 0.2461, "share_ge_15": 0.4408, "median_abs_gap": 12.93, "n": 38079}, "gen1_sr": {"share_ge_25": 0.314, "share_ge_15": 0.5211, "median_abs_gap": 15.9, "n": 38079}, "gen2": {"share_ge_25": 0.3169, "share_ge_15": 0.511, "median_abs_gap": 15.49, "n": 38079}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1546, "share_ge_15": 0.3561, "median_abs_gap": 10.77, "n": 29596}, "gen1_elo": {"share_ge_25": 0.1546, "share_ge_15": 0.3535, "median_abs_gap": 10.56, "n": 29595}, "gen1_sr": {"share_ge_25": 0.2205, "share_ge_15": 0.4433, "median_abs_gap": 13.04, "n": 29597}, "gen2": {"share_ge_25": 0.2364, "share_ge_15": 0.4426, "median_abs_gap": 12.98, "n": 29598}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.83, "share_ge_25_all": 0.0429, "share_ge_25_pregame_clean": 0.0383}, "WTA": {"median_abs_gap_pregame_clean": 7.58, "share_ge_25_all": 0.0572, "share_ge_25_pregame_clean": 0.05}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2373, "share_within_10pp_all": 0.4373, "share_within_10pp_pregame_clean": 0.4892, "corr_model_vs_mid_pregame_clean": 0.8496}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 799, "model_brier": 0.1978, "kalshi_brier": 0.1982, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 942, "model_brier": 0.222, "kalshi_brier": 0.2133, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1196, "model_brier": 0.2251, "kalshi_brier": 0.2122, "brier_diff_model_minus_kalshi": 0.0129}, "25-40": {"n_settled": 701, "model_brier": 0.2234, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": 0.0158}, "3-5": {"n_settled": 483, "model_brier": 0.2057, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": -0.0007}, "40+": {"n_settled": 147, "model_brier": 0.2778, "kalshi_brier": 0.1891, "brier_diff_model_minus_kalshi": 0.0887}, "5-10": {"n_settled": 1127, "model_brier": 0.201, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": -0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.536, "slope": 0.808, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.192, "slope": 1.049, "slope_se": 0.038}, "n": 5395}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.486, "slope": 0.854, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.166, "slope": 1.053, "slope_se": 0.032}, "n": 7519}, "NO_SKILL:gen2|WTA": {"n_settled": 235, "model_brier": 0.2568, "kalshi_brier": 0.2361, "brier_diff_model_minus_kalshi": 0.0207, "brier_diff_se": 0.0103, "corr_model_outcome": 0.2213, "corr_kalshi_outcome": 0.2536}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 483, "model_brier": 0.3103, "kalshi_brier": 0.2379, "brier_diff_model_minus_kalshi": 0.0724, "brier_diff_se": 0.0137, "corr_model_outcome": 0.0513, "corr_kalshi_outcome": 0.2334}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
