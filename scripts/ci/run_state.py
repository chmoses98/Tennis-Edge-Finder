#!/usr/bin/env python3
"""Final run-state verdicts for workflows whose individual steps deliberately keep going.

Each workflow below does its work, keeps going past nonfatal problems, publishes, and then calls this script
ONCE as its last step. The script classifies the run, writes the step summary, and exits 1 only for FAILED:

  HEALTHY    the responsibility was met
  DEGRADED   met, with a nonfatal problem worth recording (::warning:: + step summary; the run stays green)
  FAILED     the responsibility was not met (::error:: + step summary + exit 1)

Subcommands:

  capture    Kalshi capture conductor (tennis-capture.yml). One JSON line per pass in --pass-log:
             {"pass", "capture_rc", "publish_rc", "scan_rc", "scan_publish_rc"}. A pass SUCCEEDS when
             capture_tennis.py exits 0 (complete) or 2 (partial, manifest written) AND its publish succeeded.
             No successful pass in a whole conductor (~15 attempts over ~5.5 h) = FAILED: the capture the
             conductor exists for did not happen. A missing or empty pass log is FAILED too (fail closed: no
             evidence that anything was captured). Any failed or partial pass, or a failed external scan, = DEGRADED.
  espn       ESPN current results in tennis-bootstrap.yml. ESPN is the only reachable feed with CURRENT results
             for both tours and tennis_edge/data/build.py builds the production table from the newest ESPN run.
             Results that were fetched but could not be published after publish_branch.py's own 8 retries =
             FAILED (a required production input was lost). A failed fetch = DEGRADED: it is an external feed,
             the build falls back to the previous ESPN snapshot, TENNIS-14 allows 8 days, and tomorrow's run
             retries.
  core       RUN TENNIS core stages (projections run_tennis.py, settlement settle_ledger.py). Any core stage that
             exited non-zero = FAILED. The research producers keep their own ::error:: + TENNIS-15/16 recording
             and are not judged here.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

SUCCESS_CAPTURE_RCS = (0, 2)          # capture_tennis.py: 0 = complete, 2 = partial (manifest["incomplete"])


def read_pass_log(path: str) -> list[dict] | None:
    """Pass records, or None when the log is missing. A malformed line is kept as a failed pass."""
    if not path or not os.path.exists(path):
        return None
    out = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            try:
                out.append(json.loads(line))
            except ValueError:
                out.append({"malformed": line.strip()[:200]})
    return out


def classify_capture(passes: list[dict] | None) -> dict:
    if not passes:
        return {"health": "FAILED", "passes": 0, "successful": 0,
                "reason": "no capture pass recorded (pass log missing or empty)"}
    ok = [p for p in passes if p.get("capture_rc") in SUCCESS_CAPTURE_RCS and p.get("publish_rc") == 0]
    partial = [p for p in ok if p.get("capture_rc") == 2]
    ok_ids = {id(p) for p in ok}
    failed = [p for p in passes if id(p) not in ok_ids]
    scan_fail = [p for p in passes if p.get("scan_rc", 0) != 0 or p.get("scan_publish_rc", 0) != 0]
    rep = {"passes": len(passes), "successful": len(ok), "partial": len(partial), "failed": len(failed),
           "external_scan_failures": len(scan_fail),
           "failed_passes": [p.get("pass", p.get("malformed")) for p in failed][:20]}
    if not ok:
        rep.update(health="FAILED", reason=f"all {len(passes)} capture passes failed (capture crashed or publish failed)")
    elif failed or partial or scan_fail:
        rep.update(health="DEGRADED", reason=f"{len(ok)}/{len(passes)} passes captured and published; "
                                             f"{len(failed)} failed, {len(partial)} partial, "
                                             f"{len(scan_fail)} external-scan failures")
    else:
        rep.update(health="HEALTHY", reason=f"all {len(passes)} passes captured and published")
    return rep


def classify_espn(acquire_outcome: str, publish_rc) -> dict:
    rep = {"acquire_outcome": acquire_outcome, "publish_rc": publish_rc}
    try:
        rc = int(publish_rc)
    except (TypeError, ValueError):
        rep.update(health="FAILED", reason=f"ESPN publish step recorded no exit code ({publish_rc!r})")
        return rep
    if rc != 0:
        rep.update(health="FAILED", reason=f"ESPN results could not be published to tennis-data (exit {rc}) after "
                                           "publish_branch.py's retries; the production build loses current results")
    elif acquire_outcome != "success":
        rep.update(health="DEGRADED", reason="ESPN fetch failed; the build uses the previous ESPN snapshot "
                                             "(TENNIS-14 allows 8 days) and tomorrow's run retries")
    else:
        rep.update(health="HEALTHY", reason="ESPN results fetched and published (or not requested by this trigger)")
    return rep


def classify_core(failed_stages: list[str]) -> dict:
    failed = [s for s in failed_stages if s]
    if failed:
        return {"health": "FAILED", "failed_stages": failed,
                "reason": f"core stage(s) exited non-zero: {', '.join(failed)} (outputs were still published)"}
    return {"health": "HEALTHY", "failed_stages": [], "reason": "projections and settlement completed"}


def emit(kind: str, rep: dict) -> int:
    print(json.dumps({"kind": kind, **rep}, default=str))
    if rep["health"] == "FAILED":
        print(f"::error::{kind}: FAILED - {rep['reason']}")
    elif rep["health"] == "DEGRADED":
        print(f"::warning::{kind}: DEGRADED - {rep['reason']}")
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a") as f:
            f.write(f"### {kind}: {rep['health']}\n\n{rep['reason']}\n\n```json\n{json.dumps(rep, default=str)}\n```\n")
    return 1 if rep["health"] == "FAILED" else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("capture")
    c.add_argument("--pass-log", required=True)
    e = sub.add_parser("espn")
    e.add_argument("--acquire-outcome", required=True)
    e.add_argument("--publish-rc", default="")
    k = sub.add_parser("core")
    k.add_argument("--failed", default="", help="space-separated names of core stages that exited non-zero")
    a = ap.parse_args(argv)
    if a.cmd == "capture":
        return emit("capture conductor", classify_capture(read_pass_log(a.pass_log)))
    if a.cmd == "espn":
        return emit("ESPN current results", classify_espn(a.acquire_outcome, a.publish_rc))
    return emit("RUN TENNIS core", classify_core(a.failed.split()))


if __name__ == "__main__":
    raise SystemExit(main())
