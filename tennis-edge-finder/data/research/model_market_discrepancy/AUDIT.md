# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-05T14:36Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 79,343): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.0%; median gap 11.79 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.7%, Challenger 10.7%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,147): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.6%, STALE_QUOTE 19.6%, BOOK_QUALITY 17.8%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.6%, market_freshness 19.6%, execution 17.8%, data 12.8%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,147 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.4%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.3% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 483.0 points vs 1719.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.031, Gen-2 0.825, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 871 model 0.222 vs Kalshi 0.2035; n 185 model 0.2959 vs Kalshi 0.1755.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 337,938 model-market comparisons (552,626 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 112,649 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-05T14:16:18.544651+00:00'], shadow board 91,084 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-05T14:16:22.551131+00:00'], Model 4 42,120 rows, 27,892 settled tickers, 10,588 tickers with an external scan.
* By model: {"gen1_ledger": 75961, "gen1_elo": 45771, "fair_v1": 45771, "gen2": 45771, "gen1_sr": 45771, "model4_fundamental": 39488, "model4_conditioned": 39405}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 79,343 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.0 | 11.79 | 40.7% | 21.6% |
| MW fair_v1 | 45,771 | 12.8 | 8.7 | 18.8 | 15.4 | 19.6 | 14.8 | 9.8 | 13.0 | 44.2% | 24.6% |
| MW gen1_elo | 45,771 | 12.6 | 8.8 | 19.3 | 15.4 | 19.5 | 14.6 | 9.7 | 12.75 | 43.8% | 24.3% |
| MW gen1_ledger | 33,572 | 15.8 | 10.9 | 22.2 | 15.1 | 18.4 | 12.1 | 5.5 | 10.26 | 35.9% | 17.6% |
| MW gen1_sr | 45,771 | 10.1 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.5 | 15.77 | 51.9% | 31.2% |
| MW gen2 | 45,771 | 11.1 | 7.6 | 16.7 | 13.8 | 19.6 | 17.7 | 13.6 | 15.39 | 50.9% | 31.3% |
| all families model4_conditioned | 39,405 | 22.2 | 18.0 | 34.1 | 17.1 | 5.0 | 2.2 | 1.2 | 6.06 | 8.5% | 3.4% |
| all families model4_fundamental | 39,488 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.0%, >=15pp 40.7%, >=20pp 29.9%, >=25pp 21.6%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.33pp; >=10pp 44.8%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,913 | 28.4 | 15.6 | 27.6 | 13.4 | 10.6 | 3.6 | 0.6 | 5.8 | 14.9% | 4.3% |
| CHALLENGER | 6,863 | 16.0 | 9.9 | 20.7 | 15.3 | 16.2 | 11.3 | 10.7 | 10.91 | 38.2% | 22.0% |
| ITF_MEN | 12,856 | 9.9 | 7.4 | 17.1 | 15.2 | 21.3 | 17.2 | 11.9 | 15.16 | 50.5% | 29.2% |
| ITF_WOMEN | 17,819 | 9.5 | 7.1 | 16.1 | 14.9 | 22.1 | 18.3 | 12.0 | 15.79 | 52.4% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,989 | 16.7 | 13.3 | 24.5 | 21.0 | 16.5 | 6.9 | 1.1 | 8.74 | 24.5% | 8.0% |
| WTA125 | 1,325 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.6% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,913 | 26.9 | 15.8 | 26.0 | 15.4 | 11.4 | 3.7 | 0.8 | 6.02 | 15.9% | 4.5% |
| CHALLENGER | 6,863 | 14.8 | 9.0 | 18.6 | 14.0 | 18.7 | 13.4 | 11.3 | 12.48 | 43.5% | 24.8% |
| ITF_MEN | 12,856 | 8.2 | 6.2 | 15.2 | 13.8 | 19.9 | 20.5 | 16.2 | 17.82 | 56.6% | 36.7% |
| ITF_WOMEN | 17,819 | 7.8 | 5.8 | 14.1 | 12.9 | 20.7 | 21.2 | 17.5 | 19.09 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,989 | 14.1 | 10.2 | 22.0 | 15.9 | 22.2 | 13.1 | 2.6 | 11.19 | 37.9% | 15.7% |
| WTA125 | 1,325 | 10.3 | 7.2 | 16.3 | 15.4 | 24.2 | 17.4 | 9.1 | 15.22 | 50.8% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,913 | 22.9 | 13.9 | 25.2 | 15.6 | 15.0 | 6.1 | 1.2 | 7.15 | 22.3% | 7.3% |
| CHALLENGER | 6,863 | 15.2 | 9.6 | 20.9 | 15.6 | 16.0 | 11.9 | 10.8 | 11.2 | 38.7% | 22.7% |
| ITF_MEN | 12,856 | 9.5 | 7.2 | 17.3 | 14.2 | 22.0 | 17.3 | 12.4 | 15.61 | 51.7% | 29.7% |
| ITF_WOMEN | 17,819 | 9.3 | 6.9 | 16.3 | 15.8 | 22.2 | 18.1 | 11.3 | 15.55 | 51.7% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,989 | 22.8 | 17.0 | 31.8 | 15.2 | 8.8 | 3.4 | 1.1 | 6.12 | 13.2% | 4.4% |
| WTA125 | 1,325 | 21.1 | 13.3 | 25.6 | 19.0 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,317 | 26.7 | 19.6 | 30.0 | 12.3 | 8.2 | 2.6 | 0.4 | 5.37 | 11.3% | 3.0% |
| CHALLENGER | 4,434 | 22.2 | 14.5 | 27.7 | 14.7 | 13.5 | 5.8 | 1.5 | 7.09 | 20.8% | 7.3% |
| DOUBLES | 2,476 | 5.0 | 4.4 | 12.6 | 11.0 | 20.3 | 24.9 | 21.8 | 23.54 | 67.0% | 46.7% |
| ITF_MEN | 9,603 | 13.0 | 9.6 | 21.3 | 15.7 | 21.5 | 13.0 | 5.9 | 11.78 | 40.4% | 18.9% |
| ITF_WOMEN | 11,604 | 13.4 | 9.2 | 20.0 | 15.7 | 21.3 | 14.9 | 5.5 | 12.2 | 41.7% | 20.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,735 | 24.3 | 16.0 | 31.1 | 16.5 | 9.2 | 2.6 | 0.2 | 6.57 | 12.1% | 2.9% |
| WTA125 | 1,254 | 25.3 | 13.2 | 21.2 | 19.0 | 13.1 | 6.9 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,799 | 28.9 | 15.8 | 28.0 | 13.4 | 10.4 | 3.2 | 0.3 | 5.67 | 14.0% | 3.5% |
| CHALLENGER | 4,867 | 20.5 | 12.2 | 25.6 | 18.0 | 16.2 | 6.0 | 1.6 | 8.27 | 23.8% | 7.6% |
| ITF_MEN | 9,465 | 12.0 | 8.7 | 20.7 | 17.3 | 22.0 | 14.1 | 5.3 | 12.38 | 41.3% | 19.3% |
| ITF_WOMEN | 13,208 | 11.3 | 8.5 | 18.8 | 17.1 | 24.1 | 15.2 | 5.0 | 13.24 | 44.2% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,879 | 17.0 | 13.3 | 24.8 | 21.4 | 16.5 | 6.3 | 0.6 | 8.54 | 23.5% | 7.0% |
| WTA125 | 1,277 | 16.2 | 6.8 | 22.3 | 20.2 | 20.8 | 11.8 | 1.8 | 10.7 | 34.5% | 13.6% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,799 | 27.2 | 16.1 | 26.2 | 15.4 | 11.4 | 3.3 | 0.4 | 5.96 | 15.1% | 3.7% |
| CHALLENGER | 4,867 | 18.6 | 11.3 | 23.3 | 16.4 | 19.2 | 9.3 | 1.9 | 9.07 | 30.4% | 11.2% |
| ITF_MEN | 9,466 | 9.6 | 7.3 | 17.6 | 15.9 | 21.6 | 18.6 | 9.2 | 14.86 | 49.5% | 27.9% |
| ITF_WOMEN | 13,209 | 8.7 | 6.7 | 16.1 | 14.4 | 22.7 | 20.6 | 10.8 | 16.58 | 54.1% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,879 | 14.3 | 10.3 | 22.2 | 16.1 | 22.4 | 12.8 | 1.9 | 11.03 | 37.1% | 14.7% |
| WTA125 | 1,277 | 10.3 | 7.4 | 16.4 | 15.5 | 24.2 | 17.5 | 8.6 | 15.13 | 50.3% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,260 | 26.9 | 19.8 | 30.0 | 12.5 | 8.0 | 2.5 | 0.3 | 5.33 | 10.8% | 2.8% |
| CHALLENGER | 3,917 | 23.6 | 15.4 | 28.9 | 14.9 | 12.9 | 4.0 | 0.4 | 6.61 | 17.3% | 4.4% |
| DOUBLES | 2,328 | 4.9 | 4.5 | 12.8 | 11.1 | 20.1 | 24.9 | 21.7 | 23.45 | 66.7% | 46.6% |
| ITF_MEN | 8,262 | 13.8 | 10.2 | 22.9 | 16.2 | 21.5 | 11.5 | 3.9 | 10.84 | 36.9% | 15.4% |
| ITF_WOMEN | 9,944 | 14.0 | 9.8 | 21.1 | 16.2 | 21.4 | 13.8 | 3.6 | 11.39 | 38.9% | 17.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,674 | 24.6 | 16.4 | 31.1 | 16.6 | 9.2 | 2.1 | 0.1 | 6.43 | 11.3% | 2.1% |
| WTA125 | 1,113 | 26.4 | 14.0 | 22.2 | 19.8 | 12.1 | 5.0 | 0.5 | 7.2 | 17.6% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,476 | 5.0 | 4.4 | 12.6 | 11.0 | 20.3 | 24.9 | 21.8 | 23.54 | 67.0% | 46.7% |
| singles | 31,096 | 16.6 | 11.4 | 23.0 | 15.5 | 18.2 | 11.0 | 4.2 | 9.72 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 140 | 7.9 | 8.6 | 13.6 | 8.6 | 20.0 | 27.1 | 14.3 | 20.01 | 61.4% | 41.4% |
| Clay | 9,312 | 12.8 | 9.2 | 19.9 | 15.7 | 19.7 | 13.8 | 8.9 | 12.52 | 42.4% | 22.7% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 29,890 | 13.4 | 8.8 | 18.9 | 15.2 | 19.2 | 14.8 | 9.8 | 12.84 | 43.8% | 24.6% |
| UNKNOWN | 6,192 | 10.5 | 7.7 | 17.0 | 16.4 | 21.5 | 15.9 | 11.0 | 14.3 | 48.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,965 | 19.5 | 12.0 | 22.4 | 16.0 | 15.0 | 9.0 | 6.1 | 8.86 | 30.1% | 15.1% |
| B | 5,605 | 12.9 | 8.7 | 19.8 | 15.7 | 19.5 | 12.7 | 10.7 | 12.55 | 42.9% | 23.4% |
| C | 6,480 | 11.9 | 8.9 | 19.6 | 15.8 | 18.6 | 14.7 | 10.5 | 12.89 | 43.8% | 25.1% |
| D | 7,385 | 11.8 | 8.4 | 17.9 | 15.4 | 21.5 | 15.7 | 9.2 | 13.71 | 46.5% | 24.9% |
| F | 13,336 | 7.4 | 5.6 | 14.9 | 14.7 | 23.5 | 20.8 | 13.1 | 17.71 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,940 | 24.6 | 16.0 | 29.2 | 14.9 | 10.7 | 3.4 | 1.2 | 6.37 | 15.3% | 4.7% |
| B | 4,716 | 16.6 | 10.8 | 24.3 | 16.7 | 18.9 | 9.6 | 3.1 | 9.65 | 31.6% | 12.7% |
| C | 6,628 | 11.2 | 7.8 | 19.4 | 14.8 | 20.9 | 15.7 | 10.2 | 13.49 | 46.8% | 25.9% |
| D | 5,023 | 14.6 | 10.1 | 21.5 | 15.4 | 20.4 | 12.7 | 5.3 | 11.15 | 38.4% | 18.0% |
| F | 8,265 | 10.2 | 8.4 | 16.2 | 14.6 | 23.2 | 19.6 | 7.8 | 15.33 | 50.6% | 27.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,662 | 17.8 | 11.0 | 21.6 | 15.8 | 15.3 | 9.9 | 8.6 | 9.92 | 33.9% | 18.5% |
| LIMITED | 9,998 | 13.6 | 9.8 | 20.5 | 16.0 | 19.3 | 13.3 | 7.5 | 11.79 | 40.1% | 20.8% |
| POOR | 21,111 | 9.0 | 6.6 | 16.1 | 15.0 | 22.7 | 18.9 | 11.7 | 16.09 | 53.3% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,706 | 23.8 | 17.8 | 33.2 | 15.6 | 6.4 | 2.9 | 0.4 | 5.92 | 9.7% | 3.3% |
| GAME_SPREAD | 6,571 | 22.5 | 15.2 | 32.3 | 16.9 | 9.0 | 3.4 | 0.6 | 6.72 | 13.1% | 4.0% |
| MATCH_WINNER | 33,572 | 15.8 | 10.9 | 22.2 | 15.1 | 18.4 | 12.1 | 5.5 | 10.26 | 35.9% | 17.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,084 | 27.9 | 16.8 | 30.6 | 12.8 | 9.2 | 2.5 | 0.3 | 5.63 | 12.0% | 2.8% |
| TOTAL_GAMES | 11,004 | 9.8 | 10.8 | 35.5 | 26.0 | 10.7 | 4.3 | 3.0 | 9.21 | 17.9% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,976 | 24.4 | 28.9 | 33.2 | 8.1 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,099 | 46.8 | 16.1 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.3 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,330 | 6.5 | 9.8 | 40.2 | 30.2 | 7.5 | 3.4 | 2.4 | 9.22 | 13.2% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,011 | 23.9 | 16.6 | 34.8 | 14.7 | 6.9 | 2.6 | 0.5 | 6.05 | 10.0% | 3.1% |
| GAME_SPREAD | 9,108 | 20.6 | 13.5 | 28.2 | 20.1 | 12.0 | 4.5 | 1.1 | 7.63 | 17.6% | 5.6% |
| TOTAL_GAMES | 16,369 | 10.0 | 10.8 | 36.2 | 24.4 | 11.5 | 4.5 | 2.6 | 9.07 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 45,771 | 44.2% | 24.6% | 13.0 | 35.4% | 15.1% | 10.71 |
| gen1_elo | 45,771 | 43.8% | 24.3% | 12.75 | 34.9% | 14.9% | 10.49 |
| gen1_sr | 45,771 | 51.9% | 31.2% | 15.77 | 44.1% | 21.7% | 13.01 |
| gen2 | 45,771 | 50.9% | 31.3% | 15.39 | 43.9% | 23.2% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,823 | 15.5 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 25,948 | 10.8 | 7.4 | 16.9 | 14.1 | 19.3 | 17.0 | 14.7 | 15.38 | 50.9% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 27,040 | 16.4 | 11.2 | 22.8 | 15.2 | 17.9 | 11.6 | 4.8 | 9.85 | 34.3% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 79,343 | 27040 | 23295 | 29008 | 24.7 | 117.1 | 1451.1 |
| ge_15pp | 32,297 | 9270 | 8296 | 14731 | 28.0 | 421.8 | 1451.1 |
| ge_25pp | 17,147 | 4436 | 3617 | 9094 | 32.8 | 575.6 | 1431.1 |
| lt_10pp | 34,892 | 13652 | 11022 | 10218 | 22.6 | 47.8 | 1421.1 |

