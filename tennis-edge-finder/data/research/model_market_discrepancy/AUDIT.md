# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-28T12:31Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 64,167): 0-3 14.1%, 3-5 9.6%, 5-10 20.0%, 10-15 15.4%, 15-25 19.0%, 25-40 13.9%, 40+ 7.9%; median gap 11.89 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.2%, Challenger 11.4%, doubles 6.5%). Main tour: ATP 4.3% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 14,026): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.1%, STALE_QUOTE 18.9%, BOOK_QUALITY 18.9%, POOR_DATA 9.5%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.9%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.1%, market_freshness 18.9%, execution 18.9%, data 13.0%, market_freshness/coverage 9.0%, mapping 4.1%, model_calibration_or_unknown 2.2%, model_calibration 0.9%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 14,026 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.1% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 451.0 points vs 1693.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.013, Gen-2 0.8, Gen-1 ledger 0.852 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 673 model 0.2234 vs Kalshi 0.2089; n 142 model 0.2739 vs Kalshi 0.1928.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 276,151 model-market comparisons (449,152 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 92,658 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-28T12:13:58.141325+00:00'], shadow board 73,308 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-28T12:14:03.068139+00:00'], Model 4 35,124 rows, 22,549 settled tickers, 8,260 tickers with an external scan.
* By model: {"gen1_ledger": 62653, "gen1_elo": 36854, "fair_v1": 36854, "gen2": 36854, "gen1_sr": 36854, "model4_fundamental": 33063, "model4_conditioned": 33019}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 64,167 | 14.1 | 9.6 | 20.0 | 15.4 | 19.0 | 13.9 | 7.9 | 11.89 | 40.9% | 21.9% |
| MW fair_v1 | 36,854 | 13.0 | 8.7 | 18.6 | 15.5 | 19.4 | 15.0 | 9.7 | 13.01 | 44.1% | 24.7% |
| MW gen1_elo | 36,854 | 12.8 | 8.6 | 19.4 | 15.4 | 19.5 | 14.9 | 9.6 | 12.83 | 43.9% | 24.4% |
| MW gen1_ledger | 27,313 | 15.6 | 10.7 | 21.9 | 15.2 | 18.5 | 12.4 | 5.6 | 10.43 | 36.5% | 18.0% |
| MW gen1_sr | 36,854 | 10.2 | 7.2 | 16.8 | 13.7 | 20.8 | 18.6 | 12.7 | 15.92 | 52.1% | 31.3% |
| MW gen2 | 36,854 | 11.1 | 7.5 | 16.4 | 13.9 | 19.5 | 17.9 | 13.8 | 15.5 | 51.2% | 31.7% |
| all families model4_conditioned | 33,019 | 22.2 | 18.2 | 34.5 | 17.4 | 4.8 | 1.9 | 1.1 | 6.04 | 7.8% | 3.0% |
| all families model4_fundamental | 33,063 | 17.1 | 13.2 | 34.0 | 20.4 | 10.2 | 3.6 | 1.4 | 7.73 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.3%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.7%, >=40pp 7.9%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.27pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,289 | 27.0 | 15.7 | 27.3 | 13.6 | 11.6 | 4.1 | 0.6 | 5.92 | 16.4% | 4.7% |
| CHALLENGER | 5,712 | 16.2 | 9.8 | 20.4 | 15.6 | 15.5 | 12.0 | 10.7 | 11.0 | 38.1% | 22.7% |
| ITF_MEN | 10,069 | 10.0 | 7.2 | 16.8 | 15.1 | 21.1 | 17.7 | 12.1 | 15.32 | 50.9% | 29.8% |
| ITF_WOMEN | 14,414 | 9.8 | 7.0 | 16.0 | 15.1 | 22.0 | 18.4 | 11.7 | 15.64 | 52.1% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,352 | 17.6 | 13.9 | 24.6 | 20.2 | 16.5 | 6.6 | 0.6 | 8.3 | 23.7% | 7.2% |
| WTA125 | 1,012 | 15.8 | 7.1 | 23.1 | 19.2 | 20.4 | 12.8 | 1.7 | 10.73 | 34.8% | 14.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,289 | 25.6 | 15.6 | 25.2 | 16.6 | 12.0 | 4.2 | 0.8 | 6.27 | 16.9% | 5.0% |
| CHALLENGER | 5,712 | 15.1 | 8.8 | 18.0 | 14.6 | 18.1 | 13.8 | 11.7 | 12.69 | 43.5% | 25.4% |
| ITF_MEN | 10,069 | 8.0 | 6.1 | 14.5 | 13.5 | 19.8 | 20.9 | 17.4 | 18.43 | 58.1% | 38.3% |
| ITF_WOMEN | 14,414 | 8.0 | 5.7 | 14.1 | 12.8 | 20.7 | 21.4 | 17.4 | 19.21 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,352 | 14.8 | 10.8 | 22.0 | 15.7 | 22.4 | 12.9 | 1.5 | 10.77 | 36.8% | 14.5% |
| WTA125 | 1,012 | 8.7 | 6.3 | 16.5 | 17.0 | 24.6 | 17.8 | 9.1 | 15.73 | 51.5% | 26.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,289 | 22.5 | 12.9 | 24.5 | 16.0 | 16.2 | 6.5 | 1.4 | 7.58 | 24.1% | 7.8% |
| CHALLENGER | 5,712 | 15.0 | 9.2 | 21.2 | 15.8 | 15.7 | 12.2 | 11.0 | 11.3 | 38.9% | 23.2% |
| ITF_MEN | 10,069 | 9.5 | 7.1 | 17.1 | 14.2 | 21.7 | 18.2 | 12.3 | 15.77 | 52.1% | 30.4% |
| ITF_WOMEN | 14,414 | 9.5 | 6.8 | 16.5 | 15.9 | 22.1 | 18.1 | 11.1 | 15.45 | 51.3% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,352 | 23.6 | 16.3 | 31.8 | 15.0 | 9.7 | 2.5 | 1.1 | 6.12 | 13.3% | 3.6% |
| WTA125 | 1,012 | 22.4 | 12.6 | 26.6 | 16.6 | 14.9 | 6.5 | 0.4 | 7.96 | 21.8% | 6.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,906 | 24.6 | 19.1 | 30.9 | 12.8 | 9.0 | 3.1 | 0.5 | 5.67 | 12.6% | 3.6% |
| CHALLENGER | 3,898 | 22.5 | 14.5 | 26.9 | 14.6 | 13.8 | 6.1 | 1.6 | 7.14 | 21.5% | 7.7% |
| DOUBLES | 1,948 | 5.1 | 4.6 | 12.2 | 10.5 | 21.1 | 25.1 | 21.3 | 23.61 | 67.6% | 46.5% |
| ITF_MEN | 7,754 | 13.0 | 9.2 | 20.8 | 15.9 | 21.6 | 13.4 | 6.2 | 12.09 | 41.1% | 19.5% |
| ITF_WOMEN | 9,231 | 13.0 | 8.9 | 19.6 | 15.6 | 21.4 | 15.7 | 5.8 | 12.52 | 42.9% | 21.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,400 | 24.4 | 15.4 | 29.9 | 17.9 | 9.4 | 2.9 | 0.3 | 6.76 | 12.6% | 3.1% |
| WTA125 | 1,027 | 24.4 | 12.8 | 20.6 | 19.4 | 13.4 | 7.7 | 1.8 | 8.07 | 22.9% | 9.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,200 | 27.3 | 15.8 | 27.7 | 13.5 | 11.4 | 3.8 | 0.4 | 5.88 | 15.6% | 4.2% |
| CHALLENGER | 4,015 | 21.1 | 12.4 | 25.4 | 18.0 | 15.2 | 6.3 | 1.5 | 8.11 | 23.1% | 7.8% |
| ITF_MEN | 7,496 | 12.0 | 8.7 | 20.1 | 17.2 | 22.0 | 14.6 | 5.4 | 12.55 | 42.0% | 20.0% |
| ITF_WOMEN | 10,868 | 11.6 | 8.3 | 18.3 | 17.2 | 23.9 | 15.4 | 5.3 | 13.38 | 44.5% | 20.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,281 | 17.8 | 13.8 | 24.7 | 20.5 | 16.5 | 6.1 | 0.6 | 8.25 | 23.2% | 6.7% |
| WTA125 | 977 | 16.1 | 7.0 | 22.7 | 19.4 | 20.9 | 12.5 | 1.4 | 10.97 | 34.8% | 13.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,200 | 25.9 | 15.9 | 25.3 | 16.6 | 11.9 | 3.9 | 0.5 | 6.22 | 16.3% | 4.3% |
| CHALLENGER | 4,015 | 19.4 | 11.3 | 22.6 | 17.0 | 18.4 | 9.4 | 1.9 | 9.09 | 29.7% | 11.3% |
| ITF_MEN | 7,497 | 9.3 | 7.2 | 16.7 | 15.6 | 21.6 | 19.0 | 10.5 | 15.41 | 51.1% | 29.5% |
| ITF_WOMEN | 10,869 | 8.9 | 6.5 | 15.8 | 14.2 | 22.7 | 20.9 | 11.0 | 16.83 | 54.6% | 31.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,281 | 14.9 | 10.8 | 22.1 | 15.7 | 22.5 | 12.8 | 1.3 | 10.71 | 36.6% | 14.1% |
| WTA125 | 977 | 8.7 | 6.3 | 16.6 | 17.3 | 24.5 | 18.1 | 8.5 | 15.49 | 51.1% | 26.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,853 | 24.7 | 19.4 | 30.9 | 13.0 | 8.6 | 3.0 | 0.4 | 5.65 | 12.0% | 3.4% |
| CHALLENGER | 3,436 | 23.9 | 15.4 | 28.1 | 14.7 | 13.2 | 4.2 | 0.4 | 6.6 | 17.8% | 4.6% |
| DOUBLES | 1,823 | 5.0 | 4.7 | 12.4 | 10.7 | 20.9 | 25.0 | 21.1 | 23.53 | 67.1% | 46.1% |
| ITF_MEN | 6,621 | 14.0 | 9.8 | 22.4 | 16.6 | 21.5 | 11.8 | 4.0 | 11.16 | 37.3% | 15.8% |
| ITF_WOMEN | 7,838 | 13.7 | 9.4 | 20.9 | 16.3 | 21.5 | 14.6 | 3.6 | 11.67 | 39.7% | 18.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,346 | 24.7 | 15.8 | 29.9 | 17.9 | 9.4 | 2.2 | 0.1 | 6.59 | 11.7% | 2.3% |
| WTA125 | 906 | 25.9 | 13.6 | 21.6 | 20.6 | 12.2 | 5.4 | 0.6 | 7.33 | 18.2% | 6.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,948 | 5.1 | 4.6 | 12.2 | 10.5 | 21.1 | 25.1 | 21.3 | 23.61 | 67.6% | 46.5% |
| singles | 25,365 | 16.5 | 11.2 | 22.6 | 15.6 | 18.3 | 11.5 | 4.4 | 9.92 | 34.2% | 15.8% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,605 | 13.0 | 9.4 | 20.0 | 15.6 | 19.1 | 13.9 | 9.1 | 12.42 | 42.0% | 23.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 23,854 | 13.6 | 8.8 | 18.6 | 15.2 | 19.2 | 15.2 | 9.6 | 12.94 | 43.9% | 24.8% |
| UNKNOWN | 5,146 | 10.7 | 7.5 | 17.1 | 16.8 | 20.9 | 16.1 | 11.0 | 14.13 | 48.0% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,397 | 19.8 | 12.3 | 22.2 | 15.9 | 14.8 | 9.2 | 5.8 | 8.66 | 29.8% | 15.0% |
| B | 4,508 | 12.8 | 8.7 | 19.1 | 16.4 | 19.4 | 12.9 | 10.7 | 12.64 | 43.1% | 23.6% |
| C | 5,164 | 12.2 | 8.9 | 19.9 | 15.8 | 18.7 | 14.3 | 10.0 | 12.73 | 43.1% | 24.4% |
| D | 5,722 | 12.3 | 8.1 | 17.6 | 15.5 | 21.1 | 15.9 | 9.4 | 13.68 | 46.4% | 25.3% |
| F | 11,063 | 7.5 | 5.6 | 15.0 | 14.6 | 23.3 | 21.2 | 12.9 | 17.82 | 57.3% | 34.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,417 | 24.2 | 15.8 | 28.6 | 15.2 | 11.0 | 3.8 | 1.4 | 6.51 | 16.2% | 5.2% |
| B | 3,748 | 16.8 | 10.1 | 24.2 | 16.5 | 19.1 | 10.0 | 3.3 | 9.77 | 32.4% | 13.3% |
| C | 5,266 | 11.2 | 7.9 | 19.3 | 14.6 | 21.2 | 15.6 | 10.2 | 13.49 | 47.0% | 25.8% |
| D | 3,920 | 14.4 | 9.8 | 21.2 | 15.4 | 20.4 | 13.1 | 5.6 | 11.38 | 39.1% | 18.7% |
| F | 6,962 | 10.0 | 8.3 | 15.8 | 14.9 | 23.1 | 20.1 | 7.8 | 15.54 | 51.1% | 28.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,789 | 18.1 | 11.1 | 21.3 | 15.7 | 15.2 | 10.1 | 8.5 | 9.85 | 33.8% | 18.5% |
| LIMITED | 7,922 | 13.9 | 10.0 | 20.4 | 16.3 | 19.1 | 13.3 | 7.2 | 11.64 | 39.5% | 20.4% |
| POOR | 17,143 | 9.1 | 6.5 | 16.1 | 15.0 | 22.4 | 19.2 | 11.7 | 16.13 | 53.4% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,193 | 24.3 | 18.4 | 33.3 | 14.8 | 6.3 | 2.6 | 0.4 | 5.81 | 9.3% | 2.9% |
| GAME_SPREAD | 5,652 | 22.2 | 15.3 | 33.1 | 17.1 | 9.0 | 2.8 | 0.6 | 6.74 | 12.4% | 3.3% |
| MATCH_WINNER | 27,313 | 15.6 | 10.7 | 21.9 | 15.2 | 18.5 | 12.4 | 5.6 | 10.43 | 36.5% | 18.0% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,078 | 27.6 | 16.6 | 31.3 | 12.5 | 9.3 | 2.4 | 0.3 | 5.68 | 12.0% | 2.7% |
| TOTAL_GAMES | 9,393 | 9.2 | 10.2 | 36.2 | 27.0 | 10.6 | 4.1 | 2.8 | 9.35 | 17.5% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,729 | 24.5 | 30.5 | 33.0 | 7.1 | 3.9 | 0.8 | 0.2 | 4.68 | 4.9% | 1.0% |
| GAME_SPREAD | 7,726 | 47.0 | 16.2 | 25.6 | 7.3 | 2.0 | 1.2 | 0.6 | 3.29 | 3.8% | 1.8% |
| TOTAL_GAMES | 13,564 | 6.0 | 8.7 | 40.8 | 31.9 | 7.2 | 3.1 | 2.2 | 9.39 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,740 | 23.9 | 16.9 | 34.9 | 14.3 | 7.1 | 2.5 | 0.4 | 6.0 | 10.0% | 2.9% |
| GAME_SPREAD | 7,729 | 19.9 | 13.4 | 28.2 | 20.6 | 12.4 | 4.3 | 1.1 | 7.83 | 17.8% | 5.4% |
| TOTAL_GAMES | 13,594 | 9.7 | 9.9 | 36.6 | 25.5 | 11.6 | 4.2 | 2.4 | 9.24 | 18.3% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 36,854 | 44.1% | 24.7% | 13.01 | 35.7% | 15.6% | 10.8 |
| gen1_elo | 36,854 | 43.9% | 24.4% | 12.83 | 35.4% | 15.5% | 10.57 |
| gen1_sr | 36,854 | 52.1% | 31.3% | 15.92 | 44.5% | 22.2% | 13.06 |
| gen2 | 36,854 | 51.2% | 31.7% | 15.5 | 44.4% | 23.8% | 13.02 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,015 | 15.6 | 10.5 | 21.3 | 17.3 | 20.0 | 12.0 | 3.3 | 10.72 | 35.4% | 15.4% |
| STALE | 18,839 | 10.6 | 7.0 | 16.1 | 13.8 | 18.9 | 17.9 | 15.8 | 16.08 | 52.5% | 33.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 20,781 | 16.4 | 11.1 | 22.6 | 15.4 | 17.9 | 11.9 | 4.8 | 9.98 | 34.6% | 16.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 64,167 | 20781 | 21487 | 21899 | 24.1 | 114.0 | 1400.4 |
| ge_15pp | 26,240 | 7182 | 7662 | 11396 | 26.3 | 415.5 | 1399.2 |
| ge_25pp | 14,026 | 3462 | 3360 | 7204 | 31.3 | 567.9 | 1380.4 |
| lt_10pp | 28,061 | 10407 | 10165 | 7489 | 22.4 | 46.9 | 1341.5 |

