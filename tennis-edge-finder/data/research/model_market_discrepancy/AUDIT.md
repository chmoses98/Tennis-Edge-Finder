# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-19T14:23Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 40,778): 0-3 14.3%, 3-5 9.5%, 5-10 19.9%, 10-15 15.4%, 15-25 19.1%, 25-40 13.7%, 40+ 8.0%; median gap 11.88 pp.
* **Where the extremes live**: 97.4% of >=25 pp gaps are off the ATP/WTA main tour (ITF 75.3%, Challenger 12.6%, doubles 7.4%). Main tour: ATP 3.9% and WTA 4.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 8,839): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.9%, BOOK_QUALITY 19.3%, STALE_QUOTE 17.8%, POOR_DATA 8.7%, POSSIBLY_IN_PLAY_QUOTE 5.3%, IDENTITY_AMBIGUOUS 4.3%, LIMITED_DATA 3.8%, IN_PLAY_QUOTE 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.6%. By class: coverage 34.9%, execution 19.3%, market_freshness 17.8%, data 12.5%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.6%.
* **Stale / settled / in-play**: 51.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 8,839 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 21.0% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 23.9% of the time and with the model 0.6%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 531.0 points vs 1821.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.053, Gen-2 0.838, Gen-1 ledger 0.879 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 421 model 0.2219 vs Kalshi 0.2097; n 85 model 0.3039 vs Kalshi 0.1748.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 173,053 model-market comparisons (281,087 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 61,192 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-19T14:12:16.248083+00:00'], shadow board 45,346 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-19T14:12:20.016506+00:00'], Model 4 21,142 rows, 16,621 settled tickers, 5,588 tickers with an external scan.
* By model: {"gen1_ledger": 41395, "gen1_elo": 22802, "fair_v1": 22802, "gen2": 22802, "gen1_sr": 22802, "model4_fundamental": 20234, "model4_conditioned": 20216}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 40,778 | 14.3 | 9.5 | 19.9 | 15.4 | 19.1 | 13.7 | 8.0 | 11.88 | 40.7% | 21.7% |
| MW fair_v1 | 22,802 | 13.5 | 8.6 | 18.4 | 16.0 | 19.5 | 14.5 | 9.6 | 12.94 | 43.5% | 24.0% |
| MW gen1_elo | 22,802 | 13.0 | 9.1 | 19.5 | 15.3 | 19.4 | 14.4 | 9.2 | 12.55 | 43.1% | 23.6% |
| MW gen1_ledger | 17,976 | 15.5 | 10.7 | 21.8 | 14.7 | 18.6 | 12.6 | 6.1 | 10.49 | 37.2% | 18.7% |
| MW gen1_sr | 22,802 | 9.9 | 7.4 | 16.8 | 14.3 | 21.4 | 18.3 | 11.8 | 15.54 | 51.6% | 30.2% |
| MW gen2 | 22,802 | 11.4 | 7.3 | 16.4 | 14.3 | 19.9 | 17.5 | 13.1 | 15.29 | 50.5% | 30.6% |
| all families model4_conditioned | 20,216 | 21.8 | 18.8 | 34.5 | 17.6 | 4.8 | 1.4 | 1.1 | 5.98 | 7.3% | 2.5% |
| all families model4_fundamental | 20,234 | 16.1 | 12.9 | 34.5 | 20.4 | 11.3 | 3.4 | 1.4 | 7.91 | 16.1% | 4.8% |

