# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-24T12:03Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 51,572): 0-3 13.9%, 3-5 9.5%, 5-10 19.7%, 10-15 15.3%, 15-25 19.2%, 25-40 14.1%, 40+ 8.3%; median gap 12.13 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 11.9%, doubles 6.6%). Main tour: ATP 4.6% and WTA 5.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,539): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.8%, STALE_QUOTE 18.8%, BOOK_QUALITY 17.9%, POOR_DATA 8.7%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.5%, IN_PLAY_QUOTE 3.6%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.8%, market_freshness 18.8%, execution 17.9%, data 12.2%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,539 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.0% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 492.0 points vs 1682.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.036, Gen-2 0.839, Gen-1 ledger 0.862 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 564 model 0.2227 vs Kalshi 0.2091; n 113 model 0.2806 vs Kalshi 0.1974.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 223,347 model-market comparisons (363,563 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 74,146 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-24T11:50:32.683364+00:00'], shadow board 59,752 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-24T11:50:37.641573+00:00'], Model 4 27,943 rows, 19,836 settled tickers, 7,020 tickers with an external scan.
* By model: {"gen1_ledger": 50432, "gen1_elo": 30049, "fair_v1": 30049, "gen2": 30049, "gen1_sr": 30049, "model4_fundamental": 26374, "model4_conditioned": 26345}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 51,572 | 13.9 | 9.5 | 19.7 | 15.3 | 19.2 | 14.1 | 8.3 | 12.13 | 41.6% | 22.4% |
| MW fair_v1 | 30,049 | 12.8 | 8.5 | 18.5 | 15.5 | 19.7 | 15.0 | 10.0 | 13.21 | 44.7% | 25.1% |
| MW gen1_elo | 30,049 | 12.7 | 8.5 | 18.9 | 15.2 | 19.9 | 15.0 | 9.7 | 13.02 | 44.6% | 24.8% |
| MW gen1_ledger | 21,523 | 15.5 | 10.8 | 21.4 | 15.0 | 18.6 | 12.8 | 5.8 | 10.55 | 37.2% | 18.6% |
| MW gen1_sr | 30,049 | 10.2 | 7.0 | 16.5 | 13.6 | 20.8 | 18.8 | 13.1 | 16.08 | 52.7% | 31.9% |
| MW gen2 | 30,049 | 10.9 | 7.3 | 16.2 | 14.0 | 19.4 | 18.0 | 14.2 | 15.67 | 51.6% | 32.2% |
| all families model4_conditioned | 26,345 | 21.9 | 19.0 | 34.8 | 17.5 | 4.3 | 1.5 | 1.0 | 5.96 | 6.8% | 2.5% |
| all families model4_fundamental | 26,374 | 16.8 | 13.3 | 34.2 | 20.5 | 10.6 | 3.4 | 1.3 | 7.75 | 15.2% | 4.7% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.9%, >=15pp 41.6%, >=20pp 31.0%, >=25pp 22.4%, >=30pp 16.2%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.52pp; >=10pp 45.6%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,602 | 28.3 | 14.3 | 24.8 | 15.3 | 11.9 | 4.7 | 0.7 | 6.13 | 17.3% | 5.4% |
| CHALLENGER | 4,645 | 15.8 | 10.0 | 20.5 | 15.4 | 14.7 | 12.4 | 11.2 | 11.06 | 38.3% | 23.6% |
| ITF_MEN | 8,326 | 10.1 | 7.3 | 16.9 | 14.6 | 21.5 | 17.4 | 12.2 | 15.41 | 51.1% | 29.6% |
| ITF_WOMEN | 11,946 | 9.4 | 6.9 | 15.9 | 15.3 | 22.3 | 18.2 | 12.0 | 15.79 | 52.5% | 30.2% |
| OTHER | 2 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,868 | 17.2 | 13.1 | 26.1 | 19.3 | 17.8 | 5.8 | 0.7 | 8.25 | 24.3% | 6.5% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,602 | 24.1 | 15.1 | 24.7 | 17.4 | 13.1 | 4.6 | 1.0 | 6.54 | 18.6% | 5.6% |
| CHALLENGER | 4,645 | 15.1 | 8.8 | 18.5 | 14.5 | 17.3 | 13.9 | 12.0 | 12.48 | 43.2% | 25.9% |
| ITF_MEN | 8,326 | 8.2 | 5.9 | 14.4 | 12.9 | 19.7 | 21.1 | 17.8 | 18.76 | 58.6% | 38.9% |
| ITF_WOMEN | 11,946 | 8.1 | 5.6 | 13.7 | 13.3 | 20.6 | 21.0 | 17.7 | 19.1 | 59.2% | 38.7% |
| OTHER | 2 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 43.05 | 100.0% | 50.0% |
| WTA | 1,868 | 13.8 | 10.3 | 22.2 | 16.3 | 22.8 | 13.3 | 1.3 | 10.97 | 37.4% | 14.6% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,602 | 23.9 | 12.8 | 23.6 | 16.5 | 15.1 | 7.0 | 1.1 | 7.49 | 23.2% | 8.2% |
| CHALLENGER | 4,645 | 14.4 | 9.2 | 20.4 | 15.5 | 16.1 | 13.1 | 11.3 | 11.48 | 40.5% | 24.3% |
| ITF_MEN | 8,326 | 9.7 | 7.3 | 16.9 | 13.8 | 22.1 | 17.7 | 12.3 | 15.77 | 52.2% | 30.0% |
| ITF_WOMEN | 11,946 | 9.4 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.2 | 15.6 | 51.9% | 29.2% |
| OTHER | 2 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.55 | 50.0% | 0.0% |
| WTA | 1,868 | 23.9 | 17.1 | 30.5 | 15.3 | 10.2 | 2.6 | 0.5 | 6.04 | 13.3% | 3.1% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,561 | 25.6 | 19.4 | 29.9 | 12.6 | 9.2 | 3.0 | 0.3 | 5.54 | 12.5% | 3.3% |
| CHALLENGER | 3,179 | 21.6 | 14.6 | 26.3 | 14.3 | 14.5 | 6.7 | 1.9 | 7.29 | 23.1% | 8.6% |
| DOUBLES | 1,615 | 5.4 | 4.6 | 11.5 | 10.4 | 21.2 | 25.9 | 21.0 | 23.73 | 68.1% | 46.9% |
| ITF_MEN | 6,155 | 13.7 | 9.1 | 20.0 | 16.2 | 21.2 | 13.3 | 6.5 | 12.16 | 41.0% | 19.8% |
| ITF_WOMEN | 7,072 | 12.6 | 9.0 | 19.3 | 15.2 | 21.6 | 16.2 | 6.1 | 12.84 | 43.9% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,060 | 22.3 | 15.9 | 29.7 | 18.0 | 10.0 | 3.7 | 0.4 | 6.88 | 14.1% | 4.1% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,532 | 28.6 | 14.4 | 25.2 | 15.2 | 11.7 | 4.3 | 0.5 | 5.96 | 16.5% | 4.8% |
| CHALLENGER | 3,265 | 20.8 | 12.4 | 25.3 | 17.8 | 15.0 | 6.8 | 1.9 | 8.31 | 23.7% | 8.7% |
| ITF_MEN | 6,105 | 12.2 | 8.8 | 20.3 | 16.5 | 22.8 | 14.3 | 5.1 | 12.54 | 42.2% | 19.4% |
| ITF_WOMEN | 8,915 | 11.2 | 8.2 | 18.1 | 17.4 | 24.2 | 15.3 | 5.5 | 13.51 | 45.1% | 20.8% |
| OTHER | 2 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,815 | 17.5 | 12.9 | 26.0 | 19.6 | 17.8 | 5.5 | 0.7 | 8.25 | 24.0% | 6.2% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,532 | 24.3 | 15.5 | 24.8 | 17.3 | 13.1 | 4.3 | 0.6 | 6.48 | 18.0% | 4.9% |
| CHALLENGER | 3,265 | 19.1 | 11.3 | 23.1 | 17.4 | 17.5 | 9.5 | 2.1 | 9.07 | 29.1% | 11.6% |
| ITF_MEN | 6,106 | 9.8 | 7.1 | 16.8 | 14.9 | 21.6 | 19.3 | 10.5 | 15.5 | 51.5% | 29.8% |
| ITF_WOMEN | 8,916 | 9.3 | 6.5 | 15.2 | 14.8 | 22.6 | 20.5 | 11.2 | 16.62 | 54.3% | 31.7% |
| OTHER | 2 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 43.05 | 100.0% | 50.0% |
| WTA | 1,815 | 13.9 | 10.3 | 22.2 | 16.3 | 22.8 | 13.2 | 1.4 | 10.97 | 37.3% | 14.5% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,514 | 25.8 | 19.7 | 29.9 | 12.8 | 8.7 | 2.9 | 0.2 | 5.5 | 11.8% | 3.1% |
| CHALLENGER | 2,768 | 23.1 | 15.7 | 27.8 | 14.3 | 13.9 | 4.6 | 0.5 | 6.7 | 19.0% | 5.2% |
| DOUBLES | 1,498 | 5.3 | 4.7 | 11.8 | 10.6 | 21.1 | 25.9 | 20.6 | 23.62 | 67.6% | 46.5% |
| ITF_MEN | 5,157 | 14.9 | 9.7 | 21.7 | 17.0 | 21.2 | 11.6 | 4.0 | 11.17 | 36.7% | 15.6% |
| ITF_WOMEN | 5,849 | 13.6 | 9.6 | 20.7 | 16.0 | 21.8 | 14.9 | 3.4 | 11.67 | 40.1% | 18.3% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,010 | 22.8 | 16.4 | 29.7 | 18.0 | 10.0 | 3.0 | 0.1 | 6.79 | 13.1% | 3.1% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,615 | 5.4 | 4.6 | 11.5 | 10.4 | 21.2 | 25.9 | 21.0 | 23.73 | 68.1% | 46.9% |
| singles | 19,908 | 16.3 | 11.3 | 22.2 | 15.4 | 18.4 | 11.7 | 4.6 | 10.03 | 34.8% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 2 | 50.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 0.0 | 10.84 | 50.0% | 0.0% |
| Clay | 6,641 | 13.0 | 9.0 | 19.2 | 15.6 | 18.7 | 14.6 | 10.0 | 12.83 | 43.2% | 24.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 18,580 | 13.2 | 8.6 | 18.6 | 15.2 | 19.7 | 14.9 | 9.8 | 13.11 | 44.5% | 24.7% |
| UNKNOWN | 4,589 | 10.7 | 7.5 | 17.1 | 16.8 | 20.7 | 16.2 | 11.0 | 14.11 | 47.9% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,467 | 19.5 | 11.9 | 21.4 | 16.4 | 15.1 | 9.2 | 6.4 | 9.14 | 30.7% | 15.6% |
| B | 3,729 | 12.5 | 8.7 | 19.7 | 16.1 | 19.1 | 12.7 | 11.1 | 12.61 | 42.9% | 23.8% |
| C | 4,219 | 11.4 | 8.7 | 19.8 | 15.2 | 19.4 | 14.8 | 10.7 | 13.18 | 44.9% | 25.5% |
| D | 4,688 | 12.1 | 7.7 | 17.4 | 15.5 | 21.4 | 15.7 | 10.2 | 13.98 | 47.4% | 25.9% |
| F | 8,946 | 7.6 | 5.5 | 15.1 | 14.5 | 23.4 | 21.3 | 12.6 | 17.82 | 57.3% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,086 | 23.2 | 15.8 | 28.7 | 15.1 | 11.6 | 4.1 | 1.5 | 6.64 | 17.2% | 5.5% |
| B | 2,933 | 16.2 | 10.4 | 23.2 | 16.2 | 19.3 | 10.7 | 3.9 | 10.03 | 33.9% | 14.6% |
| C | 4,226 | 11.3 | 7.4 | 18.1 | 14.3 | 21.6 | 16.7 | 10.6 | 14.39 | 48.9% | 27.3% |
| D | 3,002 | 14.4 | 9.8 | 19.9 | 14.6 | 20.9 | 14.4 | 6.1 | 12.04 | 41.4% | 20.5% |
| F | 5,276 | 10.2 | 8.4 | 15.6 | 15.1 | 22.7 | 19.9 | 8.1 | 15.31 | 50.6% | 27.9% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,735 | 17.7 | 10.7 | 20.8 | 16.2 | 15.6 | 10.1 | 8.9 | 10.22 | 34.7% | 19.0% |
| LIMITED | 6,342 | 13.3 | 10.0 | 20.4 | 15.7 | 19.3 | 13.5 | 7.9 | 11.98 | 40.7% | 21.4% |
| POOR | 13,972 | 9.1 | 6.3 | 16.0 | 14.9 | 22.7 | 19.2 | 11.8 | 16.24 | 53.6% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 5,986 | 25.9 | 19.7 | 33.8 | 12.7 | 5.5 | 2.1 | 0.2 | 5.46 | 7.8% | 2.4% |
| GAME_SPREAD | 4,806 | 22.2 | 15.3 | 33.5 | 17.3 | 9.2 | 2.3 | 0.3 | 6.73 | 11.8% | 2.6% |
| MATCH_WINNER | 21,523 | 15.5 | 10.8 | 21.4 | 15.0 | 18.6 | 12.8 | 5.8 | 10.55 | 37.2% | 18.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 10,497 | 29.2 | 17.2 | 30.8 | 12.4 | 8.0 | 2.0 | 0.4 | 5.45 | 10.4% | 2.4% |
| TOTAL_GAMES | 7,596 | 9.0 | 9.8 | 36.5 | 28.5 | 10.3 | 3.2 | 2.6 | 9.39 | 16.1% | 5.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,313 | 25.3 | 33.2 | 32.6 | 4.7 | 3.2 | 0.7 | 0.2 | 4.5 | 4.1% | 0.9% |
| GAME_SPREAD | 6,292 | 45.6 | 16.7 | 26.8 | 7.9 | 1.7 | 0.9 | 0.3 | 3.47 | 2.9% | 1.2% |
| TOTAL_GAMES | 10,740 | 5.1 | 7.9 | 41.3 | 34.3 | 6.9 | 2.5 | 2.1 | 9.54 | 11.4% | 4.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,318 | 24.2 | 17.5 | 35.5 | 12.7 | 7.1 | 2.5 | 0.3 | 5.87 | 10.0% | 2.9% |
| GAME_SPREAD | 6,295 | 19.5 | 13.4 | 27.9 | 20.7 | 13.2 | 4.3 | 0.9 | 7.96 | 18.5% | 5.2% |
| TOTAL_GAMES | 10,761 | 8.7 | 9.6 | 36.8 | 27.0 | 12.0 | 3.6 | 2.3 | 9.41 | 17.9% | 5.9% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 30,049 | 44.7% | 25.1% | 13.21 | 36.3% | 15.7% | 10.97 |
| gen1_elo | 30,049 | 44.6% | 24.8% | 13.02 | 36.0% | 15.8% | 10.78 |
| gen1_sr | 30,049 | 52.7% | 31.9% | 16.08 | 44.8% | 22.4% | 13.18 |
| gen2 | 30,049 | 51.6% | 32.2% | 15.67 | 44.7% | 24.0% | 13.13 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,236 | 15.7 | 10.4 | 21.3 | 17.2 | 20.1 | 12.0 | 3.3 | 10.75 | 35.5% | 15.3% |
| STALE | 14,813 | 9.8 | 6.6 | 15.6 | 13.8 | 19.2 | 18.1 | 16.9 | 17.06 | 54.3% | 35.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 14,991 | 16.5 | 11.3 | 22.2 | 15.1 | 17.8 | 12.2 | 4.8 | 9.99 | 34.8% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 51,572 | 14991 | 18708 | 17873 | 24.2 | 148.8 | 1400.4 |
| ge_15pp | 21,461 | 5219 | 6695 | 9547 | 26.4 | 442.7 | 1380.4 |
| ge_25pp | 11,539 | 2547 | 2927 | 6065 | 32.7 | 583.2 | 1380.4 |
| lt_10pp | 22,221 | 7504 | 8843 | 5874 | 22.4 | 48.0 | 1341.5 |

