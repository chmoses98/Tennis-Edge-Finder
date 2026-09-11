# MIGRATION AUDIT — tennis system out of `chmoses98/nfl-edge-finder`

Date: 2026-09-11 (UTC). Performed by Claude Opus 5 under the controlled-migration brief.
Nothing in `chmoses98/nfl-edge-finder` was deleted, and `nfl-edge-finder:main` was never touched.

## 1. Source

| item | value |
|---|---|
| source repository | `chmoses98/nfl-edge-finder` |
| source code branch | `claude/tennis-edge-finder-nr4scu` |
| source code HEAD at migration | `0138597f09f855dc0e04cfc2682c5d160bcd6d48` ("tennis: final ATP study numbers incl. rank baseline…", 2026-09-11T14:06:30Z) |
| source code commits (tennis-only, main..branch) | 25 |
| source data branch | `tennis-data` (orphan) |
| source data HEAD at migration start | `696e89a57f37e9db7541b9e3ab22c7bf519711c7`; it kept growing during the migration because the old conductor was deliberately left running, and was frozen at `f3061fd57cbb98dfb1f037ecc7f2baa0cd68a39c` (pass 30) when the chain was stopped — see §5 |
| `nfl-edge-finder:main` (untouched, recorded for proof) | `7d073680f9f82d80e02a9959f103d41cc24e3ffe` |

## 2. Destination

| item | value |
|---|---|
| destination repository | `chmoses98/Tennis-Edge-Finder` |
| state before migration | one commit `d57aef9ce4df6dfd518eb8f1d603e227b5cdfd83` ("Initial commit", a one-line placeholder README), default branch `main`, no other branches |
| destination `main` HEAD | `4619a17be3556171f92a23add5b3c2f52d26692a` (see §9) |
| destination `tennis-data` HEAD | `b069c335eac630915cfc573b63e5369105e84541` at audit time, and growing (see §9) |

## 3. Code migration

Method: `git-filter-repo` over a clone of the source code branch, keeping only tennis-owned paths and
renaming `tennis-edge-finder/` to the repository root, then rebased onto the destination's existing
"Initial commit" so the owner's root commit is preserved as ancestry. 116 commits in → 25 tennis
commits out (every NFL commit became empty under the path filter and was pruned).

**Proof of byte-identical transfer.** The git tree object for everything except `.github/` in the
migrated repository is `50a9a7ff4a29f23b619ffdd91da010a2f958ca60`, which is exactly the tree hash of
`tennis-edge-finder/` at the source HEAD. 140 files each side. The three workflow blobs match the
source blob SHAs exactly (`1565d774…`, `fb7e3b02…`, `0c3632a0…`).

### Paths migrated
| source | destination |
|---|---|
| `tennis-edge-finder/**` (140 files: `tennis_edge/`, `scripts/`, `tests/`, `docs/`, `config/`, `research/`, `data/research/`, `MORNING_REPORT.md`, `README.md`, `pyproject.toml`, `.gitignore`, trigger files) | repository root |
| `.github/workflows/tennis-bootstrap.yml` | unchanged path |
| `.github/workflows/tennis-capture.yml` | unchanged path |
| `.github/workflows/tennis-run.yml` | unchanged path |

### Paths deliberately excluded
| path | classification | reason |
|---|---|---|
| `nfl_edge/**`, `scripts/` (NFL), `config/` (NFL), `data/` (NFL), `docs/` (NFL), `research/` (NFL), `tests/` (NFL), `.github/workflows/` (13 NFL workflows) | NFL | not tennis; untouched by the tennis branch (every tennis-branch change vs `main` is an ADD — zero NFL files were modified, verified with `git diff --name-status`) |
| `research/elo_study/log_ATP.txt`, `research/elo_study/log_WTA.txt` (repo root, not under `tennis-edge-finder/`) | TENNIS, no evidence value | 121-byte stderr files from one early background run that mis-resolved its path (`python3: can't open file …`). They contain no research content. They remain on the source branch; they were not carried over. |

### Path rewrites applied
* workflows: `python3 tennis-edge-finder/scripts/X` → `python3 scripts/X`; local data dirs `tennis-edge-finder/data/X` → `data/X`; trigger paths `tennis-edge-finder/.X-trigger` → `.X-trigger`.
* `scripts/kalshi/discover_tennis.py`: `publish()` treated the repository root as `PROJ/..` (true only while nested); now uses `PROJ`.
* user agents: `github.com/chmoses98/nfl-edge-finder` → `github.com/chmoses98/tennis-edge-finder` in `tennis_edge/kalshi/client.py` and `scripts/data/bootstrap_sources.py`.
* `README.md`, `docs/ARCHITECTURE.md`: describe the standalone layout and the retained data-branch prefix.
* `docs/DECISION_LOG.md` line 1 still says the project was built inside `nfl-edge-finder`. That is **historical fact and was deliberately left intact**.

