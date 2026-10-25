# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-25T05:49Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 52,776): 0-3 13.9%, 3-5 9.5%, 5-10 19.8%, 10-15 15.3%, 15-25 19.2%, 25-40 14.0%, 40+ 8.2%; median gap 12.09 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.6%, Challenger 11.8%, doubles 6.8%). Main tour: ATP 4.5% and WTA 5.6% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,753): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.5%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.3%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.5%, market_freshness 18.7%, execution 18.3%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,753 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.4% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 494.0 points vs 1743.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.032, Gen-2 0.836, Gen-1 ledger 0.858 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 572 model 0.2228 vs Kalshi 0.2103; n 115 model 0.2766 vs Kalshi 0.2018.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 228,997 model-market comparisons (372,143 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 77,059 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-25T05:35:26.032134+00:00'], shadow board 60,912 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-25T05:35:29.455181+00:00'], Model 4 28,728 rows, 20,205 settled tickers, 7,202 tickers with an external scan.
* By model: {"gen1_ledger": 52550, "gen1_elo": 30631, "fair_v1": 30631, "gen2": 30631, "gen1_sr": 30631, "model4_fundamental": 26979, "model4_conditioned": 26944}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 52,776 | 13.9 | 9.5 | 19.8 | 15.3 | 19.2 | 14.0 | 8.2 | 12.09 | 41.5% | 22.3% |
| MW fair_v1 | 30,631 | 12.8 | 8.5 | 18.5 | 15.6 | 19.7 | 15.0 | 9.9 | 13.16 | 44.6% | 24.9% |
| MW gen1_elo | 30,631 | 12.7 | 8.6 | 19.0 | 15.2 | 19.9 | 15.0 | 9.7 | 13.01 | 44.5% | 24.6% |
| MW gen1_ledger | 22,145 | 15.5 | 10.8 | 21.6 | 15.1 | 18.6 | 12.7 | 5.8 | 10.53 | 37.1% | 18.6% |
| MW gen1_sr | 30,631 | 10.2 | 7.1 | 16.6 | 13.6 | 20.8 | 18.7 | 13.0 | 16.01 | 52.5% | 31.7% |
| MW gen2 | 30,631 | 11.0 | 7.3 | 16.2 | 14.0 | 19.4 | 17.9 | 14.1 | 15.62 | 51.5% | 32.0% |
| all families model4_conditioned | 26,944 | 21.8 | 18.8 | 34.7 | 17.6 | 4.5 | 1.5 | 1.1 | 5.99 | 7.0% | 2.6% |
| all families model4_fundamental | 26,979 | 16.8 | 13.3 | 34.1 | 20.5 | 10.6 | 3.5 | 1.3 | 7.77 | 15.4% | 4.8% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.8%, >=15pp 41.5%, >=20pp 30.8%, >=25pp 22.3%, >=30pp 16.1%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.44pp; >=10pp 45.3%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,727 | 28.1 | 14.2 | 25.2 | 15.4 | 11.9 | 4.6 | 0.7 | 6.17 | 17.2% | 5.3% |
| CHALLENGER | 4,768 | 15.8 | 10.0 | 20.3 | 15.8 | 14.9 | 12.4 | 11.0 | 11.09 | 38.3% | 23.4% |
| ITF_MEN | 8,436 | 10.1 | 7.3 | 16.8 | 14.7 | 21.5 | 17.5 | 12.2 | 15.43 | 51.2% | 29.6% |
| ITF_WOMEN | 12,083 | 9.4 | 6.9 | 15.9 | 15.3 | 22.3 | 18.2 | 12.0 | 15.8 | 52.5% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,942 | 17.5 | 12.9 | 26.4 | 19.1 | 17.5 | 5.9 | 0.7 | 8.25 | 24.1% | 6.6% |
| WTA125 | 669 | 13.2 | 7.3 | 23.2 | 20.8 | 20.2 | 13.4 | 1.9 | 11.31 | 35.6% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,727 | 23.9 | 15.0 | 24.8 | 17.8 | 12.9 | 4.6 | 0.9 | 6.7 | 18.4% | 5.5% |
| CHALLENGER | 4,768 | 14.9 | 8.8 | 18.3 | 14.6 | 17.7 | 13.9 | 11.8 | 12.59 | 43.4% | 25.7% |
| ITF_MEN | 8,436 | 8.2 | 5.9 | 14.4 | 13.0 | 19.7 | 21.0 | 17.8 | 18.72 | 58.6% | 38.9% |
| ITF_WOMEN | 12,083 | 8.2 | 5.6 | 13.7 | 13.2 | 20.5 | 21.0 | 17.7 | 19.13 | 59.3% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,942 | 14.2 | 10.2 | 22.2 | 16.1 | 22.6 | 13.4 | 1.3 | 10.9 | 37.2% | 14.7% |
| WTA125 | 669 | 6.7 | 4.6 | 16.7 | 17.6 | 25.9 | 19.6 | 8.8 | 17.0 | 54.3% | 28.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,727 | 23.6 | 12.6 | 24.0 | 16.5 | 15.1 | 6.9 | 1.2 | 7.5 | 23.3% | 8.2% |
| CHALLENGER | 4,768 | 14.3 | 9.2 | 20.6 | 15.6 | 16.2 | 13.0 | 11.1 | 11.48 | 40.3% | 24.1% |
| ITF_MEN | 8,436 | 9.7 | 7.3 | 16.8 | 13.8 | 22.2 | 17.8 | 12.3 | 15.84 | 52.3% | 30.2% |
| ITF_WOMEN | 12,083 | 9.4 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.2 | 15.59 | 51.9% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 1,942 | 23.8 | 17.5 | 30.5 | 15.0 | 10.0 | 2.6 | 0.5 | 6.01 | 13.2% | 3.1% |
| WTA125 | 669 | 22.7 | 12.0 | 29.0 | 16.0 | 14.1 | 6.0 | 0.3 | 7.73 | 20.3% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,694 | 25.1 | 19.1 | 30.1 | 12.9 | 9.4 | 3.0 | 0.3 | 5.66 | 12.8% | 3.3% |
| CHALLENGER | 3,293 | 21.5 | 14.4 | 26.6 | 14.6 | 14.6 | 6.7 | 1.8 | 7.33 | 23.0% | 8.4% |
| DOUBLES | 1,698 | 5.2 | 4.6 | 12.1 | 10.4 | 20.7 | 26.0 | 20.9 | 23.75 | 67.6% | 46.9% |
| ITF_MEN | 6,243 | 13.7 | 9.1 | 20.0 | 16.1 | 21.3 | 13.3 | 6.5 | 12.15 | 41.0% | 19.8% |
| ITF_WOMEN | 7,200 | 12.6 | 8.9 | 19.2 | 15.2 | 21.6 | 16.2 | 6.2 | 12.89 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,123 | 22.8 | 15.8 | 30.1 | 17.8 | 9.6 | 3.5 | 0.4 | 6.82 | 13.5% | 3.8% |
| WTA125 | 745 | 21.3 | 13.8 | 21.7 | 18.3 | 14.6 | 8.1 | 2.1 | 8.22 | 24.8% | 10.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,652 | 28.4 | 14.4 | 25.6 | 15.3 | 11.7 | 4.2 | 0.5 | 6.04 | 16.3% | 4.6% |
| CHALLENGER | 3,372 | 20.6 | 12.4 | 24.9 | 18.2 | 15.2 | 6.8 | 1.9 | 8.38 | 23.9% | 8.7% |
| ITF_MEN | 6,177 | 12.2 | 8.8 | 20.2 | 16.6 | 22.7 | 14.3 | 5.1 | 12.55 | 42.2% | 19.5% |
| ITF_WOMEN | 9,027 | 11.2 | 8.2 | 18.1 | 17.3 | 24.3 | 15.3 | 5.5 | 13.53 | 45.1% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,887 | 17.8 | 12.8 | 26.4 | 19.3 | 17.5 | 5.6 | 0.7 | 8.24 | 23.7% | 6.2% |
| WTA125 | 643 | 13.5 | 7.2 | 22.7 | 21.1 | 20.8 | 13.1 | 1.6 | 11.33 | 35.5% | 14.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,652 | 24.2 | 15.4 | 25.0 | 17.7 | 12.9 | 4.2 | 0.6 | 6.5 | 17.7% | 4.8% |
| CHALLENGER | 3,372 | 18.9 | 11.3 | 22.7 | 17.4 | 18.2 | 9.5 | 2.1 | 9.29 | 29.7% | 11.5% |
| ITF_MEN | 6,178 | 9.7 | 7.1 | 16.8 | 15.1 | 21.6 | 19.2 | 10.5 | 15.48 | 51.3% | 29.7% |
| ITF_WOMEN | 9,028 | 9.3 | 6.5 | 15.2 | 14.7 | 22.5 | 20.5 | 11.3 | 16.69 | 54.4% | 31.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,887 | 14.3 | 10.2 | 22.3 | 16.1 | 22.6 | 13.2 | 1.3 | 10.9 | 37.1% | 14.5% |
| WTA125 | 643 | 6.5 | 4.8 | 16.8 | 18.0 | 25.8 | 20.1 | 7.9 | 16.74 | 53.8% | 28.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,644 | 25.3 | 19.4 | 30.2 | 13.0 | 9.1 | 2.9 | 0.2 | 5.6 | 12.1% | 3.0% |
| CHALLENGER | 2,880 | 22.9 | 15.4 | 28.1 | 14.6 | 14.0 | 4.6 | 0.5 | 6.81 | 19.1% | 5.1% |
| DOUBLES | 1,579 | 5.2 | 4.8 | 12.4 | 10.6 | 20.5 | 26.0 | 20.6 | 23.62 | 67.1% | 46.6% |
| ITF_MEN | 5,238 | 14.9 | 9.8 | 21.6 | 16.9 | 21.2 | 11.6 | 4.0 | 11.16 | 36.8% | 15.6% |
| ITF_WOMEN | 5,969 | 13.5 | 9.4 | 20.6 | 16.1 | 21.9 | 15.0 | 3.5 | 11.81 | 40.4% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,073 | 23.3 | 16.3 | 30.1 | 17.8 | 9.6 | 2.8 | 0.1 | 6.69 | 12.5% | 2.9% |
| WTA125 | 634 | 23.3 | 15.3 | 23.2 | 19.7 | 12.9 | 5.0 | 0.5 | 7.32 | 18.4% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,698 | 5.2 | 4.6 | 12.1 | 10.4 | 20.7 | 26.0 | 20.9 | 23.75 | 67.6% | 46.9% |
| singles | 20,447 | 16.3 | 11.3 | 22.3 | 15.4 | 18.4 | 11.6 | 4.6 | 10.01 | 34.6% | 16.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 7 | 14.3 | 28.6 | 42.9 | 0.0 | 14.3 | 0.0 | 0.0 | 5.48 | 14.3% | 0.0% |
| Clay | 6,733 | 12.9 | 9.0 | 19.2 | 15.7 | 18.8 | 14.5 | 9.9 | 12.8 | 43.2% | 24.4% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 19,030 | 13.3 | 8.5 | 18.6 | 15.2 | 19.7 | 14.9 | 9.7 | 13.07 | 44.3% | 24.6% |
| UNKNOWN | 4,624 | 10.7 | 7.5 | 17.0 | 16.9 | 20.6 | 16.3 | 11.1 | 14.13 | 48.0% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,745 | 19.5 | 11.9 | 21.6 | 16.5 | 15.0 | 9.2 | 6.3 | 9.14 | 30.5% | 15.5% |
| B | 3,801 | 12.4 | 8.7 | 19.5 | 16.3 | 19.3 | 12.8 | 11.1 | 12.67 | 43.1% | 23.8% |
| C | 4,279 | 11.6 | 8.7 | 19.7 | 15.3 | 19.4 | 14.7 | 10.7 | 13.18 | 44.7% | 25.3% |
| D | 4,734 | 12.1 | 7.7 | 17.4 | 15.5 | 21.5 | 15.8 | 10.1 | 13.98 | 47.4% | 25.9% |
| F | 9,072 | 7.6 | 5.5 | 15.1 | 14.6 | 23.5 | 21.2 | 12.6 | 17.79 | 57.3% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,339 | 23.2 | 15.8 | 28.9 | 15.2 | 11.5 | 4.0 | 1.4 | 6.65 | 17.0% | 5.4% |
| B | 3,009 | 16.2 | 10.4 | 23.0 | 16.2 | 19.6 | 10.6 | 3.9 | 10.06 | 34.1% | 14.5% |
| C | 4,347 | 11.1 | 7.4 | 18.4 | 14.3 | 21.4 | 16.8 | 10.7 | 14.4 | 48.8% | 27.5% |
| D | 3,048 | 14.4 | 9.7 | 19.9 | 14.6 | 21.0 | 14.3 | 6.1 | 12.05 | 41.4% | 20.4% |
| F | 5,402 | 10.2 | 8.4 | 15.7 | 15.1 | 22.6 | 19.8 | 8.2 | 15.32 | 50.6% | 28.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,009 | 17.8 | 10.6 | 20.9 | 16.2 | 15.6 | 10.1 | 8.8 | 10.19 | 34.5% | 19.0% |
| LIMITED | 6,476 | 13.3 | 10.1 | 20.2 | 15.9 | 19.3 | 13.4 | 7.8 | 11.98 | 40.5% | 21.2% |
| POOR | 14,146 | 9.1 | 6.3 | 16.0 | 15.0 | 22.7 | 19.2 | 11.7 | 16.25 | 53.6% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,404 | 25.2 | 19.2 | 33.7 | 13.6 | 5.8 | 2.2 | 0.2 | 5.55 | 8.3% | 2.5% |
| GAME_SPREAD | 4,914 | 22.2 | 15.3 | 33.4 | 17.2 | 9.2 | 2.4 | 0.3 | 6.74 | 12.0% | 2.8% |
| MATCH_WINNER | 22,145 | 15.5 | 10.8 | 21.6 | 15.1 | 18.6 | 12.7 | 5.8 | 10.53 | 37.1% | 18.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 11,248 | 28.4 | 16.8 | 31.0 | 12.6 | 8.6 | 2.3 | 0.4 | 5.58 | 11.2% | 2.6% |
| TOTAL_GAMES | 7,815 | 9.1 | 9.9 | 36.4 | 28.2 | 10.3 | 3.3 | 2.8 | 9.39 | 16.4% | 6.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,623 | 25.1 | 32.6 | 32.5 | 5.3 | 3.4 | 0.8 | 0.2 | 4.53 | 4.5% | 1.0% |
| GAME_SPREAD | 6,380 | 45.7 | 16.7 | 26.7 | 7.9 | 1.7 | 0.9 | 0.3 | 3.46 | 3.0% | 1.2% |
| TOTAL_GAMES | 10,941 | 5.1 | 7.9 | 41.3 | 34.0 | 6.9 | 2.5 | 2.2 | 9.54 | 11.7% | 4.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,634 | 24.0 | 17.4 | 35.3 | 13.1 | 7.3 | 2.6 | 0.4 | 5.92 | 10.3% | 3.0% |
| GAME_SPREAD | 6,383 | 19.7 | 13.3 | 27.9 | 20.7 | 13.2 | 4.3 | 0.9 | 7.96 | 18.4% | 5.2% |
| TOTAL_GAMES | 10,962 | 8.8 | 9.7 | 36.7 | 26.8 | 11.9 | 3.7 | 2.4 | 9.41 | 18.0% | 6.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 30,631 | 44.6% | 24.9% | 13.16 | 36.2% | 15.6% | 10.95 |
| gen1_elo | 30,631 | 44.5% | 24.6% | 13.01 | 36.0% | 15.7% | 10.74 |
| gen1_sr | 30,631 | 52.5% | 31.7% | 16.01 | 44.7% | 22.3% | 13.12 |
| gen2 | 30,631 | 51.5% | 32.0% | 15.62 | 44.6% | 23.9% | 13.1 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,491 | 15.7 | 10.3 | 21.4 | 17.3 | 20.1 | 11.9 | 3.3 | 10.72 | 35.3% | 15.2% |
| STALE | 15,140 | 9.9 | 6.6 | 15.5 | 13.8 | 19.2 | 18.1 | 16.8 | 17.01 | 54.1% | 34.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 15,613 | 16.5 | 11.3 | 22.3 | 15.2 | 17.8 | 12.1 | 4.8 | 9.98 | 34.7% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 52,776 | 15613 | 18963 | 18200 | 24.2 | 145.0 | 1400.4 |
| ge_15pp | 21,889 | 5423 | 6762 | 9704 | 26.3 | 443.3 | 1380.4 |
| ge_25pp | 11,753 | 2648 | 2949 | 6156 | 32.6 | 586.3 | 1380.4 |
| lt_10pp | 22,785 | 7820 | 8968 | 5997 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261025T054928Z-e5fe0fe6`: 873 priced rows, quote age at build {'median': 14.7, 'max': 14.7}, freshness {'AGING': 873}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 25 | 0.0 | 0.0 | 24.0 | 8.0 | 36.0 | 32.0 | 0.0 | 20.47 | 68.0% | 32.0% |
| EXTERNAL_LONE_OUTLIER | 16 | 75.0 | 25.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,933 | 19.1 | 11.2 | 24.8 | 19.0 | 18.1 | 7.1 | 0.7 | 8.87 | 25.9% | 7.7% |
| KALSHI_LONE_OUTLIER | 18 | 5.6 | 5.6 | 72.2 | 5.6 | 5.6 | 5.6 | 0.0 | 6.16 | 11.1% | 5.6% |
| MARKETS_AGREE | 601 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,289 | 0.0 | 2.4 | 35.9 | 26.1 | 24.4 | 10.6 | 0.7 | 11.99 | 35.6% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 30,631 | 4882 (15.9%) | 26.4% | 0.9% | {"EXTERNAL_STALE": 2933, "AGREES_WITH_KALSHI": 1289, "ALL_AGREE": 601, "SUPPORTS_MODEL_DIRECTION": 24, "AGREES_WITH_MODEL": 18, "EXTERNAL_OUTLIER": 16, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,667 | 1237 (9.0%) | 37.1% | 1.5% | {"EXTERNAL_STALE": 759, "AGREES_WITH_KALSHI": 459, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,643 | 381 (5.0%) | 38.1% | 2.4% | {"EXTERNAL_STALE": 227, "AGREES_WITH_KALSHI": 145, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,713 | 358 (9.6%) | 38.6% | 2.5% | {"EXTERNAL_STALE": 211, "AGREES_WITH_KALSHI": 138, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,196 | 2750 (22.6%) | 18.0% | 0.7% | {"EXTERNAL_STALE": 1618, "ALL_AGREE": 601, "AGREES_WITH_KALSHI": 494, "EXTERNAL_OUTLIER": 16, "AGREES_WITH_MODEL": 15, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,840 | 10.3 | 7.5 | 19.5 | 14.4 | 22.2 | 16.0 | 10.1 | 14.13 | 48.3% | 26.1% |
| 4-10x | 3,979 | 11.0 | 8.2 | 19.1 | 15.4 | 21.4 | 14.8 | 10.2 | 13.76 | 46.4% | 25.0% |
| <2x | 15,561 | 15.0 | 9.7 | 19.0 | 16.5 | 17.5 | 13.1 | 9.2 | 11.86 | 39.8% | 22.3% |
| >=10x | 5,251 | 10.8 | 6.2 | 15.2 | 14.3 | 21.9 | 19.6 | 12.0 | 16.41 | 53.5% | 31.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,843 | 12.5 | 8.6 | 19.3 | 16.0 | 19.0 | 13.8 | 10.8 | 12.96 | 43.6% | 24.6% |
| 300-1000 | 6,493 | 11.6 | 8.6 | 17.3 | 15.3 | 20.6 | 16.3 | 10.3 | 13.94 | 47.1% | 26.6% |
| <300 | 9,993 | 8.6 | 5.6 | 15.5 | 14.7 | 23.1 | 20.1 | 12.4 | 17.01 | 55.6% | 32.5% |
| >=3000 | 6,302 | 21.3 | 12.9 | 23.3 | 16.5 | 14.1 | 7.1 | 4.7 | 7.96 | 25.9% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 871 | 0.5506 | 0.4121 | 0.5017 | +0.049 | -0.090 | -0.0043 ± 0.0052 |
| ratio 4-10x | 594 | 0.5888 | 0.4424 | 0.4949 | +0.094 | -0.053 | 0.0117 ± 0.0066 |
| ratio <2x | 2155 | 0.5385 | 0.4155 | 0.4459 | +0.093 | -0.030 | 0.0125 ± 0.0031 |
| ratio >=10x | 796 | 0.5717 | 0.3962 | 0.4611 | +0.111 | -0.065 | 0.0076 ± 0.0065 |
| thinner_sample 1000-3000 | 1198 | 0.5432 | 0.4161 | 0.4474 | +0.096 | -0.031 | 0.0101 ± 0.0041 |
| thinner_sample 300-1000 | 999 | 0.5675 | 0.4235 | 0.4935 | +0.074 | -0.070 | 0.0004 ± 0.0051 |
| thinner_sample <300 | 1483 | 0.5616 | 0.3949 | 0.4626 | +0.099 | -0.068 | 0.0097 ± 0.0046 |
| thinner_sample >=3000 | 736 | 0.536 | 0.4419 | 0.4674 | +0.069 | -0.025 | 0.0126 ± 0.0043 |
| data_status ADEQUATE | 1285 | 0.5385 | 0.4344 | 0.4521 | +0.086 | -0.018 | 0.0119 ± 0.0034 |
| data_status LIMITED | 1008 | 0.552 | 0.4174 | 0.4821 | +0.070 | -0.065 | 0.0038 ± 0.0047 |
| data_status POOR | 2123 | 0.5636 | 0.402 | 0.4673 | +0.096 | -0.065 | 0.008 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 645 | 0.2022 | 0.2032 | -0.0009 ± 0.0006 | 0.5855 | 0.5875 | 0.5029 | 0.4881 | 0.524 | -0.070 ± 0.0187 | -0.01 (5) |
| 3-5 | 410 | 0.205 | 0.2044 | +0.0006 ± 0.0018 | 0.5934 | 0.5905 | 0.503 | 0.4629 | 0.4732 | -0.102 ± 0.023 | 0.02 (1) |
| 5-10 | 914 | 0.2033 | 0.2025 | +0.0008 ± 0.0022 | 0.5934 | 0.5885 | 0.5116 | 0.4376 | 0.465 | -0.093 ± 0.0155 | -0.0167 (6) |
| 10-15 | 762 | 0.215 | 0.2051 | +0.0099 ± 0.0041 | 0.6206 | 0.592 | 0.5308 | 0.4066 | 0.4278 | -0.105 ± 0.0164 | -0.048 (5) |
| 15-25 | 998 | 0.2249 | 0.2124 | +0.0125 ± 0.0057 | 0.6445 | 0.6084 | 0.5786 | 0.3829 | 0.4489 | -0.095 ± 0.0145 | -0.0033 (9) |
| 25-40 | 572 | 0.2228 | 0.2103 | +0.0124 ± 0.0114 | 0.6352 | 0.6041 | 0.6604 | 0.3503 | 0.4825 | -0.072 ± 0.0176 | -0.01 (1) |
| 40+ | 115 | 0.2766 | 0.2018 | +0.0748 ± 0.0362 | 0.7584 | 0.5899 | 0.7572 | 0.3096 | 0.4522 | -0.071 ± 0.0357 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3326 | 0.1858 | 0.1868 | -0.0010 ± 0.0003 | 0.5474 | 0.5485 | 0.4929 | 0.4779 | 0.5123 | -0.021 ± 0.0076 | -0.0129 (17) |
| 3-5 | 2198 | 0.1996 | 0.1984 | +0.0013 ± 0.0008 | 0.5803 | 0.5749 | 0.4858 | 0.4458 | 0.449 | -0.053 ± 0.0097 | 0.0 (2) |
| 5-10 | 4774 | 0.1983 | 0.195 | +0.0033 ± 0.001 | 0.5806 | 0.5694 | 0.4823 | 0.4085 | 0.4223 | -0.047 ± 0.0065 | -0.0119 (21) |
| 10-15 | 4049 | 0.1982 | 0.1802 | +0.0179 ± 0.0017 | 0.582 | 0.5316 | 0.4876 | 0.3632 | 0.3529 | -0.073 ± 0.0067 | -0.0281 (16) |
| 15-25 | 5070 | 0.2092 | 0.1695 | +0.0396 ± 0.0023 | 0.6121 | 0.5016 | 0.5063 | 0.31 | 0.3083 | -0.075 ± 0.0057 | -0.0025 (44) |
| 25-40 | 3998 | 0.2225 | 0.1289 | +0.0936 ± 0.0036 | 0.639 | 0.3946 | 0.5324 | 0.2191 | 0.2301 | -0.059 ± 0.0055 | -0.01 (1) |
| 40+ | 2605 | 0.3802 | 0.0457 | +0.3345 ± 0.0047 | 0.9904 | 0.1752 | 0.6331 | 0.1066 | 0.0649 | -0.077 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 507 | 0.2084 | 0.2092 | -0.0009 ± 0.0007 | 0.5992 | 0.6011 | 0.507 | 0.4918 | 0.5207 | -0.098 ± 0.0219 | -0.01 (3) |
| 3-5 | 367 | 0.2259 | 0.223 | +0.0029 ± 0.002 | 0.6384 | 0.6325 | 0.516 | 0.4761 | 0.455 | -0.132 ± 0.0263 | 0.02 (1) |
| 5-10 | 796 | 0.2064 | 0.2063 | +0.0001 ± 0.0024 | 0.5993 | 0.598 | 0.5463 | 0.4714 | 0.5113 | -0.079 ± 0.0166 | -0.01 (4) |
| 10-15 | 730 | 0.2177 | 0.2097 | +0.0079 ± 0.0042 | 0.6249 | 0.6051 | 0.5647 | 0.4404 | 0.4726 | -0.112 ± 0.0177 | -0.04 (5) |
| 15-25 | 1023 | 0.2305 | 0.2106 | +0.0199 ± 0.0056 | 0.6541 | 0.604 | 0.588 | 0.3922 | 0.4438 | -0.102 ± 0.0146 | -0.0133 (9) |
| 25-40 | 717 | 0.2618 | 0.1977 | +0.0641 ± 0.0104 | 0.7305 | 0.5759 | 0.6539 | 0.3383 | 0.3961 | -0.114 ± 0.0163 | -0.0075 (4) |
| 40+ | 276 | 0.3548 | 0.1732 | +0.1816 ± 0.0247 | 0.9757 | 0.5174 | 0.7339 | 0.2501 | 0.3188 | -0.068 ± 0.024 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2833 | 0.1952 | 0.1955 | -0.0003 ± 0.0003 | 0.5674 | 0.568 | 0.5112 | 0.4962 | 0.5125 | -0.042 ± 0.0086 | -0.0133 (15) |
| 3-5 | 1896 | 0.2005 | 0.1996 | +0.0009 ± 0.0008 | 0.5793 | 0.5768 | 0.5149 | 0.475 | 0.4831 | -0.046 ± 0.0105 | 0.02 (1) |
| 5-10 | 4212 | 0.1964 | 0.1944 | +0.0020 ± 0.001 | 0.5777 | 0.5684 | 0.5102 | 0.4362 | 0.4627 | -0.034 ± 0.0069 | -0.0117 (6) |
| 10-15 | 3670 | 0.2022 | 0.1898 | +0.0124 ± 0.0018 | 0.5912 | 0.5528 | 0.5131 | 0.3892 | 0.4019 | -0.057 ± 0.0073 | -0.0189 (18) |
| 15-25 | 5044 | 0.2162 | 0.1781 | +0.0382 ± 0.0023 | 0.628 | 0.5239 | 0.5255 | 0.3295 | 0.3343 | -0.069 ± 0.006 | -0.0086 (42) |
| 25-40 | 4654 | 0.2513 | 0.1367 | +0.1146 ± 0.0034 | 0.7069 | 0.4199 | 0.5577 | 0.2405 | 0.2211 | -0.085 ± 0.0054 | -0.0044 (18) |
| 40+ | 3711 | 0.3932 | 0.0609 | +0.3322 ± 0.0046 | 1.0348 | 0.2174 | 0.6509 | 0.1192 | 0.0857 | -0.071 ± 0.004 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 616 | 0.1998 | 0.2019 | -0.0021 ± 0.0006 | 0.5805 | 0.5857 | 0.502 | 0.4867 | 0.5471 | -0.034 ± 0.0188 | -0.0137 (8) |
| 3-5 | 441 | 0.2039 | 0.2023 | +0.0016 ± 0.0017 | 0.5914 | 0.5859 | 0.5055 | 0.4658 | 0.4671 | -0.116 ± 0.0223 | 0.0067 (3) |
| 5-10 | 932 | 0.2024 | 0.1987 | +0.0037 ± 0.0022 | 0.5914 | 0.579 | 0.5083 | 0.4343 | 0.4442 | -0.106 ± 0.015 | -0.0071 (7) |
| 10-15 | 765 | 0.2094 | 0.2057 | +0.0037 ± 0.0041 | 0.608 | 0.5937 | 0.5404 | 0.4168 | 0.4654 | -0.084 ± 0.0163 | -0.0317 (6) |
| 15-25 | 946 | 0.2305 | 0.2127 | +0.0178 ± 0.0058 | 0.6588 | 0.6085 | 0.5898 | 0.3953 | 0.4461 | -0.108 ± 0.0149 | -0.03 (1) |
| 25-40 | 595 | 0.2146 | 0.2181 | -0.0035 ± 0.0112 | 0.619 | 0.6222 | 0.6708 | 0.3596 | 0.5176 | -0.056 ± 0.0173 | 0.015 (2) |
| 40+ | 121 | 0.2922 | 0.2133 | +0.0789 ± 0.0366 | 0.8066 | 0.6151 | 0.7677 | 0.3179 | 0.4628 | -0.070 ± 0.0386 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3252 | 0.1853 | 0.1858 | -0.0005 ± 0.0003 | 0.5453 | 0.5461 | 0.4897 | 0.4745 | 0.4892 | -0.038 ± 0.0076 | -0.0163 (35) |
| 3-5 | 2213 | 0.1954 | 0.1934 | +0.0019 ± 0.0008 | 0.5733 | 0.567 | 0.4869 | 0.4473 | 0.4433 | -0.063 ± 0.0096 | -0.0094 (18) |
| 5-10 | 4826 | 0.1959 | 0.1901 | +0.0058 ± 0.0009 | 0.5757 | 0.5568 | 0.4837 | 0.4097 | 0.408 | -0.061 ± 0.0063 | -0.01 (31) |
| 10-15 | 3938 | 0.1923 | 0.177 | +0.0153 ± 0.0017 | 0.5684 | 0.5229 | 0.5001 | 0.3767 | 0.3761 | -0.065 ± 0.0067 | -0.015 (12) |
| 15-25 | 5254 | 0.2112 | 0.1725 | +0.0386 ± 0.0022 | 0.6168 | 0.5086 | 0.5158 | 0.3208 | 0.3196 | -0.072 ± 0.0057 | -0.03 (2) |
| 25-40 | 4010 | 0.2197 | 0.1328 | +0.0869 ± 0.0036 | 0.6339 | 0.403 | 0.538 | 0.2218 | 0.2441 | -0.050 ± 0.0055 | 0.01 (3) |
| 40+ | 2527 | 0.3952 | 0.0503 | +0.3449 ± 0.0051 | 1.0327 | 0.1874 | 0.6455 | 0.1132 | 0.0693 | -0.080 ± 0.0043 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1004 | 0.1952 | 0.1954 | -0.0002 ± 0.0005 | 0.5697 | 0.5698 | 0.5029 | 0.4878 | 0.496 | -0.056 ± 0.0141 | -0.0224 (49) |
| 3-5 | 700 | 0.193 | 0.1922 | +0.0008 ± 0.0013 | 0.5636 | 0.5605 | 0.4914 | 0.4515 | 0.4586 | -0.061 ± 0.017 | -0.0194 (34) |
| 5-10 | 1456 | 0.2025 | 0.1964 | +0.0061 ± 0.0017 | 0.5944 | 0.5755 | 0.4967 | 0.4233 | 0.4196 | -0.075 ± 0.0118 | -0.005 (78) |
| 10-15 | 972 | 0.211 | 0.1989 | +0.0121 ± 0.0036 | 0.6114 | 0.58 | 0.5232 | 0.4001 | 0.4105 | -0.071 ± 0.0146 | 0.0014 (64) |
| 15-25 | 1305 | 0.2312 | 0.2106 | +0.0206 ± 0.005 | 0.6608 | 0.6059 | 0.5786 | 0.3837 | 0.4291 | -0.073 ± 0.0127 | -0.0214 (59) |
| 25-40 | 789 | 0.2481 | 0.2074 | +0.0407 ± 0.01 | 0.7046 | 0.5962 | 0.6742 | 0.3614 | 0.4525 | -0.087 ± 0.0152 | -0.0219 (26) |
| 40+ | 262 | 0.3523 | 0.1994 | +0.1529 ± 0.0272 | 1.0179 | 0.5813 | 0.8088 | 0.3267 | 0.4275 | -0.095 ± 0.025 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3288 | 0.1833 | 0.1835 | -0.0002 ± 0.0003 | 0.5398 | 0.5394 | 0.5048 | 0.4894 | 0.5006 | -0.038 ± 0.0075 | -0.0157 (88) |
| 3-5 | 2280 | 0.1954 | 0.1935 | +0.0019 ± 0.0007 | 0.5699 | 0.5656 | 0.4973 | 0.4576 | 0.4535 | -0.054 ± 0.0093 | -0.0209 (69) |
| 5-10 | 4536 | 0.1975 | 0.1892 | +0.0083 ± 0.001 | 0.5809 | 0.5564 | 0.4915 | 0.418 | 0.4012 | -0.071 ± 0.0065 | -0.0082 (132) |
| 10-15 | 3182 | 0.2073 | 0.1909 | +0.0164 ± 0.0019 | 0.6034 | 0.5605 | 0.5302 | 0.4071 | 0.4013 | -0.068 ± 0.0078 | -0.0053 (105) |
| 15-25 | 3958 | 0.2298 | 0.2 | +0.0298 ± 0.0028 | 0.6631 | 0.5794 | 0.5702 | 0.3748 | 0.3974 | -0.065 ± 0.0071 | -0.0253 (107) |
| 25-40 | 2723 | 0.2593 | 0.1843 | +0.0750 ± 0.0052 | 0.7347 | 0.5378 | 0.6332 | 0.3191 | 0.3592 | -0.078 ± 0.008 | -0.0229 (51) |
| 40+ | 1208 | 0.3788 | 0.1449 | +0.2339 ± 0.0115 | 1.0731 | 0.4364 | 0.7301 | 0.2263 | 0.2591 | -0.071 ± 0.0103 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4416 | 1.032 ± 0.042 | 1.117 | 0.1685 | 0.1633 | 0.2146 | 0.2065 |
| gen2 | 4416 | 0.836 ± 0.039 | 1.087 | 0.168 | 0.164 | 0.234 | 0.2061 |
| gen1_elo | 4416 | 1.004 ± 0.041 | 1.112 | 0.1754 | 0.1634 | 0.2136 | 0.2067 |
| gen1_sr | 4416 | 1.02 ± 0.051 | 1.161 | 0.1292 | 0.1659 | 0.2301 | 0.2057 |
| gen1_ledger | 6488 | 0.858 ± 0.03 | 1.068 | 0.1835 | 0.1777 | 0.219 | 0.2005 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 21,889)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,034 | 23.0% |
| STALE_QUOTE | market_freshness | 4,757 | 21.7% |
| BOOK_QUALITY | execution | 4,124 | 18.8% |
| POOR_DATA | data | 2,453 | 11.2% |
| LIMITED_DATA | data | 1,345 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,188 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,039 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 920 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 649 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 379 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 23.0%, market_freshness 21.7%, execution 18.8%, data 17.3%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.0%, LOW_DATA_QUALITY 70.7%, THIN_PLAYER_HISTORY 59.6%, STALE_PLAYER_DATA 49.4%, STALE_KALSHI_QUOTE 44.3%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.0%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.5%, LEVEL_TRANSFER_RISK 11.0%, EVENT_MAPPING_RISK 8.1%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.6%, POST_SETTLEMENT_OBSERVATION 23.0%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,753)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,061 | 34.5% |
| STALE_QUOTE | market_freshness | 2,203 | 18.7% |
| BOOK_QUALITY | execution | 2,152 | 18.3% |
| POOR_DATA | data | 1,012 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 639 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 518 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 413 | 3.5% |
| LIMITED_DATA | data | 408 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 259 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 87 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.5%, market_freshness 18.7%, execution 18.3%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.1%, THIN_PLAYER_HISTORY 61.7%, STALE_KALSHI_QUOTE 52.4%, STALE_PLAYER_DATA 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.8%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.2%, PLAYER_IDENTITY_RISK 19.8%, MODEL_HIGH_UNCERTAINTY 18.4%, EVENT_MAPPING_RISK 9.7%, LEVEL_TRANSFER_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.0%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.6%, POST_SETTLEMENT_OBSERVATION 34.5%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9132, "IDENTITY_AMBIGUOUS": 2621}; ticker orientation: {"VERIFIED": 11753}.

Checks: discipline:AMBIGUOUS 797, discipline:PASS 10956, identity_confidence:AMBIGUOUS 2327, identity_confidence:PASS 9426, level_mapping:NA 809, level_mapping:PASS 10944, market_pair:AMBIGUOUS 421, market_pair:NA 295, market_pair:PASS 11037, model_complement:NA 262, model_complement:PASS 11491, namesake:AMBIGUOUS 6, namesake:PASS 11747, physical_match_id:NA 4110, physical_match_id:PASS 7643, player_ids:PASS 11753, same_pair_other_event:PASS 11753, ticker_orientation:PASS 11753

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,421 | 4.5% | 4.0% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 45, "data": 35, "execution": 23, "model_calibration": 17, "market_freshness/coverage": 15, "coverage": 13} | 5.92 | 0.2224 / 0.2181 (519) | 18.9% | 3.5% | 3.3% | 2.8% |
| CHALLENGER | 8,061 | 17.3% | 7.0% | 11.8% | {"coverage": 786, "market_freshness/coverage": 168, "market_freshness": 153, "data": 141, "model_calibration_or_unknown": 66, "execution": 33, "model_calibration": 30, "mapping": 15, "possible_market_error": 1} | 7.53 | 0.2198 / 0.2091 (1906) | 34.6% | 17.7% | 4.0% | 22.4% |
| DOUBLES | 1,698 | 46.9% | 46.6% | 6.8% | {"execution": 426, "mapping": 203, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.62 | 0.3096 / 0.2358 (432) | 13.8% | 0.0% | 100.0% | 7.0% |
| ITF_MEN | 14,679 | 25.4% | 17.7% | 31.8% | {"coverage": 1395, "execution": 710, "market_freshness": 638, "data": 491, "market_freshness/coverage": 324, "mapping": 174, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.91 | 0.2159 / 0.1976 (3286) | 37.5% | 69.9% | 19.8% | 22.2% |
| ITF_WOMEN | 19,283 | 27.3% | 19.9% | 44.8% | {"coverage": 1835, "market_freshness": 1154, "execution": 916, "data": 718, "market_freshness/coverage": 441, "mapping": 120, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.89 | 0.2039 / 0.1949 (3726) | 40.0% | 56.0% | 10.0% | 22.2% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,065 | 5.6% | 5.0% | 1.5% | {"market_freshness": 59, "model_calibration_or_unknown": 36, "execution": 26, "model_calibration": 16, "coverage": 12, "data": 11, "market_freshness/coverage": 10, "mapping": 1} | 7.64 | 0.2347 / 0.2299 (505) | 24.8% | 1.4% | 1.7% | 3.4% |
| WTA125 | 1,414 | 12.7% | 10.1% | 1.5% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 24, "execution": 13, "coverage": 12, "model_calibration": 11, "mapping": 4} | 9.33 | 0.219 / 0.2065 (488) | 22.9% | 8.3% | 5.9% | 9.7% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
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
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
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
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 50 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9683, "by_level_share_of_ge_25pp": {"ATP": 0.0171, "CHALLENGER": 0.1185, "DOUBLES": 0.0678, "ITF_MEN": 0.3179, "ITF_WOMEN": 0.4479, "OTHER": 0.001, "WTA": 0.0145, "WTA125": 0.0152}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5238, "share_primary_cause_market_settled_or_in_play": 0.435, "share_primary_cause_stale_quote_only": 0.1874}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11753, "identity_ambiguous_share": 0.223, "ticker_orientation": {"VERIFIED": 11753}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7643, "with_external": 381, "coverage": 0.0498, "external_status": {"EXTERNAL_STALE": 227, "AGREES_WITH_KALSHI": 145, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 227, "MODEL_LONE_OUTLIER": 145, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3806, "share_external_supports_model": 0.0236}, "pregame_clean_ge_25pp": {"n": 3713, "with_external": 358, "coverage": 0.0964, "external_status": {"EXTERNAL_STALE": 211, "AGREES_WITH_KALSHI": 138, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 211, "MODEL_LONE_OUTLIER": 138, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3855, "share_external_supports_model": 0.0251}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 494.0, "median_sample_ratio": 2.42, "median_min_matches": 21.0, "median_max_days_since_last": 226.0, "share_severe_asymmetry": 0.2146, "data_status": {"POOR": 6527, "LIMITED": 3073, "ADEQUATE": 2153}, "comparison_lt_10pp": {"median_thinner_serve_points": 1743.0, "median_sample_ratio": 1.69, "median_min_matches": 96.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 871, "model_minus_observed": 0.0489, "kalshi_minus_observed": -0.0896, "brier_diff_model_minus_kalshi": -0.0043}, "4-10x": {"n": 594, "model_minus_observed": 0.0939, "kalshi_minus_observed": -0.0526, "brier_diff_model_minus_kalshi": 0.0117}, "<2x": {"n": 2155, "model_minus_observed": 0.0926, "kalshi_minus_observed": -0.0304, "brier_diff_model_minus_kalshi": 0.0125}, ">=10x": {"n": 796, "model_minus_observed": 0.1106, "kalshi_minus_observed": -0.0648, "brier_diff_model_minus_kalshi": 0.0076}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4416, "model": {"intercept": -0.536, "slope": 0.836, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.212, "slope": 1.087, "slope_se": 0.044}, "mean_extremity_model": 0.168, "mean_extremity_kalshi": 0.164, "model_brier": 0.234, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0278, "brier_diff_se": 0.0029, "model_logloss": 0.6643, "kalshi_logloss": 0.5952}, "fair_v1": {"n": 4416, "model": {"intercept": -0.421, "slope": 1.032, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.285, "slope": 1.117, "slope_se": 0.044}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1633, "model_brier": 0.2146, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.0023, "model_logloss": 0.6182, "kalshi_logloss": 0.5957}, "gen1_elo": {"n": 4416, "model": {"intercept": -0.397, "slope": 1.004, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.305, "slope": 1.112, "slope_se": 0.044}, "mean_extremity_model": 0.1754, "mean_extremity_kalshi": 0.1634, "model_brier": 0.2136, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.0068, "brier_diff_se": 0.0024, "model_logloss": 0.6168, "kalshi_logloss": 0.5963}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2495, "share_ge_15": 0.4462, "median_abs_gap": 13.16, "n": 30631}, "gen1_elo": {"share_ge_25": 0.2465, "share_ge_15": 0.4453, "median_abs_gap": 13.01, "n": 30631}, "gen1_sr": {"share_ge_25": 0.317, "share_ge_15": 0.525, "median_abs_gap": 16.01, "n": 30631}, "gen2": {"share_ge_25": 0.3204, "share_ge_15": 0.5148, "median_abs_gap": 15.62, "n": 30631}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1562, "share_ge_15": 0.3618, "median_abs_gap": 10.95, "n": 23764}, "gen1_elo": {"share_ge_25": 0.1567, "share_ge_15": 0.3596, "median_abs_gap": 10.74, "n": 23761}, "gen1_sr": {"share_ge_25": 0.2229, "share_ge_15": 0.4468, "median_abs_gap": 13.12, "n": 23765}, "gen2": {"share_ge_25": 0.2392, "share_ge_15": 0.4461, "median_abs_gap": 13.1, "n": 23766}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.92, "share_ge_25_all": 0.0455, "share_ge_25_pregame_clean": 0.0403}, "WTA": {"median_abs_gap_pregame_clean": 7.64, "share_ge_25_all": 0.0558, "share_ge_25_pregame_clean": 0.0503}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.234, "share_within_10pp_all": 0.4317, "share_within_10pp_pregame_clean": 0.4848, "corr_model_vs_mid_pregame_clean": 0.8428}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 645, "model_brier": 0.2022, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 762, "model_brier": 0.215, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0099}, "15-25": {"n_settled": 998, "model_brier": 0.2249, "kalshi_brier": 0.2124, "brier_diff_model_minus_kalshi": 0.0125}, "25-40": {"n_settled": 572, "model_brier": 0.2228, "kalshi_brier": 0.2103, "brier_diff_model_minus_kalshi": 0.0124}, "3-5": {"n_settled": 410, "model_brier": 0.205, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 115, "model_brier": 0.2766, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0748}, "5-10": {"n_settled": 914, "model_brier": 0.2033, "kalshi_brier": 0.2025, "brier_diff_model_minus_kalshi": 0.0008}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.536, "slope": 0.836, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.212, "slope": 1.087, "slope_se": 0.044}, "n": 4416}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.506, "slope": 0.858, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.152, "slope": 1.068, "slope_se": 0.034}, "n": 6488}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 432, "model_brier": 0.3096, "kalshi_brier": 0.2358, "brier_diff_model_minus_kalshi": 0.0738, "brier_diff_se": 0.0146, "corr_model_outcome": 0.0434, "corr_kalshi_outcome": 0.2537}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
