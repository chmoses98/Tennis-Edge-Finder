#!/usr/bin/env python3
"""Is there independent-result evidence on disk that no sports-truth snapshot has used yet? (exit 0 = refresh, 10 = up to date)

The bounded truth refresh (tennis-truth-refresh.yml) runs after every source bootstrap and on a fallback schedule. GitHub
starts scheduled workflows late or not at all (2026-10-06: the 05:40Z bootstrap ran at ~12:15Z; RUN TENNIS's 12:25Z tick
never ran), so the refresh does not trust the clock: it compares the newest valid ESPN snapshot on disk with the ESPN
snapshots recorded in the truth snapshots' metadata, and rebuilds only when there is something new. Snapshots written
before 2026-10-07 carry no metadata, so the first refresh always runs.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def newest_espn(sources_root: str) -> str | None:
    runs = sorted(d for d in glob.glob(os.path.join(sources_root, "espn", "*")) if os.path.isdir(d)
                  and glob.glob(os.path.join(d, "espn_matches_*.csv.gz")) and not os.path.exists(os.path.join(d, "QUARANTINED.md")))
    return os.path.basename(runs[-1]) if runs else None


def used_espn(truth_dir: str) -> set:
    used = set()
    for p in glob.glob(os.path.join(truth_dir, "*.meta.json")):
        try:
            used.update((json.load(open(p)).get("provenance") or {}).get("espn_runs") or [])
        except ValueError:
            continue
    return used


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-root", default=os.path.join(PROJ, "data"))
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    new = newest_espn(os.path.join(a.data_root, "sources"))
    used = used_espn(os.path.join(a.data_root, "research", "sports_truth"))
    print(json.dumps({"newest_espn_on_branch": new, "espn_runs_already_used": sorted(used)[-3:], "force": a.force}))
    if a.force or (new and new not in used):
        print(f"refresh: ESPN {new} has not been used by any sports-truth snapshot")
        return 0
    print("up to date: the newest ESPN snapshot is already in a sports-truth snapshot")
    return 10


if __name__ == "__main__":
    sys.exit(main())
