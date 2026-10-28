# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-28T05:16Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 62,943): 0-3 14.1%, 3-5 9.6%, 5-10 19.9%, 10-15 15.4%, 15-25 19.1%, 25-40 14.0%, 40+ 8.0%; median gap 11.93 pp.
* **Where the extremes live**: 96.8% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.0%, Challenger 11.5%, doubles 6.5%). Main tour: ATP 4.4% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 13,806): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.3%, BOOK_QUALITY 19.0%, STALE_QUOTE 18.8%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.9%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.3%, execution 19.0%, market_freshness 18.8%, data 12.8%, market_freshness/coverage 8.9%, mapping 4.2%, model_calibration_or_unknown 2.2%, model_calibration 0.9%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 13,806 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.0% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 454.0 points vs 1726.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.025, Gen-2 0.807, Gen-1 ledger 0.86 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 656 model 0.2223 vs Kalshi 0.2085; n 138 model 0.2708 vs Kalshi 0.1972.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 271,945 model-market comparisons (441,747 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 91,228 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-28T04:59:39.932867+00:00'], shadow board 71,988 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-28T04:59:43.937840+00:00'], Model 4 34,756 rows, 22,263 settled tickers, 8,062 tickers with an external scan.
* By model: {"gen1_ledger": 61805, "gen1_elo": 36193, "fair_v1": 36193, "gen2": 36193, "gen1_sr": 36193, "model4_fundamental": 32706, "model4_conditioned": 32662}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 62,943 | 14.1 | 9.6 | 19.9 | 15.4 | 19.1 | 14.0 | 8.0 | 11.93 | 41.0% | 21.9% |
| MW fair_v1 | 36,193 | 12.9 | 8.7 | 18.6 | 15.5 | 19.5 | 15.0 | 9.7 | 13.04 | 44.2% | 24.7% |
| MW gen1_elo | 36,193 | 12.8 | 8.5 | 19.4 | 15.4 | 19.5 | 14.8 | 9.6 | 12.85 | 44.0% | 24.5% |
| MW gen1_ledger | 26,750 | 15.6 | 10.7 | 21.8 | 15.2 | 18.5 | 12.5 | 5.6 | 10.45 | 36.7% | 18.1% |
| MW gen1_sr | 36,193 | 10.2 | 7.1 | 16.8 | 13.6 | 20.8 | 18.7 | 12.7 | 15.96 | 52.2% | 31.4% |
| MW gen2 | 36,193 | 11.1 | 7.5 | 16.3 | 13.9 | 19.5 | 18.0 | 13.8 | 15.55 | 51.3% | 31.8% |
| all families model4_conditioned | 32,662 | 22.1 | 18.2 | 34.5 | 17.4 | 4.9 | 1.9 | 1.1 | 6.05 | 7.8% | 3.0% |
| all families model4_fundamental | 32,706 | 17.0 | 13.2 | 34.1 | 20.4 | 10.2 | 3.6 | 1.4 | 7.75 | 15.3% | 5.0% |

