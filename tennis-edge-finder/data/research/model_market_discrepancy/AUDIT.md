# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-25T10:21Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 53,520): 0-3 13.9%, 3-5 9.5%, 5-10 19.8%, 10-15 15.4%, 15-25 19.2%, 25-40 14.0%, 40+ 8.2%; median gap 12.06 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.3%, Challenger 11.8%, doubles 7.0%). Main tour: ATP 4.5% and WTA 5.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,869): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.3%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.6%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.3%, market_freshness 18.7%, execution 18.6%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,869 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.2% of the time and with the model 0.8%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1756.5 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.032, Gen-2 0.837, Gen-1 ledger 0.858 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 574 model 0.2227 vs Kalshi 0.2102; n 116 model 0.2743 vs Kalshi 0.202.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 233,078 model-market comparisons (378,038 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 78,915 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-25T10:08:33.941018+00:00'], shadow board 61,627 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-25T10:08:37.887808+00:00'], Model 4 29,384 rows, 20,282 settled tickers, 7,242 tickers with an external scan.
* By model: {"gen1_ledger": 53951, "gen1_elo": 30989, "fair_v1": 30989, "gen2": 30989, "gen1_sr": 30989, "model4_fundamental": 27603, "model4_conditioned": 27568}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 53,520 | 13.9 | 9.5 | 19.8 | 15.4 | 19.2 | 14.0 | 8.2 | 12.06 | 41.4% | 22.2% |
| MW fair_v1 | 30,989 | 12.9 | 8.5 | 18.5 | 15.6 | 19.7 | 15.0 | 9.9 | 13.14 | 44.5% | 24.8% |
| MW gen1_elo | 30,989 | 12.7 | 8.5 | 19.0 | 15.2 | 19.9 | 14.9 | 9.6 | 13.0 | 44.5% | 24.6% |
| MW gen1_ledger | 22,531 | 15.4 | 10.8 | 21.6 | 15.1 | 18.5 | 12.7 | 5.9 | 10.53 | 37.1% | 18.5% |
| MW gen1_sr | 30,989 | 10.2 | 7.1 | 16.7 | 13.6 | 20.8 | 18.7 | 12.9 | 15.99 | 52.4% | 31.6% |
| MW gen2 | 30,989 | 11.0 | 7.3 | 16.3 | 14.0 | 19.4 | 17.9 | 14.0 | 15.58 | 51.4% | 31.9% |
| all families model4_conditioned | 27,568 | 21.7 | 18.7 | 34.6 | 17.7 | 4.5 | 1.6 | 1.1 | 6.02 | 7.2% | 2.7% |
| all families model4_fundamental | 27,603 | 16.8 | 13.2 | 34.0 | 20.6 | 10.6 | 3.5 | 1.3 | 7.8 | 15.4% | 4.9% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.8%, >=15pp 41.4%, >=20pp 30.8%, >=25pp 22.2%, >=30pp 16.0%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.42pp; >=10pp 45.2%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,795 | 27.8 | 14.2 | 25.4 | 15.4 | 11.8 | 4.5 | 0.7 | 6.19 | 17.1% | 5.3% |
| CHALLENGER | 4,867 | 15.8 | 10.0 | 20.3 | 15.7 | 15.1 | 12.3 | 10.8 | 11.06 | 38.2% | 23.1% |
| ITF_MEN | 8,480 | 10.1 | 7.2 | 16.7 | 14.7 | 21.5 | 17.6 | 12.2 | 15.46 | 51.2% | 29.7% |
| ITF_WOMEN | 12,166 | 9.5 | 6.9 | 15.9 | 15.3 | 22.3 | 18.2 | 12.0 | 15.79 | 52.5% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,982 | 17.4 | 13.1 | 26.4 | 19.1 | 17.6 | 5.8 | 0.7 | 8.25 | 24.0% | 6.5% |
| WTA125 | 693 | 13.0 | 7.2 | 22.5 | 20.6 | 21.2 | 13.4 | 2.0 | 11.65 | 36.6% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,795 | 23.8 | 15.0 | 25.1 | 17.9 | 12.7 | 4.5 | 0.9 | 6.72 | 18.2% | 5.5% |
| CHALLENGER | 4,867 | 14.9 | 8.9 | 18.2 | 14.6 | 17.8 | 13.9 | 11.6 | 12.63 | 43.3% | 25.5% |
| ITF_MEN | 8,480 | 8.1 | 5.9 | 14.4 | 13.0 | 19.7 | 21.1 | 17.8 | 18.76 | 58.6% | 38.9% |
| ITF_WOMEN | 12,166 | 8.2 | 5.6 | 13.7 | 13.1 | 20.5 | 21.1 | 17.7 | 19.19 | 59.3% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,982 | 14.2 | 10.2 | 22.2 | 16.0 | 22.6 | 13.3 | 1.3 | 10.87 | 37.2% | 14.6% |
| WTA125 | 693 | 6.6 | 4.8 | 17.0 | 17.5 | 25.7 | 19.6 | 8.8 | 16.84 | 54.1% | 28.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,795 | 23.4 | 12.6 | 24.4 | 16.3 | 15.3 | 6.8 | 1.3 | 7.51 | 23.4% | 8.1% |
| CHALLENGER | 4,867 | 14.4 | 9.2 | 20.7 | 15.6 | 16.2 | 13.0 | 10.9 | 11.47 | 40.1% | 23.9% |
| ITF_MEN | 8,480 | 9.7 | 7.3 | 16.8 | 13.8 | 22.1 | 17.9 | 12.3 | 15.94 | 52.4% | 30.2% |
| ITF_WOMEN | 12,166 | 9.4 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.1 | 15.59 | 51.9% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 1,982 | 23.7 | 17.3 | 30.6 | 15.3 | 9.9 | 2.6 | 0.6 | 6.04 | 13.1% | 3.2% |
| WTA125 | 693 | 22.4 | 11.5 | 28.1 | 15.7 | 15.3 | 6.5 | 0.4 | 7.99 | 22.2% | 6.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,762 | 24.9 | 19.3 | 30.0 | 13.0 | 9.5 | 3.0 | 0.3 | 5.67 | 12.8% | 3.3% |
| CHALLENGER | 3,372 | 21.4 | 14.2 | 26.5 | 14.8 | 14.7 | 6.6 | 1.8 | 7.37 | 23.1% | 8.4% |
| DOUBLES | 1,756 | 5.2 | 4.6 | 12.2 | 10.3 | 20.2 | 25.9 | 21.5 | 23.9 | 67.7% | 47.4% |
| ITF_MEN | 6,282 | 13.7 | 9.2 | 19.9 | 16.2 | 21.4 | 13.3 | 6.5 | 12.19 | 41.1% | 19.8% |
| ITF_WOMEN | 7,276 | 12.6 | 8.8 | 19.4 | 15.3 | 21.6 | 16.1 | 6.2 | 12.84 | 43.9% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,162 | 22.6 | 15.8 | 30.4 | 18.1 | 9.5 | 3.4 | 0.3 | 6.83 | 13.2% | 3.7% |
| WTA125 | 772 | 20.9 | 13.6 | 21.8 | 18.4 | 14.6 | 8.6 | 2.2 | 8.32 | 25.4% | 10.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,720 | 28.1 | 14.4 | 25.9 | 15.3 | 11.7 | 4.2 | 0.4 | 6.04 | 16.2% | 4.6% |
| CHALLENGER | 3,458 | 20.5 | 12.4 | 24.9 | 18.2 | 15.3 | 6.8 | 1.8 | 8.43 | 24.0% | 8.6% |
| ITF_MEN | 6,213 | 12.2 | 8.8 | 20.1 | 16.7 | 22.7 | 14.4 | 5.1 | 12.57 | 42.2% | 19.5% |
| ITF_WOMEN | 9,105 | 11.2 | 8.2 | 18.1 | 17.3 | 24.3 | 15.4 | 5.5 | 13.53 | 45.2% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,924 | 17.7 | 12.9 | 26.4 | 19.3 | 17.5 | 5.5 | 0.7 | 8.25 | 23.6% | 6.1% |
| WTA125 | 667 | 13.3 | 7.0 | 22.0 | 21.0 | 21.9 | 13.0 | 1.6 | 11.66 | 36.6% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,720 | 24.1 | 15.3 | 25.3 | 17.8 | 12.7 | 4.2 | 0.6 | 6.54 | 17.5% | 4.7% |
| CHALLENGER | 3,458 | 18.9 | 11.4 | 22.5 | 17.4 | 18.2 | 9.6 | 2.0 | 9.34 | 29.9% | 11.6% |
| ITF_MEN | 6,214 | 9.7 | 7.1 | 16.8 | 15.1 | 21.6 | 19.3 | 10.5 | 15.48 | 51.4% | 29.8% |
| ITF_WOMEN | 9,106 | 9.3 | 6.5 | 15.2 | 14.6 | 22.5 | 20.6 | 11.3 | 16.75 | 54.4% | 31.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,924 | 14.3 | 10.2 | 22.2 | 16.1 | 22.7 | 13.1 | 1.3 | 10.87 | 37.1% | 14.4% |
| WTA125 | 667 | 6.5 | 5.0 | 17.1 | 17.8 | 25.6 | 20.1 | 8.0 | 16.74 | 53.7% | 28.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,712 | 25.0 | 19.6 | 30.1 | 13.1 | 9.2 | 2.9 | 0.2 | 5.64 | 12.2% | 3.0% |
| CHALLENGER | 2,955 | 22.7 | 15.2 | 27.9 | 14.8 | 14.2 | 4.6 | 0.5 | 6.89 | 19.3% | 5.1% |
| DOUBLES | 1,636 | 5.1 | 4.7 | 12.5 | 10.4 | 20.1 | 25.9 | 21.3 | 23.85 | 67.2% | 47.1% |
| ITF_MEN | 5,270 | 14.8 | 9.8 | 21.5 | 16.9 | 21.4 | 11.6 | 4.0 | 11.21 | 36.9% | 15.6% |
| ITF_WOMEN | 6,042 | 13.5 | 9.4 | 20.8 | 16.1 | 21.8 | 14.9 | 3.6 | 11.75 | 40.2% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,111 | 23.0 | 16.2 | 30.4 | 18.1 | 9.4 | 2.7 | 0.1 | 6.73 | 12.2% | 2.8% |
| WTA125 | 661 | 22.7 | 15.0 | 23.1 | 19.8 | 13.0 | 5.8 | 0.6 | 7.56 | 19.4% | 6.3% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,756 | 5.2 | 4.6 | 12.2 | 10.3 | 20.2 | 25.9 | 21.5 | 23.9 | 67.7% | 47.4% |
| singles | 20,775 | 16.3 | 11.3 | 22.4 | 15.5 | 18.4 | 11.5 | 4.5 | 10.0 | 34.5% | 16.1% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 9 | 11.1 | 22.2 | 55.6 | 0.0 | 11.1 | 0.0 | 0.0 | 6.98 | 11.1% | 0.0% |
| Clay | 6,806 | 12.9 | 9.0 | 19.2 | 15.8 | 18.9 | 14.3 | 9.8 | 12.8 | 43.1% | 24.2% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 19,300 | 13.4 | 8.6 | 18.6 | 15.2 | 19.7 | 14.8 | 9.6 | 13.02 | 44.2% | 24.5% |
| UNKNOWN | 4,637 | 10.7 | 7.4 | 17.0 | 16.8 | 20.6 | 16.4 | 11.0 | 14.15 | 48.0% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,888 | 19.6 | 11.9 | 21.6 | 16.5 | 15.0 | 9.2 | 6.2 | 9.09 | 30.4% | 15.4% |
| B | 3,846 | 12.3 | 8.7 | 19.4 | 16.3 | 19.5 | 12.7 | 10.9 | 12.78 | 43.2% | 23.7% |
| C | 4,326 | 11.7 | 8.8 | 19.6 | 15.3 | 19.3 | 14.7 | 10.6 | 13.13 | 44.5% | 25.2% |
| D | 4,762 | 12.1 | 7.7 | 17.4 | 15.5 | 21.6 | 15.7 | 10.1 | 13.98 | 47.3% | 25.8% |
| F | 9,167 | 7.5 | 5.5 | 15.0 | 14.6 | 23.6 | 21.2 | 12.5 | 17.79 | 57.4% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,477 | 23.1 | 15.9 | 28.9 | 15.2 | 11.5 | 4.0 | 1.4 | 6.67 | 16.9% | 5.4% |
| B | 3,058 | 16.1 | 10.4 | 23.1 | 16.2 | 19.8 | 10.6 | 3.8 | 10.06 | 34.1% | 14.4% |
| C | 4,441 | 11.0 | 7.3 | 18.4 | 14.4 | 21.1 | 16.8 | 10.9 | 14.44 | 48.9% | 27.8% |
| D | 3,074 | 14.4 | 9.7 | 20.0 | 14.6 | 21.0 | 14.2 | 6.0 | 12.04 | 41.3% | 20.3% |
| F | 5,481 | 10.2 | 8.3 | 15.7 | 15.2 | 22.6 | 19.8 | 8.1 | 15.3 | 50.6% | 27.9% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,148 | 17.8 | 10.7 | 21.0 | 16.2 | 15.6 | 10.1 | 8.7 | 10.14 | 34.4% | 18.8% |
| LIMITED | 6,570 | 13.4 | 10.1 | 20.1 | 16.0 | 19.3 | 13.3 | 7.7 | 11.95 | 40.3% | 21.0% |
| POOR | 14,271 | 9.1 | 6.3 | 16.0 | 15.0 | 22.8 | 19.2 | 11.7 | 16.25 | 53.7% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,676 | 24.9 | 18.8 | 33.6 | 14.2 | 6.0 | 2.2 | 0.2 | 5.63 | 8.5% | 2.5% |
| GAME_SPREAD | 5,023 | 22.3 | 15.3 | 33.3 | 17.1 | 9.2 | 2.5 | 0.3 | 6.73 | 12.0% | 2.8% |
| MATCH_WINNER | 22,531 | 15.4 | 10.8 | 21.6 | 15.1 | 18.5 | 12.7 | 5.9 | 10.53 | 37.1% | 18.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 11,639 | 28.0 | 16.5 | 31.2 | 12.6 | 9.0 | 2.3 | 0.3 | 5.65 | 11.7% | 2.7% |
| TOTAL_GAMES | 8,058 | 9.1 | 9.9 | 36.2 | 28.0 | 10.4 | 3.6 | 2.9 | 9.4 | 16.9% | 6.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,895 | 24.7 | 32.2 | 32.6 | 5.9 | 3.6 | 0.8 | 0.2 | 4.57 | 4.6% | 1.0% |
| GAME_SPREAD | 6,489 | 45.7 | 16.8 | 26.6 | 7.9 | 1.7 | 0.9 | 0.3 | 3.45 | 2.9% | 1.2% |
| TOTAL_GAMES | 11,184 | 5.1 | 7.9 | 41.1 | 33.9 | 7.0 | 2.7 | 2.3 | 9.55 | 12.0% | 5.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,906 | 23.7 | 17.2 | 35.2 | 13.6 | 7.3 | 2.6 | 0.4 | 5.97 | 10.2% | 3.0% |
| GAME_SPREAD | 6,492 | 19.9 | 13.1 | 27.9 | 20.8 | 13.2 | 4.2 | 0.9 | 7.96 | 18.3% | 5.1% |
| TOTAL_GAMES | 11,205 | 8.8 | 9.7 | 36.5 | 26.7 | 11.9 | 3.9 | 2.5 | 9.41 | 18.3% | 6.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 30,989 | 44.5% | 24.8% | 13.14 | 36.1% | 15.6% | 10.94 |
| gen1_elo | 30,989 | 44.5% | 24.6% | 13.0 | 35.9% | 15.7% | 10.74 |
| gen1_sr | 30,989 | 52.4% | 31.6% | 15.99 | 44.6% | 22.3% | 13.1 |
| gen2 | 30,989 | 51.4% | 31.9% | 15.58 | 44.6% | 23.9% | 13.07 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,726 | 15.6 | 10.4 | 21.4 | 17.3 | 20.2 | 11.9 | 3.3 | 10.71 | 35.3% | 15.2% |
| STALE | 15,263 | 10.0 | 6.6 | 15.5 | 13.8 | 19.2 | 18.1 | 16.6 | 16.96 | 54.0% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 15,999 | 16.4 | 11.3 | 22.4 | 15.3 | 17.8 | 12.1 | 4.9 | 9.99 | 34.7% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 53,520 | 15999 | 19198 | 18323 | 24.2 | 140.5 | 1400.4 |
| ge_15pp | 22,153 | 5553 | 6846 | 9754 | 26.3 | 440.0 | 1380.4 |
| ge_25pp | 11,869 | 2713 | 2976 | 6180 | 32.1 | 584.0 | 1380.4 |
| lt_10pp | 23,135 | 8004 | 9083 | 6048 | 22.4 | 47.3 | 1341.5 |

