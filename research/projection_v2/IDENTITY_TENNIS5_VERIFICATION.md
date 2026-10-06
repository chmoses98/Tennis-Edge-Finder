# Identity cleanup + TENNIS-5 remediation: production verification (2026-10-06)

Append-only record. Changes: chmoses98/Tennis-Edge-Finder#23 (reviewed aliases, `canonical_v2.2`, TENNIS-5 split) and
chmoses98/Tennis-Edge-Finder#24 (`canonical_v2.3`, split-opponent duplicates). No Projection V2 coefficient, feature,
ensemble weight, calibration, Elo/Gen-2 parameter, scoring logic, promotion rule, frozen spec or discrepancy threshold
was changed: the V2 `coefficients_fingerprint` is `dd6d413d5bfdd820` on the boards before and after. Real-money authority OFF.

## Production runs

| | RUN TENNIS | run id | SHA | job runtime | board |
|---|---|---|---|---|---|
| before (pre-merge) | #107 | 37414538563 | 269e73a | 04:36:53-04:59:13Z | 20261006T044905Z |
| after #23 | #108 | 37415012362 | 9a0a60d | 04:59:17-05:22:48Z (23.5 min) | 20261006T051200Z |
| **final, after #24** | **#109** | **37419865866** | **d7256d4** | **05:42:24-06:02:04Z (19.7 min)** | **20261006T055404Z** |

Build in production: `canonical_v2.3`, 1,545,881 rows, 77 reviewed aliases accepted / 77 applied / 0 refused, 16
split-opponent duplicates dropped; TENNIS-13 hash match.

## Coverage (before #107 -> final #109)

| | before | after |
|---|---|---|
| identity-excluded markets | 126 | **94** |
| unmapped-player markets (`coverage.unmapped_player`) | 126 | 94 |
| identity gap kinds | NO_HISTORY 108, ALIAS_CANDIDATES 18, AMBIGUOUS 2 | NO_HISTORY 76, ALIAS_CANDIDATES 18, AMBIGUOUS 2 |
| unresolved singles players on the board | 54 | 52 |
| doubles-excluded markets | 252 | 248 |
| projected singles / doubles | 1,053 / 18 | 1,044 / 14 |
| projectable open pregame | 1,449 | 1,400 |
| V2 grades (singles match winner) | POOR 446, LOW 100, HIGH 56, MEDIUM 10 | POOR 436, LOW 104, HIGH 48, MEDIUM 10 |
| alias review queue | 9 | 9 |

The total priced count is not comparable across runs an hour apart (markets start, settle and list); the identity
lines are. The 32 unlocked markets are Daniel Merida v Van de Zandschulp and Yunchaokete Bu v Van Assche (ATP
Shanghai, 16 markets each), both now priced, both V2 grade HIGH. Nothing was unlocked by lowering a confidence
requirement: alias names resolve at the existing 0.95, and only through an accepted, evidence-backed entry.
The `alias_review_queue` (9) is the Kalshi-name queue reviewed here: 8 rejected (different people), 1
insufficient evidence -- they correctly stay unmapped.

## Live alias sanity review (final board)

9 accepted-alias players on the board (18 match-winner rows); `alias_review/coverage_before_after.json` has every
row with canonical id, name, rated matches, last result, opponent, event, level, surface, last five results by
source, grades, probability change and model-market gap. All passed:

| player (canonical) | via | event | opponent | V2 grade | dp vs before | gap | verdict |
|---|---|---|---|---|---|---|---|
| Qinwen Zheng 221012 | espn:6048 | WTA Beijing | Alina Charaeva | LOW | 3.6 pp | 1.7 pp | PASS -- US Open QF + Beijing R3 rows are hers |
| Jia-Jing Lu 203288 | espn:2509 | WTA 125 Suzhou | Tamara Korpatsch | POOR | 0.9 pp | 1.0 pp | PASS -- Suzhou qualifying rows; the 1989-11-18 Lu, not Jing-Jing Lu |
| Diego Dedura-Palomero 212309 | tml:D0LJ / espn:14709 | CH Villena | Jack Pinnington Jones | LOW | 4.7 pp | 5.0 pp | PASS -- Tulln/Szczecin/Plovdiv TML rows |
| Rigele Te 144751 | espn:2856 | ATP Shanghai | Ilia Simakin | LOW | 0.5 pp | 1.7 pp | PASS |
| Zhizhen Zhang 111190 | espn:3024 | ATP Shanghai | Tomas Machac | HIGH | 1.3 pp | 1.6 pp | PASS after #24 (Hangzhou loss was counted twice in #108) |
| Daniel Merida Aguilar 210017 | espn:10239 | ATP Shanghai | B. van de Zandschulp | HIGH | new | 10.7 pp | PASS -- Cincinnati/US Open rows |
| Bu Yunchaokete 207352 | tml:Y09V | ATP Shanghai | Luca Van Assche | HIGH | new | 14.5 pp | PASS -- Hangzhou QF, China Open loss to Djokovic |
| Meiling Wang 216062 | espn:3992 | W15 Maanshan | Yiru Chen | POOR | 0.0 | 11.1 pp | PASS |
| Yushan Shao 269253 | espn:15422 | WTA 125 Suzhou | Katarina Zavatska | POOR | 0.3 pp | **27.8 pp** | PASS -- see below |