Configurable thresholds (primary): >=5pp 76.4%, >=10pp 56.4%, >=15pp 41.0%, >=20pp 30.4%, >=25pp 21.9%, >=30pp 15.8%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.3pp; >=10pp 44.8%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,258 | 26.9 | 15.7 | 27.3 | 13.8 | 11.6 | 4.2 | 0.6 | 5.93 | 16.4% | 4.8% |
| CHALLENGER | 5,671 | 16.1 | 9.8 | 20.2 | 15.6 | 15.5 | 12.0 | 10.8 | 11.09 | 38.3% | 22.8% |
| ITF_MEN | 9,808 | 10.0 | 7.2 | 16.5 | 15.1 | 21.3 | 17.8 | 12.1 | 15.46 | 51.2% | 29.9% |
| ITF_WOMEN | 14,132 | 9.7 | 7.0 | 16.0 | 15.2 | 22.0 | 18.4 | 11.8 | 15.65 | 52.2% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,328 | 17.3 | 13.8 | 24.7 | 20.3 | 16.6 | 6.7 | 0.6 | 8.38 | 23.8% | 7.2% |
| WTA125 | 990 | 15.4 | 7.1 | 23.1 | 19.4 | 20.6 | 12.6 | 1.7 | 11.02 | 34.9% | 14.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,258 | 25.5 | 15.6 | 25.3 | 16.7 | 11.9 | 4.2 | 0.8 | 6.3 | 16.9% | 5.0% |
| CHALLENGER | 5,671 | 15.1 | 8.8 | 17.9 | 14.6 | 18.1 | 13.9 | 11.7 | 12.75 | 43.6% | 25.6% |
| ITF_MEN | 9,808 | 7.9 | 6.1 | 14.2 | 13.2 | 19.9 | 21.1 | 17.6 | 18.63 | 58.6% | 38.7% |
| ITF_WOMEN | 14,132 | 8.0 | 5.6 | 14.1 | 12.8 | 20.6 | 21.4 | 17.5 | 19.3 | 59.6% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,328 | 14.6 | 10.7 | 22.1 | 15.7 | 22.5 | 12.9 | 1.5 | 10.82 | 36.9% | 14.4% |
| WTA125 | 990 | 8.2 | 6.3 | 16.8 | 17.0 | 24.9 | 17.9 | 9.1 | 15.89 | 51.8% | 27.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,258 | 22.6 | 12.7 | 24.7 | 16.0 | 16.2 | 6.5 | 1.4 | 7.58 | 24.0% | 7.9% |
| CHALLENGER | 5,671 | 14.8 | 9.1 | 21.2 | 15.9 | 15.7 | 12.3 | 11.0 | 11.34 | 39.0% | 23.3% |
| ITF_MEN | 9,808 | 9.5 | 7.1 | 16.9 | 14.1 | 21.9 | 18.2 | 12.3 | 15.97 | 52.4% | 30.5% |
| ITF_WOMEN | 14,132 | 9.4 | 6.8 | 16.5 | 15.9 | 22.2 | 18.1 | 11.1 | 15.47 | 51.4% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,328 | 23.7 | 16.2 | 31.8 | 15.0 | 9.7 | 2.5 | 1.1 | 6.12 | 13.2% | 3.5% |
| WTA125 | 990 | 22.4 | 12.3 | 26.7 | 16.7 | 15.1 | 6.5 | 0.4 | 7.99 | 21.9% | 6.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,890 | 24.6 | 19.1 | 30.8 | 12.9 | 9.0 | 3.1 | 0.5 | 5.7 | 12.7% | 3.6% |
| CHALLENGER | 3,873 | 22.4 | 14.4 | 26.9 | 14.6 | 13.9 | 6.2 | 1.6 | 7.17 | 21.6% | 7.7% |
| DOUBLES | 1,915 | 5.1 | 4.6 | 12.2 | 10.6 | 21.0 | 25.3 | 21.4 | 23.62 | 67.6% | 46.6% |
| ITF_MEN | 7,534 | 13.0 | 9.2 | 20.5 | 15.9 | 21.8 | 13.5 | 6.2 | 12.16 | 41.4% | 19.7% |
| ITF_WOMEN | 8,996 | 12.9 | 8.9 | 19.6 | 15.6 | 21.3 | 15.9 | 5.8 | 12.55 | 43.0% | 21.7% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,388 | 24.3 | 15.3 | 30.0 | 17.7 | 9.5 | 2.9 | 0.3 | 6.76 | 12.7% | 3.2% |
| WTA125 | 1,005 | 24.1 | 12.9 | 20.7 | 19.0 | 13.6 | 7.9 | 1.8 | 8.11 | 23.3% | 9.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,169 | 27.3 | 15.8 | 27.6 | 13.7 | 11.4 | 3.9 | 0.4 | 5.9 | 15.6% | 4.2% |
| CHALLENGER | 3,985 | 21.0 | 12.4 | 25.2 | 18.2 | 15.4 | 6.3 | 1.6 | 8.23 | 23.3% | 7.9% |
| ITF_MEN | 7,285 | 12.0 | 8.6 | 19.8 | 17.1 | 22.3 | 14.7 | 5.4 | 12.75 | 42.5% | 20.1% |
| ITF_WOMEN | 10,642 | 11.4 | 8.3 | 18.3 | 17.3 | 23.9 | 15.4 | 5.3 | 13.43 | 44.6% | 20.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,259 | 17.5 | 13.8 | 24.8 | 20.5 | 16.6 | 6.2 | 0.6 | 8.25 | 23.4% | 6.7% |
| WTA125 | 955 | 15.7 | 6.9 | 22.7 | 19.7 | 21.1 | 12.4 | 1.5 | 11.03 | 35.0% | 13.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,169 | 25.7 | 15.9 | 25.4 | 16.7 | 11.9 | 3.9 | 0.5 | 6.22 | 16.3% | 4.4% |
| CHALLENGER | 3,985 | 19.4 | 11.1 | 22.4 | 17.2 | 18.4 | 9.5 | 1.9 | 9.17 | 29.8% | 11.4% |
| ITF_MEN | 7,286 | 9.3 | 7.2 | 16.5 | 15.3 | 21.7 | 19.3 | 10.7 | 15.55 | 51.7% | 29.9% |
| ITF_WOMEN | 10,643 | 9.0 | 6.4 | 15.7 | 14.2 | 22.7 | 20.9 | 11.0 | 16.84 | 54.6% | 32.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,259 | 14.7 | 10.7 | 22.2 | 15.8 | 22.6 | 12.8 | 1.3 | 10.78 | 36.7% | 14.1% |
| WTA125 | 955 | 8.2 | 6.3 | 16.9 | 17.3 | 24.7 | 18.2 | 8.5 | 15.68 | 51.4% | 26.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,837 | 24.7 | 19.4 | 30.8 | 13.0 | 8.7 | 3.0 | 0.4 | 5.66 | 12.1% | 3.4% |
| CHALLENGER | 3,415 | 23.9 | 15.3 | 28.1 | 14.7 | 13.3 | 4.2 | 0.5 | 6.61 | 18.0% | 4.7% |
| DOUBLES | 1,795 | 5.0 | 4.7 | 12.4 | 10.7 | 20.9 | 25.2 | 21.1 | 23.54 | 67.2% | 46.3% |
| ITF_MEN | 6,426 | 14.0 | 9.7 | 22.1 | 16.6 | 21.7 | 12.0 | 4.0 | 11.25 | 37.6% | 15.9% |
| ITF_WOMEN | 7,619 | 13.6 | 9.3 | 20.9 | 16.3 | 21.4 | 14.8 | 3.6 | 11.69 | 39.8% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,334 | 24.7 | 15.7 | 30.0 | 17.8 | 9.5 | 2.2 | 0.1 | 6.59 | 11.8% | 2.3% |
| WTA125 | 884 | 25.6 | 13.8 | 21.8 | 20.2 | 12.4 | 5.5 | 0.6 | 7.33 | 18.6% | 6.1% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,915 | 5.1 | 4.6 | 12.2 | 10.6 | 21.0 | 25.3 | 21.4 | 23.62 | 67.6% | 46.6% |
| singles | 24,835 | 16.4 | 11.2 | 22.6 | 15.6 | 18.3 | 11.6 | 4.4 | 9.95 | 34.3% | 16.0% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,548 | 12.9 | 9.4 | 19.9 | 15.7 | 19.1 | 13.9 | 9.2 | 12.48 | 42.1% | 23.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 23,346 | 13.5 | 8.8 | 18.4 | 15.2 | 19.3 | 15.2 | 9.6 | 12.98 | 44.0% | 24.8% |
| UNKNOWN | 5,050 | 10.6 | 7.3 | 17.0 | 16.8 | 21.1 | 16.1 | 11.1 | 14.23 | 48.3% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,290 | 19.8 | 12.3 | 22.1 | 16.0 | 14.8 | 9.2 | 5.8 | 8.73 | 29.8% | 15.0% |
| B | 4,440 | 12.7 | 8.7 | 19.0 | 16.4 | 19.5 | 13.0 | 10.8 | 12.71 | 43.3% | 23.8% |
| C | 5,041 | 12.0 | 8.9 | 19.8 | 15.9 | 18.9 | 14.4 | 10.0 | 12.81 | 43.3% | 24.4% |
| D | 5,573 | 12.3 | 8.0 | 17.5 | 15.5 | 21.2 | 15.9 | 9.5 | 13.76 | 46.6% | 25.4% |
| F | 10,849 | 7.4 | 5.5 | 15.0 | 14.6 | 23.4 | 21.2 | 12.9 | 17.91 | 57.5% | 34.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,353 | 24.2 | 15.8 | 28.7 | 15.1 | 11.1 | 3.8 | 1.4 | 6.51 | 16.3% | 5.2% |
| B | 3,658 | 16.7 | 10.1 | 24.3 | 16.5 | 19.2 | 10.0 | 3.3 | 9.79 | 32.5% | 13.3% |
| C | 5,142 | 11.0 | 7.8 | 19.2 | 14.7 | 21.2 | 15.8 | 10.3 | 13.68 | 47.3% | 26.1% |
| D | 3,802 | 14.4 | 9.8 | 20.8 | 15.4 | 20.5 | 13.4 | 5.7 | 11.48 | 39.5% | 19.0% |
| F | 6,795 | 9.9 | 8.2 | 15.6 | 14.9 | 23.1 | 20.4 | 7.8 | 15.69 | 51.3% | 28.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,681 | 18.0 | 11.1 | 21.2 | 15.8 | 15.3 | 10.1 | 8.5 | 9.92 | 33.9% | 18.6% |
| LIMITED | 7,734 | 13.8 | 10.0 | 20.2 | 16.4 | 19.2 | 13.3 | 7.2 | 11.77 | 39.6% | 20.4% |
| POOR | 16,778 | 9.1 | 6.4 | 16.0 | 15.0 | 22.6 | 19.3 | 11.7 | 16.2 | 53.6% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,133 | 24.3 | 18.4 | 33.3 | 14.7 | 6.3 | 2.6 | 0.4 | 5.79 | 9.3% | 3.0% |
| GAME_SPREAD | 5,610 | 22.2 | 15.3 | 33.1 | 17.0 | 9.0 | 2.8 | 0.5 | 6.73 | 12.4% | 3.3% |
| MATCH_WINNER | 26,750 | 15.6 | 10.7 | 21.8 | 15.2 | 18.5 | 12.5 | 5.6 | 10.45 | 36.7% | 18.1% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 12,976 | 27.7 | 16.5 | 31.3 | 12.5 | 9.3 | 2.4 | 0.3 | 5.68 | 12.0% | 2.7% |
| TOTAL_GAMES | 9,312 | 9.2 | 10.2 | 36.2 | 27.0 | 10.7 | 4.0 | 2.8 | 9.36 | 17.5% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,613 | 24.5 | 30.5 | 33.0 | 7.1 | 3.9 | 0.8 | 0.2 | 4.68 | 4.9% | 1.0% |
| GAME_SPREAD | 7,640 | 46.9 | 16.3 | 25.7 | 7.4 | 2.0 | 1.2 | 0.6 | 3.3 | 3.8% | 1.8% |
| TOTAL_GAMES | 13,409 | 5.8 | 8.6 | 40.9 | 32.0 | 7.3 | 3.1 | 2.2 | 9.41 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,624 | 23.8 | 16.9 | 35.0 | 14.3 | 7.2 | 2.5 | 0.4 | 6.02 | 10.0% | 2.9% |
| GAME_SPREAD | 7,643 | 19.8 | 13.4 | 28.3 | 20.6 | 12.4 | 4.3 | 1.1 | 7.84 | 17.8% | 5.4% |
| TOTAL_GAMES | 13,439 | 9.5 | 9.9 | 36.6 | 25.6 | 11.7 | 4.2 | 2.4 | 9.26 | 18.4% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 36,193 | 44.2% | 24.7% | 13.04 | 35.8% | 15.6% | 10.83 |
| gen1_elo | 36,193 | 44.0% | 24.5% | 12.85 | 35.5% | 15.5% | 10.6 |
| gen1_sr | 36,193 | 52.2% | 31.4% | 15.96 | 44.6% | 22.2% | 13.06 |
| gen2 | 36,193 | 51.3% | 31.8% | 15.55 | 44.5% | 23.8% | 13.05 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 17,873 | 15.5 | 10.5 | 21.3 | 17.3 | 20.0 | 12.0 | 3.3 | 10.73 | 35.4% | 15.3% |
| STALE | 18,320 | 10.4 | 7.0 | 15.9 | 13.8 | 19.0 | 17.9 | 15.9 | 16.3 | 52.9% | 33.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 20,218 | 16.4 | 11.0 | 22.5 | 15.4 | 17.9 | 12.0 | 4.8 | 10.0 | 34.7% | 16.8% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 62,943 | 20218 | 21345 | 21380 | 24.1 | 115.8 | 1400.4 |
| ge_15pp | 25,817 | 7007 | 7610 | 11200 | 26.1 | 419.5 | 1399.2 |
| ge_25pp | 13,806 | 3391 | 3334 | 7081 | 31.1 | 571.9 | 1380.4 |
| lt_10pp | 27,432 | 10106 | 10088 | 7238 | 22.4 | 46.7 | 1341.5 |

