# First-ball wave report

**2026-09-11. Repository: `chmoses98/Tennis-Edge-Finder`. REAL-MONEY AUTHORITY: OFF.**

The mission was to replace "probably before the match" with a claim that survives a hostile audit:

> *This observation existed before the first ball.*

## Headline

**ATP and WTA main tour and the Grand Slams are solved. Challenger, ITF and qualifying are not, and are
not faked.** Those levels fail closed as `START_UNKNOWN`, produce no strict close and no strict CLV. That
is the outcome the brief anticipated, and it is reported rather than smoothed over: a gap that is visible
is a research limitation, while a gap filled with a guess is a false claim.

**Historical first-ball recovery is not available at all.** No reachable source records a real start for
a completed match. Prospective rows captured before this wave stay `START_UNKNOWN` and will be
reclassified deterministically if trustworthy truth ever arrives.

## 1. Sources researched

40 candidate endpoints across 20 hosts, probed from GitHub Actions runners in four runs whose raw
evidence is on `tennis-data` under `data/firstball/probe/` and `data/firstball/browser_probe/`. Every
candidate was requested repeatedly, spaced in time, and every host's `robots.txt` was read in the same
run. Full matrix: [docs/FIRST_BALL_SOURCES.md](docs/FIRST_BALL_SOURCES.md).

| outcome | sources |
|---|---|
| reachable and useful | ESPN site API (ATP and WTA scoreboards) |
| reachable, not useful | ESPN core API (`$ref` index), ITF tournament calendar (no match state), TheSportsDB (empty for tennis), tennisexplorer (HTML only, no API) |
| blocked | ATP Tour (Cloudflare 403), SofaScore (403 on three hosts), flashscore (401), livescore.com (503), protennislive (503/404), WTA API (404), all four Grand Slam site feeds |

Two corrections worth recording, because both were self-inflicted false negatives that would have
changed the conclusion:

* ESPN's WTA scoreboard first looked broken (HTTP 200, unparseable). It is 2,000,001 bytes and the
  prober's own 2 MB cap truncated it. The cap is now 16 MB.
* The ITF live-scores page is a React shell served by the ITF's own data provider
  (`api.itf-production.sports-data.stadion.io`, 5 s refetch interval). Guessing its API paths failed, so
  the page was loaded in a headless browser and its network recorded. The widget bundle loaded and made
  **zero data requests** in a 20 s window, so no public ITF endpoint was discovered. Re-running during
  peak ITF hours, and past the cookie-consent gate, is the open thread.

## 2. Chosen source hierarchy

1. **ESPN site API** for ATP and WTA main tour and Grand Slam singles: the only reachable feed with a
   per-match state (`pre` / `in` / `post`), a stable schema, sub-second latency and a payload that covers
   a whole tournament in one request.
2. **Kalshi** may narrow a bracket a sports source already established. It can never create one.
   Exchange evidence alone caps confidence at C.
3. **Nothing else is wired in.** tennisexplorer remains a documented candidate for Challenger and ITF and
   was deliberately not implemented: it would require scraping a page whose structure is not a contract.

## 3. Coverage by tour and level

| level | source | status |
|---|---|---|
| ATP main tour | ESPN | solved, state transitions |
| WTA main tour | ESPN | solved, state transitions |
| Grand Slam singles | ESPN | solved (one request returned all 478 US Open matches with `Final`, `Retired`, `Walkover`, `In Progress` states) |
| WTA 125 / Challenger-level WTA | ESPN | partially present on the WTA board; observed binding live |
| Doubles | ESPN | **covered.** ESPN shapes a pair as `roster` (a dict with a combined name and an athletes array), not as an `athlete`; the adapter read it as a list and so produced no doubles rows at all. Fixed and tested: 147 doubles matches now parse from the ATP board, and a pair binds to a Kalshi-style team name at affinity 0.95. |
| ATP Challenger | none | **unsolved.** ESPN's tennis league index contains `atp` and `wta` only; `atp-challenger` returns HTTP 400. |
| ITF men / ITF women | none | **unsolved** |
| Qualifying | none | **unsolved** |

## 4. Actual-start timestamp semantics

ESPN publishes ISO 8601 with an explicit `Z`. Its `date` and `startDate` are **scheduled** times, proven
below, so the usable evidence is the per-match `status.type.state` transition, not any timestamp the feed
supplies. Naive timestamps are never read as local time; `_iso_utc` and `_epoch` are unit-tested against
DST offsets, epoch seconds and epoch milliseconds, and always return timezone-aware values.

## 5. Confidence hierarchy

| level | meaning | strict-eligible |
|---|---|---|
| A | an authoritative source states the actual start outright, or a claimed start is confirmed inside an independently observed bracket | yes |
| B | a timestamped state transition brackets the first ball within 300 s | yes |
| C | indirect: wide or one-sided bracket, score back-cast, exchange-only evidence, or a match bound to the feed by a bare surname | **no** |
| UNKNOWN | insufficient evidence | no |

