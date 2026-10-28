# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-28T06:38Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 63,583): 0-3 14.1%, 3-5 9.5%, 5-10 20.0%, 10-15 15.4%, 15-25 19.0%, 25-40 13.9%, 40+ 7.9%; median gap 11.9 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.1%, Challenger 11.5%, doubles 6.5%). Main tour: ATP 4.3% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 13,910): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.1%, STALE_QUOTE 19.0%, BOOK_QUALITY 18.9%, POOR_DATA 9.4%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.1%, market_freshness 19.0%, execution 18.9%, data 12.8%, market_freshness/coverage 8.9%, mapping 4.1%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 13,910 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.1% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.0% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 451.0 points vs 1712.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.019, Gen-2 0.803, Gen-1 ledger 0.858 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 661 model 0.2231 vs Kalshi 0.2085; n 139 model 0.2716 vs Kalshi 0.1961.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 274,056 model-market comparisons (445,503 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 91,984 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-28T06:20:44.336656+00:00'], shadow board 72,658 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-28T06:20:48.428310+00:00'], Model 4 34,928 rows, 22,296 settled tickers, 8,095 tickers with an external scan.
* By model: {"gen1_ledger": 62242, "gen1_elo": 36528, "fair_v1": 36528, "gen2": 36528, "gen1_sr": 36528, "model4_fundamental": 32873, "model4_conditioned": 32829}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 63,583 | 14.1 | 9.5 | 20.0 | 15.4 | 19.0 | 13.9 | 7.9 | 11.9 | 40.9% | 21.9% |
| MW fair_v1 | 36,528 | 13.0 | 8.7 | 18.6 | 15.5 | 19.4 | 15.0 | 9.7 | 13.01 | 44.1% | 24.7% |
| MW gen1_elo | 36,528 | 12.8 | 8.6 | 19.4 | 15.4 | 19.5 | 14.8 | 9.6 | 12.82 | 43.9% | 24.4% |
| MW gen1_ledger | 27,055 | 15.7 | 10.7 | 21.9 | 15.2 | 18.5 | 12.5 | 5.6 | 10.44 | 36.6% | 18.1% |
| MW gen1_sr | 36,528 | 10.2 | 7.2 | 16.8 | 13.6 | 20.8 | 18.7 | 12.7 | 15.94 | 52.2% | 31.4% |
| MW gen2 | 36,528 | 11.1 | 7.5 | 16.3 | 13.9 | 19.5 | 17.9 | 13.8 | 15.51 | 51.2% | 31.7% |
| all families model4_conditioned | 32,829 | 22.1 | 18.2 | 34.5 | 17.4 | 4.8 | 1.9 | 1.1 | 6.04 | 7.8% | 3.0% |
| all families model4_fundamental | 32,873 | 17.1 | 13.2 | 34.1 | 20.4 | 10.2 | 3.6 | 1.4 | 7.74 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.3%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.7%, >=40pp 7.9%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.27pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,272 | 27.0 | 15.7 | 27.3 | 13.7 | 11.6 | 4.2 | 0.6 | 5.93 | 16.4% | 4.8% |
| CHALLENGER | 5,691 | 16.1 | 9.8 | 20.3 | 15.6 | 15.5 | 12.0 | 10.8 | 11.04 | 38.2% | 22.7% |
| ITF_MEN | 9,946 | 10.0 | 7.2 | 16.7 | 15.2 | 21.1 | 17.8 | 12.1 | 15.35 | 51.0% | 29.8% |
| ITF_WOMEN | 14,271 | 9.7 | 7.0 | 16.1 | 15.2 | 22.0 | 18.4 | 11.7 | 15.64 | 52.0% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,342 | 17.4 | 13.8 | 24.7 | 20.3 | 16.6 | 6.7 | 0.6 | 8.34 | 23.8% | 7.2% |
| WTA125 | 1,000 | 15.7 | 7.0 | 23.2 | 19.2 | 20.4 | 12.8 | 1.7 | 10.97 | 34.9% | 14.5% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,272 | 25.5 | 15.6 | 25.2 | 16.7 | 11.9 | 4.2 | 0.8 | 6.28 | 16.9% | 5.0% |
| CHALLENGER | 5,691 | 15.1 | 8.8 | 17.9 | 14.6 | 18.1 | 13.8 | 11.7 | 12.71 | 43.6% | 25.5% |
| ITF_MEN | 9,946 | 8.0 | 6.1 | 14.3 | 13.4 | 19.9 | 21.0 | 17.4 | 18.48 | 58.3% | 38.4% |
| ITF_WOMEN | 14,271 | 8.0 | 5.6 | 14.1 | 12.8 | 20.7 | 21.4 | 17.4 | 19.23 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,342 | 14.7 | 10.7 | 22.1 | 15.7 | 22.5 | 12.9 | 1.5 | 10.79 | 36.9% | 14.4% |
| WTA125 | 1,000 | 8.4 | 6.4 | 16.6 | 17.0 | 24.6 | 17.8 | 9.2 | 15.8 | 51.6% | 27.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,272 | 22.6 | 12.8 | 24.6 | 16.0 | 16.2 | 6.5 | 1.4 | 7.58 | 24.1% | 7.8% |
| CHALLENGER | 5,691 | 14.9 | 9.1 | 21.2 | 15.8 | 15.7 | 12.3 | 11.0 | 11.3 | 39.0% | 23.2% |
| ITF_MEN | 9,946 | 9.5 | 7.1 | 17.0 | 14.2 | 21.7 | 18.2 | 12.2 | 15.8 | 52.2% | 30.5% |
| ITF_WOMEN | 14,271 | 9.4 | 6.8 | 16.5 | 15.9 | 22.1 | 18.1 | 11.1 | 15.43 | 51.3% | 29.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,342 | 23.6 | 16.2 | 31.8 | 15.1 | 9.7 | 2.5 | 1.1 | 6.12 | 13.2% | 3.5% |
| WTA125 | 1,000 | 22.5 | 12.4 | 26.5 | 16.7 | 15.0 | 6.5 | 0.4 | 7.99 | 21.9% | 6.9% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,896 | 24.5 | 19.2 | 30.8 | 12.9 | 9.0 | 3.1 | 0.5 | 5.67 | 12.6% | 3.6% |
| CHALLENGER | 3,885 | 22.5 | 14.4 | 26.9 | 14.6 | 13.9 | 6.1 | 1.6 | 7.16 | 21.6% | 7.7% |
| DOUBLES | 1,932 | 5.1 | 4.5 | 12.3 | 10.6 | 21.0 | 25.3 | 21.2 | 23.62 | 67.5% | 46.5% |
| ITF_MEN | 7,663 | 13.1 | 9.2 | 20.7 | 15.9 | 21.6 | 13.4 | 6.2 | 12.12 | 41.2% | 19.6% |
| ITF_WOMEN | 9,119 | 12.9 | 8.9 | 19.6 | 15.6 | 21.3 | 15.8 | 5.8 | 12.52 | 42.9% | 21.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,396 | 24.4 | 15.3 | 29.9 | 17.8 | 9.5 | 2.9 | 0.3 | 6.76 | 12.6% | 3.1% |
| WTA125 | 1,015 | 24.3 | 12.8 | 20.6 | 19.1 | 13.6 | 7.8 | 1.8 | 8.11 | 23.2% | 9.6% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,183 | 27.3 | 15.8 | 27.7 | 13.6 | 11.4 | 3.8 | 0.4 | 5.9 | 15.6% | 4.2% |
| CHALLENGER | 4,003 | 21.0 | 12.4 | 25.3 | 18.1 | 15.3 | 6.3 | 1.6 | 8.18 | 23.2% | 7.9% |
| ITF_MEN | 7,416 | 12.0 | 8.6 | 19.9 | 17.2 | 22.1 | 14.7 | 5.4 | 12.66 | 42.2% | 20.2% |
| ITF_WOMEN | 10,768 | 11.5 | 8.3 | 18.4 | 17.3 | 23.8 | 15.4 | 5.3 | 13.38 | 44.5% | 20.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,273 | 17.6 | 13.8 | 24.8 | 20.5 | 16.6 | 6.2 | 0.6 | 8.25 | 23.3% | 6.7% |
| WTA125 | 965 | 16.0 | 6.8 | 22.8 | 19.5 | 20.9 | 12.5 | 1.4 | 11.03 | 34.9% | 14.0% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,183 | 25.8 | 16.0 | 25.4 | 16.6 | 11.9 | 3.9 | 0.5 | 6.22 | 16.3% | 4.4% |
| CHALLENGER | 4,003 | 19.5 | 11.2 | 22.5 | 17.1 | 18.4 | 9.4 | 1.9 | 9.14 | 29.8% | 11.3% |
| ITF_MEN | 7,417 | 9.3 | 7.2 | 16.6 | 15.5 | 21.6 | 19.1 | 10.6 | 15.47 | 51.3% | 29.7% |
| ITF_WOMEN | 10,769 | 8.9 | 6.4 | 15.8 | 14.2 | 22.7 | 20.9 | 11.0 | 16.84 | 54.6% | 31.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,273 | 14.7 | 10.7 | 22.2 | 15.7 | 22.6 | 12.8 | 1.3 | 10.77 | 36.6% | 14.1% |
| WTA125 | 965 | 8.4 | 6.4 | 16.7 | 17.3 | 24.5 | 18.1 | 8.6 | 15.65 | 51.2% | 26.7% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,843 | 24.6 | 19.5 | 30.8 | 13.0 | 8.6 | 3.0 | 0.4 | 5.65 | 12.0% | 3.4% |
| CHALLENGER | 3,427 | 23.9 | 15.3 | 28.1 | 14.7 | 13.3 | 4.2 | 0.5 | 6.61 | 17.9% | 4.6% |
| DOUBLES | 1,811 | 5.0 | 4.6 | 12.5 | 10.8 | 20.9 | 25.1 | 21.0 | 23.53 | 67.0% | 46.1% |
| ITF_MEN | 6,555 | 14.0 | 9.7 | 22.3 | 16.5 | 21.6 | 11.9 | 4.0 | 11.2 | 37.5% | 15.9% |
| ITF_WOMEN | 7,741 | 13.7 | 9.3 | 20.9 | 16.4 | 21.5 | 14.7 | 3.6 | 11.67 | 39.8% | 18.3% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,342 | 24.7 | 15.7 | 30.0 | 17.8 | 9.5 | 2.2 | 0.1 | 6.59 | 11.8% | 2.3% |
| WTA125 | 894 | 25.8 | 13.7 | 21.7 | 20.4 | 12.4 | 5.5 | 0.6 | 7.33 | 18.5% | 6.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,932 | 5.1 | 4.5 | 12.3 | 10.6 | 21.0 | 25.3 | 21.2 | 23.62 | 67.5% | 46.5% |
| singles | 25,123 | 16.5 | 11.1 | 22.6 | 15.6 | 18.3 | 11.5 | 4.4 | 9.94 | 34.2% | 15.9% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,575 | 13.0 | 9.4 | 20.0 | 15.6 | 19.1 | 13.9 | 9.2 | 12.44 | 42.1% | 23.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 23,604 | 13.5 | 8.7 | 18.6 | 15.3 | 19.2 | 15.2 | 9.6 | 12.94 | 43.9% | 24.7% |
| UNKNOWN | 5,100 | 10.6 | 7.4 | 17.1 | 16.9 | 20.9 | 16.2 | 11.0 | 14.16 | 48.1% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,343 | 19.8 | 12.3 | 22.2 | 15.9 | 14.8 | 9.2 | 5.8 | 8.71 | 29.8% | 15.0% |
| B | 4,474 | 12.7 | 8.7 | 19.1 | 16.4 | 19.4 | 12.9 | 10.7 | 12.66 | 43.1% | 23.7% |
| C | 5,103 | 12.2 | 8.9 | 19.9 | 15.9 | 18.7 | 14.3 | 10.0 | 12.74 | 43.1% | 24.4% |
| D | 5,648 | 12.3 | 8.1 | 17.6 | 15.6 | 21.1 | 15.9 | 9.4 | 13.69 | 46.4% | 25.3% |
| F | 10,960 | 7.4 | 5.5 | 15.0 | 14.6 | 23.3 | 21.2 | 12.9 | 17.84 | 57.4% | 34.1% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,385 | 24.2 | 15.8 | 28.6 | 15.1 | 11.1 | 3.8 | 1.4 | 6.51 | 16.2% | 5.2% |
| B | 3,705 | 16.7 | 10.1 | 24.3 | 16.6 | 19.1 | 10.0 | 3.3 | 9.78 | 32.4% | 13.3% |
| C | 5,208 | 11.1 | 7.8 | 19.3 | 14.7 | 21.2 | 15.7 | 10.2 | 13.53 | 47.0% | 25.9% |
| D | 3,865 | 14.5 | 9.7 | 21.1 | 15.4 | 20.5 | 13.2 | 5.6 | 11.42 | 39.3% | 18.8% |
| F | 6,892 | 10.0 | 8.2 | 15.7 | 14.9 | 23.1 | 20.3 | 7.8 | 15.62 | 51.2% | 28.1% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 11,734 | 18.1 | 11.1 | 21.3 | 15.7 | 15.3 | 10.1 | 8.5 | 9.89 | 33.8% | 18.6% |
| LIMITED | 7,829 | 13.8 | 10.0 | 20.3 | 16.4 | 19.1 | 13.3 | 7.1 | 11.68 | 39.5% | 20.4% |
| POOR | 16,965 | 9.1 | 6.4 | 16.0 | 15.0 | 22.5 | 19.2 | 11.7 | 16.14 | 53.4% | 30.9% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,157 | 24.3 | 18.4 | 33.3 | 14.8 | 6.3 | 2.6 | 0.4 | 5.79 | 9.3% | 2.9% |
| GAME_SPREAD | 5,626 | 22.2 | 15.3 | 33.1 | 17.1 | 9.0 | 2.8 | 0.6 | 6.73 | 12.4% | 3.3% |
| MATCH_WINNER | 27,055 | 15.7 | 10.7 | 21.9 | 15.2 | 18.5 | 12.5 | 5.6 | 10.44 | 36.6% | 18.1% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,026 | 27.6 | 16.5 | 31.3 | 12.5 | 9.3 | 2.4 | 0.3 | 5.68 | 12.0% | 2.7% |
| TOTAL_GAMES | 9,354 | 9.1 | 10.2 | 36.2 | 27.0 | 10.7 | 4.0 | 2.8 | 9.36 | 17.5% | 6.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,665 | 24.5 | 30.5 | 33.0 | 7.1 | 3.9 | 0.8 | 0.2 | 4.68 | 4.9% | 1.0% |
| GAME_SPREAD | 7,678 | 47.0 | 16.2 | 25.6 | 7.4 | 2.0 | 1.2 | 0.6 | 3.29 | 3.8% | 1.8% |
| TOTAL_GAMES | 13,486 | 5.9 | 8.7 | 40.9 | 32.0 | 7.3 | 3.1 | 2.2 | 9.4 | 12.6% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 11,676 | 23.9 | 16.9 | 34.9 | 14.2 | 7.1 | 2.5 | 0.4 | 6.01 | 10.0% | 2.9% |
| GAME_SPREAD | 7,681 | 19.8 | 13.4 | 28.3 | 20.6 | 12.4 | 4.3 | 1.1 | 7.84 | 17.8% | 5.4% |
| TOTAL_GAMES | 13,516 | 9.6 | 9.9 | 36.7 | 25.5 | 11.7 | 4.2 | 2.4 | 9.25 | 18.3% | 6.7% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 36,528 | 44.1% | 24.7% | 13.01 | 35.7% | 15.6% | 10.82 |
| gen1_elo | 36,528 | 43.9% | 24.4% | 12.82 | 35.4% | 15.6% | 10.58 |
| gen1_sr | 36,528 | 52.2% | 31.4% | 15.94 | 44.6% | 22.2% | 13.06 |
| gen2 | 36,528 | 51.2% | 31.7% | 15.51 | 44.5% | 23.8% | 13.03 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 17,873 | 15.5 | 10.5 | 21.3 | 17.3 | 20.0 | 12.0 | 3.3 | 10.73 | 35.4% | 15.3% |
| STALE | 18,655 | 10.6 | 7.0 | 16.1 | 13.8 | 18.9 | 17.9 | 15.8 | 16.1 | 52.5% | 33.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 20,523 | 16.4 | 11.0 | 22.6 | 15.4 | 17.9 | 12.0 | 4.7 | 9.99 | 34.6% | 16.7% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 63,583 | 20523 | 21345 | 21715 | 24.1 | 114.1 | 1400.4 |
| ge_15pp | 26,017 | 7099 | 7610 | 11308 | 26.2 | 415.9 | 1399.2 |
| ge_25pp | 13,910 | 3427 | 3334 | 7149 | 31.4 | 569.9 | 1380.4 |
| lt_10pp | 27,772 | 10270 | 10088 | 7414 | 22.4 | 47.1 | 1341.5 |