### Workflow rewrites
| workflow | change |
|---|---|
| all three | `push:` trigger moved from `branches: ['claude/tennis-edge-finder-nr4scu']` to `branches: ['main']` |
| all three | `schedule:` cron added — the workflows now live on the default branch, where GitHub actually runs cron. Capture `3 */5 * * *`, run `25 */6 * * *`, bootstrap `40 5 * * *` |
| `tennis-capture.yml` | 10-minute pass cadence, ~5h40m conductor loop and the self-dispatching successor are **unchanged**; cron is an additional safety net against a lost dispatch. `concurrency: tennis-capture-conductor, cancel-in-progress: false` still admits at most one running + one pending conductor, so cron and self-dispatch cannot produce two permanent parallel capture systems. |
| `tennis-run.yml` | unpacks evidence with `git archive origin/tennis-data tennis-edge-finder/data \| tar -x --strip-components=1` |
| all three | publish via `scripts/ci/publish_branch.py --src data/...`, which re-applies the historical branch prefix |

Self-dispatch already used `${{ github.repository }}` and `${{ github.ref_name }}`, so it retargets the
new repository automatically; there is no hardcoded repository name anywhere in the destination.

## 4. Data migration — `tennis-data`

**Git history was preserved EXACTLY. No rewrite, no re-capture, no timestamp change, no squash.**

Method: the source commits were pushed to the destination one at a time by SHA
(`git push dest <sha>:refs/heads/tennis-data`), oldest first, so each upload was a bounded pack. Because
nothing was rewritten, every commit kept its original hash — the destination root commit is
`7ef35e1313012764fef2cbec84ab6fa152c53bab`, identical to the source root.

**This is why the branch keeps the `tennis-edge-finder/data/...` path prefix.** Stripping it would have
rewritten all ~50 commits and changed every SHA on frozen prospective evidence. Path cosmetics are not
worth that, so the prefix stays and the code re-applies it (`publish_branch.py --dest-prefix`, default
`tennis-edge-finder`) and strips it on read (`tar --strip-components=1`).
`tests/test_migration_invariants.py` fails if either half of that contract is broken.

## 5. Cutover (all times UTC, 2026-09-11)

The brief's ordering was followed exactly: preserve the old capture, start the destination capture,
prove it is genuine, prove it lands on the new `tennis-data`, prove the destination conductor
self-dispatches, prove nothing writes back to the NFL repository — and only then stop the old chain.

| time | event |
|---|---|
| 18:43:19 | push to destination `main` registered the three workflows (`356036139` bootstrap, `356036140` capture, `356036141` run) and fired all three: capture `34634877585`, RUN TENNIS `34634877601`, bootstrap `34634877614` |
| 18:43:31 | **last** capture pass of the OLD NFL conductor (run `34605925414`, pass 30) — still running, deliberately |
| 18:43:51 → 18:45:34 | **first genuine destination capture**: 494 live Kalshi API requests, 360 open markets, 215 quotes written, 96 order books, 25,148 tennis trades selected from 250,000 global trades scanned |
| 18:46:18 | that capture landed on the **destination** `tennis-data` as `a1c8b5be02e996b1d4765231fc2456cb1529e6ef`, files `tennis-edge-finder/data/kalshi/capture/2026-09-11/20260911T184351Z.{quotes,books,events,trades}.jsonl.gz` + `.manifest.json` |
| 18:49:52 | **destination conductor self-dispatched its successor**: run `34635486383`, event `workflow_dispatch`, triggering actor `github-actions[bot]`, ref `main` |
| 18:50:30, 18:52:12 | successor's capture passes, published to the destination branch |
| ~18:53 | OLD workflow `chmoses98/nfl-edge-finder/.github/workflows/tennis-capture.yml` (`355559244`) set to `disabled_manually` via the Actions API, then in-flight run `34605925414` cancelled |
| 18:54:56 | overlap reconciled onto the destination branch as merge `b069c335eac630915cfc573b63e5369105e84541` |

