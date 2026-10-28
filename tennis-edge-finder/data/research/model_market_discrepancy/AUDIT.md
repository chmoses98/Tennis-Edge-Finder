# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-28T18:23Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 65,760): 0-3 14.2%, 3-5 9.6%, 5-10 20.0%, 10-15 15.3%, 15-25 19.0%, 25-40 13.9%, 40+ 8.0%; median gap 11.87 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.5%, Challenger 11.2%, doubles 6.4%). Main tour: ATP 4.3% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 14,388): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.3%, STALE_QUOTE 18.9%, BOOK_QUALITY 18.7%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.3%, market_freshness 18.9%, execution 18.7%, data 12.9%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 14,388 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.7% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 453.0 points vs 1658.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.017, Gen-2 0.804, Gen-1 ledger 0.852 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 692 model 0.2239 vs Kalshi 0.2073; n 143 model 0.2752 vs Kalshi 0.1915.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 281,901 model-market comparisons (459,211 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 94,460 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-28T18:05:39.586085+00:00'], shadow board 75,132 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-28T18:05:44.596202+00:00'], Model 4 35,680 rows, 22,871 settled tickers, 8,300 tickers with an external scan.
* By model: {"gen1_ledger": 63755, "gen1_elo": 37770, "fair_v1": 37770, "gen2": 37770, "gen1_sr": 37770, "model4_fundamental": 33555, "model4_conditioned": 33511}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 65,760 | 14.2 | 9.6 | 20.0 | 15.3 | 19.0 | 13.9 | 8.0 | 11.87 | 40.9% | 21.9% |
| MW fair_v1 | 37,770 | 13.1 | 8.8 | 18.6 | 15.4 | 19.4 | 15.0 | 9.7 | 13.0 | 44.2% | 24.8% |
| MW gen1_elo | 37,770 | 12.7 | 8.6 | 19.3 | 15.4 | 19.5 | 14.9 | 9.7 | 12.9 | 44.0% | 24.5% |
| MW gen1_ledger | 27,990 | 15.7 | 10.7 | 21.9 | 15.2 | 18.5 | 12.4 | 5.6 | 10.41 | 36.5% | 18.0% |
| MW gen1_sr | 37,770 | 10.2 | 7.2 | 16.8 | 13.7 | 20.7 | 18.7 | 12.7 | 15.9 | 52.1% | 31.4% |
| MW gen2 | 37,770 | 11.1 | 7.5 | 16.4 | 13.8 | 19.4 | 17.9 | 13.8 | 15.48 | 51.1% | 31.7% |
| all families model4_conditioned | 33,511 | 22.2 | 18.2 | 34.4 | 17.3 | 4.9 | 1.9 | 1.1 | 6.02 | 7.9% | 3.0% |
| all families model4_fundamental | 33,555 | 17.3 | 13.2 | 33.9 | 20.3 | 10.2 | 3.6 | 1.4 | 7.72 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.2%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.27pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,335 | 27.1 | 15.6 | 27.4 | 13.5 | 11.7 | 4.1 | 0.6 | 5.92 | 16.4% | 4.7% |
| CHALLENGER | 5,773 | 16.2 | 9.8 | 20.6 | 15.4 | 15.4 | 11.9 | 10.7 | 10.94 | 38.0% | 22.6% |
| ITF_MEN | 10,421 | 10.0 | 7.3 | 16.8 | 15.2 | 21.0 | 17.7 | 12.1 | 15.22 | 50.7% | 29.7% |
| ITF_WOMEN | 14,811 | 9.8 | 7.1 | 15.9 | 15.0 | 22.0 | 18.3 | 11.8 | 15.65 | 52.2% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,382 | 18.1 | 13.8 | 24.4 | 20.2 | 16.3 | 6.5 | 0.7 | 8.25 | 23.5% | 7.3% |
| WTA125 | 1,042 | 16.0 | 7.6 | 22.6 | 19.3 | 20.2 | 12.6 | 1.6 | 10.7 | 34.4% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,335 | 25.8 | 15.5 | 25.3 | 16.4 | 12.1 | 4.1 | 0.8 | 6.23 | 17.0% | 5.0% |
| CHALLENGER | 5,773 | 15.1 | 8.9 | 18.1 | 14.5 | 18.1 | 13.7 | 11.6 | 12.65 | 43.4% | 25.3% |
| ITF_MEN | 10,421 | 7.9 | 6.1 | 14.8 | 13.6 | 19.7 | 20.7 | 17.2 | 18.15 | 57.6% | 37.9% |
| ITF_WOMEN | 14,811 | 8.0 | 5.7 | 14.1 | 12.7 | 20.6 | 21.4 | 17.4 | 19.2 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,382 | 15.1 | 10.9 | 21.9 | 15.6 | 22.2 | 12.8 | 1.6 | 10.64 | 36.6% | 14.4% |
| WTA125 | 1,042 | 9.4 | 6.3 | 16.2 | 16.7 | 24.6 | 17.9 | 8.8 | 15.57 | 51.3% | 26.8% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,335 | 22.4 | 13.0 | 24.4 | 16.0 | 16.2 | 6.6 | 1.4 | 7.58 | 24.1% | 8.0% |
| CHALLENGER | 5,773 | 15.0 | 9.3 | 21.2 | 15.8 | 15.6 | 12.3 | 10.9 | 11.2 | 38.8% | 23.2% |
| ITF_MEN | 10,421 | 9.4 | 7.1 | 17.2 | 14.3 | 21.6 | 18.1 | 12.3 | 15.75 | 52.0% | 30.4% |
| ITF_WOMEN | 14,811 | 9.6 | 6.8 | 16.3 | 15.8 | 22.2 | 18.1 | 11.2 | 15.49 | 51.4% | 29.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,382 | 23.7 | 16.5 | 31.7 | 14.8 | 9.5 | 2.6 | 1.2 | 6.08 | 13.4% | 3.8% |
| WTA125 | 1,042 | 22.2 | 12.9 | 26.7 | 16.7 | 14.9 | 6.3 | 0.4 | 7.96 | 21.6% | 6.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,931 | 24.6 | 19.1 | 30.9 | 12.8 | 9.0 | 3.1 | 0.5 | 5.67 | 12.6% | 3.6% |
| CHALLENGER | 3,929 | 22.5 | 14.6 | 26.9 | 14.7 | 13.8 | 6.1 | 1.6 | 7.16 | 21.4% | 7.6% |
| DOUBLES | 2,000 | 5.1 | 4.5 | 12.3 | 10.4 | 21.2 | 25.1 | 21.3 | 23.54 | 67.5% | 46.4% |
| ITF_MEN | 8,005 | 13.1 | 9.3 | 20.9 | 15.8 | 21.4 | 13.3 | 6.1 | 12.04 | 40.8% | 19.4% |
| ITF_WOMEN | 9,508 | 13.1 | 9.0 | 19.6 | 15.6 | 21.3 | 15.6 | 5.8 | 12.49 | 42.7% | 21.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,412 | 24.4 | 15.4 | 29.8 | 17.9 | 9.3 | 2.8 | 0.3 | 6.76 | 12.5% | 3.1% |
| WTA125 | 1,056 | 24.7 | 12.5 | 21.1 | 19.3 | 13.2 | 7.5 | 1.7 | 7.92 | 22.4% | 9.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,241 | 27.5 | 15.7 | 27.7 | 13.4 | 11.5 | 3.8 | 0.4 | 5.86 | 15.7% | 4.2% |
| CHALLENGER | 4,057 | 21.1 | 12.3 | 25.7 | 17.9 | 15.1 | 6.2 | 1.5 | 8.06 | 22.9% | 7.8% |
| ITF_MEN | 7,698 | 12.1 | 8.8 | 20.1 | 17.2 | 21.9 | 14.5 | 5.4 | 12.48 | 41.8% | 19.9% |
| ITF_WOMEN | 11,119 | 11.7 | 8.4 | 18.2 | 17.2 | 23.9 | 15.3 | 5.3 | 13.37 | 44.5% | 20.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,308 | 18.3 | 13.7 | 24.6 | 20.4 | 16.3 | 6.1 | 0.6 | 8.23 | 23.0% | 6.6% |
| WTA125 | 1,006 | 16.3 | 7.5 | 22.2 | 19.6 | 20.8 | 12.3 | 1.4 | 10.97 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,241 | 26.0 | 15.8 | 25.4 | 16.4 | 12.0 | 3.9 | 0.5 | 6.2 | 16.3% | 4.3% |
| CHALLENGER | 4,057 | 19.4 | 11.3 | 22.7 | 17.0 | 18.4 | 9.3 | 1.9 | 9.08 | 29.6% | 11.2% |
| ITF_MEN | 7,699 | 9.3 | 7.2 | 17.1 | 15.8 | 21.5 | 18.9 | 10.2 | 15.24 | 50.6% | 29.1% |
| ITF_WOMEN | 11,120 | 8.9 | 6.6 | 15.8 | 14.1 | 22.7 | 20.9 | 10.9 | 16.79 | 54.6% | 31.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,308 | 15.2 | 10.9 | 22.0 | 15.6 | 22.3 | 12.7 | 1.3 | 10.59 | 36.3% | 14.0% |
| WTA125 | 1,006 | 9.4 | 6.4 | 16.3 | 16.9 | 24.4 | 18.3 | 8.2 | 15.37 | 51.0% | 26.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,877 | 24.7 | 19.3 | 30.9 | 13.0 | 8.7 | 2.9 | 0.4 | 5.66 | 12.0% | 3.4% |
| CHALLENGER | 3,462 | 23.9 | 15.5 | 28.1 | 14.8 | 13.1 | 4.2 | 0.4 | 6.6 | 17.7% | 4.6% |
| DOUBLES | 1,873 | 5.0 | 4.6 | 12.6 | 10.6 | 21.1 | 24.9 | 21.1 | 23.41 | 67.1% | 46.0% |
| ITF_MEN | 6,826 | 14.0 | 9.9 | 22.6 | 16.4 | 21.4 | 11.8 | 4.0 | 11.04 | 37.1% | 15.8% |
| ITF_WOMEN | 8,069 | 13.8 | 9.5 | 20.9 | 16.2 | 21.4 | 14.6 | 3.6 | 11.64 | 39.6% | 18.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,358 | 24.8 | 15.8 | 29.8 | 18.0 | 9.3 | 2.2 | 0.1 | 6.59 | 11.6% | 2.3% |
| WTA125 | 933 | 26.1 | 13.3 | 22.2 | 20.6 | 12.0 | 5.2 | 0.5 | 7.35 | 17.8% | 5.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,000 | 5.1 | 4.5 | 12.3 | 10.4 | 21.2 | 25.1 | 21.3 | 23.54 | 67.5% | 46.4% |
| singles | 25,990 | 16.5 | 11.2 | 22.7 | 15.6 | 18.2 | 11.4 | 4.4 | 9.9 | 34.1% | 15.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,690 | 13.1 | 9.3 | 20.0 | 15.6 | 19.1 | 13.9 | 9.0 | 12.41 | 42.0% | 22.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 24,553 | 13.6 | 8.7 | 18.4 | 15.1 | 19.2 | 15.2 | 9.7 | 12.95 | 44.1% | 24.9% |
| UNKNOWN | 5,278 | 10.7 | 7.8 | 17.1 | 16.7 | 20.8 | 15.9 | 11.1 | 14.09 | 47.8% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,547 | 20.0 | 12.3 | 22.2 | 15.8 | 14.7 | 9.3 | 5.8 | 8.59 | 29.8% | 15.1% |
| B | 4,600 | 12.9 | 8.8 | 19.0 | 16.3 | 19.4 | 12.8 | 10.8 | 12.61 | 43.0% | 23.6% |
| C | 5,346 | 12.3 | 9.0 | 19.9 | 15.8 | 18.5 | 14.4 | 10.2 | 12.71 | 43.0% | 24.5% |
| D | 5,929 | 12.3 | 8.3 | 17.5 | 15.4 | 21.3 | 15.8 | 9.4 | 13.67 | 46.5% | 25.2% |
| F | 11,348 | 7.5 | 5.6 | 15.0 | 14.6 | 23.2 | 21.1 | 13.0 | 17.8 | 57.3% | 34.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,499 | 24.2 | 15.8 | 28.5 | 15.3 | 11.0 | 3.8 | 1.4 | 6.52 | 16.2% | 5.2% |
| B | 3,854 | 16.9 | 10.2 | 24.2 | 16.3 | 19.1 | 10.0 | 3.3 | 9.72 | 32.4% | 13.3% |
| C | 5,434 | 11.3 | 7.9 | 19.4 | 14.6 | 21.2 | 15.5 | 10.1 | 13.46 | 46.8% | 25.6% |
| D | 4,076 | 14.5 | 10.0 | 21.4 | 15.4 | 20.0 | 13.1 | 5.6 | 11.26 | 38.7% | 18.7% |
| F | 7,127 | 10.0 | 8.3 | 16.0 | 14.9 | 23.0 | 20.0 | 7.9 | 15.44 | 50.8% | 27.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,961 | 18.3 | 11.1 | 21.3 | 15.6 | 15.2 | 10.1 | 8.5 | 9.8 | 33.8% | 18.6% |
| LIMITED | 8,171 | 13.9 | 10.1 | 20.2 | 16.3 | 18.9 | 13.3 | 7.3 | 11.64 | 39.6% | 20.6% |
| POOR | 17,638 | 9.2 | 6.5 | 16.0 | 15.0 | 22.5 | 19.1 | 11.7 | 16.1 | 53.4% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,289 | 24.2 | 18.3 | 33.2 | 14.8 | 6.5 | 2.6 | 0.4 | 5.82 | 9.5% | 3.0% |
| GAME_SPREAD | 5,722 | 22.2 | 15.3 | 32.9 | 17.1 | 9.0 | 2.9 | 0.5 | 6.74 | 12.4% | 3.4% |
| MATCH_WINNER | 27,990 | 15.7 | 10.7 | 21.9 | 15.2 | 18.5 | 12.4 | 5.6 | 10.41 | 36.5% | 18.0% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,226 | 27.5 | 16.6 | 31.3 | 12.5 | 9.5 | 2.4 | 0.3 | 5.69 | 12.2% | 2.7% |
| TOTAL_GAMES | 9,504 | 9.2 | 10.3 | 36.1 | 26.9 | 10.6 | 4.1 | 2.8 | 9.34 | 17.5% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,891 | 24.4 | 30.4 | 32.9 | 7.2 | 4.0 | 0.8 | 0.2 | 4.68 | 5.1% | 1.1% |
| GAME_SPREAD | 7,846 | 47.1 | 16.1 | 25.5 | 7.3 | 2.1 | 1.2 | 0.6 | 3.29 | 3.9% | 1.8% |
| TOTAL_GAMES | 13,774 | 6.2 | 8.9 | 40.6 | 31.7 | 7.2 | 3.1 | 2.2 | 9.36 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,902 | 23.9 | 16.9 | 34.9 | 14.3 | 7.1 | 2.5 | 0.4 | 6.0 | 10.0% | 2.9% |
| GAME_SPREAD | 7,849 | 20.1 | 13.4 | 28.1 | 20.5 | 12.6 | 4.3 | 1.1 | 7.82 | 17.9% | 5.4% |
| TOTAL_GAMES | 13,804 | 9.9 | 10.1 | 36.4 | 25.4 | 11.6 | 4.2 | 2.4 | 9.22 | 18.2% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 37,770 | 44.2% | 24.8% | 13.0 | 35.6% | 15.5% | 10.77 |
| gen1_elo | 37,770 | 44.0% | 24.5% | 12.9 | 35.4% | 15.5% | 10.56 |
| gen1_sr | 37,770 | 52.1% | 31.4% | 15.9 | 44.4% | 22.1% | 13.06 |
| gen2 | 37,770 | 51.1% | 31.7% | 15.48 | 44.3% | 23.7% | 12.99 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,199 | 15.6 | 10.6 | 21.3 | 17.2 | 20.0 | 12.0 | 3.4 | 10.71 | 35.4% | 15.4% |
| STALE | 19,571 | 10.7 | 7.1 | 16.1 | 13.8 | 18.9 | 17.8 | 15.7 | 16.02 | 52.4% | 33.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 21,458 | 16.4 | 11.1 | 22.6 | 15.3 | 17.9 | 11.9 | 4.8 | 9.96 | 34.5% | 16.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 65,760 | 21458 | 21671 | 22631 | 24.2 | 115.5 | 1400.4 |
| ge_15pp | 26,893 | 7409 | 7724 | 11760 | 26.7 | 419.7 | 1399.2 |
| ge_25pp | 14,388 | 3578 | 3391 | 7419 | 31.4 | 571.5 | 1380.4 |
| lt_10pp | 28,782 | 10758 | 10268 | 7756 | 22.4 | 46.9 | 1341.5 |

