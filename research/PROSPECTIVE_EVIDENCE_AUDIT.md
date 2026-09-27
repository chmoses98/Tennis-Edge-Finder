# Prospective evidence audit (2026-09-27)

**Question.** For each of the seven frozen candidates: did the fields its frozen inclusion rule needs
exist at the moment each post-freeze observation was captured, in an append-only record? If a field did
not exist then, the rows that needed it are UNSCORABLE. Nothing is reconstructed.

**Evidence snapshot.** `tennis-data` at `6344965` (2026-09-27 18:54 UTC). Code: `main` at `625bc55` plus
this change. Candidate definitions: byte-identical on `main` and `tennis-data`; every stored fingerprint
re-verified by `tennis_edge.confirmation.sources.load_candidates`. None of them was written.

**Field classes.**

| class | meaning |
|---|---|
| PRESERVED_AT_CAPTURE | on the immutable row, written when the observation was captured |
| DERIVABLE_FROM_IMMUTABLE_CAPTURE | a deterministic function of immutable captured rows only (no model re-run, no new artifact) |
| LATER_TRUTH_ATTACHMENT_ALLOWED | truth that can only exist after the event (settlement, first ball, the close); attached in a separate layer |
| NOT_AVAILABLE | never captured after the freeze |
| AMBIGUOUS | captured somewhere, but not on the same row, instant or model input as the rule requires |

The same table is machine-readable in `tennis_edge/confirmation/candidates.py::FIELD_AUDIT` and is
embedded in every `research/candidate_confirmation/<id>.json`.

## The prospective streams that actually exist

| stream (on `tennis-data`) | produced by | model / version | runs after 2026-09-12 | append-only |
|---|---|---|---|---|
| `research/ledger/*.jsonl` | `scripts/run_tennis.py` (4x daily) | `elo_surface_k_lo+sr_v0.1` (Gen-1 Elo + SR ensemble, DP-priced derivatives); doubles `doubles_baseline_prior_v0` | yes, 12,372 rows | yes, hash-chained (TENNIS-12 PASS) |
| `research/opportunities/*.jsonl` | `scripts/ops/shadow_board.py` | `gen2_dyn_hier_sr_v1+fair_v1` + `selector_v1` | **no**: one run, 2026-09-12 17:13-17:14, 502 rows; scheduled by no workflow | yes |
| `research/external/dislocations/*.jsonl` | `scripts/external/capture_and_scan.py` (every capture pass) | `external_v1`; model witness = fair_v1 Gen-2 blend computed with `surface=None` | yes, 15,938 rows from 2026-09-12 19:27 | yes, hash-chained |
| `research/external/market/*.jsonl` | same | raw Bovada / Smarkets observations with the venue's own timestamp | yes | yes, hash-chained |
| `kalshi/capture/<day>/*.{quotes,books,candles,settlements,trades}` | `scripts/kalshi/capture_tennis.py` (every ~10 min) | exchange data only | yes, 1,689 passes | yes (per-pass files) |
| `firstball/store` | `tennis-firstball.yml` | first-ball observations and truths | yes, 1,031 truths | yes, hash-chained |
| `research/settlements/*.jsonl`, `research/clv/<run>.jsonl` | `scripts/ops/settle_ledger.py` | derived; never edits a ledger row | yes | settlements append-only; CLV one file per run |
| market-conditioned (`market_conditioned_v1`) predictions | -- | -- | **never produced prospectively** | -- |

Common sources for every candidate:

* **settlement:** the capture conductor's hourly `status=settled` sweep (`kalshi/capture/*/*.settlements.jsonl.gz`,
  the exchange's own `result` and `settlement_value_dollars`), falling back to the `settled` block of the
  latest discovery snapshot. 0 conflicts between the two and the settle job's table.
* **strict CLV:** `canonical_close` over the capture quote timeline (market records + order books + bid/ask
  candles) cut at the first-ball LOWER bound of A/B truth; `clv_record` (engine v2). Entry = the observation's
  own captured bid/ask.