Configurable thresholds (primary): >=5pp 76.1%, >=10pp 56.2%, >=15pp 40.7%, >=20pp 30.2%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.6%
Executable gap (model outside the book, before fees): median 8.2pp; >=10pp 44.5%, >=25pp 16.8%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,984 | 29.3 | 13.0 | 24.8 | 16.6 | 11.7 | 4.0 | 0.6 | 6.35 | 16.3% | 4.6% |
| CHALLENGER | 3,850 | 15.3 | 10.4 | 20.1 | 16.2 | 14.8 | 12.3 | 10.9 | 11.34 | 38.0% | 23.2% |
| ITF_MEN | 6,026 | 10.9 | 7.9 | 17.2 | 14.9 | 20.1 | 16.4 | 12.5 | 14.67 | 49.1% | 28.9% |
| ITF_WOMEN | 8,890 | 10.2 | 6.9 | 15.8 | 15.6 | 22.6 | 18.1 | 10.9 | 15.57 | 51.6% | 29.0% |
| WTA | 1,392 | 18.2 | 12.4 | 24.8 | 19.4 | 20.1 | 4.2 | 0.8 | 8.42 | 25.1% | 5.0% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,984 | 23.6 | 15.3 | 23.8 | 17.6 | 14.1 | 4.6 | 0.9 | 6.85 | 19.7% | 5.5% |
| CHALLENGER | 3,850 | 14.8 | 8.1 | 18.8 | 14.2 | 17.9 | 14.2 | 12.0 | 12.79 | 44.1% | 26.2% |
| ITF_MEN | 6,026 | 9.4 | 6.6 | 15.6 | 13.5 | 19.7 | 19.4 | 15.8 | 17.08 | 55.0% | 35.2% |
| ITF_WOMEN | 8,890 | 8.3 | 5.6 | 13.7 | 13.6 | 21.3 | 20.8 | 16.7 | 18.86 | 58.8% | 37.5% |
| WTA | 1,392 | 15.7 | 8.9 | 20.3 | 16.4 | 23.3 | 14.6 | 0.9 | 11.48 | 38.7% | 15.4% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,984 | 24.0 | 13.9 | 25.6 | 16.6 | 14.3 | 5.0 | 0.7 | 6.95 | 20.0% | 5.7% |
| CHALLENGER | 3,850 | 14.5 | 9.9 | 21.1 | 15.3 | 15.8 | 12.2 | 11.2 | 11.21 | 39.3% | 23.4% |
| ITF_MEN | 6,026 | 9.9 | 8.0 | 17.7 | 14.2 | 20.9 | 16.9 | 12.5 | 15.03 | 50.3% | 29.4% |
| ITF_WOMEN | 8,890 | 9.6 | 7.0 | 16.4 | 15.7 | 23.0 | 18.3 | 10.1 | 15.54 | 51.4% | 28.4% |
| WTA | 1,392 | 24.2 | 17.2 | 30.2 | 15.2 | 10.4 | 2.2 | 0.5 | 6.0 | 13.2% | 2.7% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,165 | 27.3 | 20.3 | 30.9 | 11.3 | 7.3 | 2.6 | 0.3 | 5.24 | 10.1% | 2.8% |
| CHALLENGER | 2,693 | 21.7 | 14.7 | 27.3 | 13.8 | 14.4 | 6.2 | 1.9 | 7.08 | 22.4% | 8.1% |
| DOUBLES | 1,342 | 4.5 | 4.2 | 10.6 | 10.7 | 21.2 | 26.0 | 22.8 | 24.16 | 70.0% | 48.8% |
| ITF_MEN | 5,020 | 14.4 | 8.6 | 20.7 | 15.9 | 20.9 | 12.5 | 7.0 | 11.87 | 40.4% | 19.5% |
| ITF_WOMEN | 5,911 | 11.7 | 9.0 | 19.4 | 15.0 | 22.1 | 16.8 | 6.1 | 13.16 | 45.0% | 22.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 964 | 22.5 | 15.9 | 29.5 | 17.4 | 10.6 | 3.8 | 0.3 | 6.86 | 14.7% | 4.2% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,943 | 29.5 | 13.1 | 25.1 | 16.4 | 11.5 | 3.7 | 0.6 | 6.21 | 15.8% | 4.3% |
| CHALLENGER | 2,750 | 19.9 | 12.9 | 24.9 | 18.8 | 15.1 | 6.4 | 2.0 | 8.34 | 23.5% | 8.4% |
| ITF_MEN | 4,367 | 13.5 | 9.8 | 20.6 | 16.8 | 20.5 | 13.2 | 5.6 | 11.72 | 39.3% | 18.9% |
| ITF_WOMEN | 6,676 | 11.9 | 8.2 | 17.8 | 17.7 | 24.2 | 15.3 | 4.9 | 13.34 | 44.5% | 20.2% |
| WTA | 1,356 | 18.4 | 12.1 | 24.7 | 19.5 | 20.3 | 4.2 | 0.8 | 8.45 | 25.3% | 5.0% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,943 | 23.8 | 15.5 | 23.8 | 17.6 | 14.0 | 4.5 | 0.8 | 6.72 | 19.2% | 5.2% |
| CHALLENGER | 2,750 | 18.6 | 10.4 | 23.4 | 17.0 | 18.4 | 9.7 | 2.5 | 9.46 | 30.6% | 12.2% |
| ITF_MEN | 4,368 | 11.1 | 7.9 | 18.1 | 15.3 | 21.8 | 17.1 | 8.7 | 14.15 | 47.6% | 25.8% |
| ITF_WOMEN | 6,676 | 9.2 | 6.4 | 15.0 | 15.0 | 23.5 | 20.4 | 10.6 | 16.73 | 54.4% | 31.0% |
| WTA | 1,356 | 15.6 | 8.9 | 20.1 | 16.3 | 23.4 | 14.8 | 0.9 | 11.59 | 39.0% | 15.6% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,129 | 27.5 | 20.6 | 31.2 | 11.5 | 6.8 | 2.4 | 0.1 | 5.22 | 9.3% | 2.5% |
| CHALLENGER | 2,339 | 23.3 | 15.9 | 29.2 | 13.6 | 13.7 | 3.8 | 0.6 | 6.52 | 18.0% | 4.4% |
| DOUBLES | 1,246 | 4.6 | 4.3 | 10.7 | 10.9 | 21.1 | 26.2 | 22.2 | 24.07 | 69.5% | 48.4% |
| ITF_MEN | 4,151 | 15.8 | 9.4 | 22.6 | 16.7 | 20.7 | 10.6 | 4.2 | 10.61 | 35.4% | 14.7% |
| ITF_WOMEN | 4,900 | 12.4 | 9.6 | 21.0 | 15.8 | 22.3 | 15.5 | 3.5 | 11.9 | 41.2% | 18.9% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 918 | 23.0 | 16.3 | 29.5 | 17.4 | 10.7 | 3.0 | 0.0 | 6.79 | 13.7% | 3.0% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,342 | 4.5 | 4.2 | 10.6 | 10.7 | 21.2 | 26.0 | 22.8 | 24.16 | 70.0% | 48.8% |
| singles | 16,634 | 16.4 | 11.2 | 22.7 | 15.1 | 18.3 | 11.5 | 4.8 | 9.91 | 34.6% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 5,170 | 13.5 | 9.1 | 19.3 | 16.0 | 18.2 | 14.3 | 9.6 | 12.6 | 42.1% | 23.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 14,684 | 13.9 | 8.6 | 18.5 | 15.6 | 19.8 | 14.3 | 9.5 | 12.95 | 43.6% | 23.8% |
| UNKNOWN | 2,711 | 11.4 | 7.8 | 16.8 | 18.4 | 20.0 | 15.9 | 9.8 | 13.38 | 45.6% | 25.6% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,717 | 19.8 | 11.1 | 21.3 | 17.3 | 15.9 | 8.7 | 5.9 | 9.34 | 30.5% | 14.6% |
| B | 2,961 | 13.0 | 9.2 | 19.9 | 17.2 | 18.5 | 11.7 | 10.5 | 12.04 | 40.7% | 22.2% |
| C | 3,267 | 12.7 | 9.2 | 19.2 | 14.9 | 19.3 | 14.8 | 9.8 | 12.8 | 43.9% | 24.6% |
| D | 3,820 | 12.4 | 8.1 | 17.0 | 15.7 | 22.0 | 15.5 | 9.4 | 13.92 | 46.9% | 24.9% |
| F | 6,037 | 7.8 | 5.6 | 15.0 | 14.7 | 22.4 | 21.5 | 13.1 | 17.82 | 56.9% | 34.5% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5,281 | 23.3 | 15.9 | 28.8 | 15.0 | 11.5 | 4.0 | 1.5 | 6.6 | 17.0% | 5.5% |
| B | 2,543 | 15.3 | 10.0 | 24.2 | 16.4 | 19.2 | 10.8 | 4.0 | 10.06 | 34.1% | 14.8% |
| C | 3,624 | 11.1 | 7.5 | 18.1 | 14.2 | 21.7 | 16.4 | 11.0 | 14.56 | 49.2% | 27.4% |
| D | 2,621 | 13.8 | 9.8 | 20.5 | 13.8 | 21.0 | 14.6 | 6.5 | 12.04 | 42.0% | 21.0% |
| F | 3,907 | 10.1 | 7.8 | 15.2 | 14.4 | 23.1 | 20.5 | 8.9 | 16.15 | 52.5% | 29.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 7,633 | 18.0 | 10.0 | 20.7 | 17.2 | 16.3 | 9.4 | 8.3 | 10.37 | 34.1% | 17.7% |
| LIMITED | 5,110 | 14.4 | 10.4 | 20.2 | 15.6 | 18.9 | 13.2 | 7.3 | 11.5 | 39.5% | 20.5% |
| POOR | 10,059 | 9.6 | 6.7 | 15.9 | 15.2 | 22.1 | 19.0 | 11.6 | 15.94 | 52.7% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 4,493 | 26.8 | 21.5 | 34.8 | 11.3 | 4.0 | 1.2 | 0.2 | 5.12 | 5.5% | 1.5% |
| GAME_SPREAD | 3,999 | 23.6 | 15.4 | 33.9 | 17.3 | 7.5 | 2.1 | 0.3 | 6.43 | 9.8% | 2.4% |
| MATCH_WINNER | 17,976 | 15.5 | 10.7 | 21.8 | 14.7 | 18.6 | 12.6 | 6.1 | 10.49 | 37.2% | 18.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 8,429 | 30.4 | 17.4 | 30.3 | 12.2 | 8.0 | 1.2 | 0.4 | 5.26 | 9.6% | 1.6% |
| TOTAL_GAMES | 6,474 | 7.3 | 8.8 | 37.1 | 29.2 | 11.1 | 3.5 | 3.0 | 9.65 | 17.6% | 6.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,081 | 25.1 | 34.3 | 32.5 | 3.8 | 3.4 | 0.6 | 0.2 | 4.48 | 4.2% | 0.8% |
| GAME_SPREAD | 4,840 | 46.1 | 16.8 | 27.3 | 7.1 | 1.8 | 0.6 | 0.3 | 3.4 | 2.7% | 0.9% |
| TOTAL_GAMES | 8,295 | 4.7 | 6.8 | 40.4 | 35.4 | 7.7 | 2.6 | 2.4 | 9.81 | 12.7% | 5.0% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,084 | 24.2 | 17.6 | 36.0 | 12.0 | 7.2 | 2.6 | 0.3 | 5.85 | 10.1% | 2.9% |
| GAME_SPREAD | 4,843 | 19.4 | 13.4 | 28.5 | 20.0 | 13.9 | 3.8 | 1.0 | 7.91 | 18.7% | 4.8% |
| TOTAL_GAMES | 8,307 | 7.4 | 8.5 | 36.6 | 27.9 | 13.2 | 3.9 | 2.5 | 9.72 | 19.6% | 6.4% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 22,802 | 43.5% | 24.0% | 12.94 | 35.0% | 14.9% | 10.74 |
| gen1_elo | 22,802 | 43.1% | 23.6% | 12.55 | 34.2% | 14.9% | 10.3 |
| gen1_sr | 22,802 | 51.6% | 30.2% | 15.54 | 44.0% | 21.0% | 13.01 |
| gen2 | 22,802 | 50.5% | 30.6% | 15.29 | 44.0% | 22.7% | 13.0 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 12,180 | 16.2 | 10.4 | 21.4 | 17.5 | 19.9 | 11.4 | 3.2 | 10.55 | 34.5% | 14.6% |
| STALE | 10,622 | 10.3 | 6.5 | 15.1 | 14.2 | 19.0 | 18.0 | 16.8 | 17.0 | 53.8% | 34.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 11,444 | 16.8 | 11.4 | 23.0 | 14.7 | 17.5 | 11.7 | 4.9 | 9.69 | 34.1% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 40,778 | 11444 | 15652 | 13682 | 23.8 | 136.0 | 1400.4 |
| ge_15pp | 16,614 | 3897 | 5492 | 7225 | 25.8 | 438.6 | 1380.4 |
| ge_25pp | 8,839 | 1899 | 2372 | 4568 | 32.3 | 575.8 | 1380.4 |
| lt_10pp | 17,873 | 5861 | 7477 | 4535 | 21.8 | 47.9 | 1341.5 |

