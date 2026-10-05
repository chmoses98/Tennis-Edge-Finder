#!/usr/bin/env python3
"""Independent sports truth + exchange reconciliation for every settled prediction (TENNIS-8 / TENNIS-9).

Reads the settlement tables and the ledger, resolves each settled prediction's match in the canonical results
table (data/processed/matches.parquet -- Sackmann / TML / ESPN, never Kalshi), and writes ONE derived snapshot
data/research/sports_truth/<run>.jsonl.gz (append-only directory; the newest file is current). No settlement
row and no ledger row is edited.
"""
from __future__ import annotations

import argparse, glob, gzip, json, os, sys
from collections import Counter
from datetime import date, datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

import pandas as pd  # noqa: E402

from tennis_edge.ledger.sports_truth import ResultsIndex, reconcile_match_winner, ticker_date  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--research", default=os.path.join(PROJ, "data", "research"))
    ap.add_argument("--matches", default=os.path.join(PROJ, "data", "processed", "matches.parquet"))
    a = ap.parse_args()
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    settled = {}
    for f in sorted(glob.glob(os.path.join(a.research, "settlements", "*.jsonl"))):
        for line in open(f):
            try:
                r = json.loads(line)
            except ValueError:
                continue
            settled.setdefault(r["prediction_id"], r)
    ledger = {}
    for f in sorted(glob.glob(os.path.join(a.research, "ledger", "*.jsonl"))):
        for line in open(f):
            r = json.loads(line)
            if r["prediction_id"] in settled:
                ledger[r["prediction_id"]] = r
    cols = ["tour", "tourney_date", "canonical_id_status", "canonical_winner_id", "canonical_loser_id", "outcome_type",
            "score_raw", "games_w", "games_l", "sets_w", "sets_l", "source_label", "match_key", "tourney_name", "level_canonical"]
    m = pd.read_parquet(a.matches, columns=cols)
    manifest = json.load(open(os.path.join(os.path.dirname(a.matches), "build_manifest.json")))
    idx = ResultsIndex(m, since=date(2026, 8, 1))
    out, stats, rec_stats = [], Counter(), Counter()
    by_level = {}
    for pid, s in settled.items():
        r = ledger.get(pid)
        if r is None:
            continue
        on = ticker_date(r.get("event_ticker") or r.get("match_id")) or datetime.fromisoformat(r["generated_at_utc"]).date()
        doubles = "|" in str(r.get("player_a_id") or "")
        t = idx.resolve(r.get("tour"), None if doubles else r.get("player_a_id"), None if doubles else r.get("player_b_id"),
                        r.get("level") or "OTHER", on)
        rec = None
        if r.get("family") == "MATCH_WINNER" and s.get("exchange"):
            subj = r.get("player_a_id") if r.get("subject") == r.get("player_a") else r.get("player_b_id")
            rec = reconcile_match_winner(t, s["exchange"], subj)
            rec_stats[rec["status"]] += 1
        stats[t.status] += 1
        lv = by_level.setdefault(f"{r.get('tour')}|{r.get('level')}", Counter())
        lv[t.status] += 1
        out.append({"run_id": run_id, "prediction_id": pid, "ticker": r.get("ticker"), "match_id": r.get("match_id"),
                    "family": r.get("family"), "tour": r.get("tour"), "level": r.get("level"), "gradeable": s.get("gradeable"),
                    "independent": t.to_dict(), "reconciliation": rec,
                    "provenance": {"matches_sha256": manifest.get("matches_sha256"), "build_version": manifest.get("build_version"),
                                   "built_at": manifest.get("built_at")}})
    os.makedirs(os.path.join(a.research, "sports_truth"), exist_ok=True)
    with gzip.open(os.path.join(a.research, "sports_truth", f"{run_id}.jsonl.gz"), "wt") as f:
        for x in out:
            f.write(json.dumps(x, default=str) + "\n")
    summary = {"run_id": run_id, "settled": len(out), "by_status": dict(stats), "reconciliation": dict(rec_stats),
               "by_level": {k: dict(v) for k, v in sorted(by_level.items())}}
    json.dump(summary, open(os.path.join(a.research, "sports_truth", "latest_summary.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in summary.items() if k != "by_level"}))


if __name__ == "__main__":
    main()
