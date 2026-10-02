# Decision log (2026-09-11 overnight session, UTC)

| time | decision | why | alternative |
|---|---|---|---|
| 06:30 | Build inside the existing `nfl-edge-finder` repo as `tennis-edge-finder/` on the designated branch; reuse its read-only Kalshi client and publish pattern | sandbox cannot reach Kalshi or tennis sites; the repo's Actions runners can | separate local repo with no way to fetch data |
| 06:33 | Use the NFL project's full series-catalogue snapshot to design the taxonomy offline | 13,959-series catalogue already on `market-data` | wait for runner |
| 06:35 | Trigger workflows by pushing a trigger file; later self-dispatch for the capture chain | `workflow_dispatch`/`schedule` need the default branch | push to main (forbidden) |
| 06:46 | Fetch upstream data via codeload zip without git credentials | Actions token leaked into other-repo clones (`could not read Username`) | git clone |
| 07:06 | Discover live forks of the Sackmann repos with the GitHub search API (`fork:true`) and verify season files | upstream `tennis_atp`/`tennis_wta` 404 | hard-code a fork (stale) |
| 07:10 | Add TML-Database and the gmalbert mirror (tennis-data xlsx + TML challenger + odds merges) | tennis-data.co.uk returned 503 to every request | Kaggle (needs auth) |
| 07:15 | Exact DP scoring engine as the pricing core; Monte Carlo only for validation | exact, fast (ms per match), invariant by construction | pure simulation |
| 07:20 | Tag-based Kalshi tennis classification with title/prefix nets and explicit NOT_TENNIS (pickleball) | exchange's own taxonomy is authoritative; silent omission forbidden | regex only |
| 07:25 | Parse payoffs from `rules_primary` and cross-check ticker side codes and `floor_strike` | UI labels are not contracts | ticker-only parsing |
| 07:40 | Capture the GLOBAL trade tape filtered to tennis instead of per-ticker polling | one paginated request covers every tennis trade | per-market polling (10k requests) |
| 12:40 | gzip + shard capture streams; publisher skips > 95 MB | 163 MB candle file rejected every push for 5.7 h | LFS |
| 13:20 | Player ids are strings, one id system (Sackmann) for production ratings; TML rows kept with `id_system` | TML ids are alphanumeric and unlinked; mixed replay duplicated players | fuzzy id merge |
| 13:30 | Production Elo config K0 = 180 + surface pooling; ensemble = logit average with structural | best calibration on the tour-level Pinnacle test; ensemble best Brier | elo_plain (best all-level LL) |
| 13:40 | Kalshi backtest cutoff = min(nominal − 5 min, close − 7 h) | `occurrence_datetime` is not a start time for ITF/Challenger (it falls after close); first test leaked in-play prices | trust occurrence_datetime |
| 13:45 | Pregame policy in `run_tennis`: fresh capture universe, refuse ≤ 5 min to nominal start, flag ITF/Challenger as NOMINAL_UNRELIABLE and never actionable | no first-ball truth | price everything |
| 13:47 | Doubles priced with the singles-Elo baseline, grade capped C, unvalidated | coverage over silence; explicit uncertainty | exclude doubles |
| 13:50 | Report every model beside the market and state "no edge" | Pinnacle and Kalshi beat every model; hybrid weight on model negative | present model-only numbers |

## 2026-09-27 prospective-evidence harvest

