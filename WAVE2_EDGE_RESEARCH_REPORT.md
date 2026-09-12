# Wave 2: edge research report

**2026-09-12. `chmoses98/Tennis-Edge-Finder`. REAL-MONEY AUTHORITY: OFF.**

The question was not "can we beat Pinnacle everywhere". It was whether there are identifiable situations
where we hold a small, repeatable, executable advantage. Below is what the evidence says, including the
parts that say no.

## Headline

1. **Gen-2 beats Gen-1, narrowly and where the theory says it should.** ATP Brier 0.2023 → 0.2012, paired
   95% CI excluding zero; the gain is exactly zero where no serve evidence exists and largest in the
   moderate-evidence bucket.
2. **Market conditioning improves derivative pricing, clearly.** Anchoring the winner probability to the
   market while keeping the structural service level improved every derivative metric, with six of eight
   confidence intervals excluding zero. The control that conditions on Elo instead was WORSE than not
   conditioning at all, so the gain comes from the market's information rather than from conditioning
   as a technique.
3. **The market's residual is not predictable** from eleven pieces of pre-match context. Out of sample
   the residual model was worse than the market.
4. **There is no cross-market relative value on this board**, and the reason is structural: the fee wall
   is wider than any inconsistency observed, and 136 of 137 matches have exactly two open contracts.
5. **The biggest constraint is not modelling. It is that Kalshi tennis has almost no derivative board.**
   The lane that improved most (derivative pricing) has the least to trade against.

## The core research questions, answered

**1. Can Gen-2 improve on Gen-1?** Yes, narrowly. Walk-forward, strict chronology, randomised
orientation, 347,414 ATP and 289,906 WTA matches from 2015:

| lane | ATP Brier | ATP log loss | WTA Brier | WTA log loss |
|---|---|---|---|---|
| rank baseline | 0.2251 | 0.6419 | 0.2279 | 0.6478 |
| MODEL 1 Gen-1 Elo | 0.2023 | 0.5889 | 0.1985 | 0.5806 |
| MODEL 2 Gen-1 structural | 0.2696 | 0.7431 | 0.2637 | 0.7255 |
| MODEL 3 Gen-2 raw | 0.2409 | 0.6763 | 0.2555 | 0.7064 |
| **MODEL 3 Gen-2 blended** | **0.2012** | **0.5864** | **0.1982** | **0.5798** |

Paired Brier difference against Elo: ATP **-0.00106**, 95% CI [-0.00124, -0.00087]; WTA **-0.00034**, CI
[-0.00046, -0.00022]. Both intervals exclude zero. In relative terms this is about half a percent on ATP.

**2. Does it add incremental information in identifiable subsets?** Yes, and the pattern is the tell:

| serve evidence (thinner player) | ATP n | Elo Brier | Gen-2 blended | difference |
|---|---|---|---|---|
| none | 77,088 | 0.1897 | 0.1897 | 0.0000 |
| under 1k points | 118,316 | 0.1898 | 0.1898 | +0.0000 |
| 1k-5k | 104,188 | 0.2175 | 0.2149 | **-0.0026** |
| 5k-20k | 47,822 | 0.2204 | 0.2185 | **-0.0020** |

Identically zero where the structural model has nothing to say (the blend collapses to the rating by
construction) and clearly positive where it has moderate evidence. That is the signature of real
incremental information rather than a fitted artefact.

**3. Does conditioning on the market improve derivative pricing?** **Yes.** 12,946 ATP matches with a
de-vigged Pinnacle price, a Gen-2 state and a final score. Lower is better:

| metric | fundamental | market-conditioned | elo-conditioned (control) |
|---|---|---|---|
| exact set score, log loss | 1.35038 | **1.32710** | 1.37007 |
| game differential, mean abs error | 4.10248 | **4.00667** | 4.17372 |
| total games, squared error | 48.30173 | **47.91897** | 49.20693 |
| over 21.5 games, Brier | 0.20114 | **0.20023** | 0.20045 |
| sets played, Brier | 0.18896 | **0.18832** | 0.18850 |

