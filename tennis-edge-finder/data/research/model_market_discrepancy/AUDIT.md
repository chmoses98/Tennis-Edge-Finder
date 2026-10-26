# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-26T06:53Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 55,463): 0-3 13.9%, 3-5 9.6%, 5-10 19.8%, 10-15 15.4%, 15-25 19.2%, 25-40 13.9%, 40+ 8.1%; median gap 12.0 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.1%, Challenger 11.9%, doubles 7.1%). Main tour: ATP 4.3% and WTA 5.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 12,209): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.0%, BOOK_QUALITY 18.9%, STALE_QUOTE 18.7%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, LIMITED_DATA 3.5%, IN_PLAY_QUOTE 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.0%, execution 18.9%, market_freshness 18.7%, data 12.1%, market_freshness/coverage 8.8%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 12,209 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.4% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 478.0 points vs 1766.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.035, Gen-2 0.83, Gen-1 ledger 0.863 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 590 model 0.2216 vs Kalshi 0.2104; n 116 model 0.2743 vs Kalshi 0.202.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 243,751 model-market comparisons (393,993 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 82,144 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-26T06:42:51.542617+00:00'], shadow board 63,873 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-26T06:42:54.416981+00:00'], Model 4 31,386 rows, 20,712 settled tickers, 7,361 tickers with an external scan.
* By model: {"gen1_ledger": 56291, "gen1_elo": 32118, "fair_v1": 32118, "gen2": 32118, "gen1_sr": 32118, "model4_fundamental": 29516, "model4_conditioned": 29472}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 55,463 | 13.9 | 9.6 | 19.8 | 15.4 | 19.2 | 13.9 | 8.1 | 12.0 | 41.2% | 22.0% |
| MW fair_v1 | 32,118 | 12.9 | 8.7 | 18.5 | 15.6 | 19.7 | 14.9 | 9.7 | 13.09 | 44.4% | 24.6% |
| MW gen1_elo | 32,118 | 12.7 | 8.6 | 19.1 | 15.3 | 19.9 | 14.9 | 9.5 | 12.98 | 44.3% | 24.4% |
| MW gen1_ledger | 23,345 | 15.4 | 10.8 | 21.7 | 15.2 | 18.5 | 12.6 | 5.8 | 10.52 | 37.0% | 18.4% |
| MW gen1_sr | 32,118 | 10.2 | 7.1 | 17.0 | 13.6 | 20.7 | 18.6 | 12.7 | 15.93 | 52.1% | 31.4% |
| MW gen2 | 32,118 | 11.1 | 7.4 | 16.4 | 14.0 | 19.4 | 17.9 | 13.9 | 15.52 | 51.2% | 31.8% |
| all families model4_conditioned | 29,472 | 21.8 | 18.4 | 34.5 | 17.7 | 4.7 | 1.8 | 1.1 | 6.06 | 7.6% | 2.9% |
| all families model4_fundamental | 29,516 | 16.7 | 13.2 | 34.0 | 20.7 | 10.4 | 3.6 | 1.4 | 7.83 | 15.4% | 5.0% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.6%, >=15pp 41.2%, >=20pp 30.6%, >=25pp 22.0%, >=30pp 15.9%, >=40pp 8.1%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.35pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,969 | 27.3 | 14.7 | 26.4 | 14.9 | 11.8 | 4.3 | 0.7 | 6.11 | 16.8% | 5.0% |
| CHALLENGER | 5,099 | 15.8 | 10.1 | 20.1 | 15.6 | 15.6 | 12.3 | 10.6 | 11.12 | 38.4% | 22.8% |
| ITF_MEN | 8,621 | 10.1 | 7.2 | 16.7 | 14.6 | 21.6 | 17.6 | 12.2 | 15.51 | 51.4% | 29.8% |
| ITF_WOMEN | 12,537 | 9.4 | 6.9 | 15.9 | 15.3 | 22.4 | 18.3 | 11.8 | 15.78 | 52.5% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,118 | 17.0 | 13.6 | 25.6 | 20.1 | 17.1 | 6.0 | 0.6 | 8.32 | 23.7% | 6.6% |
| WTA125 | 768 | 14.2 | 7.5 | 21.5 | 22.0 | 20.2 | 12.8 | 1.8 | 11.33 | 34.8% | 14.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,969 | 24.1 | 15.1 | 25.8 | 17.4 | 12.4 | 4.3 | 0.9 | 6.57 | 17.6% | 5.2% |
| CHALLENGER | 5,099 | 15.0 | 8.9 | 18.1 | 14.6 | 18.2 | 14.1 | 11.3 | 12.69 | 43.6% | 25.4% |
| ITF_MEN | 8,621 | 8.0 | 5.8 | 14.4 | 13.0 | 19.6 | 21.2 | 17.8 | 18.82 | 58.7% | 39.1% |
| ITF_WOMEN | 12,537 | 8.1 | 5.6 | 13.8 | 13.0 | 20.7 | 21.1 | 17.7 | 19.2 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,118 | 14.3 | 10.4 | 22.4 | 15.9 | 22.5 | 13.2 | 1.2 | 10.87 | 36.9% | 14.4% |
| WTA125 | 768 | 7.2 | 6.1 | 16.4 | 18.2 | 24.6 | 18.9 | 8.6 | 16.04 | 52.1% | 27.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,969 | 23.1 | 12.4 | 24.4 | 16.3 | 15.9 | 6.6 | 1.2 | 7.54 | 23.8% | 7.9% |
| CHALLENGER | 5,099 | 14.3 | 9.2 | 21.0 | 15.6 | 16.2 | 12.9 | 10.8 | 11.45 | 39.8% | 23.6% |
| ITF_MEN | 8,621 | 9.6 | 7.3 | 16.8 | 13.8 | 22.2 | 17.9 | 12.4 | 16.0 | 52.6% | 30.4% |
| ITF_WOMEN | 12,537 | 9.3 | 6.6 | 16.3 | 15.8 | 22.7 | 18.2 | 11.0 | 15.59 | 51.9% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,118 | 23.8 | 17.1 | 30.6 | 15.3 | 9.6 | 2.7 | 0.8 | 6.04 | 13.1% | 3.5% |
| WTA125 | 768 | 22.4 | 11.8 | 26.8 | 16.7 | 15.9 | 6.0 | 0.4 | 7.99 | 22.3% | 6.4% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,794 | 24.8 | 19.5 | 29.8 | 13.2 | 9.5 | 3.0 | 0.3 | 5.67 | 12.8% | 3.3% |
| CHALLENGER | 3,534 | 21.1 | 14.3 | 26.7 | 15.0 | 14.7 | 6.5 | 1.7 | 7.43 | 23.0% | 8.2% |
| DOUBLES | 1,810 | 5.2 | 4.5 | 12.3 | 10.2 | 20.2 | 25.8 | 21.9 | 24.05 | 67.8% | 47.7% |
| ITF_MEN | 6,382 | 13.6 | 9.1 | 19.9 | 16.1 | 21.5 | 13.3 | 6.4 | 12.21 | 41.3% | 19.8% |
| ITF_WOMEN | 7,588 | 12.6 | 8.8 | 19.4 | 15.3 | 21.6 | 16.2 | 6.0 | 12.83 | 43.8% | 22.2% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,269 | 22.9 | 15.5 | 30.5 | 17.9 | 9.7 | 3.1 | 0.3 | 6.82 | 13.2% | 3.5% |
| WTA125 | 819 | 21.2 | 13.6 | 21.9 | 18.4 | 14.4 | 8.4 | 2.1 | 8.3 | 24.9% | 10.5% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,889 | 27.6 | 14.9 | 26.8 | 14.8 | 11.6 | 4.0 | 0.4 | 5.95 | 16.0% | 4.4% |
| CHALLENGER | 3,616 | 20.5 | 12.5 | 24.7 | 18.0 | 15.7 | 6.8 | 1.7 | 8.38 | 24.2% | 8.6% |
| ITF_MEN | 6,303 | 12.2 | 8.7 | 20.2 | 16.6 | 22.8 | 14.4 | 5.2 | 12.65 | 42.4% | 19.6% |
| ITF_WOMEN | 9,409 | 11.2 | 8.3 | 18.1 | 17.3 | 24.3 | 15.5 | 5.4 | 13.57 | 45.2% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,058 | 17.2 | 13.4 | 25.7 | 20.4 | 17.1 | 5.7 | 0.6 | 8.25 | 23.4% | 6.3% |
| WTA125 | 742 | 14.6 | 7.4 | 21.0 | 22.4 | 20.8 | 12.4 | 1.5 | 11.33 | 34.6% | 13.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,889 | 24.3 | 15.5 | 26.1 | 17.3 | 12.3 | 4.0 | 0.5 | 6.48 | 16.9% | 4.5% |
| CHALLENGER | 3,616 | 19.0 | 11.3 | 22.3 | 17.3 | 18.4 | 9.8 | 1.9 | 9.39 | 30.2% | 11.8% |
| ITF_MEN | 6,304 | 9.6 | 7.1 | 16.8 | 15.1 | 21.5 | 19.4 | 10.6 | 15.5 | 51.5% | 30.0% |
| ITF_WOMEN | 9,410 | 9.2 | 6.4 | 15.2 | 14.4 | 22.7 | 20.6 | 11.4 | 16.84 | 54.7% | 32.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,058 | 14.4 | 10.4 | 22.4 | 15.9 | 22.5 | 13.0 | 1.2 | 10.87 | 36.7% | 14.2% |
| WTA125 | 742 | 7.0 | 6.3 | 16.4 | 18.6 | 24.5 | 19.3 | 7.8 | 15.73 | 51.6% | 27.1% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,743 | 24.9 | 19.8 | 29.8 | 13.3 | 9.1 | 2.9 | 0.2 | 5.62 | 12.2% | 3.0% |
| CHALLENGER | 3,104 | 22.4 | 15.3 | 28.0 | 15.1 | 14.2 | 4.6 | 0.5 | 6.94 | 19.2% | 5.1% |
| DOUBLES | 1,690 | 5.2 | 4.6 | 12.5 | 10.4 | 20.0 | 25.7 | 21.7 | 23.91 | 67.4% | 47.4% |
| ITF_MEN | 5,360 | 14.7 | 9.7 | 21.6 | 16.9 | 21.5 | 11.7 | 3.9 | 11.27 | 37.1% | 15.6% |
| ITF_WOMEN | 6,335 | 13.5 | 9.3 | 20.7 | 16.2 | 21.8 | 15.0 | 3.5 | 11.83 | 40.4% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,217 | 23.3 | 15.9 | 30.5 | 17.9 | 9.7 | 2.5 | 0.1 | 6.78 | 12.3% | 2.6% |
| WTA125 | 708 | 23.0 | 14.8 | 23.2 | 19.8 | 12.8 | 5.8 | 0.6 | 7.6 | 19.2% | 6.4% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,810 | 5.2 | 4.5 | 12.3 | 10.2 | 20.2 | 25.8 | 21.9 | 24.05 | 67.8% | 47.7% |
| singles | 21,535 | 16.3 | 11.3 | 22.5 | 15.6 | 18.4 | 11.5 | 4.5 | 9.98 | 34.4% | 16.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,016 | 12.8 | 9.1 | 19.4 | 15.9 | 19.0 | 14.2 | 9.6 | 12.66 | 42.8% | 23.8% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 20,177 | 13.4 | 8.8 | 18.6 | 15.2 | 19.8 | 14.8 | 9.5 | 13.0 | 44.0% | 24.3% |
| UNKNOWN | 4,676 | 10.8 | 7.5 | 17.0 | 16.8 | 20.5 | 16.3 | 11.1 | 14.12 | 48.0% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,290 | 19.6 | 12.1 | 21.8 | 16.4 | 14.9 | 9.1 | 6.0 | 8.92 | 30.1% | 15.2% |
| B | 3,971 | 12.2 | 8.8 | 19.4 | 16.5 | 19.6 | 12.7 | 10.8 | 12.67 | 43.1% | 23.5% |
| C | 4,461 | 11.8 | 9.0 | 19.4 | 15.6 | 19.2 | 14.6 | 10.4 | 13.02 | 44.2% | 24.9% |
| D | 4,892 | 12.1 | 7.8 | 17.4 | 15.4 | 21.7 | 15.6 | 9.9 | 13.98 | 47.2% | 25.5% |
| F | 9,504 | 7.5 | 5.5 | 15.1 | 14.5 | 23.8 | 21.2 | 12.4 | 17.79 | 57.4% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,698 | 23.2 | 16.1 | 28.8 | 15.2 | 11.4 | 3.9 | 1.3 | 6.6 | 16.6% | 5.3% |
| B | 3,149 | 16.2 | 10.3 | 23.1 | 16.3 | 19.9 | 10.4 | 3.7 | 10.06 | 34.0% | 14.1% |
| C | 4,588 | 10.9 | 7.2 | 18.6 | 14.4 | 21.1 | 16.6 | 11.1 | 14.41 | 48.9% | 27.8% |
| D | 3,185 | 14.2 | 9.6 | 20.1 | 15.1 | 21.0 | 14.1 | 5.9 | 11.95 | 40.9% | 19.9% |
| F | 5,725 | 10.2 | 8.3 | 15.8 | 15.1 | 22.8 | 19.9 | 7.9 | 15.33 | 50.7% | 27.9% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,585 | 17.8 | 10.9 | 21.1 | 16.1 | 15.5 | 10.1 | 8.6 | 10.02 | 34.1% | 18.6% |
| LIMITED | 6,793 | 13.5 | 10.2 | 20.0 | 16.2 | 19.3 | 13.2 | 7.5 | 11.83 | 40.0% | 20.7% |
| POOR | 14,740 | 9.1 | 6.4 | 15.9 | 14.9 | 23.0 | 19.2 | 11.6 | 16.25 | 53.7% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,788 | 24.8 | 18.7 | 33.5 | 14.4 | 6.0 | 2.3 | 0.2 | 5.68 | 8.6% | 2.5% |
| GAME_SPREAD | 5,318 | 22.4 | 15.3 | 33.3 | 17.0 | 9.1 | 2.5 | 0.3 | 6.7 | 12.0% | 2.9% |
| MATCH_WINNER | 23,345 | 15.4 | 10.8 | 21.7 | 15.2 | 18.5 | 12.6 | 5.8 | 10.52 | 37.0% | 18.4% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,173 | 27.9 | 16.4 | 31.2 | 12.7 | 9.3 | 2.2 | 0.3 | 5.69 | 11.9% | 2.6% |
| TOTAL_GAMES | 8,643 | 9.0 | 10.1 | 36.3 | 27.5 | 10.5 | 3.9 | 2.8 | 9.38 | 17.2% | 6.7% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,557 | 24.5 | 31.3 | 32.9 | 6.6 | 3.7 | 0.8 | 0.2 | 4.65 | 4.7% | 1.0% |
| GAME_SPREAD | 6,900 | 46.2 | 16.6 | 26.2 | 7.8 | 1.8 | 1.1 | 0.4 | 3.39 | 3.3% | 1.5% |
| TOTAL_GAMES | 12,015 | 5.4 | 8.1 | 40.8 | 33.1 | 7.3 | 3.0 | 2.3 | 9.53 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,568 | 23.6 | 16.9 | 35.3 | 14.1 | 7.2 | 2.5 | 0.4 | 6.03 | 10.1% | 2.9% |
| GAME_SPREAD | 6,903 | 19.6 | 13.2 | 28.1 | 21.0 | 12.8 | 4.3 | 1.0 | 7.95 | 18.0% | 5.2% |
| TOTAL_GAMES | 12,045 | 8.9 | 9.8 | 36.3 | 26.3 | 12.0 | 4.2 | 2.5 | 9.41 | 18.6% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 32,118 | 44.4% | 24.6% | 13.09 | 36.0% | 15.5% | 10.89 |
| gen1_elo | 32,118 | 44.3% | 24.4% | 12.98 | 35.8% | 15.6% | 10.71 |
| gen1_sr | 32,118 | 52.1% | 31.4% | 15.93 | 44.3% | 22.1% | 13.01 |
| gen2 | 32,118 | 51.2% | 31.8% | 15.52 | 44.4% | 23.8% | 13.02 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 16,258 | 15.6 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.2 | 10.71 | 35.2% | 15.1% |
| STALE | 15,860 | 10.1 | 6.8 | 15.6 | 13.8 | 19.3 | 18.0 | 16.4 | 16.71 | 53.7% | 34.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 16,813 | 16.3 | 11.2 | 22.4 | 15.3 | 17.8 | 12.0 | 4.8 | 10.0 | 34.7% | 16.9% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 55,463 | 16813 | 19730 | 18920 | 24.1 | 134.7 | 1400.4 |
| ge_15pp | 22,876 | 5832 | 7015 | 10029 | 26.2 | 437.6 | 1380.4 |
| ge_25pp | 12,209 | 2840 | 3046 | 6323 | 31.6 | 580.4 | 1380.4 |
| lt_10pp | 24,041 | 8404 | 9346 | 6291 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261026T065349Z-9cbad550`: 875 priced rows, quote age at build {'median': 11.3, 'max': 11.4}, freshness {'AGING': 875}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 28 | 0.0 | 0.0 | 21.4 | 10.7 | 39.3 | 28.6 | 0.0 | 20.48 | 67.9% | 28.6% |
| EXTERNAL_LONE_OUTLIER | 18 | 77.8 | 22.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,114 | 19.4 | 11.3 | 24.9 | 18.9 | 18.1 | 6.9 | 0.6 | 8.81 | 25.6% | 7.5% |
| KALSHI_LONE_OUTLIER | 21 | 4.8 | 4.8 | 76.2 | 4.8 | 4.8 | 4.8 | 0.0 | 6.11 | 9.5% | 4.8% |
| MARKETS_AGREE | 637 | 65.3 | 34.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,367 | 0.0 | 2.6 | 35.0 | 26.6 | 25.0 | 10.2 | 0.7 | 12.17 | 35.9% | 10.9% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 32,118 | 5185 (16.1%) | 26.4% | 0.9% | {"EXTERNAL_STALE": 3114, "AGREES_WITH_KALSHI": 1367, "ALL_AGREE": 637, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 21, "EXTERNAL_OUTLIER": 18, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 14,245 | 1309 (9.2%) | 37.5% | 1.6% | {"EXTERNAL_STALE": 797, "AGREES_WITH_KALSHI": 491, "SUPPORTS_MODEL_DIRECTION": 19, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,907 | 393 (5.0%) | 37.9% | 2.3% | {"EXTERNAL_STALE": 235, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,871 | 370 (9.6%) | 38.4% | 2.4% | {"EXTERNAL_STALE": 219, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,868 | 2921 (22.7%) | 17.6% | 0.8% | {"EXTERNAL_STALE": 1729, "ALL_AGREE": 637, "AGREES_WITH_KALSHI": 513, "EXTERNAL_OUTLIER": 18, "AGREES_WITH_MODEL": 18, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 6,128 | 10.1 | 7.6 | 19.4 | 14.7 | 22.5 | 15.9 | 9.8 | 14.11 | 48.2% | 25.7% |
| 4-10x | 4,140 | 11.1 | 8.5 | 18.7 | 15.4 | 21.8 | 14.7 | 9.8 | 13.75 | 46.3% | 24.5% |
| <2x | 16,425 | 15.1 | 9.9 | 19.2 | 16.4 | 17.4 | 13.0 | 8.9 | 11.66 | 39.3% | 21.9% |
| >=10x | 5,425 | 10.7 | 6.2 | 15.2 | 14.2 | 21.9 | 19.8 | 12.1 | 16.48 | 53.8% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 8,210 | 12.6 | 8.6 | 19.2 | 16.2 | 19.1 | 13.8 | 10.5 | 12.88 | 43.4% | 24.3% |
| 300-1000 | 6,725 | 11.7 | 8.7 | 17.3 | 15.4 | 20.7 | 16.1 | 10.0 | 13.82 | 46.8% | 26.1% |
| <300 | 10,439 | 8.4 | 5.7 | 15.4 | 14.7 | 23.3 | 20.2 | 12.3 | 17.02 | 55.8% | 32.5% |
| >=3000 | 6,744 | 21.2 | 13.3 | 23.7 | 16.4 | 14.0 | 6.9 | 4.5 | 7.76 | 25.4% | 11.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 903 | 0.551 | 0.4133 | 0.505 | +0.046 | -0.092 | -0.0044 ± 0.0051 |
| ratio 4-10x | 612 | 0.5891 | 0.4433 | 0.5016 | +0.087 | -0.058 | 0.0089 ± 0.0064 |
| ratio <2x | 2239 | 0.5393 | 0.4161 | 0.4489 | +0.090 | -0.033 | 0.0114 ± 0.003 |
| ratio >=10x | 824 | 0.5707 | 0.3953 | 0.4612 | +0.110 | -0.066 | 0.0079 ± 0.0064 |
| thinner_sample 1000-3000 | 1246 | 0.5426 | 0.4158 | 0.451 | +0.092 | -0.035 | 0.0093 ± 0.004 |
| thinner_sample 300-1000 | 1027 | 0.5667 | 0.4231 | 0.4927 | +0.074 | -0.070 | 0.0002 ± 0.0051 |
| thinner_sample <300 | 1541 | 0.5628 | 0.3962 | 0.4666 | +0.096 | -0.070 | 0.0085 ± 0.0045 |
| thinner_sample >=3000 | 764 | 0.5371 | 0.443 | 0.4725 | +0.065 | -0.029 | 0.0113 ± 0.0042 |
| data_status ADEQUATE | 1322 | 0.5387 | 0.4346 | 0.4546 | +0.084 | -0.020 | 0.0113 ± 0.0034 |
| data_status LIMITED | 1057 | 0.5509 | 0.4173 | 0.4863 | +0.065 | -0.069 | 0.0027 ± 0.0046 |
| data_status POOR | 2199 | 0.5645 | 0.403 | 0.4698 | +0.095 | -0.067 | 0.0072 ± 0.0037 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 669 | 0.2025 | 0.2033 | -0.0008 ± 0.0006 | 0.5862 | 0.588 | 0.5016 | 0.4868 | 0.5202 | -0.074 ± 0.0184 | -0.01 (5) |
| 3-5 | 421 | 0.2055 | 0.2047 | +0.0008 ± 0.0018 | 0.5941 | 0.5909 | 0.5035 | 0.4635 | 0.4727 | -0.107 ± 0.0228 | 0.02 (1) |
| 5-10 | 945 | 0.2022 | 0.2024 | -0.0002 ± 0.0022 | 0.591 | 0.5885 | 0.5139 | 0.4398 | 0.473 | -0.089 ± 0.0151 | -0.0167 (6) |
| 10-15 | 797 | 0.2151 | 0.2068 | +0.0083 ± 0.004 | 0.6206 | 0.5958 | 0.5315 | 0.4075 | 0.4354 | -0.102 ± 0.0161 | -0.048 (5) |
| 15-25 | 1040 | 0.2253 | 0.2135 | +0.0119 ± 0.0056 | 0.6462 | 0.6106 | 0.5781 | 0.3823 | 0.45 | -0.096 ± 0.0143 | -0.0033 (9) |
| 25-40 | 590 | 0.2216 | 0.2104 | +0.0111 ± 0.0112 | 0.6324 | 0.6043 | 0.6604 | 0.3505 | 0.4847 | -0.072 ± 0.0172 | -0.01 (1) |
| 40+ | 116 | 0.2743 | 0.202 | +0.0723 ± 0.036 | 0.7526 | 0.5904 | 0.7587 | 0.3114 | 0.4569 | -0.070 ± 0.0354 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3446 | 0.1856 | 0.1865 | -0.0009 ± 0.0003 | 0.5469 | 0.5479 | 0.4913 | 0.4762 | 0.5078 | -0.024 ± 0.0074 | -0.0129 (17) |
| 3-5 | 2277 | 0.2006 | 0.1992 | +0.0014 ± 0.0008 | 0.5821 | 0.5761 | 0.4856 | 0.4457 | 0.4475 | -0.055 ± 0.0095 | 0.0 (2) |
| 5-10 | 4925 | 0.1984 | 0.1952 | +0.0032 ± 0.0009 | 0.5814 | 0.57 | 0.4838 | 0.4099 | 0.4244 | -0.047 ± 0.0064 | -0.0119 (21) |
| 10-15 | 4202 | 0.1976 | 0.1804 | +0.0171 ± 0.0016 | 0.5805 | 0.532 | 0.4883 | 0.3639 | 0.3572 | -0.070 ± 0.0065 | -0.0281 (16) |
| 15-25 | 5298 | 0.2088 | 0.1695 | +0.0394 ± 0.0022 | 0.6113 | 0.501 | 0.504 | 0.3075 | 0.3069 | -0.074 ± 0.0056 | -0.0025 (44) |
| 25-40 | 4132 | 0.2232 | 0.1284 | +0.0947 ± 0.0035 | 0.6406 | 0.3935 | 0.5325 | 0.2192 | 0.2282 | -0.061 ± 0.0054 | -0.01 (1) |
| 40+ | 2664 | 0.3794 | 0.0451 | +0.3343 ± 0.0046 | 0.9881 | 0.1738 | 0.6322 | 0.1065 | 0.0638 | -0.078 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 531 | 0.2089 | 0.2095 | -0.0006 ± 0.0007 | 0.6002 | 0.6018 | 0.5071 | 0.492 | 0.516 | -0.106 ± 0.0215 | -0.01 (3) |
| 3-5 | 373 | 0.2262 | 0.2232 | +0.0029 ± 0.002 | 0.639 | 0.6329 | 0.5149 | 0.4751 | 0.4531 | -0.134 ± 0.0261 | 0.02 (1) |
| 5-10 | 823 | 0.2074 | 0.2069 | +0.0004 ± 0.0024 | 0.6012 | 0.5996 | 0.5469 | 0.4719 | 0.5103 | -0.083 ± 0.0164 | -0.01 (4) |
| 10-15 | 760 | 0.2159 | 0.2098 | +0.0061 ± 0.0042 | 0.6209 | 0.6052 | 0.5649 | 0.4407 | 0.4803 | -0.105 ± 0.0173 | -0.04 (5) |
| 15-25 | 1059 | 0.2289 | 0.211 | +0.0179 ± 0.0055 | 0.6504 | 0.6045 | 0.5877 | 0.3922 | 0.4485 | -0.098 ± 0.0144 | -0.0133 (9) |
| 25-40 | 751 | 0.2665 | 0.1996 | +0.0669 ± 0.0102 | 0.7448 | 0.5806 | 0.6566 | 0.3415 | 0.3955 | -0.121 ± 0.0161 | -0.0075 (4) |
| 40+ | 281 | 0.3519 | 0.1748 | +0.1771 ± 0.0246 | 0.968 | 0.5207 | 0.7338 | 0.25 | 0.3238 | -0.064 ± 0.0238 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2946 | 0.1945 | 0.1948 | -0.0002 ± 0.0003 | 0.5656 | 0.566 | 0.5132 | 0.4983 | 0.5126 | -0.045 ± 0.0084 | -0.0133 (15) |
| 3-5 | 1956 | 0.201 | 0.1997 | +0.0013 ± 0.0008 | 0.5805 | 0.5769 | 0.5148 | 0.4749 | 0.4785 | -0.051 ± 0.0103 | 0.02 (1) |
| 5-10 | 4357 | 0.1974 | 0.1952 | +0.0022 ± 0.001 | 0.5809 | 0.5702 | 0.5114 | 0.4374 | 0.4629 | -0.035 ± 0.0068 | -0.0117 (6) |
| 10-15 | 3796 | 0.2012 | 0.1893 | +0.0118 ± 0.0018 | 0.5904 | 0.552 | 0.5144 | 0.3905 | 0.4054 | -0.055 ± 0.0072 | -0.0189 (18) |
| 15-25 | 5234 | 0.2154 | 0.1785 | +0.0369 ± 0.0023 | 0.6258 | 0.5245 | 0.5249 | 0.329 | 0.3368 | -0.066 ± 0.0059 | -0.0086 (42) |
| 25-40 | 4832 | 0.2533 | 0.1369 | +0.1164 ± 0.0034 | 0.7122 | 0.4204 | 0.559 | 0.242 | 0.2194 | -0.089 ± 0.0053 | -0.0044 (18) |
| 40+ | 3823 | 0.3926 | 0.0606 | +0.3320 ± 0.0045 | 1.033 | 0.2165 | 0.6504 | 0.119 | 0.0855 | -0.071 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 641 | 0.2 | 0.2022 | -0.0022 ± 0.0006 | 0.5808 | 0.5862 | 0.5001 | 0.4848 | 0.5476 | -0.032 ± 0.0184 | -0.0137 (8) |
| 3-5 | 455 | 0.2032 | 0.2017 | +0.0015 ± 0.0017 | 0.5896 | 0.5846 | 0.5068 | 0.4671 | 0.4703 | -0.118 ± 0.022 | 0.0067 (3) |
| 5-10 | 974 | 0.2029 | 0.1997 | +0.0032 ± 0.0022 | 0.5923 | 0.5815 | 0.5094 | 0.4354 | 0.4497 | -0.103 ± 0.0147 | -0.0071 (7) |
| 10-15 | 790 | 0.2091 | 0.2057 | +0.0034 ± 0.004 | 0.6072 | 0.5939 | 0.5411 | 0.4175 | 0.4671 | -0.088 ± 0.0161 | -0.0317 (6) |
| 15-25 | 978 | 0.2312 | 0.2144 | +0.0168 ± 0.0058 | 0.6603 | 0.6124 | 0.5898 | 0.3952 | 0.4489 | -0.108 ± 0.0148 | -0.03 (1) |
| 25-40 | 617 | 0.2136 | 0.2175 | -0.0039 ± 0.011 | 0.6164 | 0.6205 | 0.6693 | 0.3586 | 0.517 | -0.056 ± 0.0168 | 0.015 (2) |
| 40+ | 123 | 0.2879 | 0.2151 | +0.0728 ± 0.0362 | 0.7962 | 0.6188 | 0.7691 | 0.3198 | 0.4715 | -0.063 ± 0.0383 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3368 | 0.1864 | 0.1871 | -0.0007 ± 0.0003 | 0.5481 | 0.5492 | 0.4888 | 0.4736 | 0.4932 | -0.033 ± 0.0075 | -0.0163 (35) |
| 3-5 | 2294 | 0.1975 | 0.1955 | +0.0020 ± 0.0007 | 0.5783 | 0.5718 | 0.4887 | 0.4491 | 0.4446 | -0.064 ± 0.0094 | -0.0094 (18) |
| 5-10 | 5022 | 0.1958 | 0.1902 | +0.0056 ± 0.0009 | 0.5753 | 0.5569 | 0.4841 | 0.4101 | 0.41 | -0.060 ± 0.0062 | -0.01 (31) |
| 10-15 | 4067 | 0.1915 | 0.1765 | +0.0150 ± 0.0016 | 0.5665 | 0.5217 | 0.5 | 0.3766 | 0.3769 | -0.065 ± 0.0066 | -0.015 (12) |
| 15-25 | 5433 | 0.2112 | 0.1719 | +0.0393 ± 0.0022 | 0.6167 | 0.5068 | 0.5143 | 0.319 | 0.3168 | -0.074 ± 0.0056 | -0.03 (2) |
| 25-40 | 4158 | 0.2196 | 0.1317 | +0.0879 ± 0.0035 | 0.6334 | 0.4004 | 0.5366 | 0.2209 | 0.2412 | -0.052 ± 0.0054 | 0.01 (3) |
| 40+ | 2602 | 0.3936 | 0.0506 | +0.3430 ± 0.005 | 1.0284 | 0.188 | 0.6448 | 0.1137 | 0.0703 | -0.080 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1028 | 0.1966 | 0.1967 | -0.0001 ± 0.0005 | 0.5728 | 0.5726 | 0.5021 | 0.487 | 0.4912 | -0.063 ± 0.014 | -0.0224 (49) |
| 3-5 | 707 | 0.1924 | 0.1916 | +0.0008 ± 0.0013 | 0.5623 | 0.5591 | 0.4909 | 0.4511 | 0.4583 | -0.062 ± 0.0168 | -0.0194 (34) |
| 5-10 | 1500 | 0.2021 | 0.1964 | +0.0057 ± 0.0017 | 0.5933 | 0.5752 | 0.4967 | 0.4233 | 0.422 | -0.074 ± 0.0117 | -0.005 (78) |
| 10-15 | 1002 | 0.2105 | 0.1982 | +0.0123 ± 0.0035 | 0.6102 | 0.5783 | 0.5248 | 0.4017 | 0.4112 | -0.074 ± 0.0144 | 0.0014 (64) |
| 15-25 | 1337 | 0.2319 | 0.2118 | +0.0201 ± 0.0049 | 0.6619 | 0.6087 | 0.5797 | 0.385 | 0.4323 | -0.073 ± 0.0126 | -0.0214 (59) |
| 25-40 | 815 | 0.2453 | 0.2086 | +0.0367 ± 0.0098 | 0.6992 | 0.5989 | 0.6779 | 0.3656 | 0.4626 | -0.087 ± 0.0149 | -0.0219 (26) |
| 40+ | 269 | 0.3454 | 0.2025 | +0.1429 ± 0.0269 | 0.9985 | 0.5922 | 0.8091 | 0.3283 | 0.4387 | -0.090 ± 0.0247 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3401 | 0.1826 | 0.1828 | -0.0002 ± 0.0003 | 0.538 | 0.5374 | 0.5025 | 0.4872 | 0.496 | -0.041 ± 0.0074 | -0.0157 (88) |
| 3-5 | 2350 | 0.1961 | 0.1941 | +0.0020 ± 0.0007 | 0.5714 | 0.5668 | 0.4983 | 0.4585 | 0.4536 | -0.056 ± 0.0092 | -0.0209 (69) |
| 5-10 | 4746 | 0.1962 | 0.1882 | +0.0080 ± 0.0009 | 0.5782 | 0.554 | 0.4923 | 0.4188 | 0.4041 | -0.070 ± 0.0064 | -0.0082 (132) |
| 10-15 | 3326 | 0.2071 | 0.1911 | +0.0159 ± 0.0019 | 0.603 | 0.5607 | 0.5295 | 0.4065 | 0.4023 | -0.067 ± 0.0076 | -0.0053 (105) |
| 15-25 | 4124 | 0.2309 | 0.2007 | +0.0301 ± 0.0028 | 0.6651 | 0.581 | 0.5705 | 0.3749 | 0.3972 | -0.066 ± 0.007 | -0.0253 (107) |
| 25-40 | 2804 | 0.2591 | 0.1858 | +0.0733 ± 0.0051 | 0.7346 | 0.5414 | 0.6344 | 0.321 | 0.3631 | -0.079 ± 0.0079 | -0.0229 (51) |
| 40+ | 1229 | 0.3755 | 0.1458 | +0.2297 ± 0.0114 | 1.0633 | 0.4394 | 0.7316 | 0.2283 | 0.2653 | -0.071 ± 0.0102 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4578 | 1.035 ± 0.042 | 1.11 | 0.1685 | 0.1628 | 0.2144 | 0.207 |
| gen2 | 4578 | 0.83 ± 0.038 | 1.076 | 0.1684 | 0.1636 | 0.234 | 0.2068 |
| gen1_elo | 4578 | 1.007 ± 0.04 | 1.108 | 0.1751 | 0.163 | 0.2133 | 0.2072 |
| gen1_sr | 4578 | 1.014 ± 0.05 | 1.141 | 0.1293 | 0.1654 | 0.2304 | 0.2063 |
| gen1_ledger | 6658 | 0.863 ± 0.029 | 1.065 | 0.1839 | 0.1769 | 0.2185 | 0.201 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 22,876)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,170 | 22.6% |
| STALE_QUOTE | market_freshness | 4,956 | 21.7% |
| BOOK_QUALITY | execution | 4,403 | 19.2% |
| POOR_DATA | data | 2,567 | 11.2% |
| LIMITED_DATA | data | 1,415 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,226 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,091 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 969 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 666 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 412 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.6%, market_freshness 21.7%, execution 19.2%, data 17.4%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 93.9%, LOW_DATA_QUALITY 70.8%, THIN_PLAYER_HISTORY 59.5%, STALE_PLAYER_DATA 49.8%, STALE_KALSHI_QUOTE 43.8%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 25.3%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.7%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.9%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.6%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 12,209)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,152 | 34.0% |
| BOOK_QUALITY | execution | 2,309 | 18.9% |
| STALE_QUOTE | market_freshness | 2,285 | 18.7% |
| POOR_DATA | data | 1,054 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 654 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 539 | 4.4% |
| LIMITED_DATA | data | 424 | 3.5% |
| IN_PLAY_QUOTE | market_freshness/coverage | 423 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 271 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 97 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.0%, execution 18.9%, market_freshness 18.7%, data 12.1%, market_freshness/coverage 8.8%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.2%, THIN_PLAYER_HISTORY 61.6%, STALE_KALSHI_QUOTE 51.8%, STALE_PLAYER_DATA 44.4%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.5%, WIDE_SPREAD 24.8%, PLAYER_IDENTITY_RISK 20.1%, MODEL_HIGH_UNCERTAINTY 18.2%, EVENT_MAPPING_RISK 10.0%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.2%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.1%, POST_SETTLEMENT_OBSERVATION 34.0%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9450, "IDENTITY_AMBIGUOUS": 2759}; ticker orientation: {"VERIFIED": 12209}.

Checks: discipline:AMBIGUOUS 863, discipline:PASS 11346, identity_confidence:AMBIGUOUS 2452, identity_confidence:PASS 9757, level_mapping:NA 875, level_mapping:PASS 11334, market_pair:AMBIGUOUS 465, market_pair:NA 300, market_pair:PASS 11444, model_complement:NA 267, model_complement:PASS 11942, namesake:AMBIGUOUS 6, namesake:PASS 12203, physical_match_id:NA 4302, physical_match_id:PASS 7907, player_ids:PASS 12209, same_pair_other_event:PASS 12209, ticker_orientation:PASS 12209

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,763 | 4.3% | 3.9% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 47, "data": 35, "execution": 24, "model_calibration": 20, "market_freshness/coverage": 15, "coverage": 13} | 5.88 | 0.2239 / 0.2208 (539) | 19.5% | 3.3% | 3.3% | 2.8% |
| CHALLENGER | 8,633 | 16.8% | 6.9% | 11.9% | {"coverage": 813, "market_freshness/coverage": 175, "market_freshness": 164, "data": 144, "model_calibration_or_unknown": 70, "execution": 35, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.6 | 0.2187 / 0.2085 (2021) | 34.1% | 17.4% | 4.1% | 22.2% |
| DOUBLES | 1,810 | 47.7% | 47.4% | 7.1% | {"execution": 480, "mapping": 215, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.91 | 0.3105 / 0.2361 (438) | 12.9% | 0.0% | 100.0% | 6.6% |
| ITF_MEN | 15,003 | 25.6% | 17.8% | 31.4% | {"coverage": 1430, "execution": 730, "market_freshness": 657, "data": 505, "market_freshness/coverage": 333, "mapping": 175, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.95 | 0.2165 / 0.1985 (3335) | 37.4% | 70.1% | 19.8% | 22.3% |
| ITF_WOMEN | 20,125 | 27.1% | 20.0% | 44.7% | {"coverage": 1864, "market_freshness": 1199, "execution": 989, "data": 749, "market_freshness/coverage": 450, "mapping": 126, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.92 | 0.2032 / 0.1961 (3830) | 39.6% | 56.9% | 10.2% | 21.8% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,387 | 5.4% | 5.0% | 1.5% | {"market_freshness": 63, "model_calibration_or_unknown": 39, "execution": 26, "data": 17, "model_calibration": 16, "coverage": 12, "market_freshness/coverage": 10, "mapping": 1} | 7.67 | 0.2315 / 0.2273 (529) | 24.4% | 1.2% | 1.6% | 3.3% |
| WTA125 | 1,587 | 12.5% | 10.2% | 1.6% | {"model_calibration_or_unknown": 42, "market_freshness": 41, "market_freshness/coverage": 38, "data": 28, "execution": 20, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.52 | 0.2178 / 0.2042 (502) | 23.1% | 11.5% | 6.7% | 8.6% |

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
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 92 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 43 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.968, "by_level_share_of_ge_25pp": {"ATP": 0.017, "CHALLENGER": 0.1191, "DOUBLES": 0.0707, "ITF_MEN": 0.314, "ITF_WOMEN": 0.447, "OTHER": 0.001, "WTA": 0.0151, "WTA125": 0.0162}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5179, "share_primary_cause_market_settled_or_in_play": 0.4283, "share_primary_cause_stale_quote_only": 0.1872}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 12209, "identity_ambiguous_share": 0.226, "ticker_orientation": {"VERIFIED": 12209}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7907, "with_external": 393, "coverage": 0.0497, "external_status": {"EXTERNAL_STALE": 235, "AGREES_WITH_KALSHI": 149, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 235, "MODEL_LONE_OUTLIER": 149, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3791, "share_external_supports_model": 0.0229}, "pregame_clean_ge_25pp": {"n": 3871, "with_external": 370, "coverage": 0.0956, "external_status": {"EXTERNAL_STALE": 219, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 219, "MODEL_LONE_OUTLIER": 142, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3838, "share_external_supports_model": 0.0243}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 478.0, "median_sample_ratio": 2.43, "median_min_matches": 20.0, "median_max_days_since_last": 230.0, "share_severe_asymmetry": 0.2155, "data_status": {"POOR": 6782, "LIMITED": 3195, "ADEQUATE": 2232}, "comparison_lt_10pp": {"median_thinner_serve_points": 1766.0, "median_sample_ratio": 1.67, "median_min_matches": 98.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 903, "model_minus_observed": 0.046, "kalshi_minus_observed": -0.0917, "brier_diff_model_minus_kalshi": -0.0044}, "4-10x": {"n": 612, "model_minus_observed": 0.0874, "kalshi_minus_observed": -0.0584, "brier_diff_model_minus_kalshi": 0.0089}, "<2x": {"n": 2239, "model_minus_observed": 0.0904, "kalshi_minus_observed": -0.0328, "brier_diff_model_minus_kalshi": 0.0114}, ">=10x": {"n": 824, "model_minus_observed": 0.1095, "kalshi_minus_observed": -0.0659, "brier_diff_model_minus_kalshi": 0.0079}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4578, "model": {"intercept": -0.531, "slope": 0.83, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.209, "slope": 1.076, "slope_se": 0.043}, "mean_extremity_model": 0.1684, "mean_extremity_kalshi": 0.1636, "model_brier": 0.234, "kalshi_brier": 0.2068, "brier_diff_model_minus_kalshi": 0.0272, "brier_diff_se": 0.0028, "model_logloss": 0.6649, "kalshi_logloss": 0.5966}, "fair_v1": {"n": 4578, "model": {"intercept": -0.414, "slope": 1.035, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.288, "slope": 1.11, "slope_se": 0.043}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1628, "model_brier": 0.2144, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0073, "brier_diff_se": 0.0023, "model_logloss": 0.6177, "kalshi_logloss": 0.597}, "gen1_elo": {"n": 4578, "model": {"intercept": -0.388, "slope": 1.007, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.31, "slope": 1.108, "slope_se": 0.043}, "mean_extremity_model": 0.1751, "mean_extremity_kalshi": 0.163, "model_brier": 0.2133, "kalshi_brier": 0.2072, "brier_diff_model_minus_kalshi": 0.0061, "brier_diff_se": 0.0023, "model_logloss": 0.6163, "kalshi_logloss": 0.5975}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2462, "share_ge_15": 0.4435, "median_abs_gap": 13.09, "n": 32118}, "gen1_elo": {"share_ge_25": 0.2441, "share_ge_15": 0.4429, "median_abs_gap": 12.98, "n": 32118}, "gen1_sr": {"share_ge_25": 0.3139, "share_ge_15": 0.5212, "median_abs_gap": 15.93, "n": 32118}, "gen2": {"share_ge_25": 0.3177, "share_ge_15": 0.5121, "median_abs_gap": 15.52, "n": 32118}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1547, "share_ge_15": 0.36, "median_abs_gap": 10.89, "n": 25023}, "gen1_elo": {"share_ge_25": 0.1555, "share_ge_15": 0.3581, "median_abs_gap": 10.71, "n": 25020}, "gen1_sr": {"share_ge_25": 0.2214, "share_ge_15": 0.4434, "median_abs_gap": 13.01, "n": 25024}, "gen2": {"share_ge_25": 0.2379, "share_ge_15": 0.4443, "median_abs_gap": 13.02, "n": 25025}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.88, "share_ge_25_all": 0.0435, "share_ge_25_pregame_clean": 0.0386}, "WTA": {"median_abs_gap_pregame_clean": 7.67, "share_ge_25_all": 0.0543, "share_ge_25_pregame_clean": 0.0495}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.235, "share_within_10pp_all": 0.4335, "share_within_10pp_pregame_clean": 0.4852, "corr_model_vs_mid_pregame_clean": 0.8434}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 669, "model_brier": 0.2025, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": -0.0008}, "10-15": {"n_settled": 797, "model_brier": 0.2151, "kalshi_brier": 0.2068, "brier_diff_model_minus_kalshi": 0.0083}, "15-25": {"n_settled": 1040, "model_brier": 0.2253, "kalshi_brier": 0.2135, "brier_diff_model_minus_kalshi": 0.0119}, "25-40": {"n_settled": 590, "model_brier": 0.2216, "kalshi_brier": 0.2104, "brier_diff_model_minus_kalshi": 0.0111}, "3-5": {"n_settled": 421, "model_brier": 0.2055, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0008}, "40+": {"n_settled": 116, "model_brier": 0.2743, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0723}, "5-10": {"n_settled": 945, "model_brier": 0.2022, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": -0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.531, "slope": 0.83, "slope_se": 0.038}, "kalshi_slope": {"intercept": 0.209, "slope": 1.076, "slope_se": 0.043}, "n": 4578}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.501, "slope": 0.863, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.158, "slope": 1.065, "slope_se": 0.034}, "n": 6658}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 438, "model_brier": 0.3105, "kalshi_brier": 0.2361, "brier_diff_model_minus_kalshi": 0.0744, "brier_diff_se": 0.0144, "corr_model_outcome": 0.0353, "corr_kalshi_outcome": 0.2511}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
