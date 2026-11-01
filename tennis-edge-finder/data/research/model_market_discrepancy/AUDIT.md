# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-01T18:59Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 72,487): 0-3 14.2%, 3-5 9.6%, 5-10 20.3%, 10-15 15.3%, 15-25 19.0%, 25-40 13.7%, 40+ 8.0%; median gap 11.77 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.6%, Challenger 10.8%, doubles 6.8%). Main tour: ATP 3.9% and WTA 5.8% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,726): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.1%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.4%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.1%, market_freshness 18.8%, execution 18.4%, data 12.7%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,726 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.7% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1753.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.026, Gen-2 0.817, Gen-1 ledger 0.861 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 769 model 0.2211 vs Kalshi 0.2071; n 159 model 0.2822 vs Kalshi 0.1885.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 309,848 model-market comparisons (505,148 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 105,025 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-01T18:43:49.646440+00:00'], shadow board 82,666 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-01T18:43:53.536676+00:00'], Model 4 38,760 rows, 25,299 settled tickers, 9,320 tickers with an external scan.
* By model: {"gen1_ledger": 71060, "gen1_elo": 41544, "fair_v1": 41544, "gen2": 41544, "gen1_sr": 41544, "model4_fundamental": 36330, "model4_conditioned": 36282}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 72,487 | 14.2 | 9.6 | 20.3 | 15.3 | 19.0 | 13.7 | 8.0 | 11.77 | 40.6% | 21.7% |
| MW fair_v1 | 41,544 | 13.0 | 8.7 | 18.9 | 15.3 | 19.5 | 14.8 | 9.9 | 12.97 | 44.1% | 24.7% |
| MW gen1_elo | 41,544 | 12.6 | 8.7 | 19.4 | 15.4 | 19.5 | 14.7 | 9.8 | 12.85 | 44.0% | 24.5% |
| MW gen1_ledger | 30,943 | 15.7 | 10.9 | 22.2 | 15.2 | 18.3 | 12.2 | 5.5 | 10.28 | 36.0% | 17.7% |
| MW gen1_sr | 41,544 | 10.2 | 7.2 | 16.9 | 13.9 | 20.6 | 18.5 | 12.7 | 15.74 | 51.8% | 31.1% |
| MW gen2 | 41,544 | 11.2 | 7.6 | 16.6 | 13.8 | 19.4 | 17.7 | 13.7 | 15.38 | 50.8% | 31.4% |
| all families model4_conditioned | 36,282 | 22.4 | 18.2 | 34.0 | 17.1 | 5.0 | 2.1 | 1.2 | 6.01 | 8.3% | 3.3% |
| all families model4_fundamental | 36,330 | 17.4 | 13.3 | 33.8 | 20.2 | 10.1 | 3.8 | 1.4 | 7.67 | 15.2% | 5.2% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 55.9%, >=15pp 40.6%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.21pp; >=10pp 44.5%, >=25pp 16.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,660 | 27.6 | 15.2 | 28.2 | 13.3 | 11.3 | 3.8 | 0.6 | 5.93 | 15.7% | 4.4% |
| CHALLENGER | 6,177 | 16.3 | 9.7 | 20.9 | 15.1 | 15.6 | 11.5 | 10.8 | 10.88 | 38.0% | 22.4% |
| ITF_MEN | 11,555 | 9.8 | 7.4 | 17.0 | 15.0 | 21.2 | 17.6 | 12.0 | 15.23 | 50.7% | 29.5% |
| ITF_WOMEN | 16,302 | 9.6 | 7.1 | 16.1 | 15.1 | 22.0 | 18.1 | 12.2 | 15.68 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,677 | 18.0 | 13.3 | 25.0 | 20.4 | 15.8 | 6.3 | 1.2 | 8.25 | 23.4% | 7.5% |
| WTA125 | 1,167 | 16.4 | 7.2 | 22.5 | 19.1 | 20.8 | 12.2 | 1.8 | 10.7 | 34.8% | 14.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,660 | 26.1 | 15.5 | 26.3 | 15.8 | 11.7 | 3.9 | 0.8 | 6.2 | 16.3% | 4.6% |
| CHALLENGER | 6,177 | 15.2 | 9.1 | 18.2 | 14.1 | 18.3 | 13.4 | 11.6 | 12.49 | 43.3% | 25.1% |
| ITF_MEN | 11,555 | 8.1 | 6.2 | 15.1 | 13.8 | 19.6 | 20.6 | 16.6 | 17.93 | 56.8% | 37.2% |
| ITF_WOMEN | 16,302 | 7.9 | 5.8 | 14.0 | 12.7 | 20.6 | 21.2 | 17.7 | 19.11 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,677 | 15.1 | 10.9 | 22.0 | 15.3 | 21.8 | 12.8 | 2.0 | 10.62 | 36.6% | 14.8% |
| WTA125 | 1,167 | 9.6 | 6.8 | 17.1 | 15.7 | 24.2 | 17.9 | 8.7 | 15.22 | 50.8% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,660 | 22.2 | 13.6 | 24.9 | 16.0 | 15.6 | 6.4 | 1.2 | 7.5 | 23.3% | 7.6% |
| CHALLENGER | 6,177 | 15.1 | 9.2 | 20.8 | 16.0 | 15.8 | 12.1 | 11.0 | 11.34 | 38.8% | 23.1% |
| ITF_MEN | 11,555 | 9.3 | 7.2 | 17.3 | 14.2 | 21.8 | 17.7 | 12.4 | 15.75 | 52.0% | 30.2% |
| ITF_WOMEN | 16,302 | 9.4 | 6.9 | 16.5 | 15.8 | 22.1 | 17.9 | 11.4 | 15.49 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,677 | 22.9 | 16.4 | 32.1 | 14.7 | 9.3 | 3.4 | 1.2 | 6.18 | 13.9% | 4.6% |
| WTA125 | 1,167 | 21.2 | 12.9 | 26.9 | 17.8 | 15.1 | 5.7 | 0.3 | 8.01 | 21.2% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,209 | 25.4 | 19.5 | 30.8 | 12.6 | 8.6 | 2.7 | 0.5 | 5.56 | 11.7% | 3.1% |
| CHALLENGER | 4,209 | 22.5 | 14.5 | 27.4 | 14.5 | 13.6 | 5.9 | 1.6 | 7.1 | 21.1% | 7.5% |
| DOUBLES | 2,262 | 5.2 | 4.3 | 11.8 | 10.5 | 20.6 | 25.5 | 22.1 | 23.85 | 68.2% | 47.6% |
| ITF_MEN | 8,710 | 13.0 | 9.5 | 21.2 | 15.8 | 21.4 | 13.2 | 5.8 | 11.87 | 40.4% | 19.1% |
| ITF_WOMEN | 10,563 | 13.2 | 9.1 | 19.9 | 15.8 | 21.2 | 15.3 | 5.6 | 12.32 | 42.0% | 20.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,658 | 24.1 | 16.4 | 30.5 | 17.0 | 9.0 | 2.8 | 0.2 | 6.54 | 12.0% | 3.0% |
| WTA125 | 1,183 | 24.9 | 12.9 | 21.1 | 19.4 | 13.4 | 6.8 | 1.5 | 7.85 | 21.7% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,558 | 27.9 | 15.3 | 28.6 | 13.3 | 11.1 | 3.5 | 0.3 | 5.89 | 14.9% | 3.8% |
| CHALLENGER | 4,342 | 21.2 | 12.2 | 26.0 | 17.6 | 15.5 | 6.0 | 1.6 | 8.05 | 23.1% | 7.6% |
| ITF_MEN | 8,420 | 12.1 | 8.8 | 20.6 | 17.1 | 21.9 | 14.2 | 5.2 | 12.34 | 41.3% | 19.4% |
| ITF_WOMEN | 12,099 | 11.5 | 8.5 | 18.7 | 17.2 | 24.0 | 15.0 | 5.1 | 13.22 | 44.1% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,580 | 18.3 | 13.3 | 25.3 | 20.7 | 15.8 | 5.8 | 0.7 | 8.2 | 22.4% | 6.6% |
| WTA125 | 1,127 | 16.6 | 7.1 | 22.1 | 19.4 | 21.3 | 11.9 | 1.6 | 10.8 | 34.8% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,558 | 26.4 | 15.8 | 26.5 | 15.7 | 11.6 | 3.5 | 0.4 | 6.13 | 15.6% | 3.9% |
| CHALLENGER | 4,342 | 19.3 | 11.6 | 22.9 | 16.6 | 18.6 | 9.0 | 1.9 | 8.99 | 29.6% | 11.0% |
| ITF_MEN | 8,421 | 9.6 | 7.4 | 17.5 | 16.0 | 21.4 | 18.7 | 9.4 | 14.88 | 49.5% | 28.1% |
| ITF_WOMEN | 12,100 | 8.9 | 6.8 | 15.9 | 14.3 | 22.8 | 20.6 | 10.8 | 16.58 | 54.1% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,580 | 15.3 | 11.0 | 22.3 | 15.5 | 21.9 | 12.6 | 1.4 | 10.53 | 35.9% | 14.0% |
| WTA125 | 1,127 | 9.6 | 6.8 | 17.3 | 15.8 | 24.2 | 18.1 | 8.2 | 15.14 | 50.5% | 26.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,152 | 25.5 | 19.7 | 30.8 | 12.7 | 8.3 | 2.6 | 0.4 | 5.53 | 11.2% | 2.9% |
| CHALLENGER | 3,719 | 23.9 | 15.4 | 28.6 | 14.6 | 13.0 | 4.1 | 0.5 | 6.61 | 17.5% | 4.6% |
| DOUBLES | 2,123 | 5.1 | 4.4 | 12.0 | 10.7 | 20.4 | 25.4 | 22.1 | 23.84 | 67.9% | 47.5% |
| ITF_MEN | 7,433 | 13.8 | 10.1 | 22.9 | 16.4 | 21.3 | 11.7 | 3.8 | 10.86 | 36.7% | 15.4% |
| ITF_WOMEN | 9,023 | 13.8 | 9.6 | 21.2 | 16.4 | 21.3 | 14.2 | 3.5 | 11.52 | 39.1% | 17.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,598 | 24.5 | 16.8 | 30.4 | 17.1 | 8.9 | 2.2 | 0.1 | 6.38 | 11.2% | 2.2% |
| WTA125 | 1,052 | 26.1 | 13.7 | 22.1 | 20.4 | 12.4 | 4.8 | 0.5 | 7.36 | 17.7% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,262 | 5.2 | 4.3 | 11.8 | 10.5 | 20.6 | 25.5 | 22.1 | 23.85 | 68.2% | 47.6% |
| singles | 28,681 | 16.6 | 11.4 | 23.0 | 15.6 | 18.1 | 11.2 | 4.2 | 9.75 | 33.5% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 18 | 11.1 | 11.1 | 38.9 | 11.1 | 5.6 | 22.2 | 0.0 | 8.48 | 27.8% | 22.2% |
| Clay | 8,124 | 13.1 | 9.3 | 20.2 | 15.7 | 19.0 | 13.6 | 8.9 | 12.27 | 41.6% | 22.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 27,427 | 13.5 | 8.7 | 18.8 | 15.1 | 19.2 | 14.8 | 10.0 | 12.9 | 44.0% | 24.8% |
| UNKNOWN | 5,738 | 10.4 | 7.7 | 17.1 | 16.3 | 21.3 | 16.1 | 11.1 | 14.29 | 48.5% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 11,722 | 20.1 | 11.9 | 22.6 | 15.6 | 14.8 | 8.9 | 6.1 | 8.52 | 29.8% | 15.0% |
| B | 5,191 | 12.8 | 8.9 | 19.5 | 15.8 | 19.4 | 12.6 | 10.9 | 12.58 | 42.9% | 23.5% |
| C | 5,931 | 11.7 | 8.8 | 19.9 | 15.8 | 18.5 | 14.6 | 10.8 | 12.91 | 43.9% | 25.3% |
| D | 6,578 | 11.9 | 8.4 | 17.7 | 15.2 | 21.6 | 15.8 | 9.4 | 13.76 | 46.8% | 25.2% |
| F | 12,122 | 7.4 | 5.5 | 15.1 | 14.8 | 23.3 | 20.9 | 13.0 | 17.63 | 57.1% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,399 | 24.4 | 16.1 | 29.2 | 14.9 | 10.7 | 3.5 | 1.2 | 6.41 | 15.4% | 4.7% |
| B | 4,404 | 16.6 | 10.7 | 24.0 | 16.9 | 18.9 | 9.7 | 3.1 | 9.71 | 31.7% | 12.8% |
| C | 6,066 | 11.3 | 7.8 | 19.1 | 14.5 | 20.9 | 15.9 | 10.4 | 13.69 | 47.2% | 26.3% |
| D | 4,533 | 14.2 | 9.9 | 21.7 | 15.5 | 20.0 | 13.3 | 5.4 | 11.26 | 38.7% | 18.7% |
| F | 7,541 | 10.0 | 8.3 | 16.0 | 14.8 | 23.2 | 19.8 | 7.7 | 15.4 | 50.7% | 27.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 13,245 | 18.3 | 10.8 | 21.8 | 15.4 | 15.1 | 9.8 | 8.8 | 9.71 | 33.7% | 18.6% |
| LIMITED | 9,218 | 13.6 | 9.9 | 20.5 | 16.0 | 19.2 | 13.3 | 7.6 | 11.77 | 40.0% | 20.8% |
| POOR | 19,081 | 9.0 | 6.6 | 16.1 | 15.0 | 22.6 | 19.0 | 11.8 | 16.08 | 53.3% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,323 | 23.9 | 17.9 | 33.0 | 15.7 | 6.4 | 2.7 | 0.4 | 5.9 | 9.5% | 3.1% |
| GAME_SPREAD | 6,225 | 22.3 | 15.1 | 32.7 | 17.0 | 9.0 | 3.3 | 0.6 | 6.74 | 13.0% | 3.9% |
| MATCH_WINNER | 30,943 | 15.7 | 10.9 | 22.2 | 15.2 | 18.3 | 12.2 | 5.5 | 10.28 | 36.0% | 17.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,166 | 27.7 | 16.7 | 30.7 | 12.8 | 9.4 | 2.5 | 0.3 | 5.67 | 12.2% | 2.8% |
| TOTAL_GAMES | 10,379 | 9.9 | 10.7 | 35.4 | 26.4 | 10.5 | 4.1 | 3.0 | 9.26 | 17.6% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,049 | 24.3 | 29.3 | 33.1 | 8.0 | 4.1 | 0.9 | 0.3 | 4.78 | 5.3% | 1.2% |
| GAME_SPREAD | 8,416 | 47.0 | 16.1 | 25.0 | 7.2 | 2.2 | 1.8 | 0.6 | 3.29 | 4.6% | 2.4% |
| TOTAL_GAMES | 14,817 | 6.7 | 9.6 | 40.0 | 30.8 | 7.3 | 3.3 | 2.3 | 9.27 | 12.9% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,064 | 23.8 | 16.6 | 34.8 | 14.8 | 7.0 | 2.6 | 0.4 | 6.05 | 10.0% | 3.0% |
| GAME_SPREAD | 8,419 | 20.1 | 13.6 | 28.2 | 20.2 | 12.2 | 4.5 | 1.1 | 7.75 | 17.9% | 5.7% |
| TOTAL_GAMES | 14,847 | 10.2 | 10.3 | 36.2 | 25.0 | 11.5 | 4.3 | 2.5 | 9.17 | 18.4% | 6.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 41,544 | 44.1% | 24.7% | 12.97 | 35.2% | 15.1% | 10.64 |
| gen1_elo | 41,544 | 44.0% | 24.5% | 12.85 | 35.0% | 15.1% | 10.5 |
| gen1_sr | 41,544 | 51.8% | 31.1% | 15.74 | 43.8% | 21.5% | 12.94 |
| gen2 | 41,544 | 50.8% | 31.4% | 15.38 | 43.8% | 23.1% | 12.79 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,963 | 15.6 | 10.5 | 21.4 | 17.2 | 20.1 | 11.9 | 3.3 | 10.68 | 35.2% | 15.2% |
| STALE | 22,581 | 10.8 | 7.2 | 16.7 | 13.8 | 19.0 | 17.2 | 15.4 | 15.6 | 51.6% | 32.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 24,411 | 16.4 | 11.2 | 22.8 | 15.3 | 17.7 | 11.7 | 4.8 | 9.85 | 34.2% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 72,487 | 24411 | 22435 | 25641 | 24.4 | 122.9 | 1451.1 |
| ge_15pp | 29,467 | 8338 | 7971 | 13158 | 27.0 | 435.4 | 1451.1 |
| ge_25pp | 15,726 | 4017 | 3471 | 8238 | 32.1 | 586.7 | 1431.1 |
| lt_10pp | 31,940 | 12333 | 10650 | 8957 | 22.4 | 47.0 | 1421.1 |