Paired bootstrap, market-conditioned minus fundamental: exact score **-0.02329** CI [-0.02776, -0.01867];
game differential **-0.09581** CI [-0.11491, -0.07675]; total-games squared error **-0.38276** CI
[-0.62567, -0.13042]; over-21.5 Brier **-0.00090** CI [-0.00152, -0.00029]. Six of eight metrics have
intervals excluding zero.

**The control matters more than the result.** Conditioning on Elo made things WORSE than not conditioning.
So this is not "constraining the distribution helps"; it is specifically that the market's winner
probability carries information our fundamental model does not.

**4. Does the market price the winner well but misprice how the match gets there?** The first half is
supported: the market beats every lane we have at picking winners, and conditioning on it improves our
derivatives. The second half is **not established**. Showing that the market misprices a derivative
requires comparing against a derivative PRICE, and Kalshi listed four exact-score and three total-games
contracts across the entire captured universe. We improved our own pricing; we have not shown theirs is
wrong.

**5. Are there internally inconsistent Kalshi markets?** **No.** Zero violations over ten capture passes,
price-only or size-verified. Two-sided ask-sums: median 1.0200, minimum 0.9900. Bid-sums: median 0.9800,
maximum 1.0000. Round-trip spread median three cents.

**6. Are derivatives slower to update than parents?** **Not measurable.** Of 140 matches quoted, exactly
**2** had two or more families quoted simultaneously, giving **1** usable pair. This is a power problem,
not a null result.

**7. Do market-residual patterns survive out of sample?** **No.** Trained before 2024, tested 2024 onward
(4,804 matches), market as an offset so zero coefficients reproduce it exactly. Brier 0.20316 against the
market's 0.20302; paired difference **+0.00014**, CI [-0.00040, +0.00067], P(better) 0.31. Eleven
features tried.

**8. Which hypotheses failed?** Five, recorded in `research/REJECTED_HYPOTHESES.md`: the residual model
(R-001), cross-market coherence as a live edge (R-002), raw Gen-2 without the rating fallback (R-003),
lead-lag as currently measurable (R-004), and finding a fresher Sackmann fork (R-005).

**9. Which hypotheses deserve prospective tracking?** Four, frozen in `data/research/edge_candidates/`
before any confirmation data existed. See the candidate table below.

## Data freshness (Phase 0)

The Sackmann repositories are gone and every fork froze with them: of the twenty most recently pushed
`tennis_atp` forks, the freshest is 2026-06-10 and the rest are 2026-06-08. That is structural, not a bad
fork choice. Two things changed as a result:

* **A cross-system player crosswalk** admits the community mirror's ATP rows, moving ATP ratings from
  as-of 2026-06-01 to **as-of 2026-09-01**. It fails closed: a name shared by two players in either
  system maps to nothing, and a match with one unmapped player is unmapped as a whole. 4,701 of 4,991
  mirror players crosswalked; 88,896 rows admitted.
* **An ESPN results feed** for current results on both tours, which matters most for WTA where nothing
  else has moved since 2026-04-27. Verified against a saved payload (473 completed singles, 97% passing
  canonical validation). Its first two unattended runs published nothing: the sources job installs no
  Python packages, because the Sackmann fetcher is stdlib-only, so the step died importing pandas and
  `continue-on-error` reported it as SUCCESS. The step now installs pandas and fails loudly when the
  fetch produces no output. It publishes: **5,471 completed singles, 2026-03-28 to 2026-09-11, both
  tours current to yesterday.**