Two deliberate conservatisms, both of which make strict pregame HARDER to reach:

* **Feed lag.** Every live-score feed lags reality, and it lags in the dangerous direction: a feed still
  showing "not started" after play began pushes the observed lower bound later than the true first ball,
  which would relabel post-start observations as strictly pregame. No source documents its latency, so
  the lower bound carries a recorded 120 s allowance.
* **Provider independence.** ESPN's ATP and WTA boards return the same combined event during a Grand
  Slam. Sources are merged by provider before agreement or contradiction is judged, so two endpoints from
  one provider are one witness.

## 6. Current first-ball mapping coverage

The poller runs continuously as a self-dispatching conductor (`tennis-firstball.yml`), fetching each
board once per pass and mapping it onto the LIVE open Kalshi universe (the freshest capture pass, not a
discovery snapshot that may be hours stale). Every request in every segment returned HTTP 200.

Mapping quality across the session, as three real defects were found and fixed:

| segment | MATCHED | WEAK | AMBIGUOUS | what was wrong |
|---|---|---|---|---|
| first | 0 | 144 | 120 | full-name bindings scored 0.7, so every ESPN binding was WEAK |
| after the affinity fix | 20 | 0 | 120 | a tournament board lists the same pair in several rounds, so name-only contests tied |
| after the time tie-break | 0 | 0 | 110 | one physical match is listed under several Kalshi event tickers, and the collision guard read those as several matches fighting over one feed row |
| after the physical-key fix | **110** | 0 | **0** | — |

`UNMATCHED` stays large by design: most of the Kalshi tennis universe is ITF and Challenger, which ESPN
provably does not carry.

### The three defects, and why they matter

All three were found by running the thing against live data, not by reasoning about it, and all three
failed in the SAFE direction: they refused bindings rather than inventing them. That is the behaviour a
fail-closed design is supposed to have, and it is also why the defects were visible at all.

1. **Full names scored as uncertainty.** The project's matcher was built for "Federer R." against
   "Roger Federer", where a missing initial is genuine doubt worth 0.7. Live feeds give full names on
   both sides, where a complete token match is the strongest evidence available. A bare surname still
   scores 0.7 and still maps WEAK.
2. **The same pair appears in several rounds.** A tournament board spans a fortnight. The tie-break is
   time and only time: among top-scoring candidates, the one scheduled nearest our own nominal is the
   current meeting. Equal names AND equal times is still a genuine collision and still refuses.
3. **One match, many Kalshi events.** Match winner, exact score, set spread and set winner each get
   their own event ticker for a single meeting on a single court. Our matches now carry a physical key
   (normalised player pair, date, discipline); several tickers sharing a key may all bind to one feed
   row. Two different physical matches claiming one row still collide.

## 7. Historical first-ball recovery

**None, and this is now a repeatable check.** `scripts/firstball/assess_historical_recovery.py` scans a
dated scoreboard for any field that could carry a real start. Against the saved ESPN payloads:

| payload | competitions | completed | starts differing from schedule | end times | verdict |
|---|---|---|---|---|---|
| ATP scoreboard | 625 | 620 | 0 | 0 | NOT_RECOVERABLE |
| WTA scoreboard | 775 | 758 | 0 | 0 | NOT_RECOVERABLE |

Across 1,378 completed matches, some certainly ran late. Zero differences means the field is a schedule.
Historical coverage was not forced.

## 8. Strict pregame observations recovered

**Zero, so far, and that is the correct number today.** All 236 existing ledger rows classify as
`START_UNKNOWN`: they were captured before first-ball polling existed, and §7 shows their starts cannot
be recovered. New observations become classifiable as the poller brackets matches going forward.

## 9. Executable-close coverage

Zero strict closes so far, for the same reason: a strict close requires A/B first-ball truth for that
match. The machinery is in place and tested — the close is the last executable quote strictly before the
**earliest possible** first ball, drawn from market records, orderbook tops and Kalshi bid/ask candles,
with `NO_EXECUTABLE_QUOTE` when none exists. Nothing is synthesised, and a scheduled-time close must be
asked for explicitly and is stamped `strict=False`.

## 10. CLV coverage

Zero strict CLV rows, consistent with §8 and §9. CLV v2 is built and unit-tested: `clv_executable`
(primary), `clv_ask_to_ask` and `clv_midpoint` kept separate, spread and depth at both ends, seconds from
entry and close to the first ball, model-market disagreement, data-quality grade, and fees computed per
contract at both ends and reported **separately**. CLV is an information and execution diagnostic and is
never netted against realised P/L.

## 11. Contradictions

Zero material contradictions to date. Only one provider is wired in, so cross-provider contradiction
cannot yet occur; the machinery is unit-tested with disjoint-bracket and disagreeing-timestamp cases,
both of which fail closed to `AMBIGUOUS` with both raw observations retained and no winner chosen.

