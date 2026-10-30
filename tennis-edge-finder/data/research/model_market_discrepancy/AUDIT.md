# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-30T12:15Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 69,762): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.0%, 25-40 13.8%, 40+ 8.0%; median gap 11.86 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 10.8%, doubles 6.6%). Main tour: ATP 4.2% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,239): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.0%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.4%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.0%, market_freshness 18.8%, execution 18.4%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,239 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.2% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 473.0 points vs 1682.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.016, Gen-2 0.807, Gen-1 ledger 0.856 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 740 model 0.2218 vs Kalshi 0.2055; n 155 model 0.2842 vs Kalshi 0.1885.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 296,750 model-market comparisons (484,912 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 99,529 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-30T11:58:22.196331+00:00'], shadow board 79,715 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-30T11:58:26.226976+00:00'], Model 4 37,012 rows, 24,081 settled tickers, 8,860 tickers with an external scan.
* By model: {"gen1_ledger": 67036, "gen1_elo": 40066, "fair_v1": 40066, "gen2": 40066, "gen1_sr": 40066, "model4_fundamental": 34747, "model4_conditioned": 34703}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 69,762 | 14.1 | 9.6 | 20.2 | 15.3 | 19.0 | 13.8 | 8.0 | 11.86 | 40.9% | 21.8% |
| MW fair_v1 | 40,066 | 12.9 | 8.7 | 18.7 | 15.3 | 19.5 | 14.9 | 9.9 | 13.02 | 44.3% | 24.8% |
| MW gen1_elo | 40,066 | 12.5 | 8.6 | 19.3 | 15.4 | 19.5 | 14.8 | 9.8 | 12.93 | 44.1% | 24.6% |
| MW gen1_ledger | 29,696 | 15.6 | 10.8 | 22.1 | 15.3 | 18.4 | 12.3 | 5.5 | 10.36 | 36.2% | 17.8% |
| MW gen1_sr | 40,066 | 10.1 | 7.2 | 16.8 | 13.8 | 20.7 | 18.6 | 12.7 | 15.85 | 52.0% | 31.3% |
| MW gen2 | 40,066 | 11.1 | 7.5 | 16.5 | 13.8 | 19.4 | 17.8 | 13.8 | 15.45 | 51.0% | 31.6% |
| all families model4_conditioned | 34,703 | 22.5 | 18.2 | 34.1 | 17.2 | 4.9 | 1.9 | 1.1 | 5.99 | 8.0% | 3.1% |
| all families model4_fundamental | 34,747 | 17.4 | 13.3 | 33.9 | 20.2 | 10.2 | 3.7 | 1.4 | 7.67 | 15.2% | 5.1% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.2%, >=15pp 40.9%, >=20pp 30.2%, >=25pp 21.8%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.3pp; >=10pp 44.8%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,438 | 27.3 | 15.4 | 27.7 | 13.5 | 11.5 | 4.0 | 0.6 | 5.92 | 16.1% | 4.6% |
| CHALLENGER | 5,959 | 16.3 | 9.8 | 20.9 | 15.1 | 15.4 | 11.8 | 10.8 | 10.91 | 38.0% | 22.6% |
| ITF_MEN | 11,256 | 9.8 | 7.4 | 17.0 | 15.1 | 21.2 | 17.6 | 11.9 | 15.21 | 50.7% | 29.5% |
| ITF_WOMEN | 15,814 | 9.7 | 7.1 | 15.9 | 15.1 | 22.0 | 18.1 | 12.1 | 15.68 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,482 | 18.2 | 13.7 | 24.9 | 19.9 | 16.1 | 6.3 | 1.0 | 8.2 | 23.4% | 7.3% |
| WTA125 | 1,111 | 16.4 | 7.5 | 22.4 | 18.9 | 20.8 | 12.2 | 1.9 | 10.77 | 34.8% | 14.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,438 | 26.0 | 15.4 | 25.8 | 16.1 | 11.8 | 4.1 | 0.8 | 6.22 | 16.7% | 4.9% |
| CHALLENGER | 5,959 | 15.1 | 9.0 | 18.3 | 14.2 | 18.1 | 13.6 | 11.7 | 12.54 | 43.4% | 25.3% |
| ITF_MEN | 11,256 | 8.1 | 6.2 | 15.1 | 13.8 | 19.5 | 20.7 | 16.6 | 17.94 | 56.9% | 37.3% |
| ITF_WOMEN | 15,814 | 8.0 | 5.8 | 14.0 | 12.7 | 20.6 | 21.2 | 17.6 | 19.11 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,482 | 15.3 | 10.9 | 22.1 | 15.3 | 22.0 | 12.5 | 1.9 | 10.59 | 36.4% | 14.4% |
| WTA125 | 1,111 | 9.8 | 6.6 | 16.7 | 16.0 | 24.2 | 17.6 | 9.0 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,438 | 22.2 | 13.2 | 24.5 | 16.1 | 16.1 | 6.6 | 1.3 | 7.58 | 24.1% | 7.9% |
| CHALLENGER | 5,959 | 14.9 | 9.3 | 21.0 | 16.1 | 15.6 | 12.1 | 11.1 | 11.32 | 38.7% | 23.1% |
| ITF_MEN | 11,256 | 9.3 | 7.2 | 17.4 | 14.3 | 21.8 | 17.8 | 12.3 | 15.68 | 51.8% | 30.1% |
| ITF_WOMEN | 15,814 | 9.4 | 6.8 | 16.4 | 15.8 | 22.0 | 18.0 | 11.4 | 15.49 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,482 | 23.6 | 16.7 | 31.9 | 14.3 | 9.2 | 2.9 | 1.2 | 6.05 | 13.3% | 4.2% |
| WTA125 | 1,111 | 21.7 | 12.9 | 26.8 | 17.3 | 15.0 | 5.9 | 0.4 | 8.01 | 21.3% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,014 | 24.4 | 19.2 | 31.1 | 12.8 | 9.0 | 2.9 | 0.5 | 5.74 | 12.5% | 3.4% |
| CHALLENGER | 4,034 | 22.5 | 14.6 | 27.3 | 14.6 | 13.5 | 6.0 | 1.6 | 7.09 | 21.0% | 7.5% |
| DOUBLES | 2,143 | 5.1 | 4.4 | 12.2 | 10.7 | 21.1 | 25.0 | 21.6 | 23.54 | 67.6% | 46.6% |
| ITF_MEN | 8,547 | 13.0 | 9.4 | 21.2 | 15.8 | 21.4 | 13.3 | 5.8 | 11.9 | 40.6% | 19.2% |
| ITF_WOMEN | 10,202 | 13.1 | 9.2 | 19.9 | 15.8 | 21.2 | 15.4 | 5.5 | 12.32 | 42.1% | 20.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,482 | 24.5 | 15.4 | 30.6 | 17.5 | 9.0 | 2.7 | 0.3 | 6.64 | 12.0% | 3.0% |
| WTA125 | 1,125 | 25.1 | 12.6 | 21.1 | 19.2 | 13.4 | 7.0 | 1.6 | 7.88 | 22.0% | 8.6% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,339 | 27.7 | 15.6 | 28.0 | 13.4 | 11.3 | 3.6 | 0.4 | 5.88 | 15.3% | 4.0% |
| CHALLENGER | 4,173 | 21.2 | 12.3 | 26.0 | 17.6 | 15.3 | 6.1 | 1.6 | 8.03 | 22.9% | 7.6% |
| ITF_MEN | 8,243 | 11.9 | 8.8 | 20.6 | 17.1 | 22.0 | 14.3 | 5.2 | 12.4 | 41.5% | 19.5% |
| ITF_WOMEN | 11,750 | 11.6 | 8.5 | 18.4 | 17.3 | 23.9 | 15.1 | 5.2 | 13.28 | 44.2% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,400 | 18.5 | 13.6 | 25.1 | 20.2 | 16.2 | 5.8 | 0.5 | 8.16 | 22.6% | 6.4% |
| WTA125 | 1,075 | 16.6 | 7.3 | 21.9 | 19.2 | 21.3 | 11.9 | 1.7 | 11.02 | 34.9% | 13.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,339 | 26.3 | 15.7 | 26.0 | 16.1 | 11.8 | 3.7 | 0.5 | 6.2 | 16.0% | 4.2% |
| CHALLENGER | 4,173 | 19.3 | 11.5 | 22.9 | 16.8 | 18.6 | 9.1 | 1.9 | 9.01 | 29.5% | 11.0% |
| ITF_MEN | 8,244 | 9.5 | 7.2 | 17.4 | 16.1 | 21.3 | 18.9 | 9.6 | 14.93 | 49.8% | 28.4% |
| ITF_WOMEN | 11,751 | 8.9 | 6.8 | 15.9 | 14.2 | 22.7 | 20.6 | 10.8 | 16.57 | 54.1% | 31.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,400 | 15.5 | 11.0 | 22.3 | 15.4 | 22.2 | 12.5 | 1.2 | 10.41 | 35.8% | 13.7% |
| WTA125 | 1,075 | 9.9 | 6.6 | 16.8 | 16.2 | 24.1 | 17.9 | 8.5 | 15.14 | 50.5% | 26.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,960 | 24.5 | 19.4 | 31.2 | 12.9 | 8.7 | 2.8 | 0.4 | 5.67 | 11.9% | 3.2% |
| CHALLENGER | 3,556 | 24.0 | 15.5 | 28.5 | 14.7 | 12.8 | 4.0 | 0.5 | 6.58 | 17.3% | 4.5% |
| DOUBLES | 2,011 | 5.0 | 4.5 | 12.4 | 10.9 | 20.9 | 24.9 | 21.5 | 23.41 | 67.2% | 46.4% |
| ITF_MEN | 7,296 | 13.8 | 10.0 | 22.9 | 16.4 | 21.3 | 11.8 | 3.8 | 10.94 | 36.9% | 15.6% |
| ITF_WOMEN | 8,691 | 13.7 | 9.7 | 21.1 | 16.4 | 21.3 | 14.3 | 3.5 | 11.52 | 39.1% | 17.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,428 | 24.9 | 15.8 | 30.7 | 17.5 | 9.0 | 2.1 | 0.1 | 6.44 | 11.2% | 2.2% |
| WTA125 | 1,000 | 26.4 | 13.4 | 22.1 | 20.3 | 12.4 | 4.9 | 0.5 | 7.32 | 17.8% | 5.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,143 | 5.1 | 4.4 | 12.2 | 10.7 | 21.1 | 25.0 | 21.6 | 23.54 | 67.6% | 46.6% |
| singles | 27,553 | 16.4 | 11.2 | 22.9 | 15.6 | 18.2 | 11.4 | 4.2 | 9.83 | 33.8% | 15.6% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,951 | 13.1 | 9.3 | 20.2 | 15.6 | 19.0 | 13.8 | 8.9 | 12.31 | 41.7% | 22.7% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 26,289 | 13.4 | 8.7 | 18.6 | 15.0 | 19.2 | 15.0 | 10.0 | 12.98 | 44.2% | 25.0% |
| UNKNOWN | 5,577 | 10.4 | 7.8 | 17.1 | 16.5 | 21.2 | 16.0 | 11.1 | 14.23 | 48.3% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 11,096 | 20.0 | 12.1 | 22.4 | 15.6 | 14.7 | 9.2 | 6.0 | 8.55 | 29.9% | 15.2% |
| B | 4,961 | 12.9 | 9.0 | 19.4 | 15.8 | 19.3 | 12.6 | 11.0 | 12.54 | 43.0% | 23.6% |
| C | 5,747 | 11.9 | 8.9 | 19.9 | 15.7 | 18.6 | 14.4 | 10.6 | 12.82 | 43.5% | 25.0% |
| D | 6,344 | 11.9 | 8.3 | 17.5 | 15.4 | 21.6 | 16.0 | 9.3 | 13.83 | 46.9% | 25.2% |
| F | 11,918 | 7.3 | 5.6 | 15.0 | 14.7 | 23.3 | 20.9 | 13.0 | 17.68 | 57.3% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,888 | 24.1 | 15.7 | 29.0 | 15.2 | 11.0 | 3.7 | 1.3 | 6.52 | 16.0% | 5.0% |
| B | 4,221 | 17.0 | 10.7 | 24.2 | 16.6 | 18.7 | 9.7 | 3.1 | 9.59 | 31.5% | 12.8% |
| C | 5,810 | 11.3 | 7.9 | 19.4 | 14.7 | 21.0 | 15.7 | 10.1 | 13.47 | 46.8% | 25.8% |
| D | 4,359 | 14.3 | 9.8 | 21.8 | 15.4 | 20.0 | 13.2 | 5.4 | 11.26 | 38.7% | 18.6% |
| F | 7,418 | 9.8 | 8.3 | 16.1 | 15.0 | 23.2 | 19.9 | 7.7 | 15.43 | 50.8% | 27.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,567 | 18.3 | 11.0 | 21.5 | 15.3 | 15.1 | 10.0 | 8.8 | 9.74 | 34.0% | 18.8% |
| LIMITED | 8,866 | 13.6 | 10.0 | 20.4 | 16.1 | 19.1 | 13.2 | 7.6 | 11.7 | 39.8% | 20.8% |
| POOR | 18,633 | 9.0 | 6.5 | 16.0 | 15.0 | 22.7 | 19.1 | 11.7 | 16.15 | 53.4% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,623 | 24.2 | 18.1 | 33.0 | 14.9 | 6.6 | 2.7 | 0.4 | 5.84 | 9.7% | 3.1% |
| GAME_SPREAD | 5,965 | 22.2 | 15.2 | 32.9 | 17.2 | 9.0 | 3.0 | 0.6 | 6.74 | 12.6% | 3.5% |
| MATCH_WINNER | 29,696 | 15.6 | 10.8 | 22.1 | 15.3 | 18.4 | 12.3 | 5.5 | 10.36 | 36.2% | 17.8% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,798 | 27.6 | 16.7 | 31.0 | 12.5 | 9.5 | 2.4 | 0.3 | 5.66 | 12.2% | 2.7% |
| TOTAL_GAMES | 9,930 | 9.8 | 10.6 | 35.7 | 26.6 | 10.4 | 4.0 | 2.8 | 9.25 | 17.3% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,267 | 24.5 | 30.1 | 32.9 | 7.3 | 4.1 | 0.9 | 0.3 | 4.7 | 5.2% | 1.2% |
| GAME_SPREAD | 8,119 | 47.4 | 16.0 | 25.2 | 7.3 | 2.2 | 1.3 | 0.6 | 3.25 | 4.1% | 1.9% |
| TOTAL_GAMES | 14,317 | 6.5 | 9.4 | 40.3 | 31.3 | 7.2 | 3.2 | 2.2 | 9.29 | 12.5% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,278 | 24.0 | 16.8 | 34.8 | 14.3 | 7.1 | 2.6 | 0.4 | 6.0 | 10.1% | 3.0% |
| GAME_SPREAD | 8,122 | 20.2 | 13.6 | 28.0 | 20.5 | 12.4 | 4.3 | 1.1 | 7.76 | 17.8% | 5.3% |
| TOTAL_GAMES | 14,347 | 10.1 | 10.2 | 36.3 | 25.2 | 11.5 | 4.2 | 2.4 | 9.16 | 18.1% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 40,066 | 44.3% | 24.8% | 13.02 | 35.5% | 15.3% | 10.71 |
| gen1_elo | 40,066 | 44.1% | 24.6% | 12.93 | 35.2% | 15.3% | 10.53 |
| gen1_sr | 40,066 | 52.0% | 31.3% | 15.85 | 44.1% | 21.7% | 13.01 |
| gen2 | 40,066 | 51.0% | 31.6% | 15.45 | 44.0% | 23.4% | 12.88 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,643 | 15.6 | 10.6 | 21.3 | 17.2 | 20.1 | 12.0 | 3.3 | 10.71 | 35.4% | 15.3% |
| STALE | 21,423 | 10.6 | 7.1 | 16.4 | 13.8 | 19.0 | 17.5 | 15.6 | 15.83 | 52.1% | 33.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 23,164 | 16.3 | 11.1 | 22.8 | 15.4 | 17.8 | 11.8 | 4.7 | 9.95 | 34.4% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 69,762 | 23164 | 22115 | 24483 | 24.4 | 125.2 | 1451.1 |
| ge_15pp | 28,520 | 7965 | 7884 | 12671 | 26.9 | 437.4 | 1451.1 |
| ge_25pp | 15,239 | 3834 | 3443 | 7962 | 31.8 | 586.0 | 1431.1 |
| lt_10pp | 30,560 | 11630 | 10480 | 8450 | 22.4 | 47.1 | 1421.1 |

