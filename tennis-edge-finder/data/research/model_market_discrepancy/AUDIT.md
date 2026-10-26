# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-26T11:39Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 55,803): 0-3 14.0%, 3-5 9.6%, 5-10 19.8%, 10-15 15.4%, 15-25 19.2%, 25-40 13.9%, 40+ 8.1%; median gap 11.99 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.1%, Challenger 11.9%, doubles 7.0%). Main tour: ATP 4.3% and WTA 5.5% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 12,274): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.9%, BOOK_QUALITY 18.9%, STALE_QUOTE 18.9%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.9%, execution 18.9%, market_freshness 18.9%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 12,274 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.4% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 476.0 points vs 1774.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.036, Gen-2 0.831, Gen-1 ledger 0.864 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 591 model 0.2216 vs Kalshi 0.2101; n 116 model 0.2743 vs Kalshi 0.202.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 245,495 model-market comparisons (396,635 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 82,677 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-26T11:25:04.415578+00:00'], shadow board 64,250 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-26T11:25:08.754694+00:00'], Model 4 31,708 rows, 20,793 settled tickers, 7,391 tickers with an external scan.
* By model: {"gen1_ledger": 56655, "gen1_elo": 32308, "fair_v1": 32308, "gen2": 32308, "gen1_sr": 32308, "model4_fundamental": 29826, "model4_conditioned": 29782}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 55,803 | 14.0 | 9.6 | 19.8 | 15.4 | 19.2 | 13.9 | 8.1 | 11.99 | 41.2% | 22.0% |
| MW fair_v1 | 32,308 | 12.9 | 8.7 | 18.5 | 15.6 | 19.7 | 14.9 | 9.7 | 13.07 | 44.3% | 24.6% |
| MW gen1_elo | 32,308 | 12.7 | 8.6 | 19.1 | 15.3 | 19.9 | 14.9 | 9.5 | 12.97 | 44.2% | 24.4% |
| MW gen1_ledger | 23,495 | 15.4 | 10.8 | 21.6 | 15.2 | 18.5 | 12.6 | 5.8 | 10.51 | 36.9% | 18.4% |
| MW gen1_sr | 32,308 | 10.2 | 7.1 | 17.0 | 13.6 | 20.7 | 18.6 | 12.7 | 15.91 | 52.1% | 31.4% |
| MW gen2 | 32,308 | 11.1 | 7.4 | 16.4 | 14.0 | 19.4 | 17.9 | 13.9 | 15.52 | 51.2% | 31.7% |
| all families model4_conditioned | 29,782 | 21.8 | 18.4 | 34.5 | 17.6 | 4.8 | 1.8 | 1.1 | 6.06 | 7.6% | 2.9% |
| all families model4_fundamental | 29,826 | 16.7 | 13.1 | 34.1 | 20.7 | 10.4 | 3.6 | 1.4 | 7.83 | 15.4% | 5.0% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.6%, >=15pp 41.2%, >=20pp 30.6%, >=25pp 22.0%, >=30pp 15.8%, >=40pp 8.1%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.35pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,996 | 27.2 | 14.8 | 26.5 | 14.8 | 11.8 | 4.3 | 0.7 | 6.07 | 16.7% | 4.9% |
| CHALLENGER | 5,130 | 15.8 | 10.0 | 20.2 | 15.6 | 15.6 | 12.2 | 10.5 | 11.09 | 38.4% | 22.8% |
| ITF_MEN | 8,642 | 10.0 | 7.2 | 16.7 | 14.6 | 21.6 | 17.6 | 12.3 | 15.51 | 51.5% | 29.9% |
| ITF_WOMEN | 12,608 | 9.5 | 7.0 | 15.8 | 15.2 | 22.4 | 18.3 | 11.8 | 15.77 | 52.5% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,136 | 16.9 | 13.6 | 25.6 | 20.2 | 17.0 | 6.0 | 0.6 | 8.34 | 23.6% | 6.7% |
| WTA125 | 790 | 14.3 | 7.6 | 21.4 | 22.1 | 20.0 | 12.7 | 1.9 | 11.31 | 34.6% | 14.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,996 | 24.1 | 15.1 | 25.8 | 17.4 | 12.3 | 4.3 | 0.9 | 6.56 | 17.5% | 5.2% |
| CHALLENGER | 5,130 | 15.0 | 8.9 | 18.1 | 14.5 | 18.2 | 14.1 | 11.3 | 12.68 | 43.5% | 25.4% |
| ITF_MEN | 8,642 | 8.0 | 5.9 | 14.4 | 13.0 | 19.6 | 21.2 | 17.9 | 18.82 | 58.7% | 39.1% |
| ITF_WOMEN | 12,608 | 8.1 | 5.6 | 13.7 | 12.9 | 20.7 | 21.1 | 17.7 | 19.2 | 59.6% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,136 | 14.3 | 10.5 | 22.5 | 16.0 | 22.4 | 13.2 | 1.2 | 10.84 | 36.8% | 14.3% |
| WTA125 | 790 | 7.5 | 6.2 | 16.3 | 18.2 | 24.6 | 18.5 | 8.7 | 15.84 | 51.8% | 27.2% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,996 | 23.1 | 12.3 | 24.5 | 16.3 | 15.9 | 6.6 | 1.2 | 7.54 | 23.8% | 7.8% |
| CHALLENGER | 5,130 | 14.3 | 9.3 | 21.1 | 15.7 | 16.1 | 12.8 | 10.7 | 11.43 | 39.7% | 23.5% |
| ITF_MEN | 8,642 | 9.6 | 7.3 | 16.8 | 13.8 | 22.2 | 17.9 | 12.5 | 16.01 | 52.6% | 30.4% |
| ITF_WOMEN | 12,608 | 9.3 | 6.6 | 16.3 | 15.9 | 22.7 | 18.2 | 10.9 | 15.58 | 51.9% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,136 | 23.9 | 17.0 | 30.8 | 15.3 | 9.6 | 2.7 | 0.9 | 6.04 | 13.1% | 3.6% |
| WTA125 | 790 | 22.4 | 12.0 | 26.6 | 16.6 | 16.1 | 6.0 | 0.4 | 7.99 | 22.4% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,805 | 24.8 | 19.6 | 29.9 | 13.1 | 9.4 | 3.0 | 0.3 | 5.66 | 12.7% | 3.3% |
| CHALLENGER | 3,560 | 21.1 | 14.3 | 26.7 | 14.9 | 14.7 | 6.5 | 1.7 | 7.43 | 22.9% | 8.2% |
| DOUBLES | 1,814 | 5.2 | 4.5 | 12.2 | 10.2 | 20.2 | 25.7 | 21.9 | 24.04 | 67.8% | 47.6% |
| ITF_MEN | 6,403 | 13.5 | 9.1 | 19.9 | 16.1 | 21.5 | 13.4 | 6.5 | 12.22 | 41.3% | 19.8% |
| ITF_WOMEN | 7,656 | 12.7 | 8.8 | 19.3 | 15.4 | 21.6 | 16.2 | 6.0 | 12.83 | 43.8% | 22.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,274 | 23.0 | 15.6 | 30.4 | 17.9 | 9.7 | 3.1 | 0.3 | 6.82 | 13.1% | 3.5% |
| WTA125 | 834 | 21.2 | 13.7 | 21.8 | 18.4 | 14.5 | 8.4 | 2.0 | 8.33 | 24.9% | 10.4% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,916 | 27.5 | 15.0 | 26.9 | 14.7 | 11.6 | 3.9 | 0.4 | 5.94 | 15.9% | 4.3% |
| CHALLENGER | 3,636 | 20.5 | 12.5 | 24.8 | 18.0 | 15.7 | 6.8 | 1.7 | 8.36 | 24.2% | 8.5% |
| ITF_MEN | 6,319 | 12.1 | 8.7 | 20.2 | 16.5 | 22.8 | 14.4 | 5.2 | 12.66 | 42.5% | 19.7% |
| ITF_WOMEN | 9,470 | 11.2 | 8.3 | 18.0 | 17.3 | 24.3 | 15.5 | 5.4 | 13.56 | 45.2% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,075 | 17.2 | 13.5 | 25.6 | 20.4 | 17.0 | 5.7 | 0.6 | 8.25 | 23.3% | 6.4% |
| WTA125 | 764 | 14.7 | 7.5 | 20.9 | 22.5 | 20.6 | 12.3 | 1.6 | 11.31 | 34.4% | 13.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,916 | 24.4 | 15.5 | 26.1 | 17.4 | 12.3 | 4.0 | 0.5 | 6.47 | 16.8% | 4.5% |
| CHALLENGER | 3,636 | 19.1 | 11.2 | 22.3 | 17.2 | 18.5 | 9.8 | 1.9 | 9.36 | 30.2% | 11.7% |
| ITF_MEN | 6,320 | 9.6 | 7.1 | 16.8 | 15.0 | 21.5 | 19.4 | 10.7 | 15.5 | 51.5% | 30.1% |
| ITF_WOMEN | 9,471 | 9.2 | 6.4 | 15.2 | 14.4 | 22.8 | 20.6 | 11.4 | 16.89 | 54.8% | 32.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,075 | 14.4 | 10.5 | 22.5 | 16.0 | 22.5 | 13.0 | 1.2 | 10.87 | 36.6% | 14.2% |
| WTA125 | 764 | 7.3 | 6.4 | 16.4 | 18.6 | 24.5 | 18.9 | 8.0 | 15.68 | 51.3% | 26.8% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,754 | 25.0 | 19.8 | 29.9 | 13.2 | 9.1 | 2.9 | 0.2 | 5.6 | 12.1% | 3.0% |
| CHALLENGER | 3,125 | 22.5 | 15.3 | 28.0 | 15.0 | 14.1 | 4.6 | 0.5 | 6.94 | 19.2% | 5.1% |
| DOUBLES | 1,694 | 5.2 | 4.6 | 12.5 | 10.3 | 20.0 | 25.7 | 21.7 | 23.9 | 67.4% | 47.3% |
| ITF_MEN | 5,377 | 14.6 | 9.8 | 21.6 | 16.9 | 21.4 | 11.7 | 4.0 | 11.27 | 37.1% | 15.7% |
| ITF_WOMEN | 6,396 | 13.5 | 9.4 | 20.6 | 16.2 | 21.8 | 15.0 | 3.5 | 11.84 | 40.3% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,221 | 23.4 | 16.1 | 30.4 | 17.9 | 9.7 | 2.5 | 0.1 | 6.71 | 12.2% | 2.5% |
| WTA125 | 723 | 23.0 | 14.9 | 23.1 | 19.6 | 13.0 | 5.8 | 0.6 | 7.6 | 19.4% | 6.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,814 | 5.2 | 4.5 | 12.2 | 10.2 | 20.2 | 25.7 | 21.9 | 24.04 | 67.8% | 47.6% |
| singles | 21,681 | 16.3 | 11.3 | 22.4 | 15.6 | 18.4 | 11.5 | 4.5 | 9.98 | 34.4% | 16.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,060 | 12.8 | 9.1 | 19.5 | 15.9 | 19.0 | 14.1 | 9.6 | 12.65 | 42.7% | 23.7% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 20,311 | 13.4 | 8.8 | 18.5 | 15.2 | 19.8 | 14.8 | 9.4 | 13.0 | 44.0% | 24.3% |
| UNKNOWN | 4,688 | 10.9 | 7.5 | 17.0 | 16.7 | 20.5 | 16.3 | 11.2 | 14.12 | 48.0% | 27.5% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,356 | 19.6 | 12.2 | 21.9 | 16.4 | 14.8 | 9.1 | 6.0 | 8.88 | 30.0% | 15.1% |
| B | 3,989 | 12.2 | 8.8 | 19.4 | 16.4 | 19.6 | 12.8 | 10.8 | 12.67 | 43.1% | 23.5% |
| C | 4,480 | 11.8 | 9.0 | 19.4 | 15.7 | 19.2 | 14.5 | 10.3 | 13.0 | 44.1% | 24.8% |
| D | 4,916 | 12.1 | 7.8 | 17.4 | 15.4 | 21.7 | 15.6 | 9.9 | 13.98 | 47.2% | 25.5% |
| F | 9,567 | 7.5 | 5.6 | 15.0 | 14.5 | 23.8 | 21.2 | 12.4 | 17.78 | 57.5% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,736 | 23.3 | 16.1 | 28.8 | 15.2 | 11.3 | 4.0 | 1.3 | 6.58 | 16.6% | 5.3% |
| B | 3,164 | 16.2 | 10.4 | 23.1 | 16.3 | 19.9 | 10.4 | 3.7 | 10.05 | 33.9% | 14.1% |
| C | 4,614 | 10.9 | 7.3 | 18.6 | 14.4 | 21.1 | 16.6 | 11.1 | 14.38 | 48.8% | 27.7% |
| D | 3,207 | 14.2 | 9.7 | 20.1 | 15.2 | 20.9 | 14.0 | 5.8 | 11.86 | 40.8% | 19.8% |
| F | 5,774 | 10.2 | 8.3 | 15.7 | 15.1 | 22.8 | 20.0 | 8.0 | 15.4 | 50.8% | 28.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,651 | 17.8 | 11.0 | 21.2 | 16.1 | 15.4 | 10.0 | 8.5 | 10.01 | 34.0% | 18.6% |
| LIMITED | 6,830 | 13.5 | 10.2 | 20.0 | 16.2 | 19.3 | 13.2 | 7.5 | 11.8 | 40.0% | 20.7% |
| POOR | 14,827 | 9.0 | 6.4 | 15.9 | 14.9 | 23.0 | 19.2 | 11.6 | 16.25 | 53.7% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,818 | 24.8 | 18.7 | 33.5 | 14.4 | 6.0 | 2.3 | 0.3 | 5.68 | 8.7% | 2.6% |
| GAME_SPREAD | 5,369 | 22.4 | 15.4 | 33.3 | 16.9 | 9.1 | 2.5 | 0.3 | 6.69 | 11.9% | 2.8% |
| MATCH_WINNER | 23,495 | 15.4 | 10.8 | 21.6 | 15.2 | 18.5 | 12.6 | 5.8 | 10.51 | 36.9% | 18.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,237 | 27.9 | 16.4 | 31.1 | 12.7 | 9.4 | 2.3 | 0.3 | 5.69 | 11.9% | 2.6% |
| TOTAL_GAMES | 8,712 | 9.0 | 10.1 | 36.4 | 27.4 | 10.5 | 3.9 | 2.8 | 9.36 | 17.1% | 6.7% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,661 | 24.5 | 31.2 | 32.9 | 6.7 | 3.8 | 0.8 | 0.2 | 4.66 | 4.8% | 1.0% |
| GAME_SPREAD | 6,973 | 46.2 | 16.6 | 26.2 | 7.7 | 1.8 | 1.1 | 0.4 | 3.38 | 3.3% | 1.5% |
| TOTAL_GAMES | 12,148 | 5.4 | 8.2 | 40.8 | 33.0 | 7.3 | 3.0 | 2.3 | 9.52 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,672 | 23.6 | 16.9 | 35.3 | 14.1 | 7.2 | 2.5 | 0.4 | 6.03 | 10.1% | 2.9% |
| GAME_SPREAD | 6,976 | 19.6 | 13.1 | 28.2 | 21.1 | 12.7 | 4.2 | 1.0 | 7.93 | 17.9% | 5.2% |
| TOTAL_GAMES | 12,178 | 8.9 | 9.8 | 36.4 | 26.3 | 11.9 | 4.3 | 2.5 | 9.41 | 18.6% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 32,308 | 44.3% | 24.6% | 13.07 | 36.0% | 15.5% | 10.88 |
| gen1_elo | 32,308 | 44.2% | 24.4% | 12.97 | 35.8% | 15.5% | 10.7 |
| gen1_sr | 32,308 | 52.1% | 31.4% | 15.91 | 44.3% | 22.1% | 13.01 |
| gen2 | 32,308 | 51.2% | 31.7% | 15.52 | 44.4% | 23.8% | 13.02 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 16,258 | 15.6 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.2 | 10.71 | 35.2% | 15.1% |
| STALE | 16,050 | 10.2 | 6.9 | 15.7 | 13.8 | 19.3 | 18.0 | 16.2 | 16.59 | 53.5% | 34.2% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 16,963 | 16.4 | 11.3 | 22.4 | 15.3 | 17.8 | 12.1 | 4.8 | 9.99 | 34.7% | 16.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 55,803 | 16963 | 19730 | 19110 | 24.1 | 132.9 | 1400.4 |
| ge_15pp | 22,997 | 5881 | 7015 | 10101 | 26.3 | 435.4 | 1380.4 |
| ge_25pp | 12,274 | 2867 | 3046 | 6361 | 31.6 | 578.1 | 1380.4 |
| lt_10pp | 24,211 | 8484 | 9346 | 6381 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261026T113906Z-e5491a58`: 879 priced rows, quote age at build {'median': 14.5, 'max': 14.5}, freshness {'AGING': 879}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 28 | 0.0 | 0.0 | 21.4 | 10.7 | 39.3 | 28.6 | 0.0 | 20.48 | 67.9% | 28.6% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,127 | 19.4 | 11.2 | 24.9 | 18.9 | 18.0 | 6.9 | 0.6 | 8.8 | 25.6% | 7.6% |
| KALSHI_LONE_OUTLIER | 21 | 4.8 | 4.8 | 76.2 | 4.8 | 4.8 | 4.8 | 0.0 | 6.11 | 9.5% | 4.8% |
| MARKETS_AGREE | 641 | 65.2 | 34.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,374 | 0.0 | 2.5 | 34.9 | 26.7 | 25.0 | 10.2 | 0.7 | 12.14 | 35.8% | 10.8% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 32,308 | 5209 (16.1%) | 26.4% | 0.9% | {"EXTERNAL_STALE": 3127, "AGREES_WITH_KALSHI": 1374, "ALL_AGREE": 641, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 21, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 14,317 | 1313 (9.2%) | 37.5% | 1.6% | {"EXTERNAL_STALE": 800, "AGREES_WITH_KALSHI": 492, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,945 | 395 (5.0%) | 37.7% | 2.3% | {"EXTERNAL_STALE": 237, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,897 | 372 (9.6%) | 38.2% | 2.4% | {"EXTERNAL_STALE": 221, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,958 | 2935 (22.7%) | 17.5% | 0.8% | {"EXTERNAL_STALE": 1737, "ALL_AGREE": 641, "AGREES_WITH_KALSHI": 515, "EXTERNAL_OUTLIER": 18, "AGREES_WITH_MODEL": 18, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,172 | 10.1 | 7.6 | 19.4 | 14.7 | 22.4 | 15.9 | 9.8 | 14.09 | 48.2% | 25.7% |
| 4-10x | 4,164 | 11.1 | 8.5 | 18.6 | 15.4 | 21.9 | 14.7 | 9.7 | 13.75 | 46.4% | 24.4% |
| <2x | 16,523 | 15.1 | 10.0 | 19.3 | 16.4 | 17.4 | 12.9 | 8.8 | 11.64 | 39.2% | 21.8% |
| >=10x | 5,449 | 10.6 | 6.2 | 15.2 | 14.2 | 21.9 | 19.8 | 12.1 | 16.49 | 53.8% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,248 | 12.7 | 8.6 | 19.2 | 16.2 | 19.0 | 13.8 | 10.5 | 12.85 | 43.3% | 24.3% |
| 300-1000 | 6,763 | 11.7 | 8.7 | 17.4 | 15.4 | 20.8 | 16.1 | 9.9 | 13.81 | 46.8% | 26.0% |
| <300 | 10,499 | 8.4 | 5.7 | 15.3 | 14.7 | 23.3 | 20.2 | 12.3 | 17.02 | 55.8% | 32.5% |
| >=3000 | 6,798 | 21.2 | 13.4 | 23.7 | 16.4 | 14.0 | 6.9 | 4.5 | 7.75 | 25.4% | 11.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 909 | 0.5503 | 0.4123 | 0.5039 | +0.046 | -0.091 | -0.0042 ± 0.0051 |
| ratio 4-10x | 616 | 0.5895 | 0.4439 | 0.5032 | +0.086 | -0.059 | 0.0087 ± 0.0064 |
| ratio <2x | 2254 | 0.5392 | 0.4162 | 0.449 | +0.090 | -0.033 | 0.0114 ± 0.003 |
| ratio >=10x | 825 | 0.5706 | 0.3954 | 0.4618 | +0.109 | -0.066 | 0.0079 ± 0.0064 |
| thinner_sample 1000-3000 | 1255 | 0.5422 | 0.4156 | 0.4518 | +0.090 | -0.036 | 0.0091 ± 0.004 |
| thinner_sample 300-1000 | 1029 | 0.5672 | 0.4237 | 0.4937 | +0.074 | -0.070 | 0.0001 ± 0.005 |
| thinner_sample <300 | 1550 | 0.5628 | 0.3962 | 0.4671 | +0.096 | -0.071 | 0.0085 ± 0.0045 |
| thinner_sample >=3000 | 770 | 0.5366 | 0.4427 | 0.4701 | +0.067 | -0.028 | 0.0116 ± 0.0042 |
| data_status ADEQUATE | 1332 | 0.538 | 0.434 | 0.4535 | +0.085 | -0.019 | 0.0115 ± 0.0034 |
| data_status LIMITED | 1063 | 0.5512 | 0.4177 | 0.4873 | +0.064 | -0.070 | 0.0025 ± 0.0046 |
| data_status POOR | 2209 | 0.5645 | 0.4031 | 0.4703 | +0.094 | -0.067 | 0.0072 ± 0.0037 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 673 | 0.2021 | 0.2029 | -0.0008 ± 0.0006 | 0.5853 | 0.5871 | 0.5013 | 0.4866 | 0.5201 | -0.074 ± 0.0183 | -0.01 (5) |
| 3-5 | 422 | 0.2051 | 0.2044 | +0.0007 ± 0.0018 | 0.5934 | 0.5903 | 0.504 | 0.464 | 0.4739 | -0.107 ± 0.0227 | 0.02 (1) |
| 5-10 | 953 | 0.2024 | 0.2027 | -0.0003 ± 0.0022 | 0.5914 | 0.5893 | 0.5139 | 0.4399 | 0.4743 | -0.088 ± 0.0151 | -0.0167 (6) |
| 10-15 | 801 | 0.2157 | 0.207 | +0.0087 ± 0.004 | 0.6221 | 0.5964 | 0.532 | 0.4079 | 0.4345 | -0.104 ± 0.0161 | -0.048 (5) |
| 15-25 | 1048 | 0.2248 | 0.2132 | +0.0116 ± 0.0056 | 0.645 | 0.61 | 0.5778 | 0.382 | 0.4504 | -0.094 ± 0.0142 | -0.0033 (9) |
| 25-40 | 591 | 0.2216 | 0.2101 | +0.0115 ± 0.0112 | 0.6324 | 0.6035 | 0.6601 | 0.3501 | 0.4839 | -0.072 ± 0.0172 | -0.01 (1) |
| 40+ | 116 | 0.2743 | 0.202 | +0.0723 ± 0.036 | 0.7526 | 0.5904 | 0.7587 | 0.3114 | 0.4569 | -0.070 ± 0.0354 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3473 | 0.1851 | 0.186 | -0.0009 ± 0.0003 | 0.5458 | 0.5468 | 0.4908 | 0.4757 | 0.5079 | -0.023 ± 0.0074 | -0.0129 (17) |
| 3-5 | 2288 | 0.2004 | 0.1991 | +0.0013 ± 0.0008 | 0.5818 | 0.576 | 0.4858 | 0.4459 | 0.4489 | -0.054 ± 0.0095 | 0.0 (2) |
| 5-10 | 4954 | 0.1986 | 0.1955 | +0.0031 ± 0.0009 | 0.5818 | 0.5706 | 0.4838 | 0.4099 | 0.4247 | -0.047 ± 0.0064 | -0.0119 (21) |
| 10-15 | 4225 | 0.1981 | 0.1805 | +0.0175 ± 0.0016 | 0.5817 | 0.5323 | 0.4884 | 0.3639 | 0.3557 | -0.072 ± 0.0065 | -0.0281 (16) |
| 15-25 | 5334 | 0.2086 | 0.1692 | +0.0394 ± 0.0022 | 0.6109 | 0.5003 | 0.5039 | 0.3074 | 0.3065 | -0.074 ± 0.0056 | -0.0025 (44) |
| 25-40 | 4144 | 0.2231 | 0.1283 | +0.0948 ± 0.0035 | 0.6404 | 0.393 | 0.5322 | 0.2188 | 0.2278 | -0.061 ± 0.0054 | -0.01 (1) |
| 40+ | 2667 | 0.3793 | 0.0453 | +0.3340 ± 0.0047 | 0.9877 | 0.1742 | 0.6321 | 0.1065 | 0.0641 | -0.078 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 532 | 0.2086 | 0.2092 | -0.0007 ± 0.0007 | 0.5994 | 0.601 | 0.5077 | 0.4926 | 0.5169 | -0.106 ± 0.0214 | -0.01 (3) |
| 3-5 | 379 | 0.2282 | 0.2256 | +0.0026 ± 0.002 | 0.6434 | 0.6381 | 0.5144 | 0.4745 | 0.4565 | -0.130 ± 0.026 | 0.02 (1) |
| 5-10 | 826 | 0.2072 | 0.2067 | +0.0005 ± 0.0024 | 0.6008 | 0.5991 | 0.5468 | 0.4719 | 0.5097 | -0.084 ± 0.0164 | -0.01 (4) |
| 10-15 | 764 | 0.2153 | 0.2092 | +0.0061 ± 0.0041 | 0.6196 | 0.6039 | 0.565 | 0.4408 | 0.4804 | -0.105 ± 0.0173 | -0.04 (5) |
| 15-25 | 1068 | 0.2287 | 0.2106 | +0.0181 ± 0.0055 | 0.6501 | 0.6034 | 0.5874 | 0.3918 | 0.4476 | -0.099 ± 0.0143 | -0.0133 (9) |
| 25-40 | 754 | 0.2657 | 0.1994 | +0.0663 ± 0.0102 | 0.7431 | 0.5803 | 0.6567 | 0.3418 | 0.3966 | -0.120 ± 0.016 | -0.0075 (4) |
| 40+ | 281 | 0.3519 | 0.1748 | +0.1771 ± 0.0246 | 0.968 | 0.5207 | 0.7338 | 0.25 | 0.3238 | -0.064 ± 0.0238 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2964 | 0.1947 | 0.1949 | -0.0002 ± 0.0003 | 0.5659 | 0.5663 | 0.5129 | 0.4979 | 0.5108 | -0.046 ± 0.0084 | -0.0133 (15) |
| 3-5 | 1974 | 0.2016 | 0.2003 | +0.0014 ± 0.0008 | 0.5819 | 0.5783 | 0.5147 | 0.4748 | 0.4772 | -0.052 ± 0.0103 | 0.02 (1) |
| 5-10 | 4385 | 0.1973 | 0.1951 | +0.0022 ± 0.001 | 0.5806 | 0.5699 | 0.5115 | 0.4376 | 0.4629 | -0.035 ± 0.0068 | -0.0117 (6) |
| 10-15 | 3807 | 0.2009 | 0.189 | +0.0118 ± 0.0018 | 0.5898 | 0.5514 | 0.5146 | 0.3907 | 0.4056 | -0.055 ± 0.0072 | -0.0189 (18) |
| 15-25 | 5278 | 0.2154 | 0.1781 | +0.0373 ± 0.0023 | 0.6261 | 0.5236 | 0.5247 | 0.3289 | 0.3355 | -0.067 ± 0.0058 | -0.0086 (42) |
| 25-40 | 4849 | 0.2529 | 0.137 | +0.1159 ± 0.0034 | 0.7111 | 0.4206 | 0.5591 | 0.2421 | 0.2203 | -0.089 ± 0.0053 | -0.0044 (18) |
| 40+ | 3828 | 0.3926 | 0.0605 | +0.3321 ± 0.0045 | 1.0332 | 0.2162 | 0.6504 | 0.1188 | 0.0854 | -0.071 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 646 | 0.1998 | 0.202 | -0.0022 ± 0.0006 | 0.5804 | 0.5858 | 0.5016 | 0.4864 | 0.5495 | -0.033 ± 0.0183 | -0.0137 (8) |
| 3-5 | 457 | 0.2026 | 0.2011 | +0.0015 ± 0.0017 | 0.5884 | 0.5834 | 0.5065 | 0.4668 | 0.4705 | -0.117 ± 0.0219 | 0.0067 (3) |
| 5-10 | 979 | 0.2032 | 0.2 | +0.0032 ± 0.0022 | 0.5928 | 0.582 | 0.51 | 0.436 | 0.4505 | -0.102 ± 0.0147 | -0.0071 (7) |
| 10-15 | 795 | 0.2084 | 0.2052 | +0.0033 ± 0.004 | 0.6057 | 0.5927 | 0.5416 | 0.418 | 0.4679 | -0.088 ± 0.016 | -0.0317 (6) |
| 15-25 | 985 | 0.2311 | 0.2149 | +0.0162 ± 0.0058 | 0.66 | 0.6135 | 0.589 | 0.3944 | 0.4497 | -0.106 ± 0.0147 | -0.03 (1) |
| 25-40 | 618 | 0.2139 | 0.2173 | -0.0034 ± 0.011 | 0.617 | 0.6201 | 0.6692 | 0.3586 | 0.5162 | -0.056 ± 0.0168 | 0.015 (2) |
| 40+ | 124 | 0.2877 | 0.2134 | +0.0743 ± 0.036 | 0.7955 | 0.6147 | 0.767 | 0.3181 | 0.4677 | -0.064 ± 0.038 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3388 | 0.1862 | 0.1869 | -0.0007 ± 0.0003 | 0.5476 | 0.5487 | 0.4887 | 0.4735 | 0.492 | -0.034 ± 0.0075 | -0.0163 (35) |
| 3-5 | 2306 | 0.1972 | 0.1952 | +0.0020 ± 0.0007 | 0.5776 | 0.571 | 0.4887 | 0.4491 | 0.4441 | -0.065 ± 0.0094 | -0.0094 (18) |
| 5-10 | 5057 | 0.1957 | 0.1901 | +0.0056 ± 0.0009 | 0.5751 | 0.5566 | 0.4839 | 0.4099 | 0.4097 | -0.060 ± 0.0062 | -0.01 (31) |
| 10-15 | 4092 | 0.1915 | 0.1768 | +0.0147 ± 0.0016 | 0.5664 | 0.5225 | 0.5003 | 0.3769 | 0.3785 | -0.063 ± 0.0066 | -0.015 (12) |
| 15-25 | 5462 | 0.211 | 0.1717 | +0.0393 ± 0.0022 | 0.6163 | 0.5065 | 0.5139 | 0.3187 | 0.3164 | -0.074 ± 0.0056 | -0.03 (2) |
| 25-40 | 4173 | 0.2198 | 0.1316 | +0.0882 ± 0.0035 | 0.6339 | 0.4002 | 0.5366 | 0.2208 | 0.2406 | -0.053 ± 0.0054 | 0.01 (3) |
| 40+ | 2607 | 0.3933 | 0.0508 | +0.3425 ± 0.005 | 1.0277 | 0.1884 | 0.6446 | 0.1136 | 0.0706 | -0.079 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1030 | 0.1964 | 0.1965 | -0.0001 ± 0.0005 | 0.5724 | 0.5721 | 0.5017 | 0.4867 | 0.4903 | -0.064 ± 0.014 | -0.0224 (49) |
| 3-5 | 712 | 0.1932 | 0.1924 | +0.0008 ± 0.0013 | 0.5641 | 0.5608 | 0.4904 | 0.4506 | 0.4579 | -0.062 ± 0.0168 | -0.0194 (34) |
| 5-10 | 1506 | 0.2018 | 0.1962 | +0.0055 ± 0.0017 | 0.5926 | 0.5749 | 0.4971 | 0.4237 | 0.4236 | -0.073 ± 0.0116 | -0.005 (78) |
| 10-15 | 1006 | 0.2103 | 0.1984 | +0.0119 ± 0.0035 | 0.6099 | 0.5788 | 0.5246 | 0.4016 | 0.4125 | -0.073 ± 0.0144 | 0.0014 (64) |
| 15-25 | 1343 | 0.2318 | 0.2115 | +0.0202 ± 0.0049 | 0.6615 | 0.6082 | 0.5795 | 0.3847 | 0.4319 | -0.074 ± 0.0126 | -0.0214 (59) |
| 25-40 | 819 | 0.2446 | 0.2087 | +0.0359 ± 0.0098 | 0.6976 | 0.5992 | 0.6779 | 0.3655 | 0.464 | -0.085 ± 0.0149 | -0.0219 (26) |
| 40+ | 269 | 0.3454 | 0.2025 | +0.1429 ± 0.0269 | 0.9985 | 0.5922 | 0.8091 | 0.3283 | 0.4387 | -0.090 ± 0.0247 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3415 | 0.1825 | 0.1827 | -0.0002 ± 0.0003 | 0.5377 | 0.5372 | 0.5026 | 0.4873 | 0.4966 | -0.041 ± 0.0074 | -0.0157 (88) |
| 3-5 | 2372 | 0.1967 | 0.1946 | +0.0021 ± 0.0007 | 0.5728 | 0.5678 | 0.4977 | 0.458 | 0.4519 | -0.057 ± 0.0092 | -0.0209 (69) |
| 5-10 | 4790 | 0.1958 | 0.1878 | +0.0079 ± 0.0009 | 0.5772 | 0.5531 | 0.4923 | 0.4188 | 0.4044 | -0.070 ± 0.0063 | -0.0082 (132) |
| 10-15 | 3337 | 0.207 | 0.1912 | +0.0158 ± 0.0019 | 0.6029 | 0.5609 | 0.5293 | 0.4062 | 0.4028 | -0.066 ± 0.0076 | -0.0053 (105) |
| 15-25 | 4145 | 0.2307 | 0.2003 | +0.0304 ± 0.0028 | 0.6648 | 0.5801 | 0.5699 | 0.3743 | 0.3959 | -0.067 ± 0.007 | -0.0253 (107) |
| 25-40 | 2821 | 0.2583 | 0.1853 | +0.0730 ± 0.0051 | 0.7327 | 0.5403 | 0.6343 | 0.3209 | 0.3633 | -0.078 ± 0.0079 | -0.0229 (51) |
| 40+ | 1229 | 0.3755 | 0.1458 | +0.2297 ± 0.0114 | 1.0633 | 0.4394 | 0.7316 | 0.2283 | 0.2653 | -0.071 ± 0.0102 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4604 | 1.036 ± 0.041 | 1.112 | 0.1684 | 0.163 | 0.2143 | 0.207 |
| gen2 | 4604 | 0.831 ± 0.038 | 1.077 | 0.1685 | 0.1638 | 0.2338 | 0.2067 |
| gen1_elo | 4604 | 1.009 ± 0.04 | 1.109 | 0.175 | 0.1632 | 0.2132 | 0.2072 |
| gen1_sr | 4604 | 1.016 ± 0.05 | 1.144 | 0.1293 | 0.1656 | 0.2302 | 0.2062 |
| gen1_ledger | 6685 | 0.864 ± 0.029 | 1.066 | 0.1838 | 0.177 | 0.2184 | 0.201 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 22,997)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,179 | 22.5% |
| STALE_QUOTE | market_freshness | 5,019 | 21.8% |
| BOOK_QUALITY | execution | 4,417 | 19.2% |
| POOR_DATA | data | 2,567 | 11.2% |
| LIMITED_DATA | data | 1,420 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,239 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,090 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 978 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 674 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 413 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.5%, market_freshness 21.8%, execution 19.2%, data 17.3%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 93.9%, LOW_DATA_QUALITY 70.8%, THIN_PLAYER_HISTORY 59.6%, STALE_PLAYER_DATA 50.0%, STALE_KALSHI_QUOTE 43.9%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.3%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.8%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.7%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.9%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 12,274)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,158 | 33.9% |
| BOOK_QUALITY | execution | 2,319 | 18.9% |
| STALE_QUOTE | market_freshness | 2,317 | 18.9% |
| POOR_DATA | data | 1,055 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 661 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 541 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 428 | 3.5% |
| LIMITED_DATA | data | 425 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 272 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 97 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.9%, execution 18.9%, market_freshness 18.9%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.3%, THIN_PLAYER_HISTORY 61.7%, STALE_KALSHI_QUOTE 51.8%, STALE_PLAYER_DATA 44.5%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.8%, PLAYER_IDENTITY_RISK 20.1%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 9.9%, LEVEL_TRANSFER_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.0%, POST_SETTLEMENT_OBSERVATION 33.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9502, "IDENTITY_AMBIGUOUS": 2772}; ticker orientation: {"VERIFIED": 12274}.

Checks: discipline:AMBIGUOUS 864, discipline:PASS 11410, identity_confidence:AMBIGUOUS 2465, identity_confidence:PASS 9809, level_mapping:NA 876, level_mapping:PASS 11398, market_pair:AMBIGUOUS 465, market_pair:NA 301, market_pair:PASS 11508, model_complement:NA 268, model_complement:PASS 12006, namesake:AMBIGUOUS 6, namesake:PASS 12268, physical_match_id:NA 4329, physical_match_id:PASS 7945, player_ids:PASS 12274, same_pair_other_event:PASS 12274, ticker_orientation:PASS 12274

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,801 | 4.3% | 3.8% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 47, "data": 35, "execution": 24, "model_calibration": 20, "market_freshness/coverage": 15, "coverage": 13} | 5.87 | 0.2239 / 0.2208 (539) | 19.9% | 3.3% | 3.3% | 2.7% |
| CHALLENGER | 8,690 | 16.8% | 6.9% | 11.9% | {"coverage": 816, "market_freshness/coverage": 177, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 70, "execution": 35, "model_calibration": 35, "mapping": 16, "possible_market_error": 1} | 7.6 | 0.2185 / 0.2089 (2043) | 34.2% | 17.3% | 4.1% | 22.2% |
| DOUBLES | 1,814 | 47.6% | 47.3% | 7.0% | {"execution": 481, "mapping": 215, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.9 | 0.3101 / 0.2361 (439) | 12.9% | 0.0% | 100.0% | 6.6% |
| ITF_MEN | 15,045 | 25.6% | 17.8% | 31.4% | {"coverage": 1430, "execution": 734, "market_freshness": 667, "data": 507, "market_freshness/coverage": 335, "mapping": 176, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.98 | 0.2165 / 0.1986 (3343) | 37.5% | 70.2% | 19.8% | 22.3% |
| ITF_WOMEN | 20,264 | 27.1% | 20.0% | 44.7% | {"coverage": 1867, "market_freshness": 1215, "execution": 994, "data": 750, "market_freshness/coverage": 457, "mapping": 128, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.92 | 0.2029 / 0.1959 (3844) | 39.6% | 57.1% | 10.3% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,410 | 5.5% | 5.0% | 1.5% | {"market_freshness": 65, "model_calibration_or_unknown": 39, "execution": 26, "model_calibration": 16, "data": 16, "coverage": 12, "market_freshness/coverage": 11, "mapping": 1} | 7.66 | 0.2317 / 0.2263 (537) | 24.8% | 1.2% | 1.6% | 3.3% |
| WTA125 | 1,624 | 12.4% | 10.2% | 1.7% | {"market_freshness": 44, "model_calibration_or_unknown": 43, "market_freshness/coverage": 38, "data": 28, "execution": 20, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.52 | 0.2178 / 0.2042 (502) | 23.9% | 11.5% | 6.6% | 8.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
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
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 43 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.4h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9681, "by_level_share_of_ge_25pp": {"ATP": 0.0169, "CHALLENGER": 0.1189, "DOUBLES": 0.0704, "ITF_MEN": 0.3139, "ITF_WOMEN": 0.4474, "OTHER": 0.001, "WTA": 0.0152, "WTA125": 0.0165}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5182, "share_primary_cause_market_settled_or_in_play": 0.4276, "share_primary_cause_stale_quote_only": 0.1888}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 12274, "identity_ambiguous_share": 0.2258, "ticker_orientation": {"VERIFIED": 12274}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7945, "with_external": 395, "coverage": 0.0497, "external_status": {"EXTERNAL_STALE": 237, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 237, "MODEL_LONE_OUTLIER": 149, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3772, "share_external_supports_model": 0.0228}, "pregame_clean_ge_25pp": {"n": 3897, "with_external": 372, "coverage": 0.0955, "external_status": {"EXTERNAL_STALE": 221, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 221, "MODEL_LONE_OUTLIER": 142, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3817, "share_external_supports_model": 0.0242}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 476.0, "median_sample_ratio": 2.43, "median_min_matches": 20.0, "median_max_days_since_last": 231.0, "share_severe_asymmetry": 0.216, "data_status": {"POOR": 6831, "LIMITED": 3203, "ADEQUATE": 2240}, "comparison_lt_10pp": {"median_thinner_serve_points": 1774.0, "median_sample_ratio": 1.67, "median_min_matches": 98.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 909, "model_minus_observed": 0.0465, "kalshi_minus_observed": -0.0915, "brier_diff_model_minus_kalshi": -0.0042}, "4-10x": {"n": 616, "model_minus_observed": 0.0863, "kalshi_minus_observed": -0.0593, "brier_diff_model_minus_kalshi": 0.0087}, "<2x": {"n": 2254, "model_minus_observed": 0.0903, "kalshi_minus_observed": -0.0328, "brier_diff_model_minus_kalshi": 0.0114}, ">=10x": {"n": 825, "model_minus_observed": 0.1088, "kalshi_minus_observed": -0.0664, "brier_diff_model_minus_kalshi": 0.0079}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4604, "model": {"intercept": -0.53, "slope": 0.831, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.21, "slope": 1.077, "slope_se": 0.043}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1638, "model_brier": 0.2338, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.0271, "brier_diff_se": 0.0028, "model_logloss": 0.6644, "kalshi_logloss": 0.5965}, "fair_v1": {"n": 4604, "model": {"intercept": -0.413, "slope": 1.036, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.29, "slope": 1.112, "slope_se": 0.043}, "mean_extremity_model": 0.1684, "mean_extremity_kalshi": 0.163, "model_brier": 0.2143, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0073, "brier_diff_se": 0.0023, "model_logloss": 0.6176, "kalshi_logloss": 0.5969}, "gen1_elo": {"n": 4604, "model": {"intercept": -0.387, "slope": 1.009, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.312, "slope": 1.109, "slope_se": 0.043}, "mean_extremity_model": 0.175, "mean_extremity_kalshi": 0.1632, "model_brier": 0.2132, "kalshi_brier": 0.2072, "brier_diff_model_minus_kalshi": 0.0061, "brier_diff_se": 0.0023, "model_logloss": 0.6159, "kalshi_logloss": 0.5973}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2459, "share_ge_15": 0.4431, "median_abs_gap": 13.07, "n": 32308}, "gen1_elo": {"share_ge_25": 0.2437, "share_ge_15": 0.4425, "median_abs_gap": 12.97, "n": 32308}, "gen1_sr": {"share_ge_25": 0.3136, "share_ge_15": 0.5207, "median_abs_gap": 15.91, "n": 32308}, "gen2": {"share_ge_25": 0.3174, "share_ge_15": 0.5119, "median_abs_gap": 15.52, "n": 32308}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1547, "share_ge_15": 0.3598, "median_abs_gap": 10.88, "n": 25186}, "gen1_elo": {"share_ge_25": 0.1554, "share_ge_15": 0.3579, "median_abs_gap": 10.7, "n": 25183}, "gen1_sr": {"share_ge_25": 0.2215, "share_ge_15": 0.4432, "median_abs_gap": 13.01, "n": 25187}, "gen2": {"share_ge_25": 0.2379, "share_ge_15": 0.4443, "median_abs_gap": 13.02, "n": 25188}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.87, "share_ge_25_all": 0.0431, "share_ge_25_pregame_clean": 0.0383}, "WTA": {"median_abs_gap_pregame_clean": 7.66, "share_ge_25_all": 0.0545, "share_ge_25_pregame_clean": 0.0495}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2355, "share_within_10pp_all": 0.4339, "share_within_10pp_pregame_clean": 0.4855, "corr_model_vs_mid_pregame_clean": 0.8433}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 673, "model_brier": 0.2021, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": -0.0008}, "10-15": {"n_settled": 801, "model_brier": 0.2157, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0087}, "15-25": {"n_settled": 1048, "model_brier": 0.2248, "kalshi_brier": 0.2132, "brier_diff_model_minus_kalshi": 0.0116}, "25-40": {"n_settled": 591, "model_brier": 0.2216, "kalshi_brier": 0.2101, "brier_diff_model_minus_kalshi": 0.0115}, "3-5": {"n_settled": 422, "model_brier": 0.2051, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 116, "model_brier": 0.2743, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0723}, "5-10": {"n_settled": 953, "model_brier": 0.2024, "kalshi_brier": 0.2027, "brier_diff_model_minus_kalshi": -0.0003}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.53, "slope": 0.831, "slope_se": 0.038}, "kalshi_slope": {"intercept": 0.21, "slope": 1.077, "slope_se": 0.043}, "n": 4604}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.499, "slope": 0.864, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.161, "slope": 1.066, "slope_se": 0.034}, "n": 6685}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 439, "model_brier": 0.3101, "kalshi_brier": 0.2361, "brier_diff_model_minus_kalshi": 0.074, "brier_diff_se": 0.0144, "corr_model_outcome": 0.034, "corr_kalshi_outcome": 0.2515}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
