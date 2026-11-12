# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-12T12:04Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 90,236): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.7%, 40+ 8.3%; median gap 11.92 pp.
* **Where the extremes live**: 97.3% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.3%, Challenger 11.1%, doubles 6.4%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 19,897): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.1%, STALE_QUOTE 20.3%, BOOK_QUALITY 16.3%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.1%, market_freshness 20.3%, execution 16.3%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 19,897 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.8% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 476.0 points vs 1668.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.024, Gen-2 0.821, Gen-1 ledger 0.868 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1018 model 0.2248 vs Kalshi 0.2043; n 212 model 0.3052 vs Kalshi 0.1675.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA. Not implemented here.

## 1. Observations

* 375,470 model-market comparisons (620,968 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 123,670 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-12T11:41:33.409019+00:00'], shadow board 104,478 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-12T11:41:37.801181+00:00'], Model 4 44,105 rows, 31,085 settled tickers, 11,744 tickers with an external scan.
* By model: {"gen1_ledger": 82736, "gen1_elo": 52502, "fair_v1": 52502, "gen2": 52502, "gen1_sr": 52502, "model4_fundamental": 41405, "model4_conditioned": 41321}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 90,236 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.7 | 8.3 | 11.92 | 41.2% | 22.1% |
| MW fair_v1 | 52,502 | 12.6 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.3 | 13.18 | 44.9% | 25.3% |
| MW gen1_elo | 52,502 | 12.4 | 8.8 | 19.1 | 15.3 | 19.4 | 15.0 | 10.1 | 13.0 | 44.5% | 25.1% |
| MW gen1_ledger | 37,734 | 15.8 | 10.8 | 22.2 | 15.1 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 52,502 | 9.9 | 7.1 | 16.6 | 13.9 | 20.9 | 18.8 | 12.8 | 15.98 | 52.5% | 31.6% |
| MW gen2 | 52,502 | 10.8 | 7.5 | 16.6 | 13.7 | 19.7 | 17.7 | 13.9 | 15.51 | 51.3% | 31.6% |
| all families model4_conditioned | 41,321 | 22.2 | 17.9 | 34.6 | 16.9 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 41,405 | 17.3 | 13.5 | 34.0 | 20.0 | 9.9 | 3.8 | 1.5 | 7.61 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.4%, >=15pp 41.2%, >=20pp 30.4%, >=25pp 22.1%, >=30pp 16.0%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.56pp; >=10pp 45.6%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,116 | 28.0 | 15.8 | 28.0 | 13.3 | 10.7 | 3.5 | 0.6 | 5.81 | 14.9% | 4.2% |
| CHALLENGER | 8,264 | 16.4 | 9.6 | 20.6 | 15.3 | 15.7 | 11.4 | 11.1 | 10.93 | 38.2% | 22.5% |
| ITF_MEN | 15,361 | 9.6 | 7.3 | 17.1 | 14.9 | 21.1 | 17.2 | 12.8 | 15.45 | 51.2% | 30.0% |
| ITF_WOMEN | 20,330 | 9.4 | 7.1 | 16.1 | 14.7 | 22.1 | 18.7 | 12.0 | 16.0 | 52.8% | 30.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,098 | 16.6 | 13.3 | 25.0 | 20.7 | 16.6 | 6.7 | 1.1 | 8.62 | 24.4% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,116 | 26.3 | 15.7 | 26.3 | 15.8 | 11.3 | 3.9 | 0.8 | 6.09 | 16.0% | 4.7% |
| CHALLENGER | 8,264 | 14.4 | 9.1 | 19.0 | 13.9 | 18.4 | 13.7 | 11.6 | 12.52 | 43.6% | 25.2% |
| ITF_MEN | 15,361 | 8.1 | 6.2 | 15.2 | 13.9 | 20.4 | 19.9 | 16.4 | 17.85 | 56.7% | 36.3% |
| ITF_WOMEN | 20,330 | 7.8 | 5.9 | 14.1 | 12.7 | 20.7 | 21.2 | 17.6 | 19.11 | 59.5% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,098 | 14.1 | 10.4 | 21.6 | 16.2 | 22.5 | 12.8 | 2.5 | 11.2 | 37.7% | 15.2% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,116 | 23.4 | 14.1 | 25.6 | 15.5 | 14.3 | 6.0 | 1.1 | 7.04 | 21.4% | 7.1% |
| CHALLENGER | 8,264 | 15.1 | 9.6 | 20.8 | 15.6 | 16.1 | 11.9 | 10.9 | 11.2 | 39.0% | 22.9% |
| ITF_MEN | 15,361 | 9.3 | 7.3 | 17.2 | 14.2 | 21.5 | 17.4 | 13.2 | 15.77 | 52.0% | 30.5% |
| ITF_WOMEN | 20,330 | 9.2 | 6.8 | 16.3 | 15.6 | 22.1 | 18.6 | 11.3 | 15.71 | 52.1% | 30.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,098 | 22.5 | 17.2 | 31.8 | 15.3 | 8.9 | 3.3 | 1.0 | 6.12 | 13.2% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,487 | 28.1 | 19.5 | 29.1 | 12.1 | 8.1 | 2.5 | 0.4 | 5.24 | 11.1% | 3.0% |
| CHALLENGER | 5,002 | 22.9 | 14.5 | 27.9 | 14.8 | 13.0 | 5.4 | 1.5 | 7.02 | 20.0% | 6.9% |
| DOUBLES | 2,764 | 4.8 | 4.5 | 12.9 | 11.0 | 20.7 | 24.5 | 21.6 | 23.12 | 66.8% | 46.1% |
| ITF_MEN | 11,146 | 12.8 | 9.5 | 21.4 | 15.6 | 21.7 | 12.9 | 6.0 | 11.81 | 40.6% | 19.0% |
| ITF_WOMEN | 13,109 | 13.5 | 9.3 | 19.8 | 15.7 | 21.6 | 14.6 | 5.4 | 12.19 | 41.6% | 20.0% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,821 | 24.0 | 16.0 | 31.6 | 16.8 | 8.9 | 2.5 | 0.2 | 6.52 | 11.6% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,987 | 28.4 | 16.1 | 28.5 | 13.2 | 10.5 | 3.1 | 0.3 | 5.64 | 13.8% | 3.4% |
| CHALLENGER | 5,815 | 21.1 | 11.9 | 25.8 | 18.0 | 15.8 | 5.6 | 1.8 | 8.22 | 23.2% | 7.4% |
| ITF_MEN | 11,171 | 11.8 | 8.7 | 20.6 | 17.2 | 22.2 | 14.0 | 5.5 | 12.47 | 41.7% | 19.5% |
| ITF_WOMEN | 14,839 | 11.3 | 8.6 | 19.1 | 17.0 | 24.0 | 15.3 | 4.6 | 13.14 | 44.0% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,984 | 16.9 | 13.3 | 25.3 | 21.1 | 16.6 | 6.2 | 0.6 | 8.45 | 23.4% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,987 | 26.7 | 16.0 | 26.6 | 15.7 | 11.2 | 3.4 | 0.4 | 6.02 | 15.0% | 3.8% |
| CHALLENGER | 5,815 | 18.2 | 11.6 | 23.8 | 16.4 | 18.9 | 9.0 | 2.1 | 9.0 | 30.0% | 11.1% |
| ITF_MEN | 11,173 | 9.6 | 7.3 | 17.7 | 16.1 | 22.3 | 18.0 | 9.0 | 14.76 | 49.3% | 27.1% |
| ITF_WOMEN | 14,840 | 8.9 | 7.0 | 16.0 | 14.2 | 22.6 | 20.6 | 10.7 | 16.52 | 53.8% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,984 | 14.4 | 10.5 | 21.9 | 16.4 | 22.6 | 12.4 | 1.9 | 11.03 | 36.9% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,417 | 28.4 | 19.7 | 29.2 | 12.3 | 7.8 | 2.3 | 0.3 | 5.21 | 10.4% | 2.6% |
| CHALLENGER | 4,428 | 24.1 | 15.4 | 29.0 | 15.0 | 12.3 | 3.8 | 0.4 | 6.58 | 16.5% | 4.2% |
| DOUBLES | 2,591 | 4.7 | 4.5 | 13.2 | 11.0 | 20.6 | 24.4 | 21.6 | 23.04 | 66.6% | 46.0% |
| ITF_MEN | 9,632 | 13.6 | 10.0 | 22.9 | 16.2 | 21.7 | 11.4 | 4.1 | 10.95 | 37.3% | 15.6% |
| ITF_WOMEN | 11,293 | 14.1 | 9.9 | 20.9 | 16.2 | 21.8 | 13.5 | 3.6 | 11.42 | 38.9% | 17.1% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,758 | 24.4 | 16.4 | 31.6 | 16.8 | 8.9 | 2.0 | 0.1 | 6.42 | 10.9% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,764 | 4.8 | 4.5 | 12.9 | 11.0 | 20.7 | 24.5 | 21.6 | 23.12 | 66.8% | 46.1% |
| singles | 34,970 | 16.6 | 11.3 | 22.9 | 15.5 | 18.4 | 10.9 | 4.3 | 9.76 | 33.7% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,293 | 12.7 | 9.0 | 19.4 | 15.1 | 19.6 | 14.4 | 9.9 | 12.94 | 43.9% | 24.3% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 34,184 | 13.0 | 8.7 | 18.9 | 15.0 | 19.2 | 15.0 | 10.3 | 13.0 | 44.5% | 25.3% |
| UNKNOWN | 6,612 | 10.4 | 7.5 | 17.1 | 16.5 | 21.5 | 15.8 | 11.1 | 14.32 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,608 | 19.1 | 11.8 | 22.4 | 15.8 | 14.8 | 9.5 | 6.5 | 9.01 | 30.8% | 16.0% |
| B | 6,271 | 13.0 | 8.6 | 19.6 | 15.3 | 19.7 | 12.4 | 11.4 | 12.74 | 43.6% | 23.9% |
| C | 7,429 | 12.0 | 8.6 | 19.5 | 16.1 | 19.0 | 14.6 | 10.4 | 12.91 | 43.9% | 24.9% |
| D | 8,627 | 11.3 | 8.4 | 17.8 | 15.1 | 21.8 | 15.7 | 9.8 | 14.07 | 47.4% | 25.6% |
| F | 15,567 | 7.3 | 5.7 | 15.0 | 14.3 | 23.1 | 21.1 | 13.6 | 18.05 | 57.8% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,899 | 24.9 | 15.9 | 28.9 | 14.9 | 10.6 | 3.4 | 1.2 | 6.36 | 15.3% | 4.7% |
| B | 5,129 | 16.7 | 11.0 | 24.2 | 16.9 | 18.9 | 9.3 | 3.0 | 9.6 | 31.2% | 12.3% |
| C | 7,428 | 11.1 | 7.8 | 19.6 | 14.9 | 21.0 | 15.5 | 10.1 | 13.46 | 46.7% | 25.6% |
| D | 5,758 | 14.5 | 10.0 | 21.1 | 15.4 | 21.0 | 12.7 | 5.4 | 11.34 | 39.1% | 18.1% |
| F | 9,520 | 10.2 | 8.4 | 16.7 | 14.4 | 23.4 | 18.9 | 8.0 | 15.13 | 50.3% | 26.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,558 | 17.6 | 10.9 | 21.4 | 15.5 | 15.1 | 10.2 | 9.2 | 10.01 | 34.6% | 19.4% |
| LIMITED | 11,353 | 13.5 | 9.4 | 20.5 | 16.0 | 19.7 | 13.3 | 7.6 | 11.91 | 40.5% | 20.9% |
| POOR | 24,591 | 8.8 | 6.7 | 16.1 | 14.6 | 22.5 | 19.1 | 12.3 | 16.37 | 53.9% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,298 | 23.8 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,948 | 22.8 | 15.3 | 32.0 | 16.8 | 9.1 | 3.3 | 0.7 | 6.69 | 13.1% | 4.0% |
| MATCH_WINNER | 37,734 | 15.8 | 10.8 | 22.2 | 15.1 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,095 | 28.3 | 16.8 | 30.7 | 12.7 | 8.8 | 2.3 | 0.3 | 5.58 | 11.5% | 2.6% |
| TOTAL_GAMES | 11,637 | 9.7 | 10.8 | 36.3 | 25.7 | 10.4 | 4.2 | 2.9 | 9.14 | 17.5% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,698 | 24.5 | 28.8 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,558 | 46.7 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,065 | 6.5 | 9.8 | 40.9 | 29.8 | 7.3 | 3.3 | 2.4 | 9.16 | 12.9% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,734 | 23.8 | 16.6 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,567 | 20.3 | 13.4 | 28.4 | 20.2 | 12.2 | 4.3 | 1.1 | 7.71 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,104 | 10.0 | 10.9 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.02 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 52,502 | 44.9% | 25.3% | 13.18 | 35.5% | 15.2% | 10.71 |
| gen1_elo | 52,502 | 44.5% | 25.1% | 13.0 | 35.0% | 15.0% | 10.51 |
| gen1_sr | 52,502 | 52.5% | 31.6% | 15.98 | 44.0% | 21.5% | 13.0 |
| gen2 | 52,502 | 51.3% | 31.6% | 15.51 | 43.9% | 23.0% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,229 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 32,273 | 10.8 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.6 | 15.37 | 50.9% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 31,202 | 16.3 | 11.1 | 22.7 | 15.2 | 18.2 | 11.5 | 5.0 | 9.96 | 34.7% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 90,236 | 31202 | 23701 | 35333 | 25.2 | 142.7 | 1451.1 |
| ge_15pp | 37,201 | 10820 | 8447 | 17934 | 29.1 | 445.6 | 1451.1 |
| ge_25pp | 19,897 | 5134 | 3694 | 11069 | 34.6 | 592.5 | 1431.1 |
| lt_10pp | 39,338 | 15634 | 11206 | 12498 | 22.8 | 49.6 | 1421.7 |

