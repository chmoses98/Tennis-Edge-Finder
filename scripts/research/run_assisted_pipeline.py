#!/usr/bin/env python3
"""The scheduled half of the assisted lane: track start, canonical ledgers, settlement, scorecard.

  1. write TRACK_START.json once (the first production run fixes the track's effective start)
  2. compile the write-once records into the append-only canonical ledgers
     (assisted_decisions.jsonl, assisted_wagers.jsonl, assisted_postmortems.jsonl, assisted_evidence.jsonl)
  3. append settlement rows for newly settled markets (assisted_settlements.jsonl)
  4. rebuild the scorecard (SCORECARD.json / SCORECARD.md) and record PIPELINE_STATUS.json for TENNIS-16

It reads frozen-model outputs only through the decisions people recorded; it fits, tunes and writes no
model, candidate, threshold or experiment start. A failure is recorded (TENNIS-16 then FAILS) and never
blocks settlement or publication of anything else.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import traceback
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.assisted.health import PIPELINE_STATUS_FILE                        # noqa: E402
from tennis_edge.assisted.scorecard import build_scorecard, write_scorecard         # noqa: E402
from tennis_edge.assisted.settle import settle                                      # noqa: E402
from tennis_edge.assisted.store import CANONICAL, compile_canonical, ensure_track_start  # noqa: E402
from tennis_edge.producers.records import code_sha                                  # noqa: E402


def _status(root: str, update: dict) -> None:
    p = os.path.join(root, PIPELINE_STATUS_FILE)
    try:
        doc = json.load(open(p))
    except (OSError, ValueError):
        doc = {}
    doc.update(update)
    os.makedirs(root, exist_ok=True)
    with open(p, "w") as f:
        json.dump(doc, f, indent=1, default=str)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--data-root", default=os.path.join(PROJ, "data"))
    ap.add_argument("--store", default=os.path.join(PROJ, "data", "research", "assisted_decisions"))
    ap.add_argument("--scorecard-out", action="append",
                    help="directory for SCORECARD.json/md (repeatable); default research/assisted_handicapping")
    ap.add_argument("--write-track-start", action="store_true",
                    help="PRODUCTION ONLY (RUN TENNIS): write TRACK_START.json if it does not exist yet. Local and "
                         "test runs never pass this, so they cannot start the production track")
    a = ap.parse_args(argv)
    now = datetime.now(timezone.utc)
    outs = a.scorecard_out or [os.path.join(PROJ, "research", "assisted_handicapping")]
    try:
        started = ensure_track_start(a.store, started_at=now.isoformat(), main_sha=code_sha(PROJ)) if a.write_track_start else None
        compiled = {k: compile_canonical(a.store, k) for k in CANONICAL}
        settled = settle(a.store, a.data_root, now=now)
        sc = build_scorecard(a.store, now=now)
        for o in outs:
            write_scorecard(sc, o)
        violations = [v for c in compiled.values() for v in c["violations"]]
        _status(a.store, {"last_run_at": now.isoformat(), "code_sha": code_sha(PROJ), "track_start_written": bool(started),
                          "compiled": {k: {kk: vv for kk, vv in c.items() if kk != "violations"} for k, c in compiled.items()},
                          "integrity_violations": violations, "settle": settled,
                          "scorecard_content_sha256": sc["content_sha256"], "evidence_state": sc["evidence_state"]})
        print(json.dumps({"track_start_written": bool(started), "compiled": {k: c["appended"] for k, c in compiled.items()},
                          "integrity_violations": len(violations), "settle": settled,
                          "evidence_state": sc["evidence_state"]}, indent=1, default=str))
        return 0
    except Exception as e:                                                            # noqa: BLE001
        _status(a.store, {"last_error_at": now.isoformat(), "last_error": f"{type(e).__name__}: {e}\n{traceback.format_exc()[-1500:]}"})
        print(f"::error::assisted pipeline failed: {type(e).__name__}: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
