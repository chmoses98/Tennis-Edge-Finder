"""Conductor run-state semantics (tennis-capture.yml, tennis-firstball.yml).

Two structural defects made the self-chaining conductors produce a CANCELLED run for nearly every cron tick and
for ~44% of capture conductors, while the conductors were doing their job:

1. the loop budget ignored `timeout-minutes` (END measured from the loop step, checked only before a pass, and the
   post-pass sleep could cross it) so the last pass ran into the job timeout and GitHub cancelled the run;
2. the end-of-run dispatch raced the queued cron backstop in the shared concurrency group, and the newer pending
   run cancelled the older one.

Everything here is deterministic: the bash clock helpers are driven with fixed epoch numbers, and the GitHub API
is replaced by injected callables. Nothing reads the calendar, the network or committed data.
"""
import importlib.util
import json
import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.join(os.path.dirname(__file__), "..")
CLOCK = os.path.join(REPO, "scripts", "ci", "conductor_clock.sh")
WF_DIR = os.path.join(REPO, ".github", "workflows")
CONDUCTORS = {"tennis-capture.yml": "conduct", "tennis-firstball.yml": "poll"}


def _chain():
    spec = importlib.util.spec_from_file_location("conductor_chain", os.path.join(REPO, "scripts", "ci", "conductor_chain.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def bash(script: str) -> str:
    r = subprocess.run(["bash", "-e", "-c", f"source {CLOCK}\n{script}"], capture_output=True, text=True, check=True)
    return r.stdout.strip()


# --------------------------------------------------------------------------------------------- loop budget
def test_end_is_the_earlier_of_the_loop_budget_and_the_job_timeout_margin():
    # loop starts 5 min into the job: 340 min from the loop would be 345 min of job time == 355 - 10
    assert bash("conductor_end 300 340 0 355 10") == str(345 * 60)
    # a slow setup (20 min) must not push END past the job timeout margin
    assert bash("conductor_end 1200 340 0 355 10") == str(345 * 60)
    # a short manual run keeps its own budget
    assert bash("conductor_end 300 30 0 355 10") == str(300 + 30 * 60)


def test_a_pass_starts_only_if_the_longest_pass_so_far_still_fits():
    assert bash("conductor_should_start 0 1000 0 && echo yes || echo no") == "yes"      # first pass always runs
    assert bash("conductor_should_start 400 1000 500 && echo yes || echo no") == "yes"
    assert bash("conductor_should_start 500 1000 500 && echo yes || echo no") == "no"
    assert bash("conductor_should_start 1000 1000 0 && echo yes || echo no") == "no"     # budget spent


def test_sleep_never_crosses_end_and_is_never_negative():
    assert bash("conductor_sleep 0 10000 600 100") == "500"
    assert bash("conductor_sleep 9800 10000 600 100") == "200"   # capped at END
    assert bash("conductor_sleep 0 10000 600 900") == "0"        # overlong pass: no sleep
    assert bash("conductor_sleep 10500 10000 600 100") == "0"    # already past END


# Pass durations shaped like the capture history (run 36950014995: 5 min restore, 16 passes in ~5.5 h, i.e. ~20 min
# per pass against a 600 s interval, and the 17th pass killed by the 355-minute timeout). Pass 0 carries the daily
# discovery.
DURATIONS = [1500, 1230, 1200, 1260, 1230, 1240, 1220, 1250]
JOB_TIMEOUT = 355 * 60
SETUP = 300


def _old_loop_end() -> int:
    """The loop as it was: END from the loop start, checked before a pass, sleep regardless of END."""
    now, end, i = SETUP, SETUP + 340 * 60, 0
    while now < end:
        d = DURATIONS[i % len(DURATIONS)]
        now += d
        i += 1
        now += max(0, 600 - d)
    return now


def _new_loop_end() -> tuple[int, int]:
    durs = " ".join(map(str, DURATIONS))
    out = bash(f"""
        DURS=({durs}); JOB_T0=0; NOW={SETUP}
        END=$(conductor_end "$NOW" 340 "$JOB_T0" 355 10)
        PASS=0; LONGEST=0
        while conductor_should_start "$NOW" "$END" "$LONGEST"; do
          T0=$NOW; NOW=$(( NOW + ${{DURS[$(( PASS % ${{#DURS[@]}} ))]}} )); PASS=$((PASS+1))
          ELAPSED=$(( NOW - T0 )); [ "$ELAPSED" -gt "$LONGEST" ] && LONGEST=$ELAPSED
          SLEEP=$(conductor_sleep "$NOW" "$END" 600 "$ELAPSED"); NOW=$(( NOW + SLEEP ))
        done
        echo "$NOW $PASS"
    """)
    now, passes = out.split()
    return int(now), int(passes)


def test_regression_the_old_loop_ran_into_the_job_timeout():
    """The scenario is meaningful: the pre-fix loop overruns timeout-minutes (GitHub cancels the run)."""
    assert _old_loop_end() > JOB_TIMEOUT


def test_the_budgeted_loop_finishes_inside_the_job_timeout_with_room_for_the_hand_off():
    end, passes = _new_loop_end()
    assert end <= JOB_TIMEOUT - 5 * 60, end          # >= 5 min left for the hand-off and post steps
    assert passes >= 15                               # and it still does a full conductor's worth of passes


# --------------------------------------------------------------------------------------------- hand-off
def _runs(*pairs):
    return [{"id": i, "status": s, "event": e} for i, s, e in pairs]


def test_a_queued_cron_tick_is_the_successor_and_nothing_is_dispatched():
    C = _chain()
    posts = []
    rep = C.handoff(lambda: _runs((10, "in_progress", "workflow_dispatch"), (11, "pending", "schedule"),
                                  (9, "completed", "workflow_dispatch")),
                    lambda: posts.append(1) or 204, own_run_id=10, sleep=lambda s: None)
    assert posts == []                                   # no second pending run -> nothing gets cancelled
    assert rep["disposition"] == "SUCCESSOR_ALREADY_QUEUED" and rep["health"] == "HEALTHY"
    assert rep["successor_run_ids"] == ["11"]


@pytest.mark.parametrize("status", ["queued", "pending", "waiting", "requested"])
def test_any_not_completed_other_run_counts_as_queued(status):
    C = _chain()
    assert [r["id"] for r in C.queued_successors(_runs((1, "in_progress", "x"), (2, status, "schedule")), 1)] == [2]


def test_no_queued_run_dispatches_exactly_once():
    C = _chain()
    posts = []
    rep = C.handoff(lambda: _runs((10, "in_progress", "schedule"), (9, "completed", "workflow_dispatch")),
                    lambda: posts.append(1) or 204, own_run_id="10", sleep=lambda s: None)
    assert posts == [1]
    assert rep["disposition"] == "DISPATCHED" and rep["health"] == "HEALTHY"


def test_transient_dispatch_failure_is_retried_and_recorded():
    C = _chain()
    codes = iter([502, 204])
    slept = []
    rep = C.handoff(lambda: [], lambda: next(codes), own_run_id=1, sleep=slept.append)
    assert rep["disposition"] == "RECOVERED_AFTER_RETRY" and rep["health"] == "HEALTHY"
    assert [a["http"] for a in rep["attempts"]] == [502, 204]
    assert slept == [C.DEFAULT_BACKOFF[1]]


def test_persistent_dispatch_failure_is_bounded_and_degraded_not_failed():
    C = _chain()
    calls = []

    def post():
        calls.append(1)
        raise OSError("connection reset")
    rep = C.handoff(lambda: [], post, own_run_id=1, sleep=lambda s: None)
    assert len(calls) == len(C.DEFAULT_BACKOFF)           # bounded: no retry loop beyond the schedule
    assert rep["disposition"] == "DISPATCH_FAILED" and rep["health"] == "DEGRADED"
    assert "cron" in rep["recovery"]


def test_listing_failure_falls_back_to_dispatching():
    C = _chain()
    posts = []

    def boom():
        raise OSError("api down")
    rep = C.handoff(boom, lambda: posts.append(1) or 204, own_run_id=1, sleep=lambda s: None)
    assert posts == [1] and rep["disposition"] == "DISPATCHED"
    assert "api down" in rep["listing_error"]


def test_main_degraded_is_green_with_warning_and_step_summary(tmp_path, monkeypatch, capsys):
    C = _chain()
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GH_TOKEN", "t")
    monkeypatch.setenv("GITHUB_REPOSITORY", "o/r")
    monkeypatch.setenv("GITHUB_RUN_ID", "5")
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    seen = {}

    def fake_github(token):
        def get(url):
            seen["get"] = url
            return {"workflow_runs": [{"id": 5, "status": "in_progress"}]}

        def post(url, body):
            seen["post"], seen["body"] = url, body
            return 500
        return get, post
    monkeypatch.setattr(C, "_github", fake_github)
    monkeypatch.setattr(C, "DEFAULT_BACKOFF", (0, 0, 0))
    rc = C.main(["--workflow", "tennis-capture.yml", "--ref", "main", "--inputs", '{"chain":"true"}'])
    out = capsys.readouterr().out
    assert rc == 0
    assert "::warning::" in out
    assert json.loads(out.splitlines()[0])["health"] == "DEGRADED"
    assert "DISPATCH_FAILED" in summary.read_text()
    assert seen["post"].endswith("/repos/o/r/actions/workflows/tennis-capture.yml/dispatches")
    assert seen["body"] == {"ref": "main", "inputs": {"chain": "true"}}


def test_main_without_credentials_fails_loudly(monkeypatch):
    C = _chain()
    monkeypatch.delenv("GH_TOKEN", raising=False)
    monkeypatch.delenv("GITHUB_REPOSITORY", raising=False)
    assert C.main(["--workflow", "tennis-capture.yml", "--ref", "main"]) == 1


# --------------------------------------------------------------------------------------------- workflows
@pytest.mark.parametrize("wf,job", sorted(CONDUCTORS.items()))
def test_conductor_workflows_use_the_budget_and_the_hand_off(wf, job):
    text = open(os.path.join(WF_DIR, wf)).read()
    doc = yaml.safe_load(text)
    j = doc["jobs"][job]
    steps = j["steps"]
    # concurrency semantics unchanged: one running, one pending, never cancel a running conductor
    assert doc["concurrency"]["cancel-in-progress"] is False
    # job start is recorded first, and the loop budgets against the job's real timeout
    assert "JOB_T0=" in steps[0]["run"]
    loop = next(s["run"] for s in steps if "conductor_should_start" in s.get("run", ""))
    assert "source scripts/ci/conductor_clock.sh" in loop
    m = re.search(r'conductor_end "\$\(date \+%s\)" "\$MINUTES" "\$JOB_T0" (\d+) (\d+)', loop)
    assert m and int(m.group(1)) == j["timeout-minutes"], "budget must use the job's timeout-minutes"
    assert int(m.group(2)) >= 5
    # the hand-off replaces the bare curl, keeps the successor inputs, and runs for schedule-started conductors
    hand = next(s for s in steps if s.get("name", "").startswith("Hand off to the successor"))
    assert f"conductor_chain.py --workflow {wf}" in hand["run"]
    assert "curl" not in hand["run"]
    assert "github.event_name == 'schedule'" in hand["if"] and hand["if"].startswith("always()")
    inputs = json.loads(re.search(r"--inputs '(\{.*\})'", hand["run"]).group(1))
    assert inputs["chain"] == "true" and inputs["minutes"] == "340"
