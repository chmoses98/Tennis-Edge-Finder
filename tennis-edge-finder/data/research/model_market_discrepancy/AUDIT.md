# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-29T00:46Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 66,785): 0-3 14.1%, 3-5 9.6%, 5-10 20.0%, 10-15 15.3%, 15-25 19.0%, 25-40 13.9%, 40+ 8.0%; median gap 11.89 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 11.0%, doubles 6.4%). Main tour: ATP 4.3% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 14,644): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.7%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.7%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.7%, market_freshness 18.7%, execution 18.7%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 14,644 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.0% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 455.0 points vs 1646.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.018, Gen-2 0.809, Gen-1 ledger 0.854 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 702 model 0.2238 vs Kalshi 0.2075; n 148 model 0.2759 vs Kalshi 0.1895.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 285,713 model-market comparisons (465,891 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 95,628 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-29T00:28:57.490943+00:00'], shadow board 76,374 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-29T00:29:02.883839+00:00'], Model 4 36,072 rows, 23,183 settled tickers, 8,398 tickers with an external scan.
* By model: {"gen1_ledger": 64511, "gen1_elo": 38395, "fair_v1": 38395, "gen2": 38395, "gen1_sr": 38395, "model4_fundamental": 33833, "model4_conditioned": 33789}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 66,785 | 14.1 | 9.6 | 20.0 | 15.3 | 19.0 | 13.9 | 8.0 | 11.89 | 41.0% | 21.9% |
| MW fair_v1 | 38,395 | 13.0 | 8.7 | 18.6 | 15.4 | 19.5 | 15.0 | 9.8 | 13.03 | 44.3% | 24.9% |
| MW gen1_elo | 38,395 | 12.7 | 8.6 | 19.2 | 15.4 | 19.5 | 14.9 | 9.7 | 12.95 | 44.1% | 24.7% |
| MW gen1_ledger | 28,390 | 15.6 | 10.7 | 21.9 | 15.3 | 18.5 | 12.4 | 5.6 | 10.41 | 36.4% | 18.0% |
| MW gen1_sr | 38,395 | 10.1 | 7.2 | 16.9 | 13.8 | 20.7 | 18.6 | 12.8 | 15.92 | 52.1% | 31.4% |
| MW gen2 | 38,395 | 11.2 | 7.5 | 16.4 | 13.8 | 19.4 | 17.9 | 13.8 | 15.5 | 51.1% | 31.7% |
| all families model4_conditioned | 33,789 | 22.3 | 18.2 | 34.3 | 17.3 | 5.0 | 1.9 | 1.1 | 6.02 | 8.0% | 3.0% |
| all families model4_fundamental | 33,833 | 17.2 | 13.3 | 33.8 | 20.4 | 10.2 | 3.6 | 1.4 | 7.72 | 15.3% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.3%, >=15pp 41.0%, >=20pp 30.4%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.29pp; >=10pp 44.7%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,361 | 27.2 | 15.5 | 27.4 | 13.4 | 11.7 | 4.1 | 0.6 | 5.92 | 16.4% | 4.7% |
| CHALLENGER | 5,801 | 16.2 | 9.8 | 20.7 | 15.3 | 15.4 | 11.9 | 10.7 | 10.93 | 38.0% | 22.6% |
| ITF_MEN | 10,672 | 9.9 | 7.4 | 16.8 | 15.1 | 21.1 | 17.6 | 12.1 | 15.32 | 50.8% | 29.7% |
| ITF_WOMEN | 15,108 | 9.8 | 7.0 | 15.8 | 15.0 | 22.1 | 18.3 | 12.0 | 15.74 | 52.4% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,402 | 18.3 | 13.7 | 24.4 | 20.2 | 16.1 | 6.5 | 0.8 | 8.25 | 23.4% | 7.3% |
| WTA125 | 1,045 | 16.0 | 7.8 | 22.6 | 19.3 | 20.2 | 12.5 | 1.6 | 10.7 | 34.4% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,361 | 25.9 | 15.5 | 25.3 | 16.3 | 12.0 | 4.2 | 0.8 | 6.23 | 17.0% | 5.0% |
| CHALLENGER | 5,801 | 15.1 | 8.9 | 18.1 | 14.4 | 18.1 | 13.7 | 11.6 | 12.63 | 43.4% | 25.3% |
| ITF_MEN | 10,672 | 8.0 | 6.0 | 14.9 | 13.6 | 19.7 | 20.7 | 17.1 | 18.11 | 57.4% | 37.8% |
| ITF_WOMEN | 15,108 | 8.0 | 5.8 | 14.0 | 12.7 | 20.6 | 21.4 | 17.6 | 19.23 | 59.5% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,402 | 15.2 | 10.9 | 21.8 | 15.6 | 22.1 | 12.7 | 1.7 | 10.62 | 36.5% | 14.4% |
| WTA125 | 1,045 | 9.6 | 6.3 | 16.2 | 16.6 | 24.6 | 17.9 | 8.8 | 15.5 | 51.3% | 26.7% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,361 | 22.4 | 13.0 | 24.4 | 16.0 | 16.2 | 6.7 | 1.3 | 7.58 | 24.2% | 8.0% |
| CHALLENGER | 5,801 | 15.0 | 9.3 | 21.1 | 15.8 | 15.5 | 12.3 | 10.9 | 11.2 | 38.7% | 23.2% |
| ITF_MEN | 10,672 | 9.3 | 7.1 | 17.3 | 14.4 | 21.6 | 18.1 | 12.3 | 15.75 | 51.9% | 30.4% |
| ITF_WOMEN | 15,108 | 9.5 | 6.8 | 16.3 | 15.8 | 22.1 | 18.1 | 11.3 | 15.51 | 51.6% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,402 | 23.6 | 16.6 | 31.6 | 14.8 | 9.4 | 2.7 | 1.3 | 6.08 | 13.4% | 4.0% |
| WTA125 | 1,045 | 22.1 | 13.0 | 26.6 | 16.8 | 14.8 | 6.3 | 0.4 | 7.94 | 21.5% | 6.7% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,951 | 24.4 | 19.0 | 31.1 | 12.9 | 9.0 | 3.0 | 0.5 | 5.74 | 12.6% | 3.5% |
| CHALLENGER | 3,935 | 22.5 | 14.6 | 26.9 | 14.7 | 13.8 | 6.1 | 1.6 | 7.13 | 21.4% | 7.6% |
| DOUBLES | 2,033 | 5.2 | 4.5 | 12.2 | 10.7 | 21.1 | 25.0 | 21.4 | 23.54 | 67.4% | 46.3% |
| ITF_MEN | 8,159 | 13.1 | 9.3 | 21.1 | 15.9 | 21.3 | 13.3 | 6.0 | 11.98 | 40.6% | 19.3% |
| ITF_WOMEN | 9,684 | 13.1 | 9.1 | 19.6 | 15.6 | 21.3 | 15.5 | 5.8 | 12.48 | 42.6% | 21.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,420 | 24.3 | 15.4 | 29.9 | 18.0 | 9.3 | 2.8 | 0.3 | 6.79 | 12.4% | 3.1% |
| WTA125 | 1,059 | 24.9 | 12.5 | 21.1 | 19.3 | 13.1 | 7.5 | 1.7 | 7.88 | 22.3% | 9.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,263 | 27.5 | 15.7 | 27.8 | 13.4 | 11.5 | 3.7 | 0.4 | 5.88 | 15.6% | 4.1% |
| CHALLENGER | 4,071 | 21.2 | 12.4 | 25.8 | 17.8 | 15.1 | 6.2 | 1.5 | 8.03 | 22.8% | 7.7% |
| ITF_MEN | 7,841 | 12.1 | 8.7 | 20.3 | 17.2 | 22.0 | 14.5 | 5.3 | 12.47 | 41.7% | 19.7% |
| ITF_WOMEN | 11,279 | 11.7 | 8.4 | 18.2 | 17.2 | 24.0 | 15.3 | 5.2 | 13.38 | 44.5% | 20.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,326 | 18.6 | 13.6 | 24.6 | 20.5 | 16.2 | 6.0 | 0.6 | 8.2 | 22.8% | 6.6% |
| WTA125 | 1,009 | 16.2 | 7.6 | 22.1 | 19.6 | 20.7 | 12.3 | 1.4 | 10.97 | 34.4% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,263 | 26.2 | 15.8 | 25.5 | 16.3 | 12.0 | 3.8 | 0.5 | 6.2 | 16.2% | 4.3% |
| CHALLENGER | 4,071 | 19.4 | 11.3 | 22.9 | 16.9 | 18.4 | 9.3 | 1.9 | 9.07 | 29.5% | 11.1% |
| ITF_MEN | 7,842 | 9.3 | 7.2 | 17.3 | 15.8 | 21.5 | 18.9 | 10.0 | 15.17 | 50.4% | 28.9% |
| ITF_WOMEN | 11,280 | 8.9 | 6.7 | 15.8 | 14.1 | 22.7 | 20.9 | 10.9 | 16.74 | 54.4% | 31.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,326 | 15.4 | 11.0 | 21.9 | 15.7 | 22.2 | 12.6 | 1.2 | 10.59 | 36.1% | 13.8% |
| WTA125 | 1,009 | 9.6 | 6.3 | 16.2 | 16.9 | 24.5 | 18.2 | 8.2 | 15.35 | 50.9% | 26.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,897 | 24.6 | 19.2 | 31.1 | 13.1 | 8.7 | 2.9 | 0.4 | 5.67 | 12.0% | 3.3% |
| CHALLENGER | 3,467 | 24.0 | 15.5 | 28.1 | 14.8 | 13.1 | 4.1 | 0.4 | 6.6 | 17.6% | 4.6% |
| DOUBLES | 1,906 | 5.1 | 4.6 | 12.4 | 10.9 | 21.0 | 24.8 | 21.2 | 23.35 | 67.0% | 46.0% |
| ITF_MEN | 6,969 | 13.9 | 9.8 | 22.7 | 16.6 | 21.3 | 11.8 | 3.9 | 11.02 | 37.0% | 15.7% |
| ITF_WOMEN | 8,230 | 13.8 | 9.6 | 20.9 | 16.3 | 21.4 | 14.5 | 3.6 | 11.61 | 39.5% | 18.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,366 | 24.7 | 15.8 | 29.9 | 18.1 | 9.3 | 2.2 | 0.1 | 6.68 | 11.6% | 2.3% |
| WTA125 | 935 | 26.3 | 13.3 | 22.1 | 20.5 | 12.0 | 5.2 | 0.5 | 7.32 | 17.8% | 5.8% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,033 | 5.2 | 4.5 | 12.2 | 10.7 | 21.1 | 25.0 | 21.4 | 23.54 | 67.4% | 46.3% |
| singles | 26,357 | 16.4 | 11.2 | 22.7 | 15.6 | 18.3 | 11.4 | 4.3 | 9.91 | 34.0% | 15.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,732 | 13.1 | 9.3 | 20.1 | 15.6 | 19.1 | 13.9 | 9.0 | 12.4 | 42.0% | 22.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 25,081 | 13.5 | 8.7 | 18.4 | 15.1 | 19.3 | 15.2 | 9.8 | 12.99 | 44.2% | 25.0% |
| UNKNOWN | 5,333 | 10.6 | 7.8 | 17.0 | 16.6 | 20.8 | 15.9 | 11.2 | 14.12 | 48.0% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,640 | 20.0 | 12.2 | 22.3 | 15.8 | 14.7 | 9.3 | 5.8 | 8.59 | 29.8% | 15.1% |
| B | 4,681 | 12.9 | 8.8 | 19.0 | 16.2 | 19.4 | 12.8 | 10.8 | 12.61 | 43.0% | 23.6% |
| C | 5,474 | 12.2 | 8.9 | 19.8 | 15.8 | 18.6 | 14.4 | 10.3 | 12.76 | 43.4% | 24.7% |
| D | 6,061 | 12.1 | 8.3 | 17.5 | 15.3 | 21.5 | 15.8 | 9.4 | 13.76 | 46.8% | 25.3% |
| F | 11,539 | 7.5 | 5.6 | 14.9 | 14.6 | 23.2 | 21.1 | 13.1 | 17.82 | 57.5% | 34.2% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,552 | 24.1 | 15.7 | 28.6 | 15.4 | 11.0 | 3.8 | 1.3 | 6.53 | 16.2% | 5.2% |
| B | 3,942 | 17.1 | 10.4 | 24.0 | 16.4 | 19.1 | 9.9 | 3.2 | 9.71 | 32.2% | 13.2% |
| C | 5,535 | 11.3 | 7.9 | 19.4 | 14.7 | 21.1 | 15.5 | 10.1 | 13.48 | 46.7% | 25.6% |
| D | 4,151 | 14.5 | 10.0 | 21.5 | 15.3 | 19.9 | 13.1 | 5.6 | 11.24 | 38.6% | 18.7% |
| F | 7,210 | 9.9 | 8.3 | 16.1 | 14.9 | 23.1 | 19.9 | 7.8 | 15.41 | 50.8% | 27.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,072 | 18.3 | 11.1 | 21.4 | 15.5 | 15.2 | 10.1 | 8.5 | 9.77 | 33.8% | 18.6% |
| LIMITED | 8,359 | 13.7 | 10.0 | 20.2 | 16.3 | 19.0 | 13.4 | 7.4 | 11.71 | 39.8% | 20.8% |
| POOR | 17,964 | 9.1 | 6.5 | 15.9 | 14.9 | 22.6 | 19.1 | 11.8 | 16.19 | 53.5% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,377 | 24.1 | 18.1 | 33.1 | 15.0 | 6.6 | 2.7 | 0.4 | 5.86 | 9.7% | 3.0% |
| GAME_SPREAD | 5,782 | 22.2 | 15.2 | 33.0 | 17.1 | 9.0 | 2.9 | 0.6 | 6.74 | 12.4% | 3.5% |
| MATCH_WINNER | 28,390 | 15.6 | 10.7 | 21.9 | 15.3 | 18.5 | 12.4 | 5.6 | 10.41 | 36.4% | 18.0% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,344 | 27.3 | 16.7 | 31.3 | 12.5 | 9.5 | 2.4 | 0.3 | 5.7 | 12.2% | 2.7% |
| TOTAL_GAMES | 9,594 | 9.4 | 10.3 | 36.1 | 26.9 | 10.6 | 4.0 | 2.8 | 9.31 | 17.4% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,979 | 24.4 | 30.2 | 32.9 | 7.4 | 4.0 | 0.9 | 0.2 | 4.7 | 5.2% | 1.1% |
| GAME_SPREAD | 7,910 | 47.2 | 16.1 | 25.4 | 7.3 | 2.2 | 1.2 | 0.6 | 3.28 | 4.0% | 1.8% |
| TOTAL_GAMES | 13,900 | 6.3 | 9.0 | 40.5 | 31.6 | 7.3 | 3.1 | 2.2 | 9.34 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,990 | 23.9 | 16.8 | 34.8 | 14.4 | 7.1 | 2.6 | 0.4 | 6.03 | 10.1% | 3.0% |
| GAME_SPREAD | 7,913 | 20.1 | 13.5 | 28.0 | 20.5 | 12.6 | 4.2 | 1.1 | 7.81 | 17.9% | 5.3% |
| TOTAL_GAMES | 13,930 | 9.9 | 10.2 | 36.3 | 25.4 | 11.6 | 4.2 | 2.4 | 9.21 | 18.2% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 38,395 | 44.3% | 24.9% | 13.03 | 35.6% | 15.4% | 10.78 |
| gen1_elo | 38,395 | 44.1% | 24.7% | 12.95 | 35.4% | 15.4% | 10.57 |
| gen1_sr | 38,395 | 52.1% | 31.4% | 15.92 | 44.3% | 22.0% | 13.04 |
| gen2 | 38,395 | 51.1% | 31.7% | 15.5 | 44.2% | 23.6% | 12.97 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,317 | 15.6 | 10.6 | 21.3 | 17.2 | 20.0 | 12.0 | 3.3 | 10.71 | 35.4% | 15.4% |
| STALE | 20,078 | 10.6 | 7.0 | 16.1 | 13.8 | 19.0 | 17.8 | 15.8 | 16.06 | 52.5% | 33.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 21,858 | 16.4 | 11.1 | 22.6 | 15.4 | 17.9 | 11.9 | 4.8 | 9.98 | 34.5% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 66,785 | 21858 | 21789 | 23138 | 24.3 | 124.6 | 1451.1 |
| ge_15pp | 27,358 | 7542 | 7768 | 12048 | 26.7 | 437.4 | 1451.1 |
| ge_25pp | 14,644 | 3638 | 3408 | 7598 | 31.7 | 584.1 | 1431.1 |
| lt_10pp | 29,177 | 10944 | 10324 | 7909 | 22.4 | 46.9 | 1421.1 |