Current slate `SL-20261105T143627Z-2065c219`: 395 priced rows, quote age at build {'median': 52.8, 'max': 62.8}, freshness {'STALE': 395}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,592 | 19.1 | 11.0 | 25.4 | 17.9 | 18.2 | 7.5 | 1.0 | 8.84 | 26.6% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 927 | 65.9 | 34.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.19 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,006 | 0.0 | 2.3 | 36.8 | 26.3 | 24.4 | 9.4 | 0.8 | 11.89 | 34.6% | 10.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 45,771 | 7633 (16.7%) | 26.3% | 1.0% | {"EXTERNAL_STALE": 4592, "AGREES_WITH_KALSHI": 2006, "ALL_AGREE": 927, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,228 | 1945 (9.6%) | 35.7% | 1.5% | {"EXTERNAL_STALE": 1221, "AGREES_WITH_KALSHI": 694, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,249 | 605 (5.4%) | 33.9% | 2.1% | {"EXTERNAL_STALE": 387, "AGREES_WITH_KALSHI": 205, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,373 | 575 (10.7%) | 34.4% | 2.3% | {"EXTERNAL_STALE": 364, "AGREES_WITH_KALSHI": 198, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,471 | 4334 (23.5%) | 18.1% | 1.0% | {"EXTERNAL_STALE": 2550, "ALL_AGREE": 927, "AGREES_WITH_KALSHI": 784, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,944 | 10.4 | 7.8 | 19.6 | 14.7 | 21.6 | 16.1 | 9.8 | 14.0 | 47.5% | 25.9% |
| 4-10x | 6,134 | 11.4 | 8.5 | 18.5 | 15.3 | 22.1 | 14.2 | 10.0 | 13.67 | 46.3% | 24.2% |
| <2x | 23,375 | 14.9 | 9.8 | 19.8 | 16.1 | 17.6 | 13.1 | 8.8 | 11.54 | 39.4% | 21.8% |
| >=10x | 7,318 | 10.4 | 6.4 | 15.0 | 14.5 | 21.7 | 19.1 | 13.0 | 16.37 | 53.7% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,960 | 12.5 | 8.7 | 20.0 | 16.2 | 19.0 | 13.4 | 10.1 | 12.65 | 42.6% | 23.6% |
| 300-1000 | 9,886 | 11.8 | 8.8 | 17.8 | 15.3 | 20.7 | 16.2 | 9.3 | 13.63 | 46.2% | 25.6% |
| <300 | 14,429 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 19.9 | 13.0 | 17.1 | 56.0% | 32.9% |
| >=3000 | 9,496 | 21.3 | 13.0 | 23.9 | 15.7 | 14.0 | 7.2 | 5.0 | 7.72 | 26.1% | 12.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1383 | 0.5488 | 0.4095 | 0.491 | +0.058 | -0.082 | 0.0004 ± 0.0041 |
| ratio 4-10x | 949 | 0.5756 | 0.4306 | 0.4879 | +0.088 | -0.057 | 0.0085 ± 0.0052 |
| ratio <2x | 3366 | 0.5373 | 0.4142 | 0.4364 | +0.101 | -0.022 | 0.0147 ± 0.0025 |
| ratio >=10x | 1167 | 0.5649 | 0.3917 | 0.4473 | +0.118 | -0.056 | 0.0147 ± 0.0052 |
| thinner_sample 1000-3000 | 1901 | 0.5395 | 0.4121 | 0.4477 | +0.092 | -0.035 | 0.011 ± 0.0033 |
| thinner_sample 300-1000 | 1561 | 0.5642 | 0.4237 | 0.4766 | +0.087 | -0.053 | 0.0043 ± 0.0039 |
| thinner_sample <300 | 2247 | 0.5578 | 0.3898 | 0.4548 | +0.103 | -0.065 | 0.0131 ± 0.0037 |
| thinner_sample >=3000 | 1156 | 0.5306 | 0.4372 | 0.4464 | +0.084 | -0.009 | 0.0159 ± 0.0033 |
| data_status ADEQUATE | 1891 | 0.5325 | 0.4292 | 0.4384 | +0.094 | -0.009 | 0.0161 ± 0.0028 |
| data_status LIMITED | 1671 | 0.5482 | 0.4154 | 0.4692 | +0.079 | -0.054 | 0.0064 ± 0.0037 |
| data_status POOR | 3303 | 0.5601 | 0.3997 | 0.4602 | +0.100 | -0.060 | 0.0104 ± 0.003 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 994 | 0.1975 | 0.1978 | -0.0004 ± 0.0005 | 0.5748 | 0.5756 | 0.5024 | 0.4873 | 0.501 | -0.095 ± 0.015 | -0.0087 (8) |
| 3-5 | 629 | 0.2054 | 0.205 | +0.0004 ± 0.0015 | 0.5948 | 0.5925 | 0.5031 | 0.4632 | 0.4769 | -0.100 ± 0.0185 | 0.01 (2) |
| 5-10 | 1471 | 0.2015 | 0.2006 | +0.0010 ± 0.0018 | 0.5895 | 0.5846 | 0.5125 | 0.4387 | 0.467 | -0.091 ± 0.0121 | -0.0143 (7) |
| 10-15 | 1191 | 0.2188 | 0.2099 | +0.0088 ± 0.0033 | 0.6298 | 0.6036 | 0.524 | 0.4004 | 0.4257 | -0.104 ± 0.0135 | -0.048 (5) |
| 15-25 | 1524 | 0.2242 | 0.2078 | +0.0165 ± 0.0046 | 0.643 | 0.5989 | 0.5751 | 0.3802 | 0.4357 | -0.102 ± 0.0117 | -0.004 (10) |
| 25-40 | 871 | 0.222 | 0.2035 | +0.0185 ± 0.0091 | 0.6329 | 0.5877 | 0.6518 | 0.3418 | 0.4673 | -0.069 ± 0.014 | -0.06 (2) |
| 40+ | 185 | 0.2959 | 0.1755 | +0.1204 ± 0.0276 | 0.7971 | 0.524 | 0.7304 | 0.2755 | 0.3784 | -0.083 ± 0.0268 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5221 | 0.1852 | 0.1861 | -0.0008 ± 0.0002 | 0.546 | 0.5469 | 0.4886 | 0.4734 | 0.5039 | -0.022 ± 0.0061 | -0.01 (28) |
| 3-5 | 3489 | 0.1975 | 0.1958 | +0.0017 ± 0.0006 | 0.5748 | 0.5688 | 0.4799 | 0.4401 | 0.4382 | -0.056 ± 0.0076 | 0.0 (3) |
| 5-10 | 7534 | 0.2011 | 0.1979 | +0.0032 ± 0.0008 | 0.588 | 0.577 | 0.4849 | 0.4113 | 0.4267 | -0.043 ± 0.0052 | -0.0114 (22) |
| 10-15 | 6245 | 0.2014 | 0.1858 | +0.0157 ± 0.0014 | 0.5892 | 0.5453 | 0.4855 | 0.3616 | 0.3603 | -0.063 ± 0.0055 | -0.0281 (16) |
| 15-25 | 7869 | 0.2061 | 0.1671 | +0.0390 ± 0.0018 | 0.6041 | 0.4965 | 0.4996 | 0.3041 | 0.3028 | -0.070 ± 0.0046 | -0.0027 (45) |
| 25-40 | 6056 | 0.223 | 0.1264 | +0.0966 ± 0.0029 | 0.6402 | 0.3883 | 0.5275 | 0.2137 | 0.2211 | -0.058 ± 0.0044 | -0.0733 (3) |
| 40+ | 4009 | 0.382 | 0.0446 | +0.3373 ± 0.0038 | 0.9949 | 0.1728 | 0.631 | 0.1028 | 0.0594 | -0.076 ± 0.0032 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 796 | 0.2046 | 0.205 | -0.0004 ± 0.0006 | 0.5898 | 0.591 | 0.5055 | 0.4907 | 0.5151 | -0.102 ± 0.0173 | -0.0117 (6) |
| 3-5 | 561 | 0.211 | 0.208 | +0.0030 ± 0.0015 | 0.6047 | 0.5982 | 0.5127 | 0.4731 | 0.451 | -0.134 ± 0.0207 | 0.01 (2) |
| 5-10 | 1264 | 0.2074 | 0.2053 | +0.0021 ± 0.0019 | 0.6015 | 0.5956 | 0.5397 | 0.4651 | 0.4913 | -0.091 ± 0.0131 | -0.01 (4) |
| 10-15 | 1100 | 0.2112 | 0.2059 | +0.0053 ± 0.0034 | 0.615 | 0.5974 | 0.5632 | 0.4389 | 0.4827 | -0.098 ± 0.0142 | -0.04 (5) |
| 15-25 | 1604 | 0.2307 | 0.2121 | +0.0186 ± 0.0045 | 0.6557 | 0.6088 | 0.5847 | 0.3893 | 0.4408 | -0.098 ± 0.0118 | -0.012 (10) |
| 25-40 | 1130 | 0.2669 | 0.1974 | +0.0694 ± 0.0083 | 0.7447 | 0.5749 | 0.659 | 0.3449 | 0.3938 | -0.121 ± 0.0132 | -0.008 (5) |
| 40+ | 410 | 0.3703 | 0.1628 | +0.2074 ± 0.02 | 1.0073 | 0.4919 | 0.7351 | 0.2461 | 0.2927 | -0.084 ± 0.0192 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4479 | 0.1916 | 0.1919 | -0.0003 ± 0.0002 | 0.5588 | 0.5591 | 0.5077 | 0.4927 | 0.5093 | -0.039 ± 0.0067 | -0.0154 (26) |
| 3-5 | 3045 | 0.1924 | 0.1915 | +0.0010 ± 0.0006 | 0.5615 | 0.5582 | 0.51 | 0.4704 | 0.4768 | -0.046 ± 0.0081 | 0.01 (2) |
| 5-10 | 6724 | 0.1979 | 0.1944 | +0.0035 ± 0.0008 | 0.581 | 0.5683 | 0.508 | 0.4339 | 0.45 | -0.041 ± 0.0054 | -0.0117 (6) |
| 10-15 | 5607 | 0.2015 | 0.191 | +0.0105 ± 0.0015 | 0.5922 | 0.5589 | 0.5111 | 0.3872 | 0.4077 | -0.045 ± 0.0059 | -0.0189 (18) |
| 15-25 | 7876 | 0.217 | 0.1812 | +0.0358 ± 0.0019 | 0.6304 | 0.5314 | 0.5246 | 0.3292 | 0.338 | -0.060 ± 0.0048 | -0.0084 (43) |
| 25-40 | 7138 | 0.2508 | 0.1376 | +0.1132 ± 0.0028 | 0.708 | 0.4204 | 0.5606 | 0.2437 | 0.227 | -0.081 ± 0.0044 | -0.0095 (20) |
| 40+ | 5554 | 0.4006 | 0.0598 | +0.3408 ± 0.0038 | 1.0557 | 0.2148 | 0.6543 | 0.1195 | 0.0819 | -0.074 ± 0.0032 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 969 | 0.1961 | 0.1975 | -0.0014 ± 0.0005 | 0.5719 | 0.5754 | 0.5028 | 0.4874 | 0.5335 | -0.051 ± 0.0149 | -0.012 (10) |
| 3-5 | 676 | 0.2069 | 0.2054 | +0.0015 ± 0.0014 | 0.5993 | 0.5942 | 0.4939 | 0.4544 | 0.4571 | -0.112 ± 0.0182 | -0.0 (4) |
| 5-10 | 1504 | 0.2024 | 0.1988 | +0.0037 ± 0.0017 | 0.5899 | 0.5796 | 0.513 | 0.4393 | 0.4501 | -0.106 ± 0.0119 | -0.01 (9) |
| 10-15 | 1205 | 0.211 | 0.2024 | +0.0085 ± 0.0032 | 0.6126 | 0.5873 | 0.5374 | 0.4143 | 0.4432 | -0.106 ± 0.013 | -0.0286 (7) |
| 15-25 | 1449 | 0.2307 | 0.2127 | +0.0180 ± 0.0047 | 0.6587 | 0.6098 | 0.5861 | 0.3919 | 0.4424 | -0.108 ± 0.0121 | -0.03 (1) |
| 25-40 | 869 | 0.2122 | 0.2087 | +0.0035 ± 0.0091 | 0.612 | 0.5996 | 0.6599 | 0.349 | 0.4971 | -0.056 ± 0.014 | -0.0267 (3) |
| 40+ | 193 | 0.3126 | 0.1801 | +0.1325 ± 0.0275 | 0.8448 | 0.5339 | 0.7411 | 0.2864 | 0.3782 | -0.094 ± 0.028 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5037 | 0.1844 | 0.185 | -0.0006 ± 0.0002 | 0.5436 | 0.5444 | 0.4854 | 0.4701 | 0.4886 | -0.033 ± 0.0061 | -0.0137 (41) |
| 3-5 | 3561 | 0.2041 | 0.2024 | +0.0016 ± 0.0006 | 0.5924 | 0.5871 | 0.4784 | 0.4389 | 0.4389 | -0.055 ± 0.0077 | -0.01 (19) |
| 5-10 | 7701 | 0.1964 | 0.1913 | +0.0051 ± 0.0007 | 0.576 | 0.5602 | 0.4877 | 0.4137 | 0.4166 | -0.055 ± 0.005 | -0.0105 (37) |
| 10-15 | 6184 | 0.1932 | 0.1783 | +0.0149 ± 0.0013 | 0.571 | 0.528 | 0.4946 | 0.3713 | 0.3723 | -0.062 ± 0.0054 | -0.0146 (13) |
| 15-25 | 7953 | 0.2116 | 0.1723 | +0.0393 ± 0.0018 | 0.6172 | 0.5084 | 0.5129 | 0.3185 | 0.3157 | -0.071 ± 0.0046 | -0.0533 (3) |
| 25-40 | 6028 | 0.2173 | 0.1276 | +0.0897 ± 0.0029 | 0.6279 | 0.3909 | 0.5303 | 0.2147 | 0.2327 | -0.049 ± 0.0044 | -0.02 (4) |
| 40+ | 3959 | 0.3917 | 0.0496 | +0.3422 ± 0.004 | 1.021 | 0.1852 | 0.6403 | 0.1088 | 0.0657 | -0.077 ± 0.0034 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1396 | 0.1971 | 0.1972 | -0.0000 ± 0.0004 | 0.5726 | 0.5725 | 0.5077 | 0.4927 | 0.4957 | -0.070 ± 0.0121 | -0.0213 (54) |
| 3-5 | 992 | 0.1892 | 0.1891 | +0.0001 ± 0.0011 | 0.5569 | 0.5547 | 0.4951 | 0.4552 | 0.4718 | -0.058 ± 0.0141 | -0.0194 (34) |
| 5-10 | 2018 | 0.1989 | 0.1945 | +0.0044 ± 0.0015 | 0.5862 | 0.5716 | 0.5074 | 0.4338 | 0.4405 | -0.075 ± 0.01 | -0.005 (78) |
| 10-15 | 1384 | 0.2147 | 0.2016 | +0.0131 ± 0.003 | 0.6231 | 0.5867 | 0.5418 | 0.419 | 0.4256 | -0.092 ± 0.0124 | 0.0014 (65) |
| 15-25 | 1810 | 0.2308 | 0.207 | +0.0238 ± 0.0042 | 0.6585 | 0.5977 | 0.5898 | 0.3948 | 0.4337 | -0.089 ± 0.0108 | -0.0214 (59) |
| 25-40 | 1097 | 0.2395 | 0.2096 | +0.0299 ± 0.0084 | 0.6845 | 0.602 | 0.6878 | 0.3755 | 0.484 | -0.087 ± 0.0129 | -0.0252 (27) |
| 40+ | 389 | 0.3283 | 0.2014 | +0.1269 ± 0.0218 | 0.9457 | 0.5866 | 0.8156 | 0.3392 | 0.4602 | -0.098 ± 0.0203 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5129 | 0.1774 | 0.1776 | -0.0002 ± 0.0002 | 0.5251 | 0.525 | 0.512 | 0.4967 | 0.5069 | -0.039 ± 0.0059 | -0.0145 (98) |
| 3-5 | 3534 | 0.1956 | 0.1949 | +0.0007 ± 0.0006 | 0.5701 | 0.5679 | 0.5007 | 0.4609 | 0.472 | -0.039 ± 0.0075 | -0.0204 (72) |
| 5-10 | 7183 | 0.1958 | 0.1895 | +0.0063 ± 0.0008 | 0.5776 | 0.559 | 0.5013 | 0.4277 | 0.4227 | -0.062 ± 0.0052 | -0.0084 (134) |
| 10-15 | 4937 | 0.2092 | 0.1931 | +0.0161 ± 0.0016 | 0.6092 | 0.5668 | 0.537 | 0.414 | 0.409 | -0.071 ± 0.0063 | -0.0053 (106) |
| 15-25 | 5995 | 0.2304 | 0.1991 | +0.0313 ± 0.0023 | 0.6619 | 0.5772 | 0.5753 | 0.3798 | 0.3985 | -0.067 ± 0.0058 | -0.026 (108) |
| 25-40 | 3962 | 0.257 | 0.1892 | +0.0678 ± 0.0043 | 0.7273 | 0.5515 | 0.6391 | 0.3264 | 0.3771 | -0.068 ± 0.0068 | -0.0246 (52) |
| 40+ | 1741 | 0.3715 | 0.159 | +0.2125 ± 0.0099 | 1.0485 | 0.4737 | 0.7436 | 0.243 | 0.2918 | -0.065 ± 0.0091 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6865 | 1.031 ± 0.034 | 1.104 | 0.1695 | 0.1692 | 0.2145 | 0.2035 |
| gen2 | 6865 | 0.825 ± 0.031 | 1.076 | 0.1737 | 0.1695 | 0.233 | 0.2034 |
| gen1_elo | 6865 | 1.008 ± 0.033 | 1.093 | 0.1761 | 0.1692 | 0.2138 | 0.2036 |
| gen1_sr | 6865 | 1.009 ± 0.04 | 1.135 | 0.1335 | 0.1712 | 0.2292 | 0.203 |
| gen1_ledger | 9086 | 0.866 ± 0.025 | 1.075 | 0.1901 | 0.1763 | 0.2168 | 0.2 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 32,297)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,491 | 23.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,171 | 22.2% |
| BOOK_QUALITY | execution | 5,870 | 18.2% |
| POOR_DATA | data | 3,783 | 11.7% |
| LIMITED_DATA | data | 2,019 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,835 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,347 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,324 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 919 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 537 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.2%, coverage 22.2%, execution 18.2%, data 18.0%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 45.6%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.4%, LEVEL_TRANSFER_RISK 10.2%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.6%, POST_SETTLEMENT_OBSERVATION 22.2%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,147)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,755 | 33.6% |
| STALE_QUOTE | market_freshness | 3,360 | 19.6% |
| BOOK_QUALITY | execution | 3,053 | 17.8% |
| POOR_DATA | data | 1,607 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 979 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 732 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 603 | 3.5% |
| LIMITED_DATA | data | 592 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 333 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 132 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.6%, market_freshness 19.6%, execution 17.8%, data 12.8%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.0%, STALE_KALSHI_QUOTE 53.0%, STALE_PLAYER_DATA 46.2%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.9%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.0%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.6%, POST_SETTLEMENT_OBSERVATION 33.6%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13660, "IDENTITY_AMBIGUOUS": 3487}; ticker orientation: {"VERIFIED": 17147}.

Checks: discipline:AMBIGUOUS 1156, discipline:PASS 15991, identity_confidence:AMBIGUOUS 3161, identity_confidence:PASS 13986, level_mapping:NA 1168, level_mapping:PASS 15979, market_pair:AMBIGUOUS 487, market_pair:NA 373, market_pair:PASS 16287, model_complement:NA 335, model_complement:PASS 16812, namesake:AMBIGUOUS 6, namesake:PASS 17141, physical_match_id:NA 5898, physical_match_id:PASS 11249, player_ids:PASS 17147, same_pair_other_event:PASS 17147, ticker_orientation:PASS 17147

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,230 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.54 | 0.2264 / 0.2207 (781) | 24.5% | 2.5% | 3.1% | 2.7% |
| CHALLENGER | 11,297 | 16.2% | 6.2% | 10.7% | {"coverage": 1072, "market_freshness": 216, "market_freshness/coverage": 215, "data": 157, "model_calibration_or_unknown": 77, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.38 | 0.22 / 0.2094 (2632) | 37.6% | 15.5% | 4.1% | 22.2% |
| DOUBLES | 2,476 | 46.7% | 46.6% | 6.7% | {"execution": 657, "mapping": 322, "market_freshness": 106, "market_freshness/coverage": 64, "coverage": 7} | 23.45 | 0.2997 / 0.234 (601) | 9.4% | 0.0% | 100.0% | 6.0% |
| ITF_MEN | 22,459 | 24.8% | 17.5% | 32.5% | {"coverage": 1913, "market_freshness": 1083, "execution": 972, "data": 834, "market_freshness/coverage": 556, "mapping": 202, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.68 | 0.2157 / 0.1984 (4729) | 39.4% | 69.2% | 15.4% | 21.1% |
| ITF_WOMEN | 29,423 | 26.4% | 19.0% | 45.3% | {"coverage": 2687, "market_freshness": 1695, "execution": 1300, "data": 1107, "market_freshness/coverage": 673, "mapping": 185, "model_calibration_or_unknown": 92, "model_calibration": 22} | 12.51 | 0.2032 / 0.1935 (5644) | 40.6% | 57.3% | 9.9% | 21.3% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,724 | 6.1% | 5.2% | 1.7% | {"market_freshness": 110, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.7 | 0.2305 / 0.2218 (762) | 29.7% | 2.1% | 1.3% | 3.6% |
| WTA125 | 2,579 | 11.3% | 9.8% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 19, "coverage": 14, "mapping": 4} | 9.17 | 0.2072 / 0.1899 (760) | 28.9% | 10.7% | 4.2% | 7.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 21.5h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1296 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 869 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 899 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 48 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 49 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 50 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9692, "by_level_share_of_ge_25pp": {"ATP": 0.0138, "CHALLENGER": 0.1068, "DOUBLES": 0.0674, "ITF_MEN": 0.3247, "ITF_WOMEN": 0.4526, "OTHER": 0.0007, "WTA": 0.0169, "WTA125": 0.017}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5304, "share_primary_cause_market_settled_or_in_play": 0.4279, "share_primary_cause_stale_quote_only": 0.196}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17147, "identity_ambiguous_share": 0.2034, "ticker_orientation": {"VERIFIED": 17147}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11249, "with_external": 605, "coverage": 0.0538, "external_status": {"EXTERNAL_STALE": 387, "AGREES_WITH_KALSHI": 205, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 387, "MODEL_LONE_OUTLIER": 205, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3388, "share_external_supports_model": 0.0215}, "pregame_clean_ge_25pp": {"n": 5373, "with_external": 575, "coverage": 0.107, "external_status": {"EXTERNAL_STALE": 364, "AGREES_WITH_KALSHI": 198, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 364, "MODEL_LONE_OUTLIER": 198, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3443, "share_external_supports_model": 0.0226}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 483.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2095, "data_status": {"POOR": 9662, "LIMITED": 4446, "ADEQUATE": 3039}, "comparison_lt_10pp": {"median_thinner_serve_points": 1719.0, "median_sample_ratio": 1.7, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1383, "model_minus_observed": 0.0579, "kalshi_minus_observed": -0.0815, "brier_diff_model_minus_kalshi": 0.0004}, "4-10x": {"n": 949, "model_minus_observed": 0.0877, "kalshi_minus_observed": -0.0573, "brier_diff_model_minus_kalshi": 0.0085}, "<2x": {"n": 3366, "model_minus_observed": 0.1009, "kalshi_minus_observed": -0.0223, "brier_diff_model_minus_kalshi": 0.0147}, ">=10x": {"n": 1167, "model_minus_observed": 0.1176, "kalshi_minus_observed": -0.0556, "brier_diff_model_minus_kalshi": 0.0147}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6865, "model": {"intercept": -0.557, "slope": 0.825, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.187, "slope": 1.076, "slope_se": 0.034}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1695, "model_brier": 0.233, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0296, "brier_diff_se": 0.0023, "model_logloss": 0.663, "kalshi_logloss": 0.589}, "fair_v1": {"n": 6865, "model": {"intercept": -0.448, "slope": 1.031, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.253, "slope": 1.104, "slope_se": 0.034}, "mean_extremity_model": 0.1695, "mean_extremity_kalshi": 0.1692, "model_brier": 0.2145, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.011, "brier_diff_se": 0.0019, "model_logloss": 0.6178, "kalshi_logloss": 0.5893}, "gen1_elo": {"n": 6865, "model": {"intercept": -0.436, "slope": 1.008, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.254, "slope": 1.093, "slope_se": 0.034}, "mean_extremity_model": 0.1761, "mean_extremity_kalshi": 0.1692, "model_brier": 0.2138, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0102, "brier_diff_se": 0.0019, "model_logloss": 0.6168, "kalshi_logloss": 0.5894}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2458, "share_ge_15": 0.4419, "median_abs_gap": 13.0, "n": 45771}, "gen1_elo": {"share_ge_25": 0.243, "share_ge_15": 0.4382, "median_abs_gap": 12.75, "n": 45771}, "gen1_sr": {"share_ge_25": 0.3121, "share_ge_15": 0.5194, "median_abs_gap": 15.77, "n": 45771}, "gen2": {"share_ge_25": 0.3128, "share_ge_15": 0.5087, "median_abs_gap": 15.39, "n": 45771}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1513, "share_ge_15": 0.3539, "median_abs_gap": 10.71, "n": 35501}, "gen1_elo": {"share_ge_25": 0.1495, "share_ge_15": 0.349, "median_abs_gap": 10.49, "n": 35501}, "gen1_sr": {"share_ge_25": 0.2174, "share_ge_15": 0.4406, "median_abs_gap": 13.01, "n": 35503}, "gen2": {"share_ge_25": 0.2316, "share_ge_15": 0.4393, "median_abs_gap": 12.86, "n": 35503}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.54, "share_ge_25_all": 0.038, "share_ge_25_pregame_clean": 0.0328}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0612, "share_ge_25_pregame_clean": 0.0518}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2373, "share_within_10pp_all": 0.4398, "share_within_10pp_pregame_clean": 0.4916, "corr_model_vs_mid_pregame_clean": 0.8515}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 994, "model_brier": 0.1975, "kalshi_brier": 0.1978, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1191, "model_brier": 0.2188, "kalshi_brier": 0.2099, "brier_diff_model_minus_kalshi": 0.0088}, "15-25": {"n_settled": 1524, "model_brier": 0.2242, "kalshi_brier": 0.2078, "brier_diff_model_minus_kalshi": 0.0165}, "25-40": {"n_settled": 871, "model_brier": 0.222, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0185}, "3-5": {"n_settled": 629, "model_brier": 0.2054, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 185, "model_brier": 0.2959, "kalshi_brier": 0.1755, "brier_diff_model_minus_kalshi": 0.1204}, "5-10": {"n_settled": 1471, "model_brier": 0.2015, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.557, "slope": 0.825, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.187, "slope": 1.076, "slope_se": 0.034}, "n": 6865}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.488, "slope": 0.866, "slope_se": 0.025}, "kalshi_slope": {"intercept": 0.173, "slope": 1.075, "slope_se": 0.029}, "n": 9086}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 601, "model_brier": 0.2997, "kalshi_brier": 0.234, "brier_diff_model_minus_kalshi": 0.0657, "brier_diff_se": 0.0121, "corr_model_outcome": 0.0901, "corr_kalshi_outcome": 0.2692}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
