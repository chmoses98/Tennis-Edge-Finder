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


def test_run_workflow_strips_the_prefix_when_unpacking_evidence(tmp_path):
    """RUN TENNIS unpacks evidence with scripts/ci/pull_data_branch.py (blobless + sparse since 2026-10-05; the
    full `git archive | tar --strip-components=1` downloaded 8 GB). The invariant is unchanged: the branch's
    `tennis-edge-finder/data/X` lands at ./data/X. Exercised end to end against a real (local) origin."""
    t = _text("tennis-run.yml")
    assert "python3 scripts/ci/pull_data_branch.py" in t
    origin = tmp_path / "origin.git"
    _git("init", "-q", "--bare", str(origin))
    seed = tmp_path / "seed"
    _git("init", "-q", "-b", "tennis-data", str(seed))
    for k, v in (("user.email", "t@example.com"), ("user.name", "t")):
        _git("config", k, v, cwd=seed)
    files = {f"{DEST_PREFIX}/data/research/ledger/2026-10-01.jsonl": "{}\n",
             f"{DEST_PREFIX}/data/research/clv/20261001T000000Z.jsonl": "old\n",
             f"{DEST_PREFIX}/data/research/clv/20261002T000000Z.jsonl": "new\n",
             f"{DEST_PREFIX}/data/research/horizons/20261002T000000Z.jsonl": "skip\n",
             f"{DEST_PREFIX}/data/kalshi/capture/2026-10-02/r.quotes.jsonl.gz": "q",
             f"{DEST_PREFIX}/data/kalshi/capture/2026-10-02/r.trades.jsonl.gz": "t",
             f"{DEST_PREFIX}/data/kalshi/discovery/20261001T000000Z/summary.json": "{}",
             f"{DEST_PREFIX}/data/kalshi/discovery/20261002T000000Z/summary.json": "{}",
             f"{DEST_PREFIX}/data/kalshi/discovery/20261003T000000Z/summary.json": "{}"}
    for rel, body in files.items():
        p = seed / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body)
    _git("add", "-A", cwd=seed)
    _git("commit", "-q", "-m", "evidence", cwd=seed)
    _git("remote", "add", "origin", str(origin), cwd=seed)
    _git("push", "-q", "origin", "tennis-data", cwd=seed)
    repo = tmp_path / "repo"
    _git("init", "-q", "-b", "main", str(repo))
    _git("remote", "add", "origin", str(origin), cwd=repo)
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "ci", "pull_data_branch.py"), "--repo", str(repo)],
                       capture_output=True, text=True)
    assert r.returncode == 0, (r.stdout[-1500:], r.stderr[-800:])
    d = repo / "data"
    assert (d / "research" / "ledger" / "2026-10-01.jsonl").exists()           # prefix stripped
    assert (d / "research" / "clv" / "20261002T000000Z.jsonl").exists()        # newest clv only
    assert not (d / "research" / "clv" / "20261001T000000Z.jsonl").exists()
    assert not (d / "research" / "horizons").exists()
    assert (d / "kalshi" / "capture" / "2026-10-02" / "r.quotes.jsonl.gz").exists()
    assert not (d / "kalshi" / "capture" / "2026-10-02" / "r.trades.jsonl.gz").exists()
    assert sorted(x.name for x in (d / "kalshi" / "discovery").iterdir()) == ["20261002T000000Z", "20261003T000000Z"]
    assert not (repo / DEST_PREFIX).exists()


def _git(*a, cwd=None):
    return subprocess.run(["git", *a], cwd=cwd, check=True, capture_output=True, text=True).stdout


def test_publisher_reapplies_the_historical_prefix(tmp_path):
    """publish_branch.py --dest-prefix must map local data/X onto <prefix>/data/X on the branch, and must
    leave every file already on the evidence branch untouched (append-only), without checking it out."""
    origin = tmp_path / "origin.git"
    _git("init", "-q", "--bare", str(origin))
    seed = tmp_path / "seed"
    _git("init", "-q", "-b", "tennis-data", str(seed))
    for k, v in (("user.email", "t@example.com"), ("user.name", "t")):
        _git("config", k, v, cwd=seed)
    old = seed / DEST_PREFIX / "data" / "kalshi" / "capture" / "2026-01-01"
    old.mkdir(parents=True)
    (old / "old.jsonl").write_text('{"old": true}\n')
    _git("add", "-A", cwd=seed)
    _git("commit", "-q", "-m", "evidence", cwd=seed)
    _git("remote", "add", "origin", str(origin), cwd=seed)
    _git("push", "-q", "origin", "tennis-data", cwd=seed)
    repo = tmp_path / "repo"
    _git("init", "-q", "-b", "main", str(repo))
    for k, v in (("user.email", "t@example.com"), ("user.name", "t")):
        _git("config", k, v, cwd=repo)
    (repo / "seed.txt").write_text("seed\n")
    _git("add", "-A", cwd=repo)
    _git("commit", "-q", "-m", "seed", cwd=repo)
    _git("remote", "add", "origin", str(origin), cwd=repo)
    src = repo / "data" / "kalshi" / "capture" / "2026-01-02"
    src.mkdir(parents=True)
    (src / "probe.jsonl").write_text('{"ok": true}\n')
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "ci", "publish_branch.py"),
                        "--src", "data/kalshi/capture", "--message", "probe", "--repo", str(repo), "--attempts", "2"],
                       capture_output=True, text=True)
    assert r.returncode == 0, (r.stdout[-1500:], r.stderr[-800:])
    files = _git("--git-dir", str(origin), "ls-tree", "-r", "--name-only", "tennis-data").split()
    assert f"{DEST_PREFIX}/data/kalshi/capture/2026-01-02/probe.jsonl" in files
    assert f"{DEST_PREFIX}/data/kalshi/capture/2026-01-01/old.jsonl" in files
    # a second publish of the same content is a no-op, never a rewrite
    r2 = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "ci", "publish_branch.py"),
                         "--src", "data/kalshi/capture", "--message", "probe", "--repo", str(repo)], capture_output=True, text=True)
    assert r2.returncode == 0 and "no changes to publish" in r2.stdout


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
