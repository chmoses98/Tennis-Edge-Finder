# Wave 5: can a real exchange find what a book and a model could not?

**2026-09-13. `chmoses98/Tennis-Edge-Finder`. REAL-MONEY AUTHORITY: OFF.**

Wave 4 left one lead: Smarkets is a genuine exchange, reachable, and reaching a price needed a traversal
Phase 0 had not completed. This wave completed it.

## Strategic state: **B — accessible, integrated, and not useful for execution**

Smarkets is everything Wave 4 hoped: a real exchange, keyless, no authentication anywhere on the path,
162 upcoming tennis matches, a match-winner market on every one, derivative coverage richer than Kalshi's,
and 89% of contracts quoting both sides with real depth.

And it agrees with Kalshi more closely than the recreational book does.

| gap against the Kalshi mid | n | median | p90 | p95 | max | >2c | >3c | >5c | >10c |
|---|---|---|---|---|---|---|---|---|---|
| **Smarkets (exchange midpoint)** | 175 | **0.86c** | 1.94c | 2.36c | 7.99c | 9.1% | 4.6% | 1.1% | **0%** |
| Bovada (sportsbook, de-vigged) | 778 | 0.98c | 2.98c | 3.20c | 4.92c | 23.1% | 10.0% | **0%** | **0%** |
| Bovada against Smarkets | 90 | 1.31c | 2.73c | — | 4.35c | — | — | — | — |

The more informed venue is the one that agrees with Kalshi more. That is the strongest form the negative
finding could take, and it is the answer to the question this wave was built to ask.

## The traversal (Phase 0)

The tennis tree is real and useless for capture: **Tennis (102016) → 19 category nodes → 2,626 tournament
nodes → round nodes → matches**, every node down to the match typed `generic` and carrying no date.
Walking it to find today's tennis costs thousands of requests.

One query skips all of it:

```
GET /v3/events/?type=tennis_match&state=upcoming&limit=100   (+ pagination_last_id)
GET /v3/events/{event_ids}/markets/
GET /v3/markets/{market_ids}/contracts/
GET /v3/markets/{market_ids}/quotes/                 <- the order book
GET /v3/markets/{market_ids}/last_executed_prices/   <- what traded, with a timestamp
```

`type=tennis_match` appears nowhere in the tree the walk returns, and the global query accepts it. Recorded
in `smarkets.py:TRAVERSAL` and asserted by a test, because rediscovering it would cost another wave.

**Authentication: none.** Every endpoint answered an unauthenticated GET. `api.smarkets.com` serves no
robots.txt (404) and `smarkets.com`'s does not disallow these paths. No 401, no 403, nothing bypassed.

## Is the price real? (Phase 1)

Yes, and that is why the spread matters.

| | value |
|---|---|
| contracts with a book (probe) | 242 |
| two-sided | **215 (88.8%)** — live scan: 299 of 312 (95.8%) |
| one-sided / empty | 4 / 23 |
| depth | size on both sides of every two-sided contract |
| **median match-winner spread** | **10.3c** (p25 9.7c) — against Kalshi's **2c** |
| last traded price | present, with a per-trade timestamp |
| **order-book timestamp** | **none** |

A representative book: 0.3472 / 0.4348 one side, 0.5495 / 0.6536 the other.

Two consequences, both enforced in code rather than noted:

* **The midpoint is an opinion, not an executable price.** Ten cents of book puts five cents of
  uncertainty on the midpoint — larger than every cross-venue gap this project has ever measured. A 6c
  spread bound keeps wide-book rows out of the reference while still storing them; it applies to exchange
  rows only, since a sportsbook's overround is a different quantity from a book's width.
* **`source_timestamp` is None, honestly.** The venue stamps no time on the book. It is not quietly set
  to the capture time; the last TRADED price carries a real timestamp and is kept beside the quote as the
  different fact it is.

## Coverage (Phase 2)

| | Smarkets |
|---|---|
| upcoming tennis matches | 162 (105 within 24h, 57 within 7 days) |
| doubles | 6 (refused by mapping — four identities needed) |
| markets over the 120 soonest matches | 715 |
| **Match winner** | **120 — one on every match priced** |
| derivatives | Set 1 winner 81, Correct score Set 1 68, set betting, exact sets, game spreads, over/under 20.5–23.0 |
| families we consume | MATCH_WINNER, TOTAL_GAMES, GAME_SPREAD, EXACT_SET_SCORE, TOTAL_SETS |
| families we deliberately skip | set-scoped and in-play markets — they price a different question than a match-scope Kalshi contract |

The category tree names ATP, WTA, Challenger, ITF Men, ITF Women, WTA 125K, Davis Cup and Fed Cup, but
the match nodes do not carry their category, so per-level counts are not available from the direct query.
Naming a level would require the tree walk this wave rejected on cost.

## Mapping (Phase 3)

The existing registry, unchanged, with no new fuzzy matcher.

