# Start-time reconciliation and RUN TENNIS timing (2026-10-02)

**The rule:** a scheduled start time is never proof that a match has not started. A match is presented as
pregame (and a BET on it is accepted) only on positive, recent live evidence. Everything else fails closed.
This layer does not loosen the first-ball gate; it makes the workflow arrive before the first ball.

## What went wrong on 2026-10-02

Six WTA Beijing matches (Golubic-Stearns, Tjen-Shnaider, Fruhvirtova-Samsonova, Preston-Parry,
Yastremska-Chwalinska, Alexandrova-Sasnovich) had started before the handicapping run.

| root cause | evidence | fix |
|---|---|---|
| RC1 the first-ball watchlist came only from the once-a-day Kalshi discovery snapshot, loaded once per ~5h40m conductor job | the 00:08Z job used discovery `20261001T015107Z`, which predates the `KXWTAMATCH-26OCT01*` listings; it made 0 observations of these matches until the 05:43Z job, when they were in progress or final. Replay at 00:30Z: old code watched 0/6, fixed code 6/6 | `watchlist.capture_board`: the watchlist is the union of discovery and the live capture board (latest full snapshot + later changed passes, records at or before `now`), re-read every segment |
| RC2 Kalshi's `occurrence_datetime` is a day placeholder | all 27 WTA Beijing matches of 10-02 showed 06:00:00Z; ESPN had them at 03:05Z-06:05Z | a nominal shared by >= 4 matches of one series is a placeholder and is never used as a start; any nominal is LOW confidence |
| RC3 a pregame-only first-ball truth (`upper_bound_utc` empty: "seen NOT started at t") was read as "may have started at t" | at 06:30Z replay this hid 15 ESPN-watched pregame main-tour matches from the slate and would have refused decisions on them | `assisted.market.first_ball_bound` returns a bound only when play was observed |
| RC4 nothing computed when the next window opens; RUN TENNIS ran on a 6 h cron | | the planner below runs inside the first-ball conductor every ~10 min |

## Authority order (highest first)

1. **First-ball truth** (`firstball/store/truths`): a confirmed walkover -> `NO_PLAY`; a MATERIAL
   contradiction -> `STATUS_AMBIGUOUS`; an observed play bracket at or before now -> `STARTED`.
2. **Live state** from a live-score source (ESPN `in`/`post`) -> `STARTED`. If a *different* independence
   group later says the match is pending -> `STATUS_AMBIGUOUS` (never "the later one wins").