Current slate `SL-20261028T123129Z-f6f011d0`: 730 priced rows, quote age at build {'median': 18.0, 'max': 18.1}, freshness {'AGING': 730}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 43 | 0.0 | 0.0 | 32.6 | 7.0 | 34.9 | 23.3 | 2.3 | 20.19 | 60.5% | 25.6% |
| EXTERNAL_LONE_OUTLIER | 21 | 76.2 | 23.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,625 | 19.9 | 11.2 | 25.1 | 18.2 | 17.7 | 7.2 | 0.7 | 8.65 | 25.6% | 7.9% |
| KALSHI_LONE_OUTLIER | 25 | 4.0 | 4.0 | 76.0 | 8.0 | 4.0 | 4.0 | 0.0 | 6.42 | 8.0% | 4.0% |
| MARKETS_AGREE | 714 | 65.0 | 35.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.26 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,561 | 0.0 | 2.4 | 35.4 | 26.3 | 24.6 | 10.4 | 0.8 | 12.22 | 35.9% | 11.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 36,854 | 5989 (16.2%) | 26.1% | 1.1% | {"EXTERNAL_STALE": 3625, "AGREES_WITH_KALSHI": 1561, "ALL_AGREE": 714, "SUPPORTS_MODEL_DIRECTION": 42, "AGREES_WITH_MODEL": 25, "EXTERNAL_OUTLIER": 21, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 16,259 | 1517 (9.3%) | 36.9% | 1.8% | {"EXTERNAL_STALE": 929, "AGREES_WITH_KALSHI": 560, "SUPPORTS_MODEL_DIRECTION": 26, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,102 | 475 (5.2%) | 37.0% | 2.5% | {"EXTERNAL_STALE": 287, "AGREES_WITH_KALSHI": 176, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,485 | 450 (10.0%) | 37.6% | 2.7% | {"EXTERNAL_STALE": 269, "AGREES_WITH_KALSHI": 169, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 14,885 | 3397 (22.8%) | 17.4% | 1.0% | {"EXTERNAL_STALE": 2036, "ALL_AGREE": 714, "AGREES_WITH_KALSHI": 591, "EXTERNAL_OUTLIER": 21, "AGREES_WITH_MODEL": 21, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,163 | 10.5 | 7.4 | 19.6 | 14.6 | 21.5 | 16.6 | 9.8 | 14.09 | 47.9% | 26.4% |
| 4-10x | 4,894 | 11.3 | 8.5 | 18.8 | 15.4 | 21.5 | 14.6 | 9.8 | 13.55 | 45.9% | 24.4% |
| <2x | 18,730 | 15.2 | 10.1 | 19.4 | 16.2 | 17.4 | 13.1 | 8.7 | 11.58 | 39.2% | 21.8% |
| >=10x | 6,067 | 10.7 | 6.3 | 15.2 | 14.4 | 21.5 | 19.4 | 12.5 | 16.33 | 53.4% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,301 | 12.9 | 8.6 | 19.6 | 16.2 | 19.0 | 13.5 | 10.3 | 12.69 | 42.8% | 23.8% |
| 300-1000 | 7,816 | 12.2 | 8.7 | 17.7 | 15.4 | 20.1 | 16.5 | 9.4 | 13.57 | 46.0% | 25.9% |
| <300 | 12,064 | 8.4 | 5.8 | 15.3 | 14.8 | 22.9 | 20.2 | 12.6 | 17.02 | 55.7% | 32.8% |
| >=3000 | 7,673 | 21.3 | 13.5 | 23.8 | 15.8 | 13.8 | 7.2 | 4.6 | 7.6 | 25.6% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1038 | 0.5497 | 0.411 | 0.4971 | +0.053 | -0.086 | -0.0016 ± 0.0048 |
| ratio 4-10x | 713 | 0.5823 | 0.4368 | 0.4979 | +0.084 | -0.061 | 0.008 ± 0.0059 |
| ratio <2x | 2533 | 0.5373 | 0.4135 | 0.4493 | +0.088 | -0.036 | 0.0108 ± 0.0029 |
| ratio >=10x | 917 | 0.5687 | 0.3924 | 0.4526 | +0.116 | -0.060 | 0.0123 ± 0.0061 |
| thinner_sample 1000-3000 | 1395 | 0.5385 | 0.4112 | 0.453 | +0.085 | -0.042 | 0.0081 ± 0.0039 |
| thinner_sample 300-1000 | 1169 | 0.5683 | 0.4255 | 0.4893 | +0.079 | -0.064 | 0.0025 ± 0.0047 |
| thinner_sample <300 | 1767 | 0.5597 | 0.3918 | 0.4618 | +0.098 | -0.070 | 0.0097 ± 0.0042 |
| thinner_sample >=3000 | 870 | 0.5332 | 0.439 | 0.4644 | +0.069 | -0.025 | 0.0128 ± 0.0039 |
| data_status ADEQUATE | 1459 | 0.5342 | 0.4305 | 0.4476 | +0.087 | -0.017 | 0.013 ± 0.0032 |
| data_status LIMITED | 1218 | 0.5502 | 0.4163 | 0.4869 | +0.063 | -0.070 | 0.0029 ± 0.0043 |
| data_status POOR | 2524 | 0.5621 | 0.4002 | 0.4667 | +0.095 | -0.067 | 0.008 ± 0.0035 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 761 | 0.2008 | 0.2013 | -0.0006 ± 0.0006 | 0.5818 | 0.5833 | 0.502 | 0.487 | 0.5125 | -0.083 ± 0.0173 | -0.01 (5) |
| 3-5 | 468 | 0.207 | 0.2078 | -0.0008 ± 0.0017 | 0.598 | 0.5983 | 0.5047 | 0.4647 | 0.4936 | -0.090 ± 0.0215 | 0.02 (1) |
| 5-10 | 1077 | 0.2029 | 0.203 | -0.0001 ± 0.0021 | 0.592 | 0.5897 | 0.5112 | 0.4374 | 0.4717 | -0.091 ± 0.0142 | -0.0167 (6) |
| 10-15 | 915 | 0.2212 | 0.2125 | +0.0087 ± 0.0038 | 0.6352 | 0.6108 | 0.5274 | 0.4037 | 0.4295 | -0.107 ± 0.0154 | -0.048 (5) |
| 15-25 | 1165 | 0.2246 | 0.2123 | +0.0123 ± 0.0053 | 0.6447 | 0.6092 | 0.5753 | 0.3796 | 0.4464 | -0.097 ± 0.0135 | -0.0033 (9) |
| 25-40 | 673 | 0.2234 | 0.2089 | +0.0145 ± 0.0105 | 0.6368 | 0.6002 | 0.6562 | 0.3463 | 0.477 | -0.074 ± 0.0162 | -0.01 (1) |
| 40+ | 142 | 0.2739 | 0.1928 | +0.0811 ± 0.0319 | 0.7472 | 0.5668 | 0.7397 | 0.292 | 0.4296 | -0.064 ± 0.0313 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4024 | 0.1836 | 0.1842 | -0.0007 ± 0.0002 | 0.5425 | 0.5431 | 0.4851 | 0.4699 | 0.4948 | -0.030 ± 0.0069 | -0.0129 (17) |
| 3-5 | 2705 | 0.1966 | 0.1951 | +0.0016 ± 0.0007 | 0.5731 | 0.5671 | 0.4856 | 0.4458 | 0.4451 | -0.056 ± 0.0086 | 0.0 (2) |
| 5-10 | 5708 | 0.2023 | 0.1985 | +0.0038 ± 0.0009 | 0.5904 | 0.5773 | 0.4849 | 0.411 | 0.4215 | -0.051 ± 0.006 | -0.0119 (21) |
| 10-15 | 4921 | 0.2032 | 0.1871 | +0.0161 ± 0.0015 | 0.5933 | 0.5499 | 0.4862 | 0.362 | 0.3589 | -0.067 ± 0.0062 | -0.0281 (16) |
| 15-25 | 6081 | 0.2083 | 0.1692 | +0.0391 ± 0.0021 | 0.6097 | 0.5018 | 0.5008 | 0.3044 | 0.3034 | -0.073 ± 0.0052 | -0.0025 (44) |
| 25-40 | 4815 | 0.2233 | 0.1273 | +0.0960 ± 0.0032 | 0.6407 | 0.3905 | 0.5287 | 0.2149 | 0.2231 | -0.060 ± 0.005 | -0.01 (1) |
| 40+ | 3094 | 0.3786 | 0.0458 | +0.3328 ± 0.0043 | 0.9856 | 0.1762 | 0.6299 | 0.1043 | 0.0633 | -0.076 ± 0.0036 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 598 | 0.2067 | 0.2073 | -0.0007 ± 0.0007 | 0.595 | 0.5968 | 0.5096 | 0.4945 | 0.5167 | -0.109 ± 0.0202 | -0.01 (3) |
| 3-5 | 418 | 0.2292 | 0.226 | +0.0032 ± 0.0019 | 0.6459 | 0.6393 | 0.5102 | 0.4705 | 0.445 | -0.141 ± 0.0248 | 0.02 (1) |
| 5-10 | 938 | 0.2082 | 0.2074 | +0.0008 ± 0.0022 | 0.6022 | 0.6 | 0.55 | 0.475 | 0.5096 | -0.089 ± 0.0154 | -0.01 (4) |
| 10-15 | 848 | 0.2191 | 0.2127 | +0.0064 ± 0.004 | 0.6297 | 0.6133 | 0.565 | 0.4407 | 0.48 | -0.106 ± 0.0165 | -0.04 (5) |
| 15-25 | 1219 | 0.23 | 0.2137 | +0.0163 ± 0.0052 | 0.6545 | 0.6117 | 0.5824 | 0.3872 | 0.4463 | -0.098 ± 0.0135 | -0.0133 (9) |
| 25-40 | 860 | 0.2676 | 0.1985 | +0.0691 ± 0.0095 | 0.7472 | 0.5786 | 0.6548 | 0.3407 | 0.3907 | -0.125 ± 0.0152 | -0.0075 (4) |
| 40+ | 320 | 0.3622 | 0.1666 | +0.1955 ± 0.0226 | 0.9915 | 0.5005 | 0.7328 | 0.247 | 0.3031 | -0.081 ± 0.022 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3417 | 0.1918 | 0.192 | -0.0002 ± 0.0003 | 0.5604 | 0.5605 | 0.5104 | 0.4954 | 0.5069 | -0.046 ± 0.0078 | -0.0133 (15) |
| 3-5 | 2306 | 0.1995 | 0.198 | +0.0015 ± 0.0007 | 0.577 | 0.5732 | 0.5149 | 0.4752 | 0.4753 | -0.054 ± 0.0095 | 0.02 (1) |
| 5-10 | 5098 | 0.1991 | 0.1956 | +0.0035 ± 0.0009 | 0.5838 | 0.5704 | 0.5162 | 0.4421 | 0.4584 | -0.044 ± 0.0063 | -0.0117 (6) |
| 10-15 | 4365 | 0.2065 | 0.1946 | +0.0119 ± 0.0017 | 0.6036 | 0.5674 | 0.5134 | 0.3895 | 0.4046 | -0.053 ± 0.0068 | -0.0189 (18) |
| 15-25 | 6116 | 0.2178 | 0.1806 | +0.0372 ± 0.0021 | 0.6326 | 0.5305 | 0.5225 | 0.327 | 0.3336 | -0.066 ± 0.0055 | -0.0086 (42) |
| 25-40 | 5626 | 0.2523 | 0.138 | +0.1142 ± 0.0031 | 0.7102 | 0.4229 | 0.5576 | 0.2413 | 0.2218 | -0.085 ± 0.005 | -0.0044 (18) |
| 40+ | 4420 | 0.3957 | 0.0594 | +0.3364 ± 0.0042 | 1.0411 | 0.2137 | 0.6508 | 0.1181 | 0.0821 | -0.073 ± 0.0036 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 731 | 0.1988 | 0.2008 | -0.0021 ± 0.0006 | 0.5773 | 0.5824 | 0.4996 | 0.4843 | 0.5431 | -0.039 ± 0.0173 | -0.0137 (8) |
| 3-5 | 508 | 0.2039 | 0.2022 | +0.0017 ± 0.0016 | 0.5912 | 0.585 | 0.4999 | 0.4601 | 0.4606 | -0.121 ± 0.0208 | 0.0067 (3) |
| 5-10 | 1114 | 0.2034 | 0.2016 | +0.0018 ± 0.002 | 0.5929 | 0.5862 | 0.51 | 0.4361 | 0.4605 | -0.095 ± 0.0138 | -0.0071 (7) |
| 10-15 | 910 | 0.2121 | 0.2085 | +0.0036 ± 0.0037 | 0.6146 | 0.6023 | 0.5391 | 0.4159 | 0.4637 | -0.092 ± 0.0152 | -0.0317 (6) |
| 15-25 | 1100 | 0.232 | 0.2156 | +0.0164 ± 0.0055 | 0.6618 | 0.6164 | 0.5872 | 0.3926 | 0.4482 | -0.109 ± 0.014 | -0.03 (1) |
| 25-40 | 685 | 0.2137 | 0.2156 | -0.0018 ± 0.0104 | 0.617 | 0.6154 | 0.6655 | 0.3548 | 0.5109 | -0.058 ± 0.0161 | 0.015 (2) |
| 40+ | 153 | 0.2909 | 0.2011 | +0.0898 ± 0.0317 | 0.796 | 0.5852 | 0.7486 | 0.2992 | 0.4314 | -0.066 ± 0.0331 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3935 | 0.1853 | 0.1858 | -0.0005 ± 0.0002 | 0.5451 | 0.546 | 0.4846 | 0.4693 | 0.4844 | -0.037 ± 0.007 | -0.0163 (35) |
| 3-5 | 2651 | 0.2008 | 0.1988 | +0.0020 ± 0.0007 | 0.585 | 0.5782 | 0.4862 | 0.4466 | 0.4421 | -0.063 ± 0.0088 | -0.0094 (18) |
| 5-10 | 5952 | 0.1945 | 0.1901 | +0.0044 ± 0.0008 | 0.5723 | 0.557 | 0.4855 | 0.4114 | 0.4187 | -0.051 ± 0.0057 | -0.01 (31) |
| 10-15 | 4799 | 0.1949 | 0.1816 | +0.0133 ± 0.0015 | 0.5742 | 0.5368 | 0.4968 | 0.3735 | 0.3809 | -0.058 ± 0.0062 | -0.015 (12) |
| 15-25 | 6177 | 0.2126 | 0.1729 | +0.0396 ± 0.0021 | 0.6191 | 0.5103 | 0.5117 | 0.3167 | 0.3134 | -0.074 ± 0.0053 | -0.03 (2) |
| 25-40 | 4761 | 0.2188 | 0.13 | +0.0889 ± 0.0033 | 0.6318 | 0.3959 | 0.5319 | 0.2161 | 0.2352 | -0.052 ± 0.005 | 0.01 (3) |
| 40+ | 3073 | 0.3911 | 0.0516 | +0.3395 ± 0.0046 | 1.0208 | 0.1915 | 0.6412 | 0.1123 | 0.0696 | -0.078 ± 0.0039 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1126 | 0.1959 | 0.196 | -0.0001 ± 0.0005 | 0.5705 | 0.5705 | 0.505 | 0.49 | 0.4947 | -0.067 ± 0.0134 | -0.0224 (49) |
| 3-5 | 780 | 0.1891 | 0.1888 | +0.0003 ± 0.0013 | 0.5542 | 0.5524 | 0.4939 | 0.4541 | 0.4679 | -0.059 ± 0.0159 | -0.0194 (34) |
| 5-10 | 1638 | 0.2032 | 0.1977 | +0.0054 ± 0.0017 | 0.5966 | 0.5796 | 0.4982 | 0.4246 | 0.4255 | -0.076 ± 0.0112 | -0.005 (78) |
| 10-15 | 1111 | 0.2151 | 0.2033 | +0.0118 ± 0.0034 | 0.6223 | 0.5903 | 0.5316 | 0.4089 | 0.4203 | -0.080 ± 0.0139 | 0.0014 (64) |
| 15-25 | 1449 | 0.2326 | 0.2119 | +0.0207 ± 0.0047 | 0.6625 | 0.609 | 0.5796 | 0.3848 | 0.4313 | -0.079 ± 0.0122 | -0.0214 (59) |
| 25-40 | 906 | 0.2427 | 0.2098 | +0.0330 ± 0.0093 | 0.6942 | 0.6014 | 0.6791 | 0.3673 | 0.4702 | -0.087 ± 0.0142 | -0.0219 (26) |
| 40+ | 300 | 0.3415 | 0.2014 | +0.1401 ± 0.0252 | 0.9867 | 0.588 | 0.8096 | 0.3306 | 0.44 | -0.099 ± 0.0235 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3998 | 0.1778 | 0.178 | -0.0002 ± 0.0002 | 0.526 | 0.526 | 0.5067 | 0.4915 | 0.501 | -0.040 ± 0.0067 | -0.0157 (88) |
| 3-5 | 2723 | 0.1941 | 0.1925 | +0.0016 ± 0.0007 | 0.5654 | 0.5622 | 0.502 | 0.4622 | 0.4627 | -0.051 ± 0.0085 | -0.0209 (69) |
| 5-10 | 5558 | 0.2 | 0.1924 | +0.0076 ± 0.0009 | 0.5885 | 0.566 | 0.4949 | 0.4213 | 0.4077 | -0.070 ± 0.0059 | -0.0082 (132) |
| 10-15 | 3868 | 0.2122 | 0.1963 | +0.0159 ± 0.0018 | 0.6161 | 0.5739 | 0.5305 | 0.4078 | 0.4036 | -0.069 ± 0.0072 | -0.0053 (105) |
| 15-25 | 4783 | 0.2307 | 0.2017 | +0.0290 ± 0.0026 | 0.6634 | 0.583 | 0.5671 | 0.3716 | 0.3962 | -0.063 ± 0.0065 | -0.0253 (107) |
| 25-40 | 3259 | 0.2581 | 0.1857 | +0.0724 ± 0.0048 | 0.7318 | 0.5422 | 0.6322 | 0.3192 | 0.3627 | -0.076 ± 0.0074 | -0.0229 (51) |
| 40+ | 1395 | 0.3763 | 0.1504 | +0.2259 ± 0.0108 | 1.0648 | 0.4513 | 0.7334 | 0.2321 | 0.2695 | -0.074 ± 0.0099 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5201 | 1.013 ± 0.039 | 1.084 | 0.1678 | 0.1649 | 0.2156 | 0.2074 |
| gen2 | 5201 | 0.8 ± 0.036 | 1.041 | 0.1691 | 0.1653 | 0.2359 | 0.2073 |
| gen1_elo | 5201 | 0.991 ± 0.037 | 1.083 | 0.1745 | 0.165 | 0.2143 | 0.2076 |
| gen1_sr | 5201 | 0.974 ± 0.046 | 1.104 | 0.1297 | 0.1673 | 0.2317 | 0.2069 |
| gen1_ledger | 7310 | 0.852 ± 0.028 | 1.05 | 0.1851 | 0.1767 | 0.2188 | 0.2018 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 26,240)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,743 | 21.9% |
| STALE_QUOTE | market_freshness | 5,706 | 21.8% |
| BOOK_QUALITY | execution | 5,080 | 19.4% |
| POOR_DATA | data | 3,111 | 11.9% |
| LIMITED_DATA | data | 1,636 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,456 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,197 | 4.6% |
| IDENTITY_AMBIGUOUS | mapping | 1,087 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 761 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 462 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 21.9%, market_freshness 21.8%, execution 19.4%, data 18.1%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.6%, mapping 4.1%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.6%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 43.4%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.4%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 15.9%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 7.9%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.4%, POST_SETTLEMENT_OBSERVATION 21.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 14,026)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,649 | 33.1% |
| STALE_QUOTE | market_freshness | 2,648 | 18.9% |
| BOOK_QUALITY | execution | 2,648 | 18.9% |
| POOR_DATA | data | 1,330 | 9.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 772 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 579 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 491 | 3.5% |
| LIMITED_DATA | data | 486 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 303 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 119 | 0.9% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.1%, market_freshness 18.9%, execution 18.9%, data 13.0%, market_freshness/coverage 9.0%, mapping 4.1%, model_calibration_or_unknown 2.2%, model_calibration 0.9%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 63.1%, STALE_KALSHI_QUOTE 51.4%, STALE_PLAYER_DATA 46.7%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.8%, PLAYER_IDENTITY_RISK 18.8%, MODEL_HIGH_UNCERTAINTY 18.2%, LEVEL_TRANSFER_RISK 9.4%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.3%, POST_SETTLEMENT_OBSERVATION 33.1%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 11076, "IDENTITY_AMBIGUOUS": 2950}; ticker orientation: {"VERIFIED": 14026}.

Checks: discipline:AMBIGUOUS 905, discipline:PASS 13121, identity_confidence:AMBIGUOUS 2637, identity_confidence:PASS 11389, level_mapping:NA 917, level_mapping:PASS 13109, market_pair:AMBIGUOUS 472, market_pair:NA 331, market_pair:PASS 13223, model_complement:NA 295, model_complement:PASS 13731, namesake:AMBIGUOUS 6, namesake:PASS 14020, physical_match_id:NA 4924, physical_match_id:PASS 9102, player_ids:PASS 14026, same_pair_other_event:PASS 14026, ticker_orientation:PASS 14026

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,195 | 4.3% | 3.9% | 1.6% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 15, "coverage": 13} | 5.82 | 0.2195 / 0.2156 (587) | 21.1% | 3.0% | 3.3% | 2.7% |
| CHALLENGER | 9,610 | 16.6% | 6.3% | 11.4% | {"coverage": 930, "market_freshness/coverage": 193, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 74, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.31 | 0.2198 / 0.2107 (2207) | 34.9% | 16.0% | 4.1% | 22.5% |
| DOUBLES | 1,948 | 46.5% | 46.1% | 6.5% | {"execution": 509, "mapping": 226, "market_freshness": 106, "market_freshness/coverage": 57, "coverage": 7} | 23.53 | 0.3101 / 0.2372 (468) | 12.0% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 17,823 | 25.3% | 18.1% | 32.2% | {"coverage": 1551, "execution": 869, "market_freshness": 818, "data": 670, "market_freshness/coverage": 415, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.9 | 0.217 / 0.2005 (3698) | 36.6% | 70.4% | 17.7% | 20.8% |
| ITF_WOMEN | 23,645 | 26.7% | 19.6% | 45.0% | {"coverage": 2116, "market_freshness": 1362, "execution": 1157, "data": 909, "market_freshness/coverage": 530, "mapping": 147, "model_calibration_or_unknown": 79, "model_calibration": 18} | 12.68 | 0.2057 / 0.1974 (4316) | 38.8% | 58.1% | 10.2% | 20.9% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,752 | 5.7% | 5.1% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "execution": 27, "data": 19, "coverage": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.6 | 0.234 / 0.2278 (587) | 25.6% | 1.1% | 1.4% | 3.3% |
| WTA125 | 2,039 | 11.9% | 10.1% | 1.7% | {"market_freshness": 63, "model_calibration_or_unknown": 50, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.3 | 0.2113 / 0.1945 (606) | 25.2% | 11.9% | 5.2% | 7.6% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 117 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 6 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 7 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 8 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 9 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 194 min (STALE); no external reference |
| 12 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 13 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 16 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 17 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 18 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 19 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 20 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 21 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 22 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 23 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 24 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 25 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 26 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 27 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 28 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 29 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 30 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 31 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 32 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 33 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 34 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 35 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 36 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 37 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 39 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 40 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 41 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 42 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 124 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 43 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 44 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 46 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 47 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 48 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 49 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 50 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9686, "by_level_share_of_ge_25pp": {"ATP": 0.016, "CHALLENGER": 0.1137, "DOUBLES": 0.0645, "ITF_MEN": 0.3218, "ITF_WOMEN": 0.4504, "OTHER": 0.0009, "WTA": 0.0153, "WTA125": 0.0173}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5136, "share_primary_cause_market_settled_or_in_play": 0.4215, "share_primary_cause_stale_quote_only": 0.1888}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 14026, "identity_ambiguous_share": 0.2103, "ticker_orientation": {"VERIFIED": 14026}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9102, "with_external": 475, "coverage": 0.0522, "external_status": {"EXTERNAL_STALE": 287, "AGREES_WITH_KALSHI": 176, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 287, "MODEL_LONE_OUTLIER": 176, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3705, "share_external_supports_model": 0.0253}, "pregame_clean_ge_25pp": {"n": 4485, "with_external": 450, "coverage": 0.1003, "external_status": {"EXTERNAL_STALE": 269, "AGREES_WITH_KALSHI": 169, "SUPPORTS_MODEL_DIRECTION": 11, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 269, "MODEL_LONE_OUTLIER": 169, "ALL_THREE_DISAGREE": 11, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3756, "share_external_supports_model": 0.0267}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 451.0, "median_sample_ratio": 2.48, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2132, "data_status": {"POOR": 8007, "LIMITED": 3540, "ADEQUATE": 2479}, "comparison_lt_10pp": {"median_thinner_serve_points": 1693.0, "median_sample_ratio": 1.71, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1038, "model_minus_observed": 0.0526, "kalshi_minus_observed": -0.0861, "brier_diff_model_minus_kalshi": -0.0016}, "4-10x": {"n": 713, "model_minus_observed": 0.0844, "kalshi_minus_observed": -0.0611, "brier_diff_model_minus_kalshi": 0.008}, "<2x": {"n": 2533, "model_minus_observed": 0.0881, "kalshi_minus_observed": -0.0358, "brier_diff_model_minus_kalshi": 0.0108}, ">=10x": {"n": 917, "model_minus_observed": 0.1162, "kalshi_minus_observed": -0.0601, "brier_diff_model_minus_kalshi": 0.0123}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5201, "model": {"intercept": -0.534, "slope": 0.8, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.187, "slope": 1.041, "slope_se": 0.039}, "mean_extremity_model": 0.1691, "mean_extremity_kalshi": 0.1653, "model_brier": 0.2359, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.0286, "brier_diff_se": 0.0026, "model_logloss": 0.6696, "kalshi_logloss": 0.598}, "fair_v1": {"n": 5201, "model": {"intercept": -0.406, "slope": 1.013, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.084, "slope_se": 0.04}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1649, "model_brier": 0.2156, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.0022, "model_logloss": 0.6205, "kalshi_logloss": 0.5983}, "gen1_elo": {"n": 5201, "model": {"intercept": -0.38, "slope": 0.991, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.308, "slope": 1.083, "slope_se": 0.039}, "mean_extremity_model": 0.1745, "mean_extremity_kalshi": 0.165, "model_brier": 0.2143, "kalshi_brier": 0.2076, "brier_diff_model_minus_kalshi": 0.0068, "brier_diff_se": 0.0022, "model_logloss": 0.6181, "kalshi_logloss": 0.5986}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.247, "share_ge_15": 0.4412, "median_abs_gap": 13.01, "n": 36854}, "gen1_elo": {"share_ge_25": 0.2445, "share_ge_15": 0.4393, "median_abs_gap": 12.83, "n": 36854}, "gen1_sr": {"share_ge_25": 0.3134, "share_ge_15": 0.5215, "median_abs_gap": 15.92, "n": 36854}, "gen2": {"share_ge_25": 0.3169, "share_ge_15": 0.5116, "median_abs_gap": 15.5, "n": 36854}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1555, "share_ge_15": 0.3567, "median_abs_gap": 10.8, "n": 28843}, "gen1_elo": {"share_ge_25": 0.1554, "share_ge_15": 0.354, "median_abs_gap": 10.57, "n": 28841}, "gen1_sr": {"share_ge_25": 0.2219, "share_ge_15": 0.445, "median_abs_gap": 13.06, "n": 28844}, "gen2": {"share_ge_25": 0.2377, "share_ge_15": 0.4442, "median_abs_gap": 13.02, "n": 28845}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.82, "share_ge_25_all": 0.0433, "share_ge_25_pregame_clean": 0.039}, "WTA": {"median_abs_gap_pregame_clean": 7.6, "share_ge_25_all": 0.057, "share_ge_25_pregame_clean": 0.0507}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.237, "share_within_10pp_all": 0.4373, "share_within_10pp_pregame_clean": 0.4883, "corr_model_vs_mid_pregame_clean": 0.848}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 761, "model_brier": 0.2008, "kalshi_brier": 0.2013, "brier_diff_model_minus_kalshi": -0.0006}, "10-15": {"n_settled": 915, "model_brier": 0.2212, "kalshi_brier": 0.2125, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1165, "model_brier": 0.2246, "kalshi_brier": 0.2123, "brier_diff_model_minus_kalshi": 0.0123}, "25-40": {"n_settled": 673, "model_brier": 0.2234, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.0145}, "3-5": {"n_settled": 468, "model_brier": 0.207, "kalshi_brier": 0.2078, "brier_diff_model_minus_kalshi": -0.0008}, "40+": {"n_settled": 142, "model_brier": 0.2739, "kalshi_brier": 0.1928, "brier_diff_model_minus_kalshi": 0.0811}, "5-10": {"n_settled": 1077, "model_brier": 0.2029, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": -0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.534, "slope": 0.8, "slope_se": 0.036}, "kalshi_slope": {"intercept": 0.187, "slope": 1.041, "slope_se": 0.039}, "n": 5201}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.489, "slope": 0.852, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.162, "slope": 1.05, "slope_se": 0.032}, "n": 7310}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 468, "model_brier": 0.3101, "kalshi_brier": 0.2372, "brier_diff_model_minus_kalshi": 0.0729, "brier_diff_se": 0.014, "corr_model_outcome": 0.0526, "corr_kalshi_outcome": 0.2393}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