Current slate `SL-20261028T051635Z-55fb071e`: 820 priced rows, quote age at build {'median': 17.5, 'max': 17.6}, freshness {'AGING': 820}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 40 | 0.0 | 0.0 | 30.0 | 7.5 | 37.5 | 22.5 | 2.5 | 20.33 | 62.5% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 19 | 79.0 | 21.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,559 | 19.8 | 11.2 | 25.0 | 18.3 | 17.8 | 7.2 | 0.7 | 8.68 | 25.7% | 8.0% |
| KALSHI_LONE_OUTLIER | 24 | 4.2 | 4.2 | 75.0 | 8.3 | 4.2 | 4.2 | 0.0 | 6.31 | 8.3% | 4.2% |
| MARKETS_AGREE | 696 | 65.2 | 34.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,523 | 0.0 | 2.5 | 35.0 | 26.5 | 24.8 | 10.4 | 0.8 | 12.28 | 36.0% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 36,193 | 5861 (16.2%) | 26.0% | 1.1% | {"EXTERNAL_STALE": 3559, "AGREES_WITH_KALSHI": 1523, "ALL_AGREE": 696, "SUPPORTS_MODEL_DIRECTION": 39, "AGREES_WITH_MODEL": 24, "EXTERNAL_OUTLIER": 19, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 16,011 | 1490 (9.3%) | 36.8% | 1.8% | {"EXTERNAL_STALE": 915, "AGREES_WITH_KALSHI": 548, "SUPPORTS_MODEL_DIRECTION": 25, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 8,953 | 464 (5.2%) | 36.6% | 2.4% | {"EXTERNAL_STALE": 283, "AGREES_WITH_KALSHI": 170, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,405 | 440 (10.0%) | 37.0% | 2.5% | {"EXTERNAL_STALE": 266, "AGREES_WITH_KALSHI": 163, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 14,557 | 3312 (22.8%) | 17.2% | 0.9% | {"EXTERNAL_STALE": 1994, "ALL_AGREE": 696, "AGREES_WITH_KALSHI": 571, "AGREES_WITH_MODEL": 20, "EXTERNAL_OUTLIER": 19, "SUPPORTS_MODEL_DIRECTION": 11, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,007 | 10.4 | 7.4 | 19.4 | 14.7 | 21.7 | 16.5 | 9.8 | 14.1 | 48.0% | 26.4% |
| 4-10x | 4,780 | 11.2 | 8.5 | 18.8 | 15.5 | 21.6 | 14.7 | 9.8 | 13.63 | 46.1% | 24.5% |
| <2x | 18,446 | 15.1 | 10.1 | 19.2 | 16.3 | 17.4 | 13.1 | 8.7 | 11.63 | 39.3% | 21.9% |
| >=10x | 5,960 | 10.6 | 6.3 | 15.2 | 14.2 | 21.8 | 19.4 | 12.5 | 16.43 | 53.7% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,133 | 12.9 | 8.5 | 19.3 | 16.3 | 19.1 | 13.5 | 10.4 | 12.78 | 43.0% | 23.9% |
| 300-1000 | 7,628 | 12.0 | 8.7 | 17.6 | 15.4 | 20.3 | 16.6 | 9.5 | 13.68 | 46.4% | 26.1% |
| <300 | 11,839 | 8.3 | 5.7 | 15.3 | 14.8 | 22.9 | 20.2 | 12.6 | 17.06 | 55.8% | 32.8% |
| >=3000 | 7,593 | 21.2 | 13.6 | 23.7 | 15.9 | 13.8 | 7.2 | 4.6 | 7.64 | 25.6% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1015 | 0.5497 | 0.4117 | 0.5005 | +0.049 | -0.089 | -0.0026 ± 0.0048 |
| ratio 4-10x | 693 | 0.5857 | 0.4382 | 0.4964 | +0.089 | -0.058 | 0.0087 ± 0.0061 |
| ratio <2x | 2488 | 0.5372 | 0.4139 | 0.4482 | +0.089 | -0.034 | 0.0109 ± 0.0029 |
| ratio >=10x | 899 | 0.5709 | 0.3945 | 0.4561 | +0.115 | -0.062 | 0.0115 ± 0.0061 |
| thinner_sample 1000-3000 | 1372 | 0.5379 | 0.4108 | 0.4519 | +0.086 | -0.041 | 0.0085 ± 0.0039 |
| thinner_sample 300-1000 | 1136 | 0.5688 | 0.4263 | 0.4921 | +0.077 | -0.066 | 0.001 ± 0.0048 |
| thinner_sample <300 | 1728 | 0.5616 | 0.3934 | 0.4618 | +0.100 | -0.068 | 0.0099 ± 0.0043 |
| thinner_sample >=3000 | 859 | 0.5345 | 0.4403 | 0.4657 | +0.069 | -0.025 | 0.0127 ± 0.0039 |
| data_status ADEQUATE | 1444 | 0.5351 | 0.4315 | 0.4494 | +0.086 | -0.018 | 0.0127 ± 0.0032 |
| data_status LIMITED | 1188 | 0.5495 | 0.4158 | 0.4882 | +0.061 | -0.072 | 0.0022 ± 0.0044 |
| data_status POOR | 2463 | 0.5636 | 0.4015 | 0.4661 | +0.098 | -0.065 | 0.0081 ± 0.0035 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 747 | 0.2018 | 0.2024 | -0.0006 ± 0.0006 | 0.5843 | 0.5857 | 0.5023 | 0.4873 | 0.5141 | -0.083 ± 0.0175 | -0.01 (5) |
| 3-5 | 460 | 0.2053 | 0.2057 | -0.0005 ± 0.0017 | 0.5937 | 0.5933 | 0.5032 | 0.4632 | 0.487 | -0.093 ± 0.0217 | 0.02 (1) |
| 5-10 | 1052 | 0.2028 | 0.203 | -0.0001 ± 0.0021 | 0.5919 | 0.5898 | 0.5127 | 0.4388 | 0.4734 | -0.090 ± 0.0144 | -0.0167 (6) |
| 10-15 | 894 | 0.2207 | 0.2112 | +0.0095 ± 0.0038 | 0.6342 | 0.6066 | 0.5289 | 0.405 | 0.4273 | -0.110 ± 0.0155 | -0.048 (5) |
| 15-25 | 1148 | 0.2239 | 0.2118 | +0.0121 ± 0.0053 | 0.6432 | 0.6075 | 0.576 | 0.3804 | 0.4477 | -0.097 ± 0.0136 | -0.0033 (9) |
| 25-40 | 656 | 0.2223 | 0.2085 | +0.0138 ± 0.0106 | 0.6339 | 0.5997 | 0.657 | 0.3471 | 0.4787 | -0.073 ± 0.0164 | -0.01 (1) |
| 40+ | 138 | 0.2708 | 0.1972 | +0.0736 ± 0.0326 | 0.7406 | 0.5773 | 0.7435 | 0.2953 | 0.442 | -0.058 ± 0.0321 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3943 | 0.1847 | 0.1854 | -0.0007 ± 0.0002 | 0.5452 | 0.5458 | 0.4864 | 0.4712 | 0.4961 | -0.030 ± 0.007 | -0.0129 (17) |
| 3-5 | 2653 | 0.1957 | 0.194 | +0.0017 ± 0.0007 | 0.5708 | 0.5646 | 0.486 | 0.4462 | 0.4436 | -0.058 ± 0.0087 | 0.0 (2) |
| 5-10 | 5573 | 0.2006 | 0.1964 | +0.0042 ± 0.0009 | 0.5865 | 0.5724 | 0.4858 | 0.4119 | 0.4204 | -0.053 ± 0.006 | -0.0119 (21) |
| 10-15 | 4787 | 0.2025 | 0.1853 | +0.0172 ± 0.0016 | 0.5919 | 0.545 | 0.4881 | 0.3638 | 0.3562 | -0.071 ± 0.0062 | -0.0281 (16) |
| 15-25 | 5945 | 0.2075 | 0.1689 | +0.0386 ± 0.0021 | 0.608 | 0.5001 | 0.5013 | 0.305 | 0.3056 | -0.072 ± 0.0053 | -0.0025 (44) |
| 25-40 | 4672 | 0.2221 | 0.1259 | +0.0962 ± 0.0032 | 0.6382 | 0.3865 | 0.528 | 0.2143 | 0.2222 | -0.060 ± 0.005 | -0.01 (1) |
| 40+ | 3039 | 0.3781 | 0.0463 | +0.3318 ± 0.0044 | 0.9843 | 0.1775 | 0.63 | 0.1045 | 0.0645 | -0.075 ± 0.0037 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 588 | 0.2074 | 0.208 | -0.0007 ± 0.0007 | 0.5967 | 0.5985 | 0.5104 | 0.4952 | 0.517 | -0.108 ± 0.0204 | -0.01 (3) |
| 3-5 | 412 | 0.2275 | 0.2241 | +0.0034 ± 0.0019 | 0.642 | 0.6347 | 0.5103 | 0.4706 | 0.4417 | -0.143 ± 0.0249 | 0.02 (1) |
| 5-10 | 913 | 0.208 | 0.2077 | +0.0003 ± 0.0023 | 0.6022 | 0.6013 | 0.5487 | 0.4737 | 0.5126 | -0.085 ± 0.0156 | -0.01 (4) |
| 10-15 | 832 | 0.2197 | 0.2128 | +0.0069 ± 0.004 | 0.6311 | 0.6129 | 0.5668 | 0.4425 | 0.4796 | -0.109 ± 0.0167 | -0.04 (5) |
| 15-25 | 1194 | 0.2292 | 0.2123 | +0.0169 ± 0.0052 | 0.6524 | 0.6074 | 0.5843 | 0.3891 | 0.4464 | -0.101 ± 0.0136 | -0.0133 (9) |
| 25-40 | 840 | 0.2667 | 0.1983 | +0.0684 ± 0.0097 | 0.7451 | 0.5782 | 0.6544 | 0.3401 | 0.3917 | -0.123 ± 0.0153 | -0.0075 (4) |
| 40+ | 316 | 0.3613 | 0.1681 | +0.1932 ± 0.0229 | 0.9902 | 0.5038 | 0.7339 | 0.2476 | 0.307 | -0.078 ± 0.0222 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3361 | 0.1921 | 0.1922 | -0.0001 ± 0.0003 | 0.5612 | 0.5612 | 0.5108 | 0.4958 | 0.5058 | -0.048 ± 0.0078 | -0.0133 (15) |
| 3-5 | 2256 | 0.1982 | 0.1964 | +0.0019 ± 0.0007 | 0.5742 | 0.5695 | 0.5159 | 0.4762 | 0.4721 | -0.058 ± 0.0095 | 0.02 (1) |
| 5-10 | 4964 | 0.1985 | 0.1953 | +0.0032 ± 0.0009 | 0.5827 | 0.5701 | 0.5153 | 0.4412 | 0.4601 | -0.041 ± 0.0064 | -0.0117 (6) |
| 10-15 | 4252 | 0.2063 | 0.194 | +0.0123 ± 0.0017 | 0.6027 | 0.5648 | 0.5153 | 0.3914 | 0.4048 | -0.055 ± 0.0069 | -0.0189 (18) |
| 15-25 | 5955 | 0.2163 | 0.1783 | +0.0380 ± 0.0022 | 0.6296 | 0.5237 | 0.5238 | 0.3282 | 0.3323 | -0.069 ± 0.0055 | -0.0086 (42) |
| 25-40 | 5471 | 0.2515 | 0.1375 | +0.1140 ± 0.0032 | 0.7088 | 0.4215 | 0.5566 | 0.2402 | 0.2213 | -0.085 ± 0.005 | -0.0044 (18) |
| 40+ | 4353 | 0.3954 | 0.0597 | +0.3356 ± 0.0042 | 1.0401 | 0.2146 | 0.651 | 0.1182 | 0.0832 | -0.072 ± 0.0036 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 722 | 0.1981 | 0.2001 | -0.0021 ± 0.0006 | 0.5758 | 0.581 | 0.5001 | 0.4848 | 0.5443 | -0.038 ± 0.0174 | -0.0137 (8) |
| 3-5 | 498 | 0.202 | 0.2006 | +0.0014 ± 0.0016 | 0.5865 | 0.5813 | 0.5018 | 0.4621 | 0.4659 | -0.118 ± 0.021 | 0.0067 (3) |
| 5-10 | 1085 | 0.204 | 0.2018 | +0.0022 ± 0.0021 | 0.5943 | 0.5862 | 0.5109 | 0.4368 | 0.4581 | -0.098 ± 0.014 | -0.0071 (7) |
| 10-15 | 889 | 0.2118 | 0.2076 | +0.0043 ± 0.0038 | 0.6139 | 0.5996 | 0.5393 | 0.4161 | 0.4612 | -0.094 ± 0.0154 | -0.0317 (6) |
| 15-25 | 1081 | 0.2315 | 0.2152 | +0.0163 ± 0.0055 | 0.6608 | 0.6148 | 0.5882 | 0.3937 | 0.4496 | -0.109 ± 0.0141 | -0.03 (1) |
| 25-40 | 673 | 0.2134 | 0.2161 | -0.0027 ± 0.0105 | 0.6159 | 0.6169 | 0.6659 | 0.3555 | 0.5126 | -0.058 ± 0.0162 | 0.015 (2) |
| 40+ | 147 | 0.2881 | 0.2036 | +0.0845 ± 0.0324 | 0.7905 | 0.591 | 0.7536 | 0.3037 | 0.4422 | -0.064 ± 0.0339 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3861 | 0.1845 | 0.1851 | -0.0006 ± 0.0002 | 0.5435 | 0.5445 | 0.485 | 0.4697 | 0.4869 | -0.035 ± 0.007 | -0.0163 (35) |
| 3-5 | 2597 | 0.1989 | 0.1971 | +0.0018 ± 0.0007 | 0.5803 | 0.5742 | 0.486 | 0.4464 | 0.4447 | -0.060 ± 0.0089 | -0.0094 (18) |
| 5-10 | 5780 | 0.1941 | 0.1893 | +0.0048 ± 0.0009 | 0.5712 | 0.5547 | 0.487 | 0.4129 | 0.4178 | -0.054 ± 0.0058 | -0.01 (31) |
| 10-15 | 4667 | 0.1948 | 0.1805 | +0.0143 ± 0.0015 | 0.5741 | 0.5338 | 0.4981 | 0.3747 | 0.3782 | -0.061 ± 0.0062 | -0.015 (12) |
| 15-25 | 6055 | 0.212 | 0.1722 | +0.0398 ± 0.0021 | 0.618 | 0.5078 | 0.5123 | 0.3173 | 0.3136 | -0.075 ± 0.0053 | -0.03 (2) |
| 25-40 | 4652 | 0.2185 | 0.1293 | +0.0891 ± 0.0033 | 0.6309 | 0.3939 | 0.5318 | 0.2161 | 0.235 | -0.052 ± 0.0051 | 0.01 (3) |
| 40+ | 3000 | 0.3907 | 0.0512 | +0.3395 ± 0.0046 | 1.0202 | 0.1905 | 0.6412 | 0.112 | 0.0697 | -0.078 ± 0.0039 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1114 | 0.196 | 0.1962 | -0.0002 ± 0.0005 | 0.5709 | 0.5711 | 0.5039 | 0.4889 | 0.4955 | -0.065 ± 0.0135 | -0.0224 (49) |
| 3-5 | 763 | 0.1905 | 0.19 | +0.0004 ± 0.0013 | 0.5574 | 0.5554 | 0.4943 | 0.4545 | 0.4666 | -0.060 ± 0.0162 | -0.0194 (34) |
| 5-10 | 1612 | 0.2022 | 0.1967 | +0.0055 ± 0.0017 | 0.5944 | 0.5761 | 0.4974 | 0.4238 | 0.4231 | -0.078 ± 0.0113 | -0.005 (78) |
| 10-15 | 1094 | 0.2143 | 0.2025 | +0.0118 ± 0.0034 | 0.6202 | 0.5886 | 0.5307 | 0.408 | 0.4196 | -0.078 ± 0.0139 | 0.0014 (64) |
| 15-25 | 1421 | 0.2316 | 0.2109 | +0.0208 ± 0.0048 | 0.6606 | 0.6064 | 0.5801 | 0.3853 | 0.4314 | -0.079 ± 0.0123 | -0.0214 (59) |
| 25-40 | 891 | 0.2435 | 0.2097 | +0.0338 ± 0.0094 | 0.6955 | 0.6013 | 0.6793 | 0.3677 | 0.4691 | -0.089 ± 0.0144 | -0.0219 (26) |
| 40+ | 292 | 0.338 | 0.2 | +0.1379 ± 0.0255 | 0.9754 | 0.5853 | 0.8081 | 0.3286 | 0.4418 | -0.092 ± 0.0235 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3890 | 0.1785 | 0.1787 | -0.0002 ± 0.0002 | 0.5273 | 0.5271 | 0.505 | 0.4898 | 0.4997 | -0.040 ± 0.0068 | -0.0157 (88) |
| 3-5 | 2651 | 0.1943 | 0.1925 | +0.0018 ± 0.0007 | 0.5658 | 0.5616 | 0.5012 | 0.4614 | 0.4583 | -0.054 ± 0.0086 | -0.0209 (69) |
| 5-10 | 5394 | 0.1985 | 0.1907 | +0.0078 ± 0.0009 | 0.5847 | 0.5605 | 0.4952 | 0.4216 | 0.4071 | -0.071 ± 0.006 | -0.0082 (132) |
| 10-15 | 3763 | 0.2112 | 0.1954 | +0.0158 ± 0.0018 | 0.6133 | 0.572 | 0.5306 | 0.4078 | 0.4042 | -0.068 ± 0.0073 | -0.0053 (105) |
| 15-25 | 4588 | 0.2293 | 0.1993 | +0.0300 ± 0.0026 | 0.6608 | 0.5772 | 0.5674 | 0.3718 | 0.3932 | -0.066 ± 0.0066 | -0.0253 (107) |
| 25-40 | 3167 | 0.2592 | 0.1851 | +0.0740 ± 0.0048 | 0.7342 | 0.5405 | 0.6327 | 0.3198 | 0.3606 | -0.079 ± 0.0075 | -0.0229 (51) |
| 40+ | 1348 | 0.3736 | 0.1476 | +0.2260 ± 0.0109 | 1.0556 | 0.4448 | 0.7302 | 0.2286 | 0.2671 | -0.070 ± 0.0099 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5095 | 1.025 ± 0.039 | 1.096 | 0.1677 | 0.1641 | 0.2151 | 0.2071 |
| gen2 | 5095 | 0.807 ± 0.036 | 1.054 | 0.1689 | 0.1645 | 0.2356 | 0.207 |
| gen1_elo | 5095 | 1.002 ± 0.038 | 1.096 | 0.1743 | 0.1642 | 0.2138 | 0.2072 |
| gen1_sr | 5095 | 0.984 ± 0.047 | 1.12 | 0.1295 | 0.1664 | 0.2315 | 0.2066 |
| gen1_ledger | 7187 | 0.86 ± 0.028 | 1.062 | 0.1847 | 0.1765 | 0.2183 | 0.2014 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 25,817)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,674 | 22.0% |
| STALE_QUOTE | market_freshness | 5,602 | 21.7% |
| BOOK_QUALITY | execution | 5,020 | 19.4% |
| POOR_DATA | data | 3,032 | 11.7% |
| LIMITED_DATA | data | 1,603 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,420 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,192 | 4.6% |
| IDENTITY_AMBIGUOUS | mapping | 1,069 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 744 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 460 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.0%, market_freshness 21.7%, execution 19.4%, data 17.9%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.6%, mapping 4.1%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 71.4%, THIN_PLAYER_HISTORY 60.5%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 43.4%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.4%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 16.0%, LEVEL_TRANSFER_RISK 10.5%, LOW_DISPLAYED_LIQUIDITY 7.9%, EVENT_MAPPING_RISK 7.6%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.5%, POST_SETTLEMENT_OBSERVATION 22.0%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 13,806)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,592 | 33.3% |
| BOOK_QUALITY | execution | 2,623 | 19.0% |
| STALE_QUOTE | market_freshness | 2,594 | 18.8% |
| POOR_DATA | data | 1,290 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 754 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 574 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 480 | 3.5% |
| LIMITED_DATA | data | 477 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 304 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 117 | 0.9% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.3%, execution 19.0%, market_freshness 18.8%, data 12.8%, market_freshness/coverage 8.9%, mapping 4.2%, model_calibration_or_unknown 2.2%, model_calibration 0.9%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.8%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 63.0%, STALE_KALSHI_QUOTE 51.3%, STALE_PLAYER_DATA 46.5%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.9%, PLAYER_IDENTITY_RISK 18.9%, MODEL_HIGH_UNCERTAINTY 18.1%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 9.1%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.4%, POST_SETTLEMENT_OBSERVATION 33.3%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 10882, "IDENTITY_AMBIGUOUS": 2924}; ticker orientation: {"VERIFIED": 13806}.

Checks: discipline:AMBIGUOUS 893, discipline:PASS 12913, identity_confidence:AMBIGUOUS 2612, identity_confidence:PASS 11194, level_mapping:NA 905, level_mapping:PASS 12901, market_pair:AMBIGUOUS 470, market_pair:NA 329, market_pair:PASS 13007, model_complement:NA 293, model_complement:PASS 13513, namesake:AMBIGUOUS 6, namesake:PASS 13800, physical_match_id:NA 4853, physical_match_id:PASS 8953, player_ids:PASS 13806, same_pair_other_event:PASS 13806, ticker_orientation:PASS 13806

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,148 | 4.4% | 3.9% | 1.6% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 15, "coverage": 13} | 5.84 | 0.2195 / 0.2156 (587) | 21.0% | 3.0% | 3.3% | 2.8% |
| CHALLENGER | 9,544 | 16.7% | 6.4% | 11.5% | {"coverage": 927, "market_freshness/coverage": 191, "market_freshness": 166, "data": 144, "model_calibration_or_unknown": 75, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.34 | 0.2193 / 0.21 (2193) | 34.8% | 16.1% | 4.2% | 22.5% |
| DOUBLES | 1,915 | 46.6% | 46.3% | 6.5% | {"execution": 503, "mapping": 222, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.54 | 0.31 / 0.2362 (451) | 12.2% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 17,342 | 25.5% | 18.2% | 32.0% | {"coverage": 1528, "execution": 863, "market_freshness": 794, "data": 643, "market_freshness/coverage": 399, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 2} | 12.01 | 0.2164 / 0.1997 (3588) | 36.4% | 70.3% | 18.0% | 20.9% |
| ITF_WOMEN | 23,128 | 26.9% | 19.8% | 45.0% | {"coverage": 2086, "market_freshness": 1336, "execution": 1144, "data": 887, "market_freshness/coverage": 521, "mapping": 146, "model_calibration_or_unknown": 79, "model_calibration": 16} | 12.71 | 0.2053 / 0.1974 (4240) | 38.7% | 58.1% | 10.2% | 21.0% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,716 | 5.7% | 5.1% | 1.5% | {"market_freshness": 75, "model_calibration_or_unknown": 43, "execution": 27, "data": 19, "model_calibration": 18, "coverage": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.63 | 0.2336 / 0.2276 (575) | 25.3% | 1.1% | 1.4% | 3.3% |
| WTA125 | 1,995 | 12.0% | 10.1% | 1.7% | {"market_freshness": 59, "model_calibration_or_unknown": 50, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.38 | 0.2113 / 0.1945 (606) | 25.0% | 12.0% | 5.4% | 7.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 7 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 8 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 9 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 10 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 11 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 12 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 15 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 16 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 17 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 18 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 19 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 20 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 21 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 22 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 23 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 24 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 25 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 26 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 27 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 28 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 29 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 30 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 31 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 32 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 33 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 34 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 35 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 36 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 37 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 38 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 39 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 40 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 41 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 42 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 44 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 46 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 47 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 37 min before settlement (in-play print); quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 48 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 49 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9684, "by_level_share_of_ge_25pp": {"ATP": 0.0163, "CHALLENGER": 0.1153, "DOUBLES": 0.0647, "ITF_MEN": 0.32, "ITF_WOMEN": 0.4502, "OTHER": 0.0009, "WTA": 0.0154, "WTA125": 0.0173}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5129, "share_primary_cause_market_settled_or_in_play": 0.422, "share_primary_cause_stale_quote_only": 0.1879}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 13806, "identity_ambiguous_share": 0.2118, "ticker_orientation": {"VERIFIED": 13806}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 8953, "with_external": 464, "coverage": 0.0518, "external_status": {"EXTERNAL_STALE": 283, "AGREES_WITH_KALSHI": 170, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 283, "MODEL_LONE_OUTLIER": 170, "ALL_THREE_DISAGREE": 10, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3664, "share_external_supports_model": 0.0237}, "pregame_clean_ge_25pp": {"n": 4405, "with_external": 440, "coverage": 0.0999, "external_status": {"EXTERNAL_STALE": 266, "AGREES_WITH_KALSHI": 163, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 266, "MODEL_LONE_OUTLIER": 163, "ALL_THREE_DISAGREE": 10, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3705, "share_external_supports_model": 0.025}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 454.0, "median_sample_ratio": 2.48, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.213, "data_status": {"POOR": 7869, "LIMITED": 3475, "ADEQUATE": 2462}, "comparison_lt_10pp": {"median_thinner_serve_points": 1726.0, "median_sample_ratio": 1.7, "median_min_matches": 91.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1015, "model_minus_observed": 0.0492, "kalshi_minus_observed": -0.0888, "brier_diff_model_minus_kalshi": -0.0026}, "4-10x": {"n": 693, "model_minus_observed": 0.0893, "kalshi_minus_observed": -0.0582, "brier_diff_model_minus_kalshi": 0.0087}, "<2x": {"n": 2488, "model_minus_observed": 0.089, "kalshi_minus_observed": -0.0343, "brier_diff_model_minus_kalshi": 0.0109}, ">=10x": {"n": 899, "model_minus_observed": 0.1149, "kalshi_minus_observed": -0.0616, "brier_diff_model_minus_kalshi": 0.0115}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5095, "model": {"intercept": -0.536, "slope": 0.807, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.191, "slope": 1.054, "slope_se": 0.04}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1645, "model_brier": 0.2356, "kalshi_brier": 0.207, "brier_diff_model_minus_kalshi": 0.0286, "brier_diff_se": 0.0027, "model_logloss": 0.6689, "kalshi_logloss": 0.5971}, "fair_v1": {"n": 5095, "model": {"intercept": -0.412, "slope": 1.025, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.096, "slope_se": 0.04}, "mean_extremity_model": 0.1677, "mean_extremity_kalshi": 0.1641, "model_brier": 0.2151, "kalshi_brier": 0.2071, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.0022, "model_logloss": 0.6194, "kalshi_logloss": 0.5974}, "gen1_elo": {"n": 5095, "model": {"intercept": -0.384, "slope": 1.002, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.309, "slope": 1.096, "slope_se": 0.04}, "mean_extremity_model": 0.1743, "mean_extremity_kalshi": 0.1642, "model_brier": 0.2138, "kalshi_brier": 0.2072, "brier_diff_model_minus_kalshi": 0.0066, "brier_diff_se": 0.0022, "model_logloss": 0.617, "kalshi_logloss": 0.5976}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2474, "share_ge_15": 0.4424, "median_abs_gap": 13.04, "n": 36193}, "gen1_elo": {"share_ge_25": 0.2446, "share_ge_15": 0.44, "median_abs_gap": 12.85, "n": 36193}, "gen1_sr": {"share_ge_25": 0.3143, "share_ge_15": 0.5224, "median_abs_gap": 15.96, "n": 36193}, "gen2": {"share_ge_25": 0.3181, "share_ge_15": 0.5131, "median_abs_gap": 15.55, "n": 36193}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1556, "share_ge_15": 0.3581, "median_abs_gap": 10.83, "n": 28301}, "gen1_elo": {"share_ge_25": 0.1553, "share_ge_15": 0.3546, "median_abs_gap": 10.6, "n": 28299}, "gen1_sr": {"share_ge_25": 0.2224, "share_ge_15": 0.4459, "median_abs_gap": 13.06, "n": 28302}, "gen2": {"share_ge_25": 0.2385, "share_ge_15": 0.4455, "median_abs_gap": 13.05, "n": 28303}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.84, "share_ge_25_all": 0.0437, "share_ge_25_pregame_clean": 0.0394}, "WTA": {"median_abs_gap_pregame_clean": 7.63, "share_ge_25_all": 0.0571, "share_ge_25_pregame_clean": 0.0509}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2363, "share_within_10pp_all": 0.4358, "share_within_10pp_pregame_clean": 0.4868, "corr_model_vs_mid_pregame_clean": 0.8468}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 747, "model_brier": 0.2018, "kalshi_brier": 0.2024, "brier_diff_model_minus_kalshi": -0.0006}, "10-15": {"n_settled": 894, "model_brier": 0.2207, "kalshi_brier": 0.2112, "brier_diff_model_minus_kalshi": 0.0095}, "15-25": {"n_settled": 1148, "model_brier": 0.2239, "kalshi_brier": 0.2118, "brier_diff_model_minus_kalshi": 0.0121}, "25-40": {"n_settled": 656, "model_brier": 0.2223, "kalshi_brier": 0.2085, "brier_diff_model_minus_kalshi": 0.0138}, "3-5": {"n_settled": 460, "model_brier": 0.2053, "kalshi_brier": 0.2057, "brier_diff_model_minus_kalshi": -0.0005}, "40+": {"n_settled": 138, "model_brier": 0.2708, "kalshi_brier": 0.1972, "brier_diff_model_minus_kalshi": 0.0736}, "5-10": {"n_settled": 1052, "model_brier": 0.2028, "kalshi_brier": 0.203, "brier_diff_model_minus_kalshi": -0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.536, "slope": 0.807, "slope_se": 0.036}, "kalshi_slope": {"intercept": 0.191, "slope": 1.054, "slope_se": 0.04}, "n": 5095}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.491, "slope": 0.86, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.165, "slope": 1.062, "slope_se": 0.033}, "n": 7187}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 451, "model_brier": 0.31, "kalshi_brier": 0.2362, "brier_diff_model_minus_kalshi": 0.0739, "brier_diff_se": 0.0142, "corr_model_outcome": 0.0472, "corr_kalshi_outcome": 0.2484}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
