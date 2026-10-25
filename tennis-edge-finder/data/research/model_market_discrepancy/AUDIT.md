# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-25T12:36Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 53,840): 0-3 13.9%, 3-5 9.5%, 5-10 19.8%, 10-15 15.4%, 15-25 19.2%, 25-40 14.0%, 40+ 8.2%; median gap 12.06 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.2%, Challenger 11.9%, doubles 7.1%). Main tour: ATP 4.5% and WTA 5.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,926): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.2%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.7%, POOR_DATA 8.5%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.2%, market_freshness 18.7%, execution 18.7%, data 12.0%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,926 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.3% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1759.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.032, Gen-2 0.836, Gen-1 ledger 0.859 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 575 model 0.2226 vs Kalshi 0.2108; n 116 model 0.2743 vs Kalshi 0.202.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 234,842 model-market comparisons (380,678 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 79,450 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-25T12:21:22.333582+00:00'], shadow board 62,001 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-25T12:21:26.661001+00:00'], Model 4 29,717 rows, 20,341 settled tickers, 7,251 tickers with an external scan.
* By model: {"gen1_ledger": 54332, "gen1_elo": 31177, "fair_v1": 31177, "gen2": 31177, "gen1_sr": 31177, "model4_fundamental": 27920, "model4_conditioned": 27882}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 53,840 | 13.9 | 9.5 | 19.8 | 15.4 | 19.2 | 14.0 | 8.2 | 12.06 | 41.4% | 22.1% |
| MW fair_v1 | 31,177 | 12.9 | 8.5 | 18.5 | 15.6 | 19.7 | 14.9 | 9.8 | 13.14 | 44.5% | 24.8% |
| MW gen1_elo | 31,177 | 12.8 | 8.5 | 19.0 | 15.2 | 19.9 | 14.9 | 9.6 | 13.0 | 44.4% | 24.6% |
| MW gen1_ledger | 22,663 | 15.4 | 10.7 | 21.6 | 15.1 | 18.6 | 12.7 | 5.9 | 10.55 | 37.1% | 18.5% |
| MW gen1_sr | 31,177 | 10.2 | 7.1 | 16.8 | 13.6 | 20.8 | 18.7 | 12.9 | 15.98 | 52.4% | 31.6% |
| MW gen2 | 31,177 | 11.0 | 7.3 | 16.3 | 14.0 | 19.4 | 17.9 | 14.0 | 15.58 | 51.4% | 31.9% |
| all families model4_conditioned | 27,882 | 21.7 | 18.7 | 34.6 | 17.7 | 4.6 | 1.6 | 1.1 | 6.03 | 7.2% | 2.7% |
| all families model4_fundamental | 27,920 | 16.7 | 13.2 | 34.0 | 20.6 | 10.5 | 3.5 | 1.4 | 7.81 | 15.4% | 4.9% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.8%, >=15pp 41.4%, >=20pp 30.8%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.42pp; >=10pp 45.2%, >=25pp 17.2%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,828 | 27.8 | 14.2 | 25.6 | 15.4 | 11.9 | 4.5 | 0.7 | 6.18 | 17.1% | 5.2% |
| CHALLENGER | 4,915 | 15.8 | 10.0 | 20.2 | 15.7 | 15.3 | 12.3 | 10.7 | 11.09 | 38.3% | 23.1% |
| ITF_MEN | 8,502 | 10.1 | 7.2 | 16.7 | 14.7 | 21.5 | 17.6 | 12.2 | 15.46 | 51.3% | 29.8% |
| ITF_WOMEN | 12,215 | 9.5 | 6.9 | 15.9 | 15.3 | 22.4 | 18.2 | 11.9 | 15.79 | 52.5% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,005 | 17.3 | 13.2 | 26.3 | 19.2 | 17.5 | 5.8 | 0.7 | 8.25 | 24.0% | 6.5% |
| WTA125 | 706 | 13.0 | 7.2 | 22.1 | 21.0 | 21.5 | 13.2 | 2.0 | 11.7 | 36.7% | 15.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,828 | 23.8 | 15.0 | 25.2 | 17.9 | 12.7 | 4.5 | 0.9 | 6.71 | 18.1% | 5.5% |
| CHALLENGER | 4,915 | 15.0 | 8.8 | 18.2 | 14.6 | 17.9 | 14.0 | 11.5 | 12.67 | 43.4% | 25.5% |
| ITF_MEN | 8,502 | 8.1 | 5.8 | 14.4 | 13.0 | 19.7 | 21.1 | 17.9 | 18.79 | 58.6% | 39.0% |
| ITF_WOMEN | 12,215 | 8.2 | 5.6 | 13.7 | 13.1 | 20.5 | 21.1 | 17.7 | 19.2 | 59.4% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,005 | 14.2 | 10.2 | 22.3 | 16.1 | 22.6 | 13.3 | 1.2 | 10.87 | 37.2% | 14.6% |
| WTA125 | 706 | 6.5 | 5.0 | 17.0 | 17.6 | 25.5 | 19.7 | 8.8 | 16.84 | 54.0% | 28.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,828 | 23.4 | 12.6 | 24.3 | 16.3 | 15.3 | 6.8 | 1.3 | 7.5 | 23.4% | 8.1% |
| CHALLENGER | 4,915 | 14.5 | 9.2 | 20.8 | 15.5 | 16.2 | 13.0 | 10.9 | 11.47 | 40.1% | 23.9% |
| ITF_MEN | 8,502 | 9.6 | 7.3 | 16.8 | 13.9 | 22.1 | 17.9 | 12.4 | 15.97 | 52.4% | 30.3% |
| ITF_WOMEN | 12,215 | 9.4 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.1 | 15.59 | 51.9% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,005 | 23.7 | 17.2 | 30.7 | 15.3 | 9.9 | 2.6 | 0.7 | 6.04 | 13.1% | 3.2% |
| WTA125 | 706 | 22.4 | 11.3 | 27.6 | 15.9 | 15.9 | 6.5 | 0.4 | 7.99 | 22.8% | 6.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,766 | 24.9 | 19.2 | 30.0 | 13.0 | 9.6 | 3.1 | 0.3 | 5.67 | 12.9% | 3.3% |
| CHALLENGER | 3,402 | 21.2 | 14.2 | 26.6 | 14.8 | 14.8 | 6.6 | 1.7 | 7.42 | 23.2% | 8.3% |
| DOUBLES | 1,770 | 5.1 | 4.6 | 12.3 | 10.3 | 20.1 | 25.9 | 21.7 | 23.92 | 67.7% | 47.6% |
| ITF_MEN | 6,294 | 13.7 | 9.2 | 19.8 | 16.2 | 21.5 | 13.3 | 6.5 | 12.2 | 41.2% | 19.7% |
| ITF_WOMEN | 7,313 | 12.6 | 8.8 | 19.4 | 15.3 | 21.6 | 16.1 | 6.2 | 12.85 | 43.9% | 22.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,184 | 22.6 | 15.6 | 30.5 | 18.2 | 9.5 | 3.3 | 0.3 | 6.86 | 13.1% | 3.6% |
| WTA125 | 785 | 20.8 | 13.5 | 21.9 | 18.3 | 14.7 | 8.7 | 2.2 | 8.33 | 25.5% | 10.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,753 | 28.0 | 14.4 | 26.0 | 15.3 | 11.7 | 4.1 | 0.4 | 6.04 | 16.2% | 4.5% |
| CHALLENGER | 3,489 | 20.6 | 12.4 | 24.8 | 18.1 | 15.4 | 6.8 | 1.8 | 8.43 | 24.1% | 8.7% |
| ITF_MEN | 6,224 | 12.2 | 8.7 | 20.1 | 16.7 | 22.7 | 14.5 | 5.1 | 12.57 | 42.3% | 19.6% |
| ITF_WOMEN | 9,140 | 11.2 | 8.2 | 18.1 | 17.4 | 24.3 | 15.4 | 5.5 | 13.54 | 45.2% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,946 | 17.5 | 13.1 | 26.3 | 19.5 | 17.5 | 5.5 | 0.7 | 8.25 | 23.6% | 6.2% |
| WTA125 | 680 | 13.4 | 7.1 | 21.6 | 21.3 | 22.2 | 12.8 | 1.6 | 11.7 | 36.6% | 14.4% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,753 | 24.1 | 15.3 | 25.4 | 17.8 | 12.7 | 4.2 | 0.5 | 6.54 | 17.4% | 4.7% |
| CHALLENGER | 3,489 | 18.9 | 11.3 | 22.5 | 17.4 | 18.2 | 9.6 | 2.0 | 9.34 | 29.9% | 11.7% |
| ITF_MEN | 6,225 | 9.7 | 7.0 | 16.8 | 15.1 | 21.5 | 19.3 | 10.6 | 15.49 | 51.4% | 29.9% |
| ITF_WOMEN | 9,141 | 9.3 | 6.4 | 15.2 | 14.6 | 22.5 | 20.6 | 11.4 | 16.79 | 54.5% | 32.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,946 | 14.3 | 10.2 | 22.3 | 16.1 | 22.7 | 13.1 | 1.3 | 10.87 | 37.0% | 14.4% |
| WTA125 | 680 | 6.3 | 5.2 | 17.1 | 17.9 | 25.4 | 20.1 | 7.9 | 16.71 | 53.5% | 28.1% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,715 | 25.0 | 19.5 | 30.0 | 13.1 | 9.2 | 2.9 | 0.2 | 5.65 | 12.3% | 3.1% |
| CHALLENGER | 2,983 | 22.6 | 15.2 | 28.0 | 14.9 | 14.2 | 4.6 | 0.5 | 6.93 | 19.3% | 5.1% |
| DOUBLES | 1,650 | 5.1 | 4.7 | 12.6 | 10.4 | 19.9 | 25.8 | 21.4 | 23.85 | 67.2% | 47.3% |
| ITF_MEN | 5,279 | 14.8 | 9.8 | 21.5 | 16.9 | 21.4 | 11.6 | 3.9 | 11.23 | 37.0% | 15.5% |
| ITF_WOMEN | 6,073 | 13.5 | 9.3 | 20.8 | 16.1 | 21.9 | 14.9 | 3.6 | 11.8 | 40.3% | 18.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,132 | 23.1 | 16.1 | 30.5 | 18.2 | 9.4 | 2.6 | 0.1 | 6.79 | 12.2% | 2.7% |
| WTA125 | 674 | 22.6 | 14.8 | 23.3 | 19.7 | 13.1 | 5.9 | 0.6 | 7.6 | 19.6% | 6.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,770 | 5.1 | 4.6 | 12.3 | 10.3 | 20.1 | 25.9 | 21.7 | 23.92 | 67.7% | 47.6% |
| singles | 20,893 | 16.3 | 11.2 | 22.4 | 15.6 | 18.4 | 11.5 | 4.5 | 10.01 | 34.5% | 16.1% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 10 | 10.0 | 20.0 | 50.0 | 0.0 | 10.0 | 10.0 | 0.0 | 7.48 | 20.0% | 10.0% |
| Clay | 6,844 | 12.9 | 9.0 | 19.2 | 15.8 | 19.1 | 14.3 | 9.8 | 12.77 | 43.1% | 24.1% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 19,443 | 13.4 | 8.6 | 18.6 | 15.2 | 19.7 | 14.8 | 9.6 | 13.03 | 44.2% | 24.5% |
| UNKNOWN | 4,643 | 10.8 | 7.4 | 16.9 | 16.8 | 20.6 | 16.4 | 11.0 | 14.15 | 48.0% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,957 | 19.6 | 11.9 | 21.6 | 16.5 | 15.0 | 9.2 | 6.2 | 9.09 | 30.4% | 15.4% |
| B | 3,871 | 12.3 | 8.7 | 19.4 | 16.3 | 19.6 | 12.8 | 10.9 | 12.79 | 43.3% | 23.7% |
| C | 4,351 | 11.7 | 8.9 | 19.6 | 15.3 | 19.3 | 14.6 | 10.6 | 13.1 | 44.5% | 25.1% |
| D | 4,779 | 12.1 | 7.7 | 17.4 | 15.5 | 21.6 | 15.7 | 10.0 | 13.98 | 47.4% | 25.7% |
| F | 9,219 | 7.5 | 5.5 | 15.1 | 14.6 | 23.6 | 21.2 | 12.5 | 17.79 | 57.4% | 33.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,509 | 23.1 | 15.8 | 28.9 | 15.2 | 11.5 | 4.0 | 1.4 | 6.68 | 16.9% | 5.4% |
| B | 3,079 | 16.1 | 10.4 | 23.1 | 16.2 | 19.8 | 10.5 | 3.8 | 10.06 | 34.1% | 14.3% |
| C | 4,471 | 11.0 | 7.2 | 18.4 | 14.4 | 21.1 | 16.8 | 11.0 | 14.44 | 48.9% | 27.8% |
| D | 3,086 | 14.4 | 9.7 | 19.9 | 14.7 | 21.0 | 14.3 | 6.0 | 12.04 | 41.3% | 20.3% |
| F | 5,518 | 10.2 | 8.3 | 15.7 | 15.3 | 22.7 | 19.8 | 8.1 | 15.29 | 50.6% | 27.9% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 10,221 | 17.8 | 10.7 | 21.0 | 16.2 | 15.6 | 10.1 | 8.7 | 10.14 | 34.4% | 18.8% |
| LIMITED | 6,615 | 13.5 | 10.2 | 20.1 | 16.0 | 19.4 | 13.3 | 7.7 | 11.93 | 40.3% | 20.9% |
| POOR | 14,341 | 9.1 | 6.3 | 16.0 | 15.0 | 22.9 | 19.2 | 11.7 | 16.27 | 53.7% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,692 | 24.9 | 18.8 | 33.6 | 14.2 | 6.0 | 2.2 | 0.2 | 5.64 | 8.5% | 2.5% |
| GAME_SPREAD | 5,067 | 22.3 | 15.3 | 33.3 | 17.1 | 9.2 | 2.5 | 0.3 | 6.73 | 12.0% | 2.8% |
| MATCH_WINNER | 22,663 | 15.4 | 10.7 | 21.6 | 15.1 | 18.6 | 12.7 | 5.9 | 10.55 | 37.1% | 18.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 11,732 | 28.0 | 16.4 | 31.2 | 12.7 | 9.1 | 2.3 | 0.3 | 5.66 | 11.7% | 2.7% |
| TOTAL_GAMES | 8,154 | 9.1 | 9.9 | 36.2 | 27.9 | 10.4 | 3.6 | 2.9 | 9.39 | 16.9% | 6.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,026 | 24.6 | 32.1 | 32.7 | 6.1 | 3.6 | 0.8 | 0.2 | 4.59 | 4.6% | 1.0% |
| GAME_SPREAD | 6,549 | 45.9 | 16.7 | 26.6 | 7.9 | 1.7 | 0.9 | 0.3 | 3.44 | 2.9% | 1.2% |
| TOTAL_GAMES | 11,307 | 5.2 | 7.9 | 41.0 | 33.8 | 7.0 | 2.7 | 2.4 | 9.55 | 12.1% | 5.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 10,037 | 23.6 | 17.1 | 35.3 | 13.8 | 7.3 | 2.6 | 0.4 | 6.01 | 10.2% | 2.9% |
| GAME_SPREAD | 6,552 | 19.9 | 13.1 | 27.9 | 20.8 | 13.1 | 4.2 | 0.9 | 7.96 | 18.2% | 5.1% |
| TOTAL_GAMES | 11,331 | 8.8 | 9.8 | 36.5 | 26.7 | 11.9 | 3.9 | 2.5 | 9.42 | 18.3% | 6.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 31,177 | 44.5% | 24.8% | 13.14 | 36.1% | 15.6% | 10.94 |
| gen1_elo | 31,177 | 44.4% | 24.6% | 13.0 | 35.9% | 15.7% | 10.73 |
| gen1_sr | 31,177 | 52.4% | 31.6% | 15.98 | 44.6% | 22.3% | 13.09 |
| gen2 | 31,177 | 51.4% | 31.9% | 15.58 | 44.5% | 23.9% | 13.07 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,823 | 15.6 | 10.4 | 21.4 | 17.3 | 20.2 | 11.9 | 3.3 | 10.72 | 35.4% | 15.2% |
| STALE | 15,354 | 10.0 | 6.7 | 15.5 | 13.8 | 19.3 | 18.1 | 16.6 | 16.92 | 54.0% | 34.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 16,131 | 16.4 | 11.2 | 22.4 | 15.3 | 17.8 | 12.1 | 4.9 | 10.01 | 34.8% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 53,840 | 16131 | 19295 | 18414 | 24.1 | 139.0 | 1400.4 |
| ge_15pp | 22,289 | 5607 | 6885 | 9797 | 26.3 | 439.8 | 1380.4 |
| ge_25pp | 11,926 | 2736 | 2989 | 6201 | 32.0 | 582.7 | 1380.4 |
| lt_10pp | 23,262 | 8058 | 9123 | 6081 | 22.4 | 47.5 | 1341.5 |