Current slate `SL-20261030T121533Z-9e98d025`: 348 priced rows, quote age at build {'median': 17.6, 'max': 17.6}, freshness {'AGING': 348}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 45 | 0.0 | 0.0 | 31.1 | 6.7 | 35.6 | 22.2 | 4.4 | 20.19 | 62.2% | 26.7% |
| EXTERNAL_LONE_OUTLIER | 25 | 64.0 | 36.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,965 | 19.8 | 11.1 | 25.4 | 17.8 | 17.9 | 7.2 | 0.9 | 8.58 | 25.9% | 8.1% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 784 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,716 | 0.0 | 2.5 | 36.4 | 25.4 | 24.9 | 10.0 | 0.9 | 12.0 | 35.8% | 10.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 40,066 | 6562 (16.4%) | 26.2% | 1.1% | {"EXTERNAL_STALE": 3965, "AGREES_WITH_KALSHI": 1716, "ALL_AGREE": 784, "SUPPORTS_MODEL_DIRECTION": 44, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 25, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 17,756 | 1674 (9.4%) | 36.7% | 1.8% | {"EXTERNAL_STALE": 1029, "AGREES_WITH_KALSHI": 615, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,943 | 521 (5.2%) | 35.9% | 2.5% | {"EXTERNAL_STALE": 321, "AGREES_WITH_KALSHI": 187, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,739 | 494 (10.4%) | 36.4% | 2.6% | {"EXTERNAL_STALE": 301, "AGREES_WITH_KALSHI": 180, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 16,161 | 3742 (23.2%) | 17.8% | 1.0% | {"EXTERNAL_STALE": 2230, "ALL_AGREE": 784, "AGREES_WITH_KALSHI": 666, "EXTERNAL_OUTLIER": 25, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,837 | 10.4 | 7.5 | 19.6 | 14.3 | 21.6 | 16.5 | 10.0 | 14.11 | 48.1% | 26.5% |
| 4-10x | 5,414 | 11.1 | 8.6 | 18.7 | 15.6 | 21.8 | 14.4 | 9.9 | 13.59 | 46.1% | 24.3% |
| <2x | 20,288 | 15.2 | 10.0 | 19.5 | 16.0 | 17.4 | 13.1 | 9.0 | 11.55 | 39.4% | 22.0% |
| >=10x | 6,527 | 10.4 | 6.4 | 15.1 | 14.5 | 21.7 | 19.2 | 12.7 | 16.35 | 53.6% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,335 | 12.8 | 8.9 | 19.6 | 15.9 | 19.0 | 13.4 | 10.4 | 12.67 | 42.9% | 23.9% |
| 300-1000 | 8,677 | 12.0 | 8.7 | 17.8 | 15.3 | 20.3 | 16.4 | 9.5 | 13.59 | 46.2% | 25.9% |
| <300 | 12,882 | 8.2 | 5.8 | 15.2 | 14.8 | 23.0 | 20.0 | 12.9 | 17.06 | 56.0% | 32.9% |
| >=3000 | 8,172 | 21.5 | 13.1 | 24.1 | 15.5 | 13.8 | 7.2 | 4.9 | 7.57 | 25.8% | 12.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1152 | 0.5499 | 0.4108 | 0.4965 | +0.053 | -0.086 | -0.0017 ± 0.0045 |
| ratio 4-10x | 798 | 0.5807 | 0.4339 | 0.4962 | +0.084 | -0.062 | 0.0068 ± 0.0056 |
| ratio <2x | 2764 | 0.5382 | 0.4149 | 0.4468 | +0.091 | -0.032 | 0.0124 ± 0.0027 |
| ratio >=10x | 994 | 0.5685 | 0.3941 | 0.4527 | +0.116 | -0.059 | 0.0134 ± 0.0058 |
| thinner_sample 1000-3000 | 1556 | 0.5404 | 0.4132 | 0.4512 | +0.089 | -0.038 | 0.0098 ± 0.0037 |
| thinner_sample 300-1000 | 1303 | 0.568 | 0.4258 | 0.4866 | +0.081 | -0.061 | 0.0025 ± 0.0044 |
| thinner_sample <300 | 1909 | 0.5596 | 0.392 | 0.4615 | +0.098 | -0.070 | 0.0107 ± 0.0041 |
| thinner_sample >=3000 | 940 | 0.5322 | 0.4382 | 0.4638 | +0.068 | -0.026 | 0.0129 ± 0.0037 |
| data_status ADEQUATE | 1547 | 0.5347 | 0.4317 | 0.4505 | +0.084 | -0.019 | 0.0131 ± 0.0031 |
| data_status LIMITED | 1394 | 0.5497 | 0.4163 | 0.4727 | +0.077 | -0.057 | 0.0064 ± 0.004 |
| data_status POOR | 2767 | 0.5624 | 0.4011 | 0.4687 | +0.094 | -0.068 | 0.0079 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 827 | 0.1993 | 0.1997 | -0.0004 ± 0.0005 | 0.5781 | 0.5793 | 0.5044 | 0.4892 | 0.5091 | -0.088 ± 0.0165 | -0.01 (5) |
| 3-5 | 523 | 0.2055 | 0.2059 | -0.0004 ± 0.0016 | 0.5936 | 0.5932 | 0.5035 | 0.4637 | 0.4876 | -0.095 ± 0.0203 | 0.02 (1) |
| 5-10 | 1200 | 0.2014 | 0.2017 | -0.0003 ± 0.0019 | 0.589 | 0.587 | 0.5108 | 0.437 | 0.4733 | -0.087 ± 0.0134 | -0.0167 (6) |
| 10-15 | 1000 | 0.2201 | 0.2118 | +0.0084 ± 0.0036 | 0.6327 | 0.6089 | 0.5279 | 0.4042 | 0.431 | -0.107 ± 0.0147 | -0.048 (5) |
| 15-25 | 1263 | 0.2256 | 0.2126 | +0.0131 ± 0.0051 | 0.6473 | 0.6094 | 0.577 | 0.3815 | 0.4458 | -0.101 ± 0.013 | -0.0033 (9) |
| 25-40 | 740 | 0.2218 | 0.2055 | +0.0163 ± 0.01 | 0.6328 | 0.5923 | 0.6555 | 0.3453 | 0.4743 | -0.075 ± 0.0152 | -0.01 (1) |
| 40+ | 155 | 0.2842 | 0.1885 | +0.0957 ± 0.0305 | 0.7739 | 0.5561 | 0.7384 | 0.2901 | 0.4129 | -0.076 ± 0.0302 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4539 | 0.1841 | 0.185 | -0.0008 ± 0.0002 | 0.5427 | 0.5438 | 0.487 | 0.4718 | 0.5017 | -0.023 ± 0.0065 | -0.0129 (17) |
| 3-5 | 3056 | 0.1954 | 0.1936 | +0.0018 ± 0.0006 | 0.5698 | 0.5631 | 0.4821 | 0.4423 | 0.4385 | -0.059 ± 0.008 | 0.0 (2) |
| 5-10 | 6501 | 0.2024 | 0.1989 | +0.0035 ± 0.0008 | 0.5907 | 0.5788 | 0.4848 | 0.4112 | 0.4253 | -0.046 ± 0.0056 | -0.0119 (21) |
| 10-15 | 5403 | 0.2013 | 0.1854 | +0.0159 ± 0.0015 | 0.5886 | 0.5451 | 0.4845 | 0.3605 | 0.3578 | -0.066 ± 0.0059 | -0.0281 (16) |
| 15-25 | 6764 | 0.2067 | 0.168 | +0.0387 ± 0.002 | 0.6061 | 0.4985 | 0.5001 | 0.3042 | 0.3043 | -0.070 ± 0.005 | -0.0025 (44) |
| 25-40 | 5340 | 0.2213 | 0.1251 | +0.0962 ± 0.003 | 0.6366 | 0.3846 | 0.5261 | 0.2119 | 0.22 | -0.059 ± 0.0047 | -0.01 (1) |
| 40+ | 3502 | 0.385 | 0.0448 | +0.3402 ± 0.0041 | 1.0029 | 0.1734 | 0.6333 | 0.1041 | 0.0594 | -0.079 ± 0.0034 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 656 | 0.2051 | 0.2058 | -0.0007 ± 0.0006 | 0.5918 | 0.5936 | 0.5083 | 0.4933 | 0.5244 | -0.099 ± 0.0192 | -0.01 (3) |
| 3-5 | 466 | 0.221 | 0.2184 | +0.0026 ± 0.0017 | 0.6266 | 0.6213 | 0.5127 | 0.4731 | 0.4549 | -0.129 ± 0.023 | 0.02 (1) |
| 5-10 | 1049 | 0.2083 | 0.2074 | +0.0010 ± 0.0021 | 0.6032 | 0.5998 | 0.5434 | 0.4687 | 0.5014 | -0.089 ± 0.0145 | -0.01 (4) |
| 10-15 | 925 | 0.2164 | 0.2102 | +0.0063 ± 0.0038 | 0.6238 | 0.6075 | 0.5639 | 0.4395 | 0.4789 | -0.107 ± 0.0157 | -0.04 (5) |
| 15-25 | 1327 | 0.2297 | 0.2138 | +0.0159 ± 0.005 | 0.6542 | 0.6117 | 0.5837 | 0.3883 | 0.4476 | -0.096 ± 0.0129 | -0.0133 (9) |
| 25-40 | 937 | 0.2675 | 0.1973 | +0.0702 ± 0.0091 | 0.7475 | 0.5753 | 0.659 | 0.3449 | 0.3927 | -0.132 ± 0.0145 | -0.0075 (4) |
| 40+ | 348 | 0.3628 | 0.1666 | +0.1961 ± 0.0217 | 0.9945 | 0.5008 | 0.7323 | 0.247 | 0.3017 | -0.081 ± 0.0212 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3917 | 0.1895 | 0.1897 | -0.0003 ± 0.0002 | 0.5539 | 0.5542 | 0.5092 | 0.4942 | 0.5101 | -0.041 ± 0.0072 | -0.0133 (15) |
| 3-5 | 2647 | 0.1964 | 0.1953 | +0.0012 ± 0.0007 | 0.5698 | 0.5661 | 0.5107 | 0.4711 | 0.4745 | -0.049 ± 0.0088 | 0.02 (1) |
| 5-10 | 5778 | 0.1988 | 0.1953 | +0.0035 ± 0.0009 | 0.583 | 0.5698 | 0.5099 | 0.4358 | 0.4522 | -0.043 ± 0.0059 | -0.0117 (6) |
| 10-15 | 4842 | 0.2045 | 0.1924 | +0.0121 ± 0.0016 | 0.5984 | 0.5622 | 0.5124 | 0.3886 | 0.4025 | -0.053 ± 0.0064 | -0.0189 (18) |
| 15-25 | 6778 | 0.2171 | 0.181 | +0.0361 ± 0.002 | 0.6315 | 0.531 | 0.5236 | 0.3283 | 0.337 | -0.062 ± 0.0052 | -0.0086 (42) |
| 25-40 | 6237 | 0.2514 | 0.1361 | +0.1154 ± 0.003 | 0.7095 | 0.4172 | 0.5578 | 0.241 | 0.2208 | -0.086 ± 0.0047 | -0.0044 (18) |
| 40+ | 4906 | 0.3987 | 0.0588 | +0.3399 ± 0.004 | 1.0524 | 0.2119 | 0.6524 | 0.1174 | 0.0809 | -0.073 ± 0.0034 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 793 | 0.1957 | 0.1979 | -0.0022 ± 0.0006 | 0.5701 | 0.5757 | 0.4995 | 0.4841 | 0.5435 | -0.039 ± 0.0165 | -0.0137 (8) |
| 3-5 | 556 | 0.2053 | 0.2036 | +0.0017 ± 0.0015 | 0.5935 | 0.5877 | 0.4953 | 0.4557 | 0.455 | -0.119 ± 0.0198 | 0.0067 (3) |
| 5-10 | 1240 | 0.2034 | 0.2015 | +0.0018 ± 0.0019 | 0.5927 | 0.586 | 0.5104 | 0.4366 | 0.4597 | -0.096 ± 0.0131 | -0.0071 (7) |
| 10-15 | 1002 | 0.2088 | 0.2041 | +0.0047 ± 0.0035 | 0.6074 | 0.5917 | 0.5393 | 0.416 | 0.4601 | -0.096 ± 0.0143 | -0.0317 (6) |
| 15-25 | 1198 | 0.2345 | 0.2173 | +0.0172 ± 0.0052 | 0.6683 | 0.6198 | 0.5887 | 0.3945 | 0.4474 | -0.112 ± 0.0135 | -0.03 (1) |
| 25-40 | 756 | 0.2123 | 0.2123 | -0.0000 ± 0.0098 | 0.613 | 0.6082 | 0.6634 | 0.3529 | 0.5066 | -0.059 ± 0.0151 | 0.015 (2) |
| 40+ | 163 | 0.2995 | 0.196 | +0.1035 ± 0.0306 | 0.8153 | 0.5732 | 0.7492 | 0.2987 | 0.4172 | -0.077 ± 0.0316 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4363 | 0.1834 | 0.184 | -0.0006 ± 0.0002 | 0.54 | 0.5413 | 0.4827 | 0.4674 | 0.4854 | -0.034 ± 0.0066 | -0.0163 (35) |
| 3-5 | 3004 | 0.202 | 0.1998 | +0.0021 ± 0.0007 | 0.5869 | 0.5794 | 0.4804 | 0.4409 | 0.4341 | -0.063 ± 0.0083 | -0.0094 (18) |
| 5-10 | 6660 | 0.1945 | 0.1905 | +0.0039 ± 0.0008 | 0.5722 | 0.5586 | 0.4854 | 0.4113 | 0.4222 | -0.048 ± 0.0054 | -0.01 (31) |
| 10-15 | 5392 | 0.1922 | 0.1788 | +0.0134 ± 0.0014 | 0.5686 | 0.5295 | 0.4942 | 0.3708 | 0.3776 | -0.057 ± 0.0058 | -0.015 (12) |
| 15-25 | 6880 | 0.2134 | 0.1734 | +0.0401 ± 0.002 | 0.6216 | 0.5106 | 0.5134 | 0.3189 | 0.3145 | -0.074 ± 0.005 | -0.03 (2) |
| 25-40 | 5329 | 0.2159 | 0.1284 | +0.0875 ± 0.0031 | 0.6249 | 0.3923 | 0.5297 | 0.2142 | 0.2355 | -0.048 ± 0.0047 | 0.01 (3) |
| 40+ | 3477 | 0.3949 | 0.0503 | +0.3446 ± 0.0043 | 1.0297 | 0.1877 | 0.6428 | 0.1108 | 0.0661 | -0.079 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1193 | 0.1959 | 0.196 | -0.0001 ± 0.0004 | 0.5704 | 0.5705 | 0.5045 | 0.4894 | 0.4937 | -0.069 ± 0.0131 | -0.0224 (49) |
| 3-5 | 850 | 0.1872 | 0.1863 | +0.0009 ± 0.0012 | 0.5488 | 0.546 | 0.4966 | 0.4567 | 0.4635 | -0.069 ± 0.0152 | -0.0194 (34) |
| 5-10 | 1765 | 0.2012 | 0.1964 | +0.0048 ± 0.0016 | 0.5912 | 0.5762 | 0.5023 | 0.4286 | 0.4334 | -0.077 ± 0.0108 | -0.005 (78) |
| 10-15 | 1207 | 0.2165 | 0.204 | +0.0125 ± 0.0032 | 0.6255 | 0.592 | 0.5374 | 0.4146 | 0.4234 | -0.088 ± 0.0134 | 0.0014 (64) |
| 15-25 | 1549 | 0.2323 | 0.2111 | +0.0212 ± 0.0046 | 0.662 | 0.6072 | 0.5835 | 0.3888 | 0.4345 | -0.085 ± 0.0118 | -0.0214 (59) |
| 25-40 | 973 | 0.2441 | 0.2101 | +0.0340 ± 0.009 | 0.6976 | 0.6023 | 0.6844 | 0.3725 | 0.4748 | -0.095 ± 0.0138 | -0.0219 (26) |
| 40+ | 327 | 0.3343 | 0.2031 | +0.1312 ± 0.024 | 0.9686 | 0.5915 | 0.8158 | 0.3392 | 0.4557 | -0.099 ± 0.0225 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4475 | 0.1759 | 0.1761 | -0.0002 ± 0.0002 | 0.5207 | 0.521 | 0.5088 | 0.4936 | 0.5057 | -0.038 ± 0.0063 | -0.0157 (88) |
| 3-5 | 3078 | 0.1935 | 0.1919 | +0.0016 ± 0.0006 | 0.5634 | 0.5601 | 0.5028 | 0.4631 | 0.4626 | -0.052 ± 0.008 | -0.0209 (69) |
| 5-10 | 6278 | 0.1986 | 0.1917 | +0.0070 ± 0.0008 | 0.5839 | 0.5638 | 0.498 | 0.4243 | 0.4157 | -0.066 ± 0.0056 | -0.0082 (132) |
| 10-15 | 4381 | 0.211 | 0.1953 | +0.0156 ± 0.0017 | 0.6129 | 0.5719 | 0.536 | 0.4131 | 0.41 | -0.069 ± 0.0068 | -0.0053 (105) |
| 15-25 | 5301 | 0.2299 | 0.201 | +0.0289 ± 0.0024 | 0.6612 | 0.5814 | 0.5703 | 0.375 | 0.3997 | -0.063 ± 0.0062 | -0.0253 (107) |
| 25-40 | 3581 | 0.2605 | 0.1867 | +0.0738 ± 0.0045 | 0.7371 | 0.5449 | 0.6368 | 0.3242 | 0.3653 | -0.079 ± 0.0071 | -0.0229 (51) |
| 40+ | 1532 | 0.378 | 0.1538 | +0.2242 ± 0.0104 | 1.0704 | 0.46 | 0.7407 | 0.2392 | 0.2774 | -0.074 ± 0.0095 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5708 | 1.016 ± 0.037 | 1.09 | 0.1695 | 0.1664 | 0.215 | 0.2061 |
| gen2 | 5708 | 0.807 ± 0.034 | 1.054 | 0.1716 | 0.1668 | 0.2344 | 0.2059 |
| gen1_elo | 5708 | 0.993 ± 0.035 | 1.087 | 0.176 | 0.1665 | 0.2139 | 0.2062 |
| gen1_sr | 5708 | 0.99 ± 0.044 | 1.113 | 0.1317 | 0.1687 | 0.2304 | 0.2056 |
| gen1_ledger | 7864 | 0.856 ± 0.027 | 1.059 | 0.1879 | 0.176 | 0.2182 | 0.2013 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 28,520)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,411 | 22.5% |
| STALE_QUOTE | market_freshness | 6,285 | 22.0% |
| BOOK_QUALITY | execution | 5,382 | 18.9% |
| POOR_DATA | data | 3,339 | 11.7% |
| LIMITED_DATA | data | 1,768 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,624 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,225 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 1,170 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 825 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 490 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.5%, market_freshness 22.0%, execution 18.9%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.3%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.4%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.8%, THIN_PLAYER_HISTORY 60.4%, STALE_PLAYER_DATA 52.4%, STALE_KALSHI_QUOTE 44.4%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 18.2%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.4%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 15,239)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,179 | 34.0% |
| STALE_QUOTE | market_freshness | 2,864 | 18.8% |
| BOOK_QUALITY | execution | 2,805 | 18.4% |
| POOR_DATA | data | 1,431 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 852 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 625 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 534 | 3.5% |
| LIMITED_DATA | data | 519 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 306 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 123 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.0%, market_freshness 18.8%, execution 18.4%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.6%, STALE_KALSHI_QUOTE 52.2%, STALE_PLAYER_DATA 46.4%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 18.9%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.0%, POST_SETTLEMENT_OBSERVATION 34.0%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12119, "IDENTITY_AMBIGUOUS": 3120}; ticker orientation: {"VERIFIED": 15239}.

Checks: discipline:AMBIGUOUS 998, discipline:PASS 14241, identity_confidence:AMBIGUOUS 2799, identity_confidence:PASS 12440, level_mapping:NA 1010, level_mapping:PASS 14229, market_pair:AMBIGUOUS 480, market_pair:NA 348, market_pair:PASS 14411, model_complement:NA 312, model_complement:PASS 14927, namesake:AMBIGUOUS 6, namesake:PASS 15233, physical_match_id:NA 5296, physical_match_id:PASS 9943, player_ids:PASS 15239, same_pair_other_event:PASS 15239, ticker_orientation:PASS 15239

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,452 | 4.2% | 3.7% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.84 | 0.2219 / 0.2176 (635) | 21.9% | 2.9% | 3.2% | 2.8% |
| CHALLENGER | 9,993 | 16.5% | 6.2% | 10.8% | {"coverage": 975, "market_freshness/coverage": 198, "market_freshness": 170, "data": 144, "model_calibration_or_unknown": 74, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.25 | 0.2209 / 0.2116 (2283) | 35.5% | 15.6% | 4.1% | 22.7% |
| DOUBLES | 2,143 | 46.6% | 46.4% | 6.6% | {"execution": 565, "mapping": 261, "market_freshness": 106, "market_freshness/coverage": 59, "coverage": 7} | 23.41 | 0.309 / 0.2385 (515) | 10.9% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 19,803 | 25.0% | 17.7% | 32.5% | {"coverage": 1738, "market_freshness": 912, "execution": 912, "data": 731, "market_freshness/coverage": 474, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.72 | 0.2164 / 0.1996 (4064) | 37.9% | 69.5% | 16.5% | 21.5% |
| ITF_WOMEN | 26,016 | 26.6% | 19.2% | 45.4% | {"coverage": 2403, "market_freshness": 1471, "execution": 1214, "data": 982, "market_freshness/coverage": 585, "mapping": 158, "model_calibration_or_unknown": 81, "model_calibration": 21} | 12.55 | 0.2036 / 0.1953 (4768) | 39.7% | 57.2% | 10.0% | 21.4% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,964 | 5.7% | 4.8% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "coverage": 30, "execution": 27, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.45 | 0.2371 / 0.2301 (607) | 26.7% | 1.1% | 1.4% | 3.4% |
| WTA125 | 2,236 | 11.3% | 9.6% | 1.7% | {"market_freshness": 71, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 15, "coverage": 12, "mapping": 4} | 9.17 | 0.2103 / 0.1925 (658) | 26.1% | 11.0% | 4.8% | 7.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 117 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 19.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1173 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 658 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 32 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 82 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 46 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 50 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9703, "by_level_share_of_ge_25pp": {"ATP": 0.0149, "CHALLENGER": 0.1083, "DOUBLES": 0.0655, "ITF_MEN": 0.3253, "ITF_WOMEN": 0.4538, "OTHER": 0.0008, "WTA": 0.0148, "WTA125": 0.0166}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5225, "share_primary_cause_market_settled_or_in_play": 0.4308, "share_primary_cause_stale_quote_only": 0.1879}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15239, "identity_ambiguous_share": 0.2047, "ticker_orientation": {"VERIFIED": 15239}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9943, "with_external": 521, "coverage": 0.0524, "external_status": {"EXTERNAL_STALE": 321, "AGREES_WITH_KALSHI": 187, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 321, "MODEL_LONE_OUTLIER": 187, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3589, "share_external_supports_model": 0.025}, "pregame_clean_ge_25pp": {"n": 4739, "with_external": 494, "coverage": 0.1042, "external_status": {"EXTERNAL_STALE": 301, "AGREES_WITH_KALSHI": 180, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 301, "MODEL_LONE_OUTLIER": 180, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3644, "share_external_supports_model": 0.0263}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 473.0, "median_sample_ratio": 2.49, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2101, "data_status": {"POOR": 8635, "LIMITED": 3938, "ADEQUATE": 2666}, "comparison_lt_10pp": {"median_thinner_serve_points": 1682.0, "median_sample_ratio": 1.72, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1152, "model_minus_observed": 0.0534, "kalshi_minus_observed": -0.0857, "brier_diff_model_minus_kalshi": -0.0017}, "4-10x": {"n": 798, "model_minus_observed": 0.0844, "kalshi_minus_observed": -0.0623, "brier_diff_model_minus_kalshi": 0.0068}, "<2x": {"n": 2764, "model_minus_observed": 0.0914, "kalshi_minus_observed": -0.0319, "brier_diff_model_minus_kalshi": 0.0124}, ">=10x": {"n": 994, "model_minus_observed": 0.1158, "kalshi_minus_observed": -0.0586, "brier_diff_model_minus_kalshi": 0.0134}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5708, "model": {"intercept": -0.534, "slope": 0.807, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.193, "slope": 1.054, "slope_se": 0.037}, "mean_extremity_model": 0.1716, "mean_extremity_kalshi": 0.1668, "model_brier": 0.2344, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0285, "brier_diff_se": 0.0025, "model_logloss": 0.6665, "kalshi_logloss": 0.5948}, "fair_v1": {"n": 5708, "model": {"intercept": -0.417, "slope": 1.016, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.279, "slope": 1.09, "slope_se": 0.038}, "mean_extremity_model": 0.1695, "mean_extremity_kalshi": 0.1664, "model_brier": 0.215, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0089, "brier_diff_se": 0.0021, "model_logloss": 0.6191, "kalshi_logloss": 0.5951}, "gen1_elo": {"n": 5708, "model": {"intercept": -0.394, "slope": 0.993, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.297, "slope": 1.087, "slope_se": 0.037}, "mean_extremity_model": 0.176, "mean_extremity_kalshi": 0.1665, "model_brier": 0.2139, "kalshi_brier": 0.2062, "brier_diff_model_minus_kalshi": 0.0076, "brier_diff_se": 0.0021, "model_logloss": 0.6171, "kalshi_logloss": 0.5954}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2482, "share_ge_15": 0.4432, "median_abs_gap": 13.02, "n": 40066}, "gen1_elo": {"share_ge_25": 0.2462, "share_ge_15": 0.4412, "median_abs_gap": 12.93, "n": 40066}, "gen1_sr": {"share_ge_25": 0.3131, "share_ge_15": 0.5202, "median_abs_gap": 15.85, "n": 40066}, "gen2": {"share_ge_25": 0.3161, "share_ge_15": 0.5097, "median_abs_gap": 15.45, "n": 40066}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1529, "share_ge_15": 0.3552, "median_abs_gap": 10.71, "n": 30986}, "gen1_elo": {"share_ge_25": 0.1528, "share_ge_15": 0.3521, "median_abs_gap": 10.53, "n": 30985}, "gen1_sr": {"share_ge_25": 0.2174, "share_ge_15": 0.4409, "median_abs_gap": 13.01, "n": 30988}, "gen2": {"share_ge_25": 0.2339, "share_ge_15": 0.44, "median_abs_gap": 12.88, "n": 30988}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0416, "share_ge_25_pregame_clean": 0.0372}, "WTA": {"median_abs_gap_pregame_clean": 7.45, "share_ge_25_all": 0.0568, "share_ge_25_pregame_clean": 0.0481}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2364, "share_within_10pp_all": 0.4381, "share_within_10pp_pregame_clean": 0.4907, "corr_model_vs_mid_pregame_clean": 0.8506}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 827, "model_brier": 0.1993, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1000, "model_brier": 0.2201, "kalshi_brier": 0.2118, "brier_diff_model_minus_kalshi": 0.0084}, "15-25": {"n_settled": 1263, "model_brier": 0.2256, "kalshi_brier": 0.2126, "brier_diff_model_minus_kalshi": 0.0131}, "25-40": {"n_settled": 740, "model_brier": 0.2218, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.0163}, "3-5": {"n_settled": 523, "model_brier": 0.2055, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": -0.0004}, "40+": {"n_settled": 155, "model_brier": 0.2842, "kalshi_brier": 0.1885, "brier_diff_model_minus_kalshi": 0.0957}, "5-10": {"n_settled": 1200, "model_brier": 0.2014, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": -0.0003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.534, "slope": 0.807, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.193, "slope": 1.054, "slope_se": 0.037}, "n": 5708}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.491, "slope": 0.856, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.164, "slope": 1.059, "slope_se": 0.031}, "n": 7864}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 515, "model_brier": 0.309, "kalshi_brier": 0.2385, "brier_diff_model_minus_kalshi": 0.0705, "brier_diff_se": 0.0132, "corr_model_outcome": 0.0589, "corr_kalshi_outcome": 0.226}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
