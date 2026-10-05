#!/usr/bin/env python3
"""A FULL, stateless snapshot of every open match-scope tennis market, taken immediately before pricing.

Why (2026-10-05)
----------------
The capture conductor writes INCREMENTAL quote snapshots (only markets whose quote changed). A market that
settles simply stops appearing; nothing marks it closed. `run_tennis.py` took each ticker's newest record from
the last twelve capture files, found it "active", and priced it: 2,695 ledger rows (15.6% of everything that
later settled, mostly ITF) were priced AFTER Kalshi had already settled the market, and it was still
happening daily. RUN TENNIS also reached its slate 30+ minutes after the newest capture pass, so every slate
row was STALE by the 30-minute quote SLA.

This script is the fix's input: one read-only pass over the open markets of every MATCH-scope series,
written as a full snapshot (`snapshot_kind: "full_open"`). It touches no shared state (the conductor's
`state.json`, trade-tape cursor and fingerprints are left alone), so it cannot race the capture conductor.
`run_tennis.py` treats it as AUTHORITATIVE when it is fresh: a ticker absent from a fresh full open
snapshot is not open, whatever an older incremental record says.

Output: <out>/<YYYY-MM-DD>/<run_id>.open_snapshot.jsonl.gz and <run_id>.open_snapshot.manifest.json
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import sys
import time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__)); PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)
from tennis_edge.kalshi.client import KalshiClient  # noqa: E402
from tennis_edge.kalshi.families import FAMILIES, SERIES  # noqa: E402

MATCH_SCOPE_SERIES = sorted(tk for tk, (fam, *_r) in SERIES.items() if FAMILIES[fam]["scope"] == "MATCH")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(PROJ, "data", "kalshi", "run_snapshots"))
    ap.add_argument("--rps", type=float, default=5.0)
    a = ap.parse_args()
    t0 = time.time()
    now = datetime.now(timezone.utc)
    run_id = now.strftime("%Y%m%dT%H%M%SZ")
    day = os.path.join(a.out, now.strftime("%Y-%m-%d"))
    os.makedirs(day, exist_ok=True)
    c = KalshiClient(rps=a.rps)
    failures, n = [], 0
    path = os.path.join(day, f"{run_id}.open_snapshot.jsonl.gz")
    with gzip.open(path, "wt") as f:
        for tk in MATCH_SCOPE_SERIES:
            items, ok, info = c.markets(series_ticker=tk, status="open", limit=1000, max_pages=20)
            if not ok:
                failures.append({"series": tk, "info": str(info)[:300]})
            for m in items or []:
                f.write(json.dumps({"run_id": run_id, "captured_at": datetime.now(timezone.utc).isoformat(),
                                    "snapshot_kind": "full_open", **m}) + "\n")
                n += 1
    manifest = {"run_id": run_id, "started_at": now.isoformat(), "finished_at": datetime.now(timezone.utc).isoformat(),
                "seconds": round(time.time() - t0, 1), "series": len(MATCH_SCOPE_SERIES), "markets": n,
                "failures": failures, "complete": not failures}
    json.dump(manifest, open(os.path.join(day, f"{run_id}.open_snapshot.manifest.json"), "w"), indent=1)
    print(json.dumps(manifest))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
