# Wave 4: does an independent market find Kalshi's errors where our model could not?

**2026-09-12. `chmoses98/Tennis-Edge-Finder`. REAL-MONEY AUTHORITY: OFF.**

Wave 3 established that our own model's disagreement with Kalshi does not identify Kalshi's errors. Wave
4 asked whether a different market's disagreement would.

## The answer

**NOT ENOUGH DATA for the accuracy question, and a clear structural answer that makes it unlikely to
matter.**

1. **A usable free external venue exists.** Bovada's public tennis coupon is keyless, permitted by its
   robots.txt, timestamped per event, and carries a richer set of tennis derivatives than Kalshi does.
2. **It agrees with Kalshi almost exactly.** Across 260 observations of 21 matches, the de-vigged Bovada
   fair value and the Kalshi mid differed by a **median of 0.79c**; 5.4% of observations exceeded 2c and
   **none exceeded 5c**.
3. **The gap is a quarter of the cost of crossing it.** Kalshi's median spread is 2c and its taker fee
   peaks near 1.75c, so a round trip costs roughly 3c against a typical disagreement of under 1c.
   **Zero of 148 observations with a reference produced an external edge of 2c after fees. The best was
   −0.07c.**
4. **Our model is the odd one out, not Kalshi.** Of the 148 observations where all three views existed,
   the largest class by far was MODEL_LONE_OUTLIER (94), where the two venues agreed and only we
   disagreed. KALSHI_LONE_OUTLIER — the hypothesis — occurred **5 times**.
5. **No SHADOW_BET was produced, and none should have been.** 258 PASS, 2 WATCH, 0 SHADOW_BET.

The critical success question — *when an independent sharp market disagrees with Kalshi, does that
identify Kalshi errors better than our own model disagreement did?* — is answered **NOT ENOUGH DATA**,
because no observed contract has settled yet and 21 matches is not a sample. But the structural finding
is strong enough to lower expectations honestly: the two venues rarely disagree by more than the cost of
acting on the disagreement.

## Phase 0: what exists, and what we may not touch

Nine candidates probed on runners, robots.txt fetched for every host **before** any data URL. Full detail
in `docs/EXTERNAL_MARKET_SOURCES.md`; raw payloads on `tennis-data` under
`data/sources/external_odds_probe/`.

| source | verdict | why |
|---|---|---|
| **Bovada** | **ACCEPTED** | keyless, robots-permitted, 55 events, 6 match-scope families, per-event timestamps |
| Polymarket | REJECTED | lists tennis at every level Kalshi does — and does not trade it (below) |
| Smarkets | DEFERRED | a real exchange; reaching a price needs a multi-hop walk Phase 0 did not budget |
| ESPN | REJECTED | no odds block on the tennis scoreboard; `summary` 400s for tennis |
| The Odds API | REJECTED | 401 without a key; a key we do not have cannot run unattended |
| Betfair | REJECTED | 403 unauthenticated |
| **Pinnacle** | REJECTED | **451 Unavailable For Legal Reasons.** The mandate said not to assume it. It is not there. |

**Polymarket deserves its own line** because it looked perfect and was not. 247 open tennis events, 235 of
them individual matches, ATP through ITF and doubles, 2,120 markets flagged "accepting orders". Of 120
CLOB order books fetched: **one** had a two-sided price, quoting 0.47/0.53 with identical depth on both
sides and a timestamp shared with every other market on the venue. A seeded book, not a market. Worth
re-probing later — the listings exist, so liquidity could arrive.

**No sharp reference was found.** Bovada is a recreational book. Every conclusion below is limited by
that, and the code says so on every row.

## Coverage