Shao v Zavatska is the only > 20 pp row. Identity is right (ESPN 15422 'Shao Yushan' and Sackmann 269253 are both
born 2008-12-26, CHN); the alias moved her probability by 0.3 pp, so it did not create the gap. The "market" is an
empty book: bid 0.07 / ask 0.89, volume 0, open interest 0 -- its mid is not a price. V2 grade POOR (28 rated matches).
No still-unresolved review name appears on the board. No market moved >= 5 pp between the boards.

### Found in this review and fixed (#24)
Zhang's Hangzhou loss to Coleman Wong was in the table twice: ESPN's 'Chak Lam Coleman Wong' maps to Sackmann's
one-match stub 208597, TML's 'Coleman Wong' to 209409, so the ordered-pair dedupe could not pair them. The accepted
aliases had admitted 16 such double-counted results (opponent split across a Sackmann duplicate or a minted twin).
`canonical_v2.3` drops them (reviewed-alias rows only, fail-closed rule, audited in the build manifest). Three residual
possible duplicates are kept because the sources disagree about the opponent or the event (Burillo/Bogota 2026
Werner vs Uebelhoer; Statham Burnie vs Launceston 2019; Estrella Poznan 2018 Juszczak vs Cias). The opponent splits
themselves (Sackmann duplicates, minted twins with apostrophes) are pre-existing and remain a follow-up.

## TENNIS-5 (final, #109)

**pricing_quote_freshness: PASS** -- 1,058 rows, every one priced from full open snapshot 20261006T055355Z (3.9 s
old at pricing). Quote age at pricing: median 18.7 s, p95 22.3 s, max 27.8 s; 0 rows over 30 min, 0 of unknown age.
Snapshot quotes 05:53:55.998-05:54:03.801Z, priced 05:54:08.232-05:54:24.497Z.

**background_capture_health: FAIL** -- newest pass 20261006T053732Z finished 05:41:14Z, 1.5 min old when the runner
pulled (05:42:47Z); trade backlog clear; 0 failed passes; pass duration median 99 s. But over the last 6 h the
interval between passes had median 19.3 min and max 31.4 min, with two gaps over 30 min (31.0, 31.4 at 02:23 and
02:55Z). The conductor's interval grows within each ~5h40m conductor run (9.4 -> 10 -> 11 -> 14 -> 19 -> 23 -> 26
-> 31 min) and resets when a new run starts; the capture step itself stays 1.5-3.7 min, so the growth is in the
rest of the loop (fetch/publish/scan). That is a real operational defect; it is reported, not hidden.

**pulled_capture_artifact_age_min: 17.7** -- reported only (age at health time of the newest pass in the pulled copy).

TENNIS-5 = FAIL is correct: prices were made on seconds-old quotes, but the background conductor did let two
intervals exceed the unchanged 30-minute limit inside the gate's window.

## Health after this pass (#109)

PASS: 1, 2, 3, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18. FAIL: 4 (94 identity markets -- 76 players absent from
every source, 18 alias candidates with no verified identity, 2 ambiguous -- and 248 doubles markets with an
unresolvable teammate), 5 (conductor cadence, above), 8 (independent sports truth 6,231 / 17,918 = 34.8%; ITF has no
independent source).

## Projection V2 prospective study

Intact and untouched; nothing was retuned and no interim performance was computed. Every singles match-winner ledger
row since the first V2 run (2026-10-05 15:45Z) carries both the V2 and the incumbent probability: 369 matches so far,
57 settled by the exchange, **0 independently settled** -- the independent results sources end before the V2 era for
every level in it (e.g. WTA ITF 2026-04-27, ATP Challenger 2026-09-29). Readout stays at 1,500 independently settled
matches (PREREGISTRATION.md section 6).
