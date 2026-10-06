#!/usr/bin/env python3
"""Publish files onto the orphan evidence branch (`tennis-data`) -- append-only, without checking it out.

Why it was rewritten (2026-10-05)
---------------------------------
The previous version fetched the branch tip and checked out the WHOLE tree into a worktree on every
publish. The evidence tree passed 8 GB (100k+ files), so a RUN TENNIS publish took ~13.5 minutes and each
ten-minute capture pass spent most of its interval publishing -- the capture cadence slipped to 20-80
minutes (TENNIS-5) and every assisted slate was STALE before it was built.

Now: a BLOBLESS shallow fetch (trees only, no file contents), a worktree whose SPARSE checkout contains only
the directories this publish writes, commit, push. On a push race the worktree is re-synced to the new tip
and the files are copied again -- publishers write new per-run paths (plus a few rolling files such as
state.json / latest.json, where the newest writer wins, exactly as before), so this is equivalent to the old
rebase and never produces conflict markers. Nothing on the branch is ever deleted.

Usage: publish_branch.py --src data/research --message "..." [--branch tennis-data] [--no-overwrite]
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time

MAX_FILE = 95 * 1024 * 1024


def sh(cmd, cwd=None, check=True, capture=False):
    print("+", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, cwd=cwd, check=False, text=True, capture_output=capture)
    if check and r.returncode != 0:
        if capture:
            print(r.stdout, r.stderr)
        raise SystemExit(f"command failed ({r.returncode}): {' '.join(cmd)}")
    return r


def plan(src: str, exclude=()):
    """[(relative path, absolute source path)] of every file to publish (skips .part and oversized files, and any
    path under an `exclude` prefix relative to src)."""
    out = []
    ex = tuple(e.strip("/") + "/" for e in exclude)
    for root, _dirs, files in os.walk(src):
        rel = os.path.relpath(root, src)
        for fn in files:
            if fn.endswith(".part"):
                continue
            if ex and (os.path.normpath(os.path.join(rel, fn)) + "/").startswith(ex):
                continue
            p = os.path.join(root, fn)
            if os.path.getsize(p) > MAX_FILE:
                # GitHub rejects files > 100 MB and the whole push with them; never let one file block the rest
                print(f"::warning::skipping oversized file {p} ({os.path.getsize(p) / 1e6:.1f} MB)")
                continue
            out.append((os.path.normpath(os.path.join(rel, fn)), p))
    return sorted(out)


#: up to this many files a publish checks out exactly the files it writes; above it, their directories
EXACT_SPARSE_MAX = 300


def _glob_escape(path: str) -> str:
    return "".join("\\" + c if c in "\\*?[]!# " else c for c in path)


def sparse_patterns(dest_rel: str, files) -> list[str]:
    """What the worktree checks out (non-cone patterns). A publish of a few files checks out exactly those paths: the
    copy step only reads the files it is about to write. Directory patterns made the capture conductor's first pass
    download every blob under research/external/market (~1 GB of day files), raw/ (4,397 payloads) and scans/ (2,237)
    just to add five files -- 286 s of a 600 s interval on 2026-10-06, and growing with the tree. Large publishes
    (RUN TENNIS) keep directory patterns, which stay cheap to match."""
    paths = sorted({os.path.join(dest_rel, r) for r, _ in files})
    if len(paths) <= EXACT_SPARSE_MAX:
        return ["/" + _glob_escape(p) for p in paths]
    dirs = sorted({os.path.dirname(p) for p in paths})
    return [f"/{d}/*" if d else "/*" for d in dirs]


def fetch_tip(repo, branch):
    sh(["git", "config", "remote.origin.promisor", "true"], cwd=repo)
    sh(["git", "config", "remote.origin.partialclonefilter", "blob:none"], cwd=repo)
    r = sh(["git", "fetch", "--filter=blob:none", "--depth=1", "origin", f"+{branch}:refs/remotes/origin/{branch}"],
           cwd=repo, check=False, capture=True)
    return r.returncode == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="local directory (relative to repo) whose contents to publish")
    ap.add_argument("--dest-prefix", default="tennis-edge-finder",
                    help="path prefix the contents take ON THE DATA BRANCH. Defaults to 'tennis-edge-finder' because the "
                         "evidence tree was created while this project lived in a subdirectory of chmoses98/nfl-edge-finder; "
                         "keeping the prefix is what let the 2026-09-11 migration transfer every pre-migration commit with its "
                         "ORIGINAL SHA instead of rewriting frozen observations. Never change it to make the layout prettier: "
                         "that would fork the append-only tree in two (see MIGRATION_AUDIT.md).")
    ap.add_argument("--message", required=True)
    ap.add_argument("--branch", default="tennis-data")
    ap.add_argument("--repo", default=os.getcwd())
    ap.add_argument("--attempts", type=int, default=8)
    ap.add_argument("--no-overwrite", action="store_true",
                    help="write-once trees (assisted decision records): a file that already exists on the branch is "
                         "never replaced; if its content differs the publish fails loudly (exit 4) instead")
    ap.add_argument("--exclude", nargs="*", default=[],
                    help="directories (relative to --src) NOT to publish: trees another single writer owns. RUN TENNIS "
                         "pulls research/external (it reads it) but must not write back its older copy over the "
                         "capture conductor's newer one (2026-10-07)")
    a = ap.parse_args()
    t0 = time.time()
    repo = os.path.abspath(a.repo)
    src = os.path.join(repo, a.src)
    dest_rel = os.path.join(a.dest_prefix, a.src) if a.dest_prefix else a.src
    if not os.path.isdir(src) or not any(os.scandir(src)):
        print("nothing to publish (source empty)"); return 0
    files = plan(src, a.exclude)
    if not files:
        print("nothing to publish (no eligible files)"); return 0
    wt = os.path.join(os.path.dirname(repo), f"_{a.branch}_pub_{os.getpid()}")
    exists = subprocess.run(["git", "ls-remote", "--exit-code", "--heads", "origin", a.branch], cwd=repo,
                            capture_output=True).returncode == 0
    if not exists:
        raise SystemExit(f"branch {a.branch} does not exist on origin; refusing to create an evidence branch implicitly")
    try:
        for attempt in range(1, a.attempts + 1):
            if not fetch_tip(repo, a.branch):
                time.sleep(2 * attempt); continue
            if os.path.exists(wt):
                sh(["git", "worktree", "remove", "--force", wt], cwd=repo, check=False)
                shutil.rmtree(wt, ignore_errors=True)
                sh(["git", "worktree", "prune"], cwd=repo, check=False)
            sh(["git", "worktree", "add", "--no-checkout", "--detach", wt, f"origin/{a.branch}"], cwd=repo)
            sh(["git", "sparse-checkout", "init", "--no-cone"], cwd=wt)
            sh(["git", "sparse-checkout", "set", "--no-cone", *sparse_patterns(dest_rel, files)], cwd=wt)
            sh(["git", "checkout", "-q", "-B", a.branch, f"origin/{a.branch}"], cwd=wt)
            changed = []
            for rel, p in files:
                dst = os.path.join(wt, dest_rel, rel)
                if os.path.exists(dst):
                    if open(p, "rb").read() == open(dst, "rb").read():
                        continue
                    if a.no_overwrite:
                        print(f"::error::write-once file already on {a.branch} with different content: {rel}")
                        return 4
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(p, dst)
                changed.append(os.path.join(dest_rel, rel))
            if not changed:
                print("no changes to publish"); return 0
            for i in range(0, len(changed), 500):
                sh(["git", "add", "--sparse", "--", *changed[i:i + 500]], cwd=wt)
            if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=wt).returncode == 0:
                print("no changes to publish"); return 0
            sh(["git", "-c", "core.hooksPath=/dev/null", "commit", "-q", "-m", a.message], cwd=wt)
            r = subprocess.run(["git", "push", "origin", f"HEAD:refs/heads/{a.branch}"], cwd=wt, text=True, capture_output=True)
            if r.returncode == 0:
                print(f"published {len(changed)} file(s) to {a.branch} in {time.time() - t0:.1f}s (attempt {attempt})")
                return 0
            print("push failed (re-syncing to the new tip and re-copying):", r.stderr[-400:])
            time.sleep(2 * attempt)
        print("FAILED to publish after retries"); return 3
    finally:
        sh(["git", "worktree", "remove", "--force", wt], cwd=repo, check=False)
        shutil.rmtree(wt, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