Current slate `SL-20261029T004600Z-fdcba7b7`: 622 priced rows, quote age at build {'median': 17.5, 'max': 17.6}, freshness {'AGING': 622}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 43 | 0.0 | 0.0 | 32.6 | 7.0 | 34.9 | 23.3 | 2.3 | 20.19 | 60.5% | 25.6% |
| EXTERNAL_LONE_OUTLIER | 23 | 69.6 | 30.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,749 | 19.9 | 11.3 | 25.0 | 18.0 | 17.8 | 7.2 | 0.8 | 8.62 | 25.8% | 8.0% |
| KALSHI_LONE_OUTLIER | 26 | 3.9 | 3.9 | 76.9 | 7.7 | 3.9 | 3.9 | 0.0 | 6.31 | 7.7% | 3.9% |
| MARKETS_AGREE | 745 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.25 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,609 | 0.0 | 2.5 | 35.9 | 25.7 | 24.6 | 10.4 | 0.8 | 12.12 | 35.9% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 38,395 | 6195 (16.1%) | 26.0% | 1.1% | {"EXTERNAL_STALE": 3749, "AGREES_WITH_KALSHI": 1609, "ALL_AGREE": 745, "SUPPORTS_MODEL_DIRECTION": 42, "AGREES_WITH_MODEL": 26, "EXTERNAL_OUTLIER": 23, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 17,017 | 1572 (9.2%) | 36.7% | 1.8% | {"EXTERNAL_STALE": 967, "AGREES_WITH_KALSHI": 577, "SUPPORTS_MODEL_DIRECTION": 26, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,544 | 493 (5.2%) | 36.7% | 2.4% | {"EXTERNAL_STALE": 300, "AGREES_WITH_KALSHI": 181, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,600 | 468 (10.2%) | 37.2% | 2.6% | {"EXTERNAL_STALE": 282, "AGREES_WITH_KALSHI": 174, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 15,464 | 3529 (22.8%) | 17.5% | 1.0% | {"EXTERNAL_STALE": 2107, "ALL_AGREE": 745, "AGREES_WITH_KALSHI": 618, "EXTERNAL_OUTLIER": 23, "AGREES_WITH_MODEL": 22, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,526 | 10.5 | 7.4 | 19.7 | 14.3 | 21.6 | 16.6 | 9.9 | 14.12 | 48.2% | 26.6% |
| 4-10x | 5,166 | 11.2 | 8.6 | 18.3 | 15.5 | 21.8 | 14.6 | 9.9 | 13.71 | 46.4% | 24.5% |
| <2x | 19,374 | 15.2 | 10.0 | 19.3 | 16.1 | 17.4 | 13.2 | 8.8 | 11.58 | 39.3% | 22.0% |
| >=10x | 6,329 | 10.7 | 6.4 | 15.1 | 14.4 | 21.4 | 19.2 | 12.8 | 16.2 | 53.4% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,716 | 12.8 | 8.6 | 19.5 | 16.2 | 18.9 | 13.7 | 10.3 | 12.7 | 42.9% | 23.9% |
| 300-1000 | 8,268 | 12.2 | 8.7 | 17.7 | 15.2 | 20.3 | 16.4 | 9.6 | 13.61 | 46.3% | 25.9% |
| <300 | 12,557 | 8.3 | 5.8 | 15.2 | 14.8 | 22.9 | 20.1 | 12.9 | 17.05 | 55.9% | 33.0% |
| >=3000 | 7,854 | 21.6 | 13.4 | 23.8 | 15.7 | 13.7 | 7.2 | 4.7 | 7.56 | 25.6% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1090 | 0.55 | 0.4112 | 0.4991 | +0.051 | -0.088 | -0.0024 ± 0.0047 |
| ratio 4-10x | 748 | 0.5794 | 0.4335 | 0.4933 | +0.086 | -0.060 | 0.0085 ± 0.0058 |
| ratio <2x | 2619 | 0.5371 | 0.4137 | 0.4494 | +0.088 | -0.036 | 0.0109 ± 0.0028 |
| ratio >=10x | 953 | 0.5668 | 0.3914 | 0.4449 | +0.122 | -0.053 | 0.015 ± 0.0059 |
| thinner_sample 1000-3000 | 1447 | 0.5381 | 0.4113 | 0.4513 | +0.087 | -0.040 | 0.0082 ± 0.0038 |
| thinner_sample 300-1000 | 1227 | 0.5679 | 0.4264 | 0.489 | +0.079 | -0.063 | 0.0023 ± 0.0046 |
| thinner_sample <300 | 1842 | 0.5584 | 0.3903 | 0.4587 | +0.100 | -0.069 | 0.0112 ± 0.0042 |
| thinner_sample >=3000 | 894 | 0.5323 | 0.4381 | 0.4653 | +0.067 | -0.027 | 0.0126 ± 0.0038 |
| data_status ADEQUATE | 1486 | 0.5341 | 0.4305 | 0.4502 | +0.084 | -0.020 | 0.0126 ± 0.0032 |
| data_status LIMITED | 1282 | 0.5477 | 0.4151 | 0.4782 | +0.070 | -0.063 | 0.0039 ± 0.0042 |
| data_status POOR | 2642 | 0.5617 | 0.4001 | 0.4663 | +0.095 | -0.066 | 0.0087 ± 0.0034 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 801 | 0.1975 | 0.1979 | -0.0005 ± 0.0006 | 0.5738 | 0.575 | 0.5031 | 0.4879 | 0.5081 | -0.088 ± 0.0167 | -0.01 (5) |
| 3-5 | 484 | 0.2059 | 0.2066 | -0.0008 ± 0.0017 | 0.5952 | 0.5954 | 0.5029 | 0.4631 | 0.4917 | -0.091 ± 0.0212 | 0.02 (1) |
| 5-10 | 1129 | 0.201 | 0.2016 | -0.0006 ± 0.002 | 0.5875 | 0.5863 | 0.5098 | 0.4361 | 0.4748 | -0.086 ± 0.0138 | -0.0167 (6) |
| 10-15 | 947 | 0.2224 | 0.2132 | +0.0092 ± 0.0037 | 0.638 | 0.6126 | 0.527 | 0.4034 | 0.4266 | -0.111 ± 0.0151 | -0.048 (5) |
| 15-25 | 1199 | 0.2246 | 0.2121 | +0.0125 ± 0.0052 | 0.6449 | 0.6086 | 0.575 | 0.3793 | 0.4454 | -0.099 ± 0.0133 | -0.0033 (9) |
| 25-40 | 702 | 0.2238 | 0.2075 | +0.0164 ± 0.0103 | 0.6379 | 0.5969 | 0.6546 | 0.3441 | 0.4729 | -0.073 ± 0.0158 | -0.01 (1) |
| 40+ | 148 | 0.2759 | 0.1895 | +0.0864 ± 0.0311 | 0.7512 | 0.5584 | 0.7408 | 0.2918 | 0.4257 | -0.069 ± 0.0304 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4285 | 0.1806 | 0.1813 | -0.0006 ± 0.0002 | 0.5349 | 0.5355 | 0.4865 | 0.4712 | 0.4952 | -0.030 ± 0.0066 | -0.0129 (17) |
| 3-5 | 2901 | 0.195 | 0.1929 | +0.0021 ± 0.0007 | 0.5691 | 0.5616 | 0.4821 | 0.4423 | 0.4354 | -0.062 ± 0.0082 | 0.0 (2) |
| 5-10 | 6097 | 0.2015 | 0.1981 | +0.0034 ± 0.0009 | 0.5886 | 0.5768 | 0.4829 | 0.4093 | 0.4243 | -0.046 ± 0.0058 | -0.0119 (21) |
| 10-15 | 5115 | 0.2028 | 0.1865 | +0.0163 ± 0.0015 | 0.592 | 0.5477 | 0.483 | 0.359 | 0.3548 | -0.068 ± 0.0061 | -0.0281 (16) |
| 15-25 | 6374 | 0.2067 | 0.1688 | +0.0379 ± 0.002 | 0.6061 | 0.5006 | 0.4995 | 0.3031 | 0.3055 | -0.069 ± 0.0051 | -0.0025 (44) |
| 25-40 | 5103 | 0.2216 | 0.1248 | +0.0968 ± 0.0031 | 0.6373 | 0.3839 | 0.5259 | 0.2116 | 0.2191 | -0.059 ± 0.0048 | -0.01 (1) |
| 40+ | 3321 | 0.3821 | 0.0446 | +0.3374 ± 0.0042 | 0.9945 | 0.1729 | 0.6315 | 0.1037 | 0.0605 | -0.077 ± 0.0034 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 617 | 0.205 | 0.2057 | -0.0007 ± 0.0006 | 0.5914 | 0.5933 | 0.5102 | 0.4952 | 0.5219 | -0.103 ± 0.0198 | -0.01 (3) |
| 3-5 | 440 | 0.2244 | 0.2216 | +0.0029 ± 0.0018 | 0.6347 | 0.6289 | 0.5131 | 0.4734 | 0.4523 | -0.134 ± 0.0239 | 0.02 (1) |
| 5-10 | 981 | 0.2078 | 0.2075 | +0.0003 ± 0.0022 | 0.6012 | 0.5998 | 0.5464 | 0.4714 | 0.5087 | -0.085 ± 0.015 | -0.01 (4) |
| 10-15 | 887 | 0.2181 | 0.2106 | +0.0075 ± 0.0039 | 0.6277 | 0.6082 | 0.5647 | 0.4403 | 0.4746 | -0.112 ± 0.0161 | -0.04 (5) |
| 15-25 | 1261 | 0.2291 | 0.2134 | +0.0156 ± 0.0051 | 0.6525 | 0.611 | 0.5815 | 0.3862 | 0.4465 | -0.096 ± 0.0132 | -0.0133 (9) |
| 25-40 | 892 | 0.2686 | 0.1966 | +0.0720 ± 0.0093 | 0.7499 | 0.5737 | 0.6544 | 0.3403 | 0.3857 | -0.131 ± 0.0148 | -0.0075 (4) |
| 40+ | 332 | 0.3588 | 0.1685 | +0.1903 ± 0.0223 | 0.9818 | 0.505 | 0.7319 | 0.2467 | 0.3072 | -0.076 ± 0.0217 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3662 | 0.188 | 0.1883 | -0.0003 ± 0.0002 | 0.5508 | 0.5512 | 0.5091 | 0.494 | 0.5098 | -0.041 ± 0.0074 | -0.0133 (15) |
| 3-5 | 2479 | 0.1967 | 0.1953 | +0.0014 ± 0.0007 | 0.5705 | 0.5666 | 0.5131 | 0.4735 | 0.4752 | -0.051 ± 0.0091 | 0.02 (1) |
| 5-10 | 5408 | 0.1987 | 0.1947 | +0.0039 ± 0.0009 | 0.5827 | 0.5686 | 0.5128 | 0.4387 | 0.4523 | -0.046 ± 0.0061 | -0.0117 (6) |
| 10-15 | 4612 | 0.2062 | 0.1934 | +0.0127 ± 0.0016 | 0.6024 | 0.5641 | 0.5121 | 0.3883 | 0.3994 | -0.056 ± 0.0066 | -0.0189 (18) |
| 15-25 | 6438 | 0.2166 | 0.1804 | +0.0362 ± 0.0021 | 0.6306 | 0.5298 | 0.5214 | 0.326 | 0.3346 | -0.063 ± 0.0053 | -0.0086 (42) |
| 25-40 | 5910 | 0.251 | 0.1354 | +0.1157 ± 0.003 | 0.7075 | 0.4157 | 0.5554 | 0.2386 | 0.2176 | -0.086 ± 0.0048 | -0.0044 (18) |
| 40+ | 4687 | 0.3957 | 0.0589 | +0.3369 ± 0.0041 | 1.0419 | 0.2119 | 0.6501 | 0.1165 | 0.0813 | -0.072 ± 0.0035 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 766 | 0.1953 | 0.1974 | -0.0020 ± 0.0006 | 0.5689 | 0.5741 | 0.5008 | 0.4855 | 0.5431 | -0.040 ± 0.0168 | -0.0137 (8) |
| 3-5 | 526 | 0.2043 | 0.2026 | +0.0017 ± 0.0016 | 0.5916 | 0.5852 | 0.496 | 0.4563 | 0.4563 | -0.120 ± 0.0204 | 0.0067 (3) |
| 5-10 | 1164 | 0.2033 | 0.2014 | +0.0019 ± 0.002 | 0.5927 | 0.5856 | 0.5078 | 0.4339 | 0.4579 | -0.095 ± 0.0135 | -0.0071 (7) |
| 10-15 | 942 | 0.2104 | 0.2063 | +0.0041 ± 0.0037 | 0.6107 | 0.5969 | 0.5393 | 0.4161 | 0.4618 | -0.095 ± 0.0149 | -0.0317 (6) |
| 15-25 | 1137 | 0.2318 | 0.2158 | +0.0161 ± 0.0054 | 0.6614 | 0.6167 | 0.5867 | 0.3923 | 0.4485 | -0.109 ± 0.0138 | -0.03 (1) |
| 25-40 | 716 | 0.2138 | 0.2147 | -0.0009 ± 0.0101 | 0.6169 | 0.6138 | 0.664 | 0.3531 | 0.5084 | -0.057 ± 0.0157 | 0.015 (2) |
| 40+ | 159 | 0.2959 | 0.197 | +0.0989 ± 0.031 | 0.8067 | 0.5752 | 0.7484 | 0.2975 | 0.4214 | -0.073 ± 0.0322 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4163 | 0.1823 | 0.1828 | -0.0005 ± 0.0002 | 0.5374 | 0.5382 | 0.4818 | 0.4665 | 0.4819 | -0.036 ± 0.0067 | -0.0163 (35) |
| 3-5 | 2828 | 0.199 | 0.1972 | +0.0018 ± 0.0007 | 0.5804 | 0.5735 | 0.4815 | 0.442 | 0.4395 | -0.060 ± 0.0085 | -0.0094 (18) |
| 5-10 | 6253 | 0.1947 | 0.1905 | +0.0042 ± 0.0008 | 0.5729 | 0.5583 | 0.4834 | 0.4094 | 0.4182 | -0.050 ± 0.0056 | -0.01 (31) |
| 10-15 | 5057 | 0.1917 | 0.1783 | +0.0134 ± 0.0015 | 0.567 | 0.5284 | 0.4926 | 0.3693 | 0.3761 | -0.058 ± 0.006 | -0.015 (12) |
| 15-25 | 6511 | 0.2119 | 0.1734 | +0.0385 ± 0.002 | 0.6173 | 0.5111 | 0.5122 | 0.3174 | 0.3173 | -0.070 ± 0.0052 | -0.03 (2) |
| 25-40 | 5084 | 0.2159 | 0.1289 | +0.0871 ± 0.0032 | 0.6254 | 0.3928 | 0.5297 | 0.214 | 0.2364 | -0.047 ± 0.0049 | 0.01 (3) |
| 40+ | 3300 | 0.3945 | 0.0501 | +0.3444 ± 0.0044 | 1.0288 | 0.1874 | 0.6424 | 0.1113 | 0.0661 | -0.080 ± 0.0037 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1153 | 0.1959 | 0.196 | -0.0002 ± 0.0005 | 0.5706 | 0.5708 | 0.5057 | 0.4906 | 0.497 | -0.066 ± 0.0133 | -0.0224 (49) |
| 3-5 | 805 | 0.188 | 0.1875 | +0.0006 ± 0.0012 | 0.5512 | 0.549 | 0.4965 | 0.4567 | 0.4671 | -0.064 ± 0.0157 | -0.0194 (34) |
| 5-10 | 1689 | 0.2011 | 0.1964 | +0.0047 ± 0.0016 | 0.5911 | 0.5761 | 0.5012 | 0.4276 | 0.4334 | -0.073 ± 0.011 | -0.005 (78) |
| 10-15 | 1160 | 0.2164 | 0.2044 | +0.0120 ± 0.0033 | 0.6252 | 0.593 | 0.5345 | 0.4118 | 0.4224 | -0.084 ± 0.0136 | 0.0014 (64) |
| 15-25 | 1488 | 0.2316 | 0.2113 | +0.0203 ± 0.0047 | 0.6602 | 0.6076 | 0.5808 | 0.3859 | 0.4335 | -0.080 ± 0.012 | -0.0214 (59) |
| 25-40 | 930 | 0.2432 | 0.2097 | +0.0334 ± 0.0092 | 0.6957 | 0.6013 | 0.6816 | 0.3696 | 0.472 | -0.091 ± 0.0141 | -0.0219 (26) |
| 40+ | 312 | 0.3392 | 0.2015 | +0.1377 ± 0.0246 | 0.9794 | 0.5883 | 0.8127 | 0.3353 | 0.4455 | -0.102 ± 0.0229 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4229 | 0.1753 | 0.1755 | -0.0002 ± 0.0002 | 0.5196 | 0.5197 | 0.5118 | 0.4967 | 0.507 | -0.039 ± 0.0065 | -0.0157 (88) |
| 3-5 | 2886 | 0.1929 | 0.1914 | +0.0015 ± 0.0007 | 0.5617 | 0.5589 | 0.5062 | 0.4663 | 0.4678 | -0.050 ± 0.0083 | -0.0209 (69) |
| 5-10 | 5902 | 0.198 | 0.191 | +0.0070 ± 0.0009 | 0.5829 | 0.5624 | 0.4967 | 0.423 | 0.4138 | -0.066 ± 0.0057 | -0.0082 (132) |
| 10-15 | 4134 | 0.2121 | 0.1967 | +0.0154 ± 0.0017 | 0.6154 | 0.5752 | 0.5324 | 0.4095 | 0.4076 | -0.067 ± 0.007 | -0.0053 (105) |
| 15-25 | 5007 | 0.2294 | 0.2015 | +0.0279 ± 0.0025 | 0.6604 | 0.5824 | 0.5663 | 0.3709 | 0.3978 | -0.061 ± 0.0064 | -0.0253 (107) |
| 25-40 | 3388 | 0.2592 | 0.1855 | +0.0738 ± 0.0047 | 0.7346 | 0.5418 | 0.6348 | 0.3218 | 0.363 | -0.080 ± 0.0072 | -0.0229 (51) |
| 40+ | 1471 | 0.38 | 0.1507 | +0.2293 ± 0.0105 | 1.0731 | 0.4528 | 0.7362 | 0.2352 | 0.2678 | -0.079 ± 0.0096 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5410 | 1.018 ± 0.038 | 1.091 | 0.1688 | 0.1664 | 0.2149 | 0.2063 |
| gen2 | 5410 | 0.809 ± 0.035 | 1.05 | 0.1702 | 0.1669 | 0.2348 | 0.2061 |
| gen1_elo | 5410 | 0.996 ± 0.037 | 1.089 | 0.1754 | 0.1666 | 0.2136 | 0.2064 |
| gen1_sr | 5410 | 0.99 ± 0.045 | 1.112 | 0.1306 | 0.1688 | 0.2307 | 0.2058 |
| gen1_ledger | 7537 | 0.854 ± 0.027 | 1.055 | 0.1868 | 0.1768 | 0.2182 | 0.2014 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 27,358)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,116 | 22.4% |
| STALE_QUOTE | market_freshness | 5,966 | 21.8% |
| BOOK_QUALITY | execution | 5,244 | 19.2% |
| POOR_DATA | data | 3,202 | 11.7% |
| LIMITED_DATA | data | 1,696 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,540 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,209 | 4.4% |
| IDENTITY_AMBIGUOUS | mapping | 1,121 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 795 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 468 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.4%, market_freshness 21.8%, execution 19.2%, data 17.9%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.4%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 72.0%, THIN_PLAYER_HISTORY 60.9%, STALE_PLAYER_DATA 52.4%, STALE_KALSHI_QUOTE 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 25.2%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 15.7%, LEVEL_TRANSFER_RISK 10.4%, LOW_DISPLAYED_LIQUIDITY 7.9%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.9%, POST_SETTLEMENT_OBSERVATION 22.4%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 14,644)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,941 | 33.7% |
| STALE_QUOTE | market_freshness | 2,742 | 18.7% |
| BOOK_QUALITY | execution | 2,735 | 18.7% |
| POOR_DATA | data | 1,367 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 819 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 596 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 512 | 3.5% |
| LIMITED_DATA | data | 503 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 306 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 122 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.7%, market_freshness 18.7%, execution 18.7%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.3%, THIN_PLAYER_HISTORY 63.1%, STALE_KALSHI_QUOTE 51.9%, STALE_PLAYER_DATA 46.6%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.7%, WIDE_SPREAD 24.5%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.2%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.9%, POST_SETTLEMENT_OBSERVATION 33.7%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 11610, "IDENTITY_AMBIGUOUS": 3034}; ticker orientation: {"VERIFIED": 14644}.

Checks: discipline:AMBIGUOUS 942, discipline:PASS 13702, identity_confidence:AMBIGUOUS 2715, identity_confidence:PASS 11929, level_mapping:NA 954, level_mapping:PASS 13690, market_pair:AMBIGUOUS 478, market_pair:NA 347, market_pair:PASS 13819, model_complement:NA 311, model_complement:PASS 14333, namesake:AMBIGUOUS 6, namesake:PASS 14638, physical_match_id:NA 5100, physical_match_id:PASS 9544, player_ids:PASS 14644, same_pair_other_event:PASS 14644, ticker_orientation:PASS 14644

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,312 | 4.3% | 3.8% | 1.6% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.84 | 0.22 / 0.2173 (611) | 21.5% | 3.0% | 3.3% | 2.9% |
| CHALLENGER | 9,736 | 16.6% | 6.3% | 11.0% | {"coverage": 944, "market_freshness/coverage": 195, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 74, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.26 | 0.2193 / 0.2104 (2231) | 35.2% | 15.8% | 4.1% | 22.6% |
| DOUBLES | 2,033 | 46.3% | 46.0% | 6.4% | {"execution": 533, "mapping": 238, "market_freshness": 106, "market_freshness/coverage": 58, "coverage": 7} | 23.35 | 0.309 / 0.2374 (486) | 11.5% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 18,831 | 25.2% | 17.8% | 32.4% | {"coverage": 1659, "execution": 896, "market_freshness": 858, "data": 695, "market_freshness/coverage": 447, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.77 | 0.2168 / 0.1997 (3850) | 37.2% | 70.3% | 17.1% | 21.3% |
| ITF_WOMEN | 24,792 | 26.8% | 19.5% | 45.4% | {"coverage": 2281, "market_freshness": 1415, "execution": 1193, "data": 938, "market_freshness/coverage": 561, "mapping": 152, "model_calibration_or_unknown": 81, "model_calibration": 21} | 12.65 | 0.2046 / 0.1966 (4506) | 39.3% | 57.9% | 10.1% | 21.3% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,822 | 5.7% | 5.0% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "execution": 27, "coverage": 24, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.56 | 0.2347 / 0.2278 (591) | 26.1% | 1.1% | 1.4% | 3.4% |
| WTA125 | 2,104 | 11.6% | 9.9% | 1.7% | {"market_freshness": 64, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.18 | 0.2094 / 0.1923 (630) | 25.3% | 11.6% | 5.1% | 7.6% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 172 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 6 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 7 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 20.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1252 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 8 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 9 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 12 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 13 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 16 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 17 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 18 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 19 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 20 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 21 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 22 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 23 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 24 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 25 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 26 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 27 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 30 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 31 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 32 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 33 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 34 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 35 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 36 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 37 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 39 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 40 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 41 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 42 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 124 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 43 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 44 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 46 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 48 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 49 | `KXITFMATCH-26OCT28DELBAR-BAR` | ITF_MEN | fair_v1 | 84% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.5h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 216 min (STALE); data POOR (grade F, thinner serve sample 803.0, ratio 2.48); no external reference |
| 50 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9695, "by_level_share_of_ge_25pp": {"ATP": 0.0155, "CHALLENGER": 0.11, "DOUBLES": 0.0643, "ITF_MEN": 0.3241, "ITF_WOMEN": 0.4536, "OTHER": 0.0008, "WTA": 0.015, "WTA125": 0.0167}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5188, "share_primary_cause_market_settled_or_in_play": 0.4283, "share_primary_cause_stale_quote_only": 0.1872}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 14644, "identity_ambiguous_share": 0.2072, "ticker_orientation": {"VERIFIED": 14644}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9544, "with_external": 493, "coverage": 0.0517, "external_status": {"EXTERNAL_STALE": 300, "AGREES_WITH_KALSHI": 181, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 300, "MODEL_LONE_OUTLIER": 181, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3671, "share_external_supports_model": 0.0243}, "pregame_clean_ge_25pp": {"n": 4600, "with_external": 468, "coverage": 0.1017, "external_status": {"EXTERNAL_STALE": 282, "AGREES_WITH_KALSHI": 174, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 282, "MODEL_LONE_OUTLIER": 174, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3718, "share_external_supports_model": 0.0256}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 455.0, "median_sample_ratio": 2.5, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2124, "data_status": {"POOR": 8365, "LIMITED": 3737, "ADEQUATE": 2542}, "comparison_lt_10pp": {"median_thinner_serve_points": 1646.0, "median_sample_ratio": 1.73, "median_min_matches": 88.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1090, "model_minus_observed": 0.0509, "kalshi_minus_observed": -0.0879, "brier_diff_model_minus_kalshi": -0.0024}, "4-10x": {"n": 748, "model_minus_observed": 0.0861, "kalshi_minus_observed": -0.0598, "brier_diff_model_minus_kalshi": 0.0085}, "<2x": {"n": 2619, "model_minus_observed": 0.0877, "kalshi_minus_observed": -0.0357, "brier_diff_model_minus_kalshi": 0.0109}, ">=10x": {"n": 953, "model_minus_observed": 0.1219, "kalshi_minus_observed": -0.0535, "brier_diff_model_minus_kalshi": 0.015}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5410, "model": {"intercept": -0.537, "slope": 0.809, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.191, "slope": 1.05, "slope_se": 0.038}, "mean_extremity_model": 0.1702, "mean_extremity_kalshi": 0.1669, "model_brier": 0.2348, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0286, "brier_diff_se": 0.0026, "model_logloss": 0.667, "kalshi_logloss": 0.5953}, "fair_v1": {"n": 5410, "model": {"intercept": -0.411, "slope": 1.018, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.285, "slope": 1.091, "slope_se": 0.039}, "mean_extremity_model": 0.1688, "mean_extremity_kalshi": 0.1664, "model_brier": 0.2149, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0086, "brier_diff_se": 0.0021, "model_logloss": 0.6187, "kalshi_logloss": 0.5956}, "gen1_elo": {"n": 5410, "model": {"intercept": -0.388, "slope": 0.996, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.306, "slope": 1.089, "slope_se": 0.038}, "mean_extremity_model": 0.1754, "mean_extremity_kalshi": 0.1666, "model_brier": 0.2136, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": 0.0072, "brier_diff_se": 0.0021, "model_logloss": 0.6163, "kalshi_logloss": 0.5959}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2486, "share_ge_15": 0.4432, "median_abs_gap": 13.03, "n": 38395}, "gen1_elo": {"share_ge_25": 0.2468, "share_ge_15": 0.4415, "median_abs_gap": 12.95, "n": 38395}, "gen1_sr": {"share_ge_25": 0.3142, "share_ge_15": 0.5213, "median_abs_gap": 15.92, "n": 38395}, "gen2": {"share_ge_25": 0.3172, "share_ge_15": 0.5112, "median_abs_gap": 15.5, "n": 38395}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1544, "share_ge_15": 0.3561, "median_abs_gap": 10.78, "n": 29795}, "gen1_elo": {"share_ge_25": 0.1545, "share_ge_15": 0.3536, "median_abs_gap": 10.57, "n": 29794}, "gen1_sr": {"share_ge_25": 0.2199, "share_ge_15": 0.4432, "median_abs_gap": 13.04, "n": 29796}, "gen2": {"share_ge_25": 0.2361, "share_ge_15": 0.4424, "median_abs_gap": 12.97, "n": 29797}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0427, "share_ge_25_pregame_clean": 0.0382}, "WTA": {"median_abs_gap_pregame_clean": 7.56, "share_ge_25_all": 0.0573, "share_ge_25_pregame_clean": 0.0498}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2369, "share_within_10pp_all": 0.4369, "share_within_10pp_pregame_clean": 0.4889, "corr_model_vs_mid_pregame_clean": 0.85}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 801, "model_brier": 0.1975, "kalshi_brier": 0.1979, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 947, "model_brier": 0.2224, "kalshi_brier": 0.2132, "brier_diff_model_minus_kalshi": 0.0092}, "15-25": {"n_settled": 1199, "model_brier": 0.2246, "kalshi_brier": 0.2121, "brier_diff_model_minus_kalshi": 0.0125}, "25-40": {"n_settled": 702, "model_brier": 0.2238, "kalshi_brier": 0.2075, "brier_diff_model_minus_kalshi": 0.0164}, "3-5": {"n_settled": 484, "model_brier": 0.2059, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": -0.0008}, "40+": {"n_settled": 148, "model_brier": 0.2759, "kalshi_brier": 0.1895, "brier_diff_model_minus_kalshi": 0.0864}, "5-10": {"n_settled": 1129, "model_brier": 0.201, "kalshi_brier": 0.2016, "brier_diff_model_minus_kalshi": -0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.537, "slope": 0.809, "slope_se": 0.035}, "kalshi_slope": {"intercept": 0.191, "slope": 1.05, "slope_se": 0.038}, "n": 5410}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.486, "slope": 0.854, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.168, "slope": 1.055, "slope_se": 0.032}, "n": 7537}, "NO_SKILL:gen2|WTA": {"n_settled": 235, "model_brier": 0.2568, "kalshi_brier": 0.2361, "brier_diff_model_minus_kalshi": 0.0207, "brier_diff_se": 0.0103, "corr_model_outcome": 0.2213, "corr_kalshi_outcome": 0.2536}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 486, "model_brier": 0.309, "kalshi_brier": 0.2374, "brier_diff_model_minus_kalshi": 0.0716, "brier_diff_se": 0.0136, "corr_model_outcome": 0.0568, "corr_kalshi_outcome": 0.2379}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