Current slate `SL-20261025T123609Z-4eb0ba81`: 814 priced rows, quote age at build {'median': 15.3, 'max': 15.3}, freshness {'AGING': 814}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 26 | 0.0 | 0.0 | 23.1 | 7.7 | 38.5 | 30.8 | 0.0 | 20.48 | 69.2% | 30.8% |
| EXTERNAL_LONE_OUTLIER | 16 | 75.0 | 25.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,029 | 19.1 | 11.3 | 24.8 | 18.8 | 18.2 | 7.1 | 0.6 | 8.86 | 25.9% | 7.7% |
| KALSHI_LONE_OUTLIER | 20 | 5.0 | 5.0 | 75.0 | 5.0 | 5.0 | 5.0 | 0.0 | 5.8 | 10.0% | 5.0% |
| MARKETS_AGREE | 612 | 65.2 | 34.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.21 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,319 | 0.0 | 2.4 | 35.6 | 26.4 | 24.6 | 10.4 | 0.7 | 12.02 | 35.6% | 11.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 31,177 | 5022 (16.1%) | 26.3% | 0.9% | {"EXTERNAL_STALE": 3029, "AGREES_WITH_KALSHI": 1319, "ALL_AGREE": 612, "SUPPORTS_MODEL_DIRECTION": 25, "AGREES_WITH_MODEL": 20, "EXTERNAL_OUTLIER": 16, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,883 | 1275 (9.2%) | 36.9% | 1.6% | {"EXTERNAL_STALE": 785, "AGREES_WITH_KALSHI": 470, "SUPPORTS_MODEL_DIRECTION": 18, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,728 | 389 (5.0%) | 37.5% | 2.3% | {"EXTERNAL_STALE": 234, "AGREES_WITH_KALSHI": 146, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,773 | 366 (9.7%) | 38.0% | 2.5% | {"EXTERNAL_STALE": 218, "AGREES_WITH_KALSHI": 139, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,435 | 2827 (22.7%) | 17.7% | 0.8% | {"EXTERNAL_STALE": 1675, "ALL_AGREE": 612, "AGREES_WITH_KALSHI": 501, "AGREES_WITH_MODEL": 17, "EXTERNAL_OUTLIER": 16, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,933 | 10.3 | 7.6 | 19.5 | 14.6 | 22.2 | 15.9 | 9.9 | 14.09 | 48.1% | 25.9% |
| 4-10x | 4,028 | 11.1 | 8.3 | 18.9 | 15.3 | 21.6 | 14.8 | 10.0 | 13.76 | 46.4% | 24.8% |
| <2x | 15,893 | 15.0 | 9.8 | 19.1 | 16.5 | 17.6 | 13.1 | 9.1 | 11.83 | 39.6% | 22.1% |
| >=10x | 5,323 | 10.8 | 6.1 | 15.2 | 14.2 | 22.1 | 19.6 | 11.9 | 16.46 | 53.7% | 31.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,995 | 12.6 | 8.6 | 19.2 | 16.1 | 19.1 | 13.8 | 10.6 | 12.96 | 43.5% | 24.4% |
| 300-1000 | 6,564 | 11.6 | 8.6 | 17.4 | 15.3 | 20.7 | 16.2 | 10.2 | 13.91 | 47.1% | 26.4% |
| <300 | 10,145 | 8.5 | 5.6 | 15.4 | 14.8 | 23.2 | 20.1 | 12.3 | 17.02 | 55.7% | 32.4% |
| >=3000 | 6,473 | 21.3 | 13.0 | 23.5 | 16.5 | 14.1 | 6.9 | 4.7 | 7.92 | 25.7% | 11.6% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 878 | 0.5503 | 0.4123 | 0.5023 | +0.048 | -0.090 | -0.0046 ± 0.0052 |
| ratio 4-10x | 597 | 0.5891 | 0.4424 | 0.4975 | +0.092 | -0.055 | 0.0107 ± 0.0066 |
| ratio <2x | 2181 | 0.5382 | 0.4154 | 0.4475 | +0.091 | -0.032 | 0.0118 ± 0.0031 |
| ratio >=10x | 802 | 0.5713 | 0.3959 | 0.4613 | +0.110 | -0.066 | 0.0073 ± 0.0065 |
| thinner_sample 1000-3000 | 1215 | 0.542 | 0.4152 | 0.4494 | +0.093 | -0.034 | 0.0088 ± 0.0041 |
| thinner_sample 300-1000 | 1003 | 0.567 | 0.4232 | 0.4935 | +0.073 | -0.070 | 0.0001 ± 0.0051 |
| thinner_sample <300 | 1495 | 0.5622 | 0.3956 | 0.4642 | +0.098 | -0.069 | 0.0092 ± 0.0046 |
| thinner_sample >=3000 | 745 | 0.5359 | 0.4418 | 0.4685 | +0.067 | -0.027 | 0.0125 ± 0.0042 |
| data_status ADEQUATE | 1300 | 0.5378 | 0.434 | 0.4523 | +0.086 | -0.018 | 0.0114 ± 0.0034 |
| data_status LIMITED | 1019 | 0.5512 | 0.4168 | 0.4848 | +0.067 | -0.068 | 0.0029 ± 0.0047 |
| data_status POOR | 2139 | 0.5638 | 0.4023 | 0.4684 | +0.095 | -0.066 | 0.0075 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 654 | 0.2024 | 0.2033 | -0.0009 ± 0.0006 | 0.5859 | 0.5879 | 0.5016 | 0.4868 | 0.5214 | -0.072 ± 0.0186 | -0.01 (5) |
| 3-5 | 412 | 0.2052 | 0.2045 | +0.0007 ± 0.0018 | 0.5938 | 0.5908 | 0.5033 | 0.4633 | 0.4733 | -0.102 ± 0.0229 | 0.02 (1) |
| 5-10 | 923 | 0.2027 | 0.2021 | +0.0006 ± 0.0022 | 0.5921 | 0.5876 | 0.5124 | 0.4384 | 0.467 | -0.092 ± 0.0154 | -0.0167 (6) |
| 10-15 | 770 | 0.215 | 0.2056 | +0.0095 ± 0.0041 | 0.6206 | 0.593 | 0.5294 | 0.4052 | 0.4286 | -0.103 ± 0.0163 | -0.048 (5) |
| 15-25 | 1008 | 0.2251 | 0.214 | +0.0111 ± 0.0057 | 0.6448 | 0.6123 | 0.5786 | 0.3829 | 0.4524 | -0.092 ± 0.0145 | -0.0033 (9) |
| 25-40 | 575 | 0.2226 | 0.2108 | +0.0119 ± 0.0114 | 0.635 | 0.6051 | 0.6603 | 0.3504 | 0.4835 | -0.072 ± 0.0175 | -0.01 (1) |
| 40+ | 116 | 0.2743 | 0.202 | +0.0723 ± 0.036 | 0.7526 | 0.5904 | 0.7587 | 0.3114 | 0.4569 | -0.070 ± 0.0354 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3360 | 0.1857 | 0.1866 | -0.0010 ± 0.0003 | 0.547 | 0.5481 | 0.4915 | 0.4765 | 0.5098 | -0.022 ± 0.0075 | -0.0129 (17) |
| 3-5 | 2221 | 0.1992 | 0.1979 | +0.0014 ± 0.0008 | 0.5792 | 0.5735 | 0.4844 | 0.4444 | 0.4466 | -0.054 ± 0.0096 | 0.0 (2) |
| 5-10 | 4817 | 0.1983 | 0.1949 | +0.0034 ± 0.001 | 0.5804 | 0.5691 | 0.4827 | 0.4088 | 0.4223 | -0.048 ± 0.0064 | -0.0119 (21) |
| 10-15 | 4082 | 0.1979 | 0.1802 | +0.0177 ± 0.0017 | 0.5813 | 0.5314 | 0.4871 | 0.3627 | 0.3535 | -0.072 ± 0.0066 | -0.0281 (16) |
| 15-25 | 5135 | 0.2095 | 0.1701 | +0.0394 ± 0.0023 | 0.6126 | 0.503 | 0.5058 | 0.3095 | 0.3085 | -0.074 ± 0.0057 | -0.0025 (44) |
| 25-40 | 4023 | 0.2227 | 0.1294 | +0.0933 ± 0.0035 | 0.6395 | 0.3958 | 0.5326 | 0.2193 | 0.2309 | -0.058 ± 0.0055 | -0.01 (1) |
| 40+ | 2619 | 0.38 | 0.0456 | +0.3343 ± 0.0047 | 0.9897 | 0.1751 | 0.633 | 0.1068 | 0.0649 | -0.077 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 512 | 0.2088 | 0.2095 | -0.0007 ± 0.0007 | 0.6 | 0.6017 | 0.5073 | 0.4921 | 0.5195 | -0.101 ± 0.0218 | -0.01 (3) |
| 3-5 | 367 | 0.2259 | 0.223 | +0.0029 ± 0.002 | 0.6384 | 0.6325 | 0.516 | 0.4761 | 0.455 | -0.132 ± 0.0263 | 0.02 (1) |
| 5-10 | 807 | 0.2071 | 0.2067 | +0.0004 ± 0.0024 | 0.6006 | 0.5989 | 0.5473 | 0.4723 | 0.5105 | -0.082 ± 0.0165 | -0.01 (4) |
| 10-15 | 739 | 0.2176 | 0.2103 | +0.0073 ± 0.0042 | 0.6248 | 0.6065 | 0.5645 | 0.4402 | 0.475 | -0.110 ± 0.0176 | -0.04 (5) |
| 15-25 | 1035 | 0.2298 | 0.2105 | +0.0193 ± 0.0056 | 0.6523 | 0.6036 | 0.5872 | 0.3913 | 0.4444 | -0.099 ± 0.0146 | -0.0133 (9) |
| 25-40 | 722 | 0.2619 | 0.1993 | +0.0625 ± 0.0104 | 0.7303 | 0.5801 | 0.6535 | 0.3382 | 0.3989 | -0.110 ± 0.0163 | -0.0075 (4) |
| 40+ | 276 | 0.3548 | 0.1732 | +0.1816 ± 0.0247 | 0.9757 | 0.5174 | 0.7339 | 0.2501 | 0.3188 | -0.068 ± 0.024 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2856 | 0.1951 | 0.1954 | -0.0003 ± 0.0003 | 0.5669 | 0.5674 | 0.5118 | 0.4968 | 0.5123 | -0.043 ± 0.0086 | -0.0133 (15) |
| 3-5 | 1912 | 0.2002 | 0.1992 | +0.0010 ± 0.0008 | 0.5783 | 0.5757 | 0.515 | 0.4751 | 0.4822 | -0.047 ± 0.0104 | 0.02 (1) |
| 5-10 | 4261 | 0.1967 | 0.1945 | +0.0022 ± 0.001 | 0.5782 | 0.5685 | 0.511 | 0.4369 | 0.4619 | -0.036 ± 0.0068 | -0.0117 (6) |
| 10-15 | 3699 | 0.2022 | 0.1899 | +0.0123 ± 0.0018 | 0.5913 | 0.5531 | 0.5132 | 0.3893 | 0.4023 | -0.057 ± 0.0073 | -0.0189 (18) |
| 15-25 | 5110 | 0.2161 | 0.1788 | +0.0373 ± 0.0023 | 0.6275 | 0.5255 | 0.525 | 0.3291 | 0.3358 | -0.067 ± 0.006 | -0.0086 (42) |
| 25-40 | 4685 | 0.2514 | 0.1368 | +0.1146 ± 0.0034 | 0.7071 | 0.4202 | 0.5576 | 0.2405 | 0.2209 | -0.085 ± 0.0054 | -0.0044 (18) |
| 40+ | 3734 | 0.3926 | 0.0607 | +0.3318 ± 0.0046 | 1.0334 | 0.2169 | 0.6504 | 0.1191 | 0.0854 | -0.071 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 621 | 0.2002 | 0.2023 | -0.0021 ± 0.0006 | 0.5812 | 0.5864 | 0.5012 | 0.4861 | 0.5459 | -0.035 ± 0.0188 | -0.0137 (8) |
| 3-5 | 445 | 0.2029 | 0.2012 | +0.0017 ± 0.0017 | 0.5891 | 0.5837 | 0.5058 | 0.4661 | 0.4674 | -0.117 ± 0.0222 | 0.0067 (3) |
| 5-10 | 947 | 0.2024 | 0.1988 | +0.0036 ± 0.0022 | 0.5911 | 0.579 | 0.5085 | 0.4346 | 0.4456 | -0.105 ± 0.0149 | -0.0071 (7) |
| 10-15 | 770 | 0.2095 | 0.2061 | +0.0033 ± 0.0041 | 0.6081 | 0.5947 | 0.5397 | 0.4161 | 0.4662 | -0.083 ± 0.0163 | -0.0317 (6) |
| 15-25 | 955 | 0.2308 | 0.2141 | +0.0167 ± 0.0058 | 0.6592 | 0.612 | 0.5896 | 0.3951 | 0.4492 | -0.105 ± 0.0149 | -0.03 (1) |
| 25-40 | 598 | 0.2141 | 0.219 | -0.0049 ± 0.0112 | 0.6179 | 0.6241 | 0.6708 | 0.3597 | 0.5201 | -0.054 ± 0.0172 | 0.015 (2) |
| 40+ | 122 | 0.2899 | 0.2134 | +0.0764 ± 0.0363 | 0.8007 | 0.6154 | 0.769 | 0.3195 | 0.4672 | -0.069 ± 0.0382 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3276 | 0.1853 | 0.1859 | -0.0006 ± 0.0003 | 0.5453 | 0.5462 | 0.4901 | 0.475 | 0.4902 | -0.037 ± 0.0076 | -0.0163 (35) |
| 3-5 | 2234 | 0.1955 | 0.1935 | +0.0020 ± 0.0008 | 0.5737 | 0.5672 | 0.4875 | 0.4479 | 0.4432 | -0.064 ± 0.0095 | -0.0094 (18) |
| 5-10 | 4895 | 0.1956 | 0.1897 | +0.0059 ± 0.0009 | 0.5749 | 0.5558 | 0.4834 | 0.4094 | 0.4072 | -0.062 ± 0.0063 | -0.01 (31) |
| 10-15 | 3968 | 0.1924 | 0.1773 | +0.0151 ± 0.0017 | 0.5686 | 0.5235 | 0.4995 | 0.3761 | 0.376 | -0.064 ± 0.0067 | -0.015 (12) |
| 15-25 | 5302 | 0.2113 | 0.1728 | +0.0385 ± 0.0022 | 0.6169 | 0.5093 | 0.5153 | 0.3203 | 0.3197 | -0.072 ± 0.0057 | -0.03 (2) |
| 25-40 | 4036 | 0.2196 | 0.1333 | +0.0864 ± 0.0036 | 0.6336 | 0.4041 | 0.538 | 0.2219 | 0.245 | -0.050 ± 0.0055 | 0.01 (3) |
| 40+ | 2546 | 0.3951 | 0.0503 | +0.3448 ± 0.005 | 1.0323 | 0.1873 | 0.6454 | 0.1135 | 0.0691 | -0.081 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1011 | 0.1955 | 0.1957 | -0.0002 ± 0.0005 | 0.5703 | 0.5704 | 0.5028 | 0.4877 | 0.4955 | -0.057 ± 0.0141 | -0.0224 (49) |
| 3-5 | 703 | 0.1927 | 0.1919 | +0.0008 ± 0.0013 | 0.5631 | 0.5599 | 0.4908 | 0.451 | 0.458 | -0.061 ± 0.0169 | -0.0194 (34) |
| 5-10 | 1470 | 0.2026 | 0.1966 | +0.0060 ± 0.0017 | 0.5945 | 0.5756 | 0.4958 | 0.4224 | 0.419 | -0.075 ± 0.0118 | -0.005 (78) |
| 10-15 | 975 | 0.2113 | 0.1992 | +0.0121 ± 0.0036 | 0.612 | 0.5807 | 0.5231 | 0.4 | 0.4103 | -0.071 ± 0.0146 | 0.0014 (64) |
| 15-25 | 1315 | 0.2313 | 0.2111 | +0.0202 ± 0.005 | 0.6607 | 0.6073 | 0.5785 | 0.3838 | 0.4304 | -0.072 ± 0.0127 | -0.0214 (59) |
| 25-40 | 795 | 0.2467 | 0.2078 | +0.0390 ± 0.0099 | 0.7012 | 0.5971 | 0.6751 | 0.3626 | 0.4566 | -0.085 ± 0.0151 | -0.0219 (26) |
| 40+ | 263 | 0.3519 | 0.2022 | +0.1497 ± 0.0273 | 1.0166 | 0.5918 | 0.8077 | 0.3256 | 0.4297 | -0.091 ± 0.0252 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3333 | 0.1832 | 0.1834 | -0.0002 ± 0.0003 | 0.5396 | 0.5392 | 0.5039 | 0.4886 | 0.4992 | -0.038 ± 0.0075 | -0.0157 (88) |
| 3-5 | 2302 | 0.1955 | 0.1936 | +0.0019 ± 0.0007 | 0.5702 | 0.5657 | 0.498 | 0.4583 | 0.4535 | -0.055 ± 0.0093 | -0.0209 (69) |
| 5-10 | 4586 | 0.1973 | 0.189 | +0.0084 ± 0.001 | 0.5803 | 0.5556 | 0.4906 | 0.4171 | 0.3999 | -0.072 ± 0.0065 | -0.0082 (132) |
| 10-15 | 3207 | 0.2077 | 0.1918 | +0.0159 ± 0.0019 | 0.6041 | 0.5624 | 0.5293 | 0.4061 | 0.4022 | -0.066 ± 0.0078 | -0.0053 (105) |
| 15-25 | 3993 | 0.2298 | 0.2005 | +0.0293 ± 0.0028 | 0.6627 | 0.5806 | 0.5705 | 0.3751 | 0.3989 | -0.064 ± 0.0071 | -0.0253 (107) |
| 25-40 | 2742 | 0.2587 | 0.1846 | +0.0741 ± 0.0052 | 0.7331 | 0.5383 | 0.6333 | 0.3194 | 0.3611 | -0.077 ± 0.008 | -0.0229 (51) |
| 40+ | 1213 | 0.3781 | 0.1455 | +0.2326 ± 0.0115 | 1.071 | 0.4386 | 0.7302 | 0.2264 | 0.2605 | -0.070 ± 0.0103 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4458 | 1.032 ± 0.042 | 1.109 | 0.1685 | 0.1634 | 0.2145 | 0.2069 |
| gen2 | 4458 | 0.836 ± 0.039 | 1.078 | 0.1678 | 0.1641 | 0.2339 | 0.2066 |
| gen1_elo | 4458 | 1.004 ± 0.04 | 1.106 | 0.1753 | 0.1635 | 0.2134 | 0.2072 |
| gen1_sr | 4458 | 1.021 ± 0.051 | 1.15 | 0.1291 | 0.166 | 0.2301 | 0.2062 |
| gen1_ledger | 6532 | 0.859 ± 0.03 | 1.062 | 0.1834 | 0.1778 | 0.2189 | 0.2008 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 22,289)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,071 | 22.8% |
| STALE_QUOTE | market_freshness | 4,817 | 21.6% |
| BOOK_QUALITY | execution | 4,242 | 19.0% |
| POOR_DATA | data | 2,500 | 11.2% |
| LIMITED_DATA | data | 1,389 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,203 | 5.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,070 | 4.8% |
| IDENTITY_AMBIGUOUS | mapping | 947 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 657 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 392 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.8%, market_freshness 21.6%, execution 19.0%, data 17.4%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.8%, mapping 4.2%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.0%, LOW_DATA_QUALITY 70.6%, THIN_PLAYER_HISTORY 59.4%, STALE_PLAYER_DATA 49.5%, STALE_KALSHI_QUOTE 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 33.3%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.6%, LEVEL_TRANSFER_RISK 10.8%, EVENT_MAPPING_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 3.9%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.3%, POST_SETTLEMENT_OBSERVATION 22.8%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,926)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,080 | 34.2% |
| STALE_QUOTE | market_freshness | 2,230 | 18.7% |
| BOOK_QUALITY | execution | 2,228 | 18.7% |
| POOR_DATA | data | 1,019 | 8.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 644 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 530 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 419 | 3.5% |
| LIMITED_DATA | data | 417 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 267 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 91 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.2%, market_freshness 18.7%, execution 18.7%, data 12.0%, market_freshness/coverage 8.9%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.1%, THIN_PLAYER_HISTORY 61.5%, STALE_KALSHI_QUOTE 52.0%, STALE_PLAYER_DATA 44.0%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 24.5%, PLAYER_IDENTITY_RISK 20.1%, MODEL_HIGH_UNCERTAINTY 18.3%, EVENT_MAPPING_RISK 10.0%, LEVEL_TRANSFER_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.3%, POST_SETTLEMENT_OBSERVATION 34.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9232, "IDENTITY_AMBIGUOUS": 2694}; ticker orientation: {"VERIFIED": 11926}.

Checks: discipline:AMBIGUOUS 842, discipline:PASS 11084, identity_confidence:AMBIGUOUS 2391, identity_confidence:PASS 9535, level_mapping:NA 854, level_mapping:PASS 11072, market_pair:AMBIGUOUS 456, market_pair:NA 296, market_pair:PASS 11174, model_complement:NA 263, model_complement:PASS 11663, namesake:AMBIGUOUS 6, namesake:PASS 11920, physical_match_id:NA 4198, physical_match_id:PASS 7728, player_ids:PASS 11926, same_pair_other_event:PASS 11926, ticker_orientation:PASS 11926

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,594 | 4.5% | 4.0% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 48, "data": 35, "execution": 23, "model_calibration": 19, "market_freshness/coverage": 15, "coverage": 13} | 5.92 | 0.2224 / 0.2181 (519) | 18.9% | 3.4% | 3.2% | 2.7% |
| CHALLENGER | 8,317 | 17.0% | 7.0% | 11.9% | {"coverage": 792, "market_freshness/coverage": 171, "market_freshness": 160, "data": 144, "model_calibration_or_unknown": 71, "execution": 33, "model_calibration": 30, "mapping": 15, "possible_market_error": 1} | 7.61 | 0.2195 / 0.2095 (1934) | 34.3% | 17.7% | 4.0% | 22.2% |
| DOUBLES | 1,770 | 47.6% | 47.3% | 7.1% | {"execution": 464, "mapping": 210, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.85 | 0.3098 / 0.2359 (434) | 13.2% | 0.0% | 100.0% | 6.8% |
| ITF_MEN | 14,796 | 25.5% | 17.7% | 31.6% | {"coverage": 1405, "execution": 716, "market_freshness": 645, "data": 497, "market_freshness/coverage": 329, "mapping": 176, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.94 | 0.2163 / 0.1985 (3306) | 37.4% | 69.8% | 19.8% | 22.3% |
| ITF_WOMEN | 19,528 | 27.2% | 19.9% | 44.5% | {"coverage": 1838, "market_freshness": 1165, "execution": 941, "data": 721, "market_freshness/coverage": 444, "mapping": 123, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.9 | 0.2036 / 0.1952 (3746) | 39.7% | 56.3% | 10.0% | 22.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,189 | 5.4% | 4.9% | 1.5% | {"market_freshness": 60, "model_calibration_or_unknown": 36, "execution": 26, "model_calibration": 16, "data": 12, "coverage": 12, "market_freshness/coverage": 10, "mapping": 1} | 7.66 | 0.2327 / 0.2282 (521) | 24.4% | 1.3% | 1.7% | 3.5% |
| WTA125 | 1,491 | 12.9% | 10.5% | 1.6% | {"model_calibration_or_unknown": 39, "market_freshness": 39, "market_freshness/coverage": 38, "data": 27, "execution": 20, "model_calibration": 13, "coverage": 12, "mapping": 4} | 9.69 | 0.219 / 0.2065 (488) | 22.9% | 11.0% | 7.2% | 9.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
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
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 25 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 43 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXWTADOUBLES-26OCT25DABSTEBUCFER-BUCFER` | DOUBLES | gen1_ledger | 93% / 16% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9682, "by_level_share_of_ge_25pp": {"ATP": 0.0173, "CHALLENGER": 0.1188, "DOUBLES": 0.0706, "ITF_MEN": 0.3163, "ITF_WOMEN": 0.4454, "OTHER": 0.001, "WTA": 0.0145, "WTA125": 0.0161}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.52, "share_primary_cause_market_settled_or_in_play": 0.4312, "share_primary_cause_stale_quote_only": 0.187}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11926, "identity_ambiguous_share": 0.2259, "ticker_orientation": {"VERIFIED": 11926}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7728, "with_external": 389, "coverage": 0.0503, "external_status": {"EXTERNAL_STALE": 234, "AGREES_WITH_KALSHI": 146, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 234, "MODEL_LONE_OUTLIER": 146, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3753, "share_external_supports_model": 0.0231}, "pregame_clean_ge_25pp": {"n": 3773, "with_external": 366, "coverage": 0.097, "external_status": {"EXTERNAL_STALE": 218, "AGREES_WITH_KALSHI": 139, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 218, "MODEL_LONE_OUTLIER": 139, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3798, "share_external_supports_model": 0.0246}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.41, "median_min_matches": 21.0, "median_max_days_since_last": 227.0, "share_severe_asymmetry": 0.2143, "data_status": {"POOR": 6604, "LIMITED": 3138, "ADEQUATE": 2184}, "comparison_lt_10pp": {"median_thinner_serve_points": 1759.0, "median_sample_ratio": 1.68, "median_min_matches": 98.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 878, "model_minus_observed": 0.048, "kalshi_minus_observed": -0.09, "brier_diff_model_minus_kalshi": -0.0046}, "4-10x": {"n": 597, "model_minus_observed": 0.0916, "kalshi_minus_observed": -0.0551, "brier_diff_model_minus_kalshi": 0.0107}, "<2x": {"n": 2181, "model_minus_observed": 0.0907, "kalshi_minus_observed": -0.0321, "brier_diff_model_minus_kalshi": 0.0118}, ">=10x": {"n": 802, "model_minus_observed": 0.1099, "kalshi_minus_observed": -0.0655, "brier_diff_model_minus_kalshi": 0.0073}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4458, "model": {"intercept": -0.533, "slope": 0.836, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.211, "slope": 1.078, "slope_se": 0.043}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1641, "model_brier": 0.2339, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": 0.0273, "brier_diff_se": 0.0028, "model_logloss": 0.6639, "kalshi_logloss": 0.5962}, "fair_v1": {"n": 4458, "model": {"intercept": -0.417, "slope": 1.032, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.285, "slope": 1.109, "slope_se": 0.044}, "mean_extremity_model": 0.1685, "mean_extremity_kalshi": 0.1634, "model_brier": 0.2145, "kalshi_brier": 0.2069, "brier_diff_model_minus_kalshi": 0.0076, "brier_diff_se": 0.0023, "model_logloss": 0.6179, "kalshi_logloss": 0.5968}, "gen1_elo": {"n": 4458, "model": {"intercept": -0.391, "slope": 1.004, "slope_se": 0.04}, "kalshi_mid_same_rows": {"intercept": 0.307, "slope": 1.106, "slope_se": 0.043}, "mean_extremity_model": 0.1753, "mean_extremity_kalshi": 0.1635, "model_brier": 0.2134, "kalshi_brier": 0.2072, "brier_diff_model_minus_kalshi": 0.0062, "brier_diff_se": 0.0024, "model_logloss": 0.6164, "kalshi_logloss": 0.5973}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2479, "share_ge_15": 0.4453, "median_abs_gap": 13.14, "n": 31177}, "gen1_elo": {"share_ge_25": 0.2456, "share_ge_15": 0.4443, "median_abs_gap": 13.0, "n": 31177}, "gen1_sr": {"share_ge_25": 0.3159, "share_ge_15": 0.5236, "median_abs_gap": 15.98, "n": 31177}, "gen2": {"share_ge_25": 0.3195, "share_ge_15": 0.5137, "median_abs_gap": 15.58, "n": 31177}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1556, "share_ge_15": 0.3615, "median_abs_gap": 10.94, "n": 24238}, "gen1_elo": {"share_ge_25": 0.1568, "share_ge_15": 0.3593, "median_abs_gap": 10.73, "n": 24235}, "gen1_sr": {"share_ge_25": 0.2228, "share_ge_15": 0.4458, "median_abs_gap": 13.09, "n": 24239}, "gen2": {"share_ge_25": 0.2391, "share_ge_15": 0.4454, "median_abs_gap": 13.07, "n": 24240}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.92, "share_ge_25_all": 0.0448, "share_ge_25_pregame_clean": 0.0398}, "WTA": {"median_abs_gap_pregame_clean": 7.66, "share_ge_25_all": 0.0542, "share_ge_25_pregame_clean": 0.0491}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.234, "share_within_10pp_all": 0.4321, "share_within_10pp_pregame_clean": 0.4843, "corr_model_vs_mid_pregame_clean": 0.8426}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 654, "model_brier": 0.2024, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 770, "model_brier": 0.215, "kalshi_brier": 0.2056, "brier_diff_model_minus_kalshi": 0.0095}, "15-25": {"n_settled": 1008, "model_brier": 0.2251, "kalshi_brier": 0.214, "brier_diff_model_minus_kalshi": 0.0111}, "25-40": {"n_settled": 575, "model_brier": 0.2226, "kalshi_brier": 0.2108, "brier_diff_model_minus_kalshi": 0.0119}, "3-5": {"n_settled": 412, "model_brier": 0.2052, "kalshi_brier": 0.2045, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 116, "model_brier": 0.2743, "kalshi_brier": 0.202, "brier_diff_model_minus_kalshi": 0.0723}, "5-10": {"n_settled": 923, "model_brier": 0.2027, "kalshi_brier": 0.2021, "brier_diff_model_minus_kalshi": 0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.533, "slope": 0.836, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.211, "slope": 1.078, "slope_se": 0.043}, "n": 4458}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.504, "slope": 0.859, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.153, "slope": 1.062, "slope_se": 0.034}, "n": 6532}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 434, "model_brier": 0.3098, "kalshi_brier": 0.2359, "brier_diff_model_minus_kalshi": 0.074, "brier_diff_se": 0.0145, "corr_model_outcome": 0.0408, "corr_kalshi_outcome": 0.2531}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
