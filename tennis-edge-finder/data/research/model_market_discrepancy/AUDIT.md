# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-28T13:20Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 64,734): 0-3 14.2%, 3-5 9.6%, 5-10 20.0%, 10-15 15.4%, 15-25 19.0%, 25-40 13.9%, 40+ 7.9%; median gap 11.87 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.3%, Challenger 11.3%, doubles 6.4%). Main tour: ATP 4.3% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 14,139): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.2%, BOOK_QUALITY 18.9%, STALE_QUOTE 18.8%, POOR_DATA 9.5%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.1%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.2%, execution 18.9%, market_freshness 18.8%, data 13.0%, market_freshness/coverage 8.9%, mapping 4.1%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 14,139 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 451.0 points vs 1680.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.017, Gen-2 0.806, Gen-1 ledger 0.854 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 676 model 0.2238 vs Kalshi 0.2082; n 143 model 0.2752 vs Kalshi 0.1915.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 278,205 model-market comparisons (452,725 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 93,324 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-28T13:09:03.411239+00:00'], shadow board 73,946 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-28T13:09:06.987586+00:00'], Model 4 35,314 rows, 22,602 settled tickers, 8,268 tickers with an external scan.
* By model: {"gen1_ledger": 63061, "gen1_elo": 37174, "fair_v1": 37174, "gen2": 37174, "gen1_sr": 37174, "model4_fundamental": 33246, "model4_conditioned": 33202}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 64,734 | 14.2 | 9.6 | 20.0 | 15.4 | 19.0 | 13.9 | 7.9 | 11.87 | 40.9% | 21.8% |
| MW fair_v1 | 37,174 | 13.1 | 8.7 | 18.6 | 15.5 | 19.4 | 15.0 | 9.7 | 13.0 | 44.1% | 24.7% |
| MW gen1_elo | 37,174 | 12.8 | 8.6 | 19.3 | 15.4 | 19.5 | 14.9 | 9.6 | 12.84 | 43.9% | 24.5% |
| MW gen1_ledger | 27,560 | 15.7 | 10.7 | 21.9 | 15.2 | 18.5 | 12.4 | 5.6 | 10.41 | 36.5% | 18.0% |
| MW gen1_sr | 37,174 | 10.2 | 7.2 | 16.8 | 13.7 | 20.8 | 18.7 | 12.7 | 15.9 | 52.1% | 31.4% |
| MW gen2 | 37,174 | 11.1 | 7.5 | 16.4 | 13.9 | 19.4 | 17.9 | 13.8 | 15.49 | 51.1% | 31.7% |
| all families model4_conditioned | 33,202 | 22.2 | 18.2 | 34.4 | 17.3 | 4.8 | 1.9 | 1.1 | 6.03 | 7.8% | 3.0% |
| all families model4_fundamental | 33,246 | 17.2 | 13.2 | 34.0 | 20.3 | 10.2 | 3.6 | 1.4 | 7.72 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.2%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 7.9%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.27pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,306 | 27.1 | 15.6 | 27.4 | 13.6 | 11.7 | 4.1 | 0.6 | 5.92 | 16.4% | 4.7% |
| CHALLENGER | 5,733 | 16.2 | 9.8 | 20.5 | 15.5 | 15.4 | 11.9 | 10.7 | 10.97 | 38.1% | 22.6% |
| ITF_MEN | 10,187 | 10.0 | 7.3 | 16.8 | 15.1 | 21.0 | 17.7 | 12.1 | 15.26 | 50.8% | 29.8% |
| ITF_WOMEN | 14,555 | 9.8 | 7.0 | 16.0 | 15.1 | 22.0 | 18.3 | 11.7 | 15.64 | 52.1% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,362 | 17.7 | 13.9 | 24.5 | 20.2 | 16.4 | 6.6 | 0.6 | 8.25 | 23.7% | 7.2% |
| WTA125 | 1,025 | 15.9 | 7.4 | 22.9 | 19.2 | 20.2 | 12.7 | 1.7 | 10.7 | 34.5% | 14.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,306 | 25.7 | 15.6 | 25.2 | 16.5 | 12.0 | 4.1 | 0.8 | 6.23 | 16.9% | 4.9% |
| CHALLENGER | 5,733 | 15.2 | 8.9 | 18.0 | 14.6 | 18.1 | 13.7 | 11.6 | 12.67 | 43.5% | 25.4% |
| ITF_MEN | 10,187 | 7.9 | 6.1 | 14.6 | 13.5 | 19.7 | 20.8 | 17.3 | 18.33 | 57.9% | 38.1% |
| ITF_WOMEN | 14,555 | 8.0 | 5.7 | 14.1 | 12.8 | 20.6 | 21.4 | 17.4 | 19.2 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,362 | 14.9 | 10.8 | 22.0 | 15.6 | 22.3 | 12.9 | 1.6 | 10.71 | 36.8% | 14.5% |
| WTA125 | 1,025 | 9.1 | 6.2 | 16.4 | 17.0 | 24.6 | 17.8 | 9.0 | 15.68 | 51.3% | 26.7% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,306 | 22.5 | 12.9 | 24.4 | 16.1 | 16.2 | 6.5 | 1.4 | 7.58 | 24.1% | 7.9% |
| CHALLENGER | 5,733 | 15.0 | 9.2 | 21.2 | 15.8 | 15.6 | 12.2 | 10.9 | 11.29 | 38.8% | 23.2% |
| ITF_MEN | 10,187 | 9.5 | 7.1 | 17.2 | 14.2 | 21.6 | 18.2 | 12.3 | 15.77 | 52.1% | 30.4% |
| ITF_WOMEN | 14,555 | 9.5 | 6.8 | 16.4 | 15.9 | 22.1 | 18.1 | 11.1 | 15.46 | 51.3% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,362 | 23.6 | 16.3 | 31.8 | 14.9 | 9.6 | 2.5 | 1.1 | 6.12 | 13.3% | 3.7% |
| WTA125 | 1,025 | 22.3 | 12.8 | 26.5 | 16.6 | 14.9 | 6.4 | 0.4 | 7.94 | 21.8% | 6.8% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,916 | 24.6 | 19.1 | 30.9 | 12.8 | 9.0 | 3.1 | 0.5 | 5.67 | 12.6% | 3.6% |
| CHALLENGER | 3,911 | 22.5 | 14.5 | 26.9 | 14.6 | 13.8 | 6.1 | 1.6 | 7.16 | 21.5% | 7.6% |
| DOUBLES | 1,963 | 5.1 | 4.6 | 12.3 | 10.5 | 21.1 | 25.1 | 21.3 | 23.56 | 67.5% | 46.4% |
| ITF_MEN | 7,842 | 13.1 | 9.3 | 20.8 | 15.9 | 21.5 | 13.3 | 6.2 | 12.08 | 41.0% | 19.5% |
| ITF_WOMEN | 9,335 | 13.1 | 9.0 | 19.7 | 15.6 | 21.4 | 15.6 | 5.8 | 12.5 | 42.8% | 21.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,404 | 24.4 | 15.4 | 29.8 | 17.9 | 9.4 | 2.9 | 0.3 | 6.76 | 12.5% | 3.1% |
| WTA125 | 1,040 | 24.6 | 12.6 | 20.8 | 19.4 | 13.3 | 7.6 | 1.7 | 8.03 | 22.6% | 9.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,216 | 27.4 | 15.8 | 27.8 | 13.5 | 11.4 | 3.8 | 0.4 | 5.87 | 15.6% | 4.2% |
| CHALLENGER | 4,031 | 21.1 | 12.3 | 25.6 | 18.0 | 15.2 | 6.2 | 1.5 | 8.1 | 23.0% | 7.8% |
| ITF_MEN | 7,581 | 12.1 | 8.7 | 20.1 | 17.2 | 21.9 | 14.6 | 5.4 | 12.52 | 41.9% | 20.0% |
| ITF_WOMEN | 10,977 | 11.6 | 8.3 | 18.3 | 17.2 | 23.9 | 15.3 | 5.3 | 13.38 | 44.6% | 20.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,290 | 17.9 | 13.8 | 24.6 | 20.5 | 16.5 | 6.1 | 0.6 | 8.25 | 23.1% | 6.7% |
| WTA125 | 990 | 16.2 | 7.3 | 22.5 | 19.5 | 20.7 | 12.4 | 1.4 | 10.87 | 34.5% | 13.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,216 | 26.0 | 15.9 | 25.3 | 16.5 | 11.9 | 3.9 | 0.5 | 6.2 | 16.3% | 4.3% |
| CHALLENGER | 4,031 | 19.5 | 11.3 | 22.6 | 17.0 | 18.4 | 9.3 | 1.9 | 9.08 | 29.6% | 11.2% |
| ITF_MEN | 7,582 | 9.3 | 7.3 | 16.9 | 15.6 | 21.5 | 19.0 | 10.4 | 15.36 | 50.9% | 29.4% |
| ITF_WOMEN | 10,978 | 8.9 | 6.5 | 15.8 | 14.2 | 22.7 | 20.9 | 11.0 | 16.82 | 54.6% | 31.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,290 | 15.0 | 10.8 | 22.1 | 15.7 | 22.4 | 12.8 | 1.3 | 10.64 | 36.5% | 14.1% |
| WTA125 | 990 | 9.1 | 6.3 | 16.5 | 17.3 | 24.4 | 18.1 | 8.4 | 15.37 | 50.9% | 26.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,863 | 24.7 | 19.4 | 30.9 | 13.0 | 8.6 | 3.0 | 0.4 | 5.65 | 12.0% | 3.4% |
| CHALLENGER | 3,449 | 23.9 | 15.4 | 28.1 | 14.7 | 13.2 | 4.2 | 0.4 | 6.6 | 17.8% | 4.6% |
| DOUBLES | 1,838 | 5.1 | 4.7 | 12.5 | 10.7 | 21.0 | 24.9 | 21.2 | 23.51 | 67.1% | 46.1% |
| ITF_MEN | 6,709 | 13.9 | 9.9 | 22.4 | 16.6 | 21.4 | 11.8 | 4.0 | 11.13 | 37.2% | 15.8% |
| ITF_WOMEN | 7,941 | 13.8 | 9.4 | 20.9 | 16.3 | 21.5 | 14.5 | 3.6 | 11.66 | 39.6% | 18.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,350 | 24.7 | 15.8 | 29.9 | 17.9 | 9.4 | 2.2 | 0.1 | 6.59 | 11.7% | 2.3% |
| WTA125 | 919 | 26.1 | 13.4 | 21.9 | 20.7 | 12.1 | 5.3 | 0.5 | 7.35 | 17.9% | 5.9% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,963 | 5.1 | 4.6 | 12.3 | 10.5 | 21.1 | 25.1 | 21.3 | 23.56 | 67.5% | 46.4% |
| singles | 25,597 | 16.5 | 11.2 | 22.6 | 15.6 | 18.3 | 11.4 | 4.4 | 9.91 | 34.1% | 15.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,637 | 13.1 | 9.3 | 20.0 | 15.6 | 19.1 | 13.8 | 9.1 | 12.41 | 42.0% | 22.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 24,096 | 13.6 | 8.8 | 18.5 | 15.2 | 19.2 | 15.2 | 9.6 | 12.94 | 44.0% | 24.8% |
| UNKNOWN | 5,192 | 10.7 | 7.6 | 17.1 | 16.8 | 20.8 | 16.0 | 11.0 | 14.11 | 47.9% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,451 | 19.9 | 12.3 | 22.2 | 15.8 | 14.8 | 9.2 | 5.8 | 8.65 | 29.8% | 15.0% |
| B | 4,541 | 12.8 | 8.7 | 19.1 | 16.4 | 19.4 | 12.9 | 10.7 | 12.62 | 43.0% | 23.6% |
| C | 5,225 | 12.3 | 9.0 | 19.9 | 15.8 | 18.6 | 14.3 | 10.1 | 12.71 | 43.0% | 24.4% |
| D | 5,793 | 12.4 | 8.2 | 17.6 | 15.4 | 21.2 | 15.9 | 9.4 | 13.67 | 46.4% | 25.2% |
| F | 11,164 | 7.5 | 5.6 | 15.0 | 14.6 | 23.2 | 21.1 | 12.9 | 17.82 | 57.3% | 34.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,449 | 24.2 | 15.8 | 28.6 | 15.2 | 11.0 | 3.8 | 1.4 | 6.52 | 16.2% | 5.2% |
| B | 3,788 | 16.8 | 10.1 | 24.3 | 16.4 | 19.1 | 10.0 | 3.3 | 9.75 | 32.4% | 13.3% |
| C | 5,323 | 11.3 | 7.9 | 19.3 | 14.6 | 21.2 | 15.5 | 10.2 | 13.48 | 46.9% | 25.7% |
| D | 3,974 | 14.5 | 9.9 | 21.3 | 15.4 | 20.3 | 13.1 | 5.6 | 11.28 | 38.9% | 18.6% |
| F | 7,026 | 10.0 | 8.3 | 15.9 | 14.9 | 23.1 | 20.0 | 7.8 | 15.49 | 50.9% | 27.9% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,847 | 18.2 | 11.1 | 21.3 | 15.6 | 15.2 | 10.1 | 8.5 | 9.82 | 33.8% | 18.5% |
| LIMITED | 8,011 | 13.9 | 10.0 | 20.3 | 16.3 | 19.0 | 13.3 | 7.2 | 11.64 | 39.5% | 20.5% |
| POOR | 17,316 | 9.2 | 6.5 | 16.0 | 15.0 | 22.5 | 19.2 | 11.7 | 16.1 | 53.3% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,233 | 24.3 | 18.3 | 33.3 | 14.8 | 6.4 | 2.6 | 0.4 | 5.81 | 9.3% | 2.9% |
| GAME_SPREAD | 5,678 | 22.2 | 15.3 | 33.0 | 17.1 | 9.0 | 2.8 | 0.6 | 6.74 | 12.4% | 3.4% |
| MATCH_WINNER | 27,560 | 15.7 | 10.7 | 21.9 | 15.2 | 18.5 | 12.4 | 5.6 | 10.41 | 36.5% | 18.0% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,134 | 27.6 | 16.6 | 31.3 | 12.5 | 9.4 | 2.4 | 0.3 | 5.68 | 12.1% | 2.7% |
| TOTAL_GAMES | 9,432 | 9.2 | 10.2 | 36.1 | 26.9 | 10.6 | 4.1 | 2.8 | 9.34 | 17.5% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,791 | 24.5 | 30.5 | 33.0 | 7.1 | 3.9 | 0.8 | 0.2 | 4.68 | 4.9% | 1.0% |
| GAME_SPREAD | 7,772 | 47.1 | 16.1 | 25.6 | 7.3 | 2.1 | 1.2 | 0.6 | 3.29 | 3.9% | 1.8% |
| TOTAL_GAMES | 13,639 | 6.1 | 8.8 | 40.7 | 31.8 | 7.2 | 3.1 | 2.2 | 9.38 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,802 | 23.9 | 16.9 | 34.9 | 14.3 | 7.1 | 2.5 | 0.4 | 6.0 | 10.0% | 2.9% |
| GAME_SPREAD | 7,775 | 20.0 | 13.4 | 28.2 | 20.5 | 12.4 | 4.3 | 1.1 | 7.82 | 17.8% | 5.4% |
| TOTAL_GAMES | 13,669 | 9.8 | 10.0 | 36.5 | 25.4 | 11.6 | 4.2 | 2.4 | 9.23 | 18.2% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 37,174 | 44.1% | 24.7% | 13.0 | 35.7% | 15.5% | 10.78 |
| gen1_elo | 37,174 | 43.9% | 24.5% | 12.84 | 35.4% | 15.5% | 10.57 |
| gen1_sr | 37,174 | 52.1% | 31.4% | 15.9 | 44.5% | 22.2% | 13.06 |
| gen2 | 37,174 | 51.1% | 31.7% | 15.49 | 44.4% | 23.8% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,199 | 15.6 | 10.6 | 21.3 | 17.2 | 20.0 | 12.0 | 3.4 | 10.71 | 35.4% | 15.4% |
| STALE | 18,975 | 10.6 | 7.0 | 16.1 | 13.8 | 18.9 | 17.9 | 15.8 | 16.09 | 52.5% | 33.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 21,028 | 16.4 | 11.1 | 22.6 | 15.4 | 17.9 | 11.9 | 4.8 | 9.97 | 34.5% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 64,734 | 21028 | 21671 | 22035 | 24.1 | 114.0 | 1400.4 |
| ge_15pp | 26,457 | 7258 | 7724 | 11475 | 26.5 | 415.5 | 1399.2 |
| ge_25pp | 14,139 | 3494 | 3391 | 7254 | 31.2 | 568.2 | 1380.4 |
| lt_10pp | 28,335 | 10540 | 10268 | 7527 | 22.4 | 46.9 | 1341.5 |