* **first-ball truth / timing:** `firstball/store` latest truth per Kalshi event ticker; `classify()`;
  C never promoted.
* **identity:** the Kalshi event ticker (exact match, as the settle job does) and the external layer's
  `physical_match_id` from the one player registry. Known gap: truth is keyed under the events the
  first-ball watchlist watches, so 671 ledger rows (588 of them TOTAL_GAMES) whose physical match has A/B
  truth under a sibling series never get a strict close. Not changed here; see the report.
* **fee:** `tennis_edge.pricing.fees.taker_fee` (quadratic, M=1) at the executable price.
* **depth:** captured order books (`orderbook_fp`) and the market record's `yes_ask_size_fp`.

## Per candidate

### W4-2026-001-KALSHI-LONE-OUTLIER -- scorable

* frozen 2026-09-12T21:09:38.644348Z; confirmation_start identical.
* rule: MATCH_WINNER; reference from >= 1 admissible external group whose **venue timestamp is under 30
  minutes old**; triangulation KALSHI_LONE_OUTLIER; external fair - executable ask - taker fee >= 0.02;
  Kalshi two-sided, quote < 1 hour old, spread <= 6c, displayed size >= 1; FIRST qualifying observation per
  contract only.

| field | source | class |
|---|---|---|
| family, triangulation, external fair, external edge, model witness | dislocation row | PRESERVED_AT_CAPTURE |
| Kalshi bid/ask/mid/spread/size/quote age, fee | dislocation row | PRESERVED_AT_CAPTURE |
| venue timestamp of each contributing venue | `research/external/market` row with the same scan instant, venue and de-vigged value | DERIVABLE_FROM_IMMUTABLE_CAPTURE |
| first qualifying observation per contract | dislocation ledger order | DERIVABLE_FROM_IMMUTABLE_CAPTURE |
| first-ball timing (A/B), strict close, settlement | first-ball store, capture quotes/books/candles, capture settlements | LATER_TRUTH_ATTACHMENT_ALLOWED |

Two readings had to be made explicit rather than assumed:

1. **Freshness.** Smarkets publishes no venue timestamp. A venue with no timestamp cannot satisfy "whose
   venue timestamp is under 30 minutes old", so a reference resting only on Smarkets is
   `EXTERNAL_FRESHNESS_UNVERIFIABLE`, and one mixing a timestamped and an untimestamped venue is
   `EXTERNAL_FRESHNESS_AMBIGUOUS`; both are excluded. Of the 86 rows passing every other gate (which are
   exactly the 86 rows the scanner flagged SHADOW_BET), 18 are VERIFIED_FRESH, 58 UNVERIFIABLE, 6 MIXED
   and 4 UNRESOLVED (the observation behind the stored reference could not be matched uniquely).
   The status does not depend on this reading: taking the scanner's own flag instead gives 28 first
   observations, of which 3 are STRICT_PREGAME -- still far below 200.
2. **Timing.** The protocol binds strict pregame research to STRICT_PREGAME rows only
   (`docs/PROSPECTIVE_RESEARCH_PROTOCOL.md`), and W4's hypothesis is about the price before the first ball.
   A first qualifying observation that is START_UNKNOWN, POST_START or AMBIGUOUS is excluded, and a
   contract whose first qualifying observation is excluded does NOT fall forward to a later observation.

### EC-2026-004-COHERENCE-EXECUTABLE -- scorable (DISCOVERY_ONLY)

* frozen 2026-09-12T06:30Z. Rule: any structure `tennis_edge.pricing.coherence` detects on executable
  bid/ask with order-book depth on every leg and executable margin > 0 after taker fees; after-fee
  condition adds minimum leg size >= 10.