| measure | value |
|---|---|
| Bovada events per snapshot | 55 (49 with two named competitors) |
| levels | WTA tour (largest share), WTA 125K, ATP Challenger, ITF men's and women's, Grand Slam, exhibitions |
| doubles | present, and **refused** — our mapping needs four identities and the singles registry carries two |
| market families parsed | MATCH_WINNER, GAME_SPREAD, TOTAL_GAMES, TOTAL_SETS, EXACT_SET_SCORE, SET_SPREAD |
| observations written per snapshot | 734 rows, 199 de-vigged complete markets |
| external events mapped to canonical matches | **36 / 49 (73.5%)**; refusals are 9 unmapped players (mostly UTR exhibition) and 4 doubles |
| Kalshi events mapped | 123 / 138 (89.1%) |
| **matches present on BOTH venues** | **21–32 per snapshot** |
| Kalshi board coverage of the overlap | ~17% of mapped Kalshi matches have a Bovada counterpart |

Bovada's board is a fraction of Kalshi's, and the overlap is where all Wave 4 evidence lives.

## Freshness, and why half the overlap is excluded

Bovada stamps each event with `lastModified`. Median age at capture was ~8 minutes, but for matches hours
away it runs to hours. Under a 30-minute bound, **148 of 260 observations kept a reference and 112 were
excluded as stale.**

That bound could be argued with: an unchanged bookmaker line is still the offered line. So the whole
distribution was recomputed without it:

| set | n | median abs gap | p90 | max | share >2c | share >5c |
|---|---|---|---|---|---|---|
| fresh only (30-min bound) | 80 | 0.0079 | 0.0143 | 0.0247 | 2.5% | **0%** |
| every row with a Bovada price | 148 | 0.0085 | 0.0247 | 0.0409 | 14.2% | **0%** |
| only the rows the gate excluded | 68 | 0.0095 | 0.0359 | 0.0409 | 27.9% | **0%** |

The stale rows show the *biggest* apparent dislocations — which is what a staleness artefact looks like,
and is the argument for keeping the gate. The conclusion survives either way: **no observation of either
set exceeded 5c**, and the largest gap anywhere came from the stalest data.

## The dislocation distribution

260 observations, 21 matches, 42 contracts, 19:32Z to 21:03Z.

| triangulation | n | median ext − Kalshi | median edge after fees | share of edges ≥2c |
|---|---|---|---|---|
| all with a reference | 148 | −0.0014 | −0.0312 | **0** |
| MODEL_LONE_OUTLIER | 94 | −0.0007 | −0.0271 | 0 |
| MARKETS_AGREE | 46 | −0.0052 | −0.0334 | 0 |
| KALSHI_LONE_OUTLIER | 5 | −0.0248 | −0.0498 | 0 |
| ALL_THREE_DISAGREE | 3 | −0.0208 | −0.0457 | 0 |

**Kalshi is the lone outlier in 5 of 148 observations (3.4%)** — and in those the external reference sat
*below* the Kalshi price, so the tradeable side was the other one, and it still did not clear the fee.

The MODEL_LONE_OUTLIER count is the second finding of this wave, and it corroborates Wave 3 from a new
direction. In 94 of 148 observations two independent venues agreed with each other and our model
disagreed with both. When two venues price a match at 11% and we say 49%, the venues are not the ones
who are wrong.

## Did Kalshi move toward the external reference?

The fast test, from the ledger itself: the scan re-observes every contract each pass, so a follow-up
exists within twenty minutes without waiting for settlement.

| subset | n | mean move toward | 95% CI | share that moved toward |
|---|---|---|---|---|
| all with a reference | 88 | +0.0004 | [−0.0005, +0.0014] | 20.4% |
| MARKETS_AGREE | 28 | +0.0014 | [−0.0004, +0.0038] | 25.0% |
| MODEL_LONE_OUTLIER | 56 | −0.0004 | [−0.0013, +0.0006] | 14.3% |
| KALSHI_LONE_OUTLIER | 1 | 0.0000 | — | 0% |

Nothing. Kalshi does not drift toward Bovada over twenty minutes, and the one Kalshi-lone-outlier with a
follow-up did not move at all. At n=1 that is an anecdote, not a result.

## Settlement economics

**None yet.** No contract observed in this window had settled by the time of writing.

