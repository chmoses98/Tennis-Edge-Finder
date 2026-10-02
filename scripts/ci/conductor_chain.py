#!/usr/bin/env python3
"""Successor hand-off for the self-chaining conductors (tennis-capture.yml, tennis-firstball.yml).

Each conductor loops ~5h40m and then dispatches its own successor; a cron tick every 5 h is the backstop. Both
workflows share a workflow-level `concurrency` group with cancel-in-progress: false, which allows ONE running and
ONE pending run: a newer pending run CANCELS the older pending one. A 5h40m conductor always overlaps a 5-hourly
cron tick, so the tick queued as the pending run and was then cancelled the moment the conductor dispatched its
successor. That produced a CANCELLED run for almost every cron tick (175 of 492 runs, 2026-09-11..10-02) while
nothing was wrong.

The fix is to hand off instead of racing: if a run of this workflow is already queued (the cron backstop, or a
successor dispatched by anyone else), that run IS the successor and nothing is dispatched. Otherwise the successor
is dispatched with a bounded retry. Dispositions (printed as JSON, written to the step summary):

  SUCCESSOR_ALREADY_QUEUED   another run of this workflow is queued behind us; it continues the chain (HEALTHY)
  DISPATCHED                 dispatch accepted first time (HEALTHY)
  RECOVERED_AFTER_RETRY      dispatch accepted after a transient failure (HEALTHY)
  DISPATCH_FAILED            every attempt failed; the 5-hourly cron backstop restarts the chain (DEGRADED)

A failed dispatch is DEGRADED, not FAILED: the cron backstop is the bounded recovery, and a red conductor run would
only re-report what the next cron tick repairs. It is never silent (::warning:: + step summary); before this file
the dispatch was a bare `curl` whose HTTP status was printed and ignored.

If listing the queued runs fails, the conductor dispatches anyway (the pre-existing behaviour): continuity of the
chain matters more than a possibly superseded pending run. This script never has bet authority and touches no
data; it only lists runs of, and dispatches, the workflow it was called from.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request

API = "https://api.github.com"
DEFAULT_BACKOFF = (0, 15, 45)          # seconds before attempt 1, 2, 3 -> at most ~1 minute of retrying


def queued_successors(runs: list[dict], own_run_id) -> list[dict]:
    """Runs of this workflow, other than our own, that have not completed. Workflow-level concurrency means no
    other run can be in progress while we are, so every such run is waiting to start after us."""
    own = str(own_run_id)
    return [r for r in runs or [] if str(r.get("id")) != own and r.get("status") != "completed"]


def dispatch_with_retry(post, backoff=None, sleep=None) -> tuple[bool, list[dict]]:
    """post() -> HTTP status (raises on transport errors). Bounded: len(backoff) attempts, no loop beyond that."""
    backoff = DEFAULT_BACKOFF if backoff is None else backoff
    sleep = time.sleep if sleep is None else sleep
    attempts = []
    for wait in backoff:
        if wait:
            sleep(wait)
        try:
            code = post()
        except Exception as e:                                               # noqa: BLE001 - recorded, not swallowed
            attempts.append({"http": getattr(e, "code", None), "error": str(e)[:200]})
            continue
        attempts.append({"http": code})
        if code in (200, 201, 204):
            return True, attempts
    return False, attempts


def handoff(list_runs, post, own_run_id, backoff=None, sleep=None) -> dict:
    """Decide and perform the hand-off. Pure apart from the two injected callables."""
    rep: dict = {"own_run_id": str(own_run_id)}
    try:
        runs = list_runs()
    except Exception as e:                                                   # noqa: BLE001 - recorded below
        runs = None
        rep["listing_error"] = str(e)[:200]
    queued = queued_successors(runs, own_run_id) if runs is not None else []
    if queued:
        rep.update(disposition="SUCCESSOR_ALREADY_QUEUED", health="HEALTHY",
                   successor_run_ids=[str(r.get("id")) for r in queued],
                   successor_events=[r.get("event") for r in queued])
        return rep
    ok, attempts = dispatch_with_retry(post, backoff=backoff, sleep=sleep)
    rep["attempts"] = attempts
    if ok:
        rep.update(disposition="DISPATCHED" if len(attempts) == 1 else "RECOVERED_AFTER_RETRY", health="HEALTHY")
    else:
        rep.update(disposition="DISPATCH_FAILED", health="DEGRADED",
                   recovery="the workflow's cron backstop starts a new conductor at its next tick")
    return rep


def summary_markdown(rep: dict, workflow: str) -> str:
    L = [f"### Conductor hand-off ({workflow})", "",
         f"* disposition: **{rep['disposition']}**", f"* health: **{rep['health']}**"]
    if rep.get("successor_run_ids"):
        L.append(f"* queued successor run(s): {', '.join(rep['successor_run_ids'])} "
                 f"(event: {', '.join(str(e) for e in rep.get('successor_events', []))}); no dispatch needed")
    if rep.get("attempts"):
        L.append(f"* dispatch attempts: {json.dumps(rep['attempts'])}")
    if rep.get("listing_error"):
        L.append(f"* could not list queued runs ({rep['listing_error']}); dispatched as before")
    if rep.get("recovery"):
        L.append(f"* recovery: {rep['recovery']}")
    return "\n".join(L) + "\n"


def _github(token: str):
    hdr = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}

    def get(url):
        with urllib.request.urlopen(urllib.request.Request(url, headers=hdr), timeout=20) as r:
            return json.load(r)

    def post(url, body):
        req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST", headers=hdr)
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    return get, post


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--workflow", required=True, help="workflow file name, e.g. tennis-capture.yml")
    ap.add_argument("--ref", required=True)
    ap.add_argument("--inputs", default="{}", help="JSON object of workflow_dispatch inputs for the successor")
    a = ap.parse_args(argv)
    token, repo, run_id = os.environ.get("GH_TOKEN"), os.environ.get("GITHUB_REPOSITORY"), os.environ.get("GITHUB_RUN_ID")
    if not token or not repo:
        print("::error::conductor hand-off needs GH_TOKEN and GITHUB_REPOSITORY")
        return 1
    get, post = _github(token)
    base = f"{API}/repos/{repo}/actions/workflows/{a.workflow}"
    rep = handoff(lambda: get(f"{base}/runs?per_page=20&exclude_pull_requests=true")["workflow_runs"],
                  lambda: post(f"{base}/dispatches", {"ref": a.ref, "inputs": json.loads(a.inputs)}),
                  run_id)
    print(json.dumps(rep))
    if rep["health"] == "DEGRADED":
        print(f"::warning::conductor successor dispatch failed after {len(rep.get('attempts', []))} attempts; "
              "the cron backstop will restart the chain")
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a") as f:
            f.write(summary_markdown(rep, a.workflow))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
