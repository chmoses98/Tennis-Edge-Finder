#!/usr/bin/env python3
"""Restore today's rolling append-only day files from the evidence branch before a writer appends to them.

Why (2026-10-07). The capture conductor appends Bovada/Smarkets observations and the dislocation ledger to
`research/external/{market,dislocations}/<UTC day>.jsonl` and publishes the whole day file after every pass. Each
new conductor run started with an EMPTY local day file, so its first publish REPLACED everything earlier conductors
had written that day: on 2026-10-06 the branch tip held only rows from 13:50Z on (the 00:00-13:44Z rows survive
only in git history). Restoring the tip's copy first makes every conductor CONTINUE the day's hash chain instead.

A local file that already exists is never touched (it is this writer's own continuation). Missing on the branch ->
nothing to restore (a new day starts at GENESIS, as before). Reads only; publishes nothing.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime, timezone


def restore(repo: str, branch: str, prefix: str, rel_dirs, day: str) -> dict:
    out = {}
    for rel in rel_dirs:
        local = os.path.join(repo, "data", rel, f"{day}.jsonl")
        if os.path.exists(local):
            out[rel] = "local copy kept"
            continue
        spec = f"origin/{branch}:{prefix}/data/{rel}/{day}.jsonl"
        r = subprocess.run(["git", "show", spec], cwd=repo, capture_output=True)
        if r.returncode != 0:
            out[rel] = "absent on branch (new day)"
            continue
        os.makedirs(os.path.dirname(local), exist_ok=True)
        tmp = local + ".part"
        open(tmp, "wb").write(r.stdout)
        os.replace(tmp, local)
        out[rel] = f"restored {len(r.stdout)} bytes"
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.getcwd())
    ap.add_argument("--branch", default="tennis-data")
    ap.add_argument("--prefix", default="tennis-edge-finder")
    # the market store is sharded per pass (schema.ExternalStore(shard=...)); only the dislocation ledger is a day file
    ap.add_argument("--dirs", nargs="+", default=["research/external/dislocations"])
    ap.add_argument("--day", default=None, help="UTC day (default today)")
    a = ap.parse_args()
    day = a.day or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for k, v in restore(os.path.abspath(a.repo), a.branch, a.prefix, a.dirs, day).items():
        print(f"{k}/{day}.jsonl: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