* Its first real publish was **wrong**, and the check that caught it was arithmetic rather than a gate:
  779 ATP rows against 4,692 WTA is not a plausible split. A combined event appears on BOTH league
  boards carrying BOTH draws, and the parser took the tour from the league it fetched, so Wimbledon's
  men's draw off the WTA board was filed as WTA — 1,373 men's matches mislabelled. The grouping slug now
  decides the tour and the league is only a fallback; the corrected split is 2,152 ATP / 3,319 WTA.
  Snapshot `20260912T065821Z` on `tennis-data` is quarantined in place rather than deleted.
* The feed carries **no serve statistics**, so it can refresh Elo-family ratings and cannot feed Gen-2.
  The WTA fundamental staleness that fails TENNIS-14 is therefore *not* closed by it.

WTA history remains stale and TENNIS-14 continues to fail rather than being relaxed.

## Board accounting (Phase 1)

Every contract carries exactly one of eight states, and an invariant check fails if the states do not sum
to the contracts seen. On the 2026-09-12T04:48Z board: 451 contracts, 437 active, 205 priced.

| coverage | value | denominator |
|---|---|---|
| A, all active contracts | 46.9% | 437 |
| B, contracts that should be priceable with current inputs | 65.7% | 312 |

| state | contracts |
|---|---|
| PROJECTED | 205 |
| UNSUPPORTED_FAMILY | 118 |
| UNMAPPED_IDENTITY | 60 |
| NO_FIRST_BALL_SOURCE | 47 |
| CLOSED_SINCE_DISCOVERY | 14 |
| NO_DRAW | 7 |

Two findings. A doubles event rejected on a partner's surname was being filed as INSUFFICIENT_DATA, which
points future work at the wrong thing; it is an identity failure, and reclassifying it makes
UNMAPPED_IDENTITY the largest fixable blocker. And most of those unmapped players are recent arrivals
absent from a registry built on four-month-old data.

## Frozen candidates

| id | claim | status | minimum N |
|---|---|---|---|
| EC-2026-001-MKTCOND-EXACT-SCORE | market conditioning improves exact-score pricing | PROSPECTIVE_PENDING | 400 |
| EC-2026-002-MKTCOND-GAME-SPREAD | the same for game spread and total games | PROSPECTIVE_PENDING | 400 |
| EC-2026-003-GEN2-MODERATE-EVIDENCE | Gen-2 adds information at 1k-20k serve points | PROSPECTIVE_PENDING | 1000 |
| EC-2026-004-COHERENCE-EXECUTABLE | size-verified coherence violations occur at a non-zero rate | DISCOVERY_ONLY | 10 |

Each carries an exact inclusion rule, a pre-committed pass condition, and a mandatory strongest opposing
reason. The registry **refuses** evidence dated before a candidate's freeze, so none of them can be
confirmed on the data that produced it.

## Discipline

Model 3 cannot see a price: `tests/test_gen2.py` walks the import graph and fails if it reaches anything
price-bearing. Model 4 declares that it uses the market in its name and its docstring, and its winner
probability IS the market's, so it cannot be mistaken for a forecast. Segments were pre-registered in
code and dated before results were read. The shadow board is append-only and hash-chained, and rejects a
row with no stated counter-argument.

Two modelling defects found and fixed during the wave, both now pinned by tests: the point-probability
pair the scoring engine expects is (A on A's serve, A on B's serve), and passing (A holds, B holds)
prices every match at 0.99; and the ability estimator must be a precision-weighted mean of
opponent-adjusted excess, not an innovation filter, or every player decays back to the baseline and the
model predicts 0.50 for everything.

## What would actually move the needle next

Not a better model. **More derivative liquidity**, which is outside our control, and **fresher WTA
fundamentals**. The ESPN feed now publishes and is current to yesterday, but it is results-only: it can
carry Elo forward and it cannot carry Gen-2, which needs serve statistics. Closing TENNIS-14 properly
still needs a current source with point-level serve data, and nothing free that we have probed has one
for the WTA.

**REAL-MONEY AUTHORITY: OFF.**