Current slate `SL-20261112T120420Z-82fb7083`: 362 priced rows, quote age at build {'median': 60.1, 'max': 60.1}, freshness {'STALE': 362}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,079 | 19.1 | 11.1 | 25.7 | 18.3 | 17.7 | 7.1 | 1.0 | 8.78 | 25.8% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,077 | 66.4 | 33.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,295 | 0.0 | 2.2 | 38.5 | 25.8 | 23.8 | 8.8 | 0.9 | 11.65 | 33.5% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 52,502 | 8564 (16.3%) | 26.8% | 1.0% | {"EXTERNAL_STALE": 5079, "AGREES_WITH_KALSHI": 2295, "ALL_AGREE": 1077, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 23,582 | 2107 (8.9%) | 36.4% | 1.5% | {"EXTERNAL_STALE": 1308, "AGREES_WITH_KALSHI": 768, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,301 | 646 (4.9%) | 34.5% | 2.0% | {"EXTERNAL_STALE": 410, "AGREES_WITH_KALSHI": 223, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,083 | 614 (10.1%) | 35.2% | 2.1% | {"EXTERNAL_STALE": 385, "AGREES_WITH_KALSHI": 216, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 20,935 | 4926 (23.5%) | 19.0% | 0.9% | {"EXTERNAL_STALE": 2840, "ALL_AGREE": 1077, "AGREES_WITH_KALSHI": 934, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,294 | 10.7 | 7.6 | 19.0 | 14.2 | 21.8 | 16.5 | 10.2 | 14.38 | 48.5% | 26.7% |
| 4-10x | 7,084 | 11.0 | 8.7 | 17.9 | 14.8 | 21.6 | 14.7 | 11.2 | 14.11 | 47.6% | 26.0% |
| <2x | 26,694 | 14.5 | 9.6 | 19.9 | 16.0 | 17.5 | 13.3 | 9.1 | 11.66 | 40.0% | 22.5% |
| >=10x | 8,430 | 10.2 | 6.5 | 15.1 | 14.3 | 21.8 | 18.9 | 13.2 | 16.52 | 54.0% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,764 | 12.4 | 8.6 | 19.7 | 16.1 | 19.1 | 13.7 | 10.5 | 12.8 | 43.2% | 24.2% |
| 300-1000 | 11,413 | 11.6 | 8.7 | 17.8 | 15.1 | 20.6 | 16.4 | 9.9 | 13.87 | 46.9% | 26.3% |
| <300 | 16,687 | 8.1 | 5.9 | 15.1 | 14.4 | 22.9 | 20.1 | 13.6 | 17.47 | 56.5% | 33.7% |
| >=3000 | 10,638 | 21.0 | 12.7 | 24.1 | 15.5 | 13.9 | 7.4 | 5.4 | 7.89 | 26.7% | 12.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1621 | 0.547 | 0.4074 | 0.4769 | +0.070 | -0.069 | 0.0035 ± 0.0038 |
| ratio 4-10x | 1105 | 0.5734 | 0.4289 | 0.486 | +0.087 | -0.057 | 0.0101 ± 0.0048 |
| ratio <2x | 3949 | 0.5347 | 0.412 | 0.4315 | +0.103 | -0.019 | 0.015 ± 0.0023 |
| ratio >=10x | 1364 | 0.5606 | 0.3882 | 0.4355 | +0.125 | -0.047 | 0.0181 ± 0.0048 |
| thinner_sample 1000-3000 | 2213 | 0.5394 | 0.4124 | 0.441 | +0.098 | -0.029 | 0.0135 ± 0.0031 |
| thinner_sample 300-1000 | 1825 | 0.5608 | 0.4208 | 0.4701 | +0.091 | -0.049 | 0.0058 ± 0.0036 |
| thinner_sample <300 | 2634 | 0.5537 | 0.3862 | 0.4434 | +0.110 | -0.057 | 0.0155 ± 0.0034 |
| thinner_sample >=3000 | 1367 | 0.5274 | 0.4339 | 0.4433 | +0.084 | -0.009 | 0.0143 ± 0.0031 |
| data_status ADEQUATE | 2182 | 0.5313 | 0.4288 | 0.4377 | +0.094 | -0.009 | 0.0155 ± 0.0026 |
| data_status LIMITED | 1951 | 0.547 | 0.4142 | 0.4618 | +0.085 | -0.048 | 0.0083 ± 0.0034 |
| data_status POOR | 3906 | 0.5556 | 0.3961 | 0.4485 | +0.107 | -0.052 | 0.013 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1160 | 0.1967 | 0.1967 | -0.0001 ± 0.0005 | 0.5729 | 0.5732 | 0.5033 | 0.4881 | 0.4957 | -0.098 ± 0.0138 | -0.0087 (8) |
| 3-5 | 744 | 0.2085 | 0.208 | +0.0005 ± 0.0013 | 0.603 | 0.5999 | 0.5028 | 0.463 | 0.4758 | -0.100 ± 0.0172 | 0.01 (3) |
| 5-10 | 1727 | 0.2029 | 0.2013 | +0.0016 ± 0.0016 | 0.5924 | 0.5861 | 0.5085 | 0.4346 | 0.4592 | -0.091 ± 0.0111 | -0.0143 (7) |
| 10-15 | 1399 | 0.219 | 0.2092 | +0.0097 ± 0.003 | 0.6298 | 0.6019 | 0.5247 | 0.4013 | 0.4224 | -0.106 ± 0.0124 | -0.055 (6) |
| 15-25 | 1779 | 0.2257 | 0.2065 | +0.0192 ± 0.0042 | 0.6464 | 0.596 | 0.5715 | 0.3771 | 0.425 | -0.103 ± 0.0109 | -0.0045 (11) |
| 25-40 | 1018 | 0.2248 | 0.2043 | +0.0205 ± 0.0085 | 0.6398 | 0.5893 | 0.6444 | 0.3347 | 0.4558 | -0.065 ± 0.0132 | -0.06 (2) |
| 40+ | 212 | 0.3052 | 0.1675 | +0.1377 ± 0.0255 | 0.8164 | 0.5038 | 0.7246 | 0.2672 | 0.3538 | -0.087 ± 0.0246 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5882 | 0.1872 | 0.1881 | -0.0009 ± 0.0002 | 0.5509 | 0.5521 | 0.4918 | 0.4765 | 0.5094 | -0.019 ± 0.0057 | -0.01 (28) |
| 3-5 | 3979 | 0.1993 | 0.1974 | +0.0019 ± 0.0006 | 0.5798 | 0.5731 | 0.482 | 0.4422 | 0.4375 | -0.059 ± 0.0071 | 0.005 (6) |
| 5-10 | 8708 | 0.2012 | 0.1969 | +0.0043 ± 0.0007 | 0.5884 | 0.5745 | 0.4823 | 0.4085 | 0.4166 | -0.049 ± 0.0048 | -0.0114 (22) |
| 10-15 | 7102 | 0.2016 | 0.1856 | +0.0160 ± 0.0013 | 0.5897 | 0.5449 | 0.4852 | 0.3613 | 0.3591 | -0.064 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9123 | 0.2061 | 0.1663 | +0.0397 ± 0.0017 | 0.6039 | 0.4947 | 0.4972 | 0.3017 | 0.2987 | -0.069 ± 0.0043 | -0.0043 (51) |
| 25-40 | 7153 | 0.2229 | 0.124 | +0.0989 ± 0.0026 | 0.64 | 0.3823 | 0.5238 | 0.2098 | 0.2131 | -0.059 ± 0.004 | -0.0733 (3) |
| 40+ | 4894 | 0.3805 | 0.0439 | +0.3366 ± 0.0034 | 0.9911 | 0.1703 | 0.6284 | 0.1015 | 0.0572 | -0.076 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 925 | 0.2026 | 0.2031 | -0.0004 ± 0.0005 | 0.5855 | 0.5868 | 0.5084 | 0.4934 | 0.5211 | -0.093 ± 0.0158 | -0.0117 (6) |
| 3-5 | 671 | 0.2128 | 0.21 | +0.0029 ± 0.0014 | 0.6096 | 0.6031 | 0.5175 | 0.478 | 0.459 | -0.126 ± 0.019 | 0.01 (3) |
| 5-10 | 1488 | 0.2049 | 0.2032 | +0.0017 ± 0.0018 | 0.5955 | 0.5908 | 0.5378 | 0.4634 | 0.4906 | -0.086 ± 0.0121 | -0.01 (4) |
| 10-15 | 1302 | 0.215 | 0.2077 | +0.0073 ± 0.0032 | 0.6229 | 0.6013 | 0.5573 | 0.4329 | 0.4685 | -0.101 ± 0.0132 | -0.04 (5) |
| 15-25 | 1874 | 0.2326 | 0.2108 | +0.0218 ± 0.0042 | 0.6615 | 0.6054 | 0.5844 | 0.3888 | 0.4328 | -0.102 ± 0.0108 | -0.0183 (12) |
| 25-40 | 1303 | 0.2655 | 0.2005 | +0.0649 ± 0.0078 | 0.7408 | 0.5818 | 0.6591 | 0.3452 | 0.4006 | -0.108 ± 0.0125 | -0.008 (5) |
| 40+ | 476 | 0.3734 | 0.1595 | +0.2139 ± 0.0183 | 1.0149 | 0.4838 | 0.7317 | 0.2434 | 0.2815 | -0.089 ± 0.0177 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5053 | 0.1904 | 0.1905 | -0.0002 ± 0.0002 | 0.556 | 0.5561 | 0.5074 | 0.4923 | 0.5066 | -0.040 ± 0.0063 | -0.0154 (26) |
| 3-5 | 3483 | 0.1943 | 0.1934 | +0.0009 ± 0.0006 | 0.5659 | 0.563 | 0.5112 | 0.4716 | 0.4789 | -0.044 ± 0.0076 | 0.01 (5) |
| 5-10 | 7769 | 0.1958 | 0.1924 | +0.0034 ± 0.0008 | 0.576 | 0.5633 | 0.5062 | 0.432 | 0.449 | -0.039 ± 0.005 | -0.0117 (6) |
| 10-15 | 6470 | 0.2024 | 0.1904 | +0.0120 ± 0.0014 | 0.5944 | 0.5575 | 0.5067 | 0.3827 | 0.3974 | -0.049 ± 0.0055 | -0.0189 (18) |
| 15-25 | 9209 | 0.2157 | 0.1788 | +0.0369 ± 0.0017 | 0.628 | 0.5255 | 0.5233 | 0.3279 | 0.3336 | -0.061 ± 0.0044 | -0.014 (52) |
| 25-40 | 8281 | 0.2503 | 0.1379 | +0.1124 ± 0.0026 | 0.707 | 0.4207 | 0.5594 | 0.242 | 0.2271 | -0.076 ± 0.0041 | -0.0095 (20) |
| 40+ | 6576 | 0.4019 | 0.0594 | +0.3426 ± 0.0035 | 1.0589 | 0.2133 | 0.6546 | 0.119 | 0.0806 | -0.073 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1136 | 0.1963 | 0.1973 | -0.0011 ± 0.0005 | 0.5723 | 0.5749 | 0.5022 | 0.4867 | 0.5229 | -0.061 ± 0.0138 | -0.0191 (11) |
| 3-5 | 809 | 0.2087 | 0.2073 | +0.0014 ± 0.0013 | 0.6044 | 0.5995 | 0.4971 | 0.4575 | 0.4611 | -0.109 ± 0.0167 | 0.002 (5) |
| 5-10 | 1732 | 0.2028 | 0.1986 | +0.0043 ± 0.0016 | 0.5912 | 0.5792 | 0.5106 | 0.4369 | 0.4446 | -0.106 ± 0.011 | -0.01 (10) |
| 10-15 | 1442 | 0.2119 | 0.2023 | +0.0096 ± 0.0029 | 0.6142 | 0.5867 | 0.5382 | 0.415 | 0.4397 | -0.105 ± 0.0119 | -0.0286 (7) |
| 15-25 | 1693 | 0.2315 | 0.2122 | +0.0193 ± 0.0044 | 0.6605 | 0.6086 | 0.5808 | 0.3868 | 0.4335 | -0.105 ± 0.0113 | -0.03 (1) |
| 25-40 | 1002 | 0.2169 | 0.2074 | +0.0095 ± 0.0085 | 0.6237 | 0.596 | 0.6524 | 0.3424 | 0.48 | -0.057 ± 0.0133 | -0.0267 (3) |
| 40+ | 225 | 0.3102 | 0.179 | +0.1312 ± 0.0254 | 0.8359 | 0.5294 | 0.7377 | 0.2808 | 0.3778 | -0.079 ± 0.0259 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5697 | 0.1865 | 0.187 | -0.0005 ± 0.0002 | 0.5491 | 0.5495 | 0.4871 | 0.4717 | 0.4853 | -0.038 ± 0.0058 | -0.0189 (44) |
| 3-5 | 4072 | 0.205 | 0.2032 | +0.0018 ± 0.0006 | 0.5952 | 0.5892 | 0.4819 | 0.4423 | 0.4403 | -0.057 ± 0.0072 | -0.0073 (22) |
| 5-10 | 8839 | 0.1959 | 0.1905 | +0.0054 ± 0.0007 | 0.5753 | 0.5583 | 0.4857 | 0.4117 | 0.4119 | -0.056 ± 0.0047 | -0.0117 (42) |
| 10-15 | 7117 | 0.1949 | 0.1794 | +0.0155 ± 0.0012 | 0.575 | 0.5309 | 0.4963 | 0.373 | 0.3721 | -0.062 ± 0.005 | -0.0136 (14) |
| 15-25 | 9158 | 0.2111 | 0.1718 | +0.0392 ± 0.0017 | 0.6157 | 0.5072 | 0.5093 | 0.3147 | 0.312 | -0.069 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7141 | 0.2173 | 0.1238 | +0.0935 ± 0.0026 | 0.628 | 0.3812 | 0.5255 | 0.2099 | 0.2213 | -0.052 ± 0.004 | -0.02 (4) |
| 40+ | 4817 | 0.3889 | 0.0481 | +0.3408 ± 0.0036 | 1.0135 | 0.1811 | 0.6373 | 0.107 | 0.0637 | -0.076 ± 0.003 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1608 | 0.196 | 0.1957 | +0.0004 ± 0.0004 | 0.5701 | 0.569 | 0.5085 | 0.4934 | 0.4894 | -0.076 ± 0.0113 | -0.0221 (56) |
| 3-5 | 1123 | 0.189 | 0.189 | -0.0000 ± 0.001 | 0.5559 | 0.5544 | 0.4985 | 0.4586 | 0.4773 | -0.055 ± 0.0133 | -0.0194 (34) |
| 5-10 | 2292 | 0.1992 | 0.1943 | +0.0049 ± 0.0014 | 0.5877 | 0.5718 | 0.5078 | 0.4342 | 0.4385 | -0.075 ± 0.0094 | -0.005 (78) |
| 10-15 | 1582 | 0.2156 | 0.2026 | +0.0130 ± 0.0028 | 0.6252 | 0.5886 | 0.5442 | 0.4215 | 0.4286 | -0.091 ± 0.0116 | 0.0012 (66) |
| 15-25 | 2067 | 0.2321 | 0.2075 | +0.0245 ± 0.0039 | 0.6623 | 0.5988 | 0.5922 | 0.3971 | 0.433 | -0.090 ± 0.0101 | -0.0214 (59) |
| 25-40 | 1208 | 0.2416 | 0.2121 | +0.0295 ± 0.0081 | 0.6897 | 0.6074 | 0.6879 | 0.3763 | 0.4851 | -0.082 ± 0.0125 | -0.0252 (27) |
| 40+ | 447 | 0.327 | 0.1977 | +0.1293 ± 0.0202 | 0.9349 | 0.5771 | 0.8081 | 0.3311 | 0.4497 | -0.091 ± 0.0189 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5801 | 0.1768 | 0.1767 | +0.0001 ± 0.0002 | 0.5237 | 0.523 | 0.5097 | 0.4945 | 0.4999 | -0.043 ± 0.0056 | -0.0154 (103) |
| 3-5 | 3965 | 0.1941 | 0.1932 | +0.0009 ± 0.0006 | 0.5667 | 0.5641 | 0.502 | 0.4622 | 0.4709 | -0.041 ± 0.0071 | -0.0212 (73) |
| 5-10 | 8115 | 0.1968 | 0.1904 | +0.0064 ± 0.0007 | 0.5808 | 0.5612 | 0.5025 | 0.4289 | 0.4233 | -0.061 ± 0.0049 | -0.0084 (134) |
| 10-15 | 5561 | 0.211 | 0.194 | +0.0170 ± 0.0015 | 0.6139 | 0.5689 | 0.5373 | 0.4144 | 0.4055 | -0.074 ± 0.006 | -0.0057 (111) |
| 15-25 | 6843 | 0.2318 | 0.1991 | +0.0327 ± 0.0021 | 0.6662 | 0.5775 | 0.5764 | 0.3809 | 0.3953 | -0.069 ± 0.0054 | -0.026 (108) |
| 25-40 | 4405 | 0.2579 | 0.1909 | +0.0669 ± 0.0041 | 0.729 | 0.5554 | 0.6397 | 0.3276 | 0.3796 | -0.062 ± 0.0065 | -0.0277 (53) |
| 40+ | 1992 | 0.3689 | 0.1592 | +0.2097 ± 0.0092 | 1.037 | 0.4746 | 0.7405 | 0.241 | 0.2912 | -0.058 ± 0.0085 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8039 | 1.024 ± 0.031 | 1.089 | 0.1676 | 0.1702 | 0.2158 | 0.2033 |
| gen2 | 8039 | 0.821 ± 0.028 | 1.067 | 0.1737 | 0.1705 | 0.2332 | 0.2032 |
| gen1_elo | 8039 | 1.008 ± 0.03 | 1.079 | 0.1741 | 0.1704 | 0.2149 | 0.2033 |
| gen1_sr | 8039 | 1.008 ± 0.037 | 1.114 | 0.1333 | 0.172 | 0.2294 | 0.2029 |
| gen1_ledger | 10327 | 0.868 ± 0.023 | 1.066 | 0.19 | 0.1768 | 0.2172 | 0.2001 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 37,201)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,058 | 24.3% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,662 | 23.3% |
| BOOK_QUALITY | execution | 6,298 | 16.9% |
| POOR_DATA | data | 4,247 | 11.4% |
| LIMITED_DATA | data | 2,228 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,160 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,524 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,416 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,034 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 573 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.3%, coverage 23.3%, data 17.4%, execution 16.9%, market_freshness/coverage 8.6%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.0%, LOW_DATA_QUALITY 72.2%, THIN_PLAYER_HISTORY 60.3%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 48.2%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 33.3%, WIDE_SPREAD 23.4%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.4%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 6.9%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.6%, POST_SETTLEMENT_OBSERVATION 23.3%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 19,897)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,984 | 35.1% |
| STALE_QUOTE | market_freshness | 4,032 | 20.3% |
| BOOK_QUALITY | execution | 3,245 | 16.3% |
| POOR_DATA | data | 1,799 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,170 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 844 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 677 | 3.4% |
| LIMITED_DATA | data | 659 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 347 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 139 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.1%, market_freshness 20.3%, execution 16.3%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.3%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 62.4%, STALE_KALSHI_QUOTE 55.6%, STALE_PLAYER_DATA 45.5%, MODEL_INTERNAL_DISAGREEMENT 41.9%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 22.5%, MODEL_HIGH_UNCERTAINTY 19.2%, PLAYER_IDENTITY_RISK 17.9%, LOW_DISPLAYED_LIQUIDITY 8.5%, EVENT_MAPPING_RISK 8.4%, LEVEL_TRANSFER_RISK 8.2%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.0%, POST_SETTLEMENT_OBSERVATION 35.1%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 15996, "IDENTITY_AMBIGUOUS": 3901}; ticker orientation: {"VERIFIED": 19897}.

Checks: discipline:AMBIGUOUS 1273, discipline:PASS 18624, identity_confidence:AMBIGUOUS 3558, identity_confidence:PASS 16339, level_mapping:NA 1285, level_mapping:PASS 18612, market_pair:AMBIGUOUS 507, market_pair:NA 427, market_pair:PASS 18963, model_complement:NA 389, model_complement:PASS 19508, namesake:AMBIGUOUS 6, namesake:PASS 19891, physical_match_id:NA 6596, physical_match_id:PASS 13301, player_ids:PASS 19897, same_pair_other_event:PASS 19897, ticker_orientation:PASS 19897

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,603 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.2218 / 0.2178 (863) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,266 | 16.6% | 6.0% | 11.1% | {"coverage": 1348, "market_freshness": 274, "market_freshness/coverage": 238, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 40, "mapping": 17, "possible_market_error": 1} | 7.35 | 0.2213 / 0.2108 (3080) | 41.8% | 13.8% | 4.0% | 22.8% |
| DOUBLES | 2,764 | 46.1% | 46.0% | 6.4% | {"execution": 703, "mapping": 384, "market_freshness": 106, "market_freshness/coverage": 73, "coverage": 7} | 23.04 | 0.2986 / 0.2326 (691) | 8.5% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 26,507 | 25.4% | 17.7% | 33.8% | {"coverage": 2366, "market_freshness": 1413, "execution": 1038, "data": 989, "market_freshness/coverage": 683, "mapping": 227, "model_calibration_or_unknown": 6, "model_calibration": 6} | 11.76 | 0.2187 / 0.1986 (5605) | 42.3% | 70.1% | 14.5% | 21.5% |
| ITF_WOMEN | 33,439 | 26.5% | 18.7% | 44.5% | {"coverage": 3184, "market_freshness": 1978, "execution": 1380, "data": 1204, "market_freshness/coverage": 774, "mapping": 210, "model_calibration_or_unknown": 99, "model_calibration": 23} | 12.46 | 0.2028 / 0.1934 (6503) | 42.9% | 57.4% | 10.0% | 21.9% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,919 | 5.9% | 5.0% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.65 | 0.2315 / 0.221 (812) | 30.3% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 404 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 628 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 80 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 12 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 13 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 16 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 19 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 21 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 22 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 23 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 24 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 25 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 26 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 27 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 28 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 29 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 30 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 31 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 34 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 37 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 38 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 39 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 40 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 41 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 45 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 46 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 47 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 434 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 48 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 379 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.973, "by_level_share_of_ge_25pp": {"ATP": 0.0123, "CHALLENGER": 0.1107, "DOUBLES": 0.064, "ITF_MEN": 0.3381, "ITF_WOMEN": 0.4449, "OTHER": 0.0006, "WTA": 0.0146, "WTA125": 0.0147}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5563, "share_primary_cause_market_settled_or_in_play": 0.4438, "share_primary_cause_stale_quote_only": 0.2026}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 19897, "identity_ambiguous_share": 0.1961, "ticker_orientation": {"VERIFIED": 19897}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13301, "with_external": 646, "coverage": 0.0486, "external_status": {"EXTERNAL_STALE": 410, "AGREES_WITH_KALSHI": 223, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 410, "MODEL_LONE_OUTLIER": 223, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3452, "share_external_supports_model": 0.0201}, "pregame_clean_ge_25pp": {"n": 6083, "with_external": 614, "coverage": 0.1009, "external_status": {"EXTERNAL_STALE": 385, "AGREES_WITH_KALSHI": 216, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 385, "MODEL_LONE_OUTLIER": 216, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3518, "share_external_supports_model": 0.0212}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 476.0, "median_sample_ratio": 2.46, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2074, "data_status": {"POOR": 11346, "LIMITED": 4980, "ADEQUATE": 3571}, "comparison_lt_10pp": {"median_thinner_serve_points": 1668.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1621, "model_minus_observed": 0.0701, "kalshi_minus_observed": -0.0694, "brier_diff_model_minus_kalshi": 0.0035}, "4-10x": {"n": 1105, "model_minus_observed": 0.0875, "kalshi_minus_observed": -0.0571, "brier_diff_model_minus_kalshi": 0.0101}, "<2x": {"n": 3949, "model_minus_observed": 0.1032, "kalshi_minus_observed": -0.0195, "brier_diff_model_minus_kalshi": 0.015}, ">=10x": {"n": 1364, "model_minus_observed": 0.1252, "kalshi_minus_observed": -0.0473, "brier_diff_model_minus_kalshi": 0.0181}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8039, "model": {"intercept": -0.56, "slope": 0.821, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.172, "slope": 1.067, "slope_se": 0.031}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1705, "model_brier": 0.2332, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.03, "brier_diff_se": 0.0021, "model_logloss": 0.6637, "kalshi_logloss": 0.5887}, "fair_v1": {"n": 8039, "model": {"intercept": -0.469, "slope": 1.024, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.218, "slope": 1.089, "slope_se": 0.032}, "mean_extremity_model": 0.1676, "mean_extremity_kalshi": 0.1702, "model_brier": 0.2158, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0125, "brier_diff_se": 0.0017, "model_logloss": 0.6209, "kalshi_logloss": 0.5887}, "gen1_elo": {"n": 8039, "model": {"intercept": -0.459, "slope": 1.008, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.219, "slope": 1.079, "slope_se": 0.031}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1704, "model_brier": 0.2149, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0116, "brier_diff_se": 0.0017, "model_logloss": 0.6195, "kalshi_logloss": 0.5889}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2533, "share_ge_15": 0.4492, "median_abs_gap": 13.18, "n": 52502}, "gen1_elo": {"share_ge_25": 0.2511, "share_ge_15": 0.445, "median_abs_gap": 13.0, "n": 52502}, "gen1_sr": {"share_ge_25": 0.3158, "share_ge_15": 0.5247, "median_abs_gap": 15.98, "n": 52502}, "gen2": {"share_ge_25": 0.3157, "share_ge_15": 0.5126, "median_abs_gap": 15.51, "n": 52502}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1517, "share_ge_15": 0.3549, "median_abs_gap": 10.71, "n": 40080}, "gen1_elo": {"share_ge_25": 0.1501, "share_ge_15": 0.3496, "median_abs_gap": 10.51, "n": 40080}, "gen1_sr": {"share_ge_25": 0.2153, "share_ge_15": 0.4402, "median_abs_gap": 13.0, "n": 40083}, "gen2": {"share_ge_25": 0.2302, "share_ge_15": 0.4389, "median_abs_gap": 12.84, "n": 40083}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0371, "share_ge_25_pregame_clean": 0.0311}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0592, "share_ge_25_pregame_clean": 0.0502}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2344, "share_within_10pp_all": 0.4359, "share_within_10pp_pregame_clean": 0.4904, "corr_model_vs_mid_pregame_clean": 0.85}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1160, "model_brier": 0.1967, "kalshi_brier": 0.1967, "brier_diff_model_minus_kalshi": -0.0001}, "10-15": {"n_settled": 1399, "model_brier": 0.219, "kalshi_brier": 0.2092, "brier_diff_model_minus_kalshi": 0.0097}, "15-25": {"n_settled": 1779, "model_brier": 0.2257, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0192}, "25-40": {"n_settled": 1018, "model_brier": 0.2248, "kalshi_brier": 0.2043, "brier_diff_model_minus_kalshi": 0.0205}, "3-5": {"n_settled": 744, "model_brier": 0.2085, "kalshi_brier": 0.208, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 212, "model_brier": 0.3052, "kalshi_brier": 0.1675, "brier_diff_model_minus_kalshi": 0.1377}, "5-10": {"n_settled": 1727, "model_brier": 0.2029, "kalshi_brier": 0.2013, "brier_diff_model_minus_kalshi": 0.0016}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence; NO_SKILL:gen2|WTA
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'NO_SKILL:gen2|WTA', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.56, "slope": 0.821, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.172, "slope": 1.067, "slope_se": 0.031}, "n": 8039}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.5, "slope": 0.868, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.153, "slope": 1.066, "slope_se": 0.027}, "n": 10327}, "NO_SKILL:gen2|WTA": {"n_settled": 346, "model_brier": 0.25, "kalshi_brier": 0.2262, "brier_diff_model_minus_kalshi": 0.0238, "brier_diff_se": 0.0089, "corr_model_outcome": 0.2572, "corr_kalshi_outcome": 0.3102}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 691, "model_brier": 0.2986, "kalshi_brier": 0.2326, "brier_diff_model_minus_kalshi": 0.0661, "brier_diff_se": 0.0111, "corr_model_outcome": 0.1045, "corr_kalshi_outcome": 0.2761}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
