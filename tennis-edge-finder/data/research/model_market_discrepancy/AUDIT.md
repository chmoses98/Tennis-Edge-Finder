# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-25T01:04Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 52,398): 0-3 13.9%, 3-5 9.4%, 5-10 19.8%, 10-15 15.3%, 15-25 19.2%, 25-40 14.1%, 40+ 8.2%; median gap 12.11 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.7%, Challenger 11.8%, doubles 6.7%). Main tour: ATP 4.6% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,698): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.7%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.1%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.7%, market_freshness 18.7%, execution 18.1%, data 12.1%, market_freshness/coverage 9.0%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,698 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.0% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 495.0 points vs 1723.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.031, Gen-2 0.835, Gen-1 ledger 0.86 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 568 model 0.2229 vs Kalshi 0.2096; n 115 model 0.2766 vs Kalshi 0.2018.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 226,974 model-market comparisons (369,216 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 76,116 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-25T00:50:12.740969+00:00'], shadow board 60,560 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-25T00:50:15.983938+00:00'], Model 4 28,409 rows, 20,149 settled tickers, 7,142 tickers with an external scan.
* By model: {"gen1_ledger": 51839, "gen1_elo": 30455, "fair_v1": 30455, "gen2": 30455, "gen1_sr": 30455, "model4_fundamental": 26675, "model4_conditioned": 26640}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 52,398 | 13.9 | 9.4 | 19.8 | 15.3 | 19.2 | 14.1 | 8.2 | 12.11 | 41.5% | 22.3% |
| MW fair_v1 | 30,455 | 12.8 | 8.5 | 18.5 | 15.5 | 19.7 | 15.0 | 10.0 | 13.19 | 44.7% | 25.0% |
| MW gen1_elo | 30,455 | 12.7 | 8.5 | 19.0 | 15.2 | 19.9 | 15.0 | 9.7 | 13.02 | 44.6% | 24.7% |
| MW gen1_ledger | 21,943 | 15.5 | 10.8 | 21.5 | 15.0 | 18.6 | 12.8 | 5.8 | 10.54 | 37.2% | 18.6% |
| MW gen1_sr | 30,455 | 10.2 | 7.0 | 16.6 | 13.6 | 20.8 | 18.8 | 13.0 | 16.04 | 52.6% | 31.8% |
| MW gen2 | 30,455 | 10.9 | 7.3 | 16.2 | 14.0 | 19.4 | 17.9 | 14.2 | 15.65 | 51.5% | 32.1% |
| all families model4_conditioned | 26,640 | 21.9 | 18.9 | 34.8 | 17.5 | 4.4 | 1.5 | 1.0 | 5.97 | 7.0% | 2.5% |
| all families model4_fundamental | 26,675 | 16.8 | 13.3 | 34.1 | 20.4 | 10.6 | 3.5 | 1.3 | 7.75 | 15.3% | 4.8% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.9%, >=15pp 41.5%, >=20pp 30.9%, >=25pp 22.3%, >=30pp 16.2%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.46pp; >=10pp 45.4%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,693 | 28.1 | 14.1 | 25.0 | 15.5 | 11.9 | 4.6 | 0.7 | 6.17 | 17.3% | 5.3% |
| CHALLENGER | 4,724 | 15.7 | 9.9 | 20.3 | 15.6 | 14.9 | 12.5 | 11.1 | 11.12 | 38.4% | 23.5% |
| ITF_MEN | 8,412 | 10.1 | 7.3 | 16.8 | 14.7 | 21.5 | 17.4 | 12.2 | 15.43 | 51.1% | 29.6% |
| ITF_WOMEN | 12,040 | 9.4 | 6.9 | 15.9 | 15.3 | 22.3 | 18.2 | 12.1 | 15.82 | 52.5% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,918 | 17.6 | 12.8 | 26.4 | 19.1 | 17.5 | 6.0 | 0.7 | 8.25 | 24.1% | 6.7% |
| WTA125 | 662 | 13.3 | 7.4 | 23.4 | 20.5 | 19.8 | 13.6 | 2.0 | 11.31 | 35.4% | 15.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,693 | 23.9 | 15.1 | 24.7 | 17.7 | 13.0 | 4.6 | 1.0 | 6.69 | 18.5% | 5.6% |
| CHALLENGER | 4,724 | 14.9 | 8.7 | 18.4 | 14.6 | 17.6 | 13.9 | 11.9 | 12.55 | 43.4% | 25.8% |
| ITF_MEN | 8,412 | 8.2 | 5.9 | 14.4 | 13.0 | 19.7 | 21.0 | 17.8 | 18.72 | 58.5% | 38.9% |
| ITF_WOMEN | 12,040 | 8.2 | 5.6 | 13.7 | 13.2 | 20.6 | 21.0 | 17.7 | 19.13 | 59.3% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,918 | 14.1 | 10.2 | 22.2 | 16.2 | 22.5 | 13.4 | 1.3 | 10.91 | 37.2% | 14.7% |
| WTA125 | 662 | 6.8 | 4.7 | 16.9 | 17.5 | 26.0 | 19.3 | 8.8 | 16.84 | 54.1% | 28.1% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,693 | 23.7 | 12.6 | 23.9 | 16.6 | 15.1 | 7.0 | 1.2 | 7.5 | 23.3% | 8.2% |
| CHALLENGER | 4,724 | 14.3 | 9.1 | 20.5 | 15.6 | 16.2 | 13.1 | 11.2 | 11.49 | 40.5% | 24.2% |
| ITF_MEN | 8,412 | 9.7 | 7.3 | 16.9 | 13.8 | 22.2 | 17.8 | 12.3 | 15.84 | 52.3% | 30.1% |
| ITF_WOMEN | 12,040 | 9.4 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.2 | 15.62 | 51.9% | 29.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 1,918 | 23.8 | 17.6 | 30.4 | 15.0 | 10.1 | 2.7 | 0.5 | 6.01 | 13.2% | 3.1% |
| WTA125 | 662 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.9 | 0.3 | 7.73 | 19.9% | 6.2% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,660 | 25.2 | 19.1 | 30.1 | 12.9 | 9.4 | 3.0 | 0.3 | 5.65 | 12.7% | 3.3% |
| CHALLENGER | 3,249 | 21.5 | 14.4 | 26.5 | 14.5 | 14.7 | 6.6 | 1.8 | 7.32 | 23.1% | 8.4% |
| DOUBLES | 1,668 | 5.2 | 4.6 | 12.1 | 10.5 | 20.9 | 26.1 | 20.7 | 23.67 | 67.6% | 46.8% |
| ITF_MEN | 6,221 | 13.8 | 9.1 | 20.0 | 16.1 | 21.2 | 13.3 | 6.5 | 12.13 | 41.0% | 19.8% |
| ITF_WOMEN | 7,160 | 12.5 | 8.9 | 19.2 | 15.2 | 21.7 | 16.3 | 6.2 | 12.93 | 44.1% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,102 | 22.9 | 15.8 | 30.0 | 17.7 | 9.7 | 3.5 | 0.4 | 6.8 | 13.6% | 3.9% |
| WTA125 | 734 | 21.5 | 14.0 | 21.9 | 18.1 | 14.6 | 7.8 | 2.0 | 8.14 | 24.4% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,618 | 28.4 | 14.3 | 25.5 | 15.4 | 11.7 | 4.2 | 0.5 | 6.01 | 16.4% | 4.7% |
| CHALLENGER | 3,330 | 20.6 | 12.4 | 25.0 | 18.0 | 15.3 | 6.8 | 1.9 | 8.34 | 23.9% | 8.7% |
| ITF_MEN | 6,155 | 12.2 | 8.8 | 20.3 | 16.6 | 22.7 | 14.3 | 5.1 | 12.54 | 42.1% | 19.4% |
| ITF_WOMEN | 8,986 | 11.2 | 8.2 | 18.1 | 17.4 | 24.2 | 15.3 | 5.5 | 13.52 | 45.1% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,863 | 17.8 | 12.7 | 26.4 | 19.4 | 17.4 | 5.6 | 0.7 | 8.24 | 23.8% | 6.3% |
| WTA125 | 636 | 13.7 | 7.2 | 23.0 | 20.9 | 20.4 | 13.2 | 1.6 | 11.31 | 35.2% | 14.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,618 | 24.2 | 15.5 | 24.9 | 17.6 | 13.0 | 4.2 | 0.6 | 6.49 | 17.8% | 4.8% |
| CHALLENGER | 3,330 | 18.9 | 11.2 | 22.8 | 17.4 | 18.0 | 9.5 | 2.1 | 9.21 | 29.6% | 11.6% |
| ITF_MEN | 6,156 | 9.8 | 7.1 | 16.8 | 15.0 | 21.6 | 19.2 | 10.5 | 15.48 | 51.3% | 29.7% |
| ITF_WOMEN | 8,987 | 9.3 | 6.5 | 15.2 | 14.7 | 22.6 | 20.5 | 11.3 | 16.66 | 54.4% | 31.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,863 | 14.2 | 10.2 | 22.2 | 16.2 | 22.5 | 13.2 | 1.3 | 10.9 | 37.1% | 14.5% |
| WTA125 | 636 | 6.6 | 4.9 | 17.0 | 17.9 | 25.9 | 19.8 | 7.9 | 16.74 | 53.6% | 27.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,610 | 25.4 | 19.4 | 30.1 | 13.0 | 9.0 | 2.9 | 0.2 | 5.56 | 12.0% | 3.0% |
| CHALLENGER | 2,836 | 22.9 | 15.5 | 28.0 | 14.5 | 14.0 | 4.5 | 0.5 | 6.79 | 19.1% | 5.0% |
| DOUBLES | 1,549 | 5.2 | 4.8 | 12.3 | 10.7 | 20.7 | 26.0 | 20.3 | 23.56 | 67.1% | 46.4% |
| ITF_MEN | 5,217 | 14.9 | 9.8 | 21.7 | 16.9 | 21.1 | 11.6 | 4.0 | 11.13 | 36.7% | 15.6% |
| ITF_WOMEN | 5,930 | 13.5 | 9.4 | 20.7 | 16.0 | 21.9 | 15.0 | 3.5 | 11.79 | 40.4% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,052 | 23.4 | 16.2 | 30.0 | 17.7 | 9.7 | 2.9 | 0.1 | 6.68 | 12.6% | 2.9% |
| WTA125 | 623 | 23.6 | 15.6 | 23.4 | 19.6 | 12.8 | 4.7 | 0.3 | 7.2 | 17.8% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,668 | 5.2 | 4.6 | 12.1 | 10.5 | 20.9 | 26.1 | 20.7 | 23.67 | 67.6% | 46.8% |
| singles | 20,275 | 16.3 | 11.3 | 22.3 | 15.4 | 18.4 | 11.7 | 4.6 | 10.01 | 34.7% | 16.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 6 | 16.7 | 33.3 | 33.3 | 0.0 | 16.7 | 0.0 | 0.0 | 4.75 | 16.7% | 0.0% |
| Clay | 6,704 | 12.9 | 9.0 | 19.2 | 15.7 | 18.7 | 14.5 | 10.0 | 12.81 | 43.2% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 18,890 | 13.3 | 8.5 | 18.6 | 15.2 | 19.7 | 14.9 | 9.8 | 13.09 | 44.4% | 24.7% |
| UNKNOWN | 4,618 | 10.7 | 7.5 | 17.0 | 16.8 | 20.6 | 16.3 | 11.1 | 14.15 | 48.0% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,670 | 19.5 | 11.8 | 21.5 | 16.5 | 15.0 | 9.3 | 6.3 | 9.15 | 30.6% | 15.6% |
| B | 3,779 | 12.4 | 8.7 | 19.5 | 16.2 | 19.3 | 12.8 | 11.1 | 12.67 | 43.2% | 23.9% |
| C | 4,260 | 11.5 | 8.7 | 19.7 | 15.2 | 19.4 | 14.7 | 10.7 | 13.19 | 44.8% | 25.4% |
| D | 4,720 | 12.1 | 7.7 | 17.4 | 15.4 | 21.4 | 15.8 | 10.2 | 13.99 | 47.4% | 26.0% |
| F | 9,026 | 7.6 | 5.5 | 15.1 | 14.6 | 23.5 | 21.2 | 12.6 | 17.8 | 57.3% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,266 | 23.2 | 15.8 | 28.8 | 15.2 | 11.6 | 4.0 | 1.4 | 6.64 | 17.0% | 5.5% |
| B | 2,984 | 16.2 | 10.4 | 23.0 | 16.2 | 19.6 | 10.7 | 3.9 | 10.06 | 34.2% | 14.5% |
| C | 4,301 | 11.1 | 7.4 | 18.3 | 14.4 | 21.4 | 16.8 | 10.5 | 14.39 | 48.8% | 27.4% |
| D | 3,034 | 14.3 | 9.7 | 19.9 | 14.6 | 21.0 | 14.4 | 6.1 | 12.06 | 41.5% | 20.5% |
| F | 5,358 | 10.2 | 8.4 | 15.7 | 15.0 | 22.6 | 19.9 | 8.1 | 15.3 | 50.6% | 28.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,939 | 17.8 | 10.6 | 20.8 | 16.2 | 15.6 | 10.2 | 8.9 | 10.22 | 34.6% | 19.1% |
| LIMITED | 6,431 | 13.2 | 10.0 | 20.3 | 15.8 | 19.3 | 13.5 | 7.8 | 12.0 | 40.6% | 21.3% |
| POOR | 14,085 | 9.1 | 6.3 | 16.0 | 15.0 | 22.7 | 19.2 | 11.8 | 16.26 | 53.6% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,268 | 25.4 | 19.4 | 33.8 | 13.2 | 5.7 | 2.2 | 0.3 | 5.5 | 8.2% | 2.5% |
| GAME_SPREAD | 4,863 | 22.2 | 15.2 | 33.4 | 17.2 | 9.2 | 2.4 | 0.3 | 6.74 | 11.9% | 2.7% |
| MATCH_WINNER | 21,943 | 15.5 | 10.8 | 21.5 | 15.0 | 18.6 | 12.8 | 5.8 | 10.54 | 37.2% | 18.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 11,043 | 28.6 | 16.9 | 31.0 | 12.5 | 8.3 | 2.2 | 0.4 | 5.53 | 10.9% | 2.6% |
| TOTAL_GAMES | 7,698 | 9.1 | 9.9 | 36.5 | 28.3 | 10.3 | 3.2 | 2.7 | 9.38 | 16.2% | 5.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,487 | 25.2 | 32.8 | 32.6 | 5.0 | 3.4 | 0.8 | 0.2 | 4.51 | 4.4% | 1.0% |
| GAME_SPREAD | 6,329 | 45.6 | 16.7 | 26.8 | 7.9 | 1.7 | 0.9 | 0.3 | 3.47 | 2.9% | 1.2% |
| TOTAL_GAMES | 10,824 | 5.1 | 7.9 | 41.4 | 34.1 | 6.9 | 2.5 | 2.1 | 9.52 | 11.5% | 4.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,498 | 24.1 | 17.4 | 35.4 | 12.8 | 7.2 | 2.6 | 0.4 | 5.9 | 10.3% | 3.0% |
| GAME_SPREAD | 6,332 | 19.6 | 13.4 | 27.8 | 20.8 | 13.2 | 4.3 | 0.9 | 7.96 | 18.5% | 5.2% |
| TOTAL_GAMES | 10,845 | 8.8 | 9.8 | 36.7 | 26.9 | 12.0 | 3.6 | 2.3 | 9.41 | 17.9% | 6.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 30,455 | 44.7% | 25.0% | 13.19 | 36.2% | 15.7% | 10.95 |
| gen1_elo | 30,455 | 44.6% | 24.7% | 13.02 | 36.0% | 15.7% | 10.76 |
| gen1_sr | 30,455 | 52.6% | 31.8% | 16.04 | 44.7% | 22.3% | 13.14 |
| gen2 | 30,455 | 51.5% | 32.1% | 15.65 | 44.6% | 23.9% | 13.1 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,406 | 15.7 | 10.3 | 21.4 | 17.3 | 20.1 | 11.9 | 3.3 | 10.73 | 35.4% | 15.3% |
| STALE | 15,049 | 9.9 | 6.6 | 15.5 | 13.7 | 19.2 | 18.2 | 16.9 | 17.04 | 54.2% | 35.0% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 15,411 | 16.5 | 11.3 | 22.3 | 15.2 | 17.8 | 12.2 | 4.8 | 9.98 | 34.8% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 52,398 | 15411 | 18878 | 18109 | 24.2 | 148.8 | 1400.4 |
| ge_15pp | 21,767 | 5357 | 6738 | 9672 | 26.3 | 444.6 | 1380.4 |
| ge_25pp | 11,698 | 2612 | 2942 | 6144 | 32.7 | 588.6 | 1380.4 |
| lt_10pp | 22,599 | 7719 | 8924 | 5956 | 22.4 | 47.7 | 1341.5 |