The first destination conductor was cancelled immediately after its first publish. That was on purpose:
a conductor loops ~5h40m before it reaches its `Dispatch successor` step, and the self-dispatch had to
be **observed**, not assumed. Cancelling made the `always()` dispatch step fire at once, which is what
produced run `34635486383` — a real, conductor-originated dispatch, not a human one.

### No capture gap
Both systems were live at the same time; the old one was never stopped before the new one had published.
Across the whole cutover the largest interval between consecutive capture passes was **399 s**, *shorter*
than the normal 600 s cadence. (The largest interval anywhere on 2026-09-11, 1364 s at 13:13→13:36,
predates the migration entirely.)

### No write-back to `nfl-edge-finder`
* Static: no live reference to the NFL repository survives anywhere in the destination — the only three
  occurrences of the string are a comment, a docstring and a test assertion. Every push in the
  destination targets `origin`; the only GitHub API call uses `${{ github.repository }}`;
  `actions/checkout@v4` has no `repository:` override. `tests/test_migration_invariants.py` fails if this
  regresses.
* Empirical: the two conductors captured 20 s apart. `20260911T184351Z` (destination) appears **only** on
  the destination branch and `20260911T184331Z` (NFL) appeared **only** on the NFL branch until the
  reconciliation merge deliberately brought it across. The NFL repository's `tennis-capture.yml` run
  count is still 6 — the cancelled conductor created no successor there.

### Overlap reconciliation (`b069c335`)
The old conductor published passes 29 and 30 after the exact-SHA transfer had reached pass 28. Those
observations were brought in as a **git merge with the original commits as the second parent** — nothing
re-captured, re-timestamped or squashed. The only conflict was `data/kalshi/capture/state.json` (quote
fingerprints + trade cursor), resolved to the destination side, which is the live capturer and strictly
ahead (`trades_cursor_ts` 1789150923 vs 1789150515).

**No-data-loss proof.** Of the 33,536 blobs on the final NFL `tennis-data` head
`f3061fd57cbb98dfb1f037ecc7f2baa0cd68a39c`, **0 are missing** from the destination branch. Eight files
differ, all of them mutable "latest state" files that the destination's own pipeline legitimately
advanced: `capture/state.json`, `processed/build_manifest.json`, `processed/ratings_{ATP,WTA}.json`,
`research/health_latest.json`, `research/projections/latest.json`, `research/settlements/SCORECARD.md`
and `research/ledger/2026-09-11.jsonl`.

**Ledger proof.** The prospective ledger was extended, never reset: the source's 236 entries are the
first 236 lines of the destination's 304, byte for byte. Gate TENNIS-12 (`append_only_ledger`) reports
PASS with zero violations on the destination, so the hash chain survived the move intact.

## 6. Testing

**Unit tests.** 219 tests migrated, 219 pass in the destination — exact parity with the source. Plus 17
new tests in `tests/test_migration_invariants.py`: **236 pass, 0 fail.** The new tests assert repository
self-containment (no NFL targets, pushes to `origin`, API calls via `${{ github.repository }}`, triggers
bound to `main`), both halves of the data-branch prefix contract (`--dest-prefix` on write —
end-to-end through a real subprocess publish — and `--strip-components=1` on read), and that real-money
authority is still OFF in README, MORNING_REPORT, `run_tennis.py` and `auth_adapter.py`.

**End-to-end pipeline on the destination.** RUN TENNIS run `34634877601` (`push` → `main`) succeeded
through every stage: fetch evidence off `tennis-data` → build the canonical table (1,624,759 rows,
reproducibility hash matched) → refit ratings → discover and price live Kalshi markets → settle →
evaluate the 14 health gates → append to the ledger → publish back to `tennis-data`
(`fdb7ca11`, `8621c1ee`). The bootstrap workflow (`34634877614`) also succeeded and refreshed the
source mirrors (`93a2cb8d`).

**Health gates after the move are identical in pattern to before it** — the migration neither fixed nor
broke anything:

| PASS | FAIL | UNKNOWN (fail-closed) |
|---|---|---|
| TENNIS-1, 2, 3, 6, 7, 11, 12, 13 | TENNIS-4 (projection coverage), TENNIS-5 (trade tape truncated at the 250k-page budget), TENNIS-14 (upstream source staleness) | TENNIS-8, 9, 10 |