| decision | why | alternative rejected |
|---|---|---|
| Score frozen candidates in a separate append-only layer (`data/research/candidate_evidence/`), never in the candidate JSON | the definition files are fingerprinted; an `evidence` list inside them invites edits next to the thresholds | writing into `evidence` |
| Report W3-001/002, EC-001/002/003 as UNSCORABLE_MISSING_HISTORICAL_FIELDS | the probability each rule decides on was never computed after its freeze; recomputing it now from today's artifacts would synthesise historical state | back-filling fair_v1 / market-conditioned predictions retrospectively |
| Do not use the dislocation scan's `model_fair` as the W3 probability | it is fair_v1 computed with `surface=None` on only the externally listed matches: a different number from a different population | treating it as a proxy |
| W4 freshness read literally: every venue contributing to the stored reference must publish a timestamp under 30 minutes old | "whose venue timestamp is under 30 minutes old" cannot be satisfied by a venue with no timestamp (Smarkets); mixed cases are excluded as ambiguous, and every reading was checked to reach the same status | counting untimestamped venues as fresh |
| Protocol binding: only STRICT_PREGAME rows are eligible for any pregame claim | `docs/PROSPECTIVE_RESEARCH_PROTOCOL.md` | using START_UNKNOWN rows for P&L |
| Trade tape: new window since the last one + queued backlog inside the SAME 250-page budget | the old cursor re-read ~12 minutes of tape every pass and skipped the unread older end for good | raising the page cap |
| Laver Cup: explicit family, parsed, not priced | the contract states no scoring format and none is configured | reusing the generic team-event format |

## 2026-09-30 ChatGPT-assisted handicapping lane

| decision | why | alternative rejected |
|---|---|---|
| A separate lane (`tennis_edge/assisted/`) whose unit is a person's recorded decision, beside the frozen experiments | the question is whether the repo's data helps a handicapper, not whether a model beats Kalshi; mixing the two would let thousands of model rows swamp a few dozen decisions | scoring ChatGPT decisions inside the candidate harvest |
| One write-once file per record, canonical JSONL compiled by RUN TENNIS | `publish_branch.py` copies a tree over the branch tip, so two jobs appending to one JSONL can overwrite each other's rows | a single shared append-only JSONL written by both the recorder and RUN TENNIS |
| `publish_branch.py --no-overwrite` for the recorder | a record that already exists on the branch must never be replaced, even by a race between two dispatches | trusting job concurrency (GitHub cancels queued runs of a group) |
| Only RUN TENNIS writes TRACK_START (`--write-track-start`) | one writer fixes the effective start; local and test runs cannot start the production track | writing it from whichever job runs first |
| Refuse decisions after any observed first ball (any confidence); admit made-before/recorded-after with a flag and exclude them from the headline | refusal on an indirect bound is the conservative direction; a late write-up is contamination risk, not a lost fact | refusing on scheduled start (Challenger/ITF times are unreliable) |
| Decisions must be recorded within 3 h and after the track start | prospective only; older write-ups are reconstructions | allowing back-dated decisions |
| All probabilities stored as P(ticker YES) | one Brier convention for every family and side | side-oriented probabilities |
| "Model prefers a side" = fee-adjusted executable edge > 0 on the decision's own quote | the pass-quality question is about apparent edges a taker could have bought | model-minus-mid |
| CEO answers are INSUFFICIENT_EVIDENCE below N = 30 and never "profitable" unless the 95% CI excludes zero; fixed bootstrap seed | no hindsight re-drawing, no early claims | reporting raw means as findings |
| Postmortems are hypothesis generation only | results must not tune a frozen model or create rules without their own pre-registered test | feeding postmortems into weights |


## 2026-10-01 Discrepancy sanity layer (assisted track) and the model-market discrepancy audit