| venue | mapped | refused |
|---|---|---|
| Smarkets | **69 / 80 (86.3%)** | 10 unmapped players, 1 doubles |
| Bovada | 98 / 116 (84.5%) | 6 unmapped players, 12 doubles |
| Kalshi | 94 matches | — |
| **matches on Kalshi and at least one external venue** | **69** | |
| **observations with BOTH external venues quoting** | **151** | |

Smarkets names no tour, so both are tried and a pair that resolves in **both** is recorded as an ambiguity
rather than resolved by preference.

## The cost-aware answer (Phase 7)

Against a Kalshi round trip of roughly 3c — a 2c spread plus a taker fee peaking near 1.75c:

* **no observation of either venue exceeded a 10c gap**;
* one Smarkets observation exceeded 5c (1.1%), and it is explained below;
* across 804 ledger rows, **14 observations showed a single-venue after-fee edge of 2c or more, spread
  over exactly 2 distinct matches** — 13 of the 14 are the same Bovada row re-observed pass after pass on
  an unchanged line.

The one Smarkets case is the instructive one. Kalshi 0.57 / 0.58; Smarkets midpoint 0.6549; apparent edge
+5.5c. Its book is ten cents wide, so its executable ask sits near 0.70 — **above** the Kalshi price, not
below it. There is no trade there in either direction. It is a wide-book midpoint compared against a tight
one, which is exactly the artefact the spread bound exists to refuse.

## Triangulation across three venues (Phase 6)

Over 804 ledger rows (361 with a reference):

| class | n | median ext − Kalshi | share >2c | share of edges ≥2c |
|---|---|---|---|---|
| MODEL_LONE_OUTLIER | 260 | −0.0004 | 0% | 0 |
| MARKETS_AGREE | 65 | −0.0037 | 0% | 0 |
| KALSHI_LONE_OUTLIER | 20 | −0.0210 | 100% | 0 |
| ALL_THREE_DISAGREE | 16 | −0.0207 | 100% | 0 |

MODEL_LONE_OUTLIER remains the dominant class: two independent venues agreeing while our frozen model
disagrees with both. Wave 4 found this with one venue; a second, and a sharper one, says the same thing.

One monitoring line worth flagging **as a curiosity, not a result**: of 11 KALSHI_LONE_OUTLIER rows with a
follow-up observation ~30 minutes later, Kalshi moved toward the external reference by a mean of +0.55c,
interval [+0.23c, +0.91c]. Eleven observations of a handful of matches on one evening is an anecdote with
an interval attached. It is what `W4-2026-001-KALSHI-LONE-OUTLIER` was frozen to test, and this is not
that test.

## What was built (Phases 4, 5, 9)

* `tennis_edge/external_market/smarkets.py` — the adapter, with the traversal recorded in code.
* Smarkets registered as its own witness group (`smarkets`, kind EXCHANGE), separate from `bovada`. The
  consensus can now be a median across two independent groups; Kalshi and our model are in neither.
* A 6c exchange-spread bound in the consensus, with `excluded_wide_book` counted on every reference.
* The scan indexes both venues **on the canonical player**, so a side is matched by who is playing rather
  than by how a venue spells them.
* Autonomous capture: **enabled.** Both venues are fetched every conductor pass (~10 minutes), spaced and
  bounded; Bovada was not replaced.
* 15 new tests (389 total), covering the price scale, the family map, the exchange midpoint, the missing
  book timestamp, one-sided and empty books, the spread bound, group separation, and the traversal itself.

## Phases deliberately not acted on

**Phase 8**: no new candidate. Nothing here is a qualitatively strong pattern; the finding is negative and
`W4-2026-001` already covers the Kalshi-lone-outlier hypothesis, which now has a second venue feeding it.
**Phase 11**: Gen-1, Gen-2, `fair_v1`, `selector_v1` and all seven frozen candidates are untouched; a test
asserts their version strings and the candidate list.

## Where the project stands

| | |
|---|---|
| strict CLV rows | **238** (mean strict executable CLV −9.95c, midpoint +0.14c) |
| confidence-B first-ball truths | **48** |
| frozen candidates | 7, all PROSPECTIVE_PENDING or DISCOVERY_ONLY, all with **0** prospective evidence |
| external dislocation ledger | 804 rows, 92 matches, chain-verified |

## Conclusion

Every independent line of attack has now returned the same answer from a different direction. Wave 3: our
model's disagreement does not identify Kalshi's errors. Wave 4: a recreational book's disagreement is
smaller than the cost of acting on it. Wave 5: a genuine exchange agrees with Kalshi *more* closely still,
and its own book is five times wider than Kalshi's. The CLV ledger adds that our entries have no timing
edge either.

Kalshi tennis is, on this evidence, the tightest and best-informed venue available to us.

**The correct next state is the one the mandate names for this case: FREEZE, COLLECT, WAIT.** The capture
runs unattended on both venues, the ledgers are append-only, the candidates' goalposts are fixed, and the
accuracy comparison populates itself as settlements arrive.

**REAL-MONEY AUTHORITY: OFF.**