Current slate `SL-20261025T102145Z-60281f33`: 837 priced rows, quote age at build {'median': 13.7, 'max': 13.7}, freshness {'AGING': 837}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 25 | 0.0 | 0.0 | 24.0 | 8.0 | 36.0 | 32.0 | 0.0 | 20.47 | 68.0% | 32.0% |
| EXTERNAL_LONE_OUTLIER | 16 | 75.0 | 25.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,020 | 19.1 | 11.4 | 24.8 | 18.8 | 18.2 | 7.1 | 0.6 | 8.87 | 26.0% | 7.7% |
| KALSHI_LONE_OUTLIER | 18 | 5.6 | 5.6 | 72.2 | 5.6 | 5.6 | 5.6 | 0.0 | 6.16 | 11.1% | 5.6% |
| MARKETS_AGREE | 608 | 65.5 | 34.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,308 | 0.0 | 2.5 | 35.8 | 26.2 | 24.4 | 10.5 | 0.7 | 12.0 | 35.5% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 30,989 | 4995 (16.1%) | 26.2% | 0.8% | {"EXTERNAL_STALE": 3020, "AGREES_WITH_KALSHI": 1308, "ALL_AGREE": 608, "SUPPORTS_MODEL_DIRECTION": 24, "AGREES_WITH_MODEL": 18, "EXTERNAL_OUTLIER": 16, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,801 | 1268 (9.2%) | 36.7% | 1.5% | {"EXTERNAL_STALE": 784, "AGREES_WITH_KALSHI": 465, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,694 | 388 (5.0%) | 37.6% | 2.3% | {"EXTERNAL_STALE": 233, "AGREES_WITH_KALSHI": 146, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,756 | 365 (9.7%) | 38.1% | 2.5% | {"EXTERNAL_STALE": 217, "AGREES_WITH_KALSHI": 139, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,362 | 2813 (22.8%) | 17.8% | 0.7% | {"EXTERNAL_STALE": 1668, "ALL_AGREE": 608, "AGREES_WITH_KALSHI": 500, "EXTERNAL_OUTLIER": 16, "AGREES_WITH_MODEL": 15, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,902 | 10.3 | 7.6 | 19.5 | 14.5 | 22.2 | 16.0 | 9.9 | 14.09 | 48.1% | 25.9% |
| 4-10x | 4,007 | 11.1 | 8.3 | 18.9 | 15.3 | 21.5 | 14.8 | 10.1 | 13.76 | 46.4% | 24.9% |
| <2x | 15,780 | 15.0 | 9.8 | 19.1 | 16.5 | 17.5 | 13.1 | 9.1 | 11.83 | 39.7% | 22.1% |
| >=10x | 5,300 | 10.8 | 6.2 | 15.2 | 14.3 | 22.1 | 19.6 | 11.9 | 16.44 | 53.6% | 31.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,945 | 12.6 | 8.6 | 19.3 | 16.1 | 19.1 | 13.8 | 10.6 | 12.94 | 43.5% | 24.4% |
| 300-1000 | 6,539 | 11.7 | 8.6 | 17.3 | 15.3 | 20.6 | 16.3 | 10.2 | 13.91 | 47.1% | 26.5% |
| <300 | 10,090 | 8.5 | 5.6 | 15.4 | 14.8 | 23.2 | 20.1 | 12.3 | 17.02 | 55.6% | 32.5% |
| >=3000 | 6,415 | 21.3 | 13.0 | 23.5 | 16.5 | 14.1 | 7.0 | 4.7 | 7.93 | 25.7% | 11.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 875 | 0.55 | 0.4117 | 0.5006 | +0.049 | -0.089 | -0.0045 ± 0.0052 |
| ratio 4-10x | 596 | 0.5885 | 0.4419 | 0.4966 | +0.092 | -0.055 | 0.0109 ± 0.0066 |
| ratio <2x | 2166 | 0.5382 | 0.4153 | 0.446 | +0.092 | -0.031 | 0.0124 ± 0.0031 |
| ratio >=10x | 799 | 0.5719 | 0.3964 | 0.4618 | +0.110 | -0.065 | 0.0073 ± 0.0065 |
| thinner_sample 1000-3000 | 1202 | 0.5425 | 0.4155 | 0.4476 | +0.095 | -0.032 | 0.0097 ± 0.0041 |
| thinner_sample 300-1000 | 1002 | 0.5668 | 0.423 | 0.493 | +0.074 | -0.070 | 0.0002 ± 0.0051 |
| thinner_sample <300 | 1489 | 0.562 | 0.3953 | 0.4634 | +0.099 | -0.068 | 0.0094 ± 0.0046 |
| thinner_sample >=3000 | 743 | 0.5354 | 0.4413 | 0.467 | +0.068 | -0.026 | 0.0127 ± 0.0042 |
| data_status ADEQUATE | 1292 | 0.5378 | 0.434 | 0.452 | +0.086 | -0.018 | 0.0118 ± 0.0034 |
| data_status LIMITED | 1012 | 0.5515 | 0.4169 | 0.4822 | +0.069 | -0.065 | 0.0036 ± 0.0047 |
| data_status POOR | 2132 | 0.5636 | 0.402 | 0.4676 | +0.096 | -0.066 | 0.0076 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 650 | 0.2021 | 0.203 | -0.0009 ± 0.0006 | 0.5852 | 0.5872 | 0.5017 | 0.4869 | 0.5215 | -0.072 ± 0.0187 | -0.01 (5) |
| 3-5 | 411 | 0.2053 | 0.2045 | +0.0007 ± 0.0018 | 0.594 | 0.5908 | 0.5031 | 0.4631 | 0.472 | -0.103 ± 0.023 | 0.02 (1) |
| 5-10 | 917 | 0.2028 | 0.202 | +0.0008 ± 0.0022 | 0.5923 | 0.5873 | 0.5113 | 0.4373 | 0.4646 | -0.093 ± 0.0154 | -0.0167 (6) |
| 10-15 | 767 | 0.2152 | 0.2056 | +0.0096 ± 0.0041 | 0.6211 | 0.5932 | 0.5305 | 0.4064 | 0.4289 | -0.104 ± 0.0163 | -0.048 (5) |
| 15-25 | 1001 | 0.2252 | 0.2134 | +0.0118 ± 0.0057 | 0.645 | 0.6109 | 0.5783 | 0.3826 | 0.4505 | -0.093 ± 0.0145 | -0.0033 (9) |
| 25-40 | 574 | 0.2227 | 0.2102 | +0.0125 ± 0.0114 | 0.6351 | 0.6039 | 0.6604 | 0.3506 | 0.4826 | -0.073 ± 0.0175 | -0.01 (1) |
| 40+ | 116 | 0.2743 | 0.202 | +0.0723 ± 0.036 | 0.7526 | 0.5904 | 0.7587 | 0.3114 | 0.4569 | -0.070 ± 0.0354 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3343 | 0.1857 | 0.1866 | -0.0010 ± 0.0003 | 0.547 | 0.5481 | 0.4921 | 0.477 | 0.5103 | -0.022 ± 0.0076 | -0.0129 (17) |
| 3-5 | 2207 | 0.1995 | 0.1982 | +0.0014 ± 0.0008 | 0.5801 | 0.5744 | 0.4856 | 0.4456 | 0.4477 | -0.054 ± 0.0096 | 0.0 (2) |
| 5-10 | 4791 | 0.1982 | 0.195 | +0.0032 ± 0.001 | 0.5804 | 0.5693 | 0.4822 | 0.4084 | 0.4225 | -0.047 ± 0.0065 | -0.0119 (21) |
| 10-15 | 4072 | 0.1981 | 0.1804 | +0.0177 ± 0.0017 | 0.5818 | 0.532 | 0.4875 | 0.3631 | 0.3539 | -0.072 ± 0.0066 | -0.0281 (16) |
| 15-25 | 5095 | 0.2093 | 0.1697 | +0.0396 ± 0.0023 | 0.6123 | 0.5021 | 0.5059 | 0.3097 | 0.3081 | -0.075 ± 0.0057 | -0.0025 (44) |
| 25-40 | 4004 | 0.2226 | 0.1289 | +0.0937 ± 0.0035 | 0.6392 | 0.3946 | 0.5325 | 0.2192 | 0.23 | -0.059 ± 0.0055 | -0.01 (1) |
| 40+ | 2610 | 0.38 | 0.0457 | +0.3343 ± 0.0047 | 0.9899 | 0.1753 | 0.6331 | 0.1068 | 0.0651 | -0.077 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 511 | 0.2086 | 0.2094 | -0.0008 ± 0.0007 | 0.5997 | 0.6015 | 0.5073 | 0.4921 | 0.5205 | -0.099 ± 0.0218 | -0.01 (3) |
| 3-5 | 367 | 0.2259 | 0.223 | +0.0029 ± 0.002 | 0.6384 | 0.6325 | 0.516 | 0.4761 | 0.455 | -0.132 ± 0.0263 | 0.02 (1) |
| 5-10 | 799 | 0.2065 | 0.2062 | +0.0003 ± 0.0024 | 0.5994 | 0.5978 | 0.5468 | 0.4719 | 0.5106 | -0.081 ± 0.0165 | -0.01 (4) |
| 10-15 | 737 | 0.2176 | 0.21 | +0.0076 ± 0.0042 | 0.6248 | 0.6058 | 0.5645 | 0.4402 | 0.4735 | -0.111 ± 0.0176 | -0.04 (5) |
| 15-25 | 1027 | 0.2303 | 0.2105 | +0.0197 ± 0.0056 | 0.6535 | 0.6037 | 0.5879 | 0.392 | 0.444 | -0.101 ± 0.0146 | -0.0133 (9) |
| 25-40 | 719 | 0.2623 | 0.1985 | +0.0638 ± 0.0104 | 0.7315 | 0.5782 | 0.6535 | 0.3379 | 0.3964 | -0.113 ± 0.0163 | -0.0075 (4) |
| 40+ | 276 | 0.3548 | 0.1732 | +0.1816 ± 0.0247 | 0.9757 | 0.5174 | 0.7339 | 0.2501 | 0.3188 | -0.068 ± 0.024 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2846 | 0.1953 | 0.1956 | -0.0003 ± 0.0003 | 0.5676 | 0.5682 | 0.5109 | 0.4959 | 0.5112 | -0.043 ± 0.0086 | -0.0133 (15) |
| 3-5 | 1906 | 0.2005 | 0.1995 | +0.0010 ± 0.0008 | 0.5791 | 0.5763 | 0.5142 | 0.4743 | 0.4811 | -0.047 ± 0.0105 | 0.02 (1) |
| 5-10 | 4226 | 0.1964 | 0.1943 | +0.0021 ± 0.001 | 0.5776 | 0.5681 | 0.5106 | 0.4366 | 0.4621 | -0.035 ± 0.0069 | -0.0117 (6) |
| 10-15 | 3689 | 0.202 | 0.1898 | +0.0122 ± 0.0018 | 0.5908 | 0.5529 | 0.5132 | 0.3892 | 0.4028 | -0.056 ± 0.0073 | -0.0189 (18) |
| 15-25 | 5068 | 0.2163 | 0.1783 | +0.0380 ± 0.0023 | 0.628 | 0.5246 | 0.5255 | 0.3296 | 0.3348 | -0.068 ± 0.006 | -0.0086 (42) |
| 25-40 | 4665 | 0.2514 | 0.1367 | +0.1147 ± 0.0034 | 0.7072 | 0.42 | 0.5577 | 0.2405 | 0.2208 | -0.085 ± 0.0054 | -0.0044 (18) |
| 40+ | 3722 | 0.3928 | 0.0609 | +0.3319 ± 0.0046 | 1.034 | 0.2173 | 0.6507 | 0.1192 | 0.0857 | -0.071 ± 0.004 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 621 | 0.2002 | 0.2023 | -0.0021 ± 0.0006 | 0.5812 | 0.5864 | 0.5012 | 0.4861 | 0.5459 | -0.035 ± 0.0188 | -0.0137 (8) |
| 3-5 | 444 | 0.2032 | 0.2015 | +0.0017 ± 0.0017 | 0.5899 | 0.5843 | 0.5052 | 0.4655 | 0.4662 | -0.117 ± 0.0223 | 0.0067 (3) |
| 5-10 | 937 | 0.2022 | 0.1985 | +0.0037 ± 0.0022 | 0.5909 | 0.5785 | 0.508 | 0.434 | 0.444 | -0.106 ± 0.0149 | -0.0071 (7) |
| 10-15 | 766 | 0.2094 | 0.2055 | +0.0038 ± 0.0041 | 0.608 | 0.5935 | 0.5403 | 0.4166 | 0.4648 | -0.085 ± 0.0163 | -0.0317 (6) |
| 15-25 | 950 | 0.2309 | 0.2141 | +0.0169 ± 0.0058 | 0.6596 | 0.6119 | 0.5892 | 0.3948 | 0.4484 | -0.105 ± 0.015 | -0.03 (1) |
| 25-40 | 596 | 0.2144 | 0.2182 | -0.0038 ± 0.0112 | 0.6184 | 0.6223 | 0.671 | 0.3599 | 0.5185 | -0.056 ± 0.0172 | 0.015 (2) |
| 40+ | 122 | 0.2899 | 0.2134 | +0.0764 ± 0.0363 | 0.8007 | 0.6154 | 0.769 | 0.3195 | 0.4672 | -0.069 ± 0.0382 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3270 | 0.1853 | 0.1859 | -0.0006 ± 0.0003 | 0.5453 | 0.5462 | 0.49 | 0.4748 | 0.4899 | -0.037 ± 0.0076 | -0.0163 (35) |
| 3-5 | 2225 | 0.1953 | 0.1934 | +0.0019 ± 0.0008 | 0.5732 | 0.567 | 0.4871 | 0.4475 | 0.444 | -0.063 ± 0.0095 | -0.0094 (18) |
| 5-10 | 4854 | 0.1958 | 0.19 | +0.0058 ± 0.0009 | 0.5755 | 0.5566 | 0.4833 | 0.4093 | 0.4075 | -0.061 ± 0.0063 | -0.01 (31) |
| 10-15 | 3947 | 0.1923 | 0.177 | +0.0152 ± 0.0017 | 0.5683 | 0.5228 | 0.4998 | 0.3764 | 0.376 | -0.064 ± 0.0067 | -0.015 (12) |
| 15-25 | 5274 | 0.2112 | 0.1728 | +0.0384 ± 0.0022 | 0.6169 | 0.5093 | 0.5155 | 0.3205 | 0.3199 | -0.072 ± 0.0057 | -0.03 (2) |
| 25-40 | 4018 | 0.2196 | 0.1326 | +0.0870 ± 0.0036 | 0.6335 | 0.4026 | 0.5378 | 0.2216 | 0.2439 | -0.051 ± 0.0055 | 0.01 (3) |
| 40+ | 2534 | 0.3952 | 0.0504 | +0.3448 ± 0.0051 | 1.0327 | 0.1877 | 0.6456 | 0.1136 | 0.0695 | -0.081 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1007 | 0.1951 | 0.1953 | -0.0002 ± 0.0005 | 0.5696 | 0.5696 | 0.5027 | 0.4876 | 0.4955 | -0.057 ± 0.0141 | -0.0224 (49) |
| 3-5 | 702 | 0.1928 | 0.1921 | +0.0008 ± 0.0013 | 0.5632 | 0.5601 | 0.491 | 0.4511 | 0.4587 | -0.061 ± 0.0169 | -0.0194 (34) |
| 5-10 | 1462 | 0.2025 | 0.1964 | +0.0060 ± 0.0017 | 0.5944 | 0.5755 | 0.4962 | 0.4228 | 0.4193 | -0.075 ± 0.0118 | -0.005 (78) |
| 10-15 | 974 | 0.2111 | 0.1992 | +0.0120 ± 0.0036 | 0.6117 | 0.5806 | 0.5231 | 0.3999 | 0.4107 | -0.071 ± 0.0146 | 0.0014 (64) |
| 15-25 | 1309 | 0.2316 | 0.2109 | +0.0206 ± 0.005 | 0.6613 | 0.6069 | 0.5786 | 0.3838 | 0.4293 | -0.073 ± 0.0127 | -0.0214 (59) |
| 25-40 | 793 | 0.2473 | 0.2079 | +0.0394 ± 0.01 | 0.7026 | 0.5973 | 0.6746 | 0.362 | 0.4552 | -0.086 ± 0.0151 | -0.0219 (26) |
| 40+ | 263 | 0.3519 | 0.2022 | +0.1497 ± 0.0273 | 1.0166 | 0.5918 | 0.8077 | 0.3256 | 0.4297 | -0.091 ± 0.0252 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3305 | 0.1833 | 0.1835 | -0.0002 ± 0.0003 | 0.5399 | 0.5395 | 0.5042 | 0.4888 | 0.5002 | -0.037 ± 0.0075 | -0.0157 (88) |
| 3-5 | 2289 | 0.1955 | 0.1936 | +0.0019 ± 0.0007 | 0.5701 | 0.5657 | 0.4971 | 0.4573 | 0.4535 | -0.054 ± 0.0093 | -0.0209 (69) |
| 5-10 | 4563 | 0.1976 | 0.1893 | +0.0083 ± 0.001 | 0.5809 | 0.5564 | 0.4914 | 0.4179 | 0.4013 | -0.071 ± 0.0065 | -0.0082 (132) |
| 10-15 | 3200 | 0.2075 | 0.1914 | +0.0161 ± 0.0019 | 0.6038 | 0.5616 | 0.5295 | 0.4063 | 0.4016 | -0.067 ± 0.0078 | -0.0053 (105) |
| 15-25 | 3970 | 0.2298 | 0.2 | +0.0298 ± 0.0028 | 0.6629 | 0.5795 | 0.5704 | 0.375 | 0.3977 | -0.065 ± 0.0071 | -0.0253 (107) |
| 25-40 | 2731 | 0.2589 | 0.1844 | +0.0745 ± 0.0052 | 0.7336 | 0.5379 | 0.6334 | 0.3194 | 0.3603 | -0.077 ± 0.008 | -0.0229 (51) |
| 40+ | 1211 | 0.3781 | 0.1457 | +0.2323 ± 0.0115 | 1.0711 | 0.4392 | 0.7303 | 0.2266 | 0.2609 | -0.070 ± 0.0103 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4436 | 1.032 ± 0.042 | 1.114 | 0.1685 | 0.1633 | 0.2146 | 0.2066 |
| gen2 | 4436 | 0.837 ± 0.039 | 1.082 | 0.1679 | 0.164 | 0.234 | 0.2063 |
| gen1_elo | 4436 | 1.004 ± 0.041 | 1.109 | 0.1753 | 0.1634 | 0.2135 | 0.2069 |
| gen1_sr | 4436 | 1.021 ± 0.051 | 1.156 | 0.1291 | 0.1659 | 0.2301 | 0.2059 |
| gen1_ledger | 6510 | 0.858 ± 0.03 | 1.063 | 0.1834 | 0.1777 | 0.2189 | 0.2007 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 22,153)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,049 | 22.8% |
| STALE_QUOTE | market_freshness | 4,794 | 21.6% |
| BOOK_QUALITY | execution | 4,206 | 19.0% |
| POOR_DATA | data | 2,484 | 11.2% |
| LIMITED_DATA | data | 1,378 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,196 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,067 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 939 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 652 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 387 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.8%, market_freshness 21.6%, execution 19.0%, data 17.4%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.0%, LOW_DATA_QUALITY 70.7%, THIN_PLAYER_HISTORY 59.5%, STALE_PLAYER_DATA 49.5%, STALE_KALSHI_QUOTE 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.3%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.9%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.9%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.3%, POST_SETTLEMENT_OBSERVATION 22.8%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,869)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,067 | 34.3% |
| STALE_QUOTE | market_freshness | 2,221 | 18.7% |
| BOOK_QUALITY | execution | 2,208 | 18.6% |
| POOR_DATA | data | 1,018 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 641 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 527 | 4.4% |
| LIMITED_DATA | data | 417 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 415 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 264 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 90 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.3%, market_freshness 18.7%, execution 18.6%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.2%, THIN_PLAYER_HISTORY 61.6%, STALE_KALSHI_QUOTE 52.1%, STALE_PLAYER_DATA 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 24.4%, PLAYER_IDENTITY_RISK 20.0%, MODEL_HIGH_UNCERTAINTY 18.3%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.4%, POST_SETTLEMENT_OBSERVATION 34.3%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9194, "IDENTITY_AMBIGUOUS": 2675}; ticker orientation: {"VERIFIED": 11869}.

Checks: discipline:AMBIGUOUS 833, discipline:PASS 11036, identity_confidence:AMBIGUOUS 2377, identity_confidence:PASS 9492, level_mapping:NA 845, level_mapping:PASS 11024, market_pair:AMBIGUOUS 446, market_pair:NA 295, market_pair:PASS 11128, model_complement:NA 262, model_complement:PASS 11607, namesake:AMBIGUOUS 6, namesake:PASS 11863, physical_match_id:NA 4175, physical_match_id:PASS 7694, player_ids:PASS 11869, same_pair_other_event:PASS 11869, ticker_orientation:PASS 11869

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,557 | 4.5% | 4.0% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 48, "data": 35, "execution": 23, "model_calibration": 18, "market_freshness/coverage": 15, "coverage": 13} | 5.92 | 0.2224 / 0.2181 (519) | 18.8% | 3.5% | 3.2% | 2.7% |
| CHALLENGER | 8,239 | 17.1% | 7.0% | 11.8% | {"coverage": 788, "market_freshness/coverage": 169, "market_freshness": 159, "data": 143, "model_calibration_or_unknown": 68, "execution": 34, "model_calibration": 30, "mapping": 15, "possible_market_error": 1} | 7.6 | 0.22 / 0.2099 (1918) | 34.3% | 17.7% | 4.0% | 22.2% |
| DOUBLES | 1,756 | 47.4% | 47.1% | 7.0% | {"execution": 455, "mapping": 210, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.85 | 0.3098 / 0.2359 (434) | 13.3% | 0.0% | 100.0% | 6.8% |
| ITF_MEN | 14,762 | 25.5% | 17.7% | 31.7% | {"coverage": 1399, "execution": 714, "market_freshness": 643, "data": 498, "market_freshness/coverage": 327, "mapping": 175, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.94 | 0.2158 / 0.1978 (3294) | 37.4% | 69.8% | 19.8% | 22.2% |
| ITF_WOMEN | 19,442 | 27.2% | 19.9% | 44.6% | {"coverage": 1835, "market_freshness": 1160, "execution": 932, "data": 722, "market_freshness/coverage": 441, "mapping": 121, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.88 | 0.2037 / 0.195 (3734) | 39.8% | 56.2% | 10.0% | 22.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,144 | 5.4% | 4.9% | 1.4% | {"market_freshness": 59, "model_calibration_or_unknown": 36, "execution": 26, "model_calibration": 16, "coverage": 12, "data": 11, "market_freshness/coverage": 10, "mapping": 1} | 7.65 | 0.2339 / 0.2288 (517) | 24.4% | 1.3% | 1.7% | 3.5% |
| WTA125 | 1,465 | 13.0% | 10.5% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 39, "market_freshness/coverage": 38, "data": 26, "execution": 19, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.55 | 0.219 / 0.2065 (488) | 22.9% | 10.1% | 6.8% | 9.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 50 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9683, "by_level_share_of_ge_25pp": {"ATP": 0.0173, "CHALLENGER": 0.1185, "DOUBLES": 0.0702, "ITF_MEN": 0.3168, "ITF_WOMEN": 0.4458, "OTHER": 0.001, "WTA": 0.0144, "WTA125": 0.016}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5207, "share_primary_cause_market_settled_or_in_play": 0.4317, "share_primary_cause_stale_quote_only": 0.1871}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11869, "identity_ambiguous_share": 0.2254, "ticker_orientation": {"VERIFIED": 11869}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7694, "with_external": 388, "coverage": 0.0504, "external_status": {"EXTERNAL_STALE": 233, "AGREES_WITH_KALSHI": 146, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 233, "MODEL_LONE_OUTLIER": 146, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3763, "share_external_supports_model": 0.0232}, "pregame_clean_ge_25pp": {"n": 3756, "with_external": 365, "coverage": 0.0972, "external_status": {"EXTERNAL_STALE": 217, "AGREES_WITH_KALSHI": 139, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 217, "MODEL_LONE_OUTLIER": 139, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3808, "share_external_supports_model": 0.0247}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.42, "median_min_matches": 21.0, "median_max_days_since_last": 227.0, "share_severe_asymmetry": 0.2145, "data_status": {"POOR": 6578, "LIMITED": 3122, "ADEQUATE": 2169}, "comparison_lt_10pp": {"median_thinner_serve_points": 1756.5, "median_sample_ratio": 1.68, "median_min_matches": 98.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 875, "model_minus_observed": 0.0494, "kalshi_minus_observed": -0.0889, "brier_diff_model_minus_kalshi": -0.0045}, "4-10x": {"n": 596, "model_minus_observed": 0.0918, "kalshi_minus_observed": -0.0547, "brier_diff_model_minus_kalshi": 0.0109}, "<2x": {"n": 2166, "model_minus_observed": 0.0922, "kalshi_minus_observed": -0.0307, "brier_diff_model_minus_kalshi": 0.0124}, ">=10x": {"n": 799, "model_minus_observed": 0.1101, "kalshi_minus_observed": -0.0654, "brier_diff_model_minus_kalshi": 0.0073}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4436, "model": {"intercept": -0.536, "slope": 0.837, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.21, "slope": 1.082, "slope_se": 0.044}, "mean_extremity_model": 0.1679, "mean_extremity_kalshi": 0.164, "model_brier": 0.234, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0277, "brier_diff_se": 0.0028, "model_logloss": 0.6642, "kalshi_logloss": 0.5956}, "fair_v1": {"n": 4436, "model": {"intercept": -0.42, "slope": 1.032, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.284, "slope": 1.114, "slope_se": 0.044}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1633, "model_brier": 0.2146, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": 0.0079, "brier_diff_se": 0.0023, "model_logloss": 0.618, "kalshi_logloss": 0.5962}, "gen1_elo": {"n": 4436, "model": {"intercept": -0.395, "slope": 1.004, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.305, "slope": 1.109, "slope_se": 0.043}, "mean_extremity_model": 0.1753, "mean_extremity_kalshi": 0.1634, "model_brier": 0.2135, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0065, "brier_diff_se": 0.0024, "model_logloss": 0.6166, "kalshi_logloss": 0.5968}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2483, "share_ge_15": 0.4454, "median_abs_gap": 13.14, "n": 30989}, "gen1_elo": {"share_ge_25": 0.2457, "share_ge_15": 0.4445, "median_abs_gap": 13.0, "n": 30989}, "gen1_sr": {"share_ge_25": 0.3161, "share_ge_15": 0.5238, "median_abs_gap": 15.99, "n": 30989}, "gen2": {"share_ge_25": 0.3195, "share_ge_15": 0.5138, "median_abs_gap": 15.58, "n": 30989}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1559, "share_ge_15": 0.3615, "median_abs_gap": 10.94, "n": 24093}, "gen1_elo": {"share_ge_25": 0.1566, "share_ge_15": 0.3594, "median_abs_gap": 10.74, "n": 24090}, "gen1_sr": {"share_ge_25": 0.2229, "share_ge_15": 0.446, "median_abs_gap": 13.1, "n": 24094}, "gen2": {"share_ge_25": 0.239, "share_ge_15": 0.4456, "median_abs_gap": 13.07, "n": 24095}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.92, "share_ge_25_all": 0.045, "share_ge_25_pregame_clean": 0.0399}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0544, "share_ge_25_pregame_clean": 0.0491}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2342, "share_within_10pp_all": 0.4323, "share_within_10pp_pregame_clean": 0.4847, "corr_model_vs_mid_pregame_clean": 0.8426}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 650, "model_brier": 0.2021, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 767, "model_brier": 0.2152, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0096}, "15-25": {"n_settled": 1001, "model_brier": 0.2252, "kalshi_brier": 0.2134, "brier_diff_model_minus_kalshi": 0.0118}, "25-40": {"n_settled": 574, "model_brier": 0.2227, "kalshi_brier": 0.2102, "brier_diff_model_minus_kalshi": 0.0125}, "3-5": {"n_settled": 411, "model_brier": 0.2053, "kalshi_brier": 0.2045, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 116, "model_brier": 0.2743, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0723}, "5-10": {"n_settled": 917, "model_brier": 0.2028, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0008}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.536, "slope": 0.837, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.21, "slope": 1.082, "slope_se": 0.044}, "n": 4436}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.504, "slope": 0.858, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.153, "slope": 1.063, "slope_se": 0.034}, "n": 6510}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 434, "model_brier": 0.3098, "kalshi_brier": 0.2359, "brier_diff_model_minus_kalshi": 0.074, "brier_diff_se": 0.0145, "corr_model_outcome": 0.0408, "corr_kalshi_outcome": 0.2531}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
