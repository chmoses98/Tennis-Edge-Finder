"""Final run-state verdicts (scripts/ci/run_state.py) and their wiring.

These close three false greens found in the Actions audit: a crashed run_tennis.py / settle_ledger.py hidden by
`| tail`, a capture conductor that stayed green when every pass failed, and an ESPN publish failure swallowed by
`|| true`. Deterministic: in-memory records and tmp files only; no network, clock or committed data.
"""
import importlib.util
import json
import os

import pytest
import yaml

REPO = os.path.join(os.path.dirname(__file__), "..")
WF = os.path.join(REPO, ".github", "workflows")


def _rs():
    spec = importlib.util.spec_from_file_location("run_state", os.path.join(REPO, "scripts", "ci", "run_state.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def P(i, cap=0, pub=0, scan=0, spub=0):
    return {"pass": i, "capture_rc": cap, "publish_rc": pub, "scan_rc": scan, "scan_publish_rc": spub}


def _wf(name):
    return yaml.safe_load(open(os.path.join(WF, name)))


# ------------------------------------------------------------------------------------------ capture conductor
def test_capture_all_passes_clean_is_healthy():
    assert _rs().classify_capture([P(0), P(1), P(2)])["health"] == "HEALTHY"


def test_capture_every_pass_failed_is_failed():
    r = _rs().classify_capture([P(0, cap=1), P(1, cap=0, pub=3), P(2, cap=137)])
    assert r["health"] == "FAILED" and r["successful"] == 0 and r["failed"] == 3


def test_capture_some_failures_with_one_success_is_degraded_not_failed():
    r = _rs().classify_capture([P(0, cap=1), P(1), P(2, pub=3)])
    assert r["health"] == "DEGRADED" and r["successful"] == 1 and r["failed"] == 2 and r["failed_passes"] == [0, 2]


def test_capture_partial_pass_counts_as_success_but_degrades():
    r = _rs().classify_capture([P(0, cap=2), P(1, cap=2)])
    assert r["health"] == "DEGRADED" and r["successful"] == 2 and r["partial"] == 2


def test_capture_external_scan_failure_only_degrades():
    assert _rs().classify_capture([P(0, scan=1), P(1, spub=3)])["health"] == "DEGRADED"


@pytest.mark.parametrize("content", [None, ""])
def test_capture_missing_or_empty_pass_log_fails_closed(tmp_path, content):
    rs = _rs()
    path = tmp_path / "passes.jsonl"
    if content is not None:
        path.write_text(content)
    assert rs.classify_capture(rs.read_pass_log(str(path)))["health"] == "FAILED"


def test_capture_malformed_line_is_a_failed_pass(tmp_path):
    rs = _rs()
    path = tmp_path / "passes.jsonl"
    path.write_text(json.dumps(P(0)) + "\nnot json\n")
    r = rs.classify_capture(rs.read_pass_log(str(path)))
    assert r["health"] == "DEGRADED" and r["failed"] == 1


def test_cli_failed_exits_1_with_error_and_summary(tmp_path, monkeypatch, capsys):
    rs = _rs()
    log = tmp_path / "p.jsonl"
    log.write_text("\n".join(json.dumps(P(i, cap=1)) for i in range(3)) + "\n")
    summary = tmp_path / "s.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    assert rs.main(["capture", "--pass-log", str(log)]) == 1
    assert "::error::" in capsys.readouterr().out
    assert "FAILED" in summary.read_text()


def test_cli_degraded_is_green_with_warning(tmp_path, monkeypatch, capsys):
    rs = _rs()
    log = tmp_path / "p.jsonl"
    log.write_text(json.dumps(P(0)) + "\n" + json.dumps(P(1, cap=1)) + "\n")
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)
    assert rs.main(["capture", "--pass-log", str(log)]) == 0
    out = capsys.readouterr().out
    assert "::warning::" in out and "::error::" not in out


# ------------------------------------------------------------------------------------------ ESPN
@pytest.mark.parametrize("outcome,rc,health", [
    ("success", "0", "HEALTHY"),      # fetched + published (or kalshi-only trigger: nothing to publish)
    ("failure", "0", "DEGRADED"),     # external feed down: previous snapshot used, retried tomorrow
    ("success", "3", "FAILED"),       # fetched but lost: publish_branch exhausted its retries
    ("failure", "3", "FAILED"),
    ("success", "", "FAILED"),        # no recorded exit code: fail closed
])
def test_espn_verdict(outcome, rc, health):
    assert _rs().classify_espn(outcome, rc)["health"] == health


# ------------------------------------------------------------------------------------------ RUN TENNIS core
def test_core_verdict():
    rs = _rs()
    assert rs.classify_core([])["health"] == "HEALTHY"
    assert rs.classify_core(["", ""])["health"] == "HEALTHY"
    r = rs.classify_core(["run_tennis", "settle_ledger"])
    assert r["health"] == "FAILED" and r["failed_stages"] == ["run_tennis", "settle_ledger"]
    assert rs.main(["core", "--failed", " run_tennis"]) == 1
    assert rs.main(["core", "--failed", ""]) == 0


# ------------------------------------------------------------------------------------------ wiring
def test_run_tennis_pipes_cannot_hide_core_failures_and_enforce_once():
    steps = _wf("tennis-run.yml")["jobs"]["run"]["steps"]
    build = next(s for s in steps if s.get("name") == "Build canonical table and rating states")["run"]
    assert "set -o pipefail" in build
    proj = next(s for s in steps if s.get("id") == "project")
    run = proj["run"]
    assert "set -o pipefail" in run
    assert run.index("set -o pipefail") < run.index("scripts/run_tennis.py | tail")
    assert 'CORE_FAILED="$CORE_FAILED run_tennis"' in run and 'CORE_FAILED="$CORE_FAILED settle_ledger"' in run
    assert "core_failed=$CORE_FAILED" in run
    assert "exit 1" not in run                                   # the project step itself never ends the job
    pub = [i for i, s in enumerate(steps) if s.get("name") == "Publish research outputs"][0]
    last = steps[-1]
    assert steps.index(last) > pub                               # verdict comes after publication
    assert "run_state.py core" in last["run"] and last["if"] == "always() && steps.project.outcome == 'success'"
    assert sum("run_state.py" in s.get("run", "") for s in steps) == 1


def test_capture_conductor_records_every_pass_and_enforces_once_after_hand_off():
    steps = _wf("tennis-capture.yml")["jobs"]["conduct"]["steps"]
    loop = next(s for s in steps if s.get("id") == "loop")["run"]
    for v in ("CAP_RC", "PUB_RC", "SCAN_RC", "SCAN_PUB_RC"):
        assert f"|| {v}=$?" in loop
    assert '>> "$PASS_LOG"' in loop and "exit 1" not in loop
    names = [s.get("name", "") for s in steps]
    hand = next(i for i, n in enumerate(names) if n.startswith("Hand off"))
    assert steps[-1] is steps[hand + 1]
    assert "run_state.py capture" in steps[-1]["run"]
    assert steps[-1]["if"] == "always() && steps.loop.outcome == 'success'"


def test_bootstrap_espn_publish_is_recorded_not_swallowed():
    steps = _wf("tennis-bootstrap.yml")["jobs"]["sources"]["steps"]
    pub = next(s for s in steps if s.get("id") == "publish_espn")
    assert "|| true" not in pub["run"] and "|| RC=$?" in pub["run"] and 'rc=$RC' in pub["run"]
    verdict = steps[-1]
    assert "run_state.py espn" in verdict["run"]
    assert "steps.acquire_espn.outcome" in verdict["run"] and "steps.publish_espn.outputs.rc" in verdict["run"]
    assert verdict["if"] == "always() && steps.publish_espn.outcome == 'success'"
