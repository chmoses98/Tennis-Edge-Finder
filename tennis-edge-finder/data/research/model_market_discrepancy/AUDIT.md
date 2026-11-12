# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-12T13:21Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 90,591): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.7%, 40+ 8.3%; median gap 11.92 pp.
* **Where the extremes live**: 97.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.3%, Challenger 11.1%, doubles 6.4%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 19,975): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.1%, STALE_QUOTE 20.2%, BOOK_QUALITY 16.3%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.1%, market_freshness 20.2%, execution 16.3%, data 12.4%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 19,975 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.9% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 477.0 points vs 1667.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.025, Gen-2 0.823, Gen-1 ledger 0.869 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1020 model 0.2252 vs Kalshi 0.2041; n 212 model 0.3052 vs Kalshi 0.1675.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 376,583 model-market comparisons (623,066 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 124,022 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-12T13:07:48.547858+00:00'], shadow board 104,898 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-12T13:07:51.743569+00:00'], Model 4 44,141 rows, 31,121 settled tickers, 11,748 tickers with an external scan.
* By model: {"gen1_ledger": 82937, "gen1_elo": 52712, "fair_v1": 52712, "gen2": 52712, "gen1_sr": 52712, "model4_fundamental": 41441, "model4_conditioned": 41357}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 90,591 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.7 | 8.3 | 11.92 | 41.2% | 22.1% |
| MW fair_v1 | 52,712 | 12.6 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.3 | 13.19 | 44.9% | 25.3% |
| MW gen1_elo | 52,712 | 12.3 | 8.8 | 19.1 | 15.3 | 19.4 | 15.0 | 10.1 | 13.0 | 44.5% | 25.1% |
| MW gen1_ledger | 37,879 | 15.8 | 10.9 | 22.1 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 52,712 | 9.9 | 7.1 | 16.6 | 13.9 | 20.9 | 18.8 | 12.8 | 15.99 | 52.5% | 31.6% |
| MW gen2 | 52,712 | 10.8 | 7.5 | 16.6 | 13.7 | 19.7 | 17.7 | 13.9 | 15.52 | 51.3% | 31.6% |
| all families model4_conditioned | 41,357 | 22.2 | 17.9 | 34.6 | 16.9 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 41,441 | 17.3 | 13.5 | 34.0 | 20.0 | 9.9 | 3.8 | 1.5 | 7.61 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.4%, >=15pp 41.2%, >=20pp 30.4%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.57pp; >=10pp 45.6%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,119 | 27.9 | 15.8 | 28.1 | 13.3 | 10.7 | 3.5 | 0.6 | 5.82 | 14.9% | 4.2% |
| CHALLENGER | 8,285 | 16.4 | 9.6 | 20.6 | 15.3 | 15.7 | 11.3 | 11.1 | 10.93 | 38.2% | 22.5% |
| ITF_MEN | 15,462 | 9.6 | 7.3 | 17.1 | 14.9 | 21.1 | 17.2 | 12.8 | 15.45 | 51.1% | 30.0% |
| ITF_WOMEN | 20,413 | 9.3 | 7.1 | 16.1 | 14.7 | 22.2 | 18.7 | 12.0 | 16.01 | 52.8% | 30.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,100 | 16.6 | 13.3 | 25.0 | 20.7 | 16.6 | 6.7 | 1.1 | 8.63 | 24.4% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,119 | 26.3 | 15.7 | 26.3 | 15.8 | 11.3 | 3.9 | 0.8 | 6.1 | 16.0% | 4.7% |
| CHALLENGER | 8,285 | 14.4 | 9.1 | 19.0 | 13.9 | 18.4 | 13.7 | 11.6 | 12.52 | 43.6% | 25.2% |
| ITF_MEN | 15,462 | 8.1 | 6.2 | 15.2 | 13.9 | 20.4 | 19.9 | 16.4 | 17.83 | 56.6% | 36.3% |
| ITF_WOMEN | 20,413 | 7.8 | 5.9 | 14.1 | 12.7 | 20.7 | 21.2 | 17.6 | 19.13 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,100 | 14.1 | 10.3 | 21.6 | 16.2 | 22.5 | 12.8 | 2.5 | 11.21 | 37.7% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,119 | 23.4 | 14.1 | 25.6 | 15.5 | 14.3 | 6.0 | 1.1 | 7.04 | 21.4% | 7.1% |
| CHALLENGER | 8,285 | 15.1 | 9.6 | 20.8 | 15.6 | 16.1 | 11.9 | 10.9 | 11.2 | 38.9% | 22.9% |
| ITF_MEN | 15,462 | 9.3 | 7.3 | 17.2 | 14.2 | 21.4 | 17.3 | 13.2 | 15.75 | 51.9% | 30.5% |
| ITF_WOMEN | 20,413 | 9.2 | 6.8 | 16.3 | 15.6 | 22.1 | 18.6 | 11.4 | 15.75 | 52.1% | 30.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,100 | 22.5 | 17.3 | 31.8 | 15.3 | 8.9 | 3.3 | 1.0 | 6.12 | 13.2% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,490 | 28.1 | 19.5 | 29.2 | 12.2 | 8.1 | 2.5 | 0.4 | 5.25 | 11.1% | 3.0% |
| CHALLENGER | 5,017 | 22.9 | 14.5 | 27.8 | 14.8 | 13.0 | 5.4 | 1.5 | 7.02 | 20.0% | 6.9% |
| DOUBLES | 2,776 | 4.8 | 4.4 | 12.9 | 11.1 | 20.6 | 24.5 | 21.6 | 23.14 | 66.8% | 46.1% |
| ITF_MEN | 11,214 | 12.8 | 9.6 | 21.4 | 15.7 | 21.6 | 12.9 | 6.0 | 11.8 | 40.6% | 18.9% |
| ITF_WOMEN | 13,154 | 13.4 | 9.3 | 19.8 | 15.7 | 21.7 | 14.6 | 5.4 | 12.18 | 41.7% | 20.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,823 | 24.0 | 16.0 | 31.6 | 16.8 | 8.9 | 2.5 | 0.2 | 6.53 | 11.6% | 2.7% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,990 | 28.4 | 16.0 | 28.5 | 13.2 | 10.5 | 3.1 | 0.3 | 5.64 | 13.9% | 3.4% |
| CHALLENGER | 5,829 | 21.1 | 12.0 | 25.7 | 18.1 | 15.7 | 5.6 | 1.8 | 8.21 | 23.2% | 7.4% |
| ITF_MEN | 11,237 | 11.8 | 8.7 | 20.6 | 17.2 | 22.2 | 14.0 | 5.5 | 12.46 | 41.7% | 19.5% |
| ITF_WOMEN | 14,884 | 11.3 | 8.6 | 19.1 | 17.0 | 24.0 | 15.3 | 4.6 | 13.14 | 44.0% | 19.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,986 | 16.9 | 13.3 | 25.3 | 21.1 | 16.6 | 6.2 | 0.6 | 8.45 | 23.4% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,990 | 26.6 | 16.0 | 26.6 | 15.7 | 11.2 | 3.4 | 0.4 | 6.02 | 15.0% | 3.8% |
| CHALLENGER | 5,829 | 18.1 | 11.7 | 23.8 | 16.4 | 18.9 | 9.0 | 2.1 | 8.99 | 30.0% | 11.1% |
| ITF_MEN | 11,239 | 9.6 | 7.4 | 17.8 | 16.0 | 22.3 | 18.0 | 9.0 | 14.75 | 49.3% | 27.0% |
| ITF_WOMEN | 14,885 | 8.9 | 7.0 | 16.1 | 14.2 | 22.5 | 20.6 | 10.7 | 16.52 | 53.8% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,986 | 14.4 | 10.5 | 21.8 | 16.3 | 22.6 | 12.5 | 1.9 | 11.03 | 37.0% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,420 | 28.4 | 19.7 | 29.2 | 12.4 | 7.8 | 2.3 | 0.3 | 5.21 | 10.4% | 2.6% |
| CHALLENGER | 4,443 | 24.2 | 15.4 | 29.0 | 15.0 | 12.3 | 3.8 | 0.4 | 6.57 | 16.5% | 4.2% |
| DOUBLES | 2,603 | 4.7 | 4.5 | 13.1 | 11.1 | 20.5 | 24.4 | 21.7 | 23.04 | 66.6% | 46.1% |
| ITF_MEN | 9,697 | 13.6 | 10.1 | 22.8 | 16.2 | 21.7 | 11.4 | 4.1 | 10.94 | 37.3% | 15.5% |
| ITF_WOMEN | 11,334 | 14.1 | 9.9 | 20.9 | 16.2 | 21.9 | 13.5 | 3.6 | 11.42 | 38.9% | 17.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,760 | 24.3 | 16.4 | 31.6 | 16.8 | 8.9 | 2.0 | 0.1 | 6.43 | 10.9% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,776 | 4.8 | 4.4 | 12.9 | 11.1 | 20.6 | 24.5 | 21.6 | 23.14 | 66.8% | 46.1% |
| singles | 35,103 | 16.6 | 11.4 | 22.9 | 15.5 | 18.4 | 10.9 | 4.3 | 9.76 | 33.7% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,371 | 12.7 | 9.0 | 19.3 | 15.1 | 19.6 | 14.4 | 9.9 | 12.94 | 43.9% | 24.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 34,304 | 13.0 | 8.6 | 18.9 | 15.1 | 19.2 | 15.0 | 10.3 | 13.01 | 44.5% | 25.3% |
| UNKNOWN | 6,624 | 10.4 | 7.5 | 17.1 | 16.5 | 21.5 | 15.8 | 11.1 | 14.32 | 48.5% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,647 | 19.1 | 11.8 | 22.4 | 15.8 | 14.8 | 9.5 | 6.5 | 9.01 | 30.9% | 16.0% |
| B | 6,290 | 13.0 | 8.6 | 19.6 | 15.3 | 19.7 | 12.4 | 11.4 | 12.75 | 43.6% | 23.9% |
| C | 7,464 | 12.0 | 8.5 | 19.5 | 16.0 | 19.1 | 14.6 | 10.4 | 12.93 | 44.0% | 24.9% |
| D | 8,682 | 11.3 | 8.4 | 17.8 | 15.1 | 21.8 | 15.7 | 9.9 | 14.07 | 47.4% | 25.6% |
| F | 15,629 | 7.3 | 5.7 | 15.0 | 14.3 | 23.1 | 21.1 | 13.6 | 18.05 | 57.8% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,927 | 24.9 | 15.9 | 28.9 | 14.9 | 10.6 | 3.5 | 1.2 | 6.36 | 15.3% | 4.7% |
| B | 5,147 | 16.7 | 11.0 | 24.2 | 17.0 | 18.9 | 9.3 | 3.0 | 9.6 | 31.2% | 12.3% |
| C | 7,461 | 11.0 | 7.8 | 19.5 | 14.9 | 21.0 | 15.6 | 10.1 | 13.46 | 46.6% | 25.6% |
| D | 5,789 | 14.5 | 10.0 | 21.0 | 15.4 | 21.0 | 12.7 | 5.4 | 11.35 | 39.1% | 18.1% |
| F | 9,555 | 10.2 | 8.4 | 16.7 | 14.4 | 23.4 | 18.8 | 8.0 | 15.11 | 50.2% | 26.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,599 | 17.6 | 10.9 | 21.4 | 15.6 | 15.2 | 10.2 | 9.2 | 10.01 | 34.6% | 19.4% |
| LIMITED | 11,405 | 13.5 | 9.4 | 20.5 | 16.0 | 19.7 | 13.3 | 7.6 | 11.91 | 40.6% | 20.9% |
| POOR | 24,708 | 8.8 | 6.7 | 16.1 | 14.6 | 22.5 | 19.1 | 12.3 | 16.36 | 53.9% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,310 | 23.8 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.89 | 9.8% | 3.4% |
| GAME_SPREAD | 6,957 | 22.8 | 15.3 | 32.0 | 16.9 | 9.1 | 3.3 | 0.7 | 6.7 | 13.1% | 4.0% |
| MATCH_WINNER | 37,879 | 15.8 | 10.9 | 22.1 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,115 | 28.4 | 16.8 | 30.7 | 12.7 | 8.8 | 2.3 | 0.3 | 5.58 | 11.5% | 2.6% |
| TOTAL_GAMES | 11,652 | 9.7 | 10.8 | 36.3 | 25.7 | 10.4 | 4.2 | 2.9 | 9.14 | 17.5% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,710 | 24.5 | 28.8 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,567 | 46.7 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,080 | 6.5 | 9.8 | 40.9 | 29.8 | 7.3 | 3.3 | 2.4 | 9.16 | 12.9% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,746 | 23.8 | 16.6 | 34.7 | 14.8 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,576 | 20.3 | 13.4 | 28.4 | 20.2 | 12.2 | 4.3 | 1.1 | 7.71 | 17.7% | 5.5% |
| TOTAL_GAMES | 17,119 | 10.0 | 10.9 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.01 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 52,712 | 44.9% | 25.3% | 13.19 | 35.5% | 15.2% | 10.71 |
| gen1_elo | 52,712 | 44.5% | 25.1% | 13.0 | 34.9% | 15.0% | 10.51 |
| gen1_sr | 52,712 | 52.5% | 31.6% | 15.99 | 44.0% | 21.5% | 13.0 |
| gen2 | 52,712 | 51.3% | 31.6% | 15.52 | 43.9% | 23.0% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,313 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.72 | 35.4% | 15.3% |
| STALE | 32,399 | 10.8 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.6 | 15.37 | 50.9% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 31,347 | 16.3 | 11.1 | 22.6 | 15.2 | 18.2 | 11.5 | 5.0 | 9.97 | 34.7% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 90,591 | 31347 | 23785 | 35459 | 25.2 | 143.1 | 1451.1 |
| ge_15pp | 37,354 | 10870 | 8483 | 18001 | 29.1 | 446.0 | 1451.1 |
| ge_25pp | 19,975 | 5156 | 3709 | 11110 | 34.6 | 592.1 | 1431.1 |
| lt_10pp | 39,482 | 15701 | 11243 | 12538 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261112T132144Z-b46df0d8`: 322 priced rows, quote age at build {'median': 14.2, 'max': 14.3}, freshness {'AGING': 322}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,084 | 19.1 | 11.1 | 25.6 | 18.4 | 17.7 | 7.1 | 1.0 | 8.78 | 25.8% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,080 | 66.4 | 33.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,305 | 0.0 | 2.2 | 38.6 | 25.9 | 23.6 | 8.8 | 0.9 | 11.65 | 33.4% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 52,712 | 8582 (16.3%) | 26.9% | 1.0% | {"EXTERNAL_STALE": 5084, "AGREES_WITH_KALSHI": 2305, "ALL_AGREE": 1080, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 23,685 | 2110 (8.9%) | 36.4% | 1.5% | {"EXTERNAL_STALE": 1310, "AGREES_WITH_KALSHI": 769, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,357 | 647 (4.8%) | 34.6% | 2.0% | {"EXTERNAL_STALE": 410, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,101 | 615 (10.1%) | 35.3% | 2.1% | {"EXTERNAL_STALE": 385, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 21,012 | 4935 (23.5%) | 19.0% | 0.9% | {"EXTERNAL_STALE": 2841, "ALL_AGREE": 1080, "AGREES_WITH_KALSHI": 939, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,334 | 10.7 | 7.6 | 19.0 | 14.2 | 21.8 | 16.5 | 10.2 | 14.38 | 48.5% | 26.7% |
| 4-10x | 7,119 | 11.0 | 8.7 | 17.9 | 14.8 | 21.6 | 14.7 | 11.2 | 14.1 | 47.6% | 26.0% |
| <2x | 26,785 | 14.5 | 9.6 | 19.9 | 16.0 | 17.5 | 13.3 | 9.2 | 11.66 | 40.0% | 22.5% |
| >=10x | 8,474 | 10.1 | 6.5 | 15.1 | 14.3 | 21.8 | 18.9 | 13.2 | 16.51 | 54.0% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,821 | 12.4 | 8.6 | 19.7 | 16.1 | 19.1 | 13.7 | 10.5 | 12.81 | 43.3% | 24.2% |
| 300-1000 | 11,469 | 11.6 | 8.7 | 17.8 | 15.1 | 20.6 | 16.4 | 9.9 | 13.88 | 46.9% | 26.3% |
| <300 | 16,757 | 8.1 | 5.9 | 15.1 | 14.4 | 22.9 | 20.1 | 13.6 | 17.46 | 56.5% | 33.6% |
| >=3000 | 10,665 | 21.0 | 12.7 | 24.1 | 15.5 | 13.9 | 7.4 | 5.4 | 7.89 | 26.8% | 12.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1625 | 0.5471 | 0.4074 | 0.4757 | +0.071 | -0.068 | 0.004 ± 0.0038 |
| ratio 4-10x | 1106 | 0.5731 | 0.4286 | 0.4855 | +0.087 | -0.057 | 0.0101 ± 0.0048 |
| ratio <2x | 3956 | 0.5345 | 0.4118 | 0.4312 | +0.103 | -0.019 | 0.0151 ± 0.0023 |
| ratio >=10x | 1368 | 0.5605 | 0.3883 | 0.4349 | +0.126 | -0.047 | 0.0182 ± 0.0048 |
| thinner_sample 1000-3000 | 2219 | 0.5392 | 0.4122 | 0.4407 | +0.098 | -0.029 | 0.0136 ± 0.0031 |
| thinner_sample 300-1000 | 1829 | 0.5606 | 0.4206 | 0.4691 | +0.091 | -0.049 | 0.0061 ± 0.0036 |
| thinner_sample <300 | 2640 | 0.5535 | 0.3861 | 0.4428 | +0.111 | -0.057 | 0.0157 ± 0.0034 |
| thinner_sample >=3000 | 1367 | 0.5274 | 0.4339 | 0.4433 | +0.084 | -0.009 | 0.0143 ± 0.0031 |
| data_status ADEQUATE | 2184 | 0.5313 | 0.4288 | 0.4377 | +0.093 | -0.009 | 0.0155 ± 0.0026 |
| data_status LIMITED | 1956 | 0.5467 | 0.4138 | 0.4611 | +0.086 | -0.047 | 0.0085 ± 0.0034 |
| data_status POOR | 3915 | 0.5554 | 0.396 | 0.4478 | +0.108 | -0.052 | 0.0132 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1163 | 0.1965 | 0.1966 | -0.0001 ± 0.0005 | 0.5726 | 0.5729 | 0.503 | 0.4878 | 0.4953 | -0.098 ± 0.0138 | -0.0087 (8) |
| 3-5 | 744 | 0.2085 | 0.208 | +0.0005 ± 0.0013 | 0.603 | 0.5999 | 0.5028 | 0.463 | 0.4758 | -0.100 ± 0.0172 | 0.01 (3) |
| 5-10 | 1734 | 0.2026 | 0.201 | +0.0017 ± 0.0016 | 0.5918 | 0.5853 | 0.5082 | 0.4342 | 0.4585 | -0.091 ± 0.0111 | -0.0143 (7) |
| 10-15 | 1400 | 0.2189 | 0.2091 | +0.0098 ± 0.003 | 0.6298 | 0.6017 | 0.5246 | 0.4012 | 0.4221 | -0.106 ± 0.0124 | -0.055 (6) |
| 15-25 | 1782 | 0.2258 | 0.2063 | +0.0195 ± 0.0042 | 0.6468 | 0.5957 | 0.5715 | 0.377 | 0.4242 | -0.104 ± 0.0108 | -0.0045 (11) |
| 25-40 | 1020 | 0.2252 | 0.2041 | +0.0211 ± 0.0085 | 0.6406 | 0.5889 | 0.6444 | 0.3347 | 0.4549 | -0.066 ± 0.0132 | -0.06 (2) |
| 40+ | 212 | 0.3052 | 0.1675 | +0.1377 ± 0.0255 | 0.8164 | 0.5038 | 0.7246 | 0.2672 | 0.3538 | -0.087 ± 0.0246 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5890 | 0.1871 | 0.188 | -0.0009 ± 0.0002 | 0.5508 | 0.5519 | 0.4917 | 0.4764 | 0.509 | -0.020 ± 0.0057 | -0.01 (28) |
| 3-5 | 3982 | 0.1993 | 0.1973 | +0.0019 ± 0.0006 | 0.5796 | 0.5729 | 0.4819 | 0.4421 | 0.4372 | -0.059 ± 0.0071 | 0.005 (6) |
| 5-10 | 8731 | 0.2011 | 0.1968 | +0.0043 ± 0.0007 | 0.588 | 0.5741 | 0.4822 | 0.4083 | 0.4163 | -0.050 ± 0.0048 | -0.0114 (22) |
| 10-15 | 7114 | 0.2015 | 0.1854 | +0.0160 ± 0.0013 | 0.5894 | 0.5446 | 0.4849 | 0.361 | 0.3587 | -0.064 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9146 | 0.2061 | 0.1662 | +0.0399 ± 0.0017 | 0.604 | 0.4944 | 0.4973 | 0.3018 | 0.2984 | -0.069 ± 0.0043 | -0.0043 (51) |
| 25-40 | 7173 | 0.223 | 0.1238 | +0.0992 ± 0.0026 | 0.6401 | 0.3818 | 0.5237 | 0.2096 | 0.2126 | -0.059 ± 0.004 | -0.0733 (3) |
| 40+ | 4916 | 0.3802 | 0.0439 | +0.3363 ± 0.0034 | 0.9906 | 0.1704 | 0.6283 | 0.1016 | 0.0574 | -0.076 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 929 | 0.2022 | 0.2026 | -0.0004 ± 0.0005 | 0.5846 | 0.5859 | 0.5091 | 0.4941 | 0.521 | -0.094 ± 0.0158 | -0.0117 (6) |
| 3-5 | 672 | 0.2125 | 0.2097 | +0.0028 ± 0.0014 | 0.6087 | 0.6024 | 0.5181 | 0.4786 | 0.4598 | -0.126 ± 0.019 | 0.01 (3) |
| 5-10 | 1490 | 0.2048 | 0.203 | +0.0018 ± 0.0018 | 0.5953 | 0.5904 | 0.5375 | 0.4631 | 0.4899 | -0.086 ± 0.0121 | -0.01 (4) |
| 10-15 | 1305 | 0.215 | 0.2077 | +0.0073 ± 0.0032 | 0.6228 | 0.6013 | 0.5571 | 0.4327 | 0.4682 | -0.101 ± 0.0131 | -0.04 (5) |
| 15-25 | 1878 | 0.2326 | 0.2107 | +0.0219 ± 0.0042 | 0.6615 | 0.6051 | 0.5844 | 0.3888 | 0.4324 | -0.102 ± 0.0108 | -0.0183 (12) |
| 25-40 | 1304 | 0.2657 | 0.2005 | +0.0652 ± 0.0078 | 0.7412 | 0.5818 | 0.6592 | 0.3452 | 0.4003 | -0.108 ± 0.0125 | -0.008 (5) |
| 40+ | 477 | 0.3735 | 0.1593 | +0.2142 ± 0.0183 | 1.015 | 0.4833 | 0.7315 | 0.2433 | 0.2809 | -0.089 ± 0.0177 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5064 | 0.1902 | 0.1904 | -0.0002 ± 0.0002 | 0.5556 | 0.5558 | 0.5071 | 0.492 | 0.5065 | -0.040 ± 0.0063 | -0.0154 (26) |
| 3-5 | 3488 | 0.1941 | 0.1932 | +0.0009 ± 0.0006 | 0.5656 | 0.5627 | 0.5112 | 0.4715 | 0.4785 | -0.044 ± 0.0076 | 0.01 (5) |
| 5-10 | 7785 | 0.1957 | 0.1923 | +0.0034 ± 0.0007 | 0.5759 | 0.5631 | 0.506 | 0.4318 | 0.4486 | -0.039 ± 0.005 | -0.0117 (6) |
| 10-15 | 6480 | 0.2023 | 0.1903 | +0.0120 ± 0.0014 | 0.5941 | 0.5572 | 0.5065 | 0.3826 | 0.3971 | -0.049 ± 0.0055 | -0.0189 (18) |
| 15-25 | 9230 | 0.2156 | 0.1787 | +0.0369 ± 0.0017 | 0.6278 | 0.5252 | 0.5232 | 0.3278 | 0.3335 | -0.061 ± 0.0044 | -0.014 (52) |
| 25-40 | 8305 | 0.2503 | 0.1378 | +0.1124 ± 0.0026 | 0.7068 | 0.4204 | 0.5593 | 0.2419 | 0.227 | -0.076 ± 0.0041 | -0.0095 (20) |
| 40+ | 6600 | 0.4018 | 0.0593 | +0.3425 ± 0.0035 | 1.0586 | 0.2132 | 0.6545 | 0.119 | 0.0806 | -0.073 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1138 | 0.1962 | 0.1973 | -0.0011 ± 0.0005 | 0.5721 | 0.5747 | 0.5019 | 0.4864 | 0.5228 | -0.061 ± 0.0137 | -0.0191 (11) |
| 3-5 | 811 | 0.2087 | 0.2073 | +0.0013 ± 0.0013 | 0.6042 | 0.5995 | 0.4973 | 0.4577 | 0.4624 | -0.107 ± 0.0167 | 0.002 (5) |
| 5-10 | 1737 | 0.2027 | 0.1983 | +0.0044 ± 0.0016 | 0.5909 | 0.5786 | 0.5106 | 0.4368 | 0.4439 | -0.106 ± 0.011 | -0.01 (10) |
| 10-15 | 1443 | 0.2119 | 0.2022 | +0.0097 ± 0.0029 | 0.6141 | 0.5865 | 0.5382 | 0.4149 | 0.4394 | -0.105 ± 0.0119 | -0.0286 (7) |
| 15-25 | 1696 | 0.2316 | 0.212 | +0.0197 ± 0.0044 | 0.6608 | 0.6082 | 0.5807 | 0.3867 | 0.4328 | -0.105 ± 0.0112 | -0.03 (1) |
| 25-40 | 1005 | 0.2172 | 0.207 | +0.0102 ± 0.0085 | 0.6244 | 0.5953 | 0.6522 | 0.3423 | 0.4786 | -0.058 ± 0.0132 | -0.0267 (3) |
| 40+ | 225 | 0.3102 | 0.179 | +0.1312 ± 0.0254 | 0.8359 | 0.5294 | 0.7377 | 0.2808 | 0.3778 | -0.079 ± 0.0259 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5705 | 0.1866 | 0.1871 | -0.0005 ± 0.0002 | 0.5492 | 0.5496 | 0.487 | 0.4716 | 0.4852 | -0.038 ± 0.0058 | -0.0189 (44) |
| 3-5 | 4077 | 0.2049 | 0.2031 | +0.0018 ± 0.0006 | 0.595 | 0.5891 | 0.4818 | 0.4423 | 0.4403 | -0.057 ± 0.0072 | -0.0073 (22) |
| 5-10 | 8857 | 0.1957 | 0.1903 | +0.0054 ± 0.0007 | 0.5749 | 0.5578 | 0.4855 | 0.4115 | 0.4114 | -0.056 ± 0.0047 | -0.0117 (42) |
| 10-15 | 7128 | 0.1948 | 0.1793 | +0.0155 ± 0.0012 | 0.5748 | 0.5307 | 0.4962 | 0.3729 | 0.3718 | -0.063 ± 0.005 | -0.0136 (14) |
| 15-25 | 9186 | 0.2111 | 0.1717 | +0.0394 ± 0.0017 | 0.6157 | 0.5067 | 0.5093 | 0.3147 | 0.3116 | -0.069 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7159 | 0.2173 | 0.1237 | +0.0936 ± 0.0026 | 0.6279 | 0.3809 | 0.5253 | 0.2098 | 0.221 | -0.052 ± 0.004 | -0.02 (4) |
| 40+ | 4840 | 0.3886 | 0.0481 | +0.3405 ± 0.0036 | 1.0129 | 0.1809 | 0.6371 | 0.1071 | 0.0636 | -0.076 ± 0.003 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1610 | 0.1961 | 0.1958 | +0.0004 ± 0.0004 | 0.5704 | 0.5692 | 0.5085 | 0.4934 | 0.4888 | -0.077 ± 0.0113 | -0.0221 (56) |
| 3-5 | 1129 | 0.1883 | 0.1883 | +0.0000 ± 0.001 | 0.5543 | 0.5527 | 0.4983 | 0.4584 | 0.4765 | -0.055 ± 0.0132 | -0.0194 (34) |
| 5-10 | 2294 | 0.1992 | 0.1943 | +0.0049 ± 0.0014 | 0.5876 | 0.5718 | 0.508 | 0.4343 | 0.439 | -0.075 ± 0.0094 | -0.005 (78) |
| 10-15 | 1584 | 0.2155 | 0.2024 | +0.0131 ± 0.0028 | 0.625 | 0.5883 | 0.544 | 0.4213 | 0.428 | -0.092 ± 0.0116 | 0.0012 (66) |
| 15-25 | 2070 | 0.2321 | 0.2076 | +0.0245 ± 0.0039 | 0.6624 | 0.5989 | 0.592 | 0.397 | 0.4329 | -0.090 ± 0.0101 | -0.0214 (59) |
| 25-40 | 1211 | 0.2423 | 0.2119 | +0.0304 ± 0.0081 | 0.6913 | 0.607 | 0.688 | 0.3763 | 0.4839 | -0.083 ± 0.0125 | -0.0252 (27) |
| 40+ | 447 | 0.327 | 0.1977 | +0.1293 ± 0.0202 | 0.9349 | 0.5771 | 0.8081 | 0.3311 | 0.4497 | -0.091 ± 0.0189 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5804 | 0.1768 | 0.1768 | +0.0001 ± 0.0002 | 0.5238 | 0.5231 | 0.5098 | 0.4945 | 0.4998 | -0.043 ± 0.0056 | -0.0154 (103) |
| 3-5 | 3973 | 0.1938 | 0.1929 | +0.0009 ± 0.0006 | 0.566 | 0.5633 | 0.5019 | 0.4621 | 0.4707 | -0.041 ± 0.007 | -0.0212 (73) |
| 5-10 | 8124 | 0.1967 | 0.1903 | +0.0064 ± 0.0007 | 0.5805 | 0.561 | 0.5025 | 0.4289 | 0.4233 | -0.061 ± 0.0049 | -0.0084 (134) |
| 10-15 | 5566 | 0.211 | 0.194 | +0.0170 ± 0.0015 | 0.6139 | 0.5689 | 0.5372 | 0.4143 | 0.4053 | -0.074 ± 0.006 | -0.0057 (111) |
| 15-25 | 6848 | 0.2318 | 0.1991 | +0.0327 ± 0.0021 | 0.6662 | 0.5775 | 0.5763 | 0.3808 | 0.3952 | -0.069 ± 0.0054 | -0.026 (108) |
| 25-40 | 4414 | 0.2582 | 0.1908 | +0.0674 ± 0.0041 | 0.7297 | 0.555 | 0.6397 | 0.3275 | 0.3788 | -0.063 ± 0.0064 | -0.0277 (53) |
| 40+ | 1993 | 0.3689 | 0.1591 | +0.2097 ± 0.0092 | 1.0369 | 0.4744 | 0.7404 | 0.2409 | 0.291 | -0.058 ± 0.0085 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8055 | 1.025 ± 0.031 | 1.091 | 0.1676 | 0.1703 | 0.2158 | 0.2031 |
| gen2 | 8055 | 0.823 ± 0.028 | 1.069 | 0.1737 | 0.1706 | 0.2331 | 0.2031 |
| gen1_elo | 8055 | 1.009 ± 0.03 | 1.081 | 0.1741 | 0.1704 | 0.2149 | 0.2032 |
| gen1_sr | 8055 | 1.009 ± 0.037 | 1.116 | 0.1333 | 0.172 | 0.2293 | 0.2028 |
| gen1_ledger | 10345 | 0.869 ± 0.023 | 1.067 | 0.19 | 0.1768 | 0.2172 | 0.2 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 37,354)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,070 | 24.3% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,713 | 23.3% |
| BOOK_QUALITY | execution | 6,319 | 16.9% |
| POOR_DATA | data | 4,279 | 11.5% |
| LIMITED_DATA | data | 2,241 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,164 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,534 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,421 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,039 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 573 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.3%, coverage 23.3%, data 17.4%, execution 16.9%, market_freshness/coverage 8.6%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.0%, LOW_DATA_QUALITY 72.2%, THIN_PLAYER_HISTORY 60.3%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 48.2%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 33.3%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.7%, POST_SETTLEMENT_OBSERVATION 23.3%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 19,975)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,019 | 35.1% |
| STALE_QUOTE | market_freshness | 4,035 | 20.2% |
| BOOK_QUALITY | execution | 3,258 | 16.3% |
| POOR_DATA | data | 1,812 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,173 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 848 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 681 | 3.4% |
| LIMITED_DATA | data | 662 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 347 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 139 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.1%, market_freshness 20.2%, execution 16.3%, data 12.4%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.3%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 55.6%, STALE_PLAYER_DATA 45.5%, MODEL_INTERNAL_DISAGREEMENT 41.9%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 22.6%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 17.9%, LOW_DISPLAYED_LIQUIDITY 8.5%, EVENT_MAPPING_RISK 8.4%, LEVEL_TRANSFER_RISK 8.2%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.0%, POST_SETTLEMENT_OBSERVATION 35.1%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 16060, "IDENTITY_AMBIGUOUS": 3915}; ticker orientation: {"VERIFIED": 19975}.

Checks: discipline:AMBIGUOUS 1280, discipline:PASS 18695, identity_confidence:AMBIGUOUS 3568, identity_confidence:PASS 16407, level_mapping:NA 1292, level_mapping:PASS 18683, market_pair:AMBIGUOUS 511, market_pair:NA 427, market_pair:PASS 19037, model_complement:NA 389, model_complement:PASS 19586, namesake:AMBIGUOUS 6, namesake:PASS 19969, physical_match_id:NA 6618, physical_match_id:PASS 13357, player_ids:PASS 19975, same_pair_other_event:PASS 19975, ticker_orientation:PASS 19975

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,609 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.2218 / 0.2178 (863) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,302 | 16.6% | 6.0% | 11.1% | {"coverage": 1352, "market_freshness": 274, "market_freshness/coverage": 238, "data": 165, "model_calibration_or_unknown": 81, "execution": 41, "model_calibration": 40, "mapping": 17, "possible_market_error": 1} | 7.35 | 0.2214 / 0.2108 (3082) | 41.8% | 13.7% | 4.0% | 22.8% |
| DOUBLES | 2,776 | 46.1% | 46.1% | 6.4% | {"execution": 707, "mapping": 387, "market_freshness": 106, "market_freshness/coverage": 73, "coverage": 7} | 23.04 | 0.2982 / 0.2327 (693) | 8.4% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 26,676 | 25.3% | 17.6% | 33.8% | {"coverage": 2378, "market_freshness": 1416, "execution": 1042, "data": 998, "market_freshness/coverage": 686, "mapping": 228, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.75 | 0.2186 / 0.1985 (5615) | 42.3% | 70.1% | 14.5% | 21.5% |
| ITF_WOMEN | 33,567 | 26.5% | 18.7% | 44.5% | {"coverage": 3203, "market_freshness": 1978, "execution": 1385, "data": 1210, "market_freshness/coverage": 778, "mapping": 210, "model_calibration_or_unknown": 99, "model_calibration": 23} | 12.46 | 0.2029 / 0.1931 (6523) | 42.9% | 57.4% | 10.1% | 21.9% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,923 | 5.9% | 5.0% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.65 | 0.2315 / 0.221 (812) | 30.3% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 16.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 969 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 517 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.9h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 305 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 12 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 13 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 20.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1203 min (STALE); no external reference |
| 16 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 19 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 21 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 22 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 23 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 24 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 25 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 26 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 27 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 28 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 29 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 30 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 31 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 34 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 37 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 38 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 39 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 40 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 41 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 42 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 45 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 46 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 47 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 434 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 48 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 379 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9733, "by_level_share_of_ge_25pp": {"ATP": 0.0123, "CHALLENGER": 0.1106, "DOUBLES": 0.0641, "ITF_MEN": 0.3384, "ITF_WOMEN": 0.4449, "OTHER": 0.0006, "WTA": 0.0146, "WTA125": 0.0147}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5562, "share_primary_cause_market_settled_or_in_play": 0.4442, "share_primary_cause_stale_quote_only": 0.202}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 19975, "identity_ambiguous_share": 0.196, "ticker_orientation": {"VERIFIED": 19975}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13357, "with_external": 647, "coverage": 0.0484, "external_status": {"EXTERNAL_STALE": 410, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 410, "MODEL_LONE_OUTLIER": 224, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3462, "share_external_supports_model": 0.0201}, "pregame_clean_ge_25pp": {"n": 6101, "with_external": 615, "coverage": 0.1008, "external_status": {"EXTERNAL_STALE": 385, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 385, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3528, "share_external_supports_model": 0.0211}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 477.0, "median_sample_ratio": 2.46, "median_min_matches": 18.0, "median_max_days_since_last": 247.0, "share_severe_asymmetry": 0.2073, "data_status": {"POOR": 11390, "LIMITED": 5002, "ADEQUATE": 3583}, "comparison_lt_10pp": {"median_thinner_serve_points": 1667.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1625, "model_minus_observed": 0.0714, "kalshi_minus_observed": -0.0682, "brier_diff_model_minus_kalshi": 0.004}, "4-10x": {"n": 1106, "model_minus_observed": 0.0875, "kalshi_minus_observed": -0.0569, "brier_diff_model_minus_kalshi": 0.0101}, "<2x": {"n": 3956, "model_minus_observed": 0.1033, "kalshi_minus_observed": -0.0195, "brier_diff_model_minus_kalshi": 0.0151}, ">=10x": {"n": 1368, "model_minus_observed": 0.1255, "kalshi_minus_observed": -0.0467, "brier_diff_model_minus_kalshi": 0.0182}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8055, "model": {"intercept": -0.562, "slope": 0.823, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.171, "slope": 1.069, "slope_se": 0.031}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1706, "model_brier": 0.2331, "kalshi_brier": 0.2031, "brier_diff_model_minus_kalshi": 0.03, "brier_diff_se": 0.0021, "model_logloss": 0.6635, "kalshi_logloss": 0.5883}, "fair_v1": {"n": 8055, "model": {"intercept": -0.471, "slope": 1.025, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.217, "slope": 1.091, "slope_se": 0.032}, "mean_extremity_model": 0.1676, "mean_extremity_kalshi": 0.1703, "model_brier": 0.2158, "kalshi_brier": 0.2031, "brier_diff_model_minus_kalshi": 0.0127, "brier_diff_se": 0.0017, "model_logloss": 0.6209, "kalshi_logloss": 0.5883}, "gen1_elo": {"n": 8055, "model": {"intercept": -0.461, "slope": 1.009, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.218, "slope": 1.081, "slope_se": 0.031}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1704, "model_brier": 0.2149, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0117, "brier_diff_se": 0.0017, "model_logloss": 0.6195, "kalshi_logloss": 0.5885}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2534, "share_ge_15": 0.4493, "median_abs_gap": 13.19, "n": 52712}, "gen1_elo": {"share_ge_25": 0.2511, "share_ge_15": 0.4451, "median_abs_gap": 13.0, "n": 52712}, "gen1_sr": {"share_ge_25": 0.3159, "share_ge_15": 0.5248, "median_abs_gap": 15.99, "n": 52712}, "gen2": {"share_ge_25": 0.3159, "share_ge_15": 0.5128, "median_abs_gap": 15.52, "n": 52712}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1517, "share_ge_15": 0.355, "median_abs_gap": 10.71, "n": 40210}, "gen1_elo": {"share_ge_25": 0.1501, "share_ge_15": 0.3495, "median_abs_gap": 10.51, "n": 40210}, "gen1_sr": {"share_ge_25": 0.2153, "share_ge_15": 0.4402, "median_abs_gap": 13.0, "n": 40213}, "gen2": {"share_ge_25": 0.2302, "share_ge_15": 0.4389, "median_abs_gap": 12.84, "n": 40213}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0371, "share_ge_25_pregame_clean": 0.031}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0591, "share_ge_25_pregame_clean": 0.0501}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2344, "share_within_10pp_all": 0.4358, "share_within_10pp_pregame_clean": 0.4903, "corr_model_vs_mid_pregame_clean": 0.8502}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1163, "model_brier": 0.1965, "kalshi_brier": 0.1966, "brier_diff_model_minus_kalshi": -0.0001}, "10-15": {"n_settled": 1400, "model_brier": 0.2189, "kalshi_brier": 0.2091, "brier_diff_model_minus_kalshi": 0.0098}, "15-25": {"n_settled": 1782, "model_brier": 0.2258, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0195}, "25-40": {"n_settled": 1020, "model_brier": 0.2252, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": 0.0211}, "3-5": {"n_settled": 744, "model_brier": 0.2085, "kalshi_brier": 0.208, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 212, "model_brier": 0.3052, "kalshi_brier": 0.1675, "brier_diff_model_minus_kalshi": 0.1377}, "5-10": {"n_settled": 1734, "model_brier": 0.2026, "kalshi_brier": 0.201, "brier_diff_model_minus_kalshi": 0.0017}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.562, "slope": 0.823, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.171, "slope": 1.069, "slope_se": 0.031}, "n": 8055}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.502, "slope": 0.869, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.152, "slope": 1.067, "slope_se": 0.027}, "n": 10345}, "NO_SKILL:gen2|WTA": {"n_settled": 346, "model_brier": 0.25, "kalshi_brier": 0.2262, "brier_diff_model_minus_kalshi": 0.0238, "brier_diff_se": 0.0089, "corr_model_outcome": 0.2572, "corr_kalshi_outcome": 0.3102}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 693, "model_brier": 0.2982, "kalshi_brier": 0.2327, "brier_diff_model_minus_kalshi": 0.0655, "brier_diff_se": 0.0111, "corr_model_outcome": 0.1059, "corr_kalshi_outcome": 0.2754}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
