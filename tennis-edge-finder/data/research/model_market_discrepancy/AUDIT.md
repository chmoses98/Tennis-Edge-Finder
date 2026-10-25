# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-25T17:48Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 54,134): 0-3 13.9%, 3-5 9.5%, 5-10 19.8%, 10-15 15.4%, 15-25 19.3%, 25-40 14.0%, 40+ 8.2%; median gap 12.06 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.1%, Challenger 11.9%, doubles 7.1%). Main tour: ATP 4.5% and WTA 5.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,984): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.3%, BOOK_QUALITY 18.7%, STALE_QUOTE 18.6%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.3%, execution 18.7%, market_freshness 18.6%, data 12.0%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,984 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.3% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1761.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.03, Gen-2 0.826, Gen-1 ledger 0.857 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 583 model 0.2219 vs Kalshi 0.2101; n 116 model 0.2743 vs Kalshi 0.202.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 236,487 model-market comparisons (383,141 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 79,942 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-25T17:39:49.943684+00:00'], shadow board 62,357 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-25T17:39:53.131601+00:00'], Model 4 30,029 rows, 20,531 settled tickers, 7,263 tickers with an external scan.
* By model: {"gen1_ledger": 54682, "gen1_elo": 31357, "fair_v1": 31357, "gen2": 31357, "gen1_sr": 31357, "model4_fundamental": 28209, "model4_conditioned": 28168}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 54,134 | 13.9 | 9.5 | 19.8 | 15.4 | 19.3 | 14.0 | 8.2 | 12.06 | 41.4% | 22.1% |
| MW fair_v1 | 31,357 | 12.8 | 8.6 | 18.5 | 15.6 | 19.8 | 14.9 | 9.8 | 13.14 | 44.5% | 24.8% |
| MW gen1_elo | 31,357 | 12.7 | 8.5 | 19.0 | 15.2 | 19.9 | 14.9 | 9.6 | 13.0 | 44.5% | 24.6% |
| MW gen1_ledger | 22,777 | 15.4 | 10.7 | 21.6 | 15.1 | 18.6 | 12.6 | 5.9 | 10.55 | 37.1% | 18.5% |
| MW gen1_sr | 31,357 | 10.2 | 7.1 | 16.8 | 13.6 | 20.8 | 18.7 | 12.9 | 15.98 | 52.3% | 31.6% |
| MW gen2 | 31,357 | 11.0 | 7.3 | 16.2 | 14.0 | 19.4 | 17.9 | 14.0 | 15.58 | 51.3% | 31.9% |
| all families model4_conditioned | 28,168 | 21.7 | 18.6 | 34.6 | 17.8 | 4.6 | 1.6 | 1.1 | 6.05 | 7.3% | 2.7% |
| all families model4_fundamental | 28,209 | 16.7 | 13.2 | 34.0 | 20.7 | 10.5 | 3.5 | 1.4 | 7.83 | 15.4% | 4.9% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.8%, >=15pp 41.4%, >=20pp 30.8%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.41pp; >=10pp 45.2%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,857 | 27.6 | 14.3 | 25.7 | 15.3 | 11.9 | 4.5 | 0.7 | 6.17 | 17.1% | 5.2% |
| CHALLENGER | 4,962 | 15.7 | 10.0 | 20.2 | 15.7 | 15.4 | 12.3 | 10.7 | 11.12 | 38.4% | 23.0% |
| ITF_MEN | 8,526 | 10.1 | 7.2 | 16.7 | 14.7 | 21.5 | 17.6 | 12.2 | 15.49 | 51.3% | 29.8% |
| ITF_WOMEN | 12,265 | 9.4 | 6.9 | 15.8 | 15.3 | 22.4 | 18.2 | 11.9 | 15.82 | 52.5% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,028 | 17.2 | 13.3 | 26.2 | 19.4 | 17.4 | 5.9 | 0.6 | 8.25 | 23.9% | 6.5% |
| WTA125 | 713 | 13.2 | 7.3 | 21.9 | 21.3 | 21.3 | 13.0 | 2.0 | 11.7 | 36.3% | 15.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,857 | 23.9 | 15.0 | 25.3 | 17.8 | 12.6 | 4.5 | 0.9 | 6.7 | 18.0% | 5.4% |
| CHALLENGER | 4,962 | 14.9 | 8.8 | 18.1 | 14.7 | 18.0 | 14.0 | 11.5 | 12.67 | 43.4% | 25.4% |
| ITF_MEN | 8,526 | 8.1 | 5.8 | 14.4 | 13.0 | 19.6 | 21.1 | 17.9 | 18.8 | 58.6% | 39.0% |
| ITF_WOMEN | 12,265 | 8.2 | 5.6 | 13.7 | 13.1 | 20.6 | 21.1 | 17.8 | 19.21 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,028 | 14.2 | 10.3 | 22.3 | 16.0 | 22.6 | 13.3 | 1.2 | 10.87 | 37.2% | 14.5% |
| WTA125 | 713 | 6.5 | 5.2 | 17.0 | 17.7 | 25.4 | 19.6 | 8.7 | 16.74 | 53.7% | 28.3% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,857 | 23.4 | 12.5 | 24.3 | 16.3 | 15.5 | 6.8 | 1.3 | 7.52 | 23.5% | 8.1% |
| CHALLENGER | 4,962 | 14.4 | 9.2 | 20.8 | 15.4 | 16.3 | 13.0 | 10.9 | 11.47 | 40.2% | 23.9% |
| ITF_MEN | 8,526 | 9.6 | 7.3 | 16.8 | 13.8 | 22.1 | 17.9 | 12.4 | 15.98 | 52.5% | 30.3% |
| ITF_WOMEN | 12,265 | 9.4 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.1 | 15.62 | 51.9% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,028 | 23.7 | 17.2 | 30.7 | 15.3 | 9.8 | 2.6 | 0.7 | 6.04 | 13.1% | 3.3% |
| WTA125 | 713 | 22.4 | 11.4 | 27.4 | 16.1 | 15.8 | 6.5 | 0.4 | 7.99 | 22.7% | 6.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,770 | 24.9 | 19.2 | 29.9 | 13.1 | 9.6 | 3.0 | 0.3 | 5.67 | 12.9% | 3.3% |
| CHALLENGER | 3,432 | 21.1 | 14.2 | 26.6 | 14.8 | 14.9 | 6.6 | 1.8 | 7.45 | 23.3% | 8.4% |
| DOUBLES | 1,783 | 5.1 | 4.5 | 12.3 | 10.3 | 20.1 | 25.9 | 21.8 | 23.94 | 67.8% | 47.6% |
| ITF_MEN | 6,303 | 13.7 | 9.2 | 19.8 | 16.1 | 21.5 | 13.3 | 6.4 | 12.19 | 41.2% | 19.7% |
| ITF_WOMEN | 7,342 | 12.5 | 8.8 | 19.4 | 15.3 | 21.7 | 16.1 | 6.1 | 12.84 | 43.9% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,206 | 22.6 | 15.6 | 30.5 | 18.2 | 9.5 | 3.2 | 0.3 | 6.86 | 13.1% | 3.6% |
| WTA125 | 792 | 20.8 | 13.4 | 22.0 | 18.4 | 14.7 | 8.6 | 2.1 | 8.32 | 25.4% | 10.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,778 | 28.0 | 14.5 | 26.1 | 15.2 | 11.7 | 4.1 | 0.4 | 6.01 | 16.2% | 4.5% |
| CHALLENGER | 3,517 | 20.4 | 12.5 | 24.9 | 18.1 | 15.5 | 6.8 | 1.8 | 8.43 | 24.1% | 8.6% |
| ITF_MEN | 6,227 | 12.2 | 8.8 | 20.1 | 16.7 | 22.7 | 14.4 | 5.1 | 12.57 | 42.2% | 19.5% |
| ITF_WOMEN | 9,168 | 11.2 | 8.2 | 18.0 | 17.4 | 24.4 | 15.4 | 5.5 | 13.56 | 45.2% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,969 | 17.5 | 13.1 | 26.3 | 19.6 | 17.4 | 5.5 | 0.7 | 8.25 | 23.6% | 6.2% |
| WTA125 | 687 | 13.5 | 7.1 | 21.4 | 21.7 | 22.0 | 12.7 | 1.6 | 11.7 | 36.2% | 14.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,778 | 24.1 | 15.4 | 25.5 | 17.7 | 12.6 | 4.2 | 0.5 | 6.5 | 17.3% | 4.7% |
| CHALLENGER | 3,517 | 19.0 | 11.3 | 22.4 | 17.4 | 18.3 | 9.6 | 2.0 | 9.36 | 29.9% | 11.6% |
| ITF_MEN | 6,228 | 9.7 | 7.1 | 16.8 | 15.1 | 21.5 | 19.3 | 10.5 | 15.48 | 51.4% | 29.8% |
| ITF_WOMEN | 9,169 | 9.3 | 6.5 | 15.2 | 14.5 | 22.6 | 20.6 | 11.4 | 16.82 | 54.6% | 32.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,969 | 14.4 | 10.3 | 22.3 | 16.1 | 22.6 | 13.1 | 1.3 | 10.87 | 37.0% | 14.4% |
| WTA125 | 687 | 6.3 | 5.4 | 17.0 | 18.1 | 25.3 | 20.1 | 7.9 | 16.64 | 53.3% | 28.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,719 | 25.0 | 19.5 | 30.0 | 13.2 | 9.2 | 2.9 | 0.2 | 5.65 | 12.3% | 3.1% |
| CHALLENGER | 3,010 | 22.5 | 15.2 | 27.9 | 14.8 | 14.3 | 4.7 | 0.5 | 6.94 | 19.5% | 5.2% |
| DOUBLES | 1,663 | 5.0 | 4.6 | 12.6 | 10.4 | 20.0 | 25.8 | 21.5 | 23.87 | 67.3% | 47.3% |
| ITF_MEN | 5,282 | 14.9 | 9.8 | 21.5 | 16.9 | 21.4 | 11.6 | 3.9 | 11.22 | 36.9% | 15.5% |
| ITF_WOMEN | 6,096 | 13.4 | 9.3 | 20.8 | 16.1 | 21.9 | 14.9 | 3.6 | 11.79 | 40.3% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,154 | 23.1 | 16.0 | 30.5 | 18.2 | 9.5 | 2.6 | 0.1 | 6.8 | 12.2% | 2.7% |
| WTA125 | 681 | 22.6 | 14.7 | 23.4 | 19.8 | 13.1 | 5.9 | 0.6 | 7.6 | 19.5% | 6.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,783 | 5.1 | 4.5 | 12.3 | 10.3 | 20.1 | 25.9 | 21.8 | 23.94 | 67.8% | 47.6% |
| singles | 20,994 | 16.3 | 11.2 | 22.4 | 15.6 | 18.5 | 11.5 | 4.5 | 10.01 | 34.5% | 16.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 11 | 9.1 | 18.2 | 45.5 | 0.0 | 9.1 | 18.2 | 0.0 | 7.98 | 27.3% | 18.2% |
| Clay | 6,875 | 12.9 | 9.0 | 19.2 | 15.8 | 19.1 | 14.2 | 9.8 | 12.76 | 43.0% | 24.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 19,588 | 13.3 | 8.6 | 18.6 | 15.2 | 19.7 | 14.8 | 9.6 | 13.04 | 44.2% | 24.5% |
| UNKNOWN | 4,646 | 10.7 | 7.5 | 16.9 | 16.8 | 20.6 | 16.4 | 11.0 | 14.15 | 48.0% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,022 | 19.5 | 12.0 | 21.7 | 16.5 | 14.9 | 9.2 | 6.2 | 9.06 | 30.3% | 15.4% |
| B | 3,896 | 12.3 | 8.7 | 19.4 | 16.3 | 19.6 | 12.8 | 10.9 | 12.79 | 43.3% | 23.7% |
| C | 4,377 | 11.7 | 8.9 | 19.6 | 15.3 | 19.4 | 14.6 | 10.5 | 13.1 | 44.5% | 25.1% |
| D | 4,795 | 12.0 | 7.8 | 17.4 | 15.4 | 21.7 | 15.7 | 10.0 | 14.0 | 47.4% | 25.7% |
| F | 9,267 | 7.5 | 5.5 | 15.0 | 14.6 | 23.6 | 21.2 | 12.5 | 17.82 | 57.4% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,544 | 23.1 | 15.9 | 28.9 | 15.2 | 11.5 | 4.0 | 1.4 | 6.68 | 16.9% | 5.4% |
| B | 3,095 | 16.0 | 10.4 | 23.2 | 16.2 | 19.9 | 10.5 | 3.8 | 10.06 | 34.2% | 14.2% |
| C | 4,497 | 10.9 | 7.2 | 18.5 | 14.4 | 21.1 | 16.8 | 11.1 | 14.46 | 49.0% | 27.9% |
| D | 3,099 | 14.3 | 9.6 | 19.9 | 14.8 | 21.1 | 14.3 | 6.0 | 12.05 | 41.4% | 20.3% |
| F | 5,542 | 10.2 | 8.3 | 15.8 | 15.2 | 22.7 | 19.7 | 8.1 | 15.27 | 50.5% | 27.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,294 | 17.7 | 10.7 | 21.0 | 16.1 | 15.6 | 10.1 | 8.7 | 10.14 | 34.4% | 18.8% |
| LIMITED | 6,657 | 13.4 | 10.2 | 20.1 | 16.0 | 19.4 | 13.3 | 7.6 | 11.93 | 40.3% | 20.9% |
| POOR | 14,406 | 9.1 | 6.3 | 15.9 | 15.0 | 22.9 | 19.1 | 11.7 | 16.29 | 53.7% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,692 | 24.9 | 18.8 | 33.6 | 14.2 | 6.0 | 2.2 | 0.2 | 5.64 | 8.5% | 2.5% |
| GAME_SPREAD | 5,102 | 22.3 | 15.3 | 33.3 | 17.1 | 9.1 | 2.5 | 0.3 | 6.72 | 11.9% | 2.8% |
| MATCH_WINNER | 22,777 | 15.4 | 10.7 | 21.6 | 15.1 | 18.6 | 12.6 | 5.9 | 10.55 | 37.1% | 18.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 11,834 | 27.9 | 16.4 | 31.3 | 12.7 | 9.2 | 2.3 | 0.3 | 5.68 | 11.8% | 2.6% |
| TOTAL_GAMES | 8,253 | 9.1 | 9.9 | 36.2 | 27.9 | 10.5 | 3.6 | 2.9 | 9.4 | 17.0% | 6.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,124 | 24.5 | 31.9 | 32.7 | 6.3 | 3.6 | 0.8 | 0.2 | 4.61 | 4.6% | 1.0% |
| GAME_SPREAD | 6,605 | 45.8 | 16.8 | 26.6 | 7.9 | 1.7 | 0.9 | 0.3 | 3.43 | 2.9% | 1.3% |
| TOTAL_GAMES | 11,439 | 5.2 | 7.9 | 40.9 | 33.7 | 7.2 | 2.8 | 2.3 | 9.56 | 12.3% | 5.1% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,135 | 23.5 | 17.1 | 35.3 | 13.9 | 7.3 | 2.6 | 0.4 | 6.03 | 10.2% | 2.9% |
| GAME_SPREAD | 6,608 | 19.9 | 13.1 | 27.9 | 20.9 | 13.0 | 4.2 | 0.9 | 7.96 | 18.1% | 5.1% |
| TOTAL_GAMES | 11,466 | 8.8 | 9.8 | 36.4 | 26.6 | 12.0 | 4.0 | 2.5 | 9.42 | 18.5% | 6.5% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 31,357 | 44.5% | 24.8% | 13.14 | 36.1% | 15.5% | 10.94 |
| gen1_elo | 31,357 | 44.5% | 24.6% | 13.0 | 35.9% | 15.6% | 10.73 |
| gen1_sr | 31,357 | 52.3% | 31.6% | 15.98 | 44.5% | 22.2% | 13.06 |
| gen2 | 31,357 | 51.3% | 31.9% | 15.58 | 44.5% | 23.9% | 13.04 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,914 | 15.6 | 10.4 | 21.4 | 17.3 | 20.2 | 11.9 | 3.3 | 10.72 | 35.4% | 15.2% |
| STALE | 15,443 | 10.0 | 6.7 | 15.5 | 13.8 | 19.3 | 18.1 | 16.6 | 16.93 | 54.0% | 34.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 16,245 | 16.3 | 11.2 | 22.4 | 15.3 | 17.8 | 12.0 | 4.9 | 10.01 | 34.8% | 16.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 54,134 | 16245 | 19386 | 18503 | 24.1 | 140.2 | 1400.4 |
| ge_15pp | 22,411 | 5649 | 6914 | 9848 | 26.3 | 439.8 | 1380.4 |
| ge_25pp | 11,984 | 2752 | 3003 | 6229 | 32.0 | 582.1 | 1380.4 |
| lt_10pp | 23,387 | 8112 | 9167 | 6108 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261025T174854Z-f7897d96`: 697 priced rows, quote age at build {'median': 9.4, 'max': 9.4}, freshness {'FRESH': 697}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 28 | 0.0 | 0.0 | 21.4 | 10.7 | 39.3 | 28.6 | 0.0 | 20.48 | 67.9% | 28.6% |
| EXTERNAL_LONE_OUTLIER | 17 | 76.5 | 23.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,047 | 19.1 | 11.4 | 25.0 | 18.8 | 18.1 | 7.1 | 0.6 | 8.82 | 25.8% | 7.8% |
| KALSHI_LONE_OUTLIER | 20 | 5.0 | 5.0 | 75.0 | 5.0 | 5.0 | 5.0 | 0.0 | 5.8 | 10.0% | 5.0% |
| MARKETS_AGREE | 616 | 65.3 | 34.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,330 | 0.0 | 2.5 | 35.3 | 26.5 | 24.7 | 10.3 | 0.7 | 12.14 | 35.7% | 11.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 31,357 | 5058 (16.1%) | 26.3% | 0.9% | {"EXTERNAL_STALE": 3047, "AGREES_WITH_KALSHI": 1330, "ALL_AGREE": 616, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 20, "EXTERNAL_OUTLIER": 17, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,963 | 1282 (9.2%) | 37.0% | 1.6% | {"EXTERNAL_STALE": 786, "AGREES_WITH_KALSHI": 475, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,770 | 391 (5.0%) | 37.3% | 2.3% | {"EXTERNAL_STALE": 236, "AGREES_WITH_KALSHI": 146, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,781 | 368 (9.7%) | 37.8% | 2.5% | {"EXTERNAL_STALE": 220, "AGREES_WITH_KALSHI": 139, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,506 | 2847 (22.8%) | 17.6% | 0.8% | {"EXTERNAL_STALE": 1689, "ALL_AGREE": 616, "AGREES_WITH_KALSHI": 502, "EXTERNAL_OUTLIER": 17, "AGREES_WITH_MODEL": 17, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,966 | 10.2 | 7.6 | 19.5 | 14.6 | 22.3 | 15.9 | 9.9 | 14.09 | 48.2% | 25.9% |
| 4-10x | 4,050 | 11.1 | 8.3 | 18.8 | 15.5 | 21.6 | 14.7 | 10.0 | 13.75 | 46.3% | 24.7% |
| <2x | 16,003 | 15.0 | 9.8 | 19.1 | 16.5 | 17.6 | 13.1 | 9.0 | 11.81 | 39.6% | 22.1% |
| >=10x | 5,338 | 10.8 | 6.1 | 15.1 | 14.2 | 22.1 | 19.7 | 12.0 | 16.48 | 53.8% | 31.7% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,046 | 12.5 | 8.6 | 19.2 | 16.1 | 19.1 | 13.8 | 10.6 | 12.96 | 43.6% | 24.5% |
| 300-1000 | 6,588 | 11.6 | 8.6 | 17.4 | 15.3 | 20.7 | 16.2 | 10.1 | 13.91 | 47.1% | 26.4% |
| <300 | 10,197 | 8.5 | 5.6 | 15.4 | 14.8 | 23.3 | 20.1 | 12.3 | 17.03 | 55.7% | 32.5% |
| >=3000 | 6,526 | 21.3 | 13.1 | 23.5 | 16.5 | 14.1 | 6.9 | 4.6 | 7.89 | 25.7% | 11.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 888 | 0.5512 | 0.4129 | 0.5023 | +0.049 | -0.089 | -0.0042 ± 0.0052 |
| ratio 4-10x | 601 | 0.5899 | 0.4436 | 0.4992 | +0.091 | -0.056 | 0.0103 ± 0.0065 |
| ratio <2x | 2207 | 0.5391 | 0.4161 | 0.449 | +0.090 | -0.033 | 0.0116 ± 0.0031 |
| ratio >=10x | 815 | 0.5711 | 0.3951 | 0.4601 | +0.111 | -0.065 | 0.0079 ± 0.0064 |
| thinner_sample 1000-3000 | 1227 | 0.5429 | 0.4162 | 0.4507 | +0.092 | -0.035 | 0.0091 ± 0.0041 |
| thinner_sample 300-1000 | 1012 | 0.5676 | 0.4234 | 0.4931 | +0.074 | -0.070 | 0.0003 ± 0.0051 |
| thinner_sample <300 | 1515 | 0.5624 | 0.3955 | 0.4634 | +0.099 | -0.068 | 0.0094 ± 0.0046 |
| thinner_sample >=3000 | 757 | 0.5374 | 0.4431 | 0.4729 | +0.065 | -0.030 | 0.0116 ± 0.0042 |
| data_status ADEQUATE | 1313 | 0.5386 | 0.4345 | 0.4547 | +0.084 | -0.020 | 0.0112 ± 0.0034 |
| data_status LIMITED | 1032 | 0.5528 | 0.4187 | 0.4864 | +0.066 | -0.068 | 0.0032 ± 0.0047 |
| data_status POOR | 2166 | 0.564 | 0.4022 | 0.4677 | +0.096 | -0.066 | 0.0076 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 658 | 0.2023 | 0.2032 | -0.0008 ± 0.0006 | 0.5856 | 0.5875 | 0.5025 | 0.4876 | 0.5213 | -0.073 ± 0.0185 | -0.01 (5) |
| 3-5 | 416 | 0.2059 | 0.205 | +0.0009 ± 0.0018 | 0.5954 | 0.5919 | 0.5037 | 0.4636 | 0.4712 | -0.107 ± 0.0229 | 0.02 (1) |
| 5-10 | 930 | 0.2024 | 0.2023 | +0.0001 ± 0.0022 | 0.5913 | 0.588 | 0.5134 | 0.4393 | 0.471 | -0.090 ± 0.0153 | -0.0167 (6) |
| 10-15 | 784 | 0.2148 | 0.2056 | +0.0092 ± 0.0041 | 0.6201 | 0.5932 | 0.5307 | 0.4066 | 0.4311 | -0.102 ± 0.0162 | -0.048 (5) |
| 15-25 | 1024 | 0.2261 | 0.2144 | +0.0118 ± 0.0057 | 0.648 | 0.6129 | 0.5788 | 0.383 | 0.4512 | -0.094 ± 0.0145 | -0.0033 (9) |
| 25-40 | 583 | 0.2219 | 0.2101 | +0.0119 ± 0.0113 | 0.6334 | 0.6033 | 0.6603 | 0.3504 | 0.4837 | -0.072 ± 0.0173 | -0.01 (1) |
| 40+ | 116 | 0.2743 | 0.202 | +0.0723 ± 0.036 | 0.7526 | 0.5904 | 0.7587 | 0.3114 | 0.4569 | -0.070 ± 0.0354 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3394 | 0.1853 | 0.1862 | -0.0009 ± 0.0003 | 0.5463 | 0.5473 | 0.4915 | 0.4765 | 0.5088 | -0.023 ± 0.0075 | -0.0129 (17) |
| 3-5 | 2241 | 0.1993 | 0.198 | +0.0013 ± 0.0008 | 0.5793 | 0.5738 | 0.4849 | 0.4449 | 0.4485 | -0.053 ± 0.0096 | 0.0 (2) |
| 5-10 | 4865 | 0.1986 | 0.1955 | +0.0031 ± 0.0009 | 0.5818 | 0.5705 | 0.4836 | 0.4097 | 0.4249 | -0.046 ± 0.0064 | -0.0119 (21) |
| 10-15 | 4148 | 0.198 | 0.1804 | +0.0176 ± 0.0017 | 0.5814 | 0.532 | 0.488 | 0.3636 | 0.3551 | -0.071 ± 0.0066 | -0.0281 (16) |
| 15-25 | 5205 | 0.2093 | 0.1699 | +0.0394 ± 0.0022 | 0.6124 | 0.5021 | 0.5055 | 0.3092 | 0.3082 | -0.075 ± 0.0057 | -0.0025 (44) |
| 25-40 | 4071 | 0.2231 | 0.1292 | +0.0939 ± 0.0035 | 0.6406 | 0.3953 | 0.533 | 0.2196 | 0.2302 | -0.060 ± 0.0055 | -0.01 (1) |
| 40+ | 2640 | 0.3797 | 0.0454 | +0.3343 ± 0.0047 | 0.989 | 0.1744 | 0.6326 | 0.1066 | 0.0644 | -0.078 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 518 | 0.2084 | 0.2091 | -0.0007 ± 0.0007 | 0.5991 | 0.6008 | 0.5056 | 0.4904 | 0.5174 | -0.102 ± 0.0217 | -0.01 (3) |
| 3-5 | 369 | 0.2254 | 0.2226 | +0.0028 ± 0.002 | 0.6372 | 0.6314 | 0.5152 | 0.4753 | 0.4553 | -0.131 ± 0.0262 | 0.02 (1) |
| 5-10 | 813 | 0.2073 | 0.207 | +0.0003 ± 0.0024 | 0.601 | 0.5996 | 0.5477 | 0.4727 | 0.5117 | -0.081 ± 0.0164 | -0.01 (4) |
| 10-15 | 753 | 0.2166 | 0.2103 | +0.0064 ± 0.0042 | 0.6225 | 0.6063 | 0.5653 | 0.4411 | 0.4794 | -0.107 ± 0.0175 | -0.04 (5) |
| 15-25 | 1047 | 0.2294 | 0.2108 | +0.0186 ± 0.0056 | 0.6516 | 0.6039 | 0.5871 | 0.3914 | 0.446 | -0.099 ± 0.0145 | -0.0133 (9) |
| 25-40 | 733 | 0.266 | 0.1998 | +0.0662 ± 0.0104 | 0.7439 | 0.581 | 0.6546 | 0.3392 | 0.3943 | -0.117 ± 0.0163 | -0.0075 (4) |
| 40+ | 278 | 0.3543 | 0.1733 | +0.1810 ± 0.0246 | 0.974 | 0.5172 | 0.7342 | 0.25 | 0.3201 | -0.067 ± 0.0239 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2885 | 0.1946 | 0.1949 | -0.0003 ± 0.0003 | 0.5658 | 0.5663 | 0.5111 | 0.4962 | 0.512 | -0.043 ± 0.0085 | -0.0133 (15) |
| 3-5 | 1926 | 0.1996 | 0.1986 | +0.0010 ± 0.0008 | 0.5771 | 0.5743 | 0.5136 | 0.4737 | 0.4808 | -0.047 ± 0.0104 | 0.02 (1) |
| 5-10 | 4303 | 0.1974 | 0.1953 | +0.0021 ± 0.001 | 0.581 | 0.5705 | 0.5117 | 0.4377 | 0.4636 | -0.035 ± 0.0068 | -0.0117 (6) |
| 10-15 | 3762 | 0.2013 | 0.1897 | +0.0116 ± 0.0018 | 0.5908 | 0.5529 | 0.5149 | 0.391 | 0.4067 | -0.054 ± 0.0072 | -0.0189 (18) |
| 15-25 | 5168 | 0.2159 | 0.1789 | +0.0370 ± 0.0023 | 0.627 | 0.5255 | 0.5247 | 0.3287 | 0.3363 | -0.066 ± 0.0059 | -0.0086 (42) |
| 25-40 | 4755 | 0.2535 | 0.1368 | +0.1166 ± 0.0034 | 0.7127 | 0.4202 | 0.5584 | 0.2412 | 0.2185 | -0.089 ± 0.0053 | -0.0044 (18) |
| 40+ | 3765 | 0.3926 | 0.0605 | +0.3321 ± 0.0046 | 1.0331 | 0.2162 | 0.6502 | 0.119 | 0.085 | -0.071 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 630 | 0.2 | 0.2021 | -0.0022 ± 0.0006 | 0.5808 | 0.5861 | 0.5011 | 0.4859 | 0.5476 | -0.033 ± 0.0186 | -0.0137 (8) |
| 3-5 | 450 | 0.2035 | 0.2018 | +0.0017 ± 0.0017 | 0.5904 | 0.585 | 0.505 | 0.4652 | 0.4667 | -0.118 ± 0.0222 | 0.0067 (3) |
| 5-10 | 954 | 0.2027 | 0.1991 | +0.0036 ± 0.0022 | 0.5917 | 0.5798 | 0.5091 | 0.4351 | 0.4465 | -0.104 ± 0.0148 | -0.0071 (7) |
| 10-15 | 778 | 0.2091 | 0.2059 | +0.0032 ± 0.004 | 0.6074 | 0.5943 | 0.5408 | 0.4172 | 0.4679 | -0.083 ± 0.0162 | -0.0317 (6) |
| 15-25 | 969 | 0.2315 | 0.2142 | +0.0173 ± 0.0058 | 0.661 | 0.6121 | 0.59 | 0.3955 | 0.4479 | -0.108 ± 0.0149 | -0.03 (1) |
| 25-40 | 607 | 0.2141 | 0.2181 | -0.0041 ± 0.0111 | 0.6177 | 0.6219 | 0.6707 | 0.3597 | 0.5189 | -0.055 ± 0.017 | 0.015 (2) |
| 40+ | 123 | 0.2879 | 0.2151 | +0.0728 ± 0.0362 | 0.7962 | 0.6188 | 0.7691 | 0.3198 | 0.4715 | -0.063 ± 0.0383 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3318 | 0.1864 | 0.187 | -0.0007 ± 0.0003 | 0.5479 | 0.549 | 0.4895 | 0.4744 | 0.4925 | -0.035 ± 0.0076 | -0.0163 (35) |
| 3-5 | 2251 | 0.1958 | 0.1938 | +0.0020 ± 0.0007 | 0.5746 | 0.5681 | 0.4873 | 0.4477 | 0.4434 | -0.064 ± 0.0095 | -0.0094 (18) |
| 5-10 | 4948 | 0.1958 | 0.19 | +0.0057 ± 0.0009 | 0.5752 | 0.5564 | 0.4839 | 0.4099 | 0.4089 | -0.060 ± 0.0062 | -0.01 (31) |
| 10-15 | 4021 | 0.1919 | 0.1766 | +0.0153 ± 0.0016 | 0.5673 | 0.522 | 0.5001 | 0.3767 | 0.376 | -0.065 ± 0.0066 | -0.015 (12) |
| 15-25 | 5367 | 0.2115 | 0.1725 | +0.0391 ± 0.0022 | 0.6176 | 0.5083 | 0.5154 | 0.3203 | 0.3182 | -0.074 ± 0.0057 | -0.03 (2) |
| 25-40 | 4083 | 0.2197 | 0.1327 | +0.0870 ± 0.0036 | 0.6337 | 0.4027 | 0.5378 | 0.2218 | 0.2439 | -0.051 ± 0.0055 | 0.01 (3) |
| 40+ | 2576 | 0.394 | 0.051 | +0.3430 ± 0.005 | 1.0295 | 0.1889 | 0.6453 | 0.114 | 0.071 | -0.079 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1018 | 0.1958 | 0.196 | -0.0002 ± 0.0005 | 0.5711 | 0.5712 | 0.5021 | 0.487 | 0.4941 | -0.059 ± 0.0141 | -0.0224 (49) |
| 3-5 | 706 | 0.1924 | 0.1917 | +0.0008 ± 0.0013 | 0.5624 | 0.5593 | 0.491 | 0.4512 | 0.4589 | -0.062 ± 0.0168 | -0.0194 (34) |
| 5-10 | 1484 | 0.2024 | 0.1967 | +0.0057 ± 0.0017 | 0.5941 | 0.576 | 0.4962 | 0.4228 | 0.4218 | -0.073 ± 0.0117 | -0.005 (78) |
| 10-15 | 987 | 0.2109 | 0.1989 | +0.0120 ± 0.0035 | 0.6112 | 0.58 | 0.5238 | 0.4007 | 0.4113 | -0.072 ± 0.0145 | 0.0014 (64) |
| 15-25 | 1325 | 0.2318 | 0.2112 | +0.0207 ± 0.005 | 0.6618 | 0.6073 | 0.5794 | 0.3846 | 0.4302 | -0.074 ± 0.0127 | -0.0214 (59) |
| 25-40 | 804 | 0.2475 | 0.2088 | +0.0387 ± 0.0099 | 0.7047 | 0.5993 | 0.6763 | 0.3639 | 0.4577 | -0.087 ± 0.0151 | -0.0219 (26) |
| 40+ | 265 | 0.3492 | 0.2026 | +0.1467 ± 0.0271 | 1.0094 | 0.5926 | 0.8086 | 0.3269 | 0.434 | -0.090 ± 0.0251 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3364 | 0.1828 | 0.183 | -0.0002 ± 0.0003 | 0.5385 | 0.5381 | 0.5034 | 0.488 | 0.4979 | -0.039 ± 0.0074 | -0.0157 (88) |
| 3-5 | 2331 | 0.1956 | 0.1938 | +0.0017 ± 0.0007 | 0.5701 | 0.5661 | 0.4981 | 0.4583 | 0.4565 | -0.053 ± 0.0092 | -0.0209 (69) |
| 5-10 | 4648 | 0.197 | 0.189 | +0.0080 ± 0.001 | 0.5801 | 0.5558 | 0.4917 | 0.4182 | 0.4032 | -0.070 ± 0.0064 | -0.0082 (132) |
| 10-15 | 3272 | 0.208 | 0.1918 | +0.0162 ± 0.0019 | 0.6051 | 0.5623 | 0.5295 | 0.4064 | 0.4013 | -0.067 ± 0.0077 | -0.0053 (105) |
| 15-25 | 4058 | 0.2308 | 0.2002 | +0.0306 ± 0.0028 | 0.6653 | 0.5798 | 0.5708 | 0.3752 | 0.3963 | -0.067 ± 0.007 | -0.0253 (107) |
| 25-40 | 2776 | 0.2594 | 0.1859 | +0.0735 ± 0.0052 | 0.7356 | 0.5414 | 0.6343 | 0.3207 | 0.3628 | -0.078 ± 0.008 | -0.0229 (51) |
| 40+ | 1219 | 0.3773 | 0.1456 | +0.2317 ± 0.0115 | 1.0685 | 0.439 | 0.731 | 0.2272 | 0.2625 | -0.070 ± 0.0103 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4511 | 1.03 ± 0.042 | 1.109 | 0.1686 | 0.1632 | 0.2146 | 0.207 |
| gen2 | 4511 | 0.826 ± 0.039 | 1.078 | 0.168 | 0.1639 | 0.2342 | 0.2067 |
| gen1_elo | 4511 | 1.003 ± 0.04 | 1.106 | 0.1754 | 0.1633 | 0.2135 | 0.2072 |
| gen1_sr | 4511 | 1.011 ± 0.05 | 1.145 | 0.1293 | 0.1658 | 0.2304 | 0.2062 |
| gen1_ledger | 6589 | 0.857 ± 0.029 | 1.063 | 0.1837 | 0.1773 | 0.2189 | 0.201 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 22,411)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,112 | 22.8% |
| STALE_QUOTE | market_freshness | 4,830 | 21.6% |
| BOOK_QUALITY | execution | 4,272 | 19.1% |
| POOR_DATA | data | 2,508 | 11.2% |
| LIMITED_DATA | data | 1,395 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,215 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,071 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 950 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 661 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 396 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.8%, market_freshness 21.6%, execution 19.1%, data 17.4%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 93.9%, LOW_DATA_QUALITY 70.6%, THIN_PLAYER_HISTORY 59.4%, STALE_PLAYER_DATA 49.5%, STALE_KALSHI_QUOTE 43.9%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.8%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.9%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.4%, POST_SETTLEMENT_OBSERVATION 22.8%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,984)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,109 | 34.3% |
| BOOK_QUALITY | execution | 2,239 | 18.7% |
| STALE_QUOTE | market_freshness | 2,231 | 18.6% |
| POOR_DATA | data | 1,023 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 649 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 533 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 421 | 3.5% |
| LIMITED_DATA | data | 418 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 268 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 92 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.3%, execution 18.7%, market_freshness 18.6%, data 12.0%, market_freshness/coverage 8.9%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.1%, THIN_PLAYER_HISTORY 61.5%, STALE_KALSHI_QUOTE 52.0%, STALE_PLAYER_DATA 43.9%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 24.5%, PLAYER_IDENTITY_RISK 20.1%, MODEL_HIGH_UNCERTAINTY 18.3%, EVENT_MAPPING_RISK 10.0%, LEVEL_TRANSFER_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.4%, POST_SETTLEMENT_OBSERVATION 34.3%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9277, "IDENTITY_AMBIGUOUS": 2707}; ticker orientation: {"VERIFIED": 11984}.

Checks: discipline:AMBIGUOUS 849, discipline:PASS 11135, identity_confidence:AMBIGUOUS 2403, identity_confidence:PASS 9581, level_mapping:NA 861, level_mapping:PASS 11123, market_pair:AMBIGUOUS 458, market_pair:NA 298, market_pair:PASS 11228, model_complement:NA 265, model_complement:PASS 11719, namesake:AMBIGUOUS 6, namesake:PASS 11978, physical_match_id:NA 4214, physical_match_id:PASS 7770, player_ids:PASS 11984, same_pair_other_event:PASS 11984, ticker_orientation:PASS 11984

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,627 | 4.5% | 4.0% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 47, "data": 35, "execution": 24, "model_calibration": 20, "market_freshness/coverage": 15, "coverage": 13} | 5.92 | 0.2235 / 0.2204 (535) | 19.0% | 3.4% | 3.3% | 2.8% |
| CHALLENGER | 8,394 | 17.0% | 7.0% | 11.9% | {"coverage": 798, "market_freshness/coverage": 172, "market_freshness": 161, "data": 146, "model_calibration_or_unknown": 72, "execution": 33, "model_calibration": 30, "mapping": 17, "possible_market_error": 1} | 7.64 | 0.2188 / 0.2089 (1962) | 34.2% | 17.7% | 4.1% | 22.2% |
| DOUBLES | 1,783 | 47.6% | 47.3% | 7.1% | {"execution": 470, "mapping": 211, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.87 | 0.3106 / 0.2361 (437) | 13.1% | 0.0% | 100.0% | 6.7% |
| ITF_MEN | 14,829 | 25.5% | 17.7% | 31.6% | {"coverage": 1417, "execution": 716, "market_freshness": 644, "data": 498, "market_freshness/coverage": 331, "mapping": 175, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.94 | 0.2163 / 0.1985 (3327) | 37.4% | 69.9% | 19.8% | 22.4% |
| ITF_WOMEN | 19,607 | 27.2% | 19.9% | 44.5% | {"coverage": 1849, "market_freshness": 1166, "execution": 945, "data": 722, "market_freshness/coverage": 448, "mapping": 124, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.92 | 0.2038 / 0.1958 (3780) | 39.7% | 56.3% | 10.0% | 22.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,234 | 5.4% | 4.9% | 1.5% | {"market_freshness": 60, "model_calibration_or_unknown": 37, "execution": 26, "model_calibration": 16, "data": 13, "coverage": 12, "market_freshness/coverage": 10, "mapping": 1} | 7.65 | 0.2327 / 0.2282 (521) | 24.4% | 1.3% | 1.6% | 3.4% |
| WTA125 | 1,505 | 12.8% | 10.4% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 39, "market_freshness/coverage": 38, "data": 27, "execution": 20, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.69 | 0.2196 / 0.2052 (496) | 22.7% | 11.3% | 7.1% | 9.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.968, "by_level_share_of_ge_25pp": {"ATP": 0.0173, "CHALLENGER": 0.1193, "DOUBLES": 0.0708, "ITF_MEN": 0.3158, "ITF_WOMEN": 0.4451, "OTHER": 0.001, "WTA": 0.0146, "WTA125": 0.016}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5198, "share_primary_cause_market_settled_or_in_play": 0.4322, "share_primary_cause_stale_quote_only": 0.1862}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11984, "identity_ambiguous_share": 0.2259, "ticker_orientation": {"VERIFIED": 11984}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7770, "with_external": 391, "coverage": 0.0503, "external_status": {"EXTERNAL_STALE": 236, "AGREES_WITH_KALSHI": 146, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 236, "MODEL_LONE_OUTLIER": 146, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3734, "share_external_supports_model": 0.023}, "pregame_clean_ge_25pp": {"n": 3781, "with_external": 368, "coverage": 0.0973, "external_status": {"EXTERNAL_STALE": 220, "AGREES_WITH_KALSHI": 139, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 220, "MODEL_LONE_OUTLIER": 139, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3777, "share_external_supports_model": 0.0245}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.41, "median_min_matches": 21.0, "median_max_days_since_last": 227.0, "share_severe_asymmetry": 0.2141, "data_status": {"POOR": 6629, "LIMITED": 3155, "ADEQUATE": 2200}, "comparison_lt_10pp": {"median_thinner_serve_points": 1761.0, "median_sample_ratio": 1.68, "median_min_matches": 98.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 888, "model_minus_observed": 0.049, "kalshi_minus_observed": -0.0893, "brier_diff_model_minus_kalshi": -0.0042}, "4-10x": {"n": 601, "model_minus_observed": 0.0908, "kalshi_minus_observed": -0.0555, "brier_diff_model_minus_kalshi": 0.0103}, "<2x": {"n": 2207, "model_minus_observed": 0.0901, "kalshi_minus_observed": -0.0329, "brier_diff_model_minus_kalshi": 0.0116}, ">=10x": {"n": 815, "model_minus_observed": 0.1109, "kalshi_minus_observed": -0.065, "brier_diff_model_minus_kalshi": 0.0079}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4511, "model": {"intercept": -0.529, "slope": 0.826, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.211, "slope": 1.078, "slope_se": 0.043}, "mean_extremity_model": 0.168, "mean_extremity_kalshi": 0.1639, "model_brier": 0.2342, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.0275, "brier_diff_se": 0.0028, "model_logloss": 0.6653, "kalshi_logloss": 0.5963}, "fair_v1": {"n": 4511, "model": {"intercept": -0.418, "slope": 1.03, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.284, "slope": 1.109, "slope_se": 0.043}, "mean_extremity_model": 0.1686, "mean_extremity_kalshi": 0.1632, "model_brier": 0.2146, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0076, "brier_diff_se": 0.0023, "model_logloss": 0.6183, "kalshi_logloss": 0.5969}, "gen1_elo": {"n": 4511, "model": {"intercept": -0.392, "slope": 1.003, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.307, "slope": 1.106, "slope_se": 0.043}, "mean_extremity_model": 0.1754, "mean_extremity_kalshi": 0.1633, "model_brier": 0.2135, "kalshi_brier": 0.2072, "brier_diff_model_minus_kalshi": 0.0063, "brier_diff_se": 0.0023, "model_logloss": 0.6167, "kalshi_logloss": 0.5974}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2478, "share_ge_15": 0.4453, "median_abs_gap": 13.14, "n": 31357}, "gen1_elo": {"share_ge_25": 0.2457, "share_ge_15": 0.4445, "median_abs_gap": 13.0, "n": 31357}, "gen1_sr": {"share_ge_25": 0.3158, "share_ge_15": 0.5235, "median_abs_gap": 15.98, "n": 31357}, "gen2": {"share_ge_25": 0.3194, "share_ge_15": 0.5135, "median_abs_gap": 15.58, "n": 31357}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1552, "share_ge_15": 0.3611, "median_abs_gap": 10.94, "n": 24352}, "gen1_elo": {"share_ge_25": 0.1564, "share_ge_15": 0.359, "median_abs_gap": 10.73, "n": 24349}, "gen1_sr": {"share_ge_25": 0.2224, "share_ge_15": 0.4453, "median_abs_gap": 13.06, "n": 24353}, "gen2": {"share_ge_25": 0.2387, "share_ge_15": 0.445, "median_abs_gap": 13.04, "n": 24354}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.92, "share_ge_25_all": 0.0447, "share_ge_25_pregame_clean": 0.0398}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0541, "share_ge_25_pregame_clean": 0.049}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2339, "share_within_10pp_all": 0.432, "share_within_10pp_pregame_clean": 0.4844, "corr_model_vs_mid_pregame_clean": 0.8428}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 658, "model_brier": 0.2023, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": -0.0008}, "10-15": {"n_settled": 784, "model_brier": 0.2148, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0092}, "15-25": {"n_settled": 1024, "model_brier": 0.2261, "kalshi_brier": 0.2144, "brier_diff_model_minus_kalshi": 0.0118}, "25-40": {"n_settled": 583, "model_brier": 0.2219, "kalshi_brier": 0.2101, "brier_diff_model_minus_kalshi": 0.0119}, "3-5": {"n_settled": 416, "model_brier": 0.2059, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0009}, "40+": {"n_settled": 116, "model_brier": 0.2743, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0723}, "5-10": {"n_settled": 930, "model_brier": 0.2024, "kalshi_brier": 0.2023, "brier_diff_model_minus_kalshi": 0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.529, "slope": 0.826, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.211, "slope": 1.078, "slope_se": 0.043}, "n": 4511}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.5, "slope": 0.857, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.156, "slope": 1.063, "slope_se": 0.034}, "n": 6589}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 437, "model_brier": 0.3106, "kalshi_brier": 0.2361, "brier_diff_model_minus_kalshi": 0.0746, "brier_diff_se": 0.0144, "corr_model_outcome": 0.0381, "corr_kalshi_outcome": 0.2506}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