| decision | why | alternative rejected |
|---|---|---|
| A large model-market gap is a QUESTION before it is an edge: bands NORMAL <10 / REVIEW 10-15 / HIGH_REVIEW 15-25 / EXTREME >=25 pp | the audit found most extreme gaps were fake: markets priced after Kalshi had settled, in-play prints, stale quotes | presenting raw model-minus-mid as edge |
| The layer only CLASSIFIES; no model probability, weight, selector or frozen file changes | the defect is mostly in data/coverage, and a model change needs its own pre-registered prospective test | shrinking model numbers toward the market in the slate |
| EXTREME defaults to DATA_WARNING; a BET needs all nine Part J conditions (incl. a FRESH executable price, external support or a documented reason, and ChatGPT's own why-market / why-model explanations) and is then only ELIGIBLE_FOR_HUMAN_REVIEW | an alarm until proven otherwise; never an automatic bet | allowing a BET with a warning |
| The recorder measures the gap with the REPOSITORY's model number when the slate has one | a model probability typed into the payload must not be able to shrink a gap past the layer | trusting the payload's model numbers for the gate |
| Ambiguous identity fails closed at HIGH_REVIEW and above; FAILED identity / orientation blocks a BET at any gap | a wrong player or side makes every number meaningless | fuzzy-matching names to resolve ambiguity |
| Quote freshness from the capture's own `captured_at` (FRESH <=10, AGING <=30, STALE >30 min) | conservative: an unchanged market is not proven fresh | treating the last capture pass time as an observation of every market |
| Decision schema v2 (the discrepancy group); v1 records keep validating against v1 | no decision existed under v1; versioning rather than editing a fixed schema | silently adding fields to v1 |
| Audit uses settlement timing and first-ball truth ONLY as hindsight diagnostics (`pregame_clean`), never as live inputs; tests prove outcomes change no ex-ante classification | diagnose without leaking | filtering live rows by later settlement |
| MODEL_CHANGE_RECOMMENDED uses two generic, pre-stated criteria (too extreme; no skill) | avoid post-hoc slicing; lower-tour "worse than Kalshi" slices are listed as hypotheses | recommending changes from any slice that looked bad |

## 2026-10-01 Post-settlement evidence correction; Gen-1 doubles suppressed from assisted handicapping

| decision | why | alternative rejected |
|---|---|---|
| A producer observation at or after Kalshi's recorded `settlement_ts` of its contract is EXCLUDED as `MARKET_SETTLED_BEFORE_OBSERVATION` | START_UNKNOWN rows (no first-ball source) let already-settled markets count as prospective evidence | inferring settlement from schedule, price or result |
| Exclude the contaminated FIRST observation; never promote the next one | the first observation is the pre-registered decision unit | skipping to the first clean observation |
| Repair by appending a newer EXCLUDED version | the store is append-only; history must stay auditable | rewriting or deleting the old INCLUDED line |
| `settled_at` attached only to contaminated observations | keeps the correction to exactly the rows it changes (no re-versioning of thousands of clean rows) | attaching it to every settled row |
| Gen-1 doubles probabilities removed from the assisted slate and from assisted decisions; doubles markets stay | the model failed a pre-stated no-skill test; a person may still handicap doubles manually | deleting doubles rows, or showing the number with a warning |
| A typed doubles model probability is refused, not silently dropped | the recorder refuses rather than repairs | discarding payload fields quietly |


## 2026-10-02 Start-time reconciliation; RUN TENNIS timed off the earliest credible first ball

| decision | why | alternative rejected |
|---|---|---|
| Authority: first-ball truth > live state > live schedule (ESPN `date`, `timeValid`) > court progression > Kalshi nominal (LOW) | the Kalshi nominal was a 06:00Z day placeholder for 27 matches that ESPN had at 03:05-06:05Z | trusting one `scheduled_start` field |
| A future scheduled time is never proof of pregame; a main-tour BET needs a live PRE reading <= 30 min old | fail closed: absence of evidence of play is not evidence of no play | allowing a BET until the nominal passes |
| Sources disagree, a MATERIAL contradiction, or now >= expected start without a pending reading in 180 s -> STATUS_AMBIGUOUS, BET blocked | ambiguity must not resolve to "pregame" | "latest reading wins" |
| Court progression only pulls an estimate earlier (fixed conservative remaining-time table) | bias the refresh early; a late estimate is the expensive error | a fitted duration model, or pushing estimates later |
| The first-ball watchlist unions discovery with the live capture board each segment | the daily discovery snapshot missed matches listed after it (RC1) | a second discovery run per day |
| A pregame-only truth (no upper bound) is not a first-ball bound | it says "not started at t"; reading it as "may have started" hid pregame matches | keeping the lower bound as a conservative cut-off |
| Refreshes are dispatched by the existing first-ball conductor: slate at earliest - 45 and - 10 min, a full RUN TENNIS only when producer rows are > 3 h old (cap 6/day), each once per window | the conductor already polls every 10 min; no new frequent workflow and no unnecessary rebuild | an every-10-minute RUN TENNIS cron |
| Decision schema v3 records the start status at decision; v1/v2 stay readable | versioning, not editing, a fixed schema | silently adding fields |
