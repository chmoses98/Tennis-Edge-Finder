# Rejected hypotheses

A graveyard, so a future agent does not rediscover a dead idea and overfit it a second time. Each entry
records what was tested, on what, how, and why it was rejected. A rejected hypothesis is retested only
when something material changed: new data, a new source, or a structural change in the market.

---

## R-001 The market's residual is predictable from model disagreement and match context

* **Tested** 2026-09-12, wave 2.
* **Data** 12,946 ATP matches with a de-vigged Pinnacle price and a Gen-2 state; trained on seasons
  before 2024 (8,142 matches), tested on 2024 onward (4,804), test set untouched during fitting.
* **Method** `logit p = logit(p_market) + X·beta`, the market price as an OFFSET so that beta = 0
  reproduces the market exactly. Eleven features: Gen-2 and Elo disagreement, absolute disagreement,
  favourite extremity, log serve evidence, clay/grass/slam/masters indicators, best-of-5, model spread.
  Strong L2, chronological split.
* **Result** Out of sample the residual model was **worse** than the market: Brier 0.20316 against
  0.20302, paired difference **+0.00014**, 95% CI [-0.00040, +0.00067], P(better) 0.31.
* **Why rejected** The interval straddles zero and the point estimate has the wrong sign. Eleven features
  were tried, so even a nominally significant single coefficient would need discounting; none was.
* **Retest justified?** Only with materially different features, in particular order-book microstructure
  (depth imbalance, quote age, trade pressure), which this archive is too short to supply.

---

## R-002 Cross-market coherence violations are an exploitable source of relative value on Kalshi tennis

* **Tested** 2026-09-12 over ten capture passes, ~100 minutes of the live board.
* **Method** Partition, composite, ladder and implication relationships on executable bid/ask, with
  order-book depth on every leg and Kalshi taker fees charged per leg. Both a price-only scan (size
  ignored) and a size-verified scan.
* **Result** **Zero violations of either kind.** Two-sided match-winner ask-sums had a median of 1.0200
  and a minimum of 0.9900; bid-sums a median of 0.9800 and a maximum of 1.0000.
* **Why rejected (for now)** The fee wall is wider than the inconsistency. A two-leg structure near even
  money costs roughly four cents in taker fees; the widest gap observed anywhere was one cent.
* **Retest justified?** Yes, on a fee change, a period of fast price movement, or a materially larger
  derivative board. Frozen as candidate EC-2026-004 so that monitoring accrues against a fixed rule.

---

## R-003 Raw Gen-2 structural pricing beats Gen-1 Elo at match-winner prediction

* **Tested** 2026-09-12, walk-forward over 347,414 ATP and 289,906 WTA matches from 2015.
* **Result** It does not. ATP Brier 0.2409 against Elo's 0.2023; WTA 0.2555 against 0.1985. It does beat
  the Gen-1 structural model (0.2696 ATP) comfortably.
* **Why rejected** Serve statistics exist for 78-81% of tour-level matches but only 4.6% of ITF ones, and
  the universe is 61% ITF. A structural model with no observations for most of the board cannot compete
  with a rating that updates on every result.
* **What replaced it** The uncertainty-weighted blend, which shrinks the structural point probabilities
  toward the rating-implied ones in proportion to evidence. That version does beat Elo, narrowly. The raw
  lane is retained and reported precisely so this failure stays visible.

---

## R-004 Lead-lag between related Kalshi tennis markets

* **Tested** 2026-09-12.
* **Status** **Not rejected: not measurable.** Of 140 physical matches quoted in the archive, exactly
  **2** had two or more market families quoted simultaneously, yielding **1** usable family pair. That
  cannot distinguish a lead from noise.
* **Why it is a power problem, not a null** The cause is structural: 136 of 137 matches on the captured
  board had exactly two open contracts, the two sides of the match winner. There is no derivative present
  to lag behind anything.
* **Retest justified?** Yes, once the archive spans many more days or Kalshi lists more derivatives.

---

## R-005 A fresher Sackmann fork can fix source staleness

* **Tested** 2026-09-12.
* **Result** No. Of the twenty most recently pushed `tennis_atp` forks, the freshest was pushed
  2026-06-10 and every other one on 2026-06-08. Upstream `JeffSackmann/tennis_atp` and `tennis_wta` both
  return 404. Every fork froze when upstream disappeared.
* **Why rejected** The staleness is structural, not a bad fork choice. Chasing forks is wasted effort.
* **What replaced it** A crosswalk that admits the community mirror's ATP rows (3 months fresher) into
  the canonical id space, plus an ESPN results feed for current results on both tours.
