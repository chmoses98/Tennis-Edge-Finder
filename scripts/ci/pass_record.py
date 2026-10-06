#!/usr/bin/env python3
"""Write one capture-conductor pass record: wall-clock seconds per step, start-to-start gap, intended sleep, overrun.

    pass_record.py --out data/kalshi/capture_passes --pass 3 --run-id 123 --start-ms 1700000000000 \\
        --prev-start-ms 1699999400000 --interval 600 --sleep 412 fetch=3.1 restore=0.2 capture=95.0 ...

Records land in <out>/<UTC day>/<pass start stamp>.pass.json and are published with the next capture publish. They
are the evidence TENNIS-5's background_capture_health reads for step durations (2026-10-07)."""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone


def build(pass_no, run_id, start_ms, prev_start_ms, interval, sleep_s, steps: dict, end_ms) -> dict:
    start = datetime.fromtimestamp(start_ms / 1000, timezone.utc)
    work = (end_ms - start_ms) / 1000
    return {"pass": pass_no, "conductor_run_id": run_id, "started_at": start.isoformat(),
            "finished_work_at": datetime.fromtimestamp(end_ms / 1000, timezone.utc).isoformat(),
            "steps_s": {k: round(v, 2) for k, v in steps.items()}, "work_s": round(work, 2),
            "interval_s": interval, "intended_sleep_s": sleep_s,
            "overrun_s": round(max(0.0, work - interval), 2),
            "start_to_start_s": None if not prev_start_ms else round((start_ms - prev_start_ms) / 1000, 2)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--pass", dest="pass_no", type=int, required=True)
    ap.add_argument("--run-id", default="")
    ap.add_argument("--start-ms", type=int, required=True)
    ap.add_argument("--prev-start-ms", type=int, default=0)
    ap.add_argument("--end-ms", type=int, default=0)
    ap.add_argument("--interval", type=int, required=True)
    ap.add_argument("--sleep", type=int, default=0)
    ap.add_argument("steps", nargs="*", help="name=seconds")
    a = ap.parse_args()
    steps = {}
    for kv in a.steps:
        k, _, v = kv.partition("=")
        try:
            steps[k] = float(v)
        except ValueError:
            continue
    end_ms = a.end_ms or int(datetime.now(timezone.utc).timestamp() * 1000)
    rec = build(a.pass_no, a.run_id, a.start_ms, a.prev_start_ms, a.interval, a.sleep, steps, end_ms)
    day = rec["started_at"][:10]
    d = os.path.join(a.out, day)
    os.makedirs(d, exist_ok=True)
    stamp = datetime.fromisoformat(rec["started_at"]).strftime("%Y%m%dT%H%M%SZ")
    json.dump(rec, open(os.path.join(d, f"{stamp}.pass.json"), "w"), indent=1)
    print(json.dumps(rec))
    return 0


if __name__ == "__main__":
    sys.exit(main())