Current slate `SL-20261101T185951Z-90acc72f`: 661 priced rows, quote age at build {'median': 16.4, 'max': 16.5}, freshness {'AGING': 661}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 48 | 0.0 | 0.0 | 35.4 | 6.2 | 33.3 | 20.8 | 4.2 | 19.13 | 58.3% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 25 | 64.0 | 36.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,123 | 19.7 | 11.0 | 25.3 | 17.9 | 18.0 | 7.2 | 0.9 | 8.65 | 26.1% | 8.1% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 855 | 66.3 | 33.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.19 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,845 | 0.0 | 2.3 | 37.2 | 25.9 | 24.1 | 9.6 | 0.9 | 11.85 | 34.5% | 10.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 41,544 | 6923 (16.7%) | 26.7% | 1.1% | {"EXTERNAL_STALE": 4123, "AGREES_WITH_KALSHI": 1845, "ALL_AGREE": 855, "SUPPORTS_MODEL_DIRECTION": 47, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 25, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 18,330 | 1743 (9.5%) | 36.5% | 1.7% | {"EXTERNAL_STALE": 1076, "AGREES_WITH_KALSHI": 637, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,247 | 540 (5.3%) | 35.7% | 2.4% | {"EXTERNAL_STALE": 334, "AGREES_WITH_KALSHI": 193, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,848 | 513 (10.6%) | 36.3% | 2.5% | {"EXTERNAL_STALE": 314, "AGREES_WITH_KALSHI": 186, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 16,838 | 3958 (23.5%) | 18.4% | 1.0% | {"EXTERNAL_STALE": 2308, "ALL_AGREE": 855, "AGREES_WITH_KALSHI": 730, "EXTERNAL_OUTLIER": 25, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 16, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,060 | 10.5 | 7.5 | 19.4 | 14.4 | 21.6 | 16.5 | 10.0 | 14.11 | 48.1% | 26.5% |
| 4-10x | 5,559 | 11.1 | 8.6 | 18.8 | 15.4 | 21.8 | 14.2 | 10.0 | 13.57 | 46.1% | 24.2% |
| <2x | 21,252 | 15.2 | 9.9 | 19.8 | 15.9 | 17.3 | 12.9 | 8.9 | 11.5 | 39.1% | 21.8% |
| >=10x | 6,673 | 10.4 | 6.4 | 15.1 | 14.5 | 21.7 | 19.1 | 12.8 | 16.27 | 53.6% | 31.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,868 | 12.7 | 8.8 | 19.8 | 15.9 | 19.1 | 13.4 | 10.4 | 12.69 | 42.9% | 23.8% |
| 300-1000 | 8,919 | 11.9 | 8.8 | 17.9 | 15.2 | 20.2 | 16.4 | 9.6 | 13.58 | 46.2% | 25.9% |
| <300 | 13,141 | 8.3 | 5.8 | 15.2 | 14.8 | 23.0 | 19.9 | 12.9 | 17.03 | 55.9% | 32.8% |
| >=3000 | 8,616 | 21.6 | 12.8 | 24.3 | 15.6 | 13.6 | 7.0 | 5.0 | 7.57 | 25.6% | 12.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1203 | 0.5508 | 0.4122 | 0.4963 | +0.055 | -0.084 | -0.002 ± 0.0044 |
| ratio 4-10x | 830 | 0.5833 | 0.437 | 0.4976 | +0.086 | -0.061 | 0.0072 ± 0.0055 |
| ratio <2x | 2975 | 0.5373 | 0.4154 | 0.4447 | +0.093 | -0.029 | 0.0123 ± 0.0026 |
| ratio >=10x | 1024 | 0.5687 | 0.3942 | 0.4521 | +0.117 | -0.058 | 0.0138 ± 0.0057 |
| thinner_sample 1000-3000 | 1684 | 0.5388 | 0.4126 | 0.4519 | +0.087 | -0.039 | 0.0089 ± 0.0035 |
| thinner_sample 300-1000 | 1361 | 0.5693 | 0.4278 | 0.4864 | +0.083 | -0.059 | 0.0028 ± 0.0043 |
| thinner_sample <300 | 1963 | 0.5612 | 0.3935 | 0.4615 | +0.100 | -0.068 | 0.0106 ± 0.004 |
| thinner_sample >=3000 | 1024 | 0.531 | 0.4382 | 0.4561 | +0.075 | -0.018 | 0.0143 ± 0.0035 |
| data_status ADEQUATE | 1672 | 0.533 | 0.431 | 0.4462 | +0.087 | -0.015 | 0.0134 ± 0.003 |
| data_status LIMITED | 1489 | 0.5496 | 0.4169 | 0.4728 | +0.077 | -0.056 | 0.0063 ± 0.0039 |
| data_status POOR | 2871 | 0.5637 | 0.4029 | 0.4688 | +0.095 | -0.066 | 0.0079 ± 0.0032 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 884 | 0.2 | 0.2005 | -0.0005 ± 0.0005 | 0.5805 | 0.5817 | 0.503 | 0.4878 | 0.509 | -0.086 ± 0.016 | -0.0087 (8) |
| 3-5 | 552 | 0.2055 | 0.2052 | +0.0003 ± 0.0016 | 0.5945 | 0.5919 | 0.5051 | 0.4653 | 0.4801 | -0.105 ± 0.0198 | 0.01 (2) |
| 5-10 | 1291 | 0.2013 | 0.201 | +0.0004 ± 0.0019 | 0.5886 | 0.5856 | 0.511 | 0.4372 | 0.4694 | -0.090 ± 0.013 | -0.0143 (7) |
| 10-15 | 1044 | 0.2195 | 0.2106 | +0.0088 ± 0.0035 | 0.631 | 0.6062 | 0.5289 | 0.4053 | 0.4301 | -0.107 ± 0.0143 | -0.048 (5) |
| 15-25 | 1333 | 0.2246 | 0.2103 | +0.0143 ± 0.0049 | 0.6444 | 0.6043 | 0.5773 | 0.3821 | 0.4434 | -0.101 ± 0.0126 | -0.004 (10) |
| 25-40 | 769 | 0.2211 | 0.2071 | +0.0140 ± 0.0098 | 0.6315 | 0.5964 | 0.6573 | 0.3472 | 0.4798 | -0.071 ± 0.015 | -0.06 (2) |
| 40+ | 159 | 0.2822 | 0.1885 | +0.0938 ± 0.03 | 0.7687 | 0.5556 | 0.7384 | 0.2904 | 0.4151 | -0.073 ± 0.0297 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4777 | 0.1855 | 0.1863 | -0.0009 ± 0.0002 | 0.5465 | 0.5474 | 0.4876 | 0.4724 | 0.5035 | -0.022 ± 0.0063 | -0.01 (28) |
| 3-5 | 3201 | 0.1951 | 0.1931 | +0.0020 ± 0.0006 | 0.5689 | 0.5618 | 0.4827 | 0.443 | 0.4367 | -0.061 ± 0.0078 | 0.0 (3) |
| 5-10 | 6903 | 0.2012 | 0.1976 | +0.0036 ± 0.0008 | 0.588 | 0.5761 | 0.4851 | 0.4115 | 0.4246 | -0.046 ± 0.0054 | -0.0114 (22) |
| 10-15 | 5667 | 0.2016 | 0.1857 | +0.0160 ± 0.0014 | 0.5894 | 0.5458 | 0.4853 | 0.3613 | 0.3582 | -0.066 ± 0.0057 | -0.0281 (16) |
| 15-25 | 7099 | 0.2065 | 0.168 | +0.0385 ± 0.0019 | 0.6054 | 0.4986 | 0.5001 | 0.3044 | 0.3048 | -0.069 ± 0.0048 | -0.0027 (45) |
| 25-40 | 5520 | 0.2214 | 0.1258 | +0.0956 ± 0.003 | 0.6369 | 0.3867 | 0.5265 | 0.2124 | 0.2216 | -0.058 ± 0.0046 | -0.0733 (3) |
| 40+ | 3660 | 0.3837 | 0.0449 | +0.3388 ± 0.004 | 0.9999 | 0.1733 | 0.633 | 0.1041 | 0.0607 | -0.077 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 702 | 0.2072 | 0.2078 | -0.0006 ± 0.0006 | 0.5968 | 0.5986 | 0.5056 | 0.4908 | 0.5214 | -0.100 ± 0.0187 | -0.0117 (6) |
| 3-5 | 498 | 0.2167 | 0.2143 | +0.0024 ± 0.0017 | 0.6162 | 0.6117 | 0.5165 | 0.4769 | 0.4618 | -0.126 ± 0.0222 | 0.01 (2) |
| 5-10 | 1117 | 0.2073 | 0.205 | +0.0023 ± 0.002 | 0.6015 | 0.5948 | 0.5429 | 0.4682 | 0.4924 | -0.096 ± 0.014 | -0.01 (4) |
| 10-15 | 969 | 0.2143 | 0.2096 | +0.0047 ± 0.0037 | 0.6189 | 0.606 | 0.5657 | 0.4415 | 0.4881 | -0.098 ± 0.0153 | -0.04 (5) |
| 15-25 | 1404 | 0.2288 | 0.2125 | +0.0162 ± 0.0048 | 0.6519 | 0.6095 | 0.5834 | 0.3881 | 0.4466 | -0.096 ± 0.0125 | -0.012 (10) |
| 25-40 | 984 | 0.2677 | 0.1994 | +0.0682 ± 0.0089 | 0.7477 | 0.5799 | 0.6614 | 0.3478 | 0.3984 | -0.127 ± 0.0143 | -0.008 (5) |
| 40+ | 358 | 0.3652 | 0.1654 | +0.1998 ± 0.0213 | 0.9991 | 0.4981 | 0.7333 | 0.2486 | 0.2989 | -0.084 ± 0.0208 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4110 | 0.1917 | 0.192 | -0.0003 ± 0.0002 | 0.5593 | 0.5595 | 0.5077 | 0.4927 | 0.51 | -0.039 ± 0.0071 | -0.0154 (26) |
| 3-5 | 2801 | 0.1944 | 0.1933 | +0.0011 ± 0.0007 | 0.5653 | 0.5617 | 0.5119 | 0.4722 | 0.4763 | -0.048 ± 0.0085 | 0.01 (2) |
| 5-10 | 6121 | 0.1983 | 0.1948 | +0.0035 ± 0.0008 | 0.5818 | 0.5689 | 0.5099 | 0.4358 | 0.4517 | -0.042 ± 0.0057 | -0.0117 (6) |
| 10-15 | 5092 | 0.2031 | 0.1917 | +0.0113 ± 0.0015 | 0.5952 | 0.5611 | 0.5125 | 0.3887 | 0.4059 | -0.049 ± 0.0062 | -0.0189 (18) |
| 15-25 | 7130 | 0.2166 | 0.1806 | +0.0361 ± 0.002 | 0.6303 | 0.5302 | 0.5227 | 0.3275 | 0.3359 | -0.062 ± 0.0051 | -0.0084 (43) |
| 25-40 | 6488 | 0.2508 | 0.1369 | +0.1138 ± 0.0029 | 0.708 | 0.4189 | 0.5587 | 0.2421 | 0.2243 | -0.083 ± 0.0046 | -0.0095 (20) |
| 40+ | 5085 | 0.3996 | 0.0587 | +0.3409 ± 0.0039 | 1.0546 | 0.2114 | 0.6535 | 0.1181 | 0.0812 | -0.073 ± 0.0033 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 837 | 0.1955 | 0.1977 | -0.0022 ± 0.0005 | 0.5703 | 0.5757 | 0.5022 | 0.4869 | 0.5484 | -0.036 ± 0.0161 | -0.012 (10) |
| 3-5 | 594 | 0.207 | 0.2048 | +0.0022 ± 0.0015 | 0.5992 | 0.5919 | 0.4985 | 0.4588 | 0.4529 | -0.123 ± 0.0193 | -0.0 (4) |
| 5-10 | 1329 | 0.2027 | 0.1998 | +0.0028 ± 0.0018 | 0.5907 | 0.5821 | 0.5116 | 0.4378 | 0.4545 | -0.102 ± 0.0127 | -0.01 (9) |
| 10-15 | 1055 | 0.2087 | 0.2028 | +0.0059 ± 0.0034 | 0.6069 | 0.5889 | 0.5419 | 0.4185 | 0.4578 | -0.100 ± 0.0139 | -0.0286 (7) |
| 15-25 | 1264 | 0.2342 | 0.2164 | +0.0178 ± 0.0051 | 0.667 | 0.6178 | 0.5901 | 0.3959 | 0.447 | -0.111 ± 0.0131 | -0.03 (1) |
| 25-40 | 785 | 0.2117 | 0.2128 | -0.0011 ± 0.0096 | 0.6113 | 0.6097 | 0.6651 | 0.3547 | 0.5096 | -0.057 ± 0.0148 | -0.0267 (3) |
| 40+ | 168 | 0.3002 | 0.1961 | +0.1040 ± 0.0301 | 0.8181 | 0.5732 | 0.7497 | 0.3001 | 0.4167 | -0.080 ± 0.0314 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4569 | 0.1842 | 0.1849 | -0.0007 ± 0.0002 | 0.5426 | 0.5437 | 0.4829 | 0.4676 | 0.4898 | -0.029 ± 0.0064 | -0.0137 (41) |
| 3-5 | 3198 | 0.2023 | 0.1999 | +0.0023 ± 0.0006 | 0.5882 | 0.5805 | 0.4807 | 0.4412 | 0.4321 | -0.065 ± 0.008 | -0.01 (19) |
| 5-10 | 7044 | 0.1938 | 0.1892 | +0.0046 ± 0.0008 | 0.5703 | 0.5555 | 0.4873 | 0.4133 | 0.4201 | -0.051 ± 0.0052 | -0.0105 (37) |
| 10-15 | 5636 | 0.1923 | 0.1787 | +0.0136 ± 0.0014 | 0.5688 | 0.5294 | 0.496 | 0.3726 | 0.3786 | -0.057 ± 0.0056 | -0.0146 (13) |
| 15-25 | 7234 | 0.2137 | 0.174 | +0.0397 ± 0.0019 | 0.6219 | 0.5122 | 0.5145 | 0.3199 | 0.3166 | -0.072 ± 0.0049 | -0.0533 (3) |
| 25-40 | 5525 | 0.2164 | 0.1285 | +0.0879 ± 0.003 | 0.6259 | 0.3928 | 0.5298 | 0.2142 | 0.2349 | -0.048 ± 0.0047 | -0.02 (4) |
| 40+ | 3621 | 0.3935 | 0.0506 | +0.3428 ± 0.0042 | 1.0262 | 0.1881 | 0.6425 | 0.1109 | 0.0677 | -0.077 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1260 | 0.195 | 0.1951 | -0.0000 ± 0.0004 | 0.5683 | 0.5681 | 0.5059 | 0.4908 | 0.4937 | -0.071 ± 0.0127 | -0.0213 (54) |
| 3-5 | 890 | 0.189 | 0.1887 | +0.0003 ± 0.0012 | 0.5544 | 0.5526 | 0.4977 | 0.4579 | 0.473 | -0.061 ± 0.0149 | -0.0194 (34) |
| 5-10 | 1844 | 0.2011 | 0.1965 | +0.0045 ± 0.0016 | 0.591 | 0.5764 | 0.5044 | 0.4307 | 0.4371 | -0.075 ± 0.0106 | -0.005 (78) |
| 10-15 | 1256 | 0.217 | 0.2036 | +0.0134 ± 0.0032 | 0.6263 | 0.5911 | 0.5395 | 0.4167 | 0.422 | -0.092 ± 0.0131 | 0.0014 (65) |
| 15-25 | 1616 | 0.2308 | 0.2094 | +0.0213 ± 0.0045 | 0.6578 | 0.6035 | 0.5862 | 0.3914 | 0.4369 | -0.085 ± 0.0115 | -0.0214 (59) |
| 25-40 | 1010 | 0.2418 | 0.2108 | +0.0310 ± 0.0088 | 0.6913 | 0.6044 | 0.6875 | 0.3755 | 0.4822 | -0.091 ± 0.0136 | -0.0252 (27) |
| 40+ | 340 | 0.3331 | 0.2051 | +0.1279 ± 0.0236 | 0.9673 | 0.596 | 0.8195 | 0.3426 | 0.4618 | -0.101 ± 0.0222 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4741 | 0.1754 | 0.1756 | -0.0002 ± 0.0002 | 0.5198 | 0.5199 | 0.5108 | 0.4955 | 0.5079 | -0.037 ± 0.0061 | -0.0145 (98) |
| 3-5 | 3265 | 0.1947 | 0.1937 | +0.0010 ± 0.0006 | 0.5673 | 0.5649 | 0.5032 | 0.4634 | 0.4708 | -0.044 ± 0.0078 | -0.0204 (72) |
| 5-10 | 6671 | 0.198 | 0.1915 | +0.0065 ± 0.0008 | 0.5823 | 0.5632 | 0.5004 | 0.4267 | 0.4208 | -0.063 ± 0.0054 | -0.0084 (134) |
| 10-15 | 4592 | 0.2113 | 0.1953 | +0.0160 ± 0.0016 | 0.6133 | 0.572 | 0.5373 | 0.4144 | 0.4094 | -0.071 ± 0.0066 | -0.0053 (106) |
| 15-25 | 5531 | 0.2301 | 0.2006 | +0.0295 ± 0.0024 | 0.6615 | 0.5807 | 0.5728 | 0.3774 | 0.401 | -0.064 ± 0.0061 | -0.026 (108) |
| 25-40 | 3713 | 0.2592 | 0.1885 | +0.0707 ± 0.0045 | 0.7335 | 0.5497 | 0.6381 | 0.3255 | 0.3711 | -0.074 ± 0.007 | -0.0246 (52) |
| 40+ | 1597 | 0.3754 | 0.1576 | +0.2178 ± 0.0103 | 1.0635 | 0.469 | 0.7446 | 0.2422 | 0.2868 | -0.069 ± 0.0095 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6032 | 1.026 ± 0.036 | 1.1 | 0.1694 | 0.1659 | 0.2145 | 0.2055 |
| gen2 | 6032 | 0.817 ± 0.033 | 1.069 | 0.1717 | 0.1663 | 0.2334 | 0.2053 |
| gen1_elo | 6032 | 1.002 ± 0.035 | 1.092 | 0.1762 | 0.166 | 0.2136 | 0.2056 |
| gen1_sr | 6032 | 1.006 ± 0.043 | 1.128 | 0.1321 | 0.1681 | 0.2296 | 0.205 |
| gen1_ledger | 8216 | 0.861 ± 0.026 | 1.067 | 0.1883 | 0.175 | 0.2176 | 0.2012 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 29,467)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,635 | 22.5% |
| STALE_QUOTE | market_freshness | 6,526 | 22.1% |
| BOOK_QUALITY | execution | 5,555 | 18.9% |
| POOR_DATA | data | 3,406 | 11.6% |
| LIMITED_DATA | data | 1,850 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,682 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,251 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,212 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 844 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 505 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.5%, market_freshness 22.1%, execution 18.9%, data 17.8%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.4%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.7%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 44.6%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 18.4%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.4%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 7.6%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 15,726)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,356 | 34.1% |
| STALE_QUOTE | market_freshness | 2,949 | 18.8% |
| BOOK_QUALITY | execution | 2,898 | 18.4% |
| POOR_DATA | data | 1,457 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 883 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 658 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 548 | 3.5% |
| LIMITED_DATA | data | 543 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 308 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 125 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.1%, market_freshness 18.8%, execution 18.4%, data 12.7%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 74.9%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 52.4%, STALE_PLAYER_DATA 46.1%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.1%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 19.0%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.2%, EVENT_MAPPING_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.1%, POST_SETTLEMENT_OBSERVATION 34.1%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12498, "IDENTITY_AMBIGUOUS": 3228}; ticker orientation: {"VERIFIED": 15726}.

Checks: discipline:AMBIGUOUS 1076, discipline:PASS 14650, identity_confidence:AMBIGUOUS 2904, identity_confidence:PASS 12822, level_mapping:NA 1088, level_mapping:PASS 14638, market_pair:AMBIGUOUS 483, market_pair:NA 352, market_pair:PASS 14891, model_complement:NA 315, model_complement:PASS 15411, namesake:AMBIGUOUS 6, namesake:PASS 15720, physical_match_id:NA 5479, physical_match_id:PASS 10247, player_ids:PASS 15726, same_pair_other_event:PASS 15726, ticker_orientation:PASS 15726

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,869 | 3.9% | 3.5% | 1.5% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 15} | 5.74 | 0.2219 / 0.216 (705) | 23.2% | 2.7% | 3.1% | 2.7% |
| CHALLENGER | 10,386 | 16.4% | 6.2% | 10.8% | {"coverage": 997, "market_freshness/coverage": 202, "market_freshness": 180, "data": 153, "model_calibration_or_unknown": 74, "execution": 40, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.28 | 0.2204 / 0.2104 (2401) | 35.8% | 15.9% | 4.2% | 22.4% |
| DOUBLES | 2,262 | 47.6% | 47.5% | 6.8% | {"execution": 611, "mapping": 291, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.84 | 0.3069 / 0.2391 (543) | 10.3% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 20,265 | 25.0% | 17.5% | 32.3% | {"coverage": 1803, "market_freshness": 932, "execution": 915, "data": 742, "market_freshness/coverage": 491, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.66 | 0.2163 / 0.2003 (4192) | 38.2% | 68.8% | 16.2% | 21.8% |
| ITF_WOMEN | 26,865 | 26.5% | 19.1% | 45.3% | {"coverage": 2486, "market_freshness": 1510, "execution": 1250, "data": 1007, "market_freshness/coverage": 606, "mapping": 161, "model_calibration_or_unknown": 82, "model_calibration": 21} | 12.53 | 0.2032 / 0.1949 (4980) | 39.9% | 57.1% | 9.9% | 21.4% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,335 | 5.8% | 4.9% | 1.6% | {"market_freshness": 88, "model_calibration_or_unknown": 44, "coverage": 34, "execution": 29, "data": 24, "model_calibration": 19, "market_freshness/coverage": 12, "mapping": 1} | 7.5 | 0.2296 / 0.2241 (681) | 27.5% | 1.8% | 1.4% | 3.6% |
| WTA125 | 2,350 | 11.1% | 9.5% | 1.7% | {"market_freshness": 74, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 24, "model_calibration": 16, "coverage": 13, "mapping": 4} | 9.14 | 0.2104 / 0.1928 (704) | 26.8% | 10.6% | 4.5% | 7.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 628 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 547 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 124 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT31KUHDEK-KUH` | ITF_WOMEN | fair_v1 | 84% / 6% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 224 min (STALE); data LIMITED (grade C, thinner serve sample 1253.0, ratio 1.41); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9694, "by_level_share_of_ge_25pp": {"ATP": 0.0146, "CHALLENGER": 0.108, "DOUBLES": 0.0684, "ITF_MEN": 0.3227, "ITF_WOMEN": 0.4529, "OTHER": 0.0008, "WTA": 0.016, "WTA125": 0.0166}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5238, "share_primary_cause_market_settled_or_in_play": 0.4315, "share_primary_cause_stale_quote_only": 0.1875}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15726, "identity_ambiguous_share": 0.2053, "ticker_orientation": {"VERIFIED": 15726}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10247, "with_external": 540, "coverage": 0.0527, "external_status": {"EXTERNAL_STALE": 334, "AGREES_WITH_KALSHI": 193, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 334, "MODEL_LONE_OUTLIER": 193, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3574, "share_external_supports_model": 0.0241}, "pregame_clean_ge_25pp": {"n": 4848, "with_external": 513, "coverage": 0.1058, "external_status": {"EXTERNAL_STALE": 314, "AGREES_WITH_KALSHI": 186, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 314, "MODEL_LONE_OUTLIER": 186, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3626, "share_external_supports_model": 0.0253}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.47, "median_min_matches": 20.0, "median_max_days_since_last": 237.0, "share_severe_asymmetry": 0.2076, "data_status": {"POOR": 8821, "LIMITED": 4136, "ADEQUATE": 2769}, "comparison_lt_10pp": {"median_thinner_serve_points": 1753.0, "median_sample_ratio": 1.69, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1203, "model_minus_observed": 0.0546, "kalshi_minus_observed": -0.084, "brier_diff_model_minus_kalshi": -0.002}, "4-10x": {"n": 830, "model_minus_observed": 0.0858, "kalshi_minus_observed": -0.0606, "brier_diff_model_minus_kalshi": 0.0072}, "<2x": {"n": 2975, "model_minus_observed": 0.0926, "kalshi_minus_observed": -0.0293, "brier_diff_model_minus_kalshi": 0.0123}, ">=10x": {"n": 1024, "model_minus_observed": 0.1165, "kalshi_minus_observed": -0.058, "brier_diff_model_minus_kalshi": 0.0138}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6032, "model": {"intercept": -0.532, "slope": 0.817, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.198, "slope": 1.069, "slope_se": 0.037}, "mean_extremity_model": 0.1717, "mean_extremity_kalshi": 0.1663, "model_brier": 0.2334, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.0281, "brier_diff_se": 0.0024, "model_logloss": 0.6641, "kalshi_logloss": 0.5937}, "fair_v1": {"n": 6032, "model": {"intercept": -0.423, "slope": 1.026, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.272, "slope": 1.1, "slope_se": 0.037}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1659, "model_brier": 0.2145, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.009, "brier_diff_se": 0.002, "model_logloss": 0.6179, "kalshi_logloss": 0.5939}, "gen1_elo": {"n": 6032, "model": {"intercept": -0.407, "slope": 1.002, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.282, "slope": 1.092, "slope_se": 0.036}, "mean_extremity_model": 0.1762, "mean_extremity_kalshi": 0.166, "model_brier": 0.2136, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0081, "brier_diff_se": 0.002, "model_logloss": 0.6165, "kalshi_logloss": 0.5942}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2467, "share_ge_15": 0.4412, "median_abs_gap": 12.97, "n": 41544}, "gen1_elo": {"share_ge_25": 0.2449, "share_ge_15": 0.4398, "median_abs_gap": 12.85, "n": 41544}, "gen1_sr": {"share_ge_25": 0.3115, "share_ge_15": 0.5181, "median_abs_gap": 15.74, "n": 41544}, "gen2": {"share_ge_25": 0.3142, "share_ge_15": 0.5081, "median_abs_gap": 15.38, "n": 41544}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1508, "share_ge_15": 0.3524, "median_abs_gap": 10.64, "n": 32132}, "gen1_elo": {"share_ge_25": 0.1507, "share_ge_15": 0.3501, "median_abs_gap": 10.5, "n": 32131}, "gen1_sr": {"share_ge_25": 0.2151, "share_ge_15": 0.4377, "median_abs_gap": 12.94, "n": 32134}, "gen2": {"share_ge_25": 0.2313, "share_ge_15": 0.4375, "median_abs_gap": 12.79, "n": 32134}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.74, "share_ge_25_all": 0.0392, "share_ge_25_pregame_clean": 0.0347}, "WTA": {"median_abs_gap_pregame_clean": 7.5, "share_ge_25_all": 0.0579, "share_ge_25_pregame_clean": 0.0491}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2378, "share_within_10pp_all": 0.4406, "share_within_10pp_pregame_clean": 0.4935, "corr_model_vs_mid_pregame_clean": 0.8509}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 884, "model_brier": 0.2, "kalshi_brier": 0.2005, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 1044, "model_brier": 0.2195, "kalshi_brier": 0.2106, "brier_diff_model_minus_kalshi": 0.0088}, "15-25": {"n_settled": 1333, "model_brier": 0.2246, "kalshi_brier": 0.2103, "brier_diff_model_minus_kalshi": 0.0143}, "25-40": {"n_settled": 769, "model_brier": 0.2211, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.014}, "3-5": {"n_settled": 552, "model_brier": 0.2055, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0003}, "40+": {"n_settled": 159, "model_brier": 0.2822, "kalshi_brier": 0.1885, "brier_diff_model_minus_kalshi": 0.0938}, "5-10": {"n_settled": 1291, "model_brier": 0.2013, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.532, "slope": 0.817, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.198, "slope": 1.069, "slope_se": 0.037}, "n": 6032}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.485, "slope": 0.861, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.171, "slope": 1.067, "slope_se": 0.03}, "n": 8216}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 543, "model_brier": 0.3069, "kalshi_brier": 0.2391, "brier_diff_model_minus_kalshi": 0.0678, "brier_diff_se": 0.0129, "corr_model_outcome": 0.0592, "corr_kalshi_outcome": 0.226}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