Current slate `SL-20261019T142352Z-0da74740`: 432 priced rows, quote age at build {'median': 11.9, 'max': 12.0}, freshness {'AGING': 432}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 11 | 0.0 | 0.0 | 36.4 | 0.0 | 45.5 | 18.2 | 0.0 | 20.19 | 63.6% | 18.2% |
| EXTERNAL_LONE_OUTLIER | 12 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,117 | 20.8 | 10.8 | 23.7 | 19.1 | 18.6 | 6.6 | 0.5 | 8.77 | 25.7% | 7.1% |
| KALSHI_LONE_OUTLIER | 11 | 9.1 | 0.0 | 72.7 | 0.0 | 9.1 | 9.1 | 0.0 | 5.2 | 18.2% | 9.1% |
| MARKETS_AGREE | 373 | 69.2 | 30.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.1 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 791 | 0.0 | 2.8 | 35.3 | 28.8 | 23.1 | 9.4 | 0.6 | 12.0 | 33.1% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 22,802 | 3315 (14.5%) | 23.9% | 0.6% | {"EXTERNAL_STALE": 2117, "AGREES_WITH_KALSHI": 791, "ALL_AGREE": 373, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 11, "SUPPORTS_MODEL_DIRECTION": 10, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 9,918 | 815 (8.2%) | 32.1% | 1.1% | {"EXTERNAL_STALE": 544, "AGREES_WITH_KALSHI": 262, "SUPPORTS_MODEL_DIRECTION": 7, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 5,478 | 232 (4.2%) | 34.1% | 1.3% | {"EXTERNAL_STALE": 150, "AGREES_WITH_KALSHI": 79, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 2,650 | 220 (8.3%) | 35.0% | 1.4% | {"EXTERNAL_STALE": 140, "AGREES_WITH_KALSHI": 77, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 9,243 | 1868 (20.2%) | 16.1% | 0.6% | {"EXTERNAL_STALE": 1169, "ALL_AGREE": 373, "AGREES_WITH_KALSHI": 301, "EXTERNAL_OUTLIER": 12, "AGREES_WITH_MODEL": 9, "SUPPORTS_MODEL_DIRECTION": 3, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 4,381 | 11.0 | 7.9 | 19.4 | 15.1 | 21.7 | 15.1 | 9.8 | 13.77 | 46.7% | 24.9% |
| 4-10x | 2,976 | 12.1 | 8.9 | 18.9 | 15.9 | 19.5 | 15.1 | 9.6 | 13.02 | 44.2% | 24.7% |
| <2x | 11,845 | 15.5 | 9.5 | 19.0 | 17.0 | 17.9 | 12.5 | 8.6 | 11.68 | 39.0% | 21.1% |
| >=10x | 3,600 | 10.8 | 6.4 | 15.2 | 13.8 | 21.8 | 19.6 | 12.4 | 16.44 | 53.8% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 5,858 | 12.8 | 8.6 | 19.5 | 16.3 | 19.7 | 13.1 | 10.0 | 12.77 | 42.8% | 23.1% |
| 300-1000 | 5,049 | 12.2 | 8.8 | 16.9 | 15.9 | 20.8 | 16.0 | 9.5 | 13.73 | 46.2% | 25.5% |
| <300 | 6,874 | 8.9 | 6.0 | 15.5 | 14.8 | 22.1 | 20.1 | 12.5 | 16.81 | 54.8% | 32.7% |
| >=3000 | 5,021 | 21.7 | 12.1 | 22.8 | 17.3 | 14.4 | 6.8 | 4.9 | 8.12 | 26.1% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 686 | 0.5427 | 0.4078 | 0.4927 | +0.050 | -0.085 | -0.001 ± 0.0057 |
| ratio 4-10x | 472 | 0.5912 | 0.4496 | 0.5106 | +0.081 | -0.061 | 0.0096 ± 0.0073 |
| ratio <2x | 1701 | 0.5382 | 0.4174 | 0.4497 | +0.088 | -0.032 | 0.0126 ± 0.0034 |
| ratio >=10x | 577 | 0.5612 | 0.3886 | 0.4471 | +0.114 | -0.059 | 0.0113 ± 0.0076 |
| thinner_sample 1000-3000 | 949 | 0.5431 | 0.4172 | 0.4605 | +0.083 | -0.043 | 0.0083 ± 0.0046 |
| thinner_sample 300-1000 | 818 | 0.5665 | 0.4258 | 0.4976 | +0.069 | -0.072 | 0.0004 ± 0.0055 |
| thinner_sample <300 | 1078 | 0.5541 | 0.3917 | 0.4508 | +0.103 | -0.059 | 0.014 ± 0.0053 |
| thinner_sample >=3000 | 591 | 0.5319 | 0.4391 | 0.4602 | +0.072 | -0.021 | 0.0143 ± 0.0047 |
| data_status ADEQUATE | 1003 | 0.5341 | 0.4299 | 0.4536 | +0.081 | -0.024 | 0.0116 ± 0.0039 |
| data_status LIMITED | 845 | 0.5544 | 0.424 | 0.4899 | +0.064 | -0.066 | 0.0032 ± 0.0051 |
| data_status POOR | 1588 | 0.5582 | 0.4009 | 0.4616 | +0.097 | -0.061 | 0.0109 ± 0.0043 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 522 | 0.1957 | 0.1969 | -0.0013 ± 0.0007 | 0.5699 | 0.5725 | 0.4953 | 0.4804 | 0.5307 | -0.050 ± 0.0203 | -0.01 (5) |
| 3-5 | 329 | 0.198 | 0.1969 | +0.0011 ± 0.002 | 0.5781 | 0.5741 | 0.5054 | 0.4655 | 0.4711 | -0.091 ± 0.0252 | 0.02 (1) |
| 5-10 | 716 | 0.1998 | 0.1997 | +0.0001 ± 0.0025 | 0.5851 | 0.5831 | 0.5131 | 0.4387 | 0.4707 | -0.084 ± 0.0174 | -0.0167 (6) |
| 10-15 | 612 | 0.2151 | 0.2057 | +0.0094 ± 0.0046 | 0.6201 | 0.5936 | 0.5257 | 0.4017 | 0.4248 | -0.097 ± 0.0184 | -0.048 (5) |
| 15-25 | 751 | 0.2268 | 0.2133 | +0.0134 ± 0.0066 | 0.6473 | 0.6117 | 0.5807 | 0.3858 | 0.4487 | -0.088 ± 0.0167 | -0.0033 (9) |
| 25-40 | 421 | 0.2219 | 0.2097 | +0.0122 ± 0.0132 | 0.6322 | 0.6023 | 0.6562 | 0.3478 | 0.4822 | -0.070 ± 0.0202 | -0.01 (1) |
| 40+ | 85 | 0.3039 | 0.1748 | +0.1291 ± 0.0409 | 0.8278 | 0.523 | 0.7553 | 0.3058 | 0.3882 | -0.129 ± 0.0396 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2487 | 0.1812 | 0.1824 | -0.0013 ± 0.0003 | 0.5373 | 0.5387 | 0.4791 | 0.4641 | 0.503 | -0.019 ± 0.0087 | -0.0129 (17) |
| 3-5 | 1569 | 0.1951 | 0.1927 | +0.0024 ± 0.0009 | 0.5711 | 0.5615 | 0.4783 | 0.4385 | 0.4264 | -0.070 ± 0.0113 | 0.0 (2) |
| 5-10 | 3408 | 0.1947 | 0.1916 | +0.0031 ± 0.0011 | 0.5717 | 0.5618 | 0.4846 | 0.4109 | 0.4249 | -0.050 ± 0.0076 | -0.0119 (21) |
| 10-15 | 3006 | 0.2033 | 0.1851 | +0.0182 ± 0.002 | 0.5941 | 0.5432 | 0.4871 | 0.3624 | 0.3523 | -0.075 ± 0.0078 | -0.0281 (16) |
| 15-25 | 3635 | 0.2087 | 0.173 | +0.0357 ± 0.0027 | 0.6088 | 0.5105 | 0.5037 | 0.3076 | 0.3158 | -0.066 ± 0.0069 | -0.0025 (44) |
| 25-40 | 2807 | 0.2224 | 0.1272 | +0.0952 ± 0.0042 | 0.6392 | 0.3914 | 0.5335 | 0.2203 | 0.2287 | -0.067 ± 0.0065 | -0.01 (1) |
| 40+ | 1871 | 0.3796 | 0.0425 | +0.3372 ± 0.0053 | 0.9884 | 0.1689 | 0.6291 | 0.1066 | 0.0556 | -0.088 ± 0.0044 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 391 | 0.2 | 0.2006 | -0.0006 ± 0.0008 | 0.5818 | 0.5832 | 0.5029 | 0.4879 | 0.5115 | -0.083 ± 0.0241 | -0.01 (3) |
| 3-5 | 284 | 0.2157 | 0.215 | +0.0006 ± 0.0022 | 0.6147 | 0.6141 | 0.5161 | 0.4762 | 0.4824 | -0.093 ± 0.0293 | 0.02 (1) |
| 5-10 | 614 | 0.1987 | 0.1987 | -0.0001 ± 0.0027 | 0.5807 | 0.5805 | 0.5451 | 0.4702 | 0.5081 | -0.072 ± 0.0186 | -0.01 (4) |
| 10-15 | 568 | 0.2177 | 0.2116 | +0.0060 ± 0.0048 | 0.6256 | 0.6096 | 0.569 | 0.4446 | 0.4859 | -0.092 ± 0.02 | -0.04 (5) |
| 15-25 | 825 | 0.2306 | 0.2096 | +0.0210 ± 0.0063 | 0.653 | 0.6019 | 0.5911 | 0.3949 | 0.4436 | -0.097 ± 0.0162 | -0.0133 (9) |
| 25-40 | 552 | 0.2671 | 0.1979 | +0.0692 ± 0.012 | 0.744 | 0.5766 | 0.6654 | 0.35 | 0.3986 | -0.125 ± 0.0187 | -0.0075 (4) |
| 40+ | 202 | 0.3673 | 0.177 | +0.1903 ± 0.0293 | 1.0223 | 0.5252 | 0.7456 | 0.2633 | 0.3218 | -0.082 ± 0.0285 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2108 | 0.185 | 0.1855 | -0.0005 ± 0.0003 | 0.5461 | 0.5471 | 0.5022 | 0.4874 | 0.51 | -0.035 ± 0.0097 | -0.0133 (15) |
| 3-5 | 1341 | 0.1959 | 0.1949 | +0.0010 ± 0.001 | 0.5681 | 0.5655 | 0.5155 | 0.4756 | 0.4817 | -0.048 ± 0.0123 | 0.02 (1) |
| 5-10 | 3024 | 0.1915 | 0.1895 | +0.0020 ± 0.0012 | 0.5653 | 0.5572 | 0.5071 | 0.4331 | 0.458 | -0.037 ± 0.008 | -0.0117 (6) |
| 10-15 | 2643 | 0.2003 | 0.1896 | +0.0107 ± 0.0021 | 0.589 | 0.5519 | 0.5213 | 0.3967 | 0.4185 | -0.050 ± 0.0086 | -0.0189 (18) |
| 15-25 | 3769 | 0.2181 | 0.1806 | +0.0375 ± 0.0027 | 0.631 | 0.5302 | 0.5321 | 0.3359 | 0.342 | -0.070 ± 0.007 | -0.0086 (42) |
| 25-40 | 3316 | 0.2516 | 0.1369 | +0.1146 ± 0.0041 | 0.7097 | 0.4201 | 0.5639 | 0.2478 | 0.2259 | -0.092 ± 0.0064 | -0.0044 (18) |
| 40+ | 2582 | 0.402 | 0.0658 | +0.3362 ± 0.0058 | 1.0612 | 0.2301 | 0.6631 | 0.1261 | 0.0949 | -0.071 ± 0.0049 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 505 | 0.1983 | 0.2009 | -0.0026 ± 0.0007 | 0.5774 | 0.5835 | 0.4981 | 0.4829 | 0.5584 | -0.011 ± 0.0202 | -0.0137 (8) |
| 3-5 | 369 | 0.1937 | 0.1912 | +0.0025 ± 0.0018 | 0.565 | 0.5592 | 0.4994 | 0.4598 | 0.4499 | -0.121 ± 0.0238 | 0.0067 (3) |
| 5-10 | 744 | 0.2015 | 0.1981 | +0.0034 ± 0.0025 | 0.5899 | 0.5785 | 0.5076 | 0.4338 | 0.4449 | -0.097 ± 0.0168 | -0.0071 (7) |
| 10-15 | 597 | 0.2092 | 0.2062 | +0.0030 ± 0.0046 | 0.6061 | 0.5955 | 0.5415 | 0.4183 | 0.4707 | -0.077 ± 0.0184 | -0.0317 (6) |
| 15-25 | 703 | 0.2344 | 0.2107 | +0.0237 ± 0.0067 | 0.6677 | 0.6055 | 0.5894 | 0.3962 | 0.431 | -0.116 ± 0.0173 | -0.03 (1) |
| 25-40 | 433 | 0.2051 | 0.2153 | -0.0103 ± 0.0129 | 0.5949 | 0.6149 | 0.6626 | 0.3529 | 0.5219 | -0.042 ± 0.0196 | 0.015 (2) |
| 40+ | 85 | 0.3246 | 0.1885 | +0.1362 ± 0.0425 | 0.8809 | 0.5541 | 0.7597 | 0.3066 | 0.3882 | -0.123 ± 0.0444 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2381 | 0.1883 | 0.1893 | -0.0010 ± 0.0003 | 0.5535 | 0.5554 | 0.4885 | 0.4732 | 0.501 | -0.027 ± 0.009 | -0.0163 (35) |
| 3-5 | 1656 | 0.1896 | 0.1863 | +0.0032 ± 0.0009 | 0.5572 | 0.5494 | 0.4786 | 0.4391 | 0.4191 | -0.082 ± 0.0109 | -0.0094 (18) |
| 5-10 | 3623 | 0.1959 | 0.1894 | +0.0065 ± 0.0011 | 0.5763 | 0.5553 | 0.4831 | 0.4093 | 0.3999 | -0.070 ± 0.0073 | -0.01 (31) |
| 10-15 | 2806 | 0.1978 | 0.1812 | +0.0166 ± 0.002 | 0.5807 | 0.5323 | 0.5013 | 0.3778 | 0.3731 | -0.072 ± 0.008 | -0.015 (12) |
| 15-25 | 3750 | 0.209 | 0.1717 | +0.0374 ± 0.0026 | 0.6112 | 0.5077 | 0.5089 | 0.3142 | 0.3163 | -0.070 ± 0.0068 | -0.03 (2) |
| 25-40 | 2764 | 0.2162 | 0.1258 | +0.0904 ± 0.0042 | 0.6252 | 0.3865 | 0.5311 | 0.2154 | 0.2337 | -0.060 ± 0.0064 | 0.01 (3) |
| 40+ | 1803 | 0.3947 | 0.0471 | +0.3477 ± 0.0057 | 1.0304 | 0.1813 | 0.6404 | 0.1118 | 0.0588 | -0.090 ± 0.0049 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 848 | 0.1969 | 0.197 | -0.0002 ± 0.0005 | 0.5743 | 0.5744 | 0.5065 | 0.4915 | 0.4953 | -0.055 ± 0.0154 | -0.0224 (49) |
| 3-5 | 599 | 0.1941 | 0.1935 | +0.0006 ± 0.0015 | 0.5665 | 0.5639 | 0.4826 | 0.4427 | 0.4524 | -0.053 ± 0.0182 | -0.0194 (34) |
| 5-10 | 1254 | 0.1995 | 0.1931 | +0.0063 ± 0.0019 | 0.5867 | 0.5683 | 0.4902 | 0.4168 | 0.4115 | -0.069 ± 0.0127 | -0.005 (78) |
| 10-15 | 808 | 0.2086 | 0.197 | +0.0116 ± 0.0039 | 0.6053 | 0.5758 | 0.5127 | 0.3896 | 0.4022 | -0.065 ± 0.0158 | 0.0014 (64) |
| 15-25 | 1077 | 0.2328 | 0.2123 | +0.0205 ± 0.0055 | 0.6633 | 0.6109 | 0.5712 | 0.3762 | 0.4225 | -0.062 ± 0.0141 | -0.0214 (59) |
| 25-40 | 643 | 0.246 | 0.2005 | +0.0455 ± 0.0108 | 0.6974 | 0.5799 | 0.6586 | 0.3461 | 0.4277 | -0.084 ± 0.0164 | -0.0219 (26) |
| 40+ | 222 | 0.3534 | 0.1938 | +0.1595 ± 0.0296 | 1.0224 | 0.5688 | 0.804 | 0.3171 | 0.4189 | -0.083 ± 0.0261 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2645 | 0.1876 | 0.1877 | -0.0001 ± 0.0003 | 0.5503 | 0.5496 | 0.5047 | 0.4894 | 0.4979 | -0.038 ± 0.0085 | -0.0157 (88) |
| 3-5 | 1829 | 0.1914 | 0.1888 | +0.0026 ± 0.0008 | 0.5593 | 0.5533 | 0.4891 | 0.4494 | 0.4374 | -0.060 ± 0.0102 | -0.0209 (69) |
| 5-10 | 3660 | 0.1961 | 0.1873 | +0.0088 ± 0.0011 | 0.5774 | 0.5528 | 0.4881 | 0.4146 | 0.394 | -0.073 ± 0.0072 | -0.0082 (132) |
| 10-15 | 2511 | 0.2041 | 0.1892 | +0.0149 ± 0.0022 | 0.5952 | 0.5568 | 0.5183 | 0.3953 | 0.3955 | -0.061 ± 0.0087 | -0.0053 (105) |
| 15-25 | 3131 | 0.2286 | 0.1984 | +0.0303 ± 0.0031 | 0.6586 | 0.5768 | 0.564 | 0.3687 | 0.3903 | -0.063 ± 0.008 | -0.0253 (107) |
| 25-40 | 2137 | 0.2515 | 0.1743 | +0.0772 ± 0.0057 | 0.7141 | 0.5127 | 0.6184 | 0.3046 | 0.3421 | -0.075 ± 0.0087 | -0.0229 (51) |
| 40+ | 1009 | 0.3783 | 0.1354 | +0.2428 ± 0.0123 | 1.0742 | 0.4121 | 0.7208 | 0.2167 | 0.2418 | -0.075 ± 0.0108 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3436 | 1.053 ± 0.048 | 1.179 | 0.1678 | 0.1651 | 0.2129 | 0.2037 |
| gen2 | 3436 | 0.838 ± 0.044 | 1.139 | 0.1736 | 0.1653 | 0.2319 | 0.2036 |
| gen1_elo | 3436 | 1.034 ± 0.047 | 1.164 | 0.1736 | 0.1654 | 0.2118 | 0.2037 |
| gen1_sr | 3436 | 1.04 ± 0.057 | 1.21 | 0.1337 | 0.167 | 0.2279 | 0.2033 |
| gen1_ledger | 5451 | 0.879 ± 0.033 | 1.084 | 0.1786 | 0.1806 | 0.2182 | 0.199 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 16,614)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,902 | 23.5% |
| STALE_QUOTE | market_freshness | 3,402 | 20.5% |
| BOOK_QUALITY | execution | 3,261 | 19.6% |
| POOR_DATA | data | 1,828 | 11.0% |
| LIMITED_DATA | data | 1,130 | 6.8% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 888 | 5.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 823 | 5.0% |
| IDENTITY_AMBIGUOUS | mapping | 670 | 4.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 473 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 237 | 1.4% |

Cause class: coverage 23.5%, market_freshness 20.5%, execution 19.6%, data 17.8%, market_freshness/coverage 8.2%, model_calibration_or_unknown 5.0%, mapping 4.0%, model_calibration 1.4%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.5%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 69.8%, THIN_PLAYER_HISTORY 58.1%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 43.5%, MODEL_INTERNAL_DISAGREEMENT 40.5%, ASYMMETRIC_SAMPLE_SIZE 32.4%, WIDE_SPREAD 25.6%, MODEL_HIGH_UNCERTAINTY 17.9%, PLAYER_IDENTITY_RISK 15.1%, LEVEL_TRANSFER_RISK 9.3%, EVENT_MAPPING_RISK 8.6%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 2.4%, UNKNOWN 1.0%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.9%, POST_SETTLEMENT_OBSERVATION 23.5%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### >= ge_25 pp (N = 8,839)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 3,083 | 34.9% |
| BOOK_QUALITY | execution | 1,706 | 19.3% |
| STALE_QUOTE | market_freshness | 1,576 | 17.8% |
| POOR_DATA | data | 769 | 8.7% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 472 | 5.3% |
| IDENTITY_AMBIGUOUS | mapping | 380 | 4.3% |
| LIMITED_DATA | data | 332 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 293 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 178 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 50 | 0.6% |

Cause class: coverage 34.9%, execution 19.3%, market_freshness 17.8%, data 12.5%, market_freshness/coverage 8.6%, mapping 4.3%, model_calibration_or_unknown 2.0%, model_calibration 0.6%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.6%, START_UNVERIFIABLE 97.4%, LOW_DATA_QUALITY 73.9%, THIN_PLAYER_HISTORY 60.8%, STALE_KALSHI_QUOTE 51.7%, STALE_PLAYER_DATA 47.3%, MODEL_INTERNAL_DISAGREEMENT 41.3%, ASYMMETRIC_SAMPLE_SIZE 34.4%, WIDE_SPREAD 25.4%, PLAYER_IDENTITY_RISK 18.4%, MODEL_HIGH_UNCERTAINTY 18.1%, EVENT_MAPPING_RISK 10.4%, LEVEL_TRANSFER_RISK 8.2%, LOW_DISPLAYED_LIQUIDITY 7.9%, MODEL_CALIBRATION_OUTLIER 5.2%, EXTERNAL_MARKET_REJECTION 1.3%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.7%, POST_SETTLEMENT_OBSERVATION 34.9%, POSSIBLE_IN_PLAY_QUOTE 5.7%, CONFIRMED_IN_PLAY_QUOTE 0.5%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 6982, "IDENTITY_AMBIGUOUS": 1857}; ticker orientation: {"VERIFIED": 8839}.

Checks: discipline:AMBIGUOUS 655, discipline:PASS 8184, identity_confidence:AMBIGUOUS 1626, identity_confidence:PASS 7213, level_mapping:NA 667, level_mapping:PASS 8172, market_pair:AMBIGUOUS 321, market_pair:NA 216, market_pair:PASS 8302, model_complement:NA 183, model_complement:PASS 8656, namesake:PASS 8839, physical_match_id:NA 3361, physical_match_id:PASS 5478, player_ids:PASS 8839, same_pair_other_event:PASS 8839, ticker_orientation:PASS 8839

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,149 | 3.9% | 3.6% | 1.4% | {"market_freshness": 42, "data": 29, "model_calibration_or_unknown": 17, "execution": 15, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 2} | 5.83 | 0.2156 / 0.2094 (343) | 18.1% | 3.4% | 4.0% | 2.5% |
| CHALLENGER | 6,543 | 17.0% | 6.6% | 12.6% | {"coverage": 636, "market_freshness/coverage": 140, "market_freshness": 133, "data": 99, "model_calibration_or_unknown": 52, "execution": 26, "mapping": 13, "model_calibration": 11} | 7.32 | 0.2168 / 0.2064 (1616) | 35.4% | 15.7% | 3.6% | 22.2% |
| DOUBLES | 1,342 | 48.8% | 48.4% | 7.4% | {"execution": 325, "mapping": 172, "market_freshness": 106, "market_freshness/coverage": 45, "coverage": 7} | 24.07 | 0.322 / 0.2343 (346) | 17.4% | 0.0% | 100.0% | 7.1% |
| ITF_MEN | 11,046 | 24.6% | 16.9% | 30.8% | {"coverage": 1066, "execution": 556, "market_freshness": 421, "data": 359, "market_freshness/coverage": 222, "mapping": 97, "model_calibration_or_unknown": 2} | 11.22 | 0.2149 / 0.1953 (2680) | 36.3% | 62.4% | 13.9% | 22.9% |
| ITF_WOMEN | 14,801 | 26.6% | 19.7% | 44.5% | {"coverage": 1355, "market_freshness": 798, "execution": 754, "data": 580, "market_freshness/coverage": 299, "mapping": 92, "model_calibration_or_unknown": 43, "model_calibration": 10} | 12.83 | 0.2024 / 0.1938 (2987) | 38.1% | 57.9% | 10.3% | 21.8% |
| OTHER | 149 | 8.1% | 7.3% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 2,356 | 4.7% | 4.2% | 1.2% | {"market_freshness": 36, "model_calibration_or_unknown": 23, "execution": 16, "data": 11, "market_freshness/coverage": 10, "model_calibration": 9, "coverage": 4, "mapping": 1} | 7.74 | 0.2385 / 0.2317 (385) | 23.6% | 1.4% | 1.5% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 2.0% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 5 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 6 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 7 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 9 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 10 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 11 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 12 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 13 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 14 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 15 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 16 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 17 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 18 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 19 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 20 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 21 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 23 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 24 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 25 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 26 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 27 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 28 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 29 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 321 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 30 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 31 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 32 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 33 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 34 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 752 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 35 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 36 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.5h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 765 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 37 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.9h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 243 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |
| 38 | `KXITFMATCH-26OCT12TROCHI-TRO` | ITF_MEN | fair_v1 | 82% / 6% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 469 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 520.24); no external reference |
| 39 | `KXITFWMATCH-26OCT18NIELAG-NIE` | ITF_WOMEN | fair_v1 | 83% / 7% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 535 min (STALE); data POOR (grade D, thinner serve sample 724.0, ratio 4.19); no external reference |
| 40 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 41 | `KXITFWMATCH-26OCT13VISBRI-VIS` | ITF_WOMEN | fair_v1 | 79% / 2% | +76 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 33 min (STALE); data POOR (grade F, thinner serve sample 86.0, ratio 3.9); no external reference |
| 42 | `KXATPCHALLENGERDOUBLES-26OCT14KUMMRVGILVER-KUMMRV` | DOUBLES | gen1_ledger | 85% / 9% | +76 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 6 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 43 | `KXITFWMATCH-26OCT16ESTLAB-LAB` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 68 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1475.0, ratio 2.28); no external reference |
| 44 | `KXITFWMATCH-26OCT19VLABOU-VLA` | ITF_WOMEN | fair_v1 | 77% / 2% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 3.13); no external reference |
| 45 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXATPCHALLENGERMATCH-26OCT11RAQBOI-BOI` | CHALLENGER | fair_v1 | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 564 min (STALE); data LIMITED (grade C, thinner serve sample 397.0, ratio 3.45); no external reference |
| 47 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 48 | `KXITFMATCH-26OCT14DZHVER-DZH` | ITF_MEN | fair_v1 | 78% / 3% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 684.88); no external reference |
| 49 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 381 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 50 | `KXATPDOUBLES-26OCT18COLGOFPOLZIE-COLGOF` | DOUBLES | gen1_ledger | 90% / 15% | +75 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9736, "by_level_share_of_ge_25pp": {"ATP": 0.014, "CHALLENGER": 0.1256, "DOUBLES": 0.0741, "ITF_MEN": 0.3081, "ITF_WOMEN": 0.4447, "OTHER": 0.0014, "WTA": 0.0124, "WTA125": 0.0197}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5168, "share_primary_cause_market_settled_or_in_play": 0.4353, "share_primary_cause_stale_quote_only": 0.1783}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 8839, "identity_ambiguous_share": 0.2101, "ticker_orientation": {"VERIFIED": 8839}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 5478, "with_external": 232, "coverage": 0.0424, "external_status": {"EXTERNAL_STALE": 150, "AGREES_WITH_KALSHI": 79, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 150, "MODEL_LONE_OUTLIER": 79, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3405, "share_external_supports_model": 0.0129}, "pregame_clean_ge_25pp": {"n": 2650, "with_external": 220, "coverage": 0.083, "external_status": {"EXTERNAL_STALE": 140, "AGREES_WITH_KALSHI": 77, "SUPPORTS_MODEL_DIRECTION": 2, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 140, "MODEL_LONE_OUTLIER": 77, "ALL_THREE_DISAGREE": 2, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.35, "share_external_supports_model": 0.0136}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 531.0, "median_sample_ratio": 2.46, "median_min_matches": 21.0, "median_max_days_since_last": 218.0, "share_severe_asymmetry": 0.2077, "data_status": {"POOR": 4792, "LIMITED": 2499, "ADEQUATE": 1548}, "comparison_lt_10pp": {"median_thinner_serve_points": 1821.0, "median_sample_ratio": 1.67, "median_min_matches": 95.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 686, "model_minus_observed": 0.05, "kalshi_minus_observed": -0.0849, "brier_diff_model_minus_kalshi": -0.001}, "4-10x": {"n": 472, "model_minus_observed": 0.0806, "kalshi_minus_observed": -0.061, "brier_diff_model_minus_kalshi": 0.0096}, "<2x": {"n": 1701, "model_minus_observed": 0.0884, "kalshi_minus_observed": -0.0324, "brier_diff_model_minus_kalshi": 0.0126}, ">=10x": {"n": 577, "model_minus_observed": 0.1141, "kalshi_minus_observed": -0.0586, "brier_diff_model_minus_kalshi": 0.0113}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 3436, "model": {"intercept": -0.529, "slope": 0.838, "slope_se": 0.044}, "kalshi_mid_same_rows": {"intercept": 0.235, "slope": 1.139, "slope_se": 0.051}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.1653, "model_brier": 0.2319, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0283, "brier_diff_se": 0.0032, "model_logloss": 0.6606, "kalshi_logloss": 0.5896}, "fair_v1": {"n": 3436, "model": {"intercept": -0.404, "slope": 1.053, "slope_se": 0.048}, "kalshi_mid_same_rows": {"intercept": 0.312, "slope": 1.179, "slope_se": 0.051}, "mean_extremity_model": 0.1678, "mean_extremity_kalshi": 0.1651, "model_brier": 0.2129, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0092, "brier_diff_se": 0.0026, "model_logloss": 0.6137, "kalshi_logloss": 0.5896}, "gen1_elo": {"n": 3436, "model": {"intercept": -0.392, "slope": 1.034, "slope_se": 0.047}, "kalshi_mid_same_rows": {"intercept": 0.309, "slope": 1.164, "slope_se": 0.05}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.1654, "model_brier": 0.2118, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0081, "brier_diff_se": 0.0026, "model_logloss": 0.612, "kalshi_logloss": 0.5896}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2402, "share_ge_15": 0.435, "median_abs_gap": 12.94, "n": 22802}, "gen1_elo": {"share_ge_25": 0.2365, "share_ge_15": 0.4308, "median_abs_gap": 12.55, "n": 22802}, "gen1_sr": {"share_ge_25": 0.3017, "share_ge_15": 0.5161, "median_abs_gap": 15.54, "n": 22802}, "gen2": {"share_ge_25": 0.3058, "share_ge_15": 0.5053, "median_abs_gap": 15.29, "n": 22802}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1495, "share_ge_15": 0.3501, "median_abs_gap": 10.74, "n": 17726}, "gen1_elo": {"share_ge_25": 0.1493, "share_ge_15": 0.3424, "median_abs_gap": 10.3, "n": 17724}, "gen1_sr": {"share_ge_25": 0.2102, "share_ge_15": 0.4395, "median_abs_gap": 13.01, "n": 17726}, "gen2": {"share_ge_25": 0.2266, "share_ge_15": 0.4398, "median_abs_gap": 13.0, "n": 17727}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.83, "share_ge_25_all": 0.0394, "share_ge_25_pregame_clean": 0.0365}, "WTA": {"median_abs_gap_pregame_clean": 7.74, "share_ge_25_all": 0.0467, "share_ge_25_pregame_clean": 0.0422}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2389, "share_within_10pp_all": 0.4383, "share_within_10pp_pregame_clean": 0.4919, "corr_model_vs_mid_pregame_clean": 0.8422}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 522, "model_brier": 0.1957, "kalshi_brier": 0.1969, "brier_diff_model_minus_kalshi": -0.0013}, "10-15": {"n_settled": 612, "model_brier": 0.2151, "kalshi_brier": 0.2057, "brier_diff_model_minus_kalshi": 0.0094}, "15-25": {"n_settled": 751, "model_brier": 0.2268, "kalshi_brier": 0.2133, "brier_diff_model_minus_kalshi": 0.0134}, "25-40": {"n_settled": 421, "model_brier": 0.2219, "kalshi_brier": 0.2097, "brier_diff_model_minus_kalshi": 0.0122}, "3-5": {"n_settled": 329, "model_brier": 0.198, "kalshi_brier": 0.1969, "brier_diff_model_minus_kalshi": 0.0011}, "40+": {"n_settled": 85, "model_brier": 0.3039, "kalshi_brier": 0.1748, "brier_diff_model_minus_kalshi": 0.1291}, "5-10": {"n_settled": 716, "model_brier": 0.1998, "kalshi_brier": 0.1997, "brier_diff_model_minus_kalshi": 0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.529, "slope": 0.838, "slope_se": 0.044}, "kalshi_slope": {"intercept": 0.235, "slope": 1.139, "slope_se": 0.051}, "n": 3436}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.514, "slope": 0.879, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.152, "slope": 1.084, "slope_se": 0.038}, "n": 5451}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 346, "model_brier": 0.322, "kalshi_brier": 0.2343, "brier_diff_model_minus_kalshi": 0.0878, "brier_diff_se": 0.0169, "corr_model_outcome": 0.0119, "corr_kalshi_outcome": 0.2598}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