Current slate `SL-20261024T120301Z-8936cc59`: 383 priced rows, quote age at build {'median': 12.9, 'max': 12.9}, freshness {'AGING': 383}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 24 | 0.0 | 0.0 | 25.0 | 4.2 | 37.5 | 33.3 | 0.0 | 20.48 | 70.8% | 33.3% |
| EXTERNAL_LONE_OUTLIER | 14 | 71.4 | 28.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.4 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,870 | 19.4 | 11.2 | 24.7 | 18.7 | 18.1 | 7.2 | 0.7 | 8.82 | 26.0% | 7.8% |
| KALSHI_LONE_OUTLIER | 17 | 5.9 | 5.9 | 76.5 | 0.0 | 5.9 | 5.9 | 0.0 | 6.11 | 11.8% | 5.9% |
| MARKETS_AGREE | 578 | 64.5 | 35.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,229 | 0.0 | 2.3 | 36.0 | 25.6 | 24.6 | 10.7 | 0.7 | 12.19 | 36.1% | 11.5% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 30,049 | 4732 (15.8%) | 26.0% | 0.9% | {"EXTERNAL_STALE": 2870, "AGREES_WITH_KALSHI": 1229, "ALL_AGREE": 578, "SUPPORTS_MODEL_DIRECTION": 23, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 14, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,443 | 1209 (9.0%) | 36.7% | 1.6% | {"EXTERNAL_STALE": 746, "AGREES_WITH_KALSHI": 444, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,530 | 375 (5.0%) | 37.6% | 2.4% | {"EXTERNAL_STALE": 225, "AGREES_WITH_KALSHI": 141, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,654 | 352 (9.6%) | 38.1% | 2.6% | {"EXTERNAL_STALE": 209, "AGREES_WITH_KALSHI": 134, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 11,948 | 2670 (22.4%) | 17.6% | 0.8% | {"EXTERNAL_STALE": 1587, "ALL_AGREE": 578, "AGREES_WITH_KALSHI": 470, "AGREES_WITH_MODEL": 15, "EXTERNAL_OUTLIER": 14, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,737 | 10.2 | 7.5 | 19.4 | 14.4 | 22.3 | 16.0 | 10.2 | 14.26 | 48.5% | 26.2% |
| 4-10x | 3,937 | 11.0 | 8.2 | 19.2 | 15.3 | 21.3 | 15.0 | 10.1 | 13.76 | 46.4% | 25.1% |
| <2x | 15,184 | 14.9 | 9.8 | 19.0 | 16.4 | 17.5 | 13.1 | 9.3 | 11.89 | 40.0% | 22.4% |
| >=10x | 5,191 | 10.9 | 6.2 | 15.3 | 14.2 | 21.9 | 19.6 | 11.9 | 16.38 | 53.4% | 31.5% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,659 | 12.4 | 8.6 | 19.5 | 16.0 | 19.0 | 13.8 | 10.8 | 12.95 | 43.6% | 24.6% |
| 300-1000 | 6,432 | 11.6 | 8.6 | 17.3 | 15.3 | 20.5 | 16.3 | 10.3 | 13.96 | 47.2% | 26.7% |
| <300 | 9,868 | 8.6 | 5.6 | 15.5 | 14.7 | 23.1 | 20.1 | 12.4 | 17.02 | 55.6% | 32.5% |
| >=3000 | 6,090 | 21.4 | 13.0 | 23.1 | 16.4 | 14.2 | 7.1 | 4.8 | 7.93 | 26.1% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 855 | 0.5489 | 0.4104 | 0.4994 | +0.050 | -0.089 | -0.0032 ± 0.0053 |
| ratio 4-10x | 588 | 0.5878 | 0.4418 | 0.4949 | +0.093 | -0.053 | 0.0119 ± 0.0066 |
| ratio <2x | 2116 | 0.5381 | 0.4147 | 0.4447 | +0.093 | -0.030 | 0.0129 ± 0.0031 |
| ratio >=10x | 787 | 0.5718 | 0.3966 | 0.4651 | +0.107 | -0.068 | 0.0066 ± 0.0065 |
| thinner_sample 1000-3000 | 1174 | 0.5418 | 0.4148 | 0.4438 | +0.098 | -0.029 | 0.0113 ± 0.0042 |
| thinner_sample 300-1000 | 993 | 0.5669 | 0.4233 | 0.4924 | +0.074 | -0.069 | 0.0009 ± 0.0051 |
| thinner_sample <300 | 1468 | 0.561 | 0.3946 | 0.4653 | +0.096 | -0.071 | 0.0089 ± 0.0046 |
| thinner_sample >=3000 | 711 | 0.5359 | 0.4412 | 0.4669 | +0.069 | -0.026 | 0.0132 ± 0.0044 |
| data_status ADEQUATE | 1246 | 0.5381 | 0.4333 | 0.4502 | +0.088 | -0.017 | 0.0128 ± 0.0035 |
| data_status LIMITED | 999 | 0.5507 | 0.4166 | 0.4795 | +0.071 | -0.063 | 0.0046 ± 0.0048 |
| data_status POOR | 2101 | 0.563 | 0.4018 | 0.4688 | +0.094 | -0.067 | 0.0077 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 632 | 0.2009 | 0.2019 | -0.0010 ± 0.0006 | 0.5825 | 0.5846 | 0.5025 | 0.4877 | 0.5269 | -0.067 ± 0.0188 | -0.01 (5) |
| 3-5 | 403 | 0.2032 | 0.2027 | +0.0005 ± 0.0018 | 0.5897 | 0.5869 | 0.5022 | 0.4621 | 0.4739 | -0.098 ± 0.0232 | 0.02 (1) |
| 5-10 | 900 | 0.2025 | 0.202 | +0.0005 ± 0.0023 | 0.5916 | 0.5872 | 0.5114 | 0.4374 | 0.4667 | -0.090 ± 0.0155 | -0.0167 (6) |
| 10-15 | 747 | 0.2145 | 0.2044 | +0.0101 ± 0.0041 | 0.6194 | 0.5904 | 0.5299 | 0.4058 | 0.4257 | -0.106 ± 0.0165 | -0.048 (5) |
| 15-25 | 987 | 0.2248 | 0.2126 | +0.0123 ± 0.0057 | 0.6443 | 0.6087 | 0.5782 | 0.3825 | 0.4488 | -0.095 ± 0.0146 | -0.0033 (9) |
| 25-40 | 564 | 0.2227 | 0.2091 | +0.0135 ± 0.0115 | 0.6335 | 0.6014 | 0.6584 | 0.3485 | 0.4787 | -0.074 ± 0.0177 | -0.01 (1) |
| 40+ | 113 | 0.2806 | 0.1974 | +0.0832 ± 0.0363 | 0.768 | 0.5798 | 0.7562 | 0.3089 | 0.4425 | -0.080 ± 0.0356 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3266 | 0.1847 | 0.1857 | -0.0010 ± 0.0003 | 0.5449 | 0.5461 | 0.4934 | 0.4783 | 0.5141 | -0.019 ± 0.0076 | -0.0129 (17) |
| 3-5 | 2162 | 0.1992 | 0.1981 | +0.0011 ± 0.0008 | 0.5795 | 0.5742 | 0.4849 | 0.445 | 0.45 | -0.051 ± 0.0097 | 0.0 (2) |
| 5-10 | 4720 | 0.1978 | 0.1945 | +0.0033 ± 0.001 | 0.5795 | 0.5683 | 0.4813 | 0.4074 | 0.4216 | -0.047 ± 0.0065 | -0.0119 (21) |
| 10-15 | 3986 | 0.1978 | 0.1798 | +0.0181 ± 0.0017 | 0.5813 | 0.5305 | 0.4866 | 0.3622 | 0.3512 | -0.074 ± 0.0067 | -0.0281 (16) |
| 15-25 | 5016 | 0.2086 | 0.1696 | +0.0391 ± 0.0023 | 0.6105 | 0.5018 | 0.506 | 0.3097 | 0.3092 | -0.074 ± 0.0058 | -0.0025 (44) |
| 25-40 | 3948 | 0.2226 | 0.1291 | +0.0935 ± 0.0036 | 0.6391 | 0.3952 | 0.5319 | 0.2187 | 0.2297 | -0.059 ± 0.0055 | -0.01 (1) |
| 40+ | 2573 | 0.3807 | 0.0456 | +0.3351 ± 0.0048 | 0.9917 | 0.1751 | 0.6333 | 0.1069 | 0.0645 | -0.078 ± 0.004 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 496 | 0.206 | 0.2067 | -0.0007 ± 0.0007 | 0.5939 | 0.5953 | 0.5075 | 0.4923 | 0.5141 | -0.105 ± 0.0219 | -0.01 (3) |
| 3-5 | 361 | 0.2242 | 0.2216 | +0.0026 ± 0.002 | 0.6348 | 0.6294 | 0.5148 | 0.4749 | 0.4571 | -0.128 ± 0.0264 | 0.02 (1) |
| 5-10 | 778 | 0.2059 | 0.2062 | -0.0003 ± 0.0025 | 0.598 | 0.5978 | 0.547 | 0.4722 | 0.5141 | -0.076 ± 0.0167 | -0.01 (4) |
| 10-15 | 716 | 0.2174 | 0.209 | +0.0084 ± 0.0043 | 0.6243 | 0.6036 | 0.5661 | 0.4419 | 0.4721 | -0.113 ± 0.0178 | -0.04 (5) |
| 15-25 | 1011 | 0.2303 | 0.2103 | +0.0200 ± 0.0057 | 0.6536 | 0.6032 | 0.5877 | 0.3919 | 0.4431 | -0.102 ± 0.0147 | -0.0133 (9) |
| 25-40 | 711 | 0.2619 | 0.1976 | +0.0643 ± 0.0105 | 0.7307 | 0.5756 | 0.653 | 0.3376 | 0.3952 | -0.113 ± 0.0163 | -0.0075 (4) |
| 40+ | 273 | 0.3585 | 0.1711 | +0.1874 ± 0.0247 | 0.985 | 0.5124 | 0.7323 | 0.2483 | 0.3114 | -0.073 ± 0.024 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2782 | 0.1934 | 0.1938 | -0.0003 ± 0.0003 | 0.5635 | 0.5642 | 0.5112 | 0.4962 | 0.5137 | -0.041 ± 0.0086 | -0.0133 (15) |
| 3-5 | 1863 | 0.1993 | 0.1983 | +0.0011 ± 0.0008 | 0.5768 | 0.5739 | 0.5143 | 0.4744 | 0.4804 | -0.048 ± 0.0106 | 0.02 (1) |
| 5-10 | 4153 | 0.1961 | 0.1942 | +0.0019 ± 0.001 | 0.5772 | 0.568 | 0.5097 | 0.4357 | 0.4626 | -0.033 ± 0.0069 | -0.0117 (6) |
| 10-15 | 3612 | 0.2015 | 0.1896 | +0.0119 ± 0.0018 | 0.5898 | 0.5523 | 0.5133 | 0.3894 | 0.4042 | -0.055 ± 0.0074 | -0.0189 (18) |
| 15-25 | 4981 | 0.2164 | 0.1782 | +0.0382 ± 0.0024 | 0.6283 | 0.5241 | 0.5251 | 0.3292 | 0.3335 | -0.070 ± 0.006 | -0.0086 (42) |
| 25-40 | 4611 | 0.2515 | 0.1373 | +0.1142 ± 0.0035 | 0.7076 | 0.4216 | 0.5581 | 0.241 | 0.2221 | -0.085 ± 0.0054 | -0.0044 (18) |
| 40+ | 3669 | 0.394 | 0.0607 | +0.3333 ± 0.0046 | 1.037 | 0.217 | 0.6508 | 0.1188 | 0.0845 | -0.072 ± 0.004 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 609 | 0.1995 | 0.2017 | -0.0021 ± 0.0006 | 0.5798 | 0.585 | 0.501 | 0.4858 | 0.5484 | -0.031 ± 0.0189 | -0.0137 (8) |
| 3-5 | 430 | 0.2021 | 0.2 | +0.0021 ± 0.0017 | 0.5872 | 0.5805 | 0.507 | 0.4673 | 0.4628 | -0.122 ± 0.0224 | 0.0067 (3) |
| 5-10 | 915 | 0.2015 | 0.198 | +0.0036 ± 0.0022 | 0.5895 | 0.5773 | 0.5072 | 0.4332 | 0.4437 | -0.103 ± 0.0151 | -0.0071 (7) |
| 10-15 | 755 | 0.2084 | 0.2052 | +0.0032 ± 0.0041 | 0.6058 | 0.5927 | 0.5394 | 0.4158 | 0.4662 | -0.083 ± 0.0164 | -0.0317 (6) |
| 15-25 | 933 | 0.2309 | 0.2122 | +0.0188 ± 0.0059 | 0.6597 | 0.6074 | 0.5887 | 0.3944 | 0.4427 | -0.111 ± 0.015 | -0.03 (1) |
| 25-40 | 585 | 0.2124 | 0.2176 | -0.0052 ± 0.0113 | 0.6124 | 0.621 | 0.6694 | 0.3582 | 0.5197 | -0.052 ± 0.0173 | 0.015 (2) |
| 40+ | 119 | 0.2963 | 0.2093 | +0.0869 ± 0.0367 | 0.8166 | 0.606 | 0.7668 | 0.3173 | 0.4538 | -0.078 ± 0.0385 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3209 | 0.1851 | 0.1857 | -0.0005 ± 0.0003 | 0.5449 | 0.5457 | 0.4904 | 0.4752 | 0.4892 | -0.038 ± 0.0077 | -0.0163 (35) |
| 3-5 | 2172 | 0.1951 | 0.1929 | +0.0022 ± 0.0008 | 0.5729 | 0.5659 | 0.4873 | 0.4477 | 0.4401 | -0.067 ± 0.0096 | -0.0094 (18) |
| 5-10 | 4759 | 0.1958 | 0.19 | +0.0057 ± 0.0009 | 0.5756 | 0.5567 | 0.4826 | 0.4086 | 0.4072 | -0.061 ± 0.0064 | -0.01 (31) |
| 10-15 | 3886 | 0.1913 | 0.176 | +0.0153 ± 0.0017 | 0.5661 | 0.5206 | 0.4986 | 0.3752 | 0.3747 | -0.065 ± 0.0067 | -0.015 (12) |
| 15-25 | 5193 | 0.2106 | 0.1719 | +0.0387 ± 0.0023 | 0.6151 | 0.5074 | 0.5148 | 0.3198 | 0.3183 | -0.073 ± 0.0057 | -0.03 (2) |
| 25-40 | 3959 | 0.2188 | 0.1331 | +0.0858 ± 0.0037 | 0.6317 | 0.4036 | 0.5376 | 0.2214 | 0.2458 | -0.048 ± 0.0056 | 0.01 (3) |
| 40+ | 2493 | 0.3954 | 0.0502 | +0.3452 ± 0.0051 | 1.0332 | 0.1872 | 0.6455 | 0.1133 | 0.069 | -0.081 ± 0.0043 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 992 | 0.1949 | 0.195 | -0.0001 ± 0.0005 | 0.5691 | 0.569 | 0.5033 | 0.4881 | 0.494 | -0.058 ± 0.0142 | -0.0224 (49) |
| 3-5 | 690 | 0.1917 | 0.1912 | +0.0005 ± 0.0013 | 0.5605 | 0.5581 | 0.4897 | 0.4498 | 0.4609 | -0.055 ± 0.017 | -0.0194 (34) |
| 5-10 | 1440 | 0.2018 | 0.1958 | +0.0060 ± 0.0018 | 0.5931 | 0.5742 | 0.4965 | 0.4232 | 0.4194 | -0.073 ± 0.0118 | -0.005 (78) |
| 10-15 | 958 | 0.2105 | 0.1985 | +0.0120 ± 0.0036 | 0.6104 | 0.5791 | 0.5218 | 0.3986 | 0.4092 | -0.071 ± 0.0147 | 0.0014 (64) |
| 15-25 | 1289 | 0.2315 | 0.2099 | +0.0216 ± 0.005 | 0.6607 | 0.6045 | 0.5777 | 0.3829 | 0.4259 | -0.074 ± 0.0128 | -0.0214 (59) |
| 25-40 | 785 | 0.2477 | 0.2074 | +0.0404 ± 0.01 | 0.7039 | 0.5961 | 0.6734 | 0.3609 | 0.4522 | -0.086 ± 0.0152 | -0.0219 (26) |
| 40+ | 260 | 0.3514 | 0.1975 | +0.1539 ± 0.0272 | 1.0146 | 0.5768 | 0.8089 | 0.3265 | 0.4269 | -0.095 ± 0.0248 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3231 | 0.1828 | 0.183 | -0.0002 ± 0.0003 | 0.5387 | 0.5383 | 0.5047 | 0.4893 | 0.5008 | -0.037 ± 0.0076 | -0.0157 (88) |
| 3-5 | 2252 | 0.1942 | 0.1925 | +0.0018 ± 0.0007 | 0.567 | 0.563 | 0.4958 | 0.456 | 0.4534 | -0.052 ± 0.0094 | -0.0209 (69) |
| 5-10 | 4481 | 0.1974 | 0.1891 | +0.0083 ± 0.001 | 0.5806 | 0.5561 | 0.4917 | 0.4182 | 0.4015 | -0.071 ± 0.0066 | -0.0082 (132) |
| 10-15 | 3135 | 0.2057 | 0.1896 | +0.0161 ± 0.0019 | 0.5999 | 0.5576 | 0.5284 | 0.4052 | 0.4006 | -0.067 ± 0.0078 | -0.0053 (105) |
| 15-25 | 3909 | 0.2295 | 0.1992 | +0.0303 ± 0.0028 | 0.6618 | 0.5775 | 0.5695 | 0.374 | 0.395 | -0.067 ± 0.0072 | -0.0253 (107) |
| 25-40 | 2705 | 0.2587 | 0.1843 | +0.0744 ± 0.0052 | 0.7333 | 0.5377 | 0.6328 | 0.3188 | 0.3597 | -0.077 ± 0.008 | -0.0229 (51) |
| 40+ | 1200 | 0.378 | 0.1445 | +0.2334 ± 0.0115 | 1.0706 | 0.4354 | 0.73 | 0.2264 | 0.2592 | -0.071 ± 0.0103 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4346 | 1.036 ± 0.043 | 1.13 | 0.1689 | 0.1642 | 0.2141 | 0.2057 |
| gen2 | 4346 | 0.839 ± 0.04 | 1.094 | 0.1686 | 0.1649 | 0.2337 | 0.2053 |
| gen1_elo | 4346 | 1.012 ± 0.041 | 1.123 | 0.1756 | 0.1643 | 0.2129 | 0.2059 |
| gen1_sr | 4346 | 1.024 ± 0.051 | 1.169 | 0.1296 | 0.1669 | 0.2299 | 0.2049 |
| gen1_ledger | 6414 | 0.862 ± 0.03 | 1.073 | 0.1838 | 0.1785 | 0.2186 | 0.1999 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 21,461)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,975 | 23.2% |
| STALE_QUOTE | market_freshness | 4,666 | 21.7% |
| BOOK_QUALITY | execution | 3,977 | 18.5% |
| POOR_DATA | data | 2,427 | 11.3% |
| LIMITED_DATA | data | 1,317 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,170 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,013 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 908 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 644 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 362 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 2 | 0.0% |

Cause class: coverage 23.2%, market_freshness 21.7%, execution 18.5%, data 17.4%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 70.9%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 49.4%, STALE_KALSHI_QUOTE 44.5%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 33.6%, WIDE_SPREAD 24.6%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.4%, LEVEL_TRANSFER_RISK 11.1%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 8.0%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.8%, POST_SETTLEMENT_OBSERVATION 23.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,539)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,014 | 34.8% |
| STALE_QUOTE | market_freshness | 2,163 | 18.8% |
| BOOK_QUALITY | execution | 2,066 | 17.9% |
| POOR_DATA | data | 1,006 | 8.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 626 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 514 | 4.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 411 | 3.6% |
| LIMITED_DATA | data | 400 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 256 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 81 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 2 | 0.0% |

Cause class: coverage 34.8%, market_freshness 18.8%, execution 17.9%, data 12.2%, market_freshness/coverage 9.0%, mapping 4.5%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 74.2%, THIN_PLAYER_HISTORY 62.1%, STALE_KALSHI_QUOTE 52.6%, STALE_PLAYER_DATA 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.9%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 23.7%, PLAYER_IDENTITY_RISK 19.6%, MODEL_HIGH_UNCERTAINTY 18.4%, LEVEL_TRANSFER_RISK 9.7%, EVENT_MAPPING_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.9%, POST_SETTLEMENT_OBSERVATION 34.8%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 8988, "IDENTITY_AMBIGUOUS": 2551}; ticker orientation: {"VERIFIED": 11539}.

Checks: discipline:AMBIGUOUS 758, discipline:PASS 10781, identity_confidence:AMBIGUOUS 2266, identity_confidence:PASS 9273, level_mapping:NA 770, level_mapping:PASS 10769, market_pair:AMBIGUOUS 401, market_pair:NA 291, market_pair:PASS 10847, model_complement:NA 258, model_complement:PASS 11281, namesake:AMBIGUOUS 6, namesake:PASS 11533, physical_match_id:NA 4009, physical_match_id:PASS 7530, player_ids:PASS 11539, same_pair_other_event:PASS 11539, ticker_orientation:PASS 11539

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,163 | 4.6% | 4.2% | 1.7% | {"market_freshness": 54, "model_calibration_or_unknown": 43, "data": 35, "execution": 23, "market_freshness/coverage": 13, "model_calibration": 13, "coverage": 11, "possible_market_error": 1} | 5.86 | 0.2181 / 0.213 (477) | 18.4% | 3.8% | 3.2% | 2.8% |
| CHALLENGER | 7,824 | 17.5% | 7.1% | 11.9% | {"coverage": 776, "market_freshness/coverage": 167, "market_freshness": 149, "data": 138, "model_calibration_or_unknown": 65, "execution": 31, "model_calibration": 28, "mapping": 15, "possible_market_error": 1} | 7.4 | 0.2197 / 0.2081 (1884) | 35.0% | 17.7% | 3.8% | 22.9% |
| DOUBLES | 1,615 | 46.9% | 46.5% | 6.6% | {"execution": 390, "mapping": 201, "market_freshness": 106, "market_freshness/coverage": 54, "coverage": 7} | 23.62 | 0.3105 / 0.2357 (428) | 14.5% | 0.0% | 100.0% | 7.2% |
| ITF_MEN | 14,481 | 25.4% | 17.6% | 31.9% | {"coverage": 1376, "execution": 699, "market_freshness": 627, "data": 485, "market_freshness/coverage": 318, "mapping": 173, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.9 | 0.2153 / 0.1975 (3262) | 37.5% | 70.1% | 19.9% | 22.2% |
| ITF_WOMEN | 19,018 | 27.3% | 19.8% | 44.9% | {"coverage": 1821, "market_freshness": 1133, "execution": 883, "data": 714, "market_freshness/coverage": 436, "mapping": 119, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.84 | 0.2034 / 0.1943 (3694) | 40.0% | 55.9% | 9.9% | 22.4% |
| OTHER | 151 | 8.0% | 7.2% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.66 | 0.1411 / 0.1522 (42) | 29.1% | 5.3% | 4.6% | 8.0% |
| WTA | 2,928 | 5.6% | 5.1% | 1.4% | {"market_freshness": 54, "model_calibration_or_unknown": 36, "execution": 26, "model_calibration": 16, "data": 11, "market_freshness/coverage": 10, "coverage": 10, "mapping": 1} | 7.7 | 0.238 / 0.2316 (485) | 24.7% | 1.4% | 1.6% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.5% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

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
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 22.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1345 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 50 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.969, "by_level_share_of_ge_25pp": {"ATP": 0.0167, "CHALLENGER": 0.1187, "DOUBLES": 0.0657, "ITF_MEN": 0.3191, "ITF_WOMEN": 0.4494, "OTHER": 0.001, "WTA": 0.0142, "WTA125": 0.0151}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5256, "share_primary_cause_market_settled_or_in_play": 0.4378, "share_primary_cause_stale_quote_only": 0.1875}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11539, "identity_ambiguous_share": 0.2211, "ticker_orientation": {"VERIFIED": 11539}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7530, "with_external": 375, "coverage": 0.0498, "external_status": {"EXTERNAL_STALE": 225, "AGREES_WITH_KALSHI": 141, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 225, "MODEL_LONE_OUTLIER": 141, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.376, "share_external_supports_model": 0.024}, "pregame_clean_ge_25pp": {"n": 3654, "with_external": 352, "coverage": 0.0963, "external_status": {"EXTERNAL_STALE": 209, "AGREES_WITH_KALSHI": 134, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 209, "MODEL_LONE_OUTLIER": 134, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3807, "share_external_supports_model": 0.0256}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 492.0, "median_sample_ratio": 2.43, "median_min_matches": 21.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2147, "data_status": {"POOR": 6432, "LIMITED": 3008, "ADEQUATE": 2099}, "comparison_lt_10pp": {"median_thinner_serve_points": 1682.0, "median_sample_ratio": 1.71, "median_min_matches": 94.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 855, "model_minus_observed": 0.0495, "kalshi_minus_observed": -0.089, "brier_diff_model_minus_kalshi": -0.0032}, "4-10x": {"n": 588, "model_minus_observed": 0.0929, "kalshi_minus_observed": -0.0531, "brier_diff_model_minus_kalshi": 0.0119}, "<2x": {"n": 2116, "model_minus_observed": 0.0934, "kalshi_minus_observed": -0.0301, "brier_diff_model_minus_kalshi": 0.0129}, ">=10x": {"n": 787, "model_minus_observed": 0.1068, "kalshi_minus_observed": -0.0684, "brier_diff_model_minus_kalshi": 0.0066}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4346, "model": {"intercept": -0.542, "slope": 0.839, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.213, "slope": 1.094, "slope_se": 0.044}, "mean_extremity_model": 0.1686, "mean_extremity_kalshi": 0.1649, "model_brier": 0.2337, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.0284, "brier_diff_se": 0.0029, "model_logloss": 0.6639, "kalshi_logloss": 0.5934}, "fair_v1": {"n": 4346, "model": {"intercept": -0.417, "slope": 1.036, "slope_se": 0.043}, "kalshi_mid_same_rows": {"intercept": 0.296, "slope": 1.13, "slope_se": 0.045}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1642, "model_brier": 0.2141, "kalshi_brier": 0.2057, "brier_diff_model_minus_kalshi": 0.0085, "brier_diff_se": 0.0024, "model_logloss": 0.6169, "kalshi_logloss": 0.5939}, "gen1_elo": {"n": 4346, "model": {"intercept": -0.396, "slope": 1.012, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.314, "slope": 1.123, "slope_se": 0.044}, "mean_extremity_model": 0.1756, "mean_extremity_kalshi": 0.1643, "model_brier": 0.2129, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0069, "brier_diff_se": 0.0024, "model_logloss": 0.6151, "kalshi_logloss": 0.5945}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2506, "share_ge_15": 0.4474, "median_abs_gap": 13.21, "n": 30049}, "gen1_elo": {"share_ge_25": 0.2475, "share_ge_15": 0.4464, "median_abs_gap": 13.02, "n": 30049}, "gen1_sr": {"share_ge_25": 0.3186, "share_ge_15": 0.5266, "median_abs_gap": 16.08, "n": 30049}, "gen2": {"share_ge_25": 0.3217, "share_ge_15": 0.5159, "median_abs_gap": 15.67, "n": 30049}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.157, "share_ge_15": 0.3629, "median_abs_gap": 10.97, "n": 23268}, "gen1_elo": {"share_ge_25": 0.1576, "share_ge_15": 0.3605, "median_abs_gap": 10.78, "n": 23265}, "gen1_sr": {"share_ge_25": 0.2242, "share_ge_15": 0.4482, "median_abs_gap": 13.18, "n": 23269}, "gen2": {"share_ge_25": 0.2403, "share_ge_15": 0.4472, "median_abs_gap": 13.13, "n": 23270}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0464, "share_ge_25_pregame_clean": 0.0418}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.056, "share_ge_25_pregame_clean": 0.051}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2338, "share_within_10pp_all": 0.4309, "share_within_10pp_pregame_clean": 0.4843, "corr_model_vs_mid_pregame_clean": 0.8433}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 632, "model_brier": 0.2009, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": -0.001}, "10-15": {"n_settled": 747, "model_brier": 0.2145, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0101}, "15-25": {"n_settled": 987, "model_brier": 0.2248, "kalshi_brier": 0.2126, "brier_diff_model_minus_kalshi": 0.0123}, "25-40": {"n_settled": 564, "model_brier": 0.2227, "kalshi_brier": 0.2091, "brier_diff_model_minus_kalshi": 0.0135}, "3-5": {"n_settled": 403, "model_brier": 0.2032, "kalshi_brier": 0.2027, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 113, "model_brier": 0.2806, "kalshi_brier": 0.1974, "brier_diff_model_minus_kalshi": 0.0832}, "5-10": {"n_settled": 900, "model_brier": 0.2025, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.542, "slope": 0.839, "slope_se": 0.04}, "kalshi_slope": {"intercept": 0.213, "slope": 1.094, "slope_se": 0.044}, "n": 4346}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.509, "slope": 0.862, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.154, "slope": 1.073, "slope_se": 0.035}, "n": 6414}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 428, "model_brier": 0.3105, "kalshi_brier": 0.2357, "brier_diff_model_minus_kalshi": 0.0748, "brier_diff_se": 0.0147, "corr_model_outcome": 0.0403, "corr_kalshi_outcome": 0.2551}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
