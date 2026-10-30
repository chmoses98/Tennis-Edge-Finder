# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-30T06:53Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 69,241): 0-3 14.1%, 3-5 9.6%, 5-10 20.1%, 10-15 15.3%, 15-25 19.0%, 25-40 13.9%, 40+ 8.0%; median gap 11.88 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 10.8%, doubles 6.5%). Main tour: ATP 4.2% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,157): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.1%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.5%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.1%, market_freshness 18.7%, execution 18.5%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,157 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.1% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 473.0 points vs 1669.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.013, Gen-2 0.804, Gen-1 ledger 0.853 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 734 model 0.2229 vs Kalshi 0.2054; n 155 model 0.2842 vs Kalshi 0.1885.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 294,785 model-market comparisons (481,614 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 98,732 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-30T06:37:10.979683+00:00'], shadow board 79,172 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-30T06:37:14.539729+00:00'], Model 4 36,828 rows, 24,009 settled tickers, 8,812 tickers with an external scan.
* By model: {"gen1_ledger": 66525, "gen1_elo": 39794, "fair_v1": 39794, "gen2": 39794, "gen1_sr": 39794, "model4_fundamental": 34564, "model4_conditioned": 34520}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 69,241 | 14.1 | 9.6 | 20.1 | 15.3 | 19.0 | 13.9 | 8.0 | 11.88 | 40.9% | 21.9% |
| MW fair_v1 | 39,794 | 12.9 | 8.7 | 18.7 | 15.3 | 19.5 | 15.0 | 9.9 | 13.03 | 44.4% | 24.9% |
| MW gen1_elo | 39,794 | 12.5 | 8.6 | 19.3 | 15.4 | 19.5 | 14.8 | 9.8 | 12.95 | 44.2% | 24.7% |
| MW gen1_ledger | 29,447 | 15.6 | 10.8 | 22.1 | 15.3 | 18.4 | 12.4 | 5.5 | 10.37 | 36.3% | 17.9% |
| MW gen1_sr | 39,794 | 10.1 | 7.2 | 16.8 | 13.8 | 20.7 | 18.6 | 12.8 | 15.88 | 52.1% | 31.4% |
| MW gen2 | 39,794 | 11.1 | 7.5 | 16.5 | 13.8 | 19.4 | 17.8 | 13.8 | 15.47 | 51.0% | 31.7% |
| all families model4_conditioned | 34,520 | 22.4 | 18.2 | 34.2 | 17.2 | 4.9 | 1.9 | 1.1 | 6.0 | 8.0% | 3.1% |
| all families model4_fundamental | 34,564 | 17.3 | 13.3 | 33.8 | 20.3 | 10.2 | 3.7 | 1.4 | 7.7 | 15.3% | 5.1% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.2%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.3pp; >=10pp 44.8%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,422 | 27.4 | 15.4 | 27.6 | 13.5 | 11.6 | 4.0 | 0.6 | 5.92 | 16.2% | 4.6% |
| CHALLENGER | 5,932 | 16.3 | 9.7 | 20.8 | 15.1 | 15.4 | 11.8 | 10.8 | 10.91 | 38.0% | 22.6% |
| ITF_MEN | 11,164 | 9.8 | 7.4 | 17.1 | 15.1 | 21.2 | 17.6 | 11.9 | 15.23 | 50.7% | 29.5% |
| ITF_WOMEN | 15,713 | 9.7 | 7.1 | 15.9 | 15.1 | 22.0 | 18.2 | 12.1 | 15.71 | 52.3% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,464 | 18.2 | 13.7 | 24.8 | 19.9 | 16.1 | 6.3 | 1.0 | 8.23 | 23.5% | 7.3% |
| WTA125 | 1,093 | 16.2 | 7.6 | 22.4 | 19.0 | 20.5 | 12.3 | 1.9 | 10.97 | 34.8% | 14.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,422 | 26.1 | 15.4 | 25.6 | 16.2 | 11.9 | 4.1 | 0.8 | 6.23 | 16.8% | 4.9% |
| CHALLENGER | 5,932 | 15.1 | 9.0 | 18.3 | 14.3 | 18.1 | 13.7 | 11.6 | 12.59 | 43.4% | 25.3% |
| ITF_MEN | 11,164 | 8.0 | 6.1 | 15.1 | 13.8 | 19.5 | 20.7 | 16.7 | 17.97 | 57.0% | 37.4% |
| ITF_WOMEN | 15,713 | 8.0 | 5.8 | 14.0 | 12.7 | 20.6 | 21.3 | 17.6 | 19.18 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,464 | 15.2 | 10.9 | 22.2 | 15.3 | 22.0 | 12.6 | 1.9 | 10.59 | 36.4% | 14.5% |
| WTA125 | 1,093 | 9.6 | 6.4 | 16.6 | 16.3 | 24.4 | 17.5 | 9.2 | 15.33 | 51.0% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,422 | 22.2 | 13.2 | 24.4 | 16.0 | 16.2 | 6.7 | 1.3 | 7.58 | 24.1% | 8.0% |
| CHALLENGER | 5,932 | 14.9 | 9.2 | 21.1 | 16.1 | 15.6 | 12.1 | 11.0 | 11.31 | 38.7% | 23.1% |
| ITF_MEN | 11,164 | 9.3 | 7.1 | 17.4 | 14.4 | 21.7 | 17.8 | 12.3 | 15.7 | 51.8% | 30.1% |
| ITF_WOMEN | 15,713 | 9.4 | 6.8 | 16.4 | 15.8 | 22.0 | 18.0 | 11.5 | 15.5 | 51.5% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,464 | 23.7 | 16.7 | 31.8 | 14.4 | 9.2 | 2.9 | 1.3 | 6.05 | 13.4% | 4.2% |
| WTA125 | 1,093 | 21.9 | 12.8 | 26.9 | 16.9 | 15.1 | 6.0 | 0.4 | 8.01 | 21.5% | 6.4% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,998 | 24.5 | 19.0 | 31.2 | 12.8 | 9.0 | 3.0 | 0.5 | 5.74 | 12.5% | 3.5% |
| CHALLENGER | 4,014 | 22.6 | 14.6 | 27.2 | 14.6 | 13.6 | 6.0 | 1.5 | 7.08 | 21.1% | 7.5% |
| DOUBLES | 2,121 | 5.1 | 4.4 | 12.2 | 10.8 | 21.1 | 24.9 | 21.5 | 23.54 | 67.5% | 46.4% |
| ITF_MEN | 8,477 | 13.0 | 9.4 | 21.2 | 15.8 | 21.3 | 13.3 | 5.9 | 11.89 | 40.5% | 19.2% |
| ITF_WOMEN | 10,114 | 13.1 | 9.2 | 19.7 | 15.8 | 21.2 | 15.4 | 5.6 | 12.34 | 42.2% | 21.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,467 | 24.5 | 15.4 | 30.4 | 17.6 | 9.1 | 2.7 | 0.3 | 6.68 | 12.1% | 3.0% |
| WTA125 | 1,107 | 24.9 | 12.7 | 21.1 | 18.9 | 13.6 | 7.1 | 1.6 | 7.88 | 22.4% | 8.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,323 | 27.7 | 15.6 | 27.9 | 13.4 | 11.3 | 3.7 | 0.4 | 5.88 | 15.4% | 4.0% |
| CHALLENGER | 4,152 | 21.2 | 12.3 | 26.0 | 17.6 | 15.3 | 6.1 | 1.5 | 8.04 | 22.9% | 7.6% |
| ITF_MEN | 8,168 | 12.0 | 8.8 | 20.6 | 17.1 | 22.0 | 14.3 | 5.2 | 12.39 | 41.5% | 19.5% |
| ITF_WOMEN | 11,659 | 11.6 | 8.5 | 18.4 | 17.3 | 24.0 | 15.1 | 5.2 | 13.3 | 44.2% | 20.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,382 | 18.5 | 13.6 | 25.0 | 20.1 | 16.2 | 5.9 | 0.6 | 8.18 | 22.7% | 6.4% |
| WTA125 | 1,057 | 16.5 | 7.5 | 21.9 | 19.3 | 21.0 | 12.1 | 1.7 | 11.03 | 34.8% | 13.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,323 | 26.4 | 15.7 | 25.8 | 16.1 | 11.9 | 3.7 | 0.5 | 6.2 | 16.0% | 4.2% |
| CHALLENGER | 4,152 | 19.2 | 11.5 | 22.9 | 16.8 | 18.6 | 9.1 | 1.9 | 9.02 | 29.5% | 11.0% |
| ITF_MEN | 8,169 | 9.5 | 7.2 | 17.4 | 16.1 | 21.4 | 18.8 | 9.6 | 14.95 | 49.8% | 28.5% |
| ITF_WOMEN | 11,660 | 8.9 | 6.8 | 15.9 | 14.2 | 22.7 | 20.7 | 10.8 | 16.59 | 54.2% | 31.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,382 | 15.4 | 11.0 | 22.3 | 15.4 | 22.2 | 12.5 | 1.2 | 10.45 | 35.9% | 13.7% |
| WTA125 | 1,057 | 9.7 | 6.4 | 16.8 | 16.5 | 24.3 | 17.8 | 8.6 | 15.19 | 50.7% | 26.4% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,944 | 24.6 | 19.2 | 31.3 | 13.0 | 8.7 | 2.8 | 0.4 | 5.67 | 11.9% | 3.2% |
| CHALLENGER | 3,539 | 24.1 | 15.5 | 28.4 | 14.8 | 12.8 | 4.0 | 0.5 | 6.59 | 17.3% | 4.5% |
| DOUBLES | 1,990 | 5.0 | 4.5 | 12.5 | 10.9 | 20.9 | 24.8 | 21.4 | 23.35 | 67.1% | 46.2% |
| ITF_MEN | 7,239 | 13.8 | 10.0 | 22.9 | 16.4 | 21.2 | 11.8 | 3.8 | 10.94 | 36.9% | 15.7% |
| ITF_WOMEN | 8,605 | 13.7 | 9.7 | 21.0 | 16.4 | 21.3 | 14.4 | 3.5 | 11.55 | 39.2% | 17.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,413 | 24.8 | 15.8 | 30.4 | 17.6 | 9.1 | 2.1 | 0.1 | 6.53 | 11.3% | 2.2% |
| WTA125 | 982 | 26.3 | 13.5 | 22.1 | 20.0 | 12.6 | 5.0 | 0.5 | 7.33 | 18.1% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,121 | 5.1 | 4.4 | 12.2 | 10.8 | 21.1 | 24.9 | 21.5 | 23.54 | 67.5% | 46.4% |
| singles | 27,326 | 16.4 | 11.3 | 22.9 | 15.6 | 18.2 | 11.4 | 4.2 | 9.85 | 33.9% | 15.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,910 | 13.1 | 9.3 | 20.2 | 15.6 | 19.1 | 13.8 | 9.0 | 12.35 | 41.9% | 22.8% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 26,106 | 13.4 | 8.7 | 18.6 | 15.1 | 19.3 | 15.1 | 10.0 | 13.0 | 44.3% | 25.0% |
| UNKNOWN | 5,529 | 10.4 | 7.7 | 17.1 | 16.6 | 21.1 | 16.0 | 11.1 | 14.19 | 48.2% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,998 | 20.0 | 12.1 | 22.4 | 15.6 | 14.7 | 9.2 | 6.0 | 8.59 | 30.0% | 15.3% |
| B | 4,913 | 12.8 | 9.1 | 19.2 | 15.9 | 19.3 | 12.7 | 11.1 | 12.59 | 43.0% | 23.8% |
| C | 5,709 | 11.9 | 8.9 | 19.9 | 15.8 | 18.6 | 14.3 | 10.6 | 12.8 | 43.5% | 24.9% |
| D | 6,300 | 12.0 | 8.2 | 17.5 | 15.4 | 21.6 | 15.9 | 9.3 | 13.79 | 46.8% | 25.2% |
| F | 11,874 | 7.4 | 5.6 | 15.0 | 14.7 | 23.3 | 21.0 | 13.0 | 17.71 | 57.3% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,809 | 24.1 | 15.7 | 28.9 | 15.2 | 11.0 | 3.7 | 1.3 | 6.53 | 16.1% | 5.0% |
| B | 4,166 | 17.0 | 10.7 | 24.1 | 16.6 | 18.8 | 9.7 | 3.1 | 9.59 | 31.6% | 12.8% |
| C | 5,756 | 11.2 | 7.9 | 19.5 | 14.7 | 21.0 | 15.7 | 10.1 | 13.45 | 46.7% | 25.8% |
| D | 4,327 | 14.3 | 9.9 | 21.7 | 15.4 | 20.0 | 13.2 | 5.4 | 11.26 | 38.6% | 18.6% |
| F | 7,389 | 9.9 | 8.3 | 16.0 | 14.9 | 23.2 | 20.0 | 7.7 | 15.44 | 50.8% | 27.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,471 | 18.3 | 11.0 | 21.4 | 15.3 | 15.2 | 10.0 | 8.8 | 9.77 | 34.0% | 18.9% |
| LIMITED | 8,780 | 13.5 | 10.0 | 20.4 | 16.2 | 19.0 | 13.2 | 7.6 | 11.71 | 39.8% | 20.8% |
| POOR | 18,543 | 9.0 | 6.5 | 16.0 | 15.0 | 22.7 | 19.1 | 11.7 | 16.17 | 53.5% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,559 | 24.1 | 18.1 | 33.0 | 15.0 | 6.6 | 2.7 | 0.4 | 5.85 | 9.8% | 3.1% |
| GAME_SPREAD | 5,918 | 22.1 | 15.2 | 33.0 | 17.2 | 9.0 | 3.0 | 0.6 | 6.74 | 12.6% | 3.5% |
| MATCH_WINNER | 29,447 | 15.6 | 10.8 | 22.1 | 15.3 | 18.4 | 12.4 | 5.5 | 10.37 | 36.3% | 17.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,710 | 27.5 | 16.7 | 31.0 | 12.5 | 9.5 | 2.5 | 0.3 | 5.67 | 12.3% | 2.8% |
| TOTAL_GAMES | 9,867 | 9.7 | 10.4 | 35.8 | 26.8 | 10.5 | 4.0 | 2.8 | 9.29 | 17.4% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,203 | 24.4 | 30.1 | 32.9 | 7.3 | 4.1 | 0.9 | 0.3 | 4.7 | 5.3% | 1.2% |
| GAME_SPREAD | 8,072 | 47.3 | 16.0 | 25.3 | 7.3 | 2.2 | 1.3 | 0.6 | 3.27 | 4.1% | 1.9% |
| TOTAL_GAMES | 14,245 | 6.5 | 9.3 | 40.3 | 31.4 | 7.2 | 3.2 | 2.2 | 9.31 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,214 | 23.9 | 16.8 | 34.8 | 14.3 | 7.1 | 2.6 | 0.4 | 6.01 | 10.2% | 3.0% |
| GAME_SPREAD | 8,075 | 20.2 | 13.5 | 27.9 | 20.5 | 12.5 | 4.3 | 1.1 | 7.79 | 17.9% | 5.4% |
| TOTAL_GAMES | 14,275 | 10.0 | 10.2 | 36.3 | 25.3 | 11.5 | 4.2 | 2.4 | 9.17 | 18.2% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 39,794 | 44.4% | 24.9% | 13.03 | 35.5% | 15.3% | 10.72 |
| gen1_elo | 39,794 | 44.2% | 24.7% | 12.95 | 35.2% | 15.3% | 10.54 |
| gen1_sr | 39,794 | 52.1% | 31.4% | 15.88 | 44.1% | 21.8% | 13.02 |
| gen2 | 39,794 | 51.0% | 31.7% | 15.47 | 44.1% | 23.4% | 12.9 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,643 | 15.6 | 10.6 | 21.3 | 17.2 | 20.1 | 12.0 | 3.3 | 10.71 | 35.4% | 15.3% |
| STALE | 21,151 | 10.5 | 7.1 | 16.3 | 13.8 | 19.0 | 17.6 | 15.7 | 15.97 | 52.3% | 33.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 22,915 | 16.3 | 11.1 | 22.8 | 15.4 | 17.9 | 11.9 | 4.7 | 9.95 | 34.4% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 69,241 | 22915 | 22115 | 24211 | 24.4 | 126.8 | 1451.1 |
| ge_15pp | 28,343 | 7889 | 7884 | 12570 | 26.9 | 439.3 | 1451.1 |
| ge_25pp | 15,157 | 3799 | 3443 | 7915 | 32.1 | 586.7 | 1431.1 |
| lt_10pp | 30,294 | 11496 | 10480 | 8318 | 22.4 | 47.1 | 1421.1 |

