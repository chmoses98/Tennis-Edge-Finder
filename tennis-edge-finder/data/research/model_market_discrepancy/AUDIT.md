# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-11T08:06Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 88,085): 0-3 14.0%, 3-5 9.5%, 5-10 20.2%, 10-15 15.2%, 15-25 19.2%, 25-40 13.7%, 40+ 8.2%; median gap 11.88 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.0%, Challenger 11.2%, doubles 6.5%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 19,347): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.7%, STALE_QUOTE 20.2%, BOOK_QUALITY 16.6%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.7%, market_freshness 20.2%, execution 16.6%, data 12.4%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 19,347 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.8% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.2% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 479.0 points vs 1701.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.016, Gen-2 0.813, Gen-1 ledger 0.865 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 976 model 0.2263 vs Kalshi 0.2042; n 202 model 0.3039 vs Kalshi 0.1707.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 368,275 model-market comparisons (607,382 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 121,889 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-11T07:44:30.506539+00:00'], shadow board 101,633 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-11T07:44:34.850048+00:00'], Model 4 43,870 rows, 30,331 settled tickers, 11,479 tickers with an external scan.
* By model: {"gen1_ledger": 81697, "gen1_elo": 51074, "fair_v1": 51074, "gen2": 51074, "gen1_sr": 51074, "model4_fundamental": 41183, "model4_conditioned": 41099}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 88,085 | 14.0 | 9.5 | 20.2 | 15.2 | 19.2 | 13.7 | 8.2 | 11.88 | 41.1% | 22.0% |
| MW fair_v1 | 51,074 | 12.7 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.2 | 13.12 | 44.7% | 25.2% |
| MW gen1_elo | 51,074 | 12.4 | 8.8 | 19.2 | 15.3 | 19.4 | 14.9 | 10.0 | 12.97 | 44.3% | 24.9% |
| MW gen1_ledger | 37,011 | 15.8 | 10.8 | 22.1 | 15.1 | 18.6 | 11.9 | 5.6 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 51,074 | 9.9 | 7.2 | 16.6 | 13.9 | 20.8 | 18.7 | 12.7 | 15.92 | 52.3% | 31.5% |
| MW gen2 | 51,074 | 10.9 | 7.6 | 16.7 | 13.7 | 19.6 | 17.7 | 13.8 | 15.48 | 51.1% | 31.5% |
| all families model4_conditioned | 41,099 | 22.2 | 17.9 | 34.5 | 16.9 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 41,183 | 17.3 | 13.5 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.61 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.3%, >=15pp 41.1%, >=20pp 30.3%, >=25pp 22.0%, >=30pp 15.9%, >=40pp 8.2%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.51pp; >=10pp 45.4%, >=25pp 17.4%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,094 | 28.0 | 15.8 | 28.0 | 13.3 | 10.7 | 3.6 | 0.6 | 5.81 | 14.9% | 4.2% |
| CHALLENGER | 8,106 | 16.4 | 9.6 | 20.6 | 15.2 | 15.9 | 11.5 | 10.9 | 10.93 | 38.3% | 22.4% |
| ITF_MEN | 14,690 | 9.6 | 7.3 | 17.0 | 14.9 | 21.1 | 17.3 | 12.7 | 15.45 | 51.1% | 30.0% |
| ITF_WOMEN | 19,765 | 9.5 | 7.0 | 16.1 | 14.7 | 22.1 | 18.6 | 11.9 | 15.96 | 52.7% | 30.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,086 | 16.7 | 13.2 | 25.1 | 20.7 | 16.5 | 6.7 | 1.1 | 8.56 | 24.3% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,094 | 26.4 | 15.7 | 26.3 | 15.7 | 11.3 | 3.9 | 0.8 | 6.09 | 16.0% | 4.7% |
| CHALLENGER | 8,106 | 14.4 | 9.0 | 19.1 | 13.8 | 18.5 | 13.7 | 11.4 | 12.5 | 43.6% | 25.2% |
| ITF_MEN | 14,690 | 8.1 | 6.2 | 15.0 | 13.9 | 20.3 | 20.1 | 16.4 | 17.9 | 56.9% | 36.6% |
| ITF_WOMEN | 19,765 | 7.9 | 5.9 | 14.2 | 12.7 | 20.6 | 21.2 | 17.6 | 19.07 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,086 | 14.1 | 10.4 | 21.7 | 16.2 | 22.4 | 12.7 | 2.5 | 11.18 | 37.6% | 15.2% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,094 | 23.3 | 14.1 | 25.6 | 15.5 | 14.4 | 6.0 | 1.1 | 7.06 | 21.5% | 7.1% |
| CHALLENGER | 8,106 | 15.0 | 9.6 | 20.8 | 15.5 | 16.2 | 12.0 | 10.9 | 11.3 | 39.1% | 22.9% |
| ITF_MEN | 14,690 | 9.4 | 7.2 | 17.1 | 14.2 | 21.6 | 17.4 | 13.1 | 15.81 | 52.0% | 30.4% |
| ITF_WOMEN | 19,765 | 9.2 | 6.9 | 16.3 | 15.7 | 22.1 | 18.6 | 11.3 | 15.62 | 51.9% | 29.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,086 | 22.6 | 17.1 | 31.9 | 15.3 | 8.8 | 3.3 | 1.0 | 6.12 | 13.1% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,469 | 28.1 | 19.5 | 29.2 | 12.2 | 8.1 | 2.5 | 0.5 | 5.24 | 11.1% | 3.0% |
| CHALLENGER | 4,957 | 22.7 | 14.5 | 28.0 | 14.7 | 13.1 | 5.5 | 1.5 | 7.03 | 20.1% | 7.0% |
| DOUBLES | 2,705 | 4.8 | 4.5 | 12.9 | 11.0 | 20.6 | 24.6 | 21.6 | 23.06 | 66.7% | 46.1% |
| ITF_MEN | 10,803 | 12.7 | 9.4 | 21.4 | 15.5 | 21.8 | 13.0 | 6.1 | 11.88 | 40.9% | 19.1% |
| ITF_WOMEN | 12,857 | 13.5 | 9.3 | 19.7 | 15.7 | 21.6 | 14.7 | 5.4 | 12.2 | 41.7% | 20.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,815 | 24.1 | 16.0 | 31.5 | 16.9 | 8.9 | 2.5 | 0.2 | 6.44 | 11.6% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,966 | 28.5 | 16.0 | 28.4 | 13.2 | 10.5 | 3.1 | 0.3 | 5.64 | 13.9% | 3.4% |
| CHALLENGER | 5,687 | 21.1 | 12.0 | 25.7 | 18.0 | 15.9 | 5.7 | 1.6 | 8.2 | 23.2% | 7.3% |
| ITF_MEN | 10,736 | 11.8 | 8.6 | 20.4 | 17.2 | 22.2 | 14.1 | 5.5 | 12.51 | 41.8% | 19.7% |
| ITF_WOMEN | 14,491 | 11.4 | 8.5 | 19.0 | 17.0 | 24.0 | 15.4 | 4.7 | 13.16 | 44.1% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,972 | 17.0 | 13.3 | 25.4 | 21.0 | 16.5 | 6.2 | 0.6 | 8.42 | 23.3% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,966 | 26.7 | 16.0 | 26.6 | 15.7 | 11.2 | 3.5 | 0.4 | 6.01 | 15.0% | 3.8% |
| CHALLENGER | 5,687 | 18.3 | 11.6 | 24.0 | 16.2 | 19.0 | 9.1 | 1.9 | 8.96 | 29.9% | 10.9% |
| ITF_MEN | 10,737 | 9.5 | 7.3 | 17.5 | 16.0 | 22.2 | 18.3 | 9.2 | 14.91 | 49.6% | 27.5% |
| ITF_WOMEN | 14,492 | 8.9 | 7.0 | 16.0 | 14.3 | 22.5 | 20.6 | 10.8 | 16.51 | 53.8% | 31.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,972 | 14.3 | 10.5 | 21.9 | 16.4 | 22.5 | 12.4 | 1.9 | 11.03 | 36.8% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,400 | 28.4 | 19.7 | 29.2 | 12.3 | 7.8 | 2.3 | 0.3 | 5.21 | 10.5% | 2.7% |
| CHALLENGER | 4,384 | 24.0 | 15.4 | 29.2 | 14.8 | 12.4 | 3.8 | 0.4 | 6.58 | 16.6% | 4.2% |
| DOUBLES | 2,538 | 4.7 | 4.5 | 13.2 | 11.1 | 20.5 | 24.5 | 21.6 | 23.0 | 66.5% | 46.1% |
| ITF_MEN | 9,322 | 13.5 | 10.0 | 22.8 | 16.1 | 21.9 | 11.5 | 4.2 | 11.04 | 37.6% | 15.7% |
| ITF_WOMEN | 11,081 | 14.2 | 9.8 | 20.8 | 16.2 | 21.8 | 13.6 | 3.6 | 11.44 | 39.0% | 17.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,752 | 24.4 | 16.4 | 31.4 | 16.8 | 8.8 | 2.0 | 0.1 | 6.42 | 10.9% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,705 | 4.8 | 4.5 | 12.9 | 11.0 | 20.6 | 24.6 | 21.6 | 23.06 | 66.7% | 46.1% |
| singles | 34,306 | 16.7 | 11.3 | 22.9 | 15.4 | 18.4 | 11.0 | 4.3 | 9.76 | 33.7% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 10,800 | 12.7 | 8.9 | 19.5 | 15.2 | 19.6 | 14.3 | 9.6 | 12.82 | 43.6% | 23.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 33,322 | 13.2 | 8.7 | 18.9 | 15.1 | 19.1 | 15.0 | 10.2 | 12.95 | 44.2% | 25.1% |
| UNKNOWN | 6,539 | 10.4 | 7.5 | 17.0 | 16.4 | 21.6 | 15.9 | 11.3 | 14.48 | 48.8% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,361 | 19.3 | 11.8 | 22.4 | 15.8 | 14.8 | 9.5 | 6.4 | 8.99 | 30.6% | 15.9% |
| B | 6,176 | 12.9 | 8.4 | 19.7 | 15.3 | 19.7 | 12.5 | 11.5 | 12.81 | 43.7% | 24.0% |
| C | 7,206 | 12.0 | 8.6 | 19.5 | 16.0 | 18.9 | 14.6 | 10.4 | 12.9 | 43.9% | 25.1% |
| D | 8,303 | 11.6 | 8.4 | 17.9 | 15.0 | 22.0 | 15.7 | 9.5 | 13.97 | 47.2% | 25.2% |
| F | 15,028 | 7.3 | 5.7 | 14.9 | 14.4 | 23.0 | 21.1 | 13.5 | 18.01 | 57.7% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,794 | 24.9 | 15.9 | 28.9 | 14.9 | 10.6 | 3.5 | 1.2 | 6.35 | 15.3% | 4.7% |
| B | 5,063 | 16.6 | 10.9 | 24.3 | 16.9 | 18.9 | 9.4 | 3.0 | 9.6 | 31.3% | 12.4% |
| C | 7,264 | 11.0 | 7.8 | 19.6 | 14.9 | 21.1 | 15.5 | 10.1 | 13.49 | 46.8% | 25.6% |
| D | 5,603 | 14.6 | 10.0 | 21.0 | 15.3 | 20.9 | 12.7 | 5.5 | 11.33 | 39.1% | 18.1% |
| F | 9,287 | 10.2 | 8.3 | 16.4 | 14.4 | 23.5 | 19.1 | 8.0 | 15.31 | 50.6% | 27.1% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,270 | 17.7 | 10.8 | 21.5 | 15.6 | 15.1 | 10.2 | 9.1 | 10.0 | 34.5% | 19.3% |
| LIMITED | 11,076 | 13.5 | 9.5 | 20.5 | 16.0 | 19.6 | 13.4 | 7.6 | 11.91 | 40.5% | 21.0% |
| POOR | 23,728 | 8.9 | 6.7 | 16.0 | 14.7 | 22.6 | 19.1 | 12.1 | 16.32 | 53.8% | 31.2% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,230 | 23.7 | 18.1 | 33.0 | 15.5 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,903 | 22.8 | 15.3 | 32.0 | 16.8 | 9.1 | 3.3 | 0.7 | 6.69 | 13.1% | 4.0% |
| MATCH_WINNER | 37,011 | 15.8 | 10.8 | 22.1 | 15.1 | 18.6 | 11.9 | 5.6 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,976 | 28.4 | 16.8 | 30.7 | 12.7 | 8.9 | 2.3 | 0.3 | 5.58 | 11.5% | 2.7% |
| TOTAL_GAMES | 11,553 | 9.7 | 10.8 | 36.2 | 25.8 | 10.4 | 4.2 | 2.9 | 9.15 | 17.5% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,617 | 24.4 | 28.7 | 33.4 | 8.1 | 4.0 | 1.2 | 0.3 | 4.8 | 5.4% | 1.4% |
| GAME_SPREAD | 9,507 | 46.7 | 15.9 | 25.1 | 7.4 | 2.4 | 1.9 | 0.6 | 3.32 | 4.9% | 2.5% |
| TOTAL_GAMES | 16,975 | 6.6 | 9.8 | 40.7 | 29.9 | 7.3 | 3.3 | 2.4 | 9.17 | 13.0% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,653 | 23.8 | 16.6 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.06 | 10.1% | 3.2% |
| GAME_SPREAD | 9,516 | 20.4 | 13.4 | 28.4 | 20.1 | 12.1 | 4.4 | 1.2 | 7.69 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,014 | 10.0 | 10.8 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.02 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 51,074 | 44.7% | 25.2% | 13.12 | 35.5% | 15.2% | 10.71 |
| gen1_elo | 51,074 | 44.3% | 24.9% | 12.97 | 35.0% | 15.0% | 10.51 |
| gen1_sr | 51,074 | 52.3% | 31.5% | 15.92 | 44.0% | 21.6% | 12.99 |
| gen2 | 51,074 | 51.1% | 31.5% | 15.48 | 43.9% | 23.1% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,098 | 15.5 | 10.4 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 30,976 | 10.9 | 7.4 | 17.0 | 13.9 | 19.2 | 17.0 | 14.6 | 15.33 | 50.8% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 30,479 | 16.4 | 11.1 | 22.6 | 15.2 | 18.2 | 11.5 | 5.0 | 9.96 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 88,085 | 30479 | 23570 | 34036 | 25.1 | 135.7 | 1451.1 |
| ge_15pp | 36,223 | 10571 | 8394 | 17258 | 28.8 | 443.1 | 1451.1 |
| ge_25pp | 19,347 | 5019 | 3666 | 10662 | 34.5 | 592.3 | 1431.1 |
| lt_10pp | 38,488 | 15282 | 11149 | 12057 | 22.8 | 49.5 | 1421.7 |

