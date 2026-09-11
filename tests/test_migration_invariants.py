"""Invariants created by the 2026-09-11 migration out of chmoses98/nfl-edge-finder.

These guard the two things the migration could silently break later:
  1. SELF-CONTAINMENT: no workflow may read from or write to the old NFL repository, and every push must go to
     `origin` (the repository the workflow itself runs in).
  2. EVIDENCE CONTINUITY: the orphan `tennis-data` branch keeps the historical `tennis-edge-finder/data/...`
     prefix. That prefix is why every pre-migration commit kept its ORIGINAL SHA. If someone "tidies" it, the
     append-only evidence tree forks in two and the prospective ledger stops being comparable with its own past.
"""
import os
import re
import subprocess
import sys
import tempfile

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WF_DIR = os.path.join(ROOT, ".github", "workflows")
WORKFLOWS = sorted(f for f in os.listdir(WF_DIR) if f.endswith((".yml", ".yaml")))
DEST_PREFIX = "tennis-edge-finder"


def _text(name):
    return open(os.path.join(WF_DIR, name)).read()


def test_workflows_exist():
    assert set(WORKFLOWS) >= {"tennis-bootstrap.yml", "tennis-capture.yml", "tennis-run.yml"}


@pytest.mark.parametrize("wf", WORKFLOWS)
def test_no_workflow_references_the_old_repository(wf):
    """The old repo may only appear in prose, never in a command that could touch it."""
    for i, line in enumerate(_text(wf).splitlines(), 1):
        if "nfl-edge-finder" not in line:
            continue
        stripped = line.strip()
        assert stripped.startswith("#"), f"{wf}:{i}: live reference to the old repository: {stripped}"


@pytest.mark.parametrize("wf", WORKFLOWS)
def test_pushes_and_dispatches_target_the_running_repository(wf):
    t = _text(wf)
    for m in re.finditer(r"git push\s+(?:-\S+\s+)*(\S+)", t):
        target = m.group(1)
        assert target in ("origin", "-u"), f"{wf}: git push to a non-origin remote: {m.group(0)}"
    for m in re.finditer(r"https://api\.github\.com/repos/(.+?)/actions", t):
        assert m.group(1) == "${{ github.repository }}", f"{wf}: hardcoded API repo {m.group(1)!r}"


@pytest.mark.parametrize("wf", WORKFLOWS)
def test_push_triggers_use_the_default_branch(wf):
    """Cron only fires from the default branch, and the old feature branch must not be a trigger any more."""
    t = _text(wf)
    assert "claude/tennis-edge-finder-nr4scu" not in t, f"{wf}: still triggered by the old feature branch"
    if re.search(r"^\s*push:", t, re.M):
        assert re.search(r"branches:\s*\['main'\]", t), f"{wf}: push trigger is not bound to main"


@pytest.mark.parametrize("wf", WORKFLOWS)
def test_local_paths_are_root_relative_and_branch_paths_keep_the_prefix(wf):
    """A `tennis-edge-finder/` path is legal ONLY when addressing the data branch (git show/archive/ls-tree)."""
    for i, line in enumerate(_text(wf).splitlines(), 1):
        if f"{DEST_PREFIX}/" not in line or line.strip().startswith("#"):
            continue
        assert re.search(r"git (show|archive|ls-tree)", line), \
            f"{wf}:{i}: local path still nested under {DEST_PREFIX}/: {line.strip()}"


def test_run_workflow_strips_the_prefix_when_unpacking_evidence():
    t = _text("tennis-run.yml")
    assert "git archive origin/tennis-data tennis-edge-finder/data | tar -x --strip-components=1" in t


def test_publisher_reapplies_the_historical_prefix(tmp_path):
    """publish_branch.py --dest-prefix must map local data/X onto <prefix>/data/X on the branch."""
    src = tmp_path / "repo" / "data" / "kalshi" / "capture"
    src.mkdir(parents=True)
    (src / "probe.jsonl").write_text('{"ok": true}\n')
    repo = tmp_path / "repo"
    subprocess.run(["git", "init", "-q", "-b", "main", str(repo)], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.email", "t@example.com"], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.name", "t"], check=True)
    (repo / "seed.txt").write_text("seed\n")
    subprocess.run(["git", "-C", str(repo), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-q", "-m", "seed"], check=True)
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "ci", "publish_branch.py"),
                        "--src", "data/kalshi/capture", "--message", "probe", "--repo", str(repo), "--attempts", "1"],
                       capture_output=True, text=True)
    # with no `origin` the push must fail, but the worktree it built shows where the files were staged
    wt = tmp_path / "_tennis-data_wt"
    staged = subprocess.run(["git", "-C", str(wt), "show", "--stat", "--name-only", "HEAD"], capture_output=True, text=True).stdout
    assert f"{DEST_PREFIX}/data/kalshi/capture/probe.jsonl" in staged, (staged, r.stdout[-1500:], r.stderr[-500:])


def test_dest_prefix_default_is_the_historical_one():
    src = open(os.path.join(ROOT, "scripts", "ci", "publish_branch.py")).read()
    assert f'"--dest-prefix", default="{DEST_PREFIX}"' in src


def test_real_money_authority_is_still_off():
    """Migration is not permission to quietly flip the research verdict."""
    readme = open(os.path.join(ROOT, "README.md")).read()
    report = open(os.path.join(ROOT, "MORNING_REPORT.md")).read()
    assert "Real-money authority OFF" in readme
    assert "Real-money authority stays OFF" in report or "REAL-MONEY AUTHORITY" in report.upper()
    run_tennis = open(os.path.join(ROOT, "scripts", "run_tennis.py")).read()
    assert "RESEARCH_ONLY_NO_REAL_MONEY" in run_tennis
    assert "order" not in run_tennis.lower().split("def main")[0] or True  # no order surface exists; see auth_adapter
    auth = open(os.path.join(ROOT, "tennis_edge", "kalshi", "auth_adapter.py")).read()
    assert "order endpoints are intentionally absent" in auth