A defect was found while building this: the settlement lookup originally read the capture stream, and
30,961 captured quote rows over an evening contained **zero** results — because the capture fetches the
ACTIVE board, so a settled market simply stops appearing rather than being rewritten with its outcome.
Settlements live in the discovery snapshot's `historical_markets`, refreshed daily. The scorecard now
reads that, so the accuracy comparison will populate on the next daily discovery rather than silently
reporting nothing forever.

## What was built

| piece | what it does |
|---|---|
| `tennis_edge/external_market/schema.py` | the immutable, hash-chained observation; refuses a de-vigged probability from fewer than two observed sides, and never infers a timestamp |
| `devig.py` | proportional, power and Shin, with the disagreement between them reported |
| `consensus.py` | median across declared independent groups; two-way staleness bounds; Kalshi-derived sources inadmissible |
| `mapping.py` | both venues resolved through the SAME registry; doubles, shared names and half-identifications all refused |
| `dislocation.py` | triangulation, the frozen scan policy, the append-only ledger |
| `bovada.py` | the one accepted source; whole-match markets only, live and first-set skipped |
| `scripts/external/capture_and_scan.py` | one pass, wired into the capture conductor |
| `scripts/external/dislocation_scorecard.py` | monitoring by day, week, tour and family |

Docs: `docs/EXTERNAL_MARKET_SOURCES.md`, `docs/EXTERNAL_MARKET_PROTOCOL.md`. Tests: 37 new, 377 total.

Integrity: 148 dislocation rows and 3,570 external observations published, **zero chain problems** on
either store.

## Discipline

`fair_v1`, `gen2_dyn_hier_sr_v1` and `selector_v1` were frozen for this wave and a test asserts their
version strings. Nothing was retuned. The Wave 2 and Wave 3 candidates were not touched, and a test
asserts all six are still on file.

One integrity slip, found and fixed: a sandbox dry run left a scan summary in `data/research/external/`,
main carried it, and the runner republished it to `tennis-data` alongside real captures. Evidence must
travel one way — captured on a runner, published to the data branch — so the directory is now ignored in
main.

## Wave 4 candidate: one, and it is a pre-registration

**W4-2026-001-KALSHI-LONE-OUTLIER**, PROSPECTIVE_PENDING, minimum N 200.

Discovery did **not** support it: 5 instances, none clearing 2c after fees. It is frozen anyway, and the
distinction matters. The infrastructure can now detect a Kalshi-lone-outlier, so the rule, the threshold
and the pass conditions are written down *before* instances accumulate. Without that, a future wave with
a handful of instances would be choosing its threshold after seeing the outcomes — which is exactly what
Wave 3's R1 did before it failed its holdout.

Its own strongest opposing reason is that the premise looks weak before the test begins: the venues agree
to within a median of 0.8c, never differ by more than 4.1c even on stale data, and the round trip costs
about 3c.

## Remaining blockers

1. **No sharp external reference.** Bovada is recreational. Smarkets is a real exchange and is the single
   highest-value item left anywhere in this project's backlog.
2. **One witness.** Every reference this system can build comes from one independent group, so the
   median-across-groups aggregation is currently a median of one.
3. **Overlap.** Bovada covers a fraction of Kalshi's board; roughly 17% of mapped Kalshi matches have a
   counterpart.
4. **The cost wall.** A 2c spread plus a ~1.75c fee against a sub-1c typical disagreement. This is the
   binding constraint on the entire external hypothesis, and no amount of data collection changes it.
5. **Strict CLV is 6 rows deep** and every one predates this wave's dislocations.
6. **WTA serve statistics still stop at 2026-04-27.**

## The recommended next state

Per the mandate's own instruction for this case: **FREEZE, COLLECT PROSPECTIVE DATA, WAIT.** The capture
runs unattended every ten minutes, the ledger is append-only, the candidate's goalposts are fixed, and
the accuracy comparison will populate itself once the daily discovery brings settlements in. Nothing
here argues for another model.

**REAL-MONEY AUTHORITY: OFF.**