| field | source | class |
|---|---|---|
| executable bid/ask per leg | captured order book (`orderbook_fp`), YES ask = 1 - best NO bid | PRESERVED_AT_CAPTURE |
| depth per leg | same book, same instant | PRESERVED_AT_CAPTURE |
| contract semantics | `parse_market` on the captured market record's rules text | DERIVABLE_FROM_IMMUTABLE_CAPTURE |
| taker fee per leg | fee schedule at each leg's price | DERIVABLE_FROM_IMMUTABLE_CAPTURE |

**Defect found and fixed.** Every captured book is in Kalshi's current `orderbook_fp` shape (prices in
dollars). The coherence scan and the CLV quote builder only read the legacy `orderbook.yes/no` cent
keys, so neither ever saw a book: the discovery-era "size-verified: 0" result had no sizes to verify
with, and the close timeline had no book quotes. `tennis_edge.ledger.quotes.book_top` reads both shapes.
The price-only discovery result was real and is unaffected. Books are only captured for match-scope
markets within 6 hours of their nominal start, so this stream sees the near-start board.

### EC-2026-003-GEN2-MODERATE-EVIDENCE -- UNSCORABLE

* frozen 2026-09-12T06:30Z. Rule: singles, ATP/WTA, MATCH_WINNER, thinner player's Gen-2 serve points in
  [1,000, 20,000]; Gen-2 Brier <= Gen-1 Elo - 0.0015 (paired CI), not worse than market by > 0.005, strict
  executable CLV > 0, after-fee EV > 0.

| field | source | class |
|---|---|---|
| Gen-2 probability at decision | shadow board (one run, 502 rows); dislocation `model_fair` (no surface) | AMBIGUOUS |
| thinner player's Gen-2 serve points | shadow board `serve_evidence_points` (same single run) | AMBIGUOUS |
| Gen-1 Elo probability at the same decision | ledger `models.ELO` -- never on the same row, instant or artifact as a Gen-2 probability | AMBIGUOUS |
| Kalshi executable ask/mid | ledger, opportunities, dislocations | PRESERVED_AT_CAPTURE |
| timing, strict close, settlement | as above | LATER_TRUTH_ATTACHMENT_ALLOWED |

No single preserved row carries a Gen-2 probability, a Gen-1 probability and Gen-2 serve evidence for
the same decision. Pairing a ledger row with a shadow-board or dislocation row from a different instant,
different rating artifact (processed ratings vs walk-forward as-of states) and, for dislocations, a
different input set (no surface), would construct a comparison nobody made. The only rows with Gen-2
serve evidence are 502 (both sides of ~250 contracts, one afternoon): below the frozen 1,000 under any
pairing.

### W3-2026-001-ABSTAIN-ITF and W3-2026-002-NONITF-POSITIVE-EDGE -- UNSCORABLE

* frozen 2026-09-12T17:24:04.826616Z. Model `gen2_dyn_hier_sr_v1+fair_v1+selector_v1`.

| field | source | class |
|---|---|---|
| MATCH_WINNER, level | every stream; level from the series ticker | PRESERVED_AT_CAPTURE |
| frozen decision probability (fair_v1 with surface) | `scripts/ops/shadow_board.py` only | NOT_AVAILABLE after the freeze |
| fee-adjusted edge at the ask | needs the probability above | NOT_AVAILABLE |
| selector_v1 qualification checklist (W3-002) | shadow board only | NOT_AVAILABLE |
| Kalshi mid on the selected rows (W3-002 accuracy condition) | same rows | NOT_AVAILABLE |

The shadow board last ran at 17:14:41Z on 2026-09-12, **eleven minutes before these candidates were
frozen**, and no workflow runs it. The two streams that do continue are not the frozen model: the ledger
is Gen-1, and the dislocation scan's `model_fair` is fair_v1 computed with `surface=None`, on the subset of
matches an external venue also lists. Substituting either would be scoring a proxy rule.

### EC-2026-001-MKTCOND-EXACT-SCORE and EC-2026-002-MKTCOND-GAME-SPREAD -- UNSCORABLE

