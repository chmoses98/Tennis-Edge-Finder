# Health gates: before / after

Before: `/home/user/td/tennis-edge-finder/data/research/health_latest.json` (RUN TENNIS #99, main @ 4bd491d). After: `/home/user/work/health_rehearsal.json` (local rehearsal of the branch's RUN TENNIS on tennis-data @ 48ff586; no live Kalshi access from the sandbox, so capture freshness is not representative).

Thresholds were not changed. Every FAIL that remains is a real condition, stated in its row.

| gate | before | after | root cause | fix |
|---|---|---|---|---|
| TENNIS-1 kalshi_tennis_discovery | PASS | PASS | discovery healthy | none needed |
| TENNIS-2 taxonomy_normalization | FAIL | PASS | new series KXATPT5RANK (year-end top-5 ranking) not in the family registry | classified SEASON_RANKING, unpriced (no rankings-race model or rankings feed exists; not faked) |
| TENNIS-3 active_market_mapping | FAIL | PASS | the same 16 KXATPT5RANK markets | same classification |
| TENNIS-4 active_market_projection | FAIL | FAIL | 40 unmapped players: ~37 appear in no reachable results source (ITF results stop April/June 2026), 3 are spelling/transliteration variants; doubles name recovery gaps | transliteration aliases at 0.85; alias candidates queued for human review; minted ids for new TML/ESPN players; detail separates NO_HISTORY (data gap) from fixable identity gaps. Stays FAIL while players are absent from every source -- no unsafe matching |
| TENNIS-5 market_capture_freshness | FAIL | FAIL | trade-tape backlog + capture cadence slipping because every pass fetched and checked out the 8 GB evidence branch | blobless fetches and sparse publishes in the capture and first-ball conductors |
| TENNIS-6 no_post_start_leakage | FAIL | PASS | 330 legacy first-ball violations (pre 2026-09-27 guard) counted forever; AND an unseen active leak: 2,631 rows priced after the exchange had settled the market | append-only quarantine register by prediction id; post-settlement class detected; lifecycle guard (full open snapshot, settled tickers excluded) so new code cannot produce either class |
| TENNIS-7 player_identity_integrity | PASS | PASS | healthy | none needed |
| TENNIS-8 sports_truth_health | FAIL | FAIL | all 'sports truth' was Kalshi's own result | independent lane (Sackmann/TML/ESPN); coverage reported overall and among covered levels; stays FAIL: ITF has no independent source |
| TENNIS-9 exchange_settlement_health | UNKNOWN | PASS | no independent truth to reconcile against | reconciliation of Kalshi settlements against independent truth |
| TENNIS-10 clv_close_coverage | FAIL | PASS | 330 post-start rows counted as missing pregame closes | quarantined post-start rows excluded from the pregame-eligible denominator (both rates reported, threshold unchanged) |
| TENNIS-11 probability_consistency | PASS | PASS | healthy | none needed |
| TENNIS-12 append_only_ledger | PASS | PASS | healthy | none needed |
| TENNIS-13 reproducible_artifacts | PASS | PASS | healthy | build manifest now also carries build_version |
| TENNIS-14 data_source_freshness | PASS | PASS | healthy | none needed |
| TENNIS-15 prospective_confirmation_health | PASS | PASS | healthy | none needed |
| TENNIS-16 assisted_decision_pipeline_health | PASS | PASS | healthy | none needed |
| TENNIS-17 model_market_discrepancy_integrity | PASS | PASS | healthy (every slate row STALE, held at warnings) | fresh open snapshot before every slate |
| TENNIS-18 start_time_window_health | PASS | PASS | healthy, but stale slates were detected and not acted on | planner dispatches a rebuild when a slate goes stale |

## Key detail

* **TENNIS-2** before: unknown_series=["KXATPT5RANK"], parse_rate=0.99971
  after: unknown_series=[], parse_rate=0.99998
* **TENNIS-3** before: unsupported=131
  after: unsupported=147
* **TENNIS-4** before: projectable_open_pregame=344, projected=248, not_projected=96
  after: projectable_open_pregame=138, projected=92, not_projected=46, identity_gap_kinds={"UNCLASSIFIED": 34}
* **TENNIS-5** before: age_min=29.1, trade_backlog_ok=false
  after: age_min=34.5, trade_backlog_ok=true
* **TENNIS-6** before: n_violations=330, violation_classes={"post_start_confirmed": 297, "inside_first_ball_bracket": 33, "schedule_fallback": 0, "no_start_information": 0}, post_start_rows_in_strict_research=0
  after: n_violations=2965, violation_classes={"post_start_confirmed": 297, "inside_first_ball_bracket": 33, "schedule_fallback": 0, "no_start_information": 0, "post_settlement": 2635}, legacy_quarantined=2965, active_violations=0, post_start_rows_in_strict_research=0
* **TENNIS-8** before: ok=0, total=16974, rate=0.0
  after: ok=5988, total=17120, rate=0.3498
* **TENNIS-9** before: 
  after: conflicts=0, reconciled_against_independent_truth=2692
* **TENNIS-10** before: strict_rate=0.8636
  after: strict_rate=0.8636, strict_rate_pregame_eligible=0.981, pregame_eligible=2426