3. **Live schedule**: the live-score source's own current start (ESPN `date`, updated as courts progress).
   HIGH confidence when ESPN marks it `timeValid` and the reading is <= 30 min old, else MEDIUM. A
   `timeValid: false` time (ESPN's 04:00Z-style placeholder) is ignored.
4. **Court progression** (order of play, free from the same ESPN payload): when the preceding match on the
   same court is in progress, the target cannot start before it ends -- but it may start much sooner than
   its listed time, so the estimate is `observed + remaining(set) + 5 min` with
   remaining = 35/10/5 min (best of 3, in set 1/2/3) or 60/35/10/5/5 (best of 5). A finished preceding
   match with no other pending match ahead -> `observed + 5 min`. Only ever pulls the estimate **earlier**.
5. **Kalshi nominal** (`occurrence_datetime`): LOW confidence, ATP/WTA only, never when it is a day
   placeholder.

Kalshi being open is never evidence of anything. The expected start is the EARLIEST credible candidate.

## Statuses

| status | meaning | BET |
|---|---|---|
| VERIFIED_UPCOMING | a fresh (<= 30 min) live reading says pending, start > 15 min away, from a live time | allowed |
| ESTIMATED_UPCOMING | upcoming, but the time is an estimate (nominal / stale live reading) | ATP/WTA/WTA125: only with a live PRE reading <= 30 min old |
| START_IMMINENT | expected within 15 min, or overdue but seen pending in the last 180 s | as above |
| STARTED | truth or a live source says play began | **blocked** (dropped from the slate; recorder `POST_START_DECISION`) |
| STATUS_AMBIGUOUS | sources disagree, a MATERIAL contradiction, or now >= expected start without a pending reading in the last 180 s | **blocked** (`START_STATUS_NOT_VERIFIED`) |
| START_UNKNOWN | no credible start time (placeholder nominal, no live reading) | blocked for ATP/WTA/WTA125; Challenger/ITF have no source and keep their previous treatment |
| NO_PLAY | confirmed walkover / no play | blocked (dropped from the slate) |

The time is never invented: with no credible candidate `current_expected_start` is `null` and the slate
prints `UNKNOWN`.

Every slate match carries a `start` block: `nominal_scheduled_start`, `current_expected_start`,
`start_time_source`, `start_time_confidence`, `start_time_last_checked`, `earliest_safe_handicap_time`,
`first_ball_status`, `first_ball_source`, `start_status`, `bet_allowed`, `status_reasons`,
`start_time_candidates`, `recommended_handicap_by`, `final_check_time`, `court`, `court_context`. Decision
schema v3 records `start_status_at_decision`, `current_expected_start_at_decision`,
`start_time_source_at_decision`, `start_time_confidence_at_decision`, `start_time_last_checked_at_decision`,
`start_status_reasons_at_decision` (v1/v2 records keep validating against their own field lists).

## RUN TENNIS timing

Upcoming ATP/WTA singles matches are grouped into windows: a window starts at its earliest credible first
ball and holds every match expected within 90 minutes of it. For the next window:

| time | action | how |
|---|---|---|
| earliest - 95 min ... earliest - 45 min | full `RUN TENNIS` **only if** the producer rows are > 3 h old (max 6 dispatches a day) | `tennis-run.yml` workflow_dispatch |
| **earliest - 45 min** (window earliest - 55 ... earliest - 10) | primary refresh: `TENNIS assisted slate` (reuses the producer layers, no model rebuild), unless a slate was built since the window opened or a full run is pending | `tennis-assisted-slate.yml` |
| **earliest - 10 min** (window earliest - 15 ... earliest) | final status/price check: `TENNIS assisted slate` again | `tennis-assisted-slate.yml` |
| after the earliest first ball | nothing for that window; its started matches drop out and the next window takes over | |

Each (window, kind) is dispatched at most once, with >= 15 min between dispatches of one kind; a window whose
earliest start moves 15+ minutes earlier gets a new key and is re-planned. The 6-hourly RUN TENNIS cron
stays as the baseline.

The planner (`scripts/firstball/plan_windows.py`) runs inside the first-ball conductor
(`tennis-firstball.yml`) after every ~10-minute polling segment, so it always sees the freshest live
readings, and it writes (published with the first-ball store on `tennis-data`):

* `tennis-edge-finder/data/firstball/store/schedule/NEXT_WINDOW.md` -- the human-readable answer
* `.../schedule/plan_latest.json` -- every main-tour match's start status, the windows, slate freshness
* `.../schedule/plan_log.jsonl`, `.../schedule/dispatch_log.jsonl` -- append-only history

The slate (`assisted_slates/latest.md`) opens with a **NEXT ACTIONABLE MAIN-TOUR WINDOW** block (earliest
credible first ball, recommended RUN TENNIS time, final check time, number of matches, OVERDUE flag) and a
list of main-tour matches without a verified start status, and every match has a **START STATUS** block.
`plan_latest.json.slate_freshness` marks the published slate STALE when the primary refresh is due and the
slate is older, or a match it shows as upcoming has started, become ambiguous or moved 15+ min earlier.

## Fail-closed behaviour

* No live reading for a main-tour match -> BET refused (`START_STATUS_NOT_VERIFIED`, reason
  `NO_RECENT_LIVE_STATUS`); PASS and WATCH are always recordable and carry the status.
* Sources disagree -> `STATUS_AMBIGUOUS`, BET refused.
* now >= expected start and play not positively known -> `STATUS_AMBIGUOUS`.
* Live says started -> `STARTED` regardless of Kalshi, the nominal or ESPN's listed time.
* Planner failure is non-blocking for the conductor (polling continues) and is visible: TENNIS-18 fails
  `PLAN_STALE` when the plan is older than 45 min.

## Verifying production

1. Open `NEXT_WINDOW.md` on `tennis-data` (path above): planned within the last ~10 min, a next window with an
   earliest credible first ball taken from `LIVE_SCHEDULE:espn_*` or `COURT_PROGRESSION`.
2. `dispatch_log.jsonl` shows `slate_primary` ~45 min and `slate_final` ~10 min before each window, each with
   `dispatched: true`; the matching `TENNIS assisted slate` runs appear in Actions.
3. `assisted_slates/latest.md` has START STATUS blocks and no STARTED match.
4. TENNIS-18 `start_time_window_health` PASS in the health report (see `docs/PRODUCTION_HEALTH.md`).

## Not changed

No model, probability, selector, candidate, staking rule or authority changed.
AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF. Discrepancy rules, ITF abstention and doubles suppression are
unchanged. Nothing here chases a live market: a started match only ever leaves the slate.

## Limitations

* Challenger, ITF and qualifying have no reachable live source: their starts stay START_UNKNOWN (unchanged).
* The court-progression remaining-time table is a fixed conservative heuristic, not a fitted model.
* GitHub `workflow_dispatch` and cron can be delayed by minutes; the 45-minute lead absorbs that, the
  10-minute final check may not.
* ESPN's own `date` can lag a court's progress; the court estimate and the 180 s pending rule cover the gap.
