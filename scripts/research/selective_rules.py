#!/usr/bin/env python3
"""Candidate ABSTENTION rules: derived on discovery, checked on validation, then read once on holdout.

The order matters and is the whole method. A rule is written from the discovery block alone. If it does
not survive the validation block it is dropped there and never reaches the holdout. Only rules that
survive both are read on the holdout, once, and whatever the holdout says is the answer -- including
"this was noise".

Every rule here is a filter on top of the ordinary requirement that the fee-adjusted edge be positive.
Selecting nothing is a legitimate output of every one of them.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

RULES = {
    # name: (prose, predicate)
    "R1_moderate_nonitf_evenmoney": (
        "fee-adjusted edge 3-15c, not an ITF event, ask between 35c and 65c, and the market has not "
        "already drifted toward our side in the last six hours",
        lambda d: (d.fee_adjusted_edge.between(0.03, 0.15) & (d.level != "ITF") &
                   d.kalshi_ask.between(0.35, 0.65) &
                   (np.sign(d.p_fair - d.kalshi_mid) * d.mv_move_6h.fillna(0.0) <= 0.005))),
    "R2_moderate_edge_only": (
        "fee-adjusted edge between 3c and 15c and nothing else",
        lambda d: d.fee_adjusted_edge.between(0.03, 0.15)),
    "R3_nonitf_only": (
        "any positive fee-adjusted edge outside ITF",
        lambda d: d.level != "ITF"),
    "R4_evenmoney_only": (
        "any positive fee-adjusted edge with an ask between 40c and 60c",
        lambda d: d.kalshi_ask.between(0.40, 0.60)),
    "R5_not_already_moved": (
        "any positive fee-adjusted edge where the market has not drifted toward us in six hours",
        lambda d: np.sign(d.p_fair - d.kalshi_mid) * d.mv_move_6h.fillna(0.0) <= 0.005),
    "R6_evidence_and_quality": (
        "positive edge with at least 1,500 serve points on the thinner player and data quality >= 0.7",
        lambda d: (d.ev_min >= 1500) & (d.data_quality >= 0.7)),
}


def boot_ci(x, n_boot=6000, seed=20260914):
    x = np.asarray(x, float)
    if len(x) < 3:
        return [None, None]
    rng = np.random.default_rng(seed)
    m = x[rng.integers(0, len(x), size=(n_boot, len(x)))].mean(axis=1)
    return [float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))]


def report(d, sel, block, universe_n):
    if not len(sel):
        return {"block": block, "n": 0, "selection_rate": 0.0}
    cost = sel.kalshi_ask + sel.fee
    return {"block": block, "n": int(len(sel)),
            "selection_rate": float(len(sel) / universe_n),
            "hit_rate": float(sel.y.mean()), "avg_ask": float(sel.kalshi_ask.mean()),
            "claimed_edge": float(sel.fee_adjusted_edge.mean()),
            "realised_edge": float(sel.pnl.mean()), "ci": boot_ci(sel.pnl.to_numpy(float)),
            "roi": float(sel.pnl.sum() / cost.sum()),
            "model_brier": float(np.mean((sel.p_fair - sel.y) ** 2)),
            "market_brier": float(np.mean((sel.kalshi_mid - sel.y) ** 2)),
            "model_log_loss": float(-np.mean(sel.y * np.log(np.clip(sel.p_fair, 1e-9, 1)) +
                                             (1 - sel.y) * np.log(np.clip(1 - sel.p_fair, 1e-9, 1)))),
            "market_log_loss": float(-np.mean(sel.y * np.log(np.clip(sel.kalshi_mid, 1e-9, 1)) +
                                              (1 - sel.y) * np.log(np.clip(1 - sel.kalshi_mid, 1e-9, 1)))),
            "worst_drawdown": float((sel.pnl.cumsum() - sel.pnl.cumsum().cummax()).min())}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=os.path.join(PROJ, "research", "selector", "scored.parquet"))
    ap.add_argument("--discovery-end", default="2026-09-02")
    ap.add_argument("--validation-end", default="2026-09-06")
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "selector", "rules.json"))
    a = ap.parse_args()
    d = pd.read_parquet(a.data)
    blocks = {"discovery": d[d.sched_date <= a.discovery_end],
              "validation": d[(d.sched_date > a.discovery_end) & (d.sched_date <= a.validation_end)],
              "holdout": d[d.sched_date > a.validation_end]}

    out = {"generated_at": datetime.now(timezone.utc).isoformat(),
           "method": "derived on discovery, checked on validation, holdout read once at the end",
           "block_sizes": {k: int(len(v)) for k, v in blocks.items()}, "rules": {}}
    for name, (prose, pred) in RULES.items():
        r = {"rule": prose, "blocks": {}}
        survived = True
        for block in ("discovery", "validation", "holdout"):
            b = blocks[block]
            sel = b[(b.fee_adjusted_edge > 0) & pred(b)]
            rep = report(d, sel, block, len(b))
            r["blocks"][block] = rep
            if block == "validation":
                # a rule earns its holdout read by not being negative on validation
                survived = bool(rep.get("n", 0) >= 10 and (rep.get("realised_edge") or -1) > 0)
                r["survived_validation"] = survived
        if not survived:
            r["blocks"]["holdout"] = {"block": "holdout", "withheld": True,
                                      "reason": "did not survive validation; the holdout was not used to rescue it"}
        out["rules"][name] = r

    json.dump(out, open(a.out, "w"), indent=1, default=str)
    for name, r in out["rules"].items():
        print(f"\n{name}: {r['rule']}")
        for block in ("discovery", "validation", "holdout"):
            b = r["blocks"][block]
            if b.get("withheld"):
                print(f"  {block:11s} WITHHELD ({b['reason']})")
            elif b.get("n"):
                print(f"  {block:11s} n={b['n']:4d} rate={b['selection_rate']:.3f} hit={b['hit_rate']:.3f} "
                      f"claimed={b['claimed_edge']:+.4f} realised={b['realised_edge']:+.4f} "
                      f"ci=[{b['ci'][0]:+.3f},{b['ci'][1]:+.3f}] roi={b['roi']:+.3f}")
            else:
                print(f"  {block:11s} n=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