Current slate `SL-20261030T065348Z-9c678be2`: 379 priced rows, quote age at build {'median': 17.0, 'max': 17.1}, freshness {'AGING': 379}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 45 | 0.0 | 0.0 | 31.1 | 6.7 | 35.6 | 22.2 | 4.4 | 20.19 | 62.2% | 26.7% |
| EXTERNAL_LONE_OUTLIER | 24 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.37 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,919 | 19.6 | 11.1 | 25.3 | 18.0 | 17.9 | 7.2 | 0.9 | 8.64 | 26.1% | 8.1% |
| KALSHI_LONE_OUTLIER | 26 | 3.9 | 3.9 | 76.9 | 7.7 | 3.9 | 3.9 | 0.0 | 6.31 | 7.7% | 3.9% |
| MARKETS_AGREE | 776 | 65.5 | 34.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,692 | 0.0 | 2.4 | 36.3 | 25.4 | 24.9 | 10.1 | 0.9 | 12.12 | 35.9% | 11.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 39,794 | 6482 (16.3%) | 26.1% | 1.1% | {"EXTERNAL_STALE": 3919, "AGREES_WITH_KALSHI": 1692, "ALL_AGREE": 776, "SUPPORTS_MODEL_DIRECTION": 44, "AGREES_WITH_MODEL": 26, "EXTERNAL_OUTLIER": 24, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 17,655 | 1659 (9.4%) | 36.6% | 1.8% | {"EXTERNAL_STALE": 1021, "AGREES_WITH_KALSHI": 608, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,896 | 518 (5.2%) | 35.9% | 2.5% | {"EXTERNAL_STALE": 319, "AGREES_WITH_KALSHI": 186, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,707 | 491 (10.4%) | 36.5% | 2.6% | {"EXTERNAL_STALE": 299, "AGREES_WITH_KALSHI": 179, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 16,029 | 3684 (23.0%) | 17.8% | 0.9% | {"EXTERNAL_STALE": 2194, "ALL_AGREE": 776, "AGREES_WITH_KALSHI": 654, "EXTERNAL_OUTLIER": 24, "AGREES_WITH_MODEL": 22, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,798 | 10.4 | 7.5 | 19.7 | 14.3 | 21.6 | 16.6 | 10.0 | 14.12 | 48.1% | 26.6% |
| 4-10x | 5,380 | 11.1 | 8.5 | 18.6 | 15.6 | 21.9 | 14.4 | 9.9 | 13.66 | 46.2% | 24.3% |
| <2x | 20,113 | 15.2 | 10.0 | 19.5 | 16.0 | 17.4 | 13.1 | 9.0 | 11.58 | 39.4% | 22.1% |
| >=10x | 6,503 | 10.5 | 6.4 | 15.2 | 14.4 | 21.6 | 19.3 | 12.6 | 16.33 | 53.5% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,223 | 12.7 | 8.8 | 19.6 | 16.0 | 19.0 | 13.5 | 10.5 | 12.69 | 42.9% | 24.0% |
| 300-1000 | 8,625 | 12.0 | 8.7 | 17.8 | 15.3 | 20.3 | 16.4 | 9.6 | 13.61 | 46.3% | 26.0% |
| <300 | 12,835 | 8.2 | 5.8 | 15.2 | 14.8 | 23.0 | 20.1 | 12.9 | 17.07 | 56.0% | 32.9% |
| >=3000 | 8,111 | 21.6 | 13.1 | 24.0 | 15.5 | 13.8 | 7.2 | 4.9 | 7.56 | 25.8% | 12.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1147 | 0.5499 | 0.4109 | 0.4978 | +0.052 | -0.087 | -0.0019 ± 0.0046 |
| ratio 4-10x | 793 | 0.58 | 0.4339 | 0.4943 | +0.086 | -0.060 | 0.0079 ± 0.0056 |
| ratio <2x | 2752 | 0.538 | 0.4147 | 0.4469 | +0.091 | -0.032 | 0.0123 ± 0.0028 |
| ratio >=10x | 991 | 0.568 | 0.3935 | 0.4521 | +0.116 | -0.059 | 0.0134 ± 0.0058 |
| thinner_sample 1000-3000 | 1546 | 0.5402 | 0.413 | 0.4515 | +0.089 | -0.038 | 0.0098 ± 0.0037 |
| thinner_sample 300-1000 | 1294 | 0.5673 | 0.4256 | 0.4861 | +0.081 | -0.060 | 0.0027 ± 0.0044 |
| thinner_sample <300 | 1905 | 0.5595 | 0.3918 | 0.4614 | +0.098 | -0.070 | 0.0107 ± 0.0041 |
| thinner_sample >=3000 | 938 | 0.5319 | 0.438 | 0.4638 | +0.068 | -0.026 | 0.0129 ± 0.0037 |
| data_status ADEQUATE | 1545 | 0.5345 | 0.4316 | 0.4505 | +0.084 | -0.019 | 0.0131 ± 0.0031 |
| data_status LIMITED | 1380 | 0.5493 | 0.4159 | 0.4732 | +0.076 | -0.057 | 0.0065 ± 0.0041 |
| data_status POOR | 2758 | 0.5621 | 0.4009 | 0.4685 | +0.094 | -0.068 | 0.0079 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 826 | 0.1993 | 0.1997 | -0.0004 ± 0.0005 | 0.5782 | 0.5795 | 0.5045 | 0.4893 | 0.5097 | -0.088 ± 0.0165 | -0.01 (5) |
| 3-5 | 520 | 0.2055 | 0.206 | -0.0005 ± 0.0016 | 0.5936 | 0.5934 | 0.5034 | 0.4635 | 0.4885 | -0.094 ± 0.0203 | 0.02 (1) |
| 5-10 | 1193 | 0.2015 | 0.2019 | -0.0004 ± 0.0019 | 0.589 | 0.5874 | 0.5108 | 0.4371 | 0.4744 | -0.085 ± 0.0134 | -0.0167 (6) |
| 10-15 | 997 | 0.2206 | 0.2119 | +0.0087 ± 0.0036 | 0.6337 | 0.6091 | 0.5273 | 0.4037 | 0.4293 | -0.108 ± 0.0147 | -0.048 (5) |
| 15-25 | 1258 | 0.2252 | 0.2125 | +0.0126 ± 0.0051 | 0.6461 | 0.6092 | 0.5767 | 0.3812 | 0.4467 | -0.100 ± 0.013 | -0.0033 (9) |
| 25-40 | 734 | 0.2229 | 0.2054 | +0.0175 ± 0.01 | 0.6354 | 0.5922 | 0.6547 | 0.3444 | 0.4714 | -0.076 ± 0.0153 | -0.01 (1) |
| 40+ | 155 | 0.2842 | 0.1885 | +0.0957 ± 0.0305 | 0.7739 | 0.5561 | 0.7384 | 0.2901 | 0.4129 | -0.076 ± 0.0302 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4524 | 0.1843 | 0.1852 | -0.0008 ± 0.0002 | 0.5431 | 0.5442 | 0.4875 | 0.4723 | 0.5024 | -0.023 ± 0.0065 | -0.0129 (17) |
| 3-5 | 3042 | 0.1955 | 0.1937 | +0.0018 ± 0.0006 | 0.5701 | 0.5634 | 0.4821 | 0.4423 | 0.4382 | -0.059 ± 0.0081 | 0.0 (2) |
| 5-10 | 6460 | 0.2026 | 0.1992 | +0.0034 ± 0.0008 | 0.5911 | 0.5794 | 0.4849 | 0.4113 | 0.4259 | -0.045 ± 0.0056 | -0.0119 (21) |
| 10-15 | 5390 | 0.2014 | 0.1854 | +0.0160 ± 0.0015 | 0.589 | 0.5452 | 0.4843 | 0.3603 | 0.3571 | -0.067 ± 0.0059 | -0.0281 (16) |
| 15-25 | 6733 | 0.2064 | 0.1679 | +0.0385 ± 0.002 | 0.6053 | 0.4981 | 0.4995 | 0.3034 | 0.304 | -0.070 ± 0.005 | -0.0025 (44) |
| 25-40 | 5320 | 0.2217 | 0.1249 | +0.0968 ± 0.003 | 0.6375 | 0.3841 | 0.5255 | 0.2114 | 0.2186 | -0.060 ± 0.0047 | -0.01 (1) |
| 40+ | 3490 | 0.3848 | 0.0449 | +0.3399 ± 0.0041 | 1.0025 | 0.1737 | 0.6332 | 0.1041 | 0.0596 | -0.079 ± 0.0034 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 654 | 0.2052 | 0.2059 | -0.0007 ± 0.0006 | 0.5919 | 0.5937 | 0.508 | 0.4931 | 0.5229 | -0.100 ± 0.0192 | -0.01 (3) |
| 3-5 | 464 | 0.2208 | 0.2182 | +0.0026 ± 0.0017 | 0.626 | 0.6208 | 0.512 | 0.4724 | 0.4547 | -0.128 ± 0.0231 | 0.02 (1) |
| 5-10 | 1044 | 0.2085 | 0.2078 | +0.0007 ± 0.0021 | 0.6037 | 0.6008 | 0.5441 | 0.4694 | 0.5038 | -0.088 ± 0.0145 | -0.01 (4) |
| 10-15 | 924 | 0.2164 | 0.2103 | +0.0061 ± 0.0038 | 0.6237 | 0.6077 | 0.564 | 0.4396 | 0.4794 | -0.106 ± 0.0158 | -0.04 (5) |
| 15-25 | 1317 | 0.23 | 0.2141 | +0.0159 ± 0.005 | 0.6549 | 0.6124 | 0.5831 | 0.3877 | 0.4472 | -0.096 ± 0.013 | -0.0133 (9) |
| 25-40 | 932 | 0.2679 | 0.1968 | +0.0711 ± 0.0091 | 0.7478 | 0.5741 | 0.658 | 0.3439 | 0.3906 | -0.133 ± 0.0145 | -0.0075 (4) |
| 40+ | 348 | 0.3628 | 0.1666 | +0.1961 ± 0.0217 | 0.9945 | 0.5008 | 0.7323 | 0.247 | 0.3017 | -0.081 ± 0.0212 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3902 | 0.1895 | 0.1898 | -0.0002 ± 0.0002 | 0.554 | 0.5542 | 0.5095 | 0.4945 | 0.5097 | -0.041 ± 0.0072 | -0.0133 (15) |
| 3-5 | 2637 | 0.1964 | 0.1953 | +0.0012 ± 0.0007 | 0.5698 | 0.5661 | 0.5111 | 0.4715 | 0.4748 | -0.049 ± 0.0088 | 0.02 (1) |
| 5-10 | 5743 | 0.199 | 0.1956 | +0.0034 ± 0.0009 | 0.5835 | 0.5706 | 0.5104 | 0.4363 | 0.4538 | -0.042 ± 0.0059 | -0.0117 (6) |
| 10-15 | 4826 | 0.2046 | 0.1927 | +0.0120 ± 0.0016 | 0.5987 | 0.5628 | 0.5125 | 0.3886 | 0.4032 | -0.053 ± 0.0064 | -0.0189 (18) |
| 15-25 | 6750 | 0.2173 | 0.1811 | +0.0361 ± 0.002 | 0.632 | 0.5313 | 0.5231 | 0.3277 | 0.3363 | -0.062 ± 0.0052 | -0.0086 (42) |
| 25-40 | 6211 | 0.2512 | 0.1357 | +0.1155 ± 0.003 | 0.7087 | 0.4164 | 0.5572 | 0.2404 | 0.2201 | -0.086 ± 0.0047 | -0.0044 (18) |
| 40+ | 4890 | 0.3988 | 0.0587 | +0.3401 ± 0.004 | 1.0526 | 0.2116 | 0.652 | 0.1171 | 0.0802 | -0.074 ± 0.0034 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 791 | 0.1957 | 0.1979 | -0.0022 ± 0.0006 | 0.5701 | 0.5757 | 0.4996 | 0.4842 | 0.5449 | -0.037 ± 0.0165 | -0.0137 (8) |
| 3-5 | 552 | 0.2054 | 0.2037 | +0.0017 ± 0.0016 | 0.5937 | 0.5878 | 0.495 | 0.4553 | 0.4547 | -0.119 ± 0.0199 | 0.0067 (3) |
| 5-10 | 1233 | 0.2036 | 0.2017 | +0.0019 ± 0.0019 | 0.5931 | 0.5863 | 0.51 | 0.4362 | 0.459 | -0.096 ± 0.0132 | -0.0071 (7) |
| 10-15 | 1000 | 0.2089 | 0.2043 | +0.0046 ± 0.0035 | 0.6076 | 0.5923 | 0.5396 | 0.4163 | 0.461 | -0.096 ± 0.0143 | -0.0317 (6) |
| 15-25 | 1193 | 0.2342 | 0.2172 | +0.0170 ± 0.0052 | 0.6676 | 0.6195 | 0.5883 | 0.3941 | 0.4476 | -0.111 ± 0.0135 | -0.03 (1) |
| 25-40 | 751 | 0.2131 | 0.2123 | +0.0008 ± 0.0099 | 0.6149 | 0.6082 | 0.6628 | 0.3523 | 0.5047 | -0.060 ± 0.0152 | 0.015 (2) |
| 40+ | 163 | 0.2995 | 0.196 | +0.1035 ± 0.0306 | 0.8153 | 0.5732 | 0.7492 | 0.2987 | 0.4172 | -0.077 ± 0.0316 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4333 | 0.1838 | 0.1844 | -0.0006 ± 0.0002 | 0.5409 | 0.5421 | 0.4831 | 0.4679 | 0.4858 | -0.034 ± 0.0066 | -0.0163 (35) |
| 3-5 | 2991 | 0.2019 | 0.1996 | +0.0022 ± 0.0007 | 0.5867 | 0.579 | 0.4804 | 0.4409 | 0.433 | -0.064 ± 0.0083 | -0.0094 (18) |
| 5-10 | 6626 | 0.1947 | 0.1908 | +0.0039 ± 0.0008 | 0.5726 | 0.5591 | 0.4853 | 0.4113 | 0.4224 | -0.048 ± 0.0054 | -0.01 (31) |
| 10-15 | 5377 | 0.1923 | 0.1789 | +0.0133 ± 0.0014 | 0.5686 | 0.5298 | 0.4943 | 0.3709 | 0.3781 | -0.057 ± 0.0058 | -0.015 (12) |
| 15-25 | 6856 | 0.2132 | 0.1732 | +0.0400 ± 0.002 | 0.621 | 0.5103 | 0.513 | 0.3184 | 0.3145 | -0.074 ± 0.005 | -0.03 (2) |
| 25-40 | 5307 | 0.2162 | 0.1283 | +0.0879 ± 0.0031 | 0.6258 | 0.3921 | 0.5292 | 0.2138 | 0.2344 | -0.049 ± 0.0047 | 0.01 (3) |
| 40+ | 3469 | 0.3947 | 0.0504 | +0.3443 ± 0.0043 | 1.0294 | 0.1879 | 0.6427 | 0.1108 | 0.0663 | -0.079 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1188 | 0.196 | 0.1961 | -0.0001 ± 0.0004 | 0.5706 | 0.5707 | 0.5047 | 0.4896 | 0.4941 | -0.068 ± 0.0131 | -0.0224 (49) |
| 3-5 | 849 | 0.1874 | 0.1865 | +0.0009 ± 0.0012 | 0.5492 | 0.5465 | 0.4969 | 0.4571 | 0.4641 | -0.068 ± 0.0152 | -0.0194 (34) |
| 5-10 | 1756 | 0.2017 | 0.1967 | +0.0049 ± 0.0016 | 0.5924 | 0.5769 | 0.5014 | 0.4277 | 0.4317 | -0.077 ± 0.0108 | -0.005 (78) |
| 10-15 | 1203 | 0.2164 | 0.2041 | +0.0123 ± 0.0032 | 0.6252 | 0.5921 | 0.5373 | 0.4145 | 0.4239 | -0.087 ± 0.0134 | 0.0014 (64) |
| 15-25 | 1546 | 0.2319 | 0.211 | +0.0209 ± 0.0046 | 0.661 | 0.6069 | 0.583 | 0.3884 | 0.4347 | -0.084 ± 0.0118 | -0.0214 (59) |
| 25-40 | 968 | 0.2448 | 0.21 | +0.0348 ± 0.009 | 0.6995 | 0.6021 | 0.6843 | 0.3723 | 0.4731 | -0.096 ± 0.0139 | -0.0219 (26) |
| 40+ | 327 | 0.3343 | 0.2031 | +0.1312 ± 0.024 | 0.9686 | 0.5915 | 0.8158 | 0.3392 | 0.4557 | -0.099 ± 0.0225 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4455 | 0.176 | 0.1763 | -0.0003 ± 0.0002 | 0.521 | 0.5213 | 0.5088 | 0.4935 | 0.5062 | -0.037 ± 0.0063 | -0.0157 (88) |
| 3-5 | 3067 | 0.1936 | 0.1921 | +0.0015 ± 0.0006 | 0.5635 | 0.5605 | 0.5031 | 0.4634 | 0.464 | -0.051 ± 0.008 | -0.0209 (69) |
| 5-10 | 6231 | 0.1989 | 0.1918 | +0.0071 ± 0.0008 | 0.5847 | 0.5641 | 0.4972 | 0.4235 | 0.4141 | -0.067 ± 0.0056 | -0.0082 (132) |
| 10-15 | 4361 | 0.2114 | 0.1956 | +0.0158 ± 0.0017 | 0.6138 | 0.5724 | 0.5355 | 0.4126 | 0.4089 | -0.070 ± 0.0068 | -0.0053 (105) |
| 15-25 | 5285 | 0.2296 | 0.2009 | +0.0287 ± 0.0024 | 0.6604 | 0.5813 | 0.5697 | 0.3745 | 0.3996 | -0.063 ± 0.0062 | -0.0253 (107) |
| 25-40 | 3555 | 0.2613 | 0.1866 | +0.0747 ± 0.0046 | 0.739 | 0.5446 | 0.6364 | 0.3237 | 0.3634 | -0.081 ± 0.0071 | -0.0229 (51) |
| 40+ | 1530 | 0.378 | 0.154 | +0.2240 ± 0.0104 | 1.0706 | 0.4605 | 0.741 | 0.2394 | 0.2778 | -0.074 ± 0.0095 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5683 | 1.013 ± 0.037 | 1.088 | 0.1695 | 0.1666 | 0.2151 | 0.2061 |
| gen2 | 5683 | 0.804 ± 0.034 | 1.052 | 0.1715 | 0.167 | 0.2346 | 0.206 |
| gen1_elo | 5683 | 0.989 ± 0.036 | 1.085 | 0.176 | 0.1668 | 0.214 | 0.2063 |
| gen1_sr | 5683 | 0.986 ± 0.044 | 1.11 | 0.1317 | 0.1689 | 0.2305 | 0.2056 |
| gen1_ledger | 7837 | 0.853 ± 0.027 | 1.056 | 0.1879 | 0.1761 | 0.2184 | 0.2014 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 28,343)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,395 | 22.6% |
| STALE_QUOTE | market_freshness | 6,203 | 21.9% |
| BOOK_QUALITY | execution | 5,368 | 18.9% |
| POOR_DATA | data | 3,318 | 11.7% |
| LIMITED_DATA | data | 1,759 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,617 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,222 | 4.3% |
| IDENTITY_AMBIGUOUS | mapping | 1,154 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 818 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 488 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.6%, market_freshness 21.9%, execution 18.9%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.3%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.8%, THIN_PLAYER_HISTORY 60.5%, STALE_PLAYER_DATA 52.4%, STALE_KALSHI_QUOTE 44.4%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.0%, MODEL_HIGH_UNCERTAINTY 18.1%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.4%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.6%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 15,157)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,166 | 34.1% |
| STALE_QUOTE | market_freshness | 2,832 | 18.7% |
| BOOK_QUALITY | execution | 2,799 | 18.5% |
| POOR_DATA | data | 1,420 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 847 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 616 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 529 | 3.5% |
| LIMITED_DATA | data | 518 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 306 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 123 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.1%, market_freshness 18.7%, execution 18.5%, data 12.8%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.7%, STALE_KALSHI_QUOTE 52.2%, STALE_PLAYER_DATA 46.4%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.5%, MODEL_HIGH_UNCERTAINTY 18.8%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.2%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.1%, POST_SETTLEMENT_OBSERVATION 34.1%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12053, "IDENTITY_AMBIGUOUS": 3104}; ticker orientation: {"VERIFIED": 15157}.

Checks: discipline:AMBIGUOUS 985, discipline:PASS 14172, identity_confidence:AMBIGUOUS 2783, identity_confidence:PASS 12374, level_mapping:NA 997, level_mapping:PASS 14160, market_pair:AMBIGUOUS 480, market_pair:NA 347, market_pair:PASS 14330, model_complement:NA 311, model_complement:PASS 14846, namesake:AMBIGUOUS 6, namesake:PASS 15151, physical_match_id:NA 5261, physical_match_id:PASS 9896, player_ids:PASS 15157, same_pair_other_event:PASS 15157, ticker_orientation:PASS 15157

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,420 | 4.2% | 3.7% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.84 | 0.2219 / 0.2176 (635) | 21.7% | 2.9% | 3.2% | 2.8% |
| CHALLENGER | 9,946 | 16.5% | 6.2% | 10.8% | {"coverage": 972, "market_freshness/coverage": 196, "market_freshness": 168, "data": 144, "model_calibration_or_unknown": 74, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.26 | 0.2211 / 0.2118 (2279) | 35.4% | 15.7% | 4.1% | 22.7% |
| DOUBLES | 2,121 | 46.4% | 46.2% | 6.5% | {"execution": 560, "mapping": 253, "market_freshness": 106, "market_freshness/coverage": 59, "coverage": 7} | 23.35 | 0.3096 / 0.2385 (513) | 11.0% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 19,641 | 25.1% | 17.7% | 32.5% | {"coverage": 1733, "execution": 912, "market_freshness": 897, "data": 727, "market_freshness/coverage": 466, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.72 | 0.2165 / 0.1994 (4036) | 37.7% | 69.8% | 16.6% | 21.6% |
| ITF_WOMEN | 25,827 | 26.7% | 19.3% | 45.4% | {"coverage": 2398, "market_freshness": 1456, "execution": 1213, "data": 974, "market_freshness/coverage": 585, "mapping": 157, "model_calibration_or_unknown": 81, "model_calibration": 21} | 12.57 | 0.2039 / 0.1956 (4750) | 39.6% | 57.3% | 10.0% | 21.5% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,931 | 5.7% | 4.9% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "coverage": 30, "execution": 27, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.48 | 0.2371 / 0.2301 (607) | 26.4% | 1.1% | 1.4% | 3.5% |
| WTA125 | 2,200 | 11.5% | 9.8% | 1.7% | {"market_freshness": 71, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 15, "coverage": 12, "mapping": 4} | 9.17 | 0.2103 / 0.1925 (658) | 25.7% | 11.1% | 4.9% | 7.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 117 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 164 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 49 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 50 | `KXATPDOUBLES-26OCT29MICVANARROLI-MICVAN` | DOUBLES | gen1_ledger | 98% / 20% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9702, "by_level_share_of_ge_25pp": {"ATP": 0.015, "CHALLENGER": 0.1085, "DOUBLES": 0.065, "ITF_MEN": 0.325, "ITF_WOMEN": 0.4542, "OTHER": 0.0008, "WTA": 0.0148, "WTA125": 0.0167}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5222, "share_primary_cause_market_settled_or_in_play": 0.4316, "share_primary_cause_stale_quote_only": 0.1868}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15157, "identity_ambiguous_share": 0.2048, "ticker_orientation": {"VERIFIED": 15157}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9896, "with_external": 518, "coverage": 0.0523, "external_status": {"EXTERNAL_STALE": 319, "AGREES_WITH_KALSHI": 186, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 319, "MODEL_LONE_OUTLIER": 186, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3591, "share_external_supports_model": 0.0251}, "pregame_clean_ge_25pp": {"n": 4707, "with_external": 491, "coverage": 0.1043, "external_status": {"EXTERNAL_STALE": 299, "AGREES_WITH_KALSHI": 179, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 299, "MODEL_LONE_OUTLIER": 179, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3646, "share_external_supports_model": 0.0265}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 473.0, "median_sample_ratio": 2.5, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2104, "data_status": {"POOR": 8600, "LIMITED": 3904, "ADEQUATE": 2653}, "comparison_lt_10pp": {"median_thinner_serve_points": 1669.0, "median_sample_ratio": 1.72, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1147, "model_minus_observed": 0.0521, "kalshi_minus_observed": -0.0869, "brier_diff_model_minus_kalshi": -0.0019}, "4-10x": {"n": 793, "model_minus_observed": 0.0857, "kalshi_minus_observed": -0.0605, "brier_diff_model_minus_kalshi": 0.0079}, "<2x": {"n": 2752, "model_minus_observed": 0.091, "kalshi_minus_observed": -0.0323, "brier_diff_model_minus_kalshi": 0.0123}, ">=10x": {"n": 991, "model_minus_observed": 0.1159, "kalshi_minus_observed": -0.0585, "brier_diff_model_minus_kalshi": 0.0134}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5683, "model": {"intercept": -0.533, "slope": 0.804, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.193, "slope": 1.052, "slope_se": 0.037}, "mean_extremity_model": 0.1715, "mean_extremity_kalshi": 0.167, "model_brier": 0.2346, "kalshi_brier": 0.206, "brier_diff_model_minus_kalshi": 0.0286, "brier_diff_se": 0.0025, "model_logloss": 0.6668, "kalshi_logloss": 0.5949}, "fair_v1": {"n": 5683, "model": {"intercept": -0.415, "slope": 1.013, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.279, "slope": 1.088, "slope_se": 0.038}, "mean_extremity_model": 0.1695, "mean_extremity_kalshi": 0.1666, "model_brier": 0.2151, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.009, "brier_diff_se": 0.0021, "model_logloss": 0.6194, "kalshi_logloss": 0.5952}, "gen1_elo": {"n": 5683, "model": {"intercept": -0.392, "slope": 0.989, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.298, "slope": 1.085, "slope_se": 0.037}, "mean_extremity_model": 0.176, "mean_extremity_kalshi": 0.1668, "model_brier": 0.214, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0077, "brier_diff_se": 0.0021, "model_logloss": 0.6174, "kalshi_logloss": 0.5955}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2487, "share_ge_15": 0.4437, "median_abs_gap": 13.03, "n": 39794}, "gen1_elo": {"share_ge_25": 0.2467, "share_ge_15": 0.4416, "median_abs_gap": 12.95, "n": 39794}, "gen1_sr": {"share_ge_25": 0.3137, "share_ge_15": 0.5209, "median_abs_gap": 15.88, "n": 39794}, "gen2": {"share_ge_25": 0.3166, "share_ge_15": 0.5105, "median_abs_gap": 15.47, "n": 39794}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1531, "share_ge_15": 0.3552, "median_abs_gap": 10.72, "n": 30747}, "gen1_elo": {"share_ge_25": 0.1529, "share_ge_15": 0.352, "median_abs_gap": 10.54, "n": 30746}, "gen1_sr": {"share_ge_25": 0.2177, "share_ge_15": 0.4412, "median_abs_gap": 13.02, "n": 30749}, "gen2": {"share_ge_25": 0.2342, "share_ge_15": 0.4406, "median_abs_gap": 12.9, "n": 30749}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0419, "share_ge_25_pregame_clean": 0.0374}, "WTA": {"median_abs_gap_pregame_clean": 7.48, "share_ge_25_all": 0.0572, "share_ge_25_pregame_clean": 0.0485}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2363, "share_within_10pp_all": 0.4375, "share_within_10pp_pregame_clean": 0.4904, "corr_model_vs_mid_pregame_clean": 0.8506}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 826, "model_brier": 0.1993, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 997, "model_brier": 0.2206, "kalshi_brier": 0.2119, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1258, "model_brier": 0.2252, "kalshi_brier": 0.2125, "brier_diff_model_minus_kalshi": 0.0126}, "25-40": {"n_settled": 734, "model_brier": 0.2229, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0175}, "3-5": {"n_settled": 520, "model_brier": 0.2055, "kalshi_brier": 0.206, "brier_diff_model_minus_kalshi": -0.0005}, "40+": {"n_settled": 155, "model_brier": 0.2842, "kalshi_brier": 0.1885, "brier_diff_model_minus_kalshi": 0.0957}, "5-10": {"n_settled": 1193, "model_brier": 0.2015, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": -0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.533, "slope": 0.804, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.193, "slope": 1.052, "slope_se": 0.037}, "n": 5683}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.491, "slope": 0.853, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.163, "slope": 1.056, "slope_se": 0.031}, "n": 7837}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 513, "model_brier": 0.3096, "kalshi_brier": 0.2385, "brier_diff_model_minus_kalshi": 0.0711, "brier_diff_se": 0.0132, "corr_model_outcome": 0.0557, "corr_kalshi_outcome": 0.2264}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