Current slate `SL-20261025T010401Z-035efcc9`: 688 priced rows, quote age at build {'median': 14.4, 'max': 14.4}, freshness {'AGING': 688}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 25 | 0.0 | 0.0 | 24.0 | 8.0 | 36.0 | 32.0 | 0.0 | 20.47 | 68.0% | 32.0% |
| EXTERNAL_LONE_OUTLIER | 16 | 75.0 | 25.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,924 | 19.2 | 11.2 | 24.8 | 19.0 | 17.9 | 7.2 | 0.7 | 8.86 | 25.8% | 7.8% |
| KALSHI_LONE_OUTLIER | 18 | 5.6 | 5.6 | 72.2 | 5.6 | 5.6 | 5.6 | 0.0 | 6.16 | 11.1% | 5.6% |
| MARKETS_AGREE | 592 | 65.2 | 34.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,258 | 0.0 | 2.4 | 36.0 | 25.8 | 24.6 | 10.6 | 0.7 | 12.0 | 35.9% | 11.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 30,455 | 4833 (15.9%) | 26.0% | 0.9% | {"EXTERNAL_STALE": 2924, "AGREES_WITH_KALSHI": 1258, "ALL_AGREE": 592, "SUPPORTS_MODEL_DIRECTION": 24, "AGREES_WITH_MODEL": 18, "EXTERNAL_OUTLIER": 16, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,611 | 1224 (9.0%) | 36.9% | 1.6% | {"EXTERNAL_STALE": 754, "AGREES_WITH_KALSHI": 451, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,624 | 380 (5.0%) | 37.4% | 2.4% | {"EXTERNAL_STALE": 229, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,697 | 357 (9.7%) | 37.8% | 2.5% | {"EXTERNAL_STALE": 213, "AGREES_WITH_KALSHI": 135, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,111 | 2726 (22.5%) | 17.7% | 0.7% | {"EXTERNAL_STALE": 1614, "ALL_AGREE": 592, "AGREES_WITH_KALSHI": 483, "EXTERNAL_OUTLIER": 16, "AGREES_WITH_MODEL": 15, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,810 | 10.3 | 7.5 | 19.4 | 14.4 | 22.2 | 16.1 | 10.1 | 14.19 | 48.4% | 26.2% |
| 4-10x | 3,967 | 10.9 | 8.2 | 19.1 | 15.3 | 21.4 | 14.9 | 10.2 | 13.76 | 46.4% | 25.0% |
| <2x | 15,451 | 14.9 | 9.7 | 19.0 | 16.5 | 17.5 | 13.1 | 9.2 | 11.87 | 39.9% | 22.4% |
| >=10x | 5,227 | 10.8 | 6.2 | 15.2 | 14.2 | 21.9 | 19.6 | 12.0 | 16.41 | 53.5% | 31.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,794 | 12.4 | 8.6 | 19.4 | 16.0 | 19.0 | 13.8 | 10.8 | 12.98 | 43.7% | 24.7% |
| 300-1000 | 6,471 | 11.6 | 8.5 | 17.3 | 15.3 | 20.5 | 16.4 | 10.3 | 13.96 | 47.2% | 26.7% |
| <300 | 9,947 | 8.6 | 5.6 | 15.5 | 14.7 | 23.1 | 20.1 | 12.4 | 17.01 | 55.6% | 32.5% |
| >=3000 | 6,243 | 21.3 | 12.9 | 23.3 | 16.6 | 14.1 | 7.1 | 4.8 | 7.96 | 26.0% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 864 | 0.5503 | 0.4117 | 0.5 | +0.050 | -0.088 | -0.0037 ± 0.0052 |
| ratio 4-10x | 593 | 0.5889 | 0.4423 | 0.4958 | +0.093 | -0.053 | 0.0115 ± 0.0066 |
| ratio <2x | 2147 | 0.5383 | 0.4155 | 0.4453 | +0.093 | -0.030 | 0.0128 ± 0.0031 |
| ratio >=10x | 793 | 0.5718 | 0.3962 | 0.4628 | +0.109 | -0.067 | 0.007 ± 0.0065 |
| thinner_sample 1000-3000 | 1190 | 0.5427 | 0.4159 | 0.4445 | +0.098 | -0.029 | 0.0109 ± 0.0041 |
| thinner_sample 300-1000 | 997 | 0.5674 | 0.4235 | 0.4925 | +0.075 | -0.069 | 0.0008 ± 0.0051 |
| thinner_sample <300 | 1477 | 0.5615 | 0.3947 | 0.4645 | +0.097 | -0.070 | 0.0091 ± 0.0046 |
| thinner_sample >=3000 | 733 | 0.5362 | 0.442 | 0.4679 | +0.068 | -0.026 | 0.0127 ± 0.0043 |
| data_status ADEQUATE | 1280 | 0.5387 | 0.4345 | 0.4516 | +0.087 | -0.017 | 0.012 ± 0.0035 |
| data_status LIMITED | 1003 | 0.5514 | 0.4172 | 0.4806 | +0.071 | -0.063 | 0.0045 ± 0.0047 |
| data_status POOR | 2114 | 0.5635 | 0.4019 | 0.4678 | +0.096 | -0.066 | 0.0079 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 642 | 0.2022 | 0.2031 | -0.0009 ± 0.0006 | 0.5855 | 0.5875 | 0.5027 | 0.4879 | 0.5234 | -0.071 ± 0.0188 | -0.01 (5) |
| 3-5 | 409 | 0.2048 | 0.2043 | +0.0005 ± 0.0018 | 0.593 | 0.5902 | 0.5029 | 0.4628 | 0.4743 | -0.100 ± 0.023 | 0.02 (1) |
| 5-10 | 909 | 0.2034 | 0.2028 | +0.0005 ± 0.0023 | 0.5936 | 0.5891 | 0.5117 | 0.4377 | 0.4664 | -0.091 ± 0.0155 | -0.0167 (6) |
| 10-15 | 760 | 0.2152 | 0.205 | +0.0102 ± 0.0041 | 0.621 | 0.5919 | 0.5305 | 0.4063 | 0.4263 | -0.107 ± 0.0164 | -0.048 (5) |
| 15-25 | 994 | 0.2247 | 0.2121 | +0.0126 ± 0.0057 | 0.644 | 0.6077 | 0.5787 | 0.3831 | 0.4487 | -0.095 ± 0.0145 | -0.0033 (9) |
| 25-40 | 568 | 0.2229 | 0.2096 | +0.0133 ± 0.0114 | 0.6356 | 0.6024 | 0.6599 | 0.3498 | 0.4806 | -0.075 ± 0.0176 | -0.01 (1) |
| 40+ | 115 | 0.2766 | 0.2018 | +0.0748 ± 0.0362 | 0.7584 | 0.5899 | 0.7572 | 0.3096 | 0.4522 | -0.071 ± 0.0357 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3316 | 0.1857 | 0.1866 | -0.0010 ± 0.0003 | 0.547 | 0.5481 | 0.493 | 0.478 | 0.5115 | -0.022 ± 0.0076 | -0.0129 (17) |
| 3-5 | 2196 | 0.1996 | 0.1984 | +0.0012 ± 0.0008 | 0.5804 | 0.575 | 0.4859 | 0.4459 | 0.4495 | -0.053 ± 0.0097 | 0.0 (2) |
| 5-10 | 4761 | 0.1985 | 0.1951 | +0.0033 ± 0.001 | 0.5809 | 0.5696 | 0.4823 | 0.4085 | 0.4222 | -0.047 ± 0.0065 | -0.0119 (21) |
| 10-15 | 4034 | 0.1981 | 0.1799 | +0.0182 ± 0.0017 | 0.5817 | 0.5308 | 0.4873 | 0.3628 | 0.3515 | -0.074 ± 0.0067 | -0.0281 (16) |
| 15-25 | 5058 | 0.2091 | 0.1695 | +0.0396 ± 0.0023 | 0.6119 | 0.5015 | 0.5064 | 0.31 | 0.3084 | -0.075 ± 0.0057 | -0.0025 (44) |
| 25-40 | 3984 | 0.2226 | 0.1286 | +0.0940 ± 0.0036 | 0.6393 | 0.3938 | 0.5317 | 0.2183 | 0.2287 | -0.059 ± 0.0055 | -0.01 (1) |
| 40+ | 2602 | 0.3801 | 0.0457 | +0.3344 ± 0.0047 | 0.9902 | 0.1752 | 0.633 | 0.1066 | 0.065 | -0.077 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 504 | 0.2079 | 0.2088 | -0.0009 ± 0.0007 | 0.5982 | 0.6001 | 0.5071 | 0.492 | 0.5198 | -0.099 ± 0.0219 | -0.01 (3) |
| 3-5 | 365 | 0.2256 | 0.223 | +0.0027 ± 0.002 | 0.6379 | 0.6324 | 0.516 | 0.4761 | 0.4575 | -0.128 ± 0.0264 | 0.02 (1) |
| 5-10 | 793 | 0.2064 | 0.2065 | -0.0001 ± 0.0024 | 0.5993 | 0.5986 | 0.5467 | 0.4718 | 0.5132 | -0.078 ± 0.0166 | -0.01 (4) |
| 10-15 | 726 | 0.2179 | 0.2097 | +0.0082 ± 0.0043 | 0.6255 | 0.6052 | 0.5655 | 0.4412 | 0.4725 | -0.113 ± 0.0177 | -0.04 (5) |
| 15-25 | 1018 | 0.2305 | 0.2103 | +0.0202 ± 0.0057 | 0.654 | 0.6033 | 0.5881 | 0.3922 | 0.443 | -0.103 ± 0.0147 | -0.0133 (9) |
| 25-40 | 716 | 0.2622 | 0.1976 | +0.0646 ± 0.0105 | 0.7312 | 0.5756 | 0.6537 | 0.3381 | 0.3953 | -0.114 ± 0.0163 | -0.0075 (4) |
| 40+ | 275 | 0.3561 | 0.1731 | +0.1830 ± 0.0248 | 0.9791 | 0.5171 | 0.733 | 0.249 | 0.3164 | -0.069 ± 0.024 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2824 | 0.1949 | 0.1952 | -0.0003 ± 0.0003 | 0.5667 | 0.5673 | 0.5113 | 0.4963 | 0.5113 | -0.043 ± 0.0086 | -0.0133 (15) |
| 3-5 | 1892 | 0.2002 | 0.1993 | +0.0009 ± 0.0008 | 0.5786 | 0.5761 | 0.5151 | 0.4752 | 0.4831 | -0.046 ± 0.0105 | 0.02 (1) |
| 5-10 | 4200 | 0.1964 | 0.1944 | +0.0019 ± 0.001 | 0.5776 | 0.5684 | 0.5102 | 0.4362 | 0.4629 | -0.034 ± 0.0069 | -0.0117 (6) |
| 10-15 | 3657 | 0.2022 | 0.1899 | +0.0123 ± 0.0018 | 0.5913 | 0.553 | 0.5134 | 0.3895 | 0.4025 | -0.056 ± 0.0073 | -0.0189 (18) |
| 15-25 | 5025 | 0.2164 | 0.178 | +0.0383 ± 0.0024 | 0.6282 | 0.5237 | 0.5253 | 0.3293 | 0.3335 | -0.070 ± 0.006 | -0.0086 (42) |
| 25-40 | 4647 | 0.2513 | 0.1366 | +0.1147 ± 0.0034 | 0.707 | 0.4198 | 0.5576 | 0.2404 | 0.2208 | -0.085 ± 0.0054 | -0.0044 (18) |
| 40+ | 3706 | 0.3935 | 0.0608 | +0.3328 ± 0.0046 | 1.0358 | 0.217 | 0.6506 | 0.1187 | 0.0847 | -0.071 ± 0.004 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 615 | 0.1998 | 0.2019 | -0.0021 ± 0.0006 | 0.5805 | 0.5856 | 0.5019 | 0.4866 | 0.5463 | -0.035 ± 0.0189 | -0.0137 (8) |
| 3-5 | 437 | 0.2037 | 0.202 | +0.0017 ± 0.0017 | 0.5908 | 0.5853 | 0.506 | 0.4663 | 0.4668 | -0.116 ± 0.0224 | 0.0067 (3) |
| 5-10 | 926 | 0.2025 | 0.199 | +0.0035 ± 0.0022 | 0.5917 | 0.5796 | 0.5079 | 0.4339 | 0.4449 | -0.105 ± 0.015 | -0.0071 (7) |
| 10-15 | 763 | 0.2097 | 0.206 | +0.0037 ± 0.0041 | 0.6087 | 0.5944 | 0.5404 | 0.4168 | 0.4653 | -0.085 ± 0.0163 | -0.0317 (6) |
| 15-25 | 943 | 0.2307 | 0.2121 | +0.0186 ± 0.0058 | 0.6592 | 0.6072 | 0.5898 | 0.3953 | 0.4443 | -0.110 ± 0.0149 | -0.03 (1) |
| 25-40 | 592 | 0.2135 | 0.2176 | -0.0040 ± 0.0112 | 0.6165 | 0.621 | 0.6706 | 0.3594 | 0.5186 | -0.055 ± 0.0172 | 0.015 (2) |
| 40+ | 121 | 0.2922 | 0.2133 | +0.0789 ± 0.0366 | 0.8066 | 0.6151 | 0.7677 | 0.3179 | 0.4628 | -0.070 ± 0.0386 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3245 | 0.1854 | 0.186 | -0.0005 ± 0.0003 | 0.5455 | 0.5463 | 0.4897 | 0.4745 | 0.4888 | -0.038 ± 0.0076 | -0.0163 (35) |
| 3-5 | 2201 | 0.1951 | 0.1931 | +0.0020 ± 0.0008 | 0.5727 | 0.5662 | 0.4871 | 0.4475 | 0.4425 | -0.064 ± 0.0096 | -0.0094 (18) |
| 5-10 | 4815 | 0.1959 | 0.1901 | +0.0058 ± 0.0009 | 0.5758 | 0.5568 | 0.4834 | 0.4095 | 0.4077 | -0.061 ± 0.0063 | -0.01 (31) |
| 10-15 | 3925 | 0.1923 | 0.177 | +0.0153 ± 0.0017 | 0.5684 | 0.5228 | 0.4999 | 0.3765 | 0.3758 | -0.065 ± 0.0067 | -0.015 (12) |
| 15-25 | 5243 | 0.2112 | 0.1722 | +0.0390 ± 0.0022 | 0.6169 | 0.5078 | 0.5157 | 0.3207 | 0.3185 | -0.073 ± 0.0057 | -0.03 (2) |
| 25-40 | 4000 | 0.2194 | 0.1326 | +0.0867 ± 0.0036 | 0.6331 | 0.4027 | 0.5378 | 0.2215 | 0.2442 | -0.050 ± 0.0055 | 0.01 (3) |
| 40+ | 2522 | 0.3949 | 0.0503 | +0.3446 ± 0.0051 | 1.032 | 0.1872 | 0.6453 | 0.1129 | 0.0694 | -0.080 ± 0.0043 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1003 | 0.1952 | 0.1954 | -0.0002 ± 0.0005 | 0.5697 | 0.5697 | 0.5029 | 0.4877 | 0.4955 | -0.057 ± 0.0141 | -0.0224 (49) |
| 3-5 | 699 | 0.1933 | 0.1924 | +0.0008 ± 0.0013 | 0.5642 | 0.561 | 0.4908 | 0.451 | 0.4578 | -0.061 ± 0.017 | -0.0194 (34) |
| 5-10 | 1450 | 0.2024 | 0.1963 | +0.0061 ± 0.0018 | 0.5942 | 0.5752 | 0.4966 | 0.4233 | 0.4193 | -0.074 ± 0.0118 | -0.005 (78) |
| 10-15 | 970 | 0.2111 | 0.1987 | +0.0123 ± 0.0036 | 0.6115 | 0.5796 | 0.5231 | 0.3999 | 0.4093 | -0.072 ± 0.0147 | 0.0014 (64) |
| 15-25 | 1298 | 0.2316 | 0.2103 | +0.0213 ± 0.005 | 0.6615 | 0.6052 | 0.5784 | 0.3836 | 0.4276 | -0.074 ± 0.0127 | -0.0214 (59) |
| 25-40 | 788 | 0.2476 | 0.2074 | +0.0402 ± 0.01 | 0.7034 | 0.5963 | 0.6741 | 0.3613 | 0.453 | -0.087 ± 0.0152 | -0.0219 (26) |
| 40+ | 261 | 0.3504 | 0.1992 | +0.1512 ± 0.0272 | 1.0121 | 0.5809 | 0.8084 | 0.326 | 0.4291 | -0.091 ± 0.0249 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3281 | 0.1833 | 0.1835 | -0.0002 ± 0.0003 | 0.5399 | 0.5395 | 0.5049 | 0.4896 | 0.5002 | -0.038 ± 0.0075 | -0.0157 (88) |
| 3-5 | 2278 | 0.1956 | 0.1937 | +0.0019 ± 0.0007 | 0.5702 | 0.5658 | 0.4971 | 0.4573 | 0.453 | -0.055 ± 0.0094 | -0.0209 (69) |
| 5-10 | 4515 | 0.1974 | 0.189 | +0.0084 ± 0.001 | 0.5806 | 0.556 | 0.4915 | 0.418 | 0.4007 | -0.072 ± 0.0065 | -0.0082 (132) |
| 10-15 | 3175 | 0.2073 | 0.1908 | +0.0165 ± 0.0019 | 0.6034 | 0.5602 | 0.53 | 0.4069 | 0.4006 | -0.068 ± 0.0078 | -0.0053 (105) |
| 15-25 | 3937 | 0.2302 | 0.1996 | +0.0305 ± 0.0028 | 0.6638 | 0.5785 | 0.5701 | 0.3746 | 0.3955 | -0.067 ± 0.0071 | -0.0253 (107) |
| 25-40 | 2718 | 0.2587 | 0.1843 | +0.0744 ± 0.0052 | 0.7332 | 0.5377 | 0.6329 | 0.3189 | 0.3598 | -0.077 ± 0.008 | -0.0229 (51) |
| 40+ | 1202 | 0.3775 | 0.1453 | +0.2322 ± 0.0116 | 1.0695 | 0.4373 | 0.7299 | 0.2264 | 0.2604 | -0.070 ± 0.0103 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4397 | 1.031 ± 0.042 | 1.118 | 0.1686 | 0.1635 | 0.2146 | 0.2063 |
| gen2 | 4397 | 0.835 ± 0.039 | 1.087 | 0.1681 | 0.1641 | 0.2341 | 0.206 |
| gen1_elo | 4397 | 1.004 ± 0.041 | 1.112 | 0.1756 | 0.1636 | 0.2135 | 0.2066 |
| gen1_sr | 4397 | 1.017 ± 0.051 | 1.16 | 0.1293 | 0.166 | 0.2302 | 0.2056 |
| gen1_ledger | 6469 | 0.86 ± 0.03 | 1.068 | 0.1836 | 0.1779 | 0.2189 | 0.2004 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 21,767)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,031 | 23.1% |
| STALE_QUOTE | market_freshness | 4,728 | 21.7% |
| BOOK_QUALITY | execution | 4,081 | 18.8% |
| POOR_DATA | data | 2,440 | 11.2% |
| LIMITED_DATA | data | 1,340 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,185 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,032 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 912 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 649 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 368 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 23.1%, market_freshness 21.7%, execution 18.8%, data 17.4%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 70.7%, THIN_PLAYER_HISTORY 59.6%, STALE_PLAYER_DATA 49.4%, STALE_KALSHI_QUOTE 44.4%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.4%, LEVEL_TRANSFER_RISK 11.0%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.7%, POST_SETTLEMENT_OBSERVATION 23.1%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,698)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,060 | 34.7% |
| STALE_QUOTE | market_freshness | 2,192 | 18.7% |
| BOOK_QUALITY | execution | 2,123 | 18.1% |
| POOR_DATA | data | 1,010 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 636 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 514 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 413 | 3.5% |
| LIMITED_DATA | data | 408 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 259 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 82 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.7%, market_freshness 18.7%, execution 18.1%, data 12.1%, market_freshness/coverage 9.0%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.1%, THIN_PLAYER_HISTORY 61.8%, STALE_KALSHI_QUOTE 52.5%, STALE_PLAYER_DATA 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.8%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.0%, PLAYER_IDENTITY_RISK 19.7%, MODEL_HIGH_UNCERTAINTY 18.4%, LEVEL_TRANSFER_RISK 9.6%, EVENT_MAPPING_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.8%, POST_SETTLEMENT_OBSERVATION 34.7%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9102, "IDENTITY_AMBIGUOUS": 2596}; ticker orientation: {"VERIFIED": 11698}.

Checks: discipline:AMBIGUOUS 780, discipline:PASS 10918, identity_confidence:AMBIGUOUS 2305, identity_confidence:PASS 9393, level_mapping:NA 792, level_mapping:PASS 10906, market_pair:AMBIGUOUS 408, market_pair:NA 295, market_pair:PASS 10995, model_complement:NA 262, model_complement:PASS 11436, namesake:AMBIGUOUS 6, namesake:PASS 11692, physical_match_id:NA 4074, physical_match_id:PASS 7624, player_ids:PASS 11698, same_pair_other_event:PASS 11698, ticker_orientation:PASS 11698

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,353 | 4.6% | 4.0% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 46, "data": 35, "execution": 23, "market_freshness/coverage": 15, "model_calibration": 14, "coverage": 13} | 5.91 | 0.2224 / 0.2181 (519) | 18.7% | 3.6% | 3.3% | 2.9% |
| CHALLENGER | 7,973 | 17.4% | 7.0% | 11.8% | {"coverage": 786, "market_freshness/coverage": 168, "market_freshness": 152, "data": 140, "model_calibration_or_unknown": 65, "execution": 31, "model_calibration": 28, "mapping": 15, "possible_market_error": 1} | 7.49 | 0.2203 / 0.2089 (1896) | 34.8% | 17.7% | 3.9% | 22.7% |
| DOUBLES | 1,668 | 46.8% | 46.4% | 6.7% | {"execution": 412, "mapping": 200, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.56 | 0.3096 / 0.2358 (432) | 14.0% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 14,633 | 25.5% | 17.7% | 31.9% | {"coverage": 1394, "execution": 709, "market_freshness": 634, "data": 490, "market_freshness/coverage": 322, "mapping": 173, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.89 | 0.2155 / 0.1974 (3278) | 37.5% | 69.9% | 19.8% | 22.3% |
| ITF_WOMEN | 19,200 | 27.3% | 19.9% | 44.9% | {"coverage": 1835, "market_freshness": 1148, "execution": 907, "data": 719, "market_freshness/coverage": 440, "mapping": 120, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.9 | 0.2038 / 0.1949 (3716) | 40.0% | 55.9% | 10.0% | 22.3% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,020 | 5.7% | 5.1% | 1.5% | {"market_freshness": 59, "model_calibration_or_unknown": 36, "execution": 26, "model_calibration": 16, "coverage": 12, "data": 11, "market_freshness/coverage": 10, "mapping": 1} | 7.64 | 0.2353 / 0.2301 (495) | 24.8% | 1.4% | 1.8% | 3.5% |
| WTA125 | 1,396 | 12.5% | 9.9% | 1.5% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 10, "mapping": 4} | 9.14 | 0.219 / 0.2065 (488) | 22.9% | 7.5% | 5.3% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
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
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 739 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 50 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9684, "by_level_share_of_ge_25pp": {"ATP": 0.017, "CHALLENGER": 0.1185, "DOUBLES": 0.0667, "ITF_MEN": 0.3185, "ITF_WOMEN": 0.4487, "OTHER": 0.001, "WTA": 0.0146, "WTA125": 0.015}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5252, "share_primary_cause_market_settled_or_in_play": 0.4368, "share_primary_cause_stale_quote_only": 0.1874}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11698, "identity_ambiguous_share": 0.2219, "ticker_orientation": {"VERIFIED": 11698}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7624, "with_external": 380, "coverage": 0.0498, "external_status": {"EXTERNAL_STALE": 229, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 229, "MODEL_LONE_OUTLIER": 142, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3737, "share_external_supports_model": 0.0237}, "pregame_clean_ge_25pp": {"n": 3697, "with_external": 357, "coverage": 0.0966, "external_status": {"EXTERNAL_STALE": 213, "AGREES_WITH_KALSHI": 135, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 213, "MODEL_LONE_OUTLIER": 135, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3782, "share_external_supports_model": 0.0252}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 495.0, "median_sample_ratio": 2.43, "median_min_matches": 21.0, "median_max_days_since_last": 226.0, "share_severe_asymmetry": 0.2146, "data_status": {"POOR": 6501, "LIMITED": 3051, "ADEQUATE": 2146}, "comparison_lt_10pp": {"median_thinner_serve_points": 1723.0, "median_sample_ratio": 1.69, "median_min_matches": 96.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 864, "model_minus_observed": 0.0503, "kalshi_minus_observed": -0.0883, "brier_diff_model_minus_kalshi": -0.0037}, "4-10x": {"n": 593, "model_minus_observed": 0.0931, "kalshi_minus_observed": -0.0534, "brier_diff_model_minus_kalshi": 0.0115}, "<2x": {"n": 2147, "model_minus_observed": 0.093, "kalshi_minus_observed": -0.0298, "brier_diff_model_minus_kalshi": 0.0128}, ">=10x": {"n": 793, "model_minus_observed": 0.109, "kalshi_minus_observed": -0.0666, "brier_diff_model_minus_kalshi": 0.007}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4397, "model": {"intercept": -0.536, "slope": 0.835, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.212, "slope": 1.087, "slope_se": 0.044}, "mean_extremity_model": 0.1681, "mean_extremity_kalshi": 0.1641, "model_brier": 0.2341, "kalshi_brier": 0.206, "brier_diff_model_minus_kalshi": 0.0281, "brier_diff_se": 0.0029, "model_logloss": 0.6646, "kalshi_logloss": 0.5949}, "fair_v1": {"n": 4397, "model": {"intercept": -0.422, "slope": 1.031, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.285, "slope": 1.118, "slope_se": 0.044}, "mean_extremity_model": 0.1686, "mean_extremity_kalshi": 0.1635, "model_brier": 0.2146, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0083, "brier_diff_se": 0.0024, "model_logloss": 0.6182, "kalshi_logloss": 0.5954}, "gen1_elo": {"n": 4397, "model": {"intercept": -0.398, "slope": 1.004, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.305, "slope": 1.112, "slope_se": 0.044}, "mean_extremity_model": 0.1756, "mean_extremity_kalshi": 0.1636, "model_brier": 0.2135, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": 0.0069, "brier_diff_se": 0.0024, "model_logloss": 0.6167, "kalshi_logloss": 0.596}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2503, "share_ge_15": 0.4469, "median_abs_gap": 13.19, "n": 30455}, "gen1_elo": {"share_ge_25": 0.2472, "share_ge_15": 0.446, "median_abs_gap": 13.02, "n": 30455}, "gen1_sr": {"share_ge_25": 0.3177, "share_ge_15": 0.5258, "median_abs_gap": 16.04, "n": 30455}, "gen2": {"share_ge_25": 0.321, "share_ge_15": 0.5153, "median_abs_gap": 15.65, "n": 30455}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1567, "share_ge_15": 0.3622, "median_abs_gap": 10.95, "n": 23594}, "gen1_elo": {"share_ge_25": 0.1571, "share_ge_15": 0.36, "median_abs_gap": 10.76, "n": 23591}, "gen1_sr": {"share_ge_25": 0.223, "share_ge_15": 0.4473, "median_abs_gap": 13.14, "n": 23595}, "gen2": {"share_ge_25": 0.2392, "share_ge_15": 0.4463, "median_abs_gap": 13.1, "n": 23596}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.91, "share_ge_25_all": 0.0457, "share_ge_25_pregame_clean": 0.0404}, "WTA": {"median_abs_gap_pregame_clean": 7.64, "share_ge_25_all": 0.0566, "share_ge_25_pregame_clean": 0.0511}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2337, "share_within_10pp_all": 0.4313, "share_within_10pp_pregame_clean": 0.4847, "corr_model_vs_mid_pregame_clean": 0.8429}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 642, "model_brier": 0.2022, "kalshi_brier": 0.2031, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 760, "model_brier": 0.2152, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0102}, "15-25": {"n_settled": 994, "model_brier": 0.2247, "kalshi_brier": 0.2121, "brier_diff_model_minus_kalshi": 0.0126}, "25-40": {"n_settled": 568, "model_brier": 0.2229, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.0133}, "3-5": {"n_settled": 409, "model_brier": 0.2048, "kalshi_brier": 0.2043, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 115, "model_brier": 0.2766, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0748}, "5-10": {"n_settled": 909, "model_brier": 0.2034, "kalshi_brier": 0.2028, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.536, "slope": 0.835, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.212, "slope": 1.087, "slope_se": 0.044}, "n": 4397}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.509, "slope": 0.86, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.15, "slope": 1.068, "slope_se": 0.034}, "n": 6469}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 432, "model_brier": 0.3096, "kalshi_brier": 0.2358, "brier_diff_model_minus_kalshi": 0.0738, "brier_diff_se": 0.0146, "corr_model_outcome": 0.0434, "corr_kalshi_outcome": 0.2537}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
