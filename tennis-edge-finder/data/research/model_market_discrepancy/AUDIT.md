# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-26T02:12Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 54,813): 0-3 13.9%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 19.3%, 25-40 13.9%, 40+ 8.1%; median gap 12.04 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.0%, Challenger 12.0%, doubles 7.1%). Main tour: ATP 4.4% and WTA 5.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 12,106): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.3%, BOOK_QUALITY 18.9%, STALE_QUOTE 18.6%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.3%, execution 18.9%, market_freshness 18.6%, data 11.9%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 12,106 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.4% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1762.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.037, Gen-2 0.832, Gen-1 ledger 0.862 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 589 model 0.2219 vs Kalshi 0.2104; n 116 model 0.2743 vs Kalshi 0.202.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 240,288 model-market comparisons (388,769 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 81,156 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-26T01:58:12.750479+00:00'], shadow board 63,129 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-26T01:58:15.821088+00:00'], Model 4 30,723 rows, 20,639 settled tickers, 7,333 tickers with an external scan.
* By model: {"gen1_ledger": 55594, "gen1_elo": 31745, "fair_v1": 31745, "gen2": 31745, "gen1_sr": 31745, "model4_fundamental": 28879, "model4_conditioned": 28835}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 54,813 | 13.9 | 9.5 | 19.9 | 15.4 | 19.3 | 13.9 | 8.1 | 12.04 | 41.3% | 22.1% |
| MW fair_v1 | 31,745 | 12.8 | 8.6 | 18.5 | 15.6 | 19.8 | 14.9 | 9.8 | 13.12 | 44.5% | 24.7% |
| MW gen1_elo | 31,745 | 12.7 | 8.5 | 19.1 | 15.2 | 19.9 | 14.9 | 9.6 | 13.0 | 44.4% | 24.5% |
| MW gen1_ledger | 23,068 | 15.4 | 10.7 | 21.7 | 15.2 | 18.6 | 12.6 | 5.9 | 10.54 | 37.0% | 18.5% |
| MW gen1_sr | 31,745 | 10.2 | 7.1 | 16.9 | 13.6 | 20.8 | 18.7 | 12.8 | 15.96 | 52.2% | 31.5% |
| MW gen2 | 31,745 | 11.0 | 7.4 | 16.3 | 14.0 | 19.4 | 17.9 | 13.9 | 15.56 | 51.3% | 31.9% |
| all families model4_conditioned | 28,835 | 21.7 | 18.4 | 34.5 | 17.8 | 4.7 | 1.7 | 1.1 | 6.06 | 7.5% | 2.8% |
| all families model4_fundamental | 28,879 | 16.7 | 13.2 | 34.0 | 20.7 | 10.5 | 3.6 | 1.4 | 7.83 | 15.5% | 5.0% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.8%, >=15pp 41.3%, >=20pp 30.7%, >=25pp 22.1%, >=30pp 15.9%, >=40pp 8.1%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.38pp; >=10pp 45.1%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,915 | 27.5 | 14.4 | 26.1 | 15.1 | 11.8 | 4.4 | 0.7 | 6.14 | 16.9% | 5.1% |
| CHALLENGER | 5,038 | 15.6 | 10.1 | 20.1 | 15.7 | 15.5 | 12.3 | 10.7 | 11.16 | 38.5% | 23.0% |
| ITF_MEN | 8,578 | 10.1 | 7.2 | 16.7 | 14.6 | 21.5 | 17.6 | 12.2 | 15.5 | 51.3% | 29.8% |
| ITF_WOMEN | 12,403 | 9.5 | 6.8 | 15.9 | 15.3 | 22.4 | 18.2 | 11.9 | 15.8 | 52.5% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,073 | 17.1 | 13.4 | 26.0 | 19.6 | 17.4 | 5.9 | 0.6 | 8.25 | 23.9% | 6.6% |
| WTA125 | 732 | 13.7 | 7.2 | 21.7 | 21.7 | 20.9 | 12.8 | 1.9 | 11.46 | 35.7% | 14.8% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,915 | 24.0 | 15.2 | 25.4 | 17.6 | 12.4 | 4.4 | 0.9 | 6.6 | 17.8% | 5.3% |
| CHALLENGER | 5,038 | 14.9 | 8.8 | 18.1 | 14.6 | 18.1 | 14.1 | 11.4 | 12.73 | 43.6% | 25.5% |
| ITF_MEN | 8,578 | 8.1 | 5.8 | 14.4 | 13.1 | 19.6 | 21.2 | 17.8 | 18.8 | 58.7% | 39.0% |
| ITF_WOMEN | 12,403 | 8.2 | 5.6 | 13.7 | 13.0 | 20.7 | 21.1 | 17.8 | 19.2 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,073 | 14.3 | 10.4 | 22.3 | 15.9 | 22.6 | 13.3 | 1.2 | 10.87 | 37.1% | 14.5% |
| WTA125 | 732 | 6.6 | 5.7 | 16.7 | 18.0 | 25.0 | 19.5 | 8.5 | 16.55 | 53.0% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,915 | 23.2 | 12.4 | 24.4 | 16.4 | 15.7 | 6.7 | 1.3 | 7.53 | 23.6% | 8.0% |
| CHALLENGER | 5,038 | 14.3 | 9.2 | 20.9 | 15.5 | 16.2 | 13.0 | 10.9 | 11.47 | 40.1% | 23.9% |
| ITF_MEN | 8,578 | 9.6 | 7.3 | 16.8 | 13.8 | 22.1 | 17.9 | 12.4 | 15.98 | 52.5% | 30.4% |
| ITF_WOMEN | 12,403 | 9.3 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.1 | 15.62 | 52.0% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,073 | 23.8 | 17.1 | 30.7 | 15.2 | 9.7 | 2.6 | 0.8 | 6.03 | 13.1% | 3.4% |
| WTA125 | 732 | 22.4 | 11.3 | 27.3 | 16.1 | 16.1 | 6.3 | 0.4 | 8.0 | 22.8% | 6.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,782 | 24.8 | 19.3 | 29.9 | 13.1 | 9.5 | 3.0 | 0.3 | 5.67 | 12.8% | 3.3% |
| CHALLENGER | 3,475 | 21.0 | 14.2 | 26.8 | 14.9 | 14.8 | 6.6 | 1.7 | 7.44 | 23.1% | 8.3% |
| DOUBLES | 1,809 | 5.1 | 4.5 | 12.3 | 10.2 | 20.2 | 25.8 | 21.9 | 24.05 | 67.9% | 47.7% |
| ITF_MEN | 6,341 | 13.6 | 9.2 | 19.9 | 16.2 | 21.5 | 13.3 | 6.4 | 12.19 | 41.2% | 19.7% |
| ITF_WOMEN | 7,462 | 12.5 | 8.8 | 19.5 | 15.3 | 21.6 | 16.1 | 6.1 | 12.85 | 43.9% | 22.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,253 | 22.8 | 15.3 | 30.8 | 18.0 | 9.7 | 3.1 | 0.3 | 6.86 | 13.2% | 3.4% |
| WTA125 | 797 | 20.8 | 13.4 | 22.0 | 18.4 | 14.6 | 8.7 | 2.1 | 8.33 | 25.4% | 10.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,835 | 27.8 | 14.6 | 26.5 | 15.0 | 11.6 | 4.0 | 0.4 | 5.99 | 16.1% | 4.4% |
| CHALLENGER | 3,559 | 20.4 | 12.6 | 24.8 | 18.1 | 15.5 | 6.8 | 1.8 | 8.41 | 24.1% | 8.6% |
| ITF_MEN | 6,261 | 12.2 | 8.7 | 20.2 | 16.6 | 22.8 | 14.4 | 5.1 | 12.57 | 42.2% | 19.5% |
| ITF_WOMEN | 9,280 | 11.2 | 8.1 | 18.1 | 17.3 | 24.4 | 15.4 | 5.5 | 13.56 | 45.2% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,014 | 17.4 | 13.2 | 26.0 | 19.8 | 17.3 | 5.6 | 0.7 | 8.25 | 23.6% | 6.3% |
| WTA125 | 706 | 14.0 | 7.1 | 21.2 | 22.1 | 21.5 | 12.5 | 1.6 | 11.47 | 35.5% | 14.0% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,835 | 24.2 | 15.5 | 25.7 | 17.6 | 12.4 | 4.1 | 0.5 | 6.48 | 17.0% | 4.6% |
| CHALLENGER | 3,559 | 19.0 | 11.3 | 22.3 | 17.3 | 18.4 | 9.7 | 2.0 | 9.36 | 30.0% | 11.7% |
| ITF_MEN | 6,262 | 9.6 | 7.1 | 16.8 | 15.1 | 21.6 | 19.3 | 10.5 | 15.48 | 51.4% | 29.8% |
| ITF_WOMEN | 9,281 | 9.3 | 6.4 | 15.2 | 14.5 | 22.7 | 20.6 | 11.4 | 16.83 | 54.6% | 31.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,014 | 14.4 | 10.4 | 22.3 | 15.9 | 22.6 | 13.1 | 1.2 | 10.87 | 36.9% | 14.3% |
| WTA125 | 706 | 6.4 | 6.0 | 16.7 | 18.4 | 24.9 | 20.0 | 7.7 | 16.25 | 52.5% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,731 | 25.0 | 19.6 | 29.9 | 13.3 | 9.2 | 2.9 | 0.2 | 5.65 | 12.2% | 3.1% |
| CHALLENGER | 3,046 | 22.4 | 15.1 | 28.2 | 15.0 | 14.2 | 4.6 | 0.5 | 6.94 | 19.3% | 5.1% |
| DOUBLES | 1,689 | 5.1 | 4.6 | 12.6 | 10.4 | 20.0 | 25.8 | 21.7 | 23.92 | 67.4% | 47.4% |
| ITF_MEN | 5,319 | 14.8 | 9.8 | 21.6 | 17.0 | 21.4 | 11.6 | 3.9 | 11.23 | 36.9% | 15.5% |
| ITF_WOMEN | 6,213 | 13.4 | 9.3 | 20.9 | 16.1 | 21.9 | 14.9 | 3.6 | 11.82 | 40.3% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,201 | 23.1 | 15.7 | 30.8 | 18.0 | 9.7 | 2.5 | 0.1 | 6.8 | 12.3% | 2.6% |
| WTA125 | 686 | 22.6 | 14.7 | 23.3 | 19.8 | 13.0 | 6.0 | 0.6 | 7.6 | 19.5% | 6.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,809 | 5.1 | 4.5 | 12.3 | 10.2 | 20.2 | 25.8 | 21.9 | 24.05 | 67.9% | 47.7% |
| singles | 21,259 | 16.2 | 11.2 | 22.5 | 15.6 | 18.4 | 11.5 | 4.5 | 10.0 | 34.4% | 16.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 6,936 | 12.9 | 9.0 | 19.3 | 15.9 | 19.0 | 14.2 | 9.7 | 12.71 | 42.9% | 23.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 19,904 | 13.3 | 8.7 | 18.6 | 15.2 | 19.8 | 14.8 | 9.6 | 13.03 | 44.2% | 24.4% |
| UNKNOWN | 4,656 | 10.8 | 7.5 | 17.0 | 16.8 | 20.6 | 16.3 | 11.0 | 14.12 | 48.0% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,153 | 19.5 | 12.0 | 21.8 | 16.4 | 14.9 | 9.2 | 6.1 | 9.0 | 30.3% | 15.3% |
| B | 3,935 | 12.2 | 8.7 | 19.4 | 16.5 | 19.6 | 12.8 | 10.9 | 12.78 | 43.2% | 23.7% |
| C | 4,424 | 11.7 | 8.9 | 19.5 | 15.5 | 19.3 | 14.7 | 10.4 | 13.1 | 44.4% | 25.1% |
| D | 4,846 | 12.2 | 7.8 | 17.3 | 15.4 | 21.7 | 15.6 | 10.0 | 13.98 | 47.3% | 25.6% |
| F | 9,387 | 7.5 | 5.4 | 15.1 | 14.6 | 23.7 | 21.2 | 12.5 | 17.79 | 57.4% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,625 | 23.1 | 15.9 | 29.0 | 15.3 | 11.4 | 4.0 | 1.3 | 6.65 | 16.7% | 5.3% |
| B | 3,117 | 16.0 | 10.4 | 23.2 | 16.2 | 20.0 | 10.5 | 3.7 | 10.06 | 34.2% | 14.2% |
| C | 4,552 | 10.9 | 7.1 | 18.5 | 14.4 | 21.2 | 16.8 | 11.1 | 14.49 | 49.1% | 27.9% |
| D | 3,145 | 14.2 | 9.6 | 20.1 | 14.9 | 21.1 | 14.2 | 6.0 | 12.04 | 41.2% | 20.1% |
| F | 5,629 | 10.2 | 8.3 | 15.9 | 15.2 | 22.7 | 19.7 | 8.0 | 15.24 | 50.5% | 27.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,442 | 17.7 | 10.8 | 21.1 | 16.1 | 15.6 | 10.1 | 8.7 | 10.09 | 34.3% | 18.8% |
| LIMITED | 6,726 | 13.4 | 10.2 | 20.0 | 16.2 | 19.3 | 13.3 | 7.6 | 11.91 | 40.2% | 20.9% |
| POOR | 14,577 | 9.1 | 6.3 | 15.9 | 14.9 | 23.0 | 19.1 | 11.6 | 16.27 | 53.7% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,740 | 24.8 | 18.7 | 33.5 | 14.4 | 6.1 | 2.3 | 0.2 | 5.68 | 8.6% | 2.5% |
| GAME_SPREAD | 5,212 | 22.3 | 15.2 | 33.4 | 17.0 | 9.1 | 2.5 | 0.3 | 6.71 | 12.0% | 2.9% |
| MATCH_WINNER | 23,068 | 15.4 | 10.7 | 21.7 | 15.2 | 18.6 | 12.6 | 5.9 | 10.54 | 37.0% | 18.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,063 | 27.8 | 16.3 | 31.3 | 12.7 | 9.3 | 2.2 | 0.3 | 5.7 | 11.9% | 2.6% |
| TOTAL_GAMES | 8,487 | 9.0 | 10.0 | 36.2 | 27.7 | 10.6 | 3.8 | 2.8 | 9.4 | 17.1% | 6.6% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,347 | 24.5 | 31.4 | 32.8 | 6.5 | 3.7 | 0.8 | 0.2 | 4.65 | 4.7% | 1.0% |
| GAME_SPREAD | 6,758 | 45.9 | 16.7 | 26.4 | 7.8 | 1.8 | 1.1 | 0.4 | 3.42 | 3.2% | 1.5% |
| TOTAL_GAMES | 11,730 | 5.3 | 8.0 | 40.8 | 33.4 | 7.3 | 2.9 | 2.3 | 9.54 | 12.5% | 5.2% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,358 | 23.5 | 17.0 | 35.3 | 14.0 | 7.3 | 2.6 | 0.4 | 6.04 | 10.2% | 2.9% |
| GAME_SPREAD | 6,761 | 19.8 | 13.2 | 28.0 | 20.9 | 12.9 | 4.3 | 1.0 | 7.96 | 18.2% | 5.3% |
| TOTAL_GAMES | 11,760 | 8.9 | 9.8 | 36.2 | 26.4 | 12.0 | 4.1 | 2.5 | 9.42 | 18.6% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 31,745 | 44.5% | 24.7% | 13.12 | 36.0% | 15.5% | 10.91 |
| gen1_elo | 31,745 | 44.4% | 24.5% | 13.0 | 35.9% | 15.6% | 10.71 |
| gen1_sr | 31,745 | 52.2% | 31.5% | 15.96 | 44.4% | 22.1% | 13.03 |
| gen2 | 31,745 | 51.3% | 31.9% | 15.56 | 44.5% | 23.8% | 13.03 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 16,061 | 15.6 | 10.4 | 21.4 | 17.3 | 20.2 | 11.9 | 3.3 | 10.72 | 35.3% | 15.1% |
| STALE | 15,684 | 10.1 | 6.7 | 15.5 | 13.8 | 19.3 | 18.1 | 16.5 | 16.86 | 53.8% | 34.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 16,536 | 16.2 | 11.2 | 22.5 | 15.3 | 17.8 | 12.0 | 4.9 | 10.01 | 34.8% | 16.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 54,813 | 16536 | 19533 | 18744 | 24.1 | 139.0 | 1400.4 |
| ge_15pp | 22,661 | 5746 | 6959 | 9956 | 26.3 | 440.0 | 1380.4 |
| ge_25pp | 12,106 | 2799 | 3020 | 6287 | 31.9 | 582.7 | 1380.4 |
| lt_10pp | 23,707 | 8256 | 9239 | 6212 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261026T021237Z-532e9acb`: 878 priced rows, quote age at build {'median': 14.9, 'max': 15.0}, freshness {'AGING': 878}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 28 | 0.0 | 0.0 | 21.4 | 10.7 | 39.3 | 28.6 | 0.0 | 20.48 | 67.9% | 28.6% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,078 | 19.3 | 11.3 | 24.9 | 18.8 | 18.1 | 7.0 | 0.6 | 8.82 | 25.7% | 7.6% |
| KALSHI_LONE_OUTLIER | 21 | 4.8 | 4.8 | 76.2 | 4.8 | 4.8 | 4.8 | 0.0 | 6.11 | 9.5% | 4.8% |
| MARKETS_AGREE | 624 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.22 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,352 | 0.0 | 2.6 | 35.1 | 26.6 | 24.8 | 10.4 | 0.7 | 12.12 | 35.8% | 11.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 31,745 | 5121 (16.1%) | 26.4% | 0.9% | {"EXTERNAL_STALE": 3078, "AGREES_WITH_KALSHI": 1352, "ALL_AGREE": 624, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 21, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 14,116 | 1297 (9.2%) | 37.3% | 1.6% | {"EXTERNAL_STALE": 792, "AGREES_WITH_KALSHI": 484, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,845 | 393 (5.0%) | 37.9% | 2.3% | {"EXTERNAL_STALE": 235, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,813 | 370 (9.7%) | 38.4% | 2.4% | {"EXTERNAL_STALE": 219, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,682 | 2882 (22.7%) | 17.7% | 0.8% | {"EXTERNAL_STALE": 1707, "ALL_AGREE": 624, "AGREES_WITH_KALSHI": 509, "EXTERNAL_OUTLIER": 18, "AGREES_WITH_MODEL": 18, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,048 | 10.2 | 7.6 | 19.4 | 14.6 | 22.5 | 15.9 | 9.9 | 14.15 | 48.3% | 25.8% |
| 4-10x | 4,098 | 11.2 | 8.4 | 18.8 | 15.5 | 21.6 | 14.7 | 9.9 | 13.74 | 46.2% | 24.6% |
| <2x | 16,221 | 15.0 | 9.9 | 19.2 | 16.4 | 17.5 | 13.0 | 9.0 | 11.75 | 39.5% | 22.0% |
| >=10x | 5,378 | 10.8 | 6.1 | 15.2 | 14.2 | 22.0 | 19.6 | 12.1 | 16.47 | 53.7% | 31.7% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,131 | 12.5 | 8.7 | 19.2 | 16.1 | 19.1 | 13.9 | 10.6 | 12.96 | 43.6% | 24.5% |
| 300-1000 | 6,659 | 11.7 | 8.6 | 17.3 | 15.4 | 20.7 | 16.2 | 10.1 | 13.85 | 47.0% | 26.3% |
| <300 | 10,320 | 8.5 | 5.6 | 15.4 | 14.7 | 23.3 | 20.1 | 12.3 | 17.02 | 55.7% | 32.4% |
| >=3000 | 6,635 | 21.2 | 13.1 | 23.6 | 16.4 | 14.1 | 6.9 | 4.6 | 7.83 | 25.6% | 11.5% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 895 | 0.5508 | 0.413 | 0.5028 | +0.048 | -0.090 | -0.0042 ± 0.0051 |
| ratio 4-10x | 607 | 0.5883 | 0.4428 | 0.4975 | +0.091 | -0.055 | 0.0102 ± 0.0065 |
| ratio <2x | 2230 | 0.539 | 0.4158 | 0.4484 | +0.091 | -0.033 | 0.0116 ± 0.0031 |
| ratio >=10x | 822 | 0.5706 | 0.395 | 0.4611 | +0.110 | -0.066 | 0.0078 ± 0.0064 |
| thinner_sample 1000-3000 | 1241 | 0.5427 | 0.4159 | 0.4504 | +0.092 | -0.035 | 0.0093 ± 0.0041 |
| thinner_sample 300-1000 | 1020 | 0.5664 | 0.4225 | 0.4922 | +0.074 | -0.070 | 0.0003 ± 0.0051 |
| thinner_sample <300 | 1532 | 0.5622 | 0.3956 | 0.4641 | +0.098 | -0.069 | 0.0092 ± 0.0045 |
| thinner_sample >=3000 | 761 | 0.5369 | 0.443 | 0.4717 | +0.065 | -0.029 | 0.0116 ± 0.0042 |
| data_status ADEQUATE | 1318 | 0.5385 | 0.4345 | 0.4545 | +0.084 | -0.020 | 0.0113 ± 0.0034 |
| data_status LIMITED | 1049 | 0.5512 | 0.4174 | 0.4852 | +0.066 | -0.068 | 0.0029 ± 0.0046 |
| data_status POOR | 2187 | 0.5638 | 0.4023 | 0.4678 | +0.096 | -0.066 | 0.0076 ± 0.0037 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 668 | 0.2018 | 0.2026 | -0.0008 ± 0.0006 | 0.5846 | 0.5864 | 0.5021 | 0.4873 | 0.5195 | -0.075 ± 0.0183 | -0.01 (5) |
| 3-5 | 420 | 0.2059 | 0.2051 | +0.0008 ± 0.0018 | 0.5952 | 0.5918 | 0.5027 | 0.4626 | 0.4714 | -0.108 ± 0.0228 | 0.02 (1) |
| 5-10 | 938 | 0.2018 | 0.2017 | +0.0001 ± 0.0022 | 0.59 | 0.5868 | 0.5137 | 0.4395 | 0.4712 | -0.090 ± 0.0152 | -0.0167 (6) |
| 10-15 | 792 | 0.215 | 0.2065 | +0.0085 ± 0.004 | 0.6205 | 0.5953 | 0.5309 | 0.4068 | 0.4343 | -0.101 ± 0.0161 | -0.048 (5) |
| 15-25 | 1031 | 0.2258 | 0.2133 | +0.0125 ± 0.0056 | 0.6474 | 0.6104 | 0.5776 | 0.3818 | 0.4481 | -0.096 ± 0.0144 | -0.0033 (9) |
| 25-40 | 589 | 0.2219 | 0.2104 | +0.0116 ± 0.0112 | 0.6332 | 0.6042 | 0.66 | 0.3503 | 0.4839 | -0.072 ± 0.0172 | -0.01 (1) |
| 40+ | 116 | 0.2743 | 0.202 | +0.0723 ± 0.036 | 0.7526 | 0.5904 | 0.7587 | 0.3114 | 0.4569 | -0.070 ± 0.0354 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3433 | 0.1853 | 0.1861 | -0.0009 ± 0.0003 | 0.5462 | 0.5471 | 0.4917 | 0.4767 | 0.5077 | -0.025 ± 0.0075 | -0.0129 (17) |
| 3-5 | 2262 | 0.1992 | 0.198 | +0.0012 ± 0.0008 | 0.579 | 0.5735 | 0.4839 | 0.4439 | 0.4483 | -0.053 ± 0.0095 | 0.0 (2) |
| 5-10 | 4900 | 0.1982 | 0.195 | +0.0032 ± 0.0009 | 0.581 | 0.5696 | 0.4836 | 0.4097 | 0.4243 | -0.047 ± 0.0064 | -0.0119 (21) |
| 10-15 | 4183 | 0.1978 | 0.1805 | +0.0174 ± 0.0016 | 0.5811 | 0.5321 | 0.4878 | 0.3634 | 0.3557 | -0.071 ± 0.0066 | -0.0281 (16) |
| 15-25 | 5269 | 0.209 | 0.1693 | +0.0397 ± 0.0022 | 0.6117 | 0.5006 | 0.5042 | 0.3077 | 0.3063 | -0.075 ± 0.0056 | -0.0025 (44) |
| 25-40 | 4122 | 0.2231 | 0.1286 | +0.0946 ± 0.0035 | 0.6405 | 0.3938 | 0.5325 | 0.2191 | 0.2285 | -0.061 ± 0.0054 | -0.01 (1) |
| 40+ | 2660 | 0.3794 | 0.0451 | +0.3342 ± 0.0047 | 0.9881 | 0.1738 | 0.6322 | 0.1064 | 0.0639 | -0.078 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 527 | 0.2079 | 0.2086 | -0.0007 ± 0.0007 | 0.5978 | 0.5995 | 0.5056 | 0.4904 | 0.518 | -0.102 ± 0.0215 | -0.01 (3) |
| 3-5 | 373 | 0.2262 | 0.2232 | +0.0029 ± 0.002 | 0.639 | 0.6329 | 0.5149 | 0.4751 | 0.4531 | -0.134 ± 0.0261 | 0.02 (1) |
| 5-10 | 819 | 0.2068 | 0.2064 | +0.0004 ± 0.0024 | 0.5999 | 0.5981 | 0.5473 | 0.4724 | 0.5104 | -0.083 ± 0.0164 | -0.01 (4) |
| 10-15 | 756 | 0.2162 | 0.2098 | +0.0064 ± 0.0042 | 0.6215 | 0.6051 | 0.5645 | 0.4403 | 0.4788 | -0.107 ± 0.0174 | -0.04 (5) |
| 15-25 | 1054 | 0.2292 | 0.211 | +0.0181 ± 0.0056 | 0.651 | 0.6046 | 0.5876 | 0.392 | 0.4478 | -0.098 ± 0.0144 | -0.0133 (9) |
| 25-40 | 744 | 0.2659 | 0.1991 | +0.0669 ± 0.0103 | 0.7433 | 0.5795 | 0.6551 | 0.3401 | 0.3938 | -0.119 ± 0.0161 | -0.0075 (4) |
| 40+ | 281 | 0.3519 | 0.1748 | +0.1771 ± 0.0246 | 0.968 | 0.5207 | 0.7338 | 0.25 | 0.3238 | -0.064 ± 0.0238 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2927 | 0.1934 | 0.1937 | -0.0003 ± 0.0003 | 0.563 | 0.5635 | 0.5127 | 0.4977 | 0.5132 | -0.043 ± 0.0084 | -0.0133 (15) |
| 3-5 | 1944 | 0.1997 | 0.1986 | +0.0011 ± 0.0008 | 0.5772 | 0.5744 | 0.5141 | 0.4742 | 0.4805 | -0.048 ± 0.0103 | 0.02 (1) |
| 5-10 | 4335 | 0.1972 | 0.195 | +0.0022 ± 0.001 | 0.5803 | 0.5695 | 0.5112 | 0.4372 | 0.4627 | -0.035 ± 0.0068 | -0.0117 (6) |
| 10-15 | 3787 | 0.2012 | 0.1894 | +0.0118 ± 0.0018 | 0.5906 | 0.5521 | 0.5142 | 0.3903 | 0.4051 | -0.055 ± 0.0072 | -0.0189 (18) |
| 15-25 | 5212 | 0.2157 | 0.1788 | +0.0369 ± 0.0023 | 0.6265 | 0.5253 | 0.525 | 0.3291 | 0.3369 | -0.066 ± 0.0059 | -0.0086 (42) |
| 25-40 | 4815 | 0.2534 | 0.1366 | +0.1168 ± 0.0034 | 0.7122 | 0.4196 | 0.5583 | 0.2413 | 0.2181 | -0.089 ± 0.0053 | -0.0044 (18) |
| 40+ | 3809 | 0.3918 | 0.0608 | +0.3310 ± 0.0046 | 1.0309 | 0.2169 | 0.6499 | 0.1191 | 0.0858 | -0.071 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 639 | 0.1992 | 0.2013 | -0.0021 ± 0.0006 | 0.579 | 0.5841 | 0.5005 | 0.4853 | 0.5462 | -0.034 ± 0.0184 | -0.0137 (8) |
| 3-5 | 454 | 0.2036 | 0.202 | +0.0015 ± 0.0017 | 0.5906 | 0.5855 | 0.506 | 0.4663 | 0.4692 | -0.118 ± 0.022 | 0.0067 (3) |
| 5-10 | 965 | 0.2027 | 0.1993 | +0.0035 ± 0.0022 | 0.5918 | 0.5802 | 0.5093 | 0.4353 | 0.4477 | -0.105 ± 0.0148 | -0.0071 (7) |
| 10-15 | 784 | 0.2087 | 0.2054 | +0.0034 ± 0.004 | 0.6065 | 0.5931 | 0.5404 | 0.4169 | 0.4668 | -0.085 ± 0.0161 | -0.0317 (6) |
| 15-25 | 974 | 0.2314 | 0.2142 | +0.0171 ± 0.0058 | 0.6607 | 0.6121 | 0.5895 | 0.3949 | 0.4476 | -0.108 ± 0.0148 | -0.03 (1) |
| 25-40 | 615 | 0.2141 | 0.2173 | -0.0032 ± 0.011 | 0.6177 | 0.6202 | 0.6688 | 0.3581 | 0.5154 | -0.056 ± 0.0169 | 0.015 (2) |
| 40+ | 123 | 0.2879 | 0.2151 | +0.0728 ± 0.0362 | 0.7962 | 0.6188 | 0.7691 | 0.3198 | 0.4715 | -0.063 ± 0.0383 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3359 | 0.1862 | 0.1869 | -0.0007 ± 0.0003 | 0.5476 | 0.5487 | 0.4889 | 0.4737 | 0.4927 | -0.034 ± 0.0075 | -0.0163 (35) |
| 3-5 | 2275 | 0.1959 | 0.194 | +0.0019 ± 0.0007 | 0.5746 | 0.5683 | 0.4875 | 0.4479 | 0.4448 | -0.063 ± 0.0094 | -0.0094 (18) |
| 5-10 | 4989 | 0.1958 | 0.1902 | +0.0056 ± 0.0009 | 0.5752 | 0.5567 | 0.4839 | 0.4099 | 0.4097 | -0.060 ± 0.0062 | -0.01 (31) |
| 10-15 | 4047 | 0.1917 | 0.1764 | +0.0153 ± 0.0016 | 0.5669 | 0.5216 | 0.4996 | 0.3762 | 0.3756 | -0.065 ± 0.0066 | -0.015 (12) |
| 15-25 | 5414 | 0.2112 | 0.1721 | +0.0392 ± 0.0022 | 0.6169 | 0.5073 | 0.5145 | 0.3194 | 0.3171 | -0.074 ± 0.0056 | -0.03 (2) |
| 25-40 | 4147 | 0.2194 | 0.1314 | +0.0880 ± 0.0035 | 0.6332 | 0.3997 | 0.5366 | 0.2208 | 0.2409 | -0.053 ± 0.0054 | 0.01 (3) |
| 40+ | 2598 | 0.3936 | 0.0507 | +0.3429 ± 0.005 | 1.0284 | 0.188 | 0.6448 | 0.1136 | 0.0704 | -0.080 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1026 | 0.196 | 0.1962 | -0.0001 ± 0.0005 | 0.5715 | 0.5714 | 0.5018 | 0.4867 | 0.4912 | -0.062 ± 0.014 | -0.0224 (49) |
| 3-5 | 707 | 0.1924 | 0.1916 | +0.0008 ± 0.0013 | 0.5623 | 0.5591 | 0.4909 | 0.4511 | 0.4583 | -0.062 ± 0.0168 | -0.0194 (34) |
| 5-10 | 1494 | 0.2022 | 0.1964 | +0.0058 ± 0.0017 | 0.5935 | 0.5753 | 0.4962 | 0.4229 | 0.421 | -0.075 ± 0.0117 | -0.005 (78) |
| 10-15 | 997 | 0.21 | 0.1981 | +0.0119 ± 0.0035 | 0.609 | 0.5779 | 0.5243 | 0.4012 | 0.4122 | -0.072 ± 0.0144 | 0.0014 (64) |
| 15-25 | 1333 | 0.2317 | 0.2117 | +0.0200 ± 0.0049 | 0.6615 | 0.6085 | 0.5795 | 0.3847 | 0.4321 | -0.073 ± 0.0126 | -0.0214 (59) |
| 25-40 | 809 | 0.2469 | 0.2086 | +0.0383 ± 0.0099 | 0.7032 | 0.599 | 0.6766 | 0.3642 | 0.4586 | -0.088 ± 0.015 | -0.0219 (26) |
| 40+ | 267 | 0.3467 | 0.2029 | +0.1438 ± 0.027 | 1.0025 | 0.5933 | 0.8095 | 0.3282 | 0.4382 | -0.089 ± 0.0249 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3388 | 0.1827 | 0.1829 | -0.0002 ± 0.0003 | 0.5381 | 0.5376 | 0.5027 | 0.4874 | 0.4965 | -0.041 ± 0.0074 | -0.0157 (88) |
| 3-5 | 2346 | 0.1956 | 0.1937 | +0.0019 ± 0.0007 | 0.5701 | 0.5658 | 0.4977 | 0.4579 | 0.454 | -0.055 ± 0.0092 | -0.0209 (69) |
| 5-10 | 4704 | 0.1963 | 0.1883 | +0.0080 ± 0.0009 | 0.5784 | 0.5541 | 0.4915 | 0.418 | 0.4031 | -0.070 ± 0.0064 | -0.0082 (132) |
| 10-15 | 3311 | 0.207 | 0.1908 | +0.0162 ± 0.0019 | 0.6027 | 0.5598 | 0.5292 | 0.4062 | 0.4011 | -0.067 ± 0.0076 | -0.0053 (105) |
| 15-25 | 4108 | 0.2306 | 0.2006 | +0.0300 ± 0.0028 | 0.6645 | 0.5806 | 0.5701 | 0.3745 | 0.397 | -0.066 ± 0.007 | -0.0253 (107) |
| 25-40 | 2793 | 0.2594 | 0.1859 | +0.0735 ± 0.0051 | 0.7354 | 0.5415 | 0.634 | 0.3205 | 0.3623 | -0.078 ± 0.008 | -0.0229 (51) |
| 40+ | 1225 | 0.3759 | 0.146 | +0.2299 ± 0.0115 | 1.0646 | 0.4399 | 0.7318 | 0.2283 | 0.2653 | -0.070 ± 0.0102 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4554 | 1.037 ± 0.042 | 1.112 | 0.1684 | 0.1632 | 0.2144 | 0.2068 |
| gen2 | 4554 | 0.832 ± 0.039 | 1.08 | 0.1681 | 0.164 | 0.2339 | 0.2065 |
| gen1_elo | 4554 | 1.009 ± 0.04 | 1.109 | 0.1751 | 0.1634 | 0.2133 | 0.2069 |
| gen1_sr | 4554 | 1.019 ± 0.05 | 1.145 | 0.1292 | 0.1659 | 0.2302 | 0.206 |
| gen1_ledger | 6633 | 0.862 ± 0.029 | 1.065 | 0.1837 | 0.1772 | 0.2186 | 0.2009 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 22,661)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,164 | 22.8% |
| STALE_QUOTE | market_freshness | 4,889 | 21.6% |
| BOOK_QUALITY | execution | 4,361 | 19.2% |
| POOR_DATA | data | 2,519 | 11.1% |
| LIMITED_DATA | data | 1,398 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,225 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,075 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 957 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 666 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 406 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.8%, market_freshness 21.6%, execution 19.2%, data 17.3%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 93.9%, LOW_DATA_QUALITY 70.7%, THIN_PLAYER_HISTORY 59.4%, STALE_PLAYER_DATA 49.5%, STALE_KALSHI_QUOTE 43.9%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.7%, EVENT_MAPPING_RISK 8.3%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.9%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.3%, POST_SETTLEMENT_OBSERVATION 22.8%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 12,106)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,148 | 34.3% |
| BOOK_QUALITY | execution | 2,283 | 18.9% |
| STALE_QUOTE | market_freshness | 2,252 | 18.6% |
| POOR_DATA | data | 1,027 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 654 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 535 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 423 | 3.5% |
| LIMITED_DATA | data | 420 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 266 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 97 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.3%, execution 18.9%, market_freshness 18.6%, data 11.9%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.2%, THIN_PLAYER_HISTORY 61.4%, STALE_KALSHI_QUOTE 51.9%, STALE_PLAYER_DATA 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 24.7%, PLAYER_IDENTITY_RISK 20.1%, MODEL_HIGH_UNCERTAINTY 18.3%, EVENT_MAPPING_RISK 10.1%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.2%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.4%, POST_SETTLEMENT_OBSERVATION 34.3%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9371, "IDENTITY_AMBIGUOUS": 2735}; ticker orientation: {"VERIFIED": 12106}.

Checks: discipline:AMBIGUOUS 863, discipline:PASS 11243, identity_confidence:AMBIGUOUS 2428, identity_confidence:PASS 9678, level_mapping:NA 875, level_mapping:PASS 11231, market_pair:AMBIGUOUS 465, market_pair:NA 300, market_pair:PASS 11341, model_complement:NA 267, model_complement:PASS 11839, namesake:AMBIGUOUS 6, namesake:PASS 12100, physical_match_id:NA 4261, physical_match_id:PASS 7845, player_ids:PASS 12106, same_pair_other_event:PASS 12106, ticker_orientation:PASS 12106

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,697 | 4.4% | 3.9% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 47, "data": 35, "execution": 24, "model_calibration": 20, "market_freshness/coverage": 15, "coverage": 13} | 5.92 | 0.2239 / 0.2208 (539) | 19.4% | 3.3% | 3.3% | 2.8% |
| CHALLENGER | 8,513 | 17.0% | 7.0% | 12.0% | {"coverage": 812, "market_freshness/coverage": 175, "market_freshness": 164, "data": 144, "model_calibration_or_unknown": 69, "model_calibration": 35, "execution": 33, "mapping": 16, "possible_market_error": 1} | 7.61 | 0.2184 / 0.2082 (2005) | 34.4% | 17.6% | 4.1% | 22.4% |
| DOUBLES | 1,809 | 47.7% | 47.4% | 7.1% | {"execution": 480, "mapping": 215, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.92 | 0.3106 / 0.2361 (437) | 12.9% | 0.0% | 100.0% | 6.6% |
| ITF_MEN | 14,919 | 25.5% | 17.6% | 31.4% | {"coverage": 1429, "execution": 722, "market_freshness": 647, "data": 496, "market_freshness/coverage": 333, "mapping": 175, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.94 | 0.2165 / 0.1985 (3333) | 37.4% | 70.0% | 19.9% | 22.4% |
| ITF_WOMEN | 19,865 | 27.2% | 19.9% | 44.6% | {"coverage": 1862, "market_freshness": 1178, "execution": 973, "data": 730, "market_freshness/coverage": 450, "mapping": 123, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.92 | 0.2032 / 0.1957 (3806) | 39.6% | 56.6% | 10.1% | 22.0% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,326 | 5.4% | 4.9% | 1.5% | {"market_freshness": 62, "model_calibration_or_unknown": 38, "execution": 26, "model_calibration": 16, "data": 14, "coverage": 12, "market_freshness/coverage": 10, "mapping": 1} | 7.65 | 0.2323 / 0.2276 (523) | 24.4% | 1.3% | 1.6% | 3.3% |
| WTA125 | 1,529 | 12.7% | 10.3% | 1.6% | {"market_freshness": 40, "model_calibration_or_unknown": 39, "market_freshness/coverage": 38, "data": 28, "execution": 20, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.63 | 0.2178 / 0.2042 (502) | 23.1% | 11.6% | 7.0% | 9.0% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
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
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
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
| 49 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9681, "by_level_share_of_ge_25pp": {"ATP": 0.0171, "CHALLENGER": 0.1197, "DOUBLES": 0.0713, "ITF_MEN": 0.3144, "ITF_WOMEN": 0.4457, "OTHER": 0.001, "WTA": 0.0148, "WTA125": 0.016}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5193, "share_primary_cause_market_settled_or_in_play": 0.4315, "share_primary_cause_stale_quote_only": 0.186}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 12106, "identity_ambiguous_share": 0.2259, "ticker_orientation": {"VERIFIED": 12106}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7845, "with_external": 393, "coverage": 0.0501, "external_status": {"EXTERNAL_STALE": 235, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 235, "MODEL_LONE_OUTLIER": 149, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3791, "share_external_supports_model": 0.0229}, "pregame_clean_ge_25pp": {"n": 3813, "with_external": 370, "coverage": 0.097, "external_status": {"EXTERNAL_STALE": 219, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 219, "MODEL_LONE_OUTLIER": 142, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3838, "share_external_supports_model": 0.0243}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.41, "median_min_matches": 21.0, "median_max_days_since_last": 228.0, "share_severe_asymmetry": 0.2139, "data_status": {"POOR": 6695, "LIMITED": 3189, "ADEQUATE": 2222}, "comparison_lt_10pp": {"median_thinner_serve_points": 1762.0, "median_sample_ratio": 1.67, "median_min_matches": 98.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 895, "model_minus_observed": 0.0481, "kalshi_minus_observed": -0.0897, "brier_diff_model_minus_kalshi": -0.0042}, "4-10x": {"n": 607, "model_minus_observed": 0.0907, "kalshi_minus_observed": -0.0547, "brier_diff_model_minus_kalshi": 0.0102}, "<2x": {"n": 2230, "model_minus_observed": 0.0906, "kalshi_minus_observed": -0.0326, "brier_diff_model_minus_kalshi": 0.0116}, ">=10x": {"n": 822, "model_minus_observed": 0.1095, "kalshi_minus_observed": -0.066, "brier_diff_model_minus_kalshi": 0.0078}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4554, "model": {"intercept": -0.532, "slope": 0.832, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.21, "slope": 1.08, "slope_se": 0.043}, "mean_extremity_model": 0.1681, "mean_extremity_kalshi": 0.164, "model_brier": 0.2339, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0273, "brier_diff_se": 0.0028, "model_logloss": 0.6644, "kalshi_logloss": 0.596}, "fair_v1": {"n": 4554, "model": {"intercept": -0.419, "slope": 1.037, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.284, "slope": 1.112, "slope_se": 0.043}, "mean_extremity_model": 0.1684, "mean_extremity_kalshi": 0.1632, "model_brier": 0.2144, "kalshi_brier": 0.2068, "brier_diff_model_minus_kalshi": 0.0076, "brier_diff_se": 0.0023, "model_logloss": 0.6177, "kalshi_logloss": 0.5964}, "gen1_elo": {"n": 4554, "model": {"intercept": -0.394, "slope": 1.009, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.306, "slope": 1.109, "slope_se": 0.043}, "mean_extremity_model": 0.1751, "mean_extremity_kalshi": 0.1634, "model_brier": 0.2133, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0064, "brier_diff_se": 0.0023, "model_logloss": 0.6162, "kalshi_logloss": 0.5968}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2471, "share_ge_15": 0.4447, "median_abs_gap": 13.12, "n": 31745}, "gen1_elo": {"share_ge_25": 0.2451, "share_ge_15": 0.4441, "median_abs_gap": 13.0, "n": 31745}, "gen1_sr": {"share_ge_25": 0.3149, "share_ge_15": 0.5224, "median_abs_gap": 15.96, "n": 31745}, "gen2": {"share_ge_25": 0.3185, "share_ge_15": 0.5131, "median_abs_gap": 15.56, "n": 31745}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1546, "share_ge_15": 0.3603, "median_abs_gap": 10.91, "n": 24661}, "gen1_elo": {"share_ge_25": 0.1556, "share_ge_15": 0.3585, "median_abs_gap": 10.71, "n": 24658}, "gen1_sr": {"share_ge_25": 0.2215, "share_ge_15": 0.4439, "median_abs_gap": 13.03, "n": 24662}, "gen2": {"share_ge_25": 0.2379, "share_ge_15": 0.4445, "median_abs_gap": 13.03, "n": 24663}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.92, "share_ge_25_all": 0.0441, "share_ge_25_pregame_clean": 0.0392}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0538, "share_ge_25_pregame_clean": 0.0488}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2339, "share_within_10pp_all": 0.4325, "share_within_10pp_pregame_clean": 0.4848, "corr_model_vs_mid_pregame_clean": 0.8429}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 668, "model_brier": 0.2018, "kalshi_brier": 0.2026, "brier_diff_model_minus_kalshi": -0.0008}, "10-15": {"n_settled": 792, "model_brier": 0.215, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0085}, "15-25": {"n_settled": 1031, "model_brier": 0.2258, "kalshi_brier": 0.2133, "brier_diff_model_minus_kalshi": 0.0125}, "25-40": {"n_settled": 589, "model_brier": 0.2219, "kalshi_brier": 0.2104, "brier_diff_model_minus_kalshi": 0.0116}, "3-5": {"n_settled": 420, "model_brier": 0.2059, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0008}, "40+": {"n_settled": 116, "model_brier": 0.2743, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0723}, "5-10": {"n_settled": 938, "model_brier": 0.2018, "kalshi_brier": 0.2017, "brier_diff_model_minus_kalshi": 0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.532, "slope": 0.832, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.21, "slope": 1.08, "slope_se": 0.043}, "n": 4554}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.501, "slope": 0.862, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.157, "slope": 1.065, "slope_se": 0.034}, "n": 6633}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 437, "model_brier": 0.3106, "kalshi_brier": 0.2361, "brier_diff_model_minus_kalshi": 0.0746, "brier_diff_se": 0.0144, "corr_model_outcome": 0.0381, "corr_kalshi_outcome": 0.2506}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
