# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-25T06:49Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 53,154): 0-3 14.0%, 3-5 9.5%, 5-10 19.8%, 10-15 15.4%, 15-25 19.2%, 25-40 14.0%, 40+ 8.2%; median gap 12.08 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.4%, Challenger 11.8%, doubles 6.9%). Main tour: ATP 4.5% and WTA 5.5% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,809): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.4%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.4%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.4%, market_freshness 18.7%, execution 18.4%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.3% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,809 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.2% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.5 points vs 1754.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.03, Gen-2 0.835, Gen-1 ledger 0.857 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 573 model 0.2225 vs Kalshi 0.2104; n 115 model 0.2766 vs Kalshi 0.2018.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 231,025 model-market comparisons (375,083 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 77,998 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-25T06:34:46.099015+00:00'], shadow board 61,268 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-25T06:34:49.636619+00:00'], Model 4 29,047 rows, 20,221 settled tickers, 7,211 tickers with an external scan.
* By model: {"gen1_ledger": 53258, "gen1_elo": 30809, "fair_v1": 30809, "gen2": 30809, "gen1_sr": 30809, "model4_fundamental": 27283, "model4_conditioned": 27248}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 53,154 | 14.0 | 9.5 | 19.8 | 15.4 | 19.2 | 14.0 | 8.2 | 12.08 | 41.4% | 22.2% |
| MW fair_v1 | 30,809 | 12.9 | 8.5 | 18.5 | 15.6 | 19.7 | 15.0 | 9.9 | 13.14 | 44.6% | 24.9% |
| MW gen1_elo | 30,809 | 12.7 | 8.5 | 19.0 | 15.2 | 19.9 | 14.9 | 9.6 | 13.0 | 44.5% | 24.6% |
| MW gen1_ledger | 22,345 | 15.5 | 10.8 | 21.6 | 15.1 | 18.5 | 12.7 | 5.9 | 10.53 | 37.1% | 18.6% |
| MW gen1_sr | 30,809 | 10.2 | 7.1 | 16.7 | 13.6 | 20.8 | 18.7 | 12.9 | 16.0 | 52.4% | 31.6% |
| MW gen2 | 30,809 | 11.0 | 7.3 | 16.2 | 14.0 | 19.4 | 17.9 | 14.1 | 15.59 | 51.4% | 32.0% |
| all families model4_conditioned | 27,248 | 21.8 | 18.8 | 34.7 | 17.6 | 4.5 | 1.6 | 1.1 | 6.0 | 7.1% | 2.6% |
| all families model4_fundamental | 27,283 | 16.8 | 13.3 | 34.1 | 20.5 | 10.5 | 3.5 | 1.3 | 7.78 | 15.4% | 4.8% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.8%, >=15pp 41.4%, >=20pp 30.8%, >=25pp 22.2%, >=30pp 16.1%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.42pp; >=10pp 45.2%, >=25pp 17.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,761 | 28.0 | 14.2 | 25.2 | 15.4 | 11.8 | 4.6 | 0.7 | 6.17 | 17.1% | 5.3% |
| CHALLENGER | 4,814 | 15.8 | 10.0 | 20.3 | 15.8 | 15.0 | 12.3 | 10.9 | 11.06 | 38.2% | 23.2% |
| ITF_MEN | 8,460 | 10.1 | 7.3 | 16.8 | 14.7 | 21.6 | 17.5 | 12.2 | 15.45 | 51.2% | 29.7% |
| ITF_WOMEN | 12,125 | 9.5 | 6.9 | 15.9 | 15.3 | 22.3 | 18.2 | 12.0 | 15.78 | 52.4% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,964 | 17.5 | 13.1 | 26.4 | 19.0 | 17.5 | 5.9 | 0.7 | 8.25 | 24.0% | 6.5% |
| WTA125 | 679 | 13.0 | 7.2 | 22.8 | 20.8 | 20.8 | 13.4 | 2.1 | 11.47 | 36.2% | 15.5% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,761 | 23.9 | 15.0 | 25.0 | 17.8 | 12.8 | 4.6 | 0.9 | 6.7 | 18.3% | 5.5% |
| CHALLENGER | 4,814 | 14.9 | 8.8 | 18.3 | 14.6 | 17.8 | 13.9 | 11.7 | 12.54 | 43.3% | 25.5% |
| ITF_MEN | 8,460 | 8.1 | 5.9 | 14.4 | 13.0 | 19.7 | 21.1 | 17.8 | 18.76 | 58.6% | 38.9% |
| ITF_WOMEN | 12,125 | 8.2 | 5.6 | 13.7 | 13.2 | 20.5 | 21.0 | 17.7 | 19.14 | 59.3% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,964 | 14.3 | 10.2 | 22.4 | 16.0 | 22.6 | 13.3 | 1.3 | 10.87 | 37.2% | 14.6% |
| WTA125 | 679 | 6.6 | 4.7 | 16.8 | 17.5 | 25.9 | 19.6 | 8.8 | 17.0 | 54.3% | 28.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,761 | 23.5 | 12.6 | 24.2 | 16.4 | 15.2 | 6.9 | 1.3 | 7.5 | 23.4% | 8.2% |
| CHALLENGER | 4,814 | 14.4 | 9.2 | 20.7 | 15.6 | 16.2 | 13.0 | 11.0 | 11.47 | 40.2% | 24.0% |
| ITF_MEN | 8,460 | 9.7 | 7.3 | 16.8 | 13.8 | 22.2 | 17.9 | 12.3 | 15.94 | 52.4% | 30.2% |
| ITF_WOMEN | 12,125 | 9.4 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.1 | 15.58 | 51.9% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 1,964 | 23.8 | 17.4 | 30.6 | 15.1 | 10.0 | 2.6 | 0.6 | 6.02 | 13.1% | 3.2% |
| WTA125 | 679 | 22.4 | 11.8 | 28.6 | 15.9 | 14.7 | 6.2 | 0.4 | 7.78 | 21.3% | 6.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,728 | 25.1 | 19.2 | 30.0 | 13.0 | 9.5 | 3.0 | 0.3 | 5.67 | 12.8% | 3.3% |
| CHALLENGER | 3,334 | 21.4 | 14.3 | 26.5 | 14.7 | 14.6 | 6.6 | 1.8 | 7.34 | 23.0% | 8.4% |
| DOUBLES | 1,728 | 5.2 | 4.6 | 12.2 | 10.4 | 20.4 | 26.0 | 21.2 | 23.85 | 67.6% | 47.2% |
| ITF_MEN | 6,265 | 13.7 | 9.2 | 19.9 | 16.2 | 21.3 | 13.3 | 6.5 | 12.16 | 41.1% | 19.8% |
| ITF_WOMEN | 7,239 | 12.6 | 8.9 | 19.3 | 15.2 | 21.6 | 16.2 | 6.2 | 12.87 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,144 | 22.8 | 15.8 | 30.2 | 17.9 | 9.5 | 3.4 | 0.3 | 6.82 | 13.3% | 3.8% |
| WTA125 | 758 | 21.1 | 13.6 | 21.8 | 18.3 | 14.6 | 8.3 | 2.2 | 8.3 | 25.2% | 10.5% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,686 | 28.3 | 14.4 | 25.7 | 15.3 | 11.7 | 4.2 | 0.5 | 6.04 | 16.3% | 4.6% |
| CHALLENGER | 3,413 | 20.6 | 12.4 | 24.9 | 18.2 | 15.3 | 6.8 | 1.8 | 8.41 | 23.8% | 8.6% |
| ITF_MEN | 6,200 | 12.2 | 8.8 | 20.2 | 16.6 | 22.7 | 14.4 | 5.1 | 12.57 | 42.2% | 19.5% |
| ITF_WOMEN | 9,067 | 11.2 | 8.2 | 18.1 | 17.3 | 24.2 | 15.3 | 5.5 | 13.52 | 45.1% | 20.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,908 | 17.7 | 13.0 | 26.4 | 19.2 | 17.4 | 5.5 | 0.7 | 8.23 | 23.6% | 6.2% |
| WTA125 | 653 | 13.3 | 7.0 | 22.4 | 21.1 | 21.4 | 13.0 | 1.7 | 11.51 | 36.1% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,686 | 24.2 | 15.3 | 25.2 | 17.7 | 12.8 | 4.2 | 0.6 | 6.5 | 17.6% | 4.8% |
| CHALLENGER | 3,413 | 18.9 | 11.3 | 22.7 | 17.4 | 18.2 | 9.5 | 2.0 | 9.31 | 29.8% | 11.5% |
| ITF_MEN | 6,201 | 9.7 | 7.1 | 16.8 | 15.0 | 21.6 | 19.3 | 10.5 | 15.48 | 51.4% | 29.8% |
| ITF_WOMEN | 9,068 | 9.3 | 6.5 | 15.2 | 14.6 | 22.5 | 20.5 | 11.3 | 16.7 | 54.4% | 31.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,908 | 14.4 | 10.2 | 22.4 | 16.0 | 22.6 | 13.1 | 1.3 | 10.87 | 37.0% | 14.4% |
| WTA125 | 653 | 6.4 | 4.9 | 16.9 | 17.9 | 25.9 | 20.1 | 8.0 | 16.74 | 53.9% | 28.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,678 | 25.2 | 19.5 | 30.0 | 13.1 | 9.1 | 2.9 | 0.2 | 5.62 | 12.2% | 3.0% |
| CHALLENGER | 2,921 | 22.8 | 15.3 | 28.0 | 14.7 | 14.0 | 4.6 | 0.5 | 6.84 | 19.1% | 5.1% |
| DOUBLES | 1,609 | 5.2 | 4.8 | 12.5 | 10.5 | 20.3 | 25.9 | 20.9 | 23.62 | 67.1% | 46.8% |
| ITF_MEN | 5,260 | 14.8 | 9.8 | 21.5 | 17.0 | 21.3 | 11.6 | 4.0 | 11.2 | 36.8% | 15.6% |
| ITF_WOMEN | 6,007 | 13.5 | 9.4 | 20.7 | 16.0 | 21.8 | 14.9 | 3.6 | 11.77 | 40.3% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,094 | 23.3 | 16.3 | 30.2 | 17.9 | 9.5 | 2.7 | 0.1 | 6.7 | 12.3% | 2.8% |
| WTA125 | 647 | 23.0 | 15.0 | 23.2 | 19.8 | 13.0 | 5.4 | 0.6 | 7.42 | 19.0% | 6.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,728 | 5.2 | 4.6 | 12.2 | 10.4 | 20.4 | 26.0 | 21.2 | 23.85 | 67.6% | 47.2% |
| singles | 20,617 | 16.3 | 11.3 | 22.4 | 15.5 | 18.4 | 11.6 | 4.6 | 10.0 | 34.5% | 16.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 8 | 12.5 | 25.0 | 50.0 | 0.0 | 12.5 | 0.0 | 0.0 | 6.23 | 12.5% | 0.0% |
| Clay | 6,767 | 12.9 | 9.0 | 19.2 | 15.7 | 18.8 | 14.4 | 9.9 | 12.8 | 43.1% | 24.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 19,167 | 13.4 | 8.6 | 18.6 | 15.2 | 19.7 | 14.8 | 9.7 | 13.04 | 44.2% | 24.5% |
| UNKNOWN | 4,630 | 10.7 | 7.5 | 17.0 | 16.9 | 20.6 | 16.4 | 11.1 | 14.13 | 48.0% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,819 | 19.6 | 11.9 | 21.6 | 16.5 | 15.0 | 9.2 | 6.2 | 9.09 | 30.4% | 15.5% |
| B | 3,822 | 12.4 | 8.7 | 19.5 | 16.3 | 19.4 | 12.7 | 11.0 | 12.7 | 43.1% | 23.8% |
| C | 4,300 | 11.6 | 8.8 | 19.7 | 15.3 | 19.4 | 14.6 | 10.6 | 13.14 | 44.6% | 25.3% |
| D | 4,748 | 12.1 | 7.7 | 17.4 | 15.5 | 21.5 | 15.7 | 10.1 | 13.98 | 47.4% | 25.8% |
| F | 9,120 | 7.6 | 5.5 | 15.0 | 14.6 | 23.6 | 21.2 | 12.5 | 17.79 | 57.3% | 33.8% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,412 | 23.2 | 15.8 | 28.9 | 15.2 | 11.5 | 4.0 | 1.4 | 6.67 | 16.9% | 5.4% |
| B | 3,033 | 16.1 | 10.4 | 23.1 | 16.2 | 19.7 | 10.6 | 3.8 | 10.06 | 34.1% | 14.4% |
| C | 4,395 | 11.0 | 7.3 | 18.4 | 14.4 | 21.2 | 16.8 | 10.8 | 14.4 | 48.9% | 27.6% |
| D | 3,062 | 14.4 | 9.7 | 19.9 | 14.6 | 21.0 | 14.3 | 6.0 | 12.04 | 41.3% | 20.3% |
| F | 5,443 | 10.2 | 8.3 | 15.7 | 15.1 | 22.6 | 19.8 | 8.2 | 15.33 | 50.6% | 28.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,079 | 17.8 | 10.7 | 20.9 | 16.2 | 15.6 | 10.1 | 8.8 | 10.15 | 34.4% | 18.9% |
| LIMITED | 6,521 | 13.4 | 10.1 | 20.2 | 15.9 | 19.3 | 13.4 | 7.7 | 11.96 | 40.4% | 21.1% |
| POOR | 14,209 | 9.1 | 6.3 | 16.0 | 15.0 | 22.8 | 19.2 | 11.7 | 16.25 | 53.6% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,540 | 25.1 | 19.0 | 33.7 | 13.9 | 5.9 | 2.2 | 0.2 | 5.61 | 8.4% | 2.5% |
| GAME_SPREAD | 4,965 | 22.3 | 15.3 | 33.3 | 17.1 | 9.2 | 2.5 | 0.3 | 6.73 | 12.0% | 2.8% |
| MATCH_WINNER | 22,345 | 15.5 | 10.8 | 21.6 | 15.1 | 18.5 | 12.7 | 5.9 | 10.53 | 37.1% | 18.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 11,452 | 28.3 | 16.6 | 31.1 | 12.6 | 8.8 | 2.3 | 0.3 | 5.61 | 11.4% | 2.7% |
| TOTAL_GAMES | 7,932 | 9.1 | 9.9 | 36.4 | 28.1 | 10.3 | 3.4 | 2.9 | 9.39 | 16.6% | 6.3% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,759 | 24.9 | 32.4 | 32.6 | 5.6 | 3.5 | 0.8 | 0.2 | 4.55 | 4.5% | 1.0% |
| GAME_SPREAD | 6,431 | 45.7 | 16.8 | 26.7 | 7.9 | 1.7 | 0.9 | 0.3 | 3.46 | 2.9% | 1.2% |
| TOTAL_GAMES | 11,058 | 5.1 | 7.9 | 41.2 | 33.9 | 7.0 | 2.6 | 2.3 | 9.54 | 11.9% | 4.9% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,770 | 23.8 | 17.3 | 35.3 | 13.3 | 7.3 | 2.6 | 0.4 | 5.95 | 10.3% | 3.0% |
| GAME_SPREAD | 6,434 | 19.8 | 13.2 | 27.9 | 20.7 | 13.2 | 4.3 | 0.9 | 7.96 | 18.4% | 5.2% |
| TOTAL_GAMES | 11,079 | 8.8 | 9.8 | 36.6 | 26.7 | 11.9 | 3.8 | 2.5 | 9.41 | 18.1% | 6.3% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 30,809 | 44.6% | 24.9% | 13.14 | 36.1% | 15.6% | 10.94 |
| gen1_elo | 30,809 | 44.5% | 24.6% | 13.0 | 35.9% | 15.7% | 10.74 |
| gen1_sr | 30,809 | 52.4% | 31.6% | 16.0 | 44.6% | 22.3% | 13.1 |
| gen2 | 30,809 | 51.4% | 32.0% | 15.59 | 44.6% | 23.9% | 13.07 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,608 | 15.7 | 10.4 | 21.4 | 17.3 | 20.1 | 11.9 | 3.3 | 10.71 | 35.3% | 15.2% |
| STALE | 15,201 | 10.0 | 6.6 | 15.5 | 13.8 | 19.2 | 18.1 | 16.7 | 16.99 | 54.1% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 15,813 | 16.4 | 11.3 | 22.4 | 15.2 | 17.7 | 12.1 | 4.9 | 9.99 | 34.7% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 53,154 | 15813 | 19080 | 18261 | 24.2 | 142.3 | 1400.4 |
| ge_15pp | 22,016 | 5489 | 6799 | 9728 | 26.3 | 440.2 | 1380.4 |
| ge_25pp | 11,809 | 2684 | 2957 | 6168 | 32.3 | 584.7 | 1380.4 |
| lt_10pp | 22,969 | 7916 | 9030 | 6023 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261025T064904Z-689e4798`: 862 priced rows, quote age at build {'median': 14.9, 'max': 15.0}, freshness {'AGING': 862}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 25 | 0.0 | 0.0 | 24.0 | 8.0 | 36.0 | 32.0 | 0.0 | 20.47 | 68.0% | 32.0% |
| EXTERNAL_LONE_OUTLIER | 16 | 75.0 | 25.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,983 | 19.1 | 11.3 | 24.9 | 18.9 | 18.2 | 7.0 | 0.6 | 8.87 | 25.9% | 7.7% |
| KALSHI_LONE_OUTLIER | 18 | 5.6 | 5.6 | 72.2 | 5.6 | 5.6 | 5.6 | 0.0 | 6.16 | 11.1% | 5.6% |
| MARKETS_AGREE | 601 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,291 | 0.0 | 2.4 | 35.9 | 26.0 | 24.3 | 10.6 | 0.7 | 11.99 | 35.6% | 11.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 30,809 | 4934 (16.0%) | 26.2% | 0.9% | {"EXTERNAL_STALE": 2983, "AGREES_WITH_KALSHI": 1291, "ALL_AGREE": 601, "SUPPORTS_MODEL_DIRECTION": 24, "AGREES_WITH_MODEL": 18, "EXTERNAL_OUTLIER": 16, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,728 | 1250 (9.1%) | 36.8% | 1.5% | {"EXTERNAL_STALE": 771, "AGREES_WITH_KALSHI": 460, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,663 | 384 (5.0%) | 38.0% | 2.3% | {"EXTERNAL_STALE": 229, "AGREES_WITH_KALSHI": 146, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,730 | 361 (9.7%) | 38.5% | 2.5% | {"EXTERNAL_STALE": 213, "AGREES_WITH_KALSHI": 139, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,284 | 2781 (22.6%) | 17.8% | 0.7% | {"EXTERNAL_STALE": 1648, "ALL_AGREE": 601, "AGREES_WITH_KALSHI": 495, "EXTERNAL_OUTLIER": 16, "AGREES_WITH_MODEL": 15, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,871 | 10.3 | 7.6 | 19.5 | 14.4 | 22.2 | 16.0 | 10.0 | 14.09 | 48.2% | 26.0% |
| 4-10x | 3,991 | 11.0 | 8.2 | 19.0 | 15.4 | 21.4 | 14.8 | 10.1 | 13.75 | 46.3% | 24.9% |
| <2x | 15,670 | 15.0 | 9.7 | 19.1 | 16.5 | 17.5 | 13.1 | 9.1 | 11.83 | 39.7% | 22.2% |
| >=10x | 5,277 | 10.8 | 6.2 | 15.2 | 14.3 | 22.0 | 19.6 | 12.0 | 16.43 | 53.6% | 31.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,893 | 12.6 | 8.6 | 19.3 | 16.1 | 19.0 | 13.8 | 10.7 | 12.94 | 43.5% | 24.5% |
| 300-1000 | 6,514 | 11.6 | 8.6 | 17.3 | 15.3 | 20.6 | 16.3 | 10.2 | 13.92 | 47.1% | 26.5% |
| <300 | 10,042 | 8.5 | 5.6 | 15.5 | 14.8 | 23.2 | 20.1 | 12.4 | 17.01 | 55.6% | 32.5% |
| >=3000 | 6,360 | 21.3 | 13.0 | 23.4 | 16.5 | 14.1 | 7.0 | 4.7 | 7.94 | 25.8% | 11.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 872 | 0.5508 | 0.4122 | 0.5023 | +0.049 | -0.090 | -0.0046 ± 0.0052 |
| ratio 4-10x | 595 | 0.5883 | 0.4418 | 0.4958 | +0.092 | -0.054 | 0.0111 ± 0.0066 |
| ratio <2x | 2157 | 0.5385 | 0.4155 | 0.446 | +0.092 | -0.030 | 0.0124 ± 0.0031 |
| ratio >=10x | 796 | 0.5717 | 0.3962 | 0.4611 | +0.111 | -0.065 | 0.0076 ± 0.0065 |
| thinner_sample 1000-3000 | 1198 | 0.5432 | 0.4161 | 0.4474 | +0.096 | -0.031 | 0.0101 ± 0.0041 |
| thinner_sample 300-1000 | 1000 | 0.5672 | 0.4232 | 0.494 | +0.073 | -0.071 | 0.0001 ± 0.0051 |
| thinner_sample <300 | 1484 | 0.5617 | 0.395 | 0.4629 | +0.099 | -0.068 | 0.0096 ± 0.0046 |
| thinner_sample >=3000 | 738 | 0.5358 | 0.4418 | 0.4675 | +0.068 | -0.026 | 0.0124 ± 0.0043 |
| data_status ADEQUATE | 1287 | 0.5384 | 0.4344 | 0.4522 | +0.086 | -0.018 | 0.0118 ± 0.0034 |
| data_status LIMITED | 1008 | 0.552 | 0.4174 | 0.4821 | +0.070 | -0.065 | 0.0038 ± 0.0047 |
| data_status POOR | 2125 | 0.5636 | 0.4019 | 0.4678 | +0.096 | -0.066 | 0.0078 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 646 | 0.2024 | 0.2032 | -0.0009 ± 0.0006 | 0.5858 | 0.5877 | 0.503 | 0.4882 | 0.5232 | -0.071 ± 0.0187 | -0.01 (5) |
| 3-5 | 410 | 0.205 | 0.2044 | +0.0006 ± 0.0018 | 0.5934 | 0.5905 | 0.503 | 0.4629 | 0.4732 | -0.102 ± 0.023 | 0.02 (1) |
| 5-10 | 914 | 0.2033 | 0.2025 | +0.0008 ± 0.0022 | 0.5934 | 0.5885 | 0.5116 | 0.4376 | 0.465 | -0.093 ± 0.0155 | -0.0167 (6) |
| 10-15 | 763 | 0.2151 | 0.2054 | +0.0097 ± 0.0041 | 0.6208 | 0.5926 | 0.5307 | 0.4065 | 0.4286 | -0.104 ± 0.0164 | -0.048 (5) |
| 15-25 | 999 | 0.2252 | 0.213 | +0.0122 ± 0.0057 | 0.6451 | 0.6102 | 0.5783 | 0.3826 | 0.4494 | -0.094 ± 0.0146 | -0.0033 (9) |
| 25-40 | 573 | 0.2225 | 0.2104 | +0.0121 ± 0.0114 | 0.6346 | 0.6042 | 0.6606 | 0.3506 | 0.4834 | -0.072 ± 0.0175 | -0.01 (1) |
| 40+ | 115 | 0.2766 | 0.2018 | +0.0748 ± 0.0362 | 0.7584 | 0.5899 | 0.7572 | 0.3096 | 0.4522 | -0.071 ± 0.0357 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3330 | 0.1858 | 0.1868 | -0.0010 ± 0.0003 | 0.5474 | 0.5486 | 0.4928 | 0.4778 | 0.5117 | -0.021 ± 0.0076 | -0.0129 (17) |
| 3-5 | 2198 | 0.1996 | 0.1984 | +0.0013 ± 0.0008 | 0.5803 | 0.5749 | 0.4858 | 0.4458 | 0.449 | -0.053 ± 0.0097 | 0.0 (2) |
| 5-10 | 4775 | 0.1983 | 0.1951 | +0.0033 ± 0.001 | 0.5807 | 0.5695 | 0.4823 | 0.4085 | 0.4224 | -0.047 ± 0.0065 | -0.0119 (21) |
| 10-15 | 4052 | 0.1982 | 0.1804 | +0.0178 ± 0.0017 | 0.582 | 0.5319 | 0.4877 | 0.3633 | 0.3534 | -0.073 ± 0.0067 | -0.0281 (16) |
| 15-25 | 5078 | 0.2093 | 0.1698 | +0.0394 ± 0.0023 | 0.6123 | 0.5024 | 0.5061 | 0.3098 | 0.3086 | -0.075 ± 0.0057 | -0.0025 (44) |
| 25-40 | 4000 | 0.2225 | 0.1289 | +0.0936 ± 0.0036 | 0.639 | 0.3947 | 0.5325 | 0.2192 | 0.2303 | -0.059 ± 0.0055 | -0.01 (1) |
| 40+ | 2607 | 0.3802 | 0.0457 | +0.3345 ± 0.0047 | 0.9905 | 0.1752 | 0.6331 | 0.1067 | 0.0648 | -0.077 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 508 | 0.2085 | 0.2093 | -0.0008 ± 0.0007 | 0.5995 | 0.6013 | 0.507 | 0.4919 | 0.5197 | -0.099 ± 0.0218 | -0.01 (3) |
| 3-5 | 367 | 0.2259 | 0.223 | +0.0029 ± 0.002 | 0.6384 | 0.6325 | 0.516 | 0.4761 | 0.455 | -0.132 ± 0.0263 | 0.02 (1) |
| 5-10 | 797 | 0.2066 | 0.2063 | +0.0002 ± 0.0024 | 0.5996 | 0.5981 | 0.5463 | 0.4714 | 0.5107 | -0.080 ± 0.0166 | -0.01 (4) |
| 10-15 | 731 | 0.2177 | 0.21 | +0.0077 ± 0.0042 | 0.6251 | 0.6058 | 0.5646 | 0.4403 | 0.4733 | -0.111 ± 0.0177 | -0.04 (5) |
| 15-25 | 1023 | 0.2305 | 0.2106 | +0.0199 ± 0.0056 | 0.6541 | 0.604 | 0.588 | 0.3922 | 0.4438 | -0.102 ± 0.0146 | -0.0133 (9) |
| 25-40 | 718 | 0.2621 | 0.1986 | +0.0635 ± 0.0105 | 0.7309 | 0.5784 | 0.6534 | 0.338 | 0.3969 | -0.112 ± 0.0163 | -0.0075 (4) |
| 40+ | 276 | 0.3548 | 0.1732 | +0.1816 ± 0.0247 | 0.9757 | 0.5174 | 0.7339 | 0.2501 | 0.3188 | -0.068 ± 0.024 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2836 | 0.1953 | 0.1956 | -0.0003 ± 0.0003 | 0.5676 | 0.5682 | 0.5112 | 0.4962 | 0.512 | -0.043 ± 0.0086 | -0.0133 (15) |
| 3-5 | 1896 | 0.2005 | 0.1996 | +0.0009 ± 0.0008 | 0.5793 | 0.5768 | 0.5149 | 0.475 | 0.4831 | -0.046 ± 0.0105 | 0.02 (1) |
| 5-10 | 4216 | 0.1964 | 0.1944 | +0.0020 ± 0.001 | 0.5777 | 0.5683 | 0.5104 | 0.4363 | 0.4625 | -0.034 ± 0.0069 | -0.0117 (6) |
| 10-15 | 3674 | 0.2022 | 0.1899 | +0.0123 ± 0.0018 | 0.5913 | 0.5531 | 0.513 | 0.3891 | 0.4023 | -0.056 ± 0.0073 | -0.0189 (18) |
| 15-25 | 5049 | 0.2164 | 0.1783 | +0.0381 ± 0.0023 | 0.6282 | 0.5245 | 0.5254 | 0.3294 | 0.3343 | -0.069 ± 0.006 | -0.0086 (42) |
| 25-40 | 4656 | 0.2513 | 0.1368 | +0.1145 ± 0.0034 | 0.707 | 0.4203 | 0.5577 | 0.2405 | 0.2212 | -0.085 ± 0.0054 | -0.0044 (18) |
| 40+ | 3713 | 0.3931 | 0.0609 | +0.3322 ± 0.0046 | 1.0347 | 0.2174 | 0.6509 | 0.1191 | 0.0856 | -0.071 ± 0.004 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 617 | 0.1999 | 0.202 | -0.0021 ± 0.0006 | 0.5807 | 0.5859 | 0.5019 | 0.4867 | 0.5478 | -0.034 ± 0.0188 | -0.0137 (8) |
| 3-5 | 441 | 0.2039 | 0.2023 | +0.0016 ± 0.0017 | 0.5914 | 0.5859 | 0.5055 | 0.4658 | 0.4671 | -0.116 ± 0.0223 | 0.0067 (3) |
| 5-10 | 933 | 0.2026 | 0.199 | +0.0036 ± 0.0022 | 0.5917 | 0.5796 | 0.5082 | 0.4342 | 0.4448 | -0.105 ± 0.015 | -0.0071 (7) |
| 10-15 | 765 | 0.2094 | 0.2057 | +0.0037 ± 0.0041 | 0.608 | 0.5937 | 0.5404 | 0.4168 | 0.4654 | -0.084 ± 0.0163 | -0.0317 (6) |
| 15-25 | 947 | 0.2308 | 0.2133 | +0.0175 ± 0.0059 | 0.6594 | 0.6104 | 0.5895 | 0.3949 | 0.4467 | -0.107 ± 0.015 | -0.03 (1) |
| 25-40 | 596 | 0.2144 | 0.2182 | -0.0038 ± 0.0112 | 0.6184 | 0.6223 | 0.671 | 0.3599 | 0.5185 | -0.056 ± 0.0172 | 0.015 (2) |
| 40+ | 121 | 0.2922 | 0.2133 | +0.0789 ± 0.0366 | 0.8066 | 0.6151 | 0.7677 | 0.3179 | 0.4628 | -0.070 ± 0.0386 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3254 | 0.1854 | 0.1859 | -0.0005 ± 0.0003 | 0.5453 | 0.5462 | 0.4897 | 0.4745 | 0.4896 | -0.037 ± 0.0076 | -0.0163 (35) |
| 3-5 | 2214 | 0.1954 | 0.1935 | +0.0019 ± 0.0008 | 0.5734 | 0.5671 | 0.4869 | 0.4473 | 0.4435 | -0.063 ± 0.0096 | -0.0094 (18) |
| 5-10 | 4829 | 0.196 | 0.1903 | +0.0057 ± 0.0009 | 0.5759 | 0.5571 | 0.4836 | 0.4097 | 0.4084 | -0.061 ± 0.0063 | -0.01 (31) |
| 10-15 | 3938 | 0.1923 | 0.177 | +0.0153 ± 0.0017 | 0.5684 | 0.5229 | 0.5001 | 0.3767 | 0.3761 | -0.065 ± 0.0067 | -0.015 (12) |
| 15-25 | 5262 | 0.2113 | 0.1728 | +0.0384 ± 0.0022 | 0.617 | 0.5094 | 0.5157 | 0.3207 | 0.32 | -0.072 ± 0.0057 | -0.03 (2) |
| 25-40 | 4013 | 0.2196 | 0.1327 | +0.0869 ± 0.0036 | 0.6337 | 0.4029 | 0.538 | 0.2218 | 0.2442 | -0.050 ± 0.0055 | 0.01 (3) |
| 40+ | 2530 | 0.3954 | 0.0503 | +0.3450 ± 0.0051 | 1.033 | 0.1875 | 0.6455 | 0.1133 | 0.0692 | -0.081 ± 0.0043 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1005 | 0.1952 | 0.1955 | -0.0002 ± 0.0005 | 0.5699 | 0.5699 | 0.5029 | 0.4878 | 0.4955 | -0.057 ± 0.0141 | -0.0224 (49) |
| 3-5 | 700 | 0.193 | 0.1922 | +0.0008 ± 0.0013 | 0.5636 | 0.5605 | 0.4914 | 0.4515 | 0.4586 | -0.061 ± 0.017 | -0.0194 (34) |
| 5-10 | 1457 | 0.2026 | 0.1966 | +0.0060 ± 0.0017 | 0.5946 | 0.5758 | 0.4966 | 0.4233 | 0.42 | -0.074 ± 0.0118 | -0.005 (78) |
| 10-15 | 972 | 0.211 | 0.1989 | +0.0121 ± 0.0036 | 0.6114 | 0.58 | 0.5232 | 0.4001 | 0.4105 | -0.071 ± 0.0146 | 0.0014 (64) |
| 15-25 | 1306 | 0.2315 | 0.2111 | +0.0204 ± 0.005 | 0.6613 | 0.6072 | 0.5783 | 0.3835 | 0.4296 | -0.072 ± 0.0127 | -0.0214 (59) |
| 25-40 | 790 | 0.2478 | 0.2074 | +0.0404 ± 0.01 | 0.7039 | 0.5962 | 0.6744 | 0.3616 | 0.4532 | -0.087 ± 0.0152 | -0.0219 (26) |
| 40+ | 262 | 0.3523 | 0.1994 | +0.1529 ± 0.0272 | 1.0179 | 0.5813 | 0.8088 | 0.3267 | 0.4275 | -0.095 ± 0.025 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3291 | 0.1833 | 0.1836 | -0.0002 ± 0.0003 | 0.54 | 0.5396 | 0.5048 | 0.4894 | 0.5008 | -0.037 ± 0.0075 | -0.0157 (88) |
| 3-5 | 2280 | 0.1954 | 0.1935 | +0.0019 ± 0.0007 | 0.5699 | 0.5656 | 0.4973 | 0.4576 | 0.4535 | -0.054 ± 0.0093 | -0.0209 (69) |
| 5-10 | 4539 | 0.1976 | 0.1894 | +0.0083 ± 0.001 | 0.581 | 0.5567 | 0.4915 | 0.418 | 0.4016 | -0.071 ± 0.0065 | -0.0082 (132) |
| 10-15 | 3185 | 0.2075 | 0.1912 | +0.0163 ± 0.0019 | 0.6038 | 0.5613 | 0.5299 | 0.4068 | 0.4016 | -0.067 ± 0.0078 | -0.0053 (105) |
| 15-25 | 3959 | 0.2299 | 0.2002 | +0.0297 ± 0.0028 | 0.6632 | 0.5798 | 0.5702 | 0.3747 | 0.3976 | -0.065 ± 0.0071 | -0.0253 (107) |
| 25-40 | 2726 | 0.2591 | 0.1843 | +0.0748 ± 0.0052 | 0.7341 | 0.5378 | 0.6334 | 0.3194 | 0.3599 | -0.078 ± 0.008 | -0.0229 (51) |
| 40+ | 1208 | 0.3788 | 0.1449 | +0.2339 ± 0.0115 | 1.0731 | 0.4364 | 0.7301 | 0.2263 | 0.2591 | -0.071 ± 0.0103 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4420 | 1.03 ± 0.042 | 1.114 | 0.1685 | 0.1633 | 0.2147 | 0.2067 |
| gen2 | 4420 | 0.835 ± 0.039 | 1.082 | 0.1679 | 0.164 | 0.2341 | 0.2063 |
| gen1_elo | 4420 | 1.002 ± 0.041 | 1.109 | 0.1753 | 0.1634 | 0.2136 | 0.207 |
| gen1_sr | 4420 | 1.018 ± 0.051 | 1.157 | 0.1291 | 0.1659 | 0.2302 | 0.2059 |
| gen1_ledger | 6492 | 0.857 ± 0.03 | 1.066 | 0.1835 | 0.1777 | 0.219 | 0.2006 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 22,016)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,039 | 22.9% |
| STALE_QUOTE | market_freshness | 4,777 | 21.7% |
| BOOK_QUALITY | execution | 4,165 | 18.9% |
| POOR_DATA | data | 2,470 | 11.2% |
| LIMITED_DATA | data | 1,362 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,189 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,051 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 930 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 651 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 381 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.9%, market_freshness 21.7%, execution 18.9%, data 17.4%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.0%, LOW_DATA_QUALITY 70.7%, THIN_PLAYER_HISTORY 59.5%, STALE_PLAYER_DATA 49.5%, STALE_KALSHI_QUOTE 44.2%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.0%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.9%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.9%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.4%, POST_SETTLEMENT_OBSERVATION 22.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,809)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,063 | 34.4% |
| STALE_QUOTE | market_freshness | 2,213 | 18.7% |
| BOOK_QUALITY | execution | 2,179 | 18.4% |
| POOR_DATA | data | 1,016 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 639 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 523 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 414 | 3.5% |
| LIMITED_DATA | data | 410 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 262 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 89 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.4%, market_freshness 18.7%, execution 18.4%, data 12.1%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.1%, THIN_PLAYER_HISTORY 61.7%, STALE_KALSHI_QUOTE 52.2%, STALE_PLAYER_DATA 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.8%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.3%, PLAYER_IDENTITY_RISK 19.9%, MODEL_HIGH_UNCERTAINTY 18.3%, EVENT_MAPPING_RISK 9.8%, LEVEL_TRANSFER_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.5%, POST_SETTLEMENT_OBSERVATION 34.4%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9160, "IDENTITY_AMBIGUOUS": 2649}; ticker orientation: {"VERIFIED": 11809}.

Checks: discipline:AMBIGUOUS 815, discipline:PASS 10994, identity_confidence:AMBIGUOUS 2351, identity_confidence:PASS 9458, level_mapping:NA 827, level_mapping:PASS 10982, market_pair:AMBIGUOUS 435, market_pair:NA 295, market_pair:PASS 11079, model_complement:NA 262, model_complement:PASS 11547, namesake:AMBIGUOUS 6, namesake:PASS 11803, physical_match_id:NA 4146, physical_match_id:PASS 7663, player_ids:PASS 11809, same_pair_other_event:PASS 11809, ticker_orientation:PASS 11809

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,489 | 4.5% | 4.0% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 47, "data": 35, "execution": 23, "model_calibration": 17, "market_freshness/coverage": 15, "coverage": 13} | 5.92 | 0.2224 / 0.2181 (519) | 18.8% | 3.5% | 3.2% | 2.8% |
| CHALLENGER | 8,148 | 17.2% | 7.0% | 11.8% | {"coverage": 787, "market_freshness/coverage": 169, "market_freshness": 155, "data": 141, "model_calibration_or_unknown": 67, "execution": 33, "model_calibration": 30, "mapping": 15, "possible_market_error": 1} | 7.56 | 0.2202 / 0.21 (1910) | 34.4% | 17.7% | 4.0% | 22.3% |
| DOUBLES | 1,728 | 47.2% | 46.8% | 6.9% | {"execution": 439, "mapping": 208, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.62 | 0.3096 / 0.2358 (432) | 13.5% | 0.0% | 100.0% | 6.9% |
| ITF_MEN | 14,725 | 25.4% | 17.7% | 31.7% | {"coverage": 1396, "execution": 711, "market_freshness": 642, "data": 497, "market_freshness/coverage": 324, "mapping": 174, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.93 | 0.2159 / 0.1976 (3286) | 37.5% | 69.8% | 19.9% | 22.2% |
| ITF_WOMEN | 19,364 | 27.3% | 19.9% | 44.7% | {"coverage": 1835, "market_freshness": 1158, "execution": 925, "data": 718, "market_freshness/coverage": 441, "mapping": 120, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.89 | 0.2038 / 0.1949 (3728) | 39.9% | 56.1% | 10.0% | 22.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,108 | 5.5% | 5.0% | 1.5% | {"market_freshness": 59, "model_calibration_or_unknown": 36, "execution": 26, "model_calibration": 16, "coverage": 12, "data": 11, "market_freshness/coverage": 10, "mapping": 1} | 7.64 | 0.2348 / 0.23 (507) | 24.6% | 1.4% | 1.7% | 3.4% |
| WTA125 | 1,437 | 12.9% | 10.4% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 24, "execution": 17, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.52 | 0.219 / 0.2065 (488) | 22.8% | 9.2% | 6.3% | 9.5% |

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
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 162 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 50 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9684, "by_level_share_of_ge_25pp": {"ATP": 0.0172, "CHALLENGER": 0.1184, "DOUBLES": 0.069, "ITF_MEN": 0.3174, "ITF_WOMEN": 0.4469, "OTHER": 0.001, "WTA": 0.0145, "WTA125": 0.0157}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5223, "share_primary_cause_market_settled_or_in_play": 0.4333, "share_primary_cause_stale_quote_only": 0.1874}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11809, "identity_ambiguous_share": 0.2243, "ticker_orientation": {"VERIFIED": 11809}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7663, "with_external": 384, "coverage": 0.0501, "external_status": {"EXTERNAL_STALE": 229, "AGREES_WITH_KALSHI": 146, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 229, "MODEL_LONE_OUTLIER": 146, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3802, "share_external_supports_model": 0.0234}, "pregame_clean_ge_25pp": {"n": 3730, "with_external": 361, "coverage": 0.0968, "external_status": {"EXTERNAL_STALE": 213, "AGREES_WITH_KALSHI": 139, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 213, "MODEL_LONE_OUTLIER": 139, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.385, "share_external_supports_model": 0.0249}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.5, "median_sample_ratio": 2.42, "median_min_matches": 21.0, "median_max_days_since_last": 227.0, "share_severe_asymmetry": 0.2146, "data_status": {"POOR": 6554, "LIMITED": 3095, "ADEQUATE": 2160}, "comparison_lt_10pp": {"median_thinner_serve_points": 1754.0, "median_sample_ratio": 1.69, "median_min_matches": 97.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 872, "model_minus_observed": 0.0486, "kalshi_minus_observed": -0.0901, "brier_diff_model_minus_kalshi": -0.0046}, "4-10x": {"n": 595, "model_minus_observed": 0.0925, "kalshi_minus_observed": -0.054, "brier_diff_model_minus_kalshi": 0.0111}, "<2x": {"n": 2157, "model_minus_observed": 0.0925, "kalshi_minus_observed": -0.0305, "brier_diff_model_minus_kalshi": 0.0124}, ">=10x": {"n": 796, "model_minus_observed": 0.1106, "kalshi_minus_observed": -0.0648, "brier_diff_model_minus_kalshi": 0.0076}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4420, "model": {"intercept": -0.535, "slope": 0.835, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.212, "slope": 1.082, "slope_se": 0.044}, "mean_extremity_model": 0.1679, "mean_extremity_kalshi": 0.164, "model_brier": 0.2341, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.0277, "brier_diff_se": 0.0029, "model_logloss": 0.6644, "kalshi_logloss": 0.5957}, "fair_v1": {"n": 4420, "model": {"intercept": -0.419, "slope": 1.03, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.285, "slope": 1.114, "slope_se": 0.044}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1633, "model_brier": 0.2147, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0023, "model_logloss": 0.6183, "kalshi_logloss": 0.5962}, "gen1_elo": {"n": 4420, "model": {"intercept": -0.394, "slope": 1.002, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.307, "slope": 1.109, "slope_se": 0.043}, "mean_extremity_model": 0.1753, "mean_extremity_kalshi": 0.1634, "model_brier": 0.2136, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0067, "brier_diff_se": 0.0024, "model_logloss": 0.6169, "kalshi_logloss": 0.5969}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2487, "share_ge_15": 0.4456, "median_abs_gap": 13.14, "n": 30809}, "gen1_elo": {"share_ge_25": 0.246, "share_ge_15": 0.4448, "median_abs_gap": 13.0, "n": 30809}, "gen1_sr": {"share_ge_25": 0.3163, "share_ge_15": 0.5242, "median_abs_gap": 16.0, "n": 30809}, "gen2": {"share_ge_25": 0.3198, "share_ge_15": 0.5141, "median_abs_gap": 15.59, "n": 30809}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1558, "share_ge_15": 0.3614, "median_abs_gap": 10.94, "n": 23933}, "gen1_elo": {"share_ge_25": 0.1565, "share_ge_15": 0.3593, "median_abs_gap": 10.74, "n": 23930}, "gen1_sr": {"share_ge_25": 0.2227, "share_ge_15": 0.4461, "median_abs_gap": 13.1, "n": 23934}, "gen2": {"share_ge_25": 0.2389, "share_ge_15": 0.4456, "median_abs_gap": 13.07, "n": 23935}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.92, "share_ge_25_all": 0.0452, "share_ge_25_pregame_clean": 0.0401}, "WTA": {"median_abs_gap_pregame_clean": 7.64, "share_ge_25_all": 0.055, "share_ge_25_pregame_clean": 0.0496}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2343, "share_within_10pp_all": 0.4321, "share_within_10pp_pregame_clean": 0.4849, "corr_model_vs_mid_pregame_clean": 0.8427}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 646, "model_brier": 0.2024, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 763, "model_brier": 0.2151, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 999, "model_brier": 0.2252, "kalshi_brier": 0.213, "brier_diff_model_minus_kalshi": 0.0122}, "25-40": {"n_settled": 573, "model_brier": 0.2225, "kalshi_brier": 0.2104, "brier_diff_model_minus_kalshi": 0.0121}, "3-5": {"n_settled": 410, "model_brier": 0.205, "kalshi_brier": 0.2044, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 115, "model_brier": 0.2766, "kalshi_brier": 0.2018, "brier_diff_model_minus_kalshi": 0.0748}, "5-10": {"n_settled": 914, "model_brier": 0.2033, "kalshi_brier": 0.2025, "brier_diff_model_minus_kalshi": 0.0008}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.535, "slope": 0.835, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.212, "slope": 1.082, "slope_se": 0.044}, "n": 4420}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.505, "slope": 0.857, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.153, "slope": 1.066, "slope_se": 0.034}, "n": 6492}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 432, "model_brier": 0.3096, "kalshi_brier": 0.2358, "brier_diff_model_minus_kalshi": 0.0738, "brier_diff_se": 0.0146, "corr_model_outcome": 0.0434, "corr_kalshi_outcome": 0.2537}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