## 12. Tests

**275 passing, 0 failing.** That includes 25 new adversarial first-ball tests: a match starting 47
minutes late, one starting early, a two-hour court delay, the ITF case where the nominal time falls after
the market closed, an observation one second after the first ball, a quote exactly at the first ball, a
walkover where no ball was ever struck, a market that stays open in play, malformed and duplicate feed
events, and first-ball truth recovered days later (the original observation stays byte-identical, the
hash chain holds, and only the derived classification moves, with a new derivation version).

Structural invariants are tested too: a scheduled time cannot be passed where a truth object is required,
a Kalshi close time never produces a strict close, a post-start entry can never produce a strict CLV row,
exchange evidence alone never reaches strict confidence, and one provider's two endpoints never count as
two witnesses.

## 13. Health-gate changes

* **TENNIS-6** prefers actual first-ball truth over the scheduled fallback wherever truth exists.
* **TENNIS-8** now includes first-ball coverage: an intact store hash chain, and at least 90% of watched
  matches *at levels with a wired source* bound to that source. Levels with no source are reported as
  counts, never averaged into a percentage where a structural gap could hide.
* **TENNIS-10** measures close coverage against **strict** first-ball-anchored closes only. A close cut
  off at `scheduled_start - margin` no longer counts. With no A/B truth yet it reports UNKNOWN, which is
  a failure for production purposes, by design.

No threshold was moved to accommodate any of this.

## 14. Live prospective proof

**The transition was captured on live data.** A US Open semifinal, scheduled hours earlier and delayed
behind a long preceding match, was held under watch in the pre-match state for over two hours and then
observed starting:

| reading | time (UTC) | source status |
|---|---|---|
| last pre-match | 2026-09-11T23:42:38 | `Scheduled` |
| first in-progress | 2026-09-11T23:46:39 | `In Progress` |

The full path ran: live-universe watchlist → live-score fetch → fail-closed mapping → immutable
observation → reconciliation → truth → publication to `tennis-data`, then classification, close, CLV and
horizons through settlement, then the health gates. 1,262 immutable observations were recorded across
pre-match, in-progress and finished readings, 110 markets bound at affinity 1.0 with zero ambiguity, and
the preceding semifinal was separately observed moving from in-progress to Final, which confirms the
whole state machine against live data.

**The bracket came out at confidence C, not B, and the reason is worth recording.** The raw gap was
240.6 s; with the 120 s feed-lag allowance the bracket is 360.6 s, which exceeds the 300 s ceiling for B
by 61 seconds. The cause was the polling cadence, and it is a design defect this run exposed: the tier
was chosen from the Kalshi nominal time, and a match whose nominal had passed two hours earlier fell
into the five-minute WARM tier. That is precisely backwards. A match we have SEEN still not started,
whose schedule has already been proven worthless, is the most urgent thing on the board.

Fixed: what a source last reported now outranks what the exchange scheduled. A watched match observed
pre-match and at or past its nominal time is polled at 60 s, one observed in progress drops to cold, and
a match with no nominal at all is polled hot rather than warm. On the same transition this would have
produced a bracket of roughly 60 to 120 s plus the allowance, comfortably inside B.

**So: the path is proven end to end on a real delayed match, and the first STRICT (A/B) truth is not yet
claimed.** No strict close or strict CLV row exists yet. The conductor keeps running with a cron
backstop, and every affected ledger row is reclassified automatically as truth arrives.

## 15. Unresolved blockers

1. **Challenger, ITF and qualifying have no first-ball source.** Biggest open gap, and the levels where
   Kalshi's nominal metadata is worst.
2. **The ITF's own feed was not cracked.** The provider is identified; the widget made no data requests
   during the probe window. Re-run during peak ITF hours and past the consent gate.
3. ~~Doubles coverage unverified.~~ **Resolved:** ESPN carries doubles under a `roster` shape the adapter misread. Fixed and tested; a pair binds to a Kalshi-style team name at affinity 0.95.
4. **Feed lag is assumed, not measured.** The 120 s allowance is a conservative placeholder; measuring
   ESPN's real latency against a second independent source would tighten every bracket. On the observed
   transition it was the difference between confidence B and C.
5. **Only one provider is wired in,** so cross-provider reconciliation is exercised only in tests.
6. **No strict CLV row exists yet.** Nothing is wrong; the coverage simply does not exist until matches
   are bracketed going forward.

## 16. Governance

Existing models are untouched: no tuning, no new features, no threshold optimisation, no strategy
promoted. The segmented scorecard schema records counts and coverage only, never performance by bucket.
The research verdict from the previous wave stands unchanged: Pinnacle beats the ensemble, the Kalshi
pregame quote beats it, and the walk-forward hybrid puts a negative weight on the model.

**REAL-MONEY AUTHORITY: OFF.**