* frozen 2026-09-12T06:30Z. Model `market_conditioned_v1 + gen2_dyn_hier_sr_v1`.

| field | source | class |
|---|---|---|
| listed contract, family, line | capture market records | PRESERVED_AT_CAPTURE |
| two-sided match-winner quote to de-vig | capture market records | PRESERVED_AT_CAPTURE |
| market-conditioned lane prediction | nowhere: only `scripts/research/market_conditioned_study.py` (retrospective) | NOT_AVAILABLE |
| fundamental (Gen-2) lane prediction | nowhere prospective; ledger derivatives are Gen-1 DP prices | NOT_AVAILABLE |
| final exact set score (EC-001) | Kalshi exact-score settlement | LATER_TRUTH_ATTACHMENT_ALLOWED |
| completed-match game differential (EC-002) | no games-level sports truth is captured | NOT_AVAILABLE |

Listing volume would also have blocked both: after the freeze Kalshi listed 382 exact-score contracts on
95 physical matches, and 1,004 spread/total contracts on 254 matches, against minimums of 400 (both
metrics are per match).

## Settlement audit (Phase 9)

The health report's "no settled predictions yet" was **F: health querying the wrong layer**. The settle
job had written 12,330 unique settled rows (yes 5,939 / no 6,127 / scalar 264) covering 12,328 of the
12,372 ledger rows, with 0 duplicate prediction ids and 0 conflicts with the capture settlement stream.
The other 2 settlement rows belong to a 2026-09-11 13:59Z run whose prediction ids are not in the ledger
(the pre-migration afternoon); they are reported, not deleted. Of the 44 unsettled ledger rows, 18 had
been settled by the exchange after the last settle run (17:16Z; swept 18:14Z) and 26 were still open.
The health step called `run_all()` with no settlement inputs, so TENNIS-8/9/10 were never evaluated.
`tennis_edge.health.gates.settlement_stats` now reads the settle job's tables directly. No settlement row
was rewritten and no backfill was needed.

Two further findings, reported rather than hidden:

* Every settled row's "sports truth" is Kalshi's own result copied (`source: kalshi_result`); no
  independent results feed reaches the settle job. TENNIS-8 now fails on that instead of hiding behind
  UNKNOWN.
* The settle job embeds a copy of the CLV record computed at settlement time; first-ball truth that
  arrives later updates `research/clv/<run>.jsonl` but not that copy, so `settlements/SCORECARD.md`'s
  strict CLV line can lag. The confirmation layer always recomputes from the latest truth.

## Operational defects (Phase 10)

* **Laver Cup.** `KXLAVERCUPMATCH` / `KXLAVERCUPDOUBLESMATCH` are binary per rubber, singles and doubles,
  resolved after a ball is played, walkover to a fair price. Mapped to an explicit
  `TEAM_EVENT_MATCH_WINNER` family: parsed (competitors, side, competition), never priced, because neither
  the contract nor `config/formats.json` states the scoring format.
* **Trade tape.** All 1,689 passes truncated at 250 pages. The cursor jumped to the oldest scanned trade,
  so each pass re-read ~12 minutes of already-scanned tape (median 28 minutes of tape read per ~16-minute
  cadence) and 54 windows totalling ~2.75 hours were never read. Replaced by a new-window + queued-backlog
  scan inside the same 250-page budget (`tennis_edge/kalshi/trade_tape.py`). No strict CLV or candidate uses
  the trade tape (trades are not quotes), so no evidence above depended on it.
* **TENNIS-6.** 330 ledger rows were generated after the actual first ball (297 POST_START, 33 inside the
  bracket), all Challenger/WTA-125 matches whose nominal start was hours after the real one. None was used
  as strict evidence (0 of 2,312 strict rows). START_UNKNOWN rows (9,718) were never violations. The gate
  keeps failing; its detail now says which is which, and `run_tennis.py` refuses matches the first-ball
  store has already seen start.