Current slate `SL-20261028T182308Z-6c1d9f4e`: 590 priced rows, quote age at build {'median': 17.9, 'max': 18.0}, freshness {'AGING': 590}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 43 | 0.0 | 0.0 | 32.6 | 7.0 | 34.9 | 23.3 | 2.3 | 20.19 | 60.5% | 25.6% |
| EXTERNAL_LONE_OUTLIER | 23 | 69.6 | 30.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,717 | 20.0 | 11.2 | 25.0 | 18.0 | 17.8 | 7.2 | 0.9 | 8.63 | 25.8% | 8.0% |
| KALSHI_LONE_OUTLIER | 26 | 3.9 | 3.9 | 76.9 | 7.7 | 3.9 | 3.9 | 0.0 | 6.31 | 7.7% | 3.9% |
| MARKETS_AGREE | 737 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.26 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,575 | 0.0 | 2.5 | 35.8 | 26.0 | 24.4 | 10.4 | 0.8 | 12.12 | 35.7% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 37,770 | 6121 (16.2%) | 25.7% | 1.1% | {"EXTERNAL_STALE": 3717, "AGREES_WITH_KALSHI": 1575, "ALL_AGREE": 737, "SUPPORTS_MODEL_DIRECTION": 42, "AGREES_WITH_MODEL": 26, "EXTERNAL_OUTLIER": 23, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 16,685 | 1549 (9.3%) | 36.3% | 1.8% | {"EXTERNAL_STALE": 959, "AGREES_WITH_KALSHI": 562, "SUPPORTS_MODEL_DIRECTION": 26, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,348 | 488 (5.2%) | 36.3% | 2.5% | {"EXTERNAL_STALE": 299, "AGREES_WITH_KALSHI": 177, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,564 | 463 (10.1%) | 36.7% | 2.6% | {"EXTERNAL_STALE": 281, "AGREES_WITH_KALSHI": 170, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 15,255 | 3487 (22.9%) | 17.3% | 1.0% | {"EXTERNAL_STALE": 2088, "ALL_AGREE": 737, "AGREES_WITH_KALSHI": 603, "EXTERNAL_OUTLIER": 23, "AGREES_WITH_MODEL": 22, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,385 | 10.6 | 7.4 | 19.7 | 14.4 | 21.5 | 16.6 | 9.8 | 14.03 | 47.9% | 26.4% |
| 4-10x | 5,056 | 11.4 | 8.6 | 18.4 | 15.4 | 21.7 | 14.6 | 9.8 | 13.57 | 46.1% | 24.5% |
| <2x | 19,112 | 15.2 | 10.1 | 19.3 | 16.2 | 17.4 | 13.1 | 8.8 | 11.57 | 39.2% | 21.9% |
| >=10x | 6,217 | 10.7 | 6.4 | 15.1 | 14.5 | 21.5 | 19.2 | 12.7 | 16.24 | 53.3% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,536 | 12.9 | 8.6 | 19.5 | 16.2 | 19.0 | 13.6 | 10.3 | 12.69 | 42.9% | 23.9% |
| 300-1000 | 8,094 | 12.3 | 8.8 | 17.7 | 15.3 | 20.1 | 16.3 | 9.4 | 13.49 | 45.9% | 25.8% |
| <300 | 12,357 | 8.4 | 5.8 | 15.2 | 14.8 | 22.9 | 20.1 | 12.8 | 17.05 | 55.8% | 32.9% |
| >=3000 | 7,783 | 21.5 | 13.4 | 23.8 | 15.7 | 13.8 | 7.2 | 4.6 | 7.57 | 25.6% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1063 | 0.5475 | 0.409 | 0.4967 | +0.051 | -0.088 | -0.0024 ± 0.0047 |
| ratio 4-10x | 727 | 0.5812 | 0.4357 | 0.4952 | +0.086 | -0.059 | 0.0093 ± 0.0059 |
| ratio <2x | 2581 | 0.5375 | 0.4135 | 0.4502 | +0.087 | -0.037 | 0.0107 ± 0.0029 |
| ratio >=10x | 940 | 0.5666 | 0.3917 | 0.4468 | +0.120 | -0.055 | 0.0135 ± 0.0059 |
| thinner_sample 1000-3000 | 1423 | 0.538 | 0.4108 | 0.4533 | +0.085 | -0.042 | 0.0077 ± 0.0038 |
| thinner_sample 300-1000 | 1195 | 0.5679 | 0.4256 | 0.4895 | +0.078 | -0.064 | 0.0026 ± 0.0046 |
| thinner_sample <300 | 1810 | 0.558 | 0.3903 | 0.4586 | +0.099 | -0.068 | 0.0106 ± 0.0042 |
| thinner_sample >=3000 | 883 | 0.5325 | 0.4385 | 0.4643 | +0.068 | -0.026 | 0.0129 ± 0.0039 |
| data_status ADEQUATE | 1471 | 0.534 | 0.4303 | 0.448 | +0.086 | -0.018 | 0.013 ± 0.0032 |
| data_status LIMITED | 1254 | 0.5488 | 0.4156 | 0.4848 | +0.064 | -0.069 | 0.003 ± 0.0042 |
| data_status POOR | 2586 | 0.561 | 0.3994 | 0.4652 | +0.096 | -0.066 | 0.0084 ± 0.0034 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 782 | 0.199 | 0.1996 | -0.0006 ± 0.0006 | 0.5775 | 0.5788 | 0.5032 | 0.4881 | 0.5115 | -0.085 ± 0.017 | -0.01 (5) |
| 3-5 | 477 | 0.2057 | 0.2064 | -0.0007 ± 0.0017 | 0.595 | 0.5952 | 0.5049 | 0.465 | 0.4927 | -0.092 ± 0.0213 | 0.02 (1) |
| 5-10 | 1106 | 0.2015 | 0.2016 | -0.0002 ± 0.002 | 0.5885 | 0.5865 | 0.5096 | 0.4357 | 0.4711 | -0.089 ± 0.014 | -0.0167 (6) |
| 10-15 | 932 | 0.2221 | 0.2136 | +0.0085 ± 0.0038 | 0.6372 | 0.6136 | 0.5268 | 0.4031 | 0.4292 | -0.107 ± 0.0153 | -0.048 (5) |
| 15-25 | 1179 | 0.2246 | 0.2126 | +0.0120 ± 0.0052 | 0.6447 | 0.6097 | 0.574 | 0.3783 | 0.4461 | -0.096 ± 0.0135 | -0.0033 (9) |
| 25-40 | 692 | 0.2239 | 0.2073 | +0.0166 ± 0.0103 | 0.6379 | 0.5964 | 0.6546 | 0.3444 | 0.4725 | -0.074 ± 0.0159 | -0.01 (1) |
| 40+ | 143 | 0.2752 | 0.1915 | +0.0836 ± 0.0318 | 0.7497 | 0.5632 | 0.7392 | 0.2903 | 0.4266 | -0.064 ± 0.0311 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4134 | 0.1823 | 0.183 | -0.0007 ± 0.0002 | 0.5392 | 0.5399 | 0.4858 | 0.4705 | 0.4952 | -0.030 ± 0.0068 | -0.0129 (17) |
| 3-5 | 2789 | 0.1951 | 0.1933 | +0.0017 ± 0.0007 | 0.5693 | 0.5628 | 0.4829 | 0.4431 | 0.4403 | -0.058 ± 0.0084 | 0.0 (2) |
| 5-10 | 5941 | 0.2021 | 0.1985 | +0.0036 ± 0.0009 | 0.5897 | 0.577 | 0.4831 | 0.4093 | 0.4222 | -0.048 ± 0.0058 | -0.0119 (21) |
| 10-15 | 5025 | 0.2026 | 0.1868 | +0.0158 ± 0.0015 | 0.5918 | 0.549 | 0.4835 | 0.3593 | 0.3572 | -0.066 ± 0.0061 | -0.0281 (16) |
| 15-25 | 6202 | 0.2083 | 0.1697 | +0.0386 ± 0.0021 | 0.6096 | 0.5029 | 0.4996 | 0.3031 | 0.3036 | -0.071 ± 0.0052 | -0.0025 (44) |
| 25-40 | 4990 | 0.2224 | 0.1255 | +0.0970 ± 0.0031 | 0.639 | 0.3858 | 0.5268 | 0.213 | 0.2198 | -0.060 ± 0.0049 | -0.01 (1) |
| 40+ | 3192 | 0.3801 | 0.0449 | +0.3352 ± 0.0043 | 0.9895 | 0.1735 | 0.6303 | 0.1031 | 0.0617 | -0.076 ± 0.0035 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 605 | 0.207 | 0.2077 | -0.0007 ± 0.0006 | 0.5959 | 0.5979 | 0.5099 | 0.4948 | 0.5207 | -0.105 ± 0.0201 | -0.01 (3) |
| 3-5 | 431 | 0.2251 | 0.2222 | +0.0029 ± 0.0018 | 0.6363 | 0.6304 | 0.5141 | 0.4743 | 0.4524 | -0.137 ± 0.0242 | 0.02 (1) |
| 5-10 | 961 | 0.2079 | 0.2073 | +0.0005 ± 0.0022 | 0.6014 | 0.5997 | 0.5487 | 0.4738 | 0.5099 | -0.086 ± 0.0152 | -0.01 (4) |
| 10-15 | 871 | 0.2175 | 0.2107 | +0.0068 ± 0.0039 | 0.6261 | 0.6084 | 0.5637 | 0.4394 | 0.4765 | -0.109 ± 0.0162 | -0.04 (5) |
| 15-25 | 1235 | 0.2297 | 0.2142 | +0.0155 ± 0.0051 | 0.6538 | 0.613 | 0.5814 | 0.386 | 0.447 | -0.096 ± 0.0134 | -0.0133 (9) |
| 25-40 | 880 | 0.2683 | 0.1974 | +0.0709 ± 0.0094 | 0.7492 | 0.5756 | 0.6543 | 0.3404 | 0.3875 | -0.128 ± 0.015 | -0.0075 (4) |
| 40+ | 328 | 0.361 | 0.1667 | +0.1943 ± 0.0223 | 0.9875 | 0.5005 | 0.7308 | 0.2457 | 0.3018 | -0.079 ± 0.0218 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3531 | 0.1909 | 0.1912 | -0.0003 ± 0.0003 | 0.5577 | 0.5581 | 0.5075 | 0.4925 | 0.5061 | -0.044 ± 0.0076 | -0.0133 (15) |
| 3-5 | 2397 | 0.1973 | 0.1961 | +0.0012 ± 0.0007 | 0.5719 | 0.5687 | 0.5158 | 0.4761 | 0.4793 | -0.051 ± 0.0093 | 0.02 (1) |
| 5-10 | 5248 | 0.1984 | 0.1947 | +0.0037 ± 0.0009 | 0.5821 | 0.5683 | 0.5147 | 0.4405 | 0.456 | -0.044 ± 0.0062 | -0.0117 (6) |
| 10-15 | 4495 | 0.2059 | 0.1937 | +0.0122 ± 0.0016 | 0.602 | 0.565 | 0.5118 | 0.3879 | 0.4016 | -0.054 ± 0.0067 | -0.0189 (18) |
| 15-25 | 6251 | 0.2182 | 0.1816 | +0.0366 ± 0.0021 | 0.6339 | 0.5328 | 0.5219 | 0.3264 | 0.334 | -0.064 ± 0.0054 | -0.0086 (42) |
| 25-40 | 5793 | 0.2515 | 0.1364 | +0.1151 ± 0.0031 | 0.7087 | 0.4184 | 0.5563 | 0.2398 | 0.2192 | -0.086 ± 0.0048 | -0.0044 (18) |
| 40+ | 4558 | 0.3954 | 0.0591 | +0.3364 ± 0.0041 | 1.0408 | 0.2126 | 0.6502 | 0.1174 | 0.0816 | -0.072 ± 0.0035 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 749 | 0.1973 | 0.1995 | -0.0021 ± 0.0006 | 0.574 | 0.5793 | 0.5009 | 0.4856 | 0.5447 | -0.039 ± 0.017 | -0.0137 (8) |
| 3-5 | 519 | 0.2031 | 0.2014 | +0.0016 ± 0.0016 | 0.5889 | 0.5828 | 0.4965 | 0.4568 | 0.4586 | -0.119 ± 0.0205 | 0.0067 (3) |
| 5-10 | 1144 | 0.2033 | 0.2014 | +0.0019 ± 0.002 | 0.5924 | 0.5858 | 0.5078 | 0.434 | 0.458 | -0.096 ± 0.0136 | -0.0071 (7) |
| 10-15 | 926 | 0.211 | 0.2066 | +0.0044 ± 0.0037 | 0.6121 | 0.5978 | 0.5375 | 0.4143 | 0.459 | -0.094 ± 0.015 | -0.0317 (6) |
| 15-25 | 1115 | 0.2321 | 0.2165 | +0.0156 ± 0.0054 | 0.662 | 0.6183 | 0.5862 | 0.3917 | 0.4493 | -0.107 ± 0.014 | -0.03 (1) |
| 25-40 | 704 | 0.2145 | 0.2142 | +0.0003 ± 0.0102 | 0.6185 | 0.6124 | 0.6631 | 0.3524 | 0.5057 | -0.059 ± 0.0158 | 0.015 (2) |
| 40+ | 154 | 0.292 | 0.1999 | +0.0922 ± 0.0315 | 0.7982 | 0.5818 | 0.7481 | 0.2977 | 0.4286 | -0.066 ± 0.0328 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4039 | 0.1844 | 0.185 | -0.0006 ± 0.0002 | 0.5429 | 0.5439 | 0.4837 | 0.4685 | 0.485 | -0.035 ± 0.0068 | -0.0163 (35) |
| 3-5 | 2732 | 0.2003 | 0.1985 | +0.0018 ± 0.0007 | 0.5834 | 0.577 | 0.4827 | 0.4431 | 0.4418 | -0.059 ± 0.0087 | -0.0094 (18) |
| 5-10 | 6113 | 0.1943 | 0.19 | +0.0043 ± 0.0008 | 0.5717 | 0.5566 | 0.4832 | 0.4091 | 0.417 | -0.051 ± 0.0056 | -0.01 (31) |
| 10-15 | 4951 | 0.1924 | 0.1788 | +0.0137 ± 0.0015 | 0.5686 | 0.5301 | 0.494 | 0.3706 | 0.3765 | -0.058 ± 0.006 | -0.015 (12) |
| 15-25 | 6333 | 0.2132 | 0.1745 | +0.0387 ± 0.0021 | 0.6205 | 0.5137 | 0.5109 | 0.3158 | 0.3152 | -0.071 ± 0.0052 | -0.03 (2) |
| 25-40 | 4935 | 0.2182 | 0.1287 | +0.0895 ± 0.0032 | 0.6304 | 0.3927 | 0.5293 | 0.2136 | 0.232 | -0.051 ± 0.0049 | 0.01 (3) |
| 40+ | 3170 | 0.3923 | 0.0505 | +0.3418 ± 0.0045 | 1.0238 | 0.1883 | 0.6413 | 0.1108 | 0.0678 | -0.078 ± 0.0038 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1142 | 0.1958 | 0.1959 | -0.0001 ± 0.0005 | 0.5704 | 0.5705 | 0.5062 | 0.4911 | 0.4965 | -0.067 ± 0.0133 | -0.0224 (49) |
| 3-5 | 794 | 0.1892 | 0.1887 | +0.0005 ± 0.0012 | 0.5541 | 0.552 | 0.4952 | 0.4554 | 0.4673 | -0.062 ± 0.0158 | -0.0194 (34) |
| 5-10 | 1668 | 0.2019 | 0.1971 | +0.0048 ± 0.0016 | 0.5934 | 0.5778 | 0.4996 | 0.426 | 0.4311 | -0.073 ± 0.0111 | -0.005 (78) |
| 10-15 | 1138 | 0.2153 | 0.2036 | +0.0117 ± 0.0033 | 0.6226 | 0.5913 | 0.5326 | 0.4099 | 0.4218 | -0.081 ± 0.0137 | 0.0014 (64) |
| 15-25 | 1464 | 0.2322 | 0.2117 | +0.0205 ± 0.0047 | 0.6616 | 0.6084 | 0.5795 | 0.3847 | 0.4317 | -0.080 ± 0.0121 | -0.0214 (59) |
| 25-40 | 917 | 0.2431 | 0.2098 | +0.0333 ± 0.0093 | 0.6954 | 0.6014 | 0.6804 | 0.3684 | 0.4711 | -0.089 ± 0.0142 | -0.0219 (26) |
| 40+ | 305 | 0.342 | 0.2012 | +0.1408 ± 0.0249 | 0.9875 | 0.5874 | 0.8101 | 0.332 | 0.4393 | -0.100 ± 0.0233 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4116 | 0.1763 | 0.1765 | -0.0002 ± 0.0002 | 0.5224 | 0.5226 | 0.5099 | 0.4947 | 0.5061 | -0.038 ± 0.0066 | -0.0157 (88) |
| 3-5 | 2808 | 0.1945 | 0.193 | +0.0015 ± 0.0007 | 0.5659 | 0.5628 | 0.5036 | 0.4637 | 0.4647 | -0.051 ± 0.0084 | -0.0209 (69) |
| 5-10 | 5731 | 0.1987 | 0.1913 | +0.0074 ± 0.0009 | 0.5849 | 0.563 | 0.4967 | 0.423 | 0.4111 | -0.069 ± 0.0058 | -0.0082 (132) |
| 10-15 | 4029 | 0.2124 | 0.1968 | +0.0156 ± 0.0017 | 0.6162 | 0.5753 | 0.5294 | 0.4065 | 0.4038 | -0.068 ± 0.0071 | -0.0053 (105) |
| 15-25 | 4886 | 0.2296 | 0.201 | +0.0286 ± 0.0025 | 0.6609 | 0.5812 | 0.5648 | 0.3694 | 0.3948 | -0.062 ± 0.0064 | -0.0253 (107) |
| 25-40 | 3320 | 0.2595 | 0.1859 | +0.0736 ± 0.0047 | 0.7354 | 0.5427 | 0.6337 | 0.3207 | 0.3623 | -0.078 ± 0.0073 | -0.0229 (51) |
| 40+ | 1438 | 0.3772 | 0.1507 | +0.2264 ± 0.0106 | 1.066 | 0.4524 | 0.7339 | 0.2331 | 0.2684 | -0.076 ± 0.0097 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5311 | 1.017 ± 0.038 | 1.087 | 0.1682 | 0.1662 | 0.2151 | 0.2067 |
| gen2 | 5311 | 0.804 ± 0.035 | 1.045 | 0.1698 | 0.1666 | 0.2353 | 0.2066 |
| gen1_elo | 5311 | 0.994 ± 0.037 | 1.086 | 0.1747 | 0.1664 | 0.2139 | 0.2069 |
| gen1_sr | 5311 | 0.981 ± 0.046 | 1.106 | 0.1302 | 0.1686 | 0.2311 | 0.2062 |
| gen1_ledger | 7428 | 0.852 ± 0.027 | 1.051 | 0.186 | 0.177 | 0.2185 | 0.2016 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 26,893)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,926 | 22.0% |
| STALE_QUOTE | market_freshness | 5,882 | 21.9% |
| BOOK_QUALITY | execution | 5,177 | 19.2% |
| POOR_DATA | data | 3,162 | 11.8% |
| LIMITED_DATA | data | 1,662 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,516 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,208 | 4.5% |
| IDENTITY_AMBIGUOUS | mapping | 1,107 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 790 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 462 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.0%, market_freshness 21.9%, execution 19.2%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.5%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.8%, THIN_PLAYER_HISTORY 60.8%, STALE_PLAYER_DATA 52.4%, STALE_KALSHI_QUOTE 43.7%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.2%, MODEL_HIGH_UNCERTAINTY 17.7%, PLAYER_IDENTITY_RISK 15.8%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.6%, POST_SETTLEMENT_OBSERVATION 22.0%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 14,388)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,790 | 33.3% |
| STALE_QUOTE | market_freshness | 2,721 | 18.9% |
| BOOK_QUALITY | execution | 2,697 | 18.7% |
| POOR_DATA | data | 1,354 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 803 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 589 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 509 | 3.5% |
| LIMITED_DATA | data | 497 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 308 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 119 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.3%, market_freshness 18.9%, execution 18.7%, data 12.9%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 63.1%, STALE_KALSHI_QUOTE 51.6%, STALE_PLAYER_DATA 46.8%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.6%, PLAYER_IDENTITY_RISK 18.6%, MODEL_HIGH_UNCERTAINTY 18.4%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.5%, POST_SETTLEMENT_OBSERVATION 33.3%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 11389, "IDENTITY_AMBIGUOUS": 2999}; ticker orientation: {"VERIFIED": 14388}.

Checks: discipline:AMBIGUOUS 927, discipline:PASS 13461, identity_confidence:AMBIGUOUS 2683, identity_confidence:PASS 11705, level_mapping:NA 939, level_mapping:PASS 13449, market_pair:AMBIGUOUS 475, market_pair:NA 339, market_pair:PASS 13574, model_complement:NA 303, model_complement:PASS 14085, namesake:AMBIGUOUS 6, namesake:PASS 14382, physical_match_id:NA 5040, physical_match_id:PASS 9348, player_ids:PASS 14388, same_pair_other_event:PASS 14388, ticker_orientation:PASS 14388

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,266 | 4.3% | 3.9% | 1.6% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 16, "coverage": 13} | 5.82 | 0.2198 / 0.2166 (597) | 21.4% | 3.0% | 3.3% | 2.8% |
| CHALLENGER | 9,702 | 16.5% | 6.3% | 11.2% | {"coverage": 938, "market_freshness/coverage": 193, "market_freshness": 166, "data": 144, "model_calibration_or_unknown": 75, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.29 | 0.2195 / 0.2106 (2215) | 35.1% | 15.9% | 4.1% | 22.5% |
| DOUBLES | 2,000 | 46.4% | 46.0% | 6.4% | {"execution": 524, "mapping": 232, "market_freshness": 106, "market_freshness/coverage": 58, "coverage": 7} | 23.41 | 0.311 / 0.2376 (476) | 11.7% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 18,426 | 25.3% | 18.0% | 32.4% | {"coverage": 1605, "execution": 887, "market_freshness": 850, "data": 680, "market_freshness/coverage": 440, "mapping": 184, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.8 | 0.2166 / 0.2 (3790) | 37.0% | 70.5% | 17.3% | 21.2% |
| ITF_WOMEN | 24,319 | 26.7% | 19.6% | 45.2% | {"coverage": 2192, "market_freshness": 1400, "execution": 1173, "data": 934, "market_freshness/coverage": 552, "mapping": 150, "model_calibration_or_unknown": 82, "model_calibration": 18} | 12.65 | 0.2052 / 0.1969 (4410) | 39.0% | 58.0% | 10.2% | 21.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,794 | 5.7% | 5.0% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "execution": 27, "coverage": 22, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.58 | 0.2347 / 0.2278 (591) | 25.9% | 1.1% | 1.4% | 3.4% |
| WTA125 | 2,098 | 11.7% | 9.9% | 1.7% | {"market_freshness": 64, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.21 | 0.2091 / 0.1928 (618) | 25.3% | 11.7% | 5.1% | 7.6% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 172 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 6 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 7 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 164 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 8 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 9 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 12 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 13 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 16 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 17 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 18 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 19 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 20 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 21 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 22 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 23 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 24 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 25 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 26 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 27 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 30 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 31 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 32 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 33 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 34 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 35 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 36 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 37 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 39 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 40 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 41 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 42 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 43 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 44 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 46 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 48 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 49 | `KXITFMATCH-26OCT28DELBAR-BAR` | ITF_MEN | fair_v1 | 84% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.5h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 216 min (STALE); data POOR (grade F, thinner serve sample 803.0, ratio 2.48); no external reference |
| 50 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9691, "by_level_share_of_ge_25pp": {"ATP": 0.0158, "CHALLENGER": 0.1116, "DOUBLES": 0.0644, "ITF_MEN": 0.3235, "ITF_WOMEN": 0.4518, "OTHER": 0.0008, "WTA": 0.0151, "WTA125": 0.017}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5156, "share_primary_cause_market_settled_or_in_play": 0.4241, "share_primary_cause_stale_quote_only": 0.1891}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 14388, "identity_ambiguous_share": 0.2084, "ticker_orientation": {"VERIFIED": 14388}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9348, "with_external": 488, "coverage": 0.0522, "external_status": {"EXTERNAL_STALE": 299, "AGREES_WITH_KALSHI": 177, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 299, "MODEL_LONE_OUTLIER": 177, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3627, "share_external_supports_model": 0.0246}, "pregame_clean_ge_25pp": {"n": 4564, "with_external": 463, "coverage": 0.1014, "external_status": {"EXTERNAL_STALE": 281, "AGREES_WITH_KALSHI": 170, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 281, "MODEL_LONE_OUTLIER": 170, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3672, "share_external_supports_model": 0.0259}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 453.0, "median_sample_ratio": 2.5, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.213, "data_status": {"POOR": 8216, "LIMITED": 3654, "ADEQUATE": 2518}, "comparison_lt_10pp": {"median_thinner_serve_points": 1658.0, "median_sample_ratio": 1.73, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1063, "model_minus_observed": 0.0508, "kalshi_minus_observed": -0.0877, "brier_diff_model_minus_kalshi": -0.0024}, "4-10x": {"n": 727, "model_minus_observed": 0.086, "kalshi_minus_observed": -0.0595, "brier_diff_model_minus_kalshi": 0.0093}, "<2x": {"n": 2581, "model_minus_observed": 0.0873, "kalshi_minus_observed": -0.0367, "brier_diff_model_minus_kalshi": 0.0107}, ">=10x": {"n": 940, "model_minus_observed": 0.1198, "kalshi_minus_observed": -0.0551, "brier_diff_model_minus_kalshi": 0.0135}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5311, "model": {"intercept": -0.535, "slope": 0.804, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.191, "slope": 1.045, "slope_se": 0.039}, "mean_extremity_model": 0.1698, "mean_extremity_kalshi": 0.1666, "model_brier": 0.2353, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": 0.0287, "brier_diff_se": 0.0026, "model_logloss": 0.6682, "kalshi_logloss": 0.5964}, "fair_v1": {"n": 5311, "model": {"intercept": -0.409, "slope": 1.017, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.087, "slope_se": 0.039}, "mean_extremity_model": 0.1682, "mean_extremity_kalshi": 0.1662, "model_brier": 0.2151, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.0084, "brier_diff_se": 0.0021, "model_logloss": 0.6193, "kalshi_logloss": 0.5967}, "gen1_elo": {"n": 5311, "model": {"intercept": -0.383, "slope": 0.994, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.308, "slope": 1.086, "slope_se": 0.039}, "mean_extremity_model": 0.1747, "mean_extremity_kalshi": 0.1664, "model_brier": 0.2139, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.007, "brier_diff_se": 0.0022, "model_logloss": 0.6169, "kalshi_logloss": 0.5969}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2475, "share_ge_15": 0.4418, "median_abs_gap": 13.0, "n": 37770}, "gen1_elo": {"share_ge_25": 0.2453, "share_ge_15": 0.4402, "median_abs_gap": 12.9, "n": 37770}, "gen1_sr": {"share_ge_25": 0.3137, "share_ge_15": 0.521, "median_abs_gap": 15.9, "n": 37770}, "gen2": {"share_ge_25": 0.3166, "share_ge_15": 0.5109, "median_abs_gap": 15.48, "n": 37770}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.155, "share_ge_15": 0.3562, "median_abs_gap": 10.77, "n": 29435}, "gen1_elo": {"share_ge_25": 0.1549, "share_ge_15": 0.3538, "median_abs_gap": 10.56, "n": 29434}, "gen1_sr": {"share_ge_25": 0.2213, "share_ge_15": 0.444, "median_abs_gap": 13.06, "n": 29436}, "gen2": {"share_ge_25": 0.2368, "share_ge_15": 0.4432, "median_abs_gap": 12.99, "n": 29437}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.82, "share_ge_25_all": 0.0431, "share_ge_25_pregame_clean": 0.0387}, "WTA": {"median_abs_gap_pregame_clean": 7.58, "share_ge_25_all": 0.0572, "share_ge_25_pregame_clean": 0.0502}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2376, "share_within_10pp_all": 0.4377, "share_within_10pp_pregame_clean": 0.4892, "corr_model_vs_mid_pregame_clean": 0.8489}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 782, "model_brier": 0.199, "kalshi_brier": 0.1996, "brier_diff_model_minus_kalshi": -0.0006}, "10-15": {"n_settled": 932, "model_brier": 0.2221, "kalshi_brier": 0.2136, "brier_diff_model_minus_kalshi": 0.0085}, "15-25": {"n_settled": 1179, "model_brier": 0.2246, "kalshi_brier": 0.2126, "brier_diff_model_minus_kalshi": 0.012}, "25-40": {"n_settled": 692, "model_brier": 0.2239, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.0166}, "3-5": {"n_settled": 477, "model_brier": 0.2057, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": -0.0007}, "40+": {"n_settled": 143, "model_brier": 0.2752, "kalshi_brier": 0.1915, "brier_diff_model_minus_kalshi": 0.0836}, "5-10": {"n_settled": 1106, "model_brier": 0.2015, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": -0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.535, "slope": 0.804, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.191, "slope": 1.045, "slope_se": 0.039}, "n": 5311}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.485, "slope": 0.852, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.166, "slope": 1.051, "slope_se": 0.032}, "n": 7428}, "NO_SKILL:gen2|WTA": {"n_settled": 235, "model_brier": 0.2568, "kalshi_brier": 0.2361, "brier_diff_model_minus_kalshi": 0.0207, "brier_diff_se": 0.0103, "corr_model_outcome": 0.2213, "corr_kalshi_outcome": 0.2536}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 476, "model_brier": 0.311, "kalshi_brier": 0.2376, "brier_diff_model_minus_kalshi": 0.0734, "brier_diff_se": 0.0139, "corr_model_outcome": 0.0465, "corr_kalshi_outcome": 0.2371}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