One artifact deserves a note so it is not mistaken for a fabrication: the destination run published
`data/research/projections/20260911T135922Z.json` to the data branch for the first time. It was not
regenerated or back-dated — it had been committed into the code tree during the overnight build and its
blob on the data branch (`e3df79cc9060ca4af9ce2bbbe9c6195793f370ca`) is byte-identical to the blob on
`main`.

## 7. Known limitations (carried over unchanged — migration did not resolve any of them)

* **No first-ball feed.** Kalshi exposes a nominal start and a close time, never a first-ball timestamp.
  Every canonical close is therefore `SCHEDULED_MINUS_MARGIN`, and for ITF/Challenger series the nominal
  time is not a start time at all (it usually falls *after* the market closes), so those rows are flagged
  `NOMINAL_UNRELIABLE` and are never actionable. Strict pregame CLV is not yet possible.
* **Source freshness.** The upstream `JeffSackmann/tennis_atp` and `tennis_wta` repositories return 404;
  data comes from public forks whose rows end 2026-06-01 (ATP) and 2026-04-27 (WTA). Gate TENNIS-14 fails
  on that staleness by design.
* **Projection coverage.** Gate TENNIS-4 fails: tournament-scope families need a draw feed, some events
  do not expose both competitors' full names, and a handful of players stay unmapped (fail closed).
* **Model vs market.** Unchanged and not re-run during migration: Pinnacle beats the ensemble
  (Brier 0.2026 vs 0.2111, bootstrap CI excludes zero); the Kalshi pregame quote beats it
  (0.1871 vs 0.2060); the walk-forward hybrid puts a *negative* weight on the model; large
  model-market disagreements are model error. **REAL-MONEY AUTHORITY: OFF.**

## 8. What this migration deliberately did NOT do

* It did not rebuild, redesign or re-fit the model, and ran no new modelling research.
* It did not regenerate old captures, rewrite timestamps, collapse commits or manufacture any
  historical snapshot.
* It did not touch `nfl-edge-finder:main` (still `7d073680f9f82d80e02a9959f103d41cc24e3ffe`, exactly as
  recorded in §1 before the migration began) and opened no pull request against it.
* It deleted nothing. `claude/tennis-edge-finder-nr4scu` (`0138597f09f855dc0e04cfc2682c5d160bcd6d48`) and
  the NFL `tennis-data` branch (`f3061fd57cbb98dfb1f037ecc7f2baa0cd68a39c`) are both retained, untouched,
  as an independent check on this transfer. The old capture workflow is *disabled*, not removed, and can
  be re-enabled from the Actions API if this repository ever needs to be re-verified against it.
* It did not change the research conclusion. Every research document — MORNING_REPORT.md, MODELING.md,
  VALIDATION.md, KNOWN_LIMITATIONS.md, PROSPECTIVE_RESEARCH_PROTOCOL.md, CLV_AND_SETTLEMENT.md,
  DATA_SOURCES.md, IDENTITY.md, KALSHI_MARKET_TAXONOMY.md, PRODUCTION_HEALTH.md, DECISION_LOG.md — is
  byte-identical to the source. Only README.md and docs/ARCHITECTURE.md changed, and only to describe the
  standalone layout; no verdict sentence in either was altered.

## 9. Final state

| item | value |
|---|---|
| destination `main` HEAD | `4619a17be3556171f92a23add5b3c2f52d26692a` (26 commits: the owner's `d57aef9c` "Initial commit" + 25 filtered tennis commits) |
| destination `tennis-data` HEAD at audit time | `b069c335eac630915cfc573b63e5369105e84541` (grows every 10 minutes — it is a live capture branch) |
| destination `tennis-data` root commit | `7ef35e1313012764fef2cbec84ab6fa152c53bab` — **identical to the source root**; all ~50 pre-migration commits kept their original SHAs |
| destination capture conductor | run `34635486383`, self-dispatched, looping; cron `3 */5 * * *` as the backstop |
| tests | 236 passed, 0 failed |
| `nfl-edge-finder:main` | `7d073680f9f82d80e02a9959f103d41cc24e3ffe` — unchanged |
| `nfl-edge-finder:claude/tennis-edge-finder-nr4scu` | `0138597f09f855dc0e04cfc2682c5d160bcd6d48` — retained |
| `nfl-edge-finder:tennis-data` | `f3061fd57cbb98dfb1f037ecc7f2baa0cd68a39c` — retained, frozen |
| old capture workflow | `disabled_manually`; 6 runs total, no successor created after cancellation |
| **REAL-MONEY AUTHORITY** | **OFF.** Unchanged by this migration and not re-evaluated during it. |
