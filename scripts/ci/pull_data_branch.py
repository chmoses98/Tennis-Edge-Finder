#!/usr/bin/env python3
"""Unpack the evidence a RUN TENNIS needs from `tennis-data` into ./data -- without downloading the rest.

Replaces `git fetch --depth=1 origin tennis-data && git archive ... | tar -x --strip-components=1`, which
downloaded and unpacked the ENTIRE evidence tree (8+ GB, 100k+ files, ~8 minutes) on every run.

What is skipped, and why that is safe (each item verified against every reader in tennis_edge/ and scripts/):
  * research/horizons, research/timing -- per-run derived snapshots; nothing reads an older run's copy
  * research/clv -- only the NEWEST run is read (settlement_stats, harvest); older runs are skipped
  * research/external/raw -- archived raw venue payloads; nothing in RUN TENNIS reads them
  * kalshi/capture/*.trades.jsonl.gz -- the trade tape; no RUN TENNIS step reads it
  * kalshi/discovery -- all but the two newest runs (only the newest is ever read)
  * sources -- all but the newest run of each source the canonical build reads (manifests of every run kept)
Nothing is deleted from the branch; this only limits what this runner unpacks. Prefix handling is unchanged:
`tennis-edge-finder/data/X` on the branch lands at `./data/X`.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone

PREFIX = "tennis-edge-finder/data/"
#: written into <dest>/ after every pull (never published: it describes this runner, not the evidence)
PULL_RECORD = ".pull_record.json"
SOURCE_SUBS = ("sackmann/tennis_atp/", "sackmann/tennis_wta/", "tml/", "tennis_data/",
               "tennis_data_mirrors/gmalbert__tennis-predictions/")


def sh(cmd, cwd=None, check=True, capture=False):
    print("+", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, cwd=cwd, check=False, text=True, capture_output=capture)
    if check and r.returncode != 0:
        print((r.stdout or "")[-2000:], (r.stderr or "")[-2000:])
        raise SystemExit(f"command failed ({r.returncode}): {' '.join(cmd)}")
    return r


def patterns(paths: list[str], profile: str = "run_tennis") -> list[str]:
    """Non-cone sparse-checkout patterns for the files a run needs, computed from the branch's file list."""
    runs_with: dict[str, set] = {s: set() for s in SOURCE_SUBS}
    espn_runs, espn_quarantined, disc, clv = set(), set(), set(), []
    for p in paths:
        if not p.startswith(PREFIX):
            continue
        rel = p[len(PREFIX):]
        m = re.match(r"sources/(\d{8}T\d{6}Z)/(.*)$", rel)
        if m:
            for s in SOURCE_SUBS:
                if m.group(2).startswith(s):
                    runs_with[s].add(m.group(1))
            continue
        m = re.match(r"sources/espn/([^/]+)/(.*)$", rel)
        if m:
            if m.group(2) == "QUARANTINED.md":
                espn_quarantined.add(m.group(1))
            elif m.group(2).startswith("espn_matches_"):
                espn_runs.add(m.group(1))
            continue
        m = re.match(r"kalshi/discovery/([^/]+)/", rel)
        if m:
            disc.add(m.group(1))
            continue
        if re.match(r"research/clv/[^/]+\.jsonl(\.gz)?$", rel):
            clv.append(rel)
    if profile == "truth":
        # the bounded independent-truth refresh (tennis-truth-refresh.yml): the canonical build's newest sources, the
        # settled predictions and their ledger rows, and the truth snapshots' metadata -- not the snapshots themselves
        out = [f"/{PREFIX}research/settlements/", f"/{PREFIX}research/ledger/",
               f"/{PREFIX}research/sports_truth/*.meta.json", f"/{PREFIX}research/sports_truth/*.summary.json",
               f"/{PREFIX}research/sports_truth/resolution_log/", f"/{PREFIX}sources/*/manifest.json",
               f"/{PREFIX}sources/espn/*/manifest.json", f"/{PREFIX}sources/espn/*/QUARANTINED.md"]
        for s_, runs in runs_with.items():
            if runs:
                out.append(f"/{PREFIX}sources/{max(runs)}/{s_}")
        good = sorted(espn_runs - espn_quarantined)
        if good:
            out.append(f"/{PREFIX}sources/espn/{good[-1]}/")
            out.append(f"!/{PREFIX}sources/espn/{good[-1]}/raw/")
        return out
    out = [f"/{PREFIX}research/", f"!/{PREFIX}research/horizons/", f"!/{PREFIX}research/timing/",
           f"!/{PREFIX}research/clv/", f"!/{PREFIX}research/external/raw/",
           f"/{PREFIX}firstball/", f"/{PREFIX}app/", f"/{PREFIX}processed/", f"/{PREFIX}identity/",
           f"/{PREFIX}kalshi/capture/", f"!/{PREFIX}kalshi/capture/*/*.trades.jsonl.gz", f"/{PREFIX}kalshi/capture_passes/",
           f"/{PREFIX}kalshi/run_snapshots/", f"/{PREFIX}sources/*/manifest.json", f"/{PREFIX}sources/espn/*/manifest.json"]
    if clv:
        out.append(f"/{PREFIX}{sorted(clv)[-1]}")
    for d in sorted(disc)[-2:]:
        out.append(f"/{PREFIX}kalshi/discovery/{d}/")
    for s, runs in runs_with.items():
        if runs:
            out.append(f"/{PREFIX}sources/{max(runs)}/{s}")
    good = sorted(espn_runs - espn_quarantined)
    if good:
        out.append(f"/{PREFIX}sources/espn/{good[-1]}/")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--branch", default="tennis-data")
    ap.add_argument("--repo", default=os.getcwd())
    ap.add_argument("--dest", default="data")
    ap.add_argument("--profile", default="run_tennis", choices=["run_tennis", "truth"],
                    help="which selection to pull when --paths is not given")
    ap.add_argument("--paths", nargs="*", default=None,
                    help="explicit paths UNDER data/ to unpack (e.g. processed/ratings_ATP.json firstball/store/) instead "
                         "of the RUN TENNIS selection; a trailing / means a directory")
    a = ap.parse_args()
    t0 = time.time()
    repo = os.path.abspath(a.repo)
    sh(["git", "config", "remote.origin.promisor", "true"], cwd=repo)
    sh(["git", "config", "remote.origin.partialclonefilter", "blob:none"], cwd=repo)
    sh(["git", "fetch", "--filter=blob:none", "--depth=1", "origin", f"+{a.branch}:refs/remotes/origin/{a.branch}"], cwd=repo)
    # the instant this runner's copy of the evidence branch was taken: TENNIS-5 measures the capture conductor's
    # freshness HERE, and reports the (growing) age of the pulled artifact while the run works separately
    pulled_at = datetime.now(timezone.utc).isoformat()
    head = sh(["git", "log", "-1", "--format=%H %cI", f"origin/{a.branch}"], cwd=repo, capture=True).stdout.split()
    if a.paths:
        pats = [f"/{PREFIX}{p.lstrip('/')}" for p in a.paths]
    else:
        names = sh(["git", "ls-tree", "-r", "--name-only", f"origin/{a.branch}"], cwd=repo, capture=True).stdout.split("\n")
        pats = patterns([n for n in names if n], a.profile)
    print("\n".join(pats))
    wt = os.path.join(os.path.dirname(repo), f"_{a.branch}_pull")
    shutil.rmtree(wt, ignore_errors=True)
    sh(["git", "worktree", "prune"], cwd=repo, check=False)
    sh(["git", "worktree", "add", "--no-checkout", "--detach", wt, f"origin/{a.branch}"], cwd=repo)
    try:
        sh(["git", "sparse-checkout", "init", "--no-cone"], cwd=wt)
        sh(["git", "sparse-checkout", "set", "--no-cone", *pats], cwd=wt)
        sh(["git", "checkout", "-q", "--detach", f"origin/{a.branch}"], cwd=wt)
        src = os.path.join(wt, PREFIX)
        dest = os.path.join(repo, a.dest)
        if not os.path.isdir(src):
            print("nothing matched on the branch for these paths"); return 0
        os.makedirs(dest, exist_ok=True)
        sh(["cp", "-a", src.rstrip("/") + "/.", dest + "/"])
        json.dump({"branch": a.branch, "pulled_at": pulled_at, "branch_sha": head[0] if head else None,
                   "branch_committed_at": head[1] if len(head) > 1 else None, "paths": a.paths or "run_tennis"},
                  open(os.path.join(dest, PULL_RECORD), "w"), indent=1)
        n = sum(len(f) for _r, _d, f in os.walk(dest))
        print(f"pulled into {a.dest}/ ({n} files) in {time.time() - t0:.0f}s")
    finally:
        sh(["git", "worktree", "remove", "--force", wt], cwd=repo, check=False)
        shutil.rmtree(wt, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
