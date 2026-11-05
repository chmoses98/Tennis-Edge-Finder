# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-05T19:26Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 79,683): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.0%; median gap 11.81 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.7%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,250): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.7%, STALE_QUOTE 19.5%, BOOK_QUALITY 17.8%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.7%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.7%, market_freshness 19.5%, execution 17.8%, data 12.8%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.1% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,250 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.4%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.3% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 485.0 points vs 1719.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.031, Gen-2 0.826, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 881 model 0.2215 vs Kalshi 0.2039; n 185 model 0.2959 vs Kalshi 0.1755.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 339,105 model-market comparisons (554,804 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 112,946 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-05T19:07:32.459320+00:00'], shadow board 91,533 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-05T19:07:36.533361+00:00'], Model 4 42,165 rows, 28,095 settled tickers, 10,618 tickers with an external scan.
* By model: {"gen1_ledger": 76142, "gen1_elo": 45996, "fair_v1": 45996, "gen2": 45996, "gen1_sr": 45996, "model4_fundamental": 39531, "model4_conditioned": 39448}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 79,683 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.0 | 11.81 | 40.8% | 21.6% |
| MW fair_v1 | 45,996 | 12.8 | 8.7 | 18.8 | 15.4 | 19.6 | 14.8 | 9.8 | 13.01 | 44.3% | 24.6% |
| MW gen1_elo | 45,996 | 12.6 | 8.8 | 19.3 | 15.4 | 19.5 | 14.6 | 9.7 | 12.77 | 43.9% | 24.3% |
| MW gen1_ledger | 33,687 | 15.8 | 10.9 | 22.2 | 15.2 | 18.4 | 12.1 | 5.5 | 10.26 | 36.0% | 17.6% |
| MW gen1_sr | 45,996 | 10.1 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.5 | 15.8 | 52.0% | 31.3% |
| MW gen2 | 45,996 | 11.1 | 7.6 | 16.7 | 13.8 | 19.6 | 17.7 | 13.6 | 15.43 | 50.9% | 31.3% |
| all families model4_conditioned | 39,448 | 22.2 | 18.0 | 34.2 | 17.1 | 5.0 | 2.2 | 1.2 | 6.06 | 8.5% | 3.4% |
| all families model4_fundamental | 39,531 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.6%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.35pp; >=10pp 44.9%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,917 | 28.4 | 15.7 | 27.6 | 13.4 | 10.6 | 3.6 | 0.6 | 5.77 | 14.9% | 4.3% |
| CHALLENGER | 6,889 | 15.9 | 9.8 | 20.7 | 15.3 | 16.2 | 11.3 | 10.7 | 10.93 | 38.2% | 22.0% |
| ITF_MEN | 12,947 | 9.8 | 7.4 | 17.1 | 15.2 | 21.2 | 17.3 | 12.0 | 15.18 | 50.5% | 29.2% |
| ITF_WOMEN | 17,913 | 9.5 | 7.1 | 16.0 | 14.9 | 22.1 | 18.3 | 12.0 | 15.84 | 52.5% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,997 | 16.7 | 13.2 | 24.6 | 21.0 | 16.5 | 6.9 | 1.1 | 8.73 | 24.5% | 8.0% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,917 | 26.9 | 15.8 | 26.0 | 15.4 | 11.4 | 3.7 | 0.8 | 6.02 | 15.9% | 4.5% |
| CHALLENGER | 6,889 | 14.8 | 9.0 | 18.6 | 14.0 | 18.7 | 13.5 | 11.3 | 12.49 | 43.5% | 24.8% |
| ITF_MEN | 12,947 | 8.2 | 6.2 | 15.2 | 13.8 | 20.0 | 20.5 | 16.2 | 17.85 | 56.6% | 36.7% |
| ITF_WOMEN | 17,913 | 7.8 | 5.8 | 14.1 | 12.9 | 20.7 | 21.2 | 17.6 | 19.11 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,997 | 14.1 | 10.2 | 21.9 | 16.0 | 22.2 | 13.1 | 2.6 | 11.2 | 37.8% | 15.6% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,917 | 22.9 | 14.0 | 25.2 | 15.6 | 15.0 | 6.1 | 1.2 | 7.15 | 22.3% | 7.3% |
| CHALLENGER | 6,889 | 15.2 | 9.6 | 20.9 | 15.6 | 16.0 | 11.9 | 10.8 | 11.2 | 38.7% | 22.7% |
| ITF_MEN | 12,947 | 9.5 | 7.2 | 17.3 | 14.3 | 21.9 | 17.3 | 12.4 | 15.61 | 51.7% | 29.7% |
| ITF_WOMEN | 17,913 | 9.3 | 6.9 | 16.3 | 15.8 | 22.2 | 18.1 | 11.4 | 15.57 | 51.7% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,997 | 22.8 | 17.0 | 31.8 | 15.2 | 8.8 | 3.3 | 1.1 | 6.12 | 13.2% | 4.4% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,319 | 26.7 | 19.7 | 30.0 | 12.3 | 8.2 | 2.6 | 0.4 | 5.37 | 11.2% | 3.0% |
| CHALLENGER | 4,447 | 22.2 | 14.5 | 27.8 | 14.7 | 13.5 | 5.8 | 1.5 | 7.09 | 20.8% | 7.3% |
| DOUBLES | 2,491 | 5.0 | 4.5 | 12.7 | 11.0 | 20.1 | 24.9 | 21.8 | 23.53 | 66.8% | 46.7% |
| ITF_MEN | 9,640 | 13.0 | 9.6 | 21.3 | 15.8 | 21.5 | 13.0 | 5.9 | 11.77 | 40.4% | 18.9% |
| ITF_WOMEN | 11,642 | 13.4 | 9.2 | 20.0 | 15.7 | 21.4 | 14.9 | 5.5 | 12.23 | 41.7% | 20.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,743 | 24.2 | 15.9 | 31.1 | 16.6 | 9.2 | 2.6 | 0.2 | 6.57 | 12.0% | 2.9% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,802 | 28.9 | 15.8 | 28.0 | 13.4 | 10.4 | 3.2 | 0.3 | 5.67 | 13.9% | 3.5% |
| CHALLENGER | 4,880 | 20.4 | 12.2 | 25.6 | 18.1 | 16.2 | 6.0 | 1.6 | 8.27 | 23.8% | 7.6% |
| ITF_MEN | 9,507 | 12.0 | 8.7 | 20.7 | 17.3 | 22.0 | 14.1 | 5.3 | 12.39 | 41.4% | 19.4% |
| ITF_WOMEN | 13,239 | 11.3 | 8.6 | 18.9 | 17.1 | 24.0 | 15.2 | 5.0 | 13.23 | 44.2% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,885 | 17.0 | 13.3 | 24.9 | 21.4 | 16.5 | 6.3 | 0.6 | 8.52 | 23.4% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,802 | 27.2 | 16.1 | 26.2 | 15.4 | 11.4 | 3.3 | 0.4 | 5.96 | 15.0% | 3.7% |
| CHALLENGER | 4,880 | 18.6 | 11.3 | 23.4 | 16.4 | 19.2 | 9.3 | 1.9 | 9.07 | 30.3% | 11.2% |
| ITF_MEN | 9,508 | 9.6 | 7.3 | 17.6 | 16.0 | 21.7 | 18.6 | 9.3 | 14.88 | 49.5% | 27.9% |
| ITF_WOMEN | 13,240 | 8.8 | 6.8 | 16.0 | 14.4 | 22.7 | 20.5 | 10.8 | 16.58 | 54.0% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,885 | 14.3 | 10.3 | 22.2 | 16.1 | 22.4 | 12.7 | 1.9 | 11.03 | 37.0% | 14.7% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,262 | 26.9 | 19.9 | 30.0 | 12.5 | 8.0 | 2.5 | 0.3 | 5.33 | 10.8% | 2.8% |
| CHALLENGER | 3,928 | 23.5 | 15.4 | 28.9 | 14.8 | 12.9 | 4.0 | 0.4 | 6.62 | 17.4% | 4.5% |
| DOUBLES | 2,340 | 4.9 | 4.6 | 12.9 | 11.1 | 20.0 | 24.8 | 21.8 | 23.41 | 66.5% | 46.6% |
| ITF_MEN | 8,292 | 13.9 | 10.2 | 22.8 | 16.3 | 21.5 | 11.5 | 3.9 | 10.84 | 36.9% | 15.3% |
| ITF_WOMEN | 9,972 | 14.0 | 9.8 | 21.1 | 16.2 | 21.5 | 13.8 | 3.6 | 11.42 | 39.0% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,682 | 24.6 | 16.4 | 31.1 | 16.6 | 9.2 | 2.1 | 0.1 | 6.43 | 11.3% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,491 | 5.0 | 4.5 | 12.7 | 11.0 | 20.1 | 24.9 | 21.8 | 23.53 | 66.8% | 46.7% |
| singles | 31,196 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.73 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 148 | 7.4 | 8.8 | 12.8 | 8.1 | 20.3 | 27.7 | 14.9 | 20.91 | 62.8% | 42.6% |
| Clay | 9,379 | 12.7 | 9.2 | 19.9 | 15.7 | 19.7 | 13.8 | 9.0 | 12.57 | 42.5% | 22.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,015 | 13.4 | 8.8 | 18.8 | 15.2 | 19.2 | 14.8 | 9.8 | 12.85 | 43.8% | 24.6% |
| UNKNOWN | 6,217 | 10.4 | 7.7 | 17.0 | 16.4 | 21.5 | 16.0 | 11.0 | 14.32 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,019 | 19.4 | 12.0 | 22.4 | 16.0 | 15.0 | 9.1 | 6.1 | 8.88 | 30.2% | 15.2% |
| B | 5,623 | 12.9 | 8.8 | 19.8 | 15.7 | 19.5 | 12.7 | 10.7 | 12.57 | 42.9% | 23.4% |
| C | 6,520 | 11.9 | 8.9 | 19.6 | 15.8 | 18.6 | 14.7 | 10.5 | 12.93 | 43.9% | 25.2% |
| D | 7,442 | 11.7 | 8.4 | 17.9 | 15.4 | 21.5 | 15.7 | 9.3 | 13.75 | 46.5% | 25.0% |
| F | 13,392 | 7.4 | 5.6 | 14.9 | 14.7 | 23.5 | 20.8 | 13.1 | 17.71 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,970 | 24.6 | 16.0 | 29.2 | 14.9 | 10.7 | 3.4 | 1.2 | 6.37 | 15.3% | 4.7% |
| B | 4,729 | 16.6 | 10.8 | 24.3 | 16.8 | 18.8 | 9.6 | 3.1 | 9.66 | 31.5% | 12.7% |
| C | 6,657 | 11.2 | 7.9 | 19.4 | 14.8 | 20.9 | 15.7 | 10.2 | 13.49 | 46.8% | 25.9% |
| D | 5,046 | 14.6 | 10.1 | 21.5 | 15.4 | 20.5 | 12.7 | 5.3 | 11.18 | 38.5% | 18.0% |
| F | 8,285 | 10.2 | 8.4 | 16.2 | 14.6 | 23.3 | 19.5 | 7.8 | 15.33 | 50.6% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,727 | 17.8 | 11.0 | 21.5 | 15.8 | 15.3 | 9.9 | 8.7 | 9.95 | 34.0% | 18.6% |
| LIMITED | 10,045 | 13.6 | 9.8 | 20.5 | 16.0 | 19.3 | 13.3 | 7.5 | 11.83 | 40.2% | 20.9% |
| POOR | 21,224 | 9.0 | 6.6 | 16.0 | 15.0 | 22.7 | 18.9 | 11.8 | 16.1 | 53.3% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,710 | 23.8 | 17.8 | 33.2 | 15.6 | 6.4 | 2.9 | 0.4 | 5.92 | 9.7% | 3.3% |
| GAME_SPREAD | 6,573 | 22.5 | 15.2 | 32.3 | 16.9 | 9.0 | 3.4 | 0.6 | 6.72 | 13.1% | 4.0% |
| MATCH_WINNER | 33,687 | 15.8 | 10.9 | 22.2 | 15.2 | 18.4 | 12.1 | 5.5 | 10.26 | 36.0% | 17.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,120 | 27.9 | 16.8 | 30.6 | 12.7 | 9.2 | 2.5 | 0.3 | 5.63 | 12.0% | 2.8% |
| TOTAL_GAMES | 11,028 | 9.8 | 10.8 | 35.5 | 26.0 | 10.7 | 4.3 | 3.0 | 9.21 | 17.9% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,988 | 24.4 | 28.9 | 33.2 | 8.1 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,106 | 46.8 | 16.1 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.3 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,354 | 6.5 | 9.8 | 40.2 | 30.2 | 7.5 | 3.3 | 2.4 | 9.22 | 13.2% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,023 | 23.9 | 16.6 | 34.8 | 14.7 | 6.9 | 2.6 | 0.5 | 6.05 | 10.0% | 3.1% |
| GAME_SPREAD | 9,115 | 20.6 | 13.6 | 28.2 | 20.1 | 12.0 | 4.5 | 1.1 | 7.63 | 17.6% | 5.6% |
| TOTAL_GAMES | 16,393 | 10.0 | 10.8 | 36.2 | 24.3 | 11.5 | 4.5 | 2.6 | 9.07 | 18.6% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 45,996 | 44.3% | 24.6% | 13.01 | 35.4% | 15.1% | 10.71 |
| gen1_elo | 45,996 | 43.9% | 24.3% | 12.77 | 34.9% | 14.9% | 10.49 |
| gen1_sr | 45,996 | 52.0% | 31.3% | 15.8 | 44.0% | 21.7% | 13.01 |
| gen2 | 45,996 | 50.9% | 31.3% | 15.43 | 43.9% | 23.2% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,896 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 26,100 | 10.8 | 7.4 | 16.8 | 14.0 | 19.3 | 17.0 | 14.8 | 15.41 | 51.0% | 31.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 27,155 | 16.4 | 11.2 | 22.8 | 15.2 | 17.9 | 11.6 | 4.8 | 9.87 | 34.3% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 79,683 | 27155 | 23368 | 29160 | 24.7 | 121.8 | 1451.1 |
| ge_15pp | 32,472 | 9316 | 8324 | 14832 | 28.1 | 427.6 | 1451.1 |
| ge_25pp | 17,250 | 4453 | 3632 | 9165 | 32.9 | 575.7 | 1431.1 |
| lt_10pp | 35,004 | 13698 | 11051 | 10255 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261105T192603Z-0a52354f`: 290 priced rows, quote age at build {'median': 18.8, 'max': 18.9}, freshness {'AGING': 290}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,610 | 19.1 | 10.9 | 25.4 | 17.9 | 18.2 | 7.4 | 1.0 | 8.86 | 26.6% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 932 | 65.8 | 34.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,013 | 0.0 | 2.3 | 36.9 | 26.4 | 24.3 | 9.3 | 0.8 | 11.88 | 34.5% | 10.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 45,996 | 7663 (16.7%) | 26.3% | 1.0% | {"EXTERNAL_STALE": 4610, "AGREES_WITH_KALSHI": 2013, "ALL_AGREE": 932, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,357 | 1951 (9.6%) | 35.6% | 1.5% | {"EXTERNAL_STALE": 1227, "AGREES_WITH_KALSHI": 694, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,335 | 607 (5.4%) | 33.8% | 2.1% | {"EXTERNAL_STALE": 389, "AGREES_WITH_KALSHI": 205, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,392 | 577 (10.7%) | 34.3% | 2.2% | {"EXTERNAL_STALE": 366, "AGREES_WITH_KALSHI": 198, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,537 | 4350 (23.5%) | 18.1% | 1.0% | {"EXTERNAL_STALE": 2557, "ALL_AGREE": 932, "AGREES_WITH_KALSHI": 788, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,001 | 10.4 | 7.7 | 19.6 | 14.7 | 21.6 | 16.2 | 9.8 | 14.02 | 47.6% | 26.0% |
| 4-10x | 6,170 | 11.4 | 8.5 | 18.5 | 15.3 | 22.0 | 14.3 | 10.0 | 13.71 | 46.3% | 24.3% |
| <2x | 23,468 | 14.9 | 9.8 | 19.7 | 16.1 | 17.6 | 13.1 | 8.8 | 11.55 | 39.5% | 21.9% |
| >=10x | 7,357 | 10.5 | 6.4 | 15.0 | 14.4 | 21.7 | 19.0 | 13.0 | 16.35 | 53.7% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,023 | 12.4 | 8.7 | 20.0 | 16.2 | 19.0 | 13.5 | 10.2 | 12.66 | 42.7% | 23.7% |
| 300-1000 | 9,948 | 11.8 | 8.8 | 17.8 | 15.3 | 20.7 | 16.3 | 9.4 | 13.67 | 46.4% | 25.7% |
| <300 | 14,492 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 19.9 | 13.0 | 17.1 | 56.0% | 32.9% |
| >=3000 | 9,533 | 21.2 | 13.0 | 23.9 | 15.7 | 14.0 | 7.2 | 5.0 | 7.74 | 26.2% | 12.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1393 | 0.5479 | 0.4087 | 0.4917 | +0.056 | -0.083 | -0.0001 ± 0.0041 |
| ratio 4-10x | 956 | 0.5759 | 0.4311 | 0.4885 | +0.087 | -0.057 | 0.0082 ± 0.0051 |
| ratio <2x | 3398 | 0.5371 | 0.414 | 0.4364 | +0.101 | -0.022 | 0.0146 ± 0.0025 |
| ratio >=10x | 1176 | 0.5642 | 0.391 | 0.4464 | +0.118 | -0.055 | 0.0147 ± 0.0052 |
| thinner_sample 1000-3000 | 1917 | 0.5394 | 0.412 | 0.4486 | +0.091 | -0.037 | 0.0107 ± 0.0033 |
| thinner_sample 300-1000 | 1575 | 0.5629 | 0.4226 | 0.4762 | +0.087 | -0.054 | 0.0039 ± 0.0039 |
| thinner_sample <300 | 2259 | 0.5577 | 0.3897 | 0.4546 | +0.103 | -0.065 | 0.013 ± 0.0037 |
| thinner_sample >=3000 | 1172 | 0.5306 | 0.437 | 0.4462 | +0.084 | -0.009 | 0.0157 ± 0.0033 |
| data_status ADEQUATE | 1909 | 0.5323 | 0.429 | 0.4395 | +0.093 | -0.011 | 0.0157 ± 0.0028 |
| data_status LIMITED | 1687 | 0.5482 | 0.4156 | 0.4689 | +0.079 | -0.053 | 0.0064 ± 0.0036 |
| data_status POOR | 3327 | 0.5594 | 0.3992 | 0.4599 | +0.100 | -0.061 | 0.0102 ± 0.003 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 998 | 0.1972 | 0.1976 | -0.0003 ± 0.0005 | 0.5742 | 0.575 | 0.5027 | 0.4875 | 0.5 | -0.096 ± 0.0149 | -0.0087 (8) |
| 3-5 | 639 | 0.2048 | 0.2047 | +0.0001 ± 0.0014 | 0.5933 | 0.5918 | 0.5025 | 0.4626 | 0.4804 | -0.095 ± 0.0183 | 0.01 (2) |
| 5-10 | 1486 | 0.2019 | 0.2012 | +0.0008 ± 0.0017 | 0.5903 | 0.5861 | 0.5116 | 0.4378 | 0.467 | -0.090 ± 0.0121 | -0.0143 (7) |
| 10-15 | 1201 | 0.2188 | 0.2094 | +0.0094 ± 0.0033 | 0.6298 | 0.6024 | 0.5235 | 0.4 | 0.423 | -0.106 ± 0.0134 | -0.048 (5) |
| 15-25 | 1533 | 0.2242 | 0.208 | +0.0162 ± 0.0045 | 0.6429 | 0.5996 | 0.575 | 0.3802 | 0.4364 | -0.101 ± 0.0117 | -0.004 (10) |
| 25-40 | 881 | 0.2215 | 0.2039 | +0.0175 ± 0.0091 | 0.6317 | 0.5886 | 0.6515 | 0.3416 | 0.4688 | -0.067 ± 0.0139 | -0.06 (2) |
| 40+ | 185 | 0.2959 | 0.1755 | +0.1204 ± 0.0276 | 0.7971 | 0.524 | 0.7304 | 0.2755 | 0.3784 | -0.083 ± 0.0268 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5246 | 0.1855 | 0.1863 | -0.0009 ± 0.0002 | 0.5466 | 0.5475 | 0.4887 | 0.4735 | 0.5046 | -0.022 ± 0.006 | -0.01 (28) |
| 3-5 | 3525 | 0.1973 | 0.1957 | +0.0016 ± 0.0006 | 0.5743 | 0.5686 | 0.4805 | 0.4407 | 0.4403 | -0.055 ± 0.0075 | 0.0 (3) |
| 5-10 | 7592 | 0.2014 | 0.1982 | +0.0032 ± 0.0008 | 0.5885 | 0.5776 | 0.4844 | 0.4107 | 0.4265 | -0.043 ± 0.0052 | -0.0114 (22) |
| 10-15 | 6289 | 0.2013 | 0.1855 | +0.0158 ± 0.0014 | 0.5888 | 0.5445 | 0.4848 | 0.3609 | 0.359 | -0.064 ± 0.0055 | -0.0281 (16) |
| 15-25 | 7929 | 0.2059 | 0.1671 | +0.0387 ± 0.0018 | 0.6035 | 0.4968 | 0.4993 | 0.3038 | 0.3033 | -0.069 ± 0.0046 | -0.0027 (45) |
| 25-40 | 6116 | 0.2229 | 0.1264 | +0.0964 ± 0.0028 | 0.6399 | 0.3885 | 0.5273 | 0.2136 | 0.2212 | -0.058 ± 0.0044 | -0.0733 (3) |
| 40+ | 4043 | 0.3823 | 0.0443 | +0.3380 ± 0.0038 | 0.9959 | 0.172 | 0.631 | 0.1025 | 0.0589 | -0.077 ± 0.0031 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 800 | 0.2043 | 0.2047 | -0.0004 ± 0.0005 | 0.5892 | 0.5905 | 0.506 | 0.4911 | 0.515 | -0.102 ± 0.0172 | -0.0117 (6) |
| 3-5 | 568 | 0.2111 | 0.2081 | +0.0030 ± 0.0015 | 0.6048 | 0.5984 | 0.5126 | 0.4731 | 0.4507 | -0.134 ± 0.0206 | 0.01 (2) |
| 5-10 | 1279 | 0.2076 | 0.2058 | +0.0018 ± 0.0019 | 0.6017 | 0.5968 | 0.5397 | 0.4652 | 0.4934 | -0.089 ± 0.0131 | -0.01 (4) |
| 10-15 | 1107 | 0.2116 | 0.2065 | +0.0051 ± 0.0034 | 0.6157 | 0.5988 | 0.5631 | 0.4387 | 0.4833 | -0.097 ± 0.0142 | -0.04 (5) |
| 15-25 | 1616 | 0.2306 | 0.212 | +0.0186 ± 0.0045 | 0.6555 | 0.6083 | 0.5842 | 0.3888 | 0.44 | -0.098 ± 0.0117 | -0.012 (10) |
| 25-40 | 1142 | 0.2659 | 0.1973 | +0.0686 ± 0.0083 | 0.7425 | 0.5746 | 0.6587 | 0.3446 | 0.3949 | -0.118 ± 0.0131 | -0.008 (5) |
| 40+ | 411 | 0.3707 | 0.1626 | +0.2081 ± 0.0199 | 1.0081 | 0.4915 | 0.7351 | 0.2462 | 0.292 | -0.085 ± 0.0191 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4508 | 0.1919 | 0.1922 | -0.0003 ± 0.0002 | 0.5594 | 0.5598 | 0.5076 | 0.4925 | 0.5109 | -0.037 ± 0.0067 | -0.0154 (26) |
| 3-5 | 3064 | 0.1927 | 0.1917 | +0.0010 ± 0.0006 | 0.5619 | 0.5587 | 0.5104 | 0.4707 | 0.4772 | -0.046 ± 0.0081 | 0.01 (2) |
| 5-10 | 6779 | 0.1979 | 0.1945 | +0.0034 ± 0.0008 | 0.5809 | 0.5686 | 0.508 | 0.4339 | 0.4507 | -0.041 ± 0.0054 | -0.0117 (6) |
| 10-15 | 5645 | 0.2017 | 0.1914 | +0.0103 ± 0.0015 | 0.5925 | 0.56 | 0.5106 | 0.3867 | 0.4081 | -0.044 ± 0.0059 | -0.0189 (18) |
| 15-25 | 7952 | 0.2166 | 0.1808 | +0.0358 ± 0.0019 | 0.6294 | 0.5305 | 0.5241 | 0.3287 | 0.3374 | -0.060 ± 0.0048 | -0.0084 (43) |
| 25-40 | 7197 | 0.2505 | 0.1376 | +0.1130 ± 0.0028 | 0.7072 | 0.4204 | 0.5604 | 0.2435 | 0.2273 | -0.080 ± 0.0044 | -0.0095 (20) |
| 40+ | 5595 | 0.401 | 0.0595 | +0.3415 ± 0.0038 | 1.0569 | 0.214 | 0.6544 | 0.1194 | 0.0813 | -0.074 ± 0.0032 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 974 | 0.1957 | 0.1971 | -0.0014 ± 0.0005 | 0.5711 | 0.5745 | 0.5024 | 0.487 | 0.5329 | -0.051 ± 0.0149 | -0.012 (10) |
| 3-5 | 680 | 0.2064 | 0.2049 | +0.0015 ± 0.0014 | 0.5983 | 0.5931 | 0.4944 | 0.4549 | 0.4574 | -0.112 ± 0.0182 | -0.0 (4) |
| 5-10 | 1522 | 0.2028 | 0.1993 | +0.0035 ± 0.0017 | 0.5905 | 0.5808 | 0.5119 | 0.4382 | 0.4507 | -0.104 ± 0.0118 | -0.01 (9) |
| 10-15 | 1218 | 0.2113 | 0.2023 | +0.0089 ± 0.0032 | 0.6132 | 0.5869 | 0.5369 | 0.4138 | 0.4409 | -0.107 ± 0.0129 | -0.0286 (7) |
| 15-25 | 1460 | 0.2307 | 0.2129 | +0.0178 ± 0.0047 | 0.6585 | 0.6103 | 0.5864 | 0.3922 | 0.4432 | -0.107 ± 0.0121 | -0.03 (1) |
| 25-40 | 874 | 0.2118 | 0.2087 | +0.0030 ± 0.0091 | 0.6111 | 0.5997 | 0.6595 | 0.3487 | 0.4977 | -0.055 ± 0.0139 | -0.0267 (3) |
| 40+ | 195 | 0.3097 | 0.1824 | +0.1274 ± 0.0275 | 0.8383 | 0.5387 | 0.7419 | 0.2873 | 0.3846 | -0.087 ± 0.0282 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5064 | 0.1848 | 0.1854 | -0.0007 ± 0.0002 | 0.5445 | 0.5454 | 0.4854 | 0.47 | 0.4889 | -0.032 ± 0.0061 | -0.0137 (41) |
| 3-5 | 3596 | 0.2038 | 0.2022 | +0.0016 ± 0.0006 | 0.5918 | 0.5865 | 0.4772 | 0.4378 | 0.438 | -0.054 ± 0.0076 | -0.01 (19) |
| 5-10 | 7757 | 0.1962 | 0.1911 | +0.0051 ± 0.0007 | 0.5756 | 0.5597 | 0.487 | 0.413 | 0.416 | -0.055 ± 0.005 | -0.0105 (37) |
| 10-15 | 6245 | 0.1935 | 0.1784 | +0.0151 ± 0.0013 | 0.5715 | 0.5282 | 0.4943 | 0.3711 | 0.3713 | -0.062 ± 0.0054 | -0.0146 (13) |
| 15-25 | 8009 | 0.2114 | 0.1724 | +0.0390 ± 0.0018 | 0.6167 | 0.5087 | 0.5127 | 0.3183 | 0.3163 | -0.070 ± 0.0046 | -0.0533 (3) |
| 25-40 | 6067 | 0.2172 | 0.1275 | +0.0897 ± 0.0029 | 0.6277 | 0.3906 | 0.5299 | 0.2143 | 0.2322 | -0.049 ± 0.0044 | -0.02 (4) |
| 40+ | 4002 | 0.3915 | 0.0498 | +0.3417 ± 0.004 | 1.0205 | 0.1855 | 0.6406 | 0.1089 | 0.0665 | -0.076 ± 0.0034 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1408 | 0.1971 | 0.1971 | -0.0001 ± 0.0004 | 0.5726 | 0.5725 | 0.509 | 0.4939 | 0.4986 | -0.068 ± 0.0121 | -0.0213 (54) |
| 3-5 | 1002 | 0.1889 | 0.1887 | +0.0002 ± 0.0011 | 0.556 | 0.5536 | 0.4957 | 0.4559 | 0.4721 | -0.058 ± 0.014 | -0.0194 (34) |
| 5-10 | 2033 | 0.1992 | 0.1947 | +0.0045 ± 0.0015 | 0.5868 | 0.5722 | 0.5072 | 0.4336 | 0.4402 | -0.075 ± 0.01 | -0.005 (78) |
| 10-15 | 1397 | 0.2145 | 0.2019 | +0.0126 ± 0.003 | 0.6225 | 0.5874 | 0.5417 | 0.4189 | 0.4273 | -0.090 ± 0.0124 | 0.0014 (65) |
| 15-25 | 1818 | 0.2307 | 0.2071 | +0.0237 ± 0.0042 | 0.6584 | 0.5978 | 0.5895 | 0.3945 | 0.4334 | -0.089 ± 0.0108 | -0.0214 (59) |
| 25-40 | 1105 | 0.2393 | 0.2099 | +0.0295 ± 0.0084 | 0.684 | 0.6026 | 0.6882 | 0.3758 | 0.4851 | -0.086 ± 0.0129 | -0.0252 (27) |
| 40+ | 392 | 0.3279 | 0.2022 | +0.1257 ± 0.0217 | 0.9447 | 0.5882 | 0.816 | 0.3399 | 0.4617 | -0.098 ± 0.0204 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5177 | 0.1777 | 0.1779 | -0.0002 ± 0.0002 | 0.5258 | 0.5258 | 0.5125 | 0.4973 | 0.5096 | -0.037 ± 0.0059 | -0.0145 (98) |
| 3-5 | 3560 | 0.1959 | 0.1951 | +0.0007 ± 0.0006 | 0.5708 | 0.5684 | 0.5009 | 0.4611 | 0.4719 | -0.040 ± 0.0075 | -0.0204 (72) |
| 5-10 | 7247 | 0.1959 | 0.1896 | +0.0063 ± 0.0008 | 0.5778 | 0.5591 | 0.5008 | 0.4272 | 0.4222 | -0.061 ± 0.0052 | -0.0084 (134) |
| 10-15 | 4967 | 0.2091 | 0.1931 | +0.0160 ± 0.0015 | 0.6089 | 0.5668 | 0.5369 | 0.414 | 0.4091 | -0.071 ± 0.0063 | -0.0053 (106) |
| 15-25 | 6025 | 0.2303 | 0.1991 | +0.0312 ± 0.0023 | 0.6616 | 0.5773 | 0.575 | 0.3797 | 0.3985 | -0.067 ± 0.0058 | -0.026 (108) |
| 25-40 | 3981 | 0.2567 | 0.1894 | +0.0673 ± 0.0043 | 0.7266 | 0.552 | 0.6393 | 0.3266 | 0.378 | -0.067 ± 0.0067 | -0.0246 (52) |
| 40+ | 1754 | 0.3709 | 0.1592 | +0.2117 ± 0.0098 | 1.0468 | 0.4741 | 0.7436 | 0.2435 | 0.2925 | -0.065 ± 0.0091 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6923 | 1.031 ± 0.033 | 1.102 | 0.1695 | 0.1693 | 0.2144 | 0.2036 |
| gen2 | 6923 | 0.826 ± 0.03 | 1.075 | 0.1737 | 0.1696 | 0.2328 | 0.2035 |
| gen1_elo | 6923 | 1.009 ± 0.032 | 1.092 | 0.1761 | 0.1694 | 0.2137 | 0.2037 |
| gen1_sr | 6923 | 1.008 ± 0.04 | 1.134 | 0.1336 | 0.1713 | 0.2291 | 0.2031 |
| gen1_ledger | 9155 | 0.866 ± 0.025 | 1.074 | 0.1901 | 0.1764 | 0.2167 | 0.2001 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 32,472)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,494 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,258 | 22.4% |
| BOOK_QUALITY | execution | 5,893 | 18.1% |
| POOR_DATA | data | 3,806 | 11.7% |
| LIMITED_DATA | data | 2,021 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,851 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,360 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,327 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 924 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 537 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.4%, execution 18.1%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 45.7%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.3%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.2%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.8%, POST_SETTLEMENT_OBSERVATION 22.4%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,250)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,819 | 33.7% |
| STALE_QUOTE | market_freshness | 3,364 | 19.5% |
| BOOK_QUALITY | execution | 3,064 | 17.8% |
| POOR_DATA | data | 1,615 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 988 | 5.7% |
| IDENTITY_AMBIGUOUS | mapping | 735 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 605 | 3.5% |
| LIMITED_DATA | data | 592 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 335 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 132 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.7%, market_freshness 19.5%, execution 17.8%, data 12.8%, market_freshness/coverage 9.2%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 62.0%, STALE_KALSHI_QUOTE 53.1%, STALE_PLAYER_DATA 46.1%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.8%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 9.0%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.8%, POST_SETTLEMENT_OBSERVATION 33.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13748, "IDENTITY_AMBIGUOUS": 3502}; ticker orientation: {"VERIFIED": 17250}.

Checks: discipline:AMBIGUOUS 1162, discipline:PASS 16088, identity_confidence:AMBIGUOUS 3174, identity_confidence:PASS 14076, level_mapping:NA 1174, level_mapping:PASS 16076, market_pair:AMBIGUOUS 489, market_pair:NA 374, market_pair:PASS 16387, model_complement:NA 336, model_complement:PASS 16914, namesake:AMBIGUOUS 6, namesake:PASS 17244, physical_match_id:NA 5915, physical_match_id:PASS 11335, player_ids:PASS 17250, same_pair_other_event:PASS 17250, ticker_orientation:PASS 17250

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,236 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.54 | 0.2268 / 0.2215 (789) | 24.5% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,336 | 16.2% | 6.2% | 10.7% | {"coverage": 1080, "market_freshness/coverage": 216, "market_freshness": 215, "data": 157, "model_calibration_or_unknown": 78, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.2199 / 0.2094 (2650) | 37.6% | 15.5% | 4.1% | 22.3% |
| DOUBLES | 2,491 | 46.7% | 46.6% | 6.7% | {"execution": 661, "mapping": 323, "market_freshness": 106, "market_freshness/coverage": 65, "coverage": 7} | 23.41 | 0.2991 / 0.2341 (612) | 9.4% | 0.0% | 100.0% | 6.1% |
| ITF_MEN | 22,587 | 24.8% | 17.5% | 32.5% | {"coverage": 1932, "market_freshness": 1089, "execution": 975, "data": 837, "market_freshness/coverage": 560, "mapping": 203, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.67 | 0.2156 / 0.1984 (4765) | 39.4% | 69.1% | 15.3% | 21.2% |
| ITF_WOMEN | 29,555 | 26.4% | 19.0% | 45.3% | {"coverage": 2724, "market_freshness": 1694, "execution": 1304, "data": 1112, "market_freshness/coverage": 678, "mapping": 186, "model_calibration_or_unknown": 92, "model_calibration": 22} | 12.52 | 0.2032 / 0.1939 (5690) | 40.7% | 57.3% | 9.8% | 21.5% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,740 | 6.1% | 5.2% | 1.7% | {"market_freshness": 110, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.7 | 0.2299 / 0.2206 (768) | 29.6% | 2.1% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 57, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 19, "coverage": 14, "mapping": 4} | 9.17 | 0.2066 / 0.1894 (762) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 172 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 572 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9696, "by_level_share_of_ge_25pp": {"ATP": 0.0137, "CHALLENGER": 0.1067, "DOUBLES": 0.0674, "ITF_MEN": 0.3249, "ITF_WOMEN": 0.4529, "OTHER": 0.0007, "WTA": 0.0168, "WTA125": 0.017}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5313, "share_primary_cause_market_settled_or_in_play": 0.4297, "share_primary_cause_stale_quote_only": 0.195}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17250, "identity_ambiguous_share": 0.203, "ticker_orientation": {"VERIFIED": 17250}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11335, "with_external": 607, "coverage": 0.0536, "external_status": {"EXTERNAL_STALE": 389, "AGREES_WITH_KALSHI": 205, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 389, "MODEL_LONE_OUTLIER": 205, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3377, "share_external_supports_model": 0.0214}, "pregame_clean_ge_25pp": {"n": 5392, "with_external": 577, "coverage": 0.107, "external_status": {"EXTERNAL_STALE": 366, "AGREES_WITH_KALSHI": 198, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 366, "MODEL_LONE_OUTLIER": 198, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3432, "share_external_supports_model": 0.0225}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 485.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.209, "data_status": {"POOR": 9709, "LIMITED": 4476, "ADEQUATE": 3065}, "comparison_lt_10pp": {"median_thinner_serve_points": 1719.0, "median_sample_ratio": 1.7, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1393, "model_minus_observed": 0.0561, "kalshi_minus_observed": -0.083, "brier_diff_model_minus_kalshi": -0.0001}, "4-10x": {"n": 956, "model_minus_observed": 0.0874, "kalshi_minus_observed": -0.0574, "brier_diff_model_minus_kalshi": 0.0082}, "<2x": {"n": 3398, "model_minus_observed": 0.1007, "kalshi_minus_observed": -0.0224, "brier_diff_model_minus_kalshi": 0.0146}, ">=10x": {"n": 1176, "model_minus_observed": 0.1178, "kalshi_minus_observed": -0.0554, "brier_diff_model_minus_kalshi": 0.0147}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6923, "model": {"intercept": -0.554, "slope": 0.826, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.189, "slope": 1.075, "slope_se": 0.034}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1696, "model_brier": 0.2328, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0294, "brier_diff_se": 0.0023, "model_logloss": 0.6627, "kalshi_logloss": 0.5893}, "fair_v1": {"n": 6923, "model": {"intercept": -0.446, "slope": 1.031, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.255, "slope": 1.102, "slope_se": 0.034}, "mean_extremity_model": 0.1695, "mean_extremity_kalshi": 0.1693, "model_brier": 0.2144, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0108, "brier_diff_se": 0.0019, "model_logloss": 0.6176, "kalshi_logloss": 0.5895}, "gen1_elo": {"n": 6923, "model": {"intercept": -0.435, "slope": 1.009, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.255, "slope": 1.092, "slope_se": 0.034}, "mean_extremity_model": 0.1761, "mean_extremity_kalshi": 0.1694, "model_brier": 0.2137, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.01, "brier_diff_se": 0.0019, "model_logloss": 0.6165, "kalshi_logloss": 0.5896}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2464, "share_ge_15": 0.4426, "median_abs_gap": 13.01, "n": 45996}, "gen1_elo": {"share_ge_25": 0.2435, "share_ge_15": 0.4387, "median_abs_gap": 12.77, "n": 45996}, "gen1_sr": {"share_ge_25": 0.3126, "share_ge_15": 0.5198, "median_abs_gap": 15.8, "n": 45996}, "gen2": {"share_ge_25": 0.313, "share_ge_15": 0.5092, "median_abs_gap": 15.43, "n": 45996}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1514, "share_ge_15": 0.3539, "median_abs_gap": 10.71, "n": 35597}, "gen1_elo": {"share_ge_25": 0.1494, "share_ge_15": 0.3489, "median_abs_gap": 10.49, "n": 35597}, "gen1_sr": {"share_ge_25": 0.2173, "share_ge_15": 0.4405, "median_abs_gap": 13.01, "n": 35599}, "gen2": {"share_ge_25": 0.2316, "share_ge_15": 0.4392, "median_abs_gap": 12.86, "n": 35599}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.54, "share_ge_25_all": 0.038, "share_ge_25_pregame_clean": 0.0328}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.061, "share_ge_25_pregame_clean": 0.0517}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.237, "share_within_10pp_all": 0.4393, "share_within_10pp_pregame_clean": 0.4915, "corr_model_vs_mid_pregame_clean": 0.8513}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 998, "model_brier": 0.1972, "kalshi_brier": 0.1976, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1201, "model_brier": 0.2188, "kalshi_brier": 0.2094, "brier_diff_model_minus_kalshi": 0.0094}, "15-25": {"n_settled": 1533, "model_brier": 0.2242, "kalshi_brier": 0.208, "brier_diff_model_minus_kalshi": 0.0162}, "25-40": {"n_settled": 881, "model_brier": 0.2215, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0175}, "3-5": {"n_settled": 639, "model_brier": 0.2048, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": 0.0001}, "40+": {"n_settled": 185, "model_brier": 0.2959, "kalshi_brier": 0.1755, "brier_diff_model_minus_kalshi": 0.1204}, "5-10": {"n_settled": 1486, "model_brier": 0.2019, "kalshi_brier": 0.2012, "brier_diff_model_minus_kalshi": 0.0008}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.554, "slope": 0.826, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.189, "slope": 1.075, "slope_se": 0.034}, "n": 6923}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.485, "slope": 0.866, "slope_se": 0.025}, "kalshi_slope": {"intercept": 0.176, "slope": 1.074, "slope_se": 0.029}, "n": 9155}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 612, "model_brier": 0.2991, "kalshi_brier": 0.2341, "brier_diff_model_minus_kalshi": 0.065, "brier_diff_se": 0.0119, "corr_model_outcome": 0.0897, "corr_kalshi_outcome": 0.2687}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