Current slate `SL-20261028T132021Z-8f2252e3`: 702 priced rows, quote age at build {'median': 11.7, 'max': 11.7}, freshness {'AGING': 702}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 43 | 0.0 | 0.0 | 32.6 | 7.0 | 34.9 | 23.3 | 2.3 | 20.19 | 60.5% | 25.6% |
| EXTERNAL_LONE_OUTLIER | 21 | 76.2 | 23.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,669 | 20.0 | 11.2 | 25.0 | 18.1 | 17.7 | 7.2 | 0.8 | 8.64 | 25.8% | 8.0% |
| KALSHI_LONE_OUTLIER | 26 | 3.9 | 3.9 | 76.9 | 7.7 | 3.9 | 3.9 | 0.0 | 6.31 | 7.7% | 3.9% |
| MARKETS_AGREE | 723 | 65.2 | 34.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.26 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,567 | 0.0 | 2.5 | 35.6 | 26.2 | 24.5 | 10.4 | 0.8 | 12.19 | 35.7% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 37,174 | 6049 (16.3%) | 25.9% | 1.1% | {"EXTERNAL_STALE": 3669, "AGREES_WITH_KALSHI": 1567, "ALL_AGREE": 723, "SUPPORTS_MODEL_DIRECTION": 42, "AGREES_WITH_MODEL": 26, "EXTERNAL_OUTLIER": 21, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 16,400 | 1533 (9.3%) | 36.5% | 1.8% | {"EXTERNAL_STALE": 945, "AGREES_WITH_KALSHI": 560, "SUPPORTS_MODEL_DIRECTION": 26, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,183 | 483 (5.3%) | 36.4% | 2.5% | {"EXTERNAL_STALE": 295, "AGREES_WITH_KALSHI": 176, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,522 | 458 (10.1%) | 36.9% | 2.6% | {"EXTERNAL_STALE": 277, "AGREES_WITH_KALSHI": 169, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 15,026 | 3438 (22.9%) | 17.4% | 1.0% | {"EXTERNAL_STALE": 2061, "ALL_AGREE": 723, "AGREES_WITH_KALSHI": 597, "AGREES_WITH_MODEL": 22, "EXTERNAL_OUTLIER": 21, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,239 | 10.6 | 7.4 | 19.6 | 14.5 | 21.5 | 16.6 | 9.8 | 14.01 | 47.9% | 26.4% |
| 4-10x | 4,951 | 11.4 | 8.6 | 18.6 | 15.4 | 21.6 | 14.6 | 9.8 | 13.57 | 46.0% | 24.5% |
| <2x | 18,866 | 15.2 | 10.1 | 19.4 | 16.2 | 17.4 | 13.1 | 8.7 | 11.57 | 39.2% | 21.8% |
| >=10x | 6,118 | 10.7 | 6.4 | 15.2 | 14.4 | 21.5 | 19.3 | 12.6 | 16.28 | 53.4% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,383 | 12.8 | 8.6 | 19.5 | 16.2 | 19.0 | 13.6 | 10.2 | 12.69 | 42.8% | 23.8% |
| 300-1000 | 7,910 | 12.3 | 8.7 | 17.7 | 15.3 | 20.1 | 16.4 | 9.4 | 13.51 | 45.9% | 25.8% |
| <300 | 12,168 | 8.4 | 5.8 | 15.3 | 14.8 | 22.9 | 20.2 | 12.7 | 17.03 | 55.7% | 32.9% |
| >=3000 | 7,713 | 21.4 | 13.5 | 23.8 | 15.8 | 13.8 | 7.2 | 4.6 | 7.58 | 25.6% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1042 | 0.5486 | 0.4101 | 0.4952 | +0.053 | -0.085 | -0.0015 ± 0.0048 |
| ratio 4-10x | 716 | 0.5821 | 0.4368 | 0.4972 | +0.085 | -0.060 | 0.0081 ± 0.0059 |
| ratio <2x | 2542 | 0.5377 | 0.4135 | 0.4496 | +0.088 | -0.036 | 0.011 ± 0.0029 |
| ratio >=10x | 922 | 0.5691 | 0.3932 | 0.4523 | +0.117 | -0.059 | 0.0126 ± 0.006 |
| thinner_sample 1000-3000 | 1400 | 0.5382 | 0.4111 | 0.4529 | +0.085 | -0.042 | 0.0081 ± 0.0039 |
| thinner_sample 300-1000 | 1175 | 0.568 | 0.4254 | 0.4894 | +0.079 | -0.064 | 0.0023 ± 0.0047 |
| thinner_sample <300 | 1775 | 0.5598 | 0.3918 | 0.4608 | +0.099 | -0.069 | 0.0103 ± 0.0042 |
| thinner_sample >=3000 | 872 | 0.5335 | 0.439 | 0.4644 | +0.069 | -0.025 | 0.0131 ± 0.0039 |
| data_status ADEQUATE | 1461 | 0.5344 | 0.4305 | 0.4476 | +0.087 | -0.017 | 0.0132 ± 0.0032 |
| data_status LIMITED | 1224 | 0.5496 | 0.416 | 0.4861 | +0.064 | -0.070 | 0.003 ± 0.0043 |
| data_status POOR | 2537 | 0.5622 | 0.4003 | 0.4663 | +0.096 | -0.066 | 0.0083 ± 0.0035 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 764 | 0.2002 | 0.2008 | -0.0006 ± 0.0006 | 0.5804 | 0.5819 | 0.5033 | 0.4882 | 0.5144 | -0.083 ± 0.0173 | -0.01 (5) |
| 3-5 | 470 | 0.207 | 0.2076 | -0.0007 ± 0.0017 | 0.5979 | 0.5979 | 0.5043 | 0.4644 | 0.4915 | -0.092 ± 0.0215 | 0.02 (1) |
| 5-10 | 1083 | 0.2021 | 0.2022 | -0.0000 ± 0.0021 | 0.5902 | 0.5877 | 0.511 | 0.4371 | 0.4709 | -0.091 ± 0.0141 | -0.0167 (6) |
| 10-15 | 920 | 0.2207 | 0.212 | +0.0087 ± 0.0038 | 0.6341 | 0.6096 | 0.5271 | 0.4033 | 0.4293 | -0.107 ± 0.0153 | -0.048 (5) |
| 15-25 | 1166 | 0.2245 | 0.2124 | +0.0122 ± 0.0053 | 0.6444 | 0.6092 | 0.5754 | 0.3797 | 0.4468 | -0.097 ± 0.0135 | -0.0033 (9) |
| 25-40 | 676 | 0.2238 | 0.2082 | +0.0156 ± 0.0105 | 0.6377 | 0.5987 | 0.6558 | 0.3458 | 0.4749 | -0.075 ± 0.0161 | -0.01 (1) |
| 40+ | 143 | 0.2752 | 0.1915 | +0.0836 ± 0.0318 | 0.7497 | 0.5632 | 0.7392 | 0.2903 | 0.4266 | -0.064 ± 0.0311 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4039 | 0.1831 | 0.1838 | -0.0007 ± 0.0002 | 0.5413 | 0.5419 | 0.4858 | 0.4705 | 0.4954 | -0.030 ± 0.0069 | -0.0129 (17) |
| 3-5 | 2717 | 0.1964 | 0.1948 | +0.0017 ± 0.0007 | 0.5726 | 0.5663 | 0.4849 | 0.4451 | 0.4431 | -0.058 ± 0.0086 | 0.0 (2) |
| 5-10 | 5740 | 0.2017 | 0.1978 | +0.0039 ± 0.0009 | 0.589 | 0.5758 | 0.4846 | 0.4107 | 0.4207 | -0.051 ± 0.0059 | -0.0119 (21) |
| 10-15 | 4942 | 0.2028 | 0.1866 | +0.0162 ± 0.0015 | 0.5923 | 0.5486 | 0.4855 | 0.3613 | 0.358 | -0.067 ± 0.0062 | -0.0281 (16) |
| 15-25 | 6097 | 0.2082 | 0.1689 | +0.0393 ± 0.0021 | 0.6094 | 0.5011 | 0.5005 | 0.3042 | 0.3028 | -0.073 ± 0.0052 | -0.0025 (44) |
| 25-40 | 4853 | 0.2233 | 0.1265 | +0.0968 ± 0.0032 | 0.6408 | 0.3887 | 0.5281 | 0.2144 | 0.2213 | -0.061 ± 0.005 | -0.01 (1) |
| 40+ | 3123 | 0.379 | 0.0454 | +0.3336 ± 0.0043 | 0.9868 | 0.1751 | 0.63 | 0.1039 | 0.0628 | -0.076 ± 0.0036 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 599 | 0.2065 | 0.2072 | -0.0007 ± 0.0007 | 0.5948 | 0.5966 | 0.5098 | 0.4947 | 0.5175 | -0.108 ± 0.0202 | -0.01 (3) |
| 3-5 | 421 | 0.2279 | 0.2246 | +0.0032 ± 0.0018 | 0.6427 | 0.636 | 0.51 | 0.4702 | 0.4442 | -0.141 ± 0.0247 | 0.02 (1) |
| 5-10 | 942 | 0.2076 | 0.2069 | +0.0007 ± 0.0022 | 0.6009 | 0.599 | 0.5505 | 0.4755 | 0.5106 | -0.088 ± 0.0153 | -0.01 (4) |
| 10-15 | 853 | 0.2182 | 0.2119 | +0.0063 ± 0.0039 | 0.6277 | 0.6113 | 0.5645 | 0.4403 | 0.4795 | -0.106 ± 0.0165 | -0.04 (5) |
| 15-25 | 1222 | 0.2298 | 0.2135 | +0.0163 ± 0.0052 | 0.6542 | 0.6112 | 0.5823 | 0.387 | 0.446 | -0.098 ± 0.0135 | -0.0133 (9) |
| 25-40 | 862 | 0.2673 | 0.1984 | +0.0689 ± 0.0095 | 0.7465 | 0.5782 | 0.6547 | 0.3407 | 0.391 | -0.125 ± 0.0152 | -0.0075 (4) |
| 40+ | 323 | 0.3622 | 0.1655 | +0.1967 ± 0.0224 | 0.991 | 0.4979 | 0.7315 | 0.2465 | 0.3003 | -0.082 ± 0.0219 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3433 | 0.1911 | 0.1913 | -0.0002 ± 0.0003 | 0.5586 | 0.5587 | 0.5097 | 0.4947 | 0.506 | -0.046 ± 0.0077 | -0.0133 (15) |
| 3-5 | 2317 | 0.1988 | 0.1973 | +0.0015 ± 0.0007 | 0.5754 | 0.5715 | 0.5141 | 0.4744 | 0.4739 | -0.055 ± 0.0095 | 0.02 (1) |
| 5-10 | 5127 | 0.1986 | 0.1951 | +0.0035 ± 0.0009 | 0.5826 | 0.5693 | 0.5164 | 0.4423 | 0.4586 | -0.044 ± 0.0063 | -0.0117 (6) |
| 10-15 | 4388 | 0.206 | 0.1941 | +0.0120 ± 0.0017 | 0.6025 | 0.5661 | 0.5132 | 0.3893 | 0.4041 | -0.053 ± 0.0068 | -0.0189 (18) |
| 15-25 | 6135 | 0.2175 | 0.1802 | +0.0373 ± 0.0021 | 0.632 | 0.5296 | 0.5222 | 0.3266 | 0.3328 | -0.066 ± 0.0055 | -0.0086 (42) |
| 25-40 | 5654 | 0.2522 | 0.1375 | +0.1146 ± 0.0031 | 0.71 | 0.4216 | 0.5573 | 0.2409 | 0.2209 | -0.085 ± 0.0049 | -0.0044 (18) |
| 40+ | 4457 | 0.3957 | 0.059 | +0.3367 ± 0.0042 | 1.041 | 0.2128 | 0.6504 | 0.1179 | 0.0814 | -0.073 ± 0.0036 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 736 | 0.1978 | 0.1999 | -0.0021 ± 0.0006 | 0.5751 | 0.5803 | 0.5009 | 0.4856 | 0.5448 | -0.038 ± 0.0172 | -0.0137 (8) |
| 3-5 | 508 | 0.2039 | 0.2022 | +0.0017 ± 0.0016 | 0.5912 | 0.585 | 0.4999 | 0.4601 | 0.4606 | -0.121 ± 0.0208 | 0.0067 (3) |
| 5-10 | 1123 | 0.2028 | 0.2009 | +0.0019 ± 0.002 | 0.5914 | 0.5846 | 0.5096 | 0.4358 | 0.4595 | -0.096 ± 0.0137 | -0.0071 (7) |
| 10-15 | 912 | 0.2119 | 0.2082 | +0.0037 ± 0.0037 | 0.614 | 0.6014 | 0.5386 | 0.4154 | 0.4627 | -0.092 ± 0.0152 | -0.0317 (6) |
| 15-25 | 1101 | 0.2319 | 0.2156 | +0.0162 ± 0.0055 | 0.6615 | 0.6164 | 0.5873 | 0.3927 | 0.4487 | -0.109 ± 0.014 | -0.03 (1) |
| 25-40 | 688 | 0.2139 | 0.2148 | -0.0009 ± 0.0103 | 0.6174 | 0.6137 | 0.6648 | 0.3541 | 0.5087 | -0.059 ± 0.016 | 0.015 (2) |
| 40+ | 154 | 0.292 | 0.1999 | +0.0922 ± 0.0315 | 0.7982 | 0.5818 | 0.7481 | 0.2977 | 0.4286 | -0.066 ± 0.0328 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3954 | 0.1846 | 0.1851 | -0.0005 ± 0.0002 | 0.5435 | 0.5444 | 0.485 | 0.4697 | 0.4853 | -0.036 ± 0.0069 | -0.0163 (35) |
| 3-5 | 2663 | 0.2003 | 0.1982 | +0.0021 ± 0.0007 | 0.5838 | 0.5768 | 0.4858 | 0.4462 | 0.4412 | -0.063 ± 0.0088 | -0.0094 (18) |
| 5-10 | 5976 | 0.1943 | 0.1899 | +0.0044 ± 0.0008 | 0.5718 | 0.5566 | 0.4856 | 0.4115 | 0.4187 | -0.052 ± 0.0057 | -0.01 (31) |
| 10-15 | 4826 | 0.1944 | 0.1809 | +0.0135 ± 0.0015 | 0.5732 | 0.5353 | 0.4958 | 0.3726 | 0.379 | -0.058 ± 0.0062 | -0.015 (12) |
| 15-25 | 6195 | 0.2125 | 0.1726 | +0.0398 ± 0.0021 | 0.6189 | 0.5097 | 0.5115 | 0.3165 | 0.3127 | -0.075 ± 0.0053 | -0.03 (2) |
| 25-40 | 4795 | 0.2185 | 0.1292 | +0.0894 ± 0.0033 | 0.6312 | 0.3938 | 0.531 | 0.2153 | 0.2336 | -0.052 ± 0.005 | 0.01 (3) |
| 40+ | 3102 | 0.3915 | 0.0512 | +0.3403 ± 0.0046 | 1.0217 | 0.1903 | 0.6412 | 0.1118 | 0.069 | -0.078 ± 0.0039 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1128 | 0.1957 | 0.1958 | -0.0001 ± 0.0005 | 0.5701 | 0.57 | 0.505 | 0.4899 | 0.4947 | -0.067 ± 0.0134 | -0.0224 (49) |
| 3-5 | 784 | 0.1882 | 0.1879 | +0.0003 ± 0.0012 | 0.552 | 0.5502 | 0.4942 | 0.4543 | 0.4681 | -0.059 ± 0.0158 | -0.0194 (34) |
| 5-10 | 1642 | 0.203 | 0.1977 | +0.0053 ± 0.0017 | 0.5963 | 0.5794 | 0.4984 | 0.4248 | 0.4263 | -0.076 ± 0.0112 | -0.005 (78) |
| 10-15 | 1118 | 0.2152 | 0.2032 | +0.0119 ± 0.0033 | 0.6225 | 0.5902 | 0.5322 | 0.4095 | 0.4204 | -0.082 ± 0.0139 | 0.0014 (64) |
| 15-25 | 1452 | 0.2324 | 0.2117 | +0.0207 ± 0.0047 | 0.662 | 0.6084 | 0.5794 | 0.3846 | 0.4311 | -0.079 ± 0.0122 | -0.0214 (59) |
| 25-40 | 907 | 0.2431 | 0.2098 | +0.0333 ± 0.0093 | 0.6951 | 0.6015 | 0.6792 | 0.3675 | 0.4697 | -0.088 ± 0.0143 | -0.0219 (26) |
| 40+ | 302 | 0.3403 | 0.2009 | +0.1393 ± 0.025 | 0.983 | 0.5869 | 0.8093 | 0.3306 | 0.4404 | -0.099 ± 0.0234 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4015 | 0.1776 | 0.1778 | -0.0002 ± 0.0002 | 0.5256 | 0.5256 | 0.5065 | 0.4914 | 0.5011 | -0.040 ± 0.0067 | -0.0157 (88) |
| 3-5 | 2737 | 0.1935 | 0.192 | +0.0015 ± 0.0007 | 0.564 | 0.561 | 0.5025 | 0.4627 | 0.464 | -0.050 ± 0.0085 | -0.0209 (69) |
| 5-10 | 5587 | 0.1993 | 0.1917 | +0.0077 ± 0.0009 | 0.5867 | 0.5642 | 0.4951 | 0.4215 | 0.4079 | -0.070 ± 0.0059 | -0.0082 (132) |
| 10-15 | 3897 | 0.2119 | 0.1959 | +0.0160 ± 0.0018 | 0.6155 | 0.5732 | 0.5311 | 0.4084 | 0.4039 | -0.070 ± 0.0072 | -0.0053 (105) |
| 15-25 | 4792 | 0.2304 | 0.2014 | +0.0290 ± 0.0026 | 0.6628 | 0.5822 | 0.5667 | 0.3712 | 0.3957 | -0.063 ± 0.0065 | -0.0253 (107) |
| 25-40 | 3270 | 0.2588 | 0.1856 | +0.0732 ± 0.0047 | 0.7332 | 0.5419 | 0.6323 | 0.3193 | 0.3615 | -0.078 ± 0.0074 | -0.0229 (51) |
| 40+ | 1404 | 0.3761 | 0.1497 | +0.2264 ± 0.0107 | 1.0636 | 0.4496 | 0.7329 | 0.2316 | 0.2685 | -0.075 ± 0.0098 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5222 | 1.017 ± 0.039 | 1.09 | 0.168 | 0.1652 | 0.2154 | 0.2069 |
| gen2 | 5222 | 0.806 ± 0.035 | 1.047 | 0.1693 | 0.1657 | 0.2355 | 0.2068 |
| gen1_elo | 5222 | 0.996 ± 0.037 | 1.089 | 0.1746 | 0.1654 | 0.214 | 0.2071 |
| gen1_sr | 5222 | 0.981 ± 0.046 | 1.111 | 0.1298 | 0.1676 | 0.2313 | 0.2064 |
| gen1_ledger | 7333 | 0.854 ± 0.028 | 1.053 | 0.1853 | 0.1767 | 0.2186 | 0.2016 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 26,457)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,797 | 21.9% |
| STALE_QUOTE | market_freshness | 5,735 | 21.7% |
| BOOK_QUALITY | execution | 5,128 | 19.4% |
| POOR_DATA | data | 3,151 | 11.9% |
| LIMITED_DATA | data | 1,657 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,456 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,207 | 4.6% |
| IDENTITY_AMBIGUOUS | mapping | 1,098 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 765 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 462 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 21.9%, market_freshness 21.7%, execution 19.4%, data 18.2%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.6%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.7%, STALE_PLAYER_DATA 52.4%, STALE_KALSHI_QUOTE 43.4%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 15.9%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.4%, POST_SETTLEMENT_OBSERVATION 21.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 14,139)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,691 | 33.2% |
| BOOK_QUALITY | execution | 2,671 | 18.9% |
| STALE_QUOTE | market_freshness | 2,659 | 18.8% |
| POOR_DATA | data | 1,347 | 9.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 772 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 582 | 4.1% |
| LIMITED_DATA | data | 497 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 493 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 307 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 119 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.2%, execution 18.9%, market_freshness 18.8%, data 13.0%, market_freshness/coverage 8.9%, mapping 4.1%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 63.1%, STALE_KALSHI_QUOTE 51.3%, STALE_PLAYER_DATA 46.8%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.7%, PLAYER_IDENTITY_RISK 18.7%, MODEL_HIGH_UNCERTAINTY 18.3%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.3%, POST_SETTLEMENT_OBSERVATION 33.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 11175, "IDENTITY_AMBIGUOUS": 2964}; ticker orientation: {"VERIFIED": 14139}.

Checks: discipline:AMBIGUOUS 911, discipline:PASS 13228, identity_confidence:AMBIGUOUS 2649, identity_confidence:PASS 11490, level_mapping:NA 923, level_mapping:PASS 13216, market_pair:AMBIGUOUS 474, market_pair:NA 333, market_pair:PASS 13332, model_complement:NA 297, model_complement:PASS 13842, namesake:AMBIGUOUS 6, namesake:PASS 14133, physical_match_id:NA 4956, physical_match_id:PASS 9183, player_ids:PASS 14139, same_pair_other_event:PASS 14139, ticker_orientation:PASS 14139

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,222 | 4.3% | 3.9% | 1.6% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 15, "coverage": 13} | 5.82 | 0.2195 / 0.2156 (587) | 21.0% | 3.0% | 3.3% | 2.7% |
| CHALLENGER | 9,644 | 16.6% | 6.3% | 11.3% | {"coverage": 932, "market_freshness/coverage": 193, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 74, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.3 | 0.2196 / 0.2106 (2209) | 34.9% | 16.0% | 4.1% | 22.4% |
| DOUBLES | 1,963 | 46.4% | 46.1% | 6.4% | {"execution": 514, "mapping": 227, "market_freshness": 106, "market_freshness/coverage": 57, "coverage": 7} | 23.51 | 0.3111 / 0.2379 (470) | 11.9% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 18,029 | 25.3% | 18.0% | 32.2% | {"coverage": 1568, "execution": 876, "market_freshness": 824, "data": 683, "market_freshness/coverage": 416, "mapping": 185, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.86 | 0.2165 / 0.1999 (3720) | 36.5% | 70.4% | 17.6% | 20.7% |
| ITF_WOMEN | 23,890 | 26.7% | 19.6% | 45.1% | {"coverage": 2138, "market_freshness": 1367, "execution": 1168, "data": 924, "market_freshness/coverage": 531, "mapping": 147, "model_calibration_or_unknown": 82, "model_calibration": 18} | 12.67 | 0.2054 / 0.1971 (4332) | 38.6% | 58.1% | 10.2% | 20.8% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,766 | 5.7% | 5.1% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "execution": 27, "coverage": 20, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.59 | 0.2341 / 0.2273 (589) | 25.6% | 1.1% | 1.4% | 3.4% |
| WTA125 | 2,065 | 11.8% | 10.0% | 1.7% | {"market_freshness": 63, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.21 | 0.2113 / 0.1945 (606) | 24.9% | 11.9% | 5.2% | 7.5% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 117 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 6 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 7 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 572 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 8 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 9 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 12 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 13 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 16 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 17 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
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
| 30 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 31 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 32 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 33 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 34 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 35 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 36 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 37 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 39 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 40 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 41 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 42 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 43 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 44 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 46 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 48 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 49 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 50 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9688, "by_level_share_of_ge_25pp": {"ATP": 0.0159, "CHALLENGER": 0.1129, "DOUBLES": 0.0644, "ITF_MEN": 0.3225, "ITF_WOMEN": 0.4509, "OTHER": 0.0008, "WTA": 0.0152, "WTA125": 0.0173}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.513, "share_primary_cause_market_settled_or_in_play": 0.4213, "share_primary_cause_stale_quote_only": 0.1881}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 14139, "identity_ambiguous_share": 0.2096, "ticker_orientation": {"VERIFIED": 14139}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9183, "with_external": 483, "coverage": 0.0526, "external_status": {"EXTERNAL_STALE": 295, "AGREES_WITH_KALSHI": 176, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 295, "MODEL_LONE_OUTLIER": 176, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3644, "share_external_supports_model": 0.0248}, "pregame_clean_ge_25pp": {"n": 4522, "with_external": 458, "coverage": 0.1013, "external_status": {"EXTERNAL_STALE": 277, "AGREES_WITH_KALSHI": 169, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 277, "MODEL_LONE_OUTLIER": 169, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.369, "share_external_supports_model": 0.0262}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 451.0, "median_sample_ratio": 2.49, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2132, "data_status": {"POOR": 8072, "LIMITED": 3577, "ADEQUATE": 2490}, "comparison_lt_10pp": {"median_thinner_serve_points": 1680.0, "median_sample_ratio": 1.71, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1042, "model_minus_observed": 0.0534, "kalshi_minus_observed": -0.0851, "brier_diff_model_minus_kalshi": -0.0015}, "4-10x": {"n": 716, "model_minus_observed": 0.0849, "kalshi_minus_observed": -0.0604, "brier_diff_model_minus_kalshi": 0.0081}, "<2x": {"n": 2542, "model_minus_observed": 0.088, "kalshi_minus_observed": -0.0361, "brier_diff_model_minus_kalshi": 0.011}, ">=10x": {"n": 922, "model_minus_observed": 0.1168, "kalshi_minus_observed": -0.0591, "brier_diff_model_minus_kalshi": 0.0126}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5222, "model": {"intercept": -0.536, "slope": 0.806, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.189, "slope": 1.047, "slope_se": 0.039}, "mean_extremity_model": 0.1693, "mean_extremity_kalshi": 0.1657, "model_brier": 0.2355, "kalshi_brier": 0.2068, "brier_diff_model_minus_kalshi": 0.0287, "brier_diff_se": 0.0026, "model_logloss": 0.6686, "kalshi_logloss": 0.5969}, "fair_v1": {"n": 5222, "model": {"intercept": -0.409, "slope": 1.017, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.09, "slope_se": 0.04}, "mean_extremity_model": 0.168, "mean_extremity_kalshi": 0.1652, "model_brier": 0.2154, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0084, "brier_diff_se": 0.0022, "model_logloss": 0.6198, "kalshi_logloss": 0.5972}, "gen1_elo": {"n": 5222, "model": {"intercept": -0.383, "slope": 0.996, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.308, "slope": 1.089, "slope_se": 0.039}, "mean_extremity_model": 0.1746, "mean_extremity_kalshi": 0.1654, "model_brier": 0.214, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.007, "brier_diff_se": 0.0022, "model_logloss": 0.6174, "kalshi_logloss": 0.5974}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.247, "share_ge_15": 0.4412, "median_abs_gap": 13.0, "n": 37174}, "gen1_elo": {"share_ge_25": 0.2447, "share_ge_15": 0.4394, "median_abs_gap": 12.84, "n": 37174}, "gen1_sr": {"share_ge_25": 0.3135, "share_ge_15": 0.5211, "median_abs_gap": 15.9, "n": 37174}, "gen2": {"share_ge_25": 0.3168, "share_ge_15": 0.5113, "median_abs_gap": 15.49, "n": 37174}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1554, "share_ge_15": 0.3566, "median_abs_gap": 10.78, "n": 29091}, "gen1_elo": {"share_ge_25": 0.1554, "share_ge_15": 0.354, "median_abs_gap": 10.57, "n": 29089}, "gen1_sr": {"share_ge_25": 0.222, "share_ge_15": 0.4446, "median_abs_gap": 13.06, "n": 29092}, "gen2": {"share_ge_25": 0.2375, "share_ge_15": 0.4439, "median_abs_gap": 13.0, "n": 29093}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.82, "share_ge_25_all": 0.0431, "share_ge_25_pregame_clean": 0.0388}, "WTA": {"median_abs_gap_pregame_clean": 7.59, "share_ge_25_all": 0.0571, "share_ge_25_pregame_clean": 0.0505}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2374, "share_within_10pp_all": 0.4377, "share_within_10pp_pregame_clean": 0.4887, "corr_model_vs_mid_pregame_clean": 0.8485}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 764, "model_brier": 0.2002, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": -0.0006}, "10-15": {"n_settled": 920, "model_brier": 0.2207, "kalshi_brier": 0.212, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1166, "model_brier": 0.2245, "kalshi_brier": 0.2124, "brier_diff_model_minus_kalshi": 0.0122}, "25-40": {"n_settled": 676, "model_brier": 0.2238, "kalshi_brier": 0.2082, "brier_diff_model_minus_kalshi": 0.0156}, "3-5": {"n_settled": 470, "model_brier": 0.207, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": -0.0007}, "40+": {"n_settled": 143, "model_brier": 0.2752, "kalshi_brier": 0.1915, "brier_diff_model_minus_kalshi": 0.0836}, "5-10": {"n_settled": 1083, "model_brier": 0.2021, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": -0.0}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.536, "slope": 0.806, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.189, "slope": 1.047, "slope_se": 0.039}, "n": 5222}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.489, "slope": 0.854, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.163, "slope": 1.053, "slope_se": 0.032}, "n": 7333}, "NO_SKILL:gen2|WTA": {"n_settled": 234, "model_brier": 0.2572, "kalshi_brier": 0.2357, "brier_diff_model_minus_kalshi": 0.0214, "brier_diff_se": 0.0103, "corr_model_outcome": 0.2222, "corr_kalshi_outcome": 0.255}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 470, "model_brier": 0.3111, "kalshi_brier": 0.2379, "brier_diff_model_minus_kalshi": 0.0731, "brier_diff_se": 0.0139, "corr_model_outcome": 0.046, "corr_kalshi_outcome": 0.2337}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