Current slate `SL-20261028T063802Z-8853a2d8`: 802 priced rows, quote age at build {'median': 17.9, 'max': 18.0}, freshness {'AGING': 802}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 41 | 0.0 | 0.0 | 31.7 | 7.3 | 36.6 | 21.9 | 2.4 | 20.19 | 61.0% | 24.4% |
| EXTERNAL_LONE_OUTLIER | 19 | 79.0 | 21.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,589 | 19.8 | 11.2 | 25.1 | 18.3 | 17.7 | 7.2 | 0.7 | 8.68 | 25.6% | 7.9% |
| KALSHI_LONE_OUTLIER | 24 | 4.2 | 4.2 | 75.0 | 8.3 | 4.2 | 4.2 | 0.0 | 6.31 | 8.3% | 4.2% |
| MARKETS_AGREE | 704 | 65.1 | 34.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.25 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,536 | 0.0 | 2.5 | 35.0 | 26.6 | 24.7 | 10.4 | 0.8 | 12.27 | 35.9% | 11.2% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 36,528 | 5913 (16.2%) | 26.0% | 1.1% | {"EXTERNAL_STALE": 3589, "AGREES_WITH_KALSHI": 1536, "ALL_AGREE": 704, "SUPPORTS_MODEL_DIRECTION": 40, "AGREES_WITH_MODEL": 24, "EXTERNAL_OUTLIER": 19, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 16,119 | 1499 (9.3%) | 36.8% | 1.8% | {"EXTERNAL_STALE": 920, "AGREES_WITH_KALSHI": 552, "SUPPORTS_MODEL_DIRECTION": 25, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,021 | 467 (5.2%) | 36.8% | 2.4% | {"EXTERNAL_STALE": 284, "AGREES_WITH_KALSHI": 172, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,458 | 443 (9.9%) | 37.2% | 2.5% | {"EXTERNAL_STALE": 267, "AGREES_WITH_KALSHI": 165, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 14,733 | 3344 (22.7%) | 17.2% | 1.0% | {"EXTERNAL_STALE": 2012, "ALL_AGREE": 704, "AGREES_WITH_KALSHI": 576, "AGREES_WITH_MODEL": 20, "EXTERNAL_OUTLIER": 19, "SUPPORTS_MODEL_DIRECTION": 12, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,086 | 10.5 | 7.3 | 19.5 | 14.7 | 21.5 | 16.6 | 9.8 | 14.09 | 47.9% | 26.4% |
| 4-10x | 4,837 | 11.3 | 8.5 | 18.8 | 15.5 | 21.4 | 14.6 | 9.8 | 13.54 | 45.9% | 24.4% |
| <2x | 18,591 | 15.1 | 10.1 | 19.3 | 16.3 | 17.4 | 13.1 | 8.7 | 11.59 | 39.2% | 21.8% |
| >=10x | 6,014 | 10.7 | 6.3 | 15.3 | 14.2 | 21.6 | 19.4 | 12.5 | 16.38 | 53.5% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,217 | 12.9 | 8.5 | 19.5 | 16.3 | 19.0 | 13.5 | 10.3 | 12.7 | 42.9% | 23.8% |
| 300-1000 | 7,722 | 12.1 | 8.7 | 17.6 | 15.4 | 20.1 | 16.5 | 9.4 | 13.61 | 46.1% | 26.0% |
| <300 | 11,956 | 8.4 | 5.8 | 15.4 | 14.8 | 22.9 | 20.2 | 12.6 | 17.02 | 55.6% | 32.8% |
| >=3000 | 7,633 | 21.3 | 13.6 | 23.7 | 15.9 | 13.8 | 7.2 | 4.6 | 7.63 | 25.6% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1018 | 0.5501 | 0.4116 | 0.5 | +0.050 | -0.088 | -0.0027 ± 0.0048 |
| ratio 4-10x | 696 | 0.5847 | 0.4375 | 0.4957 | +0.089 | -0.058 | 0.0084 ± 0.0061 |
| ratio <2x | 2492 | 0.5372 | 0.4137 | 0.4478 | +0.089 | -0.034 | 0.0112 ± 0.0029 |
| ratio >=10x | 902 | 0.5711 | 0.3944 | 0.4557 | +0.115 | -0.061 | 0.0116 ± 0.0061 |
| thinner_sample 1000-3000 | 1374 | 0.5379 | 0.4106 | 0.452 | +0.086 | -0.041 | 0.0086 ± 0.0039 |
| thinner_sample 300-1000 | 1141 | 0.5688 | 0.4258 | 0.4899 | +0.079 | -0.064 | 0.0018 ± 0.0048 |
| thinner_sample <300 | 1733 | 0.5617 | 0.3934 | 0.4616 | +0.100 | -0.068 | 0.0097 ± 0.0043 |
| thinner_sample >=3000 | 860 | 0.5342 | 0.4401 | 0.4663 | +0.068 | -0.026 | 0.0126 ± 0.0039 |
| data_status ADEQUATE | 1445 | 0.535 | 0.4313 | 0.4498 | +0.085 | -0.018 | 0.0126 ± 0.0032 |
| data_status LIMITED | 1192 | 0.5499 | 0.4159 | 0.4866 | +0.063 | -0.071 | 0.003 ± 0.0044 |
| data_status POOR | 2471 | 0.5635 | 0.4012 | 0.4658 | +0.098 | -0.065 | 0.008 ± 0.0035 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 748 | 0.202 | 0.2026 | -0.0006 ± 0.0006 | 0.5848 | 0.5862 | 0.5025 | 0.4875 | 0.5134 | -0.084 ± 0.0175 | -0.01 (5) |
| 3-5 | 461 | 0.2064 | 0.2067 | -0.0003 ± 0.0017 | 0.5965 | 0.5955 | 0.5039 | 0.4639 | 0.4859 | -0.095 ± 0.0217 | 0.02 (1) |
| 5-10 | 1054 | 0.2029 | 0.2031 | -0.0002 ± 0.0021 | 0.592 | 0.5901 | 0.5123 | 0.4383 | 0.4734 | -0.090 ± 0.0143 | -0.0167 (6) |
| 10-15 | 896 | 0.2214 | 0.212 | +0.0094 ± 0.0038 | 0.6358 | 0.609 | 0.5286 | 0.4047 | 0.4275 | -0.110 ± 0.0155 | -0.048 (5) |
| 15-25 | 1149 | 0.2238 | 0.2119 | +0.0120 ± 0.0053 | 0.6429 | 0.6076 | 0.5761 | 0.3805 | 0.4482 | -0.097 ± 0.0136 | -0.0033 (9) |
| 25-40 | 661 | 0.2231 | 0.2085 | +0.0146 ± 0.0106 | 0.6358 | 0.5996 | 0.6566 | 0.3465 | 0.4766 | -0.074 ± 0.0163 | -0.01 (1) |
| 40+ | 139 | 0.2716 | 0.1961 | +0.0755 ± 0.0324 | 0.7421 | 0.5747 | 0.7425 | 0.2945 | 0.4388 | -0.060 ± 0.0319 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3944 | 0.1848 | 0.1855 | -0.0007 ± 0.0002 | 0.5453 | 0.5459 | 0.4864 | 0.4712 | 0.4959 | -0.030 ± 0.007 | -0.0129 (17) |
| 3-5 | 2658 | 0.1964 | 0.1947 | +0.0018 ± 0.0007 | 0.5727 | 0.5662 | 0.4866 | 0.4468 | 0.4432 | -0.059 ± 0.0087 | 0.0 (2) |
| 5-10 | 5588 | 0.2012 | 0.1973 | +0.0039 ± 0.0009 | 0.5878 | 0.5743 | 0.4854 | 0.4115 | 0.4214 | -0.051 ± 0.006 | -0.0119 (21) |
| 10-15 | 4802 | 0.2029 | 0.1858 | +0.0171 ± 0.0016 | 0.5927 | 0.5463 | 0.4878 | 0.3635 | 0.3563 | -0.071 ± 0.0062 | -0.0281 (16) |
| 15-25 | 5954 | 0.2075 | 0.1689 | +0.0386 ± 0.0021 | 0.608 | 0.5001 | 0.5013 | 0.305 | 0.3057 | -0.072 ± 0.0053 | -0.0025 (44) |
| 25-40 | 4709 | 0.2229 | 0.1263 | +0.0966 ± 0.0032 | 0.6399 | 0.3875 | 0.5284 | 0.2145 | 0.2217 | -0.061 ± 0.005 | -0.01 (1) |
| 40+ | 3055 | 0.3782 | 0.0461 | +0.3321 ± 0.0044 | 0.9847 | 0.1771 | 0.63 | 0.1045 | 0.0642 | -0.075 ± 0.0037 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 590 | 0.2072 | 0.2078 | -0.0006 ± 0.0007 | 0.5962 | 0.5979 | 0.5099 | 0.4946 | 0.5153 | -0.109 ± 0.0204 | -0.01 (3) |
| 3-5 | 413 | 0.2277 | 0.2242 | +0.0035 ± 0.0019 | 0.6424 | 0.6349 | 0.5104 | 0.4707 | 0.4407 | -0.145 ± 0.0249 | 0.02 (1) |
| 5-10 | 915 | 0.2088 | 0.2086 | +0.0003 ± 0.0023 | 0.6042 | 0.6032 | 0.5488 | 0.4738 | 0.5126 | -0.085 ± 0.0156 | -0.01 (4) |
| 10-15 | 833 | 0.2195 | 0.2126 | +0.0068 ± 0.004 | 0.6305 | 0.6125 | 0.5671 | 0.4428 | 0.4802 | -0.108 ± 0.0167 | -0.04 (5) |
| 15-25 | 1197 | 0.2295 | 0.2134 | +0.0161 ± 0.0052 | 0.6532 | 0.6103 | 0.5838 | 0.3886 | 0.4478 | -0.098 ± 0.0136 | -0.0133 (9) |
| 25-40 | 843 | 0.2671 | 0.198 | +0.0692 ± 0.0096 | 0.7462 | 0.5774 | 0.6542 | 0.3399 | 0.3903 | -0.124 ± 0.0153 | -0.0075 (4) |
| 40+ | 317 | 0.3619 | 0.1678 | +0.1941 ± 0.0228 | 0.9913 | 0.5031 | 0.7339 | 0.2476 | 0.306 | -0.079 ± 0.0222 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3366 | 0.192 | 0.1921 | -0.0001 ± 0.0003 | 0.5609 | 0.5609 | 0.511 | 0.496 | 0.5056 | -0.048 ± 0.0078 | -0.0133 (15) |
| 3-5 | 2265 | 0.1984 | 0.1965 | +0.0020 ± 0.0007 | 0.5747 | 0.5697 | 0.5157 | 0.4759 | 0.4702 | -0.060 ± 0.0096 | 0.02 (1) |
| 5-10 | 4983 | 0.199 | 0.196 | +0.0031 ± 0.0009 | 0.584 | 0.5717 | 0.5155 | 0.4414 | 0.461 | -0.041 ± 0.0064 | -0.0117 (6) |
| 10-15 | 4257 | 0.2062 | 0.1939 | +0.0123 ± 0.0017 | 0.6025 | 0.5644 | 0.5152 | 0.3912 | 0.4045 | -0.055 ± 0.0069 | -0.0189 (18) |
| 15-25 | 5971 | 0.2167 | 0.1793 | +0.0374 ± 0.0022 | 0.6303 | 0.5262 | 0.5234 | 0.3279 | 0.3336 | -0.067 ± 0.0055 | -0.0086 (42) |
| 25-40 | 5501 | 0.252 | 0.1376 | +0.1144 ± 0.0032 | 0.71 | 0.4218 | 0.5567 | 0.2403 | 0.2209 | -0.085 ± 0.005 | -0.0044 (18) |
| 40+ | 4367 | 0.3957 | 0.0596 | +0.3361 ± 0.0042 | 1.041 | 0.2144 | 0.6511 | 0.1182 | 0.0829 | -0.072 ± 0.0036 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 723 | 0.1983 | 0.2004 | -0.0020 ± 0.0006 | 0.5764 | 0.5815 | 0.5003 | 0.485 | 0.5436 | -0.039 ± 0.0174 | -0.0137 (8) |
| 3-5 | 499 | 0.203 | 0.2015 | +0.0016 ± 0.0016 | 0.5891 | 0.5834 | 0.5025 | 0.4628 | 0.4649 | -0.119 ± 0.021 | 0.0067 (3) |
| 5-10 | 1086 | 0.2045 | 0.2024 | +0.0021 ± 0.0021 | 0.5956 | 0.5881 | 0.5105 | 0.4365 | 0.4586 | -0.097 ± 0.014 | -0.0071 (7) |
| 10-15 | 892 | 0.2121 | 0.2078 | +0.0043 ± 0.0038 | 0.6144 | 0.6001 | 0.5389 | 0.4157 | 0.4608 | -0.094 ± 0.0154 | -0.0317 (6) |
| 15-25 | 1083 | 0.2316 | 0.2153 | +0.0163 ± 0.0055 | 0.661 | 0.6149 | 0.5884 | 0.3939 | 0.4497 | -0.109 ± 0.0141 | -0.03 (1) |
| 25-40 | 675 | 0.2137 | 0.2156 | -0.0019 ± 0.0104 | 0.6164 | 0.6157 | 0.6655 | 0.355 | 0.5111 | -0.059 ± 0.0162 | 0.015 (2) |
| 40+ | 150 | 0.2889 | 0.2043 | +0.0846 ± 0.0321 | 0.7918 | 0.5929 | 0.7513 | 0.3017 | 0.44 | -0.062 ± 0.0336 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3865 | 0.1849 | 0.1855 | -0.0006 ± 0.0002 | 0.5445 | 0.5456 | 0.4849 | 0.4696 | 0.4869 | -0.035 ± 0.007 | -0.0163 (35) |
| 3-5 | 2604 | 0.2001 | 0.1982 | +0.0019 ± 0.0007 | 0.5832 | 0.5768 | 0.4866 | 0.447 | 0.4443 | -0.061 ± 0.0089 | -0.0094 (18) |
| 5-10 | 5789 | 0.1945 | 0.1899 | +0.0046 ± 0.0009 | 0.5721 | 0.5561 | 0.4868 | 0.4126 | 0.4187 | -0.053 ± 0.0058 | -0.01 (31) |
| 10-15 | 4683 | 0.195 | 0.1807 | +0.0143 ± 0.0015 | 0.5745 | 0.5342 | 0.4976 | 0.3743 | 0.378 | -0.061 ± 0.0062 | -0.015 (12) |
| 15-25 | 6067 | 0.2123 | 0.1723 | +0.0399 ± 0.0021 | 0.6185 | 0.508 | 0.5125 | 0.3175 | 0.3135 | -0.075 ± 0.0053 | -0.03 (2) |
| 25-40 | 4672 | 0.2187 | 0.1291 | +0.0896 ± 0.0033 | 0.6315 | 0.3935 | 0.5318 | 0.216 | 0.2342 | -0.053 ± 0.0051 | 0.01 (3) |
| 40+ | 3030 | 0.3906 | 0.0519 | +0.3386 ± 0.0046 | 1.0198 | 0.1924 | 0.6412 | 0.1123 | 0.0706 | -0.077 ± 0.004 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1114 | 0.196 | 0.1962 | -0.0002 ± 0.0005 | 0.5709 | 0.5711 | 0.5039 | 0.4889 | 0.4955 | -0.065 ± 0.0135 | -0.0224 (49) |
| 3-5 | 764 | 0.1905 | 0.1901 | +0.0004 ± 0.0013 | 0.5575 | 0.5555 | 0.4943 | 0.4546 | 0.4673 | -0.060 ± 0.0161 | -0.0194 (34) |
| 5-10 | 1615 | 0.2026 | 0.1971 | +0.0055 ± 0.0017 | 0.5954 | 0.5774 | 0.4975 | 0.424 | 0.4235 | -0.078 ± 0.0113 | -0.005 (78) |
| 10-15 | 1096 | 0.2148 | 0.203 | +0.0119 ± 0.0034 | 0.6217 | 0.5896 | 0.5311 | 0.4084 | 0.4197 | -0.078 ± 0.0139 | 0.0014 (64) |
| 15-25 | 1425 | 0.2318 | 0.2109 | +0.0209 ± 0.0048 | 0.661 | 0.6065 | 0.5799 | 0.385 | 0.4309 | -0.079 ± 0.0123 | -0.0214 (59) |
| 25-40 | 895 | 0.2434 | 0.2099 | +0.0335 ± 0.0094 | 0.695 | 0.6018 | 0.6792 | 0.3673 | 0.4693 | -0.088 ± 0.0143 | -0.0219 (26) |
| 40+ | 293 | 0.3369 | 0.2006 | +0.1363 ± 0.0254 | 0.9726 | 0.5865 | 0.8083 | 0.3289 | 0.4437 | -0.091 ± 0.0234 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3898 | 0.1785 | 0.1787 | -0.0002 ± 0.0002 | 0.5272 | 0.527 | 0.5054 | 0.4901 | 0.5008 | -0.039 ± 0.0068 | -0.0157 (88) |
| 3-5 | 2663 | 0.1947 | 0.193 | +0.0017 ± 0.0007 | 0.5668 | 0.5631 | 0.5014 | 0.4616 | 0.4608 | -0.052 ± 0.0086 | -0.0209 (69) |
| 5-10 | 5402 | 0.1991 | 0.1913 | +0.0078 ± 0.0009 | 0.5861 | 0.5618 | 0.4954 | 0.4218 | 0.4071 | -0.071 ± 0.006 | -0.0082 (132) |
| 10-15 | 3771 | 0.2118 | 0.1959 | +0.0159 ± 0.0018 | 0.615 | 0.5732 | 0.5311 | 0.4083 | 0.4044 | -0.068 ± 0.0073 | -0.0053 (105) |
| 15-25 | 4616 | 0.2299 | 0.1995 | +0.0303 ± 0.0026 | 0.6619 | 0.5777 | 0.567 | 0.3713 | 0.3925 | -0.066 ± 0.0066 | -0.0253 (107) |
| 25-40 | 3189 | 0.2588 | 0.1855 | +0.0733 ± 0.0048 | 0.7332 | 0.5415 | 0.6325 | 0.3193 | 0.3612 | -0.077 ± 0.0074 | -0.0229 (51) |
| 40+ | 1355 | 0.3719 | 0.1487 | +0.2232 ± 0.0109 | 1.0513 | 0.4471 | 0.7305 | 0.229 | 0.2701 | -0.068 ± 0.0098 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5108 | 1.019 ± 0.039 | 1.089 | 0.1677 | 0.1642 | 0.2155 | 0.2074 |
| gen2 | 5108 | 0.803 ± 0.036 | 1.047 | 0.1689 | 0.1647 | 0.2359 | 0.2073 |
| gen1_elo | 5108 | 0.996 ± 0.038 | 1.088 | 0.1743 | 0.1644 | 0.2142 | 0.2075 |
| gen1_sr | 5108 | 0.977 ± 0.047 | 1.111 | 0.1296 | 0.1666 | 0.2317 | 0.2069 |
| gen1_ledger | 7202 | 0.858 ± 0.028 | 1.057 | 0.1848 | 0.1765 | 0.2185 | 0.2016 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 26,017)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,691 | 21.9% |
| STALE_QUOTE | market_freshness | 5,689 | 21.9% |
| BOOK_QUALITY | execution | 5,046 | 19.4% |
| POOR_DATA | data | 3,072 | 11.8% |
| LIMITED_DATA | data | 1,615 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,420 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,197 | 4.6% |
| IDENTITY_AMBIGUOUS | mapping | 1,076 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 750 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 460 | 1.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 21.9%, market_freshness 21.9%, execution 19.4%, data 18.0%, market_freshness/coverage 8.3%, model_calibration_or_unknown 4.6%, mapping 4.1%, model_calibration 1.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.2%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 60.6%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 43.5%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.4%, WIDE_SPREAD 25.4%, MODEL_HIGH_UNCERTAINTY 17.6%, PLAYER_IDENTITY_RISK 15.9%, LEVEL_TRANSFER_RISK 10.6%, LOW_DISPLAYED_LIQUIDITY 7.9%, EVENT_MAPPING_RISK 7.6%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.4%, POST_SETTLEMENT_OBSERVATION 21.9%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 13,910)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,606 | 33.1% |
| STALE_QUOTE | market_freshness | 2,647 | 19.0% |
| BOOK_QUALITY | execution | 2,633 | 18.9% |
| POOR_DATA | data | 1,308 | 9.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 754 | 5.4% |
| IDENTITY_AMBIGUOUS | mapping | 575 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 483 | 3.5% |
| LIMITED_DATA | data | 480 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 306 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 117 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.1%, market_freshness 19.0%, execution 18.9%, data 12.8%, market_freshness/coverage 8.9%, mapping 4.1%, model_calibration_or_unknown 2.2%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 74.9%, THIN_PLAYER_HISTORY 63.0%, STALE_KALSHI_QUOTE 51.4%, STALE_PLAYER_DATA 46.6%, MODEL_INTERNAL_DISAGREEMENT 42.6%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.9%, PLAYER_IDENTITY_RISK 18.9%, MODEL_HIGH_UNCERTAINTY 18.1%, LEVEL_TRANSFER_RISK 9.4%, EVENT_MAPPING_RISK 9.1%, LOW_DISPLAYED_LIQUIDITY 7.7%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.2%, POST_SETTLEMENT_OBSERVATION 33.1%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 10972, "IDENTITY_AMBIGUOUS": 2938}; ticker orientation: {"VERIFIED": 13910}.

Checks: discipline:AMBIGUOUS 898, discipline:PASS 13012, identity_confidence:AMBIGUOUS 2625, identity_confidence:PASS 11285, level_mapping:NA 910, level_mapping:PASS 13000, market_pair:AMBIGUOUS 472, market_pair:NA 329, market_pair:PASS 13109, model_complement:NA 293, model_complement:PASS 13617, namesake:AMBIGUOUS 6, namesake:PASS 13904, physical_match_id:NA 4889, physical_match_id:PASS 9021, player_ids:PASS 13910, same_pair_other_event:PASS 13910, ticker_orientation:PASS 13910

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,168 | 4.3% | 3.9% | 1.6% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 15, "coverage": 13} | 5.83 | 0.2195 / 0.2156 (587) | 21.2% | 3.0% | 3.3% | 2.8% |
| CHALLENGER | 9,576 | 16.6% | 6.4% | 11.5% | {"coverage": 928, "market_freshness/coverage": 191, "market_freshness": 166, "data": 144, "model_calibration_or_unknown": 75, "execution": 36, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.33 | 0.2198 / 0.2106 (2195) | 34.9% | 16.1% | 4.1% | 22.4% |
| DOUBLES | 1,932 | 46.5% | 46.1% | 6.5% | {"execution": 507, "mapping": 222, "market_freshness": 106, "market_freshness/coverage": 56, "coverage": 7} | 23.53 | 0.309 / 0.2365 (453) | 12.1% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 17,609 | 25.4% | 18.1% | 32.1% | {"coverage": 1533, "execution": 867, "market_freshness": 821, "data": 656, "market_freshness/coverage": 399, "mapping": 184, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.94 | 0.2166 / 0.1996 (3598) | 36.6% | 70.4% | 17.8% | 20.7% |
| ITF_WOMEN | 23,390 | 26.8% | 19.7% | 45.0% | {"coverage": 2094, "market_freshness": 1358, "execution": 1146, "data": 895, "market_freshness/coverage": 523, "mapping": 146, "model_calibration_or_unknown": 81, "model_calibration": 16} | 12.68 | 0.2058 / 0.1978 (4252) | 38.8% | 58.1% | 10.2% | 20.9% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,738 | 5.7% | 5.1% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "execution": 27, "data": 19, "model_calibration": 18, "coverage": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.62 | 0.2341 / 0.2288 (577) | 25.6% | 1.1% | 1.4% | 3.3% |
| WTA125 | 2,015 | 12.0% | 10.2% | 1.7% | {"market_freshness": 62, "model_calibration_or_unknown": 50, "market_freshness/coverage": 41, "data": 38, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.33 | 0.2113 / 0.1945 (606) | 25.2% | 12.0% | 5.3% | 7.7% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 7 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 8 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 9 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 10 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 194 min (STALE); no external reference |
| 11 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 12 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 15 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 16 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 17 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 18 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 19 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 20 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 21 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 22 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 23 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 24 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 25 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 26 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 27 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 28 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 29 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 30 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 31 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 32 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 33 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 34 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 35 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 36 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 37 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 178 min (STALE); no external reference |
| 38 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 39 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 40 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 41 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 379 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 42 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 43 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 45 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 47 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 48 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 49 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 50 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9686, "by_level_share_of_ge_25pp": {"ATP": 0.0162, "CHALLENGER": 0.1145, "DOUBLES": 0.0646, "ITF_MEN": 0.3212, "ITF_WOMEN": 0.45, "OTHER": 0.0009, "WTA": 0.0153, "WTA125": 0.0174}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5139, "share_primary_cause_market_settled_or_in_play": 0.42, "share_primary_cause_stale_quote_only": 0.1903}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 13910, "identity_ambiguous_share": 0.2112, "ticker_orientation": {"VERIFIED": 13910}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9021, "with_external": 467, "coverage": 0.0518, "external_status": {"EXTERNAL_STALE": 284, "AGREES_WITH_KALSHI": 172, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 284, "MODEL_LONE_OUTLIER": 172, "ALL_THREE_DISAGREE": 10, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3683, "share_external_supports_model": 0.0236}, "pregame_clean_ge_25pp": {"n": 4458, "with_external": 443, "coverage": 0.0994, "external_status": {"EXTERNAL_STALE": 267, "AGREES_WITH_KALSHI": 165, "SUPPORTS_MODEL_DIRECTION": 10, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 267, "MODEL_LONE_OUTLIER": 165, "ALL_THREE_DISAGREE": 10, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3725, "share_external_supports_model": 0.0248}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 451.0, "median_sample_ratio": 2.48, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2132, "data_status": {"POOR": 7938, "LIMITED": 3502, "ADEQUATE": 2470}, "comparison_lt_10pp": {"median_thinner_serve_points": 1712.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1018, "model_minus_observed": 0.0501, "kalshi_minus_observed": -0.0884, "brier_diff_model_minus_kalshi": -0.0027}, "4-10x": {"n": 696, "model_minus_observed": 0.089, "kalshi_minus_observed": -0.0582, "brier_diff_model_minus_kalshi": 0.0084}, "<2x": {"n": 2492, "model_minus_observed": 0.0894, "kalshi_minus_observed": -0.0341, "brier_diff_model_minus_kalshi": 0.0112}, ">=10x": {"n": 902, "model_minus_observed": 0.1154, "kalshi_minus_observed": -0.0612, "brier_diff_model_minus_kalshi": 0.0116}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5108, "model": {"intercept": -0.534, "slope": 0.803, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.189, "slope": 1.047, "slope_se": 0.04}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1647, "model_brier": 0.2359, "kalshi_brier": 0.2073, "brier_diff_model_minus_kalshi": 0.0286, "brier_diff_se": 0.0027, "model_logloss": 0.6696, "kalshi_logloss": 0.5979}, "fair_v1": {"n": 5108, "model": {"intercept": -0.412, "slope": 1.019, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.282, "slope": 1.089, "slope_se": 0.04}, "mean_extremity_model": 0.1677, "mean_extremity_kalshi": 0.1642, "model_brier": 0.2155, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.0081, "brier_diff_se": 0.0022, "model_logloss": 0.6202, "kalshi_logloss": 0.5981}, "gen1_elo": {"n": 5108, "model": {"intercept": -0.385, "slope": 0.996, "slope_se": 0.038}, "kalshi_mid_same_rows": {"intercept": 0.306, "slope": 1.088, "slope_se": 0.04}, "mean_extremity_model": 0.1743, "mean_extremity_kalshi": 0.1644, "model_brier": 0.2142, "kalshi_brier": 0.2075, "brier_diff_model_minus_kalshi": 0.0067, "brier_diff_se": 0.0022, "model_logloss": 0.6179, "kalshi_logloss": 0.5983}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.247, "share_ge_15": 0.4413, "median_abs_gap": 13.01, "n": 36528}, "gen1_elo": {"share_ge_25": 0.2443, "share_ge_15": 0.4393, "median_abs_gap": 12.82, "n": 36528}, "gen1_sr": {"share_ge_25": 0.3136, "share_ge_15": 0.5219, "median_abs_gap": 15.94, "n": 36528}, "gen2": {"share_ge_25": 0.3172, "share_ge_15": 0.512, "median_abs_gap": 15.51, "n": 36528}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1558, "share_ge_15": 0.3572, "median_abs_gap": 10.82, "n": 28614}, "gen1_elo": {"share_ge_25": 0.1555, "share_ge_15": 0.3542, "median_abs_gap": 10.58, "n": 28612}, "gen1_sr": {"share_ge_25": 0.2222, "share_ge_15": 0.4457, "median_abs_gap": 13.06, "n": 28615}, "gen2": {"share_ge_25": 0.2381, "share_ge_15": 0.4448, "median_abs_gap": 13.03, "n": 28616}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.83, "share_ge_25_all": 0.0435, "share_ge_25_pregame_clean": 0.0392}, "WTA": {"median_abs_gap_pregame_clean": 7.62, "share_ge_25_all": 0.057, "share_ge_25_pregame_clean": 0.0509}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2366, "share_within_10pp_all": 0.4368, "share_within_10pp_pregame_clean": 0.4875, "corr_model_vs_mid_pregame_clean": 0.8474}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 748, "model_brier": 0.202, "kalshi_brier": 0.2026, "brier_diff_model_minus_kalshi": -0.0006}, "10-15": {"n_settled": 896, "model_brier": 0.2214, "kalshi_brier": 0.212, "brier_diff_model_minus_kalshi": 0.0094}, "15-25": {"n_settled": 1149, "model_brier": 0.2238, "kalshi_brier": 0.2119, "brier_diff_model_minus_kalshi": 0.012}, "25-40": {"n_settled": 661, "model_brier": 0.2231, "kalshi_brier": 0.2085, "brier_diff_model_minus_kalshi": 0.0146}, "3-5": {"n_settled": 461, "model_brier": 0.2064, "kalshi_brier": 0.2067, "brier_diff_model_minus_kalshi": -0.0003}, "40+": {"n_settled": 139, "model_brier": 0.2716, "kalshi_brier": 0.1961, "brier_diff_model_minus_kalshi": 0.0755}, "5-10": {"n_settled": 1054, "model_brier": 0.2029, "kalshi_brier": 0.2031, "brier_diff_model_minus_kalshi": -0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.534, "slope": 0.803, "slope_se": 0.036}, "kalshi_slope": {"intercept": 0.189, "slope": 1.047, "slope_se": 0.04}, "n": 5108}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.49, "slope": 0.858, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.164, "slope": 1.057, "slope_se": 0.032}, "n": 7202}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 453, "model_brier": 0.309, "kalshi_brier": 0.2365, "brier_diff_model_minus_kalshi": 0.0725, "brier_diff_se": 0.0142, "corr_model_outcome": 0.0482, "corr_kalshi_outcome": 0.2475}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