Current slate `SL-20261111T080600Z-dacac2bd`: 587 priced rows, quote age at build {'median': 65.1, 'max': 106.7}, freshness {'STALE': 587}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,908 | 19.2 | 11.1 | 25.4 | 18.2 | 17.9 | 7.3 | 0.9 | 8.8 | 26.1% | 8.2% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,069 | 66.4 | 33.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,272 | 0.0 | 2.2 | 38.6 | 25.9 | 23.8 | 8.7 | 0.9 | 11.65 | 33.4% | 9.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 51,074 | 8362 (16.4%) | 27.2% | 1.0% | {"EXTERNAL_STALE": 4908, "AGREES_WITH_KALSHI": 2272, "ALL_AGREE": 1069, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 22,853 | 2068 (9.0%) | 36.6% | 1.5% | {"EXTERNAL_STALE": 1279, "AGREES_WITH_KALSHI": 758, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 12,866 | 634 (4.9%) | 34.4% | 2.1% | {"EXTERNAL_STALE": 403, "AGREES_WITH_KALSHI": 218, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,953 | 603 (10.1%) | 35.0% | 2.2% | {"EXTERNAL_STALE": 379, "AGREES_WITH_KALSHI": 211, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 20,437 | 4804 (23.5%) | 19.3% | 0.9% | {"EXTERNAL_STALE": 2734, "ALL_AGREE": 1069, "AGREES_WITH_KALSHI": 926, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,993 | 10.7 | 7.5 | 19.1 | 14.3 | 21.7 | 16.4 | 10.2 | 14.3 | 48.4% | 26.6% |
| 4-10x | 6,822 | 11.2 | 8.7 | 18.0 | 14.9 | 21.8 | 14.7 | 10.8 | 14.03 | 47.3% | 25.5% |
| <2x | 26,110 | 14.7 | 9.6 | 19.9 | 16.0 | 17.5 | 13.3 | 9.0 | 11.6 | 39.8% | 22.3% |
| >=10x | 8,149 | 10.2 | 6.5 | 15.1 | 14.3 | 21.6 | 19.1 | 13.3 | 16.52 | 54.0% | 32.4% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,429 | 12.4 | 8.4 | 19.8 | 16.2 | 19.0 | 13.6 | 10.5 | 12.79 | 43.2% | 24.1% |
| 300-1000 | 11,001 | 11.7 | 8.7 | 17.8 | 15.0 | 20.8 | 16.3 | 9.6 | 13.76 | 46.7% | 25.9% |
| <300 | 16,162 | 8.1 | 5.9 | 15.0 | 14.5 | 22.8 | 20.2 | 13.5 | 17.46 | 56.5% | 33.7% |
| >=3000 | 10,482 | 21.1 | 12.8 | 24.0 | 15.4 | 13.9 | 7.4 | 5.3 | 7.84 | 26.7% | 12.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1560 | 0.5488 | 0.4099 | 0.4788 | +0.070 | -0.069 | 0.0044 ± 0.0039 |
| ratio 4-10x | 1050 | 0.5759 | 0.4306 | 0.4838 | +0.092 | -0.053 | 0.0104 ± 0.0049 |
| ratio <2x | 3823 | 0.536 | 0.4136 | 0.435 | +0.101 | -0.021 | 0.0147 ± 0.0023 |
| ratio >=10x | 1299 | 0.5637 | 0.3913 | 0.4388 | +0.125 | -0.048 | 0.0176 ± 0.005 |
| thinner_sample 1000-3000 | 2141 | 0.5401 | 0.4132 | 0.4451 | +0.095 | -0.032 | 0.0126 ± 0.0031 |
| thinner_sample 300-1000 | 1728 | 0.5645 | 0.4243 | 0.4711 | +0.093 | -0.047 | 0.0064 ± 0.0037 |
| thinner_sample <300 | 2518 | 0.5562 | 0.3887 | 0.4472 | +0.109 | -0.058 | 0.0153 ± 0.0035 |
| thinner_sample >=3000 | 1345 | 0.5277 | 0.4344 | 0.4424 | +0.085 | -0.008 | 0.0151 ± 0.0031 |
| data_status ADEQUATE | 2141 | 0.5312 | 0.4289 | 0.4381 | +0.093 | -0.009 | 0.0156 ± 0.0026 |
| data_status LIMITED | 1886 | 0.5488 | 0.4159 | 0.4634 | +0.085 | -0.048 | 0.0084 ± 0.0035 |
| data_status POOR | 3705 | 0.5586 | 0.3989 | 0.4524 | +0.106 | -0.053 | 0.0128 ± 0.0028 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1121 | 0.1974 | 0.1976 | -0.0002 ± 0.0005 | 0.5746 | 0.5751 | 0.5036 | 0.4884 | 0.4996 | -0.095 ± 0.0141 | -0.0087 (8) |
| 3-5 | 716 | 0.2074 | 0.2067 | +0.0007 ± 0.0014 | 0.6004 | 0.5969 | 0.5035 | 0.4638 | 0.4749 | -0.104 ± 0.0174 | 0.01 (3) |
| 5-10 | 1658 | 0.2039 | 0.2024 | +0.0015 ± 0.0017 | 0.5945 | 0.5885 | 0.5113 | 0.4374 | 0.4626 | -0.093 ± 0.0114 | -0.0143 (7) |
| 10-15 | 1350 | 0.2195 | 0.2096 | +0.0100 ± 0.0031 | 0.631 | 0.6029 | 0.5248 | 0.4014 | 0.4215 | -0.109 ± 0.0127 | -0.055 (6) |
| 15-25 | 1709 | 0.2263 | 0.2074 | +0.0189 ± 0.0043 | 0.6476 | 0.5979 | 0.574 | 0.3795 | 0.4283 | -0.105 ± 0.0111 | -0.0045 (11) |
| 25-40 | 976 | 0.2263 | 0.2042 | +0.0221 ± 0.0087 | 0.6432 | 0.589 | 0.6486 | 0.3389 | 0.458 | -0.071 ± 0.0135 | -0.06 (2) |
| 40+ | 202 | 0.3039 | 0.1707 | +0.1332 ± 0.0263 | 0.8142 | 0.5125 | 0.7277 | 0.2715 | 0.3614 | -0.087 ± 0.0253 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5766 | 0.1868 | 0.1878 | -0.0009 ± 0.0002 | 0.5501 | 0.5513 | 0.4914 | 0.4761 | 0.5101 | -0.018 ± 0.0058 | -0.01 (28) |
| 3-5 | 3847 | 0.1998 | 0.1978 | +0.0020 ± 0.0006 | 0.5808 | 0.574 | 0.4823 | 0.4425 | 0.437 | -0.060 ± 0.0073 | 0.005 (6) |
| 5-10 | 8436 | 0.2018 | 0.1976 | +0.0042 ± 0.0007 | 0.5897 | 0.576 | 0.4832 | 0.4094 | 0.4179 | -0.050 ± 0.0049 | -0.0114 (22) |
| 10-15 | 6885 | 0.2026 | 0.1863 | +0.0163 ± 0.0013 | 0.5919 | 0.5466 | 0.4855 | 0.3616 | 0.358 | -0.065 ± 0.0052 | -0.0379 (19) |
| 15-25 | 8775 | 0.2064 | 0.1666 | +0.0398 ± 0.0017 | 0.6047 | 0.4955 | 0.4987 | 0.3032 | 0.3001 | -0.070 ± 0.0044 | -0.0043 (51) |
| 25-40 | 6887 | 0.2242 | 0.1244 | +0.0998 ± 0.0027 | 0.6427 | 0.3834 | 0.5254 | 0.2116 | 0.2136 | -0.061 ± 0.0041 | -0.0733 (3) |
| 40+ | 4694 | 0.3814 | 0.0436 | +0.3378 ± 0.0035 | 0.9931 | 0.1697 | 0.629 | 0.1012 | 0.0567 | -0.076 ± 0.0029 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 896 | 0.2043 | 0.2046 | -0.0003 ± 0.0005 | 0.5891 | 0.5901 | 0.508 | 0.4931 | 0.5179 | -0.098 ± 0.0162 | -0.0117 (6) |
| 3-5 | 645 | 0.2138 | 0.211 | +0.0028 ± 0.0014 | 0.6115 | 0.6055 | 0.5187 | 0.4791 | 0.462 | -0.127 ± 0.0195 | 0.01 (3) |
| 5-10 | 1429 | 0.2069 | 0.2049 | +0.0020 ± 0.0018 | 0.6001 | 0.5946 | 0.5397 | 0.4651 | 0.4913 | -0.089 ± 0.0124 | -0.01 (4) |
| 10-15 | 1251 | 0.2145 | 0.207 | +0.0075 ± 0.0032 | 0.6219 | 0.5995 | 0.5588 | 0.4345 | 0.4692 | -0.104 ± 0.0134 | -0.04 (5) |
| 15-25 | 1800 | 0.2326 | 0.2115 | +0.0211 ± 0.0043 | 0.6613 | 0.6072 | 0.5854 | 0.3898 | 0.435 | -0.104 ± 0.0111 | -0.0183 (12) |
| 25-40 | 1259 | 0.2681 | 0.1999 | +0.0682 ± 0.0079 | 0.7472 | 0.5804 | 0.6605 | 0.3465 | 0.3971 | -0.115 ± 0.0127 | -0.008 (5) |
| 40+ | 452 | 0.3745 | 0.1592 | +0.2153 ± 0.0188 | 1.0196 | 0.4833 | 0.734 | 0.2457 | 0.2832 | -0.092 ± 0.0181 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4921 | 0.1907 | 0.1908 | -0.0002 ± 0.0002 | 0.5564 | 0.5565 | 0.5072 | 0.4921 | 0.5066 | -0.040 ± 0.0064 | -0.0154 (26) |
| 3-5 | 3393 | 0.1944 | 0.1934 | +0.0009 ± 0.0006 | 0.5657 | 0.5626 | 0.5128 | 0.4732 | 0.4807 | -0.044 ± 0.0077 | 0.01 (5) |
| 5-10 | 7516 | 0.1973 | 0.194 | +0.0034 ± 0.0008 | 0.5798 | 0.567 | 0.5075 | 0.4333 | 0.4502 | -0.039 ± 0.0051 | -0.0117 (6) |
| 10-15 | 6245 | 0.203 | 0.1908 | +0.0122 ± 0.0014 | 0.596 | 0.5584 | 0.5085 | 0.3846 | 0.3981 | -0.051 ± 0.0056 | -0.0189 (18) |
| 15-25 | 8865 | 0.2167 | 0.1796 | +0.0371 ± 0.0018 | 0.6304 | 0.5278 | 0.524 | 0.3286 | 0.3336 | -0.063 ± 0.0045 | -0.014 (52) |
| 25-40 | 8016 | 0.2515 | 0.1381 | +0.1134 ± 0.0026 | 0.7097 | 0.4213 | 0.5604 | 0.2429 | 0.2268 | -0.078 ± 0.0042 | -0.0095 (20) |
| 40+ | 6334 | 0.4031 | 0.0585 | +0.3445 ± 0.0035 | 1.062 | 0.2114 | 0.6545 | 0.1185 | 0.0786 | -0.075 ± 0.003 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1099 | 0.1957 | 0.1968 | -0.0011 ± 0.0005 | 0.5709 | 0.5736 | 0.5014 | 0.4859 | 0.525 | -0.059 ± 0.014 | -0.0191 (11) |
| 3-5 | 780 | 0.2086 | 0.2068 | +0.0017 ± 0.0013 | 0.6041 | 0.5982 | 0.4979 | 0.4584 | 0.4577 | -0.114 ± 0.017 | 0.002 (5) |
| 5-10 | 1674 | 0.2044 | 0.2003 | +0.0040 ± 0.0016 | 0.5945 | 0.5831 | 0.5129 | 0.4392 | 0.448 | -0.107 ± 0.0113 | -0.01 (10) |
| 10-15 | 1378 | 0.2123 | 0.2031 | +0.0092 ± 0.003 | 0.6149 | 0.5889 | 0.5386 | 0.4155 | 0.4412 | -0.107 ± 0.0123 | -0.0286 (7) |
| 15-25 | 1632 | 0.2321 | 0.2126 | +0.0194 ± 0.0044 | 0.6616 | 0.6095 | 0.5843 | 0.3902 | 0.4369 | -0.108 ± 0.0115 | -0.03 (1) |
| 25-40 | 957 | 0.2173 | 0.208 | +0.0093 ± 0.0087 | 0.6246 | 0.5977 | 0.6569 | 0.3463 | 0.4848 | -0.062 ± 0.0136 | -0.0267 (3) |
| 40+ | 212 | 0.3112 | 0.1791 | +0.1321 ± 0.0262 | 0.8396 | 0.5302 | 0.7396 | 0.2837 | 0.3774 | -0.084 ± 0.0267 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5556 | 0.1854 | 0.1859 | -0.0005 ± 0.0002 | 0.5463 | 0.5467 | 0.4855 | 0.4701 | 0.4849 | -0.037 ± 0.0059 | -0.0189 (44) |
| 3-5 | 3977 | 0.2057 | 0.2038 | +0.0019 ± 0.0006 | 0.597 | 0.5905 | 0.4814 | 0.4418 | 0.4378 | -0.059 ± 0.0073 | -0.0073 (22) |
| 5-10 | 8580 | 0.1969 | 0.1916 | +0.0053 ± 0.0007 | 0.5775 | 0.5607 | 0.4868 | 0.4128 | 0.4134 | -0.056 ± 0.0048 | -0.0117 (42) |
| 10-15 | 6878 | 0.1951 | 0.1799 | +0.0152 ± 0.0013 | 0.5752 | 0.5319 | 0.4963 | 0.3731 | 0.3728 | -0.062 ± 0.0051 | -0.0136 (14) |
| 15-25 | 8835 | 0.2118 | 0.1722 | +0.0396 ± 0.0017 | 0.6172 | 0.5082 | 0.5111 | 0.3166 | 0.3127 | -0.070 ± 0.0044 | -0.0533 (3) |
| 25-40 | 6842 | 0.2183 | 0.1242 | +0.0941 ± 0.0027 | 0.6301 | 0.3825 | 0.5272 | 0.2116 | 0.2222 | -0.054 ± 0.0041 | -0.02 (4) |
| 40+ | 4622 | 0.3891 | 0.048 | +0.3411 ± 0.0036 | 1.014 | 0.1807 | 0.6374 | 0.1066 | 0.0634 | -0.075 ± 0.0031 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1552 | 0.1975 | 0.1973 | +0.0002 ± 0.0004 | 0.5736 | 0.5731 | 0.5092 | 0.4941 | 0.4942 | -0.073 ± 0.0115 | -0.0221 (56) |
| 3-5 | 1101 | 0.1897 | 0.1897 | -0.0000 ± 0.0011 | 0.5574 | 0.5558 | 0.4994 | 0.4594 | 0.4777 | -0.056 ± 0.0134 | -0.0194 (34) |
| 5-10 | 2219 | 0.1995 | 0.1945 | +0.0050 ± 0.0014 | 0.5884 | 0.5719 | 0.5081 | 0.4345 | 0.4371 | -0.078 ± 0.0096 | -0.005 (78) |
| 10-15 | 1527 | 0.2159 | 0.203 | +0.0128 ± 0.0029 | 0.626 | 0.5897 | 0.5433 | 0.4206 | 0.4283 | -0.092 ± 0.0119 | 0.0012 (66) |
| 15-25 | 1993 | 0.2317 | 0.2082 | +0.0235 ± 0.004 | 0.6609 | 0.6005 | 0.5915 | 0.3966 | 0.435 | -0.090 ± 0.0103 | -0.0214 (59) |
| 25-40 | 1180 | 0.2413 | 0.2106 | +0.0307 ± 0.0081 | 0.6885 | 0.6041 | 0.6887 | 0.377 | 0.4839 | -0.087 ± 0.0126 | -0.0252 (27) |
| 40+ | 433 | 0.3269 | 0.1977 | +0.1291 ± 0.0204 | 0.9365 | 0.5773 | 0.8128 | 0.337 | 0.455 | -0.097 ± 0.0191 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5646 | 0.1775 | 0.1775 | -0.0000 ± 0.0002 | 0.5254 | 0.525 | 0.5111 | 0.4959 | 0.5041 | -0.041 ± 0.0057 | -0.0154 (103) |
| 3-5 | 3894 | 0.1946 | 0.1938 | +0.0008 ± 0.0006 | 0.5677 | 0.5653 | 0.5037 | 0.4639 | 0.4735 | -0.040 ± 0.0071 | -0.0212 (73) |
| 5-10 | 7930 | 0.1973 | 0.1908 | +0.0066 ± 0.0007 | 0.5819 | 0.5618 | 0.5024 | 0.4289 | 0.4219 | -0.062 ± 0.005 | -0.0084 (134) |
| 10-15 | 5405 | 0.2106 | 0.1942 | +0.0164 ± 0.0015 | 0.6131 | 0.5694 | 0.5369 | 0.414 | 0.407 | -0.073 ± 0.0061 | -0.0057 (111) |
| 15-25 | 6641 | 0.2314 | 0.1995 | +0.0320 ± 0.0022 | 0.6648 | 0.5784 | 0.5759 | 0.3805 | 0.3966 | -0.068 ± 0.0055 | -0.026 (108) |
| 25-40 | 4298 | 0.2577 | 0.1901 | +0.0676 ± 0.0042 | 0.7285 | 0.5537 | 0.6395 | 0.3271 | 0.3781 | -0.065 ± 0.0065 | -0.0277 (53) |
| 40+ | 1950 | 0.3695 | 0.1586 | +0.2110 ± 0.0093 | 1.04 | 0.4732 | 0.742 | 0.2426 | 0.2913 | -0.061 ± 0.0086 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7732 | 1.016 ± 0.032 | 1.093 | 0.1676 | 0.1684 | 0.2164 | 0.2039 |
| gen2 | 7732 | 0.813 ± 0.029 | 1.068 | 0.1732 | 0.1687 | 0.2341 | 0.2038 |
| gen1_elo | 7732 | 1.002 ± 0.031 | 1.082 | 0.1742 | 0.1685 | 0.2154 | 0.204 |
| gen1_sr | 7732 | 0.995 ± 0.038 | 1.118 | 0.1331 | 0.1702 | 0.2302 | 0.2035 |
| gen1_ledger | 10005 | 0.865 ± 0.024 | 1.069 | 0.1894 | 0.1755 | 0.2175 | 0.2005 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 36,223)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 8,753 | 24.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,320 | 23.0% |
| BOOK_QUALITY | execution | 6,237 | 17.2% |
| POOR_DATA | data | 4,159 | 11.5% |
| LIMITED_DATA | data | 2,192 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,093 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,484 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,406 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,008 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 570 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.2%, coverage 23.0%, data 17.5%, execution 17.2%, market_freshness/coverage 8.6%, mapping 4.1%, model_calibration_or_unknown 3.9%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.9%, LOW_DATA_QUALITY 71.9%, THIN_PLAYER_HISTORY 60.1%, STALE_PLAYER_DATA 52.4%, STALE_KALSHI_QUOTE 47.6%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 23.7%, MODEL_HIGH_UNCERTAINTY 18.5%, PLAYER_IDENTITY_RISK 15.1%, LEVEL_TRANSFER_RISK 9.6%, LOW_DISPLAYED_LIQUIDITY 8.5%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.4%, POST_SETTLEMENT_OBSERVATION 23.0%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 19,347)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,707 | 34.7% |
| STALE_QUOTE | market_freshness | 3,915 | 20.2% |
| BOOK_QUALITY | execution | 3,220 | 16.6% |
| POOR_DATA | data | 1,766 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,127 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 827 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 659 | 3.4% |
| LIMITED_DATA | data | 642 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 345 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 138 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.7%, market_freshness 20.2%, execution 16.6%, data 12.4%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.2%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 62.1%, STALE_KALSHI_QUOTE 55.1%, STALE_PLAYER_DATA 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.0%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 22.9%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.1%, EVENT_MAPPING_RISK 8.5%, LEVEL_TRANSFER_RISK 8.5%, LOW_DISPLAYED_LIQUIDITY 8.4%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.6%, POST_SETTLEMENT_OBSERVATION 34.7%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 15509, "IDENTITY_AMBIGUOUS": 3838}; ticker orientation: {"VERIFIED": 19347}.

Checks: discipline:AMBIGUOUS 1247, discipline:PASS 18100, identity_confidence:AMBIGUOUS 3498, identity_confidence:PASS 15849, level_mapping:NA 1259, level_mapping:PASS 18088, market_pair:AMBIGUOUS 504, market_pair:NA 416, market_pair:PASS 18427, model_complement:NA 378, model_complement:PASS 18969, namesake:AMBIGUOUS 6, namesake:PASS 19341, physical_match_id:NA 6481, physical_match_id:PASS 12866, player_ids:PASS 19347, same_pair_other_event:PASS 19347, ticker_orientation:PASS 19347

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,563 | 3.7% | 3.1% | 1.3% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.2218 / 0.2173 (853) | 25.6% | 2.4% | 3.1% | 3.0% |
| CHALLENGER | 13,063 | 16.6% | 5.9% | 11.2% | {"coverage": 1326, "market_freshness": 257, "market_freshness/coverage": 238, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 39, "mapping": 17, "possible_market_error": 1} | 7.34 | 0.2214 / 0.2107 (3043) | 41.3% | 14.0% | 4.0% | 22.9% |
| DOUBLES | 2,705 | 46.1% | 46.1% | 6.5% | {"execution": 691, "mapping": 372, "market_freshness": 106, "market_freshness/coverage": 71, "coverage": 7} | 23.0 | 0.2979 / 0.2326 (666) | 8.6% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 25,493 | 25.4% | 17.8% | 33.5% | {"coverage": 2242, "market_freshness": 1353, "execution": 1031, "data": 958, "market_freshness/coverage": 654, "mapping": 223, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.81 | 0.2196 / 0.1994 (5303) | 41.6% | 69.9% | 14.8% | 21.3% |
| ITF_WOMEN | 32,622 | 26.4% | 18.9% | 44.6% | {"coverage": 3053, "market_freshness": 1938, "execution": 1374, "data": 1185, "market_freshness/coverage": 744, "mapping": 209, "model_calibration_or_unknown": 98, "model_calibration": 23} | 12.49 | 0.2033 / 0.194 (6252) | 42.4% | 57.4% | 9.9% | 21.6% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,901 | 5.9% | 5.0% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.64 | 0.2308 / 0.2206 (808) | 30.3% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 519 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 517 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.9h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 305 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 12 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 13 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 899 min (STALE); no external reference |
| 16 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 19 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 21 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 22 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 23 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 24 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 25 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 26 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 27 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 28 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 29 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 30 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 31 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 34 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 37 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 38 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 39 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 40 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 41 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 45 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 46 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 47 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 48 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 49 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 50 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9723, "by_level_share_of_ge_25pp": {"ATP": 0.0127, "CHALLENGER": 0.1118, "DOUBLES": 0.0645, "ITF_MEN": 0.3345, "ITF_WOMEN": 0.4458, "OTHER": 0.0006, "WTA": 0.015, "WTA125": 0.0151}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5511, "share_primary_cause_market_settled_or_in_play": 0.4391, "share_primary_cause_stale_quote_only": 0.2024}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 19347, "identity_ambiguous_share": 0.1984, "ticker_orientation": {"VERIFIED": 19347}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 12866, "with_external": 634, "coverage": 0.0493, "external_status": {"EXTERNAL_STALE": 403, "AGREES_WITH_KALSHI": 218, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 403, "MODEL_LONE_OUTLIER": 218, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3438, "share_external_supports_model": 0.0205}, "pregame_clean_ge_25pp": {"n": 5953, "with_external": 603, "coverage": 0.1013, "external_status": {"EXTERNAL_STALE": 379, "AGREES_WITH_KALSHI": 211, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 379, "MODEL_LONE_OUTLIER": 211, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3499, "share_external_supports_model": 0.0216}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 479.0, "median_sample_ratio": 2.45, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2081, "data_status": {"POOR": 10971, "LIMITED": 4884, "ADEQUATE": 3492}, "comparison_lt_10pp": {"median_thinner_serve_points": 1701.0, "median_sample_ratio": 1.7, "median_min_matches": 88.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1560, "model_minus_observed": 0.0699, "kalshi_minus_observed": -0.069, "brier_diff_model_minus_kalshi": 0.0044}, "4-10x": {"n": 1050, "model_minus_observed": 0.0921, "kalshi_minus_observed": -0.0533, "brier_diff_model_minus_kalshi": 0.0104}, "<2x": {"n": 3823, "model_minus_observed": 0.101, "kalshi_minus_observed": -0.0214, "brier_diff_model_minus_kalshi": 0.0147}, ">=10x": {"n": 1299, "model_minus_observed": 0.1249, "kalshi_minus_observed": -0.0475, "brier_diff_model_minus_kalshi": 0.0176}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7732, "model": {"intercept": -0.558, "slope": 0.813, "slope_se": 0.029}, "kalshi_mid_same_rows": {"intercept": 0.169, "slope": 1.068, "slope_se": 0.032}, "mean_extremity_model": 0.1732, "mean_extremity_kalshi": 0.1687, "model_brier": 0.2341, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0304, "brier_diff_se": 0.0021, "model_logloss": 0.666, "kalshi_logloss": 0.5899}, "fair_v1": {"n": 7732, "model": {"intercept": -0.461, "slope": 1.016, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.223, "slope": 1.093, "slope_se": 0.033}, "mean_extremity_model": 0.1676, "mean_extremity_kalshi": 0.1684, "model_brier": 0.2164, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0125, "brier_diff_se": 0.0018, "model_logloss": 0.6222, "kalshi_logloss": 0.59}, "gen1_elo": {"n": 7732, "model": {"intercept": -0.451, "slope": 1.002, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.223, "slope": 1.082, "slope_se": 0.032}, "mean_extremity_model": 0.1742, "mean_extremity_kalshi": 0.1685, "model_brier": 0.2154, "kalshi_brier": 0.204, "brier_diff_model_minus_kalshi": 0.0114, "brier_diff_se": 0.0017, "model_logloss": 0.6204, "kalshi_logloss": 0.5902}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2519, "share_ge_15": 0.4474, "median_abs_gap": 13.12, "n": 51074}, "gen1_elo": {"share_ge_25": 0.2493, "share_ge_15": 0.4432, "median_abs_gap": 12.97, "n": 51074}, "gen1_sr": {"share_ge_25": 0.3148, "share_ge_15": 0.5228, "median_abs_gap": 15.92, "n": 51074}, "gen2": {"share_ge_25": 0.3151, "share_ge_15": 0.5115, "median_abs_gap": 15.48, "n": 51074}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1521, "share_ge_15": 0.3549, "median_abs_gap": 10.71, "n": 39136}, "gen1_elo": {"share_ge_25": 0.1503, "share_ge_15": 0.3497, "median_abs_gap": 10.51, "n": 39136}, "gen1_sr": {"share_ge_25": 0.2159, "share_ge_15": 0.4397, "median_abs_gap": 12.99, "n": 39138}, "gen2": {"share_ge_25": 0.2306, "share_ge_15": 0.4386, "median_abs_gap": 12.83, "n": 39138}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0373, "share_ge_25_pregame_clean": 0.0313}, "WTA": {"median_abs_gap_pregame_clean": 7.64, "share_ge_25_all": 0.0594, "share_ge_25_pregame_clean": 0.0504}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2354, "share_within_10pp_all": 0.4369, "share_within_10pp_pregame_clean": 0.4906, "corr_model_vs_mid_pregame_clean": 0.8497}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1121, "model_brier": 0.1974, "kalshi_brier": 0.1976, "brier_diff_model_minus_kalshi": -0.0002}, "10-15": {"n_settled": 1350, "model_brier": 0.2195, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.01}, "15-25": {"n_settled": 1709, "model_brier": 0.2263, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.0189}, "25-40": {"n_settled": 976, "model_brier": 0.2263, "kalshi_brier": 0.2042, "brier_diff_model_minus_kalshi": 0.0221}, "3-5": {"n_settled": 716, "model_brier": 0.2074, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": 0.0007}, "40+": {"n_settled": 202, "model_brier": 0.3039, "kalshi_brier": 0.1707, "brier_diff_model_minus_kalshi": 0.1332}, "5-10": {"n_settled": 1658, "model_brier": 0.2039, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": 0.0015}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.558, "slope": 0.813, "slope_se": 0.029}, "kalshi_slope": {"intercept": 0.169, "slope": 1.068, "slope_se": 0.032}, "n": 7732}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.495, "slope": 0.865, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.158, "slope": 1.069, "slope_se": 0.028}, "n": 10005}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 666, "model_brier": 0.2979, "kalshi_brier": 0.2326, "brier_diff_model_minus_kalshi": 0.0653, "brier_diff_se": 0.0113, "corr_model_outcome": 0.1022, "corr_kalshi_outcome": 0.2778}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
