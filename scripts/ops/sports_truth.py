#!/usr/bin/env python3
"""Independent sports truth + exchange reconciliation for every settled prediction (TENNIS-8 / TENNIS-9).

Reads the settlement tables and the ledger, resolves each settled prediction's match in the canonical results
table (data/processed/matches.parquet -- Sackmann / TML / ESPN, never Kalshi), and writes ONE derived snapshot
data/research/sports_truth/<run>.jsonl.gz (append-only directory). No settlement row and no ledger row is edited.

Every run re-resolves EVERY settled prediction against the table it was given, so a prediction that was NOT_COVERED or
PENDING_RESULT in an earlier snapshot becomes RESOLVED in the first snapshot built after its result is published. Since
2026-10-07 each snapshot also writes:
  <run>.meta.json           exact provenance (source snapshot ids incl. ESPN, canonical hash) and its ordering stamp;
  resolution_log/<run>.jsonl  append-only: the first run that independently resolved each prediction (latency evidence);
  <run>.summary.json        summary incl. the prospective study, source freshness and resolution latency;
  latest_summary.json       advisory copy, advanced only when this snapshot's source evidence is at least as new as the
                            current one. Readers use truth_freshness.current_snapshot (newest source, then newest run).
It is run by RUN TENNIS and by the bounded truth refresh that follows every ESPN publish (tennis-truth-refresh.yml).
"""
from __future__ import annotations

import argparse, glob, gzip, json, os, sys
from collections import Counter
from datetime import date, datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

import pandas as pd  # noqa: E402

from tennis_edge.ledger.sports_truth import ResultsIndex, reconcile_match_winner, ticker_date  # noqa: E402
from tennis_edge.ledger import truth_freshness as tf  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--research", default=os.path.join(PROJ, "data", "research"))
    ap.add_argument("--matches", default=os.path.join(PROJ, "data", "processed", "matches.parquet"))
    ap.add_argument("--as-of", default=None, help="run date (YYYY-MM-DD); default today UTC")
    a = ap.parse_args()
    now = datetime.now(timezone.utc)
    run_id = now.strftime("%Y%m%dT%H%M%SZ")
    as_of = date.fromisoformat(a.as_of) if a.as_of else now.date()
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
    idx = ResultsIndex(m, since=date(2026, 8, 1), as_of=as_of)
    provenance = {"matches_sha256": manifest.get("matches_sha256"), "build_version": manifest.get("build_version"),
                  "built_at": manifest.get("built_at"),
                  "espn_runs": sorted({v.get("run") for k, v in (manifest.get("sources") or {}).items()
                                       if k.startswith("espn") and isinstance(v, dict) and v.get("run")})}
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
                    "independent": t.to_dict(), "reconciliation": rec, "provenance": provenance})
    tdir = os.path.join(a.research, "sports_truth")
    os.makedirs(tdir, exist_ok=True)
    with gzip.open(os.path.join(tdir, f"{run_id}.jsonl.gz"), "wt") as f:
        for x in out:
            f.write(json.dumps(x, default=str) + "\n")
    meta = {"run_id": run_id, "source_stamp": tf.source_stamp(manifest), "provenance": provenance,
            "sources": {k: v.get("run") for k, v in (manifest.get("sources") or {}).items() if isinstance(v, dict) and v.get("run")}}
    json.dump(meta, open(os.path.join(tdir, f"{run_id}.meta.json"), "w"), indent=1)
    resolution = tf.update_resolution_log(os.path.join(tdir, "resolution_log"), out, ledger, run_id, provenance)
    summary = {"run_id": run_id, "source_stamp": meta["source_stamp"], "settled": len(out), "by_status": dict(stats),
               "reconciliation": dict(rec_stats), "by_level": {k: dict(v) for k, v in sorted(by_level.items())},
               "freshness": tf.freshness(idx, manifest, as_of), "resolution": resolution,
               "prospective_v2": tf.prospective_summary(out, ledger, as_of)}
    json.dump(summary, open(os.path.join(tdir, f"{run_id}.summary.json"), "w"), indent=1, default=str)
    cur = tf.current_snapshot(tdir)
    if cur and os.path.basename(cur).startswith(run_id):
        json.dump(summary, open(os.path.join(tdir, "latest_summary.json"), "w"), indent=1, default=str)
    else:
        print(f"::notice::sports truth {run_id} used older sources than the current snapshot {os.path.basename(cur or '')}; "
              "latest_summary.json left as is")
    pv = summary["prospective_v2"]
    if pv["n_stale_unresolved_tour_level"]:
        print(f"::warning::{pv['n_stale_unresolved_tour_level']} tour-level prospective predictions are still unresolved more "
              f"than {tf.TOUR_PUBLICATION_WINDOW_DAYS} days after the match although ESPN covers the level")
    print(json.dumps({k: summary[k] for k in ("run_id", "settled", "by_status", "reconciliation")}))
    print(json.dumps({k: pv[k] for k in ("predictions_with_v2_and_incumbent", "independently_resolved_predictions",
                                         "independently_settled_matches", "by_status", "n_stale_unresolved_tour_level")}))


if __name__ == "__main__":
    main()
